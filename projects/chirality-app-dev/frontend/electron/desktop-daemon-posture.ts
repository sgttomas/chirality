/**
 * The one place that decides Chirality Desktop's LaunchAgent posture.
 *
 * Two surfaces install the daemon's job: the in-app runtime panel (through
 * `createDesktopDaemonLifecycle()`) and the documented `chirality daemon install`
 * command run from the generated `~/.local/bin/chirality` launcher. Stage V
 * proved those two had drifted — the CLI path rendered the historical
 * `crash-only` plist with no pinned environment, silently reinstating the very
 * defect the in-app install fixes. They now read the same values from here: the
 * lifecycle passes them to `LaunchAgentManager`, and the launcher exports them so
 * a CLI invocation resolves the identical posture through
 * `resolveRuntimeLaunchAgentOptions()`.
 *
 * `@chirality/runtime-cli` stays generic per D-GOV-20: it owns the option names
 * and the environment-variable contract; the project-specific *values* are chosen
 * here, in the caller.
 *
 * `electron`-free and environment-injectable so the values are checkable in a
 * test rather than only observable in a packaged run.
 */

import {
  RUNTIME_LAUNCH_AGENT_ENV,
  RUNTIME_LAUNCH_AGENT_LABEL,
  RUNTIME_USER_DATA_ENV,
  type LaunchAgentKeepAlivePolicy
} from '@chirality/runtime-cli';

export type DaemonPostureEnvironment = Readonly<Record<string, string | undefined>>;

/**
 * Restart posture for the desktop daemon.
 *
 * `always` (`KeepAlive <true/>`), not the package default `crash-only`
 * (`{SuccessfulExit: false}`): the observed termination was a *clean* `exit(0)`,
 * which a successful-exit semaphore contractually refuses to restart. With the
 * quit veto removed (V-D1/V-D5), this restart contract is the whole of the
 * stay-dead fix — a polite quit now shuts the daemon down gracefully and launchd
 * brings it straight back.
 */
export const DESKTOP_KEEP_ALIVE_POLICY: LaunchAgentKeepAlivePolicy = 'always';

export type DesktopDaemonPosture = {
  label: string;
  keepAlive: LaunchAgentKeepAlivePolicy;
  runAtLoad: true;
  userDataDirectory: string;
};

/**
 * Resolve the effective posture. Only `label` is environment-overridable, so an
 * isolated verification run can install a parallel job without ever naming the
 * operator's real one; the restart contract itself is not a per-run choice.
 */
export function resolveDesktopDaemonPosture(
  environment: DaemonPostureEnvironment,
  userDataDirectory: string
): DesktopDaemonPosture {
  const label = environment[RUNTIME_LAUNCH_AGENT_ENV.label]?.trim();
  return {
    label: label || RUNTIME_LAUNCH_AGENT_LABEL,
    keepAlive: DESKTOP_KEEP_ALIVE_POLICY,
    runAtLoad: true,
    userDataDirectory
  };
}

/**
 * The environment a `chirality` CLI invocation needs in order to reproduce this
 * posture. The generated launcher exports each of these *conditionally*, so an
 * externally supplied value still wins and an isolated run is never silently
 * redirected at the real job or the real runtime directory.
 */
export function daemonPostureEnvironment(
  posture: DesktopDaemonPosture
): Record<string, string> {
  return {
    [RUNTIME_USER_DATA_ENV]: posture.userDataDirectory,
    [RUNTIME_LAUNCH_AGENT_ENV.label]: posture.label,
    [RUNTIME_LAUNCH_AGENT_ENV.keepAlive]: posture.keepAlive
  };
}
