import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { WovenDialogueShell } from '../../components/woven-dialogue/woven-dialogue-shell';

const shellState = vi.hoisted(() => ({
  pathname: '/',
  query: '',
  projectRoot: '/repo/projects/chirality-app-dev' as string | null,
  streaming: false
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
  listHarnessSessions: vi.fn(async () => []),
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
  ChatPanel: () => <div data-chat-panel="mounted" />
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
vi.mock('../../components/woven-dialogue/coordination-panel', () => ({
  CoordinationPanel: () => <div data-coordination-panel="mounted" />
}));
vi.mock('../../components/woven-dialogue/activity-shelf', () => ({
  ActivityShelf: () => <div data-activity-shelf="mounted" />
}));
vi.mock('../../components/woven-dialogue/selected-session-replay-lens', () => ({
  SelectedSessionReplayLens: () => <div data-replay-lens="mounted" />
}));

function navigatorItemCount(html: string): number {
  return (html.match(/class="woven-nav-item/g) ?? []).length;
}

describe('WovenDialogueShell composition', () => {
  beforeEach(() => {
    shellState.pathname = '/';
    shellState.query = '';
    shellState.projectRoot = '/repo/projects/chirality-app-dev';
    shellState.streaming = false;
  });

  it('offers exactly the Dialogue, Workbench, and Pipeline navigator surfaces', () => {
    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="dialogue" />);

    expect(navigatorItemCount(html)).toBe(3);
    expect(html).toContain('<span>Dialogue</span>');
    expect(html).toContain('<span>Workbench</span>');
    expect(html).toContain('<span>Pipeline</span>');
    expect(html).not.toContain('Artifacts');
  });

  it('advertises the folded document reader on the Workbench navigator entry', () => {
    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="dialogue" />);

    expect(html).toContain('Documents, evidence &amp; contracts');
    expect(html).not.toContain('Deliverable documents and evidence');
  });

  it('keeps the primary dialogue mounted and visible on the dialogue surface', () => {
    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="dialogue" />);

    expect(html).toContain('data-woven-surface="dialogue"');
    expect(html).toContain('data-primary-dialogue-mounted="true"');
    expect(html).toContain('data-chat-panel="mounted"');
    expect(html).not.toContain('data-focused-surface');
  });

  it('renders the Workbench focused surface while the primary dialogue stays mounted', () => {
    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="workbench" />);

    expect(html).toContain('data-woven-surface="workbench"');
    expect(html).toContain('data-focused-surface="workbench"');
    expect(html).toContain('data-workbench-surface="mounted"');
    expect(html).toContain('<h2>Workbench</h2>');
    expect(html).toContain('data-primary-dialogue-mounted="true"');
    expect(html).toContain('data-chat-panel="mounted"');
    expect(html).toContain('Return to primary dialogue');
  });

  it('renders the Pipeline focused surface for the pipeline route', () => {
    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="pipeline" />);

    expect(html).toContain('data-woven-surface="pipeline"');
    expect(html).toContain('data-focused-surface="pipeline"');
    expect(html).toContain('data-pipeline-surface="mounted"');
    expect(html).not.toContain('data-workbench-surface="mounted"');
  });

  it('renders the navigator surfaces as expandable mode groups', () => {
    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="dialogue" />);

    expect((html.match(/aria-expanded="true"/g) ?? [])).toHaveLength(1);
    expect((html.match(/aria-expanded="false"/g) ?? [])).toHaveLength(2);
    expect(html).toContain('No recorded sessions for this surface.');
    expect(html).not.toContain('role="tab"');
  });

  it('expands the mode group matching the route surface', () => {
    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="pipeline" />);

    expect(html).toContain('aria-current="page" aria-expanded="true"');
    expect(html).toContain('<span>Pipeline</span>');
  });

  it('preserves the legacy compatibility link with the current query string', () => {
    shellState.pathname = '/workbench';
    shellState.query = 'agent=CHANGE';

    const html = renderToStaticMarkup(<WovenDialogueShell defaultSurface="workbench" />);

    expect(html).toContain('href="/workbench?agent=CHANGE&amp;legacy=1"');
  });
});
