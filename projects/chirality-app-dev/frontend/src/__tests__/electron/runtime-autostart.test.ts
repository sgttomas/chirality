import { beforeEach, describe, expect, it, vi } from 'vitest';
import { renderRuntimeLaunchAgent } from '@chirality/runtime-cli';
import {
  SKIP_RUNTIME_AUTOSTART_ENV,
  ensureRuntimeDaemonAutostart,
  readLaunchAgentProgramPath
} from '../../../electron/runtime-autostart';

const DESKTOP_EXECUTABLE = '/Applications/Chirality.app/Contents/MacOS/Chirality';
const FOREIGN_EXECUTABLE = '/Users/tester/Downloads/Chirality Trial.app/Contents/MacOS/Chirality';

function plistFor(executablePath: string): string {
  return renderRuntimeLaunchAgent({
    executablePath,
    runtimeDirectory: '/Users/tester/Library/Application Support/Chirality/runtime',
    label: 'com.chirality.runtime',
    keepAlive: 'always',
    environmentVariables: { CHIRALITY_USER_DATA: '/Users/tester/Library/Application Support/Chirality' }
  });
}

function fakeLifecycle(status: { installed: boolean; loaded: boolean }) {
  return {
    install: vi.fn<(executablePath: string) => Promise<void>>(async () => undefined),
    start: vi.fn<() => Promise<void>>(async () => undefined),
    status: vi.fn(async () => ({ ...status }))
  };
}

const log = vi.fn();

function events(): string[] {
  return log.mock.calls.map(([, event]) => event as string);
}

beforeEach(() => {
  log.mockClear();
});

describe('readLaunchAgentProgramPath', () => {
  it('reads the first ProgramArguments entry of a rendered plist, unescaped', () => {
    const quoted = "/Applications/Chirality O'Brien.app/Contents/MacOS/Chirality";
    expect(readLaunchAgentProgramPath(plistFor(DESKTOP_EXECUTABLE))).toBe(DESKTOP_EXECUTABLE);
    expect(readLaunchAgentProgramPath(plistFor(quoted))).toBe(quoted);
  });

  it('returns undefined when no executable is named', () => {
    expect(readLaunchAgentProgramPath('<plist><dict></dict></plist>')).toBeUndefined();
    expect(readLaunchAgentProgramPath('')).toBeUndefined();
  });
});

