/**
 * Shared service machinery: permission enforcement, gate evaluation with blocked-attempt
 * recording (§5.4), condition satisfaction propagation (§5.3), and the auto-state
 * synchronizers for checks, approval records, and revisions (§4).
 *
 * Every mutating service runs inside withTx() at the API boundary.
 */

import type {
  ApprovalRecord, Check, Condition, PermissionAction, PermissionContext, ProjectSnapshot,
  RecordType, Revision, Role,
} from '@pec/core'
import {
  activeHoldsFor, can, commentIsOpen, evaluateCondition, evaluateGate, explainTransition,
} from '@pec/core'
import type { EvalContext } from '@pec/core'
import type { Db } from '../db.ts'
import { Repo, nowIso } from '../repo.ts'
import type { SessionInfo } from '../auth.ts'
import { conditionsOpen, forbidden } from '../errors.ts'

/** Per-request service context. */
export interface Sx {
  db: Db
  repo: Repo
  projectId: number
  session: SessionInfo
  roles: Role[]
}

export function pctx(sx: Sx, rel: Partial<PermissionContext> = {}): PermissionContext {
  const snapCfg = sx.repo.maybeGet<{ config: { waiverRoles?: PermissionContext['waiverRoles']; allowAnyoneRaiseIntake?: boolean } }>('project', null, sx.projectId)
  return {
    roles: sx.roles,
    isInstanceAdmin: sx.session.isAdmin,
    waiverRoles: snapCfg?.config?.waiverRoles,
    allowAnyoneRaiseIntake: snapCfg?.config?.allowAnyoneRaiseIntake,
    ...rel,
  }
}

export function requireCan(sx: Sx, action: PermissionAction, rel: Partial<PermissionContext> = {}): void {
  const r = can(action, pctx(sx, rel))
  if (!r.allowed) throw forbidden(`${action}: ${r.reason}`)
}

export function snapshot(sx: Sx): ProjectSnapshot {
  return sx.repo.snapshot(sx.projectId)
}

/**
 * Evaluate a gated transition; on refusal, record the attempt with the open conditions
 * listed (metric: prevented invalid closures, PRD §9) and throw 409 CONDITIONS_OPEN.
 * Open warn conditions are logged + notified but never block (D-11).
 */
/**
 * A refused transition must be RECORDED (§9: prevented invalid closures) even though the
 * enclosing transaction rolls back. The attempt is attached to the thrown error; the API
 * transaction wrapper persists it in a fresh transaction after rollback.
 */
export interface BlockedAttempt {
  projectId: number
  recordType: RecordType
  recordId: number
  actorId: number
  summary: string
  payload: unknown
}

export function gateOrThrow(
  sx: Sx,
  snap: ProjectSnapshot,
  parentType: RecordType,
  parentId: number,
  parentRef: string,
  gate: string,
  opts: { holdVeto: boolean; ctx?: EvalContext },
): void {
  const result = evaluateGate(snap, parentType, parentId, gate, opts)
  if (!result.permitted) {
    const explanation = explainTransition(snap, parentType, parentId, gate, opts)
    const attempt: BlockedAttempt = {
      projectId: sx.projectId, recordType: parentType, recordId: parentId,
      actorId: sx.session.personId,
      summary: `${gate} blocked: ${result.hardOpen.length} open hard condition(s), ${result.holdVeto.length} active hold(s)`,
      payload: explanation,
    }
    throw Object.assign(conditionsOpen(explanation), { blockedAttempt: attempt })
  }
  for (const w of result.warnOpen) {
    sx.repo.history({
      projectId: sx.projectId, recordType: parentType, recordId: parentId,
      actorId: sx.session.personId, kind: 'condition_warn',
      summary: `${gate} proceeded with open warn condition ${w.condition.ref}: ${w.condition.description}`,
      payload: { condition: w.condition.ref }, authorityRef: null,
    })
    if (w.condition.ownerId) {
      sx.repo.notify({
        projectId: sx.projectId, personId: w.condition.ownerId, event: 'condition_warn',
        recordType: 'condition', recordId: w.condition.id, recordRef: w.condition.ref,
        reason: `warn condition open when ${parentRef} passed ${gate}`,
        nextAction: 'review the condition', due: w.condition.needBy,
      })
    }
  }
}

