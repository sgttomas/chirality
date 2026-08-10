import {
  closeSync, existsSync, mkdirSync, openSync, readFileSync, renameSync,
  statSync, writeFileSync
} from 'node:fs';
import { createHash } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
import { performance } from 'node:perf_hooks';

const REPO = '/Users/ryan/.codex/worktrees/7388/chirality';
const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const HOME = `${ROOT}/home`;
const USER_DATA = `${ROOT}/user`;
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const PROTOCOL = `${ROOT}/protocol`;
const RUNTIME = `${USER_DATA}/runtime`;
const SOCKET = `${RUNTIME}/control.sock`;
const OWNER = `${SOCKET}.owner.json`;
const HELPER = `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service`;
const GUI = `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality`;
const CLI = `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs`;
const MANIFEST = `${REPO}/projects/chirality-app-dev/chirality.project.json`;
const GUI_LOG = `${USER_DATA}/logs/desktop-main.log`;
const NODE_PATH = '/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin';
const POLL_MS = 100;
const READY_POLLS = 80;
const CONTACT_POLLS = 5;
const EXIT_POLLS = 80;
const GUI_DELAY_MS = 28000;
const SIGNAL_DELAY_MS = 102000;
const REPLAY_LIMIT_MS = 139500;
const DETACH_LIMIT_MS = 148000;

mkdirSync(EVIDENCE, { recursive: true, mode: 0o700 });
mkdirSync(PROTOCOL, { recursive: true, mode: 0o700 });

function sleep(ms) { return new Promise((resolve) => setTimeout(resolve, ms)); }
function sha256(bytes) { return createHash('sha256').update(bytes).digest('hex'); }
function readJson(file) { return JSON.parse(readFileSync(file, 'utf8')); }
function writeJsonDurable(file, value) {
  const bytes = `${JSON.stringify(value, null, 2)}\n`;
  const temporary = `${file}.${process.pid}.tmp`;
  const descriptor = openSync(temporary, 'wx', 0o600);
  try { writeFileSync(descriptor, bytes, 'utf8'); } finally { closeSync(descriptor); }
  renameSync(temporary, file);
  return sha256(bytes);
}

function runCapture(executable, args, timeout = 10000) {
  const value = spawnSync(executable, args, {
    cwd: REPO, encoding: 'utf8', timeout, maxBuffer: 1024 * 1024
  });
  return {
    executable, args, status: value.status, signal: value.signal,
    stdout: value.stdout ?? '', stderr: value.stderr ?? '', error: value.error?.message
  };
}
function requireZero(value, label) {
  if (value.status !== 0 || value.signal !== null || value.error) throw new Error(`${label} failed`);
  return value;
}

function childExitPromise(child, label) {
  return new Promise((resolve, reject) => {
    child.once('error', reject);
    child.once('exit', (code, signal) => resolve({ label, code, signal, at: new Date().toISOString() }));
  });
}
function spawnOwned(executable, args, label) {
  const stdout = openSync(`${EVIDENCE}/${label}.stdout.log`, 'a', 0o600);
  const stderr = openSync(`${EVIDENCE}/${label}.stderr.log`, 'a', 0o600);
  const child = spawn('/usr/bin/env', [
    '-i', `PATH=${NODE_PATH}`, `HOME=${HOME}`, `CHIRALITY_USER_DATA=${USER_DATA}`,
    'CHIRALITY_SKIP_CLI_LAUNCHER=1', executable, ...args
  ], { cwd: REPO, stdio: ['ignore', stdout, stderr] });
  closeSync(stdout); closeSync(stderr);
  if (!Number.isInteger(child.pid) || child.pid <= 0) throw new Error(`${label} lacked a direct-child PID`);
  const owned = { label, executable, child, exitResult: undefined };
  owned.exit = childExitPromise(child, label).then((value) => { owned.exitResult = value; return value; });
  return owned;
}

