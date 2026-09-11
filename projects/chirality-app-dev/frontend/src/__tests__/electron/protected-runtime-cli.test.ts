import { describe, expect, it, vi } from 'vitest';

import {
  runProtectedRuntimeCli,
  type ProtectedRuntimeCliEntry
} from '../../../electron/protected-runtime-cli';

function controlledEntry() {
  const io = {
    stdout: vi.fn(),
    stderr: vi.fn(),
    readStdin: vi.fn(async () => '')
  };
  const dependencies = {} as ReturnType<ProtectedRuntimeCliEntry['createDependencies']>;
  const createDependencies = vi.fn(() => dependencies);
  const run = vi.fn(async () => 0);
  return {
    entry: { createDependencies, io, run } satisfies ProtectedRuntimeCliEntry,
    createDependencies,
    dependencies,
    io,
    run
  };
}

describe('protected Runtime CLI entry', () => {
  it('hands ordinary arguments to Runtime CLI unchanged on the same controlled entry', async () => {
    const controlled = controlledEntry();
    await expect(
      runProtectedRuntimeCli(
        ['project', 'list'],
        '/Applications/Chirality.app/Contents/MacOS/Chirality',
        false,
        controlled.entry
      )
    ).resolves.toBe(0);
    expect(controlled.run).toHaveBeenCalledWith(
      ['project', 'list'],
      controlled.io,
      controlled.dependencies
    );
  });

  it('injects the exact running desktop executable for daemon install', async () => {
    const controlled = controlledEntry();
    const executable = '/Applications/Chirality.app/Contents/MacOS/Chirality';
    await runProtectedRuntimeCli(['daemon', 'install'], executable, true, controlled.entry);
    expect(controlled.run).toHaveBeenCalledWith(
      ['daemon', 'install', '--executable', executable],
      controlled.io,
      controlled.dependencies
    );
  });

  it.each([
    ['daemon', 'install', '--executable', '/tmp/other'],
    ['daemon', 'install', '--executable=/tmp/other']
  ])('rejects caller-selected daemon executables: %j', async (...arguments_) => {
    const controlled = controlledEntry();
    await expect(
      runProtectedRuntimeCli(
        arguments_,
        '/Applications/Chirality.app/Contents/MacOS/Chirality',
        true,
        controlled.entry
      )
    ).resolves.toBe(2);
    expect(controlled.run).not.toHaveBeenCalled();
    expect(controlled.io.stderr).toHaveBeenCalledOnce();
  });

  it('rejects daemon installation from an unpackaged App before Runtime dependencies exist', async () => {
    const controlled = controlledEntry();
    await expect(
      runProtectedRuntimeCli(
        ['daemon', 'install'],
        '/source/node_modules/electron/dist/Electron.app/Contents/MacOS/Electron',
        false,
        controlled.entry
      )
    ).resolves.toBe(2);
    expect(controlled.createDependencies).not.toHaveBeenCalled();
    expect(controlled.run).not.toHaveBeenCalled();
    expect(controlled.io.stderr).toHaveBeenCalledWith(
      'daemon install requires a packaged Chirality application.\n'
    );
  });
});
