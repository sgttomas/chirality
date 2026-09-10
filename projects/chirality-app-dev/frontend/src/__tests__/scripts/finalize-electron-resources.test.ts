import { chmod, mkdtemp, mkdir, readFile, realpath, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { describe, expect, it } from 'vitest';

import {
  computeDependencyResolutionDigest,
  computeSupplierTreeDigest,
  writeRuntimeArtifactInventory
} from '../../../scripts/finalize-electron-resources.mjs';
import { runtimeConformanceArtifactInventory } from '../../../../../chirality-runtime/packages/core/src/runtime-conformance.js';

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
});
