import { once } from "node:events";
import { existsSync } from "node:fs";
import { mkdtemp, mkdir, stat, writeFile } from "node:fs/promises";
import { Agent, request as httpRequest } from "node:http";
import { createConnection } from "node:net";
import { join } from "node:path";
import { pathToFileURL } from "node:url";

const runtimeRoot = process.argv[2];
if (!runtimeRoot) throw new Error("usage: node runtime-stop-reproducer.mjs <built-runtime-root>");

const daemonModule = join(runtimeRoot, "packages/daemon/dist/runtime-daemon.js");
if (!existsSync(daemonModule)) throw new Error(`built daemon module absent: ${daemonModule}`);
const { RuntimeDaemon } = await import(pathToFileURL(daemonModule));

const STOP_BOUNDARY_MS = 750;
const RELEASE_BOUNDARY_MS = 2000;
const now = () => new Date().toISOString();
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function pathState(path) {
  try {
    const metadata = await stat(path);
    return { exists: true, isSocket: metadata.isSocket(), mode: metadata.mode & 0o777 };
  } catch (error) {
    if (error?.code === "ENOENT") return { exists: false };
    throw error;
  }
}

async function raceBoundary(promise, boundaryMs) {
  return Promise.race([
    promise.then(
      () => ({ state: "RESOLVED" }),
      (error) => ({ state: "REJECTED", error: String(error?.stack ?? error) })
    ),
    sleep(boundaryMs).then(() => ({ state: "PENDING_AT_BOUNDARY" }))
  ]);
}

async function makeService(root) {
  const tokenFile = join(root, "operator.token");
  await writeFile(tokenFile, "tm112-token\n", { mode: 0o600 });
  let releaseStream;
  const streamRelease = new Promise((resolve) => {
    releaseStream = resolve;
  });
  let interruptCalls = 0;
  const service = {
    auth: {
      async ensureClient() {
        return { tokenFile };
      },
      async authenticate() {
        return { clientId: "tm112-client", projectId: "tm112-project" };
      }
    },
    async *runAgent1() {
      yield {
        type: "harness:event",
        data: { sessionId: "tm112-manager", event: { type: "session:init", data: {} } }
      };
      await streamRelease;
    },
    async interruptSession() {
      interruptCalls += 1;
      releaseStream();
    }
  };
  return { service, releaseStream, interruptCalls: () => interruptCalls };
}

async function startCase(name) {
  // macOS limits Unix-domain socket path length. Keep the disposable prefix
  // short so the test probes server behavior rather than pathname rejection.
  const root = await mkdtemp(join("/tmp", "t112-"));
  const runtimeDirectory = join(root, "runtime");
  await mkdir(runtimeDirectory, { recursive: true });
  const socketPath = join(runtimeDirectory, "control.sock");
  const serviceState = await makeService(root);
  const daemon = new RuntimeDaemon({
    runtimeDirectory,
    socketPath,
    service: serviceState.service
  });
  const startedAt = now();
  await daemon.start();
  return {
    name,
    root,
    socketPath,
    ownerPath: `${socketPath}.owner.json`,
    daemon,
    serviceState,
    startedAt,
    beforeStop: {
      socket: await pathState(socketPath),
      owner: await pathState(`${socketPath}.owner.json`)
    }
  };
}

async function stopAndObserve(context, release) {
  const stopInvokedAt = now();
  const started = process.hrtime.bigint();
  const stopPromise = context.daemon.stop();
  const initial = await raceBoundary(stopPromise, STOP_BOUNDARY_MS);
  const initialElapsedMs = Number(process.hrtime.bigint() - started) / 1e6;
  const atBoundary = {
    timestamp: now(),
    elapsedMs: initialElapsedMs,
    stop: initial,
    socket: await pathState(context.socketPath),
    owner: await pathState(context.ownerPath)
  };
  let afterRelease = null;
  if (initial.state === "PENDING_AT_BOUNDARY") {
    const releasedAt = now();
    await release();
    const released = await raceBoundary(stopPromise, RELEASE_BOUNDARY_MS);
    afterRelease = {
      releasedAt,
      observedAt: now(),
      elapsedMs: Number(process.hrtime.bigint() - started) / 1e6,
      stop: released,
      socket: await pathState(context.socketPath),
      owner: await pathState(context.ownerPath)
    };
  }
  return {
    name: context.name,
    startedAt: context.startedAt,
    stopInvokedAt,
    stopBoundaryMs: STOP_BOUNDARY_MS,
    releaseBoundaryMs: RELEASE_BOUNDARY_MS,
    pid: process.pid,
    beforeStop: context.beforeStop,
    atBoundary,
    afterRelease
  };
}

