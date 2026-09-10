import React, { useSyncExternalStore } from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { beforeEach, afterEach, expect, it, vi } from 'vitest';
import { buildChatDraftStorageKey } from '/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/lib/harness/chat-draft';
import type { QualifiedMethodReference } from '/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/lib/harness/method-selection-client';
import type { SelectedSessionReplayProjection } from '/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/lib/woven-dialogue/contracts';

const state = vi.hoisted(() => ({ root: '/chosen/subfolder', query: '', listeners: new Set<() => void>(),
  create: vi.fn(), boot: vi.fn(), stream: vi.fn(), apply: vi.fn(), append: vi.fn(), clear: vi.fn(), streaming: vi.fn(),
  replaceMethods: vi.fn(), resolveContext: vi.fn(),
  nativeCapability: vi.fn(), nativeRevisions: vi.fn(), replay: vi.fn(),
  markdownProps: [] as Array<{ source: string; projectRoot?: string | null; fileCatalog?: readonly string[]; onOpenFile?: (path: string) => void }>,
  nativeListener: undefined as ((intent: { path?: string; error?: string }) => void) | undefined
}));
vi.mock('next/navigation', () => ({ usePathname: () => '/chat', useSearchParams: () => new URLSearchParams(state.query), useRouter: () => ({ replace: vi.fn() }) }));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/components/workspace/workspace-provider', () => ({ useWorkspace: () => ({
  projectRoot: useSyncExternalStore(listener => { state.listeners.add(listener); return () => state.listeners.delete(listener); }, () => state.root),
  applyProjectRoot: state.apply, chooseProjectRoot: vi.fn(async () => false), hasElectronDirectoryPicker: false, errorMessage: null
}) }));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/components/workspace/toolkit-provider', () => ({ useToolkit: () => ({ optsPayload: undefined }) }));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/components/workspace/harness-events-provider', () => ({ useHarnessEventActions: () => ({ appendEvent: state.append, clearEvents: state.clear, setStreaming: state.streaming }) }));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/components/shell/runtime-connectivity-provider', () => ({ useRuntimeEpoch: () => 0 }));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/components/shell/persona-picker', () => ({ PersonaPicker: () => <span>Working Items</span> }));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/components/shell/file-picker', () => ({ FilePicker: ({ onAddAttachments }: { onAddAttachments: (items: Array<{ path: string; displayName: string; clientType: 'text' }>) => void }) => <button data-add-attachment onClick={() => onAddAttachments([{ path: '/chosen/subfolder/docs/input.txt', displayName: 'input.txt', clientType: 'text' }])}>add fixture attachment</button> }));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/components/shell/permission-requests', () => ({ PermissionRequests: () => null }));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/components/shell/chat-markdown', () => ({ ChatMarkdown: (props: { source: string; projectRoot?: string | null; fileCatalog?: readonly string[]; onOpenFile?: (path: string) => void }) => { state.markdownProps.push(props); return <p>{props.source}</p>; } }));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/lib/harness/method-selection-client', async importOriginal => ({
  ...await importOriginal<typeof import('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/lib/harness/method-selection-client')>(),
  replaceSelectedMethods: state.replaceMethods,
  resolveSelectedContext: state.resolveContext,
  getNativePlanCapability: state.nativeCapability,
  listNativePlanRevisions: state.nativeRevisions
}));
vi.mock('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/lib/harness/client', async importOriginal => ({ ...await importOriginal<typeof import('/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/lib/harness/client')>(), createHarnessSession: state.create, bootHarnessSession: state.boot, streamHarnessTurn: state.stream, replaySessionEvents: state.replay, interruptHarnessSession: vi.fn() }));
import { ChatPanel } from '/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/src/components/shell/chat-panel';

