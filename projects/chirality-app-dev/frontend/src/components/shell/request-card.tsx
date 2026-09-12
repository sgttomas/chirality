'use client';

import React, { useEffect, useMemo, useState } from 'react';
import type { ServerRequestAnswer } from '@chirality/runtime-contracts';
import { answerHarnessSessionRequest } from '../../lib/harness/client';
import {
  readElicitationMessage,
  readUserInputQuestions,
  selectPendingServerRequests,
  type ServerRequestRow,
  type UserInputQuestion
} from '../../lib/shell/harness-event-views';
import { useHarnessEvents } from '../workspace/harness-events-provider';

type RequestCardProps = {
  row: ServerRequestRow;
  pending: boolean;
  onAnswer: (row: ServerRequestRow, answer: ServerRequestAnswer) => void;
};

function methodLabel(row: ServerRequestRow): string {
  if (row.kind === 'userInput') return 'Codex needs your input';
  if (row.kind === 'elicitation') return 'A tool server asks for confirmation';
  return row.method;
}

function UserInputForm({ row, pending, onAnswer }: RequestCardProps): JSX.Element {
  const questions = useMemo(() => readUserInputQuestions(row.request), [row.request]);
  const [values, setValues] = useState<Record<string, string>>({});
  const complete = questions.length > 0 && questions.every((question) => Boolean(values[question.id]?.trim()));
  const answerFor = (question: UserInputQuestion): string => values[question.id]?.trim() ?? '';
  return (
    <form
      className="native-plan-clarification"
      onSubmit={(event) => {
        event.preventDefault();
        if (!complete || pending) return;
        onAnswer(row, {
          kind: 'userInput',
          answers: Object.fromEntries(questions.map((question) => [question.id, { answers: [answerFor(question)] }]))
        });
      }}
    >
      {questions.length === 0 ? <p>This request carries no questions. Inspect it in the Activity panel.</p> : null}
      {questions.map((question) => (
        <fieldset key={question.id}>
          <legend>{question.header}</legend>
          {question.question ? <p>{question.question}</p> : null}
          {question.options.map((option) => (
            <label key={option.label}>
              <input
                type="radio"
                name={`${row.requestId}:${question.id}`}
                value={option.label}
                checked={values[question.id] === option.label}
                disabled={pending}
                onChange={() => setValues((current) => ({ ...current, [question.id]: option.label }))}
              />
              <span>
                <strong>{option.label}</strong>
                {option.description ? <small>{option.description}</small> : null}
              </span>
            </label>
          ))}
          {question.isOther || question.options.length === 0 ? (
            <label className="native-plan-clarification-other">
              <span>{question.options.length === 0 ? 'Your answer' : 'Other answer'}</span>
              <input
                type={question.isSecret ? 'password' : 'text'}
                value={values[question.id] && !question.options.some((option) => option.label === values[question.id]) ? values[question.id] : ''}
                disabled={pending}
                autoComplete="off"
                onChange={(event) => setValues((current) => ({ ...current, [question.id]: event.target.value }))}
              />
            </label>
          ) : null}
        </fieldset>
      ))}
      <button type="submit" disabled={!complete || pending}>{pending ? 'Sending answers...' : 'Send answers'}</button>
    </form>
  );
}

function ElicitationForm({ row, pending, onAnswer }: RequestCardProps): JSX.Element {
  const message = readElicitationMessage(row.request);
  return (
    <div className="native-plan-clarification">
      {message ? <p>{message}</p> : <p>The tool server asked for confirmation without a message.</p>}
      <details>
        <summary>Request details</summary>
        <pre className="transcript-text">{JSON.stringify(row.request ?? null, null, 2)}</pre>
      </details>
      <div className="permission-card-actions">
        <button type="button" className="permission-card-approve" disabled={pending} onClick={() => onAnswer(row, { kind: 'elicitation', action: 'accept' })}>
          {pending ? 'Sending...' : 'Accept'}
        </button>
        <button type="button" className="button-muted permission-card-deny" disabled={pending} onClick={() => onAnswer(row, { kind: 'elicitation', action: 'decline' })}>
          Decline
        </button>
      </div>
    </div>
  );
}

/** One answerable Codex server request (user-input questions or an MCP elicitation). */
export function RequestCard({ row, pending, onAnswer }: RequestCardProps): JSX.Element {
  return (
    <article className="permission-card request-card" role="group" aria-label={`Request: ${methodLabel(row)}`}>
      <header className="permission-card-header">
        <span className="permission-card-tool" title={row.method}>{methodLabel(row)}</span>
        <span className="permission-card-badge">answer required</span>
      </header>
      {row.kind === 'userInput'
        ? <UserInputForm row={row} pending={pending} onAnswer={onAnswer} />
        : <ElicitationForm row={row} pending={pending} onAnswer={onAnswer} />}
    </article>
  );
}

type RequestCardsProps = {
  sessionId: string | null;
  requests: ServerRequestRow[];
  /** Request ids already presented elsewhere (the Plan Mode clarification card); hidden here. */
  suppressedRequestIds?: ReadonlySet<string>;
  answer?: typeof answerHarnessSessionRequest;
};

/**
 * Presentational list over already-derived pending requests, answering through
 * the session request route. The follow-up `codex.request.resolved` event
 * removes a card from the stream; a failed post keeps the card and shows why.
 */
export function RequestCards({ sessionId, requests, suppressedRequestIds, answer = answerHarnessSessionRequest }: RequestCardsProps): JSX.Element | null {
  const [pending, setPending] = useState<Record<string, true>>({});
  const [error, setError] = useState<string | null>(null);
  const visible = requests.filter((row) => !suppressedRequestIds?.has(row.requestId));
  const keys = visible.map((row) => row.key).join('|');

  useEffect(() => {
    const live = new Set(keys ? keys.split('|') : []);
    setPending((current) => {
      const next: Record<string, true> = {};
      let changed = false;
      for (const key of Object.keys(current)) {
        if (live.has(key)) next[key] = true;
        else changed = true;
      }
      return changed ? next : current;
    });
    if (live.size === 0) setError(null);
  }, [keys]);

  async function submit(row: ServerRequestRow, value: ServerRequestAnswer): Promise<void> {
    const targetSessionId = row.sessionId || sessionId;
    if (!targetSessionId) return;
    setPending((current) => ({ ...current, [row.key]: true }));
    setError(null);
    try {
      await answer({ sessionId: targetSessionId, requestId: row.requestId, answer: value });
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : 'Unable to send the answer.');
      setPending((current) => {
        const next = { ...current };
        delete next[row.key];
        return next;
      });
    }
  }

  if (visible.length === 0) return null;
  return (
    <section className="permission-card-list" role="region" aria-label="Pending requests" aria-live="polite">
      {visible.map((row) => (
        <RequestCard key={row.key} row={row} pending={Boolean(pending[row.key])} onAnswer={(target, value) => { void submit(target, value); }} />
      ))}
      {error ? <p className="permission-card-error">{error}</p> : null}
    </section>
  );
}

/** Live wrapper over the bridged event stream; `active` comes from the Runtime turn state. */
export function ServerRequests({ sessionId, active, suppressedRequestIds }: {
  sessionId: string | null;
  active: boolean;
  suppressedRequestIds?: ReadonlySet<string>;
}): JSX.Element | null {
  const { events } = useHarnessEvents();
  const pending = useMemo(() => selectPendingServerRequests(events, active), [events, active]);
  return <RequestCards sessionId={sessionId} requests={pending} suppressedRequestIds={suppressedRequestIds} />;
}
