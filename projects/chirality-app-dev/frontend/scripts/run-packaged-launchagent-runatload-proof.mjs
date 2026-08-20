#!/usr/bin/env node

import { spawn } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';
import {
  access,
  constants,
  lstat,
  mkdir,
  mkdtemp,
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

export const DEFAULT_LAUNCH_AGENT_LABEL = 'com.chirality.runtime';
export const PROOF_LABEL_PREFIX = 'com.chirality.ci.runatload.';
export const SUMMARY_SCHEMA = 'chirality-packaged-launchagent-runatload-proof/v1';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const defaultAppPath = path.join(frontendRoot, 'dist', 'mac-arm64', 'Chirality.app');
const defaultOutputRoot = path.join(
  frontendRoot,
  'artifacts',
  'release-verification',
  'launchagent-runatload'
);
const defaultTimeoutMs = 45_000;
const commandTimeoutMs = 60_000;
const pollIntervalMs = 100;
const cleanupServiceAttempts = 5;
const cleanupSignalTimeoutMs = 5_000;

const argNames = new Map([
  ['--app-path', 'appPath'],
  ['--output-root', 'outputRoot'],
  ['--label', 'label'],
  ['--source-revision', 'sourceRevision']
]);

function parseArgs(argv) {
  const result = {};
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    const name = argNames.get(token);
    if (!name) throw new Error(`Unknown argument: ${token}`);
    const value = argv[index + 1];
    if (!value || value.startsWith('--')) throw new Error(`Missing value for ${token}`);
    result[name] = value;
    index += 1;
  }
  return result;
}

function preparseOutputRoot(argv) {
  const index = argv.indexOf('--output-root');
  const requested = index === -1 ? undefined : argv[index + 1];
  return path.resolve(requested && !requested.startsWith('--') ? requested : defaultOutputRoot);
}

function preparseAppPath(argv) {
  const index = argv.indexOf('--app-path');
  const requested = index === -1 ? undefined : argv[index + 1];
  return path.resolve(requested && !requested.startsWith('--') ? requested : defaultAppPath);
}

function isWithin(candidate, parent) {
  const relative = path.relative(parent, candidate);
  return relative === '' || (!relative.startsWith(`..${path.sep}`) && relative !== '..' && !path.isAbsolute(relative));
}

async function assertNoSymlinkAncestors(candidate) {
  const absolute = path.resolve(candidate);
  const parsed = path.parse(absolute);
  let current = parsed.root;
  for (const segment of absolute.slice(parsed.root.length).split(path.sep).filter(Boolean)) {
    current = path.join(current, segment);
    try {
      const metadata = await lstat(current);
      if (metadata.isSymbolicLink()) {
        throw new Error(`Proof output path has a symbolic-link ancestor: ${current}`);
      }
    } catch (error) {
      if (error?.code === 'ENOENT') break;
      throw error;
    }
  }
  return absolute;
}

async function prepareOutputRoot(outputRoot, protectedRoots) {
  const absolute = await assertNoSymlinkAncestors(outputRoot);
  if (protectedRoots.some((protectedRoot) => protectedRoot && isWithin(absolute, protectedRoot))) {
    throw new Error('Proof output path overlaps a protected or packaged runtime path');
  }
  await mkdir(absolute, { recursive: true, mode: 0o700 });
  await assertNoSymlinkAncestors(absolute);
  const canonical = await realpath(absolute);
  if (canonical !== absolute) {
    throw new Error('Proof output path does not resolve to its no-symlink absolute path');
  }
  if (protectedRoots.some((protectedRoot) => protectedRoot && isWithin(canonical, protectedRoot))) {
    throw new Error('Proof output path overlaps a protected or packaged runtime path');
  }
  return canonical;
}

function wait(delayMs) {
  return new Promise((resolve) => setTimeout(resolve, delayMs));
}

function commandText(executable, args) {
  return [executable, ...args].map((part) => JSON.stringify(part)).join(' ');
}