function exactIdentity(pid, expectedPpid, expectedExecutable) {
  const pidValue = requireZero(runCapture('/bin/ps', ['-o', 'pid=', '-p', String(pid)]), 'identity pid').stdout.trim();
  const ppidValue = requireZero(runCapture('/bin/ps', ['-o', 'ppid=', '-p', String(pid)]), 'identity ppid').stdout.trim();
  const startValue = requireZero(runCapture('/bin/ps', ['-o', 'lstart=', '-p', String(pid)]), 'identity start').stdout.trim();
  const commandValue = requireZero(runCapture('/bin/ps', ['-o', 'comm=', '-p', String(pid)]), 'identity command').stdout.trim();
  const textValue = requireZero(runCapture('/usr/sbin/lsof', ['-a', '-p', String(pid), '-d', 'txt', '-Fn']), 'identity executable').stdout;
  if (pidValue !== String(pid) || ppidValue !== String(expectedPpid) || !startValue || commandValue !== expectedExecutable) {
    throw new Error('exact PID/PPID/start/command identity mismatch');
  }
  const textPaths = textValue.split('\n').filter((line) => line.startsWith('n')).map((line) => line.slice(1));
  if (!textPaths.includes(expectedExecutable)) throw new Error('exact executable text identity mismatch');
  return { pid, ppid: expectedPpid, start: startValue, command: commandValue, executable: expectedExecutable };
}
async function captureOwnedIdentity(owned) {
  for (let index = 1; index <= 10; index += 1) {
    if (owned.exitResult || owned.child.exitCode !== null || owned.child.signalCode !== null) throw new Error(`${owned.label} exited before identity capture`);
    try {
      owned.identity = exactIdentity(owned.child.pid, process.pid, owned.executable);
      return owned.identity;
    } catch (error) {
      if (index === 10) throw error;
      await Promise.race([sleep(50), owned.exit.then(() => { throw new Error(`${owned.label} exited during identity capture`); })]);
    }
  }
}
function verifyOwnedIdentity(owned) {
  if (!owned || owned.exitResult || owned.child.exitCode !== null || owned.child.signalCode !== null) {
    throw new Error(`${owned?.label ?? 'child'} is not live for identity verification`);
  }
  const current = exactIdentity(owned.child.pid, process.pid, owned.executable);
  if (!owned.identity || current.start !== owned.identity.start) throw new Error(`${owned.label} start identity changed`);
  return current;
}
function signalOwned(owned, signal) {
  const identity = verifyOwnedIdentity(owned);
  if (owned.exitResult || owned.child.exitCode !== null || owned.child.signalCode !== null) throw new Error(`${owned.label} exited before ${signal}`);
  const accepted = owned.child.kill(signal);
  if (!accepted) throw new Error(`${owned.label} ChildProcess rejected ${signal}`);
  return { signal, identity, at: new Date().toISOString(), monotonicMs: performance.now() };
}
function unexpectedExit(owned, context) {
  return owned.exit.then((value) => { throw new Error(`${owned.label} exited during ${context}: ${JSON.stringify(value)}`); });
}
async function guardedWait(wait, children, context) {
  return Promise.race([wait, ...children.filter(Boolean).map((owned) => unexpectedExit(owned, context))]);
}

function ownerPublic(expectedPid) {
  const raw = readJson(OWNER);
  if (raw.schemaVersion !== 'chirality.daemon-owner/v1' || raw.pid !== expectedPid || raw.socketPath !== SOCKET || typeof raw.startedAt !== 'string') {
    throw new Error('owner record mismatch');
  }
  return { schemaVersion: raw.schemaVersion, pid: raw.pid, uid: raw.uid, socketPath: raw.socketPath, startedAt: raw.startedAt };
}
async function waitReady(owned) {
  const polls = [];
  for (let index = 1; index <= READY_POLLS; index += 1) {
    const present = existsSync(SOCKET) && existsSync(OWNER);
    polls.push({ index, monotonicMs: performance.now(), present });
    if (present) {
      const owner = ownerPublic(owned.child.pid);
      const socketStat = statSync(SOCKET); const ownerStat = statSync(OWNER);
      return { owner, socket: { inode: socketStat.ino, mode: socketStat.mode }, ownerFile: { inode: ownerStat.ino, mode: ownerStat.mode, size: ownerStat.size }, polls };
    }
    await guardedWait(sleep(POLL_MS), [owned], 'readiness wait');
  }
  throw new Error('helper readiness exceeded 80 x 0.1-second polls');
}
async function waitSentinel(name, state, pid, deadline, children) {
  const file = `${PROTOCOL}/${name}`;
  while (performance.now() <= deadline) {
    if (existsSync(file)) {
      const value = readJson(file);
      if (value.schema !== 'chirality-dapp92-real-runtime-sentinel-r2/v1' || value.directChildPid !== pid || value.state !== state) throw new Error(`${name} mismatch`);
      return value;
    }
    await guardedWait(sleep(50), children, `${name} wait`);
  }
  throw new Error(`${name} deadline exceeded`);
}

