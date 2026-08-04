import { createServer } from "node:http";
import { writeFile, unlink } from "node:fs/promises";
import { connect } from "node:net";
import process from "node:process";

const outputPath = process.argv[2];
if (!outputPath) throw new Error("usage: node probe-node-http-stop.mjs OUTPUT.json");

let sequence = 0;
const delay = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));
const nextPath = () => `/tmp/e1-node-${process.pid}-${++sequence}.sock`;

async function remove(path) {
  await unlink(path).catch((error) => {
    if (error?.code !== "ENOENT") throw error;
  });
}

async function listen(server, path) {
  await remove(path);
  await new Promise((resolve, reject) => {
    const onError = (error) => reject(error);
    server.once("error", onError);
    server.listen(path, () => {
      server.off("error", onError);
      resolve();
    });
  });
}

async function openClient(path) {
  const socket = connect(path);
  socket.setEncoding("utf8");
  socket.on("error", () => undefined);
  await new Promise((resolve, reject) => {
    socket.once("connect", resolve);
    socket.once("error", reject);
  });
  return socket;
}

async function waitForData(socket, needle, milliseconds = 500) {
  let received = "";
  await new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`timeout waiting for ${needle}; got ${received}`)), milliseconds);
    const onData = (chunk) => {
      received += chunk;
      if (received.includes(needle)) {
        clearTimeout(timer);
        socket.off("data", onData);
        resolve();
      }
    };
    socket.on("data", onData);
  });
  return received;
}

function startClose(server, events = []) {
  let settled = false;
  let callbackError;
  const promise = new Promise((resolve) => {
    const returned = server.close((error) => {
      callbackError = error ? { code: error.code, name: error.name, message: error.message } : null;
      settled = true;
      events.push("close-callback");
      resolve();
    });
    events.push(returned === server ? "close-returned-server" : "close-returned-other");
  });
  return {
    promise,
    snapshot: () => ({ settled, callbackError })
  };
}

async function prepareConnection(kind) {
  const path = nextPath();
  const sockets = new Set();
  let requestObserved = false;
  const server = createServer((request, response) => {
    requestObserved = true;
    if (kind === "completedKeepAlive") {
      response.writeHead(200, { "content-length": "2", connection: "keep-alive" });
      response.end("OK");
    } else if (kind === "sse") {
      response.writeHead(200, { "content-type": "text/event-stream", connection: "keep-alive" });
      response.write("data: first\n\n");
    } else {
      request.on("data", () => undefined);
    }
  });
  server.on("connection", (socket) => {
    sockets.add(socket);
    socket.on("close", () => sockets.delete(socket));
    socket.on("error", () => undefined);
  });
  server.on("upgrade", (_request, socket) => {
    requestObserved = true;
    socket.write("HTTP/1.1 101 Switching Protocols\r\nConnection: Upgrade\r\nUpgrade: e1\r\n\r\n");
  });
  await listen(server, path);
  const client = await openClient(path);
  let clientClosed = false;
  client.on("close", () => { clientClosed = true; });

  if (kind === "idleNoBytes") {
    await delay(20);
  } else if (kind === "completedKeepAlive") {
    client.write("GET / HTTP/1.1\r\nHost: e1\r\nConnection: keep-alive\r\n\r\n");
    await waitForData(client, "OK");
    await delay(20);
  } else if (kind === "incompleteHeaders") {
    client.write("POST / HTTP/1.1\r\nHost: e1\r\nContent-Length: 10\r\n");
    await delay(20);
  } else if (kind === "incompleteBody") {
    client.write("POST / HTTP/1.1\r\nHost: e1\r\nContent-Length: 10\r\n\r\nabc");
    await delay(20);
  } else if (kind === "sse") {
    client.write("GET / HTTP/1.1\r\nHost: e1\r\n\r\n");
    await waitForData(client, "data: first");
  } else if (kind === "upgrade") {
    client.write("GET / HTTP/1.1\r\nHost: e1\r\nConnection: Upgrade\r\nUpgrade: e1\r\n\r\n");
    await waitForData(client, "101 Switching Protocols");
  } else {
    throw new Error(`unknown kind ${kind}`);
  }

  return {
    server,
    path,
    client,
    sockets,
    requestObserved: () => requestObserved,
    clientClosed: () => clientClosed
  };
}

