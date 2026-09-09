import React, { useSyncExternalStore } from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { beforeEach, afterEach, expect, it, vi } from 'vitest';
import { buildChatDraftStorageKey } from '../../lib/harness/chat-draft';

const state = vi.hoisted(() => ({ root: '/chosen/subfolder', query: '', listeners: new Set<() => void>(),
  create: vi.fn(), boot: vi.fn(), stream: vi.fn(), apply: vi.fn(), append: vi.fn(), clear: vi.fn(), streaming: vi.fn(),
  markdownProps: [] as Array<{ source: string; projectRoot?: string | null; fileCatalog?: readonly string[]; onOpenFile?: (path: string) => void }>,
  nativeListener: undefined as ((intent: { path?: string; error?: string }) => void) | undefined
}));
vi.mock('next/navigation', () => ({ usePathname: () => '/chat', useSearchParams: () => new URLSearchParams(state.query), useRouter: () => ({ replace: vi.fn() }) }));
vi.mock('../../components/workspace/workspace-provider', () => ({ useWorkspace: () => ({
  projectRoot: useSyncExternalStore(listener => { state.listeners.add(listener); return () => state.listeners.delete(listener); }, () => state.root),
  applyProjectRoot: state.apply, chooseProjectRoot: vi.fn(async () => false), hasElectronDirectoryPicker: false, errorMessage: null
}) }));
vi.mock('../../components/workspace/toolkit-provider', () => ({ useToolkit: () => ({ optsPayload: undefined }) }));
vi.mock('../../components/workspace/harness-events-provider', () => ({ useHarnessEventActions: () => ({ appendEvent: state.append, clearEvents: state.clear, setStreaming: state.streaming }) }));
vi.mock('../../components/shell/runtime-connectivity-provider', () => ({ useRuntimeEpoch: () => 0 }));
vi.mock('../../components/shell/persona-picker', () => ({ PersonaPicker: () => <span>Working Items</span> }));
vi.mock('../../components/shell/file-picker', () => ({ FilePicker: ({ onAddAttachments }: { onAddAttachments: (items: Array<{ path: string; displayName: string; clientType: 'text' }>) => void }) => <button data-add-attachment onClick={() => onAddAttachments([{ path: '/chosen/subfolder/docs/input.txt', displayName: 'input.txt', clientType: 'text' }])}>add fixture attachment</button> }));
vi.mock('../../components/shell/permission-requests', () => ({ PermissionRequests: () => null }));
vi.mock('../../components/shell/chat-markdown', () => ({ ChatMarkdown: (props: { source: string; projectRoot?: string | null; fileCatalog?: readonly string[]; onOpenFile?: (path: string) => void }) => { state.markdownProps.push(props); return <p>{props.source}</p>; } }));
vi.mock('../../lib/harness/client', async importOriginal => ({ ...await importOriginal<typeof import('../../lib/harness/client')>(), createHarnessSession: state.create, bootHarnessSession: state.boot, streamHarnessTurn: state.stream, interruptHarnessSession: vi.fn() }));
import { ChatPanel } from '../../components/shell/chat-panel';

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
beforeEach(() => {
  vi.clearAllMocks(); state.root = '/chosen/subfolder'; state.query = ''; state.listeners.clear(); state.nativeListener = undefined;
  state.markdownProps = [];
  values = new Map([[canonicalKey, canonicalDraft]]); writes = [];
  vi.stubGlobal('window', { confirm: vi.fn(() => true), localStorage: { getItem: (key: string) => values.get(key) ?? null, setItem: (key: string, value: string) => { writes.push([key, value]); values.set(key, value); }, removeItem: (key: string) => values.delete(key) }, chirality: { folders: {
    registerRecent: vi.fn(async () => ({ ok: true })), pathForFile: vi.fn(() => ''), subscribeOpen: (listener: typeof state.nativeListener) => { state.nativeListener = listener; return () => { state.nativeListener = undefined; }; }
  } } });
  state.create.mockResolvedValue({ sessionId: 'bound' });
  state.boot.mockResolvedValue({ session: { sessionId: 'bound', projectRoot: '/canonical' } });
  state.apply.mockImplementation(async (value: string) => { root(value); return true; });
  state.stream.mockRejectedValue(new Error('Fixture turn failure'));
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
  state.query = 'agent=RESEARCH';
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
  expect(state.create).toHaveBeenLastCalledWith({ projectRoot: '/canonical', persona: 'RESEARCH', mode: 'CHAT' });
  expect(binding).toHaveBeenLastCalledWith({ root: '/canonical', locked: true });
  assertCanonicalUntouched();
  await act(async () => tree!.update(<ChatPanel presentation="woven" onBindingChange={binding} newChatRequest={1} />));
  expect(binding).toHaveBeenLastCalledWith({ root: state.root, locked: false });
  expect(JSON.stringify(tree!.toJSON())).not.toContain('First completed turn');
});
it('rejects a different root from a subsequent persona boot without rebinding the retained conversation', async () => {
  state.stream.mockResolvedValue(undefined); state.apply.mockResolvedValue(false);
  const binding = vi.fn(); await mount({ onBindingChange: binding }); await type('Original turn'); await submit();
  state.query = 'agent=RESEARCH';
  await act(async () => tree!.update(<ChatPanel presentation="woven" onBindingChange={binding} />));
  state.boot.mockResolvedValue({ session: { sessionId: 'different', projectRoot: '/different' } });
  await type('Must not rebind'); await submit();
  expect(state.stream).toHaveBeenCalledTimes(1);
  expect(binding).toHaveBeenLastCalledWith({ root: '/canonical', locked: true });
  expect(JSON.stringify(tree!.toJSON())).toContain('Original turn');
  expect(JSON.stringify(tree!.toJSON())).toContain('different folder');
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('Must not rebind');
  assertCanonicalUntouched();
});

