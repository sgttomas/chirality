import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import renderer, { act } from 'react-test-renderer';
import { describe, expect, it, vi } from 'vitest';
import type { SessionRecord } from '@chirality/runtime-contracts/types';
import {
  Navigator,
  buildNavigatorSessionGroups
} from '../../components/woven-dialogue/navigator';
import type { WovenSessionSurfaceMap } from '../../lib/woven-dialogue/woven-workspace-state';

vi.mock('next/link', () => ({
  default: ({ children, ...props }: React.ComponentProps<'a'>) => (
    <a {...props}>{children}</a>
  )
}));

vi.mock('../../components/shell/file-tree-panel', () => ({
  FileTreePanel: () => <div>File tree</div>
}));

function session(
  sessionId: string,
  persona: string,
  updatedAt: string
): SessionRecord {
  return {
    sessionId,
    projectRoot: '/repo/projects/chirality-app-dev',
    persona,
    mode: 'governed',
    createdAt: updatedAt,
    updatedAt
  };
}

const SESSIONS: readonly SessionRecord[] = [
  session('ses-d1', 'WORKING_ITEMS', '2026-07-24T10:00:00.000Z'),
  session('ses-d2', 'RECONCILIATION', '2026-07-23T10:00:00.000Z'),
  session('ses-d3', 'RESEARCH', '2026-07-22T10:00:00.000Z'),
  session('ses-d4', 'CHANGE', '2026-07-21T10:00:00.000Z'),
  session('ses-d5', 'REVIEW', '2026-07-20T10:00:00.000Z'),
  session('ses-w1', 'EVALUATION', '2026-07-19T10:00:00.000Z'),
  session('ses-p1', 'TASK', '2026-07-18T10:00:00.000Z'),
  session('ses-x1', 'PDF2MD', '2026-07-17T10:00:00.000Z')
];

const SURFACES: WovenSessionSurfaceMap = {
  'ses-d1': 'dialogue',
  'ses-d2': 'dialogue',
  'ses-d3': 'dialogue',
  'ses-d4': 'dialogue',
  'ses-d5': 'dialogue',
  'ses-w1': 'workbench',
  'ses-p1': 'pipeline'
  // `ses-x1` is deliberately unattributed.
};

function renderNavigator(
  overrides: Partial<React.ComponentProps<typeof Navigator>> = {}
): string {
  return renderToStaticMarkup(
    <Navigator
      activeSurface="dialogue"
      legacyHref="/?legacy=1"
      onOpenSurface={vi.fn()}
      sessions={SESSIONS}
      sessionSurfaces={SURFACES}
      onSelectSession={vi.fn()}
      onToggleSurfaceExpanded={vi.fn()}
      {...overrides}
    />
  );
}

function sessionIds(html: string): string[] {
  return [...html.matchAll(/data-session-id="([^"]+)"/g)].map((match) => match[1]);
}

