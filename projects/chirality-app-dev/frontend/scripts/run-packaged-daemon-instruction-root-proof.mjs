#!/usr/bin/env node

import { spawn } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';
import {
  access,
  mkdir,
  mkdtemp,
  readFile,
  realpath,
  rename,
  rm,
  stat,
  writeFile
} from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const projectRoot = path.resolve(frontendRoot, '..');
const defaultManifestPath = path.join(projectRoot, 'chirality.project.json');
const defaultAppPath = path.join(frontendRoot, 'dist', 'mac-arm64', 'Chirality.app');
const defaultOutputRoot = path.join(
  frontendRoot,
  'artifacts',
  'harness',
  'packaged-daemon-instruction-root',
  'latest'
);
const startupTimeoutMs = 30_000;
const commandTimeoutMs = 10 * 60 * 1_000;
const electronTimeoutMs = 2 * 60 * 1_000;
const terminateGraceMs = 5_000;
const killGraceMs = 5_000;
const darwinShortTempPrefix = '/private/tmp';
const darwinUnixSocketPathMaxBytes = 103;
const activeProcesses = new Set();

const argNames = new Map([
  ['--app', 'app'],
  ['--manifest', 'manifest'],
  ['--output-root', 'outputRoot'],
  ['--expected-app-identity', 'expectedAppIdentity']
]);

function parseArgs(argv) {
  const result = { pack: true, keepTemp: false };
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (token === '--skip-pack') {
      result.pack = false;
      continue;
    }
    if (token === '--keep-temp') {
      result.keepTemp = true;
      continue;
    }
    if (argNames.has(token)) {
      const value = argv[index + 1];
      if (!value || value.startsWith('--')) throw new Error(`Missing value for ${token}`);
      result[argNames.get(token)] = value;
      index += 1;
      continue;
    }
    throw new Error(`Unknown argument: ${token}`);
  }
  return result;
}

function preparseOutputRoot(argv) {
  const index = argv.indexOf('--output-root');
  const requested = index === -1 ? undefined : argv[index + 1];
  return path.resolve(requested && !requested.startsWith('--') ? requested : defaultOutputRoot);
}

function commandText(executable, args) {
  return [executable, ...args].map((part) => JSON.stringify(part)).join(' ');
}

function isRunning(running) {
  return running.child.exitCode === null && running.child.signalCode === null;
}

function waitForPromise(promise, timeoutMs, description) {
  let timer;
  return Promise.race([
    promise,
    new Promise((_, reject) => {
      timer = setTimeout(() => reject(new Error(`Timed out waiting for ${description}`)), timeoutMs);
    })
  ]).finally(() => clearTimeout(timer));
}

async function terminateProcess(
  running,
  label,
  { termGraceMs = terminateGraceMs, forceGraceMs = killGraceMs } = {}
) {
  if (!isRunning(running)) return running.exited;
  running.child.kill('SIGTERM');
  try {
    return await waitForPromise(running.exited, termGraceMs, `${label} after SIGTERM`);
  } catch {
    if (isRunning(running)) running.child.kill('SIGKILL');
    return waitForPromise(running.exited, forceGraceMs, `${label} after SIGKILL`);
  }
}

