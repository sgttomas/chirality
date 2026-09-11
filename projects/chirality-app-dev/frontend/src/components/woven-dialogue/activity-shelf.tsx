'use client';

import React, { useMemo, useState } from 'react';
import type { HarnessEvent } from '@chirality/runtime-contracts/event-schema';
import { deriveToolActivity, deriveSubagentActivity, type ToolActivityRow, type SubagentActivityRow } from '../../lib/shell/harness-event-views';
import { deriveTranscriptView } from '@chirality/runtime-contracts/transcript-replay';
import { useHarnessEvents } from '../workspace/harness-events-provider';
import { SubagentStreamView } from '../shell/subagent-stream-view';
import { ToolStreamView } from '../shell/tool-stream-view';
import { TranscriptStreamView, TranscriptStreamList } from '../shell/transcript-stream-view';

type ActivityTab = 'tools' | 'events' | 'children';

type ActivityShelfProps = {
  collapsed: boolean;
  onToggleCollapsed: () => void;
};

const TABS: ReadonlyArray<{ id: ActivityTab; label: string }> = [
  { id: 'tools', label: 'Tools' },
  { id: 'events', label: 'Events' },
  { id: 'children', label: 'Children' }
];

export function ActivityShelf({
  collapsed,
  onToggleCollapsed
}: ActivityShelfProps): JSX.Element {
  const [activeTab, setActiveTab] = useState<ActivityTab>('tools');

  return (
    <section className="woven-activity" aria-label="Activity Shelf">
      <header className="woven-activity-header">
        <div>
          <p className="woven-eyebrow">Live runtime projection</p>
          <h2>Activity</h2>
        </div>
        <div className="woven-activity-controls">
          {!collapsed ? (
            <div aria-label="Activity views">
              {TABS.map((tab) => (
                <button
                  key={tab.id}
                  type="button"
                  aria-pressed={activeTab === tab.id}
                  className={activeTab === tab.id ? 'is-active' : undefined}
                  onClick={() => {
                    setActiveTab(tab.id);
                  }}
                >
                  {tab.label}
                </button>
              ))}
            </div>
          ) : null}
          <button
            type="button"
            className="button-muted"
            aria-expanded={!collapsed}
            onClick={onToggleCollapsed}
          >
            {collapsed ? 'Expand activity' : 'Collapse activity'}
          </button>
        </div>
      </header>
      {!collapsed ? (
        <div className="woven-activity-body">
          {activeTab === 'tools' ? <ToolStreamView /> : null}
          {activeTab === 'events' ? <TranscriptStreamView /> : null}
          {activeTab === 'children' ? <SubagentStreamView /> : null}
        </div>
      ) : null}
    </section>
  );
}

type PrimaryTurnActivity = { actions: number; children: number; elapsed?: number };

/** Project only an explicitly identified, bounded primary turn in observation order. */
export function derivePrimaryTurnActivity(events: readonly HarnessEvent[], primarySessionId?: string): PrimaryTurnActivity | null {
  if (typeof primarySessionId !== 'string' || !primarySessionId.trim()) return null;
  const primary = events.filter(event => event.sessionId === primarySessionId);
  // A newer incomplete turn must not fall back to a completed older turn.
  const latest = [...primary].reverse().find(event => event.turnId !== undefined || event.type.startsWith('turn.'));
  if (typeof latest?.turnId !== 'string' || !latest.turnId.trim()) return null;
  const turn = primary.filter(event => event.turnId === latest.turnId);
  const starts = turn.filter(event => event.type === 'turn.started');
  const ends = turn.filter(event => ['turn.completed', 'turn.failed', 'turn.interrupted'].includes(event.type));
  if (starts.length !== 1 || ends.length > 1) return null;
  if ([...primary].reverse().find(event => event.type === 'turn.started') !== starts[0]) return null;
  const startIndex = turn.indexOf(starts[0]);
  const endIndex = ends.length ? turn.indexOf(ends[0]) : turn.length - 1;
  if (endIndex < startIndex || (ends.length && endIndex !== turn.length - 1)) return null;
  const observed = turn.slice(startIndex, endIndex + 1);
  const times = observed.map(event => Date.parse(event.timestamp));
  if (times.some((time, index) => !Number.isFinite(time) || (index > 0 && time < times[index - 1]))) return null;
  return {
    actions: deriveToolActivity(observed).length,
    children: deriveSubagentActivity(observed).length,
    elapsed: ends.length ? times[times.length - 1] - times[0] : undefined
  };
}

