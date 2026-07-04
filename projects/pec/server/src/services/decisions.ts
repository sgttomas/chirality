/**
 * Judgment services (ADR-005): Decisions (§4.6), Approval Records (§4.5), and condition
 * waivers (I-8). `recordDecisionRow` is the ONLY code path that writes a decision outcome;
 * approval outcomes and waivers route through it (OM-6, I-6). Check acceptance deliberately
 * does NOT (PEC-CHK-005: checking verifies; it is not approval).
 */

import type {
  ApprovalRecord, Condition, ConditionSeverity, ConditionType, Decision, DecisionOutcome,
  RecordType,
} from '@pec/core'
import { CONDITION_TYPES, DECISION_OUTCOMES, findTransition } from '@pec/core'
import { badRequest } from '../errors.ts'
import { TABLE, nowIso } from '../repo.ts'
import { optDate } from '../validate.ts'
import type { Sx } from './shared.ts'
import {
  assertNoActiveHold, requireCan, satisfyConditions, snapshot, syncApprovalState,
  syncRevisionState, unsatisfyConditions,
} from './shared.ts'
import { createWorkItem } from './work.ts'
import type { CreateWorkItemInput } from './work.ts'

// ---------- conditions ----------

export interface ConditionInput {
  parentType: RecordType
  parentId: number
  gatedTransition: string
  type: ConditionType
  description: string
  severity?: ConditionSeverity
  requiredRefType?: RecordType
  requiredRefId?: number
  requiredArtifactName?: string
  ownerId?: number
  needBy?: string
  source?: Condition['source']
  sourceRef?: string
}

export function createCondition(sx: Sx, input: ConditionInput, opts?: { skipPermission?: boolean }): Condition {
  if (!opts?.skipPermission) requireCan(sx, 'condition.create')
  if (!CONDITION_TYPES.includes(input.type)) throw badRequest(`invalid condition type: ${input.type}`)
  if (!input.description) throw badRequest('condition description required')
  if (!input.gatedTransition) throw badRequest('a condition attaches to a transition (§9)')
  const table = TABLE[input.parentType]
  if (!table) throw badRequest(`invalid condition parent: ${input.parentType}`)
  sx.repo.get(table, sx.projectId, input.parentId) // must exist

  const ref = sx.repo.nextRef(sx.projectId, 'condition')
  const id = sx.repo.insert('condition_record', {
    projectId: sx.projectId, ref,
    parentType: input.parentType, parentId: input.parentId, gatedTransition: input.gatedTransition,
    type: input.type, description: input.description,
    requiredRefType: input.requiredRefType ?? null, requiredRefId: input.requiredRefId ?? null,
    requiredArtifactName: input.requiredArtifactName ?? null,
    source: input.source ?? 'manual', sourceRef: input.sourceRef ?? null,
    severity: input.severity ?? 'warn',
    ownerId: input.ownerId ?? null, needBy: optDate(input.needBy, 'need-by'), state: 'open',
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'condition', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref} [${input.severity ?? 'warn'} ${input.type}] on ${input.parentType}#${input.parentId} → ${input.gatedTransition}: ${input.description}`,
    payload: { source: input.source ?? 'manual', sourceRef: input.sourceRef ?? null }, authorityRef: null,
  })
  if (input.parentType === 'approval_record') syncApprovalState(sx, input.parentId)
  return sx.repo.get<Condition>('condition_record', sx.projectId, id)
}

