/**
 * SDK engine (D-PEC-17 rider 2, reshaped by D-PEC-21): the live-LLM seam.
 * Enablement is dependency + env + config only:
 *
 *   npm i @anthropic-ai/claude-agent-sdk -w agent-sidecar
 *   export ANTHROPIC_API_KEY=...        (never committed, never fabricated)
 *   PEC_AGENT_ENGINE=sdk
 *
 * Turn shape (D-PEC-21 O-A, owner-directed mechanism): the SDK's own agentic
 * harness runs the loop. Each bounded act is exposed as an in-process MCP
 * tool (createSdkMcpServer/tool) whose handler dispatches through the SAME
 * BoundActs surface the stub drives — every guard, clamp, and refusal binds
 * on every call, and no accept/apply/reject-of-others/force tool exists to
 * expose. query() drives read → result → next act natively, bounded by an
 * in-handler act budget plus maxTurns; the conversation history rides the
 * request (port.ts HistoryEntry — the sidecar stores nothing between
 * requests). The session is hermetic BY DEFAULT: `tools: []` disables EVERY
 * built-in tool (in this SDK `allowedTools` only auto-approves, it does not
 * restrict — adversarial-verification finding), settingSources [] keeps
 * user/project settings, hooks, skills, and ~/.claude MCP servers out, and
 * canUseTool re-denies anything outside the pec whitelist — the model gets
 * no filesystem, shell, or network tool. The owner may select the 'open'
 * profile per launch (PEC_AGENT_SESSION=open, D-T0-22/D-PEC-22) which lifts
 * exactly those two restrictors for limit-testing; the pec bounded-acts
 * surface and human-act boundary are identical in both profiles.
 *
 * The dynamic imports are typed over `unknown` behind narrow structural
 * interfaces, so typecheck never depends on the SDK's types. zod is imported
 * dynamically on the same path — it is a dependency OF the SDK (ships with
 * it), reachable only after the SDK import succeeded. No code path here
 * sources, hardcodes, or fabricates a key or model output.
 */

import type { AgentEnginePort, AgentEvent, AgentTurnInput, BoundActs, ActResult } from './port.ts'
import type { SidecarConfig, SessionProfile } from '../config.ts'
import { parseSessionProfile } from '../config.ts'

export const SDK_ABSENT_MSG =
  "engine 'sdk' selected but @anthropic-ai/claude-agent-sdk is not installed. "
  + 'Drop-in (no source change): npm i @anthropic-ai/claude-agent-sdk -w agent-sidecar, '
  + 'set ANTHROPIC_API_KEY, set PEC_AGENT_ENGINE=sdk, restart. '
  + 'Until then run the default engine: PEC_AGENT_ENGINE=stub.'

export const KEY_ABSENT_MSG =
  "engine 'sdk' selected but ANTHROPIC_API_KEY is not set. The sidecar never "
  + 'sources or fabricates a key; set it in the local environment and restart, '
  + 'or run the default engine: PEC_AGENT_ENGINE=stub.'

/** D-PEC-21 item 1 default act budget (owner-widenable per launch: PEC_AGENT_MAX_ACTS) */
export const MAX_ACTS_PER_TURN = 8
/** cap on any single act payload serialized back to the model (bytes of JSON) */
export const MAX_FEEDBACK_PAYLOAD_BYTES = 48 * 1024

/**
 * Owner-tunable turn limits (D-PEC-21 owner widening direction, 2026-07-07):
 * PEC_AGENT_MAX_ACTS raises/lowers the per-turn act budget per launch
 * (default 8); the SDK maxTurns tracks it with headroom. Invalid values fail
 * at startup, never silently.
 */
export function turnLimitsFromEnv(env: Record<string, string | undefined> = process.env): { maxActs: number; maxTurns: number } {
  const raw = env.PEC_AGENT_MAX_ACTS?.trim()
  let maxActs = MAX_ACTS_PER_TURN
  if (raw) {
    maxActs = Number(raw)
    if (!Number.isInteger(maxActs) || maxActs <= 0) {
      throw new Error(`PEC_AGENT_MAX_ACTS must be a positive integer — got '${raw}'`)
    }
  }
  return { maxActs, maxTurns: maxActs + 4 }
}

