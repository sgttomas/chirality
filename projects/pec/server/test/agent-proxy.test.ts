/**
 * Agent proxy routes (D-PEC-17): /api/projects/:pid/agent/{status,messages}.
 * Pins: RBAC (agent.direct — 401/403/404), the RV-21 same-origin guard on the
 * mutation route, 503 AGENT_UNAVAILABLE with no sidecar listening, faithful
 * forwarding to a fake loopback sidecar with the human cookie STRIPPED and the
 * server-side pid overwriting the client-sent pid, status relay, and the
 * 6 MiB payload cap.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createServer } from 'node:http'
import type { Server } from 'node:http'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'

let env: TestEnv
let P = ''

// fake loopback sidecar recording exactly what reaches it
interface SidecarSeen { method: string; path: string; headers: Record<string, unknown>; body: unknown }
let fake: Server
let fakePort = 0
const sidecarSeen: SidecarSeen[] = []
let fakeReply: { status: number; body: unknown } = { status: 200, body: { events: [] } }

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
  fake = createServer(async (req, res) => {
    const chunks: Buffer[] = []
    for await (const c of req) chunks.push(c as Buffer)
    let body: unknown = Buffer.concat(chunks).toString('utf8')
    try { body = JSON.parse(body as string) } catch { /* raw */ }
    sidecarSeen.push({ method: req.method ?? '', path: req.url ?? '', headers: { ...req.headers }, body })
    if (fakeReply.status >= 200 && fakeReply.status < 300 && typeof fakeReply.body === 'string') {
      res.writeHead(fakeReply.status, { 'content-type': 'text/event-stream; charset=utf-8' })
      res.end(fakeReply.body)
    } else {
      res.writeHead(fakeReply.status, { 'content-type': 'application/json' })
      res.end(JSON.stringify(fakeReply.body))
    }
  })
  await new Promise<void>((resolve) => fake.listen(0, '127.0.0.1', resolve))
  const addr = fake.address()
  fakePort = typeof addr === 'object' && addr ? addr.port : 0
})
after(async () => {
  delete process.env.PEC_AGENT_URL
  await new Promise<void>((r) => fake.close(() => r()))
  await env.close()
})

const pointAtFake = () => { process.env.PEC_AGENT_URL = `http://127.0.0.1:${fakePort}` }
const pointAtNothing = () => { process.env.PEC_AGENT_URL = 'http://127.0.0.1:1' }

test('401 unauthenticated', async () => {
  pointAtFake()
  const res = await fetch(`${env.base}${P}/agent/status`)
  assert.equal(res.status, 401)
})

test('403 for members without agent.direct (contributor, document_controller); 200-path for coordinator', async () => {
  pointAtFake()
  const ic = await env.as('ic@t.co')
  assert.equal((await ic.get(`${P}/agent/status`)).status, 403)
  assert.equal((await ic.post(`${P}/agent/messages`, { message: 'hi' })).status, 403)
  // GOV MINOR-2: document_controller proposes imports but may NOT direct the agent
  const dc = await env.as('dc@t.co')
  const dcRes = await dc.get(`${P}/agent/status`)
  assert.equal(dcRes.status, 403)
  assert.match(dcRes.body.error.message, /agent.direct/)
  // a role that holds agent.direct passes the gate (the fake answers)
  const coord = await env.as('coord@t.co')
  assert.equal((await coord.get(`${P}/agent/status`)).status, 200)
})

test('404 wrong project', async () => {
  pointAtFake()
  const admin = await env.as('admin@t.co')
  const res = await admin.get('/api/projects/9999/agent/status')
  assert.equal(res.status, 404)
})

test('cross-origin POST is refused 403 (RV-21) before any forwarding', async () => {
  pointAtFake()
  const pm = await env.as('pm@t.co')
  // authed cookie but a foreign Origin
  const login = await fetch(`${env.base}/api/auth/login`, {
    method: 'POST', headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ email: 'pm@t.co', password: 'pilot' }),
  })
  const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0]!
  sidecarSeen.length = 0
  const res = await fetch(`${env.base}${P}/agent/messages`, {
    method: 'POST',
    headers: { cookie, 'content-type': 'application/json', origin: 'https://evil.example.com' },
    body: JSON.stringify({ message: 'hi' }),
  })
  assert.equal(res.status, 403)
  const body = await res.json() as { error: { code: string } }
  assert.equal(body.error.code, 'CROSS_ORIGIN')
  assert.equal(sidecarSeen.length, 0, 'nothing reached the sidecar')
  void pm
})

