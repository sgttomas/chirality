import { execFile } from 'node:child_process';
import { createHash } from 'node:crypto';
import { constants, createReadStream } from 'node:fs';
import { chmod, lstat, mkdir, mkdtemp, open, readFile, realpath, rename, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { promisify } from 'node:util';

import { signAsync, walkAsync } from '@electron/osx-sign';
import { verifyPackagedRuntimeBasisV2 } from '@chirality/runtime-core/runtime-conformance-v2';
import {
  HOST_ACCOUNT_SERVICE_NAME,
  HOST_ACCOUNT_SIGNING_PREDICATE_RESOURCE,
  loadHostAccountSigningPredicate,
  parseHostAccountSigningPredicate
} from '@chirality/runtime-daemon';

import {
  DEPENDENCY_DIGEST_ENV,
  RUNTIME_MANIFEST_VERSION_ENV,
  RUNTIME_V2_GOVERNANCE_ROOT_ENV,
  RUNTIME_V2_INPUT_DIGEST_ENV,
  RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV,
  SUPPLIER_DIGEST_ENV,
  computeSupplierTreeDigest,
  inspectRuntimeV2PayloadSnapshot,
  inspectRuntimeV2ReleaseInputs,
  inspectRuntimeV2SupportProfiles,
  stageRuntimeV2Governance,
  verifyPreparedRuntimePayloadV2,
  writeRuntimePolicyParameterDeclarationV2,
  writeRuntimeArtifactInventoryV2,
  writeRuntimePayloadManifestV2
} from './finalize-electron-resources.mjs';

const execFileAsync = promisify(execFile);
const DIGEST = /^[a-f0-9]{64}$/u;
const IDENTITY_SHA1 = /^[A-F0-9]{40}$/u;
const TEAM_ID = /^[A-Z0-9]{10}$/u;
const BUNDLE_ID = /^com\.chirality\.app$/u;
const CHECKPOINT_SCHEMA = 'chirality-signed-runtime-v2-checkpoint/v1';
const CHECKPOINT_MAX_BYTES = 1_048_576;
const OUTER_MAIN_RELATIVE_PATH = 'Contents/MacOS/Chirality';
const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const defaultEntitlements = path.join(frontendRoot, 'build', 'entitlements.mac.plist');
const defaultInheritEntitlements = path.join(frontendRoot, 'build', 'entitlements.mac.inherit.plist');

export const SIGNING_IDENTITY_SHA1_ENV = 'CHIRALITY_SIGNING_IDENTITY_SHA1';
export const SIGNING_TEAM_ID_ENV = 'CHIRALITY_SIGNING_TEAM_ID';
export const SIGNING_BUNDLE_ID_ENV = 'CHIRALITY_SIGNING_BUNDLE_ID';
export const SIGNING_CHECKPOINT_FILE_ENV = 'CHIRALITY_RUNTIME_V2_SIGNING_CHECKPOINT_FILE';
export const SIGNING_ENTITLEMENTS_ENV = 'CHIRALITY_SIGNING_ENTITLEMENTS';
export const SIGNING_INHERIT_ENTITLEMENTS_ENV = 'CHIRALITY_SIGNING_INHERIT_ENTITLEMENTS';

function sha256(value) { return createHash('sha256').update(value).digest('hex'); }

function exactSigningInputs(env) {
  const identitySha1 = env[SIGNING_IDENTITY_SHA1_ENV];
  const teamId = env[SIGNING_TEAM_ID_ENV];
  const bundleId = env[SIGNING_BUNDLE_ID_ENV];
  const checkpointPath = env[SIGNING_CHECKPOINT_FILE_ENV];
  if (!IDENTITY_SHA1.test(identitySha1 ?? '')) throw new Error(`${SIGNING_IDENTITY_SHA1_ENV} must be an uppercase SHA-1 identity`);
  if (!TEAM_ID.test(teamId ?? '')) throw new Error(`${SIGNING_TEAM_ID_ENV} must be a ten-character team identifier`);
  if (!BUNDLE_ID.test(bundleId ?? '')) throw new Error(`${SIGNING_BUNDLE_ID_ENV} must equal the packaged application identifier`);
  if (!path.isAbsolute(checkpointPath ?? '') || path.resolve(checkpointPath) !== checkpointPath) {
    throw new Error(`${SIGNING_CHECKPOINT_FILE_ENV} must be an absolute canonical output path`);
  }
  return { identitySha1, teamId, bundleId, checkpointPath };
}

export function deriveHostPeerRequirement({ bundleId, teamId }) {
  if (!BUNDLE_ID.test(bundleId ?? '') || !TEAM_ID.test(teamId ?? '')) throw new Error('Invalid signing predicate input');
  return `anchor apple generic and identifier "${bundleId}" and certificate leaf[subject.OU] = "${teamId}"`;
}

function codesignDesignatedRequirement(peerRequirement) {
  return `=designated => ${peerRequirement}`;
}

async function defaultInspectBundleId(appPath) {
  const { stdout } = await execFileAsync('/usr/bin/plutil', ['-extract', 'CFBundleIdentifier', 'raw', '-o', '-', path.join(appPath, 'Contents', 'Info.plist')]);
  return stdout.trim();
}

async function stableJson(filePath, maximum = CHECKPOINT_MAX_BYTES) {
  if (!path.isAbsolute(filePath) || path.resolve(filePath) !== filePath || await realpath(filePath).catch(() => undefined) !== filePath) {
    throw new Error('Signing checkpoint is missing, linked, or noncanonical');
  }
  const handle = await open(filePath, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await handle.stat({ bigint: true });
    if (!before.isFile() || before.nlink !== 1n || before.size > BigInt(maximum)) throw new Error('Signing checkpoint is not a bounded regular file');
    const bytes = Buffer.allocUnsafe(maximum + 1);
    let length = 0;
    while (length < bytes.length) {
      let bytesRead;
      try {
        ({ bytesRead } = await handle.read(bytes, length, bytes.length - length, length));
      } catch (error) {
        if (error?.code === 'EINTR') continue;
        throw error;
      }
      if (bytesRead === 0) break;
      length += bytesRead;
    }
    const after = await handle.stat({ bigint: true });
    if (length > maximum) throw new Error('Signing checkpoint is not a bounded regular file');
    if (before.dev !== after.dev || before.ino !== after.ino || before.size !== after.size || before.mtimeNs !== after.mtimeNs || before.ctimeNs !== after.ctimeNs) {
      throw new Error('Signing checkpoint changed while reading');
    }
    if (BigInt(length) !== before.size || BigInt(length) !== after.size) throw new Error('Signing checkpoint read length does not match its file identity');
    const contents = bytes.subarray(0, length);
    return { value: JSON.parse(contents.toString('utf8')), sha256: sha256(contents) };
  } finally { await handle.close(); }
}

async function writeCheckpoint(filePath, value, { replace = false } = {}) {
  const bytes = Buffer.from(`${JSON.stringify(value, null, 2)}\n`);
  if (bytes.length > CHECKPOINT_MAX_BYTES) throw new Error('Signing checkpoint exceeds the bounded size limit');
  await mkdir(path.dirname(filePath), { recursive: true, mode: 0o700 });
  if (!replace) {
    await writeFile(filePath, bytes, { flag: 'wx', mode: 0o600 });
    return;
  }
  const pending = `${filePath}.pending`;
  await writeFile(pending, bytes, { flag: 'wx', mode: 0o600 });
  await rename(pending, filePath);
}

function inspectCheckpoint(value, expectedPhase) {
  const nestedKeys = ['appPath', 'bundleId', 'dependencyDigest', 'identitySha1', 'nestedSignatures', 'payloadSnapshotDigest', 'peerRequirement', 'phase', 'resourcesRoot', 'schema', 'signedSupplierDigest', 'supplierDigest', 'teamId'];
  const payloadKeys = [...nestedKeys, 'payloadManifest', 'supportProfilesIdentity'];
  const expectedKeys = (expectedPhase === 'payload-bound' ? payloadKeys : nestedKeys).sort();
  if (!value || typeof value !== 'object' || Array.isArray(value)
    || Object.keys(value).sort().some((key, index) => key !== expectedKeys[index]) || Object.keys(value).length !== expectedKeys.length
    || value.schema !== CHECKPOINT_SCHEMA || value.phase !== expectedPhase
    || !path.isAbsolute(value.appPath ?? '') || !path.isAbsolute(value.resourcesRoot ?? '')
    || !IDENTITY_SHA1.test(value.identitySha1 ?? '') || !TEAM_ID.test(value.teamId ?? '')
    || !BUNDLE_ID.test(value.bundleId ?? '') || typeof value.peerRequirement !== 'string'
    || !DIGEST.test(value.dependencyDigest ?? '') || !DIGEST.test(value.supplierDigest ?? '')
    || !DIGEST.test(value.signedSupplierDigest ?? '') || !DIGEST.test(value.payloadSnapshotDigest ?? '')
    || !Array.isArray(value.nestedSignatures)
    || value.nestedSignatures.some((record, index, records) => {
      const keys = (record?.type === 'file' ? ['content', 'identitySha256', 'relativePath', 'type'] : ['identitySha256', 'relativePath', 'type']).sort();
      return !record || typeof record !== 'object' || Array.isArray(record)
        || Object.keys(record).sort().some((key, keyIndex) => key !== keys[keyIndex]) || Object.keys(record).length !== keys.length
        || typeof record.relativePath !== 'string' || record.relativePath.length < 1 || path.isAbsolute(record.relativePath) || record.relativePath.includes('..')
        || (record.type !== 'file' && record.type !== 'bundle') || !DIGEST.test(record.identitySha256 ?? '')
        || (record.type === 'file' && (!DIGEST.test(record.content?.sha256 ?? '') || !Number.isSafeInteger(record.content?.size) || record.content.size < 0))
        || (index > 0 && records[index - 1].relativePath >= record.relativePath);
    })
    || (expectedPhase === 'payload-bound' && (!DIGEST.test(value.payloadManifest?.sha256 ?? '')
      || !Number.isSafeInteger(value.payloadManifest?.size) || value.payloadManifest.size < 1
      || !DIGEST.test(value.supportProfilesIdentity?.sha256 ?? '')
      || !Number.isSafeInteger(value.supportProfilesIdentity?.size) || value.supportProfilesIdentity.size < 1))) {
    throw new Error(`Invalid ${expectedPhase} Runtime v2 signing checkpoint`);
  }
  return value;
}

async function assertCheckpointPaths(checkpoint) {
  const appPath = await realpath(checkpoint.appPath).catch(() => undefined);
  const resourcesRoot = appPath && path.join(appPath, 'Contents', 'Resources');
  if (appPath !== checkpoint.appPath || resourcesRoot !== checkpoint.resourcesRoot
    || await realpath(resourcesRoot).catch(() => undefined) !== resourcesRoot) {
    throw new Error('Signing checkpoint application and Resources paths do not match one canonical bundle');
  }
}

function checkpointMatchesInputs(checkpoint, inputs) {
  if (checkpoint.identitySha1 !== inputs.identitySha1 || checkpoint.teamId !== inputs.teamId || checkpoint.bundleId !== inputs.bundleId
    || checkpoint.peerRequirement !== deriveHostPeerRequirement(inputs)) throw new Error('Signing inputs do not match the prepared application');
}

async function writeSigningPredicate(resourcesRoot, inputs) {
  const peerRequirement = deriveHostPeerRequirement(inputs);
  const predicate = parseHostAccountSigningPredicate({
    schema: 'chirality.host-account-signing-predicate/v1',
    serviceName: HOST_ACCOUNT_SERVICE_NAME,
    bundleId: inputs.bundleId,
    teamId: inputs.teamId,
    peerRequirement
  });
  const predicatePath = path.join(resourcesRoot, HOST_ACCOUNT_SIGNING_PREDICATE_RESOURCE);
  await mkdir(path.dirname(predicatePath), { recursive: true, mode: 0o700 });
  await writeFile(predicatePath, `${JSON.stringify(predicate, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
  const loaded = await loadHostAccountSigningPredicate(resourcesRoot);
  if (JSON.stringify(loaded) !== JSON.stringify(predicate)) throw new Error('Packaged signing predicate did not round-trip through Runtime');
  return peerRequirement;
}

export function createRuntimeV2SignOptions(options, { appPath, peerRequirement, outerOnly = false, entitlements, inheritEntitlements }) {
  const original = options.optionsForFile;
  return {
    ...options,
    preAutoEntitlements: false,
    ...(outerOnly ? { ignore: (filePath) => filePath !== appPath, preEmbedProvisioningProfile: false, preAutoEntitlements: false } : {}),
    optionsForFile(filePath) {
      const inherited = original?.(filePath) ?? {};
      const applicationBundle = filePath === appPath || filePath.endsWith('.app');
      return {
        ...inherited,
        entitlements: applicationBundle ? entitlements : inheritEntitlements,
        hardenedRuntime: true,
        requirements: filePath === appPath ? codesignDesignatedRequirement(peerRequirement) : undefined
      };
    }
  };
}

async function defaultVerifyFinal({ appPath, resourcesRoot, peerRequirement, teamId, identitySha1 }) {
  await execFileAsync('/usr/bin/codesign', ['--verify', '--deep', '--strict', '--verbose=2', appPath]);
  await execFileAsync('/usr/bin/codesign', ['--verify', `-R=${peerRequirement}`, appPath]);
  const predicate = await loadHostAccountSigningPredicate(resourcesRoot);
  if (predicate.peerRequirement !== peerRequirement || predicate.teamId !== teamId || predicate.bundleId !== 'com.chirality.app') {
    throw new Error('Final application does not contain the exact sealed signing predicate');
  }
  const certificateRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-signing-certificate-'));
  try {
    const prefix = path.join(certificateRoot, 'certificate');
    await execFileAsync('/usr/bin/codesign', ['-d', '--extract-certificates', prefix, appPath]);
    const leafSha1 = createHash('sha1').update(await readFile(`${prefix}0`)).digest('hex').toUpperCase();
    if (leafSha1 !== identitySha1) throw new Error('Final application certificate does not match the explicit signing identity');
  } finally { await rm(certificateRoot, { recursive: true, force: true }); }
  return verifyPackagedRuntimeBasisV2({ resourcesRoot });
}

function assertTrueNestedSignatures(checkpointSignatures, currentSignatures) {
  const checkpointMain = checkpointSignatures.filter(({ relativePath }) => relativePath === OUTER_MAIN_RELATIVE_PATH);
  const currentMain = currentSignatures.filter(({ relativePath }) => relativePath === OUTER_MAIN_RELATIVE_PATH);
  if (checkpointMain.length !== 1 || currentMain.length !== 1
    || checkpointMain[0].type !== 'file' || currentMain[0].type !== 'file') {
    throw new Error('Outer-owned application executable is missing or ambiguous');
  }
  const checkpointNested = checkpointSignatures.filter(({ relativePath }) => relativePath !== OUTER_MAIN_RELATIVE_PATH);
  const currentNested = currentSignatures.filter(({ relativePath }) => relativePath !== OUTER_MAIN_RELATIVE_PATH);
  if (JSON.stringify(currentNested) !== JSON.stringify(checkpointNested)) {
    throw new Error('Nested signed code changed during outer verification');
  }
  return currentMain[0];
}

function assertOuterMainContent(main, expected) {
  if (!expected || !DIGEST.test(expected.sha256 ?? '') || !Number.isSafeInteger(expected.size) || expected.size < 1
    || main.content?.sha256 !== expected.sha256 || main.content?.size !== expected.size) {
    throw new Error('Outer-owned application executable does not match the accepted content identity');
  }
}

async function writeVerifiedResult({ inputs, checkpoint, inventorySha256 }) {
  const artifactPath = `${inputs.checkpointPath}.sealed.json`;
  await writeCheckpoint(artifactPath, {
    schema: 'chirality-signed-runtime-v2-result/v1',
    appPath: checkpoint.appPath,
    payloadManifest: checkpoint.payloadManifest,
    inventorySha256,
    peerRequirementSha256: sha256(checkpoint.peerRequirement),
    verified: true
  });
  await chmod(artifactPath, 0o400);
  return artifactPath;
}

async function defaultInspectNestedSignatures(appPath) {
  const targets = (await walkAsync(path.join(appPath, 'Contents')))
    .filter((target) => target !== appPath)
    .sort();
  const records = [];
  for (const target of targets) {
    const inspected = await execFileAsync('/usr/bin/codesign', ['-d', '--verbose=4', target]);
    const info = await lstat(target);
    let content;
    if (info.isFile()) {
      const handle = await open(target, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
      try {
        const before = await handle.stat({ bigint: true });
        const digest = createHash('sha256');
        let size = 0;
        for await (const chunk of createReadStream(target, { fd: handle.fd, autoClose: false })) { digest.update(chunk); size += chunk.length; }
        const after = await handle.stat({ bigint: true });
        if (before.dev !== after.dev || before.ino !== after.ino || before.size !== after.size || before.mtimeNs !== after.mtimeNs || size !== Number(before.size)) {
          throw new Error(`Nested signing target changed while hashing: ${target}`);
        }
        content = { size, sha256: digest.digest('hex') };
      } finally { await handle.close(); }
    }
    records.push({
      relativePath: path.relative(appPath, target).split(path.sep).join('/'),
      type: info.isFile() ? 'file' : 'bundle',
      identitySha256: sha256(inspected.stderr),
      ...(content ? { content } : {})
    });
  }
  return records;
}

export async function prepareSignedRuntimeV2(options, {
  env = process.env,
  sign = signAsync,
  inspectBundleId = defaultInspectBundleId,
  inspectNestedSignatures = defaultInspectNestedSignatures,
  entitlements,
  inheritEntitlements
} = {}) {
  const inputs = exactSigningInputs(env);
  if (options.identity !== inputs.identitySha1) throw new Error('Electron Builder selected a different signing identity');
  const appPath = await realpath(options.app);
  if (await inspectBundleId(appPath) !== inputs.bundleId) throw new Error('Packaged application identifier does not match the signing input');
  entitlements ??= env[SIGNING_ENTITLEMENTS_ENV] ?? options.optionsForFile?.(appPath)?.entitlements;
  inheritEntitlements ??= env[SIGNING_INHERIT_ENTITLEMENTS_ENV]
    ?? options.optionsForFile?.(path.join(appPath, 'Contents', 'Frameworks', 'nested'))?.entitlements;
  if (!entitlements || !inheritEntitlements) throw new Error('Explicit signing entitlement files are required');
  const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
  const peerRequirement = await writeSigningPredicate(resourcesRoot, inputs);
  await writeRuntimePolicyParameterDeclarationV2(resourcesRoot);
  await sign(createRuntimeV2SignOptions(options, { appPath, peerRequirement, entitlements, inheritEntitlements }));
  const nestedSignatures = await inspectNestedSignatures(appPath);
  const payloadSnapshot = await inspectRuntimeV2PayloadSnapshot(resourcesRoot);
  const signedSupplierDigest = await computeSupplierTreeDigest(path.join(resourcesRoot, 'supplier'));
  const checkpoint = {
    schema: CHECKPOINT_SCHEMA,
    phase: 'nested-signed',
    appPath,
    resourcesRoot,
    identitySha1: inputs.identitySha1,
    teamId: inputs.teamId,
    bundleId: inputs.bundleId,
    peerRequirement,
    dependencyDigest: env[DEPENDENCY_DIGEST_ENV],
    supplierDigest: env[SUPPLIER_DIGEST_ENV],
    signedSupplierDigest,
    nestedSignatures,
    payloadSnapshotDigest: payloadSnapshot.digest
  };
  if (!DIGEST.test(checkpoint.dependencyDigest ?? '') || !DIGEST.test(checkpoint.supplierDigest ?? '')) throw new Error('Prepared signing inputs are missing bound payload digests');
  await writeCheckpoint(inputs.checkpointPath, checkpoint);
  return { checkpointPath: inputs.checkpointPath, checkpoint };
}

export async function bindSignedRuntimeV2Payload({ env = process.env, lockPaths } = {}) {
  const inputs = exactSigningInputs(env);
  const source = await stableJson(inputs.checkpointPath);
  const checkpoint = inspectCheckpoint(source.value, 'nested-signed');
  await assertCheckpointPaths(checkpoint);
  checkpointMatchesInputs(checkpoint, inputs);
  const preparedSnapshot = await inspectRuntimeV2PayloadSnapshot(checkpoint.resourcesRoot);
  if (preparedSnapshot.digest !== checkpoint.payloadSnapshotDigest) throw new Error('Prepared signed payload bytes changed before profile binding');
  const supportProfilesPath = env[RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV];
  if (!supportProfilesPath) throw new Error('Accepted Runtime v2 support profiles are required for payload binding');
  const profiles = await inspectRuntimeV2SupportProfiles(supportProfilesPath);
  await writeRuntimePayloadManifestV2({
    resourcesRoot: checkpoint.resourcesRoot,
    expectedDependencyResolutionDigest: checkpoint.dependencyDigest,
    expectedSupplierStagingDigest: checkpoint.signedSupplierDigest,
    supportProfiles: profiles.supportProfiles,
    lockPaths
  });
  const payload = await verifyPreparedRuntimePayloadV2({ resourcesRoot: checkpoint.resourcesRoot });
  await writeCheckpoint(inputs.checkpointPath, {
    ...checkpoint,
    phase: 'payload-bound',
    payloadManifest: { sha256: payload.sha256, size: payload.size },
    supportProfilesIdentity: { sha256: profiles.sha256, size: profiles.size }
  }, { replace: true });
  return { checkpointPath: inputs.checkpointPath, payloadManifest: payload.manifestPath };
}

/**
 * @param {{
 *   env?: NodeJS.ProcessEnv,
 *   expectedAppPath?: string,
 *   sign?: typeof signAsync,
 *   verifyFinal?: (input: {appPath: string, resourcesRoot: string, peerRequirement: string, teamId: string, identitySha1: string}) => Promise<unknown>,
 *   inspectNestedSignatures?: typeof defaultInspectNestedSignatures,
 *   verifyPayload?: typeof verifyPreparedRuntimePayloadV2,
 *   inspectReleaseInputs?: typeof inspectRuntimeV2ReleaseInputs,
 *   inspectSupportProfiles?: typeof inspectRuntimeV2SupportProfiles,
 *   stageGovernance?: typeof stageRuntimeV2Governance,
 *   writeInventory?: typeof writeRuntimeArtifactInventoryV2
 * }} [options]
 */
export async function sealSignedRuntimeV2({
  env = process.env,
  expectedAppPath,
  sign = signAsync,
  verifyFinal = defaultVerifyFinal,
  inspectNestedSignatures = defaultInspectNestedSignatures,
  verifyPayload = verifyPreparedRuntimePayloadV2,
  inspectReleaseInputs = inspectRuntimeV2ReleaseInputs,
  inspectSupportProfiles = inspectRuntimeV2SupportProfiles,
  stageGovernance = stageRuntimeV2Governance,
  writeInventory = writeRuntimeArtifactInventoryV2
} = {}) {
  const inputs = exactSigningInputs(env);
  const source = await stableJson(inputs.checkpointPath);
  const checkpoint = inspectCheckpoint(source.value, 'payload-bound');
  await assertCheckpointPaths(checkpoint);
  if (expectedAppPath !== undefined) {
    if (typeof expectedAppPath !== 'string' || !path.isAbsolute(expectedAppPath)
      || path.resolve(expectedAppPath) !== expectedAppPath || checkpoint.appPath !== expectedAppPath) {
      throw new Error('Signing checkpoint application does not match the selected Electron packaging candidate');
    }
  }
  checkpointMatchesInputs(checkpoint, inputs);
  const payload = await verifyPayload({ resourcesRoot: checkpoint.resourcesRoot });
  if (payload.sha256 !== checkpoint.payloadManifest?.sha256 || payload.size !== checkpoint.payloadManifest?.size) throw new Error('Prepared Runtime v2 payload manifest changed before sealing');
  const nestedSignatures = await inspectNestedSignatures(checkpoint.appPath);
  if (JSON.stringify(nestedSignatures) !== JSON.stringify(checkpoint.nestedSignatures)) throw new Error('Nested signed code changed before outer sealing');
  const release = await inspectReleaseInputs({
    supportProfilesPath: env[RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV],
    governanceRoot: env[RUNTIME_V2_GOVERNANCE_ROOT_ENV]
  });
  const supportIdentity = await inspectSupportProfiles(env[RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV]);
  if (supportIdentity.sha256 !== checkpoint.supportProfilesIdentity?.sha256 || supportIdentity.size !== checkpoint.supportProfilesIdentity?.size
    || release.digest !== env[RUNTIME_V2_INPUT_DIGEST_ENV]) throw new Error('Accepted Runtime v2 inputs changed before sealing');
  await stageGovernance({ resourcesRoot: checkpoint.resourcesRoot, governance: release.governance });
  const inventory = await writeInventory({
    resourcesRoot: checkpoint.resourcesRoot,
    expectedGovernance: release.governance.map(({ relativePath, size, sha256: digest }) => ({ relativePath, size, sha256: digest }))
  });
  await sign(createRuntimeV2SignOptions({ app: checkpoint.appPath, platform: 'darwin', type: 'distribution', identity: inputs.identitySha1 }, {
    appPath: checkpoint.appPath,
    peerRequirement: checkpoint.peerRequirement,
    outerOnly: true,
    entitlements: env[SIGNING_ENTITLEMENTS_ENV] ?? defaultEntitlements,
    inheritEntitlements: env[SIGNING_INHERIT_ENTITLEMENTS_ENV] ?? defaultInheritEntitlements
  }));
  await verifyFinal({ appPath: checkpoint.appPath, resourcesRoot: checkpoint.resourcesRoot, peerRequirement: checkpoint.peerRequirement, teamId: checkpoint.teamId, identitySha1: checkpoint.identitySha1 });
  const finalNestedSignatures = await inspectNestedSignatures(checkpoint.appPath);
  assertTrueNestedSignatures(checkpoint.nestedSignatures, finalNestedSignatures);
  const artifactPath = await writeVerifiedResult({ inputs, checkpoint, inventorySha256: inventory.verified.inventorySha256 });
  return { appPath: checkpoint.appPath, artifactPath, inventory };
}

/**
 * Complete a previously outer-signed Runtime v2 candidate without mutating the
 * application. This is intentionally limited to verification and the final
 * create-only result record.
 * @param {{
 *   env?: NodeJS.ProcessEnv,
 *   expectedAppPath: string,
 *   expectedOuterMainContent: {sha256: string, size: number},
 *   verifyFinal?: (input: {appPath: string, resourcesRoot: string, peerRequirement: string, teamId: string, identitySha1: string}) => Promise<Readonly<import('@chirality/runtime-core/runtime-conformance-v2').VerifiedPackagedRuntimeBasisV2>>,
 *   inspectNestedSignatures?: typeof defaultInspectNestedSignatures,
 *   inspectReleaseInputs?: typeof inspectRuntimeV2ReleaseInputs,
 *   inspectSupportProfiles?: typeof inspectRuntimeV2SupportProfiles
 * }} options
 */
export async function completeSignedRuntimeV2Verification({
  env = process.env,
  expectedAppPath,
  expectedOuterMainContent,
  verifyFinal = defaultVerifyFinal,
  inspectNestedSignatures = defaultInspectNestedSignatures,
  inspectReleaseInputs = inspectRuntimeV2ReleaseInputs,
  inspectSupportProfiles = inspectRuntimeV2SupportProfiles
} = {}) {
  const inputs = exactSigningInputs(env);
  const source = await stableJson(inputs.checkpointPath);
  const checkpoint = inspectCheckpoint(source.value, 'payload-bound');
  await assertCheckpointPaths(checkpoint);
  if (typeof expectedAppPath !== 'string' || !path.isAbsolute(expectedAppPath)
    || path.resolve(expectedAppPath) !== expectedAppPath || checkpoint.appPath !== expectedAppPath) {
    throw new Error('Signing checkpoint application does not match the selected Electron packaging candidate');
  }
  checkpointMatchesInputs(checkpoint, inputs);
  const nestedSignatures = await inspectNestedSignatures(checkpoint.appPath);
  assertOuterMainContent(assertTrueNestedSignatures(checkpoint.nestedSignatures, nestedSignatures), expectedOuterMainContent);
  const release = await inspectReleaseInputs({
    supportProfilesPath: env[RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV],
    governanceRoot: env[RUNTIME_V2_GOVERNANCE_ROOT_ENV]
  });
  const supportIdentity = await inspectSupportProfiles(env[RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV]);
  if (supportIdentity.sha256 !== checkpoint.supportProfilesIdentity.sha256
    || supportIdentity.size !== checkpoint.supportProfilesIdentity.size
    || release.digest !== env[RUNTIME_V2_INPUT_DIGEST_ENV]) {
    throw new Error('Accepted Runtime v2 inputs changed before verification completion');
  }
  const basis = await verifyFinal({
    appPath: checkpoint.appPath,
    resourcesRoot: checkpoint.resourcesRoot,
    peerRequirement: checkpoint.peerRequirement,
    teamId: checkpoint.teamId,
    identitySha1: checkpoint.identitySha1
  });
  if (!basis || basis.payloadDigest !== checkpoint.payloadManifest.sha256
    || basis.inventory?.payloadManifest.sha256 !== checkpoint.payloadManifest.sha256
    || basis.inventory.payloadManifest.size !== checkpoint.payloadManifest.size) {
    throw new Error('Packaged Runtime v2 payload identity does not match the signing checkpoint');
  }
  const expectedGovernance = release.governance.map(({ relativePath, size, sha256: digest }) => ({ relativePath, size, sha256: digest }));
  if (JSON.stringify(basis.inventory.governance) !== JSON.stringify(expectedGovernance)) {
    throw new Error('Packaged Runtime v2 governance inventory does not match the accepted inputs');
  }
  const finalNestedSignatures = await inspectNestedSignatures(checkpoint.appPath);
  assertOuterMainContent(assertTrueNestedSignatures(checkpoint.nestedSignatures, finalNestedSignatures), expectedOuterMainContent);
  const artifactPath = await writeVerifiedResult({ inputs, checkpoint, inventorySha256: basis.inventorySha256 });
  return { appPath: checkpoint.appPath, artifactPath, inventory: basis.inventory };
}

export default async function customMacSign(options) {
  if (process.env[RUNTIME_MANIFEST_VERSION_ENV] !== 'v2') return signAsync(options);
  const result = await prepareSignedRuntimeV2(options);
  throw new Error(`Runtime v2 nested signing prepared at ${result.checkpointPath}; bind accepted support and governance inputs before outer sealing`);
}
