'use client';

import React from 'react';
import type { RecordedAgentHierarchy } from '../../lib/woven-dialogue/contracts';
import { AgentsProjection } from './agents-projection';

type CoordinationPanelProps = {
  activeView: 'session' | 'agents';
  replaySlot?: React.ReactNode;
  hierarchy: RecordedAgentHierarchy;
  sessionsLoading: boolean;
  sessionsError: string | null;
  selectedSessionId?: string;
  selectionDisabled: boolean;
  onSelectView: (view: 'session' | 'agents') => void;
  onRefreshSessions: () => void;
  onSelectSession: (sessionId: string) => void;
};

export function CoordinationPanel({
  activeView,
  replaySlot,
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
          {(['session', 'agents'] as const).map((view) => (
            <button
              key={view}
              type="button"
              aria-pressed={activeView === view}
              className={activeView === view ? 'is-active' : undefined}
              onClick={() => {
                onSelectView(view);
              }}
            >
              {view === 'session' ? 'Session' : 'Agents'}
            </button>
          ))}
        </div>
      </header>
      <div className="woven-coordination-body">
        {activeView === 'session'
          ? replaySlot ?? (
              <p className="panel-empty">Select a recorded session to inspect its replay.</p>
            )
          : null}
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
