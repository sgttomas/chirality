'use client';

import React from 'react';
import type {
  OperatorSessionProjection,
  RecordedAgentHierarchy
} from '../../lib/woven-dialogue/contracts';

type AgentsProjectionProps = {
  hierarchy: RecordedAgentHierarchy;
  loading: boolean;
  error: string | null;
  selectedSessionId?: string;
  selectionDisabled: boolean;
  onRefresh: () => void;
  onSelectSession: (sessionId: string) => void;
};

function attributionLabel(session: OperatorSessionProjection): string {
  const selection = [session.adapterId, session.providerId].filter(Boolean);
  if (session.model) {
    selection.push(`selected model: ${session.model}`);
  }
  return selection.length > 0 ? selection.join(' · ') : 'Engine attribution not recorded';
}

function SessionCard({
  session,
  depth,
  childrenByParentSessionId,
  selectedSessionId,
  selectionDisabled,
  onSelectSession
}: {
  session: OperatorSessionProjection;
  depth: number;
  childrenByParentSessionId: RecordedAgentHierarchy['childrenByParentSessionId'];
  selectedSessionId?: string;
  selectionDisabled: boolean;
  onSelectSession: (sessionId: string) => void;
}): JSX.Element {
  const children = childrenByParentSessionId[session.sessionId] ?? [];

  return (
    <li className="woven-agent-branch">
      <button
        type="button"
        className={
          selectedSessionId === session.sessionId
            ? 'woven-agent-card woven-agent-card--selected'
            : 'woven-agent-card'
        }
        style={{ '--agent-depth': depth } as React.CSSProperties}
        disabled={selectionDisabled}
        aria-pressed={selectedSessionId === session.sessionId}
        onClick={() => {
          onSelectSession(session.sessionId);
        }}
      >
        <span className="woven-agent-card-topline">
          <strong>{session.role ?? 'Role not recorded'}</strong>
          <span>{session.runtimeStatus ?? 'status unknown'}</span>
        </span>
        <span>{session.persona ?? session.sessionId}</span>
        <small>{attributionLabel(session)}</small>
        <small>Currency: {session.currency}</small>
        {session.parentage.state === 'RECORDED' ? (
          <small>
            Recorded parent: <code>{session.parentage.parentSessionId}</code>{' '}
            ({session.parentage.parentAvailable ? 'record available' : 'record unavailable'})
          </small>
        ) : (
          <small>Recorded parent: not recorded</small>
        )}
        <small>
          Source: <code>{session.sourceReference}</code>
        </small>
        <small>Observed: {session.observedAt}</small>
        {session.outputArtifactReference ? (
          <small>
            Return: <code>{session.outputArtifactReference}</code>
          </small>
        ) : null}
        {session.approvalEvidenceReference ? (
          <small>
            Approval evidence: <code>{session.approvalEvidenceReference}</code>
          </small>
        ) : null}
        {session.diagnostics.length > 0 ? (
          <span className="woven-agent-diagnostics" role="status">
            {session.diagnostics.map((diagnostic) => (
              <small key={diagnostic.code}>
                {diagnostic.code}: {diagnostic.message}
              </small>
            ))}
          </span>
        ) : null}
        <small>
          Session: <code>{session.sessionId}</code>
        </small>
      </button>
      {children.length > 0 ? (
        <ol className="woven-agent-children" aria-label={`Children of ${session.sessionId}`}>
          {children.map((child) => (
            <SessionCard
              key={child.sessionId}
              session={child}
              depth={depth + 1}
              childrenByParentSessionId={childrenByParentSessionId}
              selectedSessionId={selectedSessionId}
              selectionDisabled={selectionDisabled}
              onSelectSession={onSelectSession}
            />
          ))}
        </ol>
      ) : null}
    </li>
  );
}

export function AgentsProjection({
  hierarchy,
  loading,
  error,
  selectedSessionId,
  selectionDisabled,
  onRefresh,
  onSelectSession
}: AgentsProjectionProps): JSX.Element {
  return (
    <section className="woven-projection" aria-label="Recorded agent sessions">
      <div className="woven-projection-toolbar">
        <p>
          Recorded sessions and exact parent links only. This view is not an editable work graph.
        </p>
        <button type="button" className="button-muted" disabled={loading} onClick={onRefresh}>
          {loading ? 'Refreshing…' : 'Refresh'}
        </button>
      </div>

      {selectionDisabled ? (
        <p className="woven-projection-notice" role="status">
          Session selection is paused while the primary dialogue is running.
        </p>
      ) : null}
      {error ? (
        <p className="panel-error" role="alert">
          {error}
        </p>
      ) : null}

      {!loading && hierarchy.roots.length === 0 ? (
        hierarchy.detached.length === 0 ? (
          <p className="panel-empty">No recorded sessions are available for this Working Root.</p>
        ) : null
      ) : (
        <ol className="woven-agent-tree" aria-label="Sessions without a recorded parent">
          {hierarchy.roots.map((session) => (
            <SessionCard
              key={session.sessionId}
              session={session}
              depth={0}
              childrenByParentSessionId={hierarchy.childrenByParentSessionId}
              selectedSessionId={selectedSessionId}
              selectionDisabled={selectionDisabled}
              onSelectSession={onSelectSession}
            />
          ))}
        </ol>
      )}

      {hierarchy.detached.length > 0 ? (
        <section className="woven-detached-agents" aria-label="Sessions with unresolved relationships">
          <h3>Relationships unavailable or conflicting</h3>
          <p>
            These sessions are recorded, but their parent links cannot form a safe hierarchy.
            They are shown without inferred placement.
          </p>
          <ol className="woven-agent-tree">
            {hierarchy.detached.map((session) => (
              <SessionCard
                key={session.sessionId}
                session={session}
                depth={0}
                childrenByParentSessionId={{}}
                selectedSessionId={selectedSessionId}
                selectionDisabled={selectionDisabled}
                onSelectSession={onSelectSession}
              />
            ))}
          </ol>
        </section>
      ) : null}

      {hierarchy.unresolvedParentSessionIds.length > 0 ? (
        <div className="woven-unresolved-parents">
          <h3>Parent records unavailable</h3>
          <ul>
            {hierarchy.unresolvedParentSessionIds.map((sessionId) => (
              <li key={sessionId}>{sessionId}</li>
            ))}
          </ul>
        </div>
      ) : null}

      {hierarchy.diagnostics.length > 0 ? (
        <section className="woven-hierarchy-diagnostics" aria-label="Hierarchy disclosures">
          <h3>Hierarchy disclosures</h3>
          <ul>
            {hierarchy.diagnostics.map((diagnostic, index) => (
              <li key={`${diagnostic.code}:${index}`}>
                <strong>{diagnostic.code}</strong>: {diagnostic.message}
              </li>
            ))}
          </ul>
        </section>
      ) : null}
    </section>
  );
}
