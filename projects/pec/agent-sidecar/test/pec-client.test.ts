/**
 * Bounded-client pins (D-PEC-17): method surface = the adopted UI brief §4
 * contract; URL denylist; loopback-only construction; ruled 409/403 semantics;
 * re-login-once; misprovisioning refusal; the GOV MAJOR-1 disposition-payload
 * guard asserted with a fake server that must receive NOTHING (non-negotiable);
 * and the D-T0-20 enumeration clamp (egress 'none' passes, 'model-provider'
 * refuses OUTSIDE_ENUMERATION).
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createServer } from 'node:http'
import type { Server } from 'node:http'
import type { SidecarConfig } from '../src/config.ts'
import { PecAgentClient, AgentClientError } from '../src/pec-client.ts'
import type { AgentDispositionBody } from '../src/pec-client.ts'
import { assertReadInsideEnumeration, bindActs, classifyRead } from '../src/acts.ts'

// ---------- programmable fake pec server (loopback) ----------

interface Seen { method: string; path: string; headers: Record<string, unknown>; body: unknown }

let server: Server
let base = ''
let port = 0
const seen: Seen[] = []
let loginCount = 0
let meBody: Record<string, unknown> = { personId: 16, name: 'PEC Agent', email: 'agent@t.co', isAdmin: false }
/** per-path programmable responses; fall through to 200 {} */
let responder: (method: string, path: string) => { status: number; body: unknown } | null = () => null

before(async () => {
  server = createServer(async (req, res) => {
    const chunks: Buffer[] = []
    for await (const c of req) chunks.push(c as Buffer)
    const text = Buffer.concat(chunks).toString('utf8')
    let body: unknown = text
    try { body = JSON.parse(text) } catch { /* raw */ }
    const path = req.url ?? '/'
    seen.push({ method: req.method ?? '', path, headers: { ...req.headers }, body })
    const send = (status: number, payload: unknown, headers: Record<string, string> = {}) => {
      res.writeHead(status, { 'content-type': 'application/json', ...headers })
      res.end(JSON.stringify(payload))
    }
    if (path === '/api/auth/login') {
      loginCount++
      send(200, { me: meBody }, { 'set-cookie': `pec_session=tok-${loginCount}; HttpOnly` })
      return
    }
    const custom = responder(req.method ?? '', path)
    if (custom) { send(custom.status, custom.body); return }
    send(200, {})
  })
  await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve))
  const addr = server.address()
  port = typeof addr === 'object' && addr ? addr.port : 0
  base = `http://127.0.0.1:${port}`
})
after(async () => { await new Promise<void>((r) => server.close(() => r())) })

function cfg(over: Partial<SidecarConfig> = {}): SidecarConfig {
  return {
    engine: 'stub', pecBaseUrl: base, port: 0,
    agentEmail: 'agent@t.co', agentPassword: 'secret', ...over,
  }
}

async function freshClient(): Promise<PecAgentClient> {
  responder = () => null
  meBody = { personId: 16, name: 'PEC Agent', email: 'agent@t.co', isAdmin: false }
  const client = new PecAgentClient(cfg())
  await client.login()
  seen.length = 0
  return client
}

// ---------- method surface ----------

test('method surface is the §4 contract: no accept/apply/reject-of-others/force/outcome methods', async () => {
  const client = await freshClient()
  for (const name of ['accept', 'apply', 'acceptProposal', 'applyProposal', 'reject',
    'rejectProposal', 'force', 'approvalOutcome', 'recordOutcome', 'supersede', 'waive'] as const) {
    assert.equal((client as unknown as Record<string, unknown>)[name], undefined, `no ${name}() method`)
  }
})

test('URL denylist: accept/apply/outcome/supersede/waive paths and force throw AGENT_FORBIDDEN_ACT before any network call', async () => {
  const client = await freshClient()
  const raw = (client as unknown as {
    request(method: string, path: string, body?: unknown): Promise<unknown>
  }).request.bind(client)
  const denied = [
    ['POST', '/api/projects/1/import-proposals/3/accept', { version: 1, sha256: 'x' }],
    ['POST', '/api/projects/1/import-proposals/3/apply', { version: 1 }],
    ['POST', '/api/projects/1/approval-records/2/outcome', {}],
    ['POST', '/api/projects/1/decisions/2/outcome', {}],
    ['POST', '/api/projects/1/approval-records/2/supersede', {}],
    ['POST', '/api/projects/1/conditions/2/waive', {}],
    ['POST', '/api/projects/1/import/mdl?force=true', 'csv'],
    ['POST', '/api/projects/1/import-proposals/3/refresh', { version: 1, force: true }],
  ] as const
  for (const [method, path, body] of denied) {
    await assert.rejects(raw(method, path, body),
      (e: unknown) => e instanceof AgentClientError && e.code === 'AGENT_FORBIDDEN_ACT',
      `${path} refused`)
  }
  assert.equal(seen.length, 0, 'the fake server received NOTHING')
})

