import { mkdtemp, mkdir, realpath, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { describe, expect, it } from 'vitest';
import {
  findForbiddenLegacyRuntimePackage,
  resolvePackagedDependencyBundlePath,
  verifyPackagedNativeAdmissionAsset,
  verifyPackagedRuntimeSources
} from '../../../scripts/verify-packaged-dependency-boundary.mjs';

const desktopSources = [
  '../electron/main.ts',
  '../electron/runtime-host.ts',
  '../../../chirality-runtime/packages/client/src/client.ts',
  '../../../chirality-runtime/packages/daemon/src/runtime-daemon.ts',
  '../../../chirality-runtime/packages/daemon/src/hosted-bootstrap.ts',
  '../../../chirality-runtime/packages/daemon/src/hosted-paths.ts',
  '../../../chirality-runtime/packages/daemon/src/hosted-boot.ts',
  '../../../chirality-runtime/packages/daemon/src/hosted-standalone.ts',
  '../../../chirality-runtime/packages/daemon/src/hosted-private-composition.ts',
  '../../../chirality-runtime/packages/daemon/src/hosted-private-entry.ts',
  '../../../chirality-runtime/packages/daemon/src/codex-admitted-launcher.ts',
  '../../../chirality-runtime/packages/daemon/src/codex-authenticated-transport.ts',
  '../../../chirality-runtime/packages/daemon/src/codex-supervisor.ts',
  '../../../chirality-runtime/packages/core/src/delegated-engine-adapter.ts',
  '../../../chirality-runtime/packages/native-admission/src/index.ts'
];
const cliSources = [
  '../../../chirality-runtime/packages/cli/src/bin.ts',
  '../../../chirality-runtime/packages/cli/src/cli.ts',
  '../../../chirality-runtime/packages/client/src/client.ts'
];
const packagedEntries = new Set(['/dist-electron/main.js', '/dist-electron/main.js.map']);

describe('packaged project runtime source proof', () => {
  it('resolves the dependency check from the shared explicit candidate output', () => {
    expect(resolvePackagedDependencyBundlePath({
      CHIRALITY_ELECTRON_OUTPUT_DIRECTORY: '/private/tmp/chirality candidate'
    })).toBe('/private/tmp/chirality candidate/mac-arm64/Chirality.app/Contents/Resources/app.asar');
    expect(() => resolvePackagedDependencyBundlePath({
      CHIRALITY_ELECTRON_OUTPUT_DIRECTORY: ''
    })).toThrow('must be a normalized absolute path');
  });

  it('accepts the shared hosted Codex runtime graph and a client-only CLI', () => {
    expect(
      verifyPackagedRuntimeSources({ desktopSources, cliSources, packagedEntries }).failures
    ).toEqual([]);
  });

  it('fails closed when the private hosted transport or native admission graph is incomplete', () => {
    const omitted = new Set([
      'hosted-private-composition.ts',
      'hosted-private-entry.ts',
      'codex-admitted-launcher.ts',
      'codex-authenticated-transport.ts',
      'native-admission/src/index.ts'
    ]);
    const result = verifyPackagedRuntimeSources({
      desktopSources: desktopSources.filter(
        (source) => ![...omitted].some((suffix) => source.endsWith(`/${suffix}`))
      ),
      cliSources,
      packagedEntries
    });

    expect(result.failures).toEqual(
      expect.arrayContaining([
        'desktop bundle is missing Codex production source chirality-runtime/packages/daemon/src/hosted-private-composition.ts',
        'desktop bundle is missing Codex production source chirality-runtime/packages/daemon/src/hosted-private-entry.ts',
        'desktop bundle is missing Codex production source chirality-runtime/packages/daemon/src/codex-admitted-launcher.ts',
        'desktop bundle is missing Codex production source chirality-runtime/packages/daemon/src/codex-authenticated-transport.ts',
        'desktop bundle is missing Codex production source chirality-runtime/packages/native-admission/src/index.ts'
      ])
    );
  });

  it('rejects stale server code from the previous runtime location', () => {
    const result = verifyPackagedRuntimeSources({
      desktopSources,
      cliSources: [...cliSources, '../../../../runtime/packages/daemon/src/runtime-daemon.ts'],
      packagedEntries
    });
    expect(result.failures).toEqual([
      expect.stringContaining('CLI client bundle unexpectedly embeds server source')
    ]);
  });

  it('rejects legacy engines in the Codex-only desktop and server code in the CLI client', () => {
    const result = verifyPackagedRuntimeSources({
      desktopSources: [
        ...desktopSources,
        '../electron/runtime-host-legacy.ts',
        '../src/lib/harness/claude-agent-sdk-manager.ts',
        '../src/lib/harness/pi-agent-engine-adapter.ts',
        '../../../chirality-runtime/packages/engine-claude/src/index.ts',
        '../../../chirality-runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts'
      ],
      cliSources: [...cliSources, '../../../chirality-runtime/packages/daemon/src/runtime-daemon.ts'],
      packagedEntries
    });

    expect(result.failures).toEqual(
      expect.arrayContaining([
        expect.stringContaining('unexpectedly embeds legacy engine source'),
        expect.stringContaining('CLI client bundle unexpectedly embeds server source')
      ])
    );
  });

  it('identifies base and platform-specific legacy Claude packages', () => {
    expect(
      findForbiddenLegacyRuntimePackage(
        '/node_modules/@anthropic-ai/claude-agent-sdk-darwin-arm64/claude'
      )
    ).toBe('@anthropic-ai/claude-agent-sdk-darwin-arm64');
    expect(
      findForbiddenLegacyRuntimePackage('/node_modules/@anthropic-ai/claude-agent-sdk/sdk.mjs')
    ).toBe('@anthropic-ai/claude-agent-sdk');
    expect(findForbiddenLegacyRuntimePackage('/node_modules/next/package.json')).toBeNull();
  });
});

describe('packaged native-admission asset proof', () => {
  it('accepts only the readable regular asset at the exact packaged path', async () => {
    const resourcesRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-native-resource-'));
    try {
      const nativeDirectory = path.join(resourcesRoot, 'native');
      await mkdir(nativeDirectory);
      const assetPath = path.join(nativeDirectory, 'chirality_native_admission.node');
      await writeFile(assetPath, 'fixture');
      const canonicalResourcesRoot = await realpath(resourcesRoot);

      await expect(verifyPackagedNativeAdmissionAsset({ resourcesRoot })).resolves.toMatchObject({
        status: 'PASS',
        path: path.join(canonicalResourcesRoot, 'native', 'chirality_native_admission.node'),
        canonicalResourcesRoot,
        failures: []
      });
    } finally {
      await rm(resourcesRoot, { recursive: true, force: true });
    }
  });

  it('fails when the exact native asset is missing', async () => {
    const resourcesRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-native-resource-'));
    try {
      await mkdir(path.join(resourcesRoot, 'native'));
      const result = await verifyPackagedNativeAdmissionAsset({ resourcesRoot });
      expect(result.status).toBe('FAIL');
      expect(result.failures).toEqual([
        expect.stringContaining('Unable to read packaged native-admission asset')
      ]);
    } finally {
      await rm(resourcesRoot, { recursive: true, force: true });
    }
  });

  it('rejects symlinked native directories, symlinked assets, and traversal-shaped roots', async () => {
    const fixtureRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-native-resource-'));
    try {
      const realNative = path.join(fixtureRoot, 'real-native');
      await mkdir(realNative);
      await writeFile(path.join(realNative, 'chirality_native_admission.node'), 'fixture');

      const directoryLinkRoot = path.join(fixtureRoot, 'directory-link-resources');
      await mkdir(directoryLinkRoot);
      await symlink(realNative, path.join(directoryLinkRoot, 'native'));
      const directoryLink = await verifyPackagedNativeAdmissionAsset({
        resourcesRoot: directoryLinkRoot
      });
      expect(directoryLink.status).toBe('FAIL');
      expect(directoryLink.failures).toEqual(
        expect.arrayContaining([expect.stringContaining('native directory must be')])
      );

      const assetLinkRoot = path.join(fixtureRoot, 'asset-link-resources');
      await mkdir(path.join(assetLinkRoot, 'native'), { recursive: true });
      await symlink(
        path.join(realNative, 'chirality_native_admission.node'),
        path.join(assetLinkRoot, 'native', 'chirality_native_admission.node')
      );
      const assetLink = await verifyPackagedNativeAdmissionAsset({ resourcesRoot: assetLinkRoot });
      expect(assetLink.status).toBe('FAIL');
      expect(assetLink.failures).toEqual(
        expect.arrayContaining([expect.stringContaining('native-admission asset must be')])
      );

      const traversalRoot = `${fixtureRoot}/native/..`;
      await expect(
        verifyPackagedNativeAdmissionAsset({ resourcesRoot: traversalRoot })
      ).resolves.toMatchObject({
        status: 'FAIL',
        failures: ['Resources root must be a normalized absolute path']
      });
    } finally {
      await rm(fixtureRoot, { recursive: true, force: true });
    }
  });
});
