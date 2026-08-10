import { spawn } from "node:child_process";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { setTimeout as delay } from "node:timers/promises";

const root = "/private/tmp/chirality-dapp92-attempt6-protocol";
const controllerPath = `${root}/controller.json`;
const sentinelPath = `${root}/second-session.ready`;
const resultPath = `${root}/protocol-result.json`;

if (existsSync(controllerPath) || existsSync(sentinelPath) || existsSync(resultPath)) {
  throw new Error("attempt6 protocol paths must be absent before controller start");
}

const child = spawn("/bin/sleep", ["10"], {
  stdio: "ignore",
});

if (!Number.isSafeInteger(child.pid) || child.pid <= 0) {
  throw new Error("mock direct-child PID was not created");
}

writeFileSync(
  controllerPath,
  `${JSON.stringify(
    {
      schema: "chirality-dapp92-two-session-controller/v1",
      controllerPid: process.pid,
      directChildPid: child.pid,
      childExecutable: "/bin/sleep",
      childArgv: ["10"],
      state: "ATTACH_READY",
    },
    null,
    2,
  )}\n`,
  { encoding: "utf8", flag: "wx", mode: 0o600 },
);

let sentinel;
for (let poll = 1; poll <= 100; poll += 1) {
  if (existsSync(sentinelPath)) {
    sentinel = JSON.parse(readFileSync(sentinelPath, "utf8"));
    break;
  }
  await delay(50);
}

if (
  sentinel?.schema !== "chirality-dapp92-two-session-sentinel/v1" ||
  sentinel?.directChildPid !== child.pid ||
  sentinel?.state !== "SECOND_SESSION_ACKNOWLEDGED"
) {
  throw new Error("exact second-session sentinel was not received within 5 seconds");
}

const [exitCode, signal] = await new Promise((resolve) => {
  child.once("exit", (code, childSignal) => resolve([code, childSignal]));
});

const result = {
  schema: "chirality-dapp92-two-session-result/v1",
  directChildPid: child.pid,
  sentinelMatched: true,
  childExitCode: exitCode,
  childSignal: signal,
  controllerState: "COMPLETE",
};

writeFileSync(resultPath, `${JSON.stringify(result, null, 2)}\n`, {
  encoding: "utf8",
  flag: "wx",
  mode: 0o600,
});
process.stdout.write(`${JSON.stringify(result)}\n`);
