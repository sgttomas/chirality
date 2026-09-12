import { spawn } from 'node:child_process';
import { chmod, copyFile, lstat, mkdir, readdir, realpath, rename, rm } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

import { verifyElectronDist } from './verify-electron-dist.mjs';
import {
  computeDependencyResolutionDigest,
  computeSupplierTreeDigest,
  DEPENDENCY_DIGEST_ENV,
  EXPECTED_DEPENDENCY_DIGEST_ENV,
  EXPECTED_SUPPLIER_DIGEST_ENV,
  RUNTIME_MANIFEST_VERSION_ENV,
  RUNTIME_V2_INPUT_DIGEST_ENV,
  SUPPLIER_DIGEST_ENV
} from './finalize-electron-resources.mjs';
import {
  SIGNING_BUNDLE_ID_ENV,
  SIGNING_CHECKPOINT_FILE_ENV,
  SIGNING_IDENTITY_SHA1_ENV,
  SIGNING_TEAM_ID_ENV,
  bindSignedRuntimeV2Payload,
  sealSignedRuntimeV2
} from './sign-electron-runtime-v2.mjs';

const SUPPORTED_TARGETS = new Set(['dir', 'dmg']);
const SUPPLIER_SOURCE_ENV = 'CHIRALITY_SUPPLIER_SOURCE_ROOT';
export const ELECTRON_OUTPUT_DIRECTORY_ENV = 'CHIRALITY_ELECTRON_OUTPUT_DIRECTORY';
const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const defaultSupplierStagingRoot = path.join(
  frontendRoot,
  'node_modules',
  '.cache',
  'chirality-supplier'
);

async function inspectSupplierTree(root) {
  if (!path.isAbsolute(root) || path.resolve(root) !== root) {
    throw new Error(`${SUPPLIER_SOURCE_ENV} must be an absolute canonical directory`);
  }
  const rootInfo = await lstat(root).catch(() => undefined);
  if (!rootInfo?.isDirectory() || rootInfo.isSymbolicLink() || (await realpath(root)) !== root) {
    throw new Error(`${SUPPLIER_SOURCE_ENV} must name an existing canonical non-symlink directory`);
  }
  const records = [];
  async function visit(directory, relativeDirectory = '') {
    for (const name of (await readdir(directory)).sort()) {
      const absolutePath = path.join(directory, name);
      const relativePath = path.posix.join(relativeDirectory, name);
      const info = await lstat(absolutePath);
      if (info.isSymbolicLink() || (!info.isDirectory() && !info.isFile())) {
        throw new Error(`Supplier source contains unsupported entry: ${relativePath}`);
      }
      records.push({ absolutePath, relativePath, directory: info.isDirectory(), mode: info.mode & 0o777 });
      if (records.length > 50_000) throw new Error('Supplier source exceeds 50000 entries');
      if (info.isDirectory()) await visit(absolutePath, relativePath);
    }
  }
  await visit(root);
  for (const name of ['codex', 'codex-code-mode-host']) {
    const executable = records.find((entry) => entry.relativePath === name);
    if (!executable || executable.directory || (executable.mode & 0o111) === 0) {
      throw new Error(`Supplier source must contain an executable regular file named ${name}`);
    }
  }
  return records;
}

