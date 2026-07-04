/**
 * Check + review-comment services (§4.4, OM-5, PEC-CHK-*).
 * Three distinct facts, never merged: checklist completion, comment closure,
 * checker acceptance (PEC-CHK-003). Comments are child records with assigned
 * responders projecting into My Week — never duplicated as work items.
 */

import type { Check, ChecklistItem, Deliverable, ReviewComment, Revision } from '@pec/core'
import { findTransition } from '@pec/core'
import { badRequest, forbidden } from '../errors.ts'
import { nowIso } from '../repo.ts'
import type { Sx } from './shared.ts'
import {
  assertNoActiveHold, openCommentCount, requireCan, satisfyConditions, snapshot,
  syncCheckState, syncRevisionState, unsatisfyConditions,
} from './shared.ts'

export function createCheck(
  sx: Sx,
  input: { revisionId: number; checkerId: number; templateId?: number },
): Check {
  requireCan(sx, 'check.create')
  const rev = sx.repo.get<Revision>('revision', sx.projectId, input.revisionId)
  if (!input.checkerId) throw badRequest('checker required')
  const deliverable = sx.repo.get<Deliverable>('deliverable', sx.projectId, rev.deliverableId)

  let checklist: ChecklistItem[] = []
  if (input.templateId) {
    const tpl = sx.repo.get<{ items: Array<{ text: string; category: string | null }> }>(
      'checklist_template', sx.projectId, input.templateId,
    )
    checklist = tpl.items.map((i) => ({ text: i.text, category: i.category ?? null, done: false, note: null }))
  }
  // Independence: warn when checker = originator/owner; hard block is P3-configurable (PEC-CHK-004).
  const independenceWarning = deliverable.ownerId != null && deliverable.ownerId === input.checkerId

  const ref = sx.repo.nextRef(sx.projectId, 'check')
  const id = sx.repo.insert('check_record', {
    projectId: sx.projectId, ref, revisionId: input.revisionId, checkerId: input.checkerId,
    templateId: input.templateId ?? null, state: 'open', checklist,
    independenceWarning, createdAt: nowIso(),
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'check', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref} opened on ${deliverable.docNo} rev ${rev.revCode}, checker #${input.checkerId}${independenceWarning ? ' — INDEPENDENCE WARNING: checker is the deliverable owner' : ''}`,
    payload: null, authorityRef: null,
  })
  sx.repo.notify({
    projectId: sx.projectId, personId: input.checkerId, event: 'check_requires_you',
    recordType: 'check', recordId: id, recordRef: ref,
    reason: `check assigned on ${deliverable.docNo} rev ${rev.revCode}`,
    nextAction: 'work the checklist', due: deliverable.dueDate,
  })
  syncRevisionState(sx, input.revisionId) // in_work → in_check
  return sx.repo.get<Check>('check_record', sx.projectId, id)
}

export function startCheck(sx: Sx, id: number, version: number): Check {
  const chk = sx.repo.get<Check>('check_record', sx.projectId, id)
  const def = findTransition('check', 'start', chk.state)
  if (!def) throw badRequest(`illegal transition: start from ${chk.state}`)
  requireCan(sx, 'check.work', { isChecker: chk.checkerId === sx.session.personId })
  sx.repo.update('check_record', sx.projectId, id, version, { state: 'in_check' })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'check', recordId: id, actorId: sx.session.personId,
    kind: 'transition', summary: `${chk.ref}: open → in_check`, payload: null, authorityRef: null,
  })
  return sx.repo.get<Check>('check_record', sx.projectId, id)
}

export function updateChecklist(sx: Sx, id: number, version: number, checklist: ChecklistItem[]): Check {
  const chk = sx.repo.get<Check>('check_record', sx.projectId, id)
  requireCan(sx, 'check.work', { isChecker: chk.checkerId === sx.session.personId })
  if (!Array.isArray(checklist)) throw badRequest('checklist must be an array')
  sx.repo.update('check_record', sx.projectId, id, version, { checklist })
  const done = checklist.filter((i) => i.done).length
  sx.repo.history({
    projectId: sx.projectId, recordType: 'check', recordId: id, actorId: sx.session.personId,
    kind: 'checklist', summary: `${chk.ref} checklist: ${done}/${checklist.length} complete`,
    payload: null, authorityRef: null,
  })
  return sx.repo.get<Check>('check_record', sx.projectId, id)
}

// ---------- comments ----------

