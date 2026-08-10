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
if (controller.schema !== 'chirality-dapp92-real-runtime-controller-r5/v1' || targetPid !== controller.directChildPid) throw new Error('controller/PID mismatch');

const expectedInput = Buffer.from('process detach\nquit\n', 'utf8');
const sessionId = randomUUID();
const output = { stdout: [], stderr: [] };
const inputChunks = [];
const callbackErrors = [];
let inputLength = 0;
let inputForwarded = false;
let inputRejected = false;
let interruptCount = 0;
let supervisorError = null;
let closeResult = null;
let initialIdentity = null;
let watchdogRecord = { fired: false, mode: null };
let listenersRemoved = false;
const finalizationActions = [];
let deadlineResolved;
const terminalDeadline = new Promise((resolve) => { deadlineResolved = resolve; });
const stdoutFd = openSync(`${EVIDENCE}/lldb.stdout.bin`, 'wx', 0o600);
const stderrFd = openSync(`${EVIDENCE}/lldb.stderr.bin`, 'wx', 0o600);
const inputFd = openSync(`${EVIDENCE}/c197.input.bin`, 'wx', 0o600);

function noteError(prefix, error) {
  const message = `${prefix}: ${error instanceof Error ? error.message : String(error)}`;
  callbackErrors.push(message); supervisorError ??= message;
}
function capture(actionId, executable, args, timeout) {
  const result = spawnSync(executable, args, { encoding: 'utf8', timeout, maxBuffer: 1048576 });
  if (result.status !== 0 || result.signal !== null || result.error) throw new Error(`${actionId} identity probe failed`);
  return result.stdout ?? '';
}
function identity(psAction, lsofAction, baseline) {
  if (closeResult || child.exitCode !== null || child.signalCode !== null) throw new Error('LLDB child not live');
  const ps = capture(psAction, '/bin/ps', ['-o', 'pid=', '-o', 'ppid=', '-o', 'lstart=', '-o', 'comm=', '-p', String(child.pid)], 120);
  const match = ps.match(/^\s*(\d+)\s+(\d+)\s+(\S+\s+\S+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+(.+?)\s*$/);
  const lsof = capture(lsofAction, '/usr/sbin/lsof', ['-a', '-p', String(child.pid), '-d', 'txt', '-Fn'], 120);
  if (!match || Number(match[1]) !== child.pid || Number(match[2]) !== process.pid || !lsof.split('\n').some((line) => line.endsWith('/lldb'))) throw new Error('LLDB identity mismatch');
  const value = { pid: child.pid, ppid: process.pid, start: match[3], command: match[4] };
  if (baseline && (baseline.pid !== value.pid || baseline.ppid !== value.ppid || baseline.start !== value.start)) throw new Error('LLDB identity drift');
  return value;
}
function writeStartReceipt(identityValue) {
  writeFileSync(`${PROTOCOL}/lldb-start.json`, `${JSON.stringify({ schema: 'chirality-dapp92-lldb-start-r5/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid, lldbIdentity: identityValue, spawnOriginMonotonicMs }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
}
function identityGuardedSignal(signal, psAction, lsofAction, actionId, establishLateStart = false) {
  const proof = identity(psAction, lsofAction, initialIdentity);
  if (establishLateStart && !initialIdentity) {
    writeStartReceipt(proof);
    initialIdentity = proof;
  }
  if (!child.kill(signal)) throw new Error(`${actionId} ${signal} rejected`);
  return proof;
}

const spawnOriginMonotonicMs = performance.now();
const child = spawn('/usr/bin/xcrun', ['lldb', '--batch', '-p', String(targetPid), '-s', TRACE], { stdio: ['pipe', 'pipe', 'pipe'], detached: false });
const closed = new Promise((resolve) => {
  child.once('error', (error) => { try { noteError('LLDB child error', error); if (!closeResult) closeResult = { code: null, signal: null, error: error.message, at: new Date().toISOString() }; resolve(closeResult); } catch (callbackError) { noteError('error observer', callbackError); resolve({ code: null, signal: null, error: callbackError.message }); } });
  child.once('close', (code, signal) => { try { if (!closeResult) closeResult = { code, signal, error: null, at: new Date().toISOString() }; resolve(closeResult); } catch (callbackError) { noteError('close observer', callbackError); resolve({ code, signal, error: callbackError.message }); } });
});
const watchdogTimer = setTimeout(() => {
  try {
    const proof = identityGuardedSignal('SIGKILL', 'C1008', 'C1009', 'C1010', true);
    watchdogRecord = { fired: true, mode: 'C1010_IDENTITY_GUARDED_SIGKILL', signalAccepted: true, proof, at: new Date().toISOString() };
  } catch (error) {
    noteError('watchdog unsafe to signal', error);
    watchdogRecord = { fired: true, mode: 'UNSAFE_TO_SIGNAL', signalAccepted: false, at: new Date().toISOString(), error: error instanceof Error ? error.message : String(error) };
  }
}, Math.max(0, 149000 - (performance.now() - spawnOriginMonotonicMs)));
const deadlineTimer = setTimeout(() => deadlineResolved({ deadline: true }), Math.max(0, 149900 - (performance.now() - spawnOriginMonotonicMs)));

try { writeFileSync(`${PROTOCOL}/lldb-spawn-attempt.json`, `${JSON.stringify({ schema: 'chirality-dapp92-lldb-spawn-attempt-r5/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid, spawnOriginMonotonicMs }, null, 2)}\n`, { flag: 'wx', mode: 0o600 }); }
catch (error) { noteError('C993 spawn-attempt receipt', error); }

child.stdout.on('data', (chunk) => { try { writeFileSync(stdoutFd, chunk); output.stdout.push(Buffer.from(chunk)); } catch (error) { noteError('C994 stdout callback', error); try { child.stdout.destroy(); } catch (destroyError) { noteError('stdout destroy', destroyError); } } });
child.stderr.on('data', (chunk) => { try { writeFileSync(stderrFd, chunk); output.stderr.push(Buffer.from(chunk)); } catch (error) { noteError('C995 stderr callback', error); try { child.stderr.destroy(); } catch (destroyError) { noteError('stderr destroy', destroyError); } } });

function onSupervisorSigint() {
  try {
    interruptCount += 1;
    if (interruptCount !== 1) throw new Error('duplicate newly requested supervisor SIGINT rejected');
    const proof = identityGuardedSignal('SIGINT', 'C1001', 'C1002', 'C1003');
    writeFileSync(`${PROTOCOL}/c197-interrupt.json`, `${JSON.stringify({ schema: 'chirality-dapp92-new-interrupt-r5/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid, actionId: 'C1003', proof }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
  } catch (error) { noteError('C1000/C1003 SIGINT callback', error); try { child.stdin.destroy(); } catch (destroyError) { noteError('stdin destroy', destroyError); } }
}
function onStdinData(chunk) {
  try {
    if (inputRejected || inputForwarded) throw new Error('extra newly requested stdin bytes rejected');
    const bytes = Buffer.from(chunk); inputChunks.push(bytes); inputLength += bytes.length;
    if (inputLength > expectedInput.length) throw new Error('oversize stdin rejected');
    const buffered = Buffer.concat(inputChunks, inputLength);
    if (!expectedInput.subarray(0, buffered.length).equals(buffered)) throw new Error('non-prefix stdin rejected');
  } catch (error) { inputRejected = true; noteError('C1005 stdin data callback', error); try { child.stdin.destroy(); } catch (destroyError) { noteError('stdin destroy', destroyError); } }
}
function onStdinEnd() {
  try {
    const buffered = Buffer.concat(inputChunks, inputLength); writeFileSync(inputFd, buffered);
    if (inputRejected || interruptCount !== 1 || !buffered.equals(expectedInput)) throw new Error('new input sequence not exactly one supervisor SIGINT plus detach/quit bytes');
    inputForwarded = true; child.stdin.end(expectedInput);
  } catch (error) { inputRejected = true; noteError('C1006/C1007 stdin EOF callback', error); try { child.stdin.destroy(); } catch (destroyError) { noteError('stdin destroy', destroyError); } }
}
process.on('SIGINT', onSupervisorSigint);
process.stdin.on('data', onStdinData);
process.stdin.on('end', onStdinEnd);

try {
  await Promise.race([new Promise((resolve) => setTimeout(resolve, 40)), closed]);
  if (!closeResult) {
    const observedIdentity = identity('C997', 'C998');
    writeStartReceipt(observedIdentity);
    initialIdentity = observedIdentity;
  }
} catch (error) { noteError('C996-C999 start observation', error); }

const absolute = await Promise.race([closed.then((terminal) => ({ terminal })), terminalDeadline]);
clearTimeout(deadlineTimer);
if (absolute.terminal) clearTimeout(watchdogTimer);
process.removeListener('SIGINT', onSupervisorSigint);
process.stdin.removeListener('data', onStdinData);
process.stdin.removeListener('end', onStdinEnd);
process.stdin.pause();
listenersRemoved = true;
finalizationActions.push('C1051');
const terminalObserved = Boolean(absolute.terminal);
const terminal = absolute.terminal ?? { code: null, signal: null, error: 'UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE', at: new Date().toISOString() };
const elapsedMs = performance.now() - spawnOriginMonotonicMs;
const stdoutBytes = Buffer.concat(output.stdout); const stderrBytes = Buffer.concat(output.stderr); const inputBytes = Buffer.concat(inputChunks, inputLength);
let terminalState;
if (!terminalObserved) terminalState = 'UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE';
else if (watchdogRecord.fired && watchdogRecord.mode === 'C1010_IDENTITY_GUARDED_SIGKILL' && terminal.signal === 'SIGKILL') terminalState = 'FORCED_WATCHDOG_TERMINAL';
else if (watchdogRecord.fired && watchdogRecord.mode === 'C1010_IDENTITY_GUARDED_SIGKILL') terminalState = 'WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL';
else if (!initialIdentity) terminalState = 'LLDB_TERMINAL_BEFORE_ATTACH_OBSERVED';
else if (interruptCount === 1 && inputForwarded && !inputRejected && stdoutBytes.toString('utf8').includes(`Process ${targetPid} detached`) && terminal.code === 0 && terminal.signal === null && supervisorError === null) terminalState = 'NORMAL_EXACT_DETACH';
else terminalState = 'POST_START_ABNORMAL_LLDB_TERMINAL';
closeSync(stdoutFd); closeSync(stderrFd); closeSync(inputFd);
finalizationActions.push('C1052');
const sha256 = (bytes) => createHash('sha256').update(bytes).digest('hex');
finalizationActions.push('C1053');
writeFileSync(`${PROTOCOL}/lldb-terminal.json`, `${JSON.stringify({
  schema: 'chirality-dapp92-lldb-terminal-r5/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid,
  spawnOriginMonotonicMs, elapsedMs, lldbIdentity: initialIdentity, terminalState, terminalObserved, exit: terminal,
	  watchdog: watchdogRecord, interruptCount, inputForwarded, inputRejected,
  listenersRemoved, finalizationActions, finalExitAction: 'C1057',
  exactDetachOutputObserved: stdoutBytes.toString('utf8').includes(`Process ${targetPid} detached`),
  inputSha256: sha256(inputBytes), stdoutSha256: sha256(stdoutBytes), stderrSha256: sha256(stderrBytes), supervisorError, callbackErrors
}, null, 2)}\n`, { flag: 'wx', mode: 0o600 });

if (!terminalObserved) process.exit(4);
if (terminalState === 'NORMAL_EXACT_DETACH') process.exit(0);
process.exit(1);
