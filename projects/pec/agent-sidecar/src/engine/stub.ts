/**
 * Deterministic stub engine (D-PEC-17, the v1 default): intent routing over
 * the bounded acts layer. Deterministic by construction — no randomness, no
 * clock-dependent text, identical input + engine state yields identical
 * events (pinned by test). The stub never fabricates model output, never
 * emits an accept/apply act, and never invents record state (F-PEC-2: every
 * fact comes from an API response in the same turn). Egress class 'none':
 * no external-model session exists, so the D-T0-20 clamp does not bind reads.
 */

import type { AgentEnginePort, AgentEvent, AgentTurnInput, BoundActs, ActResult } from './port.ts'
import { CONTRACTS } from '../contract-detect.ts'
import type { Contract } from '../contract-detect.ts'
import { isUserDefinedReportRequest, runUserDefinedReport } from '../user-report.ts'
import { parseDeclaredPeriod } from '../docx-report.ts'

const CAPABILITIES = [
  'I can, in this project:',
  '- file a CSV/TSV/plain tabular file or a .xlsx workbook as an import proposal (drop the file or paste tabular text; '
    + 'name the contract or let me detect it: ' + CONTRACTS.join(', ') + ')',
  '- refresh IPR-<n> (recompute a proposal\'s dry-run)',
  '- withdraw IPR-<n> because <reason> (my own proposals only)',
  '- triage INTK-<n> as parked|duplicate|rejected: <grounds> (also: open triage INTK-<n>)',
  '- status / proposals — my open proposals with lifecycle states',
  '- queue / intake — the intake queue summary',
  '- overview — the project overview and governance signals',
  '- register <name> — read a register (deliverables, packages, plan, my-week, '
    + 'holds, approvals, decisions, risks, tracker, interfaces, log)',
  '- history <recordType> <id> — a record\'s history events',
  '- explain revision <id> — a revision\'s readiness explanation',
  '- sponsor brief / package pack <id> — report payloads',
  '- weekly project status / discipline status / package issue summary / deliverable completeness — standard report payloads',
  '- generate a .docx discipline status report draft into pilot-scratch/reports/ (declare period YYYY-MM-DD to YYYY-MM-DD, or I state no period declared)',
  '- custom/user-defined reports over those bounded report reads; unsupported figures are called absent',
  '- describe what you are looking at (when the panel sends screen context)',
  '(reads outside the enumerated surface follow the launch-selected access basis — D-T0-21)',
  'Accept, apply, and reject-of-others happen in Admin, by you — never by me.',
].join('\n')

function toEvents(r: ActResult): AgentEvent[] {
  return r.kind === 'result'
    ? [{ type: 'act:result', act: r.act, ok: r.ok, summary: r.summary, payload: r.payload }]
    : [{ type: 'act:refused', act: r.act, reason: r.reason }]
}

/** WF-8 attribution + human-act boundary footer for proposal-changing replies. */
function signed(acts: BoundActs, pid: number, text: string): AgentEvent {
  const me = acts.whoami()
  return {
    type: 'agent:reply',
    text: `${text}\nHuman accept/apply: /p/${pid}/admin\n— ${me ? me.name : 'pec agent (not logged in)'}`,
  }
}

const reply = (text: string): AgentEvent => ({ type: 'agent:reply', text })

/** a fenced tabular block (CSV/TSV/plain text, normalized in the acts layer) */
function extractCsv(message: string): string | null {
  const fence = /```(?:csv|tsv|text)?\r?\n([\s\S]*?)```/.exec(message)
  if (fence?.[1] && /[,\t|;]|\S\s{2,}\S/.test(fence[1])) return fence[1].trim()
  return null
}

function namedContract(message: string): Contract | undefined {
  const m = /\b(mdl|rail|decisions|risks|schedule)\b/i.exec(message)
  return m ? (m[1]!.toLowerCase() as Contract) : undefined
}

/** D-PEC-39: a coverage declaration stated with the upload, e.g. "covering 2026-06-29 to 2026-07-05". */
function namedCoverage(message: string): { coverageStart: string; coverageEnd: string } | undefined {
  const m = /\bcover(?:ing|age|s)?\s+(\d{4}-\d{2}-\d{2})\s*(?:\.\.|to|through|-|–)\s*(\d{4}-\d{2}-\d{2})\b/i.exec(message)
  return m ? { coverageStart: m[1]!, coverageEnd: m[2]! } : undefined
}

