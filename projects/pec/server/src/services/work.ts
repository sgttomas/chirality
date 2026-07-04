/**
 * Work item services (§4.2, §3.3). One assignable entity (OM-1); always anchored (I-2);
 * close is condition-gated and hold-vetoed (I-5, OM-2).
 */

import type { AnchorType, Deliverable, WorkItem } from '@pec/core'
import { ANCHOR_TYPES, WORK_ITEM_KINDS, findTransition } from '@pec/core'
import { badRequest, notFound } from '../errors.ts'
import { nowIso } from '../repo.ts'
import { optDate } from '../validate.ts'
import type { Sx } from './shared.ts'
import { gateOrThrow, requireCan, satisfyConditions, snapshot } from './shared.ts'

/** Package attribution per anchor type (SPEC §3.3; review resolution 13). */
export function derivePackageId(sx: Sx, anchorType: AnchorType, anchorId: number): number | null {
  switch (anchorType) {
    case 'package':
      return anchorId
    case 'deliverable':
      return sx.repo.get<Deliverable>('deliverable', sx.projectId, anchorId).packageId
    case 'revision': {
      const rev = sx.repo.get<{ deliverableId: number }>('revision', sx.projectId, anchorId)
      return sx.repo.get<Deliverable>('deliverable', sx.projectId, rev.deliverableId).packageId
    }
    case 'decision':
      return sx.repo.get<{ packageId: number | null }>('decision', sx.projectId, anchorId).packageId
    case 'approval_record': {
      const a = sx.repo.get<{ appliesToType: AnchorType; appliesToId: number }>('approval_record', sx.projectId, anchorId)
      if (a.appliesToType === 'deliverable' || a.appliesToType === 'revision' || a.appliesToType === 'package') {
        return derivePackageId(sx, a.appliesToType, a.appliesToId)
      }
      return null
    }
    case 'risk':
      return sx.repo.get<{ packageId: number | null }>('risk', sx.projectId, anchorId).packageId
    case 'interface_item': {
      const i = sx.repo.get<{ givingPackageId: number | null; receivingPackageId: number | null }>('interface_item', sx.projectId, anchorId)
      return i.givingPackageId ?? i.receivingPackageId
    }
  }
}

export interface CreateWorkItemInput {
  title: string
  statement?: string
  kind?: WorkItem['kind']
  log?: WorkItem['log']
  anchorType: AnchorType
  anchorId: number
  ownerId: number
  needBy: string | null
  priority?: string
  priorityProvenance?: string
  sourceType?: WorkItem['sourceType']
  sourceId?: number
  committedWeek?: string | null
}

export function createWorkItem(sx: Sx, input: CreateWorkItemInput, opts?: { skipPermission?: boolean }): WorkItem {
  if (!opts?.skipPermission) requireCan(sx, 'work_item.create')
  if (!input.title) throw badRequest('title is required')
  if (!input.ownerId) throw badRequest('owner is required (always owned, PRD §4.4)')
  if (!ANCHOR_TYPES.includes(input.anchorType)) throw badRequest(`invalid anchor type: ${input.anchorType} (I-2)`)
  if (!input.anchorId) throw badRequest('work items must be anchored at creation (I-2)')
  if (input.kind && !WORK_ITEM_KINDS.includes(input.kind)) throw badRequest(`invalid kind: ${input.kind}`)
  const needBy = optDate(input.needBy, 'need-by')
  // verify the anchor exists in this project (throws notFound otherwise) and derive package
  const packageId = derivePackageId(sx, input.anchorType, input.anchorId)

  const ref = sx.repo.nextRef(sx.projectId, 'work_item')
  const id = sx.repo.insert('work_item', {
    projectId: sx.projectId, ref, title: input.title, statement: input.statement ?? null,
    kind: input.kind ?? 'action', log: input.log ?? 'internal',
    anchorType: input.anchorType, anchorId: input.anchorId, packageId,
    ownerId: input.ownerId, needBy,
    priority: input.priority ?? null, priorityProvenance: input.priorityProvenance ?? null,
    state: 'open', committedWeek: input.committedWeek ?? null,
    sourceType: input.sourceType ?? null, sourceId: input.sourceId ?? null,
    createdBy: sx.session.personId, createdAt: nowIso(),
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'work_item', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref} created, anchored to ${input.anchorType}#${input.anchorId}, owner #${input.ownerId}`,
    payload: { input }, authorityRef: null,
  })
  sx.repo.notify({
    projectId: sx.projectId, personId: input.ownerId, event: 'assigned',
    recordType: 'work_item', recordId: id, recordRef: ref,
    reason: 'you were assigned a work item', nextAction: 'review and start the item',
    due: input.needBy ?? null,
  })
  return sx.repo.get<WorkItem>('work_item', sx.projectId, id)
}

