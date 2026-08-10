import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const branch = process.argv[2];
const toolExit = process.argv[3] === 'NONE' ? null : Number(process.argv[3]);
const allowed = new Set(['PRE_CONTROLLER_NO_SESSION_B', 'CONTROLLER_NO_LLDB_SPAWN', 'LLDB_TERMINAL_BEFORE_ATTACH', 'NORMAL_EXACT_DETACH', 'FORCED_WATCHDOG_TERMINAL']);
if (!allowed.has(branch) || (toolExit !== null && !Number.isInteger(toolExit))) throw new Error('exact branch and typed tool exit required');
const present = (name) => existsSync(`${PROTOCOL}/${name}`);
const read = (name) => JSON.parse(readFileSync(`${PROTOCOL}/${name}`, 'utf8'));
const digest = (file) => createHash('sha256').update(readFileSync(file)).digest('hex');
const controllerPresent = present('controller.json');
const attachIntentPresent = present('attach-intent.json');
const spawnAttemptPresent = present('lldb-spawn-attempt.json');
const startPresent = present('lldb-start.json');
const terminalPresent = present('lldb-terminal.json');
let receipt = { schema: 'chirality-dapp92-session-terminal-receipt-r4/v1', branch, controllerPresent, attachIntentPresent, spawnAttemptPresent, startPresent, terminalPresent, toolExit };

if (branch === 'PRE_CONTROLLER_NO_SESSION_B') {
  if (controllerPresent || attachIntentPresent || spawnAttemptPresent || startPresent || terminalPresent || toolExit !== null) throw new Error('pre-controller branch contradiction');
  receipt.sessionB = { state: 'ABSENT', reason: 'CONTROLLER_RECORD_NOT_CREATED' };
} else if (branch === 'CONTROLLER_NO_LLDB_SPAWN') {
  if (!controllerPresent || spawnAttemptPresent || startPresent || terminalPresent || toolExit !== null) throw new Error('controller/no-LLDB branch contradiction');
  receipt.sessionB = { state: 'ABSENT', reason: attachIntentPresent ? 'ATTACH_INTENT_RECORDED_BUT_SUPERVISOR_NOT_STARTED' : 'ATTACH_INTENT_NOT_RECORDED' };
} else {
  if (!controllerPresent || !attachIntentPresent || !spawnAttemptPresent || !terminalPresent || toolExit === null) throw new Error('LLDB terminal branch artifacts missing');
  const terminal = read('lldb-terminal.json');
  const spawnAttempt = read('lldb-spawn-attempt.json');
  if (terminal.schema !== 'chirality-dapp92-lldb-terminal-r4/v1' || spawnAttempt.schema !== 'chirality-dapp92-lldb-spawn-attempt-r4/v1') throw new Error('session schema mismatch');
  if (terminal.sessionId !== spawnAttempt.sessionId || terminal.supervisorPid !== spawnAttempt.supervisorPid || terminal.targetPid !== spawnAttempt.targetPid || terminal.lldbPid !== spawnAttempt.lldbPid) throw new Error('session identity mismatch');
  receipt = { ...receipt, sessionId: terminal.sessionId, supervisorPid: terminal.supervisorPid, targetPid: terminal.targetPid, lldbPid: terminal.lldbPid, lldbStart: terminal.lldbIdentity?.start ?? null, spawnAttemptSha256: digest(`${PROTOCOL}/lldb-spawn-attempt.json`), lldbStartSha256: startPresent ? digest(`${PROTOCOL}/lldb-start.json`) : null, terminalSha256: digest(`${PROTOCOL}/lldb-terminal.json`), inputSha256: digest(`${EVIDENCE}/c197.input.bin`), stdoutSha256: digest(`${EVIDENCE}/lldb.stdout.bin`), stderrSha256: digest(`${EVIDENCE}/lldb.stderr.bin`), exactExit: terminal.exit, terminalState: terminal.terminalState, supervisorError: terminal.supervisorError, exactDetachOutputObserved: terminal.exactDetachOutputObserved };
  if (branch === 'LLDB_TERMINAL_BEFORE_ATTACH' && (startPresent || terminal.terminalState !== 'LLDB_TERMINAL_BEFORE_ATTACH_OBSERVED')) throw new Error('early-terminal branch contradiction');
  if (branch === 'NORMAL_EXACT_DETACH' && (!startPresent || terminal.terminalState !== 'NORMAL_TERMINAL')) throw new Error('normal branch contradiction');
  if (branch === 'FORCED_WATCHDOG_TERMINAL' && (!startPresent || terminal.terminalState !== 'FORCED_WATCHDOG_TERMINAL')) throw new Error('forced branch contradiction');
}
writeFileSync(`${EVIDENCE}/session-terminal-receipt-r4.json`, `${JSON.stringify(receipt, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
