'use client';

import React from 'react';
import type { TranscriptItem } from '@chirality/harness-contract/transcript-replay';
import type {
  ProjectionDiagnostic,
  SelectedSessionReplayProjection,
  SelectedSessionReplayState
} from '../../lib/woven-dialogue/contracts';

export type SelectedSessionReplayLensProps = {
  state: SelectedSessionReplayState;
  primarySessionId?: string;
  onReturnToPrimary: () => void;
  onRetry?: () => void;
};

function ReplayHeader({
  selectedSessionId,
  primarySessionId,
  onReturnToPrimary
}: {
  selectedSessionId: string;
  primarySessionId?: string;
  onReturnToPrimary: () => void;
}): JSX.Element {
  return (
    <header className="woven-replay-header">
      <div>
        <p className="woven-replay-eyebrow">Replay — read-only</p>
        <h2>Recorded session</h2>
        <p>
          <span>Selected session: </span>
          <code>{selectedSessionId}</code>
        </p>
        {primarySessionId ? (
          <p>
            <span>Primary dialogue remains mounted: </span>
            <code>{primarySessionId}</code>
          </p>
        ) : null}
      </div>
      <button type="button" onClick={onReturnToPrimary}>
        Return to primary dialogue
      </button>
    </header>
  );
}

function DiagnosticList({
  diagnostics
}: {
  diagnostics: readonly ProjectionDiagnostic[];
}): JSX.Element | null {
  if (diagnostics.length === 0) {
    return null;
  }

  return (
    <ul className="woven-replay-diagnostics" aria-label="Replay disclosures">
      {diagnostics.map((diagnostic, index) => (
        <li key={`${diagnostic.code}:${index}`}>
          <strong>{diagnostic.code}</strong>: {diagnostic.message}
        </li>
      ))}
    </ul>
  );
}

function TranscriptItemView({ item }: { item: TranscriptItem }): JSX.Element {
  const artifactReference =
    item.artifact?.artifactRelativePath ?? item.artifact?.artifactPath;

  return (
    <li className="woven-replay-item">
      <div>
        <strong>{item.title}</strong>
        <span> — {item.status}</span>
      </div>
      {item.text ? <p>{item.text}</p> : null}
      {item.summary ? <p>{item.summary}</p> : null}
      {artifactReference ? (
        <p>
          <span>Artifact reference: </span>
          <code>{artifactReference}</code>
        </p>
      ) : null}
      <p>
        <span>Event: </span>
        <code>{item.eventId}</code>
        <span> / {item.eventType}</span>
      </p>
    </li>
  );
}

function ReadyReplay({
  projection
}: {
  projection: SelectedSessionReplayProjection;
}): JSX.Element {
  const attribution = projection.session;

  return (
    <>
      <section
        className="woven-replay-provenance"
        aria-label="Replay provenance and status"
      >
        <dl>
          <dt>Source</dt>
          <dd>
            <code>{projection.sourceReference}</code>
          </dd>
          <dt>Observed</dt>
          <dd>{projection.observedAt}</dd>
          <dt>Disclosure</dt>
          <dd>{projection.disclosure}</dd>
          <dt>Currency</dt>
          <dd>{projection.currency}</dd>
          <dt>Events</dt>
          <dd>{projection.sourceEventCount}</dd>
          <dt>Transcript items shown</dt>
          <dd>
            {projection.bounded
              ? `${projection.bounded.rendered} of ${projection.bounded.available}`
              : projection.renderedItemCount}
          </dd>
          <dt>Malformed records skipped</dt>
          <dd>{projection.malformedLineCount}</dd>
        </dl>
        {attribution ? (
          <dl aria-label="Recorded session attribution">
            {attribution.persona ? (
              <>
                <dt>Persona</dt>
                <dd>{attribution.persona}</dd>
              </>
            ) : null}
            {attribution.role ? (
              <>
                <dt>Role</dt>
                <dd>{attribution.role}</dd>
              </>
            ) : null}
            {attribution.runtimeStatus ? (
              <>
                <dt>Recorded runtime status</dt>
                <dd>{attribution.runtimeStatus}</dd>
              </>
            ) : null}
            {attribution.adapterId ? (
              <>
                <dt>Adapter</dt>
                <dd>{attribution.adapterId}</dd>
              </>
            ) : null}
            {attribution.providerId ? (
              <>
                <dt>Provider</dt>
                <dd>{attribution.providerId}</dd>
              </>
            ) : null}
            {attribution.model ? (
              <>
                <dt>Recorded model selection</dt>
                <dd>{attribution.model}</dd>
              </>
            ) : null}
            {attribution.residencyEpoch ? (
              <>
                <dt>Residency epoch</dt>
                <dd>{attribution.residencyEpoch}</dd>
              </>
            ) : null}
          </dl>
        ) : (
          <p>Session metadata unavailable; event evidence only.</p>
        )}
      </section>

      <DiagnosticList diagnostics={projection.diagnostics} />

      <section className="woven-replay-transcript" aria-label="Read-only transcript">
        {projection.transcript.items.length === 0 ? (
          <p>
            {projection.disclosure === 'EVIDENCE_ONLY'
              ? 'No transcript items were recorded; canonical event evidence may still exist.'
              : 'No transcript items were recorded for this session.'}
          </p>
        ) : (
          <ol>
            {projection.transcript.items.map((item) => (
              <TranscriptItemView key={item.key} item={item} />
            ))}
          </ol>
        )}
      </section>
    </>
  );
}

/**
 * Observational presentation only. The component intentionally exposes no
 * send, continue, interrupt, permission, resume, boot, delete, or lifecycle
 * action.
 */
export function SelectedSessionReplayLens({
  state,
  primarySessionId,
  onReturnToPrimary,
  onRetry
}: SelectedSessionReplayLensProps): JSX.Element | null {
  if (state.status === 'IDLE') {
    return null;
  }

  const selectedSessionId =
    state.status === 'READY'
      ? state.projection.selectedSessionId
      : state.selectedSessionId;

  return (
    <section
      className="woven-replay-lens"
      aria-label="Selected-session read-only replay"
      data-replay-state={state.status}
      data-replay-disclosure={
        state.status === 'READY' ? state.projection.disclosure : undefined
      }
    >
      <ReplayHeader
        selectedSessionId={selectedSessionId}
        primarySessionId={primarySessionId}
        onReturnToPrimary={onReturnToPrimary}
      />

      {state.status === 'LOADING' ? (
        <p role="status">Loading canonical replay evidence…</p>
      ) : null}

      {state.status === 'UNAVAILABLE' ? (
        <div role="alert">
          <p>Replay unavailable: {state.message}</p>
          {onRetry ? (
            <button type="button" onClick={onRetry}>
              Retry
            </button>
          ) : null}
        </div>
      ) : null}

      {state.status === 'READY' ? (
        <ReadyReplay projection={state.projection} />
      ) : null}
    </section>
  );
}
