/**
 * The act/tool layer both engines drive (D-PEC-17). Every fact in an ActResult
 * comes from an API response in the same turn (F-PEC-2 — the engine formats,
 * never invents). Guards owned here:
 *
 * - D-T0-20 O-B enumeration clamp, keyed on the engine's egress class AND the
 *   D-T0-21 O-B access basis: under 'model-provider' egress with the default
 *   'enumerated' basis, reads outside the enumerated surface (i) intake,
 *   (ii) proposals/reports/import-history, (iii) chirality_readable_artifacts,
 *   (iv) dropped files throw OUTSIDE_ENUMERATION — never silently narrowed;
 *   under the owner-selected 'broad' basis (launch-time env act), RBAC-visible
 *   reads pass for model-provider engines too; under 'none' (stub) all
 *   RBAC-visible reads pass. Human-only acts move with NEITHER basis.
 * - Grounds discipline: triage without non-empty grounds is refused ("left
 *   for the owner"), never dispositioned (D-PEC-10 rider).
 * - Conversion guard (GOV MAJOR-1, belt to the client's braces): any
 *   disposition payload that would create approval records is refused before
 *   the client call — this is what binds future engines that may lawfully
 *   convert to non-approval records under the D-PEC-10 rider.
 * - Ruled stale flow: STALE_PROPOSAL → refresh → report that the human must
 *   re-review/re-accept (deep link included); 403 → report, never escalate.
 */

import type { PecAgentClient, ProposalSummary, ProposalView } from './pec-client.ts'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { AgentClientError } from './pec-client.ts'
import type { AccessBasis } from './config.ts'
import type { ActResult, BoundActs, EgressClass, ScreenContextRecord } from './engine/port.ts'
import { CONTRACTS } from './contract-detect.ts'
import { adaptStructuredFile, adaptWorkbook, mappingSummaryText } from './structured-file.ts'
import { parseXlsxWorkbook, WorkbookError } from './xlsx.ts'
import type { ParsedWorkbook } from './xlsx.ts'
import { buildDisciplineStatusDocx, writeDraftDocx } from './docx-report.ts'

const PEC_ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', '..')

export interface ActContext {
  pid: number
  egress: EgressClass
  /** D-T0-21 O-B access basis (default 'enumerated'; owner-selected per launch) */
  access: AccessBasis
  client: PecAgentClient
}

/** D-T0-20 O-B enumeration classes for readable surfaces. */
export type EnumerationClass = 'intake' | 'import' | 'readable-artifact' | 'dropped-file' | 'outside'

export function classifyRead(recordType: string): EnumerationClass {
  switch (recordType) {
    case 'intake_item': return 'intake'                        // (i)
    case 'import_proposal': return 'import'                    // (ii) incl. reports + import history
    // (iii) chirality_readable_artifacts and (iv) owner-dropped files are not
    // record-type reads; they enter through the turn input, not this resolver.
    default: return 'outside'
  }
}

/**
 * The clamp (rider 6, pinned by test), keyed on egress AND the D-T0-21 O-B
 * access basis: under 'model-provider' egress with the 'enumerated' basis a
 * read outside the enumeration throws OUTSIDE_ENUMERATION — never silently
 * narrowed; exactly the pre-D-T0-21 behavior (regression-pinned). Under the
 * owner-selected 'broad' basis, RBAC-visible reads pass for model-provider
 * engines too (D-T0-21 O-B — the owner flips it per launch, knowing any
 * RBAC-visible record the model reads may reach the model provider). Under
 * 'none' (stub: no external-model session exists) every RBAC-visible read
 * passes regardless of basis.
 */
export function assertReadInsideEnumeration(
  egress: EgressClass, recordType: string, access: AccessBasis = 'enumerated',
): void {
  if (egress !== 'model-provider') return
  if (access === 'broad') return
  if (classifyRead(recordType) === 'outside') {
    throw new AgentClientError('OUTSIDE_ENUMERATION',
      `reading '${recordType}' is outside the D-T0-20 O-B enumerated surface for a model-provider engine `
      + `on the 'enumerated' access basis (the owner may select PEC_AGENT_ACCESS=broad per launch — D-T0-21 O-B)`)
  }
}

