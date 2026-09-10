import { createHash } from 'node:crypto';
import { chmod, mkdtemp, mkdir, readFile, realpath, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { describe, expect, it } from 'vitest';

import {
  computeDependencyResolutionDigest,
  computeSupplierTreeDigest,
  finalizeRuntimeResourcesV2,
  inspectRuntimeV2ReleaseInputs,
  stageRuntimeV2Governance,
  verifyPreparedRuntimePayloadV2,
  writeRuntimeArtifactInventoryV2,
  writeRuntimePayloadManifestV2,
  writeRuntimeArtifactInventory
} from '../../../scripts/finalize-electron-resources.mjs';
import { runtimeConformanceArtifactInventory } from '../../../../../chirality-runtime/packages/core/src/runtime-conformance.js';
import {
  RUNTIME_NATIVE_ADMISSION_NAPI_VERSION_V2,
  runtimePolicyParameterSchemaDigestV2,
  runtimeStageCPolicyParameterSchemaDigest,
  verifyPackagedRuntimeBasisV2
} from '@chirality/runtime-core/runtime-conformance-v2';

const GOVERNANCE_FILES = [
  'login-purpose-record.json',
  'login-purpose-acceptance.json',
  'login-owner-act',
  'worker-purpose-record.json',
  'worker-purpose-acceptance.json',
  'worker-owner-act'
];
const digest = (value: Buffer | string) => createHash('sha256').update(value).digest('hex');

async function fixture() {
  const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-runtime-inventory-')));
  const resourcesRoot = path.join(root, 'Chirality.app', 'Contents', 'Resources');
  const lockRoot = path.join(root, 'locks');
  const lockPaths = [path.join(lockRoot, 'frontend-package-lock.json'), path.join(lockRoot, 'runtime-package-lock.json')];
  for (const directory of [
    resourcesRoot,
    path.join(resourcesRoot, 'instruction-root'),
    path.join(resourcesRoot, 'native'),
    path.join(resourcesRoot, 'runtime-cli'),
    path.join(resourcesRoot, 'supplier', 'support'),
    path.join(resourcesRoot, 'en.lproj'),
    lockRoot
  ]) await mkdir(directory, { recursive: true });
  await writeFile(path.join(resourcesRoot, 'app.asar'), 'opaque application archive');
  await writeFile(path.join(resourcesRoot, 'instruction-root', 'instruction-bundle-manifest.json'), '{}\n');
  await writeFile(path.join(resourcesRoot, 'instruction-root', 'AGENTS.md'), '# instructions\n');
  await writeFile(path.join(resourcesRoot, 'native', 'chirality_native_admission.node'), 'native bytes');
  await writeFile(path.join(resourcesRoot, 'runtime-cli', 'chirality-cli.mjs'), 'export {};\n');
  await writeFile(path.join(resourcesRoot, 'runtime-cli', 'chirality-cli.mjs.map'), '{"version":3}\n');
  await writeFile(path.join(resourcesRoot, 'supplier', 'codex'), 'supplier bytes');
  await chmod(path.join(resourcesRoot, 'supplier', 'codex'), 0o755);
  await writeFile(path.join(resourcesRoot, 'supplier', 'support', 'model.json'), '{}\n');
  await writeFile(path.join(resourcesRoot, 'Chirality.icns'), 'icon');
  await writeFile(lockPaths[0], '{"lockfileVersion":3,"packages":{}}\n');
  await writeFile(lockPaths[1], '{"lockfileVersion":3,"packages":{}}\n');
  return { root, resourcesRoot, lockPaths };
}

async function v2Inputs(
  input: Awaited<ReturnType<typeof fixture>>,
  localeCount = 40,
  nativePolicyIdentityVersion: 10 | 11 = 10,
  parameterSchemaDigest = nativePolicyIdentityVersion === 11
    ? runtimeStageCPolicyParameterSchemaDigest()
    : runtimePolicyParameterSchemaDigestV2()
) {
  for (let index = 0; index < localeCount; index += 1) {
    await mkdir(path.join(input.resourcesRoot, `locale-${String(index).padStart(2, '0')}.lproj`));
  }
  const governanceRoot = path.join(input.root, 'governance-input');
  await mkdir(governanceRoot);
  for (const name of GOVERNANCE_FILES) await writeFile(path.join(governanceRoot, name), `${name}\n`);
  const nativeBytes = await readFile(path.join(input.resourcesRoot, 'native', 'chirality_native_admission.node'));
  const supplierBytes = await readFile(path.join(input.resourcesRoot, 'supplier', 'codex'));
  const profileWithoutDigest = {
    schema: 'chirality-runtime-support-profile/v2',
    macosProductVersion: '15.6.1',
    macosBuildVersion: '24G90',
    architecture: 'arm64',
    electronVersion: '43.2.0',
    nodeVersion: '24.18.0',
    nodeModuleAbi: '148',
    napiVersion: '10',
    osMeasurement: { executablePath: '/usr/bin/sw_vers', executableSha256: '1'.repeat(64), executableSize: 1234 },
    sandboxExec: { path: '/usr/bin/sandbox-exec', sha256: '2'.repeat(64), size: 2345 },
    nativeAdmission: { contract: 'chirality-native-admission/v1', sha256: digest(nativeBytes), size: nativeBytes.length, napiVersion: RUNTIME_NATIVE_ADMISSION_NAPI_VERSION_V2 },
    supplier: { version: '0.99.0-test-only', sha256: digest(supplierBytes), size: supplierBytes.length, appServerProtocolDigest: '3'.repeat(64), authorityContract: 'chirality.local-admission-authority/1.0', identityContract: 'chirality-supplier-account-identity/1' },
    compiler: { outerPolicySchema: 'chirality-codex-outer-policy/v2', nativePolicyIdentityVersion, sourceDigest: '4'.repeat(64), parameterSchemaDigest },
    immutableSystemRoots: ['/System', '/usr'],
    kernelHelperContractDigest: '5'.repeat(64)
  } as const;
  const profile = { ...profileWithoutDigest, profileDigest: digest(`${JSON.stringify(profileWithoutDigest)}\n`) };
  const supportProfilesPath = path.join(input.root, 'support-profiles.json');
  await writeFile(supportProfilesPath, JSON.stringify([profile]));
  return { governanceRoot, supportProfilesPath, profile };
}

async function produceV2(input: Awaited<ReturnType<typeof fixture>>, supplied?: Awaited<ReturnType<typeof v2Inputs>>) {
  const release = supplied ?? await v2Inputs(input);
  const inspected = await inspectRuntimeV2ReleaseInputs(release);
  return finalizeRuntimeResourcesV2({
    resourcesRoot: input.resourcesRoot,
    expectedDependencyResolutionDigest: await computeDependencyResolutionDigest({ lockPaths: input.lockPaths }),
    expectedSupplierStagingDigest: await computeSupplierTreeDigest(path.join(input.resourcesRoot, 'supplier')),
    supportProfilesPath: release.supportProfilesPath,
    governanceRoot: release.governanceRoot,
    expectedInputDigest: inspected.digest,
    lockPaths: input.lockPaths
  });
}

async function produce(input: Awaited<ReturnType<typeof fixture>>) {
  const expectedDependencyResolutionDigest = await computeDependencyResolutionDigest({
    lockPaths: input.lockPaths
  });
  const expectedSupplierStagingDigest = await computeSupplierTreeDigest(
    path.join(input.resourcesRoot, 'supplier')
  );
  return writeRuntimeArtifactInventory({
    resourcesRoot: input.resourcesRoot,
    expectedDependencyResolutionDigest,
    expectedSupplierStagingDigest,
    lockPaths: input.lockPaths
  });
}

describe('Electron Runtime Resources inventory producer', () => {
  it('writes a complete deterministic manifest accepted by the real Runtime consumer', async () => {
    const input = await fixture();
    try {
      const { manifest, manifestPath } = await produce(input);
      expect(manifest.schema).toBe('chirality-runtime-artifact-inventory/v1');
      expect(manifest.sourceIdentityDigest).toMatch(/^[a-f0-9]{64}$/);
      expect(manifest.dependencyResolutionDigest).toMatch(/^[a-f0-9]{64}$/);
      expect(manifest.closureRoots).toEqual([
        'Chirality.icns',
        'app.asar',
        'instruction-root',
        'native',
        'runtime-cli',
        'supplier'
      ]);
      expect(manifest.entries.map((entry) => entry.relativePath)).toEqual([
        'Chirality.icns',
        'app.asar',
        'instruction-root/AGENTS.md',
        'instruction-root/instruction-bundle-manifest.json',
        'native/chirality_native_admission.node',
        'runtime-cli/chirality-cli.mjs',
        'runtime-cli/chirality-cli.mjs.map',
        'supplier/codex',
        'supplier/support/model.json'
      ]);
      const consumed = await runtimeConformanceArtifactInventory({
        kind: 'packaged-resources',
        resourcesRoot: input.resourcesRoot,
        manifestPath
      });
      expect(consumed.sourceFiles).toHaveLength(manifest.entries.length + 1);
      expect(consumed.dependencyResolutionDigest).toBe(manifest.dependencyResolutionDigest);
      await expect(produce(input)).rejects.toThrow('Refusing to overwrite');
      expect(JSON.parse(await readFile(manifestPath, 'utf8'))).toEqual(manifest);
    } finally {
      await rm(input.root, { recursive: true, force: true });
    }
  });

  it('rejects symlinks, missing supplier executable, and lock drift', async () => {
    const linked = await fixture();
    try {
      await symlink(path.join(linked.resourcesRoot, 'app.asar'), path.join(linked.resourcesRoot, 'linked-app'));
      await expect(produce(linked)).rejects.toThrow('symlink or noncanonical');
    } finally {
      await rm(linked.root, { recursive: true, force: true });
    }

    const missing = await fixture();
    try {
      await rm(path.join(missing.resourcesRoot, 'supplier', 'codex'));
      await expect(writeRuntimeArtifactInventory({
        resourcesRoot: missing.resourcesRoot,
        expectedDependencyResolutionDigest: await computeDependencyResolutionDigest({ lockPaths: missing.lockPaths }),
        expectedSupplierStagingDigest: 'a'.repeat(64),
        lockPaths: missing.lockPaths
      })).rejects.toThrow('missing required file: supplier/codex');
    } finally {
      await rm(missing.root, { recursive: true, force: true });
    }

    const drifted = await fixture();
    try {
      const dependencyDigest = await computeDependencyResolutionDigest({ lockPaths: drifted.lockPaths });
      await writeFile(drifted.lockPaths[0], '{"changed":true}\n');
      await expect(writeRuntimeArtifactInventory({
        resourcesRoot: drifted.resourcesRoot,
        expectedDependencyResolutionDigest: dependencyDigest,
        expectedSupplierStagingDigest: await computeSupplierTreeDigest(path.join(drifted.resourcesRoot, 'supplier')),
        lockPaths: drifted.lockPaths
      })).rejects.toThrow('changed after Electron packaging started');
    } finally {
      await rm(drifted.root, { recursive: true, force: true });
    }
  });

  it('produces complete canonical v2 payload and fixed-six inventory accepted by the shared Runtime verifier', async () => {
    const input = await fixture();
    try {
      const result = await produceV2(input);
      const verified = await verifyPackagedRuntimeBasisV2({ resourcesRoot: input.resourcesRoot });
      expect(result.verified.inventorySha256).toBe(verified.inventorySha256);
      expect(verified.payload.roots.length).toBeGreaterThan(32);
      expect(verified.payload.entries).toContainEqual({ relativePath: 'locale-00.lproj', type: 'directory' });
      expect(verified.payload.entries.some((entry) => entry.relativePath.startsWith('runtime-governance'))).toBe(false);
      expect(verified.payload.entries.some((entry) => entry.relativePath === 'runtime-artifact-inventory-v2.json')).toBe(false);
      expect(verified.inventory.governance.map((entry) => entry.relativePath)).toEqual(
        GOVERNANCE_FILES.map((name) => `runtime-governance/v2/${name}`)
      );
      expect(verified.payload.supportProfiles[0]?.supplier.version).toBe('0.99.0-test-only');
      await writeFile(path.join(input.resourcesRoot, 'unexpected-after-finalize'), 'unknown');
      await expect(verifyPackagedRuntimeBasisV2({ resourcesRoot: input.resourcesRoot })).rejects.toMatchObject({ code: 'ENGINE_UNAVAILABLE' });
    } finally {
      await rm(input.root, { recursive: true, force: true });
    }
  });

  it('uses the shared version-aware profile validator for native policy identity 11', async () => {
    const valid = await fixture();
    try {
      const release = await v2Inputs(valid, 0, 11);
      const result = await produceV2(valid, release);
      expect(result.verified.payload.supportProfiles[0]?.compiler).toMatchObject({
        nativePolicyIdentityVersion: 11,
        parameterSchemaDigest: runtimeStageCPolicyParameterSchemaDigest()
      });
    } finally {
      await rm(valid.root, { recursive: true, force: true });
    }

    const invalid = await fixture();
    try {
      const release = await v2Inputs(invalid, 0, 11, 'f'.repeat(64));
      await expect(produceV2(invalid, release)).rejects.toMatchObject({ code: 'ENGINE_UNAVAILABLE' });
      await expect(readFile(path.join(invalid.resourcesRoot, 'runtime-payload-manifest.json'))).rejects.toMatchObject({ code: 'ENOENT' });
    } finally {
      await rm(invalid.root, { recursive: true, force: true });
    }
  });

  it('rejects mismatched support, changed release inputs, and non-fixed governance without creating acceptance', async () => {
    const mismatch = await fixture();
    try {
      const release = await v2Inputs(mismatch, 0);
      const changedProfile = { ...release.profile, nativeAdmission: { ...release.profile.nativeAdmission, sha256: 'f'.repeat(64) } };
      await writeFile(release.supportProfilesPath, JSON.stringify([{ ...changedProfile, profileDigest: digest(`${JSON.stringify(changedProfile)}\n`) }]));
      await expect(produceV2(mismatch, release)).rejects.toThrow('support profile does not match');
    } finally {
      await rm(mismatch.root, { recursive: true, force: true });
    }

    const drift = await fixture();
    try {
      const release = await v2Inputs(drift, 0);
      const before = await inspectRuntimeV2ReleaseInputs(release);
      await writeFile(path.join(release.governanceRoot, 'worker-owner-act'), 'changed\n');
      await expect(finalizeRuntimeResourcesV2({
        resourcesRoot: drift.resourcesRoot,
        expectedDependencyResolutionDigest: await computeDependencyResolutionDigest({ lockPaths: drift.lockPaths }),
        expectedSupplierStagingDigest: await computeSupplierTreeDigest(path.join(drift.resourcesRoot, 'supplier')),
        supportProfilesPath: release.supportProfilesPath,
        governanceRoot: release.governanceRoot,
        expectedInputDigest: before.digest,
        lockPaths: drift.lockPaths
      })).rejects.toThrow('release inputs changed');
      await writeFile(path.join(release.governanceRoot, 'unexpected.json'), '{}\n');
      await expect(inspectRuntimeV2ReleaseInputs(release)).rejects.toThrow('exactly the fixed six files');
    } finally {
      await rm(drift.root, { recursive: true, force: true });
    }
  });

  it('rejects a staged governance substitution before writing a verified outer inventory', async () => {
    const input = await fixture();
    try {
      const release = await v2Inputs(input, 0);
      const bound = await inspectRuntimeV2ReleaseInputs(release);
      await stageRuntimeV2Governance({ resourcesRoot: input.resourcesRoot, governance: bound.governance });
      await writeRuntimePayloadManifestV2({
        resourcesRoot: input.resourcesRoot,
        expectedDependencyResolutionDigest: await computeDependencyResolutionDigest({ lockPaths: input.lockPaths }),
        expectedSupplierStagingDigest: await computeSupplierTreeDigest(path.join(input.resourcesRoot, 'supplier')),
        supportProfiles: bound.supportProfiles,
        lockPaths: input.lockPaths
      });
      await writeFile(path.join(input.resourcesRoot, 'runtime-governance', 'v2', 'worker-owner-act'), 'substituted\n');
      await expect(writeRuntimeArtifactInventoryV2({
        resourcesRoot: input.resourcesRoot,
        expectedGovernance: bound.governance.map(({ relativePath, size, sha256 }) => ({ relativePath, size, sha256 }))
      })).rejects.toThrow('governance changed after staging');
      await expect(readFile(path.join(input.resourcesRoot, 'runtime-artifact-inventory-v2.json'))).rejects.toMatchObject({ code: 'ENOENT' });
    } finally {
      await rm(input.root, { recursive: true, force: true });
    }
  });

  it('rejects payload mutation between profile binding and final governance sealing', async () => {
    const input = await fixture();
    try {
      const release = await v2Inputs(input, 0);
      const bound = await inspectRuntimeV2ReleaseInputs(release);
      await writeRuntimePayloadManifestV2({
        resourcesRoot: input.resourcesRoot,
        expectedDependencyResolutionDigest: await computeDependencyResolutionDigest({ lockPaths: input.lockPaths }),
        expectedSupplierStagingDigest: await computeSupplierTreeDigest(path.join(input.resourcesRoot, 'supplier')),
        supportProfiles: bound.supportProfiles,
        lockPaths: input.lockPaths
      });
      await writeFile(path.join(input.resourcesRoot, 'app.asar'), 'changed after accepted profile binding');
      await expect(verifyPreparedRuntimePayloadV2({ resourcesRoot: input.resourcesRoot })).rejects.toThrow(
        'payload changed after its manifest was written'
      );
    } finally {
      await rm(input.root, { recursive: true, force: true });
    }
  });

  it('rejects a stale v1 inventory discovered before selected v2 payload encoding', async () => {
    const input = await fixture();
    try {
      await writeFile(path.join(input.resourcesRoot, 'runtime-artifact-inventory.json'), '{"schema":"chirality-runtime-artifact-inventory/v1"}\n');
      await expect(produceV2(input)).rejects.toMatchObject({ code: 'ENGINE_UNAVAILABLE' });
      await expect(readFile(path.join(input.resourcesRoot, 'runtime-artifact-inventory-v2.json'))).rejects.toMatchObject({ code: 'ENOENT' });
    } finally {
      await rm(input.root, { recursive: true, force: true });
    }
  });
});
