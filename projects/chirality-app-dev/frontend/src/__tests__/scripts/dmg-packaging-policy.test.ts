import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { describe, expect, it } from 'vitest';

const PACKAGE_JSON_PATH = path.resolve(process.cwd(), 'package.json');

type BuildTarget = string | { target?: string; arch?: string[] };

type ExtraResource = {
  from?: string;
  to?: string;
  filter?: string[];
};

type FrontendPackageJson = {
  devDependencies?: Record<string, string>;
  engines?: {
    node?: string;
  };
  scripts?: Record<string, string>;
  build?: {
    asar?: boolean;
    files?: string[];
    electronFuses?: Record<string, boolean>;
    mac?: {
      minimumSystemVersion?: string;
      target?: BuildTarget[];
    };
    extraResources?: ExtraResource[];
    afterPack?: string;
  };
};

async function readPackageJson(): Promise<FrontendPackageJson> {
  const raw = await readFile(PACKAGE_JSON_PATH, 'utf8');
  return JSON.parse(raw) as FrontendPackageJson;
}

function parseMajor(version: string): number {
  const [majorToken] = version.split('.');
  return Number.parseInt(majorToken, 10);
}

describe('dmg packaging policy', () => {
  it('pins the approved Electron runtime toolchain and Node floor', async () => {
    const pkg = await readPackageJson();

    expect(pkg.devDependencies?.electron).toBe('43.2.0');
    expect(pkg.devDependencies?.['electron-builder']).toBe('26.15.3');
    expect(pkg.devDependencies?.['@types/node']).toBe('24.12.4');
    expect(pkg.engines?.node).toBe('>=22.19.0');
  });

  // The unsigned-packaging, packaged-proof-command, monorepo-symlink-exclusion,
  // and Pi proof-command substring pins moved to the consolidated
  // src/__tests__/contract-pins.manifest.ts (checked by contract-pins.test.ts).
  // This file keeps the structural (non-substring) packaging assertions.

  it('pins macOS minimum version and arm64 dmg target', async () => {
    const pkg = await readPackageJson();
    const minimumSystemVersion = pkg.build?.mac?.minimumSystemVersion ?? '';
    const targetEntries = pkg.build?.mac?.target ?? [];

    expect(minimumSystemVersion).not.toBe('');
    expect(parseMajor(minimumSystemVersion)).toBeGreaterThanOrEqual(15);

    const hasArm64DmgTarget = targetEntries.some((entry) => {
      if (typeof entry === 'string') {
        return entry === 'dmg';
      }

      if (entry.target !== 'dmg') {
        return false;
      }

      return (entry.arch ?? []).includes('arm64');
    });

    expect(hasArm64DmgTarget).toBe(true);
  });

  it('bundles instruction-root resources into packaged artifacts', async () => {
    const pkg = await readPackageJson();
    const resources = pkg.build?.extraResources ?? [];

    expect(resources).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          from: 'node_modules/.cache/chirality-instruction-root',
          to: 'instruction-root',
          filter: ['**/*']
        })
      ])
    );
    expect(pkg.scripts?.['instruction-root:prepare']).toContain(
      'prepare-packaged-instruction-root.mjs'
    );
    expect(pkg.scripts?.['desktop:prepare']).toContain('npm run instruction-root:prepare');
    expect(pkg.scripts?.['desktop:dist']).toContain(
      'node ./scripts/pack-electron-with-supply.mjs --target dmg'
    );
  });

  it('ships the Runtime native-admission addon at its trusted packaged path', async () => {
    const pkg = await readPackageJson();
    expect(pkg.build?.extraResources).toEqual(
      expect.arrayContaining([
        {
          from: '../../chirality-runtime/packages/native-admission/build/Release/chirality_native_admission.node',
          to: 'native/chirality_native_admission.node'
        }
      ])
    );
  });

  it('requires the staged supplier tree and final Runtime inventory hook', async () => {
    const pkg = await readPackageJson();
    expect(pkg.build?.afterPack).toBe('./scripts/finalize-electron-resources.mjs');
    expect(pkg.build?.extraResources).toEqual(
      expect.arrayContaining([
        {
          from: 'node_modules/.cache/chirality-supplier',
          to: 'supplier',
          filter: ['**/*']
        }
      ])
    );
  });

  it('keeps application source in the asar archive', async () => {
    const pkg = await readPackageJson();
    expect(pkg.build?.asar).toBe(true);
    expect(pkg.build?.electronFuses).toEqual({
      runAsNode: false,
      enableNodeOptionsEnvironmentVariable: false,
      enableNodeCliInspectArguments: false,
      enableEmbeddedAsarIntegrityValidation: true,
      onlyLoadAppFromAsar: true
    });
    expect(pkg.build?.extraResources).toEqual(
      expect.arrayContaining([
        expect.objectContaining({ from: 'dist-runtime', to: 'runtime-cli' })
      ])
    );
  });

});
