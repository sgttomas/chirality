import { once } from "node:events";
import { fork } from "node:child_process";
import { existsSync } from "node:fs";
import { mkdir, mkdtemp, stat, writeFile } from "node:fs/promises";
import { request as httpRequest } from "node:http";
import { join } from "node:path";
import { pathToFileURL } from "node:url";

const runtimeRoot = process.argv[2];
const mode = process.argv[3] ?? "parent";
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

if (mode === "child") {
  const daemonModule = join(runtimeRoot, "packages/daemon/dist/runtime-daemon.js");
  if (!existsSync(daemonModule)) throw new Error(`built daemon module absent: ${daemonModule}`);
  const { RuntimeDaemon } = await import(pathToFileURL(daemonModule));
  const root = await mkdtemp(join("/tmp", "t112s-"));
  const runtimeDirectory = join(root, "runtime");
  await mkdir(runtimeDirectory, { recursive: true });
  const socketPath = join(runtimeDirectory, "control.sock");
  const ownerPath = `${socketPath}.owner.json`;
  const tokenFile = join(root, "operator.token");
  await writeFile(tokenFile, "tm112-token\n", { mode: 0o600 });
  let releaseStream;
  const streamRelease = new Promise((resolve) => { releaseStream = resolve; });
  const service = {
    auth: {
      async ensureClient() { return { tokenFile }; },
      async authenticate() { return { clientId: "tm112-client", projectId: "tm112-project" }; }
    },
    async *runAgent1() {
      yield { type: "harness:event", data: { sessionId: "tm112-manager" } };
      await streamRelease;
    },
    async interruptSession() { releaseStream(); }
  };
  const daemon = new RuntimeDaemon({ runtimeDirectory, socketPath, service });
  await daemon.start();
  const body = Buffer.from(JSON.stringify({ brief: "tm112", approvalReference: "D-TEST" }));
  let incoming;
  let outgoing;
  const firstChunk = await new Promise((resolve, reject) => {
    outgoing = httpRequest({
      socketPath,
      path: "/v1/projects/tm112-project/runs",
      method: "POST",
      headers: {
        authorization: "Bearer tm112-token",
        "content-type": "application/json",
        "content-length": body.byteLength
      }
    }, (response) => {
      incoming = response;
      response.once("data", (chunk) => resolve(Buffer.from(chunk).toString("utf8")));
    });
    outgoing.once("error", reject);
    outgoing.write(body);
    outgoing.end();
  });
  process.send?.({ type: "READY", at: now(), pid: process.pid, root, socketPath, ownerPath, firstChunk });
  process.once("SIGUSR1", () => {
    process.send?.({ type: "CLIENT_RELEASE", at: now() });
    incoming.destroy();
    outgoing.destroy();
    releaseStream();
  });
  process.once("SIGTERM", () => {
    const began = process.hrtime.bigint();
    process.send?.({ type: "SIGTERM_RECEIVED", at: now() });
    void daemon.stop().then(async () => {
      process.send?.({
        type: "STOP_RESOLVED",
        at: now(),
        elapsedMs: Number(process.hrtime.bigint() - began) / 1e6,
        socket: await pathState(socketPath),
        owner: await pathState(ownerPath)
      });
      process.exit(0);
    });
  });
  await new Promise(() => {});
} else {
  if (!runtimeRoot) throw new Error("usage: node runtime-signal-sse-reproducer.mjs <built-runtime-root>");
  const child = fork(new URL(import.meta.url), [runtimeRoot, "child"], {
    stdio: ["ignore", "pipe", "pipe", "ipc"]
  });
  const messages = [];
  const stdout = [];
  const stderr = [];
  child.stdout.on("data", (chunk) => stdout.push(Buffer.from(chunk).toString("utf8")));
  child.stderr.on("data", (chunk) => stderr.push(Buffer.from(chunk).toString("utf8")));
  child.on("message", (message) => messages.push(message));
  while (!messages.some((message) => message.type === "READY")) await sleep(10);
  const ready = messages.find((message) => message.type === "READY");
  const sigtermSentAt = now();
  child.kill("SIGTERM");
  await sleep(750);
  const atBoundary = {
    at: now(),
    childAlive: child.exitCode === null && child.signalCode === null,
    exitCode: child.exitCode,
    signalCode: child.signalCode,
    socket: await pathState(ready.socketPath),
    owner: await pathState(ready.ownerPath),
    messages: [...messages]
  };
  const releaseSentAt = now();
  child.kill("SIGUSR1");
  const exit = await Promise.race([
    once(child, "exit").then(([exitCode, signalCode]) => ({ state: "EXITED", exitCode, signalCode })),
    sleep(2000).then(() => ({ state: "PENDING_AT_RELEASE_BOUNDARY" }))
  ]);
  if (exit.state !== "EXITED") child.kill("SIGKILL");
  console.log(JSON.stringify({
    schemaVersion: "tm112-runtime-signal-sse-reproducer/v1",
    executedAt: messages[0]?.at,
    completedAt: now(),
    node: process.version,
    platform: process.platform,
    arch: process.arch,
    parentPid: process.pid,
    childPid: ready.pid,
    runtimeRoot,
    sigtermSentAt,
    stopBoundaryMs: 750,
    atBoundary,
    releaseSentAt,
    releaseBoundaryMs: 2000,
    exit,
    finalMessages: messages,
    stdout,
    stderr
  }, null, 2));
}