export function addComment(
  sx: Sx,
  input: { checkId?: number; revisionId?: number; responderId: number; text: string; log?: ReviewComment['log'] },
): ReviewComment {
  if (!input.text) throw badRequest('comment text required')
  if (!input.responderId) throw badRequest('responder required (OM-5)')
  let checkId: number | null = null
  let revisionId: number | null = null
  if (input.checkId != null) {
    const chk = sx.repo.get<Check>('check_record', sx.projectId, input.checkId)
    requireCan(sx, 'comment.create', { isChecker: chk.checkerId === sx.session.personId })
    checkId = chk.id
  } else if (input.revisionId != null) {
    // client-return comment sheet attached to the revision (D-10)
    sx.repo.get<Revision>('revision', sx.projectId, input.revisionId)
    requireCan(sx, 'comment.create', {})
    revisionId = input.revisionId
  } else {
    throw badRequest('a comment needs a parent check or revision')
  }

  const ref = sx.repo.nextRef(sx.projectId, 'review_comment')
  const id = sx.repo.insert('review_comment', {
    projectId: sx.projectId, ref, checkId, revisionId,
    originatorId: sx.session.personId, responderId: input.responderId,
    text: input.text, disposition: 'open', log: input.log ?? 'internal', createdAt: nowIso(),
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'review_comment', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref} raised, responder #${input.responderId}`, payload: null, authorityRef: null,
  })
  sx.repo.notify({
    projectId: sx.projectId, personId: input.responderId, event: 'comment_requires_you',
    recordType: 'review_comment', recordId: id, recordRef: ref,
    reason: 'review comment assigned to you', nextAction: 'respond to the comment', due: null,
  })
  if (checkId != null) syncCheckState(sx, checkId)
  return sx.repo.get<ReviewComment>('review_comment', sx.projectId, id)
}

export function respondComment(sx: Sx, id: number, version: number, response: string): ReviewComment {
  const c = sx.repo.get<ReviewComment>('review_comment', sx.projectId, id)
  requireCan(sx, 'comment.respond', { isResponder: c.responderId === sx.session.personId })
  if (c.disposition !== 'open' && c.disposition !== 'reopened') {
    throw badRequest(`comment is ${c.disposition}; only open/reopened comments take responses`)
  }
  if (!response) throw badRequest('response text required')
  sx.repo.update('review_comment', sx.projectId, id, version, { response, disposition: 'responded' })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'review_comment', recordId: id,
    actorId: sx.session.personId, kind: 'responded', summary: `${c.ref} responded`, payload: null, authorityRef: null,
  })
  if (c.checkId != null) syncCheckState(sx, c.checkId)
  return sx.repo.get<ReviewComment>('review_comment', sx.projectId, id)
}

/** Checker accepts closure of ONE comment (individually, PEC-CHK-002). */
export function acceptComment(sx: Sx, id: number, version: number, closureEvidenceId?: number): ReviewComment {
  const c = sx.repo.get<ReviewComment>('review_comment', sx.projectId, id)
  const checkerId = c.checkId != null
    ? sx.repo.get<Check>('check_record', sx.projectId, c.checkId).checkerId
    : c.originatorId // client-return comments: originator (DC/lead who logged them) accepts
  requireCan(sx, 'comment.accept', { isChecker: checkerId === sx.session.personId })
  if (c.disposition !== 'responded') throw badRequest('only responded comments can be accepted closed')
  sx.repo.update('review_comment', sx.projectId, id, version, {
    disposition: 'accepted_closed', closureEvidenceId: closureEvidenceId ?? null,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'review_comment', recordId: id,
    actorId: sx.session.personId, kind: 'accepted_closed',
    summary: `${c.ref} closure accepted by checker`, payload: null, authorityRef: null,
  })
  if (c.checkId != null) syncCheckState(sx, c.checkId)
  return sx.repo.get<ReviewComment>('review_comment', sx.projectId, id)
}

/** Checker reopens a responded or accepted-closed comment (review resolution 17). */
export function reopenComment(sx: Sx, id: number, version: number, reason: string): ReviewComment {
  const c = sx.repo.get<ReviewComment>('review_comment', sx.projectId, id)
  const checkerId = c.checkId != null
    ? sx.repo.get<Check>('check_record', sx.projectId, c.checkId).checkerId
    : c.originatorId
  requireCan(sx, 'comment.accept', { isChecker: checkerId === sx.session.personId })
  if (c.disposition !== 'responded' && c.disposition !== 'accepted_closed') {
    throw badRequest(`cannot reopen a ${c.disposition} comment`)
  }
  if (!reason) throw badRequest('reopen reason required')
  sx.repo.update('review_comment', sx.projectId, id, version, { disposition: 'reopened' })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'review_comment', recordId: id,
    actorId: sx.session.personId, kind: 'reopened', summary: `${c.ref} reopened: ${reason}`,
    payload: null, authorityRef: null,
  })
  sx.repo.notify({
    projectId: sx.projectId, personId: c.responderId, event: 'comment_requires_you',
    recordType: 'review_comment', recordId: id, recordRef: c.ref,
    reason: `comment reopened: ${reason}`, nextAction: 'respond again', due: null,
  })
  if (c.checkId != null) syncCheckState(sx, c.checkId)
  return sx.repo.get<ReviewComment>('review_comment', sx.projectId, id)
}

