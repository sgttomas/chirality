/**
 * P2 Plan module services (PRD §12.4, ADR-013): plan items (work / check / approval — I-9),
 * Now/Next/Later + six-week lookahead + capacity views, the plan-shift workflow with reasons
 * and cross-package lead review (PEC-PLAN-005/006/008), the weekly commit that generates
 * My Week (PEC-PLAN-007), and capacity entries (PEC-PLAN-003).
 */

import type {
  CapacityEntry, PlanHorizon, PlanItem, PlanPeriod, PlanShift, ProjectSnapshot, RecordType, WorkItem,
} from '@pec/core'
import {
  PLAN_HORIZONS, PLAN_ITEM_TYPES, capacityView, isValidIsoWeek, isoWeekOf, isoWeeksFrom,
  lookahead, planHorizons, resolvePlanItem, visibleLogs,
} from '@pec/core'
import type { PlanItemType } from '@pec/core'
import { badRequest, forbidden, notFound } from '../errors.ts'
import { TABLE, nowIso } from '../repo.ts'
import type { Sx } from './shared.ts'
import { requireCan, snapshot } from './shared.ts'

// ---------- helpers ----------

function personDiscipline(sx: Sx, personId: number | null): string | null {
  if (personId == null) return null
  const row = sx.db.prepare('SELECT discipline FROM person WHERE id = ?').get(personId) as
    | { discipline: string | null } | undefined
  return row?.discipline ?? null
}

/** The person whose week a planned record loads (owner / checker / first signatory). */
function responsibleFor(sx: Sx, itemType: PlanItemType, itemId: number): number | null {
  if (itemType === 'work_item') {
    return (sx.repo.get<{ ownerId: number }>('work_item', sx.projectId, itemId)).ownerId
  }
  if (itemType === 'check') {
    return (sx.repo.get<{ checkerId: number }>('check_record', sx.projectId, itemId)).checkerId
  }
  const a = sx.repo.get<{ signatoryIds: number[] }>('approval_record', sx.projectId, itemId)
  return a.signatoryIds[0] ?? null
}

function requireWeekForHorizon(horizon: PlanHorizon, week: string | null): void {
  if ((horizon === 'now' || horizon === 'next') && !isValidIsoWeek(week ?? '')) {
    throw badRequest(`horizon '${horizon}' requires a valid ISO week (YYYY-Www) — 'later' is the unscheduled backlog (PEC-PLAN-001)`)
  }
  if (week != null && !isValidIsoWeek(week)) throw badRequest(`invalid ISO week: ${week}`)
}

function planItemHistory(sx: Sx, id: number, kind: string, summary: string): void {
  sx.repo.history({
    projectId: sx.projectId, recordType: 'plan_item', recordId: id,
    actorId: sx.session.personId, kind, summary, payload: null, authorityRef: null,
  })
}

// ---------- plan items (PEC-PLAN-001, I-9) ----------

export interface CreatePlanItemInput {
  itemType: PlanItemType
  itemId: number
  horizon: PlanHorizon
  week?: string | null
  plannedHours?: number
  discipline?: string | null
}