let tree: ReactTestRenderer | undefined;
let values: Map<string, string>;
let writes: [string, string][];
const canonicalKey = buildChatDraftStorageKey('/canonical', 'WORKING_ITEMS', 'CHAT');
const canonicalDraft = JSON.stringify({ draft: 'Unrelated canonical draft', attachments: [] });
function root(value: string) { state.root = value; for (const listener of state.listeners) listener(); }
function deferred<T>() { let resolve!: (value: T) => void; const promise = new Promise<T>(done => { resolve = done; }); return { promise, resolve }; }
async function mount(props: Partial<React.ComponentProps<typeof ChatPanel>> = {}) { await act(async () => { tree = create(<ChatPanel presentation="woven" {...props} />); }); }
async function type(value: string) { await act(async () => { tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.onChange({ target: { value } }); }); }
async function submit() { await act(async () => { tree!.root.findByType('form').props.onSubmit({ preventDefault: vi.fn() }); }); }
function assertCanonicalUntouched() { expect(values.get(canonicalKey)).toBe(canonicalDraft); expect(writes.filter(([key]) => key === canonicalKey)).toEqual([]); }
function resumableProjection(sessionId: string): SelectedSessionReplayProjection {
  return { selectedSessionId: sessionId, sourceReference: `session:${sessionId}/events`, observedAt: '2026-09-09T00:00:00.000Z', disclosure: 'EMPTY', currency: 'CURRENT',
    transcript: { sessionId, itemCount: 0, items: [] }, instructionHistory: [], instructionBases: [], malformedLineCount: 0, sourceEventCount: 0, renderedItemCount: 0, diagnostics: [],
    session: { projectionId: `operator-session:${sessionId}`, sourceReference: `session:${sessionId}`, sessionId, observedAt: '2026-09-09T00:00:00.000Z', currency: 'CURRENT', runtimeStatus: 'idle', parentage: { state: 'NOT_RECORDED' }, diagnostics: [],
      continuation: { schemaVersion: 'chirality.session/v3', projectRoot: '/chosen/subfolder', roleId: 'WORKING_ITEMS', mode: 'CHAT', interactionMode: 'chat', permissionMode: 'ask', selectedMethods: [], methodSelectionRevision: 1, instructionBasisId: `basis-${sessionId}` } }
  };
}
beforeEach(() => {
  vi.clearAllMocks(); state.root = '/chosen/subfolder'; state.query = 'agent=WORKING_ITEMS'; state.listeners.clear(); state.nativeListener = undefined;
  state.markdownProps = [];
  values = new Map([[canonicalKey, canonicalDraft]]); writes = [];
  vi.stubGlobal('window', { confirm: vi.fn(() => true), localStorage: { getItem: (key: string) => values.get(key) ?? null, setItem: (key: string, value: string) => { writes.push([key, value]); values.set(key, value); }, removeItem: (key: string) => values.delete(key) }, chirality: { folders: {
    registerRecent: vi.fn(async () => ({ ok: true })), pathForFile: vi.fn(() => ''), subscribeOpen: (listener: typeof state.nativeListener) => { state.nativeListener = listener; return () => { state.nativeListener = undefined; }; }
  } } });
  state.create.mockResolvedValue({ sessionId: 'bound' });
  state.boot.mockResolvedValue({ session: { sessionId: 'bound', projectRoot: '/canonical' } });
  state.replaceMethods.mockImplementation(async (_sessionId: string, methods: QualifiedMethodReference[] | undefined) => ({ schemaVersion: 'chirality.selected-methods/v3', sessionId: 'bound', revision: 1, methods: methods ?? [], basisPreview: { id: 'basis-1' }, transition: { status: 'unchanged', successorAvailable: false } }));
  state.resolveContext.mockResolvedValue({ schemaVersion: 'chirality.selected-context/v3', roleId: 'HELP_HUMAN', methods: [], documents: [], dispositions: [], supplied: [], basisPreview: {}, compatibilityInputs: [], compatibilityMappings: [] });
  state.nativeCapability.mockResolvedValue({ schemaVersion: 'chirality.native-plan-capability/v3', status: 'unavailable', reason: 'fixture' });
  state.nativeRevisions.mockResolvedValue({ schemaVersion: 'chirality.native-plan-revisions/v3', status: 'unavailable', reason: 'fixture', revisions: [] });
  state.apply.mockImplementation(async (value: string) => { root(value); return true; });
  state.stream.mockRejectedValue(new Error('Fixture turn failure')); state.replay.mockResolvedValue({instructionHistory:[],instructionBases:[]});
});
afterEach(() => { if (tree) act(() => tree!.unmount()); tree = undefined; vi.unstubAllGlobals(); });

