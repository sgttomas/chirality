/** Integration test harness: real HTTP server on an ephemeral port, temp DB, seeded cast. */

import { createServer } from 'node:http'
import type { Server } from 'node:http'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { randomBytes } from 'node:crypto'
import { openDb, withTx } from '../src/db.ts'
import type { Db } from '../src/db.ts'
import { buildRouter } from '../src/api.ts'
import { errorPayload, parseCookies, readBody, sendJson } from '../src/http.ts'
import { hashPassword } from '../src/auth.ts'
import { Repo, nowIso } from '../src/repo.ts'

export interface TestClient {
  get(path: string): Promise<{ status: number; body: any }>
  post(path: string, body?: unknown): Promise<{ status: number; body: any }>
  put(path: string, body?: unknown): Promise<{ status: number; body: any }>
  postCsv(path: string, csv: string): Promise<{ status: number; body: any }>
  personId: number
}

export interface TestEnv {
  db: Db
  repo: Repo
  base: string
  projectId: number
  packageId: number
  deliverableId: number
  revisionId: number
  people: Record<string, number>
  as(email: string): Promise<TestClient>
  close(): Promise<void>
}

export const CAST = [
  ['admin@t.co', 'Ada Admin', ['admin']],
  ['pm@t.co', 'Petra PM', ['pm']],
  ['coord@t.co', 'Cora Coordinator', ['coordinator']],
  ['lead@t.co', 'Lee Lead', ['package_lead']],
  ['eor@t.co', 'Eva Engineer', ['engineer_of_record']],
  ['checker@t.co', 'Chuck Checker', ['checker', 'contributor']],
  ['approver@t.co', 'Abe Approver', ['approver']],
  ['dc@t.co', 'Dana DocControl', ['document_controller']],
  ['ic@t.co', 'Ian Contributor', ['contributor']],
  ['viewer@t.co', 'Vera Viewer', ['viewer']],
] as const

export async function createTestEnv(): Promise<TestEnv> {
  const dbPath = join(tmpdir(), `pec-test-${randomBytes(6).toString('hex')}.db`)
  const db = openDb(dbPath)
  const repo = new Repo(db)

  const people: Record<string, number> = {}
  withTx(db, () => {
    for (const [email, name, _roles] of CAST) {
      people[email] = repo.insert('person', {
        name, email, passwordHash: hashPassword('pilot'),
        isAdmin: email === 'admin@t.co', discipline: null, createdAt: nowIso(),
      })
    }
  })
  const projectId = withTx(db, () => repo.insert('project', {
    code: 'TST', name: 'Test FEED', timezone: 'UTC',
    weekendDays: ['Sat', 'Sun'], holidays: [], thresholds: {}, config: {},
  }))
  withTx(db, () => {
    for (const [email, , roles] of CAST) {
      for (const role of roles) {
        db.prepare('INSERT INTO project_role (project_id, person_id, role) VALUES (?, ?, ?)')
          .run(projectId, people[email]!, role)
      }
    }
  })
  const packageId = withTx(db, () => repo.insert('package', {
    projectId, code: 'PKG-A', name: 'Process', leadId: people['lead@t.co'],
  }))
  const deliverableId = withTx(db, () => repo.insert('deliverable', {
    projectId, packageId, docNo: 'TST-PR-001', title: 'PFD', discipline: 'Process',
    deliverableType: 'drawing', ownerId: people['eor@t.co'], dueDate: '2027-06-30',
  }))
  const revisionId = withTx(db, () => repo.insert('revision', {
    projectId, deliverableId, revCode: 'A', state: 'in_work',
    createdAt: nowIso(), createdBy: people['admin@t.co'],
  }))

  const router = buildRouter(db)
  const server: Server = createServer(async (req, res) => {
    const url = new URL(req.url ?? '/', 'http://localhost')
    try {
      const match = router.match(req.method ?? 'GET', url.pathname)
      if (!match) { sendJson(res, 404, { error: { code: 'NOT_FOUND', message: url.pathname } }); return }
      const body = await readBody(req)
      const result = await match.handler({
        req, res, method: req.method ?? 'GET', path: url.pathname,
        params: match.params, query: url.searchParams, body,
        cookies: parseCookies(req.headers.cookie),
      })
      if (res.writableEnded) return
      if (!res.headersSent) {
        if (typeof result === 'string' && res.getHeader('content-type')) res.end(result)
        else sendJson(res, 200, result ?? { ok: true })
      } else res.end(typeof result === 'string' ? result : JSON.stringify(result))
    } catch (e) {
      const { status, body } = errorPayload(e)
      if (!res.headersSent) sendJson(res, status, body)
      else res.end()
    }
  })
  await new Promise<void>((resolve) => server.listen(0, resolve))
  const addr = server.address()
  const base = `http://127.0.0.1:${typeof addr === 'object' && addr ? addr.port : 0}`

  const clients = new Map<string, TestClient>()
  const as = async (email: string): Promise<TestClient> => {
    const cached = clients.get(email)
    if (cached) return cached
    const login = await fetch(`${base}/api/auth/login`, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ email, password: 'pilot' }),
    })
    if (login.status !== 200) throw new Error(`login failed for ${email}: ${login.status}`)
    const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0]!
    const call = async (method: string, path: string, body?: unknown, raw?: string) => {
      const res = await fetch(`${base}${path}`, {
        method,
        headers: {
          cookie,
          ...(raw != null ? { 'content-type': 'text/csv' } : body !== undefined ? { 'content-type': 'application/json' } : {}),
        },
        body: raw ?? (body !== undefined ? JSON.stringify(body) : undefined),
      })
      const text = await res.text()
      let parsed: any = text
      try { parsed = JSON.parse(text) } catch { /* csv/html responses stay text */ }
      return { status: res.status, body: parsed }
    }
    const client: TestClient = {
      personId: people[email]!,
      get: (p) => call('GET', p),
      post: (p, b) => call('POST', p, b),
      put: (p, b) => call('PUT', p, b),
      postCsv: (p, csv) => call('POST', p, undefined, csv),
    }
    clients.set(email, client)
    return client
  }

  return {
    db, repo, base, projectId, packageId, deliverableId, revisionId, people, as,
    close: () => new Promise((resolve) => server.close(() => resolve())),
  }
}

/** Convenience: walk a revision through check acceptance so approval/issue paths open up. */
export async function acceptCheckOn(env: TestEnv, revisionId: number): Promise<{ checkId: number }> {
  const P = `/api/projects/${env.projectId}`
  const lead = await env.as('lead@t.co')
  const checker = await env.as('checker@t.co')
  const created = await lead.post(`${P}/checks`, { revisionId, checkerId: env.people['checker@t.co'] })
  if (created.status !== 200) throw new Error(`check create failed: ${JSON.stringify(created.body)}`)
  const started = await checker.post(`${P}/checks/${created.body.id}/start`, { version: created.body.version })
  if (started.status !== 200) throw new Error(`check start failed: ${JSON.stringify(started.body)}`)
  const accepted = await checker.post(`${P}/checks/${created.body.id}/accept`, { version: started.body.version })
  if (accepted.status !== 200) throw new Error(`check accept failed: ${JSON.stringify(accepted.body)}`)
  return { checkId: created.body.id }
}
