/**
 * Read-side composition for the role homes. All derivation happens here / in core —
 * the web layer renders only (SPEC §1). Log visibility is applied at serialization
 * (SPEC §2.2): rows outside the caller's visible logs are filtered from registers;
 * contributing refs are redacted, not dropped, in explanations.
 */

import type {
  Check, Condition, ContributingRef, Deliverable, Explain, Hold, IntakeItem, InterfaceItem, Log,
  Package, PackageTracker, Project, ProjectSnapshot, ReviewComment, Revision, Risk, WorkItem,
} from '@pec/core'
import {
  activeHoldsFor, ageWorkingDays, capacityView, commentIsOpen, currentRevision, daysOverdue,
  deliverableStatus, explainTransition, isoWeekOf, isoWeeksFrom, localDate, myWeek,
  packageStatus, projectStatus, resolvePlanItem, transitionsFrom, visibleLogs, waitingOnYou,
  workflowCompleteness, workingDaysOverdue,
} from '@pec/core'
import type { Sx } from './shared.ts'
import { snapshot } from './shared.ts'
import { notFound } from '../errors.ts'

function logsFor(sx: Sx, snap: ProjectSnapshot): Log[] {
  return visibleLogs(sx.roles, snap.project.config.logVisibility)
}

/**
 * Filter a list of log-bearing records to those the caller may see (PEC-NFR-005).
 * Derived counts/health run on the unfiltered snapshot (shared truth, SPEC §2.2), but
 * any row list carrying titles/details must be visibility-filtered before serialization.
 */
function visibleByLog<T extends { log: Log }>(sx: Sx, snap: ProjectSnapshot, rows: T[]): T[] {
  const logs = logsFor(sx, snap)
  if (logs.length === 3) return rows
  return rows.filter((r) => logs.includes(r.log))
}

/**
 * Redact contributing refs pointing at records outside the caller's visible logs (SPEC §2.2):
 * the ref (type + ref) is kept, its `why` statement omitted. Only the six log-scoped record
 * types can be restricted; refs to non-log-scoped types (approval_record, plan_item, deliverable,
 * check, revision, …) carry no log-owned content and pass through unchanged.
 */
function redactRefs(sx: Sx, snap: ProjectSnapshot, refs: ContributingRef[]): ContributingRef[] {
  const logs = logsFor(sx, snap)
  if (logs.length === 3) return refs
  const holder = (rt: string, id: number): { log?: Log } | undefined => {
    switch (rt) {
      case 'work_item': return snap.workItems.find((x) => x.id === id)
      case 'hold': return snap.holds.find((x) => x.id === id)
      case 'intake_item': return snap.intakeItems.find((x) => x.id === id)
      case 'interface_item': return snap.interfaces.find((x) => x.id === id)
      case 'decision': return snap.decisions.find((x) => x.id === id)
      case 'review_comment': return snap.reviewComments.find((x) => x.id === id)
      default: return undefined
    }
  }
  return refs.map((c) => {
    const rec = holder(c.recordType, c.id)
    return rec?.log && !logs.includes(rec.log) ? { ...c, why: '[restricted log]' } : c
  })
}

/** Redact an Explain payload's contributing refs pointing outside the caller's visible logs (SPEC §2.2). */
function redact<T>(sx: Sx, snap: ProjectSnapshot, explain: Explain<T>): Explain<T> {
  return { ...explain, contributing: redactRefs(sx, snap, explain.contributing) }
}

// ---------- Overview (PEC-OV-*) ----------

