import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { mkdtemp, readFile, rm, stat, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';

const electronMocks = vi.hoisted(() => ({
  getPath: vi.fn((name: string) =>
    name === 'exe'
      ? '/Applications/Chirality.app/Contents/MacOS/Chirality'
      : '/Users/example/Library/Application Support/chirality-frontend'
  )
}));

vi.mock('electron', () => ({
  app: {
    getPath: electronMocks.getPath,
    isPackaged: true
  }
}));

import {
  installBundledCliLauncher,
  renderCliLauncher,
  SKIP_CLI_LAUNCHER_ENV
} from '../../../electron/cli-launcher';

const DESKTOP_EXECUTABLE = '/Applications/Chirality.app/Contents/MacOS/Chirality';
const CLI_ENTRY = '/Applications/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs';
const USER_DATA = '/Users/example/Library/Application Support/chirality-frontend';

describe('electron/cli-launcher renderCliLauncher', () => {
  it('uses Electron embedded Node and pins daemon install to the desktop executable', () => {
    const source = renderCliLauncher({
      desktopExecutable: "/Applications/Chirality O'Brien.app/Contents/MacOS/Chirality",
      cliEntry: CLI_ENTRY,
      pinnedEnvironment: { CHIRALITY_USER_DATA: USER_DATA }
    });

    expect(source).toContain('export ELECTRON_RUN_AS_NODE=1');
    expect(source).toContain('--executable "$desktop_executable"');
    expect(source).toContain('exec "$desktop_executable" "$cli_entry" "$@"');
    expect(source).toContain(`O'"'"'Brien`);
  });

  it('exports every pinned value conditionally so an explicit value still wins', () => {
    const source = renderCliLauncher({
      desktopExecutable: DESKTOP_EXECUTABLE,
      cliEntry: CLI_ENTRY,
      pinnedEnvironment: {
        CHIRALITY_USER_DATA: USER_DATA,
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: 'com.chirality.runtime',
        CHIRALITY_RUNTIME_KEEP_ALIVE: 'always'
      }
    });

    for (const [name, value] of [
      ['CHIRALITY_USER_DATA', `'${USER_DATA}'`],
      ['CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL', "'com.chirality.runtime'"],
      ['CHIRALITY_RUNTIME_KEEP_ALIVE', "'always'"]
    ]) {
      expect(source).toContain(`if [[ -z "\${${name}:-}" ]]; then\n  export ${name}=${value}\nfi`);
    }
  });

  it('renders pinned exports in a stable order so the file is byte-deterministic', () => {
    const pinnedEnvironment = {
      CHIRALITY_USER_DATA: USER_DATA,
      CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: 'com.chirality.runtime',
      CHIRALITY_RUNTIME_KEEP_ALIVE: 'always'
    };
    const first = renderCliLauncher({
      desktopExecutable: DESKTOP_EXECUTABLE,
      cliEntry: CLI_ENTRY,
      pinnedEnvironment
    });
    // Same values, different insertion order.
    const second = renderCliLauncher({
      desktopExecutable: DESKTOP_EXECUTABLE,
      cliEntry: CLI_ENTRY,
      pinnedEnvironment: {
        CHIRALITY_RUNTIME_KEEP_ALIVE: 'always',
        CHIRALITY_USER_DATA: USER_DATA,
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: 'com.chirality.runtime'
      }
    });

    expect(second).toBe(first);
  });

  it('shell-quotes a userData directory containing a single quote', () => {
    const source = renderCliLauncher({
      desktopExecutable: DESKTOP_EXECUTABLE,
      cliEntry: CLI_ENTRY,
      pinnedEnvironment: {
        CHIRALITY_USER_DATA: "/Users/o'brien/Library/Application Support/chirality-frontend"
      }
    });

    expect(source).toContain(
      `export CHIRALITY_USER_DATA='/Users/o'"'"'brien/Library/Application Support/chirality-frontend'`
    );
  });
});

describe('electron/cli-launcher installBundledCliLauncher', () => {
  let directory: string;
  let destination: string;
  // `resolveBundledCliEntry()` reads Electron's `process.resourcesPath`, which
  // does not exist under plain Node.
  const processWithResources = process as { resourcesPath?: string };
  const previousResourcesPath = processWithResources.resourcesPath;

  beforeEach(async () => {
    processWithResources.resourcesPath = '/Applications/Chirality.app/Contents/Resources';
    directory = await mkdtemp(path.join(os.tmpdir(), 'chirality-launcher-'));
    destination = path.join(directory, 'bin', 'chirality');
  });

  afterEach(async () => {
    if (previousResourcesPath === undefined) {
      delete processWithResources.resourcesPath;
    } else {
      processWithResources.resourcesPath = previousResourcesPath;
    }
    await rm(directory, { recursive: true, force: true });
  });

  it('writes the launcher on a first install', async () => {
    const result = await installBundledCliLauncher(destination, {});

    expect(result).toEqual({ status: 'written', path: destination });
    const contents = await readFile(destination, 'utf8');
    expect(contents).toContain('export ELECTRON_RUN_AS_NODE=1');
    expect(contents).toContain('CHIRALITY_RUNTIME_KEEP_ALIVE');
    expect((await stat(destination)).mode & 0o777).toBe(0o700);
  });

  it('is idempotent: an unchanged launcher is not rewritten', async () => {
    await installBundledCliLauncher(destination, {});
    const firstMtime = (await stat(destination)).mtimeMs;

    const result = await installBundledCliLauncher(destination, {});

    expect(result).toEqual({ status: 'unchanged', path: destination });
    expect((await stat(destination)).mtimeMs).toBe(firstMtime);
  });

  it('rewrites when the rendered content actually changes', async () => {
    await installBundledCliLauncher(destination, {});

    const result = await installBundledCliLauncher(destination, {
      CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: 'com.chirality.runtime.tranchetest'
    });

    expect(result).toEqual({ status: 'written', path: destination });
    expect(await readFile(destination, 'utf8')).toContain('com.chirality.runtime.tranchetest');
  });

  it('honors the opt-out without touching the destination', async () => {
    const result = await installBundledCliLauncher(destination, {
      [SKIP_CLI_LAUNCHER_ENV]: '1'
    });

    expect(result).toEqual({ status: 'skipped', path: destination, reason: 'opted-out' });
    await expect(stat(destination)).rejects.toMatchObject({ code: 'ENOENT' });
  });

  it('treats a blank opt-out as not set', async () => {
    const result = await installBundledCliLauncher(destination, {
      [SKIP_CLI_LAUNCHER_ENV]: '   '
    });

    expect(result).toEqual({ status: 'written', path: destination });
  });

  it('replaces an unrelated pre-existing file rather than leaving it stale', async () => {
    await installBundledCliLauncher(destination, {});
    await writeFile(destination, '#!/bin/zsh\n# something else\n', { mode: 0o700 });

    const result = await installBundledCliLauncher(destination, {});

    expect(result).toEqual({ status: 'written', path: destination });
    expect(await readFile(destination, 'utf8')).toContain('export ELECTRON_RUN_AS_NODE=1');
  });
});
