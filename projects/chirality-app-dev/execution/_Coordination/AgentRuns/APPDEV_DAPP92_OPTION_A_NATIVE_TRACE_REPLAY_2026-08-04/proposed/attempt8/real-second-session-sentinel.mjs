import {
  closeSync,
  existsSync,
  openSync,
  readFileSync,
  renameSync,
  writeFileSync
} from 'node:fs';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const phase = process.argv[2];
const suppliedPid = Number(process.argv[3]);
const phases = {
  'attach-started': {
    file: 'attach-started.json',
    state: 'LLDB_ATTACH_STARTING',
    prerequisite: undefined
  },
  'trace-ready': {
    file: 'trace-ready.json',
    state: 'LLDB_TRACE_READY',
    prerequisite: undefined
  },
  'trace-live': {
    file: 'trace-live.json',
    state: 'LLDB_TRACE_LIVE',
    prerequisite: 'signal-armed.json'
  },
  detached: {
    file: 'detached.json',
    state: 'LLDB_DETACHED_AND_TERMINAL',
    prerequisite: undefined
  },
  'no-attach-terminal': {
    file: 'detached.json',
    state: 'LLDB_DETACHED_AND_TERMINAL',
    prerequisite: undefined
  }
};

const selected = phases[phase];
if (!selected || !Number.isInteger(suppliedPid) || suppliedPid <= 0) {
  throw new Error('exact phase and positive direct-child PID are required');
}
const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
if (
  controller.schema !== 'chirality-dapp92-real-runtime-controller/v1' ||
  controller.state !== 'ATTACH_READY' ||
  controller.directChildPid !== suppliedPid ||
  controller.helperExecutable !== '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service'
) {
  throw new Error('controller schema/state/PID/executable mismatch');
}
if (selected.prerequisite && !existsSync(`${PROTOCOL}/${selected.prerequisite}`)) {
  throw new Error(`missing prerequisite ${selected.prerequisite}`);
}
if (phase === 'trace-live' && !existsSync(`${PROTOCOL}/trace-ready.json`)) {
  throw new Error('trace-ready sentinel missing');
}
const destination = `${PROTOCOL}/${selected.file}`;
if (existsSync(destination)) throw new Error('sentinel already exists');
const bytes = `${JSON.stringify({
  schema: 'chirality-dapp92-real-runtime-sentinel/v1',
  directChildPid: suppliedPid,
  state: selected.state
}, null, 2)}\n`;
const temporary = `${destination}.${process.pid}.tmp`;
const descriptor = openSync(temporary, 'wx', 0o600);
try {
  writeFileSync(descriptor, bytes, 'utf8');
} finally {
  closeSync(descriptor);
}
renameSync(temporary, destination);
process.stdout.write(bytes);
