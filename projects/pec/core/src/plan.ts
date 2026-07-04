/**
 * P2 planning & capacity derivations (PRD §12.4, I-9, ADR-013).
 * Pure functions over a ProjectSnapshot, like status.ts: computed on read, never persisted,
 * explainable. Capacity loads come from plan items — work, checks, and approvals alike
 * (I-9: checking and approving consume capacity like any other work).
 */

import type { Deliverable, PlanItem, ProjectSnapshot } from './types.ts'
import { isoWeekMonday, isoWeekOf, isoWeekSunday, isoWeeksFrom } from './calendar.ts'
import { activeHoldsInSphere, currentRevision } from './status.ts'

// ---------- resolving a plan item's underlying record ----------

export interface PlanItemView {
  planItem: PlanItem
  /** the planned record, resolved */
  itemRef: string
  title: string
  /** the person whose week this loads (owner / checker / first signatory) */
  responsibleId: number | null
  needBy: string | null
  deliverable: Deliverable | null
  packageId: number | null
  /** underlying record still needs doing — closed/accepted/decided records stop loading capacity */
  open: boolean
}

function deliverableOfRevision(snap: ProjectSnapshot, revisionId: number): Deliverable | null {
  const rev = snap.revisions.find((r) => r.id === revisionId)
  return rev ? snap.deliverables.find((d) => d.id === rev.deliverableId) ?? null : null
}

export function resolvePlanItem(snap: ProjectSnapshot, pi: PlanItem): PlanItemView | null {
  if (pi.itemType === 'work_item') {
    const w = snap.workItems.find((x) => x.id === pi.itemId)
    if (!w) return null
    const del = w.anchorType === 'deliverable'
      ? snap.deliverables.find((d) => d.id === w.anchorId) ?? null
      : w.anchorType === 'revision' ? deliverableOfRevision(snap, w.anchorId) : null
    return {
      planItem: pi, itemRef: w.ref, title: w.title, responsibleId: w.ownerId,
      needBy: w.needBy, deliverable: del, packageId: w.packageId,
      open: w.state === 'open' || w.state === 'in_work',
    }
  }
  if (pi.itemType === 'check') {
    const c = snap.checks.find((x) => x.id === pi.itemId)
    if (!c) return null
    const del = deliverableOfRevision(snap, c.revisionId)
    return {
      planItem: pi, itemRef: c.ref, title: del ? `check ${del.docNo}` : `check #${c.revisionId}`,
      responsibleId: c.checkerId, needBy: del?.dueDate ?? null,
      deliverable: del, packageId: del?.packageId ?? null,
      open: c.state !== 'accepted',
    }
  }
  const a = snap.approvalRecords.find((x) => x.id === pi.itemId)
  if (!a) return null
  const del = a.appliesToType === 'revision' ? deliverableOfRevision(snap, a.appliesToId)
    : a.appliesToType === 'deliverable' ? snap.deliverables.find((d) => d.id === a.appliesToId) ?? null
    : null
  return {
    planItem: pi, itemRef: a.ref, title: a.title,
    responsibleId: a.signatoryIds[0] ?? null, needBy: a.dueDate,
    deliverable: del,
    packageId: del?.packageId ?? (a.appliesToType === 'package' ? a.appliesToId : null),
    open: a.state !== 'decided' && a.state !== 'superseded',
  }
}

// ---------- Now / Next / Later (PEC-PLAN-001) ----------

export interface PlanHorizons {
  now: PlanItemView[]
  next: PlanItemView[]
  later: PlanItemView[]
}

export function planHorizons(snap: ProjectSnapshot): PlanHorizons {
  const out: PlanHorizons = { now: [], next: [], later: [] }
  for (const pi of snap.planItems) {
    const v = resolvePlanItem(snap, pi)
    if (v) out[pi.horizon].push(v)
  }
  const byWeekThenNeedBy = (a: PlanItemView, b: PlanItemView): number =>
    (a.planItem.week ?? '9999').localeCompare(b.planItem.week ?? '9999')
    || (a.needBy ?? '9999').localeCompare(b.needBy ?? '9999')
  out.now.sort(byWeekThenNeedBy); out.next.sort(byWeekThenNeedBy); out.later.sort(byWeekThenNeedBy)
  return out
}

