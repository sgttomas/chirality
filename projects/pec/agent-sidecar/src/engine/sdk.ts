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

import type { AgentEnginePort, AgentEvent, AgentStreamSink, AgentTurnInput, BoundActs, ActResult } from './port.ts'
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
    'For .docx discipline status report drafts, use draft_docx_report. Periods',
    'must be explicitly declared by the owner as YYYY-MM-DD to YYYY-MM-DD; do',
    'not infer dates. The generated file is a draft only and is written to the',
    'gitignored pilot-scratch/reports folder.',
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
  maxActs?: number
  emit?: AgentStreamSink
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

function systemInitOf(message: unknown): { model: string; sessionId?: string } | null {
  if (message == null || typeof message !== 'object') return null
  const m = message as { type?: string; subtype?: string; model?: unknown; session_id?: unknown }
  if (m.type !== 'system' || m.subtype !== 'init' || typeof m.model !== 'string') return null
  return { model: m.model, sessionId: typeof m.session_id === 'string' ? m.session_id : undefined }
}

/** SDK partial-message text, matching app-dev's stream-event mapper. */
function partialTextOf(message: unknown): string {
  if (message == null || typeof message !== 'object') return ''
  const m = message as { type?: string; event?: unknown }
  if (m.type !== 'stream_event' || m.event == null || typeof m.event !== 'object') return ''
  const e = m.event as { type?: string; delta?: unknown }
  if (e.type !== 'content_block_delta' || e.delta == null || typeof e.delta !== 'object') return ''
  const delta = e.delta as { type?: string; text?: unknown }
  return delta.type === 'text_delta' && typeof delta.text === 'string' ? delta.text : ''
}

interface ObservedToolUse { id: string; name: string }

export function toolUsesOf(message: unknown): ObservedToolUse[] {
  if (message == null || typeof message !== 'object') return []
  const m = message as { type?: string; event?: unknown; message?: { content?: unknown } }
  let blocks: unknown[] = []
  if (m.type === 'stream_event' && m.event != null && typeof m.event === 'object') {
    const event = m.event as { type?: string; content_block?: unknown }
    if (event.type === 'content_block_start') blocks = [event.content_block]
  } else if (m.type === 'assistant' && Array.isArray(m.message?.content)) {
    blocks = m.message!.content as unknown[]
  }
  return blocks.flatMap((block) => {
    if (block == null || typeof block !== 'object') return []
    const b = block as { type?: string; id?: unknown; name?: unknown }
    if ((b.type !== 'tool_use' && b.type !== 'server_tool_use')
      || typeof b.id !== 'string' || typeof b.name !== 'string') return []
    return [{ id: b.id, name: b.name }]
  })
}

export function toolResultOf(
  message: unknown,
  names: Map<string, string>,
): { id: string; name: string; failed: boolean } | null {
  if (message == null || typeof message !== 'object') return null
  const m = message as { type?: string; parent_tool_use_id?: unknown; tool_use_result?: unknown }
  if (m.type !== 'user' || m.tool_use_result === undefined) return null
  const result = m.tool_use_result
  const resultRecord = result != null && typeof result === 'object' ? result as Record<string, unknown> : {}
  const id = typeof m.parent_tool_use_id === 'string' ? m.parent_tool_use_id
    : typeof resultRecord.tool_use_id === 'string' ? resultRecord.tool_use_id
      : ''
  if (!id) return null
  const name = names.get(id) ?? 'tool'
  const failed = resultRecord.is_error === true || resultRecord.error != null
  return { id, name, failed }
}