export function createStubEngine(): AgentEnginePort {
  return {
    subject: 'stub',
    egress: 'none',

    async runTurn(input: AgentTurnInput, acts: BoundActs): Promise<AgentEvent[]> {
      const msg = input.message.replace(/\s+/g, ' ').trim()
      const lower = msg.toLowerCase()

      // 0. D-PEC-44 `.docx` draft generation: sidecar-side writer, declared period only.
      if (/\b(docx|word)\b/i.test(lower) && /\b(discipline|status)\b/i.test(lower) && /\breport\b/i.test(lower)) {
        const period = parseDeclaredPeriod(input.message)
        const r = await acts.draftDocx({ periodStart: period?.start, periodEnd: period?.end })
        return toEvents(r)
      }

      // 0b. user-defined reporting mode (D-PEC-37): bounded reads only, factual-or-absent.
      if (isUserDefinedReportRequest(input.message)) {
        return runUserDefinedReport({ pid: input.pid, message: input.message }, acts)
      }

      // 1. propose: attachment present (tabular text, or a base64 .xlsx
      //    workbook — D-PEC-42), or fenced/pasted CSV block in the message
      const pastedCsv = extractCsv(input.message)
      if (input.attachment || pastedCsv) {
        const r = await acts.proposeCsv({
          ...(input.attachment?.base64 != null
            ? { xlsxBase64: input.attachment.base64 }
            : { csv: input.attachment?.text ?? pastedCsv! }),
          filename: input.attachment?.name,
          contract: namedContract(msg),
          ...namedCoverage(msg),
        })
        if (r.kind === 'refused' && /name the contract/.test(r.reason)) {
          // ambiguous/unknown headers → ask (detection failure degrades to asking, never mis-files)
          return [reply(`${r.reason}`)]
        }
        return [...toEvents(r), signed(acts, input.pid,
          r.kind === 'result' && r.ok ? 'Proposal filed from your file.' : 'The proposal could not be filed — see above.')]
      }

      // 2. refresh IPR-n
      const refresh = /\brefresh\s+(ipr-\d+)\b/i.exec(msg)
      if (refresh) {
        const r = await acts.refreshProposal({ ref: refresh[1]!.toUpperCase() })
        return [...toEvents(r), signed(acts, input.pid,
          r.kind === 'result' && r.ok
            ? 'Dry-run refreshed. Any prior acceptance is voided; a human must re-review and re-accept.'
            : 'The refresh did not complete — see above.')]
      }

      // 3. withdraw IPR-n because <reason>
      const withdraw = /\bwithdraw\s+(ipr-\d+)\b(?:\s+because\s+(.+))?$/i.exec(msg)
      if (withdraw) {
        const reason = withdraw[2]?.trim() ?? ''
        if (!reason) {
          return [reply(`A withdrawal needs a reason: "withdraw ${withdraw[1]!.toUpperCase()} because <reason>".`)]
        }
        const r = await acts.withdrawProposal({ ref: withdraw[1]!.toUpperCase(), reason })
        return [...toEvents(r), signed(acts, input.pid,
          r.kind === 'result' && r.ok ? 'Withdrawn.' : 'The withdrawal did not complete — see above.')]
      }

      // 4a. open triage INTK-n (open only, no disposition)
      const openTriage = /\bopen\s+triage\s+(intk-\d+)\b/i.exec(msg)
      if (openTriage) {
        const r = await acts.triageItem({ ref: openTriage[1]!.toUpperCase() })
        return toEvents(r)
      }

      // 4b. triage INTK-n as <disposition>: <grounds>
      const triage = /\btriage\s+(intk-\d+)\s+as\s+([a-z_]+)\s*(?::\s*(.*))?$/i.exec(msg)
      if (triage) {
        const ref = triage[1]!.toUpperCase()
        const disposition = triage[2]!.toLowerCase()
        const grounds = triage[3]?.trim() ?? ''
        // GOV MAJOR-1 (pinned, non-negotiable): the v1 stub disposition
        // vocabulary is parked/duplicate/rejected ONLY. `converted` is refused
        // deterministically — conversion can create records under
        // skipPermission, including approval records the agent must never
        // create — and NO disposition call is issued.
        if (disposition === 'converted') {
          return [{
            type: 'act:refused', act: 'intake.triage',
            reason: `I do not convert intake items: conversion can create records (including approval records) `
              + `that must stay owner acts. Please perform the conversion of ${ref} on-screen `
              + `(Action & Hold Log → triage), under your own session.`,
          }]
        }
        // `merged` is outside the v1 vocabulary — disclosed scope, not a silent trim.
        if (disposition === 'merged') {
          return [{
            type: 'act:refused', act: 'intake.triage',
            reason: `'merged' is outside my v1 disposition vocabulary (parked, duplicate, rejected) — `
              + `please merge ${ref} on-screen; left for the owner.`,
          }]
        }
        if (!['parked', 'duplicate', 'rejected'].includes(disposition)) {
          return [{
            type: 'act:refused', act: 'intake.triage',
            reason: `'${disposition}' is not a disposition I can record (parked, duplicate, rejected) — left for the owner.`,
          }]
        }
        const r = await acts.triageItem({ ref, disposition, grounds })
        return toEvents(r)
      }

      // 5. read acts (D-PEC-20 item 5 — deterministic routing; the acts layer
      //    applies the D-T0-21 basis gate, so refusals surface verbatim)
      const explain = /\bexplain\s+revision\s+#?(\d+)\b/i.exec(msg)
      if (explain) {
        return toEvents(await acts.explainRevision({ id: Number(explain[1]) }))
      }
      const history = /\bhistory\s+(?:of\s+)?([a-z_]+)\s+#?(\d+)\b/i.exec(msg)
      if (history) {
        return toEvents(await acts.recordHistory({ recordType: history[1]!.toLowerCase(), id: Number(history[2]) }))
      }
      if (/\bsponsor\s+brief\b/i.test(lower)) {
        return toEvents(await acts.readReport({ report: 'sponsor-brief' }))
      }
      const pack = /\bpackage\s+pack\s+#?(\d+)\b/i.exec(msg)
      if (pack) {
        return toEvents(await acts.readReport({ report: 'package-pack', id: Number(pack[1]) }))
      }
      if (/\bdiscipline\s+(status|report)\b/i.test(lower)) {
        return toEvents(await acts.readReport({ report: 'weekly-project-status-by-discipline' }))
      }
      if (/\bweekly\s+project\s+status\b/i.test(lower)) {
        return toEvents(await acts.readReport({ report: 'weekly-project-status' }))
      }
      if (/\bpackage\s+issue\s+summary\b/i.test(lower)) {
        return toEvents(await acts.readReport({ report: 'package-issue-summary' }))
      }
      if (/\bdeliverable\s+(completeness|mdl\s+status)\b/i.test(lower)) {
        return toEvents(await acts.readReport({ report: 'deliverable-completeness' }))
      }
      const named = /\bregister\s+([a-z-]+(?:\s+week)?)\b/i.exec(msg)
      const bare = /^(deliverables|packages|plan|my[- ]week|holds|approvals|decisions|risks|tracker|interfaces|log)$/.exec(lower)
      if (named || bare) {
        const register = (named?.[1] ?? bare![1]!).toLowerCase().replace(/\s+/g, '-')
        return toEvents(await acts.readRegister({ register }))
      }
      if (/\boverview\b/i.test(lower)) {
        return toEvents(await acts.projectOverview())
      }

      // 6. status queries
      if (/\b(status|proposals)\b/i.test(lower)) {
        return toEvents(await acts.proposalStatus())
      }
      if (/\b(queue|intake)\b/i.test(lower)) {
        return toEvents(await acts.intakeSummary())
      }

      // 7. screen context
      if (input.context && /(what am i looking at|this screen|this one)/i.test(lower)) {
        return toEvents(await acts.readScreenContext(input.context))
      }

      // 8. fallback: deterministic capability statement
      return [reply(CAPABILITIES)]
    },
  }
}
