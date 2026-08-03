import { describe, expect, it } from 'vitest';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import {
  RUNTIME_HELPER_BUNDLE_ID,
  RUNTIME_HELPER_BUNDLE_NAME,
  RUNTIME_HELPER_EXECUTABLE_NAME,
  resolveRuntimeHelperExecutable
} from '../../../electron/runtime-helper-path';

const frontendRoot = path.resolve(__dirname, '..', '..', '..');

describe('standalone runtime helper packaging', () => {
  it('resolves the embedded independently named helper executable', () => {
    expect(
      resolveRuntimeHelperExecutable('/Applications/Chirality.app/Contents/MacOS/Chirality')
    ).toBe(
      '/Applications/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service'
    );
    expect(RUNTIME_HELPER_BUNDLE_ID).toBe('com.chirality.app.runtime-helper');
    expect(RUNTIME_HELPER_BUNDLE_NAME).toBe('Chirality Runtime Service.app');
    expect(RUNTIME_HELPER_EXECUTABLE_NAME).toBe('Chirality Runtime Service');
  });

  it('uses a separate builder product and whole-bundle embedding source', async () => {
    const helperConfig = JSON.parse(
      await readFile(path.join(frontendRoot, 'electron-builder.runtime-helper.json'), 'utf8')
    ) as Record<string, unknown>;
    const packageJson = JSON.parse(
      await readFile(path.join(frontendRoot, 'package.json'), 'utf8')
    ) as { build: { afterPack: string }; scripts: Record<string, string> };
    const embedSource = await readFile(
      path.join(frontendRoot, 'scripts', 'embed-runtime-helper.mjs'),
      'utf8'
    );
    const helperEntry = await readFile(
      path.join(frontendRoot, 'electron', 'runtime-helper-entry.ts'),
      'utf8'
    );

    expect(helperConfig).toMatchObject({
      appId: 'com.chirality.app.runtime-helper',
      productName: 'Chirality Runtime Service',
      executableName: 'Chirality Runtime Service',
      directories: { output: 'dist-runtime-helper' },
      extraMetadata: { main: 'dist-electron/runtime-helper.js' },
      mac: { extendInfo: { LSUIElement: true } }
    });
    expect(packageJson.build.afterPack).toBe('scripts/embed-runtime-helper.mjs');
    expect(packageJson.scripts['desktop:pack']).toContain('npm run build:runtime-helper');
    expect(embedSource).toContain("'dist-runtime-helper'");
    expect(embedSource).toContain("'LoginItems'");
    expect(embedSource).not.toContain("'dist',\n    'mac-arm64',\n    'Chirality.app'");
    expect(helperEntry).toContain("appendSwitch('single-process')");
    expect(helperEntry).toContain("appendSwitch('disable-gpu')");
  });
});
