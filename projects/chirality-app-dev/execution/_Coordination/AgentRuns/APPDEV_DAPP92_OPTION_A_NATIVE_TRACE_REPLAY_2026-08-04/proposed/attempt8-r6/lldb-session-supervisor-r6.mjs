import { closeSync, openSync, readFileSync, writeFileSync } from 'node:fs';
import { spawn, spawnSync } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';
import { performance } from 'node:perf_hooks';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const TRACE = '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt';
const EXPECTED_HELPER = '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service';
const targetPid = Number(process.argv[2]);
const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
const attachIntent = JSON.parse(readFileSync(`${PROTOCOL}/attach-intent.json`, 'utf8'));

const expectedInput = Buffer.from('process detach\nquit\n', 'utf8');
const sessionId = randomUUID();
const output = { stdout: [], stderr: [] };
const inputChunks = [];
const callbackErrors = [];
let inputLength = 0;
let inputForwarded = false;
let inputRejected = false;
let inputWriteCompleted = false;
let interruptCount = 0;
let acceptedInterrupt = null;
let interruptReceiptWritten = false;
let supervisorError = null;
let closeResult = null;
let childErrorEvent = null;
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
function targetIdentityGuard() {
  if (controller.schema !== 'chirality-dapp92-real-runtime-controller-r6/v1' || controller.state !== 'ATTACH_READY' || targetPid !== controller.directChildPid || controller.controllerPid !== controller.helperIdentity?.ppid || controller.helperExecutable !== EXPECTED_HELPER || controller.helperIdentity?.pid !== targetPid || controller.helperIdentity?.executable !== EXPECTED_HELPER) throw new Error('C992 controller binding mismatch');
  if (attachIntent.schema !== 'chirality-dapp92-real-runtime-sentinel-r6/v1' || attachIntent.state !== 'LLDB_ATTACH_INTENT_RECORDED' || attachIntent.directChildPid !== targetPid || attachIntent.controllerPid !== controller.controllerPid || attachIntent.psAction !== 'C986' || attachIntent.lsofAction !== 'C987' || JSON.stringify(attachIntent.helperIdentity) !== JSON.stringify(controller.helperIdentity)) throw new Error('C992 attach-intent binding mismatch');
  const ps = capture('C993', '/bin/ps', ['-o', 'pid=', '-o', 'ppid=', '-o', 'lstart=', '-o', 'comm=', '-p', String(targetPid)], 120);
  const match = ps.match(/^\s*(\d+)\s+(\d+)\s+(\S+\s+\S+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+(.+?)\s*$/);
  const lsof = capture('C994', '/usr/sbin/lsof', ['-a', '-p', String(targetPid), '-d', 'txt', '-Fn'], 120);
  if (!match || Number(match[1]) !== targetPid || Number(match[2]) !== controller.controllerPid || match[3] !== controller.helperIdentity.start || match[4] !== EXPECTED_HELPER || !lsof.split('\n').includes(`n${EXPECTED_HELPER}`)) throw new Error('C992-C994 immediate target identity mismatch');
  return { pid: targetPid, ppid: controller.controllerPid, start: match[3], command: match[4], executable: EXPECTED_HELPER };
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
  writeFileSync(`${PROTOCOL}/lldb-start.json`, `${JSON.stringify({ schema: 'chirality-dapp92-lldb-start-r6/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid, lldbIdentity: identityValue, spawnOriginMonotonicMs }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
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

let targetGuard;
try {
  const proof = targetIdentityGuard();
  targetGuard = { schema: 'chirality-dapp92-target-identity-guard-r6/v1', state: 'PASSED_IMMEDIATELY_BEFORE_LLDB_SPAWN', ownerActionId: 'C847', internalActionId: 'C992', controllerPid: controller.controllerPid, targetPid, attachIntentState: attachIntent.state, proof };
  writeFileSync(`${PROTOCOL}/target-identity-guard.json`, `${JSON.stringify(targetGuard, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
} catch (error) {
  const failure = { schema: 'chirality-dapp92-target-identity-guard-r6/v1', state: 'FAILED_CLOSED_NO_LLDB_SPAWN', ownerActionId: 'C847', internalActionId: 'C992', controllerPid: controller.controllerPid ?? null, targetPid, error: error instanceof Error ? error.message : String(error) };
  writeFileSync(`${PROTOCOL}/target-identity-guard.json`, `${JSON.stringify(failure, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
  process.exit(5);
}
const spawnOriginMonotonicMs = performance.now();
const child = spawn('/usr/bin/xcrun', ['lldb', '--batch', '-p', String(targetPid), '-s', TRACE], { stdio: ['pipe', 'pipe', 'pipe'], detached: false });
const closed = new Promise((resolve) => {
  child.once('error', (error) => { try { childErrorEvent = { message: error.message, at: new Date().toISOString() }; noteError('LLDB child error without terminal close', error); } catch (callbackError) { noteError('error observer', callbackError); } });
  child.once('close', (code, signal) => { try { closeResult = { code, signal, error: childErrorEvent?.message ?? null, observedEvent: 'close', streamsDrained: true, at: new Date().toISOString() }; resolve(closeResult); } catch (callbackError) { noteError('close observer', callbackError); closeResult = { code, signal, error: callbackError.message, observedEvent: 'close', streamsDrained: true, at: new Date().toISOString() }; resolve(closeResult); } });
});
const watchdogTimer = setTimeout(() => {
  try {
    const proof = identityGuardedSignal('SIGKILL', 'C1016', 'C1017', 'C1018', true);
    watchdogRecord = { fired: true, mode: 'C1018_IDENTITY_GUARDED_SIGKILL', signalAccepted: true, proof, at: new Date().toISOString() };
  } catch (error) {
    noteError('watchdog unsafe to signal', error);
    watchdogRecord = { fired: true, mode: 'UNSAFE_TO_SIGNAL', signalAccepted: false, at: new Date().toISOString(), error: error instanceof Error ? error.message : String(error) };
  }
}, Math.max(0, 149000 - (performance.now() - spawnOriginMonotonicMs)));
const deadlineTimer = setTimeout(() => deadlineResolved({ deadline: true }), Math.max(0, 149900 - (performance.now() - spawnOriginMonotonicMs)));

try { writeFileSync(`${PROTOCOL}/lldb-spawn-attempt.json`, `${JSON.stringify({ schema: 'chirality-dapp92-lldb-spawn-attempt-r6/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid, spawnOriginMonotonicMs, targetGuard }, null, 2)}\n`, { flag: 'wx', mode: 0o600 }); }
catch (error) { noteError('C999 spawn-attempt receipt', error); }

child.stdout.on('data', (chunk) => { try { writeFileSync(stdoutFd, chunk); output.stdout.push(Buffer.from(chunk)); } catch (error) { noteError('C1000 stdout callback', error); try { child.stdout.destroy(); } catch (destroyError) { noteError('stdout destroy', destroyError); } } });
child.stderr.on('data', (chunk) => { try { writeFileSync(stderrFd, chunk); output.stderr.push(Buffer.from(chunk)); } catch (error) { noteError('C1001 stderr callback', error); try { child.stderr.destroy(); } catch (destroyError) { noteError('stderr destroy', destroyError); } } });

function onSupervisorSigint() {
  try {
    interruptCount += 1;
    if (interruptCount !== 1) throw new Error('duplicate newly requested supervisor SIGINT rejected');
    const proof = identityGuardedSignal('SIGINT', 'C1007', 'C1008', 'C1009');
    acceptedInterrupt = { actionId: 'C1009', proof, acceptedAt: new Date().toISOString() };
    writeFileSync(`${PROTOCOL}/c197-interrupt.json`, `${JSON.stringify({ schema: 'chirality-dapp92-new-interrupt-r6/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid, actionId: 'C1009', proof }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
    interruptReceiptWritten = true;
  } catch (error) { noteError('C1006/C1009 SIGINT callback', error); try { child.stdin.destroy(); } catch (destroyError) { noteError('stdin destroy', destroyError); } }
}
function onStdinData(chunk) {
  try {
    if (inputRejected || inputForwarded) throw new Error('extra newly requested stdin bytes rejected');
    const bytes = Buffer.from(chunk); inputChunks.push(bytes); inputLength += bytes.length;
    if (inputLength > expectedInput.length) throw new Error('oversize stdin rejected');
    const buffered = Buffer.concat(inputChunks, inputLength);
    if (!expectedInput.subarray(0, buffered.length).equals(buffered)) throw new Error('non-prefix stdin rejected');
  } catch (error) { inputRejected = true; noteError('C1011 stdin data callback', error); try { child.stdin.destroy(); } catch (destroyError) { noteError('stdin destroy', destroyError); } }
}
function onStdinEnd() {
  try {
    const buffered = Buffer.concat(inputChunks, inputLength); writeFileSync(inputFd, buffered);
    if (inputRejected || interruptCount !== 1 || acceptedInterrupt?.actionId !== 'C1009' || !interruptReceiptWritten || !buffered.equals(expectedInput)) throw new Error('new input sequence lacks one accepted C1009 signal, its receipt, or exact detach/quit bytes');
    child.stdin.end(expectedInput, () => { try { inputWriteCompleted = true; } catch (error) { inputRejected = true; noteError('C1015 stdin completion callback', error); } });
    inputForwarded = true;
  } catch (error) { inputRejected = true; noteError('C1012/C1014 stdin EOF callback', error); try { child.stdin.destroy(); } catch (destroyError) { noteError('stdin destroy', destroyError); } }
}
function onChildStdinError(error) { inputRejected = true; noteError('C1013 child stdin stream error', error); }
process.on('SIGINT', onSupervisorSigint);
process.stdin.on('data', onStdinData);
process.stdin.on('end', onStdinEnd);
child.stdin.on('error', onChildStdinError);

try {
  await Promise.race([new Promise((resolve) => setTimeout(resolve, 40)), closed]);
  if (!closeResult) {
    const observedIdentity = identity('C1003', 'C1004');
    writeStartReceipt(observedIdentity);
    initialIdentity = observedIdentity;
  }
} catch (error) { noteError('C1002-C1005 start observation', error); }

const absolute = await Promise.race([closed.then((terminal) => ({ terminal })), terminalDeadline]);
clearTimeout(deadlineTimer);
if (absolute.terminal) clearTimeout(watchdogTimer);
process.removeListener('SIGINT', onSupervisorSigint);
process.stdin.removeListener('data', onStdinData);
process.stdin.removeListener('end', onStdinEnd);
child.stdin.removeListener('error', onChildStdinError);
process.stdin.pause();
listenersRemoved = true;
finalizationActions.push('C1060');
const terminalObserved = Boolean(absolute.terminal);
const noCloseState = watchdogRecord.mode === 'C1018_IDENTITY_GUARDED_SIGKILL' && watchdogRecord.signalAccepted === true ? 'WATCHDOG_SIGNAL_ACCEPTED_NO_CLOSE_AT_DEADLINE' : 'UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE';
if (!terminalObserved) finalizationActions.push('C1019');
const terminal = absolute.terminal ?? { code: null, signal: null, error: noCloseState, observedEvent: null, streamsDrained: false, at: new Date().toISOString() };
const elapsedMs = performance.now() - spawnOriginMonotonicMs;
const stdoutBytes = Buffer.concat(output.stdout); const stderrBytes = Buffer.concat(output.stderr); const inputBytes = Buffer.concat(inputChunks, inputLength);
let terminalState;
if (!terminalObserved) terminalState = noCloseState;
else if (watchdogRecord.fired && watchdogRecord.mode === 'C1018_IDENTITY_GUARDED_SIGKILL' && terminal.signal === 'SIGKILL') terminalState = 'FORCED_WATCHDOG_TERMINAL';
else if (watchdogRecord.fired && watchdogRecord.mode === 'C1018_IDENTITY_GUARDED_SIGKILL') terminalState = 'WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL';
else if (!initialIdentity) terminalState = 'LLDB_TERMINAL_BEFORE_ATTACH_OBSERVED';
else if (interruptCount === 1 && acceptedInterrupt?.actionId === 'C1009' && interruptReceiptWritten && inputForwarded && inputWriteCompleted && !inputRejected && stdoutBytes.toString('utf8').includes(`Process ${targetPid} detached`) && terminal.code === 0 && terminal.signal === null && terminal.observedEvent === 'close' && terminal.streamsDrained === true && supervisorError === null) terminalState = 'NORMAL_EXACT_DETACH';
else terminalState = 'POST_START_ABNORMAL_LLDB_TERMINAL';
closeSync(stdoutFd); closeSync(stderrFd); closeSync(inputFd);
finalizationActions.push('C1061');
const sha256 = (bytes) => createHash('sha256').update(bytes).digest('hex');
finalizationActions.push('C1062');
writeFileSync(`${PROTOCOL}/lldb-terminal.json`, `${JSON.stringify({
  schema: 'chirality-dapp92-lldb-terminal-r6/v1', sessionId, supervisorPid: process.pid, targetPid, lldbPid: child.pid,
  spawnOriginMonotonicMs, elapsedMs, lldbIdentity: initialIdentity, terminalState, terminalObserved, exit: terminal,
	  watchdog: watchdogRecord, interruptCount, acceptedInterrupt, interruptReceiptWritten, inputForwarded, inputWriteCompleted, inputRejected, childErrorEvent,
  listenersRemoved, finalizationActions, finalExitAction: 'C1066',
  exactDetachOutputObserved: stdoutBytes.toString('utf8').includes(`Process ${targetPid} detached`),
  inputSha256: sha256(inputBytes), stdoutSha256: sha256(stdoutBytes), stderrSha256: sha256(stderrBytes), supervisorError, callbackErrors
}, null, 2)}\n`, { flag: 'wx', mode: 0o600 });

if (!terminalObserved) process.exit(4);
if (terminalState === 'NORMAL_EXACT_DETACH') process.exit(0);
process.exit(1);
