/**
 * SDK engine loader (D-PEC-17 rider 2: the key-droppable seam). This file
 * exists so the later live-LLM enablement is dependency + env + config only —
 * ZERO source change:
 *
 *   npm i @anthropic-ai/claude-agent-sdk -w agent-sidecar
 *   export ANTHROPIC_API_KEY=...        (never committed, never fabricated)
 *   PEC_AGENT_ENGINE=sdk
 *
 * No SDK dependency is added in v1 (the package is not resolvable in the pec
 * tree — verified in the packet); the dynamic import is typed over `unknown`
 * behind a narrow local structural interface, so typecheck passes without the
 * package. No code path here sources, hardcodes, or fabricates a key or model
 * output. Egress class 'model-provider' → the D-T0-20 acts clamp binds on
 * every read the acts layer performs for this engine.
 *
 * The turn wiring drives the SAME bounded acts layer the stub drives: the
 * model may only answer with an act directive (dispatched through BoundActs —
 * so every guard, clamp, and refusal binds) or a plain reply. It cannot name
 * an accept/apply act because no such act exists on the surface it is given.
 * Live-LLM demonstration is deferred until a key exists (Receipt 32 item 4);
 * this body is exercised then, under its own evidence.
 */

import type { AgentEnginePort, AgentEvent, AgentTurnInput, BoundActs, ActResult } from './port.ts'
import type { SidecarConfig } from '../config.ts'

export const SDK_ABSENT_MSG =
  "engine 'sdk' selected but @anthropic-ai/claude-agent-sdk is not installed. "
  + 'Drop-in (no source change): npm i @anthropic-ai/claude-agent-sdk -w agent-sidecar, '
  + 'set ANTHROPIC_API_KEY, set PEC_AGENT_ENGINE=sdk, restart. '
  + 'Until then run the default engine: PEC_AGENT_ENGINE=stub.'

export const KEY_ABSENT_MSG =
  "engine 'sdk' selected but ANTHROPIC_API_KEY is not set. The sidecar never "
  + 'sources or fabricates a key; set it in the local environment and restart, '
  + 'or run the default engine: PEC_AGENT_ENGINE=stub.'

/** narrow structural view over the dynamically imported SDK (no SDK types offline) */
interface SdkModuleLike {
  query?: (opts: { prompt: string; options?: Record<string, unknown> }) => AsyncIterable<unknown>
}

const SYSTEM_PROMPT = [
  'You are the pec project agent. You act ONLY through the acts below; accept,',
  'apply, reject-of-others, and force are human acts you must direct the owner',
  'to perform in Admin. Reply with EXACTLY ONE JSON object, nothing else:',
  '  {"reply": "<text>"}  — to answer without acting, or',
  '  {"act": "<name>", "args": {...}} where <name> is one of:',
  '  proposeCsv {csv, filename?, contract?} · refreshProposal {ref} ·',
  '  withdrawProposal {ref, reason} · proposalStatus {} ·',
  '  triageItem {ref, disposition?, grounds?} · intakeSummary {} ·',
  '  readScreenContext {route, records} ·',
  '  projectOverview {} · readRegister {register} (deliverables, packages, plan,',
  '  my-week, holds, approvals, decisions, risks, tracker, interfaces, log) ·',
  '  recordHistory {recordType, id} · explainRevision {id} ·',
  '  readReport {report: "sponsor-brief"|"package-pack", id?}',
  'Reads are basis-gated (D-T0-21): a refusal naming the access basis is final',
  'for this turn — report it to the owner, never work around it.',
].join('\n')

function assistantTextOf(message: unknown): string {
  if (message == null || typeof message !== 'object') return ''
  const m = message as { type?: string; result?: unknown; message?: { content?: unknown } }
  if (m.type === 'result' && typeof m.result === 'string') return m.result
  if (m.type === 'assistant' && Array.isArray(m.message?.content)) {
    return (m.message!.content as Array<{ type?: string; text?: string }>)
      .filter((b) => b.type === 'text' && typeof b.text === 'string')
      .map((b) => b.text).join('')
  }
  return ''
}