function systemPromptOf(maxActs: number, session: SessionProfile = 'hermetic'): string {
  const openLines = session === 'open' ? [
    'This launch runs the OPEN session profile: the harness\'s built-in tools',
    '(files, shell, web, and any configured settings/skills/MCP servers) are',
    'available IN ADDITION to the pec tools, for the owner\'s limit-testing.',
    'pec record acts still go ONLY through the pec tools, and accept, apply,',
    'reject-of-others, and force remain human acts in Admin regardless.',
  ] : []
  return [
    'You are the pec project agent. You act ONLY through the pec tools provided.',
    'Accept, apply, reject-of-others, and force are human acts you must direct',
    'the owner to perform in Admin — no tool performs them and you never claim',
    'to. Answer from tool results actually returned — never invent record state.',
    'The input JSON may carry prior turns in "history": treat them as this same',
    'conversation. Reads are basis-gated (D-T0-21): a tool refusal naming the',
    `access basis is final for this turn — report it to the owner, never work`,
    `around it. You have ${maxActs} tool calls per turn; a wrong or`,
    'empty read may be followed by a better one. Finish every turn with a plain',
    'concise answer for the owner.',
    'For user-defined reports, compose only from bounded pec read/report tool',
    'results. Cite the report/read basis, state unsupported figures as absent,',
    'and refuse professional opinions, go-live/issuance claims, hidden data',
    'requests, and mutations.',
    ...openLines,
  ].join('\n')
}

/** narrow structural view over the dynamically imported SDK (no SDK types offline) */
interface SdkModuleLike {
  query?: (opts: { prompt: string; options?: Record<string, unknown> }) => AsyncIterable<unknown>
  tool?: (
    name: string,
    description: string,
    inputSchema: Record<string, unknown>,
    handler: (args: Record<string, unknown>, extra: unknown) => Promise<ToolCallResult>,
  ) => unknown
  createSdkMcpServer?: (opts: { name: string; version?: string; tools?: unknown[] }) => unknown
}

interface ZodTypeLike { optional(): unknown }
interface ZodLike {
  string(): ZodTypeLike
  number(): ZodTypeLike
}

export interface ToolCallResult {
  content: Array<{ type: 'text'; text: string }>
}

/** per-turn mutable state shared between runTurn and the tool handlers */
export interface TurnSink {
  events: AgentEvent[]
  actsUsed: number
  /** the panel is told ONCE when the budget starts refusing (the owner sees the whole chain) */
  budgetNoticed?: boolean
}

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

/** what one act feeds back to the model — payload size-capped, truncation disclosed */
export function feedbackOf(r: ActResult): Record<string, unknown> {
  if (r.kind === 'refused') return { act: r.act, refused: true, reason: r.reason }
  let payload: unknown = r.payload
  if (payload !== undefined) {
    const raw = JSON.stringify(payload)
    if (Buffer.byteLength(raw, 'utf8') > MAX_FEEDBACK_PAYLOAD_BYTES) {
      payload = {
        truncated: true,
        note: `payload exceeded the ${MAX_FEEDBACK_PAYLOAD_BYTES}-byte feedback cap; ask a narrower question or use the summary`,
        head: raw.slice(0, MAX_FEEDBACK_PAYLOAD_BYTES),
      }
    }
  }
  return { act: r.act, ok: r.ok, summary: r.summary, ...(payload === undefined ? {} : { payload }) }
}

/** the turn input as the model sees it (exported for tests) */
export function promptOf(input: AgentTurnInput): string {
  return JSON.stringify({
    message: input.message,
    context: input.context ?? null,
    attachment: input.attachment ? { name: input.attachment.name, text: input.attachment.text } : null,
    history: input.history ?? null,
  })
}

/** the full bounded tool surface — THIS LIST is the boundary; no accept/apply shape exists */
export const PEC_TOOL_NAMES = [
  'propose_csv', 'refresh_proposal', 'withdraw_proposal', 'proposal_status',
  'triage_item', 'intake_summary', 'read_screen_context', 'project_overview',
  'read_register', 'record_history', 'explain_revision', 'read_report',
] as const

const s = (v: unknown): string => String(v ?? '')
const opt = (v: unknown): string | undefined => (typeof v === 'string' ? v : undefined)

/**
 * Build the in-process MCP tool definitions over a BoundActs (D-PEC-21).
 * `toolFn`/`z` are the SDK's own `tool` and zod, passed in so tests can build
 * and drive the handlers directly with no key and no live session. Every
 * handler: (1) enforces the act budget, (2) dispatches through BoundActs so
 * every guard binds, (3) mirrors the result to the panel event sink, and
 * (4) returns the size-capped feedback JSON to the model.
 */