async function runRegistration(helper) {
  verifyOwnedIdentity(helper);
  const child = spawn('/usr/bin/env', [
    '-i', `PATH=${NODE_PATH}`, `HOME=${HOME}`, `CHIRALITY_USER_DATA=${USER_DATA}`,
    'ELECTRON_RUN_AS_NODE=1', GUI, CLI, 'project', 'register', MANIFEST,
    '--approved-by', 'D-APP-92', '--approval-reference', 'D-APP-92-OPTION-A', '--json'
  ], { cwd: REPO, stdio: ['ignore', 'pipe', 'pipe'] });
  let stdout = ''; let stderr = '';
  child.stdout.setEncoding('utf8'); child.stderr.setEncoding('utf8');
  child.stdout.on('data', (value) => { stdout += value; if (stdout.length > 1048576) child.kill('SIGKILL'); });
  child.stderr.on('data', (value) => { stderr += value; if (stderr.length > 1048576) child.kill('SIGKILL'); });
  const registrationExit = childExitPromise(child, 'registration');
  const timeout = sleep(10000).then(() => { throw new Error('registration timeout'); });
  const exit = await Promise.race([registrationExit, timeout, unexpectedExit(helper, 'registration')]);
  if (exit.code !== 0 || exit.signal !== null || stderr !== '') throw new Error('public registration failed');
  const parsed = JSON.parse(stdout);
  if (parsed.projectId !== 'chirality-app-dev' || typeof parsed.clientId !== 'string' || parsed.manifestHash !== '5a79777038acd2b5fda3b0416c0092e2c980ff0eff7e84a019fdac3bac8fdc04') throw new Error('registration result mismatch');
  const safe = { projectId: parsed.projectId, clientId: parsed.clientId, manifestHash: parsed.manifestHash, exitStatus: exit.code };
  writeJsonDurable(`${EVIDENCE}/project-registration-public.json`, safe);
  return safe;
}
async function waitGuiContact(helper, gui, guiLaunch) {
  for (let index = 1; index <= CONTACT_POLLS; index += 1) {
    if (existsSync(GUI_LOG)) {
      const line = readFileSync(GUI_LOG, 'utf8').split('\n').find((candidate) => candidate.includes('runtime.connectivity.bound'));
      if (line) {
        const matched = line.match(/^(\d{4}-\d{2}-\d{2}T[^ ]+) /);
        const wall = matched ? Date.parse(matched[1]) : NaN;
        if (!Number.isFinite(wall) || wall < guiLaunch.wallMs || wall - guiLaunch.wallMs > 500) throw new Error('contact timestamp outside sealed 0.5-second window');
        return { index, line, contactWallMs: wall, contactMonotonicMs: guiLaunch.monotonicMs + (wall - guiLaunch.wallMs) };
      }
    }
    await guardedWait(sleep(POLL_MS), [helper, gui], 'authenticated contact wait');
  }
  throw new Error('authenticated contact exceeded 5 x 0.1-second polls');
}

function snapshot(name, helper, gui) {
  verifyOwnedIdentity(helper); verifyOwnedIdentity(gui);
  const value = {
    capturedAt: new Date().toISOString(), monotonicMs: performance.now(),
    ps: runCapture('/bin/ps', ['-o', 'pid=,ppid=,pgid=,state=,etime=', '-p', `${helper.child.pid},${gui.child.pid}`]),
    helperUnix: runCapture('/usr/sbin/lsof', ['-nP', '-p', String(helper.child.pid), '-a', '-U']),
    helperTcp: runCapture('/usr/sbin/lsof', ['-nP', '-p', String(helper.child.pid), '-a', '-iTCP']),
    socketOwnerStat: runCapture('/usr/bin/stat', ['-f', '%N|%i|%p|%u|%g|%z', SOCKET, OWNER]),
    packageHashes: runCapture('/usr/bin/shasum', ['-a', '256', HELPER, `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar`, `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist`, GUI, `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar`])
  };
  writeJsonDurable(`${EVIDENCE}/${name}.json`, value);
  return value;
}
async function waitExpectedExit(owned) {
  const polls = [];
  for (let index = 1; index <= EXIT_POLLS; index += 1) {
    if (owned.exitResult) return { exited: true, exit: owned.exitResult, polls };
    polls.push({ index, monotonicMs: performance.now(), liveHandle: true });
    await Promise.race([sleep(POLL_MS), owned.exit]);
  }
  return { exited: Boolean(owned.exitResult), exit: owned.exitResult, polls };
}
async function settleOwned(owned, firstSignal) {
  if (!owned) return { present: false };
  if (owned.exitResult) return { present: true, alreadyExited: owned.exitResult };
  const first = signalOwned(owned, firstSignal);
  const firstExit = await Promise.race([owned.exit, sleep(3000).then(() => undefined)]);
  if (firstExit) return { present: true, first, exit: firstExit };
  const kill = signalOwned(owned, 'SIGKILL');
  const exit = await Promise.race([owned.exit, sleep(3000).then(() => { throw new Error(`${owned.label} did not reap after SIGKILL`); })]);
  return { present: true, first, kill, exit };
}