/** Manual satisfaction — resource/other types only (§5.3); everything else is graph- or judgment-driven. */
export function satisfyConditionManual(sx: Sx, id: number, version: number, note: string): Condition {
  const c = sx.repo.get<Condition>('condition_record', sx.projectId, id)
  requireCan(sx, 'condition.satisfy_manual')
  if (c.type !== 'resource' && c.type !== 'other') {
    throw badRequest(`${c.type}-type conditions are satisfied by their ${c.type} record, not manually (§5.3)`)
  }
  if (c.state !== 'open') throw badRequest(`condition is ${c.state}`)
  if (!note) throw badRequest('a manual satisfaction note is required (recorded)')
  sx.repo.update('condition_record', sx.projectId, id, version, {
    state: 'satisfied', satisfiedByType: 'person', satisfiedById: sx.session.personId, satisfiedAt: nowIso(),
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'condition', recordId: id,
    actorId: sx.session.personId, kind: 'satisfied',
    summary: `${c.ref} manually satisfied: ${note}`, payload: null, authorityRef: null,
  })
  if (c.parentType === 'approval_record') syncApprovalState(sx, c.parentId)
  return sx.repo.get<Condition>('condition_record', sx.projectId, id)
}

// ---------- the single judgment write path (ADR-005) ----------

interface DecisionRowInput {
  title: string
  statement: string
  authorityId: number
  outcome: DecisionOutcome
  rationale: string
  kind: Decision['kind']
  approvalRecordId?: number
  conditionId?: number
  packageId?: number | null
  log?: Decision['log']
  needBy?: string | null
  preparerId?: number | null
  optionsConsidered?: string | null
  recommendation?: string | null
}

/**
 * Create a decided Decision row. Used directly by approval outcomes and waivers (which are
 * judgments made at the moment of recording); standalone decisions instead walk the §4.6
 * lifecycle and reach `decided` via recordDecisionOutcome below — which also lands here.
 */
function recordDecisionRow(sx: Sx, input: DecisionRowInput): Decision {
  if (!DECISION_OUTCOMES.includes(input.outcome)) throw badRequest(`invalid outcome: ${input.outcome}`)
  if (!input.rationale) throw badRequest('rationale is required on every judgment (§4.4 PRD table)')
  const ref = sx.repo.nextRef(sx.projectId, 'decision')
  const id = sx.repo.insert('decision', {
    projectId: sx.projectId, ref, title: input.title, statement: input.statement,
    preparerId: input.preparerId ?? null, authorityId: input.authorityId,
    needBy: input.needBy ?? null, state: 'decided', outcome: input.outcome,
    rationale: input.rationale, optionsConsidered: input.optionsConsidered ?? null,
    recommendation: input.recommendation ?? null,
    decidedAt: nowIso(), decidedBy: sx.session.personId,
    kind: input.kind, approvalRecordId: input.approvalRecordId ?? null,
    conditionId: input.conditionId ?? null, packageId: input.packageId ?? null,
    log: input.log ?? 'internal', createdAt: nowIso(),
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'decision', recordId: id,
    actorId: sx.session.personId, kind: 'decided',
    summary: `${ref} [${input.kind}] ${input.outcome}: ${input.title}`,
    payload: { rationale: input.rationale }, authorityRef: null,
  })
  return sx.repo.get<Decision>('decision', sx.projectId, id)
}

// ---------- standalone decisions (§4.6) ----------

export interface CreateDecisionInput {
  title: string
  statement: string
  authorityId: number
  preparerId?: number
  needBy?: string
  packageId?: number
  log?: Decision['log']
  optionsConsidered?: string
  recommendation?: string
  affected?: Array<{ recordType: RecordType; recordId: number; relation?: 'affects' | 'blocks' }>
}

export function createDecision(sx: Sx, input: CreateDecisionInput, opts?: { skipPermission?: boolean }): Decision {
  if (!opts?.skipPermission) requireCan(sx, 'decision.create')
  if (!input.title || !input.statement) throw badRequest('title and decision-needed statement required (PEC-DEC-001)')
  if (!input.authorityId) throw badRequest('decision authority required (distinct from preparer)')
  const ref = sx.repo.nextRef(sx.projectId, 'decision')
  const id = sx.repo.insert('decision', {
    projectId: sx.projectId, ref, title: input.title, statement: input.statement,
    preparerId: input.preparerId ?? null, authorityId: input.authorityId,
    needBy: optDate(input.needBy, 'need-by'), state: input.preparerId ? 'in_progress' : 'identified',
    kind: 'standalone', packageId: input.packageId ?? null, log: input.log ?? 'internal',
    optionsConsidered: input.optionsConsidered ?? null, recommendation: input.recommendation ?? null,
    createdAt: nowIso(),
  })
  for (const a of input.affected ?? []) {
    sx.repo.insert('decision_link', {
      decisionId: id, recordType: a.recordType, recordId: a.recordId, relation: a.relation ?? 'affects',
    })
  }
  sx.repo.history({
    projectId: sx.projectId, recordType: 'decision', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref} identified: ${input.title}, authority #${input.authorityId}, need-by ${input.needBy ?? '—'}`,
    payload: null, authorityRef: null,
  })
  return sx.repo.get<Decision>('decision', sx.projectId, id)
}

