import {
  closeSync,
  createReadStream,
  existsSync,
  mkdirSync,
  openSync,
  readFileSync,
  renameSync,
  statSync,
  unlinkSync,
  writeFileSync
} from 'node:fs';
import { createHash } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
import { once } from 'node:events';
import { performance } from 'node:perf_hooks';
import path from 'node:path';

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
const READY_POLLS = 80;
const POLL_MS = 100;

mkdirSync(EVIDENCE, { recursive: true, mode: 0o700 });
mkdirSync(PROTOCOL, { recursive: true, mode: 0o700 });

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function sha256(bytes) {
  return createHash('sha256').update(bytes).digest('hex');
}

function writeJsonDurable(file, value) {
  const bytes = `${JSON.stringify(value, null, 2)}\n`;
  const temporary = `${file}.${process.pid}.tmp`;
  const descriptor = openSync(temporary, 'wx', 0o600);
  try {
    writeFileSync(descriptor, bytes, 'utf8');
  } finally {
    closeSync(descriptor);
  }
  renameSync(temporary, file);
  return sha256(bytes);
}

function readJson(file) {
  return JSON.parse(readFileSync(file, 'utf8'));
}

function ownerPublic(expectedPid) {
  const raw = readJson(OWNER);
  if (
    raw.schemaVersion !== 'chirality.daemon-owner/v1' ||
    raw.pid !== expectedPid ||
    !Number.isInteger(raw.pid) ||
    raw.pid <= 0 ||
    typeof raw.uid !== 'number' ||
    raw.socketPath !== SOCKET ||
    typeof raw.startedAt !== 'string'
  ) {
    throw new Error('owner-record schema/PID/path mismatch');
  }
  return {
    schemaVersion: raw.schemaVersion,
    pid: raw.pid,
    uid: raw.uid,
    socketPath: raw.socketPath,
    startedAt: raw.startedAt
  };
}

async function waitReady(expectedPid) {
  const polls = [];
  for (let index = 1; index <= READY_POLLS; index += 1) {
    const present = existsSync(SOCKET) && existsSync(OWNER);
    polls.push({ index, monotonicMs: performance.now(), present });
    if (present) {
      const owner = ownerPublic(expectedPid);
      const socketStat = statSync(SOCKET);
      const ownerStat = statSync(OWNER);
      return {
        owner,
        socket: { inode: socketStat.ino, mode: socketStat.mode, uid: socketStat.uid, gid: socketStat.gid },
        ownerFile: { inode: ownerStat.ino, mode: ownerStat.mode, uid: ownerStat.uid, gid: ownerStat.gid, size: ownerStat.size },
        polls
      };
    }
    await sleep(POLL_MS);
  }
  throw new Error('helper readiness exceeded 80 x 0.1-second polls');
}

function childExit(child) {
  return once(child, 'exit').then(([code, signal]) => ({ code, signal }));
}

function spawnLogged(executable, args, name) {
  const stdout = openSync(`${EVIDENCE}/${name}.stdout.log`, 'a', 0o600);
  const stderr = openSync(`${EVIDENCE}/${name}.stderr.log`, 'a', 0o600);
  const child = spawn('/usr/bin/env', [
    '-i',
    `PATH=${NODE_PATH}`,
    `HOME=${HOME}`,
    `CHIRALITY_USER_DATA=${USER_DATA}`,
    'CHIRALITY_SKIP_CLI_LAUNCHER=1',
    executable,
    ...args
  ], { cwd: REPO, stdio: ['ignore', stdout, stderr] });
  closeSync(stdout);
  closeSync(stderr);
  if (!Number.isInteger(child.pid) || child.pid <= 0) {
    throw new Error(`${name} did not yield a positive direct-child PID`);
  }
  return { child, exit: childExit(child) };
}

function runCapture(executable, args, options = {}) {
  const result = spawnSync(executable, args, {
    cwd: options.cwd ?? REPO,
    encoding: 'utf8',
    timeout: options.timeout ?? 10000,
    maxBuffer: 1024 * 1024,
    env: options.env
  });
  return {
    executable,
    args,
    status: result.status,
    signal: result.signal,
    stdout: result.stdout ?? '',
    stderr: result.stderr ?? '',
    error: result.error?.message
  };
}