function startProcess({ executable, args, cwd, env, deadlineMs, label }) {
  if (!Number.isSafeInteger(deadlineMs) || deadlineMs <= 0) {
    throw new Error(`A positive process deadline is required for ${label ?? executable}`);
  }
  const child = spawn(executable, args, {
    cwd,
    env,
    stdio: ['ignore', 'pipe', 'pipe']
  });
  let stdout = '';
  let stderr = '';
  child.stdout.on('data', (chunk) => {
    stdout += chunk.toString('utf8');
  });
  child.stderr.on('data', (chunk) => {
    stderr += chunk.toString('utf8');
  });
  const exited = new Promise((resolve, reject) => {
    child.once('error', reject);
    child.once('exit', (code, signal) => resolve({ code, signal }));
  });
  const running = {
    child,
    exited,
    label: label ?? commandText(executable, args),
    stdout: () => stdout,
    stderr: () => stderr
  };
  activeProcesses.add(running);
  void exited.then(
    () => activeProcesses.delete(running),
    () => activeProcesses.delete(running)
  );
  const deadline = new Promise((_, reject) => {
    running.deadlineTimer = setTimeout(async () => {
      running.deadlineExpired = true;
      try {
        await terminateProcess(running, running.label);
        reject(new Error(`${running.label} exceeded deadline ${deadlineMs}ms`));
      } catch (error) {
        reject(error);
      }
    }, deadlineMs);
  });
  running.completed = Promise.race([exited, deadline]).finally(() => {
    clearTimeout(running.deadlineTimer);
  });
  return running;
}

async function runCommand(input) {
  const running = startProcess({
    ...input,
    deadlineMs: input.deadlineMs ?? commandTimeoutMs,
    label: input.label ?? commandText(input.executable, input.args)
  });
  const exit = await running.completed;
  const result = {
    command: commandText(input.executable, input.args),
    cwd: input.cwd,
    exitCode: exit.code,
    signal: exit.signal,
    stdout: running.stdout(),
    stderr: running.stderr()
  };
  if (running.deadlineExpired) {
    throw Object.assign(new Error(`${running.label} exceeded deadline ${input.deadlineMs ?? commandTimeoutMs}ms`), {
      result
    });
  }
  if (exit.code !== 0 && !input.allowFailure) {
    throw Object.assign(new Error(`Command failed: ${result.command}`), { result });
  }
  return result;
}

