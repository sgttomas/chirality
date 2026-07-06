/**
 * The act/tool layer both engines drive (D-PEC-17). Every fact in an ActResult
 * comes from an API response in the same turn (F-PEC-2 — the engine formats,
 * never invents). Guards owned here:
 *
 * - D-T0-20 O-B enumeration clamp, keyed on the engine's egress class: reads
 *   outside the enumerated surface (i) intake, (ii) proposals/reports/
 *   import-history, (iii) chirality_readable_artifacts, (iv) dropped files
 *   throw OUTSIDE_ENUMERATION when egress is 'model-provider' — never silently
 *   narrowed; under 'none' (stub) all RBAC-visible reads pass.
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
import { AgentClientError } from './pec-client.ts'
import type { ActResult, BoundActs, EgressClass, ScreenContextRecord } from './engine/port.ts'
import { detectContract } from './contract-detect.ts'
import { CONTRACTS } from './contract-detect.ts'

export interface ActContext {
  pid: number
  egress: EgressClass
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
 * The clamp (rider 6, pinned by test): under 'model-provider' egress a read
 * outside the enumeration throws OUTSIDE_ENUMERATION — never silently
 * narrowed. Under 'none' (stub: no external-model session exists) every
 * RBAC-visible read passes; D-T0-20's own scoping sentence covers exactly
 * external-model sessions, so v1 is visibility-lawful by construction.
 */
export function assertReadInsideEnumeration(egress: EgressClass, recordType: string): void {
  if (egress !== 'model-provider') return
  if (classifyRead(recordType) === 'outside') {
    throw new AgentClientError('OUTSIDE_ENUMERATION',
      `reading '${recordType}' is outside the D-T0-20 O-B enumerated surface for a model-provider engine`)
  }
}

const refused = (act: string, reason: string): ActResult => ({ kind: 'refused', act, reason })
const result = (act: string, ok: boolean, summary: string, payload?: unknown): ActResult =>
  ({ kind: 'result', act, ok, summary, payload })

const adminLink = (pid: number): string => `/p/${pid}/admin`

function reportCounts(p: ProposalView | ProposalSummary): string {
  const r = p.dryRunReport
  if (r == null) return 'no dry-run yet'
  if (r.error) return `dry-run failed: ${r.error}`
  return `${r.accepted ?? 0} would create, ${r.updated ?? 0} would update, `
    + `${(r.conflicts ?? []).length} conflicts, ${(r.rejected ?? []).length} rejected, `
    + `${r.intakeCreated ?? 0} to intake`
}

function proposalPayload(pid: number, p: ProposalView | ProposalSummary): unknown {
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

    // detect → propose → dry-run summary + deep link
    async proposeCsv({ csv, filename, contract }) {
      let chosen = contract
      if (!chosen) {
        const det = detectContract(csv)
        if ('ambiguous' in det) {
          return refused('import.propose',
            `the CSV headers match more than one contract (${det.ambiguous.join(', ')}) — name the contract (one of: ${CONTRACTS.join(', ')})`)
        }
        if ('unknown' in det) {
          return refused('import.propose',
            `the CSV headers match no §16 contract — name the contract (one of: ${CONTRACTS.join(', ')})`)
        }
        chosen = det.contract
      }
      if (!(CONTRACTS as readonly string[]).includes(chosen)) {
        return refused('import.propose', `unknown contract '${chosen}' (one of: ${CONTRACTS.join(', ')})`)
      }
      const r = await ctx.client.propose(ctx.pid, chosen, csv, filename)
      if (!r.ok) {
        return refused('import.propose', r.kind === 'forbidden' ? r.message : 'proposal filing came back stale')
      }
      const p = r.value
      return result('import.propose', true,
        `${p.ref} proposed (${p.contract}${p.sourceName ? `, ${p.sourceName}` : ''}) — ${p.state}; ${reportCounts(p)}. `
        + `Accept/apply are human acts in Admin: ${adminLink(ctx.pid)}`,
        proposalPayload(ctx.pid, p))
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
          assertReadInsideEnumeration(ctx.egress, rec.recordType)
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
