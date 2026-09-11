import { constants, createReadStream } from 'node:fs';
import { createHash } from 'node:crypto';
import { lstat, mkdir, open, readdir, realpath, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  RUNTIME_V2_REQUIRED_PAYLOAD_FILES,
  RUNTIME_V2_REQUIRED_PAYLOAD_ROOTS,
  compareRuntimeUtf8V2,
  decodeRuntimePayloadManifestV2,
  encodeRuntimeArtifactInventoryV2,
  encodeRuntimePayloadManifestV2,
  encodeRuntimePolicyParameterDeclarationV2,
  verifyPackagedRuntimeBasisV2
} from '@chirality/runtime-core/runtime-conformance-v2';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const repositoryRoot = path.resolve(frontendRoot, '..', '..', '..');
const runtimeRoot = path.join(repositoryRoot, 'projects', 'chirality-runtime');
const MANIFEST_NAME = 'runtime-artifact-inventory.json';
const PAYLOAD_MANIFEST_V2_NAME = 'runtime-payload-manifest.json';
const INVENTORY_V2_NAME = 'runtime-artifact-inventory-v2.json';
const POLICY_DECLARATION_V2 = 'runtime-contracts/runtime-policy-parameters-v2.json';
const GOVERNANCE_V2_DIRECTORY = 'runtime-governance/v2';
const GOVERNANCE_V2_FILES = Object.freeze([
  'login-purpose-record.json',
  'login-purpose-acceptance.json',
  'login-owner-act',
  'worker-purpose-record.json',
  'worker-purpose-acceptance.json',
  'worker-owner-act'
]);
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
export const RUNTIME_MANIFEST_VERSION_ENV = 'CHIRALITY_RUNTIME_MANIFEST_VERSION';
export const RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV = 'CHIRALITY_RUNTIME_V2_SUPPORT_PROFILES_FILE';
export const RUNTIME_V2_GOVERNANCE_ROOT_ENV = 'CHIRALITY_RUNTIME_V2_GOVERNANCE_ROOT';
export const RUNTIME_V2_INPUT_DIGEST_ENV = 'CHIRALITY_RUNTIME_V2_INPUT_DIGEST';

function hash(value) {
  return createHash('sha256').update(value).digest('hex');
}