function requireZero(result, name) {
  if (result.status !== 0 || result.signal !== null || result.error) {
    throw new Error(`${name} failed`);
  }
  return result;
}

function exactKill(signal, pid, allowAbsent = false) {
  const result = runCapture('/bin/kill', [`-${signal}`, String(pid)]);
  if (allowAbsent && result.status === 1) return result;
  return requireZero(result, `/bin/kill -${signal} ${pid}`);
}

async function waitExitPoll(pid) {
  const polls = [];
  for (let index = 1; index <= 80; index += 1) {
    const result = runCapture('/bin/kill', ['-0', String(pid)]);
    const alive = result.status === 0;
    polls.push({ index, monotonicMs: performance.now(), alive, status: result.status });
    if (!alive) return { exited: true, polls };
    await sleep(100);
  }
  return { exited: false, polls };
}

async function waitSentinel(name, state, pid, deadline) {
  const file = `${PROTOCOL}/${name}`;
  while (performance.now() <= deadline) {
    if (existsSync(file)) {
      const value = readJson(file);
      if (
        value.schema !== 'chirality-dapp92-real-runtime-sentinel/v1' ||
        value.directChildPid !== pid ||
        value.state !== state
      ) {
        throw new Error(`${name} schema/PID/state mismatch`);
      }
      return value;
    }
    await sleep(50);
  }
  throw new Error(`${name} timeout`);
}

async function runProjectRegistration() {
  const result = runCapture('/usr/bin/env', [
    '-i',
    `PATH=${NODE_PATH}`,
    `HOME=${HOME}`,
    `CHIRALITY_USER_DATA=${USER_DATA}`,
    'ELECTRON_RUN_AS_NODE=1',
    GUI,
    CLI,
    'project',
    'register',
    MANIFEST,
    '--approved-by',
    'D-APP-92',
    '--approval-reference',
    'D-APP-92-OPTION-A',
    '--json'
  ], { timeout: 10000 });
  requireZero(result, 'public project registration');
  if (result.stderr !== '') throw new Error('project registration emitted stderr');
  const parsed = JSON.parse(result.stdout);
  if (
    parsed.projectId !== 'chirality-app-dev' ||
    typeof parsed.clientId !== 'string' ||
    parsed.manifestHash !== '5a79777038acd2b5fda3b0416c0092e2c980ff0eff7e84a019fdac3bac8fdc04'
  ) {
    throw new Error('project registration public result mismatch');
  }
  const safe = {
    projectId: parsed.projectId,
    clientId: parsed.clientId,
    manifestHash: parsed.manifestHash,
    exitStatus: result.status
  };
  writeJsonDurable(`${EVIDENCE}/project-registration-public.json`, safe);
  return safe;
}

async function waitGuiContact(guiLaunch) {
  for (let index = 1; index <= 80; index += 1) {
    if (existsSync(GUI_LOG)) {
      const text = readFileSync(GUI_LOG, 'utf8');
      const line = text.split('\n').find((candidate) => candidate.includes('runtime.connectivity.bound'));
      if (line) {
        const matched = line.match(/^(\d{4}-\d{2}-\d{2}T[^ ]+) /);
        if (!matched) throw new Error('GUI bound line lacks timestamp');
        const contactWallMs = Date.parse(matched[1]);
        if (!Number.isFinite(contactWallMs)) throw new Error('GUI bound timestamp invalid');
        const contactMonotonicMs = guiLaunch.monotonicMs + (contactWallMs - guiLaunch.wallMs);
        return { index, line, contactWallMs, contactMonotonicMs };
      }
    }
    await sleep(100);
  }
  throw new Error('authenticated GUI contact exceeded 80 x 0.1-second polls');
}

