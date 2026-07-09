/**
 * Reporting periods & coverage declarations — read side (D-PEC-39).
 *
 * Coverage is DECLARED per uploaded document on the import-proposal lane
 * (services/proposals.ts) and never inferred. This module only reads: it
 * projects the declarations, CATCHES overlaps / gaps / undeclared applied
 * imports as review signals for the PE and agent (never schema-prevents them),
 * and computes period-scoped counts from timestamped app records where the
 * records support them. Every figure is Explain-shaped (I-4) and names its
 * coverage basis; a figure the records don't support is absent and said to be
 * absent (period honesty, WORKPLAN_2026-07-09 corollary).
 */

import type { ContributingRef, Explain, IntakeItem } from '@pec/core'
import { visibleLogs } from '@pec/core'
import { badRequest } from '../errors.ts'
import type { Sx } from './shared.ts'

const DATE_RE = /^\d{4}-\d{2}-\d{2}$/

export interface CoverageDeclarationRow {
  proposalId: number
  ref: string
  contract: string
  sourceName: string | null
  state: string
  coverageStart: string | null
  coverageEnd: string | null
  createdAt: string
  appliedAt: string | null
}

export interface CoverageReviewItem {
  kind: 'overlap' | 'gap' | 'undeclared'
  contract: string
  detail: string
  contributing: ContributingRef[]
}

export interface CoverageView {
  declarations: CoverageDeclarationRow[]
  signals: {
    overlaps: Explain<number>
    gaps: Explain<number>
    undeclaredApplied: Explain<number>
  }
  reviewItems: CoverageReviewItem[]
}

interface ProposalRow {
  id: number
  ref: string
  contract: string
  source_name: string | null
  state: string
  coverage_start: string | null
  coverage_end: string | null
  created_at: string
  applied_at: string | null
}

function proposalRows(sx: Sx): ProposalRow[] {
  return sx.db.prepare(
    `SELECT id, ref, contract, source_name, state, coverage_start, coverage_end, created_at, applied_at
     FROM import_proposal WHERE project_id = ? ORDER BY id`,
  ).all(sx.projectId) as unknown as ProposalRow[]
}

function covRef(p: ProposalRow, why: string): ContributingRef {
  return { recordType: 'import_proposal', id: p.id, ref: p.ref, why }
}

function shiftDay(isoDate: string, days: number): string {
  const d = new Date(`${isoDate}T00:00:00Z`)
  d.setUTCDate(d.getUTCDate() + days)
  return d.toISOString().slice(0, 10)
}
const nextDay = (isoDate: string): string => shiftDay(isoDate, 1)

/**
 * Coverage declarations + caught review signals (COV- rules). Read-only over
 * import_proposal metadata (no CSV content). Any project member may read the
 * APPLIED reporting basis — exactly what period figures cite — but draft/
 * rejected/pending proposal metadata stays behind the proposal lane's own
 * read gate (RV-16/RV-19): this view never widens it.
 */
