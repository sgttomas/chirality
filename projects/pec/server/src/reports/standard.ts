import { projectStatus, visibleLogs, workflowCompleteness } from '@pec/core'
import type { ContributingRef, Deliverable, Explain, Log, ProjectSnapshot } from '@pec/core'
import { badRequest } from '../errors.ts'
import type { Sx } from '../services/shared.ts'
import { periodStatusView } from '../services/periods.ts'
import type { PeriodStatusView } from '../services/periods.ts'

export type StandardReportName = 'weekly-project-status' | 'package-issue-summary' | 'deliverable-completeness'
export type WeeklyGroupBy = 'package' | 'discipline'

export interface ReportBasis {
  route: string
  source: string
  ruleId?: string
  contributing: ContributingRef[]
}

export interface StandardReport {
  name: StandardReportName
  title: string
  generatedForProject: { id: number; code: string; name: string; today: string }
  basis: ReportBasis[]
  absent: Array<{ figure: string; reason: string; needed: string }>
  sections: Record<string, unknown>
  markdown: string
}

const REPORTS = ['weekly-project-status', 'package-issue-summary', 'deliverable-completeness'] as const

function ref(recordType: ContributingRef['recordType'], id: number, recordRef: string, why: string): ContributingRef {
  return { recordType, id, ref: recordRef, why }
}

function projectInfo(snap: ProjectSnapshot): StandardReport['generatedForProject'] {
  return { id: snap.project.id, code: snap.project.code, name: snap.project.name, today: snap.today }
}

function packageCode(snap: ProjectSnapshot, id: number | null): string {
  return snap.packages.find((p) => p.id === id)?.code ?? 'unassigned'
}

function deliverableRefs(rows: Deliverable[], why: string): ContributingRef[] {
  return rows.map((d) => ref('deliverable', d.id, d.docNo, why))
}

function logsFor(sx: Sx, snap: ProjectSnapshot): Log[] {
  return visibleLogs(sx.roles, snap.project.config.logVisibility)
}

function visibleByLog<T extends { log: Log }>(sx: Sx, snap: ProjectSnapshot, rows: T[]): T[] {
  const logs = logsFor(sx, snap)
  if (logs.length === 3) return rows
  return rows.filter((r) => logs.includes(r.log))
}

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

function redact<T>(sx: Sx, snap: ProjectSnapshot, explain: Explain<T>): Explain<T> {
  return { ...explain, contributing: redactRefs(sx, snap, explain.contributing) }
}

const baseAbsent = [
  {
    figure: 'issued this period',
    reason: 'no period was declared for this report; period-scoped figures are computed only for an explicitly requested window (D-PEC-39)',
    needed: 'pass period_start/period_end (YYYY-MM-DD) — coverage declarations arrive per uploaded document',
  },
  {
    figure: 'percent complete',
    reason: 'PE-attested percent-complete ingestion is not ruled or implemented yet',
    needed: 'future MDL/RAIL contract v2 packet',
  },
  {
    figure: 'week-over-week deltas',
    reason: 'no period snapshot model is ruled or implemented yet',
    needed: 'future reporting periods packet',
  },
]