export function progressDecision(
  sx: Sx, id: number, event: 'assign_preparer' | 'mark_pending',
  payload: { version: number; preparerId?: number },
): Decision {
  const d = sx.repo.get<Decision>('decision', sx.projectId, id)
  const def = findTransition('decision', event, d.state)
  if (!def) throw badRequest(`illegal transition: ${event} from ${d.state}`)
  requireCan(sx, 'decision.progress', {
    isPreparer: d.preparerId === sx.session.personId,
    isAuthority: d.authorityId === sx.session.personId,
  })
  if (event === 'assign_preparer' && !payload.preparerId) throw badRequest('preparer required')
  sx.repo.update('decision', sx.projectId, id, payload.version, {
    state: def.to,
    ...(event === 'assign_preparer' ? { preparerId: payload.preparerId } : {}),
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'decision', recordId: id,
    actorId: sx.session.personId, kind: 'transition',
    summary: `${d.ref}: ${d.state} → ${def.to}`, payload: null, authorityRef: null,
  })
  if (event === 'mark_pending') {
    sx.repo.notify({
      projectId: sx.projectId, personId: d.authorityId, event: 'decision_past_need_by',
      recordType: 'decision', recordId: id, recordRef: d.ref,
      reason: 'decision package ready; you are the authority',
      nextAction: 'record the decision outcome', due: d.needBy,
    })
  }
  return sx.repo.get<Decision>('decision', sx.projectId, id)
}

export interface DecisionOutcomeInput {
  version: number
  outcome: DecisionOutcome
  rationale: string
  conditionsCreated?: ConditionInput[]
  followUps?: CreateWorkItemInput[]
}

/** §4.6 pending → decided, by the authority only. */
export function recordDecisionOutcome(sx: Sx, id: number, input: DecisionOutcomeInput): Decision {
  const d = sx.repo.get<Decision>('decision', sx.projectId, id)
  const def = findTransition('decision', 'record_outcome', d.state)
  if (!def) throw badRequest(`illegal transition: record_outcome from ${d.state}`)
  // Authority only — no instance-admin break-glass on a judgment (I-6, §7.6).
  requireCan(sx, 'decision.outcome', { isAuthority: d.authorityId === sx.session.personId })
  if (!DECISION_OUTCOMES.includes(input.outcome)) throw badRequest(`invalid outcome: ${input.outcome}`)
  if (!input.rationale) throw badRequest('rationale required')
  const snap = snapshot(sx)
  assertNoActiveHold(sx, snap, 'decision', id, 'decision.record_outcome')

  sx.repo.update('decision', sx.projectId, id, input.version, {
    state: 'decided', outcome: input.outcome, rationale: input.rationale,
    decidedAt: nowIso(), decidedBy: sx.session.personId,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'decision', recordId: id,
    actorId: sx.session.personId, kind: 'decided',
    summary: `${d.ref} decided: ${input.outcome}`, payload: { rationale: input.rationale }, authorityRef: null,
  })
  applyDecisionEffects(sx, sx.repo.get<Decision>('decision', sx.projectId, id), input)
  return sx.repo.get<Decision>('decision', sx.projectId, id)
}

