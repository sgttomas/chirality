import { closeSync, existsSync, openSync, readFileSync, renameSync, writeFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const EXPECTED = '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service';
const phase = process.argv[2];
const pid = Number(process.argv[3]);
const phases = {
  'attach-intent': ['attach-intent.json', 'LLDB_ATTACH_INTENT_RECORDED', 'C720', 'C721'],
  'trace-ready': ['trace-ready.json', 'LLDB_TRACE_READY', 'C722', 'C723'],
  'trace-live': ['trace-live.json', 'LLDB_TRACE_LIVE', 'C724', 'C725']
};
if (!phases[phase] || !Number.isInteger(pid) || pid <= 0) throw new Error('exact phase/PID required');
const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
if (controller.schema !== 'chirality-dapp92-real-runtime-controller-r4/v1' || controller.state !== 'ATTACH_READY' || controller.directChildPid !== pid || controller.helperExecutable !== EXPECTED) throw new Error('controller mismatch');
function capture(actionId, executable, args) {
  const result = spawnSync(executable, args, { encoding: 'utf8', timeout: 5000 });
  if (result.status !== 0 || result.signal !== null || result.error) throw new Error(`${actionId} failed`);
  return result.stdout ?? '';
}
const [, state, psAction, lsofAction] = phases[phase];
const ps = capture(psAction, '/bin/ps', ['-o', 'pid=', '-o', 'ppid=', '-o', 'lstart=', '-o', 'comm=', '-p', String(pid)]);
const match = ps.match(/^\s*(\d+)\s+(\d+)\s+(\S+\s+\S+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+(.+?)\s*$/);
const text = capture(lsofAction, '/usr/sbin/lsof', ['-a', '-p', String(pid), '-d', 'txt', '-Fn']);
if (!match || Number(match[1]) !== pid || Number(match[2]) !== controller.controllerPid || match[3] !== controller.helperIdentity.start || match[4] !== EXPECTED || !text.split('\n').includes(`n${EXPECTED}`)) throw new Error('live identity mismatch');
if (phase === 'trace-ready' && (!existsSync(`${PROTOCOL}/attach-intent.json`) || !existsSync(`${PROTOCOL}/lldb-spawn-attempt.json`) || !existsSync(`${PROTOCOL}/lldb-start.json`))) throw new Error('trace-ready prerequisites missing');
if (phase === 'trace-live' && (!existsSync(`${PROTOCOL}/trace-ready.json`) || !existsSync(`${PROTOCOL}/signal-armed.json`))) throw new Error('trace-live prerequisites missing');
const destination = `${PROTOCOL}/${phases[phase][0]}`;
const bytes = `${JSON.stringify({ schema: 'chirality-dapp92-real-runtime-sentinel-r4/v1', state, directChildPid: pid, controllerPid: controller.controllerPid, psAction, lsofAction }, null, 2)}\n`;
const temporary = `${destination}.${process.pid}.tmp`;
const fd = openSync(temporary, 'wx', 0o600);
try { writeFileSync(fd, bytes); } finally { closeSync(fd); }
renameSync(temporary, destination);
process.stdout.write(bytes);