export function overviewView(sx: Sx): unknown {
  const snap = snapshot(sx)
  const status = projectStatus(snap)
  const waiting = waitingOnYou(snap, sx.session.personId)
  const cal = snap.project.calendar
  // top blockers: active holds by age, typed by cause (PEC-OV-005) — visibility-filtered
  // since these rows carry titles (PEC-NFR-005)
  const blockers = visibleByLog(sx, snap, snap.holds.filter((h) => h.state === 'active'))
    .map((h) => ({
      ref: h.ref, id: h.id, title: h.title, cause: h.cause, ownerId: h.ownerId,
      needBy: h.needBy, ageWd: ageWorkingDays(h.raisedAt, snap.today, cal),
      blocks: snap.holdLinks.filter((l) => l.holdId === h.id).length,
    }))
    .sort((a, b) => b.ageWd - a.ageWd)
    .slice(0, 10)

  return {
    project: { id: snap.project.id, code: snap.project.code, name: snap.project.name },
    health: redact(sx, snap, status.health),
    kpis: {
      pctOnPlan: redact(sx, snap, status.kpis.pctOnPlan),
      holdsByCause: redact(sx, snap, status.kpis.holdsByCause),
      openDecisions: redact(sx, snap, status.kpis.openDecisions),
      approvalsInFlight: redact(sx, snap, status.kpis.approvalsInFlight),
      scheduleForecastWd: redact(sx, snap, status.kpis.scheduleForecastWd),
    },
    // signals derive on the full snapshot (shared truth) but their contributing refs must be
    // visibility-redacted before serialization, like the KPIs above (SPEC §2.2, PEC-NFR-005)
    signals: status.signals.map((s) => ({ ...s, contributing: redactRefs(sx, snap, s.contributing) })),
    packageRollup: status.packageStatuses.map((p) => ({
      id: p.pkg.id, code: p.pkg.code, name: p.pkg.name, leadId: p.pkg.leadId,
      health: redact(sx, snap, p.health),
      onPlan: p.onPlanCount, total: p.totalCount,
      holds: snap.holds.filter((h) => h.state === 'active'
        && snap.holdLinks.some((l) => l.holdId === h.id && isInPackage(snap, l.targetType, l.targetId, p.pkg.id))).length,
      checksDue: snap.checks.filter((c) => c.state !== 'accepted' && c.state !== 'reopened'
        && revisionPackage(snap, c.revisionId) === p.pkg.id).length,
      approvalsDue: snap.approvalRecords.filter((a) => (a.state === 'ready' || a.state === 'prereqs_incomplete')
        && appliesPackage(snap, a.appliesToType, a.appliesToId) === p.pkg.id).length,
      openDecisions: snap.decisions.filter((d) => d.packageId === p.pkg.id
        && (d.state === 'identified' || d.state === 'in_progress' || d.state === 'pending')).length,
      // same log-scoped count the Packages register and cockpit show (ADR-012, PEC-NFR-005)
      openIssues: openIssueCount(sx, snap, p.pkg),
    })),
    // rows are self-scoped (items awaiting this caller's own signature/decision), but the
    // `blocks` refs can name records in logs the caller can't see — redact those (SPEC §2.2)
    waitingOnYou: (() => {
      const scrub = (w: typeof waiting[number]) => ({ ...w, blocks: redactRefs(sx, snap, w.blocks) })
      return {
        breaching: waiting.filter((w) => w.breach !== 'none').map(scrub),
        other: waiting.filter((w) => w.breach === 'none').map(scrub),
      }
    })(),
    topBlockers: blockers,
    // PEC-OV-008 (P2): schedule pressure — lookahead load vs capacity, next six weeks
    schedulePressure: (() => {
      const weeks = isoWeeksFrom(snap.today, 6)
      const cells = capacityView(snap, weeks)
      const th = snap.project.thresholds
      return weeks.map((week) => {
        const wk = cells.filter((c) => c.week === week)
        const loadH = wk.reduce((s, c) => s + c.loadH, 0)
        const capacityH = wk.reduce((s, c) => s + (c.capacityH ?? 0), 0)
        const raw = capacityH > 0 ? (loadH / capacityH) * 100 : null
        return {
          week, loadH, capacityH,
          pct: raw != null ? Math.round(raw) : null,
          // level from the configurable thresholds so the client never hardcodes them (PEC-OV-007)
          level: raw == null ? 'none' : raw > th.capacityRedPct ? 'red' : raw > th.capacityWarnPct ? 'warn' : 'none',
          breaches: wk.filter((c) => c.level !== 'none')
            .map((c) => ({ discipline: c.discipline, pct: c.pct, level: c.level })),
        }
      })
    })(),
  }
}

function revisionPackage(snap: ProjectSnapshot, revisionId: number): number | null {
  const rev = snap.revisions.find((r) => r.id === revisionId)
  if (!rev) return null
  return snap.deliverables.find((d) => d.id === rev.deliverableId)?.packageId ?? null
}

function appliesPackage(snap: ProjectSnapshot, type: string, id: number): number | null {
  if (type === 'revision') return revisionPackage(snap, id)
  if (type === 'deliverable') return snap.deliverables.find((d) => d.id === id)?.packageId ?? null
  if (type === 'package') return id
  return null
}

function isInPackage(snap: ProjectSnapshot, targetType: string, targetId: number, packageId: number): boolean {
  switch (targetType) {
    case 'deliverable': return snap.deliverables.find((d) => d.id === targetId)?.packageId === packageId
    case 'revision': return revisionPackage(snap, targetId) === packageId
    case 'work_item': return snap.workItems.find((w) => w.id === targetId)?.packageId === packageId
    default: return false
  }
}

// ---------- Packages (PEC-PKG-*) ----------

/** Count of the package's open issues (holds, interfaces, decisions, risks, action items),
 *  scoped to the caller's visible logs so it matches the drill-down cockpit (PEC-NFR-005). */
