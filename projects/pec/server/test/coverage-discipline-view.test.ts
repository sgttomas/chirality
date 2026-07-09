/**
 * Discipline view v1 (D-PEC-40). Pins:
 * - the index lists disciplines derived from deliverables (incl. Unspecified);
 * - the detail renders the four report sections over existing data, grouped by
 *   deliverable type, with drillable contributing refs (I-4);
 * - the metric band is factual-or-absent: % complete and stalled flags absent;
 *   period tiles appear only for an explicitly requested window and name the
 *   coverage basis (D-PEC-39 PER-COV);
 * - needs rows and refs respect log visibility (PEC-NFR-005);
 * - risks count only deliverable-attributed records (no package-only guesses);
 * - the routes are read-only and an unknown discipline is a 404.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { withTx } from '../src/db.ts'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'

let env: TestEnv
let P: string

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`

  withTx(env.db, () => {
    // a second discipline with two deliverable types
    const d2 = env.repo.insert('deliverable', {
      projectId: env.projectId, packageId: env.packageId, docNo: 'TST-EL-001', title: 'Single line diagram',
      discipline: 'Electrical', deliverableType: 'drawing', ownerId: env.people['eor@t.co'], dueDate: '2027-03-31',
    })
    const d3 = env.repo.insert('deliverable', {
      projectId: env.projectId, packageId: env.packageId, docNo: 'TST-EL-002', title: 'Cable schedule',
      discipline: 'Electrical', deliverableType: 'list', ownerId: env.people['eor@t.co'], dueDate: '2027-04-30',
    })
    // a discipline-less deliverable lands under Unspecified
    env.repo.insert('deliverable', {
      projectId: env.projectId, packageId: env.packageId, docNo: 'TST-XX-001', title: 'Unclassified doc',
      discipline: null, deliverableType: null, ownerId: null, dueDate: null,
    })
    const rev2 = env.repo.insert('revision', {
      projectId: env.projectId, deliverableId: d2, revCode: 'A', state: 'issued',
      createdAt: '2026-06-01T00:00:00Z', createdBy: env.people['admin@t.co'],
    })
    env.repo.insert('issue_event', {
      projectId: env.projectId, ref: 'IE-EL-1', revisionId: rev2, purpose: 'IFC',
      transmittalRef: 'TR-EL-1', issuedAt: '2026-06-04T10:00:00Z', issuedBy: env.people['dc@t.co'],
    })
    env.repo.insert('issue_event', {
      projectId: env.projectId, ref: 'IE-EL-0', revisionId: rev2, purpose: 'IFR',
      transmittalRef: 'TR-EL-0', issuedAt: '2026-05-28T10:00:00Z', issuedBy: env.people['dc@t.co'],
    })
    // needs: an internal-log action on an Electrical deliverable + an active hold
    env.repo.insert('work_item', {
      projectId: env.projectId, ref: 'WI-EL-1', title: 'chase vendor data', kind: 'action', log: 'internal',
      anchorType: 'deliverable', anchorId: d3, ownerId: env.people['eor@t.co'],
      state: 'open', createdBy: env.people['eor@t.co'], createdAt: '2026-06-01T09:00:00Z',
    })
    const holdId = env.repo.insert('hold', {
      projectId: env.projectId, ref: 'HLD-EL-1', title: 'awaiting client info', cause: 'information_missing',
      ownerId: env.people['lead@t.co'], raisedBy: env.people['lead@t.co'],
      raisedAt: '2026-06-02T09:00:00Z', state: 'active', log: 'package',
    })
    env.repo.insert('hold_link', { holdId, targetType: 'deliverable', targetId: d3 })
    // risks: one deliverable-attributed (counts), one package-only (must NOT count)
    env.repo.insert('risk', {
      projectId: env.projectId, ref: 'RSK-EL-1', title: 'vendor slip', state: 'open',
      deliverableId: d2, packageId: null, ownerId: env.people['lead@t.co'],
      probability: 3, impact: 4,
    })
    env.repo.insert('risk', {
      projectId: env.projectId, ref: 'RSK-PK-1', title: 'package-only risk', state: 'open',
      deliverableId: null, packageId: env.packageId, ownerId: env.people['lead@t.co'],
    })
  })
})
after(async () => { await env.close() })

test('index: disciplines derive from deliverables, including Unspecified, with count columns', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.get(`${P}/disciplines`)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  const names = res.body.map((r: { discipline: string }) => r.discipline)
  assert.deepEqual(names, ['Electrical', 'Process', 'Unspecified'])
  const el = res.body.find((r: { discipline: string }) => r.discipline === 'Electrical')
  assert.equal(el.deliverables, 2)
  assert.equal(el.inWork, 1, 'issued TST-EL-001 is out of in-work')
  assert.equal(el.issueEvents, 2)
  assert.equal(el.openNeeds, 2)
  assert.equal(el.openRisks, 1, 'package-only risk not counted')
})

test('detail: four report sections over existing data; activities grouped by deliverable type', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.get(`${P}/disciplines/Electrical`)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.discipline, 'Electrical')
  assert.equal(res.body.period, null)

  const groups = res.body.sections.activities.groups
  assert.equal(groups.length, 1, 'only the in-work list type remains')
  assert.equal(groups[0].type, 'list')
  assert.equal(groups[0].deliverables[0].docNo, 'TST-EL-002')
  assert.ok(groups[0].deliverables[0].workflow.label, 'workflow completeness rides each activity')

  assert.equal(res.body.sections.issuances.rows.length, 2, 'all recorded issue events without a period')
  assert.equal(res.body.sections.issuances.rows[0].ref, 'IE-EL-1', 'sorted latest first')
  assert.equal(res.body.sections.issuances.rows[0].docNo, 'TST-EL-001')

  const needTypes = res.body.sections.needs.rows.map((r: { type: string }) => r.type).sort()
  assert.deepEqual(needTypes, ['action', 'hold'])
  const risks = res.body.sections.risks.rows
  assert.equal(risks.length, 1)
  assert.equal(risks[0].ref, 'RSK-EL-1')

  // metric band: factual tiles carry rule ids and contributing refs
  assert.equal(res.body.band.activitiesInWork.ruleId, 'DISC-ACT')
  assert.equal(res.body.band.activitiesInWork.value, 1)
  assert.equal(res.body.band.openNeeds.value, 2)
  assert.ok(res.body.band.openNeeds.contributing.length === 2)
  assert.equal(res.body.band.openRisks.value, 1)
  assert.ok(res.body.band.needsAging.value > 0)
  // absent-honest without a period; % complete and stalled always absent in v1
  assert.equal(res.body.band.issuedInPeriod, undefined)
  const absentFigures = res.body.absent.map((a: { figure: string }) => a.figure)
  assert.ok(absentFigures.some((f: string) => /% complete/.test(f)))
  assert.ok(absentFigures.some((f: string) => /stalled/.test(f)))
  assert.ok(absentFigures.some((f: string) => /issuances this period/.test(f)))
})

test('detail with declared period: issuance tiles appear, scoped and coverage-basis-named', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.get(`${P}/disciplines/Electrical?start=2026-06-01&end=2026-06-07`)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.deepEqual(res.body.period, { start: '2026-06-01', end: '2026-06-07' })
  assert.equal(res.body.sections.issuances.rows.length, 1, 'period-filtered to the window')
  assert.equal(res.body.band.issuedInPeriod.ruleId, 'DISC-ISSUED')
  assert.equal(res.body.band.issuedInPeriod.value, 1)
  assert.match(res.body.band.issuedInPeriod.detail, /PER-COV/)
  assert.match(res.body.band.issuedInPeriod.detail, /no applied import coverage declaration/,
    'an uncovered window says so instead of implying coverage')
  assert.equal(res.body.band.issuanceDelta.ruleId, 'DISC-ISSUED-DELTA')
  assert.equal(res.body.band.issuanceDelta.value, 0, '1 in window minus 1 in preceding window (05-25..05-31)')
  assert.ok(!res.body.absent.some((a: { figure: string }) => /issuances this period/.test(a.figure)))

  assert.equal((await admin.get(`${P}/disciplines/Electrical?start=2026-06-01`)).status, 400)
  assert.equal((await admin.get(`${P}/disciplines/Electrical?start=2026-06-07&end=2026-06-01`)).status, 400)
})

test('log visibility: the viewer sees package-log needs but not internal ones (PEC-NFR-005)', async () => {
  const viewer = await env.as('viewer@t.co')
  const res = await viewer.get(`${P}/disciplines/Electrical`)
  assert.equal(res.status, 200)
  const needRefs = res.body.sections.needs.rows.map((r: { ref: string }) => r.ref)
  assert.deepEqual(needRefs, ['HLD-EL-1'], 'internal work item filtered; package hold visible')
  assert.equal(res.body.band.openNeeds.value, 1)
})

test('unknown discipline is a 404; URL-encoded names resolve; view mutates nothing', async () => {
  const admin = await env.as('admin@t.co')
  assert.equal((await admin.get(`${P}/disciplines/NoSuchDiscipline`)).status, 404)
  const unspec = await admin.get(`${P}/disciplines/${encodeURIComponent('Unspecified')}`)
  assert.equal(unspec.status, 200)
  assert.equal(unspec.body.sections.activities.groups[0].type, 'unspecified')

  const before = env.db.prepare('SELECT COUNT(*) AS n FROM history_entry').get() as { n: number }
  await admin.get(`${P}/disciplines`)
  await admin.get(`${P}/disciplines/Electrical?start=2026-06-01&end=2026-06-07`)
  const after_ = env.db.prepare('SELECT COUNT(*) AS n FROM history_entry').get() as { n: number }
  assert.equal(after_.n, before.n, 'read-only: no history rows written by the view')
})
