'use client';

import React, { useEffect, useMemo, useState } from 'react';
import { decideHarnessPermission } from '../../lib/harness/client';
import {
  derivePermissionRequests,
  type PermissionRequestRow
} from '../../lib/shell/harness-event-views';
import { useHarnessEvents } from '../workspace/harness-events-provider';

type PermissionDecisionCardsProps = {
  sessionId: string | null;
  requests: PermissionRequestRow[];
};

/**
 * Presentational approval cards over already-derived pending requests,
 * decoupled from context so they can be rendered to static markup in tests.
 */
export function PermissionDecisionCards({
  sessionId,
  requests
}: PermissionDecisionCardsProps): JSX.Element | null {
  const [submitting, setSubmitting] = useState<Record<string, 'allow' | 'deny'>>({});
  const [error, setError] = useState<string | null>(null);

  const requestKeys = requests.map((row) => row.key).join('|');

  // Prune transient state for requests that are no longer pending (e.g. a new
  // turn cleared the stream) so it never bleeds into a later approval card.
  useEffect(() => {
    const live = new Set(requestKeys.length > 0 ? requestKeys.split('|') : []);
    setSubmitting((current) => {
      const next: Record<string, 'allow' | 'deny'> = {};
      let changed = false;
      for (const [key, value] of Object.entries(current)) {
        if (live.has(key)) {
          next[key] = value;
        } else {
          changed = true;
        }
      }
      return changed ? next : current;
    });
    if (live.size === 0) {
      setError(null);
    }
  }, [requestKeys]);

  async function decide(row: PermissionRequestRow, verdict: 'allow' | 'deny'): Promise<void> {
    if (!sessionId) {
      return;
    }
    setSubmitting((current) => ({ ...current, [row.key]: verdict }));
    setError(null);
    try {
      await decideHarnessPermission({ sessionId, toolUseId: row.key, verdict });
      // The follow-up tool.permission event removes this card from the stream.
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : 'Unable to submit decision.');
      setSubmitting((current) => {
        const next = { ...current };
        delete next[row.key];
        return next;
      });
    }
  }

  if (requests.length === 0) {
    return null;
  }

  return (
    <section
      className="permission-card-list"
      role="region"
      aria-label="Pending tool approvals"
      aria-live="polite"
    >
      {requests.map((row) => {
        const pendingVerdict = submitting[row.key];
        const pathEntries = Object.entries(row.pathFields);
        return (
          <article
            key={row.key}
            className="permission-card"
            role="group"
            aria-label={`Approval required: ${row.toolName}`}
          >
            <header className="permission-card-header">
              <span className="permission-card-tool" title={row.toolName}>
                {row.toolName}
              </span>
              <span className="permission-card-badge">approval required</span>
            </header>
            {row.reason ? <p className="permission-card-reason">{row.reason}</p> : null}
            {pathEntries.length > 0 ? (
              <ul className="permission-card-paths">
                {pathEntries.map(([field, value]) => (
                  <li key={field} title={`${field}: ${value}`}>
                    <span className="permission-card-path-field">{field}</span>
                    <span className="permission-card-path-value">{value}</span>
                  </li>
                ))}
              </ul>
            ) : null}
            <div className="permission-card-actions">
              <button
                type="button"
                className="permission-card-approve"
                disabled={Boolean(pendingVerdict) || !sessionId}
                onClick={() => {
                  void decide(row, 'allow');
                }}
              >
                {pendingVerdict === 'allow' ? 'Approving...' : 'Approve'}
              </button>
              <button
                type="button"
                className="button-muted permission-card-deny"
                disabled={Boolean(pendingVerdict) || !sessionId}
                onClick={() => {
                  void decide(row, 'deny');
                }}
              >
                {pendingVerdict === 'deny' ? 'Denying...' : 'Deny'}
              </button>
            </div>
          </article>
        );
      })}
      {error ? <p className="permission-card-error">{error}</p> : null}
    </section>
  );
}

/**
 * Live wrapper: reads the bridged harness-event stream and surfaces only the
 * gated tool calls awaiting an operator decision (DESIGN §3.1 approval cards).
 * Isolated from the chat transcript so its per-event re-renders stay cheap.
 */
export function PermissionRequests({ sessionId }: { sessionId: string | null }): JSX.Element | null {
  const { events } = useHarnessEvents();
  const pending = useMemo(
    () => derivePermissionRequests(events).filter((row) => row.status === 'pending'),
    [events]
  );
  return <PermissionDecisionCards sessionId={sessionId} requests={pending} />;
}
