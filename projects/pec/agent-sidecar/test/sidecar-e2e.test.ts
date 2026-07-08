/**
 * Hermetic sidecar e2e (D-PEC-17): a harness-spawned pec server (temp DB,
 * seeded cast), an agent person provisioned per the rehearsal-01 pattern
 * (coordinator, is_admin=0), and the sidecar started IN-PROCESS pointed at it.
 * Pins: full HTTP turns (propose from attachment / refresh / withdraw-own /
 * triage-with-grounds), agent attribution end to end (WF-8), the RBAC
 * human-act boundary (agent direct-accept 403; harness admin accept+apply
 * succeed on the same server), unconfigured mode, and the documented
 * SDK-absent startup error. All key-independent.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from '../../server/test/harness.ts'
import type { TestEnv } from '../../server/test/harness.ts'
import { hashPassword } from '../../server/src/auth.ts'
import { withTx } from '../../server/src/db.ts'
import { nowIso } from '../../server/src/repo.ts'
import { startSidecar } from '../src/index.ts'
import type { RunningSidecar } from '../src/index.ts'
import type { AgentEvent } from '../src/engine/port.ts'
import { KEY_ABSENT_MSG, SDK_ABSENT_MSG } from '../src/engine/sdk.ts'

const AGENT_EMAIL = 'pec-agent@rehearsal.demo'
const AGENT_PASSWORD = 'agent-pilot'

let env: TestEnv
let sidecar: RunningSidecar
let agentPersonId = 0
let P = ''

const MDL_CSV = [
  'doc_no,title,package,discipline,owner,current_rev,state,due_date',
  'TST-PR-201,Agent Sheet 1,PKG-A,Process,eor@t.co,A,in_work,2027-03-31',
  'TST-PR-202,Agent Sheet 2,PKG-A,Process,eor@t.co,A,in_work,2027-04-30',
].join('\r\n')

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
  // provision the agent person per the rehearsal-01 pattern: own person,
  // is_admin=0, coordinator-class grant (import.propose + intake.triage)
  agentPersonId = withTx(env.db, () => env.repo.insert('person', {
    name: 'PEC Agent', email: AGENT_EMAIL, passwordHash: hashPassword(AGENT_PASSWORD),
    isAdmin: false, discipline: null, createdAt: nowIso(),
  }))
  withTx(env.db, () => {
    env.db.prepare('INSERT INTO project_role (project_id, person_id, role) VALUES (?, ?, ?)')
      .run(env.projectId, agentPersonId, 'coordinator')
  })
  sidecar = await startSidecar({
    engine: 'stub', access: 'enumerated', session: 'hermetic', pecBaseUrl: env.base, port: 0,
    agentEmail: AGENT_EMAIL, agentPassword: AGENT_PASSWORD,
  })
})
after(async () => {
  await sidecar?.close()
  await env?.close()
})

async function turn(message: string, extra: Record<string, unknown> = {}): Promise<AgentEvent[]> {
  const res = await fetch(`http://127.0.0.1:${sidecar.port}/agent/messages`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ pid: env.projectId, message, ...extra }),
  })
  assert.equal(res.status, 200)
  const body = await res.json() as { events: AgentEvent[] }
  return body.events
}

const resultEvent = (events: AgentEvent[]): Extract<AgentEvent, { type: 'act:result' }> => {
  const e = events.find((x) => x.type === 'act:result')
  assert.ok(e, `expected an act:result in ${JSON.stringify(events)}`)
  return e as Extract<AgentEvent, { type: 'act:result' }>
}

test('health reports the stub engine, no-egress class, and the agent identity (WF-8)', async () => {
  const res = await fetch(`http://127.0.0.1:${sidecar.port}/agent/health`)
  assert.equal(res.status, 200)
  const h = await res.json() as Record<string, unknown>
  assert.equal(h.ok, true)
  assert.equal(h.engine, 'stub')
  assert.equal(h.egress, 'none')
  assert.equal(h.configured, true)
  assert.deepEqual(h.agent, { name: 'PEC Agent', email: AGENT_EMAIL })
})

test('full turn: CSV attachment ⇒ proposal created, attributed to the agent person, with a dry-run report', async () => {
  const events = await turn('please file this register', {
    attachment: { name: 'mdl-agent.csv', text: MDL_CSV },
  })
  const r = resultEvent(events)
  assert.equal(r.ok, true, r.summary)
  const payload = r.payload as { ref: string; state: string; report: { accepted: number }; adminLink: string }
  assert.match(payload.ref, /^IPR-/)
  assert.equal(payload.state, 'ready_for_review')
  assert.equal(payload.report.accepted, 2, 'dry-run report present with counts')
  assert.equal(payload.adminLink, `/p/${env.projectId}/admin`, 'deep link to the human accept/apply')

  // createdBy = the agent person (WF-8) — verified through the human admin session
  const admin = await env.as('admin@t.co')
  const list = await admin.get(`${P}/import-proposals`)
  const mine = list.body.find((p: { ref: string }) => p.ref === payload.ref)
  assert.equal(mine.createdBy, agentPersonId)

  // history attributes the agent person
  const hist = await admin.get(`${P}/history/import_proposal/${mine.id}`)
  assert.equal(hist.status, 200)
  assert.equal(hist.body.every((h: { actorId: number }) => h.actorId === agentPersonId), true)
})

test('refresh turn recomputes the dry-run through the live route', async () => {
  const events = await turn('refresh IPR-0001')
  const r = resultEvent(events)
  assert.equal(r.ok, true, r.summary)
  assert.match(r.summary, /IPR-0001 dry-run refreshed/)
  assert.match(r.summary, /re-accept/, 'states the ruled voided-acceptance flow')
})

test('withdraw-own turn rejects the agent\'s own proposal with the reason recorded', async () => {
  const events = await turn('withdraw IPR-0001 because superseded by a fresh weekly file')
  const r = resultEvent(events)
  assert.equal(r.ok, true, r.summary)
  const admin = await env.as('admin@t.co')
  const list = await admin.get(`${P}/import-proposals`)
  const p = list.body.find((x: { ref: string }) => x.ref === 'IPR-0001')
  assert.equal(p.state, 'rejected')
  assert.equal(p.rejectedBy, agentPersonId)
  assert.match(p.rejectReason, /superseded by a fresh weekly file/)
})

test('seeded intake item triaged with grounds; the note carries the grounds; history attributes the agent', async () => {
  // seed an intake item as a human raiser
  const coord = await env.as('coord@t.co')
  const raised = await coord.post(`${P}/intake`, {
    statement: 'vendor data for the exchanger is late', quickType: 'action', log: 'internal',
  })
  assert.equal(raised.status, 200, JSON.stringify(raised.body))
  const ref: string = raised.body.ref

  const events = await turn(`triage ${ref} as parked: awaiting vendor data, revisit next week`)
  const r = resultEvent(events)
  assert.equal(r.ok, true, r.summary)

  const admin = await env.as('admin@t.co')
  const queue = await admin.get(`${P}/intake?state=dispositioned`)
  const item = queue.body.find((i: { ref: string }) => i.ref === ref)
  assert.equal(item.disposition, 'parked')
  assert.equal(item.dispositionNote, 'awaiting vendor data, revisit next week')

  const hist = await admin.get(`${P}/history/intake_item/${item.id}`)
  const agentActs = hist.body.filter((h: { actorId: number; kind: string }) => h.actorId === agentPersonId)
  assert.ok(agentActs.some((h: { kind: string }) => h.kind === 'dispositioned'),
    'the disposition is attributed to the agent person (WF-8)')
})

test('RBAC pin: the agent\'s direct accept attempt is refused 403 by the server itself', async () => {
  // file a proposal for the boundary exercise
  const filed = await turn('file this too', { attachment: { name: 'mdl2.csv', text: MDL_CSV } })
  const payload = resultEvent(filed).payload as { id: number; ref: string; version: number }

  // log in AS the agent person directly (raw session, no client guards in the way)
  const login = await fetch(`${env.base}/api/auth/login`, {
    method: 'POST', headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ email: AGENT_EMAIL, password: AGENT_PASSWORD }),
  })
  const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0]!
  const admin = await env.as('admin@t.co')
  const current = await admin.get(`${P}/import-proposals/${payload.id}`)

  const attempt = await fetch(`${env.base}${P}/import-proposals/${payload.id}/accept`, {
    method: 'POST', headers: { cookie, 'content-type': 'application/json' },
    body: JSON.stringify({ version: current.body.version, sha256: current.body.sourceSha256 }),
  })
  assert.equal(attempt.status, 403, 'pec RBAC refuses the agent accept — K-DOMAIN-3 enforcement is the server')

  // the human boundary stays intact end to end: the admin accepts + applies on the SAME server
  const accept = await admin.post(`${P}/import-proposals/${payload.id}/accept`,
    { version: current.body.version, sha256: current.body.sourceSha256 })
  assert.equal(accept.status, 200, JSON.stringify(accept.body))
  const apply = await admin.post(`${P}/import-proposals/${payload.id}/apply`,
    { version: accept.body.version })
  assert.equal(apply.status, 200, JSON.stringify(apply.body))
  assert.equal(apply.body.state, 'applied')
  assert.equal(apply.body.appliedBy, env.people['admin@t.co'])
})

test('unconfigured sidecar starts, reports unconfigured, and refuses messages with 503 AGENT_NOT_CONFIGURED', async () => {
  const bare = await startSidecar({
    engine: 'stub', access: 'enumerated', session: 'hermetic', pecBaseUrl: env.base, port: 0, agentEmail: null, agentPassword: null,
  })
  try {
    const health = await fetch(`http://127.0.0.1:${bare.port}/agent/health`)
    const h = await health.json() as Record<string, unknown>
    assert.equal(h.configured, false)
    assert.equal(h.agent, null)
    const msg = await fetch(`http://127.0.0.1:${bare.port}/agent/messages`, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ pid: env.projectId, message: 'status' }),
    })
    assert.equal(msg.status, 503)
    const body = await msg.json() as { error: { code: string } }
    assert.equal(body.error.code, 'AGENT_NOT_CONFIGURED')
  } finally {
    await bare.close()
  }
})

test('engine sdk without its prerequisites fails at startup with a documented drop-in message', async () => {
  // deterministic regardless of the shell: the key is stripped for this test,
  // so the refusal is the key-absent message once the package is installed,
  // or the package-absent message where it is not — never a started sidecar
  const savedKey = process.env.ANTHROPIC_API_KEY
  delete process.env.ANTHROPIC_API_KEY
  try {
    await assert.rejects(
      startSidecar({ engine: 'sdk', access: 'enumerated', session: 'hermetic', pecBaseUrl: env.base, port: 0, agentEmail: null, agentPassword: null }),
      (e: unknown) => e instanceof Error && (e.message === SDK_ABSENT_MSG || e.message === KEY_ABSENT_MSG),
    )
  } finally {
    if (savedKey !== undefined) process.env.ANTHROPIC_API_KEY = savedKey
  }
})

test('history validation (D-PEC-21): shape, entry cap, and per-entry byte cap are enforced; valid history passes', async () => {
  const post = (body: unknown) => fetch(`http://127.0.0.1:${sidecar.port}/agent/messages`, {
    method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body),
  })
  const badCases: Array<[string, unknown]> = [
    ['non-array', { pid: env.projectId, message: 'status', history: 'earlier' }],
    ['wrong who', { pid: env.projectId, message: 'status', history: [{ who: 'model', text: 'hi' }] }],
    ['missing text', { pid: env.projectId, message: 'status', history: [{ who: 'you' }] }],
    ['over the entry cap', {
      pid: env.projectId, message: 'status',
      history: Array.from({ length: 41 }, () => ({ who: 'you', text: 'x' })),
    }],
    ['oversized entry', {
      pid: env.projectId, message: 'status',
      history: [{ who: 'you', text: 'x'.repeat(8 * 1024 + 1) }],
    }],
  ]
  for (const [label, body] of badCases) {
    const res = await post(body)
    assert.equal(res.status, 400, `history case must be refused: ${label}`)
    const parsed = await res.json() as { error: { code: string } }
    assert.equal(parsed.error.code, 'BAD_REQUEST', label)
  }
  // valid history passes validation end to end (the stub ignores it by design — disclosed in D-PEC-21)
  const ok = await post({
    pid: env.projectId, message: 'status',
    history: [{ who: 'you', text: 'earlier question' }, { who: 'agent', text: '[read.register] earlier read' }],
  })
  assert.equal(ok.status, 200)
})
