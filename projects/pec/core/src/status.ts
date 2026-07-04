/**
 * Derived status (PRD §8, SPEC §6). Pure functions over a ProjectSnapshot.
 * Every value is an Explain<...>: rule id + threshold + contributing records (I-4, ADR-004).
 * Nothing here is ever persisted.
 */

import type {
  ContributingRef, Deliverable, Explain, Health, Hold, Package, ProjectSnapshot,
  Revision, Thresholds, WorkItem,
} from './types.ts'
import {
  ageWorkingDays, calendarDaysBetween, daysOverdue, isValidLocalDate, isoWeekOf, localDate,
  workingDaysBetween, workingDaysOverdue,
} from './calendar.ts'
import { activeHoldsFor, evaluateCondition } from './conditions.ts'
import { commentIsOpen } from './types.ts'

const HEALTH_RANK: Record<Health, number> = { green: 0, amber: 1, red: 2 }

function worse(a: Health, b: Health): Health {
  return HEALTH_RANK[a] >= HEALTH_RANK[b] ? a : b
}

// ---------- deliverable sphere ----------

/** Latest non-superseded revision; falls back to the latest revision when all are superseded. */
export function currentRevision(snap: ProjectSnapshot, deliverableId: number): Revision | null {
  const revs = snap.revisions
    .filter((r) => r.deliverableId === deliverableId)
    .sort((a, b) => a.id - b.id)
  if (revs.length === 0) return null
  const live = revs.filter((r) => r.state !== 'superseded')
  return (live.length > 0 ? live[live.length - 1] : revs[revs.length - 1]) ?? null
}

/**
 * Open work items in a deliverable's sphere: anchored directly to the deliverable, or to
 * ANY of its revisions (I-1 — a work item on a prior/superseded revision is still the
 * deliverable's open work and must count toward its health, not vanish). Rollups still use
 * the primary anchor to avoid double counting (§13.4).
 */
export function openWorkItemsFor(snap: ProjectSnapshot, d: Deliverable, _rev: Revision | null): WorkItem[] {
  const revIds = new Set(snap.revisions.filter((r) => r.deliverableId === d.id).map((r) => r.id))
  return snap.workItems.filter(
    (w) => (w.state === 'open' || w.state === 'in_work')
      && ((w.anchorType === 'deliverable' && w.anchorId === d.id)
        || (w.anchorType === 'revision' && revIds.has(w.anchorId))),
  )
}

/** Active holds in the deliverable's sphere: the deliverable, its current revision, open items, conditions and checks on it. */
export function activeHoldsInSphere(snap: ProjectSnapshot, d: Deliverable, rev: Revision | null): Hold[] {
  const holds = new Map<number, Hold>()
  const add = (hs: Hold[]) => { for (const h of hs) holds.set(h.id, h) }
  add(activeHoldsFor(snap, 'deliverable', d.id))
  if (rev) {
    add(activeHoldsFor(snap, 'revision', rev.id))
    for (const c of snap.conditions.filter((x) => x.parentType === 'revision' && x.parentId === rev.id)) {
      add(activeHoldsFor(snap, 'condition', c.id))
    }
    for (const c of snap.checks.filter((x) => x.revisionId === rev.id)) {
      add(activeHoldsFor(snap, 'check', c.id))
    }
  }
  for (const w of openWorkItemsFor(snap, d, rev)) add(activeHoldsFor(snap, 'work_item', w.id))
  return [...holds.values()]
}

export interface DeliverableStatus {
  deliverable: Deliverable
  revision: Revision | null
  health: Explain<Health>
  /** forecast slip in working days (SPEC §6.1 P1 forecast: need-by driven) */
  forecastSlipWd: number
  forecastDate: string | null
  openItemCount: number
  activeHoldCount: number
}

