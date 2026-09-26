import React from 'react';
import type { LifecycleTransitionEvidence } from '../../lib/workspace/deliverable-api';

type LifecycleGateFieldsProps = {
  evidence: LifecycleTransitionEvidence;
  noteId: string;
  transitionAmendment: string;
  transitionRuling: string;
  onAmendmentChange: (value: string) => void;
  onRulingChange: (value: string) => void;
};

/**
 * Ruling and amendment inputs of a lifecycle transition form (App SPEC §4.3),
 * shown only where the transition API takes them. Rendered inside the form grid.
 */
export function LifecycleGateFields({
  evidence,
  noteId,
  transitionAmendment,
  transitionRuling,
  onAmendmentChange,
  onRulingChange
}: LifecycleGateFieldsProps): JSX.Element | null {
  const showRuling = evidence.ruling !== 'none';
  const showAmendment = evidence.amendment !== 'none';
  if (!showRuling && !showAmendment) {
    return null;
  }

  return (
    <>
      {showRuling ? (
        <label>
          {evidence.ruling === 'required' ? 'Ruling record (required)' : 'Ruling record (optional)'}
          <input
            name="ruling"
            value={transitionRuling}
            onChange={(event) => {
              onRulingChange(event.target.value);
            }}
            placeholder="path of the human ruling record in the project"
            required={evidence.ruling === 'required'}
            aria-describedby={noteId}
          />
        </label>
      ) : null}

      {showAmendment ? (
        <label>
          Accepted amendment (required)
          <input
            name="amendment"
            value={transitionAmendment}
            onChange={(event) => {
              onAmendmentChange(event.target.value);
            }}
            placeholder="amendment ID, or its snapshot or group-3 decision path"
            required
            aria-describedby={noteId}
          />
        </label>
      ) : null}
    </>
  );
}

/**
 * Short help for a human gate. It states what the App checks and what it does
 * not: the actor is caller-asserted, and `write_status.sh` is the anchored check.
 */
export function LifecycleGateNote({
  evidence,
  noteId
}: {
  evidence: LifecycleTransitionEvidence;
  noteId: string;
}): JSX.Element | null {
  if (!evidence.humanGate) {
    return null;
  }

  const lead =
    evidence.kind === 'ruled-reversal'
      ? 'Reversal from CHECKING needs the approval SHA and the ruling record; it removes the Checking Approval SHA. '
      : evidence.kind === 'amendment-reopen'
        ? 'Reopening needs an ACCEPTED amendment whose action register names this deliverable (MODIFY, or scope-changing RECLASSIFY); the App reads working-tree records only. '
        : '';

  return (
    <p className="pipeline-note" id={noteId}>
      {lead}
      The actor is asserted by the caller: the App checks these entries&apos; format, location and
      content, not that a human acted. <code>tools/scaffolding/write_status.sh</code> is the anchored
      check.
    </p>
  );
}