it('uses the returned canonical root without migrating or overwriting either conversation draft', async () => {
  const pending = deferred<boolean>(); state.stream.mockImplementation(() => pending.promise);
  await mount(); await type('Keep my failed prompt'); await submit();
  expect(state.root).toBe('/canonical'); assertCanonicalUntouched();
  expect(tree!.root.findByProps({ className: 'chat-folder-fixed' }).props.title).toBe('/canonical');
  await act(async () => pending.resolve(false));
  await type('Second prompt'); state.stream.mockRejectedValue(new Error('Failed again')); await submit();
  expect(state.create).toHaveBeenCalledTimes(1); expect(state.boot).toHaveBeenCalledTimes(1);
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('Second prompt');
  assertCanonicalUntouched();
});
it('retains the actual binding and failed draft when provider synchronization refuses', async () => {
  state.apply.mockResolvedValue(false); const binding = vi.fn();
  await mount({ onBindingChange: binding }); await type('Keep this prompt'); await submit();
  expect(state.root).toBe('/chosen/subfolder'); expect(binding).toHaveBeenLastCalledWith({ root: '/canonical', locked: true });
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('Keep this prompt');
  expect(JSON.stringify(tree!.toJSON())).toContain('file browsing could not switch'); assertCanonicalUntouched();
});
it('rejects a stale boot result after an unrelated folder change without restoring its old draft', async () => {
  const boot = deferred<unknown>(); state.boot.mockReturnValue(boot.promise);
  await mount(); await type('Old context prompt'); await submit();
  await act(async () => root('/other'));
  await act(async () => boot.resolve({ session: { sessionId: 'old', projectRoot: '/canonical' } }));
  expect(state.apply).not.toHaveBeenCalled(); expect(state.stream).not.toHaveBeenCalled();
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).not.toBe('Old context prompt'); assertCanonicalUntouched();
});
it('rejects a stale synchronization completion after a different folder transition', async () => {
  const applied = deferred<boolean>(); state.apply.mockReturnValue(applied.promise);
  await mount(); await type('Old context prompt'); await submit();
  await act(async () => root('/other'));
  await act(async () => applied.resolve(false));
  expect(state.stream).not.toHaveBeenCalled();
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).not.toBe('Old context prompt'); assertCanonicalUntouched();
});
it('blocks native folder intent while bound or pending and blocks Send during pending selection', async () => {
  await mount({ folderSelectionPending: true }); await type('Pending'); await submit();
  expect(state.create).not.toHaveBeenCalled();
  await act(async () => state.nativeListener?.({ path: '/native-folder' })); expect(state.apply).not.toHaveBeenCalled();
  await act(async () => tree!.update(<ChatPanel presentation="woven" folderSelectionPending={false} />));
  await submit(); const calls = state.apply.mock.calls.length;
  await act(async () => state.nativeListener?.({ path: '/native-folder' })); expect(state.apply).toHaveBeenCalledTimes(calls);
});
it('keeps Enter submission distinct from Shift+Enter and IME composition', async () => {
  await mount(); const submit = vi.fn(); const preventDefault = vi.fn(); const handler = tree!.root.findByType('textarea').props.onKeyDown;
  handler({ key: 'Enter', shiftKey: true, nativeEvent: { isComposing: false }, preventDefault, currentTarget: { form: { requestSubmit: submit } } });
  handler({ key: 'Enter', shiftKey: false, nativeEvent: { isComposing: true }, preventDefault, currentTarget: { form: { requestSubmit: submit } } });
  expect(submit).not.toHaveBeenCalled();
  handler({ key: 'Enter', shiftKey: false, nativeEvent: { isComposing: false }, preventDefault, currentTarget: { form: { requestSubmit: submit } } });
  expect(submit).toHaveBeenCalledTimes(1); expect(preventDefault).toHaveBeenCalledTimes(1);
});

it('captures only the first prompt after a session boots successfully', async () => {
  state.stream.mockResolvedValue(undefined);
  const captured = vi.fn();
  await mount({ onSessionBootedPrompt: captured });
  await type('First prompt'); await submit();
  expect(captured).toHaveBeenCalledWith({ sessionId: 'bound', prompt: 'First prompt', persona: 'WORKING_ITEMS' });
  await type('Second prompt'); await submit();
  expect(captured).toHaveBeenCalledTimes(1);
  expect(state.create).toHaveBeenCalledTimes(1);
  expect(state.boot).toHaveBeenCalledTimes(1);
});

it('merges next-message methods into the active basis without sending turn-time overrides', async () => {
  const method = { kind: 'workflow' as const, name: 'project-setup', source: 'bundled' as const, sourceRootId: 'chirality-root' };
  values.set(buildChatDraftStorageKey('/chosen/subfolder', 'WORKING_ITEMS', 'CHAT'), JSON.stringify({ draft: '', attachments: [], methods: [method] }));
  state.stream.mockResolvedValue(undefined);
  state.nativeCapability.mockResolvedValue({ schemaVersion: 'chirality.native-plan-capability/v3', status: 'qualified', qualification: { adapterId: 'fixture', providerId: 'fixture', qualificationId: 'qualified-fixture', admissionSha256: 'a'.repeat(64), evidenceClass: 'native-adapter-qualified' } });
  function Fixture() {
    const [methods, setMethods] = React.useState<QualifiedMethodReference[]>([method]);
    return <ChatPanel presentation="woven" selectedMethods={methods} onSelectedMethodsChange={setMethods} />;
  }
  await act(async () => { tree = create(<Fixture />); });
  await type('First selected message'); await submit();
  expect(state.stream).toHaveBeenLastCalledWith(expect.objectContaining({ interactionMode: 'chat', permissionMode: 'ask' }), expect.any(Function));
  expect(state.stream.mock.calls.at(-1)?.[0]).not.toHaveProperty('methods');
  expect(state.replaceMethods).toHaveBeenLastCalledWith('bound', [method], { boundaryConfirmed: true, selectionMode: 'merge' });
  expect(tree!.root.findAllByProps({ 'aria-label': 'Methods for next turn' })).toHaveLength(0);

  await act(async () => tree!.root.findByProps({ 'aria-label': 'Interaction mode' }).props.onChange({ target: { value: 'native-plan' } }));
  await type('Second message'); await submit();
  expect(state.stream).toHaveBeenLastCalledWith(expect.objectContaining({ interactionMode: 'native-plan', permissionMode: 'ask' }), expect.any(Function));
  expect(state.stream.mock.calls.at(-1)?.[0]).not.toHaveProperty('methods');
  expect(state.replaceMethods).toHaveBeenCalledTimes(1);
});