export function deliverableStatus(snap: ProjectSnapshot, d: Deliverable): DeliverableStatus {
  const cal = snap.project.calendar
  const th = snap.project.thresholds
  const today = snap.today
  const rev = currentRevision(snap, d.id)
  const items = openWorkItemsFor(snap, d, rev)
  const holds = activeHoldsInSphere(snap, d, rev)

  const revConditions = rev
    ? snap.conditions
      .filter((c) => c.parentType === 'revision' && c.parentId === rev.id)
      .map((c) => evaluateCondition(snap, c))
      .filter((e) => e.effectiveState === 'open' || e.effectiveState === 'blocked_by_hold')
    : []

  // --- forecast (P1: need-by driven; plan-sourced in P2) ---
  // Only well-formed dates participate; a malformed stored value is ignored, never thrown (I-4).
  let forecastDate = isValidLocalDate(d.dueDate) ? d.dueDate : null
  const candidates: string[] = []
  for (const w of items) if (isValidLocalDate(w.needBy)) candidates.push(w.needBy)
  for (const e of revConditions) if (e.condition.severity === 'hard' && isValidLocalDate(e.condition.needBy)) candidates.push(e.condition.needBy)
  for (const h of holds) if (isValidLocalDate(h.needBy)) candidates.push(h.needBy)
  for (const c of candidates) {
    if (!forecastDate || calendarDaysBetween(forecastDate, c) > 0) forecastDate = c
  }
  const dueValid = isValidLocalDate(d.dueDate)
  const slip = dueValid && forecastDate ? workingDaysBetween(d.dueDate!, forecastDate, cal) : 0

  const mk = (value: Health, ruleId: string, detail: string, threshold: string, contributing: ContributingRef[]): DeliverableStatus => ({
    deliverable: d, revision: rev, health: { value, ruleId, detail, threshold, contributing },
    forecastSlipWd: slip, forecastDate, openItemCount: items.length, activeHoldCount: holds.length,
  })

  // --- red rules ---
  if (slip > th.forecastSlipAmberWd) {
    return mk('red', 'DH-R1', `forecast slip ${slip} working days beyond due date`, `> ${th.forecastSlipAmberWd} wd`, [
      { recordType: 'deliverable', id: d.id, ref: d.docNo, why: `due ${d.dueDate}, forecast ${forecastDate}` },
    ])
  }
  const oldHolds = holds.filter((h) => ageWorkingDays(h.raisedAt, today, cal) > th.holdAgeRedWd)
  if (oldHolds.length > 0) {
    return mk('red', 'DH-R2', 'hold older than escalation threshold', `> ${th.holdAgeRedWd} wd`,
      oldHolds.map((h) => ({ recordType: 'hold', id: h.id, ref: h.ref, why: `${h.cause}, age ${ageWorkingDays(h.raisedAt, today, cal)} wd` })))
  }
  if (d.milestone) {
    const breached = revConditions.filter((e) => e.condition.severity === 'hard' && e.condition.needBy && daysOverdue(e.condition.needBy, today) > 0)
    if (breached.length > 0) {
      return mk('red', 'DH-R3', 'breached milestone-linked condition', 'need-by past on hard condition', breached.map((e) => ({
        recordType: 'condition', id: e.condition.id, ref: e.condition.ref, why: `need-by ${e.condition.needBy} past, milestone ${d.milestone}`,
      })))
    }
  }

  // --- amber rules ---
  if (holds.length > 0) {
    return mk('amber', 'DH-A1', 'active hold', 'any active hold',
      holds.map((h) => ({ recordType: 'hold', id: h.id, ref: h.ref, why: `${h.cause}, owner needs by ${h.needBy ?? '—'}` })))
  }
  const overdueItems: ContributingRef[] = []
  for (const w of items) {
    if (w.needBy && daysOverdue(w.needBy, today) > 0) {
      overdueItems.push({ recordType: 'work_item', id: w.id, ref: w.ref, why: `need-by ${w.needBy} past` })
    }
  }
  for (const e of revConditions) {
    if (e.condition.needBy && daysOverdue(e.condition.needBy, today) > 0) {
      overdueItems.push({ recordType: 'condition', id: e.condition.id, ref: e.condition.ref, why: `need-by ${e.condition.needBy} past` })
    }
  }
  if (overdueItems.length > 0) {
    return mk('amber', 'DH-A2', 'overdue open item or condition', 'need-by past', overdueItems)
  }
  if (slip > 0) {
    return mk('amber', 'DH-A3', `forecast slip ${slip} working days`, `1..${th.forecastSlipAmberWd} wd`, [
      { recordType: 'deliverable', id: d.id, ref: d.docNo, why: `due ${d.dueDate}, forecast ${forecastDate}` },
    ])
  }
  if (rev) {
    const agingComments = snap.reviewComments.filter((c) => {
      if (!commentIsOpen(c)) return false
      const onRev = c.revisionId === rev.id
        || snap.checks.some((x) => x.id === c.checkId && x.revisionId === rev.id)
      return onRev && ageWorkingDays(c.createdAt, today, cal) > th.commentAgeWarnWd
    })
    if (agingComments.length > 0) {
      return mk('amber', 'DH-A4', 'check comments aging past threshold', `> ${th.commentAgeWarnWd} wd`,
        agingComments.map((c) => ({ recordType: 'review_comment', id: c.id, ref: c.ref, why: `open ${ageWorkingDays(c.createdAt, today, cal)} wd` })))
    }
  }
  return mk('green', 'DH-G', 'on plan', 'no hold, no overdue, no slip', [])
}

