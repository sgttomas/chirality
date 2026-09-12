import React, { useSyncExternalStore } from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { afterEach, beforeEach, expect, it, vi } from 'vitest';
import type { SelectedSessionReplayProjection } from '../../lib/woven-dialogue/contracts';

/**
 * Runtime owns the turn (D-GOV-43 A2); the panel only observes it. Opening a
 * chat with an active turn replays the persisted log, attaches from seq 0 and
 * deduplicates by eventId; a stream that closes without a terminal frame while
 * the turn is still active shows "Reconnecting" (never Idle) and re-attaches
 * after the last sequence it saw; Stop is an explicit interrupt call, not a
 * disconnect; `turn.interrupted` renders the moment it arrives.
 */
const state = vi.hoisted(() => ({ root: '/chosen/subfolder', listeners: new Set<() => void>(),
  create: vi.fn(), boot: vi.fn(), replay: vi.fn(), stream: vi.fn(), attach: vi.fn(), turnState: vi.fn(), interrupt: vi.fn(),
  append: vi.fn(), clear: vi.fn(), hydrate: vi.fn(), streaming: vi.fn(),
  replaceMethods: vi.fn(), resolveContext: vi.fn(), nativeCapability: vi.fn(), nativeRevisions: vi.fn(), nativeClarifications: vi.fn()
}));
vi.mock('next/navigation', () => ({ usePathname: () => '/chat', useSearchParams: () => new URLSearchParams('agent=WORKING_ITEMS'), useRouter: () => ({ replace: vi.fn() }) }));
vi.mock('../../components/workspace/workspace-provider', () => ({ useWorkspace: () => ({
  projectRoot: useSyncExternalStore(listener => { state.listeners.add(listener); return () => state.listeners.delete(listener); }, () => state.root),
  applyProjectRoot: vi.fn(async () => true), chooseProjectRoot: vi.fn(async () => false), hasElectronDirectoryPicker: false, errorMessage: null
}) }));
vi.mock('../../components/workspace/toolkit-provider', () => ({ useToolkit: () => ({ optsPayload: undefined }) }));
vi.mock('../../components/workspace/harness-events-provider', () => ({
  useHarnessEventActions: () => ({ appendEvent: state.append, clearEvents: state.clear, hydrateEvents: state.hydrate, setStreaming: state.streaming }),
  useHarnessEvents: () => ({ events: [], streaming: false })
}));
vi.mock('../../components/shell/runtime-connectivity-provider', () => ({ useRuntimeEpoch: () => 0 }));
vi.mock('../../components/shell/persona-picker', () => ({ PersonaPicker: () => <span>Working Items</span> }));
vi.mock('../../components/shell/file-picker', () => ({ FilePicker: () => null }));
vi.mock('../../components/shell/permission-requests', () => ({ PermissionRequests: () => null }));
vi.mock('../../components/shell/chat-markdown', () => ({ ChatMarkdown: (props: { source: string }) => <p>{props.source}</p> }));
vi.mock('../../lib/harness/method-selection-client', async importOriginal => ({
  ...await importOriginal<typeof import('../../lib/harness/method-selection-client')>(),
  replaceSelectedMethods: state.replaceMethods, resolveSelectedContext: state.resolveContext,
  getNativePlanCapability: state.nativeCapability, listNativePlanRevisions: state.nativeRevisions, listNativePlanClarifications: state.nativeClarifications,
  replyNativePlanClarification: vi.fn(), exportNativePlanRevision: vi.fn()
}));
vi.mock('../../lib/harness/client', async importOriginal => ({ ...await importOriginal<typeof import('../../lib/harness/client')>(),
  createHarnessSession: state.create, bootHarnessSession: state.boot, replaySessionEvents: state.replay, streamHarnessTurn: state.stream,
  attachHarnessTurn: state.attach, getHarnessTurnState: state.turnState, interruptHarnessSession: state.interrupt }));
