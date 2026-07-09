/**
 * Reporting periods & coverage declarations (D-PEC-39). Pins:
 * - additive schema migration (coverage columns appear on pre-D-PEC-39 DBs);
 * - coverage is declared per proposal, shape-validated, never inferred;
 * - overlaps / gaps / undeclared applied imports are CAUGHT review signals,
 *   never schema-prevented, and applying never rewrites prior declarations;
 * - period-status figures come from timestamped app records, are Explain-shaped,
 *   name their coverage basis (PER-COV), and respect log visibility;
 * - the weekly standard report stays absent-honest without a period and gains
 *   issuance figures only when a period is explicitly declared.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { randomBytes } from 'node:crypto'
import { DatabaseSync } from 'node:sqlite'
import { openDb, withTx } from '../src/db.ts'
import { nowIso } from '../src/repo.ts'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'

let env: TestEnv
let P: string

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
})
after(async () => { await env.close() })

function mdlCsv(docNos: string[]): string {
  return [
    'doc_no,title,package,discipline,owner,current_rev,state,due_date',
    ...docNos.map((d) => `${d},Sheet ${d},PKG-A,Process,eor@t.co,A,in_work,2027-01-31`),
  ].join('\r\n')
}

/** create → accept → apply one proposal, sequentially (watermark discipline). */
async function applyProposal(csv: string, coverage?: { start: string; end: string }): Promise<number> {
  const admin = await env.as('admin@t.co')
  const cov = coverage ? `&coverage_start=${coverage.start}&coverage_end=${coverage.end}` : ''
  const created = await admin.postCsv(`${P}/import-proposals?contract=mdl${cov}`, csv)
  assert.equal(created.status, 200, JSON.stringify(created.body))
  assert.equal(created.body.state, 'ready_for_review')
  const accepted = await admin.post(`${P}/import-proposals/${created.body.id}/accept`,
    { version: created.body.version, sha256: created.body.sourceSha256 })
  assert.equal(accepted.status, 200, JSON.stringify(accepted.body))
  const applied = await admin.post(`${P}/import-proposals/${created.body.id}/apply`,
    { version: accepted.body.version, force: false })
  assert.equal(applied.status, 200, JSON.stringify(applied.body))
  assert.equal(applied.body.state, 'applied')
  return created.body.id as number
}

test('migration: a pre-D-PEC-39 import_proposal table gains the coverage columns additively', () => {
  const path = join(tmpdir(), `pec-mig-${randomBytes(6).toString('hex')}.db`)
  const old = new DatabaseSync(path)
  old.exec(`CREATE TABLE import_proposal (
    id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL, ref TEXT NOT NULL,
    contract TEXT NOT NULL, source_name TEXT, source_sha256 TEXT NOT NULL,
    source_bytes INTEGER NOT NULL, source_csv TEXT NOT NULL,
    state TEXT NOT NULL DEFAULT 'draft', basis_history_id INTEGER,
    dry_run_report TEXT, dry_run_at TEXT, accepted_by INTEGER, accepted_at TEXT,
    accepted_sha256 TEXT, rejected_by INTEGER, rejected_at TEXT, reject_reason TEXT,
    applied_by INTEGER, applied_at TEXT, apply_report TEXT,
    created_by INTEGER NOT NULL, created_at TEXT NOT NULL,
    version INTEGER NOT NULL DEFAULT 1
  )`)
  old.close()
  const db = openDb(path)
  const cols = (db.prepare('PRAGMA table_info(import_proposal)').all() as Array<{ name: string }>).map((c) => c.name)
  assert.ok(cols.includes('coverage_start'), 'coverage_start added')
  assert.ok(cols.includes('coverage_end'), 'coverage_end added')
  db.close()
})

test('coverage declarations are captured verbatim and shape-validated, never inferred', async () => {
  const dc = await env.as('dc@t.co')
  const withCov = await dc.postCsv(
    `${P}/import-proposals?contract=mdl&filename=w27.csv&coverage_start=2026-06-29&coverage_end=2026-07-05`,
    mdlCsv(['TST-CV-001']))
  assert.equal(withCov.status, 200, JSON.stringify(withCov.body))
  assert.equal(withCov.body.coverageStart, '2026-06-29')
  assert.equal(withCov.body.coverageEnd, '2026-07-05')
  // dry-run rolled back: coverage declaration alone imports nothing
  const n = env.db.prepare("SELECT COUNT(*) AS n FROM deliverable WHERE doc_no = 'TST-CV-001'").get() as { n: number }
  assert.equal(n.n, 0)

  const without = await dc.postCsv(`${P}/import-proposals?contract=mdl`, mdlCsv(['TST-CV-001']))
  assert.equal(without.status, 200)
  assert.equal(without.body.coverageStart, null, 'no declaration → null, never inferred')

  const oneSided = await dc.postCsv(`${P}/import-proposals?contract=mdl&coverage_start=2026-06-29`, mdlCsv(['TST-CV-001']))
  assert.equal(oneSided.status, 400)
  const badShape = await dc.postCsv(`${P}/import-proposals?contract=mdl&coverage_start=06/29/2026&coverage_end=2026-07-05`, mdlCsv(['TST-CV-001']))
  assert.equal(badShape.status, 400)
  const inverted = await dc.postCsv(`${P}/import-proposals?contract=mdl&coverage_start=2026-07-05&coverage_end=2026-06-29`, mdlCsv(['TST-CV-001']))
  assert.equal(inverted.status, 400)
})

