import { closeSync, openSync, readFileSync, writeFileSync } from 'node:fs';
import { spawn, spawnSync } from 'node:child_process';
import { performance } from 'node:perf_hooks';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`; const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const TRACE = '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt';
const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
const pid = Number(process.argv[2]);
if (controller.schema !== 'chirality-dapp92-real-runtime-controller-r3/v1' || pid !== controller.directChildPid) throw new Error('controller/PID mismatch');
const stdoutFd = openSync(`${EVIDENCE}/lldb-pty.stdout.txt`, 'wx', 0o600);
const stderrFd = openSync(`${EVIDENCE}/lldb-pty.stderr.txt`, 'wx', 0o600);
const inputFd = openSync(`${EVIDENCE}/lldb-pty.input.bin`, 'wx', 0o600);
const child = spawn('/usr/bin/xcrun', ['lldb', '--batch', '-p', String(pid), '-s', TRACE], { stdio: ['pipe', 'pipe', 'pipe'], detached: true });
if (!Number.isInteger(child.pid) || child.pid <= 0) throw new Error('LLDB PID missing');
writeFileSync(`${PROTOCOL}/lldb-spawn-attempt.json`, `${JSON.stringify({ schema: 'chirality-dapp92-lldb-spawn-attempt-r3/v1', actionId: 'C515', targetPid: pid, lldbPid: child.pid, observedAt: new Date().toISOString() }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
let exitResult; let interruptObserved = false; let input = Buffer.alloc(0); let stdoutText = '';
const exit = new Promise((resolve, reject) => { child.once('error', reject); child.once('exit', (code, signal) => { exitResult = { code, signal, at: new Date().toISOString() }; resolve(exitResult); }); });
function capture(actionId, executable, args) {
  const value = spawnSync(executable, args, { encoding: 'utf8', timeout: 5000 });
  if (value.status !== 0 || value.signal !== null || value.error) throw new Error(`${actionId} failed`);
  return value.stdout ?? '';
}
function identity(psAction, lsofAction, baseline) {
  if (exitResult || child.exitCode !== null || child.signalCode !== null) throw new Error('LLDB not live');
  const text = capture(psAction, '/bin/ps', ['-o', 'pid=', '-o', 'ppid=', '-o', 'lstart=', '-o', 'comm=', '-p', String(child.pid)]);
  const match = text.match(/^\s*(\d+)\s+(\d+)\s+(\S+\s+\S+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+(.+?)\s*$/);
  const lsof = capture(lsofAction, '/usr/sbin/lsof', ['-a', '-p', String(child.pid), '-d', 'txt', '-Fn']);
  if (!match || Number(match[1]) !== child.pid || Number(match[2]) !== process.pid || !lsof.split('\n').some((line) => line.endsWith('/lldb'))) throw new Error('LLDB live identity mismatch');
  const value = { pid: child.pid, ppid: process.pid, start: match[3], command: match[4] };
  if (baseline && baseline.start !== value.start) throw new Error('LLDB start identity drift');
  return value;
}
let initialIdentity; let supervisorError;
child.stdout.on('data', (chunk) => { writeFileSync(stdoutFd, chunk); stdoutText += chunk.toString('utf8'); process.stdout.write(chunk); });
child.stderr.on('data', (chunk) => { writeFileSync(stderrFd, chunk); process.stderr.write(chunk); });
process.on('SIGINT', () => {
  try {
    if (interruptObserved) throw new Error('duplicate C197 interrupt rejected');
    interruptObserved = true;
    const proof = identity('C518', 'C519', initialIdentity);
    if (!child.kill('SIGINT')) throw new Error('C520 LLDB SIGINT rejected');
    writeFileSync(`${PROTOCOL}/c197-interrupt-observed.json`, `${JSON.stringify({ schema: 'chirality-dapp92-c197-interrupt-r3/v1', actionId: 'C520', proof }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
  } catch (error) { supervisorError = error instanceof Error ? error.message : String(error); }
});
process.stdin.on('data', (chunk) => {
  try {
    writeFileSync(inputFd, chunk); input = Buffer.concat([input, chunk]);
    if (input.length > 64) throw new Error('LLDB input exceeded sealed C197 bytes');
    child.stdin.write(chunk);
  } catch (error) { supervisorError = error instanceof Error ? error.message : String(error); }
});
let watchdogTimer;
const watchdog = new Promise((resolve, reject) => {
  watchdogTimer = setTimeout(() => {
    if (exitResult) return resolve({ fired: false });
    try {
      const proof = identity('C521', 'C522', initialIdentity);
      if (!child.kill('SIGKILL')) throw new Error('C523 LLDB SIGKILL rejected');
      resolve({ fired: true, actionId: 'C523', proof, at: new Date().toISOString() });
    } catch (error) { reject(error); }
  }, 149000);
});
let terminal;
try {
  await new Promise((resolve) => setTimeout(resolve, 100));
  initialIdentity = identity('C516', 'C517');
  writeFileSync(`${PROTOCOL}/lldb-start.json`, `${JSON.stringify({ schema: 'chirality-dapp92-lldb-start-r3/v1', actionId: 'C196', targetPid: pid, lldbIdentity: initialIdentity, startedMonotonicMs: performance.now() }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
  terminal = await Promise.race([
    exit.then((value) => ({ exit: value, watchdog: { fired: false } })),
    watchdog.then(async (watchdogValue) => ({ exit: await Promise.race([exit, new Promise((_, reject) => setTimeout(() => reject(new Error('LLDB failed to terminate by 150 seconds')), 900))]), watchdog: watchdogValue }))
  ]);
} catch (error) {
  supervisorError = error instanceof Error ? error.message : String(error);
  terminal = await watchdog.then(async (watchdogValue) => ({ exit: await Promise.race([exit, new Promise((_, reject) => setTimeout(() => reject(new Error('LLDB failed to terminate by 150 seconds')), 900))]), watchdog: watchdogValue }));
} finally {
  if (exitResult) clearTimeout(watchdogTimer);
}
const expectedText = Buffer.from('process detach\nquit\n');
const c197Exact = interruptObserved && input.equals(expectedText);
const detachOutputObserved = /Process \d+ detached/.test(stdoutText);
closeSync(stdoutFd); closeSync(stderrFd); closeSync(inputFd);
writeFileSync(`${PROTOCOL}/lldb-terminal.json`, `${JSON.stringify({ schema: 'chirality-dapp92-lldb-terminal-r3/v1', targetPid: pid, lldbIdentity: initialIdentity, ...terminal, interruptObserved, c197Exact, detachOutputObserved, supervisorError }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
if (!((c197Exact && detachOutputObserved) || terminal.watchdog.fired)) process.exitCode = 2;