function snapshot(name, helperPid, guiPid) {
  const results = {
    capturedAt: new Date().toISOString(),
    monotonicMs: performance.now(),
    ps: runCapture('/bin/ps', ['-o', 'pid=,ppid=,pgid=,state=,etime=', '-p', `${helperPid},${guiPid}`]),
    helperUnix: runCapture('/usr/sbin/lsof', ['-nP', '-p', String(helperPid), '-a', '-U']),
    helperTcp: runCapture('/usr/sbin/lsof', ['-nP', '-p', String(helperPid), '-a', '-iTCP']),
    socketOwnerStat: runCapture('/usr/bin/stat', ['-f', '%N|%i|%p|%u|%g|%z', SOCKET, OWNER]),
    packageHashes: runCapture('/usr/bin/shasum', [
      '-a', '256',
      HELPER,
      `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar`,
      `${REPO}/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist`,
      GUI,
      `${REPO}/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar`
    ])
  };
  writeJsonDurable(`${EVIDENCE}/${name}.json`, results);
  return results;
}

async function cleanupOwned(gui, helper, record) {
  const cleanup = { startedAt: new Date().toISOString() };
  if (gui) {
    cleanup.guiTerm = exactKill('TERM', gui.child.pid, true);
    cleanup.guiPoll = await waitExitPoll(gui.child.pid);
    if (!cleanup.guiPoll.exited) {
      cleanup.guiKill = exactKill('KILL', gui.child.pid, true);
      cleanup.guiPollAfterKill = await waitExitPoll(gui.child.pid);
    }
  }
  if (helper) {
    cleanup.helperPoll = await waitExitPoll(helper.child.pid);
    if (!cleanup.helperPoll.exited) {
      cleanup.helperKill = exactKill('KILL', helper.child.pid, true);
      cleanup.helperPollAfterKill = await waitExitPoll(helper.child.pid);
    }
  }
  cleanup.completedAt = new Date().toISOString();
  record.cleanup = cleanup;
  writeJsonDurable(`${EVIDENCE}/controller-cleanup.json`, cleanup);
}

const result = {
  schema: 'chirality-dapp92-real-runtime-result/v1',
  controllerPid: process.pid,
  status: 'INITIAL',
  startedAt: new Date().toISOString()
};
let helper;
let gui;
let traceReady = false;