export async function prepareSupplierResources({
  env = process.env,
  stagingRoot = defaultSupplierStagingRoot
} = {}) {
  const sourceRoot = env[SUPPLIER_SOURCE_ENV];
  if (!sourceRoot) {
    throw new Error(`${SUPPLIER_SOURCE_ENV} is required and must identify the accepted supplier tree`);
  }
  const sourceRecords = await inspectSupplierTree(sourceRoot);
  const pendingRoot = `${stagingRoot}.pending`;
  for (const candidate of [stagingRoot, pendingRoot]) {
    if (await lstat(candidate).then(() => true, () => false)) {
      throw new Error(`Refusing to overwrite existing supplier staging path: ${candidate}`);
    }
  }
  await mkdir(path.dirname(stagingRoot), { recursive: true });
  await mkdir(pendingRoot, { mode: 0o700 });
  try {
    for (const record of sourceRecords) {
      const destination = path.join(pendingRoot, ...record.relativePath.split('/'));
      if (record.directory) {
        await mkdir(destination, { mode: record.mode });
        await chmod(destination, record.mode);
      } else {
        await copyFile(record.absolutePath, destination);
        await chmod(destination, record.mode);
      }
    }
    const digest = await computeSupplierTreeDigest(pendingRoot);
    await rename(pendingRoot, stagingRoot);
    return {
      digest,
      stagingRoot,
      cleanup: () => rm(stagingRoot, { recursive: true, force: false })
    };
  } catch (error) {
    throw new Error(`Supplier staging failed and was preserved at ${pendingRoot}: ${error.message}`);
  }
}

function validateTarget(target) {
  if (!SUPPORTED_TARGETS.has(target)) {
    throw new Error(`Unsupported Electron packaging target: ${String(target)}`);
  }
  return target;
}

function expectedDigest(env, name) {
  const value = env[name];
  if (typeof value !== 'string' || !/^[a-f0-9]{64}$/.test(value)) {
    throw new Error(`${name} is required and must be a lowercase SHA-256 digest`);
  }
  return value;
}

export function resolveElectronOutputDirectory(env = process.env) {
  if (!Object.prototype.hasOwnProperty.call(env, ELECTRON_OUTPUT_DIRECTORY_ENV)) {
    return path.join(frontendRoot, 'dist');
  }
  const candidate = env[ELECTRON_OUTPUT_DIRECTORY_ENV];
  if (
    typeof candidate !== 'string' ||
    candidate.length === 0 ||
    candidate.includes('\0') ||
    !path.isAbsolute(candidate) ||
    path.normalize(candidate) !== candidate
  ) {
    throw new Error(`${ELECTRON_OUTPUT_DIRECTORY_ENV} must be a normalized absolute path`);
  }
  return candidate;
}

export function expectedPackagedAppPath(outputDirectory) {
  return path.join(outputDirectory, 'mac-arm64', 'Chirality.app');
}

export function buildElectronBuilderArgs(electronDistDirectory, target = 'dir', prepackaged, outputDirectory) {
  if (typeof electronDistDirectory !== 'string' || electronDistDirectory.length === 0) {
    throw new Error('Verified Electron distribution directory is required');
  }
  const validatedTarget = validateTarget(target);
  return [
    '--mac',
    ...(validatedTarget === 'dir' ? ['--dir'] : ['dmg']),
    '--arm64',
    '--publish',
    'never',
    `-c.electronDist=${electronDistDirectory}`,
    ...(outputDirectory ? [`-c.directories.output=${outputDirectory}`] : []),
    ...(prepackaged ? ['--prepackaged', prepackaged] : [])
  ];
}

function spawnAndWait(command, args, options, spawnProcess) {
  return new Promise((resolve, reject) => {
    const child = spawnProcess(command, args, options);
    child.once('error', reject);
    child.once('exit', (code, signal) => {
      if (code === 0) {
        resolve();
        return;
      }
      reject(
        new Error(
          signal
            ? `electron-builder terminated by signal ${signal}`
            : `electron-builder exited with status ${String(code)}`
        )
      );
    });
  });
}

/**
 * @param {{
 *   verify?: typeof verifyElectronDist,
 *   spawnProcess?: typeof spawn,
 *   prepareSupplier?: typeof prepareSupplierResources,
 *   computeDependencyDigest?: typeof computeDependencyResolutionDigest,
 *   env?: NodeJS.ProcessEnv,
 *   target?: string,
 *   runtimeManifestVersion?: string,
 *   runtimeV2Phase?: string,
 *   resumeCheckpoint?: string,
 *   bindPayload?: typeof bindSignedRuntimeV2Payload,
 *   seal?: typeof sealSignedRuntimeV2
 * }} [options]
 */