export function buildPecTools(
  toolFn: NonNullable<SdkModuleLike['tool']>,
  z: ZodLike,
  ctx: { input: AgentTurnInput; acts: BoundActs; sink: TurnSink; maxActs?: number },
): unknown[] {
  const { input, acts, sink } = ctx
  const maxActs = ctx.maxActs ?? MAX_ACTS_PER_TURN

  const bounded = (
    name: string, description: string, schema: Record<string, unknown>,
    exec: (args: Record<string, unknown>) => Promise<ActResult>,
  ): unknown =>
    toolFn(name, description, schema, async (args) => {
      if (sink.actsUsed >= maxActs) {
        const reason = `act budget exhausted (${maxActs} acts this turn) — answer now from the results you already have`
        if (!sink.budgetNoticed) {
          sink.budgetNoticed = true
          sink.events.push({ type: 'act:refused', act: name, reason })
        }
        return { content: [{ type: 'text' as const, text: JSON.stringify({ refused: true, reason }) }] }
      }
      sink.actsUsed += 1
      const r = await exec(args)
      sink.events.push(...toEvents(r))
      return { content: [{ type: 'text' as const, text: JSON.stringify(feedbackOf(r)) }] }
    })

  return [
    bounded('propose_csv',
      'File CSV/TSV/plain tabular text as an import proposal (dry-run only; accept/apply stay human, in Admin).',
      { csv: z.string().optional(), filename: z.string().optional(), contract: z.string().optional() },
      (a) => acts.proposeCsv({
        csv: typeof a.csv === 'string' ? a.csv : input.attachment?.text ?? '',
        filename: opt(a.filename) ?? input.attachment?.name,
        contract: opt(a.contract),
      })),
    bounded('refresh_proposal',
      'Recompute an import proposal dry-run (voids any prior acceptance; a human re-reviews).',
      { ref: z.string() },
      (a) => acts.refreshProposal({ ref: s(a.ref) })),
    bounded('withdraw_proposal',
      'Withdraw one of MY OWN import proposals, with a reason.',
      { ref: z.string(), reason: z.string() },
      (a) => acts.withdrawProposal({ ref: s(a.ref), reason: s(a.reason) })),
    bounded('proposal_status',
      'My open import proposals with lifecycle states.',
      {},
      () => acts.proposalStatus()),
    bounded('triage_item',
      'Triage an intake item (dispositions: parked, duplicate, rejected — conversion stays human).',
      { ref: z.string(), disposition: z.string().optional(), grounds: z.string().optional() },
      (a) => acts.triageItem({ ref: s(a.ref), disposition: opt(a.disposition), grounds: opt(a.grounds) })),
    bounded('intake_summary',
      'The intake queue summary.',
      {},
      () => acts.intakeSummary()),
    bounded('read_screen_context',
      'What the owner is looking at (route + visible record ids the panel published).',
      {},
      () => acts.readScreenContext(input.context ?? { route: '', records: [] })),
    bounded('project_overview',
      'The project overview and governance signals.',
      {},
      () => acts.projectOverview()),
    bounded('read_register',
      'Read a register: deliverables, packages, plan, my-week, holds, approvals, decisions, risks, tracker, interfaces, log.',
      { register: z.string() },
      (a) => acts.readRegister({ register: s(a.register) })),
    bounded('record_history',
      'A record\'s history events.',
      { recordType: z.string(), id: z.number() },
      (a) => acts.recordHistory({ recordType: s(a.recordType), id: Number(a.id ?? 0) })),
    bounded('explain_revision',
      'A revision\'s readiness explanation.',
      { id: z.number() },
      (a) => acts.explainRevision({ id: Number(a.id ?? 0) })),
    bounded('read_report',
      'Report payloads: sponsor-brief, package-pack with an id, or standard report names.',
      { report: z.string(), id: z.number().optional() },
      (a) => acts.readReport({ report: s(a.report), id: a.id != null ? Number(a.id) : undefined })),
  ]
}

