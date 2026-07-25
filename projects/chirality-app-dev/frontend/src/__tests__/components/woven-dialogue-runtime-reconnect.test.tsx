import React from 'react';
import renderer, { act, type ReactTestRenderer } from 'react-test-renderer';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { RuntimeConnectivitySnapshot } from '../../lib/shell/runtime-connectivity';
import type { SelectedSessionReplayState } from '../../lib/woven-dialogue/contracts';

/**
 * Reconnect coverage for the woven shell — the surface the operator actually
 * opens. Two stale-state paths live here: the recorded-session list that feeds
 * both the Navigator's mode groups and the Coordination panel, and a replay lens
 * left showing UNAVAILABLE.
 *
 * `woven-dialogue-shell.test.tsx` renders this shell to static markup for
 * composition; this file drives it with react-test-renderer because the behaviour
 * under test is entirely in effects.
 */

const state = vi.hoisted(() => ({
  listHarnessSessions: vi.fn(),
  replayLoad: vi.fn(),
  replayCancel: vi.fn(),
  replayDispose: vi.fn(),
  replayListeners: new Set<(next: unknown) => void>()
}));

vi.mock('next/navigation', () => ({
  usePathname: () => '/',
  useSearchParams: () => new URLSearchParams()
}));
vi.mock('next/link', () => ({
  default: ({ children, ...props }: React.AnchorHTMLAttributes<HTMLAnchorElement>) =>
    React.createElement('a', props, children)
}));

vi.mock('../../lib/harness/client', () => ({
  listHarnessSessions: state.listHarnessSessions,
  replaySessionEvents: vi.fn(),
  harnessApiErrorMessage: (error: unknown) =>
    error instanceof Error ? error.message : String(error)
}));

// The loader is faked rather than the network beneath it: the shell's contract
// here is "ask the loader to load again", and a fake makes the published
// UNAVAILABLE state directly settable.
vi.mock('../../lib/woven-dialogue/selected-session-replay', () => ({
  createSelectedSessionReplayLoader: () => ({
    getState: () => ({ status: 'IDLE' }),
    subscribe: (listener: (next: unknown) => void) => {
      state.replayListeners.add(listener);
      return () => {
        state.replayListeners.delete(listener);
      };
    },
    load: state.replayLoad,
    cancel: state.replayCancel,
    dispose: state.replayDispose
  })
}));

vi.mock('../../components/workspace/workspace-provider', () => ({
  useWorkspace: () => ({ projectRoot: '/repo/projects/chirality-app-dev' })
}));
vi.mock('../../components/workspace/harness-events-provider', () => ({
  useHarnessStreaming: () => false
}));
vi.mock('../../components/shell/shell-frame', () => ({
  ShellFrame: ({ children }: { children: React.ReactNode }) => <div>{children}</div>
}));
vi.mock('../../components/shell/chat-panel', () => ({
  ChatPanel: () => <div data-chat-panel="mounted" />
}));
vi.mock('../../components/shell/persona-picker', () => ({
  PersonaPicker: () => <div data-persona-picker="mounted" />
}));
vi.mock('../../components/shell/file-tree-panel', () => ({
  FileTreePanel: () => <div data-file-tree="mounted" />
}));
vi.mock('../../components/shell/document-view', () => ({
  DocumentView: () => <div data-document-view="mounted" />
}));
vi.mock('../../components/workbench/workbench-surface', () => ({
  WorkbenchSurface: () => <div data-workbench-surface="mounted" />
}));
vi.mock('../../components/pipeline/pipeline-surface', () => ({
  PipelineSurface: () => <div data-pipeline-surface="mounted" />
}));
vi.mock('../../components/woven-dialogue/coordination-panel', () => ({
  CoordinationPanel: ({ sessionsError }: { sessionsError: string | null }) => (
    <div data-coordination-panel="mounted" data-sessions-error={sessionsError ?? ''} />
  )
}));
vi.mock('../../components/woven-dialogue/activity-shelf', () => ({
  ActivityShelf: () => <div data-activity-shelf="mounted" />
}));
vi.mock('../../components/woven-dialogue/selected-session-replay-lens', () => ({
  SelectedSessionReplayLens: () => <div data-replay-lens="mounted" />
}));

import { RuntimeConnectivityProvider } from '../../components/shell/runtime-connectivity-provider';
import { WovenDialogueShell } from '../../components/woven-dialogue/woven-dialogue-shell';

Object.assign(globalThis, { React });

const DAEMON_UNBOUND = 'Chirality runtime daemon client is not configured';

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

