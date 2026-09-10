import { constants, createReadStream } from 'node:fs';
import { createHash } from 'node:crypto';
import { lstat, open, readdir, realpath, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const repositoryRoot = path.resolve(frontendRoot, '..', '..', '..');
const runtimeRoot = path.join(repositoryRoot, 'projects', 'chirality-runtime');
const MANIFEST_NAME = 'runtime-artifact-inventory.json';
const MAX_ENTRIES = 50_000;
const MAX_ROOTS = 32;
const DIGEST_PATTERN = /^[a-f0-9]{64}$/;
const REQUIRED_ROOTS = Object.freeze(['app.asar', 'instruction-root', 'native', 'runtime-cli', 'supplier']);
const REQUIRED_FILES = Object.freeze([
  'app.asar',
  'instruction-root/instruction-bundle-manifest.json',
  'native/chirality_native_admission.node',
  'runtime-cli/chirality-cli.mjs',
  'runtime-cli/chirality-cli.mjs.map',
  'supplier/codex'
]);
export const DEPENDENCY_DIGEST_ENV = 'CHIRALITY_PACKAGING_DEPENDENCY_RESOLUTION_DIGEST';
export const SUPPLIER_DIGEST_ENV = 'CHIRALITY_PACKAGING_SUPPLIER_STAGING_DIGEST';
export const EXPECTED_DEPENDENCY_DIGEST_ENV = 'CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST';
export const EXPECTED_SUPPLIER_DIGEST_ENV = 'CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST';

function hash(value) {
  return createHash('sha256').update(value).digest('hex');
}

async function hashRegularFile(filePath) {
  if (!path.isAbsolute(filePath) || path.resolve(filePath) !== filePath) {
    throw new Error(`Inventory input is not an absolute canonical path: ${filePath}`);
  }
  if ((await realpath(filePath).catch(() => undefined)) !== filePath) {
    throw new Error(`Inventory input is missing, linked, or noncanonical: ${filePath}`);
  }
  const handle = await open(filePath, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await handle.stat({ bigint: true });
    if (!before.isFile()) throw new Error(`Inventory input is not a regular file: ${filePath}`);
    const digest = createHash('sha256');
    let size = 0;
    for await (const chunk of createReadStream(filePath, { fd: handle.fd, autoClose: false })) {
      digest.update(chunk);
      size += chunk.length;
    }
    const after = await handle.stat({ bigint: true });
    const current = await lstat(filePath, { bigint: true });
    for (const key of ['dev', 'ino', 'size', 'mtimeNs', 'ctimeNs', 'mode', 'uid']) {
      if (before[key] !== after[key] || before[key] !== current[key]) {
        throw new Error(`Inventory input changed while hashing: ${filePath}`);
      }
    }
    if (size !== Number(before.size) || (await realpath(filePath)) !== filePath) {
      throw new Error(`Inventory input changed while hashing: ${filePath}`);
    }
    return { sha256: digest.digest('hex'), size, mode: Number(before.mode & 0o777n) };
  } finally {
    await handle.close();
  }
}

async function walkTree(root, { includeDirectories = false } = {}) {
  if (!path.isAbsolute(root) || path.resolve(root) !== root || (await realpath(root).catch(() => undefined)) !== root) {
    throw new Error(`Inventory root must be an existing canonical absolute directory: ${root}`);
  }
  const rootInfo = await lstat(root);
  if (!rootInfo.isDirectory() || rootInfo.isSymbolicLink()) {
    throw new Error(`Inventory root must be a real directory: ${root}`);
  }
  const records = [];
  let visited = 0;
  let fileCount = 0;
  async function visit(directory, relativeDirectory = '') {
    for (const name of (await readdir(directory)).sort()) {
      visited += 1;
      if (visited > MAX_ENTRIES * 2) throw new Error('Resource tree exceeds bounded membership');
      const absolutePath = path.join(directory, name);
      const relativePath = path.posix.join(relativeDirectory, name);
      const info = await lstat(absolutePath);
      if (info.isSymbolicLink() || (await realpath(absolutePath).catch(() => undefined)) !== absolutePath) {
        throw new Error(`Resource tree contains a symlink or noncanonical entry: ${relativePath}`);
      }
      if (info.isDirectory()) {
        if (includeDirectories) records.push({ relativePath, kind: 'directory', mode: info.mode & 0o777 });
        await visit(absolutePath, relativePath);
      } else if (info.isFile()) {
        const identity = await hashRegularFile(absolutePath);
        records.push({ relativePath, kind: 'file', ...identity });
        fileCount += 1;
        if (fileCount > MAX_ENTRIES) {
          throw new Error(`Resource inventory exceeds ${MAX_ENTRIES} files`);
        }
      } else {
        throw new Error(`Resource tree contains a special entry: ${relativePath}`);
      }
    }
  }
  await visit(root);
  return records;
}

export async function computeSupplierTreeDigest(root) {
  const records = await walkTree(root, { includeDirectories: true });
  const executable = records.find((record) => record.relativePath === 'codex');
  if (!executable || executable.kind !== 'file' || (executable.mode & 0o111) === 0) {
    throw new Error('Supplier tree must contain an executable regular file named codex');
  }
  return hash(JSON.stringify(records.map(({ relativePath, kind, mode, sha256, size }) => ({
    relativePath,
    kind,
    mode,
    ...(kind === 'file' ? { sha256, size } : {})
  }))));
}

export async function computeDependencyResolutionDigest({
  lockPaths = [path.join(frontendRoot, 'package-lock.json'), path.join(runtimeRoot, 'package-lock.json')]
} = {}) {
  const records = [];
  for (const lockPath of lockPaths) {
    const identity = await hashRegularFile(lockPath);
    records.push({
      identity: path.relative(repositoryRoot, lockPath).split(path.sep).join('/'),
      sha256: identity.sha256,
      size: identity.size
    });
  }
  records.sort((left, right) => left.identity < right.identity ? -1 : left.identity > right.identity ? 1 : 0);
  return hash(JSON.stringify(records));
}

export async function writeRuntimeArtifactInventory({
  resourcesRoot,
  expectedDependencyResolutionDigest,
  expectedSupplierStagingDigest,
  lockPaths
}) {
  if (!DIGEST_PATTERN.test(expectedDependencyResolutionDigest ?? '')) {
    throw new Error(`Missing or invalid ${DEPENDENCY_DIGEST_ENV}`);
  }
  if (!DIGEST_PATTERN.test(expectedSupplierStagingDigest ?? '')) {
    throw new Error(`Missing or invalid ${SUPPLIER_DIGEST_ENV}`);
  }
  const manifestPath = path.join(resourcesRoot, MANIFEST_NAME);
  if (await lstat(manifestPath).then(() => true, () => false)) {
    throw new Error(`Refusing to overwrite existing Runtime inventory: ${manifestPath}`);
  }
  const dependencyResolutionDigest = await computeDependencyResolutionDigest({ lockPaths });
  if (dependencyResolutionDigest !== expectedDependencyResolutionDigest) {
    throw new Error('Dependency resolution inputs changed after Electron packaging started');
  }
  const walked = await walkTree(resourcesRoot);
  const entries = walked
    .filter((record) => record.kind === 'file' && record.relativePath !== MANIFEST_NAME)
    .map(({ relativePath, sha256, size }) => ({ relativePath, sha256, size }))
    .sort((left, right) => left.relativePath < right.relativePath ? -1 : left.relativePath > right.relativePath ? 1 : 0);
  if (entries.length > MAX_ENTRIES || new Set(entries.map((entry) => entry.relativePath)).size !== entries.length) {
    throw new Error('Runtime resource inventory is too large or contains duplicate paths');
  }
  for (const required of REQUIRED_FILES) {
    if (!entries.some((entry) => entry.relativePath === required)) {
      throw new Error(`Packaged Resources is missing required file: ${required}`);
    }
  }
  const closureRoots = [...new Set([...REQUIRED_ROOTS, ...entries.map((entry) => entry.relativePath.split('/')[0])])].sort();
  if (closureRoots.length > MAX_ROOTS) throw new Error(`Runtime closure exceeds ${MAX_ROOTS} semantic roots`);
  const supplierDigest = await computeSupplierTreeDigest(path.join(resourcesRoot, 'supplier'));
  if (supplierDigest !== expectedSupplierStagingDigest) {
    throw new Error('Packaged supplier tree changed after verified staging');
  }
  const sourceIdentityEntries = entries.filter((entry) => entry.relativePath === 'app.asar' || entry.relativePath.endsWith('.map'));
  if (!sourceIdentityEntries.some((entry) => entry.relativePath === 'app.asar')
    || !sourceIdentityEntries.some((entry) => entry.relativePath === 'runtime-cli/chirality-cli.mjs.map')) {
    throw new Error('Deployed bundle/source-map identity is incomplete');
  }
  const manifest = {
    schema: 'chirality-runtime-artifact-inventory/v1',
    sourceIdentityDigest: hash(JSON.stringify(sourceIdentityEntries)),
    dependencyResolutionDigest,
    closureRoots,
    entries
  };
  await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
  return { manifestPath, manifest };
}

export default async function afterPack(context) {
  if (context?.electronPlatformName !== 'darwin') {
    throw new Error('Runtime artifact inventory currently supports only the macOS Electron package');
  }
  const productFilename = context?.packager?.appInfo?.productFilename;
  if (typeof productFilename !== 'string' || productFilename.trim() !== productFilename || productFilename.length === 0) {
    throw new Error('Electron afterPack context is missing productFilename');
  }
  const resourcesRoot = path.resolve(context.appOutDir, `${productFilename}.app`, 'Contents', 'Resources');
  await writeRuntimeArtifactInventory({
    resourcesRoot,
    expectedDependencyResolutionDigest: process.env[DEPENDENCY_DIGEST_ENV],
    expectedSupplierStagingDigest: process.env[SUPPLIER_DIGEST_ENV]
  });
}