// ---------- package health ----------

export interface PackageStatus {
  pkg: Package
  health: Explain<Health>
  deliverableStatuses: DeliverableStatus[]
  onPlanCount: number
  totalCount: number
}

export function packageStatus(snap: ProjectSnapshot, pkg: Package): PackageStatus {
  const th = snap.project.thresholds
  const cal = snap.project.calendar
  const today = snap.today
  const dels = snap.deliverables.filter((d) => d.packageId === pkg.id)
  const statuses = dels.map((d) => deliverableStatus(snap, d))
  const onPlan = statuses.filter((s) => s.health.value === 'green').length

  const mk = (value: Health, ruleId: string, detail: string, threshold: string, contributing: ContributingRef[]): PackageStatus => ({
    pkg, health: { value, ruleId, detail, threshold, contributing },
    deliverableStatuses: statuses, onPlanCount: onPlan, totalCount: dels.length,
  })

  // PH-R1: red deliverable linked to a package milestone
  const redMilestone = statuses.filter((s) => s.health.value === 'red' && s.deliverable.milestone)
  if (redMilestone.length > 0) {
    return mk('red', 'PH-R1', 'red deliverable linked to a package milestone', 'any', redMilestone.map((s) => ({
      recordType: 'deliverable', id: s.deliverable.id, ref: s.deliverable.docNo,
      why: `red (${s.health.ruleId}), milestone ${s.deliverable.milestone}`,
    })))
  }
  // PH-R2: interface overdue past escalation
  const lateInterfaces = snap.interfaces.filter((i) =>
    (i.givingPackageId === pkg.id || i.receivingPackageId === pkg.id)
    && (i.state === 'open' || i.state === 'agreed')
    && workingDaysOverdue(i.needBy, today, cal) > th.interfaceOverdueRedWd)
  if (lateInterfaces.length > 0) {
    return mk('red', 'PH-R2', 'interface item overdue past escalation', `> ${th.interfaceOverdueRedWd} wd overdue`,
      lateInterfaces.map((i) => ({ recordType: 'interface_item', id: i.id, ref: i.ref, why: `need-by ${i.needBy}, ${i.givingParty} → ${i.receivingParty}` })))
  }
  // PH-A1: ≥ 20% of active deliverables amber/red
  const pressured = statuses.filter((s) => s.health.value !== 'green')
  if (dels.length > 0 && pressured.length / dels.length >= 0.2) {
    return mk('amber', 'PH-A1', `${pressured.length}/${dels.length} deliverables amber or red`, '>= 20%',
      pressured.map((s) => ({ recordType: 'deliverable', id: s.deliverable.id, ref: s.deliverable.docNo, why: `${s.health.value} (${s.health.ruleId})` })))
  }
  // PH-A2: package-level decision past need-by
  const lateDecisions = snap.decisions.filter((d) =>
    d.packageId === pkg.id
    && (d.state === 'identified' || d.state === 'in_progress' || d.state === 'pending')
    && daysOverdue(d.needBy, today) > 0)
  if (lateDecisions.length > 0) {
    return mk('amber', 'PH-A2', 'package-level decision past need-by', 'need-by past',
      lateDecisions.map((d) => ({ recordType: 'decision', id: d.id, ref: d.ref, why: `need-by ${d.needBy}, state ${d.state}` })))
  }
  return mk('green', 'PH-G', 'no breach', '', [])
}

// ---------- governance signals (§8.4) ----------

export type SignalLevel = 'none' | 'warn' | 'red'