async function connectionScenario(kind, operation) {
  const fixture = await prepareConnection(kind);
  const events = [];
  fixture.server.once("close", () => events.push("close-event"));
  let closeRun;
  if (operation === "close") {
    closeRun = startClose(fixture.server, events);
  } else if (operation === "closeIdleConnections") {
    fixture.server.closeIdleConnections();
    events.push("closeIdleConnections-returned");
  } else if (operation === "closeAllConnections") {
    fixture.server.closeAllConnections();
    events.push("closeAllConnections-returned");
  } else if (operation === "closeThenCloseAll") {
    closeRun = startClose(fixture.server, events);
    fixture.server.closeAllConnections();
    events.push("closeAllConnections-returned");
  } else if (operation === "closeThenCloseIdle") {
    closeRun = startClose(fixture.server, events);
    fixture.server.closeIdleConnections();
    events.push("closeIdleConnections-returned");
  } else {
    throw new Error(`unknown operation ${operation}`);
  }

  await delay(80);
  const observation = {
    serverListening: fixture.server.listening,
    close: closeRun?.snapshot() ?? null,
    clientDestroyed: fixture.client.destroyed,
    clientClosed: fixture.clientClosed(),
    trackedServerSockets: fixture.sockets.size,
    requestObserved: fixture.requestObserved(),
    events: [...events]
  };

  for (const socket of fixture.sockets) socket.destroy();
  fixture.client.destroy();
  if (closeRun) {
    await closeRun.promise;
  } else if (fixture.server.listening) {
    const cleanup = startClose(fixture.server);
    await cleanup.promise;
  }
  await remove(fixture.path);
  return { kind, operation, observation, finalClose: closeRun?.snapshot() ?? null, finalEvents: events };
}

async function callbackAndOrdering() {
  const unopened = createServer();
  const unopenedEvents = [];
  unopened.once("close", () => unopenedEvents.push("close-event"));
  const unopenedClose = startClose(unopened, unopenedEvents);
  unopenedEvents.push("after-close-call");
  await unopenedClose.promise;

  const path = nextPath();
  const server = createServer();
  await listen(server, path);
  const openEvents = [];
  server.once("close", () => openEvents.push("close-event"));
  const first = startClose(server, openEvents);
  openEvents.push("after-first-close-call");
  const second = startClose(server, openEvents);
  openEvents.push("after-second-close-call");
  await Promise.all([first.promise, second.promise]);
  await remove(path);

  const afterEvents = [];
  server.once("close", () => afterEvents.push("close-event"));
  const after = startClose(server, afterEvents);
  afterEvents.push("after-close-call");
  await after.promise;

  return {
    neverListened: { events: unopenedEvents, callback: unopenedClose.snapshot() },
    doubleCloseWhileNoConnections: {
      events: openEvents,
      first: first.snapshot(),
      second: second.snapshot()
    },
    closeAfterClosed: { events: afterEvents, callback: after.snapshot() }
  };
}

async function acceptsAfterConnectionClosers() {
  const results = [];
  for (const operation of ["closeIdleConnections", "closeAllConnections"]) {
    const path = nextPath();
    const server = createServer((_request, response) => response.end("OK"));
    await listen(server, path);
    server[operation]();
    const client = await openClient(path);
    client.write("GET / HTTP/1.1\r\nHost: e1\r\nConnection: close\r\n\r\n");
    const response = await waitForData(client, "OK");
    results.push({ operation, remainedListening: server.listening, acceptedNewRequest: response.includes("OK") });
    client.destroy();
    await startClose(server).promise;
    await remove(path);
  }
  return results;
}

async function trackedSocketDestroyUpgrade() {
  const fixture = await prepareConnection("upgrade");
  const closeRun = startClose(fixture.server);
  await delay(40);
  const before = { close: closeRun.snapshot(), sockets: fixture.sockets.size, clientDestroyed: fixture.client.destroyed };
  for (const socket of fixture.sockets) socket.destroy();
  await closeRun.promise;
  await delay(20);
  const after = { close: closeRun.snapshot(), sockets: fixture.sockets.size, clientDestroyed: fixture.client.destroyed };
  fixture.client.destroy();
  await remove(fixture.path);
  return { before, after };
}

