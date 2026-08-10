import { spawn } from "node:child_process";
import {
  closeSync,
  existsSync,
  fsyncSync,
  openSync,
  readFileSync,
  writeFileSync,
} from "node:fs";
import { setTimeout as delay } from "node:timers/promises";

const root = "/private/tmp/chirality-dapp92-attempt6-protocol";
const controllerPath = `${root}/controller.json`;
const sentinelPath = `${root}/second-session.ready`;
const resultPath = `${root}/protocol-result.json`;
const sentinelWindowMs = 30_000;

function writeExclusiveDurably(path, value) {
  const descriptor = openSync(path, "wx", 0o600);
  try {
    writeFileSync(descriptor, value, { encoding: "utf8" });
    fsyncSync(descriptor);
  } finally {
    closeSync(descriptor);
  }
}

if (existsSync(controllerPath) || existsSync(sentinelPath) || existsSync(resultPath)) {
  throw new Error("attempt6 protocol paths must be absent before controller start");
}

const child = spawn("/bin/sleep", ["35"], {
  stdio: "ignore",
});

let childExitObserved = false;
const childExitPromise = new Promise((resolve) => {
  child.once("error", (error) => {
    childExitObserved = true;
    resolve({ kind: "error", message: error.message });
  });
  child.once("exit", (code, signal) => {
    childExitObserved = true;
    resolve({ kind: "exit", code, signal });
  });
});

if (!Number.isSafeInteger(child.pid) || child.pid <= 0) {
  await childExitPromise;
  throw new Error("mock direct-child PID was not created");
}

const controller = {
  schema: "chirality-dapp92-two-session-controller/v1",
  controllerPid: process.pid,
  directChildPid: child.pid,
  childExecutable: "/bin/sleep",
  childArgv: ["35"],
  state: "ATTACH_READY",
};

try {
  writeExclusiveDurably(controllerPath, `${JSON.stringify(controller, null, 2)}\n`);
} catch (error) {
  await childExitPromise;
  throw error;
}

try {
  await new Promise((resolve, reject) => {
    process.stdout.write(`${JSON.stringify(controller)}\n`, (error) => {
      if (error) {
        reject(error);
        return;
      }
      resolve();
    });
  });
} catch (error) {
  await childExitPromise;
  throw error;
}

let sentinel;
let sentinelFailure = "exact second-session sentinel was not received within 30 seconds";
const sentinelDeadline = Date.now() + sentinelWindowMs;

while (Date.now() < sentinelDeadline) {
  if (existsSync(sentinelPath)) {
    try {
      sentinel = JSON.parse(readFileSync(sentinelPath, "utf8"));
    } catch {
      sentinelFailure = "second-session sentinel was not valid JSON";
      break;
    }

    if (
      sentinel?.schema !== "chirality-dapp92-two-session-sentinel/v1" ||
      sentinel?.directChildPid !== child.pid ||
      sentinel?.state !== "SECOND_SESSION_ACKNOWLEDGED"
    ) {
      sentinelFailure = "second-session sentinel did not match the exact schema, PID, and state";
      break;
    }

    if (childExitObserved) {
      sentinelFailure = "mock direct child exited before the matching sentinel was consumed";
      sentinel = undefined;
    }
    break;
  }

  if (childExitObserved) {
    sentinelFailure = "mock direct child exited before a matching sentinel was available";
    break;
  }

  await delay(Math.min(50, Math.max(1, sentinelDeadline - Date.now())));
}

if (!sentinel) {
  await childExitPromise;
  throw new Error(sentinelFailure);
}

const childExit = await childExitPromise;
if (childExit.kind !== "exit" || childExit.code !== 0 || childExit.signal !== null) {
  throw new Error("mock direct child did not exit naturally with code 0 and no signal");
}

const result = {
  schema: "chirality-dapp92-two-session-result/v2",
  directChildPid: child.pid,
  sentinelMatched: true,
  sentinelState: sentinel.state,
  childExecutable: "/bin/sleep",
  childArgv: ["35"],
  sentinelWindowMs,
  childExitCode: childExit.code,
  childSignal: childExit.signal,
  controllerState: "COMPLETE",
};

writeExclusiveDurably(resultPath, `${JSON.stringify(result, null, 2)}\n`);
process.stdout.write(`${JSON.stringify(result)}\n`);