export interface Signal {
  id: string
  label: string
  level: SignalLevel
  detail: string
  threshold: string
  contributing: ContributingRef[]
}

export function projectSignals(snap: ProjectSnapshot): Signal[] {
  const th = snap.project.thresholds
  const cal = snap.project.calendar
  const today = snap.today
  const signals: Signal[] = []

  const push = (id: string, label: string, threshold: string, warn: ContributingRef[], red: ContributingRef[]) => {
    const level: SignalLevel = red.length > 0 ? 'red' : warn.length > 0 ? 'warn' : 'none'
    signals.push({
      id, label, level, threshold,
      detail: level === 'none' ? 'within thresholds' : `${red.length > 0 ? red.length : warn.length} record(s) breaching`,
      contributing: red.length > 0 ? red : warn,
    })
  }

  // S-HOLD: hold age
  {
    const warn: ContributingRef[] = []; const red: ContributingRef[] = []
    for (const h of snap.holds.filter((x) => x.state === 'active')) {
      const age = ageWorkingDays(h.raisedAt, today, cal)
      const c: ContributingRef = { recordType: 'hold', id: h.id, ref: h.ref, why: `${h.cause}, age ${age} wd` }
      if (age > th.holdAgeRedWd) red.push(c)
      else if (age > th.holdAgeWarnWd) warn.push(c)
    }
    push('S-HOLD', 'Hold age', `warn > ${th.holdAgeWarnWd} wd, escalate > ${th.holdAgeRedWd} wd`, warn, red)
  }

  // S-DEC: decision past need-by (red also when blocking an issue transition)
  {
    const warn: ContributingRef[] = []; const red: ContributingRef[] = []
    const undecided = snap.decisions.filter((d) => d.state === 'identified' || d.state === 'in_progress' || d.state === 'pending')
    const issueBlockingDecisionIds = new Set<number>()
    for (const c of snap.conditions) {
      if (c.gatedTransition === 'revision.issue' && c.severity === 'hard'
        && c.requiredRefType === 'decision' && c.requiredRefId != null) {
        const ev = evaluateCondition(snap, c)
        if (ev.effectiveState === 'open' || ev.effectiveState === 'blocked_by_hold') {
          issueBlockingDecisionIds.add(c.requiredRefId)
        }
      }
    }
    for (const d of undecided) {
      const over = daysOverdue(d.needBy, today)
      if (over <= 0) continue
      const blocking = issueBlockingDecisionIds.has(d.id)
      const c: ContributingRef = {
        recordType: 'decision', id: d.id, ref: d.ref,
        why: `${over} d past need-by${blocking ? ', blocks an issue transition' : ''}`,
      }
      if (over > th.decisionOverdueRedD || blocking) red.push(c)
      else warn.push(c)
    }
    push('S-DEC', 'Decision past need-by', `warn > ${th.decisionOverdueWarnD} d, escalate > ${th.decisionOverdueRedD} d or blocking issue`, warn, red)
  }

  // S-APPR: approval latency (ready, undecided)
  {
    const warn: ContributingRef[] = []; const red: ContributingRef[] = []
    for (const a of snap.approvalRecords.filter((x) => x.state === 'ready' && x.readyAt)) {
      const age = ageWorkingDays(a.readyAt!, today, cal)
      const c: ContributingRef = { recordType: 'approval_record', id: a.id, ref: a.ref, why: `ready ${age} wd, undecided` }
      if (age > th.approvalLatencyRedWd) red.push(c)
      else if (age > th.approvalLatencyWarnWd) warn.push(c)
    }
    push('S-APPR', 'Approval latency', `warn > ${th.approvalLatencyWarnWd} wd, escalate > ${th.approvalLatencyRedWd} wd`, warn, red)
  }

  // S-CMT: open check-comment age
  {
    const warn: ContributingRef[] = []; const red: ContributingRef[] = []
    for (const c of snap.reviewComments.filter(commentIsOpen)) {
      const age = ageWorkingDays(c.createdAt, today, cal)
      const r: ContributingRef = { recordType: 'review_comment', id: c.id, ref: c.ref, why: `open ${age} wd` }
      if (age > th.commentAgeRedWd) red.push(r)
      else if (age > th.commentAgeWarnWd) warn.push(r)
    }
    push('S-CMT', 'Check comment age', `warn > ${th.commentAgeWarnWd} wd, escalate > ${th.commentAgeRedWd} wd`, warn, red)
  }

  // S-INTAKE: untriaged intake age
  {
    const warn: ContributingRef[] = []; const red: ContributingRef[] = []
    for (const i of snap.intakeItems.filter((x) => x.state === 'raised' || x.state === 'in_triage')) {
      const age = ageWorkingDays(i.raisedAt, today, cal)
      const c: ContributingRef = { recordType: 'intake_item', id: i.id, ref: i.ref, why: `untriaged ${age} wd` }
      if (age > th.untriagedRedWd) red.push(c)
      else if (age > th.untriagedWarnWd) warn.push(c)
    }
    push('S-INTAKE', 'Untriaged intake age', `warn > ${th.untriagedWarnWd} wd, escalate > ${th.untriagedRedWd} wd`, warn, red)
  }

  // S-ANCHOR: unanchored items (I-2: untriaged intake is the unanchored population in P1)
  {
    const unanchored = snap.intakeItems.filter((x) => x.state !== 'dispositioned')
    const aged = unanchored.filter((x) => calendarDaysBetween(localDate(x.raisedAt, cal.timezone), today) > th.unanchoredRedAgeD)
    const refs = unanchored.map((i) => ({
      recordType: 'intake_item' as const, id: i.id, ref: i.ref, why: `awaiting triage/anchor since ${localDate(i.raisedAt, cal.timezone)}`,
    }))
    const level: SignalLevel = unanchored.length > th.unanchoredRedCount || aged.length > 0
      ? 'red' : unanchored.length > th.unanchoredWarnCount ? 'warn' : 'none'
    signals.push({
      id: 'S-ANCHOR', label: 'Unanchored items', level,
      detail: level === 'none' ? 'none unanchored' : `${unanchored.length} unanchored${aged.length > 0 ? `, ${aged.length} older than ${th.unanchoredRedAgeD} d` : ''}`,
      threshold: `warn > ${th.unanchoredWarnCount}, escalate > ${th.unanchoredRedCount} or age > ${th.unanchoredRedAgeD} d`,
      contributing: refs,
    })
  }

  // S-SCHED: schedule forecast vs gate (deliverables carrying a milestone)
  {
    const warn: ContributingRef[] = []; const red: ContributingRef[] = []
    for (const d of snap.deliverables.filter((x) => x.milestone)) {
      const s = deliverableStatus(snap, d)
      if (s.forecastSlipWd > th.schedulePressureRedD) {
        red.push({ recordType: 'deliverable', id: d.id, ref: d.docNo, why: `slip ${s.forecastSlipWd} wd vs ${d.milestone}` })
      } else if (s.forecastSlipWd > th.schedulePressureWarnD) {
        warn.push({ recordType: 'deliverable', id: d.id, ref: d.docNo, why: `slip ${s.forecastSlipWd} wd vs ${d.milestone}` })
      }
    }
    push('S-SCHED', 'Schedule forecast vs gate', `warn > ${th.schedulePressureWarnD} d, escalate > ${th.schedulePressureRedD} d`, warn, red)
  }

  return signals
}