describe('ensureRuntimeDaemonAutostart', () => {
  it('installs with the desktop executable and starts when the job is not installed', async () => {
    const lifecycle = fakeLifecycle({ installed: false, loaded: false });
    const readInstalledPlist = vi.fn(async () => undefined);

    const outcome = await ensureRuntimeDaemonAutostart({
      lifecycle,
      desktopExecutable: DESKTOP_EXECUTABLE,
      packaged: true,
      readInstalledPlist,
      environment: {},
      log
    });

    expect(outcome).toEqual({ action: 'installed-and-started' });
    expect(lifecycle.install).toHaveBeenCalledWith(DESKTOP_EXECUTABLE);
    expect(lifecycle.start).toHaveBeenCalledOnce();
    expect(lifecycle.install.mock.invocationCallOrder[0]).toBeLessThan(
      lifecycle.start.mock.invocationCallOrder[0]
    );
    // Nothing to inspect: no plist existed before this install.
    expect(readInstalledPlist).not.toHaveBeenCalled();
    expect(events()).toEqual([
      'runtime.autostart.status',
      'runtime.autostart.installed',
      'runtime.autostart.started'
    ]);
  });

  it('only starts when the job is installed for this executable but not loaded', async () => {
    const lifecycle = fakeLifecycle({ installed: true, loaded: false });

    const outcome = await ensureRuntimeDaemonAutostart({
      lifecycle,
      desktopExecutable: DESKTOP_EXECUTABLE,
      packaged: true,
      readInstalledPlist: async () => plistFor(DESKTOP_EXECUTABLE),
      environment: {},
      log
    });

    expect(outcome).toEqual({ action: 'started' });
    expect(lifecycle.install).not.toHaveBeenCalled();
    expect(lifecycle.start).toHaveBeenCalledOnce();
    expect(events()).toEqual(['runtime.autostart.status', 'runtime.autostart.started']);
  });

  it('does nothing when the job is installed for this executable and loaded', async () => {
    const lifecycle = fakeLifecycle({ installed: true, loaded: true });

    const outcome = await ensureRuntimeDaemonAutostart({
      lifecycle,
      desktopExecutable: DESKTOP_EXECUTABLE,
      packaged: true,
      readInstalledPlist: async () => plistFor(DESKTOP_EXECUTABLE),
      environment: {},
      log
    });

    expect(outcome).toEqual({ action: 'skipped', reason: 'already-loaded' });
    expect(lifecycle.install).not.toHaveBeenCalled();
    expect(lifecycle.start).not.toHaveBeenCalled();
  });

  it('refuses to start or overwrite a plist that names a different executable, loaded or not', async () => {
    for (const loaded of [false, true]) {
      log.mockClear();
      const lifecycle = fakeLifecycle({ installed: true, loaded });

      const outcome = await ensureRuntimeDaemonAutostart({
        lifecycle,
        desktopExecutable: DESKTOP_EXECUTABLE,
        packaged: true,
        readInstalledPlist: async () => plistFor(FOREIGN_EXECUTABLE),
        environment: {},
        log
      });

      expect(outcome).toEqual({
        action: 'refused',
        reason: 'foreign-executable',
        installedExecutable: FOREIGN_EXECUTABLE
      });
      expect(lifecycle.install).not.toHaveBeenCalled();
      expect(lifecycle.start).not.toHaveBeenCalled();
      expect(log).toHaveBeenCalledWith('error', 'runtime.autostart.refused_foreign_executable', {
        installedExecutable: FOREIGN_EXECUTABLE,
        desktopExecutable: DESKTOP_EXECUTABLE
      });
    }
  });

  it('treats an installed plist that cannot be identified as a failure, not as ours', async () => {
    const lifecycle = fakeLifecycle({ installed: true, loaded: false });

    const outcome = await ensureRuntimeDaemonAutostart({
      lifecycle,
      desktopExecutable: DESKTOP_EXECUTABLE,
      packaged: true,
      readInstalledPlist: async () => undefined,
      environment: {},
      log
    });

    expect(outcome).toMatchObject({ action: 'failed', stage: 'inspect' });
    expect(lifecycle.install).not.toHaveBeenCalled();
    expect(lifecycle.start).not.toHaveBeenCalled();
  });

  it('isolates every lifecycle failure into a logged outcome instead of throwing', async () => {
    const failing = fakeLifecycle({ installed: false, loaded: false });
    failing.status.mockRejectedValueOnce(new Error('launchctl unavailable'));
    await expect(
      ensureRuntimeDaemonAutostart({
        lifecycle: failing,
        desktopExecutable: DESKTOP_EXECUTABLE,
        packaged: true,
        readInstalledPlist: async () => undefined,
        environment: {},
        log
      })
    ).resolves.toEqual({ action: 'failed', stage: 'status', error: 'launchctl unavailable' });
    expect(failing.install).not.toHaveBeenCalled();

    const installFails = fakeLifecycle({ installed: false, loaded: false });
    installFails.install.mockRejectedValueOnce(new Error('EACCES: LaunchAgents'));
    await expect(
      ensureRuntimeDaemonAutostart({
        lifecycle: installFails,
        desktopExecutable: DESKTOP_EXECUTABLE,
        packaged: true,
        readInstalledPlist: async () => undefined,
        environment: {},
        log
      })
    ).resolves.toEqual({ action: 'failed', stage: 'install', error: 'EACCES: LaunchAgents' });
    expect(installFails.start).not.toHaveBeenCalled();

    const startFails = fakeLifecycle({ installed: true, loaded: false });
    startFails.start.mockRejectedValueOnce(new Error('Bootstrap failed: 5: Input/output error'));
    await expect(
      ensureRuntimeDaemonAutostart({
        lifecycle: startFails,
        desktopExecutable: DESKTOP_EXECUTABLE,
        packaged: true,
        readInstalledPlist: async () => plistFor(DESKTOP_EXECUTABLE),
        environment: {},
        log
      })
    ).resolves.toEqual({
      action: 'failed',
      stage: 'start',
      error: 'Bootstrap failed: 5: Input/output error'
    });

    const readFails = fakeLifecycle({ installed: true, loaded: false });
    await expect(
      ensureRuntimeDaemonAutostart({
        lifecycle: readFails,
        desktopExecutable: DESKTOP_EXECUTABLE,
        packaged: true,
        readInstalledPlist: async () => {
          throw new Error('EIO');
        },
        environment: {},
        log
      })
    ).resolves.toEqual({ action: 'failed', stage: 'inspect', error: 'EIO' });
    expect(readFails.start).not.toHaveBeenCalled();

    expect(log.mock.calls.filter(([level, event]) => level === 'error' && event === 'runtime.autostart.failed')).toHaveLength(4);
  });

  it('never touches the lifecycle when unpackaged or explicitly opted out', async () => {
    const lifecycle = fakeLifecycle({ installed: false, loaded: false });

    await expect(
      ensureRuntimeDaemonAutostart({
        lifecycle,
        desktopExecutable: DESKTOP_EXECUTABLE,
        packaged: false,
        readInstalledPlist: async () => undefined,
        environment: {},
        log
      })
    ).resolves.toEqual({ action: 'skipped', reason: 'unpackaged' });

    await expect(
      ensureRuntimeDaemonAutostart({
        lifecycle,
        desktopExecutable: DESKTOP_EXECUTABLE,
        packaged: true,
        readInstalledPlist: async () => undefined,
        environment: { [SKIP_RUNTIME_AUTOSTART_ENV]: '1' },
        log
      })
    ).resolves.toEqual({ action: 'skipped', reason: 'opted-out' });

    expect(lifecycle.status).not.toHaveBeenCalled();
    expect(lifecycle.install).not.toHaveBeenCalled();
    expect(lifecycle.start).not.toHaveBeenCalled();
  });
});