/** Fixed status line; counts describe the observed primary turn, never complete work. */
export function ActivityStrip({ reconnectControl, onOpenDetails, running, events, primarySessionId }: {
  reconnectControl?: React.ReactNode; onOpenDetails: () => void; running: boolean; events: readonly HarnessEvent[]; primarySessionId?: string;
}): JSX.Element {
  const observedTurn = derivePrimaryTurnActivity(events, primarySessionId);
  // Streaming may begin before its first event; do not label an older completed turn current.
  const turn = running && observedTurn?.elapsed !== undefined ? null : observedTurn;
  return <div className="woven-activity-strip" aria-label="Activity status">
    {reconnectControl}
    <span role="status">{running ? 'Working' : 'Idle'}{turn ? ` · ${turn.actions} actions · ${turn.children} children observed` : ''}{!running && turn?.elapsed !== undefined ? ` · Last turn: ${(turn.elapsed / 1000).toFixed(1)} s` : ''}</span>
    <button type="button" onClick={onOpenDetails}>Details ›</button>
  </div>;
}

// Presentation belongs to the mounted Activity view; the legacy shelf above
// retains its existing stream components and labels.
function actionSentence(row: ToolActivityRow): string {
  // These two operations are defined by the registered tool descriptors. Do not
  // infer a purpose or result from an unfamiliar name or from arbitrary inputs.
  const operation = row.toolName === 'read_file' ? { verb: 'read', ongoing: 'Reading', name: 'Read' }
    : row.toolName === 'write_file' ? { verb: 'write', ongoing: 'Writing', name: 'Write' } : undefined;
  if (!operation) return {
    queued: 'Action queued', permission: 'Action permission check', running: 'Action running',
    completed: 'Action completed', failed: 'Action failed'
  }[row.status];
  return {
    queued: `Queued to ${operation.verb} file`,
    permission: `Permission check to ${operation.verb} file`,
    running: `${operation.ongoing} file`,
    // A summary can finish an invocation without establishing a file effect.
    completed: `${operation.name} action finished`,
    failed: `Failed to ${operation.verb} file`
  }[row.status];
}

function taskSentence(row: SubagentActivityRow): string {
  const name = row.agentName === 'subagent' ? '' : row.agentName === 'HELP_HUMAN' ? 'Assistant'
    : /^[A-Z][A-Z0-9_]*$/.test(row.agentName)
      ? row.agentName.toLowerCase().split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')
      : row.agentName;
  return `Task ${row.status}${name ? `: ${name}` : ''}`;
}

function timeLabel(timestamp: string): string {
  const date = new Date(timestamp);
  return Number.isFinite(date.getTime())
    ? date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })
    : 'Time unavailable';
}

function actionDetail(row: ToolActivityRow): string {
  return [row.toolName === 'tool' ? 'Tool name unavailable' : row.toolName, row.source, row.surface,
    `${row.eventCount} event${row.eventCount === 1 ? '' : 's'}`, row.lastEventType].filter(Boolean).join(' · ');
}

function taskDetail(row: SubagentActivityRow): string {
  return [row.agentName === 'subagent' ? 'Agent name unavailable' : row.agentName,
    row.lastToolName ? `Last action: ${row.lastToolName}` : '', row.outputArtifactPath ? 'Recorded output path' : '',
    `${row.eventCount} event${row.eventCount === 1 ? '' : 's'}`, row.lastEventType].filter(Boolean).join(' · ');
}

function ActivityTime({ timestamp }: { timestamp: string }): JSX.Element {
  const date = new Date(timestamp);
  return Number.isFinite(date.getTime())
    ? <time className="harness-stream-meta" style={{ flexShrink: 0, whiteSpace: 'nowrap' }} dateTime={timestamp} title={timestamp}>{timeLabel(timestamp)}</time>
    : <span className="harness-stream-meta" style={{ flexShrink: 0, whiteSpace: 'nowrap' }} title={timestamp || 'No recorded timestamp'}>Time unavailable</span>;
}

