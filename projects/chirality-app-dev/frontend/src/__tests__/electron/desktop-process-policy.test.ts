import { describe, expect, it } from 'vitest';
import {
  DEFAULT_DAEMON_ACTIVATION_POLICY,
  GUI_SPAWN_MIN_INTERVAL_MS,
  isDaemonGuiSpawnEnabled,
  resolveDaemonActivationPolicy,
  resolveUserDataOverride
} from '../../../electron/desktop-process-policy';

describe('resolveUserDataOverride', () => {
  it('reports absent when the variable is unset or blank', () => {
    expect(resolveUserDataOverride({})).toEqual({ kind: 'absent' });
    expect(resolveUserDataOverride({ CHIRALITY_USER_DATA: '' })).toEqual({ kind: 'absent' });
    expect(resolveUserDataOverride({ CHIRALITY_USER_DATA: '   ' })).toEqual({
      kind: 'absent'
    });
  });

  it('applies an absolute directory', () => {
    expect(
      resolveUserDataOverride({
        CHIRALITY_USER_DATA: '/Users/tester/Library/Application Support/chirality-frontend'
      })
    ).toEqual({
      kind: 'apply',
      directory: '/Users/tester/Library/Application Support/chirality-frontend'
    });
  });

  it('trims surrounding whitespace before applying', () => {
    expect(resolveUserDataOverride({ CHIRALITY_USER_DATA: '  /tmp/isolated-user-data  ' })).toEqual(
      { kind: 'apply', directory: '/tmp/isolated-user-data' }
    );
  });

  it('normalises redundant separators without changing the target', () => {
    expect(resolveUserDataOverride({ CHIRALITY_USER_DATA: '/tmp//iso/./data' })).toEqual({
      kind: 'apply',
      directory: '/tmp/iso/data'
    });
  });

  it('rejects a relative value instead of resolving it against an unknown cwd', () => {
    // launchd runs jobs from `/`, so resolving a relative value would point the
    // daemon at a different directory than a shell-launched app.
    expect(resolveUserDataOverride({ CHIRALITY_USER_DATA: 'relative/user-data' })).toEqual({
      kind: 'rejected',
      requested: 'relative/user-data',
      reason: 'not-absolute'
    });
    expect(resolveUserDataOverride({ CHIRALITY_USER_DATA: './data' })).toEqual({
      kind: 'rejected',
      requested: './data',
      reason: 'not-absolute'
    });
    expect(resolveUserDataOverride({ CHIRALITY_USER_DATA: '~/Library/Chirality' })).toEqual({
      kind: 'rejected',
      requested: '~/Library/Chirality',
      reason: 'not-absolute'
    });
  });
});

describe('resolveDaemonActivationPolicy', () => {
  it('defaults to the headless prohibited posture', () => {
    expect(DEFAULT_DAEMON_ACTIVATION_POLICY).toBe('prohibited');
    expect(resolveDaemonActivationPolicy({})).toBe('prohibited');
  });

  it('accepts every documented policy so postures can be compared', () => {
    for (const policy of ['regular', 'accessory', 'prohibited'] as const) {
      expect(
        resolveDaemonActivationPolicy({ CHIRALITY_DAEMON_ACTIVATION_POLICY: policy })
      ).toBe(policy);
    }
  });

  it('falls back to the default rather than failing on an unknown value', () => {
    expect(
      resolveDaemonActivationPolicy({ CHIRALITY_DAEMON_ACTIVATION_POLICY: 'headless' })
    ).toBe('prohibited');
    expect(resolveDaemonActivationPolicy({ CHIRALITY_DAEMON_ACTIVATION_POLICY: '' })).toBe(
      'prohibited'
    );
  });

  it('tolerates surrounding whitespace for the activation policy', () => {
    expect(
      resolveDaemonActivationPolicy({ CHIRALITY_DAEMON_ACTIVATION_POLICY: ' accessory ' })
    ).toBe('accessory');
  });
});

describe('isDaemonGuiSpawnEnabled', () => {
  it('is on by default so a double-click opens the app', () => {
    expect(isDaemonGuiSpawnEnabled({})).toBe(true);
    expect(isDaemonGuiSpawnEnabled({ CHIRALITY_DAEMON_GUI_SPAWN: '' })).toBe(true);
    expect(isDaemonGuiSpawnEnabled({ CHIRALITY_DAEMON_GUI_SPAWN: '1' })).toBe(true);
  });

  it('accepts the documented off spellings', () => {
    for (const value of ['0', 'false', 'no', 'OFF', ' off ']) {
      expect(isDaemonGuiSpawnEnabled({ CHIRALITY_DAEMON_GUI_SPAWN: value })).toBe(false);
    }
  });

  it('rate-limits GUI launches on a human-scale interval', () => {
    // One user gesture can produce several `activate` events; the throttle has to
    // be long enough to collapse a burst into one launch.
    expect(GUI_SPAWN_MIN_INTERVAL_MS).toBeGreaterThanOrEqual(1_000);
    expect(GUI_SPAWN_MIN_INTERVAL_MS).toBeLessThanOrEqual(10_000);
  });
});