async function idleCase() {
  const context = await startCase("idle");
  return stopAndObserve(context, async () => {});
}

async function ordinaryKeepAliveCase() {
  const context = await startCase("ordinary-keepalive");
  const agent = new Agent({ keepAlive: true, maxSockets: 1 });
  let clientSocket;
  const response = await new Promise((resolve, reject) => {
    const outgoing = httpRequest(
      {
        socketPath: context.socketPath,
        path: "/v1/health",
        headers: { authorization: "Bearer tm112-token" },
        agent
      },
      (incoming) => {
        const chunks = [];
        incoming.on("data", (chunk) => chunks.push(Buffer.from(chunk)));
        incoming.on("end", () => resolve({
          status: incoming.statusCode,
          body: Buffer.concat(chunks).toString("utf8")
        }));
      }
    );
    outgoing.on("socket", (socket) => {
      clientSocket = socket;
    });
    outgoing.once("error", reject);
    outgoing.end();
  });
  await new Promise((resolve) => setImmediate(resolve));
  const clientBeforeStop = {
    connected: Boolean(clientSocket && !clientSocket.destroyed),
    destroyed: clientSocket?.destroyed ?? null,
    response
  };
  const result = await stopAndObserve(context, async () => agent.destroy());
  result.clientBeforeStop = clientBeforeStop;
  result.clientAfterStop = {
    destroyed: clientSocket?.destroyed ?? null
  };
  agent.destroy();
  return result;
}

async function partialOrdinaryRequestCase() {
  const context = await startCase("ordinary-partial-request");
  const socket = createConnection(context.socketPath);
  await once(socket, "connect");
  socket.write(
    "GET /v1/health HTTP/1.1\r\nHost: chirality.invalid\r\nAuthorization: Bearer tm112-token\r\n"
  );
  const clientBeforeStop = { connected: !socket.destroyed, destroyed: socket.destroyed };
  const result = await stopAndObserve(context, async () => {
    socket.destroy();
    await once(socket, "close").catch(() => undefined);
  });
  result.clientBeforeStop = clientBeforeStop;
  result.clientAfterStop = { destroyed: socket.destroyed };
  return result;
}

async function liveSseCase() {
  const context = await startCase("live-sse");
  let incoming;
  let outgoing;
  const firstChunk = await new Promise((resolve, reject) => {
    const body = Buffer.from(JSON.stringify({ brief: "tm112", approvalReference: "D-TEST" }));
    outgoing = httpRequest(
      {
        socketPath: context.socketPath,
        path: "/v1/projects/tm112-project/runs",
        method: "POST",
        headers: {
          authorization: "Bearer tm112-token",
          "content-type": "application/json",
          "content-length": body.byteLength
        }
      },
      (response) => {
        incoming = response;
        response.once("data", (chunk) => resolve({
          status: response.statusCode,
          contentType: response.headers["content-type"],
          chunk: Buffer.from(chunk).toString("utf8")
        }));
        response.once("error", (error) => {
          if (!response.destroyed) reject(error);
        });
      }
    );
    outgoing.once("error", (error) => {
      if (!outgoing.destroyed) reject(error);
    });
    outgoing.write(body);
    outgoing.end();
  });
  const clientBeforeStop = {
    responseDestroyed: incoming.destroyed,
    requestDestroyed: outgoing.destroyed,
    firstChunk
  };
  const result = await stopAndObserve(context, async () => {
    incoming.destroy();
    outgoing.destroy();
    await sleep(20);
    context.serviceState.releaseStream();
  });
  result.clientBeforeStop = clientBeforeStop;
  result.clientAfterStop = {
    responseDestroyed: incoming.destroyed,
    requestDestroyed: outgoing.destroyed,
    interruptCalls: context.serviceState.interruptCalls()
  };
  return result;
}

const executedAt = now();
const cases = [];
for (const run of [idleCase, ordinaryKeepAliveCase, partialOrdinaryRequestCase, liveSseCase]) {
  cases.push(await run());
}
console.log(JSON.stringify({
  schemaVersion: "tm112-runtime-stop-reproducer/v1",
  executedAt,
  completedAt: now(),
  node: process.version,
  platform: process.platform,
  arch: process.arch,
  pid: process.pid,
  runtimeRoot,
  cases
}, null, 2));
