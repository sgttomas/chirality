import { closeSync, existsSync, mkdirSync, openSync, readFileSync, renameSync, statSync, writeFileSync } from 'node:fs';
import { spawn, spawnSync } from 'node:child_process';
import { performance } from 'node:perf_hooks';

const REPO = '/Users/ryan/.codex/worktrees/7388/chirality';
const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const HOME = `${ROOT}/home`;
const USER = `${ROOT}/user`;
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const PROTOCOL = `${ROOT}/protocol`;
const SOCKET = `${USER}/runtime/control.sock`;
const OWNER = `${SOCKET}.owner.json`;
const HELPER = `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service`;
const GUI = `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality`;
const CLI = `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs`;
const MANIFEST = `${REPO}/projects/chirality-app-dev/chirality.project.json`;
const GUI_LOG = `${USER}/logs/desktop-main.log`;
const PATH_VALUE = '/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin';
const registry = { stale: null, helper: null, gui: null, registration: null };
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

mkdirSync(EVIDENCE, { recursive: true, mode: 0o700 });
mkdirSync(PROTOCOL, { recursive: true, mode: 0o700 });
const actionFd = openSync(`${EVIDENCE}/controller-actions.jsonl`, 'wx', 0o600);
const stdoutFd = openSync(`${EVIDENCE}/controller.stdout.bin`, 'wx', 0o600);
const stderrFd = openSync(`${EVIDENCE}/controller.stderr.bin`, 'wx', 0o600);
const originalStdoutWrite = process.stdout.write.bind(process.stdout);
const originalStderrWrite = process.stderr.write.bind(process.stderr);
process.stdout.write = (chunk, encoding, callback) => { writeFileSync(stdoutFd, chunk); return originalStdoutWrite(chunk, encoding, callback); };
process.stderr.write = (chunk, encoding, callback) => { writeFileSync(stderrFd, chunk); return originalStderrWrite(chunk, encoding, callback); };