function openIssueCount(sx: Sx, snap: ProjectSnapshot, pkg: Package): number {
  const logs = logsFor(sx, snap)
  const sees = (l: Log): boolean => logs.length === 3 || logs.includes(l)
  const delIds = new Set(snap.deliverables.filter((d) => d.packageId === pkg.id).map((d) => d.id))
  const revIds = new Set(snap.revisions.filter((r) => delIds.has(r.deliverableId)).map((r) => r.id))
  const holds = snap.holds.filter((h) => h.state === 'active' && sees(h.log)
    && snap.holdLinks.some((l) => l.holdId === h.id && isInPackage(snap, l.targetType, l.targetId, pkg.id))).length
  const interfaces = snap.interfaces.filter((i) => sees(i.log)
    && (i.givingPackageId === pkg.id || i.receivingPackageId === pkg.id) && (i.state === 'open' || i.state === 'agreed')).length
  const decisions = snap.decisions.filter((d) => sees(d.log)
    && d.packageId === pkg.id && d.state !== 'decided' && d.state !== 'superseded').length
  const risks = (snap.risks as Risk[]).filter((r) =>
    (r.packageId === pkg.id || (r.deliverableId != null && delIds.has(r.deliverableId))) && r.state !== 'closed').length
  const actions = snap.workItems.filter((w) =>
    (w.state === 'open' || w.state === 'in_work') && (w.kind === 'action' || w.kind === 'coordination') && sees(w.log)
    && (w.packageId === pkg.id
      || (w.anchorType === 'deliverable' && delIds.has(w.anchorId))
      || (w.anchorType === 'revision' && revIds.has(w.anchorId)))).length
  return holds + interfaces + decisions + risks + actions
}

export function packagesView(sx: Sx): unknown {
  const snap = snapshot(sx)
  return snap.packages.map((p) => {
    const st = packageStatus(snap, p)
    return {
      id: p.id, code: p.code, name: p.name, leadId: p.leadId, milestone: p.milestone,
      health: redact(sx, snap, st.health), onPlan: st.onPlanCount, total: st.totalCount,
      openIssues: openIssueCount(sx, snap, p),
    }
  })
}