/** Shared post-outcome effects: conditions created, follow-ups, condition satisfaction, notifications. */
function applyDecisionEffects(
  sx: Sx, d: Decision,
  input: { conditionsCreated?: ConditionInput[]; followUps?: CreateWorkItemInput[] },
): void {
  for (const c of input.conditionsCreated ?? []) {
    createCondition(sx, { ...c, source: 'decision', sourceRef: d.ref }, { skipPermission: true })
  }
  for (const f of input.followUps ?? []) {
    const wi = createWorkItem(sx, { ...f, sourceType: 'decision', sourceId: d.id }, { skipPermission: true })
    sx.repo.insert('decision_link', { decisionId: d.id, recordType: 'work_item', recordId: wi.id, relation: 'follow_up' })
  }
  // decision-type conditions pinned to this decision (or unpinned on records this decision links)
  const linked = sx.repo.db.prepare('SELECT record_type, record_id FROM decision_link WHERE decision_id = ?')
    .all(d.id) as Array<{ record_type: string; record_id: number }>
  satisfyConditions(
    sx,
    (c) => c.type === 'decision' && (
      (c.requiredRefType === 'decision' && c.requiredRefId === d.id)
      || (c.requiredRefId == null && linked.some((l) => l.record_type === c.parentType && l.record_id === c.parentId))
    ),
    { type: 'decision', id: d.id, ref: d.ref },
  )
  // notify owners of affected records
  for (const l of linked) {
    const table = TABLE[l.record_type]
    if (!table) continue
    const rec = sx.repo.maybeGet<Record<string, unknown>>(table, sx.projectId, l.record_id)
    const owner = (rec?.ownerId ?? null) as number | null
    if (owner && owner !== sx.session.personId) {
      sx.repo.notify({
        projectId: sx.projectId, personId: owner, event: 'raised_item_updated',
        recordType: l.record_type, recordId: l.record_id,
        recordRef: String(rec?.ref ?? rec?.docNo ?? `#${l.record_id}`),
        reason: `${d.ref} decided (${d.outcome}) affects your record`,
        nextAction: 'review the decision', due: null,
      })
    }
  }
}

export function supersedeDecision(sx: Sx, id: number, payload: { version: number; replacementId: number }): Decision {
  const d = sx.repo.get<Decision>('decision', sx.projectId, id)
  const def = findTransition('decision', 'supersede', d.state)
  if (!def) throw badRequest(`illegal transition: supersede from ${d.state}`)
  requireCan(sx, 'decision.supersede')
  if (!payload.replacementId) throw badRequest('supersession requires the replacement decision (I-10)')
  if (payload.replacementId === id) throw badRequest('a decision cannot supersede itself — the replacement must be a distinct record (I-10)')
  const replacement = sx.repo.get<Decision>('decision', sx.projectId, payload.replacementId)
  if (replacement.state === 'superseded') throw badRequest(`${replacement.ref} is itself superseded; supersede with a live replacement (I-10)`)
  sx.repo.update('decision', sx.projectId, id, payload.version, {
    state: 'superseded', supersededById: replacement.id,
  })
  sx.repo.insert('decision_link', { decisionId: replacement.id, recordType: 'decision', recordId: id, relation: 'supersedes' })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'decision', recordId: id,
    actorId: sx.session.personId, kind: 'superseded',
    summary: `${d.ref} superseded by ${replacement.ref} — remains visible, linked (I-10)`,
    payload: null, authorityRef: null,
  })
  // basis drift response: flag affected records for review
  const linked = sx.repo.db.prepare('SELECT record_type, record_id FROM decision_link WHERE decision_id = ?')
    .all(id) as Array<{ record_type: string; record_id: number }>
  const affected: Array<{ recordType: RecordType; id: number; ref: string }> = []
  for (const l of linked) {
    const table = TABLE[l.record_type]
    if (!table) continue
    const rec = sx.repo.maybeGet<Record<string, unknown>>(table, sx.projectId, l.record_id)
    if (!rec) continue
    affected.push({
      recordType: l.record_type as RecordType, id: l.record_id,
      ref: String(rec.ref ?? rec.docNo ?? `#${l.record_id}`),
    })
    sx.repo.history({
      projectId: sx.projectId, recordType: l.record_type as RecordType, recordId: l.record_id,
      actorId: sx.session.personId, kind: 'basis_superseded',
      summary: `basis ${d.ref} superseded by ${replacement.ref}; review this record`,
      payload: null, authorityRef: null,
    })
    const owner = (rec.ownerId ?? null) as number | null
    if (owner) {
      sx.repo.notify({
        projectId: sx.projectId, personId: owner, event: 'basis_superseded',
        recordType: l.record_type, recordId: l.record_id,
        recordRef: String(rec.ref ?? rec.docNo ?? `#${l.record_id}`),
        reason: `${d.ref} (a basis of your record) was superseded by ${replacement.ref}`,
        nextAction: 'review whether your work is affected', due: null,
      })
    }
  }
  // P2: the supersession link is a first-class record — old basis → replacement with the
  // affected-record set identified for review (PEC-AUTH-005 pattern; propagation is P3)
  sx.repo.insert('supersession_link', {
    projectId: sx.projectId, recordType: 'decision', oldId: id, newId: replacement.id,
    affected, createdBy: sx.session.personId, createdAt: nowIso(),
  })
  // conditions satisfied by the superseded decision flip back open (defense in depth mirrors core)
  unsatisfyConditions(sx, (c) => c.satisfiedByType === 'decision' && c.satisfiedById === id,
    `decision ${d.ref} superseded`)
  return sx.repo.get<Decision>('decision', sx.projectId, id)
}

