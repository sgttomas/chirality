import { EventEmitter } from 'node:events';
import { chmod, mkdtemp, mkdir, readFile, realpath, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { describe, expect, it, vi } from 'vitest';
import type { RuntimeArtifactEntryV2, RuntimePayloadManifestV2, VerifiedPackagedRuntimeBasisV2 } from '@chirality/runtime-core/runtime-conformance-v2';

import {
  buildElectronBuilderArgs,
  ELECTRON_OUTPUT_DIRECTORY_ENV,
  expectedPackagedAppPath,
  parseArgs,
  prepareSupplierResources,
  resolveElectronOutputDirectory,
  runElectronPack
} from '../../../scripts/pack-electron-with-supply.mjs';
import {
  computeDependencyResolutionDigest,
  RUNTIME_MANIFEST_VERSION_ENV,
  RUNTIME_V2_GOVERNANCE_ROOT_ENV,
  RUNTIME_V2_INPUT_DIGEST_ENV,
  RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV
} from '../../../scripts/finalize-electron-resources.mjs';
import {
  SIGNING_BUNDLE_ID_ENV,
  SIGNING_CHECKPOINT_FILE_ENV,
  SIGNING_IDENTITY_SHA1_ENV,
  SIGNING_TEAM_ID_ENV
} from '../../../scripts/sign-electron-runtime-v2.mjs';

const GOVERNANCE_FILES = [
  'login-purpose-record.json',
  'login-purpose-acceptance.json',
  'login-owner-act',
  'worker-purpose-record.json',
  'worker-purpose-acceptance.json',
  'worker-owner-act'
];

type GovernanceFixture = [
  RuntimeArtifactEntryV2<'runtime-governance/v2/login-purpose-record.json'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/login-purpose-acceptance.json'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/login-owner-act'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/worker-purpose-record.json'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/worker-purpose-acceptance.json'>,
  RuntimeArtifactEntryV2<'runtime-governance/v2/worker-owner-act'>
];

function governanceArtifact<P extends string>(relativePath: P): RuntimeArtifactEntryV2<P> {
  return { relativePath, size: 1, sha256: 'd'.repeat(64) };
}

function sealedResult(appPath: string) {
  const resourcesRoot = path.join(appPath, 'Contents', 'Resources');
  const payload: RuntimePayloadManifestV2 = {
    schema: 'chirality-runtime-payload-manifest/v2',
    dependencyResolutionDigest: 'c'.repeat(64),
    roots: [], supportProfiles: [], entries: []
  };
  const governance = [
    governanceArtifact('runtime-governance/v2/login-purpose-record.json'), governanceArtifact('runtime-governance/v2/login-purpose-acceptance.json'), governanceArtifact('runtime-governance/v2/login-owner-act'),
    governanceArtifact('runtime-governance/v2/worker-purpose-record.json'), governanceArtifact('runtime-governance/v2/worker-purpose-acceptance.json'), governanceArtifact('runtime-governance/v2/worker-owner-act')
  ] satisfies GovernanceFixture;
  const inventoryDocument = {
    schema: 'chirality-runtime-artifact-inventory/v2' as const,
    payloadManifest: { relativePath: 'runtime-payload-manifest.json' as const, size: 1, sha256: 'a'.repeat(64) },
    governance
  };
  const verified: VerifiedPackagedRuntimeBasisV2 = {
    resourcesRoot,
    inventoryPath: path.join(resourcesRoot, 'runtime-artifact-inventory-v2.json'),
    payloadManifestPath: path.join(resourcesRoot, 'runtime-payload-manifest.json'),
    inventorySha256: 'b'.repeat(64), payloadDigest: 'c'.repeat(64), identityDigest: 'd'.repeat(64), payload, inventory: inventoryDocument
  };
  return {
    appPath,
    artifactPath: path.join(appPath, 'sealed.json'),
    inventory: { inventoryPath: verified.inventoryPath, inventory: inventoryDocument, verified }
  };
}

async function v2ReleaseInputs(root: string) {
  const supportProfilesPath = path.join(root, 'support-profiles.json');
  const governanceRoot = path.join(root, 'governance');
  await mkdir(governanceRoot);
  await writeFile(supportProfilesPath, '[{"fixture":"bound-only"}]\n');
  for (const name of GOVERNANCE_FILES) await writeFile(path.join(governanceRoot, name), `${name}\n`);
  return { supportProfilesPath, governanceRoot };
}

describe('pack-electron-with-supply', () => {
  it('passes exactly one spaces-safe electronDist argument without a shell', async () => {
    const directory = '/Users/example/Library/Caches/chirality/electron dist';
    const dependencyDigest = await computeDependencyResolutionDigest();
    const calls: Array<{ command: string; args: string[]; options: Record<string, unknown> }> = [];
    const spawnProcess = (
      command: string,
      args: string[],
      options: Record<string, unknown>
    ) => {
      calls.push({ command, args, options });
      const child = new EventEmitter();
      queueMicrotask(() => child.emit('exit', 0, null));
      return child;
    };

    await runElectronPack({
      verify: async () => directory,
      spawnProcess: spawnProcess as never,
      prepareSupplier: async () => ({
        digest: 'a'.repeat(64),
        stagingRoot: '/staged/supplier',
        cleanup: async () => undefined
      }),
      env: {
        NODE_ENV: 'test',
        PATH: '/usr/bin',
        CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST: 'a'.repeat(64),
        CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST: dependencyDigest
      }
    });

    expect(calls).toHaveLength(1);
    expect(calls[0]?.command).toBe('electron-builder');
    expect(calls[0]?.args).toEqual(
      buildElectronBuilderArgs(directory, 'dir', undefined, resolveElectronOutputDirectory())
    );
    expect(calls[0]?.args.filter((arg) => arg.startsWith('-c.electronDist='))).toEqual([
      `-c.electronDist=${directory}`
    ]);
    expect(calls[0]?.options.shell).toBe(false);
    expect(calls[0]?.options.env).toMatchObject({ CSC_IDENTITY_AUTO_DISCOVERY: 'false' });
    expect(calls[0]?.options.env).toMatchObject({
      CHIRALITY_PACKAGING_DEPENDENCY_RESOLUTION_DIGEST: dependencyDigest,
      CHIRALITY_PACKAGING_SUPPLIER_STAGING_DIGEST: 'a'.repeat(64)
    });
  });

  it('uses the verified Electron distribution for a dmg target', async () => {
    const directory = '/verified/electron dist';
    expect(buildElectronBuilderArgs(directory, 'dmg')).toEqual([
      '--mac',
      'dmg',
      '--arm64',
      '--publish',
      'never',
      `-c.electronDist=${directory}`
    ]);
    expect(parseArgs(['--target', 'dmg'])).toEqual({ target: 'dmg' });
    expect(parseArgs(['--target', 'dmg', '--runtime-manifest', 'v2'])).toEqual({ target: 'dmg', runtimeManifestVersion: 'v2' });
  });

  it('routes an explicit candidate output directory through preparation and rejects malformed values', async () => {
    const outputDirectory = '/private/tmp/chirality candidate';
    const dependencyDigest = await computeDependencyResolutionDigest();
    const calls: string[][] = [];
    const spawnProcess = vi.fn((_command: string, args: string[]) => {
      calls.push(args);
      const child = new EventEmitter();
      queueMicrotask(() => child.emit('exit', 0, null));
      return child;
    });
    await runElectronPack({
      verify: async () => '/verified/electron',
      spawnProcess: spawnProcess as never,
      prepareSupplier: async () => ({ digest: 'a'.repeat(64), stagingRoot: '/staged/supplier', cleanup: async () => undefined }),
      env: {
        NODE_ENV: 'test',
        [ELECTRON_OUTPUT_DIRECTORY_ENV]: outputDirectory,
        CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST: 'a'.repeat(64),
        CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST: dependencyDigest
      }
    });
    expect(calls[0]).toContain(`-c.directories.output=${outputDirectory}`);
    expect(expectedPackagedAppPath(outputDirectory)).toBe(
      '/private/tmp/chirality candidate/mac-arm64/Chirality.app'
    );
    expect(() => resolveElectronOutputDirectory({ NODE_ENV: 'test', [ELECTRON_OUTPUT_DIRECTORY_ENV]: '' })).toThrow(
      'must be a normalized absolute path'
    );
    expect(() => resolveElectronOutputDirectory({ NODE_ENV: 'test', [ELECTRON_OUTPUT_DIRECTORY_ENV]: 'relative/dist' })).toThrow(
      'must be a normalized absolute path'
    );
  });

  it('routes prepare, payload binding, and final package commands through explicit v2 phases', async () => {
    const pkg = JSON.parse(await readFile(path.resolve(process.cwd(), 'package.json'), 'utf8')) as { scripts: Record<string, string> };
    expect(pkg.scripts['runtime:build-core']).toBe('npm --prefix ../../chirality-runtime run build --workspace @chirality/runtime-core');
    const invocation = (name: string) => (pkg.scripts[name] ?? '').split('pack-electron-with-supply.mjs ')[1]?.split(' && ')[0]?.trim().split(' ') ?? [];
    expect(parseArgs(invocation('desktop:prepare'))).toEqual({ target: 'dir', runtimeManifestVersion: 'v2' });
    expect(parseArgs(invocation('desktop:bind-payload'))).toEqual({ target: 'dir', runtimeManifestVersion: 'v2', runtimeV2Phase: 'payload' });
    expect(parseArgs(invocation('desktop:pack'))).toEqual({ target: 'dir', runtimeManifestVersion: 'v2', runtimeV2Phase: 'seal' });
    expect(parseArgs(invocation('desktop:dist'))).toEqual({ target: 'dmg', runtimeManifestVersion: 'v2', runtimeV2Phase: 'seal' });
    expect(pkg.scripts['desktop:prepare']).toContain('npm run runtime:build-core');
  });

  it('prepares signed v2 bytes without claiming future profile or governance identities', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-runtime-v2-pack-')));
    const inputs = await v2ReleaseInputs(root);
    const dependencyDigest = await computeDependencyResolutionDigest();
    const calls: Array<{ args: string[]; options: { env?: Record<string, string> } }> = [];
    try {
      await runElectronPack({
        runtimeManifestVersion: 'v2',
        verify: async () => '/verified/electron',
        spawnProcess: ((_command: string, _args: string[], options: { env?: Record<string, string> }) => {
          calls.push({ args: _args, options });
          const child = new EventEmitter();
          queueMicrotask(async () => {
            await writeFile(path.join(root, 'prepared.json'), '{}\n');
            child.emit('exit', 0, null);
          });
          return child;
        }) as never,
        prepareSupplier: async () => ({ digest: 'a'.repeat(64), stagingRoot: '/staged/supplier', cleanup: async () => undefined }),
        env: {
          NODE_ENV: 'test',
          CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST: 'a'.repeat(64),
          CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST: dependencyDigest,
          [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40),
          [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
          [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app',
          [SIGNING_CHECKPOINT_FILE_ENV]: path.join(root, 'prepared.json'),
          [RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV]: inputs.supportProfilesPath,
          [RUNTIME_V2_GOVERNANCE_ROOT_ENV]: inputs.governanceRoot
        }
      });
      expect(calls[0]?.options.env).toMatchObject({
        [RUNTIME_MANIFEST_VERSION_ENV]: 'v2',
        [RUNTIME_V2_SUPPORT_PROFILES_FILE_ENV]: inputs.supportProfilesPath,
        [RUNTIME_V2_GOVERNANCE_ROOT_ENV]: inputs.governanceRoot
      });
      expect(calls[0]?.options.env?.[RUNTIME_V2_INPUT_DIGEST_ENV]).toBeUndefined();
      expect(calls[0]?.args).toContain('-c.npmRebuild=false');
      expect(parseArgs(['--runtime-manifest', 'v2'])).toEqual({ target: 'dir', runtimeManifestVersion: 'v2' });
    } finally {
      await rm(root, { recursive: true, force: true });
    }
  });

  it('allows the nested-signing preparation stage before support and governance acceptance exists', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-runtime-v2-checkpoint-')));
    const checkpoint = path.join(root, 'prepared.json');
    const dependencyDigest = await computeDependencyResolutionDigest();
    const verify = vi.fn(async () => '/verified/electron');
    const spawnProcess = vi.fn(() => {
      const child = new EventEmitter();
      queueMicrotask(async () => {
        await writeFile(checkpoint, '{}\n');
        child.emit('exit', 0, null);
      });
      return child;
    });
    try {
      await runElectronPack({
        runtimeManifestVersion: 'v2',
        verify,
        spawnProcess: spawnProcess as never,
        prepareSupplier: async () => ({ digest: 'a'.repeat(64), stagingRoot: '/staged/supplier', cleanup: async () => undefined }),
        env: {
          NODE_ENV: 'test',
          CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST: 'a'.repeat(64),
          CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST: dependencyDigest,
          [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40),
          [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
          [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app',
          [SIGNING_CHECKPOINT_FILE_ENV]: checkpoint
        }
      });
      expect(verify).toHaveBeenCalledOnce();
      expect(spawnProcess).toHaveBeenCalledOnce();
    } finally {
      await rm(root, { recursive: true, force: true });
    }
  });

  it('fails closed and preserves supplier custody when the builder exits normally without a v2 checkpoint', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-runtime-v2-missing-checkpoint-')));
    const cleanup = vi.fn(async () => undefined);
    const dependencyDigest = await computeDependencyResolutionDigest();
    try {
      await expect(runElectronPack({
        runtimeManifestVersion: 'v2',
        verify: async () => '/verified/electron',
        spawnProcess: (() => {
          const child = new EventEmitter();
          queueMicrotask(() => child.emit('exit', 0, null));
          return child;
        }) as never,
        prepareSupplier: async () => ({ digest: 'a'.repeat(64), stagingRoot: '/staged/supplier', cleanup }),
        env: {
          NODE_ENV: 'test',
          CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST: 'a'.repeat(64),
          CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST: dependencyDigest,
          [SIGNING_IDENTITY_SHA1_ENV]: 'A'.repeat(40),
          [SIGNING_TEAM_ID_ENV]: 'A1B2C3D4E5',
          [SIGNING_BUNDLE_ID_ENV]: 'com.chirality.app',
          [SIGNING_CHECKPOINT_FILE_ENV]: path.join(root, 'missing.json')
        }
      })).rejects.toThrow('completed without the required Runtime v2 nested-signing checkpoint');
      expect(cleanup).not.toHaveBeenCalled();
    } finally {
      await rm(root, { recursive: true, force: true });
    }
  });

  it('routes payload binding and sealing explicitly, packaging only a successfully sealed app', async () => {
    const checkpoint = path.join(os.tmpdir(), 'prepared.json');
    const bindPayload = vi.fn(async () => ({ checkpointPath: checkpoint, payloadManifest: '/stage/Chirality.app/Contents/Resources/runtime-payload-manifest.json' }));
    const payloadManifest: RuntimePayloadManifestV2 = { schema: 'chirality-runtime-payload-manifest/v2', dependencyResolutionDigest: 'c'.repeat(64), roots: [], supportProfiles: [], entries: [] };
    const governance = [
      governanceArtifact('runtime-governance/v2/login-purpose-record.json'), governanceArtifact('runtime-governance/v2/login-purpose-acceptance.json'), governanceArtifact('runtime-governance/v2/login-owner-act'),
      governanceArtifact('runtime-governance/v2/worker-purpose-record.json'), governanceArtifact('runtime-governance/v2/worker-purpose-acceptance.json'), governanceArtifact('runtime-governance/v2/worker-owner-act')
    ] satisfies GovernanceFixture;
    const inventoryDocument = {
      schema: 'chirality-runtime-artifact-inventory/v2' as const,
      payloadManifest: { relativePath: 'runtime-payload-manifest.json' as const, size: 1, sha256: 'a'.repeat(64) },
      governance
    };
    const verified: VerifiedPackagedRuntimeBasisV2 = {
      resourcesRoot: '/stage/Chirality.app/Contents/Resources',
      inventoryPath: '/stage/Chirality.app/Contents/Resources/runtime-artifact-inventory-v2.json',
      payloadManifestPath: '/stage/Chirality.app/Contents/Resources/runtime-payload-manifest.json',
      inventorySha256: 'b'.repeat(64), payloadDigest: 'c'.repeat(64), identityDigest: 'd'.repeat(64), payload: payloadManifest,
      inventory: inventoryDocument
    };
    const inventory = {
      inventoryPath: '/stage/Chirality.app/Contents/Resources/runtime-artifact-inventory-v2.json',
      inventory: inventoryDocument,
      verified
    };
    const outputDirectory = '/stage';
    const sealedAppPath = '/stage/mac-arm64/Chirality.app';
    const seal = vi.fn(async () => ({ appPath: sealedAppPath, artifactPath: '/stage/sealed.json', inventory }));
    const verify = vi.fn(async () => '/verified/electron');
    const calls: string[][] = [];
    const spawnProcess = vi.fn((_command: string, args: string[]) => {
      calls.push(args);
      const child = new EventEmitter();
      queueMicrotask(() => child.emit('exit', 0, null));
      return child;
    });
    const payloadPhase = parseArgs(['--runtime-manifest', 'v2', '--resume-checkpoint', checkpoint, '--runtime-v2-phase', 'payload']);
    await runElectronPack({ ...payloadPhase, bindPayload, seal, env: { NODE_ENV: 'test' } });
    expect(bindPayload).toHaveBeenCalledOnce();
    expect(seal).not.toHaveBeenCalled();
    const sealPhase = parseArgs(['--runtime-manifest', 'v2', '--resume-checkpoint', checkpoint, '--runtime-v2-phase', 'seal', '--target', 'dmg']);
    await runElectronPack({ ...sealPhase, bindPayload, seal, verify, spawnProcess: spawnProcess as never, env: { NODE_ENV: 'test', [ELECTRON_OUTPUT_DIRECTORY_ENV]: outputDirectory } });
    expect(seal).toHaveBeenCalledOnce();
    expect(seal).toHaveBeenCalledWith({
      env: expect.objectContaining({ [SIGNING_CHECKPOINT_FILE_ENV]: checkpoint }),
      expectedAppPath: sealedAppPath
    });
    expect(calls[0]).toEqual(buildElectronBuilderArgs('/verified/electron', 'dmg', sealedAppPath, outputDirectory));
    expect(parseArgs(['--runtime-manifest', 'v2', '--resume-checkpoint', checkpoint, '--runtime-v2-phase', 'seal'])).toEqual({
      target: 'dir', runtimeManifestVersion: 'v2', resumeCheckpoint: checkpoint, runtimeV2Phase: 'seal'
    });
  });

  it('rejects unknown targets and malformed CLI arguments', () => {
    expect(() => buildElectronBuilderArgs('/verified/electron', 'zip')).toThrow(
      'Unsupported Electron packaging target'
    );
    expect(() => parseArgs(['--target'])).toThrow('Usage:');
  });

  it('rejects a sealed app outside the selected candidate output before DMG packaging', async () => {
    const spawnProcess = vi.fn();
    await expect(runElectronPack({
      target: 'dmg',
      runtimeManifestVersion: 'v2',
      runtimeV2Phase: 'seal',
      resumeCheckpoint: '/checkpoint.json',
      seal: async () => sealedResult('/other/mac-arm64/Chirality.app'),
      spawnProcess: spawnProcess as never,
      env: {
        NODE_ENV: 'test',
        [ELECTRON_OUTPUT_DIRECTORY_ENV]: '/selected',
        [SIGNING_CHECKPOINT_FILE_ENV]: '/checkpoint.json'
      }
    })).rejects.toThrow('outside the selected Electron output directory');
    expect(spawnProcess).not.toHaveBeenCalled();
  });

  it('stages one explicit regular supplier tree without overwriting prior custody', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-supplier-source-')));
    const source = path.join(root, 'source');
    const staging = path.join(root, 'cache', 'chirality-supplier');
    await mkdir(path.join(source, 'support'), { recursive: true });
    await writeFile(path.join(source, 'codex'), 'supplier');
    await chmod(path.join(source, 'codex'), 0o755);
    await writeFile(path.join(source, 'codex-code-mode-host'), 'host');
    await chmod(path.join(source, 'codex-code-mode-host'), 0o755);
    await writeFile(path.join(source, 'support', 'model.json'), '{"model":"codex"}\n');
    try {
      const prepared = await prepareSupplierResources({
        env: { NODE_ENV: 'test', CHIRALITY_SUPPLIER_SOURCE_ROOT: source },
        stagingRoot: staging
      });
      expect(prepared.digest).toMatch(/^[a-f0-9]{64}$/);
      expect(await readFile(path.join(staging, 'codex'), 'utf8')).toBe('supplier');
      expect(await readFile(path.join(staging, 'codex-code-mode-host'), 'utf8')).toBe('host');
      expect(await readFile(path.join(staging, 'support', 'model.json'), 'utf8')).toContain('codex');
      await expect(prepareSupplierResources({
        env: { NODE_ENV: 'test', CHIRALITY_SUPPLIER_SOURCE_ROOT: source },
        stagingRoot: staging
      })).rejects.toThrow('Refusing to overwrite');
      await prepared.cleanup();
    } finally {
      await rm(root, { recursive: true, force: true });
    }
  });

  it('fails closed for absent, linked, or non-executable supplier input', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-supplier-invalid-')));
    const source = path.join(root, 'source');
    const staging = path.join(root, 'staging');
    await mkdir(source);
    await writeFile(path.join(source, 'codex'), 'supplier');
    try {
      await expect(prepareSupplierResources({ env: { NODE_ENV: 'test' }, stagingRoot: staging })).rejects.toThrow(
        'CHIRALITY_SUPPLIER_SOURCE_ROOT is required'
      );
      await expect(prepareSupplierResources({
        env: { NODE_ENV: 'test', CHIRALITY_SUPPLIER_SOURCE_ROOT: source },
        stagingRoot: staging
      })).rejects.toThrow('executable regular file named codex');
      await chmod(path.join(source, 'codex'), 0o755);
      await symlink(path.join(source, 'codex'), path.join(source, 'linked-sidecar'));
      await expect(prepareSupplierResources({
        env: { NODE_ENV: 'test', CHIRALITY_SUPPLIER_SOURCE_ROOT: source },
        stagingRoot: staging
      })).rejects.toThrow('unsupported entry');
    } finally {
      await rm(root, { recursive: true, force: true });
    }
  });

  it.each(['missing', 'directory', 'non-executable', 'symlink'])('rejects a %s Code Mode host before staging', async (kind) => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-host-invalid-')));
    const source = path.join(root, 'source');
    const stagingRoot = path.join(root, 'staged');
    try {
      await mkdir(source);
      await writeFile(path.join(source, 'codex'), 'supplier', { mode: 0o755 });
      const host = path.join(source, 'codex-code-mode-host');
      if (kind === 'directory') await mkdir(host);
      if (kind === 'non-executable') await writeFile(host, 'host', { mode: 0o644 });
      if (kind === 'symlink') await symlink(path.join(source, 'codex'), host);
      await expect(prepareSupplierResources({ env: { NODE_ENV: 'test', CHIRALITY_SUPPLIER_SOURCE_ROOT: source }, stagingRoot }))
        .rejects.toThrow(kind === 'symlink' ? 'unsupported entry' : 'executable regular file named codex-code-mode-host');
      await expect(readFile(path.join(stagingRoot, 'codex'))).rejects.toMatchObject({ code: 'ENOENT' });
    } finally {
      await rm(root, { recursive: true, force: true });
    }
  });

  it('preserves staged supplier custody when electron-builder fails', async () => {
    const dependencyDigest = await computeDependencyResolutionDigest();
    const cleanup = vi.fn(async () => undefined);
    const spawnProcess = () => {
      const child = new EventEmitter();
      queueMicrotask(() => child.emit('exit', 1, null));
      return child;
    };
    await expect(runElectronPack({
      verify: async () => '/verified/electron',
      spawnProcess: spawnProcess as never,
      prepareSupplier: async () => ({
        digest: 'a'.repeat(64),
        stagingRoot: '/staged/supplier',
        cleanup
      }),
      env: {
        NODE_ENV: 'test',
        CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST: 'a'.repeat(64),
        CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST: dependencyDigest
      }
    })).rejects.toThrow('electron-builder exited with status 1');
    expect(cleanup).not.toHaveBeenCalled();
  });

  it('does not invoke the builder without exact release-provided input digests', async () => {
    const dependencyDigest = await computeDependencyResolutionDigest();
    const spawnProcess = vi.fn();
    const common = {
      verify: async () => '/verified/electron',
      spawnProcess: spawnProcess as never,
      prepareSupplier: async () => ({
        digest: 'a'.repeat(64),
        stagingRoot: '/staged/supplier',
        cleanup: async () => undefined
      })
    };
    await expect(runElectronPack({ ...common, env: { NODE_ENV: 'test' } })).rejects.toThrow(
      'CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST is required'
    );
    await expect(runElectronPack({
      ...common,
      env: {
        NODE_ENV: 'test',
        CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST: 'a'.repeat(64)
      }
    })).rejects.toThrow('CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST is required');
    await expect(runElectronPack({
      ...common,
      env: {
        NODE_ENV: 'test',
        CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST: 'c'.repeat(64),
        CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST: dependencyDigest
      }
    })).rejects.toThrow('Staged supplier tree does not match');
    await expect(runElectronPack({
      ...common,
      env: {
        NODE_ENV: 'test',
        CHIRALITY_EXPECTED_SUPPLIER_TREE_DIGEST: 'a'.repeat(64),
        CHIRALITY_EXPECTED_DEPENDENCY_RESOLUTION_DIGEST: 'c'.repeat(64)
      }
    })).rejects.toThrow('Dependency resolution inputs do not match');
    expect(spawnProcess).not.toHaveBeenCalled();
  });
});