function issueCountsForPackage(sx: Sx, snap: ProjectSnapshot, packageId: number): {
  clientIssues: number
  holds: number
  interfaces: number
  decisions: number
  risks: number
  actions: number
  needsSplit: { internal: number; client: number; unclassified: number }
  contributing: ContributingRef[]
  operationalContributing: ContributingRef[]
} {
  const deliverableIds = new Set(snap.deliverables.filter((d) => d.packageId === packageId).map((d) => d.id))
  const revisionIds = new Set(snap.revisions.filter((r) => deliverableIds.has(r.deliverableId)).map((r) => r.id))
  const workIds = new Set(visibleByLog(sx, snap, snap.workItems)
    .filter((w) => w.packageId === packageId
      || (w.anchorType === 'deliverable' && deliverableIds.has(w.anchorId))
      || (w.anchorType === 'revision' && revisionIds.has(w.anchorId)))
    .map((w) => w.id))
  const holds = visibleByLog(sx, snap, snap.holds).filter((h) => h.state === 'active'
    && snap.holdLinks.some((l) =>
      l.holdId === h.id && (
        (l.targetType === 'deliverable' && deliverableIds.has(l.targetId))
      || (l.targetType === 'revision' && revisionIds.has(l.targetId))
      || (l.targetType === 'work_item' && workIds.has(l.targetId)))))
  const decisions = visibleByLog(sx, snap, snap.decisions).filter((d) => d.packageId === packageId
    && d.state !== 'decided' && d.state !== 'superseded')
  const interfaces = visibleByLog(sx, snap, snap.interfaces).filter((i) =>
    (i.givingPackageId === packageId || i.receivingPackageId === packageId) && (i.state === 'open' || i.state === 'agreed'))
  const risks = snap.risks.filter((r) => (r.packageId === packageId || (r.deliverableId != null && deliverableIds.has(r.deliverableId)))
    && r.state !== 'closed')
  const actions = visibleByLog(sx, snap, snap.workItems).filter((w) => w.packageId === packageId
    && (w.state === 'open' || w.state === 'in_work'))
  const clientContributing = [
    ...holds.map((h) => ref('hold', h.id, h.ref, 'active hold linked to this package')),
    ...risks.map((r) => ref('risk', r.id, r.ref, 'open package risk')),
    ...actions.map((w) => ref('work_item', w.id, w.ref, 'open package action')),
  ]
  const needRows = [...holds, ...actions]
  return {
    clientIssues: holds.length + risks.length + actions.length,
    holds: holds.length,
    interfaces: interfaces.length,
    decisions: decisions.length,
    risks: risks.length,
    actions: actions.length,
    needsSplit: {
      internal: needRows.filter((r) => r.needsAudience === 'internal').length,
      client: needRows.filter((r) => r.needsAudience === 'client').length,
      unclassified: needRows.filter((r) => r.needsAudience == null).length,
    },
    contributing: clientContributing,
    operationalContributing: [
      ...clientContributing,
      ...interfaces.map((i) => ref('interface_item', i.id, i.ref, 'open package interface relationship')),
      ...decisions.map((d) => ref('decision', d.id, d.ref, 'open package decision')),
    ],
  }
}

function isOnHoldText(v: unknown): boolean {
  return typeof v === 'string' && v.trim().toLowerCase().replaceAll(' ', '_').replaceAll('-', '_') === 'on_hold'
}

function mdlRailHoldDiscrepancies(sx: Sx, snap: ProjectSnapshot): Array<{
  key: string
  package: string
  direction: 'mdl_without_rail' | 'rail_without_mdl'
  detail: string
  contributing: ContributingRef[]
}> {
  const logs = logsFor(sx, snap)
  const mdl = snap.deliverables.filter((d) => isOnHoldText(d.workingStatus))
  const rail = visibleByLog(sx, snap, snap.workItems).filter((w) => isOnHoldText(w.sourcePayload?.status))
  const mdlByPkg = new Map<number, Deliverable[]>()
  for (const d of mdl) mdlByPkg.set(d.packageId, [...(mdlByPkg.get(d.packageId) ?? []), d])
  const railByPkg = new Map<number, typeof rail>()
  for (const w of rail) {
    if (w.packageId == null || !logs.includes(w.log)) continue
    railByPkg.set(w.packageId, [...(railByPkg.get(w.packageId) ?? []), w])
  }
  const pkgLabel = (id: number): string => snap.packages.find((p) => p.id === id)?.code ?? `package#${id}`
  const rows: ReturnType<typeof mdlRailHoldDiscrepancies> = []
  for (const [pkgId, dels] of mdlByPkg) {
    if ((railByPkg.get(pkgId) ?? []).length > 0) continue
    rows.push({
      key: `${pkgLabel(pkgId)}:mdl-on-hold-without-rail`,
      package: pkgLabel(pkgId),
      direction: 'mdl_without_rail',
      detail: `${dels.length} MDL deliverable(s) have working_status On Hold, but no visible RAIL v2 package issue has source status On Hold.`,
      contributing: dels.map((d) => ref('deliverable', d.id, d.docNo, 'MDL working_status is On Hold')),
    })
  }
  for (const [pkgId, items] of railByPkg) {
    if ((mdlByPkg.get(pkgId) ?? []).length > 0) continue
    rows.push({
      key: `${pkgLabel(pkgId)}:rail-on-hold-without-mdl`,
      package: pkgLabel(pkgId),
      direction: 'rail_without_mdl',
      detail: `${items.length} RAIL v2 issue(s) have source status On Hold, but no MDL deliverable in the package has working_status On Hold.`,
      contributing: items.map((w) => ref('work_item', w.id, w.ref, 'RAIL source status is On Hold')),
    })
  }
  return rows
}

/**
 * D-PEC-39: a weekly report may carry an explicitly declared period. The period is a
 * request parameter (never inferred); the payload then includes period-scoped issuance
 * figures computed from timestamped issue events, and names the applied coverage
 * declarations intersecting the window (PER-COV). Without a period, the period-scoped
 * absent entries stand unchanged.
 */
