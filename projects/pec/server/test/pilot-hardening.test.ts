/**
 * Pilot-hardening regression tests (2026-07-04). Each closes a confirmed finding from the
 * live probe workflow over the three P1 gaps that had implementation but no automated cover:
 *   - cross-project isolation (PEC-NFR-007): the history endpoint leaked another project's rows;
 *   - CSV importers (§16): decisions/risks/RAIL discarded the external id, so re-import duplicated;
 *   - load (PEC-NFR-003): derived views were O(deliverables × work-items) and blew the 2s budget.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { randomBytes } from 'node:crypto'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'
import { openDb, withTx } from '../src/db.ts'
import { Repo, nowIso } from '../src/repo.ts'
import type { Sx } from '../src/services/shared.ts'
import { overviewView, packagesView, deliverablesView } from '../src/services/views.ts'
import { planView } from '../src/services/plan.ts'
import { isoWeekOf } from '@pec/core'

// ============================================================================
// Cross-project isolation (PEC-NFR-007)
// ============================================================================

let env: TestEnv
let P: string
before(async () => { env = await createTestEnv(); P = `/api/projects/${env.projectId}` })
after(async () => { await env.close() })

test('PEC-NFR-007: the history endpoint does not leak another project\'s history rows', async () => {
  const A = env.projectId
  // A second project B with its own member and a deliverable carrying a marked history entry.
  const pmHash = (env.db.prepare('SELECT password_hash h FROM person WHERE email = ?')
    .get('pm@t.co') as { h: string }).h
  const bMember = withTx(env.db, () => env.repo.insert('person', {
    name: 'Bob B', email: `b-${randomBytes(3).toString('hex')}@t.co`,
    passwordHash: pmHash, isAdmin: 0, discipline: null, createdAt: nowIso(),
  }))
  const B = withTx(env.db, () => env.repo.insert('project', {
    code: `INTRUDE-${randomBytes(3).toString('hex')}`, name: 'B', timezone: 'UTC',
    weekendDays: ['Sat', 'Sun'], holidays: [], thresholds: {}, config: {},
  }))
  const bPkg = withTx(env.db, () => env.repo.insert('package', { projectId: B, code: 'PKG-B', name: 'B pkg', leadId: bMember }))
  const bDeliverable = withTx(env.db, () => env.repo.insert('deliverable', {
    projectId: B, packageId: bPkg, docNo: 'B-PR-001', title: 'B PFD',
    discipline: 'Process', deliverableType: 'drawing', ownerId: bMember, dueDate: '2027-06-30',
  }))
  withTx(env.db, () => env.repo.history({
    projectId: B, recordType: 'deliverable', recordId: bDeliverable,
    actorId: bMember, kind: 'created', summary: 'SECRET-B-HISTORY', payload: { secret: 'xyz' }, authorityRef: null,
  }))

  const pm = await env.as('pm@t.co') // member of A only
  const res = await pm.get(`/api/projects/${A}/history/deliverable/${bDeliverable}`)
  assert.ok(!JSON.stringify(res.body).includes('SECRET-B-HISTORY'),
    'project B history must not be reachable through a project A route')
  // The record is not in project A, so its history is empty for an A-scoped request.
  if (res.status === 200) assert.deepEqual(res.body, [])
  else assert.equal(res.status, 404)

  // A's own history still resolves (scoping did not over-restrict).
  const own = await pm.get(`${P}/history/deliverable/${env.deliverableId}`)
  assert.equal(own.status, 200)
  assert.ok(Array.isArray(own.body))
})

// ============================================================================
// Importers — decisions (§16)
// ============================================================================

test('decisions import: happy path, decided-requires-outcome, bad status/authority rejected', async () => {
  const e = await createTestEnv()
  try {
    const admin = await e.as('admin@t.co')
    const D = `/api/projects/${e.projectId}`
    const ok = await admin.postCsv(`${D}/import/decisions`,
      'decision_id,title,statement,authority,need_by,status,outcome,rationale\r\n' +
      'DEC-1,First,Proceed?,pm@t.co,2027-01-01,identified,,\r\n' +
      'DEC-2,Second,Which path?,pm@t.co,2027-01-01,decided,option_a,chosen\r\n')
    assert.equal(ok.body.accepted, 2, JSON.stringify(ok.body))
    assert.equal(ok.body.rejected.length, 0)

    const bad = await admin.postCsv(`${D}/import/decisions`,
      'decision_id,title,statement,authority,need_by,status,outcome\r\n' +
      'DEC-3,NoOutcome,Path?,pm@t.co,2027-01-01,decided,\r\n' +      // decided without outcome
      'DEC-4,BadStatus,Q?,pm@t.co,2027-01-01,frobnicated,\r\n' +      // unrecognized status
      'DEC-5,BadAuth,Q?,nobody@nowhere.co,2027-01-01,identified,\r\n') // authority matches nobody
    assert.equal(bad.body.accepted, 0)
    assert.equal(bad.body.rejected.length, 3, JSON.stringify(bad.body))
  } finally { await e.close() }
})

test('decisions import: external decision_id is preserved as the ref and re-import is idempotent (no duplicate)', async () => {
  const e = await createTestEnv()
  try {
    const admin = await e.as('admin@t.co')
    const D = `/api/projects/${e.projectId}`
    const r1 = await admin.postCsv(`${D}/import/decisions`,
      'decision_id,title,statement,authority,need_by,status\r\n' +
      'DEC-X,Title v1,Q?,pm@t.co,2027-01-01,identified\r\n')
    assert.equal(r1.body.accepted, 1)
    const dec = e.db.prepare('SELECT id, ref FROM decision WHERE project_id = ?').get(e.projectId) as { id: number; ref: string }
    assert.equal(dec.ref, 'DEC-X', 'the CSV decision_id is stored verbatim as the ref (idempotency key)')

    // Re-import the SAME decision_id: it must UPDATE the existing row, not create a second.
    const r2 = await admin.postCsv(`${D}/import/decisions`,
      'decision_id,title,statement,authority,need_by,status\r\n' +
      'DEC-X,Title v2,Q?,pm@t.co,2027-01-01,identified\r\n')
    assert.equal(r2.body.updated, 1, JSON.stringify(r2.body))
    assert.equal(r2.body.accepted, 0, 're-import must not create a duplicate')
    const count = e.db.prepare('SELECT COUNT(*) c FROM decision WHERE project_id = ?').get(e.projectId) as { c: number }
    assert.equal(count.c, 1, 'exactly one decision row for the external id')
    const title = e.db.prepare('SELECT title FROM decision WHERE project_id = ?').get(e.projectId) as { title: string }
    assert.equal(title.title, 'Title v2', 're-import applied the update')
  } finally { await e.close() }
})

test('decisions import: affected_refs links matching deliverables (unmatched tokens dropped), export round-trips', async () => {
  const e = await createTestEnv()
  try {
    const admin = await e.as('admin@t.co')
    const D = `/api/projects/${e.projectId}`
    withTx(e.db, () => e.repo.insert('deliverable', {
      projectId: e.projectId, packageId: e.packageId, docNo: 'TST-PR-002',
      title: 'P&ID', discipline: 'Process', ownerId: e.people['eor@t.co'], dueDate: '2027-06-30',
    }))
    const r = await admin.postCsv(`${D}/import/decisions`,
      'decision_id,title,statement,authority,need_by,status,affected_refs\r\n' +
      'DEC-L,Linked,Q?,pm@t.co,2027-01-01,identified,TST-PR-001;TST-PR-002;NOPE\r\n')
    assert.equal(r.body.accepted, 1, JSON.stringify(r.body))
    const dec = e.db.prepare('SELECT id FROM decision WHERE project_id = ? AND ref = ?').get(e.projectId, 'DEC-L') as { id: number }
    const links = e.db.prepare('SELECT record_id FROM decision_link WHERE decision_id = ?').all(dec.id)
    assert.equal(links.length, 2, 'two matching deliverables linked; unmatched "NOPE" dropped')

    // Export mirrors the import schema and a re-import of the export stays a single row.
    const exp = await admin.get(`${D}/export/decisions.csv`)
    assert.equal(exp.status, 200)
    for (const h of ['decision_id', 'title', 'statement', 'authority', 'need_by', 'status', 'outcome', 'rationale', 'decided_date', 'affected_refs']) {
      assert.ok((exp.body as string).split('\r\n')[0]!.includes(h), `export header missing ${h}`)
    }
    const r2 = await admin.postCsv(`${D}/import/decisions`, exp.body as string)
    assert.equal(r2.body.rejected.length, 0, JSON.stringify(r2.body))
    assert.equal(r2.body.updated, 1, 're-importing the export updates the same row')
  } finally { await e.close() }
})

// ============================================================================
// Importers — risks (§16)
// ============================================================================

test('risks import: happy path + linking + bounds/status validation; re-import is idempotent', async () => {
  const e = await createTestEnv()
  try {
    const admin = await e.as('admin@t.co')
    const D = `/api/projects/${e.projectId}`
    const ok = await admin.postCsv(`${D}/import/risks`,
      'risk_id,title,cause,consequence,owner,status,package,deliverable_ref,probability,impact,mitigation,need_by\r\n' +
      'RSK-1,Slippage,late vendor,delay,eor@t.co,treating,PKG-A,TST-PR-001,3,4,expedite,2027-03-03\r\n')
    assert.equal(ok.body.accepted, 1, JSON.stringify(ok.body))
    const risk = e.db.prepare('SELECT ref, state, package_id, deliverable_id, probability FROM risk WHERE project_id = ?').get(e.projectId) as any
    assert.equal(risk.ref, 'RSK-1', 'the CSV risk_id is stored verbatim as the ref')
    assert.equal(risk.state, 'mitigating', "'treating' normalizes to mitigating")
    assert.equal(risk.package_id, e.packageId)
    assert.equal(risk.deliverable_id, e.deliverableId)

    const bad = await admin.postCsv(`${D}/import/risks`,
      'risk_id,title,cause,consequence,owner,status,probability,impact\r\n' +
      'RSK-2,Bad,c,q,eor@t.co,open,6,0\r\n' +           // probability & impact out of 1..5
      'RSK-3,BadStatus,c,q,eor@t.co,exploded,,\r\n')     // unrecognized status
    assert.equal(bad.body.accepted, 0)
    assert.equal(bad.body.rejected.length, 2, JSON.stringify(bad.body))
    assert.equal(bad.body.rejected[0].errors.length, 2, 'both probability and impact flagged')

    // Re-import RSK-1: update, not duplicate.
    const r2 = await admin.postCsv(`${D}/import/risks`,
      'risk_id,title,cause,consequence,owner,status\r\n' +
      'RSK-1,Slippage v2,late vendor,delay,eor@t.co,closed\r\n')
    assert.equal(r2.body.updated, 1, JSON.stringify(r2.body))
    assert.equal(r2.body.accepted, 0)
    const count = e.db.prepare('SELECT COUNT(*) c FROM risk WHERE project_id = ?').get(e.projectId) as { c: number }
    assert.equal(count.c, 1, 'one risk row for the external id')
  } finally { await e.close() }
})

// ============================================================================
// Importers — RAIL anchored records (§16)
// ============================================================================

test('RAIL import: anchored records key on item_id, so re-import updates instead of duplicating', async () => {
  const e = await createTestEnv()
  try {
    const admin = await e.as('admin@t.co')
    const D = `/api/projects/${e.projectId}`
    const header = 'item_id,statement,type,log,owner,need_by,status,raised_by,raised_date,package,deliverable_ref,hold_cause'
    const rows =
      'A-100,Update pump curves,action,internal,eor@t.co,2027-05-01,open,lead@t.co,2026-06-01,PKG-A,TST-PR-001,\r\n' +
      'H-100,Vendor data hold,hold,internal,lead@t.co,2027-05-01,open,lead@t.co,2026-06-01,,TST-PR-001,vendor_data\r\n'
    const r1 = await admin.postCsv(`${D}/import/rail`, `${header}\r\n${rows}`)
    assert.equal(r1.body.accepted, 2, JSON.stringify(r1.body))
    assert.ok(e.db.prepare('SELECT id FROM work_item WHERE project_id = ? AND ref = ?').get(e.projectId, 'A-100'), 'work item stored under item_id ref')
    assert.ok(e.db.prepare('SELECT id FROM hold WHERE project_id = ? AND ref = ?').get(e.projectId, 'H-100'), 'hold stored under item_id ref')

    // Re-import the SAME source rows: updates, no duplicates.
    const r2 = await admin.postCsv(`${D}/import/rail`, `${header}\r\n${rows}`)
    assert.equal(r2.body.updated, 2, JSON.stringify(r2.body))
    assert.equal(r2.body.accepted, 0, 're-import must not create duplicates')
    const wi = e.db.prepare('SELECT COUNT(*) c FROM work_item WHERE project_id = ?').get(e.projectId) as { c: number }
    const hld = e.db.prepare('SELECT COUNT(*) c FROM hold WHERE project_id = ?').get(e.projectId) as { c: number }
    assert.equal(wi.c, 1, 'one work item for A-100')
    assert.equal(hld.c, 1, 'one hold for H-100')
  } finally { await e.close() }
})

// ============================================================================
// Intake → multi-record conversion (PEC-AHL-005)
// ============================================================================

test('intake conversion: one intake resolves into multiple records, each back-linked (PEC-AHL-005)', async () => {
  const e = await createTestEnv()
  try {
    const coord = await e.as('coord@t.co')
    const D = `/api/projects/${e.projectId}`
    const raised = await coord.post(`${D}/intake`, { statement: 'Vendor issue: needs an action and a risk', quickType: 'action' })
    assert.equal(raised.status, 200, JSON.stringify(raised.body))
    const ot = await coord.post(`${D}/intake/${raised.body.id}/open-triage`, { version: raised.body.version })
    assert.equal(ot.status, 200, JSON.stringify(ot.body))
    const disp = await coord.post(`${D}/intake/${raised.body.id}/triage`, {
      version: ot.body.version, disposition: 'converted',
      records: {
        workItems: [{ title: 'Chase vendor', statement: 'Chase vendor', kind: 'action', ownerId: e.people['eor@t.co'], needBy: '2027-05-05', anchorType: 'deliverable', anchorId: e.deliverableId }],
        risks: [{ title: 'Vendor risk', cause: 'late data', consequence: 'delay', ownerId: e.people['eor@t.co'] }],
      },
    })
    assert.equal(disp.status, 200, JSON.stringify(disp.body))
    assert.equal(disp.body.created.length, 2, 'two records created')
    const links = e.db.prepare('SELECT record_type FROM intake_link WHERE intake_id = ?').all(raised.body.id) as Array<{ record_type: string }>
    assert.equal(links.length, 2, 'a back-link per created record')
    assert.ok(links.some((l) => l.record_type === 'work_item') && links.some((l) => l.record_type === 'risk'))
  } finally { await e.close() }
})

// ============================================================================
// Load / performance (PEC-NFR-003): derived views must render within 2s at scale
// ============================================================================

function seedAtScale(deliverables: number): { repo: Repo; sx: Sx; pid: number } {
  const db = openDb(join(tmpdir(), `pec-perf-${randomBytes(6).toString('hex')}.db`))
  const repo = new Repo(db)
  const now = nowIso()
  const owner = repo.insert('person', { name: 'O', email: `o-${randomBytes(4).toString('hex')}@t.co`, passwordHash: 'x', isAdmin: 1, discipline: null, createdAt: now })
  const pid = repo.insert('project', { code: `PERF-${randomBytes(3).toString('hex')}`, name: 'PERF', timezone: 'UTC', weekendDays: ['Sat', 'Sun'], holidays: [], thresholds: {}, config: {} })
  const pkgIds: number[] = []
  withTx(db, () => { for (let i = 0; i < 10; i++) pkgIds.push(repo.insert('package', { projectId: pid, code: `P${i}`, name: `p${i}`, leadId: owner })) })
  const revIds: number[] = []
  withTx(db, () => {
    for (let i = 0; i < deliverables; i++) {
      const d = repo.insert('deliverable', { projectId: pid, packageId: pkgIds[i % pkgIds.length]!, docNo: `D${i}`, title: `d${i}`, discipline: 'Process', deliverableType: 'drawing', ownerId: owner, dueDate: '2027-06-30' })
      revIds.push(repo.insert('revision', { projectId: pid, deliverableId: d, revCode: 'A', state: 'in_work', createdAt: now, createdBy: owner }))
    }
  })
  const wiIds: number[] = []
  withTx(db, () => {
    for (let i = 0; i < deliverables; i++) {
      wiIds.push(repo.insert('work_item', { projectId: pid, ref: `WI${i}`, title: `w${i}`, kind: 'action', log: 'internal', anchorType: 'revision', anchorId: revIds[i % revIds.length]!, packageId: pkgIds[i % pkgIds.length], ownerId: owner, state: 'open', needBy: '2027-01-01', createdBy: owner, createdAt: now }))
    }
  })
  // P2 plan data at scale: 2k plan items + capacity + 500 schedule activities — the plan
  // index (core/src/plan.ts) must keep deliverableStatus/packageStatus off O(n²) paths
  withTx(db, () => {
    const week = isoWeekOf(new Date().toISOString().slice(0, 10))
    for (let i = 0; i < Math.min(2000, wiIds.length); i++) {
      repo.insert('plan_item', {
        projectId: pid, ref: `PLN${i}`, itemType: 'work_item', itemId: wiIds[i]!,
        horizon: 'now', week, discipline: 'Process', plannedHours: 4, createdBy: owner, createdAt: now,
      })
    }
    repo.insert('capacity_entry', { projectId: pid, week, discipline: 'Process', hours: 4000 })
    for (let i = 0; i < 500; i++) {
      repo.insert('schedule_activity', {
        projectId: pid, activityId: `ACT${i}`, description: `a${i}`,
        startDate: '2027-01-04', finishDate: '2027-01-15',
        packageId: pkgIds[i % pkgIds.length], deliverableId: (i % deliverables) + 1,
      })
    }
  })
  // a few hundred holds on deliverables, to exercise the hold-overlay index too
  withTx(db, () => {
    for (let i = 0; i < 200; i++) {
      const hid = repo.insert('hold', { projectId: pid, ref: `H${i}`, title: `hold ${i}`, cause: 'vendor_data', ownerId: owner, needBy: '2027-02-02', raisedBy: owner, raisedAt: now, state: 'active', log: 'internal' })
      repo.insert('hold_link', { holdId: hid, targetType: 'deliverable', targetId: (i % deliverables) + 1 })
    }
  })
  const session = { personId: owner, name: 'O', email: 'o@t.co', isAdmin: true }
  const sx: Sx = { db, repo, projectId: pid, session, roles: [] as never }
  return { repo, sx, pid }
}

function median(fn: () => unknown, runs = 3): number {
  fn() // warm
  const s: number[] = []
  for (let i = 0; i < runs; i++) {
    const t = process.hrtime.bigint()
    fn()
    s.push(Number((process.hrtime.bigint() - t) / 1000n) / 1000)
  }
  return s.sort((a, b) => a - b)[Math.floor(s.length / 2)]!
}

test('PEC-NFR-003: derived views render within 2s at 10k deliverables/work-items', () => {
  const { sx } = seedAtScale(10000)
  const ov = median(() => overviewView(sx))
  const pk = median(() => packagesView(sx))
  const dl = median(() => deliverablesView(sx, {}))
  const pl = median(() => planView(sx))
  // Budget is 2000ms; a reintroduced O(n^2) put these at 11-13s, so this both asserts the NFR
  // and hard-fails a quadratic regression.
  assert.ok(ov <= 2000, `overviewView ${ov.toFixed(0)}ms must be <= 2000ms`)
  assert.ok(pk <= 2000, `packagesView ${pk.toFixed(0)}ms must be <= 2000ms`)
  assert.ok(dl <= 2000, `deliverablesView ${dl.toFixed(0)}ms must be <= 2000ms`)
  assert.ok(pl <= 2000, `planView ${pl.toFixed(0)}ms must be <= 2000ms`)
})

test('PEC-NFR-003: snapshot load is bounded and history-independent', () => {
  const { repo, pid } = seedAtScale(10000)
  const t = median(() => repo.snapshot(pid))
  assert.ok(t <= 2000, `snapshot ${t.toFixed(0)}ms must be well under budget`)
})
