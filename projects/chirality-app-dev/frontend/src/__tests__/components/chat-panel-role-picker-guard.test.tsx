import React, { useSyncExternalStore } from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

// SCA-APP-012 (DEL-08-02): the role picker in the chat context row is the live
// role-selection guard. It is disabled while a turn runs and enabled otherwise.
// Hermetic ChatPanel pattern from chat-panel-model-selectors.test.tsx; the
// picker is stubbed so the test reads exactly what ChatPanel passes to it.
const state = vi.hoisted(() => ({ root: '/chosen/subfolder', query: '', listeners: new Set<() => void>(),
  create: vi.fn(), boot: vi.fn(), replay: vi.fn(), stream: vi.fn(), apply: vi.fn(), append: vi.fn(), clear: vi.fn(), hydrate: vi.fn(), streaming: vi.fn(), turnState: vi.fn(), attach: vi.fn(),
  replaceMethods: vi.fn(), resolveContext: vi.fn(),
  nativeCapability: vi.fn(), nativeRevisions: vi.fn(), nativeClarifications: vi.fn()
}));
vi.mock('next/navigation', () => ({ usePathname: () => '/chat', useSearchParams: () => new URLSearchParams(state.query), useRouter: () => ({ replace: vi.fn() }) }));
vi.mock('../../components/workspace/workspace-provider', () => ({ useWorkspace: () => ({
  projectRoot: useSyncExternalStore(listener => { state.listeners.add(listener); return () => state.listeners.delete(listener); }, () => state.root),
  applyProjectRoot: state.apply, chooseProjectRoot: vi.fn(async () => false), hasElectronDirectoryPicker: false, errorMessage: null
}) }));
vi.mock('../../components/workspace/toolkit-provider', () => ({ useToolkit: () => ({ optsPayload: undefined }) }));
vi.mock('../../components/workspace/harness-events-provider', () => ({ useHarnessEventActions: () => ({ appendEvent: state.append, clearEvents: state.clear, hydrateEvents: state.hydrate, setStreaming: state.streaming }), useHarnessEvents: () => ({ events: [], streaming: false }) }));
vi.mock('../../components/shell/runtime-connectivity-provider', () => ({ useRuntimeEpoch: () => 0 }));
vi.mock('../../components/shell/persona-picker', () => ({
  PersonaPicker: ({ compact, disabled }: { compact?: boolean; disabled?: boolean }) => (
    <span data-role-picker="true" data-compact={String(Boolean(compact))} data-disabled={String(Boolean(disabled))}>Working Items</span>
  )
}));
vi.mock('../../components/shell/file-picker', () => ({ FilePicker: () => null }));
vi.mock('../../components/shell/permission-requests', () => ({ PermissionRequests: () => null }));
vi.mock('../../components/shell/chat-markdown', () => ({ ChatMarkdown: (props: { source: string }) => <p>{props.source}</p> }));
vi.mock('../../lib/harness/method-selection-client', async importOriginal => ({
  ...await importOriginal<typeof import('../../lib/harness/method-selection-client')>(),
  replaceSelectedMethods: state.replaceMethods,
  resolveSelectedContext: state.resolveContext,
  getNativePlanCapability: state.nativeCapability,
  listNativePlanRevisions: state.nativeRevisions,
  listNativePlanClarifications: state.nativeClarifications
}));
vi.mock('../../lib/harness/client', async importOriginal => ({ ...await importOriginal<typeof import('../../lib/harness/client')>(), createHarnessSession: state.create, bootHarnessSession: state.boot, replaySessionEvents: state.replay, streamHarnessTurn: state.stream, interruptHarnessSession: vi.fn(), getHarnessTurnState: state.turnState, attachHarnessTurn: state.attach }));
import { ChatPanel } from '../../components/shell/chat-panel';

let tree: ReactTestRenderer | undefined;
let values: Map<string, string>;