export function packageDetailView(sx: Sx, packageId: number): unknown {
  const snap = snapshot(sx)
  const pkg = snap.packages.find((p) => p.id === packageId)
  if (!pkg) throw notFound(`package #${packageId}`)
  const st = packageStatus(snap, pkg)
  const cal = snap.project.calendar
  const today = snap.today
  const leadId = pkg.leadId
  const overdue = (needBy: string | null): boolean => needBy != null && daysOverdue(needBy, today) > 0

  // sphere: deliverables in this package + their revisions (for anchoring action items & risks)
  const pkgDelIds = new Set(snap.deliverables.filter((d) => d.packageId === pkg.id).map((d) => d.id))
  const pkgRevIds = new Set(snap.revisions.filter((r) => pkgDelIds.has(r.deliverableId)).map((r) => r.id))
  const workItemInPkg = (w: WorkItem): boolean =>
    w.packageId === pkg.id
    || (w.anchorType === 'deliverable' && pkgDelIds.has(w.anchorId))
    || (w.anchorType === 'revision' && pkgRevIds.has(w.anchorId))

  // ---- the package's open issues (holds, interfaces, decisions, risks, action items) ----
  // Tasks live on deliverables (workflow status); ISSUES live here — the lead's cockpit.
  const holdsByCause: Record<string, number> = {}
  const pkgHolds = snap.holds.filter((h) => h.state === 'active'
    && snap.holdLinks.some((l) => l.holdId === h.id && isInPackage(snap, l.targetType, l.targetId, pkg.id)))
  for (const h of pkgHolds) holdsByCause[h.cause] = (holdsByCause[h.cause] ?? 0) + 1

  // Row lists carry titles/details → filter by log visibility (PEC-NFR-005). Counts and health
  // run on the unfiltered snapshot (shared truth).
  const visHolds = visibleByLog(sx, snap, pkgHolds)
  const allInterfaces = visibleByLog(sx, snap, snap.interfaces.filter((i) =>
    i.givingPackageId === pkg.id || i.receivingPackageId === pkg.id))
  const openInterfaces = allInterfaces.filter((i) => i.state === 'open' || i.state === 'agreed')
  const allDecisions = visibleByLog(sx, snap, snap.decisions.filter((d) => d.packageId === pkg.id))
  const openDecisions = allDecisions.filter((d) => d.state !== 'decided' && d.state !== 'superseded')
  const pkgRisks = (snap.risks as Risk[]).filter((r) =>
    (r.packageId === pkg.id || (r.deliverableId != null && pkgDelIds.has(r.deliverableId))) && r.state !== 'closed')
  const actionItems = visibleByLog(sx, snap, snap.workItems.filter((w) =>
    (w.state === 'open' || w.state === 'in_work') && (w.kind === 'action' || w.kind === 'coordination') && workItemInPkg(w)))

  interface Issue {
    type: 'hold' | 'interface' | 'decision' | 'risk' | 'action'
    recordType: string; ref: string; id: number; title: string
    ownerId: number | null; needBy: string | null; state: string
    overdue: boolean; ageWd: number; detail: string
  }
  const issues: Issue[] = [
    ...visHolds.map((h) => ({
      type: 'hold' as const, recordType: 'hold', ref: h.ref, id: h.id, title: h.title,
      ownerId: h.ownerId, needBy: h.needBy, state: h.state, overdue: overdue(h.needBy),
      ageWd: ageWorkingDays(h.raisedAt, today, cal), detail: h.cause.replaceAll('_', ' '),
    })),
    ...openInterfaces.map((i) => ({
      type: 'interface' as const, recordType: 'interface_item', ref: i.ref, id: i.id, title: i.title,
      ownerId: null, needBy: i.needBy, state: i.state, overdue: overdue(i.needBy),
      ageWd: 0, detail: `${i.givingParty} → ${i.receivingParty}`,
    })),
    ...openDecisions.map((d) => ({
      type: 'decision' as const, recordType: 'decision', ref: d.ref, id: d.id, title: d.title,
      ownerId: d.authorityId, needBy: d.needBy, state: d.state, overdue: overdue(d.needBy),
      ageWd: ageWorkingDays(d.createdAt, today, cal), detail: `state ${d.state}`,
    })),
    ...pkgRisks.map((r) => ({
      type: 'risk' as const, recordType: 'risk', ref: r.ref, id: r.id, title: r.title,
      ownerId: r.ownerId, needBy: r.needBy, state: r.state, overdue: overdue(r.needBy),
      ageWd: 0, detail: r.probability != null && r.impact != null ? `P${r.probability}×I${r.impact}` : (r.cause ?? '—'),
    })),
    ...actionItems.map((w) => ({
      type: 'action' as const, recordType: 'work_item', ref: w.ref, id: w.id, title: w.title,
      ownerId: w.ownerId, needBy: w.needBy, state: w.state, overdue: overdue(w.needBy),
      ageWd: ageWorkingDays(w.createdAt, today, cal), detail: w.kind.replaceAll('_', ' '),
    })),
  ].sort((a, b) =>
    Number(b.overdue) - Number(a.overdue)
    || b.ageWd - a.ageWd
    || (a.needBy ?? '9999').localeCompare(b.needBy ?? '9999'))

  // "Needs the lead this week" (PEC-PKG-005) — the lead's personal action queue
  const needsLead = leadId == null ? [] : [
    ...snap.approvalRecords
      .filter((a) => a.state === 'ready' && a.signatoryIds.includes(leadId))
      .map((a) => ({ kind: 'sign_off_due', ref: a.ref, id: a.id, recordType: 'approval_record', title: a.title, due: a.dueDate })),
    ...openDecisions
      .filter((d) => d.state === 'pending' && d.authorityId === leadId)
      .map((d) => ({ kind: 'decision_to_rule', ref: d.ref, id: d.id, recordType: 'decision', title: d.title, due: d.needBy })),
    ...visHolds
      .filter((h) => h.ownerId === leadId)
      .map((h) => ({ kind: 'hold_to_resolve', ref: h.ref, id: h.id, recordType: 'hold', title: h.title, due: h.needBy })),
    ...openInterfaces
      .filter((i) => i.givingPackageId === pkg.id)
      .map((i) => ({ kind: 'interface_obligation', ref: i.ref, id: i.id, recordType: 'interface_item', title: i.title, due: i.needBy })),
  ]

  // PEC-PKG-003 (P2): the package's capacity/discipline load for the current planning period —
  // this package's plan items in the current week, against the project's discipline capacity
  const currentWeek = isoWeekOf(snap.today)
  const capacityCells = capacityView(snap, [currentWeek])
  const pkgLoad = capacityCells
    .map((cell) => {
      const pkgHours = cell.planItemIds.reduce((sum, piId) => {
        const pi = snap.planItems.find((x) => x.id === piId)
        if (!pi) return sum
        return resolvePlanItem(snap, pi)?.packageId === pkg.id ? sum + pi.plannedHours : sum
      }, 0)
      return { week: cell.week, discipline: cell.discipline, packageLoadH: pkgHours, disciplineLoadH: cell.loadH, capacityH: cell.capacityH, pct: cell.pct, level: cell.level }
    })
    .filter((row) => row.packageLoadH > 0 || row.level !== 'none')

  return {
    package: pkg,
    health: redact(sx, snap, st.health),
    summary: {
      deliverablesOnPlan: `${st.onPlanCount}/${st.totalCount}`,
      openIssues: issues.length,
      overdueIssues: issues.filter((i) => i.overdue).length,
      holdsByCause,
      openHolds: visHolds.length,
      openInterfaces: openInterfaces.length,
      openDecisions: openDecisions.length,
      openRisks: pkgRisks.length,
      openActionItems: actionItems.length,
    },
    capacity: { week: currentWeek, rows: pkgLoad },
    // the cockpit: every open issue, urgency-first (PEC-PKG issues orientation)
    issues,
    needsLead,
    // deliverables carry their WORKFLOW status (not issues), ordered by nearest commitment (PEC-PKG-004)
    deliverables: snap.deliverables
      .filter((d) => d.packageId === pkg.id)
      .map((d) => ({
        id: d.id, docNo: d.docNo, title: d.title, discipline: d.discipline, ownerId: d.ownerId,
        dueDate: d.dueDate, milestone: d.milestone, workflow: workflowCompleteness(snap, d),
      }))
      .sort((a, b) => (a.dueDate ?? '9999').localeCompare(b.dueDate ?? '9999')),
    // the grouped registers remain available for detail/CSV
    decisions: allDecisions.map((d) => ({
      ref: d.ref, id: d.id, title: d.title, state: d.state, needBy: d.needBy,
      overdueDays: (d.state === 'decided' || d.state === 'superseded') ? 0 : daysOverdue(d.needBy, today),
      affected: snap.decisionLinks.filter((l) => l.decisionId === d.id).length,
    })),
    interfaces: allInterfaces.map((i) => ({
      ref: i.ref, id: i.id, title: i.title, giving: i.givingParty, receiving: i.receivingParty,
      state: i.state, needBy: i.needBy, requiredInfo: i.requiredInfo,
      overdueWd: i.needBy ? ageWorkingDays(`${i.needBy}T00:00:00Z`, today, cal) : 0,
      blockingImpact: snap.holdLinks.filter((l) => {
        const h = snap.holds.find((x) => x.id === l.holdId)
        return h?.state === 'active' && h.cause === 'interface'
      }).length,
    })),
    risks: pkgRisks.map((r) => ({
      ref: r.ref, id: r.id, title: r.title, ownerId: r.ownerId, state: r.state,
      probability: r.probability, impact: r.impact, needBy: r.needBy,
      overdue: overdue(r.needBy), mitigation: r.mitigation,
    })),
  }
}

