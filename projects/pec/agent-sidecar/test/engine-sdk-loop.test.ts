/**
 * D-PEC-21 pins: the SDK-native act surface (buildPecTools) driven directly —
 * real SDK tool() + real zod, no key, no live session. What is pinned: the
 * tool list IS the boundary (no accept/apply/reject/force shape exists); every
 * handler dispatches through BoundActs and mirrors the result to the panel
 * event sink; act results feed back to the model size-capped with disclosed
 * truncation; refusals feed back verbatim; the 8-act budget refuses further
 * acts WITHOUT executing them; request-borne history rides the prompt.
 * (The query() loop itself is the SDK's own harness — exercised live at the
 * owner's screen under the row's evidence plan, never simulated here.)
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { tool } from '@anthropic-ai/claude-agent-sdk'
import { z } from 'zod'
import {
  buildPecTools, feedbackOf, promptOf,
  MAX_ACTS_PER_TURN, MAX_FEEDBACK_PAYLOAD_BYTES, PEC_TOOL_NAMES,
} from '../src/engine/sdk.ts'
import type { TurnSink, ToolCallResult } from '../src/engine/sdk.ts'
import type { AgentTurnInput, BoundActs, ActResult } from '../src/engine/port.ts'

const INPUT: AgentTurnInput = { pid: 1, message: 'what % of deliverables are on plan?' }

const never = (name: string) => async (): Promise<ActResult> => {
  assert.fail(`act ${name} must not be called by this test`)
}

/** a BoundActs where everything fails loudly unless overridden */
function makeActs(overrides: Partial<BoundActs> = {}): BoundActs {
  return {
    whoami: () => ({ personId: 46, name: 'PEC Agent', email: 'pec-agent@test' }),
    proposeCsv: never('proposeCsv'),
    refreshProposal: never('refreshProposal'),
    withdrawProposal: never('withdrawProposal'),
    proposalStatus: never('proposalStatus'),
    triageItem: never('triageItem'),
    intakeSummary: never('intakeSummary'),
    readScreenContext: never('readScreenContext'),
    projectOverview: never('projectOverview'),
    readRegister: never('readRegister'),
    recordHistory: never('recordHistory'),
    explainRevision: never('explainRevision'),
    readReport: never('readReport'),
    draftDocx: never('draftDocx'),
    ...overrides,
  }
}

interface BuiltTool {
  name: string
  handler: (args: Record<string, unknown>, extra: unknown) => Promise<ToolCallResult>
}

function build(acts: BoundActs, input: AgentTurnInput = INPUT): { tools: BuiltTool[]; sink: TurnSink } {
  const sink: TurnSink = { events: [], actsUsed: 0 }
  const tools = buildPecTools(
    tool as Parameters<typeof buildPecTools>[0],
    z as Parameters<typeof buildPecTools>[1],
    { input, acts, sink },
  ) as BuiltTool[]
  return { tools, sink }
}

const toolByName = (tools: BuiltTool[], name: string): BuiltTool => {
  const t = tools.find((x) => x.name === name)
  assert.ok(t, `tool ${name} must exist`)
  return t
}

const textOf = (r: ToolCallResult): Record<string, unknown> =>
  JSON.parse(r.content[0]!.text) as Record<string, unknown>

test('the tool list IS the boundary: exactly the bounded acts, no accept/apply/reject/force shape', () => {
  const { tools } = build(makeActs())
  assert.deepEqual(tools.map((t) => t.name).sort(), [...PEC_TOOL_NAMES].sort())
  for (const t of tools) {
    assert.doesNotMatch(t.name, /accept|apply|reject|force|approve/i,
      'no human-act-shaped tool may exist on the surface')
  }
})

test('read-then-feedback: the handler dispatches through BoundActs, mirrors the panel event, returns the payload to the model', async () => {
  const rows = { register: 'deliverables', rows: [{ ref: 'DEL-1', onPlan: true }, { ref: 'DEL-2', onPlan: false }] }
  const acts = makeActs({
    readRegister: async ({ register }) => {
      assert.equal(register, 'deliverables')
      return { kind: 'result', act: 'read.register', ok: true, summary: 'deliverables register read — 2 row(s)', payload: rows }
    },
  })
  const { tools, sink } = build(acts)
  const fed = textOf(await toolByName(tools, 'read_register').handler({ register: 'deliverables' }, {}))
  // the model sees the actual rows — the whole point of D-PEC-21
  assert.equal(fed.act, 'read.register')
  assert.deepEqual(fed.payload, rows)
  // the panel sees the same act as an event
  assert.equal(sink.events.length, 1)
  assert.equal(sink.events[0]!.type, 'act:result')
  assert.equal(sink.actsUsed, 1)
})

