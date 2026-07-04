/**
 * Intake services (§4.1, OM-3, PEC-AHL-*). The concern-as-raised is preserved verbatim
 * (trigger-enforced); triage resolves it into controlled records, each back-linked;
 * the raiser is notified at routing and closure (PEC-AHL-007).
 */

import type { IntakeItem, Log } from '@pec/core'
import { INTAKE_DISPOSITIONS, INTAKE_QUICK_TYPES, findTransition } from '@pec/core'
import { badRequest } from '../errors.ts'
import { nowIso } from '../repo.ts'
import { optDate } from '../validate.ts'
import type { Sx } from './shared.ts'
import { requireCan } from './shared.ts'
import { createWorkItem } from './work.ts'
import type { CreateWorkItemInput } from './work.ts'
import { raiseHold } from './holds.ts'
import type { RaiseHoldInput } from './holds.ts'
import { createDecision } from './decisions.ts'
import type { CreateApprovalInput, CreateDecisionInput } from './decisions.ts'
import { createApprovalRecord } from './decisions.ts'
import { createInterface, createRisk } from './registers.ts'
import type { CreateInterfaceInput, CreateRiskInput } from './registers.ts'

/** Raise-an-item: ≤ 8 fields (PEC-AHL-003). */
export interface RaiseIntakeInput {
  statement: string
  quickType: IntakeItem['quickType']
  anchorSuggestion?: string
  needBy?: string
  suggestedOwnerId?: number
  log?: Log
}