try {
  if (!existsSync(ROOT) || !existsSync(HELPER) || !existsSync(GUI) || !existsSync(CLI)) {
    throw new Error('runtime root or exact packaged executable/CLI missing');
  }

  const stale = spawnLogged(HELPER, ['--runtime-daemon'], 'stale-helper');
  const staleReady = await waitReady(stale.child.pid);
  result.stale = { pid: stale.child.pid, ready: staleReady };
  exactKill('KILL', stale.child.pid);
  const staleExit = await stale.exit;
  if (staleExit.signal !== 'SIGKILL') throw new Error('stale helper did not exit by SIGKILL');
  const staleSocket = statSync(SOCKET);
  const staleOwner = statSync(OWNER);
  if (staleSocket.ino !== staleReady.socket.inode || staleOwner.ino !== staleReady.ownerFile.inode) {
    throw new Error('stale socket/owner identity changed before recovery');
  }

  helper = spawnLogged(HELPER, ['--runtime-daemon'], 'helper');
  const helperExit = helper.exit;
  const helperReady = await waitReady(helper.child.pid);
  if (
    helperReady.socket.inode === staleReady.socket.inode ||
    helperReady.ownerFile.inode === staleReady.ownerFile.inode
  ) {
    throw new Error('final helper did not replace stale socket/owner');
  }
  const readyWallMs = Date.now();
  const readyMonotonicMs = performance.now();
  const controllerRecord = {
    schema: 'chirality-dapp92-real-runtime-controller/v1',
    controllerPid: process.pid,
    directChildPid: helper.child.pid,
    helperExecutable: HELPER,
    helperArgv: ['--runtime-daemon'],
    state: 'ATTACH_READY',
    readyWallMs,
    readyMonotonicMs,
    helperReady
  };
  const controllerSha256 = writeJsonDurable(`${PROTOCOL}/controller.json`, controllerRecord);
  result.controllerRecordSha256 = controllerSha256;
  process.stdout.write(`${JSON.stringify({ ...controllerRecord, controllerSha256 })}\n`);

  const guiTarget = readyMonotonicMs + 28000;
  await waitSentinel('trace-ready.json', 'LLDB_TRACE_READY', helper.child.pid, guiTarget);
  traceReady = true;
  result.registration = await runProjectRegistration();
  const remaining = guiTarget - performance.now();
  if (remaining < 0) throw new Error('LLDB/registration exceeded 28.0-second helper-to-GUI bound');
  await sleep(remaining);

  const guiLaunch = { wallMs: Date.now(), monotonicMs: performance.now() };
  gui = spawnLogged(GUI, [`--user-data-dir=${USER_DATA}`], 'gui');
  guiLaunch.pid = gui.child.pid;
  guiLaunch.helperReadyToGuiMs = guiLaunch.monotonicMs - readyMonotonicMs;
  if (guiLaunch.helperReadyToGuiMs < 28000 || guiLaunch.helperReadyToGuiMs >= 28100) {
    throw new Error('helper-to-GUI observed delay outside sealed 28.0-second scheduler window');
  }
  result.guiLaunch = guiLaunch;
  result.contact = await waitGuiContact(guiLaunch);
  const signalTarget = result.contact.contactMonotonicMs + 102000;
  result.preSignal = snapshot('pre-signal-snapshot', helper.child.pid, gui.child.pid);

  const armTarget = signalTarget - 2000;
  const untilArm = armTarget - performance.now();
  if (untilArm > 0) await sleep(untilArm);
  const signalArmed = {
    schema: 'chirality-dapp92-real-runtime-signal-armed/v1',
    directChildPid: helper.child.pid,
    state: 'SIGNAL_ARMED',
    signalTargetMonotonicMs: signalTarget
  };
  writeJsonDurable(`${PROTOCOL}/signal-armed.json`, signalArmed);
  process.stdout.write(`${JSON.stringify(signalArmed)}\n`);
  await waitSentinel('trace-live.json', 'LLDB_TRACE_LIVE', helper.child.pid, signalTarget);
  const untilSignal = signalTarget - performance.now();
  if (untilSignal < 0) throw new Error('trace-live sentinel missed 102.0-second contact-to-signal bound');
  await sleep(untilSignal);

  result.signal = {
    command: `/bin/kill -TERM ${helper.child.pid}`,
    wallTime: new Date().toISOString(),
    monotonicMs: performance.now(),
    contactToSignalMs: performance.now() - result.contact.contactMonotonicMs
  };
  exactKill('TERM', helper.child.pid);
  result.poll = await waitExitPoll(helper.child.pid);
  result.helperExit = await Promise.race([helperExit, Promise.resolve(undefined)]);
  result.postSignal = snapshot('post-signal-snapshot', helper.child.pid, gui.child.pid);
  result.status = 'REPLAY_CAPTURED_AWAITING_LLDB_DETACH';
} catch (error) {
  result.status = traceReady ? 'FAILED_AWAITING_LLDB_DETACH' : 'FAILED_BEFORE_TRACE_READY';
  result.error = error instanceof Error ? error.message : String(error);
} finally {
  result.replayTerminalAt = new Date().toISOString();
  writeJsonDurable(`${PROTOCOL}/replay-terminal.json`, result);
  process.stdout.write(`${JSON.stringify({ schema: result.schema, directChildPid: helper?.child.pid, status: result.status })}\n`);

  if (helper && (traceReady || existsSync(`${PROTOCOL}/attach-started.json`))) {
    try {
      await waitSentinel('detached.json', 'LLDB_DETACHED_AND_TERMINAL', helper.child.pid, performance.now() + 30000);
      await cleanupOwned(gui, helper, result);
    } catch (cleanupError) {
      result.cleanupBlocked = true;
      result.cleanupError = cleanupError instanceof Error ? cleanupError.message : String(cleanupError);
    }
  } else {
    await cleanupOwned(gui, helper, result);
  }
  result.completedAt = new Date().toISOString();
  writeJsonDurable(`${EVIDENCE}/protocol-result.json`, result);
  process.stdout.write(`${JSON.stringify({ schema: result.schema, status: result.status, cleanupBlocked: Boolean(result.cleanupBlocked) })}\n`);
  if (result.cleanupBlocked) process.exitCode = 2;
  else if (result.status !== 'REPLAY_CAPTURED_AWAITING_LLDB_DETACH') process.exitCode = 1;
}