test('draft_docx_report dispatches through the sidecar writer act with explicit period dates', async () => {
  const acts = makeActs({
    draftDocx: async ({ periodStart, periodEnd }) => {
      assert.equal(periodStart, '2026-07-01')
      assert.equal(periodEnd, '2026-07-07')
      return { kind: 'result', act: 'report.draftDocx', ok: true, summary: 'draft written', payload: { filename: 'synthetic.docx' } }
    },
  })
  const { tools, sink } = build(acts)
  const fed = textOf(await toolByName(tools, 'draft_docx_report').handler({
    period_start: '2026-07-01',
    period_end: '2026-07-07',
  }, {}))
  assert.equal(fed.act, 'report.draftDocx')
  assert.deepEqual(fed.payload, { filename: 'synthetic.docx' })
  assert.equal(sink.events[0]!.type, 'act:result')
})

test('refusal feedback: a basis refusal reaches the model verbatim and the panel as act:refused', async () => {
  const reason = "reads outside the enumerated surface are refused under the 'enumerated' access basis (D-T0-21)"
  const acts = makeActs({ readRegister: async () => ({ kind: 'refused', act: 'read.register', reason }) })
  const { tools, sink } = build(acts)
  const fed = textOf(await toolByName(tools, 'read_register').handler({ register: 'plan' }, {}))
  assert.equal(fed.refused, true)
  assert.equal(fed.reason, reason)
  assert.equal(sink.events[0]!.type, 'act:refused')
})

test(`act budget: call ${MAX_ACTS_PER_TURN + 1} refuses the last WITHOUT executing it`, async () => {
  let executed = 0
  const acts = makeActs({
    projectOverview: async () => {
      executed += 1
      return { kind: 'result', act: 'read.overview', ok: true, summary: 'overview read' }
    },
  })
  const { tools, sink } = build(acts)
  const overview = toolByName(tools, 'project_overview')
  for (let i = 0; i < MAX_ACTS_PER_TURN; i++) await overview.handler({}, {})
  const fed = textOf(await overview.handler({}, {}))
  assert.equal(fed.refused, true)
  assert.match(String(fed.reason), /act budget exhausted/)
  assert.equal(executed, MAX_ACTS_PER_TURN, 'the over-budget act must never reach BoundActs')
  // the panel is told exactly once, however many times the model keeps trying
  await overview.handler({}, {})
  const refusals = sink.events.filter((e) => e.type === 'act:refused')
  assert.equal(refusals.length, 1, 'one budget notice for the owner, no spam')
  assert.match((refusals[0] as { reason: string }).reason, /act budget exhausted/)
  assert.equal(sink.events.length, MAX_ACTS_PER_TURN + 1)
})

test('feedback payload cap: oversized payloads are truncated with a disclosure; the panel event keeps the full payload', async () => {
  const big = { rows: 'x'.repeat(MAX_FEEDBACK_PAYLOAD_BYTES + 1024) }
  const acts = makeActs({
    readRegister: async () => ({ kind: 'result', act: 'read.register', ok: true, summary: 'log register read — huge', payload: big }),
  })
  const { tools, sink } = build(acts)
  const fed = textOf(await toolByName(tools, 'read_register').handler({ register: 'log' }, {}))
  const payload = fed.payload as { truncated?: boolean; note?: string; head?: string }
  assert.equal(payload.truncated, true)
  assert.match(payload.note ?? '', /feedback cap/)
  assert.ok((payload.head ?? '').length <= MAX_FEEDBACK_PAYLOAD_BYTES)
  assert.deepEqual((sink.events[0] as { payload: unknown }).payload, big)
})

test('screen context: the tool reads the request context, not model-supplied coordinates', async () => {
  const context = { route: '/p/1/deliverables', records: [{ recordType: 'deliverable', ref: 'DEL-1', id: 7 }] }
  const acts = makeActs({
    readScreenContext: async (c) => {
      assert.deepEqual(c, context)
      return { kind: 'result', act: 'screen.read', ok: true, summary: 'screen context read' }
    },
  })
  const { tools } = build(acts, { ...INPUT, context })
  await toolByName(tools, 'read_screen_context').handler({ route: '/somewhere/else', records: [] }, {})
})

test('proposal from attachment: csv falls back to the request attachment (the model need not re-paste)', async () => {
  const attachment = { name: 'mdl.csv', text: 'doc_no,title\nX-1,T' }
  const acts = makeActs({
    proposeCsv: async ({ csv, filename }) => {
      assert.equal(csv, attachment.text)
      assert.equal(filename, attachment.name)
      return { kind: 'result', act: 'proposal.propose', ok: true, summary: 'IPR-1 filed' }
    },
  })
  const { tools } = build(acts, { ...INPUT, attachment })
  await toolByName(tools, 'propose_csv').handler({}, {})
})