async function repeatedListen() {
  const server = createServer((_request, response) => response.end("OK"));
  const cycles = [];
  for (let generation = 1; generation <= 2; generation++) {
    const path = nextPath();
    await listen(server, path);
    const client = await openClient(path);
    client.write("GET / HTTP/1.1\r\nHost: e1\r\nConnection: close\r\n\r\n");
    const response = await waitForData(client, "OK");
    client.destroy();
    const closeRun = startClose(server);
    await closeRun.promise;
    cycles.push({ generation, acceptedRequest: response.includes("OK"), close: closeRun.snapshot(), listeningAfterClose: server.listening });
    await remove(path);
  }
  return cycles;
}

async function overlappingGenerations() {
  const path = nextPath();
  const sockets1 = new Set();
  const server1 = createServer((_request, response) => {
    response.writeHead(200, { "content-type": "text/event-stream" });
    response.write("data: old\n\n");
  });
  server1.on("connection", (socket) => {
    sockets1.add(socket);
    socket.on("close", () => sockets1.delete(socket));
  });
  await listen(server1, path);
  const oldClient = await openClient(path);
  oldClient.write("GET / HTTP/1.1\r\nHost: e1\r\n\r\n");
  await waitForData(oldClient, "data: old");
  const close1 = startClose(server1);
  await delay(20);

  const server2 = createServer((_request, response) => response.end("NEW"));
  let replacement;
  try {
    await listen(server2, path);
    const newClient = await openClient(path);
    newClient.write("GET / HTTP/1.1\r\nHost: e1\r\nConnection: close\r\n\r\n");
    const response = await waitForData(newClient, "NEW");
    replacement = { listenSucceeded: true, acceptedRequest: response.includes("NEW") };
    newClient.destroy();
    await startClose(server2).promise;
  } catch (error) {
    replacement = { listenSucceeded: false, error: { code: error.code, message: error.message } };
  }
  const oldBeforeRelease = close1.snapshot();
  for (const socket of sockets1) socket.destroy();
  oldClient.destroy();
  await close1.promise;
  await remove(path);
  return { oldBeforeRelease, replacement, oldAfterRelease: close1.snapshot() };
}

const matrix = [];
for (const kind of ["idleNoBytes", "completedKeepAlive", "incompleteHeaders", "incompleteBody", "sse", "upgrade"]) {
  matrix.push(await connectionScenario(kind, "close"));
}
for (const kind of ["idleNoBytes", "completedKeepAlive", "incompleteHeaders", "incompleteBody", "sse", "upgrade"]) {
  matrix.push(await connectionScenario(kind, "closeIdleConnections"));
}
for (const kind of ["idleNoBytes", "completedKeepAlive", "incompleteHeaders", "incompleteBody", "sse", "upgrade"]) {
  matrix.push(await connectionScenario(kind, "closeAllConnections"));
}
for (const kind of ["idleNoBytes", "incompleteHeaders", "incompleteBody", "sse", "upgrade"]) {
  matrix.push(await connectionScenario(kind, "closeThenCloseAll"));
}
for (const kind of ["idleNoBytes", "incompleteHeaders", "incompleteBody", "sse"]) {
  matrix.push(await connectionScenario(kind, "closeThenCloseIdle"));
}

const output = {
  schemaVersion: "e1-node-http-stop-probe/v1",
  executedAt: new Date().toISOString(),
  environment: {
    node: process.version,
    versions: process.versions,
    platform: process.platform,
    arch: process.arch,
    pid: process.pid
  },
  observationBoundaryMs: 80,
  callbackAndOrdering: await callbackAndOrdering(),
  matrix,
  acceptsAfterConnectionClosers: await acceptsAfterConnectionClosers(),
  trackedSocketDestroyUpgrade: await trackedSocketDestroyUpgrade(),
  repeatedListen: await repeatedListen(),
  overlappingGenerations: await overlappingGenerations()
};

await writeFile(outputPath, `${JSON.stringify(output, null, 2)}\n`, "utf8");
console.log(JSON.stringify({ outputPath, matrixCases: matrix.length, executedAt: output.executedAt }));