function ActivityActions({ rows }: { rows: ToolActivityRow[] }): JSX.Element {
  return rows.length === 0 ? <p className="panel-empty">No matching actions.</p> : <ul className="harness-stream-list" aria-label="Actions">
    {rows.map(row => <li key={row.key} className={`harness-stream-item harness-stream-item--${row.status}`}>
      <div className="harness-stream-row">
        <span className="harness-stream-name" title={row.toolName}>{actionSentence(row)}</span>
        <ActivityTime timestamp={row.timestamp} />
      </div>
      <span className={`harness-status-badge harness-status-badge--${row.status}`}>{row.status === 'permission' ? 'Permission check' : row.status}</span>
      {Object.keys(row.pathFields).length > 0 ? <ul className="harness-stream-paths">
        {Object.entries(row.pathFields).map(([field, value]) => <li key={field} title={`${field}: ${value}`}>
          <span className="harness-stream-path-field">{field}</span>
          <span className="harness-stream-path-value">{value}</span>
        </li>)}
      </ul> : null}
      <p className="harness-stream-meta">{actionDetail(row)}</p>
    </li>)}
  </ul>;
}

function ActivityTasks({ rows }: { rows: SubagentActivityRow[] }): JSX.Element {
  return rows.length === 0 ? <p className="panel-empty">No matching tasks.</p> : <ul className="harness-stream-list" aria-label="Tasks">
    {rows.map(row => <li key={row.key} className={`harness-stream-item harness-stream-item--${row.status}`}>
      <div className="harness-stream-row">
        <span className="harness-stream-name" title={row.agentName}>{taskSentence(row)}</span>
        <ActivityTime timestamp={row.timestamp} />
      </div>
      <span className={`harness-status-badge harness-status-badge--${row.status}`}>{row.status}</span>
      {row.description ? <p className="harness-stream-description">{row.description}</p> : null}
      {row.summary ? <p className="harness-stream-summary">{row.summary}</p> : null}
      <p className="harness-stream-meta">{taskDetail(row)}</p>
    </li>)}
  </ul>;
}

export function ActivityView(): JSX.Element {
  const [tab, setTab] = useState<ActivityTab>('tools');
  const [filter, setFilter] = useState('');
  const [clearedVersions, setClearedVersions] = useState<ReadonlyMap<string, string>>(new Map());
  const { events } = useHarnessEvents();
  // Project the complete lifecycle before applying local visibility. Clearing
  // a row must not discard its completion event when a retained event updates.
  const projected = useMemo(() => {
    const sessions = new Map<string, HarnessEvent[]>();
    for (const event of events) sessions.set(event.sessionId, [...(sessions.get(event.sessionId) ?? []), event]);
    return {
      tools: [...sessions].flatMap(([session, source]) => deriveToolActivity(source).map(row => ({ ...row, key: `${session}:${row.key}` }))),
      children: [...sessions].flatMap(([session, source]) => deriveSubagentActivity(source).map(row => ({ ...row, key: `${session}:${row.key}` }))),
      transcript: [...sessions].flatMap(([session, source]) => deriveTranscriptView(source).items.map(row => ({ ...row, key: `${session}:${row.key}` })))
    };
  }, [events]);
  const query = filter.trim().toLocaleLowerCase();
  const visible = (kind: string, row: { key: string }, presentation = '') => clearedVersions.get(`${kind}:${row.key}`) !== JSON.stringify(row) && (!query || `${JSON.stringify(row)} ${presentation}`.toLocaleLowerCase().includes(query));
  const clearView = () => setClearedVersions(new Map([
    ...projected.tools.map(row => [`tools:${row.key}`, JSON.stringify(row)] as const),
    ...projected.children.map(row => [`children:${row.key}`, JSON.stringify(row)] as const),
    ...projected.transcript.map(row => [`transcript:${row.key}`, JSON.stringify(row)] as const)
  ]));
  return <section className="woven-activity-view" aria-label="Activity details">
    <div className="woven-activity-tabs" aria-label="Activity views">
      {TABS.map(item => <button type="button" key={item.id} aria-pressed={tab === item.id}
        onClick={() => setTab(item.id)}>{item.id === 'tools' ? 'Actions' : item.id === 'children' ? 'Tasks' : item.label}</button>)}
    </div>
    <div className="woven-activity-filter">
      <input aria-label="Filter activity" placeholder="Filter activity…" value={filter} onChange={event => setFilter(event.target.value)} />
      <button type="button" onClick={clearView}>Clear view</button>
    </div>
    {tab === 'tools' ? <ActivityActions rows={projected.tools.filter(row => visible('tools', row, `${actionSentence(row)} ${actionDetail(row)} ${timeLabel(row.timestamp)}`))} /> : tab === 'events' ? <TranscriptStreamList items={projected.transcript.filter(row => visible('transcript', row))} /> : <ActivityTasks rows={projected.children.filter(row => visible('children', row, `${taskSentence(row)} ${taskDetail(row)} ${timeLabel(row.timestamp)}`))} />}
  </section>;
}
