/**
 * Register services: risks (§12.10), interface items (§12.11, OM-7),
 * packages and deliverables (§3.2).
 */

import type { Deliverable, InterfaceItem, Log, Package, Risk } from '@pec/core'
import { INTERFACE_STATES, RISK_STATES } from '@pec/core'
import { badRequest } from '../errors.ts'
import { optDate } from '../validate.ts'
import type { Sx } from './shared.ts'
import { requireCan } from './shared.ts'

// ---------- risks ----------

export interface CreateRiskInput {
  title: string
  cause?: string
  consequence?: string
  packageId?: number
  deliverableId?: number
  ownerId?: number
  probability?: number
  impact?: number
  mitigation?: string
  needBy?: string
}

/** probability/impact are a 1-5 scale (PEC-RISK-001); enforced here as in the CSV importer. */
function validateRiskScore(name: string, v: unknown): void {
  if (v == null) return
  if (typeof v !== 'number' || !Number.isInteger(v) || v < 1 || v > 5) {
    throw badRequest(`${name} must be an integer 1-5 (PEC-RISK-001)`)
  }
}

export function createRisk(sx: Sx, input: CreateRiskInput, opts?: { skipPermission?: boolean }): Risk {
  if (!opts?.skipPermission) requireCan(sx, 'risk.create')
  if (!input.title) throw badRequest('risk title required')
  validateRiskScore('probability', input.probability)
  validateRiskScore('impact', input.impact)
  if (input.packageId) sx.repo.get('package', sx.projectId, input.packageId)
  if (input.deliverableId) sx.repo.get('deliverable', sx.projectId, input.deliverableId)
  const ref = sx.repo.nextRef(sx.projectId, 'risk')
  const id = sx.repo.insert('risk', {
    projectId: sx.projectId, ref, title: input.title,
    cause: input.cause ?? null, consequence: input.consequence ?? null,
    packageId: input.packageId ?? null, deliverableId: input.deliverableId ?? null,
    ownerId: input.ownerId ?? null, probability: input.probability ?? null,
    impact: input.impact ?? null, mitigation: input.mitigation ?? null,
    needBy: optDate(input.needBy, 'need-by'), state: 'open',
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'risk', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref} raised: ${input.title}`, payload: null, authorityRef: null,
  })
  return sx.repo.get<Risk>('risk', sx.projectId, id)
}

export function updateRisk(sx: Sx, id: number, version: number, patch: Partial<Risk>): Risk {
  const r = sx.repo.get<Risk>('risk', sx.projectId, id)
  requireCan(sx, 'risk.update', { isOwner: r.ownerId === sx.session.personId })
  const editable = ['title', 'cause', 'consequence', 'packageId', 'deliverableId', 'ownerId',
    'probability', 'impact', 'mitigation', 'needBy', 'state'] as const
  const clean: Record<string, unknown> = {}
  for (const k of editable) if (k in patch) clean[k] = patch[k]
  if ('state' in clean && !RISK_STATES.includes(clean.state as never)) throw badRequest('invalid risk state')
  if ('probability' in clean) validateRiskScore('probability', clean.probability)
  if ('impact' in clean) validateRiskScore('impact', clean.impact)
  if ('needBy' in clean) clean.needBy = optDate(clean.needBy, 'need-by')
  if (Object.keys(clean).length === 0) throw badRequest('no editable fields')
  sx.repo.update('risk', sx.projectId, id, version, clean)
  sx.repo.history({
    projectId: sx.projectId, recordType: 'risk', recordId: id,
    actorId: sx.session.personId, kind: 'field_change',
    summary: `${r.ref} updated: ${Object.keys(clean).join(', ')}`, payload: clean, authorityRef: null,
  })
  return sx.repo.get<Risk>('risk', sx.projectId, id)
}

// ---------- interfaces (OM-7) ----------

export interface CreateInterfaceInput {
  title: string
  givingParty: string
  receivingParty: string
  givingPackageId?: number
  receivingPackageId?: number
  requiredInfo?: string
  needBy?: string
  log?: Log
  affectedDeliverableIds?: number[]
}

export function createInterface(sx: Sx, input: CreateInterfaceInput, opts?: { skipPermission?: boolean }): InterfaceItem {
  if (!opts?.skipPermission) requireCan(sx, 'interface.create')
  if (!input.title || !input.givingParty || !input.receivingParty) {
    throw badRequest('interface items carry giving party, receiving party (PEC-PKG-007)')
  }
  const ref = sx.repo.nextRef(sx.projectId, 'interface_item')
  const id = sx.repo.insert('interface_item', {
    projectId: sx.projectId, ref, title: input.title,
    givingParty: input.givingParty, receivingParty: input.receivingParty,
    givingPackageId: input.givingPackageId ?? null, receivingPackageId: input.receivingPackageId ?? null,
    requiredInfo: input.requiredInfo ?? null, needBy: optDate(input.needBy, 'need-by'),
    state: 'open', log: input.log ?? 'internal',
  })
  for (const dId of input.affectedDeliverableIds ?? []) {
    sx.repo.get('deliverable', sx.projectId, dId)
    sx.repo.insert('interface_deliverable', { interfaceId: id, deliverableId: dId })
  }
  sx.repo.history({
    projectId: sx.projectId, recordType: 'interface_item', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref}: ${input.givingParty} → ${input.receivingParty}, need-by ${input.needBy ?? '—'}`,
    payload: null, authorityRef: null,
  })
  return sx.repo.get<InterfaceItem>('interface_item', sx.projectId, id)
}

