'use client';

import Link from 'next/link';
import React from 'react';
import { handoffDocument } from '../shell/document-view';
import type { SessionRecord } from '@chirality/runtime-contracts/types';
import type {
  WovenSessionSurfaceMap,
  WovenWorkspaceSurface
} from '../../lib/woven-dialogue/woven-workspace-state';

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
  persona: string | undefined;
  projectRoot: string | undefined;
  when: string;
  surface: WovenSurface | null;
};

export type NavigatorSessionGroups = {
  bySurface: Record<WovenSurface, NavigatorSessionEntry[]>;
  all: NavigatorSessionEntry[];
};

type NavigatorProps = {
  footerSlot?: React.ReactNode;
  onNewChat?: () => void;
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

function personaLabel(persona: string | undefined, sessionId: string): string {
  const value = persona?.trim();
  if (!value) return sessionId;
  if (value === 'HELP_HUMAN') return 'Assistant';
  return /^[A-Z][A-Z0-9_]*$/.test(value)
    ? value.toLowerCase().split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')
    : value;
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
      label: personaLabel(session.persona, session.sessionId),
      persona: session.persona,
      projectRoot: session.projectRoot,
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
  const [pending, setPending] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);
  const active = React.useRef(true);
  const inFlight = React.useRef(false);
  const noticeId = React.useId();
  React.useEffect(() => {
    active.current = true;
    return () => { active.current = false; };
  }, []);

  async function reveal(): Promise<void> {
    if (inFlight.current) return;
    const root = entry.projectRoot;
    // Do not repair or replace a recorded root. Native policy remains the
    // authority for directory existence, canonical containment and sender access.
    if (typeof root !== 'string' || !root.startsWith('/') || /[\x00-\x1f\x7f]/.test(root)) {
      setError('This chat has no valid recorded folder to reveal.');
      return;
    }
    inFlight.current = true;
    setPending(true);
    setError(null);
    try {
      await handoffDocument({ action: 'reveal-root', projectRoot: root });
    } catch (failure) {
      if (active.current) {
        const message = failure instanceof Error ? failure.message.trim() : '';
        setError(message || 'Unable to reveal this chat’s folder. Try again.');
      }
    } finally {
      inFlight.current = false;
      if (active.current) setPending(false);
    }
  }

  return (
    <li>
      <div className="woven-navigator-session-row">
        <button
          type="button"
          className={
            live
              ? 'woven-navigator-session woven-navigator-session--live'
              : 'woven-navigator-session'
          }
          title={`${entry.persona ? `${entry.persona} · ` : ''}${entry.sessionId}${entry.surface ? ` · Recorded surface: ${entry.surface}` : ''}`}
          data-session-id={entry.sessionId}
          disabled={disabled || !onSelectSession}
          aria-pressed={selected}
          onClick={() => {
            if (!disabled) onSelectSession?.(entry.sessionId);
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
        <button
          type="button"
          className="woven-navigator-session-reveal"
          aria-label={`${pending ? 'Revealing' : error ? 'Retry revealing' : 'Reveal'} folder for ${entry.label} (${entry.sessionId})`}
          title={`Reveal in Finder · ${entry.projectRoot || 'No recorded folder'}`}
          aria-describedby={error ? noticeId : undefined}
          aria-busy={pending}
          disabled={pending}
          onClick={() => { void reveal(); }}
        >
          <svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M3 7V5a1 1 0 0 1 1-1h5l2 3h9a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V7Z" />
            <path d="M9 13h6m-3-3 3 3-3 3" />
          </svg>
        </button>
      </div>
      {error ? <p id={noticeId} className="panel-error" role="alert">{error}</p> : null}
    </li>
  );
}

export function Navigator({
  activeSurface,
  footerSlot,
  onNewChat,
  legacyHref,
  onOpenSurface,
  sessions = EMPTY_SESSIONS,
  sessionSurfaces = EMPTY_SESSION_SURFACES,
  liveSessionId,
  selectedSessionId,
  selectionDisabled = false,
  sessionsLoading = false,
  sessionsError = null,
  onSelectSession
}: NavigatorProps): JSX.Element {
  const groups = React.useMemo(
    () => buildNavigatorSessionGroups(sessions, sessionSurfaces),
    [sessions, sessionSurfaces]
  );

  return (
    <nav className="woven-navigator" aria-label="Workspace Navigator">
      <header className="woven-navigator-brand">Chirality</header>

      <div className="woven-navigator-sections" aria-label="Workspace surfaces">
        {onNewChat ? <button type="button" className="woven-new-chat" disabled={selectionDisabled} onClick={onNewChat}><span aria-hidden="true">＋</span> New chat</button> : null}
        <button type="button" className="woven-nav-item woven-nav-item--active"
          aria-current={activeSurface === 'dialogue' ? 'page' : undefined}
          onClick={() => onOpenSurface('dialogue')}>
          <span>Current chat</span>
        </button>
        <div className="woven-navigator-sessions">
          {sessionsError ? <p className="panel-error" role="alert">{sessionsError}</p> : null}
          {sessionsLoading ? <p className="panel-empty">Loading recorded sessions…</p> : null}
          {selectionDisabled ? <p role="status">Paused while a turn is running.</p> : null}
          {!sessionsLoading && !sessionsError && groups.all.length === 0 ? <p className="panel-empty">No recorded sessions.</p> : null}
          <ul className="woven-navigator-session-list" aria-label="Recorded sessions">
            {groups.all.map(entry => <SessionRow key={JSON.stringify([entry.sessionId, entry.projectRoot])} entry={entry}
              live={entry.sessionId === liveSessionId} selected={entry.sessionId === selectedSessionId}
              disabled={selectionDisabled} onSelectSession={onSelectSession} />)}
          </ul>
        </div>
      </div>

      <footer className="woven-compatibility">
        {footerSlot}
        {!footerSlot ? <Link href={legacyHref} target="_blank" rel="noreferrer" aria-label="Open legacy interface in a new window">
          Legacy window
        </Link> : null}
      </footer>
    </nav>
  );
}