it('preserves methods selected for the next message while the current turn finishes', async () => {
  const pending = deferred<void>();
  state.stream.mockImplementation(() => pending.promise);
  const method = { kind: 'workflow' as const, name: 'research-orchestration', source: 'bundled' as const, sourceRootId: 'chirality-root' };
  let select!: (methods: QualifiedMethodReference[]) => void;
  function Fixture() {
    const [methods, setMethods] = React.useState<QualifiedMethodReference[]>([]);
    select = setMethods;
    return <ChatPanel presentation="woven" selectedMethods={methods} onSelectedMethodsChange={setMethods} />;
  }
  await act(async () => { tree = create(<Fixture />); });
  await type('Current turn'); await submit();
  await act(async () => select([method]));
  expect(tree!.root.findAllByProps({ 'aria-label': 'Methods for next turn' })).toHaveLength(1);
  await act(async () => pending.resolve());
  expect(tree!.root.findAllByProps({ 'aria-label': 'Methods for next turn' })).toHaveLength(1);
});

it('rejects empty and multiple-file drops without invoking folder validation', async () => {
  await mount(); const drop = tree!.root.findByType('form').props.onDrop;
  await act(async () => drop({ preventDefault: vi.fn(), dataTransfer: { files: [] } }));
  await act(async () => drop({ preventDefault: vi.fn(), dataTransfer: { files: [{}, {}] } }));
  await act(async () => drop({ preventDefault: vi.fn(), dataTransfer: { files: [{}] } }));
  expect(state.apply).not.toHaveBeenCalled();
  expect(JSON.stringify(tree!.toJSON())).toContain('Drop a folder');
});

it.each([true, false])('retains conversation binding across an Agent change (provider sync %s), until New chat', async (sync) => {
  state.stream.mockResolvedValue(undefined);
  if (!sync) state.apply.mockResolvedValue(false);
  const binding = vi.fn();
  await mount({ onBindingChange: binding }); await type('First completed turn'); await submit();
  state.query = 'agent=HELPS_HUMANS';
  await act(async () => tree!.update(<ChatPanel presentation="woven" onBindingChange={binding} />));
  expect(JSON.stringify(tree!.toJSON())).toContain('First completed turn');
  expect(binding).toHaveBeenLastCalledWith({ root: '/canonical', locked: true });
  expect(tree!.root.findByProps({ className: 'chat-folder-fixed' }).props.title).toBe('/canonical');
  const calls = state.apply.mock.calls.length;
  await act(async () => state.nativeListener?.({ path: '/native-other' }));
  const bridge = (window as unknown as { chirality: { folders: { pathForFile: ReturnType<typeof vi.fn> } } }).chirality.folders;
  bridge.pathForFile.mockReturnValue('/drop-other');
  await act(async () => tree!.root.findByType('form').props.onDrop({ preventDefault: vi.fn(), dataTransfer: { files: [{}] } }));
  expect(state.apply).toHaveBeenCalledTimes(calls);
  await type('Second agent turn'); await submit();
  expect(state.create).toHaveBeenCalledTimes(1);
  expect(state.replaceMethods).toHaveBeenLastCalledWith('bound', undefined, { roleId: 'HELPS_HUMANS', boundaryConfirmed: true });
  expect(binding).toHaveBeenLastCalledWith({ root: '/canonical', locked: true });
  assertCanonicalUntouched();
  await act(async () => tree!.update(<ChatPanel presentation="woven" onBindingChange={binding} newChatRequest={1} />));
  expect(binding).toHaveBeenLastCalledWith({ root: state.root, locked: false });
  expect(JSON.stringify(tree!.toJSON())).not.toContain('First completed turn');
});
it('changes roles at a confirmed boundary without booting another App session', async () => {
  state.stream.mockResolvedValue(undefined); state.apply.mockResolvedValue(false);
  const binding = vi.fn(); await mount({ onBindingChange: binding }); await type('Original turn'); await submit();
  state.query = 'agent=HELPS_HUMANS';
  await act(async () => tree!.update(<ChatPanel presentation="woven" onBindingChange={binding} />));
  await type('Continue in one chat'); await submit();
  expect(state.stream).toHaveBeenCalledTimes(2);
  expect(state.create).toHaveBeenCalledTimes(1);
  expect(state.boot).toHaveBeenCalledTimes(1);
  expect(state.replaceMethods).toHaveBeenLastCalledWith('bound', undefined, { roleId: 'HELPS_HUMANS', boundaryConfirmed: true });
  expect(binding).toHaveBeenLastCalledWith({ root: '/canonical', locked: true });
  expect(JSON.stringify(tree!.toJSON())).toContain('Original turn');
  assertCanonicalUntouched();
});