// ---------- Deliverables (PEC-DEL-*) ----------

export interface DeliverableFilters {
  packageId?: number
  discipline?: string
  state?: string
  holdCause?: string
  dueBefore?: string
  view?: 'active' | 'master' | 'issued'
}

export function deliverablesView(sx: Sx, f: DeliverableFilters): unknown {
  const snap = snapshot(sx)
  // A deliverable's summary STATUS is its workflow completeness (which gates are closed),
  // not its issue load — issues are surfaced at the package level (PEC-PKG issues cockpit).
  let rows = snap.deliverables.map((d) => {
    const rev = currentRevision(snap, d.id)
    return { d, rev, workflow: workflowCompleteness(snap, d) }
  })
  if (f.packageId) rows = rows.filter((r) => r.d.packageId === f.packageId)
  if (f.discipline) rows = rows.filter((r) => r.d.discipline === f.discipline)
  if (f.state) rows = rows.filter((r) => (r.rev?.state ?? 'no_revision') === f.state)
  if (f.dueBefore) rows = rows.filter((r) => r.d.dueDate != null && r.d.dueDate <= f.dueBefore!)
  if (f.view === 'issued') rows = rows.filter((r) => r.rev?.state === 'issued')
  else if (f.view === 'active' || !f.view) rows = rows.filter((r) => r.rev?.state !== 'superseded')

  return rows.map(({ d, rev, workflow }) => ({
    id: d.id, docNo: d.docNo, title: d.title, packageId: d.packageId,
    discipline: d.discipline, ownerId: d.ownerId, revCode: rev?.revCode ?? null,
    state: rev?.state ?? 'no_revision', dueDate: d.dueDate, milestone: d.milestone,
    dcRef: d.dcRef, workflow,
  }))
}