// ---------- waivers (I-8, D-09) ----------

export function waiveCondition(
  sx: Sx, conditionId: number,
  payload: { version: number; rationale: string },
): { condition: Condition; decision: Decision } {
  const c = sx.repo.get<Condition>('condition_record', sx.projectId, conditionId)
  requireCan(sx, 'condition.waive', { conditionType: c.type })
  if (c.state !== 'open') throw badRequest(`only open conditions can be waived (state: ${c.state})`)
  if (!payload.rationale) throw badRequest('waiver rationale required (I-8)')

  const decision = recordDecisionRow(sx, {
    title: `Waive ${c.ref}`,
    statement: `Waive condition ${c.ref}: ${c.description} (gate ${c.gatedTransition} on ${c.parentType}#${c.parentId})`,
    authorityId: sx.session.personId,
    outcome: 'waive', rationale: payload.rationale, kind: 'waiver', conditionId: c.id,
  })
  sx.repo.insert('decision_link', { decisionId: decision.id, recordType: 'condition', recordId: c.id, relation: 'affects' })
  sx.repo.update('condition_record', sx.projectId, conditionId, payload.version, {
    state: 'waived', waiverDecisionId: decision.id,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'condition', recordId: conditionId,
    actorId: sx.session.personId, kind: 'waived',
    summary: `${c.ref} waived by ${decision.ref}: ${payload.rationale}`,
    payload: { decisionRef: decision.ref }, authorityRef: decision.ref,
  })
  sx.repo.audit({
    projectId: sx.projectId, actorId: sx.session.personId, action: 'waiver',
    recordType: 'condition', recordId: conditionId,
    priorValue: { state: 'open' }, newValue: { state: 'waived', decision: decision.ref },
    authorityRef: decision.ref,
  })
  if (c.parentType === 'approval_record') syncApprovalState(sx, c.parentId)
  return { condition: sx.repo.get<Condition>('condition_record', sx.projectId, conditionId), decision }
}

// ---------- approval records (§4.5) ----------

export interface CreateApprovalInput {
  title: string
  approvalType: string
  authoritySource?: string
  appliesToType: RecordType
  appliesToId: number
  authorityHolder?: string
  requiredDecisionType?: string
  signatoryIds: number[]
  basisRef?: string
  dueDate?: string
  holdPoint?: boolean
  /** extra prerequisites beyond the default check prerequisite */
  prerequisites?: Array<Omit<ConditionInput, 'parentType' | 'parentId' | 'gatedTransition'>>
  /** set false to skip the default check prerequisite (e.g. non-revision targets) */
  defaultCheckPrereq?: boolean
}

