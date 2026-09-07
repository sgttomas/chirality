import React, { useEffect } from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { renderToStaticMarkup } from 'react-dom/server';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { RightPanel } from '../../components/woven-dialogue/right-panel';
import { Navigator } from '../../components/woven-dialogue/navigator';
import { CoordinationPanel } from '../../components/woven-dialogue/coordination-panel';
import { WovenDialogueShell } from '../../components/woven-dialogue/woven-dialogue-shell';

const shellState = vi.hoisted(() => ({
  pathname: '/',
  query: '',
  projectRoot: '/repo/projects/chirality-app-dev' as string | null,
  streaming: false,
  extraSessions: [] as string[],
  mounted: 0,
  unmounted: 0,
  replayLoad: vi.fn(),
  replayNotify: undefined as ((state: unknown) => void) | undefined
}));

vi.mock('next/navigation', () => ({
  usePathname: () => shellState.pathname,
  useSearchParams: () => new URLSearchParams(shellState.query)
}));
vi.mock('next/link', () => ({
  default: ({ children, ...props }: React.AnchorHTMLAttributes<HTMLAnchorElement>) =>
    React.createElement('a', props, children)
}));

// The node test environment has no `window`/`fetch`; every child that reaches
// for the network, the harness stream, or the shared chrome is mocked so this
// test observes the shell's own composition only.
vi.mock('../../lib/harness/client', () => ({
  listHarnessSessions: vi.fn(async () => ['primary', 'recorded', ...shellState.extraSessions].map(sessionId => ({ sessionId, persona: 'TASK', projectRoot: shellState.projectRoot, mode: 'governed', createdAt: '2026-09-05', updatedAt: '2026-09-05' }))),
  harnessApiErrorMessage: (error: unknown) => String(error),
  replaySessionEvents: vi.fn(async () => ({ events: [] }))
}));
vi.mock('../../components/workspace/workspace-provider', () => ({
  useWorkspace: () => ({ projectRoot: shellState.projectRoot })
}));
vi.mock('../../components/workspace/harness-events-provider', () => ({
  useHarnessEvents: () => ({ events: [] }),
  useHarnessStreaming: () => shellState.streaming
}));
vi.mock('../../components/shell/shell-frame', () => ({
  ShellFrame: ({ children, title, renderWorkspaceContent, onOpenSettings, legacyHref }: { children?: React.ReactNode; title: string; onOpenSettings?: () => void; legacyHref?: string; renderWorkspaceContent?: (controls: object) => React.ReactNode }) => (
    <div data-shell-frame={title}>{renderWorkspaceContent ? renderWorkspaceContent({ settingsControl: <><button data-account-control="true" onClick={onOpenSettings}>Account settings</button><a href={legacyHref}>Legacy window</a></>, settingsView: <div data-settings-view="true">Settings controls</div> }) : children}</div>
  )
}));
vi.mock('../../components/shell/chat-panel', () => ({
  ChatPanel: ({ onActiveSessionChange, onDraftCaptured }: { onActiveSessionChange: (id: string) => void; onDraftCaptured: () => void }) => {
    useEffect(() => { shellState.mounted++; onActiveSessionChange('primary'); return () => { shellState.unmounted++; }; }, [onActiveSessionChange]);
    return <input data-chat-panel="mounted" data-chat-input="primary" onChange={onDraftCaptured} />;
  }
}));
vi.mock('../../components/shell/persona-picker', () => ({
  PersonaPicker: () => <div data-persona-picker="mounted" />
}));
vi.mock('../../components/shell/file-tree-panel', () => ({
  FileTreePanel: () => <div data-file-tree="mounted" />
}));
// Mocked defensively: after the Artifacts→Workbench fold, `WorkbenchSurface`
// transitively imports `DocumentView` (react-markdown ESM + fetch).
vi.mock('../../components/shell/document-view', () => ({
  DocumentView: () => <div data-document-view="mounted" />
}));
vi.mock('../../components/workbench/workbench-surface', () => ({
  WorkbenchSurface: () => <div data-workbench-surface="mounted" />
}));
vi.mock('../../components/pipeline/pipeline-surface', () => ({
  PipelineSurface: () => <div data-pipeline-surface="mounted" />
}));
vi.mock('../../components/woven-dialogue/agents-projection', () => ({
  AgentsProjection: () => <div data-agents="mounted" />
}));
vi.mock('../../components/shell/runtime-connectivity-provider', () => ({ useRuntimeEpoch: () => 0 }));
vi.mock('../../lib/woven-dialogue/selected-session-replay', () => ({
  createSelectedSessionReplayLoader: () => ({
    subscribe: (notify: (state: unknown) => void) => { shellState.replayNotify = notify; return () => {}; },
    load: (id: string) => { shellState.replayLoad(id); shellState.replayNotify?.({ status: 'LOADING', selectedSessionId: id }); },
    cancel: () => shellState.replayNotify?.({ status: 'IDLE' }),
    dispose: () => {}
  })
}));
vi.mock('../../components/woven-dialogue/activity-shelf', () => ({
  ActivityStrip: ({ onOpenDetails, primarySessionId }: { onOpenDetails: () => void; primarySessionId?: string }) => <button onClick={onOpenDetails} data-primary-session={primarySessionId} data-activity-strip="mounted">Details</button>,
  ActivityView: () => <div data-activity-view="mounted" />
}));
vi.mock('../../components/woven-dialogue/selected-session-replay-lens', () => ({
  SelectedSessionReplayLens: ({ state, onReturnToPrimary, onRetry }: { state: { status: string }; onReturnToPrimary: () => void; onRetry: () => void }) => <section data-replay-lens={state.status}><button onClick={onReturnToPrimary}>Return to primary dialogue</button><button onClick={onRetry}>Retry</button></section>
}));