/**
 * The query options (exported so tests pin the shape — adversarial finding:
 * this object IS the session's capability boundary). Profile-keyed
 * (D-T0-22/D-PEC-22, `PEC_AGENT_SESSION`, default 'hermetic'):
 *
 * - hermetic (default, the ruled D-PEC-21 shape unchanged): `tools: []`
 *   disables every built-in tool (allowedTools alone does NOT restrict in
 *   this SDK); settingSources [] keeps the user's ~/.claude out;
 *   allowedTools auto-approves exactly the pec tools; canUseTool re-denies
 *   everything else, belt-and-braces.
 * - open (owner-selected per launch, D-T0-22 direction): the `tools`
 *   restrictor is omitted so the SDK's built-in tool set loads;
 *   settingSources carries the harness's normal user/project/local surface;
 *   the pec tools stay auto-approved and canUseTool allows the rest. The
 *   pec bounded-acts surface, budget, clamp, and human-act boundary are
 *   IDENTICAL in both profiles.
 */
export function buildQueryOptions(
  server: unknown,
  env: Record<string, string | undefined> = process.env,
): Record<string, unknown> {
  const allowed = PEC_TOOL_NAMES.map((n) => `mcp__pec__${n}`)
  const { maxActs, maxTurns } = turnLimitsFromEnv(env)
  const session = parseSessionProfile(env.PEC_AGENT_SESSION)
  // PEC_AGENT_MODEL: owner-selected per launch (default: the SDK's default model)
  const model = env.PEC_AGENT_MODEL?.trim()
  return {
    systemPrompt: systemPromptOf(maxActs, session),
    maxTurns,
    ...(model ? { model } : {}),
    ...(session === 'hermetic' ? { tools: [] } : {}),
    mcpServers: { pec: server },
    settingSources: session === 'hermetic' ? [] : ['user', 'project', 'local'],
    allowedTools: allowed,
    canUseTool: async (toolName: string, toolInput: unknown) =>
      allowed.includes(toolName) || session === 'open'
        ? { behavior: 'allow', updatedInput: toolInput }
        : { behavior: 'deny', message: `outside the pec act surface: ${toolName}` },
  }
}

export async function createSdkEngine(_cfg: SidecarConfig): Promise<AgentEnginePort> {
  let mod: unknown
  try {
    mod = await import('@anthropic-ai/claude-agent-sdk' as string)
  } catch {
    throw new Error(SDK_ABSENT_MSG)
  }
  let zmod: unknown
  try {
    // zod ships as the SDK's own dependency — reachable only once the SDK resolved
    zmod = await import('zod' as string)
  } catch {
    throw new Error("the installed @anthropic-ai/claude-agent-sdk did not bring its own 'zod' dependency — reinstall it (npm i @anthropic-ai/claude-agent-sdk -w agent-sidecar)")
  }
  if (!process.env.ANTHROPIC_API_KEY) throw new Error(KEY_ABSENT_MSG)
  turnLimitsFromEnv() // invalid PEC_AGENT_MAX_ACTS fails at startup, never mid-turn
  parseSessionProfile(process.env.PEC_AGENT_SESSION) // invalid PEC_AGENT_SESSION likewise

  const sdk = mod as SdkModuleLike
  const z = (zmod as { z?: ZodLike }).z
  if (typeof sdk.query !== 'function' || typeof sdk.tool !== 'function'
    || typeof sdk.createSdkMcpServer !== 'function' || z == null) {
    throw new Error('the installed @anthropic-ai/claude-agent-sdk does not expose query/tool/createSdkMcpServer; check its version')
  }

  return {
    subject: 'sdk',
    egress: 'model-provider',

    async runTurn(input: AgentTurnInput, acts: BoundActs): Promise<AgentEvent[]> {
      const sink: TurnSink = { events: [], actsUsed: 0 }
      const { maxActs } = turnLimitsFromEnv()
      const server = sdk.createSdkMcpServer!({
        name: 'pec', version: '1.0.0',
        tools: buildPecTools(sdk.tool!, z, { input, acts, sink, maxActs }),
      })
      let text = ''
      for await (const message of sdk.query!({
        prompt: promptOf(input),
        options: buildQueryOptions(server),
      })) {
        const t = assistantTextOf(message)
        if (t) text = t
      }
      if (!text) {
        return [...sink.events, {
          type: 'turn:error', code: 'TURN_EMPTY',
          message: 'the model session ended without a reply — try again or narrow the question',
        }]
      }
      return [...sink.events, { type: 'agent:reply', text }]
    },
  }
}