async function defaultRunCommand({ executable, args, cwd, env, timeoutMs = commandTimeoutMs }) {
  return new Promise((resolve, reject) => {
    const child = spawn(executable, args, {
      cwd,
      env,
      stdio: ['ignore', 'pipe', 'pipe']
    });
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

async function defaultTerminateProcess(pid, signal) {
  process.kill(pid, signal);
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

function defaultDependencies(overrides = {}) {
  const runCommand = overrides.runCommand ?? defaultRunCommand;
  return {
    platform: overrides.platform ?? process.platform,
    environment: overrides.environment ?? process.env,
    userInfo: overrides.userInfo ?? (() => os.userInfo()),
    uid: overrides.uid ?? (() => process.getuid?.()),
    tempDirectory: overrides.tempDirectory ?? (() => os.tmpdir()),
    now: overrides.now ?? (() => new Date()),
    randomId: overrides.randomId ?? (() => randomUUID()),
    runCommand,
    cleanupSignalTimeoutMs:
      overrides.cleanupSignalTimeoutMs ?? cleanupSignalTimeoutMs,
    processAlive: overrides.processAlive ?? defaultProcessAlive,
    terminateProcess: overrides.terminateProcess ?? defaultTerminateProcess,
    inspectProcessExecutables:
      overrides.inspectProcessExecutables ??
      ((pid) => defaultInspectProcessExecutables(pid, runCommand))
  };
}

export function validateProofLabel(label) {
  if (label === DEFAULT_LAUNCH_AGENT_LABEL) {
    throw new Error('The default LaunchAgent label is forbidden for this proof');
  }
  if (
    !label.startsWith(PROOF_LABEL_PREFIX) ||
    !/^com\.chirality\.ci\.runatload\.[a-z0-9](?:[a-z0-9.-]{0,95}[a-z0-9])?$/u.test(label)
  ) {
    throw new Error(`Unsafe proof LaunchAgent label: ${label}`);
  }
  return label;
}

function xmlDecode(value) {
  return value
    .replaceAll('&lt;', '<')
    .replaceAll('&gt;', '>')
    .replaceAll('&quot;', '"')
    .replaceAll('&apos;', "'")
    .replaceAll('&amp;', '&');
}

function uniqueMatch(source, pattern, description) {
  const matches = [...source.matchAll(pattern)];
  if (matches.length !== 1 || matches[0]?.[1] === undefined) {
    throw new Error(`Installed plist has ambiguous or missing ${description}`);
  }
  return xmlDecode(matches[0][1]);
}

function uniqueRawMatch(source, pattern, description) {
  const matches = [...source.matchAll(pattern)];
  if (matches.length !== 1 || matches[0]?.[1] === undefined) {
    throw new Error(`Installed plist has ambiguous or missing ${description}`);
  }
  return matches[0][1];
}

export function inspectInstalledPlist(source) {
  const label = uniqueMatch(
    source,
    /<key>Label<\/key>\s*<string>([\s\S]*?)<\/string>/gu,
    'Label'
  );
  const programArgumentsBody = uniqueRawMatch(
    source,
    /<key>ProgramArguments<\/key>\s*<array>([\s\S]*?)<\/array>/gu,
    'ProgramArguments'
  );
  const argumentPattern = /<string>([\s\S]*?)<\/string>/gu;
  const programArguments = [...programArgumentsBody.matchAll(argumentPattern)].map((match) =>
    xmlDecode(match[1])
  );
  if (programArgumentsBody.replace(argumentPattern, '').trim() !== '') {
    throw new Error('Installed plist ProgramArguments contains unsupported entries');
  }
  const runAtLoad = uniqueMatch(
    source,
    /<key>RunAtLoad<\/key>\s*<(true|false)\s*\/>/gu,
    'RunAtLoad'
  );
  return { label, programArguments, runAtLoad: runAtLoad === 'true' };
}

export function assertExactRuntimeArguments(actual, expectedExecutable, source) {
  const expected = [expectedExecutable, '--runtime-daemon'];
  if (!Array.isArray(actual) || !sameValue(actual, expected)) {
    throw new Error(`${source} arguments do not exactly match the packaged runtime daemon vector`);
  }
}

function launchctlNotFoundMessage(service) {
  const match = service.match(/^gui\/([0-9]+)\/(.+)$/u);
  if (!match) throw new Error(`Unsupported launchctl service identity: ${service}`);
  return `Bad request.\nCould not find service "${match[2]}" in domain for user gui: ${match[1]}`;
}

export function isExactLaunchctlNotFound(result, service) {
  return (
    result.exitCode === 113 &&
    result.stdout.trim() === '' &&
    result.stderr.trim() === launchctlNotFoundMessage(service)
  );
}

function classifyLaunchctlPrint(result, service) {
  if (result.exitCode === 0) return 'LOADED';
  if (isExactLaunchctlNotFound(result, service)) return 'NOT_FOUND';
  throw new Error(`Unexpected launchctl print failure for proof service (exit ${result.exitCode})`);
}

function parseLaunchctlTopLevel(source) {
  const lines = source.split(/\r?\n/u);
  const firstContentIndex = lines.findIndex((line) => line.trim().length > 0);
  const wrapped = firstContentIndex >= 0 && /=\s*\{\s*$/u.test(lines[firstContentIndex]);
  const jobDepth = wrapped ? 1 : 0;
  let depth = jobDepth;
  let currentArguments;
  const stateMatches = [];
  const programMatches = [];
  const pidMatches = [];
  const argumentBlocks = [];
  for (let index = wrapped ? firstContentIndex + 1 : 0; index < lines.length; index += 1) {
    const line = lines[index];
    if (currentArguments && depth === jobDepth + 1 && line.trim() !== '}') {
      currentArguments.push(line.trim());
    }
    if (depth === jobDepth) {
      const state = line.match(/^\s*state = (.+?)\s*$/u)?.[1];
      const program = line.match(/^\s*program = (.+?)\s*$/u)?.[1];
      const pid = line.match(/^\s*pid = ([0-9]+)\s*$/u)?.[1];
      if (state !== undefined) stateMatches.push(state);
      if (program !== undefined) programMatches.push(program);
      if (pid !== undefined) pidMatches.push(Number.parseInt(pid, 10));
      if (/^\s*arguments = \{\s*$/u.test(line)) {
        currentArguments = [];
        argumentBlocks.push(currentArguments);
      }
    }
    depth += (line.match(/\{/gu) ?? []).length - (line.match(/\}/gu) ?? []).length;
    if (currentArguments && depth === jobDepth) currentArguments = undefined;
  }
  return { stateMatches, programMatches, pidMatches, argumentBlocks };
}

export function parseLaunchctlJob(source) {
  const { stateMatches, programMatches, pidMatches, argumentBlocks } =
    parseLaunchctlTopLevel(source);
  if (stateMatches.length !== 1 || programMatches.length !== 1 || pidMatches.length !== 1) {
    throw new Error('Loaded job has ambiguous process identity');
  }
  if (argumentBlocks.length > 1) throw new Error('Loaded job has ambiguous argument identity');
  if (!Number.isSafeInteger(pidMatches[0]) || pidMatches[0] <= 0) {
    throw new Error('Loaded job reported an invalid process identifier');
  }
  return {
    state: stateMatches[0],
    program: programMatches[0],
    pid: pidMatches[0],
    ...(argumentBlocks.length === 1 ? { programArguments: argumentBlocks[0] } : {})
  };
}

async function sha256File(filePath) {
  return createHash('sha256').update(await readFile(filePath)).digest('hex');
}

async function fileSnapshot(filePath) {
  try {
    const metadata = await stat(filePath);
    if (!metadata.isFile()) throw new Error('protected path is not a regular file');
    return {
      present: true,
      bytes: metadata.size,
      mode: metadata.mode & 0o777,
      sha256: await sha256File(filePath)
    };
  } catch (error) {
    if (error?.code === 'ENOENT') return { present: false };
    throw error;
  }
}

async function protectedState({ defaultPlistPath, defaultService, deps }) {
  const [plist, job] = await Promise.all([
    fileSnapshot(defaultPlistPath),
    deps.runCommand({ executable: '/bin/launchctl', args: ['print', defaultService] })
  ]);
  return { plist, jobLoaded: classifyLaunchctlPrint(job, defaultService) === 'LOADED' };
}

function sameValue(left, right) {
  return JSON.stringify(left) === JSON.stringify(right);
}

async function writeJsonAtomic(filePath, value) {
  const directory = path.dirname(filePath);
  await assertNoSymlinkAncestors(directory);
  await mkdir(directory, { recursive: true });
  await assertNoSymlinkAncestors(directory);
  const temporary = `${filePath}.${process.pid}.${Date.now()}.tmp`;
  await writeFile(temporary, `${JSON.stringify(value, null, 2)}\n`, {
    encoding: 'utf8',
    mode: 0o600,
    flag: 'wx'
  });
  await rename(temporary, filePath);
}

function redactError(error, replacements) {
  let message = error instanceof Error ? error.message : String(error);
  for (const [value, replacement] of replacements) {
    if (value) message = message.replaceAll(value, replacement);
  }
  return message.replaceAll(/[\r\n\t]+/gu, ' ').slice(0, 500);
}

async function waitForJob({
  service,
  deps,
  expectedExecutable,
  expectedArguments,
  timeoutMs,
  onPidObserved
}) {
  const deadline = Date.now() + timeoutMs;
  let lastReason = 'job was not loaded';
  while (Date.now() < deadline) {
    const result = await deps.runCommand({
      executable: '/bin/launchctl',
      args: ['print', service]
    });
    const classification = classifyLaunchctlPrint(result, service);
    if (classification === 'LOADED') {
      const { pidMatches } = parseLaunchctlTopLevel(result.stdout);
      if (pidMatches.length === 1 && Number.isSafeInteger(pidMatches[0]) && pidMatches[0] > 0) {
        onPidObserved?.(pidMatches[0]);
      }
      const job = parseLaunchctlJob(result.stdout);
      if (job.state !== 'running') {
        lastReason = `job state was ${job.state}`;
      } else if (path.resolve(job.program) !== expectedExecutable) {
        throw new Error('Loaded job program does not match the staged packaged executable');
      } else {
        if (job.programArguments !== undefined) {
          assertExactRuntimeArguments(job.programArguments, expectedArguments[0], 'Loaded job');
        }
        return job;
      }
    }
    await wait(pollIntervalMs);
  }
  throw new Error(`Automatic RunAtLoad process was not observed: ${lastReason}`);
}

async function waitForCondition(predicate, timeoutMs) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    if (await predicate()) return true;
    await wait(pollIntervalMs);
  }
  return predicate();
}

function observedServicePid(source) {
  const { pidMatches } = parseLaunchctlTopLevel(source);
  if (pidMatches.length !== 1 || !Number.isSafeInteger(pidMatches[0]) || pidMatches[0] <= 0) {
    return undefined;
  }
  return pidMatches[0];
}

async function terminateVerifiedProcess({ pid, deps, expectedExecutable }) {
  if (!deps.processAlive(pid)) return;
  const candidates = await canonicalPackagedExecutables(
    await deps.inspectProcessExecutables(pid)
  );
  if (candidates.length !== 1 || candidates[0] !== expectedExecutable) {
    throw new Error('refused to signal a process whose packaged identity is ambiguous');
  }
  await deps.terminateProcess(pid, 'SIGTERM');
  if (await waitForCondition(() => !deps.processAlive(pid), deps.cleanupSignalTimeoutMs)) return;
  const killCandidates = await canonicalPackagedExecutables(
    await deps.inspectProcessExecutables(pid)
  );
  if (killCandidates.length !== 1 || killCandidates[0] !== expectedExecutable) {
    throw new Error('refused to SIGKILL a process whose packaged identity changed or is ambiguous');
  }
  await deps.terminateProcess(pid, 'SIGKILL');
  if (!(await waitForCondition(() => !deps.processAlive(pid), deps.cleanupSignalTimeoutMs))) {
    throw new Error(`proof process ${pid} remained alive after SIGKILL`);
  }
}

async function reclaimProofService({
  service,
  label,
  expectedExecutable,
  observedPids,
  deps,
  mutations
}) {
  const errors = [];
  let serviceAbsent = false;
  let lastBootoutFailure;

  for (let attempt = 0; attempt < cleanupServiceAttempts; attempt += 1) {
    let inspection;
    try {
      inspection = await deps.runCommand({
        executable: '/bin/launchctl',
        args: ['print', service]
      });
      const classification = classifyLaunchctlPrint(inspection, service);
      if (classification === 'NOT_FOUND') {
        serviceAbsent = true;
        break;
      }
    } catch (error) {
      errors.push(
        `Cleanup verification failed: ${error instanceof Error ? error.message : String(error)}`
      );
      await wait(pollIntervalMs);
      continue;
    }

    let currentPid = observedServicePid(inspection.stdout);
    if (currentPid !== undefined) observedPids.add(currentPid);

    // A prior bootout did not reach exact-not-found. Stop the currently
    // observed packaged process before retrying, then reinspect so a KeepAlive
    // replacement PID is tracked before the next service mutation.
    if (attempt > 0 && currentPid !== undefined) {
      try {
        await terminateVerifiedProcess({
          pid: currentPid,
          deps,
          expectedExecutable
        });
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        lastBootoutFailure = message;
        errors.push(`Cleanup process termination failed: ${message}`);
      }

      try {
        const afterSignal = await deps.runCommand({
          executable: '/bin/launchctl',
          args: ['print', service]
        });
        const classification = classifyLaunchctlPrint(afterSignal, service);
        if (classification === 'NOT_FOUND') {
          serviceAbsent = true;
          break;
        }
        currentPid = observedServicePid(afterSignal.stdout);
        if (currentPid !== undefined) observedPids.add(currentPid);
      } catch (error) {
        errors.push(
          `Cleanup verification failed: ${error instanceof Error ? error.message : String(error)}`
        );
      }
    }

    try {
      const bootout = await deps.runCommand({
        executable: '/bin/launchctl',
        args: ['bootout', service]
      });
      mutations.push({ kind: 'bootout', label, path: service });
      lastBootoutFailure =
        bootout.exitCode === 0
          ? undefined
          : `LaunchAgent bootout failed with exit ${bootout.exitCode}`;
    } catch (error) {
      lastBootoutFailure = `LaunchAgent bootout failed: ${
        error instanceof Error ? error.message : String(error)
      }`;
    }
    await wait(pollIntervalMs);
  }

  if (!serviceAbsent) {
    try {
      const terminal = await deps.runCommand({
        executable: '/bin/launchctl',
        args: ['print', service]
      });
      const classification = classifyLaunchctlPrint(terminal, service);
      if (classification === 'NOT_FOUND') {
        serviceAbsent = true;
      } else {
        const replacementPid = observedServicePid(terminal.stdout);
        if (replacementPid !== undefined) observedPids.add(replacementPid);
      }
    } catch (error) {
      errors.push(
        `Cleanup verification failed: ${error instanceof Error ? error.message : String(error)}`
      );
    }
  }

  if (!serviceAbsent) {
    errors.push(
      lastBootoutFailure ??
        `LaunchAgent service remained loaded after ${cleanupServiceAttempts} cleanup attempts`
    );
  }
  return { serviceAbsent, errors };
}

async function canonicalPackagedExecutables(paths) {
  const candidates = [];
  for (const candidate of paths) {
    if (!/\.app\/Contents\/MacOS\/Chirality$/u.test(candidate)) continue;
    candidates.push(await realpath(candidate).catch(() => path.resolve(candidate)));
  }
  return [...new Set(candidates)];
}

function defaultSummary({ label, sourceRevision, timestamp }) {
  return {
    schema: SUMMARY_SCHEMA,
    status: 'FAIL',
    timestamp,
    scope: 'disposable-ci-account-packaged-app-only',
    sourceRevision: sourceRevision || 'unavailable',
    launchAgent: {
      label,
      launchAgentsDirectory: '~/Library/LaunchAgents',
      plist: label ? `~/Library/LaunchAgents/${label}.plist` : 'unavailable',
      runAtLoad: false,
      bootstrapOnly: false,
      automaticLaunchObserved: false,
      loadedProgramMatches: false,
      loadedArgumentsAvailable: false,
      loadedArgumentsMatch: null
    },
    process: {
      pidObserved: false,
      executableIdentityMatches: false
    },
    cleanup: {
      processAbsent: false,
      jobAbsent: false,
      plistAbsent: false,
      runtimeDataRemoved: false
    },
    defaultProtection: {
      label: DEFAULT_LAUNCH_AGENT_LABEL,
      plist: `~/Library/LaunchAgents/${DEFAULT_LAUNCH_AGENT_LABEL}.plist`,
      plistUnchanged: false,
      jobLoadedStateUnchanged: false,
      mutationTargetsExcluded: false
    }
  };
}

export async function main(argv = process.argv.slice(2), dependencyOverrides = {}) {
  const deps = defaultDependencies(dependencyOverrides);
  const outputRoot = preparseOutputRoot(argv);
  let summaryPath = path.join(outputRoot, 'summary.json');
  let args = {};
  let summary = defaultSummary({
    label: undefined,
    sourceRevision: undefined,
    timestamp: deps.now().toISOString()
  });
  let actualHome;
  let appPath;
  let executablePath;
  let runtimeRoot;
  let plistPath;
  let service;
  let launchedPid;
  const observedPids = new Set();
  let ownsPlist = false;
  let ownsJob = false;
  let defaultBefore;
  let defaultPlistPath;
  let defaultService;
  let proofServiceAbsent = false;
  let outputSafe = false;
  const cleanupErrors = [];
  const mutations = [];
  let primaryError;

  try {
    const requestedAppPath = preparseAppPath(argv);
    const accountHome = deps.userInfo().homedir;
    if (!accountHome) throw new Error('Account home is required');
    const canonicalAccountHome = await realpath(accountHome);
    actualHome = canonicalAccountHome;
    const launchAgentsDirectory = path.join(actualHome, 'Library', 'LaunchAgents');
    const canonicalAppCandidate = await realpath(requestedAppPath).catch((error) => {
      if (error?.code === 'ENOENT') return undefined;
      throw error;
    });
    const canonicalOutputRoot = await prepareOutputRoot(outputRoot, [
      launchAgentsDirectory,
      requestedAppPath,
      canonicalAppCandidate
    ]);
    summaryPath = path.join(canonicalOutputRoot, 'summary.json');
    outputSafe = true;
    // Replace any stale PASS before argument, platform, uid, HOME, or label validation.
    await writeJsonAtomic(summaryPath, { ...summary, status: 'PENDING' });

    args = parseArgs(argv);
    const label = validateProofLabel(
      args.label ?? `${PROOF_LABEL_PREFIX}${process.pid}.${deps.randomId().replaceAll('-', '').slice(0, 12)}`
    );
    summary = defaultSummary({
      label,
      sourceRevision: args.sourceRevision,
      timestamp: deps.now().toISOString()
    });
    await writeJsonAtomic(summaryPath, { ...summary, status: 'PENDING' });

    if (deps.platform !== 'darwin') {
      throw new Error('Packaged LaunchAgent RunAtLoad proof requires macOS');
    }
    const uid = deps.uid();
    if (!Number.isSafeInteger(uid) || uid < 1) throw new Error('A non-root GUI user is required');

    const environmentHome = deps.environment.HOME;
    if (!environmentHome) throw new Error('HOME is required');
    const canonicalEnvironmentHome = await realpath(environmentHome);
    if (canonicalEnvironmentHome !== canonicalAccountHome) {
      throw new Error('HOME does not resolve to the current account home');
    }
    await mkdir(launchAgentsDirectory, { recursive: true, mode: 0o700 });

    appPath = await realpath(requestedAppPath);
    if (path.basename(appPath) !== 'Chirality.app') {
      throw new Error('Packaged app path must identify Chirality.app');
    }
    executablePath = await realpath(path.join(appPath, 'Contents', 'MacOS', 'Chirality'));
    const cliEntry = await realpath(
      path.join(appPath, 'Contents', 'Resources', 'runtime-cli', 'chirality-cli.mjs')
    );
    if (!isWithin(executablePath, appPath) || !isWithin(cliEntry, appPath)) {
      throw new Error('Packaged executable identity escapes the staged app bundle');
    }
    await access(executablePath, constants.X_OK);
    await access(cliEntry, constants.R_OK);

    plistPath = path.join(launchAgentsDirectory, `${label}.plist`);
    service = `gui/${uid}/${label}`;
    defaultPlistPath = path.join(launchAgentsDirectory, `${DEFAULT_LAUNCH_AGENT_LABEL}.plist`);
    defaultService = `gui/${uid}/${DEFAULT_LAUNCH_AGENT_LABEL}`;
    if (await fileSnapshot(plistPath).then((snapshot) => snapshot.present)) {
      throw new Error('Unique proof plist already exists; refusing to overwrite it');
    }
    const preexistingJob = await deps.runCommand({
      executable: '/bin/launchctl',
      args: ['print', service]
    });
    if (classifyLaunchctlPrint(preexistingJob, service) === 'LOADED') {
      throw new Error('Unique proof LaunchAgent job already exists; refusing to take ownership');
    }

    defaultBefore = await protectedState({ defaultPlistPath, defaultService, deps });

    runtimeRoot = await mkdtemp(path.join(deps.tempDirectory(), 'chirality-runatload-'));
    // The preflight proved this unique path absent, so from this point onward
    // cleanup owns it even if the packaged CLI times out after creating it.
    ownsPlist = true;
    const install = await deps.runCommand({
      executable: executablePath,
      args: [cliEntry, 'daemon', 'install', '--executable', executablePath],
      cwd: frontendRoot,
      env: {
        ...deps.environment,
        HOME: actualHome,
        ELECTRON_RUN_AS_NODE: '1',
        CHIRALITY_SKIP_CLI_LAUNCHER: '1',
        CHIRALITY_LAUNCH_AGENTS_DIRECTORY: launchAgentsDirectory,
        CHIRALITY_USER_DATA: runtimeRoot,
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: label,
        CHIRALITY_RUNTIME_KEEP_ALIVE: 'always',
        CHIRALITY_RUNTIME_RUN_AT_LOAD: 'true'
      }
    });
    mutations.push({ kind: 'packaged-cli-install', label, path: plistPath });
    if (install.exitCode !== 0) {
      throw new Error(`Packaged CLI LaunchAgent install failed with exit ${install.exitCode}`);
    }

    const plist = inspectInstalledPlist(await readFile(plistPath, 'utf8'));
    if (plist.label !== label) throw new Error('Installed plist label does not match the proof label');
    assertExactRuntimeArguments(plist.programArguments, executablePath, 'Installed plist');
    if (!plist.runAtLoad) throw new Error('Installed plist does not enable RunAtLoad');
    summary.launchAgent.runAtLoad = true;

    // Likewise, once a bootstrap is attempted against a preflight-absent unique
    // service, cleanup must boot it out even if launchctl loses its response.
    ownsJob = true;
    const bootstrap = await deps.runCommand({
      executable: '/bin/launchctl',
      args: ['bootstrap', `gui/${uid}`, plistPath]
    });
    mutations.push({ kind: 'bootstrap', label, path: plistPath });
    if (bootstrap.exitCode !== 0) {
      throw new Error(`LaunchAgent bootstrap failed with exit ${bootstrap.exitCode}`);
    }
    summary.launchAgent.bootstrapOnly = true;

    const job = await waitForJob({
      service,
      deps,
      expectedExecutable: executablePath,
      expectedArguments: [executablePath, '--runtime-daemon'],
      onPidObserved: (pid) => {
        if (launchedPid !== undefined && launchedPid !== pid) {
          throw new Error('LaunchAgent process identifier changed during proof observation');
        }
        launchedPid = pid;
        observedPids.add(pid);
        summary.process.pidObserved = true;
      },
      timeoutMs: defaultTimeoutMs
    });
    summary.launchAgent.automaticLaunchObserved = true;
    summary.launchAgent.loadedProgramMatches = true;
    summary.launchAgent.loadedArgumentsAvailable = job.programArguments !== undefined;
    summary.launchAgent.loadedArgumentsMatch =
      job.programArguments === undefined ? null : true;

    const processExecutables = await canonicalPackagedExecutables(
      await deps.inspectProcessExecutables(launchedPid)
    );
    if (processExecutables.length !== 1 || processExecutables[0] !== executablePath) {
      throw new Error('Launched process executable identity is missing or ambiguous');
    }
    summary.process.executableIdentityMatches = true;
    summary.app = {
      path: 'dist/mac-arm64/Chirality.app',
      executableSha256: await sha256File(executablePath)
    };
  } catch (error) {
    primaryError = error;
  } finally {
    if (ownsJob && service) {
      try {
        const reclamation = await reclaimProofService({
          service,
          label: summary.launchAgent.label,
          expectedExecutable: executablePath,
          observedPids,
          deps,
          mutations
        });
        proofServiceAbsent = reclamation.serviceAbsent;
        cleanupErrors.push(...reclamation.errors);
      } catch (error) {
        cleanupErrors.push(
          `LaunchAgent cleanup failed: ${error instanceof Error ? error.message : String(error)}`
        );
      }
    }

    if (proofServiceAbsent) {
      for (const pid of observedPids) {
        if (!deps.processAlive(pid)) continue;
        try {
          await terminateVerifiedProcess({ pid, deps, expectedExecutable: executablePath });
        } catch (error) {
          cleanupErrors.push(error instanceof Error ? error.message : String(error));
        }
      }
    }

    if (ownsPlist && plistPath) {
      try {
        await unlink(plistPath).catch((error) => {
          if (error?.code !== 'ENOENT') throw error;
        });
        mutations.push({ kind: 'unlink-plist', label: summary.launchAgent.label, path: plistPath });
      } catch (error) {
        cleanupErrors.push(`Unable to remove proof plist: ${error instanceof Error ? error.message : String(error)}`);
      }
    }

    if (runtimeRoot) {
      try {
        await rm(runtimeRoot, { recursive: true, force: true });
        summary.cleanup.runtimeDataRemoved = true;
      } catch (error) {
        cleanupErrors.push(`Unable to remove proof runtime data: ${error instanceof Error ? error.message : String(error)}`);
      }
    }

    try {
      summary.cleanup.processAbsent =
        observedPids.size > 0 && [...observedPids].every((pid) => !deps.processAlive(pid));
      if (service) {
        const job = await deps.runCommand({
          executable: '/bin/launchctl',
          args: ['print', service]
        });
        summary.cleanup.jobAbsent = classifyLaunchctlPrint(job, service) === 'NOT_FOUND';
      }
      summary.cleanup.plistAbsent =
        plistPath !== undefined && !(await fileSnapshot(plistPath)).present;

      if (defaultBefore && defaultPlistPath && defaultService) {
        const defaultAfter = await protectedState({ defaultPlistPath, defaultService, deps });
        summary.defaultProtection.plistUnchanged = sameValue(defaultBefore.plist, defaultAfter.plist);
        summary.defaultProtection.jobLoadedStateUnchanged =
          defaultBefore.jobLoaded === defaultAfter.jobLoaded;
      }
      summary.defaultProtection.mutationTargetsExcluded = mutations.every(
        (mutation) =>
          mutation.label !== DEFAULT_LAUNCH_AGENT_LABEL &&
          mutation.path !== defaultPlistPath &&
          mutation.path !== defaultService
      );
    } catch (error) {
      cleanupErrors.push(`Cleanup verification failed: ${error instanceof Error ? error.message : String(error)}`);
    }
  }

  const cleanupComplete =
    summary.cleanup.processAbsent &&
    summary.cleanup.jobAbsent &&
    summary.cleanup.plistAbsent &&
    summary.cleanup.runtimeDataRemoved;
  const defaultProtected =
    summary.defaultProtection.plistUnchanged &&
    summary.defaultProtection.jobLoadedStateUnchanged &&
    summary.defaultProtection.mutationTargetsExcluded;
  if (!cleanupComplete) cleanupErrors.push('Process, job, plist, or runtime-data cleanup is incomplete');
  if (!defaultProtected) cleanupErrors.push('Default LaunchAgent protection could not be proven');

  if (!primaryError && cleanupErrors.length === 0) {
    summary.status = 'PASS';
  } else {
    summary.status = 'FAIL';
    const replacements = [
      [actualHome, '~'],
      [appPath, '<packaged-app>'],
      [runtimeRoot, '<proof-runtime>'],
      [outputRoot, '<proof-output>']
    ];
    summary.error = redactError(
      primaryError ?? new Error(cleanupErrors.join('; ')),
      replacements
    );
    summary.cleanupErrors = cleanupErrors.map((error) => redactError(error, replacements));
  }

  if (outputSafe) await writeJsonAtomic(summaryPath, summary);
  if (summary.status !== 'PASS') {
    const error = new Error(summary.error ?? 'Packaged LaunchAgent RunAtLoad proof failed');
    error.summary = summary;
    throw error;
  }
  return summary;
}

const invokedPath = process.argv[1] ? path.resolve(process.argv[1]) : undefined;
if (invokedPath === fileURLToPath(import.meta.url)) {
  main().then(
    (summary) => {
      process.stdout.write(`${JSON.stringify(summary, null, 2)}\n`);
    },
    (error) => {
      process.stderr.write(`${error instanceof Error ? error.message : String(error)}\n`);
      process.exitCode = 1;
    }
  );
}