it('keeps retained assistant speaker labels and titles tied to their originating Agent', async () => {
  state.stream.mockResolvedValue(undefined);
  await mount(); await type('First agent'); await submit();
  const speakers = () => tree!.root.findAllByProps({ className: 'chat-speaker' }).filter(node => node.props.title);
  expect(speakers().map(node => [node.props.title, node.children.join('')])).toEqual([
    ['WORKING_ITEMS', 'Working Items'], ['WORKING_ITEMS', 'Working Items']
  ]);
  state.query = 'agent=RESEARCH';
  await act(async () => tree!.update(<ChatPanel presentation="woven" />));
  await type('Second agent'); await submit();
  expect(speakers().map(node => [node.props.title, node.children.join('')])).toEqual([
    ['WORKING_ITEMS', 'Working Items'], ['WORKING_ITEMS', 'Working Items'], ['RESEARCH', 'Research']
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
  const keyA = buildChatDraftStorageKey('/root-a', 'WORKING_ITEMS', 'CHAT');
  const keyB = buildChatDraftStorageKey('/root-b', 'WORKING_ITEMS', 'CHAT');
  values.set(keyB, JSON.stringify({ draft: 'Saved root B prompt', attachments: [] }));
  await mount({ presentation: undefined }); await type('Completed root A turn'); await submit();
  await type('Unsent root A prompt');
  expect(JSON.parse(values.get(keyA)!).draft).toBe('Unsent root A prompt');
  await act(async () => root('/root-b'));
  expect(tree!.root.findByProps({ 'aria-label': 'Chat input' }).props.value).toBe('Saved root B prompt');
  state.boot.mockResolvedValue({ session: { sessionId: 'b', projectRoot: '/root-b' } });
  await submit();
  expect(state.create).toHaveBeenLastCalledWith({ projectRoot: '/root-b', persona: 'WORKING_ITEMS', mode: 'CHAT' });
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
