import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const receiptPath = `${EVIDENCE}/session-terminal-receipt-r4.json`;
const receipt = JSON.parse(readFileSync(receiptPath, 'utf8'));
const digest = (file) => createHash('sha256').update(readFileSync(file)).digest('hex');
if (receipt.schema !== 'chirality-dapp92-session-terminal-receipt-r4/v1') throw new Error('receipt schema mismatch');
const noSession = receipt.branch === 'PRE_CONTROLLER_NO_SESSION_B' || receipt.branch === 'CONTROLLER_NO_LLDB_SPAWN';
let proof;
if (noSession) {
  if (receipt.sessionB?.state !== 'ABSENT' || receipt.spawnAttemptPresent || receipt.startPresent || receipt.terminalPresent) throw new Error('dishonest no-session receipt');
  proof = { state: receipt.branch, sessionB: 'ABSENT', receiptSha256: digest(receiptPath) };
} else {
  const terminalPath = `${PROTOCOL}/lldb-terminal.json`;
  const terminal = JSON.parse(readFileSync(terminalPath, 'utf8'));
  const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
  if (terminal.supervisorError !== null || receipt.supervisorError !== null || terminal.elapsedMs > 149900 || terminal.targetPid !== controller.directChildPid) throw new Error('terminal safety binding failed');
  if (receipt.sessionId !== terminal.sessionId || receipt.supervisorPid !== terminal.supervisorPid || receipt.lldbPid !== terminal.lldbPid || receipt.targetPid !== terminal.targetPid || receipt.spawnAttemptSha256 !== digest(`${PROTOCOL}/lldb-spawn-attempt.json`) || receipt.terminalSha256 !== digest(terminalPath) || receipt.inputSha256 !== digest(`${EVIDENCE}/c197.input.bin`) || receipt.stdoutSha256 !== digest(`${EVIDENCE}/lldb.stdout.bin`) || receipt.stderrSha256 !== digest(`${EVIDENCE}/lldb.stderr.bin`) || JSON.stringify(receipt.exactExit) !== JSON.stringify(terminal.exit)) throw new Error('terminal receipt byte/session mismatch');
  if (receipt.branch === 'LLDB_TERMINAL_BEFORE_ATTACH') {
    if (existsSync(`${PROTOCOL}/lldb-start.json`) || terminal.lldbIdentity !== null || terminal.terminalState !== 'LLDB_TERMINAL_BEFORE_ATTACH_OBSERVED') throw new Error('early terminal not proved');
  } else {
    const startPath = `${PROTOCOL}/lldb-start.json`;
    const start = JSON.parse(readFileSync(startPath, 'utf8'));
    if (receipt.lldbStartSha256 !== digest(startPath) || start.sessionId !== terminal.sessionId || start.supervisorPid !== terminal.supervisorPid || start.lldbPid !== terminal.lldbPid || start.targetPid !== terminal.targetPid || start.lldbIdentity.start !== receipt.lldbStart) throw new Error('LLDB start/session binding failed');
    if (receipt.branch === 'NORMAL_EXACT_DETACH') {
      const exactInput = Buffer.from('process detach\nquit\n');
      if (receipt.toolExit !== 0 || terminal.exit.code !== 0 || terminal.exit.signal !== null || terminal.interruptCount !== 1 || !terminal.inputForwarded || terminal.inputRejected || digest(`${EVIDENCE}/c197.input.bin`) !== createHash('sha256').update(exactInput).digest('hex') || !terminal.exactDetachOutputObserved || !readFileSync(`${EVIDENCE}/lldb.stdout.bin`, 'utf8').includes(`Process ${terminal.targetPid} detached`)) throw new Error('exact normal detach proof failed');
    } else if (receipt.branch === 'FORCED_WATCHDOG_TERMINAL') {
      if (terminal.exit.signal !== 'SIGKILL' || terminal.watchdog?.fired !== true || !['C737_IDENTITY_GUARDED_SIGKILL', 'C738_DIRECT_CHILD_HANDLE_FAILSAFE'].includes(terminal.watchdog.mode)) throw new Error('forced terminal proof failed');
    } else throw new Error('unknown terminal branch');
  }
  proof = { state: receipt.branch, sessionId: terminal.sessionId, supervisorPid: terminal.supervisorPid, lldbPid: terminal.lldbPid, targetPid: terminal.targetPid, receiptSha256: digest(receiptPath), terminalSha256: digest(terminalPath), exactExit: terminal.exit };
}
writeFileSync(`${PROTOCOL}/session-terminal-proof.json`, `${JSON.stringify({ schema: 'chirality-dapp92-session-terminal-proof-r4/v1', ...proof }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
writeFileSync(`${PROTOCOL}/cleanup-permission.json`, `${JSON.stringify({ schema: 'chirality-dapp92-cleanup-permission-r4/v1', branch: receipt.branch, proofSha256: digest(`${PROTOCOL}/session-terminal-proof.json`) }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
