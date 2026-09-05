/**
 * D-PEC-20 evidence driver (2026-07-06): enumerated-vs-broad capture on a
 * hermetic scratch basis (server/test/harness.ts temp DB + seeded cast),
 * per the packet's verification plan. Same questions on both bases, plus
 * boundary refusals under 'broad'. Direct acts-layer invocation with egress
 * 'model-provider' — the exact seam the SDK engine drives; no ANTHROPIC_API_KEY
 * exists in this environment, so no model session occurs (disclosed).
 */

const REPO = '/Users/ryan/ai-env/projects/chirality'
const OUT = process.argv[2]
if (!OUT) { console.error('usage: node dpec20-evidence.ts <outdir>'); process.exit(1) }

import { mkdirSync, writeFileSync, existsSync, rmSync } from 'node:fs'
import { join } from 'node:path'
import { createHash } from 'node:crypto'

const { createTestEnv } = await import(`${REPO}/projects/pec/server/test/harness.ts`)
const { hashPassword } = await import(`${REPO}/projects/pec/server/src/auth.ts`)
const { withTx } = await import(`${REPO}/projects/pec/server/src/db.ts`)
const { nowIso } = await import(`${REPO}/projects/pec/server/src/repo.ts`)
const { PecAgentClient, AgentClientError } = await import(`${REPO}/projects/pec/agent-sidecar/src/pec-client.ts`)
const { bindActs } = await import(`${REPO}/projects/pec/agent-sidecar/src/acts.ts`)
const { startSidecar } = await import(`${REPO}/projects/pec/agent-sidecar/src/index.ts`)

const AGENT_EMAIL = 'pec-agent@rehearsal.demo'
const AGENT_PASSWORD = 'agent-scratch-' + Math.random().toString(36).slice(2)

mkdirSync(OUT, { recursive: true })
const record: Record<string, unknown> = {}

const env = await createTestEnv()
const pid = env.projectId
const dbFile = (env.db as { name?: string }).name ?? null

// ---- basis prep (disclosed): agent person per the rehearsal-01 pattern;
// one intake item raised and one proposal filed by the HUMAN coordinator so
// inside-enumeration reads and the withdraw-of-others pin have subjects.
// No accept, no apply, no force, no disposition — by anyone.
const agentPersonId = withTx(env.db, () => env.repo.insert('person', {
  name: 'PEC Agent', email: AGENT_EMAIL, passwordHash: hashPassword(AGENT_PASSWORD),
  isAdmin: false, discipline: null, createdAt: nowIso(),
}))
withTx(env.db, () => {
  env.db.prepare('INSERT INTO project_role (project_id, person_id, role) VALUES (?, ?, ?)')
    .run(pid, agentPersonId, 'coordinator')
})
const coord = await env.as('coord@t.co')
const P = `/api/projects/${pid}`
const intakeRes = await coord.post(`${P}/intake`, {
  statement: 'Evidence scratch item: confirm vendor data need-by for PKG-A.',
  quickType: 'action',
})
if (intakeRes.status !== 200) throw new Error(`intake raise failed: ${JSON.stringify(intakeRes.body)}`)
const intakeId: number = intakeRes.body.id
const RISK_CSV = 'title,cause,consequence,probability,impact\nLate vendor data,Vendor backlog,Schedule slip,3,4'
const proposalRes = await coord.postCsv(`${P}/import-proposals?contract=risks&filename=risks-evidence.csv`, RISK_CSV)
if (proposalRes.status !== 200) throw new Error(`coord proposal failed: ${JSON.stringify(proposalRes.body)}`)
const foreignProposalId: number = proposalRes.body.id
record.basisPrep = {
  agentPerson: { id: agentPersonId, email: AGENT_EMAIL, is_admin: 0, role: 'coordinator' },
  humanCoordinatorActs: {
    intakeItem: { id: intakeId, ref: intakeRes.body.ref },
    foreignProposal: { id: foreignProposalId, ref: proposalRes.body.ref, contract: 'risks', state: proposalRes.body.state },
  },
  note: 'no accept/apply/force/disposition performed by anyone in this capture',
}