describe('Woven Dialogue Navigator', () => {
  it('opens the legacy compatibility surface separately so primary dialogue stays mounted', () => {
    const html = renderToStaticMarkup(
      <Navigator
        activeSurface="dialogue"
        legacyHref="/?legacy=1"
        onOpenSurface={vi.fn()}
      />
    );

    expect(html).toContain('href="/?legacy=1"');
    expect(html).toContain('target="_blank"');
    expect(html).toContain('Open legacy interface in a new window');
  });

  it('lists every recorded session flat in updatedAt order, including historical annotations', () => {
    const html = renderNavigator({ sessions: [...SESSIONS].reverse(), expandedSurfaces: ['pipeline'] });
    expect(sessionIds(html)).toEqual(SESSIONS.map(entry => entry.sessionId));
    expect(html).not.toContain('aria-expanded=');
    expect(html).not.toContain('woven-navigator-chevron');
    expect(html).not.toContain('<span>Workbench</span>');
    expect(html).not.toContain('<span>Pipeline</span>');
    expect(html).toContain('Recorded surface: workbench');
    expect(html).toContain('Recorded surface: pipeline');
  });

  it('selects historical and unattributed sessions directly', () => {
    const select = vi.fn();
    const tree = renderer.create(<Navigator activeSurface="dialogue" legacyHref="/?legacy=1"
      onOpenSurface={vi.fn()} sessions={SESSIONS} sessionSurfaces={SURFACES} onSelectSession={select} />);
    for (const id of ['ses-w1', 'ses-p1', 'ses-x1']) {
      act(() => tree.root.findByProps({ 'data-session-id': id }).props.onClick());
      expect(select).toHaveBeenLastCalledWith(id);
    }
    act(() => tree.unmount());
  });

  it('marks the live session and the selected replay session distinctly', () => {
    const html = renderNavigator({
      liveSessionId: 'ses-d1',
      selectedSessionId: 'ses-d3'
    });

    expect(html).toContain('woven-navigator-session woven-navigator-session--live');
    expect(html).toContain('woven-navigator-session-dot');
    expect(html).toContain('aria-label="Live session"');
    expect(html).toContain(
      '<span class="woven-navigator-session-title">RESEARCH</span>'
    );
    expect((html.match(/aria-pressed="true"/g) ?? [])).toHaveLength(1);
    expect((html.match(/woven-navigator-session--live/g) ?? [])).toHaveLength(1);
  });

  it('formats the session timestamp from the record without consulting a clock', () => {
    const html = renderNavigator();

    expect(html).toContain(
      '<span class="woven-navigator-session-when">Jul 24, 2026</span>'
    );
    expect(html).toContain(
      '<span class="woven-navigator-session-when">Jul 21, 2026</span>'
    );
  });

  it('disables session selection while a turn is in flight', () => {
    const html = renderNavigator({ selectionDisabled: true });

    expect(html).toContain(
      'Session selection is paused while the primary dialogue is running.'
    );
    expect((html.match(/data-session-id="[^"]+" disabled=""/g) ?? [])).toHaveLength(
      SESSIONS.length
    );
  });

  it('renders the loading, error, and empty states of the expanded group', () => {
    const loading = renderNavigator({ sessions: [], sessionsLoading: true });
    expect(loading).toContain('Loading recorded sessions…');
    expect(loading).not.toContain('No recorded sessions.');

    const failed = renderNavigator({
      sessions: [],
      sessionsError: 'Working Root is not reachable.'
    });
    expect(failed).toContain('role="alert"');
    expect(failed).toContain('Working Root is not reachable.');
    expect(failed).not.toContain('No recorded sessions.');

    const empty = renderNavigator({ sessions: [], sessionSurfaces: {} });
    expect(empty).toContain('No recorded sessions.');
    expect(empty).not.toContain('All sessions (');

    const unattributedOnly = renderNavigator({
      sessions: [session('ses-x1', 'PDF2MD', '2026-07-17T10:00:00.000Z')],
      sessionSurfaces: {}
    });
    expect(unattributedOnly).not.toContain('No recorded sessions.');
    expect(sessionIds(unattributedOnly)).toEqual(['ses-x1']);
  });

  it('uses disclosure and toggle ARIA only, and no resume-style verbs', () => {
    const html = renderNavigator({ liveSessionId: 'ses-d1' });

    expect(html).not.toContain('role="tab"');
    expect(html).not.toContain('role="tablist"');
    expect(html).not.toContain('Resume');
    expect(html).not.toContain('Continue');
    expect(html).not.toContain('aria-expanded=');
    expect(html).toContain('aria-pressed="false"');
  });
});

describe('Navigator session grouping', () => {
  it('orders sessions recency-first and scopes them by local attribution only', () => {
    const groups = buildNavigatorSessionGroups(SESSIONS, SURFACES);

    expect(groups.bySurface.dialogue.map((entry) => entry.sessionId)).toEqual([
      'ses-d1',
      'ses-d2',
      'ses-d3',
      'ses-d4',
      'ses-d5'
    ]);
    expect(groups.bySurface.workbench.map((entry) => entry.sessionId)).toEqual([
      'ses-w1'
    ]);
    expect(groups.bySurface.pipeline.map((entry) => entry.sessionId)).toEqual([
      'ses-p1'
    ]);
    expect(groups.all).toHaveLength(SESSIONS.length);
    expect(groups.all[groups.all.length - 1]).toMatchObject({
      sessionId: 'ses-x1',
      surface: null
    });
  });

  it('falls back to the session id when no persona or timestamp is recorded', () => {
    const groups = buildNavigatorSessionGroups(
      [
        {
          ...session('ses-blank', '   ', ''),
          createdAt: '',
          updatedAt: ''
        }
      ],
      {}
    );

    expect(groups.all[0]).toMatchObject({
      sessionId: 'ses-blank',
      label: 'ses-blank',
      when: '',
      surface: null
    });
  });

  it('renders no timestamp for an invalid recorded date', () => {
    const groups = buildNavigatorSessionGroups(
      [session('ses-invalid', 'TASK', 'not-a-date')],
      {}
    );

    expect(groups.all[0]?.when).toBe('');
  });
});