// ---------- capacity by discipline per week (PEC-PLAN-003, I-9) ----------

export type CapacityLevel = 'none' | 'warn' | 'red'

export interface CapacityCell {
  week: string
  discipline: string
  capacityH: number | null
  loadH: number
  /** load as % of capacity; null without a capacity baseline */
  pct: number | null
  level: CapacityLevel
  /** hours split by what loads them (I-9 visibility: checking/approving are visible load) */
  byType: { work_item: number; check: number; approval_record: number }
  /** the plan items loading this cell */
  planItemIds: number[]
}

/** Load vs capacity per (week, discipline). Only open underlying records load capacity. */
export function capacityView(snap: ProjectSnapshot, weeks: string[]): CapacityCell[] {
  const th = snap.project.thresholds
  const cells = new Map<string, CapacityCell>()
  const cell = (week: string, discipline: string): CapacityCell => {
    const key = `${week}|${discipline}`
    let c = cells.get(key)
    if (!c) {
      c = {
        week, discipline, capacityH: null, loadH: 0, pct: null, level: 'none',
        byType: { work_item: 0, check: 0, approval_record: 0 }, planItemIds: [],
      }
      cells.set(key, c)
    }
    return c
  }
  const wanted = new Set(weeks)
  for (const ce of snap.capacityEntries) {
    if (!wanted.has(ce.week)) continue
    const c = cell(ce.week, ce.discipline)
    c.capacityH = (c.capacityH ?? 0) + ce.hours
  }
  for (const pi of snap.planItems) {
    if (!pi.week || !wanted.has(pi.week) || pi.plannedHours <= 0) continue
    const v = resolvePlanItem(snap, pi)
    if (!v || !v.open) continue
    const c = cell(pi.week, pi.discipline ?? 'unassigned')
    c.loadH += pi.plannedHours
    c.byType[pi.itemType] += pi.plannedHours
    c.planItemIds.push(pi.id)
  }
  for (const c of cells.values()) {
    if (c.capacityH != null && c.capacityH > 0) {
      c.pct = Math.round((c.loadH / c.capacityH) * 100)
      c.level = c.pct > th.capacityRedPct ? 'red' : c.pct > th.capacityWarnPct ? 'warn' : 'none'
    }
  }
  return [...cells.values()].sort((a, b) =>
    a.week.localeCompare(b.week) || a.discipline.localeCompare(b.discipline))
}

/** Overloaded (week, discipline) cells for the current week — feeds S-CAP and PH-R3/PH-A3 (§8.3/§8.4 P2). */
export function capacityBreaches(snap: ProjectSnapshot): CapacityCell[] {
  return capacityView(snap, [isoWeekOf(snap.today)]).filter((c) => c.level !== 'none')
}

// ---------- six-week lookahead (PEC-PLAN-002) ----------

export type LookaheadState = 'hold' | 'issue' | 'approve' | 'check' | 'work'

export interface LookaheadCell {
  week: string
  state: LookaheadState
  detail: string
}

export interface LookaheadRow {
  deliverable: Deliverable
  cells: Array<LookaheadCell | null>
}

/**
 * Rows are deliverables, cells the derived weekly state — Hold-by-cause > Issue > Approve >
 * Check > Work — sourced from the plan and the schedule import (PEC-PLAN-002). A hold shows
 * on the current week (holds have no week of their own); Issue is the week the due date
 * falls in; Work also derives from imported schedule activities overlapping the week.
 */
