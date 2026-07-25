/**
 * Environment-driven process policy for the desktop main process.
 *
 * `main.ts` applies these decisions before `app.whenReady()` resolves, which is
 * the one place in the app that cannot be exercised from a test. Keeping the
 * decisions here — pure, `electron`-free, taking an explicit environment — makes
 * the rules themselves checkable, and leaves `main.ts` holding only the
 * side effects.
 */

import path from 'node:path';

/**
 * Minimal read-only environment shape. Deliberately not `NodeJS.ProcessEnv`:
 * that type is augmented project-wide with required keys, which would force
 * every caller (and every test) to supply unrelated variables.
 */
export type ProcessPolicyEnvironment = Readonly<Record<string, string | undefined>>;

export type DaemonActivationPolicy = 'regular' | 'accessory' | 'prohibited';

/**
 * Default headless posture for the runtime daemon.
 *
 * `'prohibited'` — "doesn't appear in the Dock and may not create windows or be
 * activated" — is the strongest posture available and is safe for the daemon
 * because it never creates a BrowserWindow. It is what removes the daemon as a
 * target for a LaunchServices activation of `Chirality.app`.
 */
export const DEFAULT_DAEMON_ACTIVATION_POLICY: DaemonActivationPolicy = 'prohibited';

const DAEMON_ACTIVATION_POLICIES: readonly DaemonActivationPolicy[] = [
  'regular',
  'accessory',
  'prohibited'
];

export type UserDataOverride =
  | { kind: 'absent' }
  | { kind: 'apply'; directory: string }
  | { kind: 'rejected'; requested: string; reason: 'not-absolute' };

/**
 * Decide what `CHIRALITY_USER_DATA` should do to this process.
 *
 * A relative value is rejected rather than resolved: launchd starts jobs with
 * `/` as the working directory, so resolving one would silently pick a different
 * directory for the daemon than for a shell-launched app — the exact class of
 * mismatch this variable exists to eliminate.
 */
export function resolveUserDataOverride(
  environment: ProcessPolicyEnvironment = process.env
): UserDataOverride {
  const requested = environment.CHIRALITY_USER_DATA?.trim();
  if (!requested) {
    return { kind: 'absent' };
  }
  if (!path.isAbsolute(requested)) {
    return { kind: 'rejected', requested, reason: 'not-absolute' };
  }
  return { kind: 'apply', directory: path.normalize(requested) };
}

/**
 * Minimum gap between two GUI processes spawned from daemon mode.
 *
 * macOS can deliver several `activate` events for one user gesture (and an
 * impatient operator produces more), so an unthrottled handler could fan out into
 * a pile of windows. Three seconds is long enough to collapse a burst and short
 * enough that a deliberate second launch is not swallowed.
 */
export const GUI_SPAWN_MIN_INTERVAL_MS = 3_000;

/** Disable the daemon's spawn-a-GUI-on-activate behaviour. */
export const DAEMON_GUI_SPAWN_ENV = 'CHIRALITY_DAEMON_GUI_SPAWN';

/**
 * Whether the daemon should start a GUI when macOS resolves a bundle launch
 * against it. Defaults on; `CHIRALITY_DAEMON_GUI_SPAWN=0` turns it off, which is
 * both an operator escape hatch and the control arm for isolating spawn-related
 * behaviour in a verification run.
 */
export function isDaemonGuiSpawnEnabled(
  environment: ProcessPolicyEnvironment = process.env
): boolean {
  const requested = environment[DAEMON_GUI_SPAWN_ENV]?.trim().toLowerCase();
  return !(requested === '0' || requested === 'false' || requested === 'no' || requested === 'off');
}

/**
 * Resolve the daemon's macOS activation policy, allowing an operator or a
 * verification run to compare postures without a rebuild. An unrecognised value
 * falls back to the default rather than failing the daemon's startup.
 */
export function resolveDaemonActivationPolicy(
  environment: ProcessPolicyEnvironment = process.env
): DaemonActivationPolicy {
  const requested = environment.CHIRALITY_DAEMON_ACTIVATION_POLICY?.trim();
  if (
    requested !== undefined &&
    (DAEMON_ACTIVATION_POLICIES as readonly string[]).includes(requested)
  ) {
    return requested as DaemonActivationPolicy;
  }
  return DEFAULT_DAEMON_ACTIVATION_POLICY;
}
