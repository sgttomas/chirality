'use client';

import React, { useState } from 'react';
import { SubagentStreamView } from '../shell/subagent-stream-view';
import { ToolStreamView } from '../shell/tool-stream-view';
import { TranscriptStreamView } from '../shell/transcript-stream-view';

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
