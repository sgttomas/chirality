import React from 'react';
import renderer, { act, type ReactTestInstance, type ReactTestRenderer } from 'react-test-renderer';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { RuntimeConnectivitySnapshot } from '../../lib/shell/runtime-connectivity';

/**
 * Coverage for the reconnect refresh: when the main process reports that the
 * runtime daemon is reachable again, the panes that fetched into a dead socket
 * must ask again and drop the error they latched.
 *
 * The defect this pins down was observed in the packaged app: opening it while
 * the daemon was being replaced left the persona picker on
 * "WORKING_ITEMS (unavailable)" and every list on a permanent
 * ENGINE_UNAVAILABLE banner, while the top-bar chip correctly flipped back to
 * "connected". The chip and the panes now read the same signal.
 *
 * Conventions follow `shell-frame-runtime-connectivity.test.tsx`: node
 * environment, react-test-renderer, a fake desktop bridge assigned onto
 * `globalThis.window`, no DOM and no CSS.
 */

const state = vi.hoisted(() => ({
  listDirectChatPersonas: vi.fn(),
  listHarnessSessions: vi.fn(),
  projectRoot: '/tmp/execution-root' as string | null
}));

vi.mock('next/navigation', () => ({
  usePathname: () => '/',
  useRouter: () => ({ replace: vi.fn() }),
  useSearchParams: () => new URLSearchParams()
}));

// The real error formatter and error class are kept: the operator-visible string
// is part of what this test asserts, so faking it would prove nothing.
vi.mock('../../lib/harness/client', async (importOriginal) => {
  const original = await importOriginal<typeof import('../../lib/harness/client')>();
  return {
    ...original,
    listDirectChatPersonas: state.listDirectChatPersonas,
    listHarnessSessions: state.listHarnessSessions
  };
});

vi.mock('../../components/workspace/workspace-provider', () => ({
  useWorkspace: () => ({ projectRoot: state.projectRoot })
}));

vi.mock('../../components/workspace/harness-events-provider', () => ({
  useHarnessEventActions: () => ({ hydrateEvents: vi.fn() }),
  useHarnessStreaming: () => false
}));

import { HarnessApiClientError } from '../../lib/harness/client';
import { PersonaPicker } from '../../components/shell/persona-picker';
import {
  RuntimeConnectivityProvider,
  useRuntimeEpoch
} from '../../components/shell/runtime-connectivity-provider';
import { SessionListView } from '../../components/shell/session-list-view';

// The repo compiles JSX with the classic transform, so component modules that do
// not import React themselves resolve `React.createElement` off the global.
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

function engineUnavailable(): HarnessApiClientError {
  return new HarnessApiClientError(503, 'ENGINE_UNAVAILABLE', DAEMON_UNBOUND);
}

type BridgeHarness = {
  push: (next: RuntimeConnectivitySnapshot) => void;
};