const result = { schema: 'chirality-dapp92-real-runtime-result-r2/v1', controllerPid: process.pid, status: 'INITIAL', startedAt: new Date().toISOString() };
let stale; let helper; let gui; let controllerIssued = false; let attachStarted = false;
try {
  if (!existsSync(ROOT) || !existsSync(HELPER) || !existsSync(GUI) || !existsSync(CLI)) throw new Error('runtime/package input missing');
  stale = spawnOwned(HELPER, ['--runtime-daemon'], 'stale-helper');
  await captureOwnedIdentity(stale);
  const staleReady = await waitReady(stale);
  result.stale = { identity: stale.identity, ready: staleReady, signal: signalOwned(stale, 'SIGKILL'), exit: await stale.exit };
  if (result.stale.exit.signal !== 'SIGKILL') throw new Error('stale helper exit mismatch');
  const staleSocket = statSync(SOCKET); const staleOwner = statSync(OWNER);
  if (staleSocket.ino !== staleReady.socket.inode || staleOwner.ino !== staleReady.ownerFile.inode) throw new Error('stale ownership changed');

  helper = spawnOwned(HELPER, ['--runtime-daemon'], 'helper');
  await captureOwnedIdentity(helper);
  const helperReady = await waitReady(helper);
  if (helperReady.socket.inode === staleReady.socket.inode || helperReady.ownerFile.inode === staleReady.ownerFile.inode) throw new Error('stale recovery did not replace identity');
  const readyWallMs = Date.now(); const readyMonotonicMs = performance.now();
  const controller = {
    schema: 'chirality-dapp92-real-runtime-controller-r2/v1', state: 'ATTACH_READY',
    controllerPid: process.pid, directChildPid: helper.child.pid, helperExecutable: HELPER,
    helperIdentity: helper.identity, readyWallMs, readyMonotonicMs,
    replayDeadlineMonotonicMs: readyMonotonicMs + REPLAY_LIMIT_MS,
    detachDeadlineMonotonicMs: readyMonotonicMs + DETACH_LIMIT_MS,
    helperReady
  };
  const controllerSha256 = writeJsonDurable(`${PROTOCOL}/controller.json`, controller);
  controllerIssued = true; result.controllerSha256 = controllerSha256;
  process.stdout.write(`${JSON.stringify({ ...controller, controllerSha256 })}\n`);

  const guiTarget = readyMonotonicMs + GUI_DELAY_MS;
  await waitSentinel('trace-ready.json', 'LLDB_TRACE_READY', helper.child.pid, guiTarget, [helper]);
  attachStarted = existsSync(`${PROTOCOL}/attach-started.json`);
  result.registration = await runRegistration(helper);
  const remaining = guiTarget - performance.now();
  if (remaining < 0) throw new Error('trace/registration exceeded GUI target');
  await guardedWait(sleep(remaining), [helper], '28-second GUI timer');
  verifyOwnedIdentity(helper);

  const guiLaunch = { wallMs: Date.now(), monotonicMs: performance.now() };
  gui = spawnOwned(GUI, [`--user-data-dir=${USER_DATA}`], 'gui');
  await captureOwnedIdentity(gui);
  guiLaunch.pid = gui.child.pid; guiLaunch.identity = gui.identity;
  guiLaunch.helperReadyToGuiMs = guiLaunch.monotonicMs - readyMonotonicMs;
  if (guiLaunch.helperReadyToGuiMs < 28000 || guiLaunch.helperReadyToGuiMs >= 28100) throw new Error('28.0-second GUI scheduler window missed');
  result.guiLaunch = guiLaunch;
  result.contact = await waitGuiContact(helper, gui, guiLaunch);
  const signalTarget = result.contact.contactMonotonicMs + SIGNAL_DELAY_MS;
  if (signalTarget > readyMonotonicMs + 130600) throw new Error('contact window leaves insufficient detach budget');
  result.preSignal = snapshot('pre-signal-snapshot', helper, gui);
  const armTarget = signalTarget - 2000;
  if (armTarget > performance.now()) await guardedWait(sleep(armTarget - performance.now()), [helper, gui], 'signal-arm timer');
  const armed = { schema: 'chirality-dapp92-real-runtime-signal-armed-r2/v1', state: 'SIGNAL_ARMED', directChildPid: helper.child.pid, signalTargetMonotonicMs: signalTarget };
  writeJsonDurable(`${PROTOCOL}/signal-armed.json`, armed); process.stdout.write(`${JSON.stringify(armed)}\n`);
  await waitSentinel('trace-live.json', 'LLDB_TRACE_LIVE', helper.child.pid, signalTarget, [helper, gui]);
  if (signalTarget > performance.now()) await guardedWait(sleep(signalTarget - performance.now()), [helper, gui], '102-second signal timer');
  result.signal = signalOwned(helper, 'SIGTERM');
  result.signal.contactToSignalMs = result.signal.monotonicMs - result.contact.contactMonotonicMs;
  if (result.signal.contactToSignalMs < 102000 || result.signal.contactToSignalMs >= 102100) throw new Error('102.0-second signal window missed');
  result.poll = await waitExpectedExit(helper);
  if (!result.poll.exited) throw new Error('helper survived 80 x 0.1-second post-signal polls');
  result.postSignal = { capturedAt: new Date().toISOString(), helperExit: result.poll.exit, guiIdentity: verifyOwnedIdentity(gui) };
  if (performance.now() >= readyMonotonicMs + REPLAY_LIMIT_MS) throw new Error('replay exceeded ready+139.5-second deadline');
  result.status = 'REPLAY_CAPTURED_AWAITING_LLDB_DETACH';
} catch (error) {
  result.status = attachStarted || existsSync(`${PROTOCOL}/attach-started.json`) ? 'FAILED_AWAITING_LLDB_DETACH' : 'FAILED_BEFORE_ATTACH';
  result.error = error instanceof Error ? error.message : String(error);
} finally {
  result.replayTerminalAt = new Date().toISOString();
  writeJsonDurable(`${PROTOCOL}/replay-terminal.json`, result);
  process.stdout.write(`${JSON.stringify({ schema: result.schema, status: result.status, directChildPid: helper?.child.pid })}\n`);
  const cleanup = { schema: 'chirality-dapp92-controller-cleanup-r2/v1', startedAt: new Date().toISOString(), controllerIssued };
  try {
    if (controllerIssued && existsSync(`${PROTOCOL}/attach-started.json`)) {
      const controller = readJson(`${PROTOCOL}/controller.json`);
      await waitSentinel('detached.json', 'LLDB_DETACHED_AND_TERMINAL', helper.child.pid, controller.detachDeadlineMonotonicMs, [gui]);
    }
    cleanup.gui = await settleOwned(gui, 'SIGTERM');
    cleanup.helper = await settleOwned(helper, 'SIGKILL');
    cleanup.stale = await settleOwned(stale, 'SIGKILL');
    cleanup.status = 'ALL_CONTROLLER_CHILDREN_REAPED';
  } catch (error) {
    cleanup.status = 'CLEANUP_FAILED'; cleanup.error = error instanceof Error ? error.message : String(error);
    result.cleanupBlocked = true;
  }
  cleanup.completedAt = new Date().toISOString();
  writeJsonDurable(`${EVIDENCE}/controller-cleanup-r2.json`, cleanup);
  if (!controllerIssued && cleanup.status === 'ALL_CONTROLLER_CHILDREN_REAPED') {
    writeJsonDurable(`${PROTOCOL}/pre-controller-cleanup-safe.json`, {
      schema: 'chirality-dapp92-pre-controller-cleanup-safe-r2/v1', state: 'NO_CONTROLLER_RECORD_ALL_CHILDREN_REAPED', cleanup
    });
  }
  result.completedAt = new Date().toISOString();
  writeJsonDurable(`${EVIDENCE}/protocol-result-r2.json`, result);
  process.stdout.write(`${JSON.stringify({ schema: result.schema, status: result.status, cleanup: cleanup.status })}\n`);
  if (cleanup.status !== 'ALL_CONTROLLER_CHILDREN_REAPED') process.exitCode = 2;
  else if (result.status !== 'REPLAY_CAPTURED_AWAITING_LLDB_DETACH') process.exitCode = 1;
}
