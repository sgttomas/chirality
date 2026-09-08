import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { AgentsProjection } from './production/src/components/woven-dialogue/agents-projection';
import { buildRecordedAgentHierarchy, type RecordedSessionEvidence } from './production/src/lib/woven-dialogue/recorded-agent-hierarchy';

const records: RecordedSessionEvidence[] = [
  {
    sessionId: 'session-root-supervisor-0123456789',
    sourceReference: 'synthetic://agent/root',
    observedAt: '2026-09-07T18:00:00Z',
    currency: 'CURRENT',
    persona: 'HELP_HUMAN',
    role: 'agent0',
    status: 'idle'
  },
  {
    sessionId: 'session-manager-working-items-abcdef',
    sourceReference: 'synthetic://agent/manager',
    observedAt: '2026-09-07T18:00:01Z',
    currency: 'CURRENT',
    persona: 'WORKING_ITEMS',
    role: 'agent1',
    status: 'running',
    parentSessionId: 'session-root-supervisor-0123456789'
  },
  {
    sessionId: 'session-specialist-review-fedcba',
    sourceReference: 'synthetic://agent/specialist-review',
    observedAt: '2026-09-07T18:00:02Z',
    currency: 'CURRENT',
    persona: 'REVIEW',
    role: 'agent2',
    status: 'completed',
    parentSessionId: 'session-manager-working-items-abcdef'
  },
  {
    sessionId: 'session-specialist-task-112233',
    sourceReference: 'synthetic://agent/specialist-task',
    observedAt: '2026-09-07T18:00:03Z',
    currency: 'CURRENT',
    persona: 'TASK',
    role: 'agent2',
    status: 'idle',
    parentSessionId: 'session-manager-working-items-abcdef'
  },
  {
    sessionId: 'session-unknown-445566',
    sourceReference: 'synthetic://agent/unknown',
    observedAt: '2026-09-07T18:00:04Z',
    currency: 'CURRENT',
    role: 'agent9',
    status: 'idle',
    parentSessionId: 'session-root-supervisor-0123456789'
  },
  {
    sessionId: 'session-detached-778899',
    sourceReference: 'synthetic://agent/detached',
    observedAt: '2026-09-07T18:00:05Z',
    currency: 'CURRENT',
    persona: 'RESEARCHER',
    role: 'agent2',
    status: 'interrupted',
    parentSessionId: 'session-missing-parent-secret-id'
  }
];

function Fixture(): JSX.Element {
  const params = new URLSearchParams(window.location.search);
  const [selectedSessionId, setSelectedSessionId] = useState<string>();
  const [loading, setLoading] = useState(false);
  const [refreshCount, setRefreshCount] = useState(0);
  const hierarchy = useMemo(() => buildRecordedAgentHierarchy(records), []);
  const selectionDisabled = params.get('disabled') === '1';
  const theme = params.get('theme') === 'dark' ? 'dark' : 'light';
  document.documentElement.dataset.theme = theme;

  return (
    <main className="fixture-shell" data-testid="fixture-shell" data-theme-state={theme}>
      <header className="fixture-heading">
        <p>Browser visual fixture · synthetic records</p>
        <span aria-live="polite">Refresh completed {refreshCount} time{refreshCount === 1 ? '' : 's'}.</span>
      </header>
      <div className="fixture-panel woven-coordination-body">
        <AgentsProjection
          hierarchy={hierarchy}
          loading={loading}
          selectedSessionId={selectedSessionId}
          selectionDisabled={selectionDisabled}
          error={null}
          onRefresh={() => {
            setLoading(true);
            window.setTimeout(() => {
              setRefreshCount((count) => count + 1);
              setLoading(false);
            }, 350);
          }}
          onSelectSession={setSelectedSessionId}
        />
      </div>
    </main>
  );
}

createRoot(document.getElementById('root')!).render(<Fixture />);