export function raiseIntake(sx: Sx, input: RaiseIntakeInput): IntakeItem {
  requireCan(sx, 'intake.raise')
  if (!input.statement) throw badRequest('statement required — it is preserved verbatim (OM-3)')
  if (!INTAKE_QUICK_TYPES.includes(input.quickType)) {
    throw badRequest(`type must be one of the quick types (PEC-AHL-003): ${INTAKE_QUICK_TYPES.join(', ')}`)
  }
  const ref = sx.repo.nextRef(sx.projectId, 'intake_item')
  const id = sx.repo.insert('intake_item', {
    projectId: sx.projectId, ref, statementVerbatim: input.statement, quickType: input.quickType,
    anchorSuggestion: input.anchorSuggestion ?? null, needBy: optDate(input.needBy, 'need-by'),
    suggestedOwnerId: input.suggestedOwnerId ?? null, log: input.log ?? 'internal',
    raisedBy: sx.session.personId, raisedAt: nowIso(), state: 'raised',
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'intake_item', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref} raised (${input.quickType})`, payload: null, authorityRef: null,
  })
  return sx.repo.get<IntakeItem>('intake_item', sx.projectId, id)
}

export function openTriage(sx: Sx, id: number, version: number): IntakeItem {
  const item = sx.repo.get<IntakeItem>('intake_item', sx.projectId, id)
  const def = findTransition('intake_item', 'open_triage', item.state)
  if (!def) throw badRequest(`illegal transition: open_triage from ${item.state}`)
  requireCan(sx, 'intake.triage')
  sx.repo.update('intake_item', sx.projectId, id, version, { state: 'in_triage' })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'intake_item', recordId: id,
    actorId: sx.session.personId, kind: 'transition',
    summary: `${item.ref}: raised → in_triage`, payload: null, authorityRef: null,
  })
  return sx.repo.get<IntakeItem>('intake_item', sx.projectId, id)
}

/** One intake may resolve into multiple controlled records (PEC-AHL-005). */
export interface ConversionRecords {
  workItems?: CreateWorkItemInput[]
  holds?: RaiseHoldInput[]
  risks?: CreateRiskInput[]
  decisions?: CreateDecisionInput[]
  approvalRecords?: CreateApprovalInput[]
  interfaces?: CreateInterfaceInput[]
}

export interface DispositionInput {
  version: number
  disposition: IntakeItem['disposition']
  note?: string
  mergedIntoIntakeId?: number
  records?: ConversionRecords
}

export function dispositionIntake(sx: Sx, id: number, input: DispositionInput): {
  intake: IntakeItem
  created: Array<{ recordType: string; recordId: number; ref: string }>
} {
  const item = sx.repo.get<IntakeItem>('intake_item', sx.projectId, id)
  const def = findTransition('intake_item', 'disposition', item.state)
  if (!def) throw badRequest(`illegal transition: disposition from ${item.state}`)
  requireCan(sx, 'intake.triage')
  if (!input.disposition || !INTAKE_DISPOSITIONS.includes(input.disposition)) {
    throw badRequest(`disposition must be one of: ${INTAKE_DISPOSITIONS.join(', ')} (PEC-AHL-004)`)
  }
  if (input.disposition === 'merged' && !input.mergedIntoIntakeId) {
    throw badRequest('merged disposition requires the surviving intake item')
  }
  const created: Array<{ recordType: string; recordId: number; ref: string }> = []
  if (input.disposition === 'converted') {
    const r = input.records ?? {}
    const total = (r.workItems?.length ?? 0) + (r.holds?.length ?? 0) + (r.risks?.length ?? 0)
      + (r.decisions?.length ?? 0) + (r.approvalRecords?.length ?? 0) + (r.interfaces?.length ?? 0)
    if (total === 0) throw badRequest('converted disposition requires ≥1 record to create (PEC-AHL-005)')
    // Conversion acts under the coordinator's triage authority: skip per-type create
    // permissions (the coordinator routes; owners stay accountable — 12 Rules, rule 11).
    for (const w of r.workItems ?? []) {
      const wi = createWorkItem(sx, { ...w, sourceType: 'intake_item', sourceId: id }, { skipPermission: true })
      created.push({ recordType: 'work_item', recordId: wi.id, ref: wi.ref })
    }
    for (const h of r.holds ?? []) {
      const hold = raiseHold(sx, h, { skipPermission: true })
      created.push({ recordType: 'hold', recordId: hold.id, ref: hold.ref })
    }
    for (const rk of r.risks ?? []) {
      const risk = createRisk(sx, rk, { skipPermission: true })
      created.push({ recordType: 'risk', recordId: risk.id, ref: risk.ref })
    }
    for (const d of r.decisions ?? []) {
      const dec = createDecision(sx, d, { skipPermission: true })
      created.push({ recordType: 'decision', recordId: dec.id, ref: dec.ref })
    }
    for (const ap of r.approvalRecords ?? []) {
      const a = createApprovalRecord(sx, ap, { skipPermission: true })
      created.push({ recordType: 'approval_record', recordId: a.id, ref: a.ref })
    }
    for (const itf of r.interfaces ?? []) {
      const i = createInterface(sx, itf, { skipPermission: true })
      created.push({ recordType: 'interface_item', recordId: i.id, ref: i.ref })
    }
    for (const c of created) {
      sx.repo.insert('intake_link', { intakeId: id, recordType: c.recordType, recordId: c.recordId })
    }
  }

  sx.repo.update('intake_item', sx.projectId, id, input.version, {
    state: 'dispositioned', disposition: input.disposition,
    dispositionNote: input.note ?? null, mergedIntoIntakeId: input.mergedIntoIntakeId ?? null,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'intake_item', recordId: id,
    actorId: sx.session.personId, kind: 'dispositioned',
    summary: `${item.ref} dispositioned: ${input.disposition}${created.length > 0 ? ` → ${created.map((c) => c.ref).join(', ')}` : ''}${input.note ? ` (${input.note})` : ''}`,
    payload: { disposition: input.disposition, created }, authorityRef: null,
  })
  // Raiser notified at routing (PEC-AHL-007); ownership/closure notifications follow on the records.
  sx.repo.notify({
    projectId: sx.projectId, personId: item.raisedBy, event: 'raised_item_routed',
    recordType: 'intake_item', recordId: id, recordRef: item.ref,
    reason: `your item was ${input.disposition}${created.length > 0 ? `: ${created.map((c) => c.ref).join(', ')}` : ''}`,
    nextAction: 'no action needed', due: null,
  })
  return { intake: sx.repo.get<IntakeItem>('intake_item', sx.projectId, id), created }
}
