import { EventEmitter } from 'node:events';
import { chmod, mkdtemp, mkdir, readFile, realpath, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { describe, expect, it, vi } from 'vitest';

import {
  buildElectronBuilderArgs,
  parseArgs,
  prepareSupplierResources,
  runElectronPack
} from '../../../scripts/pack-electron-with-supply.mjs';
import { computeDependencyResolutionDigest } from '../../../scripts/finalize-electron-resources.mjs';

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
    expect(calls[0]?.args).toEqual(buildElectronBuilderArgs(directory));
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
  });

  it('rejects unknown targets and malformed CLI arguments', () => {
    expect(() => buildElectronBuilderArgs('/verified/electron', 'zip')).toThrow(
      'Unsupported Electron packaging target'
    );
    expect(() => parseArgs(['--target'])).toThrow('Usage:');
  });

  it('stages one explicit regular supplier tree without overwriting prior custody', async () => {
    const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-supplier-source-')));
    const source = path.join(root, 'source');
    const staging = path.join(root, 'cache', 'chirality-supplier');
    await mkdir(path.join(source, 'support'), { recursive: true });
    await writeFile(path.join(source, 'codex'), 'supplier');
    await chmod(path.join(source, 'codex'), 0o755);
    await writeFile(path.join(source, 'support', 'model.json'), '{"model":"codex"}\n');
    try {
      const prepared = await prepareSupplierResources({
        env: { NODE_ENV: 'test', CHIRALITY_SUPPLIER_SOURCE_ROOT: source },
        stagingRoot: staging
      });
      expect(prepared.digest).toMatch(/^[a-f0-9]{64}$/);
      expect(await readFile(path.join(staging, 'codex'), 'utf8')).toBe('supplier');
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