const EDITABLE = [
  'title', 'statement', 'kind', 'log', 'needBy', 'priority', 'priorityProvenance',
  'committedWeek', 'ownerId', 'anchorType', 'anchorId',
] as const

export function updateWorkItem(
  sx: Sx, id: number, version: number, patch: Partial<WorkItem>,
): WorkItem {
  const wi = sx.repo.get<WorkItem>('work_item', sx.projectId, id)
  requireCan(sx, 'work_item.update', { isOwner: wi.ownerId === sx.session.personId })
  const clean: Record<string, unknown> = {}
  for (const k of EDITABLE) if (k in patch) clean[k] = patch[k]
  if (Object.keys(clean).length === 0) throw badRequest('no editable fields in patch')
  if ('needBy' in clean) clean.needBy = optDate(clean.needBy, 'need-by')
  if ('committedWeek' in clean) {
    // the API commit toggle is the owner's manual flag; the weekly planning commit stamps
    // commit_source='plan' through its own path (PEC-MW-007 / PEC-PLAN-007)
    clean.commitSource = clean.committedWeek == null ? null : 'manual'
  }
  if ('anchorType' in clean || 'anchorId' in clean) {
    const at = (clean.anchorType ?? wi.anchorType) as AnchorType
    const ai = (clean.anchorId ?? wi.anchorId) as number
    if (!ANCHOR_TYPES.includes(at) || !ai) throw badRequest('re-anchoring requires a valid anchor (I-2)')
    clean.anchorType = at
    clean.anchorId = ai
    clean.packageId = derivePackageId(sx, at, ai)
  }
  if ('log' in clean && clean.log !== wi.log) {
    // items never change log silently (PEC-AHL-002)
    sx.repo.history({
      projectId: sx.projectId, recordType: 'work_item', recordId: id,
      actorId: sx.session.personId, kind: 'log_change',
      summary: `${wi.ref} moved from ${wi.log} log to ${clean.log} log`, payload: null, authorityRef: null,
    })
  }
  sx.repo.update('work_item', sx.projectId, id, version, clean)
  const changed = Object.keys(clean).filter((k) => (clean as Record<string, unknown>)[k] !== (wi as unknown as Record<string, unknown>)[k])
  sx.repo.history({
    projectId: sx.projectId, recordType: 'work_item', recordId: id,
    actorId: sx.session.personId, kind: 'field_change',
    summary: `${wi.ref} updated: ${changed.join(', ')}`, payload: clean, authorityRef: null,
  })
  if ('ownerId' in clean && clean.ownerId !== wi.ownerId) {
    sx.repo.notify({
      projectId: sx.projectId, personId: clean.ownerId as number, event: 'assigned',
      recordType: 'work_item', recordId: id, recordRef: wi.ref,
      reason: 'work item reassigned to you', nextAction: 'review and start the item', due: wi.needBy,
    })
    notifyIntakeRaiser(sx, wi, 'raised_item_updated', `ownership of ${wi.ref} changed`)
  }
  return sx.repo.get<WorkItem>('work_item', sx.projectId, id)
}

/** Progress update: the status update and its history entry are the same record (PEC-DEL-005). */
export function addProgress(sx: Sx, id: number, note: string): void {
  const wi = sx.repo.get<WorkItem>('work_item', sx.projectId, id)
  requireCan(sx, 'work_item.update', { isOwner: wi.ownerId === sx.session.personId })
  if (!note) throw badRequest('progress note required')
  sx.repo.history({
    projectId: sx.projectId, recordType: 'work_item', recordId: id,
    actorId: sx.session.personId, kind: 'progress', summary: note, payload: null, authorityRef: null,
  })
}