/**
 * Basis gate for the D-PEC-20 read acts (overview / registers / explain /
 * reports): these surfaces are outside the D-T0-20 enumeration by
 * construction, so for a model-provider engine they pass only on the
 * owner-selected 'broad' basis. Refusals name the basis — never silent.
 */
function broadReadRefusal(ctx: ActContext, act: string, surface: string): ActResult | null {
  if (ctx.egress !== 'model-provider' || ctx.access === 'broad') return null
  return refused(act,
    `reading ${surface} is outside the D-T0-20 O-B enumerated surface for a model-provider engine `
    + `on the 'enumerated' access basis — the owner may select PEC_AGENT_ACCESS=broad per launch (D-T0-21 O-B)`)
}

const refused = (act: string, reason: string): ActResult => ({ kind: 'refused', act, reason })
const result = (act: string, ok: boolean, summary: string, payload?: unknown): ActResult =>
  ({ kind: 'result', act, ok, summary, payload })

const adminLink = (pid: number): string => `/p/${pid}/admin`
const reportsDir = (): string => join(PEC_ROOT, 'pilot-scratch', 'reports')

function reportCounts(p: ProposalView | ProposalSummary): string {
  const r = p.dryRunReport
  if (r == null) return 'no dry-run yet'
  if (r.error) return `dry-run failed: ${r.error}`
  return `${r.accepted ?? 0} would create, ${r.updated ?? 0} would update, `
    + `${(r.conflicts ?? []).length} conflicts, ${(r.rejected ?? []).length} rejected, `
    + `${r.intakeCreated ?? 0} to intake`
}

function proposalPayload(pid: number, p: ProposalView | ProposalSummary): Record<string, unknown> {
  return {
    id: p.id, ref: p.ref, contract: p.contract, state: p.state, version: p.version,
    sourceName: p.sourceName, report: p.dryRunReport, adminLink: adminLink(pid),
  }
}

async function resolveProposal(ctx: ActContext, ref: string): Promise<ProposalSummary | { refusal: ActResult }> {
  const list = await ctx.client.listProposals(ctx.pid)
  if (!list.ok) {
    return { refusal: refused('proposal.resolve', list.kind === 'forbidden' ? list.message : 'proposal list unavailable (stale)') }
  }
  const hit = list.value.find((p) => p.ref.toUpperCase() === ref.toUpperCase())
  if (!hit) return { refusal: refused('proposal.resolve', `no proposal ${ref} is visible to the agent`) }
  return hit
}

