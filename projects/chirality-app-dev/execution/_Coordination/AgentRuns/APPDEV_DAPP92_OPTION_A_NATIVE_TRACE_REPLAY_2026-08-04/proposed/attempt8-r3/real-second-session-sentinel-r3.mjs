import { closeSync, existsSync, openSync, readFileSync, renameSync, writeFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const EXPECTED = '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service';
const phase = process.argv[2]; const pid = Number(process.argv[3]);
const phases = {
  'attach-started': ['attach-started.json', 'LLDB_ATTACH_STARTING', 'C509', 'C510'],
  'trace-ready': ['trace-ready.json', 'LLDB_TRACE_READY', 'C511', 'C512'],
  'trace-live': ['trace-live.json', 'LLDB_TRACE_LIVE', 'C513', 'C514'],
  'no-debugger-start': ['no-debugger-start-observed.json', 'NO_LLDB_PROCESS_STARTED', undefined, undefined]
};
if (!phases[phase] || !Number.isInteger(pid) || pid <= 0) throw new Error('exact phase/PID required');
const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
if (controller.schema !== 'chirality-dapp92-real-runtime-controller-r3/v1' || controller.state !== 'ATTACH_READY' || controller.directChildPid !== pid || controller.helperExecutable !== EXPECTED) throw new Error('controller mismatch');
function capture(actionId, executable, args) {
  const value = spawnSync(executable, args, { encoding: 'utf8', timeout: 5000 });
  if (value.status !== 0 || value.signal !== null || value.error) throw new Error(`${actionId} failed`);
  return value.stdout ?? '';
}
const [, state, psAction, lsofAction] = phases[phase];
if (phase === 'no-debugger-start') {
  if (existsSync(`${PROTOCOL}/lldb-spawn-attempt.json`) || existsSync(`${PROTOCOL}/lldb-start.json`)) throw new Error('LLDB process start was observed');
} else {
  const ps = capture(psAction, '/bin/ps', ['-o', 'pid=', '-o', 'ppid=', '-o', 'lstart=', '-o', 'comm=', '-p', String(pid)]);
  const match = ps.match(/^\s*(\d+)\s+(\d+)\s+(\S+\s+\S+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+(.+?)\s*$/);
  const text = capture(lsofAction, '/usr/sbin/lsof', ['-a', '-p', String(pid), '-d', 'txt', '-Fn']);
  if (!match || Number(match[1]) !== pid || Number(match[2]) !== controller.controllerPid || match[3] !== controller.helperIdentity.start || match[4] !== EXPECTED || !text.split('\n').includes(`n${EXPECTED}`)) throw new Error('live identity mismatch');
}
if (phase === 'trace-ready' && !existsSync(`${PROTOCOL}/attach-started.json`)) throw new Error('attach-started missing');
if (phase === 'trace-live' && (!existsSync(`${PROTOCOL}/trace-ready.json`) || !existsSync(`${PROTOCOL}/signal-armed.json`))) throw new Error('trace-live prerequisite missing');
const destination = `${PROTOCOL}/${phases[phase][0]}`;
if (existsSync(destination)) throw new Error('sentinel already exists');
const bytes = `${JSON.stringify({ schema: 'chirality-dapp92-real-runtime-sentinel-r3/v1', state, directChildPid: pid, psAction, lsofAction }, null, 2)}\n`;
const temporary = `${destination}.${process.pid}.tmp`; const descriptor = openSync(temporary, 'wx', 0o600);
try { writeFileSync(descriptor, bytes, 'utf8'); } finally { closeSync(descriptor); }
renameSync(temporary, destination); process.stdout.write(bytes);