export function transitionWorkItem(
  sx: Sx, id: number, event: string,
  payload: { version: number; reason?: string; closingStatement?: string },
): WorkItem {
  const wi = sx.repo.get<WorkItem>('work_item', sx.projectId, id)
  const def = findTransition('work_item', event, wi.state)
  if (!def) throw badRequest(`illegal transition: ${event} from ${wi.state}`)
  if (def.auto) throw badRequest(`${event} is system-driven`)
  requireCan(sx, def.permission as never, { isOwner: wi.ownerId === sx.session.personId })
  if (def.requires.includes('reason') && !payload.reason) throw badRequest('reason is required')

  const snap = snapshot(sx)
  if (def.gate || def.holdVeto) {
    gateOrThrow(sx, snap, 'work_item', id, wi.ref, def.gate ?? `work_item.${event}`, { holdVeto: def.holdVeto })
  }

  const patch: Record<string, unknown> = { state: def.to }
  if (event === 'close') {
    patch.closingStatement = payload.closingStatement ?? null
    patch.closedBy = sx.session.personId
    patch.closedAt = nowIso()
  }
  if (event === 'cancel') patch.cancelReason = payload.reason
  sx.repo.update('work_item', sx.projectId, id, payload.version, patch)
  sx.repo.history({
    projectId: sx.projectId, recordType: 'work_item', recordId: id,
    actorId: sx.session.personId, kind: 'transition',
    summary: `${wi.ref}: ${wi.state} → ${def.to}${payload.reason ? ` (${payload.reason})` : ''}`,
    payload: { event, reason: payload.reason ?? null }, authorityRef: null,
  })
  if (event === 'close' || event === 'cancel') {
    notifyIntakeRaiser(sx, wi, 'raised_item_closed', `${wi.ref} ${def.to}`)
  }
  return sx.repo.get<WorkItem>('work_item', sx.projectId, id)
}

/** PEC-AHL-007: raiser notified at routing, ownership, and closure of records created from their intake. */
export function notifyIntakeRaiser(
  sx: Sx, wi: Pick<WorkItem, 'sourceType' | 'sourceId' | 'ref' | 'id'>,
  event: 'raised_item_updated' | 'raised_item_closed', reason: string,
): void {
  if (wi.sourceType !== 'intake_item' || wi.sourceId == null) return
  const intake = sx.repo.maybeGet<{ raisedBy: number; ref: string }>('intake_item', sx.projectId, wi.sourceId)
  if (!intake) return
  sx.repo.notify({
    projectId: sx.projectId, personId: intake.raisedBy, event,
    recordType: 'work_item', recordId: wi.id, recordRef: wi.ref,
    reason: `${reason} (from your ${intake.ref})`, nextAction: 'no action needed', due: null,
  })
}

// ---------- evidence (review resolution 13) ----------

export function addEvidence(
  sx: Sx,
  recordType: string, recordId: number,
  input: { kind?: string; label: string; urlOrPath?: string; content?: string },
): number {
  requireCan(sx, 'evidence.add')
  if (!input.label) throw badRequest('evidence label required')
  // verify parent exists in this project
  const table = ({
    work_item: 'work_item', revision: 'revision', deliverable: 'deliverable', hold: 'hold',
    check: 'check_record', review_comment: 'review_comment', approval_record: 'approval_record',
    decision: 'decision', risk: 'risk', interface_item: 'interface_item', condition: 'condition_record',
    intake_item: 'intake_item', issue_event: 'issue_event',
  } as Record<string, string>)[recordType]
  if (!table) throw badRequest(`evidence cannot attach to ${recordType}`)
  if (!sx.repo.maybeGet(table, sx.projectId, recordId)) throw notFound(`${recordType}#${recordId}`)

  const id = sx.repo.insert('evidence', {
    projectId: sx.projectId, recordType, recordId,
    kind: input.kind ?? 'attachment', label: input.label,
    urlOrPath: input.urlOrPath ?? null, content: input.content ?? null,
    addedBy: sx.session.personId, addedAt: nowIso(),
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: recordType as never, recordId,
    actorId: sx.session.personId, kind: 'evidence',
    summary: `evidence attached: ${input.label}`, payload: { evidenceId: id }, authorityRef: null,
  })
  // evidence-type conditions on this parent with the matching artifact name (§5.3)
  satisfyConditions(
    sx,
    (c) => c.type === 'evidence' && c.parentType === recordType && c.parentId === recordId
      && c.requiredArtifactName === input.label,
    { type: 'evidence', id, ref: input.label },
  )
  return id
}