test('503 AGENT_UNAVAILABLE when no sidecar listens', async () => {
  pointAtNothing()
  const pm = await env.as('pm@t.co')
  const res = await pm.get(`${P}/agent/status`)
  assert.equal(res.status, 503)
  assert.equal(res.body.error.code, 'AGENT_UNAVAILABLE')
  const msg = await pm.post(`${P}/agent/messages`, { message: 'hi' })
  assert.equal(msg.status, 503)
  assert.equal(msg.body.error.code, 'AGENT_UNAVAILABLE')
})

test('forwarding: harness SSE streams, body is relayed, cookie stripped, and server pid wins', async () => {
  pointAtFake()
  fakeReply = { status: 200, body: 'event: turn.started\ndata: {"engine":"sdk"}\n\nevent: model.delta\ndata: {"text":"ok"}\n\nevent: turn.completed\ndata: {}\n\n' }
  sidecarSeen.length = 0
  const login = await fetch(`${env.base}/api/auth/login`, {
    method: 'POST', headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ email: 'pm@t.co', password: 'pilot' }),
  })
  const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0]!
  const res = await fetch(`${env.base}${P}/agent/messages`, {
    method: 'POST',
    headers: { cookie, origin: env.base, 'content-type': 'application/json', accept: 'text/event-stream' },
    body: JSON.stringify({ message: 'status', pid: 424242, context: { route: '/p/1/overview', records: [] } }),
  })
  assert.equal(res.status, 200)
  assert.match(res.headers.get('content-type') ?? '', /^text\/event-stream/)
  const stream = await res.text()
  assert.match(stream, /event: turn\.started/)
  assert.match(stream, /event: model\.delta/)
  assert.match(stream, /event: turn\.completed/)

  assert.equal(sidecarSeen.length, 1)
  const seen = sidecarSeen[0]!
  assert.equal(seen.method, 'POST')
  assert.equal(seen.path, '/agent/messages')
  assert.equal((seen.body as { message: string }).message, 'status')
  assert.deepEqual((seen.body as { context: unknown }).context, { route: '/p/1/overview', records: [] })
  // the client-sent pid was overwritten server-side with the authed project
  assert.equal((seen.body as { pid: number }).pid, env.projectId)
  // NO cookie header reached the fake sidecar — the human session never leaves the server
  assert.equal(seen.headers.cookie, undefined, 'cookie stripped')
  assert.equal(seen.headers.authorization, undefined)
  assert.equal(seen.headers.accept, 'text/event-stream')
})

test('sidecar non-2xx JSON is relayed with its status', async () => {
  pointAtFake()
  fakeReply = { status: 503, body: { error: { code: 'AGENT_NOT_CONFIGURED', message: 'set PEC_AGENT_EMAIL' } } }
  const pm = await env.as('pm@t.co')
  const res = await pm.post(`${P}/agent/messages`, { message: 'hi' })
  assert.equal(res.status, 503)
  assert.equal(res.body.error.code, 'AGENT_NOT_CONFIGURED')
  fakeReply = { status: 200, body: { events: [] } }
})

test('payloads over the 6 MiB cap are refused, never forwarded', async () => {
  pointAtFake()
  sidecarSeen.length = 0
  const pm = await env.as('pm@t.co')
  const big = 'x'.repeat(6 * 1024 * 1024 + 1024)
  const res = await pm.post(`${P}/agent/messages`, { message: big })
  assert.equal(res.status, 413)
  assert.equal(res.body.error.code, 'PAYLOAD_TOO_LARGE')
  assert.equal(sidecarSeen.length, 0, 'nothing reached the sidecar')
})

test('message timeout (D-PEC-21): default 300 000 ms, env-overridable per request, invalid values refused', async () => {
  const { messageTimeoutFromEnv } = await import('../src/agent-proxy.ts')
  assert.equal(messageTimeoutFromEnv({}), 300_000)
  assert.equal(messageTimeoutFromEnv({ PEC_AGENT_MESSAGE_TIMEOUT_MS: '120000' }), 120_000)
  for (const bad of ['0', '-5', 'soon', '1.5']) {
    assert.throws(
      () => messageTimeoutFromEnv({ PEC_AGENT_MESSAGE_TIMEOUT_MS: bad }),
      (e: unknown) => (e as { status?: number; code?: string }).status === 500
        && (e as { code?: string }).code === 'AGENT_MISCONFIGURED',
      `must refuse: ${bad}`,
    )
  }
})
