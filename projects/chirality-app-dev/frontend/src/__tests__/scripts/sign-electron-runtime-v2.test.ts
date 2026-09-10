import { createHash } from 'node:crypto';
import { appendFile, chmod, lstat, mkdtemp, mkdir, open, readFile, realpath, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { describe, expect, it, vi } from 'vitest';
import { signAsync, walkAsync } from '@electron/osx-sign';
import type { RuntimeArtifactEntryV2, RuntimePayloadManifestV2, VerifiedPackagedRuntimeBasisV2 } from '@chirality/runtime-core/runtime-conformance-v2';

import {
  SIGNING_BUNDLE_ID_ENV,
  SIGNING_CHECKPOINT_FILE_ENV,
  SIGNING_IDENTITY_SHA1_ENV,
  SIGNING_TEAM_ID_ENV,
  bindSignedRuntimeV2Payload,
  completeSignedRuntimeV2Verification,
  createRuntimeV2SignOptions,
  deriveHostPeerRequirement,
  prepareSignedRuntimeV2,
  sealSignedRuntimeV2
} from '../../../scripts/sign-electron-runtime-v2.mjs';
import {
  DEPENDENCY_DIGEST_ENV,
  RUNTIME_V2_GOVERNANCE_ROOT_ENV,
  RUNTIME_V2_INPUT_DIGEST_ENV,
  RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV,
  SUPPLIER_DIGEST_ENV,
  computeDependencyResolutionDigest,
  computeSupplierTreeDigest,
  finalizeRuntimeResourcesV2,
  inspectRuntimeV2ReleaseInputs
} from '../../../scripts/finalize-electron-resources.mjs';
import {
  RUNTIME_NATIVE_ADMISSION_NAPI_VERSION_V2,
  runtimePolicyParameterSchemaDigestV2,
  verifyPackagedRuntimeBasisV2
} from '@chirality/runtime-core/runtime-conformance-v2';

type GovernanceFixture = [
  RuntimeArtifactEntryV2<'runtime-governance/v2/login-purpose-record.json'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/login-purpose-acceptance.json'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/login-owner-act'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/worker-purpose-record.json'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/worker-purpose-acceptance.json'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/worker-owner-act'>
];

function governanceArtifact<P extends string>(relativePath: P): RuntimeArtifactEntryV2<P> {
  return { relativePath, size: 1, sha256: 'c'.repeat(64) };
}

function governanceFixture(): GovernanceFixture {
  return [
    governanceArtifact('runtime-governance/v2/login-purpose-record.json'),
    governanceArtifact('runtime-governance/v2/login-purpose-acceptance.json'),
    governanceArtifact('runtime-governance/v2/login-owner-act'),
    governanceArtifact('runtime-governance/v2/worker-purpose-record.json'),
    governanceArtifact('runtime-governance/v2/worker-purpose-acceptance.json'),
    governanceArtifact('runtime-governance/v2/worker-owner-act')
  ];
}

async function completionFixture() {
  const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-complete-')));
  const appPath = path.join(root, 'Chirality.app');
  const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
  const checkpointPath = path.join(root, 'prepared.json');
  const checkpointNestedSignatures = [
    { relativePath: 'Contents/Frameworks/Electron Framework.framework', type: 'bundle' as const, identitySha256: '5'.repeat(64) },
    { relativePath: 'Contents/MacOS/Chirality', type: 'file' as const, identitySha256: '6'.repeat(64), content: { size: 40, sha256: '7'.repeat(64) } }
  ];
  const expectedOuterMainContent = { size: 42, sha256: '8'.repeat(64) };
  const currentNestedSignatures = [
    checkpointNestedSignatures[0],
    { relativePath: 'Contents/MacOS/Chirality', type: 'file' as const, identitySha256: '9'.repeat(64), content: expectedOuterMainContent }
  ];
  const governance = governanceFixture();
  const payload: RuntimePayloadManifestV2 = {
    schema: 'chirality-runtime-payload-manifest/v2', dependencyResolutionDigest: 'd'.repeat(64), roots: [], supportProfiles: [], entries: []
  };
  const inventory = {
    schema: 'chirality-runtime-artifact-inventory/v2' as const,
    payloadManifest: { relativePath: 'runtime-payload-manifest.json' as const, size: 20, sha256: 'a'.repeat(64) },
    governance
  };
  const basis: VerifiedPackagedRuntimeBasisV2 = {
    resourcesRoot,
    inventoryPath: path.join(resourcesRoot, 'runtime-artifact-inventory-v2.json'),
    payloadManifestPath: path.join(resourcesRoot, 'runtime-payload-manifest.json'),
    inventorySha256: 'b'.repeat(64), payloadDigest: 'a'.repeat(64), payload, inventory
  };
  await mkdir(resourcesRoot, { recursive: true });
  const checkpoint = {
    schema: 'chirality-signed-runtime-v2-checkpoint/v1', phase: 'payload-bound', appPath, resourcesRoot,
    identitySha1: 'A'.repeat(40), teamId: 'A1B2C3D4E5', bundleId: 'com.chirality.app',
    peerRequirement: deriveHostPeerRequirement({ bundleId: 'com.chirality.app', teamId: 'A1B2C3D4E5' }),
    dependencyDigest: '1'.repeat(64), supplierDigest: '2'.repeat(64), signedSupplierDigest: '3'.repeat(64),
    nestedSignatures: checkpointNestedSignatures, payloadSnapshotDigest: '4'.repeat(64),
    payloadManifest: { sha256: 'a'.repeat(64), size: 20 }, supportProfilesIdentity: { sha256: 'e'.repeat(64), size: 30 }
  };
  await writeFile(checkpointPath, `${JSON.stringify(checkpoint)}\n`);
  const env = {
    NODE_ENV: 'test' as const,
    [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40), [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
    [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app', [SIGNING_CHECKPOINT_FILE_ENV]: checkpointPath,
    [RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV]: '/accepted/profiles.json', [RUNTIME_V2_GOVERNANCE_ROOT_ENV]: '/accepted/governance',
    [RUNTIME_V2_INPUT_DIGEST_ENV]: 'f'.repeat(64)
  };
  return { root, appPath, resourcesRoot, checkpointPath, checkpoint, env, governance, basis, currentNestedSignatures, expectedOuterMainContent };
}

async function governedCompletionFixture() {
  const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-governed-complete-')));
  const appPath = path.join(root, 'Chirality.app');
  const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
  const checkpointPath = path.join(root, 'prepared.json');
  const lockRoot = path.join(root, 'locks');
  const lockPaths = [path.join(lockRoot, 'frontend.json'), path.join(lockRoot, 'runtime.json')];
  for (const directory of [resourcesRoot, path.join(resourcesRoot, 'instruction-root'), path.join(resourcesRoot, 'native'),
    path.join(resourcesRoot, 'runtime-cli'), path.join(resourcesRoot, 'supplier'), lockRoot]) await mkdir(directory, { recursive: true });
  await writeFile(path.join(resourcesRoot, 'app.asar'), 'application');
  await writeFile(path.join(resourcesRoot, 'instruction-root', 'instruction-bundle-manifest.json'), '{}\n');
  await writeFile(path.join(resourcesRoot, 'native', 'chirality_native_admission.node'), 'native');
  await writeFile(path.join(resourcesRoot, 'runtime-cli', 'chirality-cli.mjs'), 'export {};\n');
  await writeFile(path.join(resourcesRoot, 'runtime-cli', 'chirality-cli.mjs.map'), '{"version":3}\n');
  await writeFile(path.join(resourcesRoot, 'supplier', 'codex'), 'supplier');
  await chmod(path.join(resourcesRoot, 'supplier', 'codex'), 0o755);
  await writeFile(lockPaths[0], '{"lockfileVersion":3,"packages":{}}\n');
  await writeFile(lockPaths[1], '{"lockfileVersion":3,"packages":{}}\n');
  const governanceRoot = path.join(root, 'governance');
  await mkdir(governanceRoot);
  for (const entry of governanceFixture()) await writeFile(path.join(governanceRoot, path.basename(entry.relativePath)), `${entry.relativePath}\n`);
  const fileDigest = (value: Buffer | string) => createHash('sha256').update(value).digest('hex');
  const nativeBytes = await readFile(path.join(resourcesRoot, 'native', 'chirality_native_admission.node'));
  const supplierBytes = await readFile(path.join(resourcesRoot, 'supplier', 'codex'));
  const profileWithoutDigest = {
    schema: 'chirality-runtime-support-profile/v2', macosProductVersion: '15.6.1', macosBuildVersion: '24G90', architecture: 'arm64',
    electronVersion: '43.2.0', nodeVersion: '24.18.0', nodeModuleAbi: '148', napiVersion: '10',
    osMeasurement: { executablePath: '/usr/bin/sw_vers', executableSha256: '1'.repeat(64), executableSize: 1234 },
    sandboxExec: { path: '/usr/bin/sandbox-exec', sha256: '2'.repeat(64), size: 2345 },
    nativeAdmission: { contract: 'chirality-native-admission/v1', sha256: fileDigest(nativeBytes), size: nativeBytes.length, napiVersion: RUNTIME_NATIVE_ADMISSION_NAPI_VERSION_V2 },
    supplier: { version: '0.99.0-test-only', sha256: fileDigest(supplierBytes), size: supplierBytes.length, appServerProtocolDigest: '3'.repeat(64), authorityContract: 'chirality.local-admission-authority/1.0', identityContract: 'chirality-supplier-account-identity/1' },
    compiler: { outerPolicySchema: 'chirality-codex-outer-policy/v2', nativePolicyIdentityVersion: 10, sourceDigest: '4'.repeat(64), parameterSchemaDigest: runtimePolicyParameterSchemaDigestV2() },
    immutableSystemRoots: ['/System', '/usr'], kernelHelperContractDigest: '5'.repeat(64)
  } as const;
  const profile = { ...profileWithoutDigest, profileDigest: fileDigest(`${JSON.stringify(profileWithoutDigest)}\n`) };
  const supportProfilesPath = path.join(root, 'support-profiles.json');
  await writeFile(supportProfilesPath, JSON.stringify([profile]));
  const release = await inspectRuntimeV2ReleaseInputs({ supportProfilesPath, governanceRoot });
  const finalized = await finalizeRuntimeResourcesV2({
    resourcesRoot,
    expectedDependencyResolutionDigest: await computeDependencyResolutionDigest({ lockPaths }),
    expectedSupplierStagingDigest: await computeSupplierTreeDigest(path.join(resourcesRoot, 'supplier')),
    supportProfilesPath,
    governanceRoot,
    expectedInputDigest: release.digest,
    lockPaths
  });
  const supportBytes = await readFile(supportProfilesPath);
  const checkpointNestedSignatures = [
    { relativePath: 'Contents/Frameworks/Electron Framework.framework', type: 'bundle' as const, identitySha256: '5'.repeat(64) },
    { relativePath: 'Contents/MacOS/Chirality', type: 'file' as const, identitySha256: '6'.repeat(64), content: { size: 40, sha256: '7'.repeat(64) } }
  ];
  const expectedOuterMainContent = { size: 42, sha256: '8'.repeat(64) };
  const currentNestedSignatures = [checkpointNestedSignatures[0], {
    relativePath: 'Contents/MacOS/Chirality', type: 'file' as const, identitySha256: '9'.repeat(64), content: expectedOuterMainContent
  }];
  const checkpoint = {
    schema: 'chirality-signed-runtime-v2-checkpoint/v1', phase: 'payload-bound', appPath, resourcesRoot,
    identitySha1: 'A'.repeat(40), teamId: 'A1B2C3D4E5', bundleId: 'com.chirality.app',
    peerRequirement: deriveHostPeerRequirement({ bundleId: 'com.chirality.app', teamId: 'A1B2C3D4E5' }),
    dependencyDigest: '1'.repeat(64), supplierDigest: '2'.repeat(64), signedSupplierDigest: '3'.repeat(64),
    nestedSignatures: checkpointNestedSignatures, payloadSnapshotDigest: '4'.repeat(64),
    payloadManifest: { sha256: finalized.verified.payloadDigest, size: finalized.verified.inventory.payloadManifest.size },
    supportProfilesIdentity: { sha256: fileDigest(supportBytes), size: supportBytes.length }
  };
  await writeFile(checkpointPath, `${JSON.stringify(checkpoint)}\n`);
  const env = {
    NODE_ENV: 'test' as const,
    [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40), [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
    [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app', [SIGNING_CHECKPOINT_FILE_ENV]: checkpointPath,
    [RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV]: supportProfilesPath, [RUNTIME_V2_GOVERNANCE_ROOT_ENV]: governanceRoot,
    [RUNTIME_V2_INPUT_DIGEST_ENV]: release.digest
  };
  return { root, appPath, resourcesRoot, checkpointPath, env, finalized, release, currentNestedSignatures, expectedOuterMainContent };
}

describe('signed Runtime v2 assembly', () => {
  it('writes the Runtime-owned predicate before awaited nested signing and records only a prepared checkpoint', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-v2-')));
    const appPath = path.join(root, 'Chirality.app');
    const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
    const checkpointPath = path.join(root, 'evidence', 'prepared.json');
    await mkdir(resourcesRoot, { recursive: true });
    await mkdir(path.join(resourcesRoot, 'supplier'));
    await writeFile(path.join(resourcesRoot, 'supplier', 'codex'), 'signed supplier');
    await chmod(path.join(resourcesRoot, 'supplier', 'codex'), 0o755);
    await writeFile(path.join(appPath, 'Contents', 'Info.plist'), '<plist/>');
    const env = {
      NODE_ENV: 'test' as const,
      [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40),
      [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
      [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app',
      [SIGNING_CHECKPOINT_FILE_ENV]: checkpointPath,
      [DEPENDENCY_DIGEST_ENV]: '1'.repeat(64),
      [SUPPLIER_DIGEST_ENV]: '2'.repeat(64)
    };
    const sign = vi.fn(async () => {
      const predicate = JSON.parse(await readFile(path.join(resourcesRoot, 'runtime-contracts', 'host-account-signing-predicate.json'), 'utf8'));
      expect(predicate).toEqual({
        schema: 'chirality.host-account-signing-predicate/v1',
        serviceName: 'com.chirality.app.runtime.account-host',
        bundleId: 'com.chirality.app',
        teamId: 'A1B2C3D4E5',
        peerRequirement: deriveHostPeerRequirement({ bundleId: 'com.chirality.app', teamId: 'A1B2C3D4E5' })
      });
      expect(predicate.peerRequirement).not.toContain('designated =>');
      expect(await readFile(checkpointPath).then(() => true, () => false)).toBe(false);
    });
    try {
      await prepareSignedRuntimeV2({
        app: appPath,
        identity: 'A'.repeat(40),
        optionsForFile: (filePath: string) => ({ entitlements: filePath === appPath ? '/main.plist' : '/inherit.plist' })
      }, {
        env,
        sign: sign as never,
        inspectBundleId: async () => 'com.chirality.app',
        inspectNestedSignatures: async () => [{ relativePath: 'Contents/Frameworks/Electron Framework.framework', type: 'bundle', identitySha256: '3'.repeat(64) }]
      });
      expect(sign).toHaveBeenCalledTimes(1);
      const checkpoint = JSON.parse(await readFile(checkpointPath, 'utf8'));
      expect(checkpoint).toMatchObject({
        schema: 'chirality-signed-runtime-v2-checkpoint/v1',
        phase: 'nested-signed',
        appPath,
        resourcesRoot,
        identitySha1: 'A'.repeat(40),
        nestedSignatures: [{ relativePath: 'Contents/Frameworks/Electron Framework.framework', type: 'bundle', identitySha256: '3'.repeat(64) }]
      });
      expect(await readFile(path.join(resourcesRoot, 'runtime-payload-manifest.json')).then(() => true, () => false)).toBe(false);
      expect(await readFile(path.join(resourcesRoot, 'runtime-artifact-inventory-v2.json')).then(() => true, () => false)).toBe(false);
    } finally {
      await rm(root, { recursive: true, force: true });
    }
  });

  it('reads a valid nested checkpoint above 64 KiB through the payload resume path', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-large-resume-')));
    const appPath = path.join(root, 'Chirality.app');
    const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
    const checkpointPath = path.join(root, 'prepared.json');
    const nestedSignatures = Array.from({ length: 729 }, (_, index) => ({
      relativePath: `Contents/Frameworks/F${String(index).padStart(4, '0')}`,
      type: 'file',
      identitySha256: '3'.repeat(64),
      content: { size: index, sha256: '4'.repeat(64) }
    }));
    await mkdir(resourcesRoot, { recursive: true });
    await writeFile(checkpointPath, `${JSON.stringify({
      schema: 'chirality-signed-runtime-v2-checkpoint/v1', phase: 'nested-signed', appPath, resourcesRoot,
      identitySha1: 'A'.repeat(40), teamId: 'A1B2C3D4E5', bundleId: 'com.chirality.app',
      peerRequirement: deriveHostPeerRequirement({ bundleId: 'com.chirality.app', teamId: 'A1B2C3D4E5' }),
      dependencyDigest: '1'.repeat(64), supplierDigest: '2'.repeat(64), signedSupplierDigest: '3'.repeat(64),
      nestedSignatures, payloadSnapshotDigest: '4'.repeat(64)
    }, null, 2)}\n`);
    try {
      const checkpointSize = (await lstat(checkpointPath)).size;
      expect(checkpointSize).toBeGreaterThan(65_536);
      expect(checkpointSize).toBeLessThanOrEqual(1_048_576);
      await expect(bindSignedRuntimeV2Payload({ env: {
        NODE_ENV: 'test' as const,
        [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40), [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
        [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app', [SIGNING_CHECKPOINT_FILE_ENV]: checkpointPath
      } })).rejects.toThrow('Prepared signed payload bytes changed before profile binding');
      await expect(readFile(path.join(resourcesRoot, 'runtime-payload-manifest.json'))).rejects.toMatchObject({ code: 'ENOENT' });
    } finally { await rm(root, { recursive: true, force: true }); }
  });

  it('caps a checkpoint read when the held regular file grows after its initial stat', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-growing-read-')));
    const appPath = path.join(root, 'Chirality.app');
    const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
    const checkpointPath = path.join(root, 'prepared.json');
    await mkdir(resourcesRoot, { recursive: true });
    await writeFile(checkpointPath, `${JSON.stringify({
      schema: 'chirality-signed-runtime-v2-checkpoint/v1', phase: 'nested-signed', appPath, resourcesRoot,
      identitySha1: 'A'.repeat(40), teamId: 'A1B2C3D4E5', bundleId: 'com.chirality.app',
      peerRequirement: deriveHostPeerRequirement({ bundleId: 'com.chirality.app', teamId: 'A1B2C3D4E5' }),
      dependencyDigest: '1'.repeat(64), supplierDigest: '2'.repeat(64), signedSupplierDigest: '3'.repeat(64),
      nestedSignatures: [], payloadSnapshotDigest: '4'.repeat(64)
    })}\n`);
    const prototypeHandle = await open(checkpointPath, 'r');
    const fileHandlePrototype = Object.getPrototypeOf(prototypeHandle);
    await prototypeHandle.close();
    const originalRead = fileHandlePrototype.read;
    let grew = false;
    const readSpy = vi.spyOn(fileHandlePrototype, 'read').mockImplementation(async function (...args) {
      if (!grew) {
        grew = true;
        await appendFile(checkpointPath, Buffer.alloc(1_048_576));
      }
      return Reflect.apply(originalRead, this, args);
    });
    try {
      await expect(bindSignedRuntimeV2Payload({ env: {
        NODE_ENV: 'test' as const,
        [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40), [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
        [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app', [SIGNING_CHECKPOINT_FILE_ENV]: checkpointPath
      } })).rejects.toThrow('Signing checkpoint is not a bounded regular file');
      expect(grew).toBe(true);
      expect(readSpy).toHaveBeenCalledTimes(1);
      await expect(readFile(path.join(resourcesRoot, 'runtime-payload-manifest.json'))).rejects.toMatchObject({ code: 'ENOENT' });
    } finally {
      readSpy.mockRestore();
      await rm(root, { recursive: true, force: true });
    }
  });

  it('rejects an overbound prepared checkpoint before creating its output directory', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-overbound-')));
    const appPath = path.join(root, 'Chirality.app');
    const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
    const checkpointPath = path.join(root, 'evidence', 'prepared.json');
    await mkdir(path.join(resourcesRoot, 'supplier'), { recursive: true });
    await writeFile(path.join(resourcesRoot, 'supplier', 'codex'), 'signed supplier');
    await chmod(path.join(resourcesRoot, 'supplier', 'codex'), 0o755);
    await writeFile(path.join(appPath, 'Contents', 'Info.plist'), '<plist/>');
    try {
      await expect(prepareSignedRuntimeV2({
        app: appPath,
        identity: 'A'.repeat(40),
        optionsForFile: (filePath: string) => ({ entitlements: filePath === appPath ? '/main.plist' : '/inherit.plist' })
      }, {
        env: {
          NODE_ENV: 'test' as const,
          [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40), [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
          [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app', [SIGNING_CHECKPOINT_FILE_ENV]: checkpointPath,
          [DEPENDENCY_DIGEST_ENV]: '1'.repeat(64), [SUPPLIER_DIGEST_ENV]: '2'.repeat(64)
        },
        sign: async () => undefined,
        inspectBundleId: async () => 'com.chirality.app',
        inspectNestedSignatures: async () => Array.from({ length: 10_000 }, (_, index) => ({
          relativePath: `Contents/Frameworks/F${String(index).padStart(5, '0')}`,
          type: 'file' as const,
          identitySha256: '3'.repeat(64),
          content: { size: index, sha256: '4'.repeat(64) }
        }))
      })).rejects.toThrow('Signing checkpoint exceeds the bounded size limit');
      await expect(lstat(path.dirname(checkpointPath))).rejects.toMatchObject({ code: 'ENOENT' });
      await expect(readFile(checkpointPath)).rejects.toMatchObject({ code: 'ENOENT' });
    } finally { await rm(root, { recursive: true, force: true }); }
  });

  it('makes the resumed signing pass outer-only and prevents late provisioning or entitlement mutation', () => {
    const appPath = '/stage/Chirality.app';
    const options = createRuntimeV2SignOptions({
      app: appPath,
      identity: 'A'.repeat(40),
      ignore: [() => false],
      preEmbedProvisioningProfile: true,
      preAutoEntitlements: true,
      optionsForFile: () => ({ timestamp: true })
    }, {
      appPath,
      peerRequirement: 'requirement',
      outerOnly: true,
      entitlements: '/main.plist',
      inheritEntitlements: '/inherit.plist'
    });
    expect(options.preEmbedProvisioningProfile).toBe(false);
    expect(options.preAutoEntitlements).toBe(false);
    expect(options.ignore('/stage/Chirality.app/Contents/MacOS/Chirality')).toBe(true);
    expect(options.ignore(appPath)).toBe(false);
    expect(options.optionsForFile(appPath)).toMatchObject({
      entitlements: '/main.plist',
      hardenedRuntime: true,
      requirements: '=designated => requirement',
      timestamp: true
    });
  });

  it('preserves the scalar outer-only filter through the installed signer option normalization', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-outer-filter-')));
    const appPath = path.join(root, 'Chirality.app');
    const mainPath = path.join(appPath, 'Contents', 'MacOS', 'Chirality');
    const binRoot = path.join(root, 'bin');
    const logPath = path.join(root, 'codesign.jsonl');
    const previousPath = process.env.PATH;
    const previousLog = process.env.CHIRALITY_TEST_CODESIGN_LOG;
    await mkdir(path.dirname(mainPath), { recursive: true });
    await mkdir(binRoot);
    const mainBytes = Buffer.alloc(64);
    mainBytes.writeUInt32LE(0xfeedfacf, 0);
    await writeFile(mainPath, mainBytes);
    await chmod(mainPath, 0o755);
    await writeFile(path.join(appPath, 'Contents', 'Info.plist'), [
      '<?xml version="1.0" encoding="UTF-8"?>',
      '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">',
      '<plist version="1.0"><dict><key>CFBundleExecutable</key><string>Chirality</string><key>CFBundleIdentifier</key><string>com.chirality.app</string></dict></plist>'
    ].join('\n'));
    const fakeCodesign = path.join(binRoot, 'codesign');
    await writeFile(fakeCodesign, [
      '#!/bin/sh',
      `printf '%s\\n' "$*" >> "${logPath}"`,
      'exit 0'
    ].join('\n'));
    await chmod(fakeCodesign, 0o755);
    process.env.PATH = `${binRoot}:/usr/bin:/bin`;
    process.env.CHIRALITY_TEST_CODESIGN_LOG = logPath;
    try {
      expect(await walkAsync(path.join(appPath, 'Contents'))).toContain(mainPath);
      const options = createRuntimeV2SignOptions({
        app: appPath,
        platform: 'darwin',
        type: 'distribution',
        identity: 'A'.repeat(40),
        identityValidation: false
      }, {
        appPath,
        peerRequirement: deriveHostPeerRequirement({ bundleId: 'com.chirality.app', teamId: 'A1B2C3D4E5' }),
        outerOnly: true,
        entitlements: '/main.plist',
        inheritEntitlements: '/inherit.plist'
      });
      await signAsync(options);
      const calls = (await readFile(logPath, 'utf8')).trim().split('\n');
      const signingCalls = calls.filter((call) => call.includes('--sign'));
      expect(signingCalls).toHaveLength(1);
      expect(signingCalls[0]).toContain(appPath);
      expect(signingCalls[0]).not.toContain(mainPath);
    } finally {
      if (previousPath === undefined) delete process.env.PATH; else process.env.PATH = previousPath;
      if (previousLog === undefined) delete process.env.CHIRALITY_TEST_CODESIGN_LOG; else process.env.CHIRALITY_TEST_CODESIGN_LOG = previousLog;
      await rm(root, { recursive: true, force: true });
    }
  });

  it('rejects a checkpoint that combines an app with a different Resources tree before any payload write', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-paths-')));
    const appPath = path.join(root, 'A.app');
    const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
    const otherResources = path.join(root, 'B.app', 'Contents', 'Resources');
    const checkpointPath = path.join(root, 'prepared.json');
    await mkdir(resourcesRoot, { recursive: true });
    await mkdir(otherResources, { recursive: true });
    await writeFile(checkpointPath, `${JSON.stringify({
      schema: 'chirality-signed-runtime-v2-checkpoint/v1', phase: 'nested-signed', appPath, resourcesRoot: otherResources,
      identitySha1: 'A'.repeat(40), teamId: 'A1B2C3D4E5', bundleId: 'com.chirality.app',
      peerRequirement: deriveHostPeerRequirement({ bundleId: 'com.chirality.app', teamId: 'A1B2C3D4E5' }),
      dependencyDigest: '1'.repeat(64), supplierDigest: '2'.repeat(64), signedSupplierDigest: '3'.repeat(64),
      nestedSignatures: [], payloadSnapshotDigest: '4'.repeat(64)
    })}\n`);
    try {
      await expect(bindSignedRuntimeV2Payload({ env: {
        NODE_ENV: 'test' as const,
        [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40), [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
        [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app', [SIGNING_CHECKPOINT_FILE_ENV]: checkpointPath
      } })).rejects.toThrow('do not match one canonical bundle');
      await expect(readFile(path.join(otherResources, 'runtime-payload-manifest.json'))).rejects.toMatchObject({ code: 'ENOENT' });
    } finally { await rm(root, { recursive: true, force: true }); }
  });

  it('rejects nested file drift after outer signing and does not write a verified result', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-race-')));
    const appPath = path.join(root, 'Chirality.app');
    const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
    const checkpointPath = path.join(root, 'prepared.json');
    await mkdir(resourcesRoot, { recursive: true });
    const nestedA = [
      { relativePath: 'Contents/Frameworks/Electron Framework.framework/Versions/A/Electron Framework', type: 'file', identitySha256: '5'.repeat(64), content: { size: 10, sha256: '6'.repeat(64) } },
      { relativePath: 'Contents/MacOS/Chirality', type: 'file', identitySha256: '7'.repeat(64), content: { size: 10, sha256: '8'.repeat(64) } }
    ];
    const nestedB = [{ ...nestedA[0], content: { size: 10, sha256: '9'.repeat(64) } }, nestedA[1]];
    await writeFile(checkpointPath, `${JSON.stringify({
      schema: 'chirality-signed-runtime-v2-checkpoint/v1', phase: 'payload-bound', appPath, resourcesRoot,
      identitySha1: 'A'.repeat(40), teamId: 'A1B2C3D4E5', bundleId: 'com.chirality.app',
      peerRequirement: deriveHostPeerRequirement({ bundleId: 'com.chirality.app', teamId: 'A1B2C3D4E5' }),
      dependencyDigest: '1'.repeat(64), supplierDigest: '2'.repeat(64), signedSupplierDigest: '3'.repeat(64),
      nestedSignatures: nestedA, payloadSnapshotDigest: '4'.repeat(64),
      payloadManifest: { sha256: '8'.repeat(64), size: 20 }, supportProfilesIdentity: { sha256: '9'.repeat(64), size: 30 }
    })}\n`);
    const env = {
      NODE_ENV: 'test' as const,
      [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40), [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
      [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app', [SIGNING_CHECKPOINT_FILE_ENV]: checkpointPath,
      [RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV]: '/accepted/profiles.json', [RUNTIME_V2_GOVERNANCE_ROOT_ENV]: '/accepted/governance',
      [RUNTIME_V2_INPUT_DIGEST_ENV]: 'a'.repeat(64)
    };
    let inspection = 0;
    try {
      await expect(sealSignedRuntimeV2({
        env,
        sign: async () => undefined,
        verifyFinal: async () => undefined,
        inspectNestedSignatures: async () => inspection++ === 0 ? nestedA : nestedB,
        verifyPayload: async () => ({
          manifestPath: path.join(resourcesRoot, 'runtime-payload-manifest.json'),
          manifest: { schema: 'chirality-runtime-payload-manifest/v2' as const, dependencyResolutionDigest: 'b'.repeat(64), roots: [], supportProfiles: [], entries: [] },
          sha256: '8'.repeat(64),
          size: 20
        }),
        inspectReleaseInputs: async () => ({ digest: 'a'.repeat(64), supportProfiles: [], governance: [] }),
        inspectSupportProfiles: async () => ({ sha256: '9'.repeat(64), size: 30, supportProfiles: [] }),
        stageGovernance: async () => undefined,
        writeInventory: async () => {
          const inventoryPath = path.join(resourcesRoot, 'runtime-artifact-inventory-v2.json');
          const payloadManifestPath = path.join(resourcesRoot, 'runtime-payload-manifest.json');
          const payload: RuntimePayloadManifestV2 = { schema: 'chirality-runtime-payload-manifest/v2', dependencyResolutionDigest: 'd'.repeat(64), roots: [], supportProfiles: [], entries: [] };
          const governance = [
            governanceArtifact('runtime-governance/v2/login-purpose-record.json'), governanceArtifact('runtime-governance/v2/login-purpose-acceptance.json'), governanceArtifact('runtime-governance/v2/login-owner-act'),
            governanceArtifact('runtime-governance/v2/worker-purpose-record.json'), governanceArtifact('runtime-governance/v2/worker-purpose-acceptance.json'), governanceArtifact('runtime-governance/v2/worker-owner-act')
          ] satisfies GovernanceFixture;
          const inventory = {
            schema: 'chirality-runtime-artifact-inventory/v2' as const,
            payloadManifest: { relativePath: 'runtime-payload-manifest.json' as const, size: 20, sha256: '8'.repeat(64) },
            governance
          };
          const verified: VerifiedPackagedRuntimeBasisV2 = { resourcesRoot, inventoryPath, payloadManifestPath, inventorySha256: 'b'.repeat(64), payloadDigest: 'e'.repeat(64), payload, inventory };
          return { inventoryPath, inventory, verified };
        }
      })).rejects.toThrow('changed during outer verification');
      await expect(readFile(`${checkpointPath}.sealed.json`)).rejects.toMatchObject({ code: 'ENOENT' });
    } finally { await rm(root, { recursive: true, force: true }); }
  });

  it('completes verification of an already outer-signed candidate without signing or staging again', async () => {
    const fixture = await completionFixture();
    const checkpointBefore = await readFile(fixture.checkpointPath);
    const inspectNestedSignatures = vi.fn(async () => fixture.currentNestedSignatures);
    const verifyFinal = vi.fn(async () => fixture.basis);
    try {
      const result = await completeSignedRuntimeV2Verification({
        env: fixture.env,
        expectedAppPath: fixture.appPath,
        expectedOuterMainContent: fixture.expectedOuterMainContent,
        inspectNestedSignatures,
        inspectReleaseInputs: async () => ({
          digest: 'f'.repeat(64), supportProfiles: [], governance: fixture.governance.map((entry) => ({ ...entry, bytes: Buffer.from('x') }))
        }),
        inspectSupportProfiles: async () => ({ sha256: 'e'.repeat(64), size: 30, supportProfiles: [] }),
        verifyFinal
      });
      expect(result).toMatchObject({ appPath: fixture.appPath, inventory: fixture.basis.inventory });
      expect(inspectNestedSignatures).toHaveBeenCalledTimes(2);
      expect(verifyFinal).toHaveBeenCalledTimes(1);
      expect(await readFile(fixture.checkpointPath)).toEqual(checkpointBefore);
      expect(JSON.parse(await readFile(result.artifactPath, 'utf8'))).toMatchObject({
        schema: 'chirality-signed-runtime-v2-result/v1', inventorySha256: 'b'.repeat(64), verified: true
      });
    } finally { await rm(fixture.root, { recursive: true, force: true }); }
  });

  it('completes against a real post-inventory Resources basis', async () => {
    const fixture = await governedCompletionFixture();
    try {
      const result = await completeSignedRuntimeV2Verification({
        env: fixture.env,
        expectedAppPath: fixture.appPath,
        expectedOuterMainContent: fixture.expectedOuterMainContent,
        inspectNestedSignatures: async () => fixture.currentNestedSignatures,
        verifyFinal: async ({ resourcesRoot }) => verifyPackagedRuntimeBasisV2({ resourcesRoot })
      });
      expect(result.inventory).toEqual(fixture.finalized.verified.inventory);
      expect(JSON.parse(await readFile(result.artifactPath, 'utf8'))).toMatchObject({
        inventorySha256: fixture.finalized.verified.inventorySha256,
        verified: true
      });
    } finally { await rm(fixture.root, { recursive: true, force: true }); }
  });

  it.each([
    ['payload manifest', 'runtime-payload-manifest.json'],
    ['governance member', 'runtime-governance/v2/login-purpose-record.json']
  ])('rejects a changed %s in a real post-inventory Resources basis', async (_label, relativePath) => {
    const fixture = await governedCompletionFixture();
    await writeFile(path.join(fixture.resourcesRoot, relativePath), 'changed\n');
    try {
      await expect(completeSignedRuntimeV2Verification({
        env: fixture.env,
        expectedAppPath: fixture.appPath,
        expectedOuterMainContent: fixture.expectedOuterMainContent,
        inspectNestedSignatures: async () => fixture.currentNestedSignatures,
        verifyFinal: async ({ resourcesRoot }) => verifyPackagedRuntimeBasisV2({ resourcesRoot })
      })).rejects.toMatchObject({ code: 'ENGINE_UNAVAILABLE' });
      await expect(readFile(`${fixture.checkpointPath}.sealed.json`)).rejects.toMatchObject({ code: 'ENOENT' });
    } finally { await rm(fixture.root, { recursive: true, force: true }); }
  });

  it('rejects a wrong checkpoint predicate without writing a completion result', async () => {
    const fixture = await completionFixture();
    await writeFile(fixture.checkpointPath, `${JSON.stringify({ ...fixture.checkpoint, peerRequirement: 'anchor apple' })}\n`);
    try {
      await expect(completeSignedRuntimeV2Verification({
        env: fixture.env,
        expectedAppPath: fixture.appPath,
        expectedOuterMainContent: fixture.expectedOuterMainContent
      })).rejects.toThrow('Signing inputs do not match');
      await expect(readFile(`${fixture.checkpointPath}.sealed.json`)).rejects.toMatchObject({ code: 'ENOENT' });
    } finally { await rm(fixture.root, { recursive: true, force: true }); }
  });

  it('rejects changed accepted governance without writing a completion result', async () => {
    const fixture = await completionFixture();
    const changedGovernance = fixture.governance.map((entry, index) => index === 0 ? { ...entry, sha256: 'd'.repeat(64) } : entry) as GovernanceFixture;
    try {
      await expect(completeSignedRuntimeV2Verification({
        env: fixture.env,
        expectedAppPath: fixture.appPath,
        expectedOuterMainContent: fixture.expectedOuterMainContent,
        inspectNestedSignatures: async () => fixture.currentNestedSignatures,
        inspectReleaseInputs: async () => ({ digest: 'f'.repeat(64), supportProfiles: [], governance: changedGovernance.map((entry) => ({ ...entry, bytes: Buffer.from('x') })) }),
        inspectSupportProfiles: async () => ({ sha256: 'e'.repeat(64), size: 30, supportProfiles: [] }),
        verifyFinal: async () => fixture.basis
      })).rejects.toThrow('governance inventory does not match');
      await expect(readFile(`${fixture.checkpointPath}.sealed.json`)).rejects.toMatchObject({ code: 'ENOENT' });
    } finally { await rm(fixture.root, { recursive: true, force: true }); }
  });

  it('rejects true nested-code drift without writing a completion result', async () => {
    const fixture = await completionFixture();
    const verifyFinal = vi.fn(async () => fixture.basis);
    const changedNested = [{ ...fixture.currentNestedSignatures[0], identitySha256: '0'.repeat(64) }, fixture.currentNestedSignatures[1]];
    try {
      await expect(completeSignedRuntimeV2Verification({
        env: fixture.env,
        expectedAppPath: fixture.appPath,
        expectedOuterMainContent: fixture.expectedOuterMainContent,
        inspectNestedSignatures: async () => changedNested
      })).rejects.toThrow('Nested signed code changed during outer verification');
      expect(verifyFinal).not.toHaveBeenCalled();
      await expect(readFile(`${fixture.checkpointPath}.sealed.json`)).rejects.toMatchObject({ code: 'ENOENT' });
    } finally { await rm(fixture.root, { recursive: true, force: true }); }
  });

  it('rejects a different selected packaging candidate before sealing work begins', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-sign-candidate-')));
    const appPath = path.join(root, 'selected', 'Chirality.app');
    const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
    const checkpointPath = path.join(root, 'prepared.json');
    await mkdir(resourcesRoot, { recursive: true });
    await writeFile(checkpointPath, `${JSON.stringify({
      schema: 'chirality-signed-runtime-v2-checkpoint/v1', phase: 'payload-bound', appPath, resourcesRoot,
      identitySha1: 'A'.repeat(40), teamId: 'A1B2C3D4E5', bundleId: 'com.chirality.app',
      peerRequirement: deriveHostPeerRequirement({ bundleId: 'com.chirality.app', teamId: 'A1B2C3D4E5' }),
      dependencyDigest: '1'.repeat(64), supplierDigest: '2'.repeat(64), signedSupplierDigest: '3'.repeat(64),
      nestedSignatures: [], payloadSnapshotDigest: '4'.repeat(64),
      payloadManifest: { sha256: '8'.repeat(64), size: 20 }, supportProfilesIdentity: { sha256: '9'.repeat(64), size: 30 }
    })}\n`);
    const verifyPayload = vi.fn();
    const inspectNestedSignatures = vi.fn();
    const inspectReleaseInputs = vi.fn();
    const inspectSupportProfiles = vi.fn();
    const stageGovernance = vi.fn();
    const writeInventory = vi.fn();
    const sign = vi.fn();
    const verifyFinal = vi.fn();
    try {
      await expect(sealSignedRuntimeV2({
        env: {
          NODE_ENV: 'test' as const,
          [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40), [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
          [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app', [SIGNING_CHECKPOINT_FILE_ENV]: checkpointPath
        },
        expectedAppPath: path.join(root, 'other', 'Chirality.app'),
        verifyPayload,
        inspectNestedSignatures,
        inspectReleaseInputs,
        inspectSupportProfiles,
        stageGovernance,
        writeInventory,
        sign,
        verifyFinal
      })).rejects.toThrow('does not match the selected Electron packaging candidate');
      expect(verifyPayload).not.toHaveBeenCalled();
      expect(inspectNestedSignatures).not.toHaveBeenCalled();
      expect(inspectReleaseInputs).not.toHaveBeenCalled();
      expect(inspectSupportProfiles).not.toHaveBeenCalled();
      expect(stageGovernance).not.toHaveBeenCalled();
      expect(writeInventory).not.toHaveBeenCalled();
      expect(sign).not.toHaveBeenCalled();
      expect(verifyFinal).not.toHaveBeenCalled();
    } finally { await rm(root, { recursive: true, force: true }); }
  });
});