export function lookahead(snap: ProjectSnapshot, weeks?: string[]): LookaheadRow[] {
  const wks = weeks ?? isoWeeksFrom(snap.today, 6)
  const currentWeek = isoWeekOf(snap.today)

  // plan items by deliverable id, resolved once
  const planByDel = new Map<number, PlanItemView[]>()
  for (const pi of snap.planItems) {
    if (!pi.week) continue
    const v = resolvePlanItem(snap, pi)
    if (!v || !v.open || !v.deliverable) continue
    const list = planByDel.get(v.deliverable.id) ?? []
    list.push(v)
    planByDel.set(v.deliverable.id, list)
  }
  const actsByDel = new Map<number, typeof snap.scheduleActivities>()
  for (const a of snap.scheduleActivities) {
    if (a.deliverableId == null) continue
    const list = actsByDel.get(a.deliverableId) ?? []
    list.push(a)
    actsByDel.set(a.deliverableId, list)
  }

  const stateOf = (d: Deliverable, week: string): LookaheadCell | null => {
    if (week === currentWeek) {
      const holds = activeHoldsInSphere(snap, d, currentRevision(snap, d.id))
      if (holds.length > 0) {
        return { week, state: 'hold', detail: holds.map((h) => `${h.ref} (${h.cause})`).join(', ') }
      }
    }
    if (d.dueDate && isoWeekOf(d.dueDate) === week) {
      return { week, state: 'issue', detail: `due ${d.dueDate}` }
    }
    const plans = (planByDel.get(d.id) ?? []).filter((v) => v.planItem.week === week)
    const approve = plans.find((v) => v.planItem.itemType === 'approval_record')
    if (approve) return { week, state: 'approve', detail: approve.itemRef }
    const check = plans.find((v) => v.planItem.itemType === 'check')
    if (check) return { week, state: 'check', detail: check.itemRef }
    const work = plans.filter((v) => v.planItem.itemType === 'work_item')
    if (work.length > 0) return { week, state: 'work', detail: work.map((v) => v.itemRef).join(', ') }
    const monday = isoWeekMonday(week)
    const sunday = isoWeekSunday(week)
    const acts = (actsByDel.get(d.id) ?? []).filter((a) => a.startDate <= sunday && a.finishDate >= monday)
    if (acts.length > 0) return { week, state: 'work', detail: acts.map((a) => a.activityId).join(', ') }
    return null
  }

  const rows = snap.deliverables.map((d) => ({
    deliverable: d,
    cells: wks.map((w) => stateOf(d, w)),
  }))
  // deliverables with near-term content first, then by due date
  return rows.sort((a, b) => {
    const an = a.cells.some((c) => c != null) ? 0 : 1
    const bn = b.cells.some((c) => c != null) ? 0 : 1
    return an - bn || (a.deliverable.dueDate ?? '9999').localeCompare(b.deliverable.dueDate ?? '9999')
  })
}

// ---------- plan-sourced forecast candidates (SPEC §6.1: P2 replaces need-by-only forecast) ----------

/**
 * Latest planned completion date for a deliverable's sphere: the Sunday of the latest planned
 * week among its open plan items, and the latest finish of schedule activities mapped to it.
 * Feeds deliverableStatus() forecast alongside the P1 need-by candidates.
 */
export function planForecastCandidates(snap: ProjectSnapshot, d: Deliverable): string[] {
  const out: string[] = []
  for (const pi of snap.planItems) {
    if (!pi.week) continue
    const v = resolvePlanItem(snap, pi)
    if (v && v.open && v.deliverable?.id === d.id) out.push(isoWeekSunday(pi.week))
  }
  for (const a of snap.scheduleActivities) {
    if (a.deliverableId === d.id && a.finishDate) out.push(a.finishDate)
  }
  return out
}

// ---------- helpers shared with the server layer ----------

export function planItemPackageId(snap: ProjectSnapshot, pi: PlanItem): number | null {
  return resolvePlanItem(snap, pi)?.packageId ?? null
}
