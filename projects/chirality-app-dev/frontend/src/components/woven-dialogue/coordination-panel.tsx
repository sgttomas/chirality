'use client';

import React from 'react';
import type {
  CoordinationPanelView,
  CoordinationWorkItem,
  RecordedAgentHierarchy
} from '../../lib/woven-dialogue/contracts';
import { AgentsProjection } from './agents-projection';
import { WorkProjection } from './work-projection';

type CoordinationPanelProps = {
  activeView: CoordinationPanelView;
  workItems: readonly CoordinationWorkItem[];
  hierarchy: RecordedAgentHierarchy;
  sessionsLoading: boolean;
  sessionsError: string | null;
  selectedSessionId?: string;
  selectionDisabled: boolean;
  onSelectView: (view: CoordinationPanelView) => void;
  onRefreshSessions: () => void;
  onSelectSession: (sessionId: string) => void;
};

export function CoordinationPanel({
  activeView,
  workItems,
  hierarchy,
  sessionsLoading,
  sessionsError,
  selectedSessionId,
  selectionDisabled,
  onSelectView,
  onRefreshSessions,
  onSelectSession
}: CoordinationPanelProps): JSX.Element {
  return (
    <section className="woven-coordination" aria-label="Coordination Panel">
      <header className="woven-region-header">
        <div>
          <p className="woven-eyebrow">Recorded coordination</p>
          <h2>Coordination</h2>
        </div>
        <div className="woven-coordination-tabs" aria-label="Coordination views">
          {(['work', 'agents'] as const).map((view) => (
            <button
              key={view}
              type="button"
              aria-pressed={activeView === view}
              className={activeView === view ? 'is-active' : undefined}
              onClick={() => {
                onSelectView(view);
              }}
            >
              {view === 'work' ? 'Work' : 'Agents'}
            </button>
          ))}
        </div>
      </header>
      <div className="woven-coordination-body">
        {activeView === 'work' ? <WorkProjection items={workItems} /> : null}
        {activeView === 'agents' ? (
          <AgentsProjection
            hierarchy={hierarchy}
            loading={sessionsLoading}
            error={sessionsError}
            selectedSessionId={selectedSessionId}
            selectionDisabled={selectionDisabled}
            onRefresh={onRefreshSessions}
            onSelectSession={onSelectSession}
          />
        ) : null}
      </div>
    </section>
  );
}