function navigatorItemCount(html: string): number {
  return (html.match(/class="woven-nav-item/g) ?? []).length;
}

describe('WovenDialogueShell composition', () => {
  afterEach(() => { vi.unstubAllGlobals(); });
  beforeEach(() => {
    shellState.pathname = '/';
    shellState.query = '';
    shellState.projectRoot = '/repo/projects/chirality-app-dev';
    shellState.streaming = false;
    shellState.extraSessions = [];
  });

  it.each(['dialogue', 'workbench', 'pipeline'] as const)('only mounts Dialogue even with historical %s surface input', (surface) => {
    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface={surface} />);
    expect(navigatorItemCount(html)).toBe(1);
    expect(html).toContain('<span>Current chat</span>');
    expect(html).toContain('data-woven-surface="dialogue"');
    expect(html).toContain('data-chat-panel="mounted"');
    expect(html).not.toContain('data-focused-surface');
    expect(html).not.toContain('data-workbench-surface');
    expect(html).not.toContain('data-pipeline-surface');
    expect(html).not.toContain('woven-navigator-chevron');
    expect(html).not.toMatch(/\shidden=/);
  });

  it('preserves controller identity and focusable composer through replay, panel controls, resize, and return', async () => {
    const focus = vi.fn();
    const persist = vi.fn();
    vi.stubGlobal('window', { localStorage: { getItem: () => JSON.stringify({ schema: 'chirality.woven-workspace/v1', coordinationView: 'work', rightPanelView: 'agents', sessionSurfaces: { recorded: 'workbench' } }), setItem: persist }, addEventListener: vi.fn(), removeEventListener: vi.fn(), requestAnimationFrame: (callback: () => void) => callback() });
    vi.stubGlobal('document', { querySelector: () => ({ focus }) });
    shellState.mounted = 0; shellState.unmounted = 0; shellState.replayLoad.mockClear();
    let tree!: ReactTestRenderer;
    await act(async () => { tree = create(<WovenDialogueShell defaultSurface="dialogue" />); });
    expect(tree.root.findByType(CoordinationPanel).props.activeView).toBe('agents');
    expect(tree.root.findByType(Navigator).props.sessionSurfaces).toEqual({ recorded: 'workbench', primary: 'dialogue' });
    expect(JSON.parse(persist.mock.calls.at(-1)![1]).sessionSurfaces).toEqual({ recorded: 'workbench', primary: 'dialogue' });
    const input = tree.root.findByProps({ 'data-chat-input': 'primary' });
    const assertPrimary = () => {
      expect(tree.root.findByProps({ 'data-chat-input': 'primary' })).toBe(input);
      let node: typeof input | null = input;
      while (node) { expect(node.props.hidden).not.toBe(true); expect(node.props['aria-hidden']).not.toBe(true); node = node.parent; }
      expect(input.props.disabled).toBeUndefined();
      expect(shellState.mounted).toBe(1); expect(shellState.unmounted).toBe(0);
      expect(tree.root.findAll(node => Boolean(node.props['data-focused-surface']))).toHaveLength(0);
    };
    const click = (label: string) => act(() => { tree.root.findAllByType('button').find(button => (button.props['aria-label'] ?? button.children.join('')) === label)!.props.onClick(); });
    act(() => tree.root.findByType(RightPanel).props.onClose());
    act(() => tree.root.findByType(Navigator).props.onSelectSession('recorded'));
    expect(tree.root.findByType(CoordinationPanel).props.activeView).toBe('session');
    expect(tree.root.findByProps({ 'data-replay-lens': 'LOADING' })).toBeTruthy();
    assertPrimary();
    act(() => shellState.replayNotify?.({ status: 'UNAVAILABLE', selectedSessionId: 'recorded', message: 'offline' }));
    assertPrimary();
    click('Retry');
    expect(shellState.replayLoad).toHaveBeenCalledTimes(2);
    act(() => shellState.replayNotify?.({ status: 'READY', projection: { selectedSessionId: 'recorded' } }));
    assertPrimary();
    click('Who is working'); assertPrimary();
    act(() => tree.root.findByType(Navigator).props.onSelectSession('recorded'));
    expect(tree.root.findByType(CoordinationPanel).props.activeView).toBe('session');
    expect(shellState.replayLoad).toHaveBeenCalledTimes(2); assertPrimary();
    click('Who is working'); act(() => tree.root.findByType(Navigator).props.onSelectSession('recorded')); assertPrimary();
    click('Close Navigator'); assertPrimary(); click('Open Navigator'); assertPrimary();
    act(() => tree.root.findByType(RightPanel).props.onView('files'));
    act(() => tree.root.findByType(RightPanel).props.onClose()); assertPrimary(); click('Open Coordination'); assertPrimary();
    for (const label of ['Resize Navigator', 'Resize Coordination Panel']) {
      for (const key of ['Home', 'End', 'ArrowLeft']) {
        act(() => tree.root.findByProps({ 'aria-label': label }).props.onKeyDown({ key, shiftKey: false, preventDefault: vi.fn() }));
        assertPrimary();
      }
    }
    act(() => tree.root.findByType(Navigator).props.onSelectSession('recorded'));
    click('Return to primary dialogue');
    expect(focus).toHaveBeenCalled(); assertPrimary();
    expect(tree.root.findAll(node => Boolean(node.props['data-replay-lens']))).toHaveLength(0);
    shellState.streaming = true;
    act(() => tree.update(<WovenDialogueShell defaultSurface="dialogue" />));
    act(() => tree.root.findByType(Navigator).props.onSelectSession('recorded'));
    expect(shellState.replayLoad).toHaveBeenCalledTimes(2); assertPrimary();
    act(() => tree.unmount());
    expect(shellState.unmounted).toBe(1);
  });

  it('persists file/document widths and expand return while primary stays mounted', async () => {
    const persist = vi.fn(); const listeners: Record<string, (event: unknown) => void> = {};
    vi.stubGlobal('window', { localStorage: { getItem: () => null, setItem: persist },
      addEventListener: (name: string, callback: (event: unknown) => void) => { listeners[name] = callback; }, removeEventListener: vi.fn(), requestAnimationFrame: (cb: () => void) => cb() });
    vi.stubGlobal('document', { querySelector: () => ({ focus: vi.fn() }) });
    let tree!: ReactTestRenderer; await act(async () => { tree = create(<WovenDialogueShell defaultSurface="dialogue" />); });
    const input = tree.root.findByProps({ 'data-chat-input': 'primary' });
    const panel = () => tree.root.findByType(RightPanel);
    const state = () => JSON.parse(persist.mock.calls.at(-1)![1]);
    const resize = () => tree.root.findByProps({ 'aria-label': 'Resize Coordination Panel' });
    expect(panel().props.state.rightPanelView).toBe('files');
    act(() => resize().props.onKeyDown({ key: 'ArrowLeft', shiftKey: false, preventDefault: vi.fn() }));
    expect(state().rightPanelWidths.files).toBe(316);
    act(() => panel().props.onOpenFile(`${shellState.projectRoot}/spec.md`));
    expect(state().openDocumentPath).toBe('spec.md'); expect(resize().props['aria-valuenow']).toBe(480);
    act(() => resize().props.onPointerDown({ button: 0, clientX: 700, clientY: 0, preventDefault: vi.fn() }));
    act(() => listeners.pointermove({ clientX: 620, clientY: 0 })); act(() => listeners.pointerup({}));
    expect(state().rightPanelWidths.document).toBe(560);
    act(() => panel().props.onExpand());
    expect(state()).toMatchObject({ rightPanelExpanded: true, navigatorCollapsed: true, preExpandState: { rightWidth: 560, leftCollapsed: false } });
    act(() => input.props.onChange());
    expect(state()).toMatchObject({ rightPanelExpanded: false, navigatorCollapsed: false, rightPanelWidths: { document: 560 } });
    act(() => panel().props.onView('files'));
    expect(state().openDocumentPath).toBeNull(); expect(resize().props['aria-valuenow']).toBe(316);
    act(() => panel().props.onView('agents')); expect(resize().props['aria-valuenow']).toBe(360);
    expect(tree.root.findByProps({ 'data-chat-input': 'primary' })).toBe(input);
    act(() => tree.unmount());
  });

  it('opens a recorded parent through the existing selection guard, preserving live-turn and primary behavior', async () => {
    shellState.extraSessions = ['parent']; shellState.replayLoad.mockClear();
    const focus = vi.fn();
    vi.stubGlobal('window', { localStorage: { getItem: () => null, setItem: vi.fn() }, addEventListener: vi.fn(), removeEventListener: vi.fn(), requestAnimationFrame: (cb: () => void) => cb() });
    vi.stubGlobal('document', { querySelector: () => ({ focus }) });
    let tree!: ReactTestRenderer; await act(async () => { tree = create(<WovenDialogueShell defaultSurface="dialogue" />); });
    const input = tree.root.findByProps({ 'data-chat-input': 'primary' });
    act(() => tree.root.findByType(Navigator).props.onSelectSession('recorded'));
    const projection = (parentSessionId: string) => ({ selectedSessionId: 'recorded', sourceReference: 'events:recorded', observedAt: '2026-09-05', disclosure: 'READY_SNAPSHOT', currency: 'CURRENT', sourceEventCount: 2, renderedItemCount: 1, malformedLineCount: 0, diagnostics: [], session: { sessionId: 'recorded', currency: 'CURRENT', parentage: { state: 'RECORDED', parentSessionId, parentAvailable: true }, diagnostics: [] } });
    act(() => shellState.replayNotify?.({ status: 'READY', projection: projection('parent') }));
    const openParent = () => tree.root.findAllByType('button').find(x => x.children.includes('Open parent chat'))!;
    expect(openParent().props.disabled).toBe(false); act(() => openParent().props.onClick()); expect(shellState.replayLoad).toHaveBeenLastCalledWith('parent');
    act(() => shellState.replayNotify?.({ status: 'READY', projection: projection('parent') }));
    shellState.streaming = true; act(() => tree.update(<WovenDialogueShell defaultSurface="dialogue" />));
    expect(openParent().props.disabled).toBe(true);
    const calls = shellState.replayLoad.mock.calls.length;
    act(() => tree.root.findByType(RightPanel).props.onOpenParent('parent')); expect(shellState.replayLoad).toHaveBeenCalledTimes(calls);
    act(() => shellState.replayNotify?.({ status: 'READY', projection: projection('primary') }));
    expect(openParent().props.disabled).toBe(false); act(() => openParent().props.onClick());
    expect(focus).toHaveBeenCalled(); expect(shellState.replayLoad).toHaveBeenCalledTimes(calls);
    expect(tree.root.findByProps({ 'data-chat-input': 'primary' })).toBe(input);
    act(() => tree.unmount());
  });

  it('responds to measured stacked widths without removing primary, document or activity controls', async () => {
    let measure!: (entries: Array<{ contentRect: { width: number } }>) => void;
    vi.stubGlobal('ResizeObserver', class { constructor(callback: typeof measure) { measure = callback; } observe() {} disconnect() {} });
    vi.stubGlobal('window', { localStorage: { getItem: () => null, setItem: vi.fn() }, addEventListener: vi.fn(), removeEventListener: vi.fn(), requestAnimationFrame: (cb: () => void) => cb() });
    let tree!: ReactTestRenderer;
    await act(async () => { tree = create(<WovenDialogueShell defaultSurface="dialogue" />, { createNodeMock: element => element.type === 'section' && element.props['data-woven-surface'] ? {} : null }); });
    const primary = tree.root.findByProps({ 'data-chat-input': 'primary' });
    act(() => tree.root.findByType(RightPanel).props.onOpenFile(`${shellState.projectRoot}/spec.md`));
    for (const width of [1440, 960, 959, 900, 861, 860]) {
      act(() => measure([{ contentRect: { width } }]));
      expect(tree.root.findByProps({ 'data-woven-surface': 'dialogue' }).props.className.includes('is-stacked')).toBe(width < 960);
      expect(tree.root.findByProps({ 'data-chat-input': 'primary' })).toBe(primary);
      expect(tree.root.findByProps({ 'data-document-view': 'mounted' })).toBeTruthy();
      expect(tree.root.findByProps({ 'data-activity-strip': 'mounted' })).toBeTruthy();
    }
    // This tests measured state/identity only; browser scroll geometry is a separate manager-owned proof.
    act(() => tree.unmount());
  });

  it('provides explicit desktop reopen glyphs and full accessible names across responsive states', async () => {
    let measure!: (entries: Array<{ contentRect: { width: number } }>) => void;
    vi.stubGlobal('ResizeObserver', class { constructor(callback: typeof measure) { measure = callback; } observe() {} disconnect() {} });
    vi.stubGlobal('window', { localStorage: { getItem: () => null, setItem: vi.fn() }, addEventListener: vi.fn(), removeEventListener: vi.fn(), requestAnimationFrame: (cb: () => void) => cb() });
    let tree!: ReactTestRenderer;
    await act(async () => { tree = create(<WovenDialogueShell defaultSurface="dialogue" />, { createNodeMock: element => element.type === 'section' && element.props['data-woven-surface'] ? {} : null }); });
    act(() => tree.root.findByProps({ 'aria-label': 'Close Navigator' }).props.onClick());
    act(() => tree.root.findByType(RightPanel).props.onClose());
    for (const width of [1440, 960, 959, 860, 1440]) {
      act(() => measure([{ contentRect: { width } }]));
      expect(tree.root.findByProps({ 'aria-label': 'Open Navigator' }).findByProps({ className: 'woven-collapsed-brand' }).children).toEqual(['C']);
      expect(tree.root.findByProps({ 'aria-label': 'Open Coordination' }).children).toEqual(['›']);
    }
    act(() => tree.root.findByProps({ 'aria-label': 'Open Navigator' }).props.onClick());
    act(() => tree.root.findByProps({ 'aria-label': 'Open Coordination' }).props.onClick());
    expect(tree.root.findByType(Navigator)).toBeTruthy();
    expect(tree.root.findByType(RightPanel)).toBeTruthy();
    // Rendered content/state is covered here; actual glyph visibility and geometry need browser proof.
    act(() => tree.unmount());
  });

  it('keeps collapse, detail return and expansion as distinct real controls without remounting primary', async () => {
    const persist = vi.fn();
    vi.stubGlobal('window', { localStorage: { getItem: () => null, setItem: persist }, addEventListener: vi.fn(), removeEventListener: vi.fn(), requestAnimationFrame: (cb: () => void) => cb() });
    let tree!: ReactTestRenderer; await act(async () => { tree = create(<WovenDialogueShell defaultSurface="dialogue" />); });
    const primary = tree.root.findByProps({ 'data-chat-input': 'primary' });
    const saved = () => JSON.parse(persist.mock.calls.at(-1)![1]);
    const click = (label: string) => act(() => tree.root.findAllByType('button').find(button => (button.props['aria-label'] ?? button.children.join('')) === label)!.props.onClick());
    const assertPrimary = () => expect(tree.root.findByProps({ 'data-chat-input': 'primary' })).toBe(primary);
    act(() => tree.root.findByType(RightPanel).props.onOpenFile(`${shellState.projectRoot}/spec.md`));
    click('Expand panel'); expect(saved().rightPanelExpanded).toBe(true); assertPrimary();
    click('Return panel'); expect(saved().rightPanelExpanded).toBe(false); expect(saved().openDocumentPath).toBe('spec.md'); assertPrimary();
    click('Close detail'); expect(saved()).toMatchObject({ coordinationCollapsed: false, openDocumentPath: null }); assertPrimary();
    click('Collapse right panel'); expect(saved()).toMatchObject({ coordinationCollapsed: true, openDocumentPath: null });
    expect(tree.root.findAllByType(RightPanel)).toHaveLength(0); assertPrimary();
    click('Close Navigator'); expect(saved().navigatorCollapsed).toBe(true); assertPrimary();
    click('Open Navigator'); expect(saved().navigatorCollapsed).toBe(false); assertPrimary();
    click('Open Coordination'); expect(saved()).toMatchObject({ coordinationCollapsed: false, openDocumentPath: null }); assertPrimary();
    click('Expand panel'); expect(saved().rightPanelExpanded).toBe(true);
    act(() => tree.root.findByProps({ 'aria-label': 'Collapse right panel' }).props.onClick());
    expect(saved()).toMatchObject({ coordinationCollapsed: true, rightPanelExpanded: false, navigatorCollapsed: false }); assertPrimary();
    click('Open Coordination'); expect(saved().rightPanelView).toBe('files'); assertPrimary();
    act(() => tree.unmount());
  });

  it('preserves the legacy compatibility link with the current query string', () => {
    shellState.pathname = '/workbench';
    shellState.query = 'agent=CHANGE';

    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="workbench" />);

    expect(html).toContain('href="/workbench?agent=CHANGE&amp;legacy=1"');
  });
});

