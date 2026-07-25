import React from 'react';
import renderer, { act, type ReactTestRenderer } from 'react-test-renderer';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { RuntimeConnectivitySnapshot } from '../../lib/shell/runtime-connectivity';
import { RuntimeConnectivityProvider } from '../../components/shell/runtime-connectivity-provider';
import { RuntimeSettings } from '../../components/settings/runtime-settings';

/**
 * The Runtime & credentials panel is the operator's diagnostic, and its entire
 * content is a claim about the daemon. Probed once at mount, that claim froze at
 * "daemon: not running" for the rest of the session; it is now re-probed when the
 * main process reports the daemon is reachable again.
 */

Object.assign(globalThis, { React });

const daemonStatus = vi.fn();
const modelStatus = vi.fn();

function snapshot(
  overrides: Partial<RuntimeConnectivitySnapshot> = {}
): RuntimeConnectivitySnapshot {
  return {
    state: 'connected',
    failedAttempts: 0,
    lastError: null,
    changedAt: '2026-07-25T12:00:00.000Z',
    ...overrides
  };
}

function installBridge(initial: RuntimeConnectivitySnapshot | null): {
  push: (next: RuntimeConnectivitySnapshot) => void;
} {
  const listeners = new Set<(value: RuntimeConnectivitySnapshot) => void>();
  Object.assign(globalThis, {
    window: {
      chirality: {
        runtime: {
          daemon: {
            status: daemonStatus,
            install: vi.fn(),
            start: vi.fn(),
            stop: vi.fn(),
            uninstall: vi.fn()
          },
          models: { status: modelStatus, activate: vi.fn() },
          connectivity: {
            get: async () => initial,
            subscribe: (listener: (value: RuntimeConnectivitySnapshot) => void) => {
              listeners.add(listener);
              return () => {
                listeners.delete(listener);
              };
            }
          }
        }
      }
    }
  });
  return {
    push: (next) => {
      for (const listener of listeners) {
        listener(next);
      }
    }
  };
}

describe('RuntimeSettings re-probe on runtime reconnect', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    delete (globalThis as { window?: unknown }).window;
  });

  it('re-probes the daemon exactly once per reconnect', async () => {
    const bridge = installBridge(snapshot({ state: 'disconnected' }));
    daemonStatus.mockResolvedValue({
      ok: true,
      launchAgent: { installed: true, loaded: true },
      daemon: { running: false }
    });

    let tree!: ReactTestRenderer;
    await act(async () => {
      tree = renderer.create(
        <RuntimeConnectivityProvider>
          <RuntimeSettings />
        </RuntimeConnectivityProvider>
      );
    });
    await act(async () => {});
    expect(daemonStatus).toHaveBeenCalledTimes(1);

    daemonStatus.mockResolvedValue({
      ok: true,
      launchAgent: { installed: true, loaded: true },
      daemon: { running: true, pid: 4242 }
    });
    modelStatus.mockResolvedValue({
      ok: true,
      residency: {
        phase: 'NO_MODEL',
        activeTurns: 0,
        acceptingLocalTurns: true,
        models: []
      }
    });

    await act(async () => {
      bridge.push(snapshot({ changedAt: '2026-07-25T12:00:05.000Z' }));
    });
    await act(async () => {});

    expect(daemonStatus).toHaveBeenCalledTimes(2);
    expect(modelStatus).toHaveBeenCalledTimes(1);

    // A repeated connected report is not a transition.
    await act(async () => {
      bridge.push(snapshot({ changedAt: '2026-07-25T12:00:15.000Z' }));
    });
    await act(async () => {});
    expect(daemonStatus).toHaveBeenCalledTimes(2);

    tree.unmount();
  });
});
