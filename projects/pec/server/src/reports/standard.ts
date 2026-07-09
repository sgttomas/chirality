import { projectStatus, workflowCompleteness } from '@pec/core'
import type { ContributingRef, Deliverable, ProjectSnapshot } from '@pec/core'
import { badRequest } from '../errors.ts'
import type { Sx } from '../services/shared.ts'

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

const baseAbsent = [
  {
    figure: 'issued this period',
    reason: 'no reporting-period/coverage declaration model is ruled or implemented yet',
    needed: 'future reporting periods packet',
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

function issueCountsForPackage(snap: ProjectSnapshot, packageId: number): {
  holds: number
  decisions: number
  risks: number
  actions: number
  contributing: ContributingRef[]
} {
  const deliverableIds = new Set(snap.deliverables.filter((d) => d.packageId === packageId).map((d) => d.id))
  const revisionIds = new Set(snap.revisions.filter((r) => deliverableIds.has(r.deliverableId)).map((r) => r.id))
  const workIds = new Set(snap.workItems.filter((w) => w.packageId === packageId || deliverableIds.has(w.anchorId)).map((w) => w.id))
  const holds = snap.holds.filter((h) => h.state === 'active'
    && snap.holdLinks.some((l) =>
      (l.targetType === 'deliverable' && deliverableIds.has(l.targetId))
      || (l.targetType === 'revision' && revisionIds.has(l.targetId))
      || (l.targetType === 'work_item' && workIds.has(l.targetId))))
  const decisions = snap.decisions.filter((d) => d.packageId === packageId
    && d.state !== 'decided' && d.state !== 'superseded')
  const risks = snap.risks.filter((r) => (r.packageId === packageId || (r.deliverableId != null && deliverableIds.has(r.deliverableId)))
    && r.state !== 'closed')
  const actions = snap.workItems.filter((w) => w.packageId === packageId
    && (w.state === 'open' || w.state === 'in_work'))
  return {
    holds: holds.length,
    decisions: decisions.length,
    risks: risks.length,
    actions: actions.length,
    contributing: [
      ...holds.map((h) => ref('hold', h.id, h.ref, 'active hold linked to this package')),
      ...decisions.map((d) => ref('decision', d.id, d.ref, 'open package decision')),
      ...risks.map((r) => ref('risk', r.id, r.ref, 'open package risk')),
      ...actions.map((w) => ref('work_item', w.id, w.ref, 'open package action')),
    ],
  }
}

function weeklyProjectStatus(sx: Sx, groupBy: WeeklyGroupBy): StandardReport {
  const snap = sx.repo.snapshot(sx.projectId)
  const status = projectStatus(snap)
  const activeHolds = snap.holds.filter((h) => h.state === 'active')
  const openRisks = snap.risks.filter((r) => r.state !== 'closed')
  const openActions = snap.workItems.filter((w) => w.state === 'open' || w.state === 'in_work')
  const openDecisions = snap.decisions.filter((d) => d.state !== 'decided' && d.state !== 'superseded')
  const groups = groupBy === 'package'
    ? snap.packages.map((pkg) => {
      const deliverables = snap.deliverables.filter((d) => d.packageId === pkg.id)
      const issues = issueCountsForPackage(snap, pkg.id)
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
      return {
        key: discipline,
        label: discipline,
        activities: deliverables.filter((d) => workflowCompleteness(snap, d).currentState !== 'issued')
          .map((d) => ({ docNo: d.docNo, title: d.title, type: d.deliverableType, workflow: workflowCompleteness(snap, d).label })),
        issues: {
          holds: activeHolds.filter((h) => snap.holdLinks.some((l) => l.targetType === 'deliverable' && delIds.has(l.targetId))).length,
          decisions: openDecisions.filter((d) => d.packageId != null
            && snap.deliverables.some((del) => del.packageId === d.packageId && delIds.has(del.id))).length,
          risks: openRisks.filter((r) => r.deliverableId != null && delIds.has(r.deliverableId)).length,
          actions: openActions.filter((w) => w.anchorType === 'deliverable' && delIds.has(w.anchorId)).length,
          contributing: deliverableRefs(deliverables, 'discipline report group source deliverable'),
        },
      }
    })
  const sections = {
    groupBy,
    projectHealth: status.health,
    kpis: status.kpis,
    groups,
    totals: {
      deliverables: snap.deliverables.length,
      activeHolds: activeHolds.length,
      openRisks: openRisks.length,
      openActions: openActions.length,
      openDecisions: openDecisions.length,
    },
  }
  return {
    name: 'weekly-project-status',
    title: `Weekly project status (${groupBy})`,
    generatedForProject: projectInfo(snap),
    basis: [
      { route: `/api/projects/${sx.projectId}/overview`, source: 'projectStatus(snap)', ruleId: status.health.ruleId, contributing: status.health.contributing },
      { route: `/api/projects/${sx.projectId}/log-summary`, source: 'active holds/actions/risks from project snapshot', contributing: [
        ...activeHolds.map((h) => ref('hold', h.id, h.ref, 'active hold counted in weekly status')),
        ...openRisks.map((r) => ref('risk', r.id, r.ref, 'open risk counted in weekly status')),
        ...openActions.map((w) => ref('work_item', w.id, w.ref, 'open action counted in weekly status')),
      ] },
    ],
    absent: baseAbsent,
    sections,
    markdown: [
      `# Weekly project status (${groupBy})`,
      `Project health: ${status.health.value} (${status.health.ruleId}) - ${status.health.detail}`,
      `Totals: ${snap.deliverables.length} deliverables; ${activeHolds.length} active holds; ${openDecisions.length} open decisions; ${openRisks.length} open risks.`,
      ...groups.map((g) => `## ${g.label}\nActivities in work: ${g.activities.length}\nIssues: holds ${g.issues.holds}, decisions ${g.issues.decisions}, risks ${g.issues.risks}, actions ${g.issues.actions}`),
      'Absent: period-scoped issuances, percent complete, and week-over-week deltas are not available until their ruled tranches land.',
    ].join('\n\n'),
  }
}

function packageIssueSummary(sx: Sx): StandardReport {
  const snap = sx.repo.snapshot(sx.projectId)
  const rows = snap.packages.map((pkg) => ({ package: { id: pkg.id, code: pkg.code, name: pkg.name }, ...issueCountsForPackage(snap, pkg.id) }))
  return {
    name: 'package-issue-summary',
    title: 'Package issue summary',
    generatedForProject: projectInfo(snap),
    basis: [{
      route: `/api/projects/${sx.projectId}/packages`,
      source: 'packageDetailView issue categories plus logSummaryView-compatible snapshot filters',
      contributing: rows.flatMap((r) => r.contributing),
    }],
    absent: [{
      figure: 'client/internal needs split',
      reason: 'needs typing is not ruled or implemented yet',
      needed: 'future needs internal/client typing packet',
    }],
    sections: { packages: rows },
    markdown: [
      '# Package issue summary',
      ...rows.map((r) => `${r.package.code}: holds ${r.holds}, decisions ${r.decisions}, risks ${r.risks}, actions ${r.actions}`),
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

export function standardReport(sx: Sx, name: string, groupByRaw?: string | null): StandardReport {
  if (!(REPORTS as readonly string[]).includes(name)) {
    throw badRequest(`unknown standard report: ${name} (${REPORTS.join(', ')})`)
  }
  const groupBy = groupByRaw === 'discipline' ? 'discipline' : 'package'
  switch (name as StandardReportName) {
    case 'weekly-project-status': return weeklyProjectStatus(sx, groupBy)
    case 'package-issue-summary': return packageIssueSummary(sx)
    case 'deliverable-completeness': return deliverableCompleteness(sx)
  }
}