export interface ReportPeriodInput {
  start?: string | null
  end?: string | null
}

function resolvePeriod(period: ReportPeriodInput | undefined): { start: string; end: string } | null {
  const start = period?.start || null
  const end = period?.end || null
  if (start == null && end == null) return null
  if (start == null || end == null) {
    throw badRequest('a report period requires both period_start and period_end (D-PEC-39)')
  }
  return { start, end } // shape/order validation happens in periodStatusView
}

function weeklyProjectStatus(sx: Sx, groupBy: WeeklyGroupBy, period: { start: string; end: string } | null): StandardReport {
  const snap = sx.repo.snapshot(sx.projectId)
  const status = projectStatus(snap)
  const activeHolds = visibleByLog(sx, snap, snap.holds).filter((h) => h.state === 'active')
  const openRisks = snap.risks.filter((r) => r.state !== 'closed')
  const openActions = visibleByLog(sx, snap, snap.workItems).filter((w) => w.state === 'open' || w.state === 'in_work')
  const openDecisions = visibleByLog(sx, snap, snap.decisions).filter((d) => d.state !== 'decided' && d.state !== 'superseded')
  const visibleInterfaces = visibleByLog(sx, snap, snap.interfaces).filter((i) => i.state === 'open' || i.state === 'agreed')
  const consistency = mdlRailHoldDiscrepancies(sx, snap)
  const kpis = {
    pctOnPlan: redact(sx, snap, status.kpis.pctOnPlan),
    holdsByCause: redact(sx, snap, status.kpis.holdsByCause),
    openDecisions: redact(sx, snap, status.kpis.openDecisions),
    approvalsInFlight: redact(sx, snap, status.kpis.approvalsInFlight),
    scheduleForecastWd: redact(sx, snap, status.kpis.scheduleForecastWd),
  }
  const groups = groupBy === 'package'
    ? snap.packages.map((pkg) => {
      const deliverables = snap.deliverables.filter((d) => d.packageId === pkg.id)
      const issues = issueCountsForPackage(sx, snap, pkg.id)
      return {
        key: pkg.code,
        label: `${pkg.code} - ${pkg.name}`,
        activities: deliverables.filter((d) => workflowCompleteness(snap, d).currentState !== 'issued')
          .map((d) => ({ docNo: d.docNo, title: d.title, type: d.deliverableType, workflow: workflowCompleteness(snap, d).label })),
        issues,
      }
    })
    : [...new Set(snap.deliverables.map((d) => d.discipline ?? 'Unspecified'))].sort().map((discipline) => {
      const deliverables = snap.deliverables.filter((d) => (d.discipline ?? 'Unspecified') === discipline)
      const delIds = new Set(deliverables.map((d) => d.id))
      const disciplineHolds = activeHolds.filter((h) => snap.holdLinks.some((l) => l.holdId === h.id && l.targetType === 'deliverable' && delIds.has(l.targetId)))
      const disciplineActions = openActions.filter((w) => w.anchorType === 'deliverable' && delIds.has(w.anchorId))
      const needRows = [...disciplineHolds, ...disciplineActions]
      return {
        key: discipline,
        label: discipline,
        activities: deliverables.filter((d) => workflowCompleteness(snap, d).currentState !== 'issued')
          .map((d) => ({ docNo: d.docNo, title: d.title, type: d.deliverableType, workflow: workflowCompleteness(snap, d).label })),
        issues: {
          holds: disciplineHolds.length,
          decisions: openDecisions.filter((d) => d.packageId != null
            && snap.deliverables.some((del) => del.packageId === d.packageId && delIds.has(del.id))).length,
          interfaces: visibleInterfaces.filter((i) =>
            snap.deliverables.some((del) => delIds.has(del.id) && (del.packageId === i.givingPackageId || del.packageId === i.receivingPackageId))).length,
          risks: openRisks.filter((r) => r.deliverableId != null && delIds.has(r.deliverableId)).length,
          actions: disciplineActions.length,
          needsSplit: {
            internal: needRows.filter((r) => r.needsAudience === 'internal').length,
            client: needRows.filter((r) => r.needsAudience === 'client').length,
            unclassified: needRows.filter((r) => r.needsAudience == null).length,
          },
          contributing: deliverableRefs(deliverables, 'discipline report group source deliverable'),
        },
      }
    })
  // period enrichment: only where a factual period basis exists (D-PEC-39)
  const periodStatus: PeriodStatusView | null = period ? periodStatusView(sx, period.start, period.end) : null
  const sections = {
    groupBy,
    projectHealth: redact(sx, snap, status.health),
    kpis,
    groups,
    ...(periodStatus ? {
      period: periodStatus.period,
      periodCoverage: periodStatus.coverageBasis,
      issuancesThisPeriod: periodStatus.figures.issuances,
      issuanceDelta: periodStatus.figures.issuanceDelta,
    } : {}),
    totals: {
      deliverables: snap.deliverables.length,
      activeHolds: activeHolds.length,
      openRisks: openRisks.length,
      openActions: openActions.length,
      openDecisions: openDecisions.length,
      openInterfaces: visibleInterfaces.length,
    },
    consistencyChecks: {
      mdlRailHoldDiscrepancies: {
        count: consistency.length,
        ruleId: 'CONSIST-MDL-RAIL-HOLD',
        detail: 'Report-only check: compares MDL working_status On Hold against visible RAIL v2 source status On Hold by package; no intake or disposition records are created.',
        rows: consistency,
      },
    },
  }
  return {
    name: 'weekly-project-status',
    title: `Weekly project status (${groupBy})`,
    generatedForProject: projectInfo(snap),
    basis: [
      { route: `/api/projects/${sx.projectId}/overview`, source: 'projectStatus(snap)', ruleId: status.health.ruleId, contributing: redactRefs(sx, snap, status.health.contributing) },
      { route: `/api/projects/${sx.projectId}/log-summary`, source: 'active holds/actions/risks from project snapshot', contributing: [
        ...activeHolds.map((h) => ref('hold', h.id, h.ref, 'active hold counted in weekly status')),
        ...openRisks.map((r) => ref('risk', r.id, r.ref, 'open risk counted in weekly status')),
        ...openActions.map((w) => ref('work_item', w.id, w.ref, 'open action counted in weekly status')),
      ] },
      ...(periodStatus ? [{
        route: `/api/projects/${sx.projectId}/period-status?start=${periodStatus.period.start}&end=${periodStatus.period.end}`,
        source: 'periodStatusView (PER-ISSUED / PER-ISSUED-DELTA); coverage basis PER-COV',
        ruleId: 'PER-COV',
        contributing: periodStatus.coverageBasis.declared.contributing,
      }] : []),
      ...(consistency.length > 0 ? [{
        route: `/api/projects/${sx.projectId}/reports/standard/weekly-project-status`,
        source: 'report-only MDL working_status On Hold vs RAIL v2 source status On Hold comparison by package',
        ruleId: 'CONSIST-MDL-RAIL-HOLD',
        contributing: consistency.flatMap((r) => r.contributing),
      }] : []),
    ],
    absent: periodStatus
      ? [
        baseAbsent[1]!, // percent complete: still absent until contract v2
        {
          figure: 'week-over-week deltas beyond issuances',
          reason: 'no period snapshot model exists; only the issuance delta computable from timestamped issue events (PER-ISSUED-DELTA) is provided',
          needed: 'future period-snapshot tranche if ruled',
        },
      ]
      : baseAbsent,
    sections,
    markdown: [
      `# Weekly project status (${groupBy})`,
      ...(periodStatus ? [`Period: ${periodStatus.period.start} to ${periodStatus.period.end} — ${periodStatus.coverageBasis.declared.detail}`] : []),
      `Project health: ${status.health.value} (${status.health.ruleId}) - ${status.health.detail}`,
      `Totals: ${snap.deliverables.length} deliverables; ${activeHolds.length + openRisks.length + openActions.length} client-facing issues; ${activeHolds.length} active holds; ${openDecisions.length} open decisions; ${visibleInterfaces.length} open interfaces.`,
      ...(periodStatus ? [`Issuances this period: ${periodStatus.figures.issuances.value} (${periodStatus.figures.issuances.ruleId}); delta vs preceding equal window: ${periodStatus.figures.issuanceDelta.value >= 0 ? '+' : ''}${periodStatus.figures.issuanceDelta.value} (${periodStatus.figures.issuanceDelta.ruleId}).`] : []),
      ...groups.map((g) => `## ${g.label}\nActivities in work: ${g.activities.length}\nIssues: holds ${g.issues.holds}, risks ${g.issues.risks}, actions ${g.issues.actions}\nNeeds split: internal ${g.issues.needsSplit.internal}, client ${g.issues.needsSplit.client}, unclassified ${g.issues.needsSplit.unclassified}\nDecisions: ${g.issues.decisions}${'interfaces' in g.issues ? `\nInterfaces: ${g.issues.interfaces}` : ''}`),
      consistency.length > 0
        ? `MDL/RAIL hold discrepancies (${consistency.length}): ${consistency.map((r) => r.key).join(', ')}`
        : 'MDL/RAIL hold discrepancies: none surfaced by the report-only check.',
      periodStatus
        ? 'Absent: percent complete and week-over-week deltas beyond issuances are not available until their ruled tranches land.'
        : 'Absent: period-scoped issuances, percent complete, and week-over-week deltas are not available until their ruled tranches land.',
    ].join('\n\n'),
  }
}