export function updateInterface(sx: Sx, id: number, version: number, patch: Partial<InterfaceItem>): InterfaceItem {
  const i = sx.repo.get<InterfaceItem>('interface_item', sx.projectId, id)
  requireCan(sx, 'interface.update')
  const editable = ['title', 'givingParty', 'receivingParty', 'givingPackageId', 'receivingPackageId',
    'requiredInfo', 'needBy', 'state', 'log'] as const
  const clean: Record<string, unknown> = {}
  for (const k of editable) if (k in patch) clean[k] = patch[k]
  if ('state' in clean && !INTERFACE_STATES.includes(clean.state as never)) throw badRequest('invalid interface state')
  if ('needBy' in clean) clean.needBy = optDate(clean.needBy, 'need-by')
  if (Object.keys(clean).length === 0) throw badRequest('no editable fields')
  if ('log' in clean && clean.log !== i.log) {
    sx.repo.history({
      projectId: sx.projectId, recordType: 'interface_item', recordId: id,
      actorId: sx.session.personId, kind: 'log_change',
      summary: `${i.ref} moved from ${i.log} log to ${clean.log} log`, payload: null, authorityRef: null,
    })
  }
  sx.repo.update('interface_item', sx.projectId, id, version, clean)
  sx.repo.history({
    projectId: sx.projectId, recordType: 'interface_item', recordId: id,
    actorId: sx.session.personId, kind: 'field_change',
    summary: `${i.ref} updated: ${Object.keys(clean).join(', ')}`, payload: clean, authorityRef: null,
  })
  return sx.repo.get<InterfaceItem>('interface_item', sx.projectId, id)
}

// ---------- packages & deliverables ----------

export function createPackage(sx: Sx, input: { code: string; name: string; leadId?: number; description?: string; milestone?: string }): Package {
  requireCan(sx, 'deliverable.create')
  if (!input.code || !input.name) throw badRequest('package code and name required')
  const id = sx.repo.insert('package', {
    projectId: sx.projectId, code: input.code, name: input.name,
    leadId: input.leadId ?? null, description: input.description ?? null,
    milestone: input.milestone ?? null,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'package', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `package ${input.code} created`, payload: null, authorityRef: null,
  })
  return sx.repo.get<Package>('package', sx.projectId, id)
}

export interface CreateDeliverableInput {
  packageId: number
  docNo: string
  title: string
  discipline?: string
  deliverableType?: string
  ownerId?: number
  dcRef?: string
  clientNo?: string
  milestone?: string
  dueDate?: string
  issuePurposePlan?: string
  remarks?: string
}

export function createDeliverable(sx: Sx, input: CreateDeliverableInput, opts?: { skipPermission?: boolean }): Deliverable {
  if (!opts?.skipPermission) requireCan(sx, 'deliverable.create')
  if (!input.docNo || !input.title || !input.packageId) {
    throw badRequest('doc number, title, and package required (PEC-DEL-002)')
  }
  sx.repo.get('package', sx.projectId, input.packageId)
  const id = sx.repo.insert('deliverable', {
    projectId: sx.projectId, packageId: input.packageId, docNo: input.docNo, title: input.title,
    discipline: input.discipline ?? null, deliverableType: input.deliverableType ?? null,
    ownerId: input.ownerId ?? null, dcRef: input.dcRef ?? null, clientNo: input.clientNo ?? null,
    milestone: input.milestone ?? null, dueDate: optDate(input.dueDate, 'due date'),
    issuePurposePlan: input.issuePurposePlan ?? null, remarks: input.remarks ?? null,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'deliverable', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${input.docNo} added to master deliverables list`, payload: null, authorityRef: null,
  })
  return sx.repo.get<Deliverable>('deliverable', sx.projectId, id)
}

export function updateDeliverable(sx: Sx, id: number, version: number, patch: Partial<Deliverable>): Deliverable {
  const d = sx.repo.get<Deliverable>('deliverable', sx.projectId, id)
  requireCan(sx, 'deliverable.update')
  const editable = ['title', 'discipline', 'deliverableType', 'ownerId', 'dcRef', 'clientNo',
    'milestone', 'dueDate', 'issuePurposePlan', 'remarks', 'packageId'] as const
  const clean: Record<string, unknown> = {}
  for (const k of editable) if (k in patch) clean[k] = patch[k]
  if ('dueDate' in clean) clean.dueDate = optDate(clean.dueDate, 'due date')
  if (Object.keys(clean).length === 0) throw badRequest('no editable fields')
  if ('packageId' in clean) sx.repo.get('package', sx.projectId, clean.packageId as number)
  sx.repo.update('deliverable', sx.projectId, id, version, clean)
  sx.repo.history({
    projectId: sx.projectId, recordType: 'deliverable', recordId: id,
    actorId: sx.session.personId, kind: 'field_change',
    summary: `${d.docNo} updated: ${Object.keys(clean).join(', ')}`, payload: clean, authorityRef: null,
  })
  if ('ownerId' in clean && clean.ownerId && clean.ownerId !== d.ownerId) {
    sx.repo.notify({
      projectId: sx.projectId, personId: clean.ownerId as number, event: 'assigned',
      recordType: 'deliverable', recordId: id, recordRef: d.docNo,
      reason: 'you are now the responsible engineer', nextAction: 'review the deliverable', due: d.dueDate,
    })
  }
  return sx.repo.get<Deliverable>('deliverable', sx.projectId, id)
}
