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

const CAPABILITIES = [
  'I can, in this project:',
  '- file a CSV as an import proposal (drop/paste a CSV; name the contract or let me detect it: '
    + CONTRACTS.join(', ') + ')',
  '- refresh IPR-<n> (recompute a proposal\'s dry-run)',
  '- withdraw IPR-<n> because <reason> (my own proposals only)',
  '- triage INTK-<n> as parked|duplicate|rejected: <grounds> (also: open triage INTK-<n>)',
  '- status / proposals — my open proposals with lifecycle states',
  '- queue / intake — the intake queue summary',
  '- describe what you are looking at (when the panel sends screen context)',
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

/** a fenced ``` block, or raw pasted CSV (a comma-bearing header + ≥1 data line) */
function extractCsv(message: string): string | null {
  const fence = /```(?:csv)?\r?\n([\s\S]*?)```/.exec(message)
  if (fence?.[1] && fence[1].includes(',')) return fence[1].trim()
  return null
}

function namedContract(message: string): Contract | undefined {
  const m = /\b(mdl|rail|decisions|risks|schedule)\b/i.exec(message)
  return m ? (m[1]!.toLowerCase() as Contract) : undefined
}

export function createStubEngine(): AgentEnginePort {
  return {
    subject: 'stub',
    egress: 'none',

    async runTurn(input: AgentTurnInput, acts: BoundActs): Promise<AgentEvent[]> {
      const msg = input.message.replace(/\s+/g, ' ').trim()
      const lower = msg.toLowerCase()

      // 1. propose: attachment present, or fenced/pasted CSV block in the message
      const pastedCsv = extractCsv(input.message)
      if (input.attachment || pastedCsv) {
        const csv = input.attachment?.text ?? pastedCsv!
        const r = await acts.proposeCsv({
          csv,
          filename: input.attachment?.name,
          contract: namedContract(msg),
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

      // 5. status queries
      if (/\b(status|proposals)\b/i.test(lower)) {
        return toEvents(await acts.proposalStatus())
      }
      if (/\b(queue|intake)\b/i.test(lower)) {
        return toEvents(await acts.intakeSummary())
      }

      // 6. screen context
      if (input.context && /(what am i looking at|this screen|this one)/i.test(lower)) {
        return toEvents(await acts.readScreenContext(input.context))
      }

      // 7. fallback: deterministic capability statement
      return [reply(CAPABILITIES)]
    },
  }
}
