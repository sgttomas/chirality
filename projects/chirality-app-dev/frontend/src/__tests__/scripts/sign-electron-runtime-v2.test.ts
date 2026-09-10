import { chmod, mkdtemp, mkdir, readFile, realpath, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { describe, expect, it, vi } from 'vitest';
import type { RuntimeArtifactEntryV2, RuntimePayloadManifestV2, VerifiedPackagedRuntimeBasisV2 } from '@chirality/runtime-core/runtime-conformance-v2';

import {
  SIGNING_BUNDLE_ID_ENV,
  SIGNING_CHECKPOINT_FILE_ENV,
  SIGNING_IDENTITY_SHA1_ENV,
  SIGNING_TEAM_ID_ENV,
  bindSignedRuntimeV2Payload,
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
  SUPPLIER_DIGEST_ENV
} from '../../../scripts/finalize-electron-resources.mjs';

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
    expect(options.ignore[0]('/stage/Chirality.app/Contents/MacOS/Chirality')).toBe(true);
    expect(options.ignore[0](appPath)).toBe(false);
    expect(options.optionsForFile(appPath)).toMatchObject({
      entitlements: '/main.plist',
      hardenedRuntime: true,
      requirements: '=designated => requirement',
      timestamp: true
    });
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
    const nestedA = [{ relativePath: 'Contents/MacOS/Chirality', type: 'file', identitySha256: '5'.repeat(64), content: { size: 10, sha256: '6'.repeat(64) } }];
    const nestedB = [{ ...nestedA[0], content: { size: 10, sha256: '7'.repeat(64) } }];
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
      })).rejects.toThrow('changed during outer sealing');
      await expect(readFile(`${checkpointPath}.sealed.json`)).rejects.toMatchObject({ code: 'ENOENT' });
    } finally { await rm(root, { recursive: true, force: true }); }
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
