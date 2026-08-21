#!/usr/bin/env node

import { spawn } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';
import {
  access,
  constants,
  lstat,
  mkdir,
  readFile,
  realpath,
  rename,
  rm,
  stat,
  unlink,
  writeFile
} from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import {
  DEFAULT_LAUNCH_AGENT_LABEL,
  assertExactRuntimeArguments,
  inspectInstalledPlist,
  isExactLaunchctlNotFound,
  parseLaunchctlJob,
  validateProofLabel
} from './run-packaged-launchagent-runatload-proof.mjs';

export const SESSION_SCHEMA = 'chirality-packaged-launchagent-login-proof-session/v1';
const CAPTURE_STATE_SCHEMA = 'chirality-packaged-launchagent-login-proof-capture-state/v1';
export const SUMMARY_SCHEMA = 'chirality-packaged-launchagent-login-proof/v1';
export const EVIDENCE_SCHEMA = 'chirality-packaged-launchagent-login-proof-evidence/v1';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const defaultAppPath = path.join(frontendRoot, 'dist', 'mac-arm64', 'Chirality.app');
const defaultSessionRoot = path.join(
  frontendRoot,
  'artifacts',
  'release-verification',
  'launchagent-login-proof'
);
const commandTimeoutMs = 60_000;
const cleanupAttempts = 5;
const cleanupPollMs = 150;

const optionNames = new Map([
  ['--app-path', 'appPath'],
  ['--session-root', 'sessionRoot'],
  ['--label', 'label'],
  ['--source-revision', 'sourceRevision']
]);

function parseArgs(argv) {
  const [command, ...tokens] = argv;
  if (command !== 'prepare' && command !== 'capture') {
    throw new Error('First argument must be prepare or capture');
  }
  const options = {};
  for (let index = 0; index < tokens.length; index += 1) {
    const token = tokens[index];
    const name = optionNames.get(token);
    if (!name) throw new Error(`Unknown argument: ${token}`);
    const value = tokens[index + 1];
    if (!value || value.startsWith('--')) throw new Error(`Missing value for ${token}`);
    options[name] = value;
    index += 1;
  }
  if (command === 'capture' && Object.keys(options).some((name) => name !== 'sessionRoot')) {
    throw new Error('Capture accepts only --session-root');
  }
  return { command, options };
}

function preparseSessionRoot(argv) {
  const index = argv.indexOf('--session-root');
  const requested = index === -1 ? undefined : argv[index + 1];
  return path.resolve(
    requested && !requested.startsWith('--') ? requested : defaultSessionRoot
  );
}

function wait(delayMs) {
  return new Promise((resolve) => setTimeout(resolve, delayMs));
}

function commandText(executable, args) {
  return [executable, ...args].map((part) => JSON.stringify(part)).join(' ');
}