async function waitFor(predicate, description, timeoutMs = startupTimeoutMs) {
  const startedAt = Date.now();
  let lastError;
  while (Date.now() - startedAt < timeoutMs) {
    try {
      const value = await predicate();
      if (value) return value;
    } catch (error) {
      lastError = error;
    }
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  throw new Error(
    `Timed out waiting for ${description}${lastError ? `: ${lastError.message}` : ''}`
  );
}

async function stopProcess(running, label, options) {
  const exit = await terminateProcess(running, label, options);
  if (exit.code !== 0) {
    throw new Error(`${label} exited with code=${exit.code} signal=${exit.signal}`);
  }
  return {
    exitCode: exit.code,
    signal: exit.signal,
    stdout: running.stdout(),
    stderr: running.stderr()
  };
}

async function cleanupActiveProcesses(options) {
  const failures = [];
  for (const running of [...activeProcesses]) {
    try {
      await terminateProcess(running, running.label, options);
    } catch (error) {
      failures.push(error instanceof Error ? error.message : String(error));
    }
  }
  if (failures.length > 0 || activeProcesses.size > 0) {
    throw new Error(
      `Unable to confirm proof child cleanup: ${[
        ...failures,
        ...(activeProcesses.size > 0 ? [`${activeProcesses.size} process(es) still active`] : [])
      ].join('; ')}`
    );
  }
}

async function waitForLog(filePath, event, afterOffset = 0) {
  return waitFor(async () => {
    const source = await readFile(filePath, 'utf8');
    const relevant = sliceLogFromOffset(source, afterOffset);
    return relevant.includes(event) ? { source, relevant } : undefined;
  }, `${event} in ${filePath}`);
}

function logTextOffset(source) {
  return source.length;
}

function sliceLogFromOffset(source, offset) {
  return source.slice(offset);
}

function eventDetail(logText, event) {
  const line = logText
    .split(/\r?\n/u)
    .reverse()
    .find((candidate) => candidate.includes(` ${event} `));
  if (!line) return undefined;
  const marker = ` ${event} `;
  return JSON.parse(line.slice(line.indexOf(marker) + marker.length));
}

async function readExpectedInstructionRoot(manifestPath) {
  const manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
  if (manifest.schemaVersion !== 'chirality.project/v1' || typeof manifest.instructionRoot !== 'string') {
    throw new Error('Proof manifest does not contain a chirality.project/v1 instructionRoot');
  }
  return realpath(path.resolve(path.dirname(manifestPath), manifest.instructionRoot));
}

async function sha256File(filePath) {
  return createHash('sha256').update(await readFile(filePath)).digest('hex');
}

async function captureAppIdentity(appPath) {
  const canonicalAppPath = await realpath(appPath);
  const relativeFiles = [
    'Contents/MacOS/Chirality',
    'Contents/Resources/app.asar',
    'Contents/Resources/runtime-cli/chirality-cli.mjs'
  ];
  const files = [];
  for (const relativePath of relativeFiles) {
    const absolutePath = await realpath(path.join(canonicalAppPath, relativePath));
    const metadata = await stat(absolutePath);
    if (!metadata.isFile()) throw new Error(`App identity target is not a file: ${absolutePath}`);
    files.push({
      relativePath,
      bytes: metadata.size,
      sha256: await sha256File(absolutePath)
    });
  }
  const identityBasis = JSON.stringify({ appPath: canonicalAppPath, files });
  return {
    schema: 'chirality-packaged-app-identity/v1',
    appPath: canonicalAppPath,
    files,
    sha256: createHash('sha256').update(identityBasis).digest('hex')
  };
}

function sameAppIdentity(left, right) {
  return (
    left?.schema === 'chirality-packaged-app-identity/v1' &&
    right?.schema === left.schema &&
    left.appPath === right.appPath &&
    left.sha256 === right.sha256 &&
    JSON.stringify(left.files) === JSON.stringify(right.files)
  );
}

function validateExpectedAppIdentityMarker(marker, nowMs = Date.now()) {
  const capturedAtMs = Date.parse(marker?.capturedAt);
  if (
    marker?.kind !== 'current-invocation' ||
    !Number.isFinite(capturedAtMs) ||
    nowMs - capturedAtMs < 0 ||
    nowMs - capturedAtMs > 10 * 60 * 1_000 ||
    marker.identity?.schema !== 'chirality-packaged-app-identity/v1'
  ) {
    throw new Error('--expected-app-identity is stale or is not a pack invocation marker');
  }
  return marker.identity;
}

async function assertAppIdentity(appPath, expected) {
  const actual = await captureAppIdentity(appPath);
  if (!sameAppIdentity(actual, expected)) {
    throw new Error('Packaged app content identity changed during the proof');
  }
  return actual;
}

async function atomicWriteJson(filePath, value) {
  await mkdir(path.dirname(filePath), { recursive: true });
  const temporary = path.join(
    path.dirname(filePath),
    `.${path.basename(filePath)}.${process.pid}.${randomUUID()}.tmp`
  );
  await writeFile(temporary, `${JSON.stringify(value, null, 2)}\n`, {
    encoding: 'utf8',
    flag: 'wx'
  });
  await rename(temporary, filePath);
}

async function allocateDarwinProofTempRoot({
  canonicalize = realpath,
  makeTemp = mkdtemp,
  remove = rm
} = {}) {
  const canonicalPrefix = await canonicalize(darwinShortTempPrefix);
  if (!path.isAbsolute(canonicalPrefix)) {
    throw new Error('The packaged proof temp prefix did not resolve to an absolute path');
  }
  const tempRoot = await makeTemp(path.join(canonicalPrefix, 'ch-d100-'));
  const userData = path.join(tempRoot, 'u');
  const controlSocketPath = path.join(userData, 'runtime', 'control.sock');
  const controlSocketPathBytes = Buffer.byteLength(controlSocketPath, 'utf8');
  if (controlSocketPathBytes > darwinUnixSocketPathMaxBytes) {
    await remove(tempRoot, { recursive: true, force: true });
    throw new Error(
      `Packaged proof control socket path is ${controlSocketPathBytes} bytes; maximum is ${darwinUnixSocketPathMaxBytes}`
    );
  }
  return { tempRoot, userData, controlSocketPath, controlSocketPathBytes };
}

async function main(argv = process.argv.slice(2)) {
  const invocationId = randomUUID();
  const startedAt = new Date().toISOString();
  const outputRoot = preparseOutputRoot(argv);
  const summaryPath = path.join(outputRoot, 'summary.json');
  const identityMarkerPath = path.join(outputRoot, 'app-identity.json');
  const commands = [];
  let args;
  let tempRoot;
  let finalSummary;
  let failure;

  await atomicWriteJson(summaryPath, {
    schema: 'chirality-packaged-daemon-instruction-root-proof/v1',
    invocationId,
    startedAt,
    status: 'PENDING'
  });

  try {
    args = parseArgs(argv);
    const requestedAppPath = path.resolve(args.app ?? defaultAppPath);
    if (args.pack && requestedAppPath !== path.resolve(defaultAppPath)) {
      throw new Error('--app cannot override the registered desktop:pack output');
    }
    if (!args.pack && !args.expectedAppIdentity) {
      throw new Error('--skip-pack requires --expected-app-identity with a fresh captured identity');
    }
    if (process.platform !== 'darwin' || process.arch !== 'arm64') {
      throw new Error('The packaged daemon isolation proof requires a macOS arm64 host');
    }

    const manifestPath = await realpath(path.resolve(args.manifest ?? defaultManifestPath));
    const tempAllocation = await allocateDarwinProofTempRoot();
    tempRoot = tempAllocation.tempRoot;
    const isolationCwd = path.join(tempRoot, 'c');
    const isolatedHome = path.join(tempRoot, 'h');
    const userData = tempAllocation.userData;
    const daemonLogPath = path.join(userData, 'logs', 'desktop-daemon.log');
    const guiLogPath = path.join(userData, 'logs', 'desktop-main.log');
    await mkdir(isolationCwd, { recursive: true });
    await mkdir(isolatedHome, { recursive: true });

    let appIdentity;
    let packBinding;
    if (args.pack) {
      const packStartedAt = new Date().toISOString();
      const pack = await runCommand({
        executable: 'npm',
        args: ['run', 'desktop:pack'],
        cwd: frontendRoot,
        env: process.env,
        deadlineMs: commandTimeoutMs,
        label: 'desktop:pack'
      });
      commands.push(pack);
      appIdentity = await captureAppIdentity(requestedAppPath);
      packBinding = {
        kind: 'current-invocation',
        invocationId,
        packStartedAt,
        capturedAt: new Date().toISOString(),
        identity: appIdentity
      };
      await atomicWriteJson(identityMarkerPath, packBinding);
    } else {
      const expectedMarkerPath = await realpath(path.resolve(args.expectedAppIdentity));
      const expectedMarker = JSON.parse(await readFile(expectedMarkerPath, 'utf8'));
      const expectedIdentity = validateExpectedAppIdentityMarker(expectedMarker);
      appIdentity = await captureAppIdentity(requestedAppPath);
      if (!sameAppIdentity(appIdentity, expectedIdentity)) {
        throw new Error('Selected --app bytes do not match --expected-app-identity');
      }
      packBinding = {
        kind: 'verified-captured-identity',
        markerPath: expectedMarkerPath,
        markerInvocationId: expectedMarker.invocationId,
        capturedAt: expectedMarker.capturedAt,
        identity: appIdentity
      };
    }

    const appPath = appIdentity.appPath;
    const executable = path.join(appPath, 'Contents', 'MacOS', 'Chirality');
    const cliEntry = path.join(
      appPath,
      'Contents',
      'Resources',
      'runtime-cli',
      'chirality-cli.mjs'
    );
    await access(executable);
    await access(cliEntry);
    const expectedInstructionRoot = await readExpectedInstructionRoot(manifestPath);
    const signature = await runCommand({
      executable: '/usr/bin/codesign',
      args: ['--display', '--verbose=4', appPath],
      cwd: isolationCwd,
      env: { PATH: '/usr/bin:/bin' },
      allowFailure: true,
      deadlineMs: startupTimeoutMs,
      label: 'codesign inspection'
    });
    commands.push(signature);
    const signatureEvidence = `${signature.stdout}\n${signature.stderr}`;

    const isolatedEnvironment = {
      HOME: isolatedHome,
      LANG: process.env.LANG ?? 'en_US.UTF-8',
      PATH: '/usr/bin:/bin',
      TMPDIR: tempRoot,
      CHIRALITY_USER_DATA: userData,
      CHIRALITY_SKIP_CLI_LAUNCHER: '1',
      CHIRALITY_DAEMON_GUI_SPAWN: '0'
    };

    await assertAppIdentity(appPath, appIdentity);
    const initialDaemon = startProcess({
      executable,
      args: ['--runtime-daemon'],
      cwd: isolationCwd,
      env: isolatedEnvironment,
      deadlineMs: electronTimeoutMs,
      label: 'initial packaged daemon'
    });
    await waitForLog(daemonLogPath, 'runtime.daemon.started');
    const fallbackLog = await waitForLog(
      daemonLogPath,
      'runtime.daemon.instruction_root.fallback'
    );

    await assertAppIdentity(appPath, appIdentity);
    const cliEnvironment = { ...isolatedEnvironment, ELECTRON_RUN_AS_NODE: '1' };
    const registration = await runCommand({
      executable,
      args: [
        cliEntry,
        'project',
        'register',
        '--manifest',
        manifestPath,
        '--approved-by',
        'D-APP-100-packaged-proof',
        '--approval-reference',
        'D-APP-100',
        '--json'
      ],
      cwd: isolationCwd,
      env: cliEnvironment,
      deadlineMs: startupTimeoutMs,
      label: 'bundled CLI project register'
    });
    commands.push(registration);
    const initialStop = await stopProcess(initialDaemon, 'initial packaged daemon');

    const previousLogOffset = logTextOffset(fallbackLog.source);
    await assertAppIdentity(appPath, appIdentity);
    const registeredDaemon = startProcess({
      executable,
      args: ['--runtime-daemon'],
      cwd: isolationCwd,
      env: isolatedEnvironment,
      deadlineMs: electronTimeoutMs,
      label: 'registered packaged daemon'
    });
    const resolvedLog = await waitForLog(
      daemonLogPath,
      'runtime.daemon.instruction_root.resolved',
      previousLogOffset
    );
    await waitForLog(daemonLogPath, 'runtime.daemon.started', previousLogOffset);

    const cliStatus = await runCommand({
      executable,
      args: [
        cliEntry,
        'project',
        'status',
        '--project',
        'chirality-app-dev',
        '--json'
      ],
      cwd: isolationCwd,
      env: cliEnvironment,
      deadlineMs: startupTimeoutMs,
      label: 'bundled CLI project status'
    });
    commands.push(cliStatus);
    const cliProject = JSON.parse(cliStatus.stdout);
    const resolvedDetail = eventDetail(
      resolvedLog.relevant,
      'runtime.daemon.instruction_root.resolved'
    );
    const fallbackDetail = eventDetail(
      fallbackLog.relevant,
      'runtime.daemon.instruction_root.fallback'
    );
    const registeredStop = await stopProcess(registeredDaemon, 'registered packaged daemon');

    await assertAppIdentity(appPath, appIdentity);
    const gui = startProcess({
      executable,
      args: [],
      cwd: isolationCwd,
      env: isolatedEnvironment,
      deadlineMs: electronTimeoutMs,
      label: 'packaged GUI'
    });
    await waitForLog(guiLogPath, 'desktop.gui.starting');
    const guiStop = await stopProcess(gui, 'packaged GUI');
    const finalAppIdentity = await assertAppIdentity(appPath, appIdentity);

    const checks = {
      appIdentityBound: sameAppIdentity(finalAppIdentity, appIdentity),
      noDistributionSignature:
        !signatureEvidence.includes('Authority=') &&
        (signatureEvidence.includes('Signature=adhoc') ||
          signatureEvidence.includes('code object is not signed at all')),
      noAmbientInstructionRoot: !('CHIRALITY_INSTRUCTION_ROOT' in isolatedEnvironment),
      packagedChildrenUseEmbeddedNode: true,
      nonRepositoryCwd:
        isolationCwd !== frontendRoot && !isolationCwd.startsWith(`${projectRoot}${path.sep}`),
      fallbackWasExplicit:
        fallbackDetail?.instructionRoot === path.join(appPath, 'Contents', 'Resources') &&
        typeof fallbackDetail?.reason === 'string',
      daemonUsedManifestRoot:
        resolvedDetail?.instructionRoot === expectedInstructionRoot &&
        resolvedDetail?.source === 'registered-project-manifest',
      cliUsedSameManifest:
        path.resolve(cliProject.project.manifestPath) === manifestPath &&
        cliProject.project.projectId === 'chirality-app-dev' &&
        cliProject.manifestDrift === false,
      packagedGuiStarted: true
    };
    const failures = Object.entries(checks)
      .filter(([, passed]) => !passed)
      .map(([name]) => name);
    finalSummary = {
      schema: 'chirality-packaged-daemon-instruction-root-proof/v1',
      invocationId,
      startedAt,
      completedAt: new Date().toISOString(),
      status: failures.length === 0 ? 'PASS' : 'FAIL',
      failures,
      appPath,
      appIdentity,
      packBinding,
      manifestPath,
      expectedInstructionRoot,
      isolation: {
        cwd: isolationCwd,
        home: isolatedHome,
        userData,
        controlSocketPath: tempAllocation.controlSocketPath,
        controlSocketPathBytes: tempAllocation.controlSocketPathBytes,
        path: isolatedEnvironment.PATH,
        ambientInstructionRootRemoved: true
      },
      fallbackDetail,
      resolvedDetail,
      cliProject,
      checks,
      commands,
      processStops: { initialStop, registeredStop, guiStop },
      daemonLog: await readFile(daemonLogPath, 'utf8'),
      guiLog: await readFile(guiLogPath, 'utf8')
    };
  } catch (error) {
    failure = error;
  }

  try {
    await cleanupActiveProcesses();
  } catch (error) {
    failure ??= error;
  }
  if (tempRoot && !args?.keepTemp) {
    try {
      await rm(tempRoot, { recursive: true, force: true });
    } catch (error) {
      failure ??= error;
    }
  }

  if (failure) {
    finalSummary = {
      schema: 'chirality-packaged-daemon-instruction-root-proof/v1',
      invocationId,
      startedAt,
      completedAt: new Date().toISOString(),
      status: 'FAIL',
      error: failure instanceof Error ? failure.message : String(failure),
      commands
    };
  }
  await atomicWriteJson(summaryPath, finalSummary);
  process.stdout.write(
    `${JSON.stringify({ status: finalSummary.status, summaryPath, checks: finalSummary.checks })}\n`
  );
  if (failure) throw failure;
  return finalSummary;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main()
    .then((summary) => {
      if (summary.status !== 'PASS') process.exitCode = 1;
    })
    .catch(async (error) => {
      const detail = error.result ?? {
        message: error instanceof Error ? error.message : String(error)
      };
      process.stderr.write(`${JSON.stringify({ status: 'FAIL', error: detail })}\n`);
      process.exitCode = 1;
    });
}

export {
  allocateDarwinProofTempRoot,
  atomicWriteJson,
  captureAppIdentity,
  cleanupActiveProcesses,
  logTextOffset,
  main,
  runCommand,
  sameAppIdentity,
  sliceLogFromOffset,
  startProcess,
  stopProcess,
  terminateProcess,
  validateExpectedAppIdentityMarker,
  darwinUnixSocketPathMaxBytes
};