export function coverageView(sx: Sx): CoverageView {
  const rows = proposalRows(sx).filter((p) => p.state === 'applied')
  const declarations: CoverageDeclarationRow[] = rows.map((p) => ({
    proposalId: p.id, ref: p.ref, contract: p.contract, sourceName: p.source_name,
    state: p.state, coverageStart: p.coverage_start, coverageEnd: p.coverage_end,
    createdAt: p.created_at, appliedAt: p.applied_at,
  }))

  const reviewItems: CoverageReviewItem[] = []
  const applied = rows.filter((p) => p.state === 'applied')

  // COV-UNDECLARED: applied imports with no declared coverage — period-scoped
  // report figures cannot cite them; the PE should re-declare on the next upload.
  const undeclared = applied.filter((p) => p.coverage_start == null)
  for (const p of undeclared) {
    reviewItems.push({
      kind: 'undeclared', contract: p.contract,
      detail: `${p.ref} (${p.contract}${p.source_name ? `, ${p.source_name}` : ''}) was applied without a coverage declaration`,
      contributing: [covRef(p, 'applied import with no declared coverage')],
    })
  }

  // Per contract, in applied order: overlaps (possible retroactive corrections)
  // and gaps between consecutive declared windows. Caught, never prevented.
  const contracts = [...new Set(applied.map((p) => p.contract))].sort()
  let overlapCount = 0
  let gapCount = 0
  const overlapRefs: ContributingRef[] = []
  const gapRefs: ContributingRef[] = []
  for (const contract of contracts) {
    const declared = applied
      .filter((p) => p.contract === contract && p.coverage_start != null && p.coverage_end != null)
      .sort((a, b) => a.coverage_start! < b.coverage_start! ? -1 : a.coverage_start! > b.coverage_start! ? 1 : a.id - b.id)
    for (let i = 0; i < declared.length; i++) {
      for (let j = i + 1; j < declared.length; j++) {
        const a = declared[i]!, b = declared[j]!
        if (b.coverage_start! <= a.coverage_end!) {
          overlapCount++
          const later = a.id > b.id ? a : b
          reviewItems.push({
            kind: 'overlap', contract,
            detail: `${a.ref} (${a.coverage_start}..${a.coverage_end}) and ${b.ref} (${b.coverage_start}..${b.coverage_end}) `
              + `declare overlapping ${contract} coverage — possible retroactive correction by ${later.ref}; review with the PE`,
            contributing: [covRef(a, 'earlier declared window in overlap'), covRef(b, 'later declared window in overlap')],
          })
          overlapRefs.push(covRef(a, `overlaps ${b.ref}`), covRef(b, `overlaps ${a.ref}`))
        }
      }
    }
    for (let i = 0; i + 1 < declared.length; i++) {
      const prev = declared[i]!, next = declared[i + 1]!
      if (next.coverage_start! > nextDay(prev.coverage_end!)) {
        gapCount++
        reviewItems.push({
          kind: 'gap', contract,
          detail: `no applied ${contract} coverage between ${nextDay(prev.coverage_end!)} and ${shiftDay(next.coverage_start!, -1)} `
            + `(${prev.ref} ends ${prev.coverage_end}; ${next.ref} starts ${next.coverage_start})`,
          contributing: [covRef(prev, 'window before the gap'), covRef(next, 'window after the gap')],
        })
        gapRefs.push(covRef(prev, 'window before a coverage gap'), covRef(next, 'window after a coverage gap'))
      }
    }
  }

  return {
    declarations,
    signals: {
      overlaps: {
        value: overlapCount, ruleId: 'COV-OVERLAP',
        detail: overlapCount === 0 ? 'no overlapping declared coverage windows among applied imports'
          : `${overlapCount} overlapping declared coverage window pair(s) among applied imports (possible retroactive corrections) — review with the PE`,
        contributing: overlapRefs,
      },
      gaps: {
        value: gapCount, ruleId: 'COV-GAP',
        detail: gapCount === 0 ? 'no gaps between consecutive declared coverage windows of applied imports'
          : `${gapCount} gap(s) between consecutive declared coverage windows of applied imports`,
        contributing: gapRefs,
      },
      undeclaredApplied: {
        value: undeclared.length, ruleId: 'COV-UNDECLARED',
        detail: undeclared.length === 0 ? 'every applied import declares its coverage'
          : `${undeclared.length} applied import(s) carry no coverage declaration; period-scoped figures cannot cite them`,
        contributing: undeclared.map((p) => covRef(p, 'applied import with no declared coverage')),
      },
    },
    reviewItems,
  }
}

// ---------- period-scoped counts (PER- rules) ----------