import { ChatPanel } from '../../components/shell/chat-panel';
import { HarnessApiClientError } from '../../lib/harness/client';

type Frame = { event: string; data: unknown; seq?: number };
const harness = (seq: number, eventId: string, type: string, data: Record<string, unknown> = {}) => ({
  event: 'harness:event', seq, data: { schemaVersion: 1, eventId, sessionId: 'resumed', turnId: 'turn-1', timestamp: '2026-09-12T00:00:00.000Z', type, data }
});
const persisted = (eventId: string, type: string, data: Record<string, unknown> = {}) => ({ schemaVersion: 1, eventId, sessionId: 'resumed', turnId: 'turn-1', timestamp: '2026-09-12T00:00:00.000Z', type, data });

function projection(sessionId: string): SelectedSessionReplayProjection {
  return { selectedSessionId: sessionId, sourceReference: `session:${sessionId}/events`, observedAt: '2026-09-10T00:00:00.000Z', disclosure: 'EMPTY', currency: 'CURRENT',
    transcript: { sessionId, itemCount: 0, items: [] }, instructionHistory: [], instructionBases: [], malformedLineCount: 0, sourceEventCount: 0, renderedItemCount: 0, diagnostics: [],
    session: { projectionId: `operator-session:${sessionId}`, sourceReference: `session:${sessionId}`, sessionId, observedAt: '2026-09-10T00:00:00.000Z', currency: 'CURRENT', runtimeStatus: 'running', parentage: { state: 'NOT_RECORDED' }, diagnostics: [],
      continuation: { schemaVersion: 'chirality.session/v3', projectRoot: '/chosen/subfolder', roleId: 'WORKING_ITEMS', mode: 'CHAT', interactionMode: 'chat', permissionMode: 'workspaceWrite', selectedMethods: [], methodSelectionRevision: 1, instructionBasisId: `basis-${sessionId}` } }
  };
}

let tree: ReactTestRenderer | undefined;
const rendered = () => JSON.stringify(tree!.toJSON());
const status = () => tree!.root.findAllByProps({ className: 'chat-runtime-status' }).map(node => node.children.join('')).join('');
const stopButtons = () => tree!.root.findAllByType('button').filter(node => node.children.join('') === 'Stop');
const flush = async () => { await act(async () => { await Promise.resolve(); await Promise.resolve(); await Promise.resolve(); }); };
async function mountResumed() {
  await act(async () => { tree = create(<ChatPanel presentation="woven" resumeConversation={{ requestId: 1, projection: projection('resumed') }} />); });
  await flush();
}

beforeEach(() => {
  vi.clearAllMocks(); state.listeners.clear();
  vi.stubGlobal('window', { confirm: vi.fn(() => true), requestAnimationFrame: (callback: () => void) => { callback(); return 1; }, setInterval: globalThis.setInterval, clearInterval: globalThis.clearInterval,
    localStorage: { getItem: () => null, setItem: () => undefined, removeItem: () => undefined },
    chirality: { folders: { registerRecent: vi.fn(async () => ({ ok: true })), pathForFile: vi.fn(() => ''), subscribeOpen: () => () => {} } } });
  state.replay.mockResolvedValue({ session: { schemaVersion: 'chirality.session/v3', sessionId: 'resumed' }, events: [] });
  state.turnState.mockResolvedValue({ active: false, lastSeq: 0 });
  state.attach.mockResolvedValue(undefined);
  state.stream.mockResolvedValue(undefined);
  state.interrupt.mockResolvedValue({ ok: true });
  state.resolveContext.mockResolvedValue({ schemaVersion: 'chirality.selected-context/v3', roleId: 'WORKING_ITEMS', methods: [], documents: [], dispositions: [], supplied: [], basisPreview: {}, compatibilityInputs: [], compatibilityMappings: [] });
  state.nativeCapability.mockResolvedValue({ schemaVersion: 'chirality.native-plan-capability/v3', status: 'unavailable', reason: 'fixture' });
  state.nativeRevisions.mockResolvedValue({ schemaVersion: 'chirality.native-plan-revisions/v3', status: 'unavailable', reason: 'fixture', revisions: [] });
  state.nativeClarifications.mockResolvedValue({ schemaVersion: 'chirality.native-plan-clarifications/v3', status: 'unavailable', reason: 'fixture', clarifications: [] });
});
afterEach(() => { if (tree) act(() => tree!.unmount()); tree = undefined; vi.unstubAllGlobals(); vi.useRealTimers(); });