it('keeps the unsent draft under the bound conversation when its role changes', async () => {
  state.stream.mockResolvedValue(undefined);
  await mount(); await type('First completed turn'); await submit();
  await type('Unsent next instruction');
  state.query = 'agent=HELPS_HUMANS';
  await act(async () => tree!.update(<ChatPanel presentation="woven" />));
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('Unsent next instruction');
});

it('continues a compatible recorded v3 conversation without creating or booting another session', async () => {
  state.stream.mockResolvedValue(undefined);
  const activeMethod = { kind: 'workflow' as const, name: 'project-setup', source: 'bundled' as const, sourceRootId: 'chirality-root' };
  const projection = {
    selectedSessionId: 'recorded-v3', sourceReference: 'session:recorded-v3/events', observedAt: '2026-09-09T00:00:00.000Z',
    disclosure: 'READY_SNAPSHOT', currency: 'CURRENT', malformedLineCount: 0, sourceEventCount: 2, renderedItemCount: 2, diagnostics: [],
    transcript: { sessionId: 'recorded-v3', itemCount: 2, items: [
      { key: 'old-user', kind: 'message', role: 'user', status: 'completed', title: 'You', timestamp: '2026-09-09T00:00:00.000Z', eventId: 'event-1', eventType: 'message.completed', text: 'Earlier question' },
      { key: 'old-answer', kind: 'message', role: 'assistant', status: 'completed', title: 'Assistant', timestamp: '2026-09-09T00:00:01.000Z', eventId: 'event-2', eventType: 'message.completed', text: 'Earlier answer' }
    ] }, instructionHistory: [], instructionBases: [],
    session: { projectionId: 'operator-session:recorded-v3', sourceReference: 'session:recorded-v3', sessionId: 'recorded-v3', observedAt: '2026-09-09T00:00:02.000Z', currency: 'CURRENT', runtimeStatus: 'completed', parentage: { state: 'NOT_RECORDED' }, diagnostics: [], continuation: {
      schemaVersion: 'chirality.session/v3', projectRoot: '/chosen/subfolder', roleId: 'WORKING_ITEMS', mode: 'CHAT', interactionMode: 'chat', permissionMode: 'ask', selectedMethods: [activeMethod], methodSelectionRevision: 2, instructionBasisId: 'basis-2'
    } }
  } satisfies SelectedSessionReplayProjection;
  const resumed = vi.fn();
  await mount({ resumeConversation: { requestId: 1, projection }, onConversationResumed: resumed });
  expect(resumed).toHaveBeenCalledWith('recorded-v3');
  expect(JSON.stringify(tree!.toJSON())).toContain('Earlier question');
  expect(JSON.stringify(tree!.toJSON())).toContain('Earlier answer');
  await type('Continue here'); await submit();
  expect(state.create).not.toHaveBeenCalled();
  expect(state.boot).not.toHaveBeenCalled();
  expect(state.replaceMethods).not.toHaveBeenCalled();
  expect(state.resolveContext).toHaveBeenCalledWith(expect.objectContaining({ sessionId: 'recorded-v3', methods: [activeMethod] }));
  expect(state.stream).toHaveBeenCalledWith(expect.objectContaining({ sessionId: 'recorded-v3', message: 'Continue here' }), expect.any(Function));
  expect(state.stream.mock.calls.at(-1)?.[0]).not.toHaveProperty('methods');
});

it('keeps unsent drafts isolated between recorded conversations with the same root and role', async () => {
  values.set(buildChatDraftStorageKey('/chosen/subfolder', 'session:recorded-b', 'CHAT'), JSON.stringify({ draft: 'Draft for B', attachments: [], methods: [] }));
  await mount({ resumeConversation: { requestId: 1, projection: resumableProjection('recorded-a') } });
  await type('Draft for A');
  expect(JSON.parse(values.get(buildChatDraftStorageKey('/chosen/subfolder', 'session:recorded-a', 'CHAT'))!).draft).toBe('Draft for A');
  await act(async () => tree!.update(<ChatPanel presentation="woven" resumeConversation={{ requestId: 2, projection: resumableProjection('recorded-b') }} />));
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('Draft for B');
  expect(JSON.parse(values.get(buildChatDraftStorageKey('/chosen/subfolder', 'session:recorded-a', 'CHAT'))!).draft).toBe('Draft for A');
});