function packageIssueSummary(sx: Sx): StandardReport {
  const snap = sx.repo.snapshot(sx.projectId)
  const rows = snap.packages.map((pkg) => ({ package: { id: pkg.id, code: pkg.code, name: pkg.name }, ...issueCountsForPackage(sx, snap, pkg.id) }))
  return {
    name: 'package-issue-summary',
    title: 'Package issues, decisions, and interfaces summary',
    generatedForProject: projectInfo(snap),
    basis: [{
      route: `/api/projects/${sx.projectId}/packages`,
      source: 'packageDetailView client-facing issue categories plus segregated decisions/interfaces',
      contributing: rows.flatMap((r) => r.operationalContributing),
    }],
    absent: rows.some((r) => r.needsSplit.unclassified > 0) ? [{
      figure: 'fully classified internal/client needs split',
      reason: 'some open hold/action issue rows do not carry an explicit imported needs_audience value',
      needed: 'an imported internal/client classification column for each open need row',
    }] : [],
    sections: { packages: rows },
    markdown: [
      '# Package issues, decisions, and interfaces summary',
      ...rows.map((r) => `${r.package.code}: issues ${r.clientIssues} (holds ${r.holds}, risks ${r.risks}, actions ${r.actions}); needs internal ${r.needsSplit.internal}, client ${r.needsSplit.client}, unclassified ${r.needsSplit.unclassified}; decisions ${r.decisions}; interfaces ${r.interfaces}`),
    ].join('\n'),
  }
}

