/**
 * D-PEC-56 production project-adapter path.
 *
 * Proves the production entrypoint owns no model loop, executes deterministic
 * acts under the person-bound PEC identity, and structurally/RBAC-denies
 * human-only acts.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { chmod, mkdtemp, writeFile } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { createTestEnv } from '../../server/test/harness.ts'
import type { TestEnv } from '../../server/test/harness.ts'
import { hashPassword } from '../../server/src/auth.ts'
import { withTx } from '../../server/src/db.ts'
import { nowIso } from '../../server/src/repo.ts'
import { startProjectAdapter } from '../src/index.ts'
import type { RunningProjectAdapter } from '../src/index.ts'

const AGENT_EMAIL = 'pec-runtime-adapter@rehearsal.demo'
const AGENT_PASSWORD = 'adapter-pilot'
const ADAPTER_TOKEN = 'test-project-adapter-token-000000000001'

let env: TestEnv
let adapter: RunningProjectAdapter
let agentPersonId = 0
let P = ''

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
  agentPersonId = withTx(env.db, () => env.repo.insert('person', {
    name: 'PEC Runtime Adapter',
    email: AGENT_EMAIL,
    passwordHash: hashPassword(AGENT_PASSWORD),
    isAdmin: false,
    discipline: null,
    createdAt: nowIso(),
  }))
  withTx(env.db, () => {
    env.db.prepare('INSERT INTO project_role (project_id, person_id, role) VALUES (?, ?, ?)')
      .run(env.projectId, agentPersonId, 'coordinator')
  })
  const tokenDirectory = await mkdtemp(join(tmpdir(), 'pec-adapter-token-'))
  const adapterTokenFile = join(tokenDirectory, 'adapter.token')
  await writeFile(adapterTokenFile, `${ADAPTER_TOKEN}\n`, 'utf8')
  await chmod(adapterTokenFile, 0o600)
  adapter = await startProjectAdapter({
    access: 'enumerated',
    pecBaseUrl: env.base,
    port: 0,
    adapterTokenFile,
    agentEmail: AGENT_EMAIL,
    agentPassword: AGENT_PASSWORD,
  })
})

after(async () => {
  await adapter.close()
  await env.close()
})

async function execute(act: string, input: unknown = {}): Promise<Response> {
  return fetch(`http://127.0.0.1:${adapter.port}/adapter/execute`, {
    method: 'POST',
    headers: {
      authorization: `Bearer ${ADAPTER_TOKEN}`,
      'content-type': 'application/json',
    },
    body: JSON.stringify({ pid: env.projectId, act, input }),
  })
}

test('health describes only the deterministic adapter and person-bound identity', async () => {
  const denied = await fetch(`http://127.0.0.1:${adapter.port}/adapter/health`)
  assert.equal(denied.status, 401)
  const response = await fetch(`http://127.0.0.1:${adapter.port}/adapter/health`, {
    headers: { authorization: `Bearer ${ADAPTER_TOKEN}` },
  })
  assert.equal(response.status, 200)
  const health = await response.json() as Record<string, unknown>
  assert.equal(health.service, 'pec-project-adapter')
  assert.equal(health.schemaVersion, 'pec.adapter/v1')
  assert.equal(health.configured, true)
  assert.deepEqual(health.agent, { name: 'PEC Runtime Adapter', email: AGENT_EMAIL })
  assert.equal('engine' in health, false)
  assert.equal('model' in health, false)
  assert.equal('session' in health, false)
  assert.equal('delegation' in health, false)
})

test('retired production agent-loop routes return 410 and never execute a turn', async () => {
  for (const [method, path] of [
    ['GET', '/agent/health'],
    ['POST', '/agent/messages'],
  ] as const) {
    const response = await fetch(`http://127.0.0.1:${adapter.port}${path}`, {
      method,
      ...(method === 'POST'
        ? { headers: { 'content-type': 'application/json' }, body: JSON.stringify({ message: 'status' }) }
        : {}),
    })
    assert.equal(response.status, 410)
    const body = await response.json() as { error: { code: string } }
    assert.equal(body.error.code, 'AGENT_RUNTIME_MIGRATED')
  }
})

test('deterministic enumerated act executes through the PEC RBAC client', async () => {
  const coordinator = await env.as('coord@t.co')
  const raised = await coordinator.post(`${P}/intake`, {
    statement: 'scratch adapter visibility check',
    quickType: 'action',
    log: 'internal',
  })
  assert.equal(raised.status, 200)

  const response = await execute('intake.summary')
  assert.equal(response.status, 200)
  const result = await response.json() as { kind: string; act: string; payload?: { open?: unknown[] } }
  assert.equal(result.kind, 'result')
  assert.equal(result.act, 'intake.summary')
  assert.ok((result.payload?.open?.length ?? 0) >= 1)
})

test('human-only acts are absent from dispatch and cause no PEC mutation', async () => {
  const beforeHistory = Number((env.db.prepare('SELECT COUNT(*) AS n FROM history_entry').get() as { n: number }).n)
  const beforeAudit = Number((env.db.prepare('SELECT COUNT(*) AS n FROM audit_event').get() as { n: number }).n)
  for (const act of [
    'import.accept',
    'import.apply',
    'import.force',
    'approval.outcome',
    'decision.outcome',
    'check.accept',
    'condition.waive',
    'issue.record',
    'access.change',
    'consequence.close',
  ]) {
    const response = await execute(act, { id: 1, force: true })
    assert.equal(response.status, 403, act)
    const body = await response.json() as { error: { code: string } }
    assert.equal(body.error.code, 'AGENT_FORBIDDEN_ACT', act)
  }
  assert.equal(Number((env.db.prepare('SELECT COUNT(*) AS n FROM history_entry').get() as { n: number }).n), beforeHistory)
  assert.equal(Number((env.db.prepare('SELECT COUNT(*) AS n FROM audit_event').get() as { n: number }).n), beforeAudit)
})

test('PEC RBAC independently denies import acceptance to the adapter person', async () => {
  const proposal = await execute('import.propose', {
    filename: 'scratch-mdl.csv',
    contract: 'mdl',
    csv: [
      'doc_no,title,package,discipline,owner,current_rev,state,due_date',
      'TST-ADAPTER-001,Adapter proposal,PKG-A,Process,eor@t.co,A,in_work,2027-08-01',
    ].join('\n'),
  })
  assert.equal(proposal.status, 200)
  const result = await proposal.json() as { kind: string; payload?: { id?: number } }
  assert.equal(result.kind, 'result')
  const id = Number(result.payload?.id)
  assert.ok(id > 0)

  const login = await fetch(`${env.base}/api/auth/login`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ email: AGENT_EMAIL, password: AGENT_PASSWORD }),
  })
  const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0]!
  const detail = await fetch(`${env.base}${P}/import-proposals/${id}`, { headers: { cookie } })
  const current = await detail.json() as { version: number; sourceSha256: string }
  const attempt = await fetch(`${env.base}${P}/import-proposals/${id}/accept`, {
    method: 'POST',
    headers: { cookie, 'content-type': 'application/json' },
    body: JSON.stringify({ version: current.version, sha256: current.sourceSha256 }),
  })
  assert.equal(attempt.status, 403)
  const body = await attempt.json() as { error: { code: string } }
  assert.equal(body.error.code, 'FORBIDDEN')
})