test('non-loopback PEC_BASE_URL is refused at construction', () => {
  assert.throws(() => new PecAgentClient(cfg({ pecBaseUrl: 'http://pec.example.com:4810' })),
    /loopback/)
  assert.throws(() => new PecAgentClient(cfg({ pecBaseUrl: 'http://10.0.0.5:4810' })),
    /loopback/)
  // loopback forms pass construction
  new PecAgentClient(cfg({ pecBaseUrl: 'http://localhost:4810' }))
  new PecAgentClient(cfg({ pecBaseUrl: 'http://127.0.0.1:4810' }))
})

// ---------- ruled failure semantics ----------

test('409 STALE_PROPOSAL comes back as the typed stale result (fake server), never retried', async () => {
  const client = await freshClient()
  responder = (m, p) => m === 'POST' && /refresh$/.test(p.split('?')[0]!)
    ? { status: 409, body: { error: { code: 'STALE_PROPOSAL', message: 'stale', details: { basisHistoryId: 1, currentWatermark: 5 } } } }
    : null
  const r = await client.refresh(1, 3, 2)
  assert.deepEqual(r, { ok: false, kind: 'stale', details: { basisHistoryId: 1, currentWatermark: 5 } })
  assert.equal(seen.filter((s) => /refresh$/.test(s.path)).length, 1, 'exactly one call — no retry')
})

test('403 comes back as the typed forbidden result (report, never escalate), exactly one call', async () => {
  const client = await freshClient()
  responder = (m, p) => p === '/api/projects/1/import-proposals'
    ? { status: 403, body: { error: { code: 'FORBIDDEN', message: 'import.propose: nope' } } }
    : null
  const r = await client.listProposals(1)
  assert.deepEqual(r, { ok: false, kind: 'forbidden', message: 'import.propose: nope' })
  assert.equal(seen.length, 1, 'exactly one call — no retry, no escalation')
})

test('401 triggers exactly one re-login then a replay', async () => {
  const client = await freshClient()
  const startLogins = loginCount
  let first = true
  responder = (m, p) => {
    if (p === '/api/projects/1/import-proposals' && first) {
      first = false
      return { status: 401, body: { error: { code: 'UNAUTHORIZED', message: 'expired' } } }
    }
    if (p === '/api/projects/1/import-proposals') return { status: 200, body: [] }
    return null
  }
  const r = await client.listProposals(1)
  assert.deepEqual(r, { ok: true, value: [] })
  assert.equal(loginCount - startLogins, 1, 'one re-login')
  assert.equal(seen.filter((s) => s.path === '/api/projects/1/import-proposals').length, 2, 'one replay')
})

// ---------- misprovisioning refusals (rider 3) ----------

test('an instance-admin session is fatal at login (AGENT_MISPROVISIONED)', async () => {
  meBody = { personId: 9, name: 'Root', email: 'agent@t.co', isAdmin: true }
  const client = new PecAgentClient(cfg())
  await assert.rejects(client.login(),
    (e: unknown) => e instanceof AgentClientError && e.code === 'AGENT_MISPROVISIONED')
})

test('an accept-capable grant is fatal on the first act in a project', async () => {
  const client = await freshClient()
  responder = (m, p) => p === '/api/projects/1/can/import.accept'
    ? { status: 200, body: { allowed: true, reason: 'admin' } }
    : null
  await assert.rejects(client.propose(1, 'mdl', 'doc_no\nX', 'x.csv'),
    (e: unknown) => e instanceof AgentClientError && e.code === 'AGENT_MISPROVISIONED')
  // the probe was the only thing that reached the server — the propose was not sent
  assert.equal(seen.filter((s) => /import-proposals/.test(s.path)).length, 0)
})

// ---------- GOV MAJOR-1 pin (non-negotiable) ----------

