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
  SUPPLIER_DIGEST_ENV
} from './finalize-electron-resources.mjs';

const SUPPORTED_TARGETS = new Set(['dir', 'dmg']);
const SUPPLIER_SOURCE_ENV = 'CHIRALITY_SUPPLIER_SOURCE_ROOT';
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
  const executable = records.find((entry) => entry.relativePath === 'codex');
  if (!executable || executable.directory || (executable.mode & 0o111) === 0) {
    throw new Error('Supplier source must contain an executable regular file named codex');
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

export function buildElectronBuilderArgs(electronDistDirectory, target = 'dir') {
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
    `-c.electronDist=${electronDistDirectory}`
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

export async function runElectronPack({
  verify = verifyElectronDist,
  spawnProcess = spawn,
  prepareSupplier = prepareSupplierResources,
  computeDependencyDigest,
  env = process.env,
  target = 'dir'
} = {}) {
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
  const args = buildElectronBuilderArgs(electronDistDirectory, target);
  await spawnAndWait('electron-builder', args, {
    stdio: 'inherit',
    shell: false,
    env: {
      ...env,
      CSC_IDENTITY_AUTO_DISCOVERY: 'false',
      [DEPENDENCY_DIGEST_ENV]: dependencyDigest,
      [SUPPLIER_DIGEST_ENV]: supplier.digest
    }
  }, spawnProcess);
  await supplier.cleanup();
}

export function parseArgs(argv) {
  if (argv.length === 0) return { target: 'dir' };
  if (argv.length === 2 && argv[0] === '--target') {
    return { target: validateTarget(argv[1]) };
  }
  throw new Error('Usage: node ./scripts/pack-electron-with-supply.mjs [--target dir|dmg]');
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