it('does not resurrect a sent unbound draft when a new chat starts with the same root and role', async () => {
  const entryKey = buildChatDraftStorageKey('/chosen/subfolder', 'WORKING_ITEMS', 'CHAT');
  values.set(entryKey, JSON.stringify({ draft: 'Send this once', attachments: [], methods: [] }));
  state.boot.mockResolvedValue({ session: { sessionId: 'same-root', projectRoot: '/chosen/subfolder' } });
  state.stream.mockResolvedValue(undefined);
  await mount();
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('Send this once');
  await submit();
  expect(values.has(entryKey)).toBe(false);
  await act(async () => tree!.update(<ChatPanel presentation="woven" newChatRequest={1} />));
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('');
});

it('keeps retained assistant speaker labels and titles tied to their originating Agent', async () => {
  state.stream.mockResolvedValue(undefined);
  await mount(); await type('First agent'); await submit();
  const speakers = () => tree!.root.findAllByProps({ className: 'chat-speaker' }).filter(node => node.props.title);
  expect(speakers().map(node => [node.props.title, node.children.join('')])).toEqual([
    ['WORKING_ITEMS', 'Working Items'], ['WORKING_ITEMS', 'Working Items']
  ]);
  state.query = 'agent=HELPS_HUMANS';
  await act(async () => tree!.update(<ChatPanel presentation="woven" />));
  await type('Second agent'); await submit();
  expect(speakers().map(node => [node.props.title, node.children.join('')])).toEqual([
    ['WORKING_ITEMS', 'Working Items'], ['WORKING_ITEMS', 'Working Items'], ['HELPS_HUMANS', 'Helps Humans']
  ]);
});

it('captures first input and paste before parent restoration, and delays restoration during IME', async () => {
  const restored = vi.fn();
  function Fixture() {
    const [expanded, setExpanded] = React.useState(true);
    return <section data-expanded={expanded}><ChatPanel presentation="woven" onDraftCaptured={() => { restored(); setExpanded(false); }} /></section>;
  }
  await act(async () => { tree = create(<Fixture />); });
  const input = tree!.root.findByType('textarea');
  await act(async () => input.props.onChange({ target: { value: 'a' }, nativeEvent: { isComposing: false } }));
  expect(tree!.root.findByType('textarea')).toBe(input);
  expect(input.props.value).toBe('a'); expect(tree!.root.findByType('section').props['data-expanded']).toBe(false);
  await act(async () => input.props.onChange({ target: { value: 'a pasted text' }, nativeEvent: { inputType: 'insertFromPaste', isComposing: false } }));
  expect(input.props.value).toBe('a pasted text');
  const calls = restored.mock.calls.length;
  await act(async () => input.props.onChange({ target: { value: 'あ' }, nativeEvent: { isComposing: true } }));
  expect(input.props.value).toBe('あ'); expect(restored).toHaveBeenCalledTimes(calls);
  await act(async () => input.props.onCompositionEnd({ currentTarget: { value: 'あい' } }));
  expect(input.props.value).toBe('あい'); expect(restored).toHaveBeenCalledTimes(calls + 1);
  expect(tree!.root.findByType('textarea')).toBe(input);
});

it('keeps legacy session creation and draft storage aligned with a changed Working Root', async () => {
  state.stream.mockResolvedValue(undefined);
  state.root = '/root-a';
  state.boot.mockResolvedValue({ session: { sessionId: 'a', projectRoot: '/root-a' } });
  const keyA = buildChatDraftStorageKey('/root-a', 'session:a', 'CHAT');
  const keyB = buildChatDraftStorageKey('/root-b', 'WORKING_ITEMS', 'CHAT');
  values.set(keyB, JSON.stringify({ draft: 'Saved root B prompt', attachments: [] }));
  await mount({ presentation: undefined }); await type('Completed root A turn'); await submit();
  await type('Unsent root A prompt');
  expect(JSON.parse(values.get(keyA)!).draft).toBe('Unsent root A prompt');
  await act(async () => root('/root-b'));
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('Saved root B prompt');
  state.boot.mockResolvedValue({ session: { sessionId: 'b', projectRoot: '/root-b' } });
  await submit();
  expect(state.create).toHaveBeenLastCalledWith({ projectRoot: '/root-b', persona: 'WORKING_ITEMS', roleId: 'WORKING_ITEMS', mode: 'CHAT', interactionMode: 'chat', permissionMode: 'ask', selectedMethods: [] });
  expect(state.create).toHaveBeenCalledTimes(2);
  expect(JSON.parse(values.get(keyA)!).draft).toBe('Unsent root A prompt');
  expect(values.has(keyB)).toBe(false);
});