test('conversation memory: request-borne history rides the prompt JSON', () => {
  const input: AgentTurnInput = {
    ...INPUT,
    history: [
      { who: 'you', text: 'what % of deliverables are on plan?' },
      { who: 'agent', text: '[read.register] deliverables register read — 14 row(s)' },
    ],
  }
  const prompt = JSON.parse(promptOf(input)) as { history: Array<{ who: string; text: string }>; message: string }
  assert.equal(prompt.history.length, 2)
  assert.equal(prompt.history[1]!.who, 'agent')
  assert.equal(prompt.message, INPUT.message)
  // and absent history is explicit null, never fabricated
  assert.equal((JSON.parse(promptOf(INPUT)) as { history: unknown }).history, null)
})

test('feedbackOf: refusals carry no payload; results without payload stay bare', () => {
  assert.deepEqual(feedbackOf({ kind: 'refused', act: 'a', reason: 'r' }), { act: 'a', refused: true, reason: 'r' })
  assert.deepEqual(feedbackOf({ kind: 'result', act: 'a', ok: true, summary: 's' }), { act: 'a', ok: true, summary: 's' })
})

test('hermetic session options (adversarial finding): tools [] disables built-ins; whitelist + canUseTool deny pin the rest', async () => {
  const { buildQueryOptions } = await import('../src/engine/sdk.ts')
  const opts = buildQueryOptions({ marker: 'server' }, {})
  // tools: [] is the load-bearing restrictor — allowedTools alone does NOT
  // restrict the tool set in this SDK (it only auto-approves)
  assert.deepEqual(opts.tools, [])
  assert.deepEqual(opts.settingSources, [], 'no user/project settings, hooks, skills, or ~/.claude MCP servers')
  assert.deepEqual(opts.allowedTools, PEC_TOOL_NAMES.map((n) => `mcp__pec__${n}`))
  assert.deepEqual(opts.mcpServers, { pec: { marker: 'server' } })
  assert.equal(opts.maxTurns, MAX_ACTS_PER_TURN + 4)
  assert.equal('model' in opts, false, 'no model pin unless the owner selects one')
  const canUseTool = opts.canUseTool as (name: string, input: unknown) => Promise<{ behavior: string; message?: string }>
  assert.equal((await canUseTool('mcp__pec__read_register', { register: 'plan' })).behavior, 'allow')
  for (const outside of ['Bash', 'Read', 'WebFetch', 'Glob', 'mcp__other__tool']) {
    const denied = await canUseTool(outside, {})
    assert.equal(denied.behavior, 'deny', `must deny ${outside}`)
    assert.match(denied.message ?? '', /outside the pec act surface/)
  }
})

test('owner-tunable limits (widening direction): PEC_AGENT_MAX_ACTS and PEC_AGENT_MODEL are per-launch knobs; invalid budget fails loudly', async () => {
  const { buildQueryOptions, turnLimitsFromEnv } = await import('../src/engine/sdk.ts')
  // defaults
  assert.deepEqual(turnLimitsFromEnv({}), { maxActs: MAX_ACTS_PER_TURN, maxTurns: MAX_ACTS_PER_TURN + 4 })
  // owner widens the budget per launch
  const wide = buildQueryOptions({ marker: 'server' }, { PEC_AGENT_MAX_ACTS: '32', PEC_AGENT_MODEL: 'claude-fable-5' })
  assert.equal(wide.maxTurns, 36)
  assert.equal(wide.model, 'claude-fable-5')
  assert.match(String(wide.systemPrompt), /32 tool calls per turn/)
  // the widened budget binds in the handlers too
  const sink: TurnSink = { events: [], actsUsed: 0 }
  const acts = makeActs({
    projectOverview: async () => ({ kind: 'result', act: 'read.overview', ok: true, summary: 'overview read' }),
  })
  const tools = buildPecTools(
    tool as Parameters<typeof buildPecTools>[0],
    z as Parameters<typeof buildPecTools>[1],
    { input: INPUT, acts, sink, maxActs: 2 },
  ) as BuiltTool[]
  const overview = toolByName(tools, 'project_overview')
  await overview.handler({}, {})
  await overview.handler({}, {})
  const refused = JSON.parse((await overview.handler({}, {})).content[0]!.text) as { refused?: boolean; reason?: string }
  assert.equal(refused.refused, true)
  assert.match(refused.reason ?? '', /2 acts this turn/)
  // invalid values refuse at resolution, never silently clamp
  for (const bad of ['0', '-1', 'many', '2.5']) {
    assert.throws(() => turnLimitsFromEnv({ PEC_AGENT_MAX_ACTS: bad }), /positive integer/, `must refuse: ${bad}`)
  }
})