it('opens Settings from the sole footer or collapsed account control without remounting the chat', async () => {
  let tree!: ReactTestRenderer;
  vi.stubGlobal('window', { innerWidth: 1440, innerHeight: 900, addEventListener: vi.fn(), removeEventListener: vi.fn(), localStorage: { getItem: () => null, setItem: vi.fn() } });
  await act(async () => { tree = create(<WovenDialogueShell defaultSurface="dialogue" />); });
  const chat = tree.root.findByProps({ 'data-chat-panel': 'mounted' });
  expect(tree.root.findByProps({ 'data-activity-strip': 'mounted' }).props['data-primary-session']).toBe('primary');
  const mounted = shellState.mounted;
  const unmounted = shellState.unmounted;
  expect(tree.root.findAllByProps({ 'data-account-control': 'true' })).toHaveLength(1);
  act(() => tree.root.findByProps({ 'data-account-control': 'true' }).props.onClick());
  expect(tree.root.findAllByProps({ 'data-settings-view': 'true' })).toHaveLength(1);
  expect(tree.root.findByProps({ 'data-chat-panel': 'mounted' })).toBe(chat);
  act(() => tree.root.findByProps({ 'aria-label': 'Close Navigator' }).props.onClick());
  expect(tree.root.findAllByProps({ 'data-account-control': 'true' })).toHaveLength(1);
  act(() => tree.root.findByProps({ 'data-account-control': 'true' }).props.onClick());
  expect(tree.root.findByProps({ 'data-chat-panel': 'mounted' })).toBe(chat);
  expect(shellState.mounted).toBe(mounted); expect(shellState.unmounted).toBe(unmounted);
  expect(tree.root.findByProps({ 'data-activity-strip': 'mounted' }).props['data-primary-session']).toBe('primary');
  act(() => tree.unmount());
  vi.unstubAllGlobals();
});
