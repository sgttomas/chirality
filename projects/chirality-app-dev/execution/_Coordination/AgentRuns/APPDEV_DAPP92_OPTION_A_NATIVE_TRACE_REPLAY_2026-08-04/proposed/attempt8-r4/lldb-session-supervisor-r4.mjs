import { closeSync, openSync, readFileSync, writeFileSync } from 'node:fs';
import { spawn, spawnSync } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';
import { performance } from 'node:perf_hooks';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const TRACE = '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt';
const targetPid = Number(process.argv[2]);
const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
if (controller.schema !== 'chirality-dapp92-real-runtime-controller-r4/v1' || targetPid !== controller.directChildPid) throw new Error('controller/PID mismatch');

const expectedInput = Buffer.from('process detach\nquit\n', 'utf8');
const sessionId = randomUUID();
const output = { stdout: [], stderr: [] };
const inputChunks = [];
let inputLength = 0;
let inputForwarded = false;
let inputRejected = false;
let interruptCount = 0;
let supervisorError = null;
let exitResult = null;
let initialIdentity = null;
let watchdogRecord = { fired: false, mode: null };
const registry = { lldb: null };

const stdoutFd = openSync(`${EVIDENCE}/lldb.stdout.bin`, 'wx', 0o600);
const stderrFd = openSync(`${EVIDENCE}/lldb.stderr.bin`, 'wx', 0o600);
const inputFd = openSync(`${EVIDENCE}/c197.input.bin`, 'wx', 0o600);

function capture(actionId, executable, args, timeout) {
  const result = spawnSync(executable, args, { encoding: 'utf8', timeout, maxBuffer: 1048576 });
  if (result.status !== 0 || result.signal !== null || result.error) throw new Error(`${actionId} identity probe failed`);
  return result.stdout ?? '';
}