export function createPlanItem(sx: Sx, input: CreatePlanItemInput): PlanItem {
  requireCan(sx, 'plan.manage')
  if (!PLAN_ITEM_TYPES.includes(input.itemType)) {
    throw badRequest(`itemType must be one of ${PLAN_ITEM_TYPES.join(', ')} — checking and approving load capacity like any other work (I-9)`)
  }
  if (!PLAN_HORIZONS.includes(input.horizon)) throw badRequest(`horizon must be one of ${PLAN_HORIZONS.join(', ')}`)
  const week = input.week ?? null
  requireWeekForHorizon(input.horizon, week)
  const hours = input.plannedHours ?? 0
  if (typeof hours !== 'number' || Number.isNaN(hours) || hours < 0) throw badRequest('plannedHours must be a number ≥ 0')

  // The underlying record must exist in this project; it also gives the named owner
  // (PEC-PLAN-001: "Now" items carry a named owner) and the default discipline.
  const responsibleId = responsibleFor(sx, input.itemType, input.itemId)
  if (input.horizon === 'now' && responsibleId == null) {
    throw badRequest("'now' items carry a named owner (PEC-PLAN-001) — assign the underlying record first")
  }
  const existing = sx.db.prepare(
    'SELECT id FROM plan_item WHERE project_id = ? AND item_type = ? AND item_id = ?',
  ).get(sx.projectId, input.itemType, input.itemId) as { id: number } | undefined
  if (existing) throw badRequest('record is already on the plan — move it with a plan shift (PEC-PLAN-006) or edit its hours')

  const ref = sx.repo.nextRef(sx.projectId, 'plan_item')
  const id = sx.repo.insert('plan_item', {
    projectId: sx.projectId, ref, itemType: input.itemType, itemId: input.itemId,
    horizon: input.horizon, week, discipline: input.discipline ?? personDiscipline(sx, responsibleId),
    plannedHours: hours, createdBy: sx.session.personId, createdAt: nowIso(),
  })
  planItemHistory(sx, id, 'created',
    `${ref} planned ${input.itemType}#${input.itemId} → ${input.horizon}${week ? ` (${week})` : ''}, ${hours} h`)
  return sx.repo.get<PlanItem>('plan_item', sx.projectId, id)
}

export interface UpdatePlanItemInput {
  version: number
  plannedHours?: number
  discipline?: string | null
}

/** Hours/discipline edits only — placement changes go through the shift workflow (PEC-PLAN-006). */
export function updatePlanItem(sx: Sx, id: number, input: UpdatePlanItemInput): PlanItem {
  requireCan(sx, 'plan.manage')
  const pi = sx.repo.get<PlanItem>('plan_item', sx.projectId, id)
  const patch: Record<string, unknown> = {}
  if (input.plannedHours !== undefined) {
    if (typeof input.plannedHours !== 'number' || Number.isNaN(input.plannedHours) || input.plannedHours < 0) {
      throw badRequest('plannedHours must be a number ≥ 0')
    }
    patch.plannedHours = input.plannedHours
  }
  if (input.discipline !== undefined) patch.discipline = input.discipline
  if (Object.keys(patch).length === 0) {
    throw badRequest('nothing to update — plannedHours and discipline are the editable fields; placement changes go through a shift (PEC-PLAN-006)')
  }
  sx.repo.update('plan_item', sx.projectId, id, input.version, patch)
  planItemHistory(sx, id, 'field_change', `${pi.ref} updated (${Object.keys(patch).join(', ')})`)
  return sx.repo.get<PlanItem>('plan_item', sx.projectId, id)
}

// ---------- plan shifts (PEC-PLAN-005/006/008) ----------

const SHIFT_LINK_TYPES: RecordType[] = ['condition', 'hold', 'risk', 'schedule_activity', 'interface_item']

/** Best-effort package attribution of a linked record, for the cross-package test. */
function packageOfRecord(sx: Sx, snap: ProjectSnapshot, recordType: RecordType, recordId: number): number[] {
  switch (recordType) {
    case 'risk': {
      const r = snap.risks.find((x) => x.id === recordId)
      if (!r) return []
      if (r.packageId != null) return [r.packageId]
      const d = snap.deliverables.find((x) => x.id === r.deliverableId)
      return d?.packageId != null ? [d.packageId] : []
    }
    case 'interface_item': {
      const i = snap.interfaces.find((x) => x.id === recordId)
      return i ? [i.givingPackageId, i.receivingPackageId].filter((x): x is number => x != null) : []
    }
    case 'schedule_activity': {
      const a = snap.scheduleActivities.find((x) => x.id === recordId)
      if (!a) return []
      if (a.packageId != null) return [a.packageId]
      const d = snap.deliverables.find((x) => x.id === a.deliverableId)
      return d?.packageId != null ? [d.packageId] : []
    }
    case 'hold': {
      const pkgs = new Set<number>()
      for (const l of snap.holdLinks.filter((x) => x.holdId === recordId)) {
        if (l.targetType === 'deliverable') {
          const d = snap.deliverables.find((x) => x.id === l.targetId)
          if (d?.packageId != null) pkgs.add(d.packageId)
        } else if (l.targetType === 'revision') {
          const rev = snap.revisions.find((x) => x.id === l.targetId)
          const d = rev ? snap.deliverables.find((x) => x.id === rev.deliverableId) : undefined
          if (d?.packageId != null) pkgs.add(d.packageId)
        } else if (l.targetType === 'work_item') {
          const w = snap.workItems.find((x) => x.id === l.targetId)
          if (w?.packageId != null) pkgs.add(w.packageId)
        }
      }
      return [...pkgs]
    }
    case 'condition': {
      const c = snap.conditions.find((x) => x.id === recordId)
      if (!c) return []
      if (c.parentType === 'revision') {
        const rev = snap.revisions.find((x) => x.id === c.parentId)
        const d = rev ? snap.deliverables.find((x) => x.id === rev.deliverableId) : undefined
        return d?.packageId != null ? [d.packageId] : []
      }
      if (c.parentType === 'work_item') {
        const w = snap.workItems.find((x) => x.id === c.parentId)
        return w?.packageId != null ? [w.packageId] : []
      }
      return []
    }
    default:
      return []
  }
}