export function createApprovalRecord(sx: Sx, input: CreateApprovalInput, opts?: { skipPermission?: boolean }): ApprovalRecord {
  if (!opts?.skipPermission) requireCan(sx, 'approval.create')
  if (!input.title || !input.approvalType) throw badRequest('title and approval type required (PEC-AUTH-001)')
  if (!input.signatoryIds || input.signatoryIds.length === 0) {
    throw badRequest('named signatories required in P1 (D-12)')
  }
  const table = TABLE[input.appliesToType]
  if (!table) throw badRequest(`invalid applies-to type: ${input.appliesToType}`)
  sx.repo.get(table, sx.projectId, input.appliesToId)

  const ref = sx.repo.nextRef(sx.projectId, 'approval_record')
  const id = sx.repo.insert('approval_record', {
    projectId: sx.projectId, ref, title: input.title, approvalType: input.approvalType,
    authoritySource: input.authoritySource ?? null,
    appliesToType: input.appliesToType, appliesToId: input.appliesToId,
    authorityHolder: input.authorityHolder ?? null,
    requiredDecisionType: input.requiredDecisionType ?? null,
    signatoryIds: input.signatoryIds, basisRef: input.basisRef ?? null,
    dueDate: optDate(input.dueDate, 'due date'), holdPoint: input.holdPoint ?? false,
    state: 'required', createdAt: nowIso(),
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'approval_record', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref} required: ${input.title} (${input.approvalType}), authority: ${input.authoritySource ?? 'unstated'}, signatories: ${input.signatoryIds.join(', ')}`,
    payload: null, authorityRef: input.basisRef ?? null,
  })

  // Default prerequisite: a check-type condition resolving through applies_to (review resolution 6).
  const wantDefault = input.defaultCheckPrereq ?? (input.appliesToType === 'revision')
  if (wantDefault) {
    createCondition(sx, {
      parentType: 'approval_record', parentId: id, gatedTransition: 'approval_record.ready',
      type: 'check', description: 'Check accepted on the revision under approval',
      severity: 'hard', source: 'template', sourceRef: 'default-approval-prereq',
    }, { skipPermission: true })
  }
  for (const p of input.prerequisites ?? []) {
    createCondition(sx, {
      ...p, parentType: 'approval_record', parentId: id, gatedTransition: 'approval_record.ready',
      severity: p.severity ?? 'hard', source: p.source ?? 'manual',
    }, { skipPermission: true })
  }
  // Pure readiness re-evaluation: zero prerequisites → ready immediately.
  syncApprovalState(sx, id)
  return sx.repo.get<ApprovalRecord>('approval_record', sx.projectId, id)
}

export interface ApprovalOutcomeInput {
  version: number
  outcome: 'approve' | 'conditionally_accept' | 'reject' | 'defer'
  rationale: string
  /** conditions instantiated on the target when approved-with-conditions */
  conditionsCreated?: ConditionInput[]
  /** rework items created on reject */
  reworkItems?: CreateWorkItemInput[]
  /** new due date on defer */
  newDueDate?: string
}

/**
 * §4.5 ready → decided: the ONLY path (PEC-AUTH-004). Creates the outcome Decision
 * (OM-6) linked back, writes the audit event, instantiates outcome conditions,
 * creates rework items on reject, and advances/reverts the target revision.
 */
export function recordApprovalOutcome(sx: Sx, id: number, input: ApprovalOutcomeInput): ApprovalRecord {
  const a = sx.repo.get<ApprovalRecord>('approval_record', sx.projectId, id)
  const def = findTransition('approval_record', 'record_outcome', a.state)
  if (!def) throw badRequest(`approval record is ${a.state}; outcomes are recorded from ready only (§7.5)`)
  // Approval outcomes are a restricted set (I-6, PEC-AUTH-002): an approval record is not a
  // free-form decision. Reject anything outside {approve, conditionally_accept, reject, defer}.
  const APPROVAL_OUTCOMES = ['approve', 'conditionally_accept', 'reject', 'defer']
  if (!APPROVAL_OUTCOMES.includes(input.outcome)) {
    throw badRequest(`approval outcome must be one of ${APPROVAL_OUTCOMES.join(', ')} (PEC-AUTH-002); got ${input.outcome}`)
  }
  const isSignatory = a.signatoryIds.includes(sx.session.personId)
  requireCan(sx, 'approval.outcome', { isSignatory })
  if (!input.rationale) throw badRequest('rationale required')
  const deferDue = input.outcome === 'defer' ? optDate(input.newDueDate, 'new due date') : null
  const snap = snapshot(sx)
  assertNoActiveHold(sx, snap, 'approval_record', id, 'approval_record.record_outcome')

  const decision = recordDecisionRow(sx, {
    title: `${a.ref} outcome: ${input.outcome}`,
    statement: `Approval outcome for ${a.ref} (${a.title})`,
    authorityId: sx.session.personId,
    outcome: input.outcome, rationale: input.rationale,
    kind: 'approval_outcome', approvalRecordId: a.id,
  })
  sx.repo.insert('decision_link', { decisionId: decision.id, recordType: 'approval_record', recordId: a.id, relation: 'affects' })

  if (input.outcome === 'defer') {
    // §7.5: deferred → need-by reset; the record stays a pending basis record (state ready).
    sx.repo.update('approval_record', sx.projectId, id, input.version, {
      dueDate: deferDue ?? a.dueDate, outcomeDecisionId: decision.id,
    })
    sx.repo.history({
      projectId: sx.projectId, recordType: 'approval_record', recordId: id,
      actorId: sx.session.personId, kind: 'deferred',
      summary: `${a.ref} deferred by ${decision.ref}; due reset to ${deferDue ?? a.dueDate ?? '—'}`,
      payload: null, authorityRef: decision.ref,
    })
  } else {
    sx.repo.update('approval_record', sx.projectId, id, input.version, {
      state: 'decided', outcomeDecisionId: decision.id,
    })
    sx.repo.history({
      projectId: sx.projectId, recordType: 'approval_record', recordId: id,
      actorId: sx.session.personId, kind: 'decided',
      summary: `${a.ref} ${input.outcome} — outcome recorded as ${decision.ref} (OM-6); record remains the authorization basis`,
      payload: null, authorityRef: decision.ref,
    })
  }
  sx.repo.audit({
    projectId: sx.projectId, actorId: sx.session.personId, action: 'approval_outcome',
    recordType: 'approval_record', recordId: id,
    priorValue: { state: a.state }, newValue: { outcome: input.outcome, decision: decision.ref },
    authorityRef: decision.ref,
  })

  if (input.outcome === 'approve' || input.outcome === 'conditionally_accept') {
    for (const c of input.conditionsCreated ?? []) {
      createCondition(sx, { ...c, source: 'decision', sourceRef: decision.ref }, { skipPermission: true })
    }
    // approval-type conditions pinned to this record or unpinned on its target (§5.3)
    satisfyConditions(
      sx,
      (c) => c.type === 'approval' && (
        (c.requiredRefType === 'approval_record' && c.requiredRefId === id)
        || (c.requiredRefId == null && c.parentType === a.appliesToType && c.parentId === a.appliesToId)
      ),
      { type: 'approval_record', id, ref: a.ref },
    )
  }
  if (input.outcome === 'reject') {
    const items = input.reworkItems ?? []
    if (items.length === 0 && a.appliesToType === 'revision') {
      const rev = sx.repo.get<{ deliverableId: number }>('revision', sx.projectId, a.appliesToId)
      const del = sx.repo.get<{ ownerId: number | null; docNo: string }>('deliverable', sx.projectId, rev.deliverableId)
      if (del.ownerId) {
        items.push({
          title: `Rework ${del.docNo} after ${a.ref} rejection`,
          statement: input.rationale, kind: 'rework',
          anchorType: 'revision', anchorId: a.appliesToId,
          ownerId: del.ownerId, needBy: null,
        })
      }
    }
    for (const f of items) {
      const wi = createWorkItem(sx, { ...f, kind: f.kind ?? 'rework', sourceType: 'decision', sourceId: decision.id }, { skipPermission: true })
      sx.repo.insert('decision_link', { decisionId: decision.id, recordType: 'work_item', recordId: wi.id, relation: 'follow_up' })
    }
  }
  if (a.appliesToType === 'revision') syncRevisionState(sx, a.appliesToId)
  return sx.repo.get<ApprovalRecord>('approval_record', sx.projectId, id)
}

export function supersedeApproval(sx: Sx, id: number, payload: { version: number; replacementId: number }): ApprovalRecord {
  const a = sx.repo.get<ApprovalRecord>('approval_record', sx.projectId, id)
  const def = findTransition('approval_record', 'supersede', a.state)
  if (!def) throw badRequest(`illegal transition: supersede from ${a.state}`)
  requireCan(sx, 'approval.supersede')
  if (!payload.replacementId) throw badRequest('supersession requires the replacement approval record (I-10)')
  if (payload.replacementId === id) throw badRequest('an approval record cannot supersede itself — the replacement must be a distinct record (I-10)')
  const replacement = sx.repo.get<ApprovalRecord>('approval_record', sx.projectId, payload.replacementId)
  if (replacement.state === 'superseded') throw badRequest(`${replacement.ref} is itself superseded; supersede with a live replacement (I-10)`)
  sx.repo.update('approval_record', sx.projectId, id, payload.version, {
    state: 'superseded', supersededById: replacement.id,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'approval_record', recordId: id,
    actorId: sx.session.personId, kind: 'superseded',
    summary: `${a.ref} superseded by ${replacement.ref} — remains visible (I-10); affected records flagged`,
    payload: null, authorityRef: null,
  })
  // flag target for review + reopen conditions satisfied by this approval
  const affected: Array<{ recordType: RecordType; id: number; ref: string }> = []
  const table = TABLE[a.appliesToType]
  if (table) {
    const rec = sx.repo.maybeGet<Record<string, unknown>>(table, sx.projectId, a.appliesToId)
    if (rec) {
      affected.push({
        recordType: a.appliesToType as RecordType, id: a.appliesToId,
        ref: String(rec.ref ?? rec.docNo ?? `#${a.appliesToId}`),
      })
    }
    const owner = (rec?.ownerId ?? null) as number | null
    if (owner) {
      sx.repo.notify({
        projectId: sx.projectId, personId: owner, event: 'basis_superseded',
        recordType: a.appliesToType, recordId: a.appliesToId,
        recordRef: String(rec?.ref ?? rec?.docNo ?? `#${a.appliesToId}`),
        reason: `${a.ref} (authorization basis) superseded by ${replacement.ref}`,
        nextAction: 'review whether your work is affected', due: null,
      })
    }
  }
  const satisfiedConds = sx.repo.list<Condition>('condition_record', sx.projectId,
    "satisfied_by_type = 'approval_record' AND satisfied_by_id = ?", [id])
  for (const c of satisfiedConds) affected.push({ recordType: 'condition', id: c.id, ref: c.ref })
  unsatisfyConditions(sx, (c) => c.satisfiedByType === 'approval_record' && c.satisfiedById === id,
    `approval ${a.ref} superseded`)
  // P2: first-class supersession link with the affected-record set (PEC-AUTH-005)
  sx.repo.insert('supersession_link', {
    projectId: sx.projectId, recordType: 'approval_record', oldId: id, newId: replacement.id,
    affected, createdBy: sx.session.personId, createdAt: nowIso(),
  })
  if (a.appliesToType === 'revision') syncRevisionState(sx, a.appliesToId)
  return sx.repo.get<ApprovalRecord>('approval_record', sx.projectId, id)
}
