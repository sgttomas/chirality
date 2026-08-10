import { readFileSync, writeFileSync } from "node:fs";

const root = "/private/tmp/chirality-dapp92-attempt6-protocol";
const controller = JSON.parse(readFileSync(`${root}/controller.json`, "utf8"));

if (
  controller?.schema !== "chirality-dapp92-two-session-controller/v1" ||
  controller?.state !== "ATTACH_READY" ||
  !Number.isSafeInteger(controller?.directChildPid) ||
  controller.directChildPid <= 0 ||
  controller?.childExecutable !== "/bin/sleep"
) {
  throw new Error("controller PID record is not an exact valid mock binding");
}

const sentinel = {
  schema: "chirality-dapp92-two-session-sentinel/v1",
  directChildPid: controller.directChildPid,
  state: "SECOND_SESSION_ACKNOWLEDGED",
};

writeFileSync(`${root}/second-session.ready`, `${JSON.stringify(sentinel, null, 2)}\n`, {
  encoding: "utf8",
  flag: "wx",
  mode: 0o600,
});
process.stdout.write(`${JSON.stringify(sentinel)}\n`);