function permissionDeniedOf(message: unknown): { id: string; name: string; reason: string } | null {
  if (message == null || typeof message !== 'object') return null
  const m = message as { type?: string; subtype?: string; tool_use_id?: unknown; tool_name?: unknown; message?: unknown }
  if (m.type !== 'system' || m.subtype !== 'permission_denied'
    || typeof m.tool_use_id !== 'string' || typeof m.tool_name !== 'string') return null
  return { id: m.tool_use_id, name: m.tool_name, reason: typeof m.message === 'string' ? m.message : 'permission denied' }
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
  'read_register', 'record_history', 'explain_revision', 'read_report', 'draft_docx_report',
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
    toolFn(name, description, schema, async (args, extra) => {
      const extraRecord = extra != null && typeof extra === 'object' ? extra as Record<string, unknown> : {}
      const toolUseId = typeof extraRecord.toolUseId === 'string'
        ? extraRecord.toolUseId
        : `${name}-${sink.actsUsed + 1}`
      if (sink.actsUsed >= maxActs) {
        const reason = `act budget exhausted (${maxActs} acts this turn) — answer now from the results you already have`
        const budget = { used: sink.actsUsed, max: maxActs, remaining: 0 }
        if (!sink.budgetNoticed) {
          sink.budgetNoticed = true
          sink.events.push({ type: 'act:refused', act: name, reason })
          sink.emit?.({ type: 'tool.failed', data: { toolName: name, toolUseId, act: name, refused: true, reason, actBudget: budget } })
        }
        return { content: [{ type: 'text' as const, text: JSON.stringify({ refused: true, reason }) }] }
      }
      sink.actsUsed += 1
      sink.emit?.({
        type: 'tool.started',
        data: { toolName: name, toolUseId, act: name, actBudget: { used: sink.actsUsed, max: maxActs, remaining: maxActs - sink.actsUsed } },
      })
      const r = await exec(args)
      sink.events.push(...toEvents(r))
      const budget = { used: sink.actsUsed, max: maxActs, remaining: maxActs - sink.actsUsed }
      sink.emit?.(r.kind === 'result'
        ? { type: r.ok ? 'tool.completed' : 'tool.failed', data: { toolName: name, toolUseId, act: r.act, ok: r.ok, summary: r.summary, payload: r.payload, actBudget: budget } }
        : { type: 'tool.failed', data: { toolName: name, toolUseId, act: r.act, refused: true, reason: r.reason, actBudget: budget } })
      return { content: [{ type: 'text' as const, text: JSON.stringify(feedbackOf(r)) }] }
    })

  return [
    bounded('propose_csv',
      'File CSV/TSV/plain tabular text — or the attached .xlsx workbook (D-PEC-42; leave csv empty, optionally name a sheet) — '
      + 'as an import proposal (dry-run only; accept/apply stay human, in Admin). '
      + 'Pass the PE\'s declared coverage dates (coverage_start/coverage_end, YYYY-MM-DD) when stated — never infer them (D-PEC-39).',
      { csv: z.string().optional(), sheet: z.string().optional(), filename: z.string().optional(), contract: z.string().optional(),
        coverage_start: z.string().optional(), coverage_end: z.string().optional() },
      (a) => acts.proposeCsv({
        // a .xlsx attachment rides as base64 workbook bytes unless the model pasted csv itself
        ...(typeof a.csv !== 'string' && input.attachment?.base64 != null
          ? { xlsxBase64: input.attachment.base64 }
          : { csv: typeof a.csv === 'string' ? a.csv : input.attachment?.text ?? '' }),
        sheet: opt(a.sheet),
        filename: opt(a.filename) ?? input.attachment?.name,
        contract: opt(a.contract),
        coverageStart: opt(a.coverage_start),
        coverageEnd: opt(a.coverage_end),
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
    bounded('draft_docx_report',
      'Generate a .docx discipline status report draft in pilot-scratch/reports. Pass period_start/period_end only when the owner explicitly declared both dates; never infer dates.',
      { period_start: z.string().optional(), period_end: z.string().optional() },
      (a) => acts.draftDocx({ periodStart: opt(a.period_start), periodEnd: opt(a.period_end) })),
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
  runtime: { hooks?: Record<string, unknown> } = {},
): Record<string, unknown> {
  const allowed = PEC_TOOL_NAMES.map((n) => `mcp__pec__${n}`)
  const { maxActs, maxTurns } = turnLimitsFromEnv(env)
  const session = parseSessionProfile(env.PEC_AGENT_SESSION)
  // PEC_AGENT_MODEL: owner-selected per launch (default: the SDK's default model)
  const model = env.PEC_AGENT_MODEL?.trim()
  return {
    systemPrompt: systemPromptOf(maxActs, session),
    maxTurns,
    includePartialMessages: true,
    ...(runtime.hooks ? { hooks: runtime.hooks } : {}),
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

  let resolvedModel = process.env.PEC_AGENT_MODEL?.trim() || null
  return {
    subject: 'sdk',
    egress: 'model-provider',
    resolvedModel: () => resolvedModel,

    async runTurn(input: AgentTurnInput, acts: BoundActs, emit?: AgentStreamSink): Promise<AgentEvent[]> {
      const { maxActs } = turnLimitsFromEnv()
      const sink: TurnSink = { events: [], actsUsed: 0, maxActs, emit }
      const server = sdk.createSdkMcpServer!({
        name: 'pec', version: '1.0.0',
        tools: buildPecTools(sdk.tool!, z, { input, acts, sink, maxActs }),
      })
      let text = ''
      let streamedText = ''
      const toolNames = new Map<string, string>()
      const observedToolStarts = new Set<string>()
      const observedToolTerminals = new Set<string>()
      const startObservedTool = (raw: unknown): void => {
        if (raw == null || typeof raw !== 'object') return
        const hook = raw as { tool_name?: unknown; tool_use_id?: unknown }
        if (typeof hook.tool_name !== 'string' || typeof hook.tool_use_id !== 'string'
          || hook.tool_name.startsWith('mcp__pec__')) return
        toolNames.set(hook.tool_use_id, hook.tool_name)
        if (observedToolStarts.has(hook.tool_use_id)) return
        observedToolStarts.add(hook.tool_use_id)
        emit?.({ type: 'tool.started', data: { toolName: hook.tool_name, toolUseId: hook.tool_use_id, source: 'sdk-hook' } })
      }
      const finishObservedTool = (raw: unknown, failed: boolean): void => {
        if (raw == null || typeof raw !== 'object') return
        const hook = raw as { tool_name?: unknown; tool_use_id?: unknown; error?: unknown; duration_ms?: unknown }
        if (typeof hook.tool_name !== 'string' || typeof hook.tool_use_id !== 'string'
          || hook.tool_name.startsWith('mcp__pec__')) return
        startObservedTool(raw)
        if (observedToolTerminals.has(hook.tool_use_id)) return
        observedToolTerminals.add(hook.tool_use_id)
        emit?.({
          type: failed ? 'tool.failed' : 'tool.completed',
          data: {
            toolName: hook.tool_name,
            toolUseId: hook.tool_use_id,
            source: 'sdk-hook',
            ok: !failed,
            summary: `${hook.tool_name} ${failed ? 'failed' : 'completed'}`,
            ...(typeof hook.duration_ms === 'number' ? { durationMs: hook.duration_ms } : {}),
            ...(failed && typeof hook.error === 'string' ? { reason: hook.error } : {}),
          },
        })
      }
      const hooks = {
        PreToolUse: [{ hooks: [async (hook: unknown) => { startObservedTool(hook); return { continue: true } }] }],
        PostToolUse: [{ hooks: [async (hook: unknown) => { finishObservedTool(hook, false); return { continue: true } }] }],
        PostToolUseFailure: [{ hooks: [async (hook: unknown) => { finishObservedTool(hook, true); return { continue: true } }] }],
      }
      emit?.({ type: 'model.request.started', data: { maxActs } })
      for await (const message of sdk.query!({
        prompt: promptOf(input),
        options: buildQueryOptions(server, process.env, { hooks }),
      })) {
        const init = systemInitOf(message)
        if (init) {
          resolvedModel = init.model
          emit?.({ type: 'adapter.initialized', data: { engine: 'sdk', model: init.model, engineSessionId: init.sessionId } })
        }
        const delta = partialTextOf(message)
        if (delta) {
          streamedText += delta
          emit?.({ type: 'model.delta', data: { text: delta } })
        }
        for (const toolUse of toolUsesOf(message)) {
          toolNames.set(toolUse.id, toolUse.name)
          // PEC MCP tools emit richer events in their bounded handler,
          // including the act budget and refusal payload. The generic SDK
          // observer covers open-profile built-ins without duplicating PEC.
          if (!toolUse.name.startsWith('mcp__pec__') && !observedToolStarts.has(toolUse.id)) {
            observedToolStarts.add(toolUse.id)
            emit?.({ type: 'tool.started', data: { toolName: toolUse.name, toolUseId: toolUse.id, source: 'sdk' } })
          }
        }
        if (message != null && typeof message === 'object') {
          const observed = message as {
            type?: string; tool_use_id?: unknown; tool_name?: unknown
            preceding_tool_use_ids?: unknown; summary?: unknown
          }
          if (observed.type === 'tool_progress'
            && typeof observed.tool_use_id === 'string' && typeof observed.tool_name === 'string') {
            startObservedTool({ tool_use_id: observed.tool_use_id, tool_name: observed.tool_name })
          }
          // app-dev uses SDK tool_use_summary as the terminal evidence for
          // server/built-in tools that do not produce a normal user result.
          if (observed.type === 'tool_use_summary' && Array.isArray(observed.preceding_tool_use_ids)) {
            for (const id of observed.preceding_tool_use_ids) {
              if (typeof id !== 'string' || observedToolTerminals.has(id)) continue
              const name = toolNames.get(id) ?? 'tool'
              if (name.startsWith('mcp__pec__')) continue
              observedToolTerminals.add(id)
              emit?.({
                type: 'tool.completed',
                data: {
                  toolName: name,
                  toolUseId: id,
                  source: 'sdk-summary',
                  ok: true,
                  summary: typeof observed.summary === 'string' ? observed.summary : `${name} completed`,
                },
              })
            }
          }
        }
        const toolResult = toolResultOf(message, toolNames)
        if (toolResult && !toolResult.name.startsWith('mcp__pec__') && !observedToolTerminals.has(toolResult.id)) {
          observedToolTerminals.add(toolResult.id)
          emit?.({
            type: toolResult.failed ? 'tool.failed' : 'tool.completed',
            data: {
              toolName: toolResult.name,
              toolUseId: toolResult.id,
              source: 'sdk',
              ok: !toolResult.failed,
              summary: `${toolResult.name} ${toolResult.failed ? 'failed' : 'completed'}`,
            },
          })
        }
        const denied = permissionDeniedOf(message)
        if (denied && !observedToolTerminals.has(denied.id)) {
          observedToolTerminals.add(denied.id)
          emit?.({ type: 'tool.failed', data: { toolName: denied.name, toolUseId: denied.id, source: 'sdk', refused: true, reason: denied.reason } })
        }
        const t = assistantTextOf(message)
        if (t) text = t
      }
      if (!text) {
        return [...sink.events, {
          type: 'turn:error', code: 'TURN_EMPTY',
          message: 'the model session ended without a reply — try again or narrow the question',
        }]
      }
      // The result message is authoritative. Partial deltas are presentation;
      // message.completed lets the UI reconcile without duplicating them.
      emit?.({ type: 'model.completed', data: { actsUsed: sink.actsUsed, maxActs } })
      emit?.({ type: 'message.completed', data: { role: 'assistant', source: 'model', text, streamed: streamedText.length > 0 } })
      return [...sink.events, { type: 'agent:reply', text }]
    },
  }
}
