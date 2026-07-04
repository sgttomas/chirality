/**
 * Revision services (§4.7). Creating a revision instantiates conditions from templates
 * (§5.2) and supersedes the prior revision (chain preserved, I-10). Issue is the manual,
 * hard-gated transition (D-11): recording the issue event IS the transition.
 */

import type {
  Condition, ConditionTemplate, Deliverable, IssueEvent, Project, Revision,
} from '@pec/core'
import { findTransition } from '@pec/core'
import { badRequest } from '../errors.ts'
import { nowIso } from '../repo.ts'
import type { Sx } from './shared.ts'
import { gateOrThrow, requireCan, satisfyConditions, snapshot, syncRevisionState, unsatisfyConditions } from './shared.ts'
import { addComment } from './checks.ts'

export function createRevision(
  sx: Sx,
  input: { deliverableId: number; revCode: string; issuePurpose?: string },
  opts?: { skipPermission?: boolean; skipTemplates?: boolean; initialState?: Revision['state'] },
): Revision {
  if (!opts?.skipPermission) requireCan(sx, 'revision.create')
  const d = sx.repo.get<Deliverable>('deliverable', sx.projectId, input.deliverableId)
  if (!input.revCode) throw badRequest('revision code required')

  const prior = sx.repo.list<Revision>('revision', sx.projectId,
    "deliverable_id = ? AND state != 'superseded'", [input.deliverableId])

  const id = sx.repo.insert('revision', {
    projectId: sx.projectId, deliverableId: input.deliverableId, revCode: input.revCode,
    state: opts?.initialState ?? 'in_work', createdAt: nowIso(), createdBy: sx.session.personId,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'revision', recordId: id,
    actorId: sx.session.personId, kind: opts?.initialState ? 'import' : 'created',
    summary: `${d.docNo} rev ${input.revCode} created${opts?.initialState ? ` at imported state ${opts.initialState} (seeding, not a transition)` : ''}`,
    payload: null, authorityRef: null,
  })

  // Supersede prior revisions: chain preserved, never deleted (I-10, §4.7).
  for (const p of prior) {
    sx.repo.systemUpdate('revision', sx.projectId, p.id, { state: 'superseded', supersededByRevisionId: id })
    sx.repo.history({
      projectId: sx.projectId, recordType: 'revision', recordId: p.id,
      actorId: sx.session.personId, kind: 'superseded',
      summary: `${d.docNo} rev ${p.revCode} superseded by rev ${input.revCode} — chain preserved (I-10)`,
      payload: { supersededBy: id }, authorityRef: null,
    })
    // conditions satisfied by records of the superseded revision stay with that revision;
    // open conditions on it are superseded (they gate a surface that no longer moves)
    const priorConds = sx.repo.list<Condition>('condition_record', sx.projectId,
      "parent_type = 'revision' AND parent_id = ? AND state = 'open'", [p.id])
    for (const c of priorConds) {
      sx.repo.systemUpdate('condition_record', sx.projectId, c.id, { state: 'superseded' })
      sx.repo.history({
        projectId: sx.projectId, recordType: 'condition', recordId: c.id,
        actorId: sx.session.personId, kind: 'superseded',
        summary: `${c.ref} superseded with rev ${p.revCode}`, payload: null, authorityRef: null,
      })
    }
    if (d.ownerId) {
      sx.repo.notify({
        projectId: sx.projectId, personId: d.ownerId, event: 'basis_superseded',
        recordType: 'revision', recordId: p.id, recordRef: `${d.docNo} rev ${p.revCode}`,
        reason: `superseded by rev ${input.revCode}`, nextAction: 'work continues on the new revision', due: null,
      })
    }
  }

  // Instantiate conditions from templates keyed by deliverable type + issue purpose + package (§5.2).
  if (!opts?.skipTemplates) {
    const purpose = input.issuePurpose ?? d.issuePurposePlan
    const templates = sx.repo.list<ConditionTemplate>('condition_template', sx.projectId)
    for (const t of templates) {
      if (t.deliverableType != null && t.deliverableType !== d.deliverableType) continue
      if (t.issuePurpose != null && purpose != null && t.issuePurpose !== purpose) continue
      if (t.issuePurpose != null && purpose == null) continue
      if (t.packageId != null && t.packageId !== d.packageId) continue
      const ref = sx.repo.nextRef(sx.projectId, 'condition')
      const condId = sx.repo.insert('condition_record', {
        projectId: sx.projectId, ref, parentType: 'revision', parentId: id,
        gatedTransition: t.transition, type: t.type, description: t.description,
        requiredArtifactName: t.requiredArtifactName ?? null,
        source: 'template', sourceRef: t.name, severity: t.severity,
        ownerId: d.ownerId ?? null, needBy: d.dueDate ?? null, state: 'open',
      })
      sx.repo.history({
        projectId: sx.projectId, recordType: 'condition', recordId: condId,
        actorId: sx.session.personId, kind: 'created',
        summary: `${ref} instantiated from template "${t.name}" on ${d.docNo} rev ${input.revCode} (${t.severity} ${t.type} → ${t.transition})`,
        payload: null, authorityRef: null,
      })
    }
  }
  return sx.repo.get<Revision>('revision', sx.projectId, id)
}

