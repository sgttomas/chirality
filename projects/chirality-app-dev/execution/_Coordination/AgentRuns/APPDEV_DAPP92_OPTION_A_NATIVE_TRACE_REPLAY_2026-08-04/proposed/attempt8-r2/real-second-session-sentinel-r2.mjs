import { closeSync, existsSync, openSync, readFileSync, renameSync, writeFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const EXPECTED = '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service';
const phase = process.argv[2];
const pid = Number(process.argv[3]);
const phases = {
  'attach-started': ['attach-started.json', 'LLDB_ATTACH_STARTING'],
  'trace-ready': ['trace-ready.json', 'LLDB_TRACE_READY'],
  'trace-live': ['trace-live.json', 'LLDB_TRACE_LIVE'],
  detached: ['detached.json', 'LLDB_DETACHED_AND_TERMINAL'],
  'no-attach-terminal': ['detached.json', 'LLDB_DETACHED_AND_TERMINAL']
};
if (!phases[phase] || !Number.isInteger(pid) || pid <= 0) throw new Error('exact phase/PID required');
const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
if (controller.schema !== 'chirality-dapp92-real-runtime-controller-r2/v1' || controller.state !== 'ATTACH_READY' || controller.directChildPid !== pid || controller.helperExecutable !== EXPECTED) throw new Error('controller binding mismatch');

function capture(executable, args) {
  const value = spawnSync(executable, args, { encoding: 'utf8', timeout: 5000 });
  if (value.status !== 0 || value.signal !== null || value.error) throw new Error(`${executable} identity check failed`);
  return (value.stdout ?? '').trim();
}
if (phase !== 'detached' && phase !== 'no-attach-terminal') {
  const live = {
    pid: capture('/bin/ps', ['-o', 'pid=', '-p', String(pid)]),
    ppid: capture('/bin/ps', ['-o', 'ppid=', '-p', String(pid)]),
    start: capture('/bin/ps', ['-o', 'lstart=', '-p', String(pid)]),
    command: capture('/bin/ps', ['-o', 'comm=', '-p', String(pid)]),
    text: capture('/usr/sbin/lsof', ['-a', '-p', String(pid), '-d', 'txt', '-Fn'])
  };
  if (live.pid !== String(pid) || live.ppid !== String(controller.controllerPid) || live.start !== controller.helperIdentity.start || live.command !== EXPECTED || !live.text.split('\n').includes(`n${EXPECTED}`)) throw new Error('live PID/PPID/executable/start identity mismatch');
}
if (phase === 'trace-ready' && !existsSync(`${PROTOCOL}/attach-started.json`)) throw new Error('attach-started missing');
if (phase === 'trace-live' && (!existsSync(`${PROTOCOL}/trace-ready.json`) || !existsSync(`${PROTOCOL}/signal-armed.json`))) throw new Error('trace-live prerequisites missing');
if (phase === 'no-attach-terminal' && existsSync(`${PROTOCOL}/attach-started.json`)) throw new Error('attach did start');
const [name, state] = phases[phase];
const destination = `${PROTOCOL}/${name}`;
if (existsSync(destination)) throw new Error('sentinel already exists');
const bytes = `${JSON.stringify({ schema: 'chirality-dapp92-real-runtime-sentinel-r2/v1', directChildPid: pid, state }, null, 2)}\n`;
const temporary = `${destination}.${process.pid}.tmp`;
const descriptor = openSync(temporary, 'wx', 0o600);
try { writeFileSync(descriptor, bytes, 'utf8'); } finally { closeSync(descriptor); }
renameSync(temporary, destination);
process.stdout.write(bytes);