it('threads file navigation only to assistant Markdown and preserves attachment payload and failure restoration', async () => {
  const open = vi.fn();
  const catalog = ['/chosen/subfolder/docs/SPEC.md'];
  await mount({ fileCatalog: catalog, onOpenFile: open });
  expect(state.markdownProps.at(-1)).toMatchObject({ source: 'What would you like to work on?', fileCatalog: catalog, onOpenFile: open });
  expect(state.markdownProps.at(-1)?.projectRoot).toBeUndefined();
  await act(async () => tree!.root.findByProps({ 'data-add-attachment': true }).props.onClick());
  await type('Keep attachment');
  await submit();
  expect(state.stream).toHaveBeenCalledWith(expect.objectContaining({
    message: 'Keep attachment',
    attachments: ['/chosen/subfolder/docs/input.txt']
  }), expect.any(Function));
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('Keep attachment');
  expect(tree!.root.findAllByProps({ className: 'attachment-chip' }).some(node => node.props.title === '/chosen/subfolder/docs/input.txt')).toBe(true);
  expect(state.markdownProps.every(props => props.fileCatalog === catalog && props.onOpenFile === open)).toBe(true);
});

it('keeps retained assistant Markdown bound to the root that produced it', async () => {
  state.stream.mockImplementation(async (_input, onEvent) => { onEvent({ event: 'chat:complete', data: { text: '[spec](docs/SPEC.md)' } }); });
  state.boot.mockResolvedValue({ session: { sessionId: 'bound', projectRoot: '/chosen/subfolder' } });
  await mount({ fileCatalog: ['/chosen/subfolder/docs/SPEC.md'], onOpenFile: vi.fn() });
  await type('Create a link'); await submit();
  expect(state.markdownProps.at(-1)?.projectRoot).toBe('/chosen/subfolder');
  await act(async () => root('/other'));
  await act(async () => tree!.update(<ChatPanel presentation="woven" fileCatalog={['/other/docs/SPEC.md']} onOpenFile={vi.fn()} />));
  expect(state.markdownProps.at(-1)).toMatchObject({ projectRoot: '/chosen/subfolder', fileCatalog: ['/other/docs/SPEC.md'] });
  act(() => tree!.unmount()); tree = undefined;
  state.markdownProps = [];
  await mount({ fileCatalog: ['/other/docs/SPEC.md'], onOpenFile: vi.fn() });
  expect(state.markdownProps.at(-1)?.projectRoot).toBeUndefined();
});

it('successor: retains method-bearing first-message draft after a post-boot rejection', async () => {
 const method = {kind:'workflow' as const,name:'research-orchestration',source:'bundled' as const,sourceRootId:'chirality-root'};
 values.set(buildChatDraftStorageKey('/chosen/subfolder','WORKING_ITEMS','CHAT'),JSON.stringify({draft:'Retry this instruction',attachments:[],methods:[method]}));
 function Fixture(){const [methods,setMethods]=React.useState<QualifiedMethodReference[]>([]);return <ChatPanel presentation="woven" selectedMethods={methods} onSelectedMethodsChange={setMethods}/>;}
 await act(async()=>{tree=create(<Fixture/>);});
 expect(tree!.root.findAllByProps({'aria-label':'Methods for next turn'})).toHaveLength(1);
 await submit();
 expect(tree!.root.findByProps({'aria-label':'Chat input'}).props.value).toBe('Retry this instruction');
 expect(tree!.root.findAllByProps({'aria-label':'Methods for next turn'})).toHaveLength(1);
});
it('successor: adopts Runtime method revision after agent method changes during a turn', async()=>{
 const agentMethod={kind:'skill' as const,name:'agent-method',source:'bundled' as const,sourceRootId:'chirality-root'};
 const userMethod={...agentMethod,name:'user-method'};
 const projection=resumableProjection('recorded-agent-method');
 state.stream.mockResolvedValue(undefined);
 state.replay.mockResolvedValue({instructionHistory:[],instructionBases:[{basisId:'basis-2',selectedMethods:[agentMethod],suppliedEntries:[]}],session:{schemaVersion:'chirality.session/v3',methodSelectionRevision:2,instructionBasisId:'basis-2',selectedMethods:[agentMethod]}});
 let select!:(methods:QualifiedMethodReference[])=>void;
 function Fixture(){const [methods,setMethods]=React.useState<QualifiedMethodReference[]>([]);select=setMethods;return <ChatPanel presentation="woven" selectedMethods={methods} onSelectedMethodsChange={setMethods} resumeConversation={{requestId:1,projection}}/>;}
 await act(async()=>{tree=create(<Fixture/>);});
 await type('Use the method you need');await submit();
 await act(async()=>select([userMethod]));await type('Add this method');await submit();
 expect(state.replaceMethods).toHaveBeenLastCalledWith('recorded-agent-method',[userMethod],expect.objectContaining({expectedRevision:2}));
});