/**
 * The shell reads `localStorage` and installs pointer listeners on mount, so the
 * fake window carries those alongside the connectivity bridge.
 */
function installWindow(initial: RuntimeConnectivitySnapshot | null): {
  push: (next: RuntimeConnectivitySnapshot) => void;
} {
  const listeners = new Set<(value: RuntimeConnectivitySnapshot) => void>();
  const store = new Map<string, string>();
  Object.assign(globalThis, {
    window: {
      localStorage: {
        getItem: (key: string) => store.get(key) ?? null,
        setItem: (key: string, value: string) => {
          store.set(key, value);
        },
        removeItem: (key: string) => {
          store.delete(key);
        }
      },
      addEventListener: () => undefined,
      removeEventListener: () => undefined,
      chirality: {
        runtime: {
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

function publishReplayState(next: SelectedSessionReplayState): void {
  for (const listener of state.replayListeners) {
    listener(next);
  }
}

async function renderShell(): Promise<ReactTestRenderer> {
  let tree!: ReactTestRenderer;
  await act(async () => {
    tree = renderer.create(
      <RuntimeConnectivityProvider>
        <WovenDialogueShell defaultSurface="dialogue" />
      </RuntimeConnectivityProvider>
    );
  });
  await act(async () => {});
  return tree;
}

function coordinationError(tree: ReactTestRenderer): string {
  return tree.root.findByProps({ 'data-coordination-panel': 'mounted' }).props[
    'data-sessions-error'
  ] as string;
}

describe('WovenDialogueShell runtime reconnect refresh', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    state.replayListeners.clear();
  });

  afterEach(() => {
    delete (globalThis as { window?: unknown }).window;
  });

  it('re-lists recorded sessions once and clears the error the panels showed', async () => {
    const bridge = installWindow(snapshot({ state: 'disconnected', lastError: 'socket refused' }));
    state.listHarnessSessions
      .mockRejectedValueOnce(new Error(`ENGINE_UNAVAILABLE: ${DAEMON_UNBOUND}`))
      .mockResolvedValue([
        {
          sessionId: 'session-1',
          projectRoot: '/repo/projects/chirality-app-dev',
          persona: 'WORKING_ITEMS',
          mode: 'CHAT',
          createdAt: '2026-07-25T11:59:00.000Z'
        }
      ]);

    const tree = await renderShell();
    expect(state.listHarnessSessions).toHaveBeenCalledTimes(1);
    expect(coordinationError(tree)).toBe(`ENGINE_UNAVAILABLE: ${DAEMON_UNBOUND}`);

    await act(async () => {
      bridge.push(snapshot({ changedAt: '2026-07-25T12:00:05.000Z' }));
    });
    await act(async () => {});

    expect(state.listHarnessSessions).toHaveBeenCalledTimes(2);
    expect(coordinationError(tree)).toBe('');

    // Liveness re-published without a transition is not a reason to re-list.
    await act(async () => {
      bridge.push(snapshot({ changedAt: '2026-07-25T12:00:15.000Z' }));
    });
    await act(async () => {});
    expect(state.listHarnessSessions).toHaveBeenCalledTimes(2);
  });

  it('reloads a replay lens that was left unavailable', async () => {
    const bridge = installWindow(snapshot({ state: 'disconnected' }));
    state.listHarnessSessions.mockResolvedValue([]);

    const tree = await renderShell();
    await act(async () => {
      publishReplayState({
        status: 'UNAVAILABLE',
        selectedSessionId: 'session-7',
        message: `ENGINE_UNAVAILABLE: ${DAEMON_UNBOUND}`
      });
    });
    expect(tree.root.findAllByProps({ 'data-replay-lens': 'mounted' })).toHaveLength(1);
    expect(state.replayLoad).not.toHaveBeenCalled();

    await act(async () => {
      bridge.push(snapshot({ changedAt: '2026-07-25T12:00:05.000Z' }));
    });
    await act(async () => {});

    expect(state.replayLoad).toHaveBeenCalledTimes(1);
    expect(state.replayLoad.mock.calls[0]?.[0]).toBe('session-7');
  });

  it('leaves an idle replay lens alone on reconnect', async () => {
    const bridge = installWindow(snapshot({ state: 'disconnected' }));
    state.listHarnessSessions.mockResolvedValue([]);

    await renderShell();
    await act(async () => {
      bridge.push(snapshot({ changedAt: '2026-07-25T12:00:05.000Z' }));
    });
    await act(async () => {});

    // Nothing was selected, so there is nothing to recover; a reconnect must not
    // open a lens the operator never asked for.
    expect(state.replayLoad).not.toHaveBeenCalled();
  });
});