// ---- the agent client (one identity, both bases drive the same client) ----
const cfg = (access: 'enumerated' | 'broad') => ({
  engine: 'stub' as const, access, pecBaseUrl: env.base, port: 0,
  agentEmail: AGENT_EMAIL, agentPassword: AGENT_PASSWORD,
})
const client = new PecAgentClient(cfg('enumerated'))
const identity = await client.login()
record.agentIdentity = identity

type Outcome = { kind: string; ok?: boolean; summary?: string; reason?: string; payloadNote?: string }
const capture = async (fn: () => Promise<{ kind: string; ok?: boolean; summary?: string; reason?: string; payload?: unknown }>): Promise<Outcome> => {
  const r = await fn()
  const o: Outcome = { kind: r.kind }
  if (r.kind === 'result') { o.ok = r.ok; o.summary = r.summary }
  else o.reason = r.reason
  return o
}

// ---- same questions, both bases (egress 'model-provider' at the acts seam) ----
const QUESTIONS: Array<{ q: string; run: (acts: ReturnType<typeof bindActs>) => Promise<Outcome> }> = [
  { q: 'project overview', run: (a) => capture(() => a.projectOverview()) },
  { q: 'register deliverables', run: (a) => capture(() => a.readRegister({ register: 'deliverables' })) },
  { q: 'register risks', run: (a) => capture(() => a.readRegister({ register: 'risks' })) },
  { q: 'register tracker', run: (a) => capture(() => a.readRegister({ register: 'tracker' })) },
  { q: 'history deliverable #' + env.deliverableId, run: (a) => capture(() => a.recordHistory({ recordType: 'deliverable', id: env.deliverableId })) },
  { q: 'history intake_item #' + intakeId + ' (inside the D-T0-20 enumeration)', run: (a) => capture(() => a.recordHistory({ recordType: 'intake_item', id: intakeId })) },
  { q: 'explain revision #' + env.revisionId, run: (a) => capture(() => a.explainRevision({ id: env.revisionId })) },
  { q: 'sponsor brief report', run: (a) => capture(() => a.readReport({ report: 'sponsor-brief' })) },
  { q: 'screen.read deliverable #' + env.deliverableId, run: (a) => capture(() => a.readScreenContext({ route: `/p/${pid}/deliverables/${env.deliverableId}`, records: [{ recordType: 'deliverable', ref: 'TST-PR-001', id: env.deliverableId }] })) },
  { q: 'screen.read intake_item #' + intakeId + ' (inside the enumeration)', run: (a) => capture(() => a.readScreenContext({ route: `/p/${pid}/log`, records: [{ recordType: 'intake_item', ref: intakeRes.body.ref, id: intakeId }] })) },
  { q: 'proposal status (existing enumerated act)', run: (a) => capture(() => a.proposalStatus()) },
  { q: 'intake queue summary (existing enumerated act)', run: (a) => capture(() => a.intakeSummary()) },
]

const byBasis: Record<string, Array<{ question: string; outcome: Outcome }>> = {}
for (const access of ['enumerated', 'broad'] as const) {
  const acts = bindActs({ pid, egress: 'model-provider', access, client })
  const rows: Array<{ question: string; outcome: Outcome }> = []
  for (const { q, run } of QUESTIONS) rows.push({ question: q, outcome: await run(acts) })
  byBasis[access] = rows
}
record.egressNote = "egress 'model-provider' set at the acts seam (the exact context the SDK engine runs under); "
  + 'no ANTHROPIC_API_KEY exists in this environment, no model session occurred — live-LLM demonstration remains deferred'
writeFileSync(join(OUT, 'enumerated-vs-broad.json'), JSON.stringify(byBasis, null, 2))

// ---- boundary refusals under broad ----
const broadActs = bindActs({ pid, egress: 'model-provider', access: 'broad', client })
const boundary: Array<Record<string, unknown>> = []