export function bindActs(ctx: ActContext): BoundActs {
  return {
    whoami: () => ctx.client.whoami(),

    // detect/map → propose → dry-run summary + deep link
    // D-PEC-42 O-A: a .xlsx attachment arrives as base64, is parsed by the
    // zero-dep sidecar reader, and feeds the SAME mapping/proposal lane; the
    // FULL parsed workbook (every sheet, verbatim grid) rides the result
    // payload so non-tabular sheets are carried, not dropped. Unreadable or
    // unsupported workbooks refuse with the parser's stated basis.
    async proposeCsv({ csv, xlsxBase64, sheet, filename, contract, coverageStart, coverageEnd }) {
      let mapped: ReturnType<typeof adaptStructuredFile> | ReturnType<typeof adaptWorkbook>
      let workbook: ParsedWorkbook | undefined
      if (xlsxBase64 != null) {
        try {
          workbook = parseXlsxWorkbook(Buffer.from(xlsxBase64, 'base64'))
        } catch (e) {
          if (e instanceof WorkbookError) {
            return refused('import.propose', `${filename ?? 'the workbook'} was not filed — ${e.message}`)
          }
          throw e
        }
        mapped = adaptWorkbook(workbook, { filename, contract, sheet })
      } else {
        mapped = adaptStructuredFile(csv ?? '', { filename, contract })
      }
      if (!mapped.ok) {
        return refused('import.propose', `${mapped.reason} (one of: ${CONTRACTS.join(', ')})`)
      }
      // D-PEC-39: coverage is the PE's declaration, carried verbatim — half a declaration
      // is refused here rather than surfacing as a server 400 mid-proposal
      if ((coverageStart == null) !== (coverageEnd == null)) {
        return refused('import.propose', 'a coverage declaration needs both start and end dates (YYYY-MM-DD), e.g. "covering 2026-06-29 to 2026-07-05"')
      }
      const r = await ctx.client.propose(ctx.pid, mapped.contract, mapped.csv, mapped.filename ?? filename,
        coverageStart && coverageEnd ? { start: coverageStart, end: coverageEnd } : undefined,
        // D-PEC-41: the FULL workbook (every sheet verbatim, incl. title/metadata rows the
        // mapped CSV necessarily drops) persists on the proposal as source_extras
        workbook && 'sheetName' in mapped
          ? {
              sourceName: filename ?? null,
              sheets: workbook.sheets,
              mappedSheet: { name: mapped.sheetName, headerRowIndex: mapped.headerRowIndex },
            }
          : undefined)
      if (!r.ok) {
        return refused('import.propose', r.kind === 'forbidden' ? r.message : 'proposal filing came back stale')
      }
      const p = r.value
      const covNote = p.coverageStart
        ? `Declared coverage ${p.coverageStart}..${p.coverageEnd}.`
        : 'No coverage declared — declare the covered dates per uploaded document to support period reporting (D-PEC-39).'
      return result('import.propose', true,
        `${p.ref} proposed (${p.contract}${p.sourceName ? `, ${p.sourceName}` : ''}) — ${p.state}; ${reportCounts(p)}. `
        + `${covNote} ${mappingSummaryText(mapped.summary)}. Accept/apply are human acts in Admin: ${adminLink(ctx.pid)}`,
        {
          ...proposalPayload(ctx.pid, p),
          coverage: { start: p.coverageStart ?? null, end: p.coverageEnd ?? null },
          mapping: mapped.summary,
          // D-PEC-42: the FULL parsed workbook rides the result verbatim (every
          // sheet, tabular or not) for the D-PEC-41 full-fidelity capture — the
          // proposal CSV alone would drop the non-tabular sheets.
          ...(workbook && 'sheetName' in mapped
            ? {
                workbook: { sourceName: filename ?? null, sheets: workbook.sheets },
                mappedSheet: { name: mapped.sheetName, headerRowIndex: mapped.headerRowIndex },
              }
            : {}),
        })
    },

    async refreshProposal({ ref }) {
      const found = await resolveProposal(ctx, ref)
      if ('refusal' in found) return found.refusal
      const r = await ctx.client.refresh(ctx.pid, found.id, found.version)
      if (!r.ok) {
        return r.kind === 'forbidden'
          ? refused('import.refresh', r.message)
          : result('import.refresh', false,
            `${ref} is mid-change (stale/version conflict) — re-check its state in Admin: ${adminLink(ctx.pid)}`)
      }
      const p = r.value
      return result('import.refresh', true,
        `${p.ref} dry-run refreshed — ${p.state}; ${reportCounts(p)}. Any prior acceptance is voided; `
        + `a human must re-review and re-accept in Admin: ${adminLink(ctx.pid)}`,
        proposalPayload(ctx.pid, p))
    },

    async withdrawProposal({ ref, reason }) {
      if (!reason.trim()) return refused('import.withdraw', 'a withdrawal reason is required')
      const found = await resolveProposal(ctx, ref)
      if ('refusal' in found) return found.refusal
      const r = await ctx.client.withdrawOwn(ctx.pid, found.id, found.version, reason)
      if (!r.ok) {
        return r.kind === 'forbidden'
          ? refused('import.withdraw', r.message)
          : result('import.withdraw', false,
            `${ref} changed since it was read (stale) — re-check its state in Admin: ${adminLink(ctx.pid)}`)
      }
      return result('import.withdraw', true,
        `${r.value.ref} withdrawn: ${reason}`, proposalPayload(ctx.pid, r.value))
    },

    async proposalStatus() {
      const list = await ctx.client.listProposals(ctx.pid)
      if (!list.ok) {
        return refused('import.status', list.kind === 'forbidden' ? list.message : 'proposal list unavailable (stale)')
      }
      const me = ctx.client.whoami()
      const mine = list.value.filter((p) => me != null && p.createdBy === me.personId)
      const lines = mine.map((p) => `${p.ref} [${p.state}] ${p.contract} — ${reportCounts(p)}`)
      return result('import.status', true,
        mine.length === 0
          ? `the agent has no proposals in this project. Admin: ${adminLink(ctx.pid)}`
          : `${mine.length} agent proposal(s):\n${lines.join('\n')}\nAdmin: ${adminLink(ctx.pid)}`,
        { proposals: mine.map((p) => proposalPayload(ctx.pid, p)) })
    },

    // open-triage if needed, then disposition; grounds required
    async triageItem({ ref, disposition, grounds }) {
      const list = await ctx.client.listIntake(ctx.pid)
      if (!list.ok) {
        return refused('intake.triage', list.kind === 'forbidden' ? list.message : 'intake queue unavailable (stale)')
      }
      const item = list.value.find((i) => i.ref.toUpperCase() === ref.toUpperCase())
      if (!item) return refused('intake.triage', `no intake item ${ref} is visible to the agent`)

      if (disposition == null) {
        // bare "open triage INTK-n"
        if (item.state !== 'raised') {
          return result('intake.triage', true, `${item.ref} is already ${item.state}`, { item })
        }
        const opened = await ctx.client.openTriage(ctx.pid, item.id, item.version)
        if (!opened.ok) {
          return refused('intake.triage', opened.kind === 'forbidden' ? opened.message : `${item.ref} changed underneath (stale) — retry from the queue`)
        }
        return result('intake.triage', true, `${opened.value.ref} opened for triage (${opened.value.state})`, { item: opened.value })
      }

      if (!grounds || !grounds.trim()) {
        return refused('intake.triage',
          `no grounds given for ${item.ref} — left for the owner (a disposition needs stated grounds; D-PEC-10 rider)`)
      }
      // Conversion guard (GOV MAJOR-1, engine-independent): refuse any payload
      // that would create approval records BEFORE the client call.
      if (payloadWouldCreateApprovalRecords(disposition)) {
        return refused('intake.triage',
          `disposition '${disposition}' could create approval records under conversion — the agent never creates approval records (GOV MAJOR-1; D-PEC-10 rider); the owner performs conversions on-screen`)
      }
      if (!['parked', 'duplicate', 'rejected'].includes(disposition)) {
        return refused('intake.triage',
          `disposition '${disposition}' is outside the agent's v1 vocabulary (parked, duplicate, rejected) — left for the owner`)
      }
      let current = item
      if (current.state === 'raised') {
        const opened = await ctx.client.openTriage(ctx.pid, current.id, current.version)
        if (!opened.ok) {
          return refused('intake.triage', opened.kind === 'forbidden' ? opened.message : `${item.ref} changed underneath (stale) — retry from the queue`)
        }
        current = opened.value
      }
      const done = await ctx.client.disposition(ctx.pid, current.id, {
        version: current.version,
        disposition: disposition as 'parked' | 'duplicate' | 'rejected',
        note: grounds,
      })
      if (!done.ok) {
        return done.kind === 'forbidden'
          ? refused('intake.triage', done.message)
          : result('intake.triage', false, `${item.ref} changed underneath (stale) — retry from the queue`)
      }
      return result('intake.triage', true,
        `${done.value.intake.ref} dispositioned ${done.value.intake.disposition}: ${grounds}`,
        { item: done.value.intake })
    },

    async intakeSummary() {
      const list = await ctx.client.listIntake(ctx.pid)
      if (!list.ok) {
        return refused('intake.summary', list.kind === 'forbidden' ? list.message : 'intake queue unavailable (stale)')
      }
      const byState: Record<string, number> = {}
      for (const i of list.value) byState[i.state] = (byState[i.state] ?? 0) + 1
      const open = list.value.filter((i) => i.state !== 'dispositioned')
      const lines = open.map((i) => `${i.ref} [${i.state}] ${i.statementVerbatim.slice(0, 80)}`)
      return result('intake.summary', true,
        open.length === 0
          ? 'the intake queue has no open items'
          : `${open.length} open intake item(s):\n${lines.join('\n')}`,
        { counts: byState, open: open.map((i) => ({ id: i.id, ref: i.ref, state: i.state, quickType: i.quickType })) })
    },

    // resolves screen refs → enumerated reads only (clamped under model-provider egress)
    async readScreenContext({ route, records }) {
      const readings: Array<{ record: ScreenContextRecord; view: unknown }> = []
      for (const rec of records) {
        try {
          assertReadInsideEnumeration(ctx.egress, rec.recordType, ctx.access)
        } catch (e) {
          // never silently narrowed: the whole act refuses, naming the record
          return refused('screen.read',
            e instanceof Error ? `${rec.recordType} ${rec.ref}: ${e.message}` : String(e))
        }
        const view = await ctx.client.screenRead(ctx.pid, rec.recordType, rec.id)
        if (!view.ok) {
          return refused('screen.read', view.kind === 'forbidden' ? view.message : `${rec.ref} is mid-change (stale)`)
        }
        readings.push({ record: rec, view: view.value })
      }
      return result('screen.read', true,
        readings.length === 0
          ? `route ${route} — no records in view`
          : `route ${route} — ${readings.map((r) => `${r.record.recordType} ${r.record.ref}`).join(', ')}`,
        { route, readings })
    },

    // ---- D-PEC-20 read acts (existing RBAC'd GET routes; basis-gated) ----

    async projectOverview() {
      const gate = broadReadRefusal(ctx, 'read.overview', 'the project overview')
      if (gate) return gate
      const r = await ctx.client.overview(ctx.pid)
      if (!r.ok) {
        return refused('read.overview', r.kind === 'forbidden' ? r.message : 'overview unavailable (stale)')
      }
      return result('read.overview', true, `project overview read (project ${ctx.pid})`, r.value)
    },

    async readRegister({ register }) {
      const name = register.trim().toLowerCase()
      const gate = broadReadRefusal(ctx, 'read.register', `the ${name} register`)
      if (gate) return gate
      let r
      try {
        r = await ctx.client.readRegister(ctx.pid, name)
      } catch (e) {
        if (e instanceof AgentClientError && e.code === 'AGENT_UNMAPPED_READ') {
          return refused('read.register', e.message)
        }
        throw e
      }
      if (!r.ok) {
        return refused('read.register', r.kind === 'forbidden' ? r.message : `${name} register unavailable (stale)`)
      }
      const rows = Array.isArray(r.value) ? r.value : (r.value as { rows?: unknown[] })?.rows
      const count = Array.isArray(rows) ? `${rows.length} row(s)` : 'view'
      return result('read.register', true, `${name} register read — ${count}`, r.value)
    },

    async recordHistory({ recordType, id }) {
      // record-typed read: the enumeration clamp applies per record type
      // (intake/import history stays inside the enumeration on either basis)
      try {
        assertReadInsideEnumeration(ctx.egress, recordType, ctx.access)
      } catch (e) {
        return refused('read.history', e instanceof Error ? e.message : String(e))
      }
      const r = await ctx.client.historyFor(ctx.pid, recordType, id)
      if (!r.ok) {
        return refused('read.history', r.kind === 'forbidden' ? r.message : 'history unavailable (stale)')
      }
      return result('read.history', true,
        `history for ${recordType} #${id} — ${r.value.length} event(s)`, { recordType, id, events: r.value })
    },

    async explainRevision({ id }) {
      const gate = broadReadRefusal(ctx, 'read.explain', `revision #${id} readiness`)
      if (gate) return gate
      const r = await ctx.client.explainRevision(ctx.pid, id)
      if (!r.ok) {
        return refused('read.explain', r.kind === 'forbidden' ? r.message : 'explain unavailable (stale)')
      }
      return result('read.explain', true, `revision #${id} readiness explained`, r.value)
    },

    async readReport({ report, id }) {
      const name = report.trim().toLowerCase()
      const gate = broadReadRefusal(ctx, 'read.report', `the ${name} report`)
      if (gate) return gate
      if (name === 'sponsor-brief') {
        const r = await ctx.client.sponsorBrief(ctx.pid)
        if (!r.ok) return refused('read.report', r.kind === 'forbidden' ? r.message : 'report unavailable (stale)')
        return result('read.report', true, 'sponsor brief read', r.value)
      }
      if (name === 'package-pack') {
        if (!Number.isInteger(id) || (id as number) <= 0) {
          return refused('read.report', 'package-pack needs a package id (e.g. "package pack 3")')
        }
        const r = await ctx.client.packagePack(ctx.pid, id as number)
        if (!r.ok) return refused('read.report', r.kind === 'forbidden' ? r.message : 'report unavailable (stale)')
        return result('read.report', true, `package pack read (package #${id})`, r.value)
      }
      if (name === 'weekly-project-status' || name === 'weekly-project-status-by-discipline') {
        const r = await ctx.client.standardReport(ctx.pid, 'weekly-project-status',
          name.endsWith('discipline') ? 'discipline' : 'package')
        if (!r.ok) return refused('read.report', r.kind === 'forbidden' ? r.message : 'report unavailable (stale)')
        return result('read.report', true, `${name} report read`, r.value)
      }
      if (name === 'package-issue-summary' || name === 'deliverable-completeness') {
        const r = await ctx.client.standardReport(ctx.pid, name)
        if (!r.ok) return refused('read.report', r.kind === 'forbidden' ? r.message : 'report unavailable (stale)')
        return result('read.report', true, `${name} report read`, r.value)
      }
      return refused('read.report',
        `unknown report '${report}' (one of: sponsor-brief, package-pack <id>, weekly-project-status, `
        + `weekly-project-status-by-discipline, package-issue-summary, deliverable-completeness)`)
    },

    async draftDocx({ periodStart, periodEnd }) {
      const act = 'report.draftDocx'
      const gate = broadReadRefusal(ctx, act, 'the .docx discipline status draft inputs')
      if (gate) return gate
      if ((periodStart == null) !== (periodEnd == null)) {
        return refused(act, 'a declared period needs both start and end dates (YYYY-MM-DD); no date is inferred')
      }
      const period = periodStart && periodEnd ? { start: periodStart, end: periodEnd } : null
      if (period && (!/^\d{4}-\d{2}-\d{2}$/.test(period.start) || !/^\d{4}-\d{2}-\d{2}$/.test(period.end) || period.end < period.start)) {
        return refused(act, 'period start/end must be ordered YYYY-MM-DD dates')
      }

      const overview = await ctx.client.overview(ctx.pid)
      if (!overview.ok) return refused(act, overview.kind === 'forbidden' ? overview.message : 'overview unavailable (stale)')
      const project = (overview.value as { project?: { code?: string; name?: string } }).project
      if (!project?.code || !project.name) return refused(act, 'overview did not include the project identity needed for the draft')

      const disciplines = await ctx.client.disciplines(ctx.pid)
      if (!disciplines.ok) return refused(act, disciplines.kind === 'forbidden' ? disciplines.message : 'discipline list unavailable (stale)')
      const disciplineRows = disciplines.value as Array<{ discipline?: string }>
      const disciplineDetails: unknown[] = []
      for (const d of disciplineRows) {
        if (!d.discipline) continue
        const detail = await ctx.client.disciplineDetail(ctx.pid, d.discipline, period ?? undefined)
        if (!detail.ok) return refused(act, detail.kind === 'forbidden' ? detail.message : `discipline ${d.discipline} unavailable (stale)`)
        disciplineDetails.push(detail.value)
      }

      const packageRows = await ctx.client.packages(ctx.pid)
      if (!packageRows.ok) return refused(act, packageRows.kind === 'forbidden' ? packageRows.message : 'packages unavailable (stale)')
      const packageDetails: unknown[] = []
      for (const p of packageRows.value as Array<{ id?: number; openIssues?: number; operationalItems?: number }>) {
        if (!p.id || ((p.openIssues ?? 0) === 0 && (p.operationalItems ?? 0) === 0)) continue
        const detail = await ctx.client.packageDetail(ctx.pid, p.id)
        if (!detail.ok) return refused(act, detail.kind === 'forbidden' ? detail.message : `package #${p.id} unavailable (stale)`)
        packageDetails.push(detail.value)
      }

      const weekly = await ctx.client.standardReport(ctx.pid, 'weekly-project-status', 'discipline', period ?? undefined)
      if (!weekly.ok) return refused(act, weekly.kind === 'forbidden' ? weekly.message : 'weekly status payload unavailable (stale)')
      const packageSummary = await ctx.client.standardReport(ctx.pid, 'package-issue-summary')
      if (!packageSummary.ok) return refused(act, packageSummary.kind === 'forbidden' ? packageSummary.message : 'package issue summary payload unavailable (stale)')

      const draft = buildDisciplineStatusDocx({
        project: { code: project.code, name: project.name },
        period,
        generatedAt: new Date().toISOString(),
        compositionClarification: 'Needs and issues are tracked and reported by package. This includes decisions, risks, action items, clarifications, needs for information and resources etc. Status (i.e. working status, such as in progress or complete) and % complete are tracked by deliverable. Period declaration can happen in the agent sidecar via prompt. Yes I accept the honest absences.',
        disciplines: disciplineDetails as Parameters<typeof buildDisciplineStatusDocx>[0]['disciplines'],
        packageDetails: packageDetails as Parameters<typeof buildDisciplineStatusDocx>[0]['packageDetails'],
      })
      const path = await writeDraftDocx(reportsDir(), draft)
      const weeklyGroups = ((weekly.value as { sections?: { groups?: unknown[] } }).sections?.groups ?? []).length
      const packageReportTotal = ((packageSummary.value as { sections?: { packages?: Array<{ clientIssues?: number }> } }).sections?.packages ?? [])
        .reduce((sum, r) => sum + (r.clientIssues ?? 0), 0)
      return result(act, true,
        `${draft.filename} written to pilot-scratch/reports from imported/reportable facts; `
        + `${draft.figures.disciplines} discipline section(s), ${draft.figures.packageIssueRows} package issue row(s), `
        + `declared period ${period ? `${period.start}..${period.end}` : 'absent'}.`,
        { path, filename: draft.filename, figures: draft.figures, reportPayloadChecks: { weeklyGroups, packageReportTotal } })
    },
  }
}

/**
 * GOV MAJOR-1 acts-layer conversion guard: the v1 stub never sends
 * converted/merged at all (its vocabulary excludes them), so this binds FUTURE
 * engines — a `converted` disposition runs intake conversion under
 * skipPermission, which can create approval records. v1 refuses `converted`
 * wholesale here; a future engine lawfully converting to non-approval records
 * needs its own ruled row and would relax this to a payload-key check (the
 * client's payload guard stays regardless).
 */
function payloadWouldCreateApprovalRecords(disposition: string): boolean {
  return disposition === 'converted'
}