function deliverableCompleteness(sx: Sx): StandardReport {
  const snap = sx.repo.snapshot(sx.projectId)
  const rows = snap.deliverables.map((d) => {
    const workflow = workflowCompleteness(snap, d)
    return {
      id: d.id,
      docNo: d.docNo,
      title: d.title,
      package: packageCode(snap, d.packageId),
      discipline: d.discipline,
      deliverableType: d.deliverableType,
      dueDate: d.dueDate,
      workflow,
      basis: ref('deliverable', d.id, d.docNo, 'deliverable workflow completeness source'),
    }
  })
  const byWorkflow = rows.reduce<Record<string, number>>((acc, row) => {
    acc[row.workflow.label] = (acc[row.workflow.label] ?? 0) + 1
    return acc
  }, {})
  return {
    name: 'deliverable-completeness',
    title: 'Deliverable completeness / MDL status',
    generatedForProject: projectInfo(snap),
    basis: [{
      route: `/api/projects/${sx.projectId}/deliverables?view=master`,
      source: 'deliverablesView + workflowCompleteness(snap, deliverable)',
      contributing: rows.map((r) => r.basis),
    }],
    absent: [{
      figure: 'PE-attested percent complete',
      reason: 'the current MDL contract has no percent-complete source column',
      needed: 'future MDL/RAIL contract v2 packet',
    }],
    sections: { byWorkflow, deliverables: rows },
    markdown: [
      '# Deliverable completeness / MDL status',
      ...Object.entries(byWorkflow).map(([label, count]) => `${label}: ${count}`),
      '',
      ...rows.map((r) => `${r.docNo}: ${r.workflow.label} (${r.workflow.gatesClosed}/${r.workflow.gatesTotal} gates) - ${r.title}`),
    ].join('\n'),
  }
}

export function standardReport(sx: Sx, name: string, groupByRaw?: string | null, periodRaw?: ReportPeriodInput): StandardReport {
  if (!(REPORTS as readonly string[]).includes(name)) {
    throw badRequest(`unknown standard report: ${name} (${REPORTS.join(', ')})`)
  }
  const groupBy = groupByRaw === 'discipline' ? 'discipline' : 'package'
  const period = resolvePeriod(periodRaw)
  if (period && name !== 'weekly-project-status') {
    // refuse rather than accept-and-ignore: a caller passing a period must not
    // believe an unscoped report was period-scoped (period honesty, D-PEC-39)
    throw badRequest(`report ${name} does not support a period; only weekly-project-status is period-scopable`)
  }
  switch (name as StandardReportName) {
    case 'weekly-project-status': return weeklyProjectStatus(sx, groupBy, period)
    case 'package-issue-summary': return packageIssueSummary(sx)
    case 'deliverable-completeness': return deliverableCompleteness(sx)
  }
}
