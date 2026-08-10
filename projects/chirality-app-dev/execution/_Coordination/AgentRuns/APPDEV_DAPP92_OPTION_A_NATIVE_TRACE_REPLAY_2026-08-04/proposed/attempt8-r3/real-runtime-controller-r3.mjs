import { closeSync, existsSync, mkdirSync, openSync, readFileSync, renameSync, statSync, writeFileSync } from 'node:fs';
import { spawn, spawnSync } from 'node:child_process';
import { performance } from 'node:perf_hooks';

const REPO = '/Users/ryan/.codex/worktrees/7388/chirality';
const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const HOME = `${ROOT}/home`;
const USER = `${ROOT}/user`;
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const PROTOCOL = `${ROOT}/protocol`;
const ACTION_LOG = `${EVIDENCE}/controller-actions.jsonl`;
const SOCKET = `${USER}/runtime/control.sock`;
const OWNER = `${SOCKET}.owner.json`;
const HELPER = `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service`;
const GUI = `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality`;
const CLI = `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs`;
const MANIFEST = `${REPO}/projects/chirality-app-dev/chirality.project.json`;
const GUI_LOG = `${USER}/logs/desktop-main.log`;
const PATH_VALUE = '/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin';
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

mkdirSync(EVIDENCE, { recursive: true, mode: 0o700 });
mkdirSync(PROTOCOL, { recursive: true, mode: 0o700 });