function identity(psAction, lsofAction, baseline) {
  const owned = registry.lldb;
  if (!owned || owned.exitResult || owned.child.exitCode !== null || owned.child.signalCode !== null) throw new Error('LLDB child not live');
  const ps = capture(psAction, '/bin/ps', ['-o', 'pid=', '-o', 'ppid=', '-o', 'lstart=', '-o', 'comm=', '-p', String(owned.child.pid)], 120);
  const match = ps.match(/^\s*(\d+)\s+(\d+)\s+(\S+\s+\S+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+(.+?)\s*$/);
  const lsof = capture(lsofAction, '/usr/sbin/lsof', ['-a', '-p', String(owned.child.pid), '-d', 'txt', '-Fn'], 120);
  if (!match || Number(match[1]) !== owned.child.pid || Number(match[2]) !== process.pid || !lsof.split('\n').some((line) => line.endsWith('/lldb'))) throw new Error('LLDB identity mismatch');
  const value = { pid: owned.child.pid, ppid: process.pid, start: match[3], command: match[4] };
  if (baseline && (baseline.pid !== value.pid || baseline.ppid !== value.ppid || baseline.start !== value.start)) throw new Error('LLDB identity drift');
  return value;
}

function directHandleFailsafe(reason) {
  const owned = registry.lldb;
  if (!owned || owned.exitResult || owned.child.exitCode !== null || owned.child.signalCode !== null) return false;
  if (owned.child !== registry.lldb.child || owned.child.pid !== registry.lldb.pid || owned.spawnedByPid !== process.pid) throw new Error('direct-child handle ownership mismatch');
  watchdogRecord = { fired: true, mode: 'C738_DIRECT_CHILD_HANDLE_FAILSAFE', reason, at: new Date().toISOString() };
  return owned.child.kill('SIGKILL');
}

const spawnOriginMonotonicMs = performance.now();
const child = spawn('/usr/bin/xcrun', ['lldb', '--batch', '-p', String(targetPid), '-s', TRACE], { stdio: ['pipe', 'pipe', 'pipe'], detached: true });
const owned = registry.lldb = { child, pid: child.pid, spawnedByPid: process.pid, exitResult: null, exit: null, watchdog: null };
owned.exit = new Promise((resolve) => {
  child.once('error', (error) => {
    supervisorError ??= `LLDB child error: ${error.message}`;
    if (!owned.exitResult) owned.exitResult = { code: null, signal: null, error: error.message, at: new Date().toISOString() };
    exitResult = owned.exitResult;
    resolve(owned.exitResult);
  });
  child.once('exit', (code, signal) => {
    if (!owned.exitResult) owned.exitResult = { code, signal, error: null, at: new Date().toISOString() };
    exitResult = owned.exitResult;
    resolve(owned.exitResult);
  });
});
owned.watchdog = setTimeout(() => {
  if (owned.exitResult || child.exitCode !== null || child.signalCode !== null) return;
  try {
    const proof = identity('C735', 'C736', initialIdentity);
    watchdogRecord = { fired: true, mode: 'C737_IDENTITY_GUARDED_SIGKILL', proof, at: new Date().toISOString() };
    if (!child.kill('SIGKILL')) throw new Error('C737 SIGKILL rejected');
  } catch (error) {
    supervisorError ??= error instanceof Error ? error.message : String(error);
    if (!directHandleFailsafe('watchdog identity probe failed')) supervisorError += '; C726 fail-safe signal rejected';
  }
}, Math.max(0, 149000 - (performance.now() - spawnOriginMonotonicMs)));

if (!Number.isInteger(child.pid) || child.pid <= 0) {
  supervisorError = 'LLDB PID missing';
  directHandleFailsafe('spawn returned invalid PID');
}
try {
  writeFileSync(`${PROTOCOL}/lldb-spawn-attempt.json`, `${JSON.stringify({ schema: 'chirality-dapp92-lldb-spawn-attempt-r4/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid, spawnOriginMonotonicMs }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
} catch (error) {
  supervisorError ??= `C740 spawn-attempt receipt failed: ${error instanceof Error ? error.message : String(error)}`;
  directHandleFailsafe('spawn-attempt receipt failed');
}

child.stdout.on('data', (chunk) => { writeFileSync(stdoutFd, chunk); output.stdout.push(Buffer.from(chunk)); });
child.stderr.on('data', (chunk) => { writeFileSync(stderrFd, chunk); output.stderr.push(Buffer.from(chunk)); });

process.on('SIGINT', () => {
  interruptCount += 1;
  if (interruptCount !== 1) {
    supervisorError ??= 'duplicate C197 ETX/SIGINT rejected';
    child.stdin.destroy();
    return;
  }
  try {
    const proof = identity('C732', 'C733', initialIdentity);
    if (!child.kill('SIGINT')) throw new Error('C734 SIGINT rejected');
    writeFileSync(`${PROTOCOL}/c197-interrupt.json`, `${JSON.stringify({ schema: 'chirality-dapp92-c197-interrupt-r4/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid, proof }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
  } catch (error) {
    supervisorError ??= error instanceof Error ? error.message : String(error);
    child.stdin.destroy();
  }
});

process.stdin.on('data', (chunk) => {
  if (inputRejected || inputForwarded) {
    inputRejected = true;
    supervisorError ??= 'extra C197 stdin bytes rejected';
    child.stdin.destroy();
    return;
  }
  const bytes = Buffer.from(chunk);
  inputChunks.push(bytes);
  inputLength += bytes.length;
  if (inputLength > expectedInput.length) {
    inputRejected = true;
    supervisorError ??= 'oversize C197 stdin rejected';
    child.stdin.destroy();
    return;
  }
  const buffered = Buffer.concat(inputChunks, inputLength);
  if (!expectedInput.subarray(0, buffered.length).equals(buffered)) {
    inputRejected = true;
    supervisorError ??= 'non-prefix C197 stdin rejected';
    child.stdin.destroy();
  }
});

process.stdin.on('end', () => {
  const buffered = Buffer.concat(inputChunks, inputLength);
  writeFileSync(inputFd, buffered);
  if (inputRejected || interruptCount !== 1 || !buffered.equals(expectedInput)) {
    inputRejected = true;
    supervisorError ??= 'C197 input was not one ETX plus exact detach/quit bytes';
    child.stdin.destroy();
    return;
  }
  inputForwarded = true;
  child.stdin.end(expectedInput);
});

let terminal;
try {
  await new Promise((resolve) => setTimeout(resolve, 40));
  if (!exitResult) {
    initialIdentity = identity('C730', 'C731');
    writeFileSync(`${PROTOCOL}/lldb-start.json`, `${JSON.stringify({ schema: 'chirality-dapp92-lldb-start-r4/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid, lldbIdentity: initialIdentity, spawnOriginMonotonicMs }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
  }
  terminal = await owned.exit;
  if (watchdogRecord.fired) {
    const remaining = Math.max(0, 149900 - (performance.now() - spawnOriginMonotonicMs));
    if (remaining === 0 && !exitResult) throw new Error('LLDB not terminal by spawn +149.9 seconds');
    if (!exitResult) terminal = await Promise.race([owned.exit, new Promise((_, reject) => setTimeout(() => reject(new Error('LLDB not terminal by spawn +149.9 seconds')), remaining))]);
  }
} catch (error) {
  supervisorError ??= error instanceof Error ? error.message : String(error);
  if (!exitResult) directHandleFailsafe('supervisor terminal-path exception');
  const remaining = Math.max(0, 149900 - (performance.now() - spawnOriginMonotonicMs));
  terminal = exitResult ?? await Promise.race([owned.exit, new Promise((_, reject) => setTimeout(() => reject(new Error('LLDB fail-safe did not terminate by spawn +149.9 seconds')), remaining))]);
} finally {
  if (exitResult) clearTimeout(owned.watchdog);
  closeSync(stdoutFd);
  closeSync(stderrFd);
  closeSync(inputFd);
}

const stdoutBytes = Buffer.concat(output.stdout);
const stderrBytes = Buffer.concat(output.stderr);
const inputBytes = Buffer.concat(inputChunks, inputLength);
const exactDetach = stdoutBytes.toString('utf8').includes(`Process ${targetPid} detached`);
const terminalState = !initialIdentity ? 'LLDB_TERMINAL_BEFORE_ATTACH_OBSERVED' : watchdogRecord.fired ? 'FORCED_WATCHDOG_TERMINAL' : 'NORMAL_TERMINAL';
const sha256 = (bytes) => createHash('sha256').update(bytes).digest('hex');
writeFileSync(`${PROTOCOL}/lldb-terminal.json`, `${JSON.stringify({
  schema: 'chirality-dapp92-lldb-terminal-r4/v1', sessionId, supervisorPid: process.pid,
  targetPid, lldbPid: child.pid, spawnOriginMonotonicMs, elapsedMs: performance.now() - spawnOriginMonotonicMs,
  lldbIdentity: initialIdentity, terminalState, exit: terminal, watchdog: watchdogRecord,
  interruptCount, inputForwarded, inputRejected, exactDetachOutputObserved: exactDetach,
  inputSha256: sha256(inputBytes), stdoutSha256: sha256(stdoutBytes), stderrSha256: sha256(stderrBytes), supervisorError
}, null, 2)}\n`, { flag: 'wx', mode: 0o600 });

if (performance.now() - spawnOriginMonotonicMs > 149900 || !exitResult) process.exitCode = 3;
else if (terminalState === 'NORMAL_TERMINAL' && !(interruptCount === 1 && inputForwarded && !inputRejected && exactDetach && terminal.code === 0 && terminal.signal === null && supervisorError === null)) process.exitCode = 2;
else if (terminalState === 'LLDB_TERMINAL_BEFORE_ATTACH_OBSERVED' && supervisorError !== null) process.exitCode = 1;
else if (terminalState === 'FORCED_WATCHDOG_TERMINAL') process.exitCode = 1;
