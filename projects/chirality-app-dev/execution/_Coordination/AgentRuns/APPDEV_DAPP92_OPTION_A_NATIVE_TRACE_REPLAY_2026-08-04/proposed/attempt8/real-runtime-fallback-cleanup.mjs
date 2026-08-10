import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const PROTOCOL = `${ROOT}/protocol`;
const expectedHelper = '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service';

if (!existsSync(`${PROTOCOL}/detached.json`)) {
  throw new Error('LLDB detached-and-terminal sentinel is required');
}
const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
if (
  controller.schema !== 'chirality-dapp92-real-runtime-controller/v1' ||
  controller.helperExecutable !== expectedHelper ||
  !Number.isInteger(controller.directChildPid) ||
  controller.directChildPid <= 0
) {
  throw new Error('controller record mismatch');
}

function run(signal, pid) {
  return spawnSync('/bin/kill', [`-${signal}`, String(pid)], {
    encoding: 'utf8',
    timeout: 5000
  }).status;
}

async function terminate(pid, firstSignal) {
  const result = { pid, firstSignal, initial: run('0', pid), polls: [] };
  if (result.initial !== 0) return result;
  result.first = run(firstSignal, pid);
  for (let index = 1; index <= 80; index += 1) {
    const status = run('0', pid);
    result.polls.push({ index, status });
    if (status !== 0) return result;
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  result.kill = run('KILL', pid);
  for (let index = 1; index <= 80; index += 1) {
    const status = run('0', pid);
    result.polls.push({ index: 80 + index, status });
    if (status !== 0) return result;
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  throw new Error(`run-owned PID ${pid} survived bounded cleanup`);
}

const replay = existsSync(`${PROTOCOL}/replay-terminal.json`)
  ? JSON.parse(readFileSync(`${PROTOCOL}/replay-terminal.json`, 'utf8'))
  : {};
const cleanup = {
  schema: 'chirality-dapp92-real-runtime-fallback-cleanup/v1',
  helper: await terminate(controller.directChildPid, 'KILL')
};
if (Number.isInteger(replay.guiLaunch?.pid) && replay.guiLaunch.pid > 0) {
  cleanup.gui = await terminate(replay.guiLaunch.pid, 'TERM');
}
writeFileSync(`${EVIDENCE}/fallback-cleanup.json`, `${JSON.stringify(cleanup, null, 2)}\n`, {
  encoding: 'utf8',
  mode: 0o600
});