async function mount(): Promise<void> {
  await act(async () => { tree = create(<ChatPanel presentation="woven" />); });
}
async function type(value: string): Promise<void> {
  await act(async () => { tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.onChange({ target: { value } }); });
}
async function submit(): Promise<void> {
  await act(async () => { tree!.root.findByType('form').props.onSubmit({ preventDefault: vi.fn() }); });
}
function rolePicker(): { compact: string; disabled: string } {
  const node = tree!.root.findByProps({ 'data-role-picker': 'true' });
  return { compact: node.props['data-compact'], disabled: node.props['data-disabled'] };
}

beforeEach(() => {
  vi.clearAllMocks(); state.root = '/chosen/subfolder'; state.query = 'agent=WORKING_ITEMS'; state.listeners.clear();
  values = new Map();
  vi.stubGlobal('window', { confirm: vi.fn(() => true), requestAnimationFrame: (callback: () => void) => { callback(); return 1; }, setInterval: globalThis.setInterval, clearInterval: globalThis.clearInterval,
    localStorage: { getItem: (key: string) => values.get(key) ?? null, setItem: (key: string, value: string) => { values.set(key, value); }, removeItem: (key: string) => values.delete(key) },
    chirality: { folders: { registerRecent: vi.fn(async () => ({ ok: true })), pathForFile: vi.fn(() => ''), subscribeOpen: () => () => {} } } });
  state.create.mockResolvedValue({ sessionId: 'bound', engineSelection: { adapterId: 'codex-app-server', providerId: 'openai', model: 'gpt-default' } });
  state.boot.mockResolvedValue({ session: { schemaVersion: 'chirality.session/v3', sessionId: 'bound', projectRoot: '/chosen/subfolder', engineSelection: { adapterId: 'codex-app-server', providerId: 'openai', model: 'gpt-default' },
    selectedMethods: [], methodSelectionRevision: 0, instructionBasisId: 'basis-1' } });
  state.replay.mockRejectedValue(new Error('No replay fixture'));
  state.replaceMethods.mockResolvedValue({ schemaVersion: 'chirality.selected-methods/v3', sessionId: 'bound', revision: 1, methods: [], basisPreview: { id: 'basis-1' }, transition: { status: 'unchanged', successorAvailable: false } });
  state.resolveContext.mockResolvedValue({ schemaVersion: 'chirality.selected-context/v3', roleId: 'WORKING_ITEMS', methods: [], documents: [], dispositions: [], supplied: [], basisPreview: {}, compatibilityInputs: [], compatibilityMappings: [] });
  state.nativeCapability.mockResolvedValue({ schemaVersion: 'chirality.native-plan-capability/v3', status: 'unavailable', reason: 'fixture' });
  state.nativeRevisions.mockResolvedValue({ schemaVersion: 'chirality.native-plan-revisions/v3', status: 'unavailable', reason: 'fixture', revisions: [] });
  state.nativeClarifications.mockResolvedValue({ schemaVersion: 'chirality.native-plan-clarifications/v3', status: 'unavailable', reason: 'fixture', clarifications: [] });
  state.apply.mockImplementation(async () => true);
  state.stream.mockResolvedValue(undefined);
  state.turnState.mockResolvedValue({ active: false, lastSeq: 0 });
  state.attach.mockResolvedValue(undefined);
});
afterEach(() => { if (tree) act(() => tree!.unmount()); tree = undefined; vi.unstubAllGlobals(); });

describe('ChatPanel role picker guard', () => {
  it('enables the role picker while no turn is running', async () => {
    await mount();
    expect(rolePicker()).toEqual({ compact: 'true', disabled: 'false' });
  });

  it('disables the role picker while a turn runs and re-enables it when the turn ends', async () => {
    let finish!: () => void;
    state.stream.mockImplementation(() => new Promise<void>(resolve => { finish = resolve; }));
    await mount();
    expect(rolePicker().disabled).toBe('false');

    await type('hold the turn open'); await submit();
    expect(state.stream).toHaveBeenCalledTimes(1);
    expect(rolePicker().disabled).toBe('true');

    await act(async () => { finish(); await Promise.resolve(); await Promise.resolve(); });
    await act(async () => { await Promise.resolve(); });
    expect(rolePicker().disabled).toBe('false');
  });
});