const raw = (client as unknown as { request(m: string, p: string, b?: unknown): Promise<unknown> }).request.bind(client)
for (const [method, path, body] of [
  ['POST', `${P}/import-proposals/${foreignProposalId}/accept`, { version: 1, sha256: 'x' }],
  ['POST', `${P}/import-proposals/${foreignProposalId}/apply`, { version: 1 }],
  ['POST', `${P}/approval-records/1/outcome`, {}],
  ['POST', `${P}/approval-records/1/supersede`, {}],
  ['POST', `${P}/conditions/1/waive`, {}],
  ['POST', `${P}/import/mdl?force=true`, 'csv'],
  ['POST', `${P}/import-proposals/${foreignProposalId}/refresh`, { version: 1, force: true }],
] as const) {
  try {
    await raw(method, path, body)
    boundary.push({ act: `${method} ${path}`, outcome: 'ALLOWED — VIOLATION' })
  } catch (e) {
    boundary.push({
      act: `${method} ${path}`,
      outcome: 'refused before any network call',
      code: e instanceof AgentClientError ? e.code : String(e),
    })
  }
}
boundary.push({
  act: `triage ${intakeRes.body.ref} as converted (broad basis)`,
  outcome: await capture(() => broadActs.triageItem({ ref: intakeRes.body.ref, disposition: 'converted', grounds: 'evidence probe' })),
})
try {
  await client.withdrawOwn(pid, foreignProposalId, proposalRes.body.version, 'evidence probe — not the agent\'s proposal')
  boundary.push({ act: 'withdraw of the coordinator\'s proposal', outcome: 'ALLOWED — VIOLATION' })
} catch (e) {
  boundary.push({
    act: 'withdraw of the coordinator\'s proposal',
    outcome: 'refused before the reject call',
    code: e instanceof AgentClientError ? e.code : String(e),
  })
}
// RBAC pin: the server itself refuses the agent's direct accept (bypassing the client guard)
const loginRaw = await fetch(`${env.base}/api/auth/login`, {
  method: 'POST', headers: { 'content-type': 'application/json' },
  body: JSON.stringify({ email: AGENT_EMAIL, password: AGENT_PASSWORD }),
})
const agentCookie = (loginRaw.headers.get('set-cookie') ?? '').split(';')[0]
const directAccept = await fetch(`${env.base}${P}/import-proposals/${foreignProposalId}/accept`, {
  method: 'POST', headers: { 'content-type': 'application/json', cookie: agentCookie },
  body: JSON.stringify({ version: proposalRes.body.version, sha256: proposalRes.body.sourceSha256 }),
})
boundary.push({
  act: 'direct HTTP accept as the agent person (client guard bypassed)',
  outcome: `server refused HTTP ${directAccept.status}`,
  body: await directAccept.json(),
})
writeFileSync(join(OUT, 'boundary-refusals-under-broad.json'), JSON.stringify(boundary, null, 2))

// ---- health disclosure, both bases ----
const health: Record<string, unknown> = {}
for (const access of ['enumerated', 'broad'] as const) {
  const s = await startSidecar(cfg(access))
  health[access] = await (await fetch(`http://127.0.0.1:${s.port}/agent/health`)).json()
  await s.close()
}
writeFileSync(join(OUT, 'health-disclosure.json'), JSON.stringify(health, null, 2))

// ---- one full stub-engine HTTP turn (route wiring live; stub egress 'none' is basis-independent by design) ----
const s2 = await startSidecar(cfg('broad'))
const turn = await (await fetch(`http://127.0.0.1:${s2.port}/agent/messages`, {
  method: 'POST', headers: { 'content-type': 'application/json' },
  body: JSON.stringify({ pid, message: 'register deliverables' }),
})).json()
await s2.close()
writeFileSync(join(OUT, 'stub-turn-register-read.json'), JSON.stringify(turn, null, 2))

writeFileSync(join(OUT, 'capture-record.json'), JSON.stringify(record, null, 2))

await env.close()
if (dbFile && existsSync(dbFile)) {
  rmSync(dbFile)
  for (const suffix of ['-wal', '-shm']) if (existsSync(dbFile + suffix)) rmSync(dbFile + suffix)
  console.log(`scratch DB deleted: ${dbFile}`)
}
console.log('capture complete →', OUT)