async function defaultRunCommand({ executable, args, cwd, env, timeoutMs = commandTimeoutMs }) {
  return new Promise((resolve, reject) => {
    const child = spawn(executable, args, { cwd, env, stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = '';
    let stderr = '';
    let settled = false;
    const timer = setTimeout(() => {
      child.kill('SIGKILL');
      if (!settled) {
        settled = true;
        reject(new Error(`Command exceeded ${timeoutMs}ms: ${commandText(executable, args)}`));
      }
    }, timeoutMs);
    child.stdout.setEncoding('utf8');
    child.stderr.setEncoding('utf8');
    child.stdout.on('data', (chunk) => {
      stdout += chunk;
    });
    child.stderr.on('data', (chunk) => {
      stderr += chunk;
    });
    child.once('error', (error) => {
      clearTimeout(timer);
      if (!settled) {
        settled = true;
        reject(error);
      }
    });
    child.once('exit', (code, signal) => {
      clearTimeout(timer);
      if (!settled) {
        settled = true;
        resolve({ exitCode: code ?? 1, signal, stdout, stderr });
      }
    });
  });
}

function defaultProcessAlive(pid) {
  try {
    process.kill(pid, 0);
    return true;
  } catch (error) {
    return error?.code === 'EPERM';
  }
}

async function defaultInspectProcessExecutables(pid, runCommand) {
  const result = await runCommand({
    executable: '/usr/sbin/lsof',
    args: ['-a', '-p', String(pid), '-d', 'txt', '-Fn'],
    timeoutMs: 10_000
  });
  if (result.exitCode !== 0) {
    throw new Error(`Unable to inspect launched process executable (lsof exit ${result.exitCode})`);
  }
  return result.stdout
    .split(/\r?\n/u)
    .filter((line) => line.startsWith('n'))
    .map((line) => line.slice(1))
    .filter(Boolean);
}

function dependencies(overrides = {}) {
  const runCommand = overrides.runCommand ?? defaultRunCommand;
  return {
    platform: overrides.platform ?? process.platform,
    environment: overrides.environment ?? process.env,
    userInfo: overrides.userInfo ?? (() => os.userInfo()),
    uid: overrides.uid ?? (() => process.getuid?.()),
    now: overrides.now ?? (() => new Date()),
    randomId: overrides.randomId ?? (() => randomUUID()),
    runCommand,
    processAlive: overrides.processAlive ?? defaultProcessAlive,
    inspectProcessExecutables:
      overrides.inspectProcessExecutables ??
      ((pid) => defaultInspectProcessExecutables(pid, runCommand))
  };
}

function isWithin(candidate, parent) {
  const relative = path.relative(parent, candidate);
  return (
    relative === '' ||
    (!relative.startsWith(`..${path.sep}`) && relative !== '..' && !path.isAbsolute(relative))
  );
}

async function assertNoSymlinkAncestors(candidate) {
  const absolute = path.resolve(candidate);
  const parsed = path.parse(absolute);
  let current = parsed.root;
  for (const segment of absolute.slice(parsed.root.length).split(path.sep).filter(Boolean)) {
    current = path.join(current, segment);
    try {
      if ((await lstat(current)).isSymbolicLink()) {
        throw new Error(`Session path has a symbolic-link ancestor: ${current}`);
      }
    } catch (error) {
      if (error?.code === 'ENOENT') break;
      throw error;
    }
  }
  return absolute;
}

async function sha256File(filePath) {
  return createHash('sha256').update(await readFile(filePath)).digest('hex');
}

async function fileSnapshot(filePath) {
  try {
    const metadata = await stat(filePath);
    if (!metadata.isFile()) throw new Error('protected path is not a regular file');
    return { present: true, bytes: metadata.size, sha256: await sha256File(filePath) };
  } catch (error) {
    if (error?.code === 'ENOENT') return { present: false };
    throw error;
  }
}

async function writeJsonAtomic(filePath, value) {
  await mkdir(path.dirname(filePath), { recursive: true, mode: 0o700 });
  const temporary = `${filePath}.${process.pid}.${Date.now()}.tmp`;
  await writeFile(temporary, `${JSON.stringify(value, null, 2)}\n`, {
    encoding: 'utf8',
    mode: 0o600,
    flag: 'wx'
  });
  await rename(temporary, filePath);
}

function launchctlClassification(result, service) {
  if (result.exitCode === 0) return 'LOADED';
  if (isExactLaunchctlNotFound(result, service)) return 'NOT_FOUND';
  throw new Error(`Unexpected launchctl print failure for proof service (exit ${result.exitCode})`);
}

async function jobState(service, deps) {
  const result = await deps.runCommand({
    executable: '/bin/launchctl',
    args: ['print', service]
  });
  return { classification: launchctlClassification(result, service), result };
}

async function protectedState(defaultPlistPath, defaultService, deps) {
  const [plist, job] = await Promise.all([
    fileSnapshot(defaultPlistPath),
    jobState(defaultService, deps)
  ]);
  return { plist, jobLoaded: job.classification === 'LOADED' };
}

async function canonicalPackagedExecutables(paths) {
  const candidates = [];
  for (const candidate of paths) {
    if (!/\.app\/Contents\/MacOS\/Chirality$/u.test(candidate)) continue;
    candidates.push(await realpath(candidate).catch(() => path.resolve(candidate)));
  }
  return [...new Set(candidates)];
}

async function validateAccount(deps) {
  if (deps.platform !== 'darwin') throw new Error('LaunchAgent login proof requires macOS');
  const uid = deps.uid();
  if (!Number.isSafeInteger(uid) || uid < 1) throw new Error('A non-root GUI user is required');
  const accountHome = deps.userInfo().homedir;
  if (!accountHome || !deps.environment.HOME) throw new Error('HOME and account home are required');
  const canonicalAccountHome = await realpath(accountHome);
  const canonicalEnvironmentHome = await realpath(deps.environment.HOME);
  if (canonicalAccountHome !== canonicalEnvironmentHome) {
    throw new Error('HOME does not resolve to the current account home');
  }
  return { uid, home: canonicalAccountHome };
}

function redact(message, replacements) {
  let result = message instanceof Error ? message.message : String(message);
  for (const [value, replacement] of replacements) {
    if (value) result = result.replaceAll(value, replacement);
  }
  return result.replaceAll(/[\r\n\t]+/gu, ' ').slice(0, 500);
}

function validateSourceRevision(value) {
  if (typeof value !== 'string' || value.trim() === '') {
    throw new Error('Source revision is required');
  }
  const revision = value.trim();
  if (!/^[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}$/u.test(revision)) {
    throw new Error('Source revision must be a path-free revision identifier');
  }
  if (
    new Set(['unavailable', 'unknown', 'none', 'null', 'n-a', 'na', 'tbd', 'placeholder']).has(
      revision.toLowerCase()
    )
  ) {
    throw new Error('Source revision must not be a placeholder');
  }
  return revision;
}

async function loginSessionIdentity(uid, deps) {
  const result = await deps.runCommand({
    executable: '/usr/bin/osascript',
    args: [
      '-l',
      'JavaScript',
      '-e',
      'ObjC.import("CoreGraphics"); JSON.stringify(ObjC.deepUnwrap($.CGSessionCopyCurrentDictionary()))'
    ]
  });
  if (result.exitCode !== 0 || result.stderr.trim() !== '') {
    throw new Error(`Unable to inspect the current GUI login session (exit ${result.exitCode})`);
  }
  let record;
  try {
    record = JSON.parse(result.stdout);
  } catch {
    throw new Error('Current GUI login-session identity is not valid JSON');
  }
  const sessionId = record?.kCGSSessionIDKey;
  const sessionUid = record?.kCGSessionUserIDKey;
  if (
    record?.kCGSessionOnConsoleKey !== true ||
    record?.kCGSessionLoginDoneKey !== true ||
    !Number.isSafeInteger(sessionId) ||
    sessionId < 1 ||
    sessionUid !== uid
  ) {
    throw new Error('Current GUI login-session identity is missing, ambiguous, or incomplete');
  }
  return createHash('sha256').update(`${uid}:${sessionId}`).digest('hex');
}

async function assertCleanupTargets({ uid, home, label, service, sessionRoot, plistPath, runtimeRoot }) {
  validateProofLabel(label);
  const expectedPlist = path.join(home, 'Library', 'LaunchAgents', `${label}.plist`);
  const expectedRuntime = path.join(sessionRoot, 'runtime-data');
  if (
    service !== `gui/${uid}/${label}` ||
    plistPath !== expectedPlist ||
    runtimeRoot !== expectedRuntime
  ) {
    throw new Error('Proof cleanup targets are inconsistent with the owned session');
  }
  if (label === DEFAULT_LAUNCH_AGENT_LABEL || `gui/${uid}/${label}` === `gui/${uid}/${DEFAULT_LAUNCH_AGENT_LABEL}`) {
    throw new Error('Proof cleanup cannot target the default LaunchAgent');
  }
  const runtimeMetadata = await lstat(runtimeRoot).catch((error) => {
    if (error?.code === 'ENOENT') return undefined;
    throw error;
  });
  if (runtimeMetadata?.isSymbolicLink() || (runtimeMetadata && !runtimeMetadata.isDirectory())) {
    throw new Error('Proof runtime cleanup target is not an owned directory');
  }
  const plistMetadata = await lstat(plistPath).catch((error) => {
    if (error?.code === 'ENOENT') return undefined;
    throw error;
  });
  if (plistMetadata?.isSymbolicLink() || (plistMetadata && !plistMetadata.isFile())) {
    throw new Error('Proof plist cleanup target is not an owned regular file');
  }
}

async function assertProofOwnedLoadedJob({ result, executablePath, deps }) {
  const job = parseLaunchctlJob(result.stdout);
  if (job.state !== 'running') {
    throw new Error(`Refusing proof-service bootout because loaded job state was ${job.state}`);
  }
  if (typeof job.program !== 'string' || path.resolve(job.program) !== executablePath) {
    throw new Error('Refusing proof-service bootout because loaded job program is missing or mismatched');
  }
  if (job.programArguments === undefined) {
    throw new Error('Refusing proof-service bootout because loaded job arguments are missing');
  }
  try {
    assertExactRuntimeArguments(job.programArguments, executablePath, 'Loaded cleanup job');
  } catch {
    throw new Error('Refusing proof-service bootout because loaded job arguments are mismatched');
  }
  if (!Number.isSafeInteger(job.pid) || job.pid < 1) {
    throw new Error('Refusing proof-service bootout because loaded job PID is missing or invalid');
  }
  const processExecutables = await canonicalPackagedExecutables(
    await deps.inspectProcessExecutables(job.pid)
  );
  if (processExecutables.length !== 1 || processExecutables[0] !== executablePath) {
    throw new Error(
      'Refusing proof-service bootout because executable identity is missing, ambiguous, or mismatched'
    );
  }
}

async function cleanupProof({
  uid,
  home,
  label,
  service,
  sessionRoot,
  plistPath,
  runtimeRoot,
  executablePath,
  deps
}) {
  await assertCleanupTargets({ uid, home, label, service, sessionRoot, plistPath, runtimeRoot });
  const errors = [];
  let jobAbsent = false;
  let jobMutationRefused = false;
  for (let attempt = 0; attempt < cleanupAttempts; attempt += 1) {
    try {
      const current = await jobState(service, deps);
      if (current.classification === 'NOT_FOUND') {
        jobAbsent = true;
        break;
      }
      try {
        await assertProofOwnedLoadedJob({
          result: current.result,
          executablePath,
          deps
        });
      } catch (error) {
        errors.push(error instanceof Error ? error.message : String(error));
        jobMutationRefused = true;
        break;
      }
      const bootout = await deps.runCommand({
        executable: '/bin/launchctl',
        args: ['bootout', service]
      });
      if (bootout.exitCode !== 0) {
        errors.push(`LaunchAgent bootout attempt ${attempt + 1} failed with exit ${bootout.exitCode}`);
      }
    } catch (error) {
      errors.push(error instanceof Error ? error.message : String(error));
    }
    await wait(cleanupPollMs);
  }
  if (!jobAbsent) {
    try {
      jobAbsent = (await jobState(service, deps)).classification === 'NOT_FOUND';
    } catch (error) {
      errors.push(error instanceof Error ? error.message : String(error));
    }
  }
  try {
    await unlink(plistPath).catch((error) => {
      if (error?.code !== 'ENOENT') throw error;
    });
  } catch (error) {
    errors.push(`Unable to remove proof plist: ${error instanceof Error ? error.message : String(error)}`);
  }
  try {
    await rm(runtimeRoot, { recursive: true, force: true });
  } catch (error) {
    errors.push(`Unable to remove proof runtime data: ${error instanceof Error ? error.message : String(error)}`);
  }
  const plistAbsent = !(await fileSnapshot(plistPath)).present;
  return {
    jobAbsent,
    jobMutationRefused,
    plistAbsent,
    runtimeDataRemoved: !(await stat(runtimeRoot).then(() => true).catch(() => false)),
    errors
  };
}

async function prepare(options, deps, sessionRoot, sourceRevision) {
  const { uid, home } = await validateAccount(deps);
  const launchAgentsDirectory = path.join(home, 'Library', 'LaunchAgents');
  await mkdir(launchAgentsDirectory, { recursive: true, mode: 0o700 });
  const appPath = await realpath(path.resolve(options.appPath ?? defaultAppPath));
  if (path.basename(appPath) !== 'Chirality.app') throw new Error('App path must identify Chirality.app');
  const executablePath = await realpath(path.join(appPath, 'Contents', 'MacOS', 'Chirality'));
  const cliEntry = await realpath(
    path.join(appPath, 'Contents', 'Resources', 'runtime-cli', 'chirality-cli.mjs')
  );
  if (!isWithin(executablePath, appPath) || !isWithin(cliEntry, appPath)) {
    throw new Error('Packaged executable identity escapes the app bundle');
  }
  if (
    isWithin(sessionRoot, launchAgentsDirectory) ||
    isWithin(launchAgentsDirectory, sessionRoot) ||
    isWithin(sessionRoot, appPath) ||
    isWithin(appPath, sessionRoot)
  ) {
    throw new Error('Proof session root must be disjoint from the app and LaunchAgents directory');
  }
  await access(executablePath, constants.X_OK);
  await access(cliEntry, constants.R_OK);

  const label = validateProofLabel(
    options.label ??
      `com.chirality.ci.runatload.login.${process.pid}.${deps.randomId().replaceAll('-', '').slice(0, 8)}`
  );
  const plistPath = path.join(launchAgentsDirectory, `${label}.plist`);
  const service = `gui/${uid}/${label}`;
  if ((await fileSnapshot(plistPath)).present) {
    throw new Error('Proof plist already exists; refusing to overwrite it');
  }
  if ((await jobState(service, deps)).classification !== 'NOT_FOUND') {
    throw new Error('Proof job already exists; refusing to take ownership');
  }
  const defaultPlistPath = path.join(
    launchAgentsDirectory,
    `${DEFAULT_LAUNCH_AGENT_LABEL}.plist`
  );
  const defaultService = `gui/${uid}/${DEFAULT_LAUNCH_AGENT_LABEL}`;
  const defaultBefore = await protectedState(defaultPlistPath, defaultService, deps);
  const preparedLoginSessionSha256 = await loginSessionIdentity(uid, deps);
  const runtimeRoot = path.join(sessionRoot, 'runtime-data');
  await mkdir(runtimeRoot, { recursive: true, mode: 0o700 });

  let installAttempted = false;
  try {
    installAttempted = true;
    const install = await deps.runCommand({
      executable: executablePath,
      args: [cliEntry, 'daemon', 'install', '--executable', executablePath],
      cwd: frontendRoot,
      env: {
        ...deps.environment,
        HOME: home,
        ELECTRON_RUN_AS_NODE: '1',
        CHIRALITY_SKIP_CLI_LAUNCHER: '1',
        CHIRALITY_LAUNCH_AGENTS_DIRECTORY: launchAgentsDirectory,
        CHIRALITY_USER_DATA: runtimeRoot,
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: label,
        CHIRALITY_RUNTIME_KEEP_ALIVE: 'always',
        CHIRALITY_RUNTIME_RUN_AT_LOAD: 'true'
      }
    });
    if (install.exitCode !== 0) throw new Error(`Packaged CLI install failed with exit ${install.exitCode}`);
    const plist = inspectInstalledPlist(await readFile(plistPath, 'utf8'));
    if (plist.label !== label) throw new Error('Installed plist label does not match proof label');
    assertExactRuntimeArguments(plist.programArguments, executablePath, 'Installed plist');
    if (!plist.runAtLoad) throw new Error('Installed plist does not enable RunAtLoad');
    if ((await jobState(service, deps)).classification !== 'NOT_FOUND') {
      throw new Error('Prepare unexpectedly loaded the proof job');
    }
    const prepared = {
      schema: SESSION_SCHEMA,
      status: 'PREPARED',
      preparedAt: deps.now().toISOString(),
      sourceRevision,
      label,
      service,
      plist: `~/Library/LaunchAgents/${label}.plist`,
      plistSha256: await sha256File(plistPath),
      app: {
        path: '<packaged-app>',
        executableSha256: await sha256File(executablePath)
      },
      runtimeData: '<proof-session>/runtime-data',
      preparedLoginSessionSha256,
      preparedJobAbsent: true,
      defaultProtection: {
        label: DEFAULT_LAUNCH_AGENT_LABEL,
        plist: `~/Library/LaunchAgents/${DEFAULT_LAUNCH_AGENT_LABEL}.plist`,
        recordedOnly: true
      },
      prepareMutations: ['packaged-cli-install'],
      bootstrapInvoked: false,
      kickstartInvoked: false,
      proofClaimed: false
    };
    const preparedPath = path.join(sessionRoot, 'prepared.json');
    await writeJsonAtomic(preparedPath, prepared);
    await writeJsonAtomic(path.join(sessionRoot, '.capture-state.json'), {
      schema: CAPTURE_STATE_SCHEMA,
      status: 'PREPARED',
      preparedManifestSha256: await sha256File(preparedPath),
      uid,
      home,
      label,
      service,
      plistPath,
      plistSha256: prepared.plistSha256,
      appPath,
      executablePath,
      executableSha256: prepared.app.executableSha256,
      runtimeRoot,
      defaultPlistPath,
      defaultService,
      defaultBefore,
      preparedAt: prepared.preparedAt,
      preparedLoginSessionSha256,
      sourceRevision
    });
    return {
      status: 'PREPARED',
      sessionRoot: '<proof-session>',
      label,
      next: 'Owner performs one logout/login act, then runs the single capture command.',
      proofClaimed: false
    };
  } catch (error) {
    if (!installAttempted) throw error;
    const replacements = [
      [home, '~'],
      [appPath, '<packaged-app>'],
      [executablePath, '<packaged-executable>'],
      [runtimeRoot, '<proof-runtime>'],
      [sessionRoot, '<proof-session>']
    ];
    let cleanup;
    try {
      cleanup = await cleanupProof({
        uid,
        home,
        label,
        service,
        sessionRoot,
        plistPath,
        runtimeRoot,
        executablePath,
        deps
      });
    } catch (cleanupError) {
      throw new Error(
        `${redact(error, replacements)}; install-attempt cleanup failed before residual verification: ${redact(cleanupError, replacements)}`
      );
    }
    const cleanupComplete = cleanup.jobAbsent && cleanup.plistAbsent && cleanup.runtimeDataRemoved;
    const residuals = [
      `job=${cleanup.jobAbsent ? 'absent' : 'present-or-unknown'}`,
      `job-mutation-refused=${cleanup.jobMutationRefused}`,
      `plist=${cleanup.plistAbsent ? 'absent' : 'present'}`,
      `runtime-data=${cleanup.runtimeDataRemoved ? 'absent' : 'present'}`
    ].join(', ');
    const cleanupErrors = cleanup.errors.map((cleanupEntry) => redact(cleanupEntry, replacements));
    throw new Error(
      `${redact(error, replacements)}; install-attempt cleanup ${cleanupComplete ? 'complete' : 'incomplete'} (${residuals})${
        cleanupErrors.length > 0 ? `; cleanup errors: ${cleanupErrors.join('; ')}` : ''
      }`
    );
  }
}

async function capture(deps, sessionRoot) {
  const preparedPath = path.join(sessionRoot, 'prepared.json');
  const captureStatePath = path.join(sessionRoot, '.capture-state.json');
  const consumedStatePath = path.join(sessionRoot, '.capture-state.consumed.json');
  for (const output of ['summary.json', 'evidence-package.json', '.capture-state.consumed.json']) {
    if ((await fileSnapshot(path.join(sessionRoot, output))).present) {
      throw new Error('Capture session was already consumed or contains stale evidence');
    }
  }
  const preparedBytes = await readFile(preparedPath, 'utf8');
  const prepared = JSON.parse(preparedBytes);
  if (prepared.schema !== SESSION_SCHEMA || prepared.status !== 'PREPARED') {
    throw new Error('Prepared session is missing or invalid');
  }
  const captureState = JSON.parse(await readFile(captureStatePath, 'utf8'));
  if (captureState.schema !== CAPTURE_STATE_SCHEMA || captureState.status !== 'PREPARED') {
    throw new Error('Private capture state is missing or invalid');
  }
  if ((await sha256File(preparedPath)) !== captureState.preparedManifestSha256) {
    throw new Error('Prepared manifest does not match the bound capture state');
  }
  const { uid, home } = await validateAccount(deps);
  if (captureState.uid !== uid || captureState.home !== home) {
    throw new Error('Prepared session belongs to a different GUI account');
  }
  validateProofLabel(captureState.label);
  const expectedPlist = path.join(home, 'Library', 'LaunchAgents', `${captureState.label}.plist`);
  const expectedRuntime = path.join(sessionRoot, 'runtime-data');
  if (
    captureState.plistPath !== expectedPlist ||
    captureState.runtimeRoot !== expectedRuntime ||
    captureState.service !== `gui/${uid}/${captureState.label}` ||
    prepared.label !== captureState.label ||
    prepared.service !== captureState.service ||
    prepared.plistSha256 !== captureState.plistSha256 ||
    prepared.app?.executableSha256 !== captureState.executableSha256 ||
    prepared.preparedLoginSessionSha256 !== captureState.preparedLoginSessionSha256 ||
    prepared.sourceRevision !== captureState.sourceRevision
  ) {
    throw new Error('Prepared LaunchAgent identity is inconsistent');
  }
  const canonicalAppPath = await realpath(captureState.appPath);
  const canonicalExecutablePath = await realpath(
    path.join(canonicalAppPath, 'Contents', 'MacOS', 'Chirality')
  );
  if (
    canonicalAppPath !== captureState.appPath ||
    path.basename(canonicalAppPath) !== 'Chirality.app' ||
    canonicalExecutablePath !== captureState.executablePath ||
    !isWithin(canonicalExecutablePath, canonicalAppPath) ||
    captureState.defaultPlistPath !==
      path.join(home, 'Library', 'LaunchAgents', `${DEFAULT_LAUNCH_AGENT_LABEL}.plist`) ||
    captureState.defaultService !== `gui/${uid}/${DEFAULT_LAUNCH_AGENT_LABEL}`
  ) {
    throw new Error('Prepared packaged-app or protected default identity is inconsistent');
  }
  const sourceRevision = validateSourceRevision(captureState.sourceRevision);
  if (prepared.sourceRevision !== sourceRevision) {
    throw new Error('Prepared source revision does not match the bound capture state');
  }
  await assertCleanupTargets({
    uid,
    home,
    label: captureState.label,
    service: captureState.service,
    sessionRoot,
    plistPath: captureState.plistPath,
    runtimeRoot: captureState.runtimeRoot
  });
  await rename(captureStatePath, consumedStatePath);

  const summary = {
    schema: SUMMARY_SCHEMA,
    status: 'FAIL',
    timestamp: deps.now().toISOString(),
    scope: 'owner-scheduled-login-session-packaged-app-only',
    sourceRevision,
    launchAgent: {
      label: captureState.label,
      launchAgentsDirectory: '~/Library/LaunchAgents',
      plist: `~/Library/LaunchAgents/${captureState.label}.plist`,
      preparedJobAbsent: true,
      bootstrapInvoked: false,
      kickstartInvoked: false,
      runAtLoad: false,
      loginDiscoveredJobObserved: false,
      loadedProgramMatches: false,
      loadedArgumentsAvailable: false,
      loadedArgumentsMatch: null
    },
    loginSession: {
      preparedIdentitySha256: captureState.preparedLoginSessionSha256,
      capturedIdentitySha256: null,
      identityTransitionObserved: false
    },
    process: { pidObserved: false, executableIdentityMatches: false },
    cleanup: {
      processAbsent: false,
      jobAbsent: false,
      jobMutationRefused: false,
      plistAbsent: false,
      runtimeDataRemoved: false
    },
    defaultProtection: {
      label: DEFAULT_LAUNCH_AGENT_LABEL,
      plist: `~/Library/LaunchAgents/${DEFAULT_LAUNCH_AGENT_LABEL}.plist`,
      plistUnchanged: false,
      jobLoadedStateUnchanged: false,
      mutationTargetsExcluded: true
    },
    proofBoundary: {
      ownerLogoutLoginActRequired: true,
      harnessPerformedLogoutLogin: false,
      preparationClaimedProof: false
    }
  };
  let observedPid;
  let proofError;
  try {
    const capturedLoginSessionSha256 = await loginSessionIdentity(uid, deps);
    summary.loginSession.capturedIdentitySha256 = capturedLoginSessionSha256;
    if (capturedLoginSessionSha256 === captureState.preparedLoginSessionSha256) {
      throw new Error('Current GUI login session is the same session recorded during preparation');
    }
    summary.loginSession.identityTransitionObserved = true;
    if ((await sha256File(captureState.plistPath)) !== captureState.plistSha256) {
      throw new Error('Prepared plist bytes changed before capture');
    }
    if ((await sha256File(captureState.executablePath)) !== captureState.executableSha256) {
      throw new Error('Packaged executable bytes changed before capture');
    }
    const plist = inspectInstalledPlist(await readFile(captureState.plistPath, 'utf8'));
    if (plist.label !== captureState.label) throw new Error('Prepared plist label changed');
    assertExactRuntimeArguments(plist.programArguments, captureState.executablePath, 'Prepared plist');
    if (!plist.runAtLoad) throw new Error('Prepared plist no longer enables RunAtLoad');
    summary.launchAgent.runAtLoad = true;

    const captured = await jobState(captureState.service, deps);
    if (captured.classification !== 'LOADED') {
      throw new Error('Prepared job was not discovered in the current login session');
    }
    const job = parseLaunchctlJob(captured.result.stdout);
    observedPid = job.pid;
    summary.process.pidObserved = true;
    if (job.state !== 'running') throw new Error(`Prepared job state was ${job.state}`);
    if (path.resolve(job.program) !== captureState.executablePath) {
      throw new Error('Loaded job program does not match prepared packaged executable');
    }
    summary.launchAgent.loadedProgramMatches = true;
    summary.launchAgent.loadedArgumentsAvailable = job.programArguments !== undefined;
    if (job.programArguments === undefined) throw new Error('Loaded job arguments are missing');
    assertExactRuntimeArguments(job.programArguments, captureState.executablePath, 'Loaded job');
    summary.launchAgent.loadedArgumentsMatch = true;
    const processExecutables = await canonicalPackagedExecutables(
      await deps.inspectProcessExecutables(observedPid)
    );
    if (processExecutables.length !== 1 || processExecutables[0] !== captureState.executablePath) {
      throw new Error('Launched process executable identity is missing or ambiguous');
    }
    summary.process.executableIdentityMatches = true;
    summary.launchAgent.loginDiscoveredJobObserved = true;
    summary.app = {
      path: 'dist/mac-arm64/Chirality.app',
      executableSha256: captureState.executableSha256
    };
  } catch (error) {
    proofError = error;
  }

  const cleanup = await cleanupProof({
    uid,
    home,
    label: captureState.label,
    service: captureState.service,
    sessionRoot,
    plistPath: captureState.plistPath,
    runtimeRoot: captureState.runtimeRoot,
    executablePath: captureState.executablePath,
    deps
  });
  summary.cleanup = {
    processAbsent: observedPid !== undefined && !deps.processAlive(observedPid),
    jobAbsent: cleanup.jobAbsent,
    jobMutationRefused: cleanup.jobMutationRefused,
    plistAbsent: cleanup.plistAbsent,
    runtimeDataRemoved: cleanup.runtimeDataRemoved
  };
  try {
    const defaultAfter = await protectedState(captureState.defaultPlistPath, captureState.defaultService, deps);
    summary.defaultProtection.plistUnchanged =
      JSON.stringify(captureState.defaultBefore.plist) === JSON.stringify(defaultAfter.plist);
    summary.defaultProtection.jobLoadedStateUnchanged =
      captureState.defaultBefore.jobLoaded === defaultAfter.jobLoaded;
  } catch (error) {
    cleanup.errors.push(error instanceof Error ? error.message : String(error));
  }

  const cleanupComplete =
    summary.cleanup.processAbsent &&
    summary.cleanup.jobAbsent &&
    summary.cleanup.plistAbsent &&
    summary.cleanup.runtimeDataRemoved;
  const defaultProtected = Object.values(summary.defaultProtection)
    .filter((value) => typeof value === 'boolean')
    .every(Boolean);
  if (!proofError && cleanup.errors.length === 0 && cleanupComplete && defaultProtected) {
    summary.status = 'PASS';
  } else {
    const errors = [proofError, ...cleanup.errors].filter(Boolean);
    summary.error = redact(errors[0] ?? new Error('Capture or cleanup incomplete'), [
      [home, '~'],
      [captureState.appPath, '<packaged-app>'],
      [captureState.executablePath, '<packaged-executable>'],
      [captureState.runtimeRoot, '<proof-runtime>'],
      [sessionRoot, '<proof-session>']
    ]);
    summary.cleanupErrors = cleanup.errors.map((error) =>
      redact(error, [
        [home, '~'],
        [captureState.appPath, '<packaged-app>'],
        [captureState.executablePath, '<packaged-executable>'],
        [captureState.runtimeRoot, '<proof-runtime>'],
        [sessionRoot, '<proof-session>']
      ])
    );
  }

  const summaryPath = path.join(sessionRoot, 'summary.json');
  await writeJsonAtomic(summaryPath, summary);
  const evidence = {
    schema: EVIDENCE_SCHEMA,
    status: summary.status,
    sourceRevision: summary.sourceRevision,
    preparedManifestSha256: createHash('sha256').update(preparedBytes).digest('hex'),
    summarySha256: await sha256File(summaryPath),
    files: ['prepared.json', 'summary.json']
  };
  await writeJsonAtomic(path.join(sessionRoot, 'evidence-package.json'), evidence);
  if (summary.status !== 'PASS') throw new Error(summary.error ?? 'Login-session proof capture failed');
  return summary;
}

export async function main(argv = process.argv.slice(2), dependencyOverrides = {}) {
  const deps = dependencies(dependencyOverrides);
  const sessionRoot = await assertNoSymlinkAncestors(preparseSessionRoot(argv));
  const { command, options } = parseArgs(argv);
  if (command === 'prepare') {
    const sourceRevision = validateSourceRevision(options.sourceRevision);
    try {
      await lstat(sessionRoot);
      throw new Error('Session root already exists; choose a new proof session root');
    } catch (error) {
      if (error?.code !== 'ENOENT') throw error;
    }
    await mkdir(sessionRoot, { recursive: false, mode: 0o700 });
    return prepare(options, deps, await realpath(sessionRoot), sourceRevision);
  }
  return capture(deps, await realpath(sessionRoot));
}

const invokedPath = process.argv[1] ? path.resolve(process.argv[1]) : undefined;
if (invokedPath === fileURLToPath(import.meta.url)) {
  main().then(
    (result) => process.stdout.write(`${JSON.stringify(result, null, 2)}\n`),
    (error) => {
      process.stderr.write(`${error instanceof Error ? error.message : String(error)}\n`);
      process.exitCode = 1;
    }
  );
}
