'use client';

import Link from 'next/link';
import React from 'react';
import type { SessionRecord } from '@chirality/harness-contract/types';
import type {
  WovenSessionSurfaceMap,
  WovenWorkspaceSurface
} from '../../lib/woven-dialogue/woven-workspace-state';
import { FileTreePanel } from '../shell/file-tree-panel';

export type WovenSurface = WovenWorkspaceSurface;

/**
 * One recorded session as the navigator presents it. Session records carry no
 * title, so the label is the recorded persona and the timestamp is formatted
 * from the record's own ISO string — never from a clock, so the markup is
 * deterministic on the server and in tests.
 */
export type NavigatorSessionEntry = {
  sessionId: string;
  label: string;
  when: string;
  surface: WovenSurface | null;
};

export type NavigatorSessionGroups = {
  bySurface: Record<WovenSurface, NavigatorSessionEntry[]>;
  all: NavigatorSessionEntry[];
};

type NavigatorProps = {
  activeSurface: WovenSurface;
  legacyHref: string;
  onOpenSurface: (surface: WovenSurface) => void;
  sessions?: readonly SessionRecord[];
  sessionSurfaces?: WovenSessionSurfaceMap;
  expandedSurfaces?: readonly WovenSurface[];
  liveSessionId?: string;
  selectedSessionId?: string;
  selectionDisabled?: boolean;
  sessionsLoading?: boolean;
  sessionsError?: string | null;
  onToggleSurfaceExpanded?: (surface: WovenSurface) => void;
  onSelectSession?: (sessionId: string) => void;
};

const SURFACES: ReadonlyArray<{ id: WovenSurface; label: string; note: string }> = [
  { id: 'dialogue', label: 'Dialogue', note: 'Primary human–agent conversation' },
  { id: 'workbench', label: 'Workbench', note: 'Documents, evidence & contracts' },
  { id: 'pipeline', label: 'Pipeline', note: 'DECOMP, PREP, TASK, and AUDIT intent' }
];

export const NAVIGATOR_RECENT_SESSION_LIMIT = 4;

const EMPTY_SESSIONS: readonly SessionRecord[] = [];
const EMPTY_SESSION_SURFACES: WovenSessionSurfaceMap = {};

const MONTH_LABELS = [
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec'
];

function formatSessionWhen(value: string | undefined): string {
  const match = /^(\d{4})-(\d{2})-(\d{2})/.exec(value ?? '');
  if (!match) {
    return '';
  }
  const month = MONTH_LABELS[Number(match[2]) - 1];
  if (!month) {
    return '';
  }
  return `${month} ${Number(match[3])}, ${match[1]}`;
}

function sessionOrderKey(session: SessionRecord): string {
  return session.updatedAt || session.createdAt || '';
}

/**
 * Pure projection of recorded sessions into the navigator's mode groups.
 * Attribution comes only from the local `sessionSurfaces` annotation; sessions
 * without one stay out of every mode group and appear in `all` only.
 */
export function buildNavigatorSessionGroups(
  sessions: readonly SessionRecord[],
  sessionSurfaces: WovenSessionSurfaceMap
): NavigatorSessionGroups {
  const ordered = [...sessions].sort((left, right) => {
    const leftKey = sessionOrderKey(left);
    const rightKey = sessionOrderKey(right);
    if (leftKey === rightKey) {
      return left.sessionId.localeCompare(right.sessionId);
    }
    return leftKey < rightKey ? 1 : -1;
  });

  const bySurface: Record<WovenSurface, NavigatorSessionEntry[]> = {
    dialogue: [],
    workbench: [],
    pipeline: []
  };
  const all: NavigatorSessionEntry[] = [];

  for (const session of ordered) {
    const surface = sessionSurfaces[session.sessionId] ?? null;
    const entry: NavigatorSessionEntry = {
      sessionId: session.sessionId,
      label: session.persona?.trim() || session.sessionId,
      when: formatSessionWhen(sessionOrderKey(session)),
      surface
    };
    all.push(entry);
    if (surface) {
      bySurface[surface].push(entry);
    }
  }

  return { bySurface, all };
}

function SessionRow({
  entry,
  live,
  selected,
  disabled,
  onSelectSession
}: {
  entry: NavigatorSessionEntry;
  live: boolean;
  selected: boolean;
  disabled: boolean;
  onSelectSession?: (sessionId: string) => void;
}): JSX.Element {
  return (
    <li>
      <button
        type="button"
        className={
          live
            ? 'woven-navigator-session woven-navigator-session--live'
            : 'woven-navigator-session'
        }
        data-session-id={entry.sessionId}
        disabled={disabled || !onSelectSession}
        aria-pressed={selected}
        onClick={() => {
          onSelectSession?.(entry.sessionId);
        }}
      >
        {live ? (
          <span
            className="woven-navigator-session-dot"
            role="img"
            aria-label="Live session"
          />
        ) : null}
        <span className="woven-navigator-session-title">{entry.label}</span>
        <span className="woven-navigator-session-when">{entry.when}</span>
      </button>
    </li>
  );
}