it('continuationqa: restores a session draft after canonical root synchronization and reopening',async()=>{
 state.stream.mockResolvedValue(undefined);
 await mount();await type('Completed turn');await submit();
 expect(state.root).toBe('/canonical');
 await type('Unsent draft after canonical synchronization');
 await act(async()=>tree!.unmount());tree=undefined;
 const projection=resumableProjection('bound');projection.session!.continuation!.projectRoot='/canonical';
 await mount({resumeConversation:{requestId:1,projection}});
 expect(tree!.root.findByProps({'aria-label':'Chat input'}).props.value).toBe('Unsent draft after canonical synchronization');
});
it('continuationqa: does not relabel an earlier assistant answer as the latest role',async()=>{
 const projection=resumableProjection('roles-changed');
 projection.transcript.items=[{key:'old-answer',kind:'message',role:'assistant',status:'completed',title:'Assistant',timestamp:'2026-09-09T00:00:00.000Z',eventId:'old-answer',eventType:'message.completed',turnId:'help-turn',text:'Answer originally supplied as Help Human'}];
 projection.instructionBases=[{basisId:'help-basis',roleId:'HELP_HUMAN',turnId:'help-turn',createdAt:'2026-09-09T00:00:00.000Z',selectedMethods:[],suppliedEntries:[]} as any];
 await mount({resumeConversation:{requestId:1,projection}});
 const speakers=tree!.root.findAllByProps({className:'chat-speaker'}).map(node=>node.children.join(''));
 expect(speakers).not.toContain('Working Items');
});

it('terminalqa: retries after successful selection PUT followed by stream failure using updated revision',async()=>{
 const projection=resumableProjection('retry-selection');
 const method={kind:'skill' as const,name:'review',source:'bundled' as const,sourceRootId:'chirality-root'};
 let revision=1;state.replaceMethods.mockImplementation(async(_id,methods)=>({revision:++revision,methods:methods??[],basisPreview:{id:`basis-${revision}`}}));
 let select!:(methods:QualifiedMethodReference[])=>void;
 function Fixture(){const [methods,setMethods]=React.useState<QualifiedMethodReference[]>([]);select=setMethods;return <ChatPanel presentation="woven" selectedMethods={methods} onSelectedMethodsChange={setMethods} resumeConversation={{requestId:1,projection}}/>;}
 await act(async()=>{tree=create(<Fixture/>);});
 await act(async()=>select([method]));await type('Retry after this failure');await submit();
 expect(state.replaceMethods).toHaveBeenCalledTimes(1);
 await submit();
 expect(state.replaceMethods).toHaveBeenLastCalledWith('retry-selection',[method],expect.objectContaining({expectedRevision:2,expectedBasisId:'basis-2'}));
});

it('terminaledge: a new chat does not resurrect a method already consumed by a successful first turn',async()=>{
 const method={kind:'skill' as const,name:'review',source:'bundled' as const,sourceRootId:'chirality-root'};
 values.set(buildChatDraftStorageKey('/chosen/subfolder','WORKING_ITEMS','CHAT'),JSON.stringify({draft:'Send once',attachments:[],methods:[method]}));
 state.boot.mockResolvedValue({session:{sessionId:'same-root',projectRoot:'/chosen/subfolder'}});state.stream.mockResolvedValue(undefined);
 let newChat!:(value:number)=>void;
 function Fixture(){const [methods,setMethods]=React.useState<QualifiedMethodReference[]>([]);const [request,setRequest]=React.useState(0);newChat=setRequest;return <ChatPanel presentation="woven" selectedMethods={methods} onSelectedMethodsChange={setMethods} newChatRequest={request}/>;}
 await act(async()=>{tree=create(<Fixture/>);});await submit();
 expect(tree!.root.findAllByProps({'aria-label':'Methods for next turn'})).toHaveLength(0);
 await act(async()=>newChat(1));
 expect(tree!.root.findAllByProps({'aria-label':'Methods for next turn'})).toHaveLength(0);
});

it('terminalremove: failure preserves a newer empty selection made in the method library',async()=>{
 const projection=resumableProjection('remove-before-failure');
 const method={kind:'skill' as const,name:'review',source:'bundled' as const,sourceRootId:'chirality-root'};
 let reject!:(error:Error)=>void;
 state.stream.mockImplementation(()=>new Promise((_resolve,fail)=>{reject=fail;}));
 let select!:(methods:QualifiedMethodReference[])=>void;
 function Fixture(){const [methods,setMethods]=React.useState<QualifiedMethodReference[]>([]);select=setMethods;return <ChatPanel presentation="woven" selectedMethods={methods} onSelectedMethodsChange={setMethods} resumeConversation={{requestId:1,projection}}/>;}
 await act(async()=>{tree=create(<Fixture/>);});
 await act(async()=>select([method]));await type('Try this method');await submit();
 await act(async()=>select([]));
 expect(tree!.root.findAllByProps({'aria-label':'Methods for next turn'})).toHaveLength(0);
 await act(async()=>reject(new Error('Turn failed after the operator removed the next-message method')));
 expect(tree!.root.findAllByProps({'aria-label':'Methods for next turn'})).toHaveLength(0);
});
