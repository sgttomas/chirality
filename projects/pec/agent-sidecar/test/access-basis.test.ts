/**
 * D-T0-21 O-B / D-PEC-20 pins — the dual access basis:
 *
 * - config: PEC_AGENT_ACCESS default 'enumerated', 'broad' accepted, anything
 *   else refused at load (never silently widened OR narrowed);
 * - clamp regression: 'enumerated' basis ⇒ EXACTLY the pre-D-T0-21 behavior;
 * - broad basis: RBAC-visible reads pass for model-provider engines;
 * - read acts (overview/register/history/explain/report): basis-gated for
 *   model-provider engines, refused with the basis named, ZERO network on
 *   refusal;
 * - boundary pins under 'broad': accept/apply/reject-of-others/force/
 *   conversion-dispositions still refused — the human-act boundary moves with
 *   NEITHER basis (D-T0-21 O-B exclusion list);
 * - health disclosure: /agent/health states the active basis;
 * - stub vocabulary: deterministic routing to the new read acts, with the
 *   pre-existing intents unshadowed.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createServer } from 'node:http'
import type { Server } from 'node:http'
import { loadConfig } from '../src/config.ts'
import type { SidecarConfig } from '../src/config.ts'
import { PecAgentClient, AgentClientError } from '../src/pec-client.ts'
import type { AgentDispositionBody } from '../src/pec-client.ts'
import { assertReadInsideEnumeration, bindActs } from '../src/acts.ts'
import type { ActContext } from '../src/acts.ts'
import { createStubEngine } from '../src/engine/stub.ts'
import type { ActResult, BoundActs } from '../src/engine/port.ts'
import { startSidecar } from '../src/index.ts'

// ---------- programmable fake pec server (loopback), pec-client.test pattern ----------

interface Seen { method: string; path: string; body: unknown }

let server: Server
let base = ''
const seen: Seen[] = []
let responder: (method: string, path: string) => { status: number; body: unknown } | null = () => null

before(async () => {
  server = createServer(async (req, res) => {
    const chunks: Buffer[] = []
    for await (const c of req) chunks.push(c as Buffer)
    const text = Buffer.concat(chunks).toString('utf8')
    let body: unknown = text
    try { body = JSON.parse(text) } catch { /* raw */ }
    const path = req.url ?? '/'
    seen.push({ method: req.method ?? '', path, body })
    const send = (status: number, payload: unknown, headers: Record<string, string> = {}) => {
      res.writeHead(status, { 'content-type': 'application/json', ...headers })
      res.end(JSON.stringify(payload))
    }
    if (path === '/api/auth/login') {
      send(200, { me: { personId: 16, name: 'PEC Agent', email: 'agent@t.co', isAdmin: false } },
        { 'set-cookie': 'pec_session=tok; HttpOnly' })
      return
    }
    const custom = responder(req.method ?? '', path)
    if (custom) { send(custom.status, custom.body); return }
    send(200, {})
  })
  await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve))
  const addr = server.address()
  base = `http://127.0.0.1:${typeof addr === 'object' && addr ? addr.port : 0}`
})
after(async () => { await new Promise<void>((r) => server.close(() => r())) })

function cfg(over: Partial<SidecarConfig> = {}): SidecarConfig {
  return {
    engine: 'stub', access: 'enumerated', pecBaseUrl: base, port: 0,
    agentEmail: 'agent@t.co', agentPassword: 'secret', ...over,
  }
}

async function actsWith(access: 'enumerated' | 'broad', egress: 'none' | 'model-provider'): Promise<{ acts: BoundActs; client: PecAgentClient }> {
  responder = () => null
  const client = new PecAgentClient(cfg())
  await client.login()
  seen.length = 0
  const ctx: ActContext = { pid: 1, egress, access, client }
  return { acts: bindActs(ctx), client }
}

// ---------- config ----------