function toEvents(r: ActResult): AgentEvent[] {
  return r.kind === 'result'
    ? [{ type: 'act:result', act: r.act, ok: r.ok, summary: r.summary, payload: r.payload }]
    : [{ type: 'act:refused', act: r.act, reason: r.reason }]
}

export async function createSdkEngine(_cfg: SidecarConfig): Promise<AgentEnginePort> {
  let mod: unknown
  try {
    mod = await import('@anthropic-ai/claude-agent-sdk' as string)
  } catch {
    throw new Error(SDK_ABSENT_MSG)
  }
  if (!process.env.ANTHROPIC_API_KEY) throw new Error(KEY_ABSENT_MSG)

  const sdk = mod as SdkModuleLike
  if (typeof sdk.query !== 'function') {
    throw new Error('the installed @anthropic-ai/claude-agent-sdk does not expose query(); check its version')
  }

  return {
    subject: 'sdk',
    egress: 'model-provider',

    async runTurn(input: AgentTurnInput, acts: BoundActs): Promise<AgentEvent[]> {
      const prompt = JSON.stringify({
        message: input.message,
        context: input.context ?? null,
        attachment: input.attachment ? { name: input.attachment.name, text: input.attachment.text } : null,
      })
      let text = ''
      for await (const message of sdk.query!({
        prompt, options: { systemPrompt: SYSTEM_PROMPT, maxTurns: 1, allowedTools: [] },
      })) {
        const t = assistantTextOf(message)
        if (t) text = t
      }
      let directive: { reply?: string; act?: string; args?: Record<string, unknown> }
      try {
        directive = JSON.parse(text) as typeof directive
      } catch {
        return [{ type: 'agent:reply', text }]
      }
      if (typeof directive.reply === 'string') return [{ type: 'agent:reply', text: directive.reply }]
      const args = directive.args ?? {}
      // dispatch through the SAME bounded acts surface the stub uses — every
      // guard (denylist, disposition-payload, grounds, D-T0-20 clamp) binds
      switch (directive.act) {
        case 'proposeCsv':
          return toEvents(await acts.proposeCsv({
            csv: typeof args.csv === 'string' ? args.csv : input.attachment?.text ?? '',
            filename: typeof args.filename === 'string' ? args.filename : input.attachment?.name,
            contract: typeof args.contract === 'string' ? args.contract : undefined,
          }))
        case 'refreshProposal':
          return toEvents(await acts.refreshProposal({ ref: String(args.ref ?? '') }))
        case 'withdrawProposal':
          return toEvents(await acts.withdrawProposal({ ref: String(args.ref ?? ''), reason: String(args.reason ?? '') }))
        case 'proposalStatus':
          return toEvents(await acts.proposalStatus())
        case 'triageItem':
          return toEvents(await acts.triageItem({
            ref: String(args.ref ?? ''),
            disposition: typeof args.disposition === 'string' ? args.disposition : undefined,
            grounds: typeof args.grounds === 'string' ? args.grounds : undefined,
          }))
        case 'intakeSummary':
          return toEvents(await acts.intakeSummary())
        case 'projectOverview':
          return toEvents(await acts.projectOverview())
        case 'readRegister':
          return toEvents(await acts.readRegister({ register: String(args.register ?? '') }))
        case 'recordHistory':
          return toEvents(await acts.recordHistory({
            recordType: String(args.recordType ?? ''), id: Number(args.id ?? 0),
          }))
        case 'explainRevision':
          return toEvents(await acts.explainRevision({ id: Number(args.id ?? 0) }))
        case 'readReport':
          return toEvents(await acts.readReport({
            report: String(args.report ?? ''),
            id: args.id != null ? Number(args.id) : undefined,
          }))
        case 'readScreenContext':
          return toEvents(await acts.readScreenContext(
            (input.context ?? { route: '', records: [] })))
        default:
          return [{
            type: 'turn:error', code: 'UNKNOWN_ACT',
            message: `the model named an act outside the bounded surface: ${String(directive.act)}`,
          }]
      }
    },
  }
}