export interface ShiftPlanItemInput {
  version: number
  toHorizon: PlanHorizon
  toWeek?: string | null
  reason: string
  impactStatement?: string
  links?: Array<{ recordType: RecordType; recordId: number }>
}

export function shiftPlanItem(sx: Sx, id: number, input: ShiftPlanItemInput): PlanShift {
  requireCan(sx, 'plan.propose')
  const pi = sx.repo.get<PlanItem>('plan_item', sx.projectId, id)
  if (!input.reason) throw badRequest('every plan shift records its reason (PEC-PLAN-006)')
  if (!PLAN_HORIZONS.includes(input.toHorizon)) throw badRequest(`horizon must be one of ${PLAN_HORIZONS.join(', ')}`)
  const toWeek = input.toWeek ?? null
  requireWeekForHorizon(input.toHorizon, toWeek)
  if (pi.horizon === input.toHorizon && (pi.week ?? null) === toWeek) {
    throw badRequest('shift changes nothing — same horizon and week')
  }
  for (const l of input.links ?? []) {
    if (!SHIFT_LINK_TYPES.includes(l.recordType)) {
      throw badRequest(`shift links cover conditions, holds, risks, interfaces, and schedule activities (PEC-PLAN-008); got ${l.recordType}`)
    }
    const table = TABLE[l.recordType]
    if (!table || !sx.repo.maybeGet(table, sx.projectId, l.recordId)) throw notFound(`${l.recordType}#${l.recordId}`)
  }

  const snap = snapshot(sx)
  const ownPkg = resolvePlanItem(snap, pi)?.packageId ?? null
  // affectedPackageIds holds the FOREIGN packages the shift reaches into — they are whose
  // leads must review (PEC-PLAN-005); the origin package never reviews its own shift.
  const affected = new Set<number>()
  for (const l of input.links ?? []) {
    for (const p of packageOfRecord(sx, snap, l.recordType, l.recordId)) {
      if (p !== ownPkg) affected.add(p)
    }
  }
  const crossPackage = affected.size > 0
  if (crossPackage && !input.impactStatement) {
    throw badRequest('cross-package shifts carry an impact statement (milestones, capacity, affected deliverables) and are reviewed by the affected leads (PEC-PLAN-005)')
  }
  // the proposed path applies nothing yet, but a stale read must still be rejected up front
  // (PEC-NFR-004) rather than surfacing later at review time
  if (input.version !== pi.version) {
    throw badRequest(`stale plan item: expected version ${pi.version}, got ${input.version} (PEC-NFR-004) — reload and retry`)
  }

  const ref = sx.repo.nextRef(sx.projectId, 'plan_shift')
  const shiftId = sx.repo.insert('plan_shift', {
    projectId: sx.projectId, ref, planItemId: pi.id,
    fromHorizon: pi.horizon, toHorizon: input.toHorizon,
    fromWeek: pi.week, toWeek,
    reason: input.reason, impactStatement: input.impactStatement ?? null,
    crossPackage, affectedPackageIds: [...affected],
    state: crossPackage ? 'proposed' : 'applied',
    createdBy: sx.session.personId, createdAt: nowIso(),
  })
  for (const l of input.links ?? []) {
    sx.repo.insert('plan_shift_link', { planShiftId: shiftId, recordType: l.recordType, recordId: l.recordId })
  }
  sx.repo.history({
    projectId: sx.projectId, recordType: 'plan_shift', recordId: shiftId,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref}: ${pi.ref} ${pi.horizon}${pi.week ? `/${pi.week}` : ''} → ${input.toHorizon}${toWeek ? `/${toWeek}` : ''} — ${input.reason}`,
    payload: { crossPackage, affectedPackageIds: [...affected] }, authorityRef: null,
  })

  if (crossPackage) {
    // review required before the move applies (PEC-PLAN-005)
    const leads = snap.packages.filter((p) => affected.has(p.id) && p.leadId != null)
    for (const p of leads) {
      sx.repo.notify({
        projectId: sx.projectId, personId: p.leadId!, event: 'plan_shift_review',
        recordType: 'plan_shift', recordId: shiftId, recordRef: ref,
        reason: `plan shift crossing into ${p.code} needs your review: ${input.reason}`,
        nextAction: 'review the proposed shift on the Plan page', due: null,
      })
    }
  } else {
    sx.repo.update('plan_item', sx.projectId, pi.id, input.version, { horizon: input.toHorizon, week: toWeek })
    planItemHistory(sx, pi.id, 'transition',
      `${pi.ref} moved to ${input.toHorizon}${toWeek ? ` (${toWeek})` : ''} — ${input.reason}`)
  }
  return sx.repo.get<PlanShift>('plan_shift', sx.projectId, shiftId)
}

export interface ReviewPlanShiftInput {
  version: number
  approve: boolean
  note?: string
}

export function reviewPlanShift(sx: Sx, id: number, input: ReviewPlanShiftInput): PlanShift {
  requireCan(sx, 'plan.review')
  const shift = sx.repo.get<PlanShift>('plan_shift', sx.projectId, id)
  if (shift.state !== 'proposed') throw badRequest(`only proposed shifts are reviewable; ${shift.ref} is ${shift.state}`)
  // A lead must lead one of the AFFECTED (foreign) packages — the origin package's lead,
  // including the proposer, cannot self-approve (PEC-PLAN-005); pm/EM/admin review any.
  const seniorReviewer = sx.session.isAdmin
    || sx.roles.some((r) => r === 'pm' || r === 'engineering_manager' || r === 'admin')
  if (!seniorReviewer) {
    const leadsAffected = shift.affectedPackageIds.length === 0 ? { n: 0 } : sx.db.prepare(
      `SELECT COUNT(*) AS n FROM package WHERE project_id = ? AND lead_id = ? AND id IN (${shift.affectedPackageIds.map(() => '?').join(',')})`,
    ).get(sx.projectId, sx.session.personId, ...shift.affectedPackageIds) as { n: number }
    if (leadsAffected.n === 0) throw forbidden('plan.review: you do not lead an affected package (PEC-PLAN-005)')
    if (shift.createdBy === sx.session.personId) {
      throw forbidden('plan.review: the proposer does not review their own shift (PEC-PLAN-005)')
    }
  }

  if (input.approve) {
    const pi = sx.repo.get<PlanItem>('plan_item', sx.projectId, shift.planItemId)
    // the proposal captured the placement it moves FROM; if the plan item has moved since
    // (another shift applied), this review is stale and must not blind-apply (PEC-NFR-004)
    if (pi.horizon !== shift.fromHorizon || (pi.week ?? null) !== (shift.fromWeek ?? null)) {
      throw badRequest(`${shift.ref} is stale: ${pi.ref} has moved since the proposal (now ${pi.horizon}${pi.week ? `/${pi.week}` : ''}) — re-propose the shift`)
    }
    sx.repo.systemUpdate('plan_item', sx.projectId, pi.id, { horizon: shift.toHorizon, week: shift.toWeek })
    planItemHistory(sx, pi.id, 'transition',
      `${pi.ref} moved to ${shift.toHorizon}${shift.toWeek ? ` (${shift.toWeek})` : ''} — ${shift.ref} approved by review`)
  }
  sx.repo.update('plan_shift', sx.projectId, id, input.version, {
    state: input.approve ? 'applied' : 'rejected',
    reviewedBy: sx.session.personId, reviewedAt: nowIso(),
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'plan_shift', recordId: id,
    actorId: sx.session.personId, kind: 'transition',
    summary: `${shift.ref} ${input.approve ? 'approved' : 'rejected'} by review${input.note ? ` — ${input.note}` : ''}`,
    payload: null, authorityRef: null,
  })
  sx.repo.notify({
    projectId: sx.projectId, personId: shift.createdBy, event: 'plan_shift_review',
    recordType: 'plan_shift', recordId: id, recordRef: shift.ref,
    reason: `your plan shift was ${input.approve ? 'approved' : 'rejected'}${input.note ? `: ${input.note}` : ''}`,
    nextAction: input.approve ? 'no action needed' : 'revise and re-propose if still required', due: null,
  })
  return sx.repo.get<PlanShift>('plan_shift', sx.projectId, id)
}

// ---------- weekly commit (PEC-PLAN-007, PEC-MW-007) ----------

export interface CommitWeekResult {
  week: string
  period: PlanPeriod
  committedWorkItems: number
  notified: number
}

export function commitWeek(sx: Sx, week: string): CommitWeekResult {
  requireCan(sx, 'plan.commit')
  if (!isValidIsoWeek(week)) throw badRequest('week must be an ISO week (YYYY-Www)')

  let period = sx.db.prepare('SELECT * FROM plan_period WHERE project_id = ? AND week = ?')
    .get(sx.projectId, week) as { id: number } | undefined
  if (!period) {
    const pid = sx.repo.insert('plan_period', {
      projectId: sx.projectId, week, state: 'committed',
      committedAt: nowIso(), committedBy: sx.session.personId,
    })
    period = { id: pid }
  } else {
    sx.repo.systemUpdate('plan_period', sx.projectId, period.id, {
      state: 'committed', committedAt: nowIso(), committedBy: sx.session.personId,
    })
  }

  const planItems = sx.repo.list<PlanItem>('plan_item', sx.projectId, 'week = ?', [week])
  let committed = 0
  let notified = 0
  const alreadyNotified = (personId: number, recordType: string, recordId: number): boolean => {
    const row = sx.db.prepare(
      `SELECT COUNT(*) AS n FROM notification
       WHERE project_id = ? AND person_id = ? AND event = 'week_committed'
         AND record_type = ? AND record_id = ? AND reason LIKE ?`,
    ).get(sx.projectId, personId, recordType, recordId, `%${week}%`) as { n: number }
    return row.n > 0
  }
  for (const pi of planItems) {
    if (pi.itemType === 'work_item') {
      const w = sx.repo.maybeGet<WorkItem>('work_item', sx.projectId, pi.itemId)
      if (!w || (w.state !== 'open' && w.state !== 'in_work')) continue
      if (w.committedWeek !== week || w.commitSource !== 'plan') {
        sx.repo.systemUpdate('work_item', sx.projectId, w.id, { committedWeek: week, commitSource: 'plan' })
        sx.repo.history({
          projectId: sx.projectId, recordType: 'work_item', recordId: w.id,
          actorId: sx.session.personId, kind: 'plan_commit',
          summary: `${w.ref} committed to ${week} by the weekly planning commit (PEC-PLAN-007)`,
          payload: null, authorityRef: null,
        })
        committed++
      }
      if (!alreadyNotified(w.ownerId, 'work_item', w.id)) {
        sx.repo.notify({
          projectId: sx.projectId, personId: w.ownerId, event: 'week_committed',
          recordType: 'work_item', recordId: w.id, recordRef: w.ref,
          reason: `committed to your week ${week} by the weekly planning commit`,
          nextAction: 'see My Week', due: w.needBy ?? null,
        })
        notified++
      }
    } else {
      const responsible = responsibleFor(sx, pi.itemType, pi.itemId)
      if (responsible == null) continue
      const table = pi.itemType === 'check' ? 'check_record' : 'approval_record'
      const rec = sx.repo.maybeGet<{ ref: string }>(table, sx.projectId, pi.itemId)
      if (!rec) continue
      if (!alreadyNotified(responsible, pi.itemType, pi.itemId)) {
        sx.repo.notify({
          projectId: sx.projectId, personId: responsible, event: 'week_committed',
          recordType: pi.itemType, recordId: pi.itemId, recordRef: rec.ref,
          reason: `${pi.itemType === 'check' ? 'checking' : 'approval'} booked into week ${week} (${pi.plannedHours} h — I-9)`,
          // checks project into My Week (checks owed); approvals surface in the approval
          // register and in Waiting-on-you once ready — point people where the record lives
          nextAction: pi.itemType === 'check' ? 'see My Week (checks you owe)' : 'see the approval register / Waiting on you',
          due: null,
        })
        notified++
      }
    }
  }
  const fresh = sx.repo.get<PlanPeriod>('plan_period', sx.projectId, period.id)
  return { week, period: fresh, committedWorkItems: committed, notified }
}

// ---------- capacity (PEC-PLAN-003) ----------

export interface UpsertCapacityInput {
  week: string
  discipline: string
  hours: number
}

export function upsertCapacity(sx: Sx, input: UpsertCapacityInput): CapacityEntry {
  requireCan(sx, 'plan.manage')
  if (!isValidIsoWeek(input.week)) throw badRequest('week must be an ISO week (YYYY-Www)')
  if (!input.discipline) throw badRequest('discipline is required (capacity is by discipline, PEC-PLAN-003)')
  if (typeof input.hours !== 'number' || Number.isNaN(input.hours) || input.hours < 0) {
    throw badRequest('hours must be a number ≥ 0')
  }
  const existing = sx.db.prepare(
    'SELECT id, hours FROM capacity_entry WHERE project_id = ? AND week = ? AND discipline = ?',
  ).get(sx.projectId, input.week, input.discipline) as { id: number; hours: number } | undefined
  let id: number
  if (existing) {
    sx.repo.systemUpdate('capacity_entry', sx.projectId, existing.id, { hours: input.hours })
    id = existing.id
  } else {
    id = sx.repo.insert('capacity_entry', {
      projectId: sx.projectId, week: input.week, discipline: input.discipline, hours: input.hours,
    })
  }
  // capacity drives the §8.3/§8.4 rules; changes leave an audit trail like config does
  sx.repo.audit({
    projectId: sx.projectId, actorId: sx.session.personId, action: 'capacity_change',
    recordType: 'project', recordId: sx.projectId,
    priorValue: existing ? { week: input.week, discipline: input.discipline, hours: existing.hours } : null,
    newValue: { week: input.week, discipline: input.discipline, hours: input.hours },
  })
  return sx.repo.get<CapacityEntry>('capacity_entry', sx.projectId, id)
}

// ---------- the Plan view (PEC-PLAN-001/002/003/006) ----------

export function planView(sx: Sx, weeksCount = 6): unknown {
  const snap = snapshot(sx)
  const weeks = isoWeeksFrom(snap.today, weeksCount)
  const currentWeek = isoWeekOf(snap.today)
  const horizons = planHorizons(snap)
  const pkgCode = (id: number | null): string | null =>
    snap.packages.find((p) => p.id === id)?.code ?? null

  // Log visibility (PEC-NFR-005): derived numbers stay on the unfiltered snapshot, but
  // title-bearing rows follow the register rule — work-item titles outside the caller's
  // visible logs are redacted to ref-only (checks/approvals carry no log).
  const logs = visibleLogs(sx.roles, snap.project.config.logVisibility)
  const seesAll = logs.length === 3
  const wiById = seesAll ? null : new Map(snap.workItems.map((w) => [w.id, w]))
  const wiRestricted = (itemType: string, itemId: number): boolean => {
    if (seesAll || itemType !== 'work_item') return false
    const w = wiById!.get(itemId)
    return w != null && !logs.includes(w.log)
  }

  const serialize = (vs: ReturnType<typeof planHorizons>['now']) => vs.map((v) => {
    const restricted = wiRestricted(v.planItem.itemType, v.planItem.itemId)
    return {
      id: v.planItem.id, ref: v.planItem.ref, itemType: v.planItem.itemType, itemId: v.planItem.itemId,
      version: v.planItem.version, horizon: v.planItem.horizon, week: v.planItem.week,
      discipline: v.planItem.discipline, plannedHours: v.planItem.plannedHours,
      itemRef: v.itemRef, title: restricted ? '[restricted log]' : v.title,
      responsibleId: v.responsibleId, needBy: v.needBy,
      deliverableDocNo: v.deliverable?.docNo ?? null, packageCode: pkgCode(v.packageId), open: v.open,
    }
  })

  const shifts = [...snap.planShifts]
    .sort((a, b) => b.id - a.id)
    .slice(0, 50)
    .map((s) => {
      const pi = snap.planItems.find((x) => x.id === s.planItemId)
      const v = pi ? resolvePlanItem(snap, pi) : null
      const restricted = pi != null && wiRestricted(pi.itemType, pi.itemId)
      return {
        id: s.id, ref: s.ref, version: s.version, state: s.state,
        planItemRef: pi?.ref ?? null, itemRef: v?.itemRef ?? null,
        title: restricted ? '[restricted log]' : v?.title ?? null,
        fromHorizon: s.fromHorizon, toHorizon: s.toHorizon, fromWeek: s.fromWeek, toWeek: s.toWeek,
        reason: s.reason, impactStatement: s.impactStatement,
        crossPackage: s.crossPackage,
        affectedPackages: s.affectedPackageIds.map((p) => pkgCode(p)).filter(Boolean),
        createdBy: s.createdBy, createdAt: s.createdAt,
        reviewedBy: s.reviewedBy, reviewedAt: s.reviewedAt,
      }
    })

  // records that could be placed on the plan but aren't yet (work / check / approve — I-9)
  const plannedKeys = new Set(snap.planItems.map((pi) => `${pi.itemType}:${pi.itemId}`))
  const docOfRev = (revisionId: number): string | null => {
    const rev = snap.revisions.find((r) => r.id === revisionId)
    return rev ? snap.deliverables.find((d) => d.id === rev.deliverableId)?.docNo ?? null : null
  }
  const plannable = [
    ...snap.workItems
      .filter((w) => (w.state === 'open' || w.state === 'in_work') && !plannedKeys.has(`work_item:${w.id}`))
      .filter((w) => seesAll || logs.includes(w.log))
      .map((w) => ({ itemType: 'work_item' as const, itemId: w.id, ref: w.ref, label: `${w.ref} — ${w.title}` })),
    ...snap.checks
      .filter((c) => c.state !== 'accepted' && c.state !== 'reopened' && !plannedKeys.has(`check:${c.id}`))
      .map((c) => ({ itemType: 'check' as const, itemId: c.id, ref: c.ref, label: `${c.ref} — check ${docOfRev(c.revisionId) ?? ''}` })),
    ...snap.approvalRecords
      .filter((a) => (a.state === 'required' || a.state === 'prereqs_incomplete' || a.state === 'ready') && !plannedKeys.has(`approval_record:${a.id}`))
      .map((a) => ({ itemType: 'approval_record' as const, itemId: a.id, ref: a.ref, label: `${a.ref} — ${a.title}` })),
  ]

  return {
    currentWeek,
    weeks,
    plannable,
    periods: snap.planPeriods
      .filter((p) => weeks.includes(p.week))
      .map((p) => ({ id: p.id, week: p.week, state: p.state, committedAt: p.committedAt, committedBy: p.committedBy, version: p.version })),
    horizons: {
      now: serialize(horizons.now), next: serialize(horizons.next), later: serialize(horizons.later),
    },
    lookahead: lookahead(snap, weeks).map((r) => ({
      deliverableId: r.deliverable.id, docNo: r.deliverable.docNo, title: r.deliverable.title,
      packageCode: pkgCode(r.deliverable.packageId), dueDate: r.deliverable.dueDate,
      cells: r.cells,
    })),
    capacity: capacityView(snap, weeks),
    shifts,
    scheduleActivityCount: snap.scheduleActivities.length,
  }
}
