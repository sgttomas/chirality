import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const PROTOCOL = `${ROOT}/protocol`;
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const branch = process.argv[2];
const toolExit = process.argv[3] === 'NONE' ? null : Number(process.argv[3]);
const allowed = new Set(['PRE_CONTROLLER_NO_SESSION_B', 'CONTROLLER_NO_LLDB_SPAWN', 'LLDB_TERMINAL_BEFORE_ATTACH', 'POST_START_ABNORMAL_LLDB_TERMINAL', 'NORMAL_EXACT_DETACH', 'FORCED_WATCHDOG_TERMINAL', 'WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL', 'UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE']);
if (!allowed.has(branch) || (toolExit !== null && !Number.isInteger(toolExit))) throw new Error('exact branch and typed tool exit required');
const present = (name) => existsSync(`${PROTOCOL}/${name}`);
const read = (name) => JSON.parse(readFileSync(`${PROTOCOL}/${name}`, 'utf8'));
const digest = (file) => createHash('sha256').update(readFileSync(file)).digest('hex');
const controllerPresent = present('controller.json');
const attachIntentPresent = present('attach-intent.json');
const spawnAttemptPresent = present('lldb-spawn-attempt.json');
const startPresent = present('lldb-start.json');
const terminalPresent = present('lldb-terminal.json');
let receipt = { schema: 'chirality-dapp92-session-terminal-receipt-r5/v1', branch, controllerPresent, attachIntentPresent, spawnAttemptPresent, startPresent, terminalPresent, toolExit };

if (branch === 'PRE_CONTROLLER_NO_SESSION_B') {
  if (controllerPresent || attachIntentPresent || spawnAttemptPresent || startPresent || terminalPresent || toolExit !== null) throw new Error('pre-controller branch contradiction');
  receipt.sessionB = { state: 'ABSENT', reason: 'CONTROLLER_RECORD_NOT_CREATED' };
} else if (branch === 'CONTROLLER_NO_LLDB_SPAWN') {
  if (!controllerPresent || spawnAttemptPresent || startPresent || terminalPresent || toolExit !== null) throw new Error('controller/no-LLDB branch contradiction');
  receipt.sessionB = { state: 'ABSENT', reason: attachIntentPresent ? 'ATTACH_INTENT_RECORDED_BUT_SUPERVISOR_NOT_STARTED' : 'ATTACH_INTENT_NOT_RECORDED' };
} else {
  if (!controllerPresent || !attachIntentPresent || !spawnAttemptPresent || !terminalPresent || toolExit === null) throw new Error('LLDB branch artifacts missing');
  const terminal = read('lldb-terminal.json'); const spawnAttempt = read('lldb-spawn-attempt.json');
  if (terminal.schema !== 'chirality-dapp92-lldb-terminal-r5/v1' || spawnAttempt.schema !== 'chirality-dapp92-lldb-spawn-attempt-r5/v1') throw new Error('session schema mismatch');
  if (terminal.sessionId !== spawnAttempt.sessionId || terminal.supervisorPid !== spawnAttempt.supervisorPid || terminal.targetPid !== spawnAttempt.targetPid || terminal.lldbPid !== spawnAttempt.lldbPid) throw new Error('session identity mismatch');
  receipt = { ...receipt, sessionId: terminal.sessionId, supervisorPid: terminal.supervisorPid, targetPid: terminal.targetPid, lldbPid: terminal.lldbPid, lldbStart: terminal.lldbIdentity?.start ?? null, spawnAttemptSha256: digest(`${PROTOCOL}/lldb-spawn-attempt.json`), lldbStartSha256: startPresent ? digest(`${PROTOCOL}/lldb-start.json`) : null, terminalSha256: digest(`${PROTOCOL}/lldb-terminal.json`), inputSha256: digest(`${EVIDENCE}/c197.input.bin`), stdoutSha256: digest(`${EVIDENCE}/lldb.stdout.bin`), stderrSha256: digest(`${EVIDENCE}/lldb.stderr.bin`), exactExit: terminal.exit, terminalState: terminal.terminalState, terminalObserved: terminal.terminalObserved, listenersRemoved: terminal.listenersRemoved, supervisorError: terminal.supervisorError, callbackErrors: terminal.callbackErrors, exactDetachOutputObserved: terminal.exactDetachOutputObserved };
  const expected = {
    LLDB_TERMINAL_BEFORE_ATTACH: ['LLDB_TERMINAL_BEFORE_ATTACH_OBSERVED', false, true],
    POST_START_ABNORMAL_LLDB_TERMINAL: ['POST_START_ABNORMAL_LLDB_TERMINAL', true, true],
    NORMAL_EXACT_DETACH: ['NORMAL_EXACT_DETACH', true, true],
    FORCED_WATCHDOG_TERMINAL: ['FORCED_WATCHDOG_TERMINAL', true, true],
    WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL: ['WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL', true, true],
    UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE: ['UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE', null, false]
  }[branch];
  if (!expected || terminal.terminalState !== expected[0] || (expected[1] !== null && startPresent !== expected[1]) || terminal.terminalObserved !== expected[2]) throw new Error('terminal branch contradiction');
}
writeFileSync(`${EVIDENCE}/session-terminal-receipt-r5.json`, `${JSON.stringify(receipt, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