// ---------- project health & KPIs ----------

export interface ProjectStatus {
  health: Explain<Health>
  packageStatuses: PackageStatus[]
  signals: Signal[]
  kpis: {
    pctOnPlan: Explain<number>
    holdsByCause: Explain<Record<string, number>>
    openDecisions: Explain<number>
    approvalsInFlight: Explain<number>
    scheduleForecastWd: Explain<number>
  }
}

export function projectStatus(snap: ProjectSnapshot): ProjectStatus {
  const pkgs = snap.packages.map((p) => packageStatus(snap, p))
  const signals = projectSignals(snap)

  let health: Health = 'green'
  for (const p of pkgs) health = worse(health, p.health.value)
  const worstPkg = pkgs.find((p) => p.health.value === health)

  // §8.4 table: warn column = amber contribution (floor amber), escalate column = red contribution.
  const redSignals = signals.filter((s) => s.level === 'red')
  const warnSignals = signals.filter((s) => s.level === 'warn')
  let ruleId = 'PJ-PKG'
  let detail = worstPkg ? `worst package: ${worstPkg.pkg.code} (${worstPkg.health.ruleId})` : 'no packages'
  const contributing: ContributingRef[] = worstPkg
    ? [{ recordType: 'package', id: worstPkg.pkg.id, ref: worstPkg.pkg.code, why: worstPkg.health.detail }]
    : []
  if (redSignals.length > 0) {
    health = 'red'
    ruleId = 'PJ-ESC'
    detail += `; red contribution: ${redSignals.map((s) => s.id).join(', ')} breached escalation threshold`
    for (const s of redSignals) contributing.push(...s.contributing.slice(0, 5))
  } else if (warnSignals.length > 0 && health === 'green') {
    health = 'amber'
    ruleId = 'PJ-WARN'
    detail += `; amber contribution: ${warnSignals.map((s) => s.id).join(', ')}`
    for (const s of warnSignals) contributing.push(...s.contributing.slice(0, 5))
  }

  const allDel = pkgs.flatMap((p) => p.deliverableStatuses)
  const green = allDel.filter((s) => s.health.value === 'green')
  const holdsByCause: Record<string, number> = {}
  const activeHolds = snap.holds.filter((h) => h.state === 'active')
  for (const h of activeHolds) holdsByCause[h.cause] = (holdsByCause[h.cause] ?? 0) + 1
  const openDecisions = snap.decisions.filter((d) => d.state === 'identified' || d.state === 'in_progress' || d.state === 'pending')
  const inFlight = snap.approvalRecords.filter((a) => a.state === 'required' || a.state === 'prereqs_incomplete' || a.state === 'ready')
  const maxSlip = allDel.reduce((m, s) => Math.max(m, s.forecastSlipWd), 0)
  const maxSlipDel = allDel.find((s) => s.forecastSlipWd === maxSlip && maxSlip > 0)

  return {
    health: { value: health, ruleId, detail, threshold: 'worst package, escalated on signal breach (§8.4)', contributing },
    packageStatuses: pkgs,
    signals,
    kpis: {
      pctOnPlan: {
        value: allDel.length > 0 ? Math.round((green.length / allDel.length) * 100) : 100,
        ruleId: 'KPI-ONPLAN', detail: `${green.length}/${allDel.length} deliverables green`,
        contributing: allDel.filter((s) => s.health.value !== 'green').map((s) => ({
          recordType: 'deliverable' as const, id: s.deliverable.id, ref: s.deliverable.docNo, why: `${s.health.value} (${s.health.ruleId})`,
        })),
      },
      holdsByCause: {
        value: holdsByCause, ruleId: 'KPI-HOLDS', detail: `${activeHolds.length} active holds`,
        contributing: activeHolds.map((h) => ({ recordType: 'hold' as const, id: h.id, ref: h.ref, why: h.cause })),
      },
      openDecisions: {
        value: openDecisions.length, ruleId: 'KPI-DEC', detail: 'decisions not yet decided',
        contributing: openDecisions.map((d) => ({ recordType: 'decision' as const, id: d.id, ref: d.ref, why: d.state })),
      },
      approvalsInFlight: {
        value: inFlight.length, ruleId: 'KPI-APPR', detail: 'approval records not yet decided',
        contributing: inFlight.map((a) => ({ recordType: 'approval_record' as const, id: a.id, ref: a.ref, why: a.state })),
      },
      scheduleForecastWd: {
        value: maxSlip, ruleId: 'KPI-SCHED', detail: maxSlipDel ? `worst slip ${maxSlip} wd (${maxSlipDel.deliverable.docNo})` : 'no slip',
        contributing: maxSlipDel ? [{ recordType: 'deliverable', id: maxSlipDel.deliverable.id, ref: maxSlipDel.deliverable.docNo, why: `slip ${maxSlip} wd` }] : [],
      },
    },
  }
}

