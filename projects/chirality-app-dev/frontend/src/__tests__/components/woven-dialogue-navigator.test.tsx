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

  it('expands the active mode group and collapses the others', () => {
    const html = renderNavigator({ activeSurface: 'workbench' });

    expect(html).toContain('aria-expanded="true"');
    expect(html).toContain('aria-expanded="false"');
    expect(html).toContain('aria-current="page"');
    // Only the expanded group lists sessions, and it lists only its own.
    expect(sessionIds(html)).toEqual(['ses-w1']);
    expect(html).toContain('Workbench sessions');
    expect(html).not.toContain('Dialogue sessions');
  });

  it('honours an explicit expansion set over the active surface default', () => {
    const collapsed = renderNavigator({ expandedSurfaces: [] });
    expect(collapsed).not.toContain('aria-expanded="true"');
    expect(sessionIds(collapsed)).toEqual([]);

    const pipelineOnly = renderNavigator({ expandedSurfaces: ['pipeline'] });
    expect(sessionIds(pipelineOnly)).toEqual(['ses-p1']);
  });

  it('caps the recent list at four and offers the full recorded list', () => {
    const html = renderNavigator();

    expect(sessionIds(html)).toEqual(['ses-d1', 'ses-d2', 'ses-d3', 'ses-d4']);
    expect(html).not.toContain('data-session-id="ses-d5"');
    expect(html).toContain(`All sessions (${SESSIONS.length})`);
    // Unattributed sessions are reachable only through that affordance.
    expect(html).not.toContain('data-session-id="ses-x1"');
  });

  it('toggles from recent to all recorded sessions and back through the actual control', () => {
    const tree = renderer.create(
      <Navigator
        activeSurface="dialogue"
        legacyHref="/?legacy=1"
        onOpenSurface={vi.fn()}
        sessions={SESSIONS}
        sessionSurfaces={SURFACES}
        onSelectSession={vi.fn()}
        onToggleSurfaceExpanded={vi.fn()}
      />
    );
    const visibleSessionIds = () =>
      tree.root
        .findAll((node) => typeof node.props['data-session-id'] === 'string')
        .map((node) => node.props['data-session-id']);
    const findSessionToggle = () =>
      tree.root.findAllByType('button').find((button) =>
        ['All sessions (8)', 'Recent sessions'].includes(
          button.children.join('')
        )
      );

    expect(visibleSessionIds()).toEqual(['ses-d1', 'ses-d2', 'ses-d3', 'ses-d4']);
    expect(findSessionToggle()?.children.join('')).toBe('All sessions (8)');
    expect(findSessionToggle()?.props['aria-expanded']).toBe(false);

    act(() => {
      findSessionToggle()?.props.onClick();
    });

    expect(visibleSessionIds()).toEqual(SESSIONS.map((entry) => entry.sessionId));
    expect(visibleSessionIds()).toContain('ses-x1');
    expect(findSessionToggle()?.children.join('')).toBe('Recent sessions');
    expect(findSessionToggle()?.props['aria-expanded']).toBe(true);

    act(() => {
      findSessionToggle()?.props.onClick();
    });

    expect(visibleSessionIds()).toEqual(['ses-d1', 'ses-d2', 'ses-d3', 'ses-d4']);
    expect(findSessionToggle()?.children.join('')).toBe('All sessions (8)');
    expect(findSessionToggle()?.props['aria-expanded']).toBe(false);
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
      4
    );
  });

  it('renders the loading, error, and empty states of the expanded group', () => {
    const loading = renderNavigator({ sessions: [], sessionsLoading: true });
    expect(loading).toContain('Loading recorded sessions…');
    expect(loading).not.toContain('No recorded sessions for this surface.');

    const failed = renderNavigator({
      sessions: [],
      sessionsError: 'Working Root is not reachable.'
    });
    expect(failed).toContain('role="alert"');
    expect(failed).toContain('Working Root is not reachable.');
    expect(failed).not.toContain('No recorded sessions for this surface.');

    const empty = renderNavigator({ sessions: [], sessionSurfaces: {} });
    expect(empty).toContain('No recorded sessions for this surface.');
    expect(empty).not.toContain('All sessions (');

    const unattributedOnly = renderNavigator({
      sessions: [session('ses-x1', 'PDF2MD', '2026-07-17T10:00:00.000Z')],
      sessionSurfaces: {}
    });
    expect(unattributedOnly).toContain('No recorded sessions for this surface.');
    expect(unattributedOnly).toContain('All sessions (1)');
  });

  it('uses disclosure and toggle ARIA only, and no resume-style verbs', () => {
    const html = renderNavigator({ liveSessionId: 'ses-d1' });

    expect(html).not.toContain('role="tab"');
    expect(html).not.toContain('role="tablist"');
    expect(html).not.toContain('Resume');
    expect(html).not.toContain('Continue');
    expect(html).toContain('aria-expanded=');
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