function appendAction(value) { writeFileSync(actionFd, `${JSON.stringify({ at: new Date().toISOString(), ...value })}\n`); }
function writeJson(file, value) {
  const temporary = `${file}.${process.pid}.tmp`;
  const fd = openSync(temporary, 'wx', 0o600);
  try { writeFileSync(fd, `${JSON.stringify(value, null, 2)}\n`); } finally { closeSync(fd); }
  renameSync(temporary, file);
}
function readJson(file) { return JSON.parse(readFileSync(file, 'utf8')); }
function capture(actionId, executable, args, timeout = 5000) {
  appendAction({ actionId, kind: 'spawnSync', executable, args });
  const result = spawnSync(executable, args, { cwd: REPO, encoding: 'utf8', timeout, maxBuffer: 1048576 });
  appendAction({ actionId, kind: 'spawnSyncReturn', status: result.status, signal: result.signal, error: result.error?.message });
  if (result.status !== 0 || result.signal !== null || result.error) throw new Error(`${actionId} failed`);
  return result.stdout ?? '';
}
function parseIdentity(text, owned) {
  const match = text.match(/^\s*(\d+)\s+(\d+)\s+(\S+\s+\S+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+(.+?)\s*$/);
  if (!match || Number(match[1]) !== owned.child.pid || Number(match[2]) !== process.pid || match[4] !== owned.executable) throw new Error(`${owned.label} PID/PPID/start/command mismatch`);
  return { pid: owned.child.pid, ppid: process.pid, start: match[3], command: match[4], executable: owned.executable };
}
function identity(owned, psAction, lsofAction, baseline) {
  if (!owned || owned.exitResult || owned.child.exitCode !== null || owned.child.signalCode !== null) throw new Error(`${owned?.label ?? 'child'} not live`);
  const current = parseIdentity(capture(psAction, '/bin/ps', ['-o', 'pid=', '-o', 'ppid=', '-o', 'lstart=', '-o', 'comm=', '-p', String(owned.child.pid)]), owned);
  const text = capture(lsofAction, '/usr/sbin/lsof', ['-a', '-p', String(owned.child.pid), '-d', 'txt', '-Fn']);
  if (!text.split('\n').includes(`n${owned.executable}`)) throw new Error(`${owned.label} executable text mismatch`);
  if (baseline && (baseline.pid !== current.pid || baseline.ppid !== current.ppid || baseline.start !== current.start)) throw new Error(`${owned.label} identity drift`);
  return current;
}
function directHandleFailsafe(owned, actionId, reason) {
  if (!owned || owned.exitResult || owned.child.exitCode !== null || owned.child.signalCode !== null) return false;
  if (registry[owned.slot] !== owned || owned.child !== registry[owned.slot].child || owned.spawnedByPid !== process.pid) throw new Error(`${owned.label} direct-handle ownership mismatch`);
  appendAction({ actionId, kind: 'directChildHandleFailsafe', pid: owned.child.pid, signal: 'SIGKILL', reason });
  return owned.child.kill('SIGKILL');
}
function spawnOwned(slot, actionId, exitAction, watchdogAction, executable, args, captureOutput = false) {
  const envArgs = captureOutput
    ? ['-i', `PATH=${PATH_VALUE}`, `HOME=${HOME}`, `CHIRALITY_USER_DATA=${USER}`, 'ELECTRON_RUN_AS_NODE=1', executable, ...args]
    : ['-i', `PATH=${PATH_VALUE}`, `HOME=${HOME}`, `CHIRALITY_USER_DATA=${USER}`, 'CHIRALITY_SKIP_CLI_LAUNCHER=1', executable, ...args];
  const stdout = captureOutput ? 'pipe' : openSync(`${EVIDENCE}/${slot}.stdout.log`, 'wx', 0o600);
  const stderr = captureOutput ? 'pipe' : openSync(`${EVIDENCE}/${slot}.stderr.log`, 'wx', 0o600);
  const child = spawn('/usr/bin/env', envArgs, { cwd: REPO, stdio: ['ignore', stdout, stderr] });
  const owned = registry[slot] = { slot, label: slot, actionId, executable, child, spawnedByPid: process.pid, exitResult: null, exit: null, watchdog: null, identity: null };
  owned.exit = new Promise((resolve) => {
    child.once('error', (error) => { if (!owned.exitResult) owned.exitResult = { code: null, signal: null, error: error.message, at: new Date().toISOString() }; resolve(owned.exitResult); });
    child.once('exit', (code, signal) => { if (!owned.exitResult) owned.exitResult = { code, signal, error: null, at: new Date().toISOString() }; resolve(owned.exitResult); });
  }).then((result) => { appendAction({ actionId: exitAction, kind: 'childTerminal', slot, result }); return result; });
  owned.watchdog = setTimeout(() => { try { directHandleFailsafe(owned, watchdogAction, 'controller-owned child absolute lifetime exceeded'); } catch (error) { appendAction({ actionId: watchdogAction, kind: 'failsafeError', slot, error: error.message }); } }, 170000);
  appendAction({ actionId, kind: 'spawn', executable: '/usr/bin/env', args: envArgs, pid: child.pid });
  if (!captureOutput) { closeSync(stdout); closeSync(stderr); }
  return owned;
}
async function initializeOwned(owned, graceAction, psAction, lsofAction) {
  await Promise.race([wait(40), owned.exit]);
  appendAction({ actionId: graceAction, kind: 'boundedSpawnGrace', ms: 40 });
  if (!owned.exitResult) owned.identity = identity(owned, psAction, lsofAction);
  return owned;
}
function signalOwned(owned, signal, actionId, psAction, lsofAction) {
  const proof = identity(owned, psAction, lsofAction, owned.identity);
  appendAction({ actionId, kind: 'ChildProcess.kill', pid: owned.child.pid, signal, proof });
  if (!owned.child.kill(signal)) throw new Error(`${actionId} rejected`);
  return { actionId, signal, proof, at: new Date().toISOString(), monotonicMs: performance.now() };
}
async function boundedExit(owned, ms, actionId) {
  if (owned.exitResult) return owned.exitResult;
  appendAction({ actionId, kind: 'boundedTerminalWait', slot: owned.slot, ms });
  return Promise.race([owned.exit, wait(ms).then(() => { throw new Error(`${owned.label} terminal wait exceeded`); })]);
}
async function settleOwned(owned, spec) {
  if (!owned) return { present: false, terminal: true };
  clearTimeout(owned.watchdog);
  if (owned.exitResult) return { present: true, terminal: true, exit: owned.exitResult };
  const first = signalOwned(owned, spec.firstSignal, spec.firstAction, spec.firstPs, spec.firstLsof);
  try { return { present: true, terminal: true, first, exit: await boundedExit(owned, 3000, spec.firstWait) }; }
  catch (firstError) {
    if (!spec.killAction) {
      const killed = directHandleFailsafe(owned, spec.failsafeAction, 'identity-guarded settlement failed');
      return { present: true, terminal: killed ? Boolean(await boundedExit(owned, 3000, spec.failsafeWait)) : false, firstError: firstError.message };
    }
    const kill = signalOwned(owned, 'SIGKILL', spec.killAction, spec.killPs, spec.killLsof);
    return { present: true, terminal: true, first, firstError: firstError.message, kill, exit: await boundedExit(owned, 3000, spec.killWait) };
  }
}
async function settleIndependent(name, owned, spec, cleanup, actionId) {
  try { cleanup[name] = await settleOwned(owned, spec); }
  catch (error) { cleanup[name] = { terminal: false, error: error instanceof Error ? error.message : String(error) }; cleanup.failures.push(name); }
  appendAction({ actionId, kind: 'independentSettlementComplete', name, value: cleanup[name] });
}
async function ready(owned, actionId) {
  appendAction({ actionId, kind: 'boundedReadinessPoll', attempts: 80, intervalMs: 100 });
  for (let index = 1; index <= 80; index += 1) {
    if (owned.exitResult) throw new Error(`${owned.label} exited during readiness`);
    if (existsSync(SOCKET) && existsSync(OWNER)) {
      const value = readJson(OWNER);
      if (value.schemaVersion !== 'chirality.daemon-owner/v1' || value.pid !== owned.child.pid || value.socketPath !== SOCKET || typeof value.startedAt !== 'string') throw new Error('owner record mismatch');
      return { owner: { schemaVersion: value.schemaVersion, pid: value.pid, uid: value.uid, socketPath: value.socketPath, startedAt: value.startedAt }, socketInode: statSync(SOCKET).ino, ownerInode: statSync(OWNER).ino, index, monotonicMs: performance.now() };
    }
    await Promise.race([wait(100), owned.exit.then(() => { throw new Error(`${owned.label} exited during readiness wait`); })]);
  }
  throw new Error('readiness timeout');
}
async function waitFile(file, state, pid, deadline, actionId, liveChildren) {
  appendAction({ actionId, kind: 'boundedProtocolWait', file, state, deadline });
  while (performance.now() <= deadline) {
    for (const owned of liveChildren) if (owned?.exitResult) throw new Error(`${owned.label} exited while waiting for ${file}`);
    if (existsSync(`${PROTOCOL}/${file}`)) {
      const value = readJson(`${PROTOCOL}/${file}`);
      if (value.schema !== 'chirality-dapp92-real-runtime-sentinel-r4/v1' || value.state !== state || value.directChildPid !== pid) throw new Error(`${file} mismatch`);
      return value;
    }
    await wait(50);
  }
  throw new Error(`${file} timeout`);
}
async function registrationRun(helper) {
  const registration = spawnOwned('registration', 'C658', 'C659', 'C660', GUI, [CLI, 'project', 'register', MANIFEST, '--approved-by', 'D-APP-92', '--approval-reference', 'D-APP-92-OPTION-A', '--json'], true);
  await initializeOwned(registration, 'C661', 'C662', 'C663');
  let stdout = ''; let stderr = ''; let overflowReject;
  const overflow = new Promise((_, reject) => { overflowReject = reject; });
  registration.child.stdout.setEncoding('utf8');
  registration.child.stderr.setEncoding('utf8');
  registration.child.stdout.on('data', (chunk) => { stdout += chunk; if (Buffer.byteLength(stdout) > 1048576) overflowReject(new Error('C664 registration stdout overflow')); });
  registration.child.stderr.on('data', (chunk) => { stderr += chunk; if (Buffer.byteLength(stderr) > 1048576) overflowReject(new Error('C665 registration stderr overflow')); });
  const timeout = wait(10000).then(() => { throw new Error('C666 registration timeout'); });
  const helperTerminal = helper.exit.then(() => { throw new Error('C667 helper exited during registration'); });
  appendAction({ actionId: 'C668', kind: 'registrationRaceResolution', arms: ['C659', 'C664', 'C665', 'C666', 'C667'] });
  const exit = await Promise.race([registration.exit, overflow, timeout, helperTerminal]);
  if (exit.code !== 0 || exit.signal !== null || exit.error || stderr !== '') throw new Error('registration failed');
  const parsed = JSON.parse(stdout);
  if (parsed.projectId !== 'chirality-app-dev' || typeof parsed.clientId !== 'string' || parsed.manifestHash !== '5a79777038acd2b5fda3b0416c0092e2c980ff0eff7e84a019fdac3bac8fdc04') throw new Error('registration public result mismatch');
  const safe = { projectId: parsed.projectId, clientId: parsed.clientId, manifestHash: parsed.manifestHash, exitStatus: exit.code };
  writeJson(`${EVIDENCE}/project-registration-public.json`, safe);
  stdout = ''; stderr = '';
  return safe;
}
async function contact(guiLaunch, helper, gui) {
  appendAction({ actionId: 'C676', kind: 'boundedContactPoll', attempts: 5, intervalMs: 100 });
  for (let index = 1; index <= 5; index += 1) {
    if (helper.exitResult || gui.exitResult) throw new Error('runtime child exited during contact');
    if (existsSync(GUI_LOG)) {
      const line = readFileSync(GUI_LOG, 'utf8').split('\n').find((item) => item.includes('runtime.connectivity.bound'));
      if (line) {
        const match = line.match(/^(\d{4}-\d{2}-\d{2}T[^ ]+) /); const wall = match ? Date.parse(match[1]) : NaN;
        if (!Number.isFinite(wall) || wall < guiLaunch.wallMs || wall - guiLaunch.wallMs > 500) throw new Error('contact window mismatch');
        return { line, index, wallMs: wall, monotonicMs: guiLaunch.monotonicMs + wall - guiLaunch.wallMs };
      }
    }
    await wait(100);
  }
  throw new Error('contact timeout');
}
function snapshot(helper, gui) {
  return {
    ps: capture('C677', '/bin/ps', ['-o', 'pid=,ppid=,pgid=,state=,etime=', '-p', `${helper.child.pid},${gui.child.pid}`]),
    unix: capture('C678', '/usr/sbin/lsof', ['-nP', '-p', String(helper.child.pid), '-a', '-U']),
    tcp: capture('C679', '/usr/sbin/lsof', ['-nP', '-p', String(helper.child.pid), '-a', '-iTCP']),
    stat: capture('C680', '/usr/bin/stat', ['-f', '%N|%i|%p|%u|%g|%z', SOCKET, OWNER]),
    hashes: capture('C681', '/usr/bin/shasum', ['-a', '256', HELPER, `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar`, `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist`, GUI, `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar`])
  };
}

const result = { schema: 'chirality-dapp92-real-runtime-result-r4/v1', controllerPid: process.pid, status: 'INITIAL', startedAt: new Date().toISOString(), deviations: [] };
let controllerIssued = false;
try {
  const stale = spawnOwned('stale', 'C638', 'C639', 'C640', HELPER, ['--runtime-daemon']);
  await initializeOwned(stale, 'C641', 'C642', 'C643');
  const staleReady = await ready(stale, 'C644');
  const staleSignal = signalOwned(stale, 'SIGKILL', 'C647', 'C645', 'C646');
  const staleExit = await boundedExit(stale, 3000, 'C648');
  if (staleExit.signal !== 'SIGKILL') throw new Error('stale helper signal mismatch');
  const helper = spawnOwned('helper', 'C649', 'C650', 'C651', HELPER, ['--runtime-daemon']);
  await initializeOwned(helper, 'C652', 'C653', 'C654');
  const helperReady = await ready(helper, 'C655');
  if (helperReady.socketInode === staleReady.socketInode || helperReady.ownerInode === staleReady.ownerInode) throw new Error('stale recovery identity unchanged');
  const readyMs = performance.now();
  const controller = { schema: 'chirality-dapp92-real-runtime-controller-r4/v1', state: 'ATTACH_READY', controllerPid: process.pid, directChildPid: helper.child.pid, helperExecutable: HELPER, helperIdentity: helper.identity, readyMonotonicMs: readyMs, replayDeadlineMonotonicMs: readyMs + 139500, detachDeadlineMonotonicMs: readyMs + 151000, helperReady };
  writeJson(`${PROTOCOL}/controller.json`, controller); controllerIssued = true;
  process.stdout.write(`${JSON.stringify(controller)}\n`);
  await waitFile('trace-ready.json', 'LLDB_TRACE_READY', helper.child.pid, readyMs + 28000, 'C657', [helper]);
  result.registration = await registrationRun(helper);
  const remaining = readyMs + 28000 - performance.now();
  appendAction({ actionId: 'C669', kind: 'boundedGuiLaunchTimer', remaining });
  if (remaining < 0) throw new Error('GUI launch target exceeded');
  await Promise.race([wait(remaining), helper.exit.then(() => { throw new Error('helper exited during GUI timer'); })]);
  const guiLaunch = { wallMs: Date.now(), monotonicMs: performance.now() };
  const gui = spawnOwned('gui', 'C670', 'C671', 'C672', GUI, [`--user-data-dir=${USER}`]);
  await initializeOwned(gui, 'C673', 'C674', 'C675');
  guiLaunch.pid = gui.child.pid; guiLaunch.delayMs = guiLaunch.monotonicMs - readyMs;
  if (guiLaunch.delayMs < 28000 || guiLaunch.delayMs >= 28100) throw new Error('28-second bound missed');
  result.guiLaunch = guiLaunch; result.contact = await contact(guiLaunch, helper, gui);
  const signalTarget = result.contact.monotonicMs + 102000;
  result.preSignal = snapshot(helper, gui);
  const armRemaining = signalTarget - 2000 - performance.now();
  appendAction({ actionId: 'C682', kind: 'boundedArmTimer', remaining: Math.max(0, armRemaining) });
  if (armRemaining > 0) await Promise.race([wait(armRemaining), helper.exit.then(() => { throw new Error('helper exited during arm timer'); }), gui.exit.then(() => { throw new Error('GUI exited during arm timer'); })]);
  writeJson(`${PROTOCOL}/signal-armed.json`, { schema: 'chirality-dapp92-signal-armed-r4/v1', state: 'SIGNAL_ARMED', directChildPid: helper.child.pid, signalTargetMonotonicMs: signalTarget });
  process.stdout.write(`${JSON.stringify({ state: 'SIGNAL_ARMED', directChildPid: helper.child.pid, signalTargetMonotonicMs: signalTarget })}\n`);
  await waitFile('trace-live.json', 'LLDB_TRACE_LIVE', helper.child.pid, signalTarget, 'C683', [helper, gui]);
  const signalRemaining = signalTarget - performance.now();
  appendAction({ actionId: 'C684', kind: 'boundedSignalTimer', remaining: Math.max(0, signalRemaining) });
  if (signalRemaining > 0) await Promise.race([wait(signalRemaining), helper.exit.then(() => { throw new Error('helper exited before first signal'); }), gui.exit.then(() => { throw new Error('GUI exited before first signal'); })]);
  result.signal = signalOwned(helper, 'SIGTERM', 'C687', 'C685', 'C686');
  result.signal.contactToSignalMs = result.signal.monotonicMs - result.contact.monotonicMs;
  appendAction({ actionId: 'C688', kind: 'boundedHelperExitPoll', attempts: 80, intervalMs: 100 });
  for (let index = 1; index <= 80 && !helper.exitResult; index += 1) await Promise.race([wait(100), helper.exit]);
  if (!helper.exitResult) throw new Error('helper survived 80 x 0.1 seconds');
  if (performance.now() >= readyMs + 139500) throw new Error('replay deadline missed');
  result.status = 'REPLAY_CAPTURED_AWAITING_SESSION_TERMINAL_PROOF';
} catch (error) {
  result.status = controllerIssued ? 'CONTROLLER_TERMINAL_AWAITING_BRANCH_PROOF' : 'PRE_CONTROLLER_TERMINAL';
  result.error = error instanceof Error ? error.message : String(error);
  result.deviations.push(result.error);
} finally {
  writeJson(`${PROTOCOL}/replay-terminal.json`, result);
  const cleanup = { schema: 'chirality-dapp92-controller-cleanup-r4/v1', controllerPid: process.pid, controllerIssued, startedAt: new Date().toISOString(), failures: [] };
  const debuggerObserved = existsSync(`${PROTOCOL}/lldb-spawn-attempt.json`);
  const attachIntent = existsSync(`${PROTOCOL}/attach-intent.json`);
  let cleanupPermission = !controllerIssued;
  if (controllerIssued) {
    appendAction({ actionId: 'C689', kind: 'boundedCleanupPermissionWait', attempts: 3040, intervalMs: 50 });
    for (let index = 1; index <= 3040; index += 1) {
      if (existsSync(`${PROTOCOL}/cleanup-permission.json`)) { cleanupPermission = true; break; }
      await wait(50);
    }
  }
  cleanup.branchInputs = { controllerIssued, attachIntent, debuggerObserved, cleanupPermission };
  await settleIndependent('registration', registry.registration, { firstSignal: 'SIGKILL', firstAction: 'C692', firstPs: 'C690', firstLsof: 'C691', firstWait: 'C693', failsafeAction: 'C694', failsafeWait: 'C695' }, cleanup, 'C710');
  await settleIndependent('stale', registry.stale, { firstSignal: 'SIGKILL', firstAction: 'C698', firstPs: 'C696', firstLsof: 'C697', firstWait: 'C699', failsafeAction: 'C700', failsafeWait: 'C701' }, cleanup, 'C711');
  if (cleanupPermission) {
    await settleIndependent('gui', registry.gui, { firstSignal: 'SIGTERM', firstAction: 'C704', firstPs: 'C702', firstLsof: 'C703', firstWait: 'C705', killAction: 'C708', killPs: 'C706', killLsof: 'C707', killWait: 'C709', failsafeAction: 'C708', failsafeWait: 'C709' }, cleanup, 'C712');
    await settleIndependent('helper', registry.helper, { firstSignal: 'SIGKILL', firstAction: 'C715', firstPs: 'C713', firstLsof: 'C714', firstWait: 'C716', failsafeAction: 'C717', failsafeWait: 'C718' }, cleanup, 'C719');
  } else {
    cleanup.gui = { terminal: false, blocked: 'NO_CLEANUP_PERMISSION' };
    cleanup.helper = { terminal: false, blocked: 'NO_CLEANUP_PERMISSION' };
    cleanup.failures.push('cleanup-permission');
  }
  for (const owned of Object.values(registry)) if (owned?.exitResult) clearTimeout(owned.watchdog);
  cleanup.status = cleanup.failures.length === 0 && Object.values(cleanup).filter((value) => value && typeof value === 'object' && 'terminal' in value).every((value) => value.terminal) ? 'ALL_CONTROLLER_CHILDREN_TERMINAL' : 'CLEANUP_INCOMPLETE';
  cleanup.completedAt = new Date().toISOString();
  writeJson(`${EVIDENCE}/controller-cleanup-r4.json`, cleanup);
  result.cleanup = cleanup; result.completedAt = new Date().toISOString();
  writeJson(`${EVIDENCE}/protocol-result-r4.json`, result);
  process.stdout.write(`${JSON.stringify({ status: result.status, cleanup: cleanup.status })}\n`);
  closeSync(actionFd); closeSync(stdoutFd); closeSync(stderrFd);
  if (cleanup.status !== 'ALL_CONTROLLER_CHILDREN_TERMINAL') process.exitCode = 3;
  else if (result.status !== 'REPLAY_CAPTURED_AWAITING_SESSION_TERMINAL_PROOF') process.exitCode = 1;
}