it('leaves an idle session alone: turn state is read once and nothing is attached', async () => {
  await mountResumed();
  expect(state.turnState).toHaveBeenCalledWith('resumed');
  expect(state.attach).not.toHaveBeenCalled();
  expect(state.hydrate).not.toHaveBeenCalled();
  expect(stopButtons()).toHaveLength(0);
});

it('replays the log, attaches from seq 0, deduplicates by eventId and streams message.delta text', async () => {
  state.turnState.mockResolvedValue({ active: true, turnId: 'turn-1', lastSeq: 2, startedAt: '2026-09-12T00:00:00.000Z' });
  state.replay.mockResolvedValue({ session: { schemaVersion: 'chirality.session/v3', sessionId: 'resumed' }, events: [persisted('e1', 'turn.accepted'), persisted('e2', 'message.delta', { text: 'Hel' })] });
  let deliver!: (frame: Frame) => void;
  let finish!: () => void;
  state.attach.mockImplementation((_sessionId: string, _after: number, onEvent: (frame: Frame) => void) => new Promise<void>(resolve => { deliver = onEvent; finish = resolve; }));
  await mountResumed();

  expect(state.hydrate).toHaveBeenCalledWith([expect.objectContaining({ eventId: 'e1' }), expect.objectContaining({ eventId: 'e2' })]);
  expect(state.attach).toHaveBeenCalledWith('resumed', 0, expect.any(Function), expect.any(AbortSignal));
  expect(stopButtons()).toHaveLength(1);
  expect(state.streaming).toHaveBeenLastCalledWith(true);

  // The buffer replays from seq 1: e1 and e2 are already in the log and are not appended twice.
  await act(async () => { deliver(harness(1, 'e1', 'turn.accepted')); deliver(harness(2, 'e2', 'message.delta', { text: 'Hel' })); deliver(harness(3, 'e3', 'message.delta', { text: 'lo' })); });
  expect(state.append.mock.calls.map(call => call[0].eventId)).toEqual(['e3']);
  expect(rendered()).toContain('Hello');

  await act(async () => { deliver(harness(4, 'e4', 'turn.completed')); finish(); });
  await flush();
  expect(stopButtons()).toHaveLength(0);
  expect(state.streaming).toHaveBeenLastCalledWith(false);
  expect(rendered()).toContain('Hello');
});

it('shows Reconnecting, never Idle, when the stream closes on a still-active turn and re-attaches after the last seq', async () => {
  vi.useFakeTimers();
  state.turnState.mockResolvedValue({ active: true, turnId: 'turn-1', lastSeq: 1, startedAt: '2026-09-12T00:00:00.000Z' });
  const attachCalls: Array<{ after: number; deliver: (frame: Frame) => void; finish: () => void }> = [];
  state.attach.mockImplementation((_sessionId: string, after: number, onEvent: (frame: Frame) => void) => new Promise<void>(resolve => { attachCalls.push({ after, deliver: onEvent, finish: resolve }); }));
  await mountResumed();
  expect(attachCalls.map(call => call.after)).toEqual([0]);

  await act(async () => { attachCalls[0].deliver(harness(5, 'e5', 'message.delta', { text: 'partial' })); attachCalls[0].finish(); });
  await flush();
  // The turn is still active according to the Runtime: the panel keeps running and says so.
  expect(status()).toContain('Reconnecting to the running turn');
  expect(stopButtons()).toHaveLength(1);
  expect(attachCalls).toHaveLength(1);

  await act(async () => { await vi.advanceTimersByTimeAsync(1_000); });
  await flush();
  expect(attachCalls.map(call => call.after)).toEqual([0, 5]);

  await act(async () => { attachCalls[1].deliver(harness(6, 'e6', 'message.delta', { text: ' and rest' })); attachCalls[1].deliver(harness(7, 'e7', 'turn.completed')); attachCalls[1].finish(); });
  await flush();
  expect(rendered()).toContain('partial and rest');
  expect(stopButtons()).toHaveLength(0);
  expect(status()).not.toContain('Reconnecting');
});