export function deliverableDetailView(sx: Sx, id: number): unknown {
  const snap = snapshot(sx)
  const d = snap.deliverables.find((x) => x.id === id)
  if (!d) throw notFound(`deliverable #${id}`)
  const logs = logsFor(sx, snap)
  const s = deliverableStatus(snap, d)
  const rev = s.revision
  const chain = snap.revisions
    .filter((r) => r.deliverableId === id)
    .sort((a, b) => a.id - b.id)
    .map((r) => ({
      id: r.id, revCode: r.revCode, state: r.state, createdAt: r.createdAt, version: r.version,
      supersededBy: r.supersededByRevisionId,
      issueEvents: snap.issueEvents.filter((e) => e.revisionId === r.id)
        .map((e) => ({ ref: e.ref, purpose: e.purpose, transmittalRef: e.transmittalRef, issuedAt: e.issuedAt, archiveRef: e.archiveRef, recipients: e.recipients })),
    }))

  const deliverableRevIds = new Set(snap.revisions.filter((r) => r.deliverableId === id).map((r) => r.id))
  const openItems = rev == null ? [] : {
    // I-1: open items on ANY revision of this deliverable, not just the current one
    workItems: snap.workItems.filter((w) => (w.state === 'open' || w.state === 'in_work')
      && ((w.anchorType === 'deliverable' && w.anchorId === id) || (w.anchorType === 'revision' && deliverableRevIds.has(w.anchorId)))
      && logs.includes(w.log)),
    checks: snap.checks.filter((c) => c.revisionId === rev.id).map((c) => ({
      ...c,
      openComments: snap.reviewComments.filter((x) => x.checkId === c.id && commentIsOpen(x)).length,
      totalComments: snap.reviewComments.filter((x) => x.checkId === c.id).length,
      checklistDone: c.checklist.filter((i) => i.done).length,
      checklistTotal: c.checklist.length,
    })),
    comments: snap.reviewComments.filter((c) => (c.revisionId === rev.id
      || snap.checks.some((k) => k.id === c.checkId && k.revisionId === rev.id)) && logs.includes(c.log)),
    holds: [...activeHoldsFor(snap, 'deliverable', id), ...activeHoldsFor(snap, 'revision', rev.id)],
    approvalRecords: snap.approvalRecords.filter((a) => a.appliesToType === 'revision' && a.appliesToId === rev.id),
    decisionDependencies: snap.conditions
      .filter((c) => c.parentType === 'revision' && c.parentId === rev.id && c.type === 'decision' && c.state === 'open')
      .map((c) => snap.decisions.find((x) => x.id === c.requiredRefId))
      .filter(Boolean),
  }

  // Distinct visible facts — never one merged flag (PEC-DEL-009, I-6)
  const workItems = rev == null ? [] : snap.workItems.filter((w) =>
    (w.anchorType === 'deliverable' && w.anchorId === id) || (w.anchorType === 'revision' && w.anchorId === rev.id))
  const approvals = rev == null ? [] : snap.approvalRecords.filter((a) => a.appliesToType === 'revision' && a.appliesToId === rev.id && a.state !== 'superseded')
  const facts = {
    workComplete: workItems.length > 0 && workItems.every((w) => w.state === 'closed' || w.state === 'cancelled'),
    checkAccepted: rev != null && snap.checks.some((c) => c.revisionId === rev.id && c.state === 'accepted'),
    approvalRecorded: approvals.length > 0 && approvals.every((a) => a.state === 'decided'),
    authorizedForIssue: rev?.state === 'approved' || rev?.state === 'issued',
    issued: rev != null && snap.issueEvents.some((e) => e.revisionId === rev.id),
    returnedWithComments: rev?.state === 'returned_with_comments',
    superseded: rev == null ? false : snap.revisions.some((r) => r.deliverableId === id && r.state === 'superseded'),
    archived: false, // P3
  }

  // Evidence trail: updates + attachments + history are one stream (PEC-DEL-005)
  const evidence = snap.evidence.filter((e) =>
    (e.recordType === 'deliverable' && e.recordId === id)
    || (rev != null && e.recordType === 'revision' && e.recordId === rev.id))
  const history = [
    ...sx.repo.historyFor(sx.projectId, 'deliverable', id, 100),
    ...(rev ? sx.repo.historyFor(sx.projectId, 'revision', rev.id, 100) : []),
  ].sort((a, b) => b.at.localeCompare(a.at)).slice(0, 150)

  // Before-this-issues panel (PEC-DEL-004): conditions on the issue gate of the current revision
  const beforeIssue = rev ? explainTransition(snap, 'revision', rev.id, 'revision.issue', { holdVeto: true }) : null
  const offered = rev ? transitionsFrom('revision', rev.state).filter((t) => !t.auto).map((t) => t.event) : []

  return {
    deliverable: d, workflow: workflowCompleteness(snap, d),
    health: redact(sx, snap, s.health), forecastSlipWd: s.forecastSlipWd,
    currentRevision: rev, revisionChain: chain, openItems, facts,
    beforeIssue, offeredTransitions: offered, evidence, history,
  }
}

// ---------- Action & Hold Log (PEC-AHL-001; review resolution 5) ----------

export interface LogFilters {
  log?: Log
  packageId?: number
  ownerId?: number
  type?: 'work_item' | 'hold' | 'interface_item' | 'intake_item'
  cause?: string
  overdue?: boolean
  anchored?: boolean
}

