import React, { useEffect } from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { renderToStaticMarkup } from 'react-dom/server';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { Navigator } from '../../components/woven-dialogue/navigator';
import { CoordinationPanel } from '../../components/woven-dialogue/coordination-panel';
import { WovenDialogueShell } from '../../components/woven-dialogue/woven-dialogue-shell';

const shellState = vi.hoisted(() => ({
  pathname: '/',
  query: '',
  projectRoot: '/repo/projects/chirality-app-dev' as string | null,
  streaming: false,
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
  listHarnessSessions: vi.fn(async () => ['primary', 'recorded'].map(sessionId => ({ sessionId, persona: 'TASK', projectRoot: shellState.projectRoot, mode: 'governed', createdAt: '2026-09-05', updatedAt: '2026-09-05' }))),
  harnessApiErrorMessage: (error: unknown) => String(error),
  replaySessionEvents: vi.fn(async () => ({ events: [] }))
}));
vi.mock('../../components/workspace/workspace-provider', () => ({
  useWorkspace: () => ({ projectRoot: shellState.projectRoot })
}));
vi.mock('../../components/workspace/harness-events-provider', () => ({
  useHarnessStreaming: () => shellState.streaming
}));
vi.mock('../../components/shell/shell-frame', () => ({
  ShellFrame: ({ children, title }: { children: React.ReactNode; title: string }) => (
    <div data-shell-frame={title}>{children}</div>
  )
}));
vi.mock('../../components/shell/chat-panel', () => ({
  ChatPanel: ({ onActiveSessionChange }: { onActiveSessionChange: (id: string) => void }) => {
    useEffect(() => { shellState.mounted++; onActiveSessionChange('primary'); return () => { shellState.unmounted++; }; }, [onActiveSessionChange]);
    return <input data-chat-panel="mounted" data-chat-input="primary" />;
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
  ActivityShelf: () => <div data-activity-shelf="mounted" />
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
  });

  it.each(['dialogue', 'workbench', 'pipeline'] as const)('only mounts Dialogue even with historical %s surface input', (surface) => {
    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface={surface} />);
    expect(navigatorItemCount(html)).toBe(1);
    expect(html).toContain('<span>Dialogue</span>');
    expect(html).toContain('data-woven-surface="dialogue"');
    expect(html).toContain('data-chat-panel="mounted"');
    expect(html).not.toContain('data-focused-surface');
    expect(html).not.toContain('data-workbench-surface');
    expect(html).not.toContain('data-pipeline-surface');
    expect(html).not.toContain('woven-navigator-chevron');
    expect(html).not.toContain('hidden=');
  });

  it('preserves controller identity and focusable composer through replay, panel controls, resize, and return', async () => {
    const focus = vi.fn();
    const persist = vi.fn();
    vi.stubGlobal('window', { localStorage: { getItem: () => JSON.stringify({ schema: 'chirality.woven-workspace/v1', coordinationView: 'work', sessionSurfaces: { recorded: 'workbench' } }), setItem: persist }, addEventListener: vi.fn(), removeEventListener: vi.fn(), requestAnimationFrame: (callback: () => void) => callback() });
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
    const click = (label: string) => act(() => { tree.root.findAllByType('button').find(button => button.children.join('') === label)!.props.onClick(); });
    click('Close Coordination');
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
    click('Agents'); assertPrimary();
    act(() => tree.root.findByType(Navigator).props.onSelectSession('recorded'));
    expect(tree.root.findByType(CoordinationPanel).props.activeView).toBe('session');
    expect(shellState.replayLoad).toHaveBeenCalledTimes(2); assertPrimary();
    click('Agents'); click('Session'); assertPrimary();
    for (const region of ['Navigator', 'Coordination']) { click(`Close ${region}`); assertPrimary(); click(`Open ${region}`); assertPrimary(); }
    for (const label of ['Resize Navigator', 'Resize Coordination Panel', 'Resize Activity Shelf']) {
      for (const key of ['Home', 'End', 'ArrowLeft']) {
        act(() => tree.root.findByProps({ 'aria-label': label }).props.onKeyDown({ key, shiftKey: false, preventDefault: vi.fn() }));
        assertPrimary();
      }
    }
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

  it('preserves the legacy compatibility link with the current query string', () => {
    shellState.pathname = '/workbench';
    shellState.query = 'agent=CHANGE';

    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="workbench" />);

    expect(html).toContain('href="/workbench?agent=CHANGE&amp;legacy=1"');
  });
});