it('settles from the log when the turn finished while detached, without a reconnect', async () => {
  state.turnState
    .mockResolvedValueOnce({ active: true, turnId: 'turn-1', lastSeq: 1 })
    .mockResolvedValue({ active: false, turnId: 'turn-1', lastSeq: 2, endedAt: '2026-09-12T00:00:05.000Z' });
  state.attach.mockImplementationOnce(async (_s: string, _a: number, onEvent: (frame: Frame) => void) => { onEvent(harness(2, 'e2', 'message.delta', { text: 'done text' })); });
  await mountResumed();
  await flush();
  expect(state.attach).toHaveBeenCalledTimes(1);
  expect(rendered()).toContain('done text');
  expect(status()).not.toContain('Reconnecting');
  expect(stopButtons()).toHaveLength(0);
});

it('treats a 404 TURN_NOT_ACTIVE on re-attach as the turn having ended and reads the outcome from the log', async () => {
  vi.useFakeTimers();
  state.turnState.mockResolvedValue({ active: true, turnId: 'turn-1', lastSeq: 3 });
  state.attach
    .mockImplementationOnce(async (_s: string, _a: number, onEvent: (frame: Frame) => void) => { onEvent(harness(3, 'e3', 'message.delta', { text: 'before drop' })); throw new TypeError('network dropped'); })
    .mockRejectedValueOnce(new HarnessApiClientError(404, 'SESSION_NOT_FOUND', 'No active turn', { reason: 'TURN_NOT_ACTIVE' }));
  state.replay.mockResolvedValue({ session: { schemaVersion: 'chirality.session/v3', sessionId: 'resumed' }, events: [persisted('e3', 'message.delta', { text: 'before drop' }), persisted('e4', 'turn.interrupted')] });
  await mountResumed();
  await flush();
  expect(status()).toContain('Reconnecting to the running turn');
  await act(async () => { await vi.advanceTimersByTimeAsync(1_000); });
  await flush();
  expect(state.attach).toHaveBeenCalledTimes(2);
  expect(state.attach.mock.calls[1][1]).toBe(3);
  expect(rendered()).toContain('before drop');
  expect(rendered()).toContain('"data-turn-outcome":"interrupted"');
  expect(stopButtons()).toHaveLength(0);
});

it('renders turn.interrupted the moment it arrives and Stop calls the interrupt route without closing the stream', async () => {
  state.turnState.mockResolvedValue({ active: true, turnId: 'turn-1', lastSeq: 0 });
  let deliver!: (frame: Frame) => void;
  let finish!: () => void;
  state.attach.mockImplementation((_s: string, _a: number, onEvent: (frame: Frame) => void) => new Promise<void>(resolve => { deliver = onEvent; finish = resolve; }));
  await mountResumed();
  await act(async () => stopButtons()[0].props.onClick());
  expect(state.interrupt).toHaveBeenCalledWith({ sessionId: 'resumed' });
  // Still attached: the interruption is confirmed by the Runtime's own event.
  expect(stopButtons()).toHaveLength(1);
  await act(async () => { deliver(harness(1, 'e1', 'turn.interrupted')); });
  expect(rendered()).toContain('Turn interrupted by operator.');
  await act(async () => { finish(); });
  await flush();
  expect(stopButtons()).toHaveLength(0);
  expect(rendered()).not.toContain('Reconnecting');
});
