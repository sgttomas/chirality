'use client';

import React, { useMemo, useState } from 'react';
import type { HarnessEvent } from '@chirality/runtime-contracts/event-schema';
import { deriveToolActivity, deriveSubagentActivity } from '../../lib/shell/harness-event-views';
import { deriveTranscriptView } from '@chirality/runtime-contracts/transcript-replay';
import { useHarnessEvents } from '../workspace/harness-events-provider';
import { SubagentStreamView, SubagentStreamList } from '../shell/subagent-stream-view';
import { ToolStreamView, ToolStreamList } from '../shell/tool-stream-view';
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

/** Fixed status line; counts describe the observed buffer, never inferred work. */
export function ActivityStrip({ reconnectControl, onOpenDetails, running, events }: {
  reconnectControl?: React.ReactNode; onOpenDetails: () => void; running: boolean; events: readonly HarnessEvent[];
}): JSX.Element {
  const sessions = new Map<string, HarnessEvent[]>();
  for (const event of events) {
    const source = sessions.get(event.sessionId) ?? [];
    source.push(event); sessions.set(event.sessionId, source);
  }
  const actions = [...sessions.values()].reduce((count, source) => count + deriveToolActivity(source).length, 0);
  const children = [...sessions.values()].reduce((count, source) => count + deriveSubagentActivity(source).length, 0);
  const start = [...events].reverse().find(event => event.type === 'turn.started');
  const end = start ? [...events].reverse().find(event => event.sessionId === start.sessionId && Boolean(start.turnId) && event.turnId === start.turnId && ['turn.completed', 'turn.failed', 'turn.interrupted'].includes(event.type) && Date.parse(event.timestamp) >= Date.parse(start.timestamp)) : undefined;
  const elapsed = start && end ? Math.max(0, Date.parse(end.timestamp) - Date.parse(start.timestamp)) : undefined;
  return <div className="woven-activity-strip" aria-label="Activity status">
    {reconnectControl}
    <span role="status">{running ? 'Working' : 'Idle'}{actions || children ? ` · ${actions} actions · ${children} children observed` : ''}{elapsed !== undefined && Number.isFinite(elapsed) ? ` · Last turn: ${(elapsed / 1000).toFixed(1)} s` : ''}</span>
    <button type="button" onClick={onOpenDetails}>Details ›</button>
  </div>;
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
  const visible = (kind: string, row: { key: string }) => clearedVersions.get(`${kind}:${row.key}`) !== JSON.stringify(row) && (!query || JSON.stringify(row).toLocaleLowerCase().includes(query));
  const clearView = () => setClearedVersions(new Map([
    ...projected.tools.map(row => [`tools:${row.key}`, JSON.stringify(row)] as const),
    ...projected.children.map(row => [`children:${row.key}`, JSON.stringify(row)] as const),
    ...projected.transcript.map(row => [`transcript:${row.key}`, JSON.stringify(row)] as const)
  ]));
  return <section className="woven-activity-view" aria-label="Activity details">
    <div className="woven-activity-tabs" aria-label="Activity views">
      {TABS.map(item => <button type="button" key={item.id} aria-pressed={tab === item.id}
        onClick={() => setTab(item.id)}>{item.id === 'tools' ? 'Actions' : item.label}</button>)}
    </div>
    <div className="woven-activity-filter">
      <input aria-label="Filter activity" placeholder="Filter activity…" value={filter} onChange={event => setFilter(event.target.value)} />
      <button type="button" onClick={clearView}>Clear view</button>
    </div>
    {tab === 'tools' ? <ToolStreamList rows={projected.tools.filter(row => visible('tools', row))} /> : tab === 'events' ? <TranscriptStreamList items={projected.transcript.filter(row => visible('transcript', row))} /> : <SubagentStreamList rows={projected.children.filter(row => visible('children', row))} />}
  </section>;
}
