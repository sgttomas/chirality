'use client';

import React, { useEffect, useState } from 'react';
import type { NativePlanClarification, NativePlanRevision } from '@chirality/runtime-contracts/v3';
import { nativePlanText } from '../../lib/harness/native-plan-text';
import { ChatMarkdown } from './chat-markdown';

/**
 * Everything the Plan tab needs, built by the chat panel (which owns the
 * session's plan state and the composer the actions write into) and rendered
 * by the right sidebar. Handlers are stable so the model changes only when the
 * plan itself does.
 */
export type NativePlanPanelModel = {
  sessionId?: string;
  revisions: readonly NativePlanRevision[];
  clarifications: readonly NativePlanClarification[];
  /** Plan Mode is the current interaction mode. */
  active: boolean;
  refreshing: boolean;
  projectRoot?: string;
  fileCatalog: readonly string[];
  clarificationPendingId?: string | number;
  clarificationError?: string | null;
  exportStatus?: string | null;
  actionsDisabled: boolean;
  onOpenFile?: (path: string) => void;
  onRefresh: () => void;
  onRevise: (revision: number | undefined) => void;
  onSave: (revision: NativePlanRevision) => void;
  onExecute: (revision: NativePlanRevision) => void;
  onSaveAsWorkflow: (revision: NativePlanRevision) => void;
  onReplyClarification: (clarification: NativePlanClarification, answers: Record<string, { answers: string[] }>) => void;
};

export function NativePlanClarificationCard({ clarification, pending, onReply }: {
  clarification: NativePlanClarification;
  pending: boolean;
  onReply: (clarification: NativePlanClarification, answers: Record<string, { answers: string[] }>) => void;
}): JSX.Element {
  const [values, setValues] = useState<Record<string, string>>({});
  const complete = clarification.questions.every(question => Boolean(values[question.id]?.trim()));
  return <form className="native-plan-clarification" onSubmit={event => {
    event.preventDefault();
    if (!complete || pending) return;
    onReply(clarification, Object.fromEntries(clarification.questions.map(question => [question.id, { answers: [values[question.id]!.trim()] }])));
  }}>
    <p className="native-plan-sidebar-meta">Planning needs your input{clarification.isBlocking ? ' before it can continue' : ''}.</p>
    {clarification.questions.map(question => <fieldset key={question.id}>
      <legend>{question.header}</legend>
      <p>{question.question}</p>
      {question.options.map(option => <label key={option.label}><input type="radio" name={`${String(clarification.requestId)}:${question.id}`} value={option.label}
        checked={values[question.id] === option.label} disabled={pending}
        onChange={() => setValues(current => ({ ...current, [question.id]: option.label }))} />
        <span><strong>{option.label}</strong>{option.description ? <small>{option.description}</small> : null}</span></label>)}
      {question.isOther ? <label className="native-plan-clarification-other"><span>Other answer</span><input type={question.isSecret ? 'password' : 'text'} value={values[question.id] && !question.options.some(option => option.label === values[question.id]) ? values[question.id] : ''}
        disabled={pending} autoComplete="off" onChange={event => setValues(current => ({ ...current, [question.id]: event.target.value }))} /></label> : null}
    </fieldset>)}
    <button type="submit" disabled={!complete || pending}>{pending ? 'Sending answers…' : 'Continue planning'}</button>
  </form>;
}

/**
 * The Plan tab. Shows the current revision, its actions, the earlier
 * revisions, and any clarification Codex is waiting on. `focusRevision`
 * (from a "Plan · Revision N" link in the conversation) opens that revision.
 */
export function NativePlanPanel({ model, focusRevision }: { model: NativePlanPanelModel | null; focusRevision?: { revision: number; sequence: number } }): JSX.Element {
  const [openRevision, setOpenRevision] = useState<number | null>(null);
  useEffect(() => { setOpenRevision(focusRevision ? focusRevision.revision : null); }, [focusRevision]);
  if (!model) {
    return <section className="native-plan-sidebar native-plan-sidebar--empty" aria-label="Plan">
      <p>No plan in this chat yet. Choose Plan Mode in the conversation to start one.</p>
    </section>;
  }
  const { revisions, clarifications, active, refreshing, clarificationPendingId, clarificationError, exportStatus, projectRoot, fileCatalog, onOpenFile, actionsDisabled } = model;
  const current = revisions.at(-1);
  const focusIsCurrent = current !== undefined && openRevision === current.revision;
  return <section className="native-plan-sidebar" aria-label="Plan">
    <header>
      <div><p className="woven-eyebrow">Plan Mode</p><h2>{current ? `Revision ${current.revision}` : 'Current plan'}</h2></div>
      <button type="button" className="button-muted" disabled={refreshing} onClick={model.onRefresh}>{refreshing ? 'Refreshing…' : 'Refresh'}</button>
    </header>
    {clarifications.map(clarification => <NativePlanClarificationCard key={String(clarification.requestId)} clarification={clarification}
      pending={clarificationPendingId === clarification.requestId} onReply={model.onReplyClarification} />)}
    {clarificationError ? <p className="panel-error" role="alert">{clarificationError}</p> : null}
    {!current ? <p>{active ? 'Describe what you want to plan in the conversation. The first revision will appear here.' : 'Switch to Plan Mode to inspect and revise a plan in this conversation.'}</p> : <>
      <p className="native-plan-sidebar-meta">Current plan · read-only</p>
      <div className="native-plan-sidebar-body" data-plan-revision={current.revision} data-plan-focused={focusIsCurrent ? 'true' : undefined}><ChatMarkdown source={nativePlanText(current)} projectRoot={projectRoot} fileCatalog={fileCatalog} onOpenFile={onOpenFile} /></div>
      <div className="native-plan-sidebar-actions">
        <button type="button" disabled={actionsDisabled} onClick={() => model.onRevise(current.revision)}>Revise in chat</button>
        <button type="button" disabled={actionsDisabled} onClick={() => model.onExecute(current)}>Execute plan</button>
        <button type="button" disabled={actionsDisabled} className="button-muted" onClick={() => model.onSaveAsWorkflow(current)}>Save as workflow in chat</button>
        <button type="button" className="button-muted" onClick={() => model.onSave(current)}>Save plan…</button>
      </div>
      {exportStatus ? <p role="status" className="native-plan-sidebar-meta">{exportStatus}</p> : null}
      {revisions.length > 1 ? <details className="native-plan-history" open={openRevision !== null && !focusIsCurrent ? true : undefined}><summary>Earlier revisions ({revisions.length - 1})</summary>
        <ol>{revisions.slice(0, -1).reverse().map(revision => <li key={revision.revision}><details open={openRevision === revision.revision ? true : undefined} data-plan-revision={revision.revision}><summary>Revision {revision.revision}</summary><div><ChatMarkdown source={nativePlanText(revision)} projectRoot={projectRoot} fileCatalog={fileCatalog} onOpenFile={onOpenFile} /></div><button type="button" className="button-muted" onClick={() => model.onSave(revision)}>Save this revision…</button></details></li>)}</ol>
      </details> : null}
    </>}
  </section>;
}
