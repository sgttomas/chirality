import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804'; const PROTOCOL = `${ROOT}/protocol`;
const terminalReturn = `${ROOT}/evidence/attempt8-runtime/session-b-terminal-return.json`;
for (const file of [`${PROTOCOL}/attach-started.json`, `${PROTOCOL}/lldb-spawn-attempt.json`, `${PROTOCOL}/lldb-terminal.json`, terminalReturn]) if (!existsSync(file)) throw new Error(`missing ${file}`);
const terminal = JSON.parse(readFileSync(`${PROTOCOL}/lldb-terminal.json`, 'utf8'));
const controller = JSON.parse(readFileSync(`${PROTOCOL}/controller.json`, 'utf8'));
const toolReturn = JSON.parse(readFileSync(terminalReturn, 'utf8'));
const digest = (file) => createHash('sha256').update(readFileSync(file)).digest('hex');
if (
  terminal.schema !== 'chirality-dapp92-lldb-terminal-r3/v1' ||
  terminal.targetPid !== controller.directChildPid ||
  !terminal.exit ||
  toolReturn.schema !== 'chirality-dapp92-session-terminal-return-r3/v1' ||
  toolReturn.sessionRole !== 'LLDB_SUPERVISOR' ||
  toolReturn.terminal !== true ||
  toolReturn.exitCode !== 0 ||
  toolReturn.lldbTerminalSha256 !== digest(`${PROTOCOL}/lldb-terminal.json`) ||
  toolReturn.c197InputSha256 !== digest(`${ROOT}/evidence/attempt8-runtime/lldb-pty.input.bin`) ||
  toolReturn.stdoutSha256 !== digest(`${ROOT}/evidence/attempt8-runtime/lldb-pty.stdout.txt`) ||
  toolReturn.stderrSha256 !== digest(`${ROOT}/evidence/attempt8-runtime/lldb-pty.stderr.txt`) ||
  terminal.supervisorError !== undefined
) throw new Error('machine-readable terminal-return binding mismatch');
const normalDetach = terminal.c197Exact === true && terminal.detachOutputObserved === true;
const forcedTerminal = terminal.watchdog?.fired === true && terminal.watchdog.actionId === 'C523' && terminal.exit.signal === 'SIGKILL';
if (!normalDetach && !forcedTerminal) throw new Error('neither exact C197 detach nor bounded watchdog terminality proved');
writeFileSync(`${PROTOCOL}/detached.json`, `${JSON.stringify({ schema: 'chirality-dapp92-real-runtime-sentinel-r3/v1', state: 'LLDB_TERMINAL_DETACH_PROVED', directChildPid: controller.directChildPid, proof: normalDetach ? 'NORMAL_C197_EXACT_DETACH' : 'FORCED_C523_WATCHDOG_TERMINAL_NO_DEBUGGER_PROCESS', terminalReturn: toolReturn }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