test('overlaps, gaps, and undeclared applied imports are caught as review signals — never prevented', async () => {
  const idA = await applyProposal(mdlCsv(['TST-CV-101']), { start: '2026-06-01', end: '2026-06-07' })
  await applyProposal(mdlCsv(['TST-CV-102']), { start: '2026-06-15', end: '2026-06-21' })
  const idC = await applyProposal(mdlCsv(['TST-CV-103']), { start: '2026-06-05', end: '2026-06-10' }) // overlaps A; retro vs A
  await applyProposal(mdlCsv(['TST-CV-104'])) // applied undeclared

  const admin = await env.as('admin@t.co')
  const res = await admin.get(`${P}/coverage`)
  assert.equal(res.status, 200, JSON.stringify(res.body))

  assert.equal(res.body.signals.overlaps.ruleId, 'COV-OVERLAP')
  assert.equal(res.body.signals.overlaps.value, 1, 'A and C overlap; B is disjoint')
  assert.equal(res.body.signals.gaps.ruleId, 'COV-GAP')
  assert.equal(res.body.signals.gaps.value, 1, 'gap between C(..06-10) and B(06-15..)')
  assert.equal(res.body.signals.undeclaredApplied.value, 1)
  assert.ok(res.body.signals.overlaps.contributing.length >= 2, 'overlap signal carries proposal refs')
  assert.ok(res.body.signals.overlaps.contributing.every((c: { recordType: string }) => c.recordType === 'import_proposal'))

  const kinds = res.body.reviewItems.map((i: { kind: string }) => i.kind).sort()
  assert.deepEqual(kinds, ['gap', 'overlap', 'undeclared'])
  const overlapItem = res.body.reviewItems.find((i: { kind: string }) => i.kind === 'overlap')
  assert.match(overlapItem.detail, /retroactive correction/)

  // no destructive mutation: the earlier declaration is untouched by the later overlap
  const a = await admin.get(`${P}/import-proposals/${idA}`)
  assert.equal(a.body.coverageStart, '2026-06-01')
  assert.equal(a.body.coverageEnd, '2026-06-07')
  assert.equal(a.body.state, 'applied')
  const c = await admin.get(`${P}/import-proposals/${idC}`)
  assert.equal(c.body.state, 'applied', 'overlapping window applied — caught, not blocked')
})

