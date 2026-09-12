/**
 * Automatic runtime-daemon start for the packaged desktop app.
 *
 * Ordinary use must not require an operator to install, start, or manage the
 * daemon: the GUI reconciles the LaunchAgent at every packaged launch and the
 * manual runtime controls remain a repair surface behind Settings. The decision
 * logic lives here, free of `electron` imports, so the installed/loaded matrix,
 * the foreign-plist refusal, and the failure isolation are checkable in a unit
 * test rather than only in a packaged run.
 *
 * The lifecycle is the same `createDesktopDaemonLifecycle()` instance the manual
 * controls use, so the job carries the same posture (`resolveDesktopDaemonPosture`):
 * a run driven with `CHIRALITY_USER_DATA` installs the job for that userData and
 * a run with `CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL` addresses that label only.
 *
 * `LaunchAgentManager.install()` overwrites the plist unconditionally. Autostart
 * therefore never calls it for an already-installed job, and it refuses to
 * bootstrap a plist whose `ProgramArguments` name a different executable: that
 * plist belongs to another bundle (a second install of the app, a trial copy,
 * or an operator's own job) and starting it from here would launch that other
 * executable under this label. The refusal is logged and returned so a later
 * UI can surface it; it is never thrown.
 */

import path from 'node:path';
import type { LaunchAgentStatus } from '@chirality/runtime-cli';
import type { DesktopLogLevel } from './desktop-log';

/** Opt out of automatic daemon start entirely (verification runs, CI). */
export const SKIP_RUNTIME_AUTOSTART_ENV = 'CHIRALITY_SKIP_RUNTIME_AUTOSTART';

export type RuntimeAutostartLifecycle = {
  install(executablePath: string): Promise<void>;
  start(): Promise<void>;
  status(): Promise<LaunchAgentStatus>;
};

export type RuntimeAutostartStage = 'status' | 'inspect' | 'install' | 'start';

export type RuntimeAutostartOutcome =
  | { action: 'skipped'; reason: 'unpackaged' | 'opted-out' | 'already-loaded' }
  | { action: 'installed-and-started' }
  | { action: 'started' }
  | { action: 'refused'; reason: 'foreign-executable'; installedExecutable: string }
  | { action: 'failed'; stage: RuntimeAutostartStage; error: string };

export type RuntimeAutostartDependencies = {
  lifecycle: RuntimeAutostartLifecycle;
  /** `app.getPath('exe')` of the running bundle. */
  desktopExecutable: string;
  /** `app.isPackaged`; autostart is packaged-only. */
  packaged: boolean;
  /**
   * Bytes of the installed plist, or `undefined` when it cannot be read. Only
   * consulted when `status()` reports the job as installed.
   */
  readInstalledPlist: () => Promise<string | undefined>;
  environment?: Readonly<Record<string, string | undefined>>;
  log: (level: DesktopLogLevel, event: string, detail?: unknown) => void;
};

function unescapeXml(value: string): string {
  return value
    .replaceAll('&lt;', '<')
    .replaceAll('&gt;', '>')
    .replaceAll('&quot;', '"')
    .replaceAll('&apos;', "'")
    .replaceAll('&amp;', '&');
}

/**
 * The executable a rendered LaunchAgent plist would run: the first `<string>`
 * of its `ProgramArguments` array. `undefined` when the plist has no such
 * entry, which a caller must treat as "cannot verify", not as "ours".
 */
export function readLaunchAgentProgramPath(plist: string): string | undefined {
  const match =
    /<key>\s*ProgramArguments\s*<\/key>\s*<array>\s*<string>([^<]*)<\/string>/u.exec(plist);
  if (!match) {
    return undefined;
  }
  const program = unescapeXml(match[1] ?? '').trim();
  return program.length > 0 ? program : undefined;
}

function sameExecutable(installed: string, expected: string): boolean {
  return path.resolve(installed) === path.resolve(expected);
}

function describeError(error: unknown): string {
  return error instanceof Error && error.message.trim() ? error.message : String(error);
}

/**
 * Reconcile the LaunchAgent with the running bundle. Never throws: a daemon
 * that cannot be auto-started must not stop the app from starting, and the
 * binding supervisor keeps retrying regardless of the outcome here.
 *
 * Matrix:
 * - not installed            -> install(exe), start()
 * - installed, not loaded    -> start()   (after the foreign-executable check)
 * - installed, loaded        -> nothing
 * - installed, plist names a different executable -> refused, no start
 */
export async function ensureRuntimeDaemonAutostart(
  deps: RuntimeAutostartDependencies
): Promise<RuntimeAutostartOutcome> {
  const environment = deps.environment ?? process.env;
  if (!deps.packaged) {
    return { action: 'skipped', reason: 'unpackaged' };
  }
  if (environment[SKIP_RUNTIME_AUTOSTART_ENV]?.trim()) {
    deps.log('info', 'runtime.autostart.skipped', { reason: 'opted-out' });
    return { action: 'skipped', reason: 'opted-out' };
  }

  let status: LaunchAgentStatus;
  try {
    status = await deps.lifecycle.status();
  } catch (error) {
    const failure = { stage: 'status' as const, error: describeError(error) };
    deps.log('error', 'runtime.autostart.failed', failure);
    return { action: 'failed', ...failure };
  }
  deps.log('info', 'runtime.autostart.status', {
    installed: status.installed,
    loaded: status.loaded
  });

  if (status.installed) {
    let plist: string | undefined;
    try {
      plist = await deps.readInstalledPlist();
    } catch (error) {
      const failure = { stage: 'inspect' as const, error: describeError(error) };
      deps.log('error', 'runtime.autostart.failed', failure);
      return { action: 'failed', ...failure };
    }
    const installedExecutable = plist === undefined ? undefined : readLaunchAgentProgramPath(plist);
    if (installedExecutable === undefined) {
      // The job exists but its program cannot be verified. Do not start what
      // cannot be identified, and do not overwrite it either.
      const failure = {
        stage: 'inspect' as const,
        error: 'Installed LaunchAgent plist does not name an executable'
      };
      deps.log('error', 'runtime.autostart.failed', failure);
      return { action: 'failed', ...failure };
    }
    if (!sameExecutable(installedExecutable, deps.desktopExecutable)) {
      deps.log('error', 'runtime.autostart.refused_foreign_executable', {
        installedExecutable,
        desktopExecutable: deps.desktopExecutable
      });
      return { action: 'refused', reason: 'foreign-executable', installedExecutable };
    }
    if (status.loaded) {
      return { action: 'skipped', reason: 'already-loaded' };
    }
  } else {
    try {
      await deps.lifecycle.install(deps.desktopExecutable);
      deps.log('info', 'runtime.autostart.installed', {
        desktopExecutable: deps.desktopExecutable
      });
    } catch (error) {
      const failure = { stage: 'install' as const, error: describeError(error) };
      deps.log('error', 'runtime.autostart.failed', failure);
      return { action: 'failed', ...failure };
    }
  }

  try {
    await deps.lifecycle.start();
  } catch (error) {
    const failure = { stage: 'start' as const, error: describeError(error) };
    deps.log('error', 'runtime.autostart.failed', failure);
    return { action: 'failed', ...failure };
  }
  deps.log('info', 'runtime.autostart.started', { installed: status.installed });
  return status.installed ? { action: 'started' } : { action: 'installed-and-started' };
}