export async function runElectronPack({
  verify = verifyElectronDist,
  spawnProcess = spawn,
  prepareSupplier = prepareSupplierResources,
  computeDependencyDigest,
  env = process.env,
  target = 'dir',
  runtimeManifestVersion = 'v1',
  runtimeV2Phase,
  resumeCheckpoint,
  bindPayload = bindSignedRuntimeV2Payload,
  seal = sealSignedRuntimeV2
} = {}) {
  const outputDirectory = resolveElectronOutputDirectory(env);
  const packagedAppPath = expectedPackagedAppPath(outputDirectory);
  if (runtimeManifestVersion !== 'v1' && runtimeManifestVersion !== 'v2') {
    throw new Error(`Unsupported Runtime manifest version: ${String(runtimeManifestVersion)}`);
  }
  if (runtimeV2Phase) {
    const selectedCheckpoint = resumeCheckpoint ?? env[SIGNING_CHECKPOINT_FILE_ENV];
    if (runtimeManifestVersion !== 'v2' || !selectedCheckpoint) throw new Error('Runtime v2 payload/seal requires CHIRALITY_RUNTIME_V2_SIGNING_CHECKPOINT_FILE');
    const resumeEnvironment = { ...env, [SIGNING_CHECKPOINT_FILE_ENV]: selectedCheckpoint };
    if (runtimeV2Phase === 'payload') return bindPayload({ env: resumeEnvironment });
    if (runtimeV2Phase !== 'seal') throw new Error(`Unsupported Runtime v2 signing phase: ${runtimeV2Phase}`);
    const sealed = await seal({ env: resumeEnvironment, expectedAppPath: packagedAppPath });
    if (path.resolve(sealed.appPath) !== packagedAppPath) {
      throw new Error(`Sealed application is outside the selected Electron output directory: ${sealed.appPath}`);
    }
    if (target === 'dmg') {
      const electronDistDirectory = await verify();
      await spawnAndWait('electron-builder', buildElectronBuilderArgs(electronDistDirectory, target, sealed.appPath, outputDirectory), {
        stdio: 'inherit', shell: false, env: resumeEnvironment
      }, spawnProcess);
    }
    return sealed;
  }
  const expectedSupplierDigest = expectedDigest(env, EXPECTED_SUPPLIER_DIGEST_ENV);
  const expectedDependencyDigest = expectedDigest(env, EXPECTED_DEPENDENCY_DIGEST_ENV);
  const electronDistDirectory = await verify();
  const supplier = await prepareSupplier({ env });
  const dependencyDigest = await (computeDependencyDigest
    ? computeDependencyDigest()
    : computeDependencyResolutionDigest());
  if (supplier.digest !== expectedSupplierDigest) {
    throw new Error('Staged supplier tree does not match the release-provided expected digest');
  }
  if (dependencyDigest !== expectedDependencyDigest) {
    throw new Error('Dependency resolution inputs do not match the release-provided expected digest');
  }
  const args = buildElectronBuilderArgs(electronDistDirectory, target, undefined, outputDirectory);
  const builderEnvironment = {
    ...env,
    CSC_IDENTITY_AUTO_DISCOVERY: 'false',
    [DEPENDENCY_DIGEST_ENV]: dependencyDigest,
    [SUPPLIER_DIGEST_ENV]: supplier.digest
  };
  if (runtimeManifestVersion === 'v2') {
    if (!/^[A-F0-9]{40}$/.test(env[SIGNING_IDENTITY_SHA1_ENV] ?? '')
      || !/^[A-Z0-9]{10}$/.test(env[SIGNING_TEAM_ID_ENV] ?? '')
      || env[SIGNING_BUNDLE_ID_ENV] !== 'com.chirality.app'
      || !path.isAbsolute(env[SIGNING_CHECKPOINT_FILE_ENV] ?? '')) {
      throw new Error('Runtime v2 signed preparation requires explicit identity, team, bundle, and checkpoint inputs');
    }
    builderEnvironment[RUNTIME_MANIFEST_VERSION_ENV] = 'v2';
    // V2 packages admitted native inputs; rebuilding here changes their basis.
    args.push('-c.npmRebuild=false');
    builderEnvironment.CSC_NAME = env[SIGNING_IDENTITY_SHA1_ENV];
    delete builderEnvironment[RUNTIME_V2_INPUT_DIGEST_ENV];
  } else {
    delete builderEnvironment[RUNTIME_MANIFEST_VERSION_ENV];
    delete builderEnvironment[RUNTIME_V2_INPUT_DIGEST_ENV];
  }
  if (runtimeManifestVersion === 'v2' && await lstat(env[SIGNING_CHECKPOINT_FILE_ENV]).then(() => true, () => false)) {
    throw new Error('Runtime v2 signing checkpoint output already exists');
  }
  try {
    await spawnAndWait('electron-builder', args, {
      stdio: 'inherit',
      shell: false,
      env: builderEnvironment
    }, spawnProcess);
  } catch (error) {
    if (runtimeManifestVersion !== 'v2'
      || !(await lstat(env[SIGNING_CHECKPOINT_FILE_ENV]).then(() => true, () => false))) throw error;
    await supplier.cleanup();
    return { phase: 'nested-signed', checkpointPath: env[SIGNING_CHECKPOINT_FILE_ENV] };
  }
  if (runtimeManifestVersion === 'v2') {
    const checkpointPath = env[SIGNING_CHECKPOINT_FILE_ENV];
    if (!(await lstat(checkpointPath).then(() => true, () => false))) {
      throw new Error('electron-builder completed without the required Runtime v2 nested-signing checkpoint');
    }
    await supplier.cleanup();
    return { phase: 'nested-signed', checkpointPath };
  }
  await supplier.cleanup();
}