// ---------- waiting on you (PEC-OV-004, SPEC §6.5) ----------

export interface WaitingOnYouItem {
  kind: 'decision' | 'approval'
  recordType: 'decision' | 'approval_record'
  id: number
  ref: string
  title: string
  needBy: string | null
  ageWd: number
  breach: SignalLevel
  blocks: ContributingRef[]
}

export function waitingOnYou(snap: ProjectSnapshot, personId: number): WaitingOnYouItem[] {
  const th = snap.project.thresholds
  const cal = snap.project.calendar
  const today = snap.today
  const out: WaitingOnYouItem[] = []

  const blocksOf = (refType: 'decision' | 'approval_record', id: number): ContributingRef[] => {
    const res: ContributingRef[] = []
    for (const c of snap.conditions) {
      if (c.requiredRefType !== refType || c.requiredRefId !== id) continue
      const ev = evaluateCondition(snap, c)
      if (ev.effectiveState === 'open' || ev.effectiveState === 'blocked_by_hold') {
        res.push({ recordType: c.parentType, id: c.parentId, ref: c.ref, why: `gates ${c.gatedTransition}` })
      }
    }
    return res
  }

  for (const d of snap.decisions.filter((x) => x.state === 'pending' && x.authorityId === personId)) {
    const over = daysOverdue(d.needBy, today)
    out.push({
      kind: 'decision', recordType: 'decision', id: d.id, ref: d.ref, title: d.title,
      needBy: d.needBy, ageWd: ageWorkingDays(d.createdAt, today, cal),
      breach: over > th.decisionOverdueRedD ? 'red' : over > th.decisionOverdueWarnD ? 'warn' : 'none',
      blocks: blocksOf('decision', d.id),
    })
  }
  for (const a of snap.approvalRecords.filter((x) => x.state === 'ready' && x.signatoryIds.includes(personId))) {
    const age = a.readyAt ? ageWorkingDays(a.readyAt, today, cal) : 0
    out.push({
      kind: 'approval', recordType: 'approval_record', id: a.id, ref: a.ref, title: a.title,
      needBy: a.dueDate, ageWd: age,
      breach: age > th.approvalLatencyRedWd ? 'red' : age > th.approvalLatencyWarnWd ? 'warn' : 'none',
      blocks: blocksOf('approval_record', a.id),
    })
  }
  const rank: Record<SignalLevel, number> = { red: 2, warn: 1, none: 0 }
  return out.sort((x, y) => rank[y.breach] - rank[x.breach] || x.ageWd - y.ageWd)
}