/** Manual revision transitions: rework, issue, return_comments (§4.7). */
export function transitionRevision(
  sx: Sx, id: number, event: string,
  payload: {
    version: number
    issueEvent?: { purpose: string; transmittalRef: string; recipients: string[] }
    clientComments?: Array<{ text: string; responderId: number }>
  },
): Revision {
  const rev = sx.repo.get<Revision>('revision', sx.projectId, id)
  const d = sx.repo.get<Deliverable>('deliverable', sx.projectId, rev.deliverableId)
  const def = findTransition('revision', event, rev.state)
  if (!def) throw badRequest(`illegal transition: ${event} from ${rev.state}`)
  if (def.auto) throw badRequest(`${event} is system-driven`)
  requireCan(sx, def.permission as never, { isOwner: d.ownerId === sx.session.personId })

  if (event === 'issue') return issueRevision(sx, rev, d, payload)

  sx.repo.update('revision', sx.projectId, id, payload.version, { state: def.to })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'revision', recordId: id,
    actorId: sx.session.personId, kind: 'transition',
    summary: `${d.docNo} rev ${rev.revCode}: ${rev.state} → ${def.to}`, payload: { event }, authorityRef: null,
  })
  if (event === 'return_comments') {
    // D-10: client comments logged as review comments with log=client on the revision
    for (const c of payload.clientComments ?? []) {
      addComment(sx, { revisionId: id, responderId: c.responderId, text: c.text, log: 'client' })
    }
  }
  return sx.repo.get<Revision>('revision', sx.projectId, id)
}

/**
 * §4.7 approved → issued. Hard-gated (D-11): every hard condition on revision.issue must
 * pass with the pending issue event in evaluation context; active holds veto. Recording
 * the issue event IS the transition; the archive reference completes the P1 chain
 * (PEC-ARC-002); an audit event is written (PEC-NFR-001).
 */
function issueRevision(
  sx: Sx, rev: Revision, d: Deliverable,
  payload: {
    version: number
    issueEvent?: { purpose: string; transmittalRef: string; recipients: string[] }
  },
): Revision {
  const ev = payload.issueEvent
  if (!ev?.purpose || !ev.transmittalRef || !ev.recipients || ev.recipients.length === 0) {
    throw badRequest('issue requires purpose, transmittal reference, and recipients (PEC-DEL-008)')
  }
  const project = sx.repo.get<Project>('project', null, sx.projectId)
  const purposes = project.config.issuePurposes ?? ['IFR', 'IFA', 'IFC']
  if (!purposes.includes(ev.purpose) && ev.purpose !== 'other') {
    throw badRequest(`issue purpose must be one of ${purposes.join(', ')} or "other" (D-07)`)
  }

  const snap = snapshot(sx)
  gateOrThrow(sx, snap, 'revision', rev.id, `${d.docNo} rev ${rev.revCode}`, 'revision.issue', {
    holdVeto: true,
    ctx: { pendingIssueEvent: { transmittalRef: ev.transmittalRef, recipients: ev.recipients } },
  })

  // linked chain: approvals on this revision and their outcome decisions (PEC-ARC-002)
  const approvals = sx.repo.list<{ id: number; outcomeDecisionId: number | null }>('approval_record', sx.projectId,
    "applies_to_type = 'revision' AND applies_to_id = ? AND state = 'decided'", [rev.id])
  const decisionIds = approvals.map((a) => a.outcomeDecisionId).filter((x): x is number => x != null)

  const ref = sx.repo.nextRef(sx.projectId, 'issue_event')
  const archiveRef = `ARC-${project.code}-${d.docNo}-${rev.revCode}`
  const issueId = sx.repo.insert('issue_event', {
    projectId: sx.projectId, ref, revisionId: rev.id, purpose: ev.purpose,
    transmittalRef: ev.transmittalRef, recipients: ev.recipients,
    issuedAt: nowIso(), issuedBy: sx.session.personId,
    approvalRecordIds: approvals.map((a) => a.id), decisionIds, archiveRef,
  })
  sx.repo.update('revision', sx.projectId, rev.id, payload.version, { state: 'issued' })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'revision', recordId: rev.id,
    actorId: sx.session.personId, kind: 'issued',
    summary: `${d.docNo} rev ${rev.revCode} ISSUED (${ev.purpose}) — transmittal ${ev.transmittalRef} → ${ev.recipients.join(', ')}; archive ${archiveRef}`,
    payload: { issueEventRef: ref }, authorityRef: ev.transmittalRef,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'issue_event', recordId: issueId,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref}: ${d.docNo} rev ${rev.revCode} ${ev.purpose}, chain: ${approvals.length} approval record(s), ${decisionIds.length} decision(s)`,
    payload: null, authorityRef: ev.transmittalRef,
  })
  sx.repo.audit({
    projectId: sx.projectId, actorId: sx.session.personId, action: 'issue',
    recordType: 'revision', recordId: rev.id,
    priorValue: { state: 'approved' }, newValue: { state: 'issued', issueEvent: ref, transmittal: ev.transmittalRef },
    authorityRef: ev.transmittalRef,
  })
  // document_control conditions on this revision are satisfied by the recorded event (§5.3)
  satisfyConditions(
    sx,
    (c) => c.type === 'document_control' && c.parentType === 'revision' && c.parentId === rev.id,
    { type: 'issue_event', id: issueId, ref },
  )
  return sx.repo.get<Revision>('revision', sx.projectId, rev.id)
}

/** Rework loop helper used by API: revision back to in_work reopens nothing by itself (§7.7 loops are expected). */
export function reworkRevision(sx: Sx, id: number, version: number): Revision {
  return transitionRevision(sx, id, 'rework', { version })
}

export type { IssueEvent }
export { unsatisfyConditions, syncRevisionState }
