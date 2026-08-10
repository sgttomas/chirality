import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const receiptPath = `${EVIDENCE}/session-terminal-receipt-r5.json`;
const receipt = JSON.parse(readFileSync(receiptPath, 'utf8'));
const digest = (file) => createHash('sha256').update(readFileSync(file)).digest('hex');
if (receipt.schema !== 'chirality-dapp92-session-terminal-receipt-r5/v1') throw new Error('receipt schema mismatch');
const noSession = receipt.branch === 'PRE_CONTROLLER_NO_SESSION_B' || receipt.branch === 'CONTROLLER_NO_LLDB_SPAWN';
let proof;
if (noSession) {
  if (receipt.sessionB?.state !== 'ABSENT' || receipt.spawnAttemptPresent || receipt.startPresent || receipt.terminalPresent) throw new Error('dishonest no-session receipt');
  proof = { state: receipt.branch, sessionB: 'ABSENT', terminalSafeForCleanup: true, receiptSha256: digest(receiptPath) };
} else {
  const terminalPath = `${PROTOCOL}/lldb-terminal.json`; const terminal = JSON.parse(readFileSync(terminalPath, 'utf8')); const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
  if (terminal.elapsedMs > 150000 || terminal.targetPid !== controller.directChildPid || terminal.listenersRemoved !== true || receipt.listenersRemoved !== true) throw new Error('terminal deadline/target/listener-teardown binding failed');
  if (receipt.sessionId !== terminal.sessionId || receipt.supervisorPid !== terminal.supervisorPid || receipt.lldbPid !== terminal.lldbPid || receipt.targetPid !== terminal.targetPid || receipt.spawnAttemptSha256 !== digest(`${PROTOCOL}/lldb-spawn-attempt.json`) || receipt.terminalSha256 !== digest(terminalPath) || receipt.inputSha256 !== digest(`${EVIDENCE}/c197.input.bin`) || receipt.stdoutSha256 !== digest(`${EVIDENCE}/lldb.stdout.bin`) || receipt.stderrSha256 !== digest(`${EVIDENCE}/lldb.stderr.bin`) || JSON.stringify(receipt.exactExit) !== JSON.stringify(terminal.exit)) throw new Error('terminal receipt byte/session mismatch');
  if (receipt.branch === 'LLDB_TERMINAL_BEFORE_ATTACH') {
    if (existsSync(`${PROTOCOL}/lldb-start.json`) || terminal.lldbIdentity !== null || !terminal.terminalObserved) throw new Error('early terminal not proved');
  } else if (receipt.branch !== 'UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE' || receipt.startPresent) {
    const startPath = `${PROTOCOL}/lldb-start.json`; const start = JSON.parse(readFileSync(startPath, 'utf8'));
    if (receipt.lldbStartSha256 !== digest(startPath) || start.sessionId !== terminal.sessionId || start.supervisorPid !== terminal.supervisorPid || start.lldbPid !== terminal.lldbPid || start.targetPid !== terminal.targetPid || start.lldbIdentity.start !== receipt.lldbStart) throw new Error('LLDB start/session binding failed');
  }
  if (receipt.branch === 'NORMAL_EXACT_DETACH') {
    const exactInput = Buffer.from('process detach\nquit\n');
    if (receipt.toolExit !== 0 || terminal.exit.code !== 0 || terminal.exit.signal !== null || terminal.interruptCount !== 1 || !terminal.inputForwarded || terminal.inputRejected || digest(`${EVIDENCE}/c197.input.bin`) !== createHash('sha256').update(exactInput).digest('hex') || !terminal.exactDetachOutputObserved || terminal.supervisorError !== null || terminal.callbackErrors.length !== 0) throw new Error('exact normal detach proof failed');
  } else if (receipt.branch === 'FORCED_WATCHDOG_TERMINAL') {
    if (!terminal.terminalObserved || terminal.exit.signal !== 'SIGKILL' || terminal.watchdog?.mode !== 'C1010_IDENTITY_GUARDED_SIGKILL' || terminal.watchdog?.signalAccepted !== true) throw new Error('forced terminal proof failed');
  } else if (receipt.branch === 'WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL') {
    if (!terminal.terminalObserved || terminal.exit.signal === 'SIGKILL' || terminal.watchdog?.mode !== 'C1010_IDENTITY_GUARDED_SIGKILL' || terminal.watchdog?.signalAccepted !== true) throw new Error('watchdog accepted/race terminal proof failed');
  } else if (receipt.branch === 'POST_START_ABNORMAL_LLDB_TERMINAL') {
    if (!terminal.terminalObserved || terminal.terminalState !== 'POST_START_ABNORMAL_LLDB_TERMINAL') throw new Error('abnormal terminal proof failed');
  } else if (receipt.branch === 'UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE') {
    if (terminal.terminalObserved || terminal.watchdog?.mode !== 'UNSAFE_TO_SIGNAL' || terminal.watchdog?.signalAccepted !== false || (receipt.startPresent && terminal.lldbIdentity === null) || (!receipt.startPresent && terminal.lldbIdentity !== null)) throw new Error('unsafe-to-signal deadline proof failed');
  } else if (receipt.branch !== 'LLDB_TERMINAL_BEFORE_ATTACH') throw new Error('unknown terminal branch');
  proof = { state: receipt.branch, sessionId: terminal.sessionId, supervisorPid: terminal.supervisorPid, lldbPid: terminal.lldbPid, targetPid: terminal.targetPid, terminalSafeForCleanup: terminal.terminalObserved, lldbMaximum150SecondsProved: terminal.terminalObserved && terminal.elapsedMs <= 150000, diagnosticFailure: terminal.terminalObserved ? null : 'LLDB_MAXIMUM_NOT_PROVED_IDENTITY_UNSAFE', receiptSha256: digest(receiptPath), terminalSha256: digest(terminalPath), exactExit: terminal.exit };
}
writeFileSync(`${PROTOCOL}/session-terminal-proof.json`, `${JSON.stringify({ schema: 'chirality-dapp92-session-terminal-proof-r5/v1', ...proof }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
if (!proof.terminalSafeForCleanup) process.exit(4);
writeFileSync(`${PROTOCOL}/cleanup-permission.json`, `${JSON.stringify({ schema: 'chirality-dapp92-cleanup-permission-r5/v1', branch: receipt.branch, proofSha256: digest(`${PROTOCOL}/session-terminal-proof.json`) }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