async function hashRegularFile(filePath, maximum = Number.MAX_SAFE_INTEGER) {
  if (!path.isAbsolute(filePath) || path.resolve(filePath) !== filePath) {
    throw new Error(`Inventory input is not an absolute canonical path: ${filePath}`);
  }
  if ((await realpath(filePath).catch(() => undefined)) !== filePath) {
    throw new Error(`Inventory input is missing, linked, or noncanonical: ${filePath}`);
  }
  const handle = await open(filePath, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await handle.stat({ bigint: true });
    if (!before.isFile() || before.nlink !== 1n || before.size > BigInt(maximum)) {
      throw new Error(`Inventory input is not a bounded singly-linked regular file: ${filePath}`);
    }
    const digest = createHash('sha256');
    let size = 0;
    for await (const chunk of createReadStream(filePath, { fd: handle.fd, autoClose: false })) {
      digest.update(chunk);
      size += chunk.length;
    }
    const after = await handle.stat({ bigint: true });
    const current = await lstat(filePath, { bigint: true });
    for (const key of ['dev', 'ino', 'size', 'mtimeNs', 'ctimeNs', 'mode', 'uid', 'nlink']) {
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

async function readBoundedFile(filePath, maximum) {
  if (!path.isAbsolute(filePath) || path.resolve(filePath) !== filePath || (await realpath(filePath).catch(() => undefined)) !== filePath) {
    throw new Error(`Inventory input is missing, linked, or noncanonical: ${filePath}`);
  }
  const handle = await open(filePath, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await handle.stat({ bigint: true });
    if (!before.isFile() || before.nlink !== 1n || before.size > BigInt(maximum)) {
      throw new Error(`Inventory input is not a bounded singly-linked regular file: ${filePath}`);
    }
    const bytes = await handle.readFile();
    const after = await handle.stat({ bigint: true });
    const current = await lstat(filePath, { bigint: true });
    for (const key of ['dev', 'ino', 'size', 'mtimeNs', 'ctimeNs', 'mode', 'uid', 'nlink']) {
      if (before[key] !== after[key] || before[key] !== current[key]) {
        throw new Error(`Inventory input changed while reading: ${filePath}`);
      }
    }
    if (bytes.length !== Number(before.size) || (await realpath(filePath)) !== filePath) {
      throw new Error(`Inventory input changed while reading: ${filePath}`);
    }
    return { sha256: hash(bytes), size: bytes.length, bytes };
  } finally {
    await handle.close();
  }
}

async function readBoundedJson(filePath, maximum) {
  const source = await readBoundedFile(filePath, maximum);
  return { ...source, value: JSON.parse(source.bytes.toString('utf8')) };
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

async function inspectRuntimeV2GovernanceSource(governanceRoot) {
  if (!path.isAbsolute(governanceRoot) || path.resolve(governanceRoot) !== governanceRoot
    || (await realpath(governanceRoot).catch(() => undefined)) !== governanceRoot
    || !(await lstat(governanceRoot)).isDirectory()) {
    throw new Error(`${RUNTIME_V2_GOVERNANCE_ROOT_ENV} must identify a canonical directory`);
  }
  const names = (await readdir(governanceRoot)).sort(compareRuntimeUtf8V2);
  const expected = [...GOVERNANCE_V2_FILES].sort(compareRuntimeUtf8V2);
  if (names.length !== expected.length || names.some((name, index) => name !== expected[index])) {
    throw new Error('Runtime v2 governance input must contain exactly the fixed six files');
  }
  const records = [];
  for (const name of GOVERNANCE_V2_FILES) {
    const source = await readBoundedFile(path.join(governanceRoot, name), 1_048_576);
    records.push({ relativePath: `${GOVERNANCE_V2_DIRECTORY}/${name}`, ...source });
  }
  if (records.reduce((sum, record) => sum + record.size, 0) > 6_291_456) {
    throw new Error('Runtime v2 governance input exceeds its aggregate bound');
  }
  return records;
}

export async function inspectRuntimeV2ReleaseInputs({ supportProfilesPath, governanceRoot }) {
  const profileSource = await inspectRuntimeV2SupportProfiles(supportProfilesPath);
  const governance = await inspectRuntimeV2GovernanceSource(governanceRoot);
  const digest = hash(JSON.stringify({
    supportProfiles: { sha256: profileSource.sha256, size: profileSource.size },
    governance: governance.map(({ relativePath, sha256, size }) => ({ relativePath, sha256, size }))
  }));
  return { digest, supportProfiles: profileSource.supportProfiles, governance };
}

export async function inspectRuntimeV2SupportProfiles(supportProfilesPath) {
  const profileSource = await readBoundedJson(supportProfilesPath, 1_048_576);
  if (!Array.isArray(profileSource.value) || profileSource.value.length < 1 || profileSource.value.length > 8) {
    throw new Error('Runtime v2 support profile input must be a nonempty bounded JSON array');
  }
  return { sha256: profileSource.sha256, size: profileSource.size, supportProfiles: profileSource.value };
}

export async function stageRuntimeV2Governance({ resourcesRoot, governance }) {
  const governanceDirectory = path.join(resourcesRoot, 'runtime-governance');
  const targetRoot = path.join(resourcesRoot, GOVERNANCE_V2_DIRECTORY);
  if (await lstat(governanceDirectory).then(() => true, () => false)) {
    throw new Error('Refusing to overwrite existing Runtime v2 governance resources');
  }
  await mkdir(governanceDirectory, { mode: 0o700 });
  await mkdir(targetRoot, { mode: 0o700 });
  for (const record of governance) {
    const expectedPath = `${GOVERNANCE_V2_DIRECTORY}/${path.basename(record.relativePath)}`;
    if (record.relativePath !== expectedPath || !GOVERNANCE_V2_FILES.includes(path.basename(record.relativePath))) {
      throw new Error('Runtime v2 governance staging received an unknown member');
    }
    await writeFile(path.join(resourcesRoot, record.relativePath), record.bytes, { flag: 'wx', mode: 0o600 });
    const staged = await hashRegularFile(path.join(resourcesRoot, record.relativePath), 1_048_576);
    if (staged.sha256 !== record.sha256 || staged.size !== record.size) {
      throw new Error(`Runtime v2 governance input changed during staging: ${record.relativePath}`);
    }
  }
}

async function payloadEntriesV2(resourcesRoot) {
  const records = await walkTree(resourcesRoot, { includeDirectories: true });
  return records
    .filter((record) => record.relativePath !== PAYLOAD_MANIFEST_V2_NAME
      && record.relativePath !== INVENTORY_V2_NAME
      && record.relativePath !== 'runtime-governance'
      && !record.relativePath.startsWith('runtime-governance/'))
    .map((record) => record.kind === 'directory'
      ? { relativePath: record.relativePath, type: 'directory' }
      : { relativePath: record.relativePath, type: 'file', size: record.size, sha256: record.sha256 })
    .sort((left, right) => compareRuntimeUtf8V2(left.relativePath, right.relativePath));
}

export async function inspectRuntimeV2PayloadSnapshot(resourcesRoot) {
  const entries = await payloadEntriesV2(resourcesRoot);
  return { entries, digest: hash(JSON.stringify(entries)) };
}

export async function writeRuntimePolicyParameterDeclarationV2(resourcesRoot) {
  const contractsRoot = path.join(resourcesRoot, 'runtime-contracts');
  if (await lstat(contractsRoot).then(() => true, () => false)) {
    if ((await realpath(contractsRoot).catch(() => undefined)) !== contractsRoot || !(await lstat(contractsRoot)).isDirectory()) {
      throw new Error('Runtime v2 contract root must be a canonical directory');
    }
  } else await mkdir(contractsRoot, { mode: 0o700 });
  const policyPath = path.join(resourcesRoot, POLICY_DECLARATION_V2);
  const expected = encodeRuntimePolicyParameterDeclarationV2();
  if (await lstat(policyPath).then(() => true, () => false)) {
    const current = await readBoundedFile(policyPath, 1_048_576);
    if (Buffer.compare(current.bytes, expected) !== 0) throw new Error('Runtime v2 policy declaration changed before payload binding');
  } else await writeFile(policyPath, expected, { flag: 'wx', mode: 0o600 });
  return policyPath;
}

export async function writeRuntimePayloadManifestV2({
  resourcesRoot,
  expectedDependencyResolutionDigest,
  expectedSupplierStagingDigest,
  supportProfiles,
  lockPaths
}) {
  if (!DIGEST_PATTERN.test(expectedDependencyResolutionDigest ?? '')) throw new Error(`Missing or invalid ${DEPENDENCY_DIGEST_ENV}`);
  if (!DIGEST_PATTERN.test(expectedSupplierStagingDigest ?? '')) throw new Error(`Missing or invalid ${SUPPLIER_DIGEST_ENV}`);
  for (const name of [PAYLOAD_MANIFEST_V2_NAME, INVENTORY_V2_NAME]) {
    if (await lstat(path.join(resourcesRoot, name)).then(() => true, () => false)) {
      throw new Error(`Refusing to overwrite existing Runtime v2 output: ${name}`);
    }
  }
  const dependencyResolutionDigest = await computeDependencyResolutionDigest({ lockPaths });
  if (dependencyResolutionDigest !== expectedDependencyResolutionDigest) throw new Error('Dependency resolution inputs changed after Electron packaging started');
  const supplierDigest = await computeSupplierTreeDigest(path.join(resourcesRoot, 'supplier'));
  if (supplierDigest !== expectedSupplierStagingDigest) throw new Error('Packaged supplier tree changed after verified staging');

  await writeRuntimePolicyParameterDeclarationV2(resourcesRoot);

  const entries = await payloadEntriesV2(resourcesRoot);
  if (entries.length > MAX_ENTRIES) throw new Error('Runtime v2 payload exceeds 50000 entries');
  const roots = entries.filter((entry) => !entry.relativePath.includes('/')).map((entry) => entry.relativePath);
  for (const required of RUNTIME_V2_REQUIRED_PAYLOAD_ROOTS) if (!roots.includes(required)) throw new Error(`Packaged Resources is missing required v2 root: ${required}`);
  for (const required of RUNTIME_V2_REQUIRED_PAYLOAD_FILES) if (!entries.some((entry) => entry.relativePath === required && entry.type === 'file')) throw new Error(`Packaged Resources is missing required v2 file: ${required}`);
  const byPath = new Map(entries.filter((entry) => entry.type === 'file').map((entry) => [entry.relativePath, entry]));
  const native = byPath.get('native/chirality_native_admission.node');
  const supplier = byPath.get('supplier/codex');
  for (const profile of supportProfiles ?? []) {
    if (profile?.nativeAdmission?.sha256 !== native?.sha256 || profile?.nativeAdmission?.size !== native?.size
      || profile?.supplier?.sha256 !== supplier?.sha256 || profile?.supplier?.size !== supplier?.size) {
      throw new Error('Runtime v2 support profile does not match the packaged payload');
    }
  }
  const manifest = {
    schema: 'chirality-runtime-payload-manifest/v2',
    dependencyResolutionDigest,
    roots,
    supportProfiles,
    entries
  };
  const bytes = encodeRuntimePayloadManifestV2(manifest);
  const manifestPath = path.join(resourcesRoot, PAYLOAD_MANIFEST_V2_NAME);
  await writeFile(manifestPath, bytes, { flag: 'wx', mode: 0o600 });
  return { manifestPath, manifest };
}

export async function verifyPreparedRuntimePayloadV2({ resourcesRoot }) {
  const manifestPath = path.join(resourcesRoot, PAYLOAD_MANIFEST_V2_NAME);
  const source = await readBoundedFile(manifestPath, 16_777_216);
  const manifest = decodeRuntimePayloadManifestV2(source.bytes);
  const entries = await payloadEntriesV2(resourcesRoot);
  if (encodeRuntimePayloadManifestV2({ ...manifest, entries }).compare(source.bytes) !== 0) {
    throw new Error('Prepared Runtime v2 payload changed after its manifest was written');
  }
  return { manifestPath, manifest, sha256: source.sha256, size: source.size };
}

export async function writeRuntimeArtifactInventoryV2({ resourcesRoot, expectedGovernance }) {
  const governanceRoot = path.join(resourcesRoot, GOVERNANCE_V2_DIRECTORY);
  const names = (await readdir(governanceRoot).catch(() => [])).sort(compareRuntimeUtf8V2);
  const expected = [...GOVERNANCE_V2_FILES].sort(compareRuntimeUtf8V2);
  if (names.length !== expected.length || names.some((name, index) => name !== expected[index])) {
    throw new Error('Packaged Runtime v2 governance must contain exactly the fixed six files');
  }
  if (!Array.isArray(expectedGovernance) || expectedGovernance.length !== GOVERNANCE_V2_FILES.length) {
    throw new Error('Runtime v2 inventory requires the bound fixed-six governance identities');
  }
  const governance = [];
  for (const [index, name] of GOVERNANCE_V2_FILES.entries()) {
    const relativePath = `${GOVERNANCE_V2_DIRECTORY}/${name}`;
    const { sha256, size } = await hashRegularFile(path.join(resourcesRoot, relativePath), 1_048_576);
    const bound = expectedGovernance[index];
    if (!bound || bound.relativePath !== relativePath || bound.size !== size || bound.sha256 !== sha256) {
      throw new Error(`Runtime v2 governance changed after staging: ${relativePath}`);
    }
    governance.push({ relativePath: bound.relativePath, size: bound.size, sha256: bound.sha256 });
  }
  const payloadIdentity = await hashRegularFile(path.join(resourcesRoot, PAYLOAD_MANIFEST_V2_NAME), 16_777_216);
  const payloadManifest = { relativePath: PAYLOAD_MANIFEST_V2_NAME, size: payloadIdentity.size, sha256: payloadIdentity.sha256 };
  const inventory = { schema: 'chirality-runtime-artifact-inventory/v2', payloadManifest, governance };
  const inventoryPath = path.join(resourcesRoot, INVENTORY_V2_NAME);
  await writeFile(inventoryPath, encodeRuntimeArtifactInventoryV2(inventory), { flag: 'wx', mode: 0o600 });
  const verified = await verifyPackagedRuntimeBasisV2({ resourcesRoot });
  return { inventoryPath, inventory, verified };
}

export async function finalizeRuntimeResourcesV2({
  resourcesRoot,
  expectedDependencyResolutionDigest,
  expectedSupplierStagingDigest,
  supportProfilesPath,
  governanceRoot,
  expectedInputDigest,
  lockPaths
}) {
  const inputs = await inspectRuntimeV2ReleaseInputs({ supportProfilesPath, governanceRoot });
  if (!DIGEST_PATTERN.test(expectedInputDigest ?? '') || inputs.digest !== expectedInputDigest) {
    throw new Error('Runtime v2 release inputs changed after Electron packaging started');
  }
  await stageRuntimeV2Governance({ resourcesRoot, governance: inputs.governance });
  await writeRuntimePayloadManifestV2({ resourcesRoot, expectedDependencyResolutionDigest, expectedSupplierStagingDigest, supportProfiles: inputs.supportProfiles, lockPaths });
  return writeRuntimeArtifactInventoryV2({
    resourcesRoot,
    expectedGovernance: inputs.governance.map(({ relativePath, size, sha256 }) => ({ relativePath, size, sha256 }))
  });
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

export default async function afterPack(context, { env = process.env } = {}) {
  if (context?.electronPlatformName !== 'darwin') {
    throw new Error('Runtime artifact inventory currently supports only the macOS Electron package');
  }
  const productFilename = context?.packager?.appInfo?.productFilename;
  if (typeof productFilename !== 'string' || productFilename.trim() !== productFilename || productFilename.length === 0) {
    throw new Error('Electron afterPack context is missing productFilename');
  }
  const resourcesRoot = path.resolve(context.appOutDir, `${productFilename}.app`, 'Contents', 'Resources');
  const manifestVersion = env[RUNTIME_MANIFEST_VERSION_ENV];
  if (manifestVersion !== undefined && manifestVersion !== 'v2') {
    throw new Error(`Unsupported Runtime manifest version: ${manifestVersion}`);
  }
  if (manifestVersion === 'v2') {
    if (!DIGEST_PATTERN.test(env[DEPENDENCY_DIGEST_ENV] ?? '') || !DIGEST_PATTERN.test(env[SUPPLIER_DIGEST_ENV] ?? '')) {
      throw new Error('Runtime v2 signed preparation requires bound dependency and supplier digests');
    }
    for (const name of [PAYLOAD_MANIFEST_V2_NAME, INVENTORY_V2_NAME]) {
      if (await lstat(path.join(resourcesRoot, name)).then(() => true, () => false)) {
        throw new Error(`Signed Runtime v2 preparation found premature output: ${name}`);
      }
    }
    return;
  }
  await writeRuntimeArtifactInventory({
    resourcesRoot,
    expectedDependencyResolutionDigest: env[DEPENDENCY_DIGEST_ENV],
    expectedSupplierStagingDigest: env[SUPPLIER_DIGEST_ENV]
  });
}