test('GOV MAJOR-1: a conversion payload naming approvalRecords throws AGENT_FORBIDDEN_ACT before ANY network call — the fake server receives nothing', async () => {
  const client = await freshClient()
  const payload = {
    version: 1,
    disposition: 'converted',
    note: 'convert with an approval record',
    records: { approvalRecords: [{ title: 'sneaky', approvalType: 'internal', signatoryIds: [1] }] },
  } as unknown as AgentDispositionBody
  await assert.rejects(client.disposition(1, 5, payload),
    (e: unknown) => e instanceof AgentClientError && e.code === 'AGENT_FORBIDDEN_ACT'
      && /approval records/.test(e.message))
  assert.equal(seen.length, 0, 'the fake server received NOTHING — refused before any network call')

  // deep nesting does not evade the guard
  const nested = {
    version: 1, disposition: 'converted', note: 'n',
    records: { workItems: [{ title: 'x', extra: { approvalRecords: [] } }] },
  } as unknown as AgentDispositionBody
  await assert.rejects(client.disposition(1, 5, nested),
    (e: unknown) => e instanceof AgentClientError && e.code === 'AGENT_FORBIDDEN_ACT')
  assert.equal(seen.length, 0, 'still nothing')
})

test('a lawful disposition payload does reach the server (the guard is targeted, not a block on triage)', async () => {
  const client = await freshClient()
  responder = (m, p) => p === '/api/projects/1/can/import.accept'
    ? { status: 200, body: { allowed: false, reason: 'coordinator does not accept' } }
    : m === 'POST' && p === '/api/projects/1/intake/5/triage'
      ? { status: 200, body: { intake: { id: 5, ref: 'INTK-0005', state: 'dispositioned', disposition: 'parked' }, created: [] } }
      : null
  const r = await client.disposition(1, 5, { version: 2, disposition: 'parked', note: 'grounds here' })
  assert.equal(r.ok, true)
  const hit = seen.find((s) => s.path === '/api/projects/1/intake/5/triage')
  assert.ok(hit, 'the triage route was called')
  assert.deepEqual(hit!.body, { version: 2, disposition: 'parked', note: 'grounds here' })
})

// ---------- D-T0-20 enumeration clamp ----------

test('enumeration clamp: out-of-enumeration reads pass under egress none, throw OUTSIDE_ENUMERATION under model-provider', async () => {
  assert.equal(classifyRead('intake_item'), 'intake')
  assert.equal(classifyRead('import_proposal'), 'import')
  assert.equal(classifyRead('deliverable'), 'outside')

  // 'none' (stub): all RBAC-visible reads pass — no throw
  assertReadInsideEnumeration('none', 'deliverable')
  assertReadInsideEnumeration('none', 'intake_item')
  // 'model-provider' (sdk): outside-enumeration reads refuse, never silently narrowed
  assert.throws(() => assertReadInsideEnumeration('model-provider', 'deliverable'),
    (e: unknown) => e instanceof AgentClientError && e.code === 'OUTSIDE_ENUMERATION')
  assertReadInsideEnumeration('model-provider', 'intake_item')
  assertReadInsideEnumeration('model-provider', 'import_proposal')

  // end to end through acts.readScreenContext
  const client = await freshClient()
  responder = (m, p) => p === '/api/projects/1/deliverables/7'
    ? { status: 200, body: { id: 7, docNo: 'TST-PR-001' } }
    : null
  const records = [{ recordType: 'deliverable', ref: 'TST-PR-001', id: 7 }]
  const underStub = await bindActs({ pid: 1, egress: 'none', client })
    .readScreenContext({ route: '/p/1/deliverables/7', records })
  assert.equal(underStub.kind, 'result', 'stub egress reads the deliverable')

  seen.length = 0
  const underSdk = await bindActs({ pid: 1, egress: 'model-provider', client })
    .readScreenContext({ route: '/p/1/deliverables/7', records })
  assert.equal(underSdk.kind, 'refused')
  assert.match((underSdk as { reason: string }).reason, /OUTSIDE|enumerated/i)
  assert.equal(seen.length, 0, 'the clamped read never reached the server')
})

test('withdrawOwn refuses when the proposal belongs to someone else — before the reject call', async () => {
  const client = await freshClient()
  responder = (m, p) => p === '/api/projects/1/can/import.accept'
    ? { status: 200, body: { allowed: false, reason: 'no' } }
    : p === '/api/projects/1/import-proposals/4'
      ? { status: 200, body: { id: 4, ref: 'IPR-0004', state: 'ready_for_review', version: 2, createdBy: 999, contract: 'mdl', sourceName: null, sourceSha256: 'x', dryRunReport: null } }
      : null
  await assert.rejects(client.withdrawOwn(1, 4, 2, 'not mine'),
    (e: unknown) => e instanceof AgentClientError && e.code === 'AGENT_FORBIDDEN_ACT')
  assert.equal(seen.filter((s) => /reject$/.test(s.path)).length, 0, 'the reject route was never called')
})