export function logRegisterView(sx: Sx, f: LogFilters): unknown {
  const snap = snapshot(sx)
  const logs = logsFor(sx, snap)
  const cal = snap.project.calendar
  const today = snap.today

  interface Row {
    recordType: string; id: number; ref: string; title: string; log: Log
    packageId: number | null; ownerId: number | null; state: string
    ageWd: number; needBy: string | null; overdue: boolean
    holdCause: string | null; anchorStatus: 'anchored' | 'unanchored'
  }
  const rows: Row[] = []

  for (const w of snap.workItems) {
    if (w.state !== 'open' && w.state !== 'in_work') continue
    rows.push({
      recordType: 'work_item', id: w.id, ref: w.ref, title: w.title, log: w.log,
      packageId: w.packageId, ownerId: w.ownerId, state: w.state,
      ageWd: ageWorkingDays(w.createdAt, today, cal), needBy: w.needBy,
      overdue: daysOverdue(w.needBy, today) > 0, holdCause: null, anchorStatus: 'anchored',
    })
  }
  for (const h of snap.holds) {
    if (h.state !== 'active') continue
    rows.push({
      recordType: 'hold', id: h.id, ref: h.ref, title: h.title, log: h.log,
      packageId: null, ownerId: h.ownerId, state: h.state,
      ageWd: ageWorkingDays(h.raisedAt, today, cal), needBy: h.needBy,
      overdue: daysOverdue(h.needBy, today) > 0, holdCause: h.cause, anchorStatus: 'anchored',
    })
  }
  for (const i of snap.interfaces) {
    if (i.state !== 'open' && i.state !== 'agreed') continue
    rows.push({
      recordType: 'interface_item', id: i.id, ref: i.ref, title: i.title, log: i.log,
      packageId: i.givingPackageId ?? i.receivingPackageId, ownerId: null, state: i.state,
      ageWd: 0, needBy: i.needBy, overdue: daysOverdue(i.needBy, today) > 0,
      holdCause: null, anchorStatus: 'anchored',
    })
  }
  for (const t of snap.intakeItems) {
    if (t.state === 'dispositioned') continue
    rows.push({
      recordType: 'intake_item', id: t.id, ref: t.ref, title: t.statementVerbatim.slice(0, 120), log: t.log,
      packageId: null, ownerId: t.suggestedOwnerId, state: t.state,
      ageWd: ageWorkingDays(t.raisedAt, today, cal), needBy: t.needBy,
      overdue: daysOverdue(t.needBy, today) > 0, holdCause: null,
      anchorStatus: 'unanchored', // I-2: flagged until triaged; excluded from plans/rollups
    })
  }

  let out = rows.filter((r) => logs.includes(r.log))
  if (f.log) out = out.filter((r) => r.log === f.log)
  if (f.packageId != null) out = out.filter((r) => r.packageId === f.packageId)
  if (f.ownerId != null) out = out.filter((r) => r.ownerId === f.ownerId)
  if (f.type) out = out.filter((r) => r.recordType === f.type)
  if (f.cause) out = out.filter((r) => r.holdCause === f.cause)
  if (f.overdue != null) out = out.filter((r) => r.overdue === f.overdue)
  if (f.anchored != null) out = out.filter((r) => (r.anchorStatus === 'anchored') === f.anchored)
  return out.sort((a, b) => b.ageWd - a.ageWd)
}

// ---------- My Week (PEC-MW-*) ----------

export function myWeekView(sx: Sx): unknown {
  const snap = snapshot(sx)
  return myWeek(snap, sx.session.personId)
}

// ---------- registers ----------

export function intakeQueueView(sx: Sx, state?: string): unknown {
  const snap = snapshot(sx)
  const logs = logsFor(sx, snap)
  const cal = snap.project.calendar
  return snap.intakeItems
    .filter((i) => logs.includes(i.log))
    .filter((i) => (state ? i.state === state : i.state !== 'dispositioned'))
    .map((i) => ({
      ...i,
      untriagedAgeWd: i.state === 'dispositioned' ? 0 : ageWorkingDays(i.raisedAt, snap.today, cal),
      links: (sx.repo.db.prepare('SELECT record_type, record_id FROM intake_link WHERE intake_id = ?')
        .all(i.id) as Array<{ record_type: string; record_id: number }>),
    }))
    .sort((a, b) => b.untriagedAgeWd - a.untriagedAgeWd)
}

export function approvalRegisterView(sx: Sx): unknown {
  const snap = snapshot(sx)
  const cal = snap.project.calendar
  return snap.approvalRecords.map((a) => ({
    ...a,
    latencyWd: a.readyAt ? ageWorkingDays(a.readyAt, snap.today, cal) : 0,
    outcome: a.outcomeDecisionId != null
      ? snap.decisions.find((d) => d.id === a.outcomeDecisionId)?.outcome ?? null
      : null,
    outcomeDecisionRef: a.outcomeDecisionId != null
      ? snap.decisions.find((d) => d.id === a.outcomeDecisionId)?.ref ?? null
      : null,
    prerequisites: snap.conditions
      .filter((c) => c.parentType === 'approval_record' && c.parentId === a.id)
      .map((c) => ({ ref: c.ref, description: c.description, state: c.state, severity: c.severity })),
  }))
}