function installBridge(initial: RuntimeConnectivitySnapshot | null): BridgeHarness {
  const listeners = new Set<(value: RuntimeConnectivitySnapshot) => void>();
  Object.assign(globalThis, {
    window: {
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

function EpochProbe(): JSX.Element {
  return <span data-runtime-epoch={useRuntimeEpoch()} />;
}

async function render(node: React.ReactElement): Promise<ReactTestRenderer> {
  let tree!: ReactTestRenderer;
  await act(async () => {
    tree = renderer.create(node);
  });
  // The provider hydrates from an async bridge query; let it settle so the
  // assertions below describe a steady state rather than a race.
  await act(async () => {});
  return tree;
}

async function pushSnapshot(
  bridge: BridgeHarness,
  next: RuntimeConnectivitySnapshot
): Promise<void> {
  await act(async () => {
    bridge.push(next);
  });
  await act(async () => {});
}

function epochOf(tree: ReactTestRenderer): number {
  const probe = tree.root.findAll(
    (node) => typeof node.props['data-runtime-epoch'] === 'number'
  )[0];
  return probe?.props['data-runtime-epoch'] as number;
}

function textOf(node: ReactTestInstance): string {
  return node.children
    .map((child) => (typeof child === 'string' ? child : textOf(child)))
    .join('');
}

function textByClass(tree: ReactTestRenderer, className: string): string[] {
  return tree.root
    .findAll((node) =>
      typeof node.props.className === 'string'
        ? node.props.className.split(/\s+/).includes(className)
        : false
    )
    .map((node) => textOf(node));
}

function optionTexts(tree: ReactTestRenderer): string[] {
  return tree.root.findAllByType('option').map((option) => textOf(option));
}

describe('persona roster refresh on runtime reconnect', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    state.projectRoot = '/tmp/execution-root';
  });

  afterEach(() => {
    delete (globalThis as { window?: unknown }).window;
  });

  it('re-fetches once and drops the stale error when the daemon comes back', async () => {
    const bridge = installBridge(snapshot({ state: 'disconnected', lastError: 'socket refused' }));
    state.listDirectChatPersonas
      .mockRejectedValueOnce(engineUnavailable())
      .mockResolvedValue([{ name: 'HELP_HUMAN', type: 0 }]);

    const tree = await render(
      <RuntimeConnectivityProvider>
        <EpochProbe />
        <PersonaPicker />
      </RuntimeConnectivityProvider>
    );

    // The reported symptom, reproduced: an unusable picker and a banner that
    // nothing in the renderer would ever clear.
    expect(epochOf(tree)).toBe(0);
    expect(state.listDirectChatPersonas).toHaveBeenCalledTimes(1);
    expect(textByClass(tree, 'persona-picker-error')).toEqual([
      `ENGINE_UNAVAILABLE: ${DAEMON_UNBOUND}`
    ]);
    expect(optionTexts(tree)).toEqual(['WORKING_ITEMS (unavailable)']);

    await pushSnapshot(bridge, snapshot({ changedAt: '2026-07-25T12:00:05.000Z' }));

    expect(epochOf(tree)).toBe(1);
    expect(state.listDirectChatPersonas).toHaveBeenCalledTimes(2);
    expect(textByClass(tree, 'persona-picker-error')).toEqual([]);
    expect(optionTexts(tree)).toEqual(['WORKING_ITEMS (unavailable)', 'HELP_HUMAN · Type 0']);
  });

  it('does not re-fetch when the main process repeats a connected report', async () => {
    const bridge = installBridge(snapshot({ state: 'disconnected' }));
    state.listDirectChatPersonas.mockResolvedValue([{ name: 'HELP_HUMAN', type: 0 }]);

    const tree = await render(
      <RuntimeConnectivityProvider>
        <EpochProbe />
        <PersonaPicker />
      </RuntimeConnectivityProvider>
    );
    await pushSnapshot(bridge, snapshot({ changedAt: '2026-07-25T12:00:05.000Z' }));
    expect(state.listDirectChatPersonas).toHaveBeenCalledTimes(2);

    // The main process owns retry and backoff and may re-publish liveness; only
    // an actual transition is a reason to ask the API again.
    await pushSnapshot(bridge, snapshot({ changedAt: '2026-07-25T12:00:15.000Z' }));
    await pushSnapshot(bridge, snapshot({ changedAt: '2026-07-25T12:00:25.000Z' }));

    expect(epochOf(tree)).toBe(1);
    expect(state.listDirectChatPersonas).toHaveBeenCalledTimes(2);
  });

  it('does not re-fetch when the daemon merely drops out', async () => {
    const bridge = installBridge(snapshot({ state: 'connected' }));
    state.listDirectChatPersonas.mockResolvedValue([{ name: 'HELP_HUMAN', type: 0 }]);

    const tree = await render(
      <RuntimeConnectivityProvider>
        <EpochProbe />
        <PersonaPicker />
      </RuntimeConnectivityProvider>
    );
    expect(state.listDirectChatPersonas).toHaveBeenCalledTimes(1);

    await pushSnapshot(
      bridge,
      snapshot({ state: 'disconnected', failedAttempts: 1, lastError: 'gone' })
    );

    expect(epochOf(tree)).toBe(0);
    expect(state.listDirectChatPersonas).toHaveBeenCalledTimes(1);
  });

  it('leaves a pane rendered without the provider exactly as it was', async () => {
    // Most suites render one pane in isolation. Those panes must keep fetching
    // once and only once, with no bridge subscription of their own.
    const bridge = installBridge(snapshot({ state: 'disconnected' }));
    state.listDirectChatPersonas.mockResolvedValue([{ name: 'HELP_HUMAN', type: 0 }]);

    await render(<PersonaPicker />);
    expect(state.listDirectChatPersonas).toHaveBeenCalledTimes(1);

    await pushSnapshot(bridge, snapshot({ changedAt: '2026-07-25T12:00:05.000Z' }));

    expect(state.listDirectChatPersonas).toHaveBeenCalledTimes(1);
  });
});

describe('session list refresh on runtime reconnect', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    state.projectRoot = '/tmp/execution-root';
  });

  afterEach(() => {
    delete (globalThis as { window?: unknown }).window;
  });

  it('re-lists once and replaces the stale error with the recorded sessions', async () => {
    const bridge = installBridge(snapshot({ state: 'connecting' }));
    state.listHarnessSessions.mockRejectedValueOnce(engineUnavailable()).mockResolvedValue([
      {
        sessionId: 'session-1',
        projectRoot: '/tmp/execution-root',
        persona: 'WORKING_ITEMS',
        mode: 'CHAT',
        createdAt: '2026-07-25T11:59:00.000Z'
      }
    ]);

    const tree = await render(
      <RuntimeConnectivityProvider>
        <EpochProbe />
        <SessionListView />
      </RuntimeConnectivityProvider>
    );

    expect(state.listHarnessSessions).toHaveBeenCalledTimes(1);
    expect(textByClass(tree, 'panel-error')).toEqual([
      `ENGINE_UNAVAILABLE: ${DAEMON_UNBOUND}`
    ]);
    expect(tree.root.findAll((node) => node.props.className === 'session-list-item')).toHaveLength(
      0
    );

    // `connecting` → `connected` is the packaged-app case: the panes mounted
    // while the very first bind was still in flight.
    await pushSnapshot(bridge, snapshot({ changedAt: '2026-07-25T12:00:05.000Z' }));

    expect(epochOf(tree)).toBe(1);
    expect(state.listHarnessSessions).toHaveBeenCalledTimes(2);
    expect(state.listHarnessSessions).toHaveBeenLastCalledWith('/tmp/execution-root');
    expect(textByClass(tree, 'panel-error')).toEqual([]);
    expect(tree.root.findAll((node) => node.props.className === 'session-list-item')).toHaveLength(
      1
    );
  });

  it('does not call the API on reconnect while no Working Root is selected', async () => {
    state.projectRoot = null;
    const bridge = installBridge(snapshot({ state: 'disconnected' }));
    state.listHarnessSessions.mockResolvedValue([]);

    await render(
      <RuntimeConnectivityProvider>
        <SessionListView />
      </RuntimeConnectivityProvider>
    );
    await pushSnapshot(bridge, snapshot({ changedAt: '2026-07-25T12:00:05.000Z' }));

    expect(state.listHarnessSessions).not.toHaveBeenCalled();
  });
});