export function assertNoActiveHold(sx: Sx, snap: ProjectSnapshot, targetType: RecordType, targetId: number, gateName: string): void {
  const holds = activeHoldsFor(snap, targetType as never, targetId)
  if (holds.length > 0) {
    const detail = holds.map((h) => ({ ref: h.ref, cause: h.cause, title: h.title, ownerId: h.ownerId }))
    const attempt: BlockedAttempt = {
      projectId: sx.projectId, recordType: targetType, recordId: targetId,
      actorId: sx.session.personId,
      summary: `${gateName} vetoed by active hold(s): ${holds.map((h) => h.ref).join(', ')}`,
      payload: { holds: detail },
    }
    throw Object.assign(
      conditionsOpen({ gate: gateName, permitted: false, holdVeto: detail, conditions: [] }),
      { blockedAttempt: attempt },
    )
  }
}

// ---------- condition satisfaction propagation (§5.3, event-driven side) ----------

export interface Satisfier { type: RecordType; id: number; ref: string }

/** Mark matching open conditions satisfied; write history; resync dependent parents. */
export function satisfyConditions(
  sx: Sx,
  match: (c: Condition) => boolean,
  by: Satisfier,
): void {
  const open = sx.repo.list<Condition>('condition_record', sx.projectId, "state = 'open'")
  const touched: Condition[] = []
  for (const c of open) {
    if (!match(c)) continue
    sx.repo.systemUpdate('condition_record', sx.projectId, c.id, {
      state: 'satisfied', satisfiedByType: by.type, satisfiedById: by.id, satisfiedAt: nowIso(),
    })
    sx.repo.history({
      projectId: sx.projectId, recordType: 'condition', recordId: c.id,
      actorId: sx.session.personId, kind: 'satisfied',
      summary: `${c.ref} satisfied by ${by.ref}`, payload: { by }, authorityRef: null,
    })
    touched.push(c)
  }
  resyncParents(sx, touched)
}

/** Flip previously satisfied conditions back to open (reopen/supersession); resync parents. */
export function unsatisfyConditions(
  sx: Sx,
  match: (c: Condition) => boolean,
  reason: string,
): void {
  const sat = sx.repo.list<Condition>('condition_record', sx.projectId, "state = 'satisfied'")
  const touched: Condition[] = []
  for (const c of sat) {
    if (!match(c)) continue
    sx.repo.systemUpdate('condition_record', sx.projectId, c.id, {
      state: 'open', satisfiedByType: null, satisfiedById: null, satisfiedAt: null,
    })
    sx.repo.history({
      projectId: sx.projectId, recordType: 'condition', recordId: c.id,
      actorId: sx.session.personId, kind: 'reopened',
      summary: `${c.ref} reopened: ${reason}`, payload: null, authorityRef: null,
    })
    touched.push(c)
  }
  resyncParents(sx, touched)
}

function resyncParents(sx: Sx, touched: Condition[]): void {
  const approvalIds = new Set<number>()
  for (const c of touched) {
    if (c.parentType === 'approval_record') approvalIds.add(c.parentId)
  }
  for (const id of approvalIds) syncApprovalState(sx, id)
}

// ---------- auto-state synchronizers (§4) ----------

/** Check state from its comments: in_check ↔ comments_open ↔ comments_closed (auto rows in §4.4). */
export function syncCheckState(sx: Sx, checkId: number): void {
  const chk = sx.repo.get<Check>('check_record', sx.projectId, checkId)
  if (chk.state === 'accepted' || chk.state === 'reopened' || chk.state === 'open') return
  const comments = sx.repo.list<{ disposition: string }>('review_comment', sx.projectId, 'check_id = ?', [checkId])
  const openCount = comments.filter((c) => c.disposition !== 'accepted_closed').length
  const target = comments.length === 0 ? 'in_check' : openCount > 0 ? 'comments_open' : 'comments_closed'
  if (target !== chk.state) {
    sx.repo.systemUpdate('check_record', sx.projectId, checkId, { state: target })
    sx.repo.history({
      projectId: sx.projectId, recordType: 'check', recordId: checkId,
      actorId: sx.session.personId, kind: 'transition',
      summary: `${chk.ref}: ${chk.state} → ${target} (comments: ${openCount} open of ${comments.length})`,
      payload: null, authorityRef: null,
    })
  }
}