export function Navigator({
  activeSurface,
  legacyHref,
  onOpenSurface,
  sessions = EMPTY_SESSIONS,
  sessionSurfaces = EMPTY_SESSION_SURFACES,
  expandedSurfaces,
  liveSessionId,
  selectedSessionId,
  selectionDisabled = false,
  sessionsLoading = false,
  sessionsError = null,
  onToggleSurfaceExpanded,
  onSelectSession
}: NavigatorProps): JSX.Element {
  // Which group, if any, has escaped its mode scope to show every recorded
  // session. Transient by design: it is a reading affordance, not a preference.
  const [allSessionsSurface, setAllSessionsSurface] =
    React.useState<WovenSurface | null>(null);

  const groups = React.useMemo(
    () => buildNavigatorSessionGroups(sessions, sessionSurfaces),
    [sessions, sessionSurfaces]
  );

  return (
    <nav className="woven-navigator" aria-label="Workspace Navigator">
      <header className="woven-region-header">
        <div>
          <p className="woven-eyebrow">Workspace</p>
          <h2>Navigator</h2>
        </div>
      </header>

      <div className="woven-navigator-sections" aria-label="Workspace surfaces">
        {SURFACES.map((surface) => {
          const active = activeSurface === surface.id;
          const expanded = expandedSurfaces
            ? expandedSurfaces.includes(surface.id)
            : active;
          const showingAll = allSessionsSurface === surface.id;
          const scoped = groups.bySurface[surface.id];
          const visible = showingAll
            ? groups.all
            : scoped.slice(0, NAVIGATOR_RECENT_SESSION_LIMIT);

          return (
            <div
              key={surface.id}
              className={
                expanded
                  ? 'woven-navigator-group woven-navigator-group--expanded'
                  : 'woven-navigator-group'
              }
            >
              <button
                type="button"
                className={
                  active ? 'woven-nav-item woven-nav-item--active' : 'woven-nav-item'
                }
                aria-current={active ? 'page' : undefined}
                aria-expanded={expanded}
                onClick={() => {
                  if (active) {
                    onToggleSurfaceExpanded?.(surface.id);
                    return;
                  }
                  onOpenSurface(surface.id);
                }}
              >
                <span>{surface.label}</span>
                <small>{surface.note}</small>
                <span className="woven-navigator-chevron" aria-hidden="true">
                  {expanded ? '▾' : '▸'}
                </span>
              </button>

              {expanded ? (
                <div className="woven-navigator-sessions">
                  {sessionsError ? (
                    <p className="panel-error" role="alert">
                      {sessionsError}
                    </p>
                  ) : null}
                  {sessionsLoading ? (
                    <p className="panel-empty">Loading recorded sessions…</p>
                  ) : null}
                  {selectionDisabled ? (
                    <p className="woven-navigator-session-notice" role="status">
                      Session selection is paused while the primary dialogue is
                      running.
                    </p>
                  ) : null}
                  {!sessionsLoading && !sessionsError && visible.length === 0 ? (
                    <p className="panel-empty">
                      No recorded sessions for this surface.
                    </p>
                  ) : null}
                  {visible.length > 0 ? (
                    <ul
                      className="woven-navigator-session-list"
                      aria-label={`${surface.label} sessions`}
                    >
                      {visible.map((entry) => (
                        <SessionRow
                          key={entry.sessionId}
                          entry={entry}
                          live={
                            Boolean(liveSessionId) &&
                            entry.sessionId === liveSessionId
                          }
                          selected={entry.sessionId === selectedSessionId}
                          disabled={selectionDisabled}
                          onSelectSession={onSelectSession}
                        />
                      ))}
                    </ul>
                  ) : null}
                  {groups.all.length > 0 ? (
                    <p className="woven-navigator-more">
                      <button
                        type="button"
                        aria-expanded={showingAll}
                        onClick={() => {
                          setAllSessionsSurface(showingAll ? null : surface.id);
                        }}
                      >
                        {showingAll
                          ? 'Recent sessions'
                          : `All sessions (${groups.all.length})`}
                      </button>
                    </p>
                  ) : null}
                </div>
              ) : null}
            </div>
          );
        })}
      </div>

      <section className="woven-navigator-files" aria-label="Project files">
        <FileTreePanel />
      </section>

      <footer className="woven-compatibility">
        <p>Compatibility</p>
        <Link href={legacyHref} target="_blank" rel="noreferrer">
          Open legacy interface in a new window
        </Link>
      </footer>
    </nav>
  );
}