export interface PeriodStatusView {
  period: { start: string; end: string }
  coverageBasis: {
    declared: Explain<number>
    coveredContracts: string[]
  }
  figures: {
    issuances: Explain<number>
    issuanceDelta: Explain<number>
    workItemsClosed: Explain<number>
    holdsRaised: Explain<number>
    holdsResolved: Explain<number>
    decisionsDecided: Explain<number>
    intakeRaised: Explain<number>
  }
  absent: Array<{ figure: string; reason: string; needed: string }>
}

function inWindow(ts: string | null | undefined, start: string, end: string): boolean {
  if (!ts) return false
  const day = ts.slice(0, 10)
  return day >= start && day <= end
}

/**
 * Period-scoped counts from timestamped app records. The period itself is an
 * explicit request parameter — never silently inferred — and the response names
 * the applied coverage declarations that intersect it (PER-COV), so every figure
 * is traceable to both its records and its coverage basis.
 */
export function periodStatusView(sx: Sx, startRaw: string, endRaw: string): PeriodStatusView {
  if (!DATE_RE.test(startRaw) || !DATE_RE.test(endRaw)) {
    throw badRequest('period-status requires start and end as YYYY-MM-DD (D-PEC-39)')
  }
  if (endRaw < startRaw) throw badRequest(`period end ${endRaw} is before start ${startRaw}`)
  const start = startRaw
  const end = endRaw

  const snap = sx.repo.snapshot(sx.projectId)
  const logs = visibleLogs(sx.roles, snap.project.config.logVisibility)
  const seeAll = logs.length === 3
  const vis = <T extends { log: import('@pec/core').Log }>(rows: T[]): T[] =>
    seeAll ? rows : rows.filter((r) => logs.includes(r.log))

  // coverage basis: applied declarations intersecting the requested window
  const intersecting = proposalRows(sx).filter((p) => p.state === 'applied'
    && p.coverage_start != null && p.coverage_end != null
    && p.coverage_start <= end && p.coverage_end >= start)
  const coveredContracts = [...new Set(intersecting.map((p) => p.contract))].sort()

  // issuances: issue events recorded in the window (app records; ref via deliverable)
  const docNo = (revisionId: number): string => {
    const rev = snap.revisions.find((r) => r.id === revisionId)
    const d = rev ? snap.deliverables.find((x) => x.id === rev.deliverableId) : undefined
    return d?.docNo ?? `revision#${revisionId}`
  }
  const issued = snap.issueEvents.filter((e) => inWindow(e.issuedAt, start, end))
  // previous window of equal length, immediately before — computed from the same
  // timestamped records (not a snapshot model; broader deltas remain absent)
  const spanDays = Math.round((Date.parse(`${end}T00:00:00Z`) - Date.parse(`${start}T00:00:00Z`)) / 86400000) + 1
  const prevEnd = new Date(Date.parse(`${start}T00:00:00Z`) - 86400000).toISOString().slice(0, 10)
  const prevStart = new Date(Date.parse(prevEnd + 'T00:00:00Z') - (spanDays - 1) * 86400000).toISOString().slice(0, 10)
  const issuedPrev = snap.issueEvents.filter((e) => inWindow(e.issuedAt, prevStart, prevEnd))

  const closed = vis(snap.workItems).filter((w) => w.state === 'closed' && inWindow(w.closedAt, start, end))
  const holdsRaised = vis(snap.holds).filter((h) => inWindow(h.raisedAt, start, end))
  const holdsResolved = vis(snap.holds).filter((h) => inWindow(h.resolvedAt, start, end))
  const decided = vis(snap.decisions).filter((d) => d.state === 'decided' && inWindow(d.decidedAt, start, end))
  const intake = vis(snap.intakeItems as IntakeItem[]).filter((t) => inWindow(t.raisedAt, start, end))

  const covDetail = intersecting.length === 0
    ? `no applied import coverage declaration intersects ${start}..${end}; imported-register facts for this window may be incomplete`
    : `applied coverage declarations intersecting ${start}..${end}: ${intersecting.map((p) => `${p.ref} (${p.contract} ${p.coverage_start}..${p.coverage_end})`).join(', ')}`

  return {
    period: { start, end },
    coverageBasis: {
      declared: {
        value: intersecting.length, ruleId: 'PER-COV', detail: covDetail,
        contributing: intersecting.map((p) => covRef(p, 'applied coverage declaration intersecting the requested period')),
      },
      coveredContracts,
    },
    figures: {
      issuances: {
        value: issued.length, ruleId: 'PER-ISSUED',
        detail: `issue events recorded ${start}..${end} (issue_event.issued_at)`,
        contributing: issued.map((e) => ({ recordType: 'issue_event' as const, id: e.id, ref: e.ref, why: `${docNo(e.revisionId)} issued ${e.issuedAt.slice(0, 10)} (${e.purpose})` })),
      },
      issuanceDelta: {
        value: issued.length - issuedPrev.length, ruleId: 'PER-ISSUED-DELTA',
        detail: `issuances ${start}..${end} (${issued.length}) minus the preceding equal window ${prevStart}..${prevEnd} (${issuedPrev.length}); computed from timestamped issue events, not a snapshot model`,
        contributing: [
          ...issued.map((e) => ({ recordType: 'issue_event' as const, id: e.id, ref: e.ref, why: 'issued in the requested window' })),
          ...issuedPrev.map((e) => ({ recordType: 'issue_event' as const, id: e.id, ref: e.ref, why: 'issued in the preceding window' })),
        ],
      },
      workItemsClosed: {
        value: closed.length, ruleId: 'PER-CLOSED',
        detail: `work items closed ${start}..${end} (work_item.closed_at), visibility-filtered per log`,
        contributing: closed.map((w) => ({ recordType: 'work_item' as const, id: w.id, ref: w.ref, why: `closed ${w.closedAt?.slice(0, 10)}` })),
      },
      holdsRaised: {
        value: holdsRaised.length, ruleId: 'PER-HOLD-RAISED',
        detail: `holds raised ${start}..${end} (hold.raised_at), visibility-filtered per log`,
        contributing: holdsRaised.map((h) => ({ recordType: 'hold' as const, id: h.id, ref: h.ref, why: `raised ${h.raisedAt.slice(0, 10)}` })),
      },
      holdsResolved: {
        value: holdsResolved.length, ruleId: 'PER-HOLD-RESOLVED',
        detail: `holds resolved ${start}..${end} (hold.resolved_at), visibility-filtered per log`,
        contributing: holdsResolved.map((h) => ({ recordType: 'hold' as const, id: h.id, ref: h.ref, why: `resolved ${h.resolvedAt?.slice(0, 10)}` })),
      },
      decisionsDecided: {
        value: decided.length, ruleId: 'PER-DECIDED',
        detail: `decisions decided ${start}..${end} (decision.decided_at), visibility-filtered per log`,
        contributing: decided.map((d) => ({ recordType: 'decision' as const, id: d.id, ref: d.ref, why: `decided ${d.decidedAt?.slice(0, 10)}` })),
      },
      intakeRaised: {
        value: intake.length, ruleId: 'PER-INTAKE',
        detail: `intake items raised ${start}..${end} (intake_item.raised_at), visibility-filtered per log`,
        contributing: intake.map((t) => ({ recordType: 'intake_item' as const, id: t.id, ref: t.ref, why: `raised ${t.raisedAt.slice(0, 10)}` })),
      },
    },
    absent: [
      {
        figure: 'percent complete (period-scoped or otherwise)',
        reason: 'PE-attested percent-complete ingestion is not ruled or implemented yet',
        needed: 'MDL/RAIL contract v2 packet (Tier-P revised templates)',
      },
      {
        figure: 'week-over-week deltas beyond issuances',
        reason: 'no period snapshot model exists; only deltas computable from timestamped records (PER-ISSUED-DELTA) are provided',
        needed: 'future period-snapshot tranche if ruled',
      },
    ],
  }
}