test('PEC_AGENT_ACCESS: default enumerated, broad accepted, anything else refused at load', () => {
  const env = { PEC_BASE_URL: 'http://127.0.0.1:4810' }
  assert.equal(loadConfig({ ...env }).access, 'enumerated')
  assert.equal(loadConfig({ ...env, PEC_AGENT_ACCESS: 'enumerated' }).access, 'enumerated')
  assert.equal(loadConfig({ ...env, PEC_AGENT_ACCESS: 'broad' }).access, 'broad')
  assert.throws(() => loadConfig({ ...env, PEC_AGENT_ACCESS: 'open' }), /PEC_AGENT_ACCESS/)
  assert.throws(() => loadConfig({ ...env, PEC_AGENT_ACCESS: 'BROAD' }), /PEC_AGENT_ACCESS/)
})

// ---------- clamp: enumerated regression + broad widening ----------

test('clamp regression pin: the enumerated basis (and the no-basis default) is exactly the pre-D-T0-21 behavior', () => {
  // egress none: everything passes on either basis
  assertReadInsideEnumeration('none', 'deliverable')
  assertReadInsideEnumeration('none', 'deliverable', 'enumerated')
  assertReadInsideEnumeration('none', 'deliverable', 'broad')
  // model-provider + enumerated (explicit AND defaulted): outside refuses
  for (const call of [
    () => assertReadInsideEnumeration('model-provider', 'deliverable'),
    () => assertReadInsideEnumeration('model-provider', 'deliverable', 'enumerated'),
  ]) {
    assert.throws(call, (e: unknown) =>
      e instanceof AgentClientError && e.code === 'OUTSIDE_ENUMERATION')
  }
  // inside the enumeration passes on either basis
  assertReadInsideEnumeration('model-provider', 'intake_item', 'enumerated')
  assertReadInsideEnumeration('model-provider', 'import_proposal', 'enumerated')
})

test('clamp under broad: model-provider reads outside the enumeration pass (D-T0-21 O-B)', () => {
  assertReadInsideEnumeration('model-provider', 'deliverable', 'broad')
  assertReadInsideEnumeration('model-provider', 'risk', 'broad')
})

// ---------- read acts: basis gate + zero network on refusal ----------

test('read acts refuse under model-provider + enumerated, naming the basis, with ZERO network', async () => {
  const { acts } = await actsWith('enumerated', 'model-provider')
  const refusals: ActResult[] = [
    await acts.projectOverview(),
    await acts.readRegister({ register: 'risks' }),
    await acts.explainRevision({ id: 3 }),
    await acts.readReport({ report: 'sponsor-brief' }),
    await acts.recordHistory({ recordType: 'deliverable', id: 7 }),
  ]
  for (const r of refusals) {
    assert.equal(r.kind, 'refused')
    assert.match((r as { reason: string }).reason, /enumerated|D-T0-2[01]/)
  }
  assert.equal(seen.length, 0, 'no refused read reached the server')
})

test('read acts pass under model-provider + broad over the existing GET routes', async () => {
  const { acts } = await actsWith('broad', 'model-provider')
  responder = (m, p) => {
    if (m !== 'GET') return null
    if (p === '/api/projects/1/overview') return { status: 200, body: { project: { name: 'AUR' } } }
    if (p === '/api/projects/1/risks') return { status: 200, body: [{ id: 1, ref: 'RISK-0001' }] }
    if (p === '/api/projects/1/revisions/3/explain') return { status: 200, body: { ready: false } }
    if (p === '/api/projects/1/reports/sponsor-brief') return { status: 200, body: { headline: 'ok' } }
    if (p === '/api/projects/1/reports/package-pack/2') return { status: 200, body: { package: 'PKG-0002' } }
    if (p === '/api/projects/1/history/deliverable/7') return { status: 200, body: [{ event: 'created' }] }
    return null
  }
  const overview = await acts.projectOverview()
  assert.equal(overview.kind, 'result')
  const reg = await acts.readRegister({ register: 'risks' })
  assert.equal(reg.kind, 'result')
  assert.match((reg as { summary: string }).summary, /risks register read — 1 row/)
  const hist = await acts.recordHistory({ recordType: 'deliverable', id: 7 })
  assert.equal(hist.kind, 'result')
  const expl = await acts.explainRevision({ id: 3 })
  assert.equal(expl.kind, 'result')
  const brief = await acts.readReport({ report: 'sponsor-brief' })
  assert.equal(brief.kind, 'result')
  const pack = await acts.readReport({ report: 'package-pack', id: 2 })
  assert.equal(pack.kind, 'result')
  // read-only by construction: every call the server saw was a GET
  assert.ok(seen.length > 0)
  assert.ok(seen.every((s) => s.method === 'GET'), 'broad reads never mutate')
})