// ---------- My Week (PEC-MW-*, SPEC §6 / §9) ----------

export interface MyWeekItem {
  workItem: WorkItem
  deliverable: Deliverable | null
  whyInWeek: string // PEC-MW-005
  overdue: boolean
  blockedBy: Array<{ ref: string; cause: string; title: string }>
}

export interface MyWeek {
  week: string
  committed: MyWeekItem[]
  /** checks and comment responses the user owes others — booked work (PEC-MW-002) */
  checksOwed: Array<{ checkRef: string; checkId: number; revisionId: number; deliverable: Deliverable | null; state: string; openComments: number; overdue: boolean }>
  commentsOwed: Array<{ commentRef: string; commentId: number; checkRef: string; deliverable: Deliverable | null; text: string; ageWd: number; overdue: boolean }>
  /** holds and decisions gating the user's work — chase-able, not commitments (PEC-MW-003) */
  waitingOnOthers: Array<{ kind: 'hold' | 'decision'; ref: string; id: number; title: string; ownerId: number | null; needBy: string | null; gates: string }>
}

export function myWeek(snap: ProjectSnapshot, personId: number): MyWeek {
  const cal = snap.project.calendar
  const today = snap.today
  const week = isoWeekOf(today)

  const deliverableOf = (w: WorkItem): Deliverable | null => {
    if (w.anchorType === 'deliverable') return snap.deliverables.find((d) => d.id === w.anchorId) ?? null
    if (w.anchorType === 'revision') {
      const r = snap.revisions.find((x) => x.id === w.anchorId)
      return r ? snap.deliverables.find((d) => d.id === r.deliverableId) ?? null : null
    }
    return null
  }
  const deliverableOfRevision = (revisionId: number): Deliverable | null => {
    const r = snap.revisions.find((x) => x.id === revisionId)
    return r ? snap.deliverables.find((d) => d.id === r.deliverableId) ?? null : null
  }

  const committed: MyWeekItem[] = []
  for (const w of snap.workItems) {
    if (w.ownerId !== personId || (w.state !== 'open' && w.state !== 'in_work')) continue
    const overdue = w.needBy != null && daysOverdue(w.needBy, today) > 0
    let why: string | null = null
    if (w.committedWeek === week) why = 'committed to this week (manual)'
    else if (overdue) why = `overdue: need-by ${w.needBy} past (escalation)`
    else if (w.needBy && isoWeekOf(w.needBy) === week) why = `need-by ${w.needBy} falls this week`
    if (!why) continue
    committed.push({
      workItem: w, deliverable: deliverableOf(w), whyInWeek: why, overdue,
      blockedBy: activeHoldsFor(snap, 'work_item', w.id).map((h) => ({ ref: h.ref, cause: h.cause, title: h.title })),
    })
  }

  const checksOwed = snap.checks
    .filter((c) => c.checkerId === personId && (c.state === 'open' || c.state === 'in_check' || c.state === 'comments_open' || c.state === 'comments_closed'))
    .map((c) => {
      const open = snap.reviewComments.filter((x) => x.checkId === c.id && commentIsOpen(x)).length
      const del = deliverableOfRevision(c.revisionId)
      const overdue = del?.dueDate != null && daysOverdue(del.dueDate, today) > 0
      return { checkRef: c.ref, checkId: c.id, revisionId: c.revisionId, deliverable: del, state: c.state, openComments: open, overdue }
    })

  const commentsOwed = snap.reviewComments
    .filter((c) => c.responderId === personId && (c.disposition === 'open' || c.disposition === 'reopened'))
    .map((c) => {
      const chk = c.checkId != null ? snap.checks.find((x) => x.id === c.checkId) : undefined
      const revId = chk?.revisionId ?? c.revisionId
      return {
        commentRef: c.ref, commentId: c.id, checkRef: chk?.ref ?? 'client return',
        deliverable: revId != null ? deliverableOfRevision(revId) : null,
        text: c.text, ageWd: ageWorkingDays(c.createdAt, today, cal),
        overdue: ageWorkingDays(c.createdAt, today, cal) > snap.project.thresholds.commentAgeWarnWd,
      }
    })

  // Waiting on others: active holds on my records; undecided decisions pinned on open conditions of my records.
  const myOpenItems = snap.workItems.filter((w) => w.ownerId === personId && (w.state === 'open' || w.state === 'in_work'))
  const myDeliverables = snap.deliverables.filter((d) => d.ownerId === personId)
  const myRevisionIds = new Set(
    myDeliverables.map((d) => currentRevision(snap, d.id)?.id).filter((x): x is number => x != null),
  )
  const waiting: MyWeek['waitingOnOthers'] = []
  const seenHold = new Set<number>()
  const holdTargets: Array<['work_item' | 'revision' | 'deliverable', number, string]> = [
    ...myOpenItems.map((w) => ['work_item', w.id, w.ref] as ['work_item', number, string]),
    ...myDeliverables.map((d) => ['deliverable', d.id, d.docNo] as ['deliverable', number, string]),
    ...[...myRevisionIds].map((id) => ['revision', id, `rev#${id}`] as ['revision', number, string]),
  ]
  for (const [tt, tid, tref] of holdTargets) {
    for (const h of activeHoldsFor(snap, tt, tid)) {
      if (seenHold.has(h.id)) continue
      seenHold.add(h.id)
      waiting.push({ kind: 'hold', ref: h.ref, id: h.id, title: h.title, ownerId: h.ownerId, needBy: h.needBy, gates: `blocks ${tref}` })
    }
  }
  const seenDec = new Set<number>()
  for (const c of snap.conditions) {
    if (c.requiredRefType !== 'decision' || c.requiredRefId == null) continue
    const mine = (c.parentType === 'work_item' && myOpenItems.some((w) => w.id === c.parentId))
      || (c.parentType === 'revision' && myRevisionIds.has(c.parentId))
    if (!mine) continue
    const ev = evaluateCondition(snap, c)
    if (ev.effectiveState !== 'open' && ev.effectiveState !== 'blocked_by_hold') continue
    const d = snap.decisions.find((x) => x.id === c.requiredRefId)
    if (!d || d.state === 'decided' || d.state === 'superseded' || seenDec.has(d.id)) continue
    seenDec.add(d.id)
    waiting.push({ kind: 'decision', ref: d.ref, id: d.id, title: d.title, ownerId: d.authorityId, needBy: d.needBy, gates: `gates ${c.gatedTransition} (${c.ref})` })
  }

  return { week, committed, checksOwed, commentsOwed, waitingOnOthers: waiting }
}