export function decisionRegisterView(sx: Sx): unknown {
  const snap = snapshot(sx)
  const logs = logsFor(sx, snap)
  return snap.decisions
    .filter((d) => logs.includes(d.log))
    .map((d) => ({
      ...d,
      overdueDays: (d.state !== 'decided' && d.state !== 'superseded') ? daysOverdue(d.needBy, snap.today) : 0,
      links: snap.decisionLinks.filter((l) => l.decisionId === d.id),
    }))
}

export function riskRegisterView(sx: Sx): Risk[] {
  const snap = snapshot(sx)
  return snap.risks
}

/** Package Tracker register (§16 tracker contract, D-PEC-13): import-owned rows, read-only.
 *  Direct table read — tracker rows stay out of the snapshot by design. */
export function trackerRegisterView(sx: Sx): PackageTracker[] {
  return sx.repo.list<PackageTracker>('package_tracker', sx.projectId)
}

/** Dedicated interface register (PEC-INT-002, P2): aging + giving/receiving filters. */
export interface InterfaceFilters {
  givingPackageId?: number
  receivingPackageId?: number
  state?: string
}

export function interfaceRegisterView(sx: Sx, f: InterfaceFilters = {}): unknown {
  const snap = snapshot(sx)
  const logs = logsFor(sx, snap)
  const cal = snap.project.calendar
  const today = snap.today
  const th = snap.project.thresholds
  const pkgCode = (id: number | null): string | null => snap.packages.find((p) => p.id === id)?.code ?? null
  return snap.interfaces
    .filter((i) => logs.includes(i.log))
    .filter((i) => (f.givingPackageId ? i.givingPackageId === f.givingPackageId : true))
    .filter((i) => (f.receivingPackageId ? i.receivingPackageId === f.receivingPackageId : true))
    .filter((i) => (f.state ? i.state === f.state : true))
    .map((i) => {
      const open = i.state === 'open' || i.state === 'agreed'
      const overdueWd = open ? workingDaysOverdue(i.needBy, today, cal) : 0
      return {
        ...i,
        givingPackageCode: pkgCode(i.givingPackageId),
        receivingPackageCode: pkgCode(i.receivingPackageId),
        overdueWd,
        aging: overdueWd > th.interfaceOverdueRedWd ? 'red'
          : overdueWd > th.interfaceOverdueWarnWd ? 'warn' : 'none',
      }
    })
    .sort((a, b) => b.overdueWd - a.overdueWd || (a.needBy ?? '9999').localeCompare(b.needBy ?? '9999'))
}

export function holdRegisterView(sx: Sx, cause?: string): unknown {
  const snap = snapshot(sx)
  const logs = logsFor(sx, snap)
  const cal = snap.project.calendar
  return snap.holds
    .filter((h) => logs.includes(h.log))
    .filter((h) => (cause ? h.cause === cause : true))
    .map((h) => ({
      ...h,
      ageWd: ageWorkingDays(h.raisedAt, snap.today, cal),
      targets: snap.holdLinks.filter((l) => l.holdId === h.id)
        .map((l) => ({ targetType: l.targetType, targetId: l.targetId })),
    }))
}

export function workItemDetailView(sx: Sx, id: number): unknown {
  const snap = snapshot(sx)
  const w = snap.workItems.find((x) => x.id === id)
  if (!w) throw notFound(`work item #${id}`)
  const closeExplain = explainTransition(snap, 'work_item', w.id, 'work_item.close', { holdVeto: true })
  return {
    workItem: w,
    blockedBy: activeHoldsFor(snap, 'work_item', id).map((h) => ({ ref: h.ref, cause: h.cause, title: h.title, ownerId: h.ownerId, needBy: h.needBy })),
    closureConditions: closeExplain,
    offeredTransitions: transitionsFrom('work_item', w.state).filter((t) => !t.auto).map((t) => t.event),
    history: sx.repo.historyFor(sx.projectId, 'work_item', id, 100),
    evidence: snap.evidence.filter((e) => e.recordType === 'work_item' && e.recordId === id),
  }
}

export function checkDetailView(sx: Sx, id: number): unknown {
  const snap = snapshot(sx)
  const c = snap.checks.find((x) => x.id === id)
  if (!c) throw notFound(`check #${id}`)
  const rev = snap.revisions.find((r) => r.id === c.revisionId)
  const del = rev ? snap.deliverables.find((d) => d.id === rev.deliverableId) : null
  return {
    check: c, revision: rev, deliverable: del,
    comments: snap.reviewComments.filter((x) => x.checkId === id),
    // three distinct facts (PEC-CHK-003)
    facts: {
      checklistComplete: c.checklist.length > 0 && c.checklist.every((i) => i.done),
      commentsClosed: snap.reviewComments.filter((x) => x.checkId === id && commentIsOpen(x)).length === 0,
      checkerAccepted: c.state === 'accepted',
    },
    history: sx.repo.historyFor(sx.projectId, 'check', id, 100),
  }
}