test('read acts pass under egress none regardless of basis (stub unchanged)', async () => {
  const { acts } = await actsWith('enumerated', 'none')
  responder = (m, p) => p === '/api/projects/1/overview'
    ? { status: 200, body: { project: { name: 'AUR' } } }
    : null
  const r = await acts.projectOverview()
  assert.equal(r.kind, 'result')
})

test('unknown register and unknown report are refused by name, never guessed', async () => {
  const { acts } = await actsWith('broad', 'model-provider')
  const reg = await acts.readRegister({ register: 'people' })
  assert.equal(reg.kind, 'refused')
  assert.match((reg as { reason: string }).reason, /no register read mapped/)
  const rep = await acts.readReport({ report: 'export' })
  assert.equal(rep.kind, 'refused')
})

test('screen.read under broad reads register-view record types via the register routes (GET only)', async () => {
  const { acts } = await actsWith('broad', 'model-provider')
  responder = (m, p) => m === 'GET' && p === '/api/projects/1/risks'
    ? { status: 200, body: [{ id: 4, ref: 'RISK-0004', title: 'late vendor data' }] }
    : null
  const r = await acts.readScreenContext({
    route: '/p/1/registers/risks',
    records: [{ recordType: 'risk', ref: 'RISK-0004', id: 4 }],
  })
  assert.equal(r.kind, 'result')
  assert.ok(seen.every((s) => s.method === 'GET'))
})

// ---------- boundary pins under broad (D-T0-21 O-B exclusions) ----------

test('boundary pins under broad: accept/apply/outcome/supersede/waive/force still refused before any network call', async () => {
  const { client } = await actsWith('broad', 'model-provider')
  const raw = (client as unknown as {
    request(method: string, path: string, body?: unknown): Promise<unknown>
  }).request.bind(client)
  const denied = [
    ['POST', '/api/projects/1/import-proposals/3/accept', { version: 1, sha256: 'x' }],
    ['POST', '/api/projects/1/import-proposals/3/apply', { version: 1 }],
    ['POST', '/api/projects/1/approval-records/2/outcome', {}],
    ['POST', '/api/projects/1/approval-records/2/supersede', {}],
    ['POST', '/api/projects/1/conditions/2/waive', {}],
    ['POST', '/api/projects/1/import/mdl?force=true', 'csv'],
    ['POST', '/api/projects/1/import-proposals/3/refresh', { version: 1, force: true }],
  ] as const
  for (const [method, path, body] of denied) {
    await assert.rejects(raw(method, path, body),
      (e: unknown) => e instanceof AgentClientError && e.code === 'AGENT_FORBIDDEN_ACT',
      `${path} refused under broad`)
  }
  assert.equal(seen.length, 0, 'the fake server received NOTHING under broad')
})

test('boundary pins under broad: conversion dispositions still refused (acts vocabulary + payload guard)', async () => {
  const { acts, client } = await actsWith('broad', 'model-provider')
  responder = (m, p) => p === '/api/projects/1/can/import.accept'
    ? { status: 200, body: { allowed: false, reason: 'no' } }
    : p === '/api/projects/1/intake'
      ? { status: 200, body: [{ id: 5, ref: 'INTK-0005', state: 'in_triage', version: 2, statementVerbatim: 's', quickType: 'action', disposition: null, dispositionNote: null }] }
      : null
  // acts-layer conversion guard is basis-independent
  const converted = await acts.triageItem({ ref: 'INTK-0005', disposition: 'converted', grounds: 'g' })
  assert.equal(converted.kind, 'refused')
  assert.match((converted as { reason: string }).reason, /approval records|owner/)
  assert.equal(seen.filter((s) => /triage$/.test(s.path)).length, 0, 'no disposition call was issued')
  // client-layer payload guard is basis-independent
  const payload = {
    version: 1, disposition: 'converted', note: 'n',
    records: { approvalRecords: [] },
  } as unknown as AgentDispositionBody
  await assert.rejects(client.disposition(1, 5, payload),
    (e: unknown) => e instanceof AgentClientError && e.code === 'AGENT_FORBIDDEN_ACT')
})