export function parseArgs(argv) {
  if (argv.length === 0) return { target: 'dir' };
  const parsed = { target: 'dir', runtimeManifestVersion: undefined, runtimeV2Phase: undefined, resumeCheckpoint: undefined };
  for (let index = 0; index < argv.length; index += 2) {
    const flag = argv[index], value = argv[index + 1];
    if (value === undefined) throw new Error('Usage: node ./scripts/pack-electron-with-supply.mjs [--target dir|dmg] [--runtime-manifest v2] [--resume-checkpoint PATH --runtime-v2-phase payload|seal]');
    if (flag === '--target') parsed.target = validateTarget(value);
    else if (flag === '--runtime-manifest' && value === 'v2') parsed.runtimeManifestVersion = 'v2';
    else if (flag === '--runtime-v2-phase' && (value === 'payload' || value === 'seal')) parsed.runtimeV2Phase = value;
    else if (flag === '--resume-checkpoint' && path.isAbsolute(value) && path.resolve(value) === value) parsed.resumeCheckpoint = value;
    else throw new Error('Usage: node ./scripts/pack-electron-with-supply.mjs [--target dir|dmg] [--runtime-manifest v2] [--resume-checkpoint PATH --runtime-v2-phase payload|seal]');
  }
  return parsed.runtimeManifestVersion ? {
    target: parsed.target,
    runtimeManifestVersion: parsed.runtimeManifestVersion,
    ...(parsed.runtimeV2Phase ? { runtimeV2Phase: parsed.runtimeV2Phase } : {}),
    ...(parsed.resumeCheckpoint ? { resumeCheckpoint: parsed.resumeCheckpoint } : {})
  } : { target: parsed.target };
}

const isMain =
  process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url;
if (isMain) {
  try {
    await runElectronPack(parseArgs(process.argv.slice(2)));
  } catch (error) {
    process.stderr.write(`Offline Electron packaging failed: ${error.message}\n`);
    process.exitCode = 1;
  }
}