// ---------- acceptance ----------

/**
 * Checker acceptance (§4.4): requires zero open comments; incomplete checklist items do
 * not block but are recorded in the acceptance history entry (three distinct facts).
 * Satisfies check-type conditions and advances the revision (§5.3 event-driven side).
 */
export function acceptCheck(sx: Sx, id: number, version: number): Check {
  const chk = sx.repo.get<Check>('check_record', sx.projectId, id)
  // permission before state legality: unauthorized callers get 403, not state hints
  if (chk.checkerId !== sx.session.personId) {
    throw forbidden('only the assigned checker may accept (I-6, PEC-CHK-002)')
  }
  requireCan(sx, 'check.accept', { isChecker: true })
  const def = findTransition('check', 'accept', chk.state)
  if (!def) throw badRequest(`illegal transition: accept from ${chk.state}`)
  const open = openCommentCount(sx, id)
  if (open > 0) throw badRequest(`cannot accept: ${open} comment(s) not accepted-closed (PEC-CHK-003)`)
  const snap = snapshot(sx)
  assertNoActiveHold(sx, snap, 'check', id, 'check.accept')

  const incomplete = chk.checklist.filter((i) => !i.done)
  sx.repo.update('check_record', sx.projectId, id, version, { state: 'accepted', acceptedAt: nowIso() })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'check', recordId: id,
    actorId: sx.session.personId, kind: 'accepted',
    summary: `${chk.ref} accepted by checker${incomplete.length > 0 ? ` — ${incomplete.length} checklist item(s) incomplete at acceptance` : ' — checklist complete'}`,
    payload: { incomplete: incomplete.map((i) => i.text) }, authorityRef: null,
  })

  const rev = sx.repo.get<Revision>('revision', sx.projectId, chk.revisionId)
  // check-type conditions: pinned to this check, unpinned on the revision, or unpinned on
  // approval records applying to this revision (§5.3)
  const approvalIdsForRev = new Set(
    sx.repo.list<{ id: number }>('approval_record', sx.projectId,
      "applies_to_type = 'revision' AND applies_to_id = ?", [chk.revisionId]).map((a) => a.id),
  )
  satisfyConditions(
    sx,
    (c) => c.type === 'check' && (
      (c.requiredRefType === 'check' && c.requiredRefId === id)
      || (c.requiredRefId == null && c.parentType === 'revision' && c.parentId === chk.revisionId)
      || (c.requiredRefId == null && c.parentType === 'approval_record' && approvalIdsForRev.has(c.parentId))
    ),
    { type: 'check', id, ref: chk.ref },
  )
  syncRevisionState(sx, chk.revisionId)
  const deliverable = sx.repo.get<Deliverable>('deliverable', sx.projectId, rev.deliverableId)
  if (deliverable.ownerId) {
    sx.repo.notify({
      projectId: sx.projectId, personId: deliverable.ownerId, event: 'raised_item_updated',
      recordType: 'check', recordId: id, recordRef: chk.ref,
      reason: `check accepted on ${deliverable.docNo} rev ${rev.revCode}`,
      nextAction: 'revision advances toward approval', due: null,
    })
  }
  return sx.repo.get<Check>('check_record', sx.projectId, id)
}

/** Reopen an accepted check (new revision / supersession); flips its conditions back open. */
export function reopenCheck(sx: Sx, id: number, version: number, reason: string): Check {
  const chk = sx.repo.get<Check>('check_record', sx.projectId, id)
  const def = findTransition('check', 'reopen', chk.state)
  if (!def) throw badRequest(`illegal transition: reopen from ${chk.state}`)
  requireCan(sx, 'check.work', { isChecker: chk.checkerId === sx.session.personId })
  if (!reason) throw badRequest('reopen reason required (§7.4)')
  sx.repo.update('check_record', sx.projectId, id, version, { state: 'reopened', reopenReason: reason, acceptedAt: null })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'check', recordId: id,
    actorId: sx.session.personId, kind: 'reopened', summary: `${chk.ref} reopened: ${reason}`,
    payload: null, authorityRef: null,
  })
  unsatisfyConditions(
    sx,
    (c) => c.satisfiedByType === 'check' && c.satisfiedById === id,
    `check ${chk.ref} reopened`,
  )
  syncRevisionState(sx, chk.revisionId)
  return sx.repo.get<Check>('check_record', sx.projectId, id)
}