test('boundary pins under broad: withdraw of another person\'s proposal still refused before the reject call', async () => {
  const { client } = await actsWith('broad', 'model-provider')
  responder = (m, p) => p === '/api/projects/1/can/import.accept'
    ? { status: 200, body: { allowed: false, reason: 'no' } }
    : p === '/api/projects/1/import-proposals/4'
      ? { status: 200, body: { id: 4, ref: 'IPR-0004', state: 'ready_for_review', version: 2, createdBy: 999, contract: 'mdl', sourceName: null, sourceSha256: 'x', dryRunReport: null } }
      : null
  await assert.rejects(client.withdrawOwn(1, 4, 2, 'not mine'),
    (e: unknown) => e instanceof AgentClientError && e.code === 'AGENT_FORBIDDEN_ACT')
  assert.equal(seen.filter((s) => /reject$/.test(s.path)).length, 0)
})

// ---------- health disclosure ----------

test('/agent/health states the active access basis (enumerated and broad)', async () => {
  for (const access of ['enumerated', 'broad'] as const) {
    const s = await startSidecar(cfg({ access, agentEmail: null, agentPassword: null }))
    try {
      const health = await fetch(`http://127.0.0.1:${s.port}/agent/health`)
      const h = await health.json() as Record<string, unknown>
      assert.equal(h.access, access)
    } finally {
      await s.close()
    }
  }
})

// ---------- stub vocabulary: deterministic routing, old intents unshadowed ----------

function recordingActs(): { acts: BoundActs; calls: string[] } {
  const calls: string[] = []
  const hit = (name: string): Promise<ActResult> => {
    calls.push(name)
    return Promise.resolve({ kind: 'result', act: name, ok: true, summary: name })
  }
  return {
    calls,
    acts: {
      whoami: () => ({ personId: 16, name: 'PEC Agent', email: 'agent@t.co' }),
      proposeCsv: () => hit('proposeCsv'),
      refreshProposal: () => hit('refreshProposal'),
      withdrawProposal: () => hit('withdrawProposal'),
      proposalStatus: () => hit('proposalStatus'),
      triageItem: () => hit('triageItem'),
      intakeSummary: () => hit('intakeSummary'),
      readScreenContext: () => hit('readScreenContext'),
      projectOverview: () => hit('projectOverview'),
      readRegister: (i) => hit(`readRegister:${i.register}`),
      recordHistory: (i) => hit(`recordHistory:${i.recordType}:${i.id}`),
      explainRevision: (i) => hit(`explainRevision:${i.id}`),
      readReport: (i) => hit(`readReport:${i.report}:${i.id ?? ''}`),
    },
  }
}

test('stub routes the new read intents deterministically and leaves the old intents unshadowed', async () => {
  const engine = createStubEngine()
  const cases: Array<[string, string]> = [
    ['overview', 'projectOverview'],
    ['register risks', 'readRegister:risks'],
    ['register my-week', 'readRegister:my-week'],
    ['register my week', 'readRegister:my-week'],
    ['decisions', 'readRegister:decisions'],
    ['tracker', 'readRegister:tracker'],
    ['history deliverable 7', 'recordHistory:deliverable:7'],
    ['history of risk #4', 'recordHistory:risk:4'],
    ['explain revision 3', 'explainRevision:3'],
    ['sponsor brief', 'readReport:sponsor-brief:'],
    ['package pack 2', 'readReport:package-pack:2'],
    // pre-existing intents keep their meaning (regression)
    ['status', 'proposalStatus'],
    ['proposals', 'proposalStatus'],
    ['intake', 'intakeSummary'],
    ['queue', 'intakeSummary'],
  ]
  for (const [message, expected] of cases) {
    const { acts, calls } = recordingActs()
    await engine.runTurn({ pid: 1, message }, acts)
    assert.deepEqual(calls, [expected], `"${message}" → ${expected}`)
  }
  // determinism: identical input twice → identical events
  const { acts: a1 } = recordingActs()
  const { acts: a2 } = recordingActs()
  const e1 = await engine.runTurn({ pid: 1, message: 'register risks' }, a1)
  const e2 = await engine.runTurn({ pid: 1, message: 'register risks' }, a2)
  assert.deepEqual(e1, e2)
})