/** Approval record auto states: required / prereqs_incomplete / ready (§4.5). */
export function syncApprovalState(sx: Sx, approvalId: number): void {
  const a = sx.repo.get<ApprovalRecord>('approval_record', sx.projectId, approvalId)
  if (a.state === 'decided' || a.state === 'superseded') return
  const snap = snapshot(sx)
  const prereqs = snap.conditions.filter(
    (c) => c.parentType === 'approval_record' && c.parentId === approvalId
      && c.gatedTransition === 'approval_record.ready',
  )
  const allPass = prereqs.every((c) => {
    const ev = evaluateCondition(snap, c)
    return ev.effectiveState === 'satisfied' || ev.effectiveState === 'waived' || ev.effectiveState === 'superseded'
  })
  const target = allPass ? 'ready' : 'prereqs_incomplete'
  if (target === a.state) return
  if (target === 'ready') {
    sx.repo.systemUpdate('approval_record', sx.projectId, approvalId, { state: 'ready', readyAt: a.readyAt ?? nowIso() })
    for (const sig of a.signatoryIds) {
      sx.repo.notify({
        projectId: sx.projectId, personId: sig, event: 'approval_requires_you',
        recordType: 'approval_record', recordId: a.id, recordRef: a.ref,
        reason: 'all prerequisites satisfied; your approval decision is required',
        nextAction: 'record the approval outcome', due: a.dueDate,
      })
    }
  } else {
    sx.repo.systemUpdate('approval_record', sx.projectId, approvalId, { state: 'prereqs_incomplete', readyAt: null })
  }
  sx.repo.history({
    projectId: sx.projectId, recordType: 'approval_record', recordId: approvalId,
    actorId: sx.session.personId, kind: 'transition',
    summary: `${a.ref}: ${a.state} → ${target}`, payload: null, authorityRef: null,
  })
  syncRevisionForApproval(sx, a)
}

function syncRevisionForApproval(sx: Sx, a: ApprovalRecord): void {
  if (a.appliesToType === 'revision') syncRevisionState(sx, a.appliesToId)
}

/**
 * Revision auto chain (§4.7): in_check → check_accepted → ready_for_approval → approved,
 * forward and backward from the record graph. Never auto-touches issued /
 * returned_with_comments / superseded; `issue` is only reachable through the manual,
 * hard-gated transition.
 */
export function syncRevisionState(sx: Sx, revisionId: number): void {
  const rev = sx.repo.get<Revision>('revision', sx.projectId, revisionId)
  if (rev.state === 'issued' || rev.state === 'returned_with_comments' || rev.state === 'superseded') return

  const checks = sx.repo.list<Check>('check_record', sx.projectId, 'revision_id = ?', [revisionId])
  const hasCheck = checks.length > 0
  const checkAccepted = checks.some((c) => c.state === 'accepted')
  const approvals = sx.repo.list<ApprovalRecord>('approval_record', sx.projectId,
    "applies_to_type = 'revision' AND applies_to_id = ? AND state != 'superseded'", [revisionId])
  const outcomes = approvals.map((a) => {
    if (a.state !== 'decided' || a.outcomeDecisionId == null) return null
    const d = sx.repo.maybeGet<{ outcome: string }>('decision', sx.projectId, a.outcomeDecisionId)
    return d?.outcome ?? null
  })
  const allApproved = approvals.length > 0
    && outcomes.every((o) => o === 'approve' || o === 'conditionally_accept')
  const allReadyOrDecided = approvals.every((a) => a.state === 'ready' || a.state === 'decided')

  let target: Revision['state']
  if (!checkAccepted) {
    target = hasCheck && checks.some((c) => c.state !== 'reopened') ? 'in_check' : 'in_work'
  } else if (approvals.length === 0) {
    // No approval records required: check acceptance carries the revision to approved;
    // the issue gate (conditions, D-11) still stands between approved and issued.
    target = 'approved'
  } else if (allApproved) {
    target = 'approved'
  } else if (allReadyOrDecided) {
    target = 'ready_for_approval'
  } else {
    target = 'check_accepted'
  }

  if (target !== rev.state) {
    sx.repo.systemUpdate('revision', sx.projectId, revisionId, { state: target })
    sx.repo.history({
      projectId: sx.projectId, recordType: 'revision', recordId: revisionId,
      actorId: sx.session.personId, kind: 'transition',
      summary: `revision ${rev.revCode}: ${rev.state} → ${target}`, payload: null, authorityRef: null,
    })
    if (target === 'ready_for_approval') {
      for (const a of approvals.filter((x) => x.state === 'ready')) {
        for (const sig of a.signatoryIds) {
          sx.repo.notify({
            projectId: sx.projectId, personId: sig, event: 'revision_ready_for_approval',
            recordType: 'revision', recordId: revisionId, recordRef: `rev ${rev.revCode}`,
            reason: 'revision reached ready-for-approval', nextAction: `record outcome on ${a.ref}`,
            due: a.dueDate,
          })
        }
      }
    }
  }
}

/** Comment-open check helper shared by accept paths. */
export function openCommentCount(sx: Sx, checkId: number): number {
  return sx.repo.list<{ disposition: 'open' | 'responded' | 'accepted_closed' | 'reopened' }>(
    'review_comment', sx.projectId, 'check_id = ?', [checkId],
  ).filter((c) => commentIsOpen(c as never)).length
}