function appendAction(value) { writeFileSync(ACTION_LOG, `${JSON.stringify({ at: new Date().toISOString(), ...value })}\n`, { flag: 'a', mode: 0o600 }); }
function writeJson(file, value) {
  const temporary = `${file}.${process.pid}.tmp`;
  const descriptor = openSync(temporary, 'wx', 0o600);
  try { writeFileSync(descriptor, `${JSON.stringify(value, null, 2)}\n`, 'utf8'); } finally { closeSync(descriptor); }
  renameSync(temporary, file);
}
function readJson(file) { return JSON.parse(readFileSync(file, 'utf8')); }
function run(actionId, executable, args) {
  appendAction({ actionId, kind: 'spawnSync', executable, args });
  const result = spawnSync(executable, args, { cwd: REPO, encoding: 'utf8', timeout: 10000, maxBuffer: 1048576 });
  appendAction({ actionId, kind: 'spawnSyncReturn', status: result.status, signal: result.signal, error: result.error?.message });
  if (result.status !== 0 || result.signal !== null || result.error) throw new Error(`${actionId} failed`);
  return result.stdout ?? '';
}
function parseIdentity(text, pid, ppid, executable) {
  const match = text.match(/^\s*(\d+)\s+(\d+)\s+(\S+\s+\S+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+(.+?)\s*$/);
  if (!match || Number(match[1]) !== pid || Number(match[2]) !== ppid || match[4] !== executable) throw new Error('PID/PPID/start/command mismatch');
  return { pid, ppid, start: match[3], command: match[4], executable };
}
function identity(owned, psAction, lsofAction, baseline) {
  if (!owned || owned.exitResult || owned.child.exitCode !== null || owned.child.signalCode !== null) throw new Error(`${owned?.label ?? 'child'} not live`);
  const current = parseIdentity(run(psAction, '/bin/ps', ['-o', 'pid=', '-o', 'ppid=', '-o', 'lstart=', '-o', 'comm=', '-p', String(owned.child.pid)]), owned.child.pid, process.pid, owned.executable);
  const text = run(lsofAction, '/usr/sbin/lsof', ['-a', '-p', String(owned.child.pid), '-d', 'txt', '-Fn']);
  if (!text.split('\n').includes(`n${owned.executable}`)) throw new Error('executable text mismatch');
  if (baseline && baseline.start !== current.start) throw new Error('start identity drift');
  return current;
}
function exitPromise(child, label) {
  return new Promise((resolve, reject) => {
    child.once('error', reject);
    child.once('exit', (code, signal) => resolve({ label, code, signal, at: new Date().toISOString() }));
  });
}
async function spawnOwned(actionId, executable, args, label, psAction, lsofAction, capture = false) {
  const stdout = capture ? undefined : openSync(`${EVIDENCE}/${label}.stdout.log`, 'a', 0o600);
  const stderr = capture ? undefined : openSync(`${EVIDENCE}/${label}.stderr.log`, 'a', 0o600);
  const envArgs = capture
    ? ['-i', `PATH=${PATH_VALUE}`, `HOME=${HOME}`, `CHIRALITY_USER_DATA=${USER}`, 'ELECTRON_RUN_AS_NODE=1', executable, ...args]
    : ['-i', `PATH=${PATH_VALUE}`, `HOME=${HOME}`, `CHIRALITY_USER_DATA=${USER}`, 'CHIRALITY_SKIP_CLI_LAUNCHER=1', executable, ...args];
  appendAction({ actionId, kind: 'spawn', executable: '/usr/bin/env', args: envArgs });
  const child = spawn('/usr/bin/env', envArgs, { cwd: REPO, stdio: capture ? ['ignore', 'pipe', 'pipe'] : ['ignore', stdout, stderr] });
  if (!capture) { closeSync(stdout); closeSync(stderr); }
  if (!Number.isInteger(child.pid) || child.pid <= 0) throw new Error(`${label} PID missing`);
  const owned = { actionId, label, executable, child, exitResult: undefined };
  owned.exit = exitPromise(child, label).then((result) => { owned.exitResult = result; appendAction({ actionId, kind: 'childExit', result }); return result; });
  await Promise.race([wait(100), owned.exit.then(() => undefined)]);
  if (!owned.exitResult) owned.identity = identity(owned, psAction, lsofAction);
  return owned;
}
function signalOwned(owned, signal, actionId, psAction, lsofAction) {
  const proof = identity(owned, psAction, lsofAction, owned.identity);
  if (owned.exitResult || owned.child.exitCode !== null || owned.child.signalCode !== null) throw new Error(`${owned.label} exited before ${signal}`);
  appendAction({ actionId, kind: 'ChildProcess.kill', ownerActionId: owned.actionId, pid: owned.child.pid, signal, proof });
  if (!owned.child.kill(signal)) throw new Error(`${actionId} rejected`);
  return { actionId, signal, proof, at: new Date().toISOString(), monotonicMs: performance.now() };
}
function unexpected(owned, context) { return owned.exit.then((value) => { throw new Error(`${owned.label} exited during ${context}: ${JSON.stringify(value)}`); }); }
async function guarded(promise, owned, context) { return Promise.race([promise, ...owned.filter(Boolean).map((child) => unexpected(child, context))]); }
async function boundedExit(owned, ms, label) {
  if (owned.exitResult) return owned.exitResult;
  return Promise.race([owned.exit, wait(ms).then(() => { throw new Error(`${label} reap timeout`); })]);
}
async function settleOne(owned, firstSignal, firstAction, firstPs, firstLsof, killAction, killPs, killLsof) {
  if (!owned) return { present: false };
  if (owned.exitResult) return { present: true, exit: owned.exitResult };
  const first = signalOwned(owned, firstSignal, firstAction, firstPs, firstLsof);
  try { return { present: true, first, exit: await boundedExit(owned, 3000, `${owned.label} first-signal`) }; }
  catch (error) {
    if (!killAction) throw error;
    const kill = signalOwned(owned, 'SIGKILL', killAction, killPs, killLsof);
    return { present: true, first, kill, exit: await boundedExit(owned, 3000, `${owned.label} SIGKILL`) };
  }
}
async function settleIndependent(name, operation, cleanup) {
  try { cleanup[name] = await operation(); }
  catch (error) { cleanup[name] = { status: 'FAILED', error: error instanceof Error ? error.message : String(error) }; cleanup.failures.push(name); }
}
function ownerRecord(pid) {
  const value = readJson(OWNER);
  if (value.schemaVersion !== 'chirality.daemon-owner/v1' || value.pid !== pid || value.socketPath !== SOCKET || typeof value.startedAt !== 'string') throw new Error('owner record mismatch');
  return { schemaVersion: value.schemaVersion, pid: value.pid, uid: value.uid, socketPath: value.socketPath, startedAt: value.startedAt };
}
async function ready(owned) {
  for (let index = 1; index <= 80; index += 1) {
    if (existsSync(SOCKET) && existsSync(OWNER)) {
      const socket = statSync(SOCKET); const owner = statSync(OWNER);
      return { owner: ownerRecord(owned.child.pid), socketInode: socket.ino, ownerInode: owner.ino, index, monotonicMs: performance.now() };
    }
    await guarded(wait(100), [owned], 'readiness');
  }
  throw new Error('readiness timeout');
}
async function sentinel(name, state, pid, deadline, children) {
  while (performance.now() <= deadline) {
    const file = `${PROTOCOL}/${name}`;
    if (existsSync(file)) {
      const value = readJson(file);
      if (value.schema !== 'chirality-dapp92-real-runtime-sentinel-r3/v1' || value.directChildPid !== pid || value.state !== state) throw new Error(`${name} mismatch`);
      return value;
    }
    await guarded(wait(50), children, name);
  }
  throw new Error(`${name} timeout`);
}
async function registrationRun() {
  const args = [CLI, 'project', 'register', MANIFEST, '--approved-by', 'D-APP-92', '--approval-reference', 'D-APP-92-OPTION-A', '--json'];
  registration = await spawnOwned('C470', GUI, args, 'registration', 'C488', 'C489', true);
  let stdout = ''; let stderr = ''; let overflow;
  const overflowPromise = new Promise((_, reject) => { overflow = reject; });
  registration.child.stdout?.setEncoding('utf8'); registration.child.stderr?.setEncoding('utf8');
  registration.child.stdout?.on('data', (chunk) => { stdout += chunk; if (stdout.length > 1048576) overflow(new Error('registration stdout overflow')); });
  registration.child.stderr?.on('data', (chunk) => { stderr += chunk; if (stderr.length > 1048576) overflow(new Error('registration stderr overflow')); });
  const timeout = wait(10000).then(() => { throw new Error('registration timeout'); });
  const exit = await Promise.race([registration.exit, overflowPromise, timeout, unexpected(helper, 'registration')]);
  if (exit.code !== 0 || exit.signal !== null || stderr !== '') throw new Error('registration failed');
  const parsed = JSON.parse(stdout);
  if (parsed.projectId !== 'chirality-app-dev' || typeof parsed.clientId !== 'string' || parsed.manifestHash !== '5a79777038acd2b5fda3b0416c0092e2c980ff0eff7e84a019fdac3bac8fdc04') throw new Error('registration public result mismatch');
  const safe = { projectId: parsed.projectId, clientId: parsed.clientId, manifestHash: parsed.manifestHash, exitStatus: exit.code };
  writeJson(`${EVIDENCE}/project-registration-public.json`, safe);
  return safe;
}
async function contact(guiLaunch) {
  for (let index = 1; index <= 5; index += 1) {
    if (existsSync(GUI_LOG)) {
      const line = readFileSync(GUI_LOG, 'utf8').split('\n').find((item) => item.includes('runtime.connectivity.bound'));
      if (line) {
        const match = line.match(/^(\d{4}-\d{2}-\d{2}T[^ ]+) /); const wall = match ? Date.parse(match[1]) : NaN;
        if (!Number.isFinite(wall) || wall < guiLaunch.wallMs || wall - guiLaunch.wallMs > 500) throw new Error('contact window mismatch');
        return { line, index, wallMs: wall, monotonicMs: guiLaunch.monotonicMs + wall - guiLaunch.wallMs };
      }
    }
    await guarded(wait(100), [helper, gui], 'contact');
  }
  throw new Error('contact timeout');
}
function snapshot() {
  return {
    ps: run('C504', '/bin/ps', ['-o', 'pid=,ppid=,pgid=,state=,etime=', '-p', `${helper.child.pid},${gui.child.pid}`]),
    unix: run('C505', '/usr/sbin/lsof', ['-nP', '-p', String(helper.child.pid), '-a', '-U']),
    tcp: run('C506', '/usr/sbin/lsof', ['-nP', '-p', String(helper.child.pid), '-a', '-iTCP']),
    stat: run('C507', '/usr/bin/stat', ['-f', '%N|%i|%p|%u|%g|%z', SOCKET, OWNER]),
    hashes: run('C508', '/usr/bin/shasum', ['-a', '256', HELPER, `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar`, `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist`, GUI, `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar`])
  };
}

const result = { schema: 'chirality-dapp92-real-runtime-result-r3/v1', controllerPid: process.pid, status: 'INITIAL', startedAt: new Date().toISOString(), deviations: [] };
let stale; let helper; let gui; let registration; let controllerIssued = false;
try {
  stale = await spawnOwned('C467', HELPER, ['--runtime-daemon'], 'stale-helper', 'C482', 'C483');
  const staleReady = await ready(stale);
  const staleSignal = signalOwned(stale, 'SIGKILL', 'C472', 'C490', 'C491');
  const staleExit = await boundedExit(stale, 3000, 'stale success-path');
  result.stale = { staleReady, staleSignal, staleExit };
  if (staleExit.signal !== 'SIGKILL') throw new Error('stale signal mismatch');
  helper = await spawnOwned('C468', HELPER, ['--runtime-daemon'], 'helper', 'C484', 'C485');
  const helperReady = await ready(helper);
  if (helperReady.socketInode === staleReady.socketInode || helperReady.ownerInode === staleReady.ownerInode) throw new Error('stale recovery identity unchanged');
  const readyMs = performance.now();
  const controller = { schema: 'chirality-dapp92-real-runtime-controller-r3/v1', state: 'ATTACH_READY', controllerPid: process.pid, directChildPid: helper.child.pid, helperExecutable: HELPER, helperIdentity: helper.identity, readyMonotonicMs: readyMs, replayDeadlineMonotonicMs: readyMs + 139500, detachDeadlineMonotonicMs: readyMs + 148000, helperReady };
  writeJson(`${PROTOCOL}/controller.json`, controller); controllerIssued = true;
  process.stdout.write(`${JSON.stringify(controller)}\n`);
  await sentinel('trace-ready.json', 'LLDB_TRACE_READY', helper.child.pid, readyMs + 28000, [helper]);
  result.registration = await registrationRun();
  const remaining = readyMs + 28000 - performance.now();
  if (remaining < 0) throw new Error('GUI target exceeded');
  await guarded(wait(remaining), [helper], 'GUI timer');
  const guiLaunch = { wallMs: Date.now(), monotonicMs: performance.now() };
  gui = await spawnOwned('C469', GUI, [`--user-data-dir=${USER}`], 'gui', 'C486', 'C487');
  guiLaunch.pid = gui.child.pid; guiLaunch.delayMs = guiLaunch.monotonicMs - readyMs;
  if (guiLaunch.delayMs < 28000 || guiLaunch.delayMs >= 28100) throw new Error('28-second bound missed');
  result.guiLaunch = guiLaunch; result.contact = await contact(guiLaunch);
  const signalTarget = result.contact.monotonicMs + 102000;
  result.preSignal = snapshot();
  if (signalTarget - 2000 > performance.now()) await guarded(wait(signalTarget - 2000 - performance.now()), [helper, gui], 'arm timer');
  writeJson(`${PROTOCOL}/signal-armed.json`, { schema: 'chirality-dapp92-signal-armed-r3/v1', state: 'SIGNAL_ARMED', directChildPid: helper.child.pid, signalTargetMonotonicMs: signalTarget });
  process.stdout.write(`${JSON.stringify({ state: 'SIGNAL_ARMED', directChildPid: helper.child.pid, signalTargetMonotonicMs: signalTarget })}\n`);
  await sentinel('trace-live.json', 'LLDB_TRACE_LIVE', helper.child.pid, signalTarget, [helper, gui]);
  if (signalTarget > performance.now()) await guarded(wait(signalTarget - performance.now()), [helper, gui], 'signal timer');
  result.signal = signalOwned(helper, 'SIGTERM', 'C473', 'C492', 'C493');
  result.signal.contactToSignalMs = result.signal.monotonicMs - result.contact.monotonicMs;
  const exitPolls = [];
  for (let index = 1; index <= 80 && !helper.exitResult; index += 1) { exitPolls.push({ index, monotonicMs: performance.now() }); await Promise.race([wait(100), helper.exit]); }
  result.exitPolls = exitPolls;
  if (!helper.exitResult) throw new Error('helper survived 80 x 0.1 seconds');
  if (performance.now() >= readyMs + 139500) throw new Error('replay deadline missed');
  result.status = 'REPLAY_CAPTURED_AWAITING_LLDB_TERMINAL_PROOF';
} catch (error) {
  result.status = existsSync(`${PROTOCOL}/lldb-spawn-attempt.json`) ? 'FAILED_AWAITING_LLDB_TERMINAL_PROOF' : 'FAILED_AWAITING_DEBUGGER_DISPOSITION';
  result.error = error instanceof Error ? error.message : String(error); result.deviations.push(result.error);
} finally {
  writeJson(`${PROTOCOL}/replay-terminal.json`, result);
  process.stdout.write(`${JSON.stringify({ schema: result.schema, status: result.status })}\n`);
  const cleanup = { schema: 'chirality-dapp92-controller-cleanup-r3/v1', startedAt: new Date().toISOString(), controllerIssued, failures: [] };
  const attachIntent = existsSync(`${PROTOCOL}/attach-started.json`);
  let debuggerStarted = existsSync(`${PROTOCOL}/lldb-spawn-attempt.json`);
  let debuggerTerminal = !attachIntent;
  if (attachIntent) {
    try {
      const deadline = readJson(`${PROTOCOL}/controller.json`).detachDeadlineMonotonicMs;
      while (performance.now() <= deadline) {
        if (existsSync(`${PROTOCOL}/detached.json`)) { await sentinel('detached.json', 'LLDB_TERMINAL_DETACH_PROVED', helper.child.pid, deadline, []); debuggerTerminal = true; debuggerStarted = true; break; }
        if (existsSync(`${PROTOCOL}/no-debugger-start-observed.json`)) { debuggerTerminal = true; debuggerStarted = false; break; }
        await wait(50);
      }
      if (!debuggerTerminal) throw new Error('debugger disposition deadline exceeded');
    } catch (error) { cleanup.failures.push('debugger-terminal-proof'); cleanup.debuggerTerminalError = error instanceof Error ? error.message : String(error); }
  }
  await settleIndependent('registration', () => settleOne(registration, 'SIGKILL', 'C474', 'C494', 'C495'), cleanup);
  await settleIndependent('stale', () => settleOne(stale, 'SIGKILL', 'C478', 'C502', 'C503'), cleanup);
  if (debuggerTerminal) {
    await settleIndependent('gui', () => settleOne(gui, 'SIGTERM', 'C475', 'C496', 'C497', 'C476', 'C498', 'C499'), cleanup);
    await settleIndependent('helper', () => settleOne(helper, 'SIGKILL', 'C477', 'C500', 'C501'), cleanup);
  } else {
    cleanup.gui = { status: 'BLOCKED_DEBUGGER_NOT_TERMINAL' }; cleanup.helper = { status: 'BLOCKED_DEBUGGER_NOT_TERMINAL' };
  }
  cleanup.status = cleanup.failures.length === 0 && debuggerTerminal ? 'ALL_CONTROLLER_CHILDREN_REAPED' : 'CLEANUP_INCOMPLETE';
  cleanup.completedAt = new Date().toISOString(); writeJson(`${EVIDENCE}/controller-cleanup-r3.json`, cleanup);
  if (!debuggerStarted && cleanup.status === 'ALL_CONTROLLER_CHILDREN_REAPED') writeJson(`${PROTOCOL}/no-debugger-start-cleanup-safe-r3.json`, { schema: 'chirality-dapp92-no-debugger-start-cleanup-safe-r3/v1', state: 'NO_LLDB_START_ALL_CONTROLLER_CHILDREN_REAPED', attachIntentPresent: attachIntent });
  if (!controllerIssued && cleanup.status === 'ALL_CONTROLLER_CHILDREN_REAPED') writeJson(`${PROTOCOL}/pre-controller-cleanup-safe-r3.json`, { schema: 'chirality-dapp92-pre-controller-cleanup-safe-r3/v1', state: 'NO_CONTROLLER_RECORD_ALL_CHILDREN_REAPED' });
  result.cleanup = cleanup; result.completedAt = new Date().toISOString(); writeJson(`${EVIDENCE}/protocol-result-r3.json`, result);
  process.stdout.write(`${JSON.stringify({ status: result.status, cleanup: cleanup.status })}\n`);
  if (cleanup.status !== 'ALL_CONTROLLER_CHILDREN_REAPED') process.exitCode = 2; else if (result.status !== 'REPLAY_CAPTURED_AWAITING_LLDB_TERMINAL_PROOF') process.exitCode = 1;
}