test('period-status figures come from timestamped records, name their coverage basis, and respect log visibility', async () => {
  withTx(env.db, () => {
    env.repo.insert('issue_event', {
      projectId: env.projectId, ref: 'IE-CV-1', revisionId: env.revisionId, purpose: 'IFR',
      transmittalRef: 'TR-CV-1', issuedAt: '2026-06-03T12:00:00Z', issuedBy: env.people['dc@t.co'],
    })
    env.repo.insert('issue_event', {
      projectId: env.projectId, ref: 'IE-CV-0', revisionId: env.revisionId, purpose: 'IFR',
      transmittalRef: 'TR-CV-0', issuedAt: '2026-05-27T12:00:00Z', issuedBy: env.people['dc@t.co'],
    })
    env.repo.insert('work_item', {
      projectId: env.projectId, ref: 'WI-CV-1', title: 'closed in window', kind: 'action', log: 'internal',
      anchorType: 'deliverable', anchorId: env.deliverableId, ownerId: env.people['eor@t.co'],
      state: 'closed', closedAt: '2026-06-05T09:00:00Z', createdBy: env.people['eor@t.co'], createdAt: '2026-06-01T09:00:00Z',
    })
    env.repo.insert('hold', {
      projectId: env.projectId, ref: 'HLD-CV-1', title: 'raised in window', cause: 'information_missing',
      ownerId: env.people['lead@t.co'], raisedBy: env.people['lead@t.co'],
      raisedAt: '2026-06-02T08:00:00Z', state: 'active', log: 'internal',
    })
  })

  const admin = await env.as('admin@t.co')
  const res = await admin.get(`${P}/period-status?start=2026-06-01&end=2026-06-07`)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.deepEqual(res.body.period, { start: '2026-06-01', end: '2026-06-07' })
  assert.equal(res.body.figures.issuances.ruleId, 'PER-ISSUED')
  assert.equal(res.body.figures.issuances.value, 1)
  assert.equal(res.body.figures.issuances.contributing[0].recordType, 'issue_event')
  assert.equal(res.body.figures.issuanceDelta.ruleId, 'PER-ISSUED-DELTA')
  assert.equal(res.body.figures.issuanceDelta.value, 0, '1 in window minus 1 in preceding window (2026-05-25..05-31)')
  assert.equal(res.body.figures.workItemsClosed.value, 1)
  assert.equal(res.body.figures.holdsRaised.value, 1)
  // coverage basis: the applied 2026-06-01..07 and 2026-06-05..10 mdl declarations intersect
  assert.equal(res.body.coverageBasis.declared.ruleId, 'PER-COV')
  assert.ok(res.body.coverageBasis.declared.value >= 2)
  assert.deepEqual(res.body.coverageBasis.coveredContracts, ['mdl'])
  // absent figures are named absent, not synthesized
  assert.ok(res.body.absent.some((a: { figure: string }) => /percent complete/.test(a.figure)))

  // log visibility: the viewer (package+client logs) must not see internal-log records
  const viewer = await env.as('viewer@t.co')
  const vres = await viewer.get(`${P}/period-status?start=2026-06-01&end=2026-06-07`)
  assert.equal(vres.status, 200)
  assert.equal(vres.body.figures.workItemsClosed.value, 0, 'internal work item hidden from viewer')
  assert.equal(vres.body.figures.holdsRaised.value, 0, 'internal hold hidden from viewer')
  assert.equal(vres.body.figures.issuances.value, 1, 'issue events are not log-scoped')

  // an uncovered window says so rather than failing
  const far = await admin.get(`${P}/period-status?start=2027-01-01&end=2027-01-07`)
  assert.equal(far.status, 200)
  assert.equal(far.body.coverageBasis.declared.value, 0)
  assert.match(far.body.coverageBasis.declared.detail, /no applied import coverage declaration/)

  // malformed periods refuse
  assert.equal((await admin.get(`${P}/period-status?start=2026-06-01`)).status, 400)
  assert.equal((await admin.get(`${P}/period-status?start=2026-06-07&end=2026-06-01`)).status, 400)
})

test('weekly report: absent-honest without a period; issuance figures only under a declared period', async () => {
  const admin = await env.as('admin@t.co')
  const bare = await admin.get(`${P}/reports/standard/weekly-project-status`)
  assert.equal(bare.status, 200)
  assert.ok(bare.body.absent.some((a: { figure: string }) => a.figure === 'issued this period'))
  assert.equal(bare.body.sections.issuancesThisPeriod, undefined)

  const withPeriod = await admin.get(`${P}/reports/standard/weekly-project-status?groupBy=discipline&period_start=2026-06-01&period_end=2026-06-07`)
  assert.equal(withPeriod.status, 200, JSON.stringify(withPeriod.body))
  assert.equal(withPeriod.body.sections.issuancesThisPeriod.ruleId, 'PER-ISSUED')
  assert.equal(withPeriod.body.sections.issuancesThisPeriod.value, 1)
  assert.equal(withPeriod.body.sections.periodCoverage.declared.ruleId, 'PER-COV')
  assert.ok(!withPeriod.body.absent.some((a: { figure: string }) => a.figure === 'issued this period'),
    'period-scoped issuances are no longer absent under a declared period')
  assert.ok(withPeriod.body.absent.some((a: { figure: string }) => /percent complete/.test(a.figure)),
    'percent complete stays absent until contract v2')
  assert.ok(withPeriod.body.basis.some((b: { ruleId?: string }) => b.ruleId === 'PER-COV'), 'report basis names the coverage rule')
  assert.match(withPeriod.body.markdown, /Issuances this period: 1/)

  // a one-sided period refuses rather than inferring the other bound
  assert.equal((await admin.get(`${P}/reports/standard/weekly-project-status?period_start=2026-06-01`)).status, 400)
})

test('history records the declared coverage on the proposal (append-only trail)', async () => {
  const admin = await env.as('admin@t.co')
  const created = await admin.postCsv(
    `${P}/import-proposals?contract=mdl&coverage_start=2026-07-06&coverage_end=2026-07-12`, mdlCsv(['TST-CV-201']))
  assert.equal(created.status, 200)
  const hist = await admin.get(`${P}/history/import_proposal/${created.body.id}`)
  assert.equal(hist.status, 200)
  const createdEntry = (hist.body as Array<{ kind: string; summary: string }>).find((h) => h.kind === 'created')
  assert.ok(createdEntry, 'created history entry exists')
  assert.match(createdEntry!.summary, /coverage 2026-07-06\.\.2026-07-12/)
  // hygiene: withdraw to keep later watermark expectations clean
  const rej = await admin.post(`${P}/import-proposals/${created.body.id}/reject`,
    { version: created.body.version, reason: 'test hygiene withdrawal' })
  assert.equal(rej.status, 200)
})
