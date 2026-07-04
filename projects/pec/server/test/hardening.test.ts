/**
 * Regression tests for the confirmed findings from the adversarial invariant-attack
 * workflow (2026-07-04). Each test reproduces the original exploit and asserts it is
 * now refused. Titled by the finding it closes.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv, acceptCheckOn } from './harness.ts'
import type { TestEnv } from './harness.ts'

let env: TestEnv
let P: string

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
})
after(async () => { await env.close() })

// ---------- findings 0/5/7/10: date-poisoning DoS ----------

test('HARDEN date DoS: malformed dates are rejected at write time (400), derived views never crash', async () => {
  const lead = await env.as('lead@t.co')
  const pm = await env.as('pm@t.co')

  // baseline: overview works
  assert.equal((await pm.get(`${P}/overview`)).status, 200)

  // every date-bearing write rejects a non-date
  const badHold = await lead.post(`${P}/holds`, {
    title: 'poison', cause: 'vendor_data', ownerId: env.people['lead@t.co'], needBy: 'not-a-date',
    targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
  })
  assert.equal(badHold.status, 400)
  assert.match(badHold.body.error.message, /YYYY-MM-DD/)

  const badWi = await lead.post(`${P}/work-items`, {
    title: 'poison', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'], needBy: 'garbage',
  })
  assert.equal(badWi.status, 400)

  const badDel = await lead.put(`${P}/deliverables/${env.deliverableId}`, { version: 1, dueDate: 'BADDATE' })
  assert.equal(badDel.status, 400)

  const badDec = await lead.post(`${P}/decisions`, {
    title: 'x', statement: 'y', authorityId: env.people['pm@t.co'], needBy: '2026-13-99',
  })
  assert.equal(badDec.status, 400, 'impossible calendar date rejected')

  // all derived views remain healthy — nothing was poisoned
  for (const v of ['overview', 'packages', 'deliverables', 'log']) {
    assert.equal((await pm.get(`${P}/${v}`)).status, 200, `${v} still 200`)
  }
})

test('HARDEN date DoS (defense in depth): a malformed stored date does not crash derivation', async () => {
  // simulate a pre-existing bad row (e.g. from before validation) via direct SQL
  const lead = await env.as('lead@t.co')
  const wi = await lead.post(`${P}/work-items`, {
    title: 'legacy', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'], needBy: '2027-01-01',
  })
  env.db.prepare('UPDATE work_item SET need_by = ? WHERE id = ?').run('corrupt', wi.body.id)
  const pm = await env.as('pm@t.co')
  const ov = await pm.get(`${P}/overview`)
  assert.equal(ov.status, 200, 'derivation tolerates a malformed stored date (I-4)')
  const del = await pm.get(`${P}/deliverables/${env.deliverableId}`)
  assert.equal(del.status, 200)
})

// ---------- finding 1: work item on a superseded revision ----------

test('HARDEN I-1: an open item on a superseded revision stays visible on the deliverable and counts toward health', async () => {
  const lead = await env.as('lead@t.co')
  const del = await lead.post(`${P}/deliverables`, {
    packageId: env.packageId, docNo: 'TST-SR-001', title: 'Superseded-rev test', ownerId: env.people['eor@t.co'], dueDate: '2027-06-30',
  })
  const revA = await lead.post(`${P}/deliverables/${del.body.id}/revisions`, { revCode: 'A' })
  // an overdue open item anchored to rev A
  const wi = await lead.post(`${P}/work-items`, {
    title: 'unfinished on rev A', anchorType: 'revision', anchorId: revA.body.id,
    ownerId: env.people['eor@t.co'], needBy: '2026-01-01',
  })
  // create rev B → rev A is superseded
  await lead.post(`${P}/deliverables/${del.body.id}/revisions`, { revCode: 'B' })

  const detail = await lead.get(`${P}/deliverables/${del.body.id}`)
  assert.ok(detail.body.openItems.workItems.some((w: any) => w.ref === wi.body.ref),
    'the rev-A item is still listed on the deliverable (I-1)')
  // health is not green: it carries an overdue open item
  assert.notEqual(detail.body.health.value, 'green', 'deliverable does not derive green while carrying an overdue item')
})

// ---------- finding 3: approval outcome enum ----------

test('HARDEN I-6: an approval outcome outside {approve,conditionally_accept,reject,defer} is rejected', async () => {
  const lead = await env.as('lead@t.co')
  const approver = await env.as('approver@t.co')
  const del = await lead.post(`${P}/deliverables`, {
    packageId: env.packageId, docNo: 'TST-AO-001', title: 'Approval outcome test', ownerId: env.people['eor@t.co'], dueDate: '2027-06-30',
  })
  const rev = await lead.post(`${P}/deliverables/${del.body.id}/revisions`, { revCode: 'A' })
  const apr = await lead.post(`${P}/approval-records`, {
    title: 'auth', approvalType: 'issue_authorization', appliesToType: 'revision', appliesToId: rev.body.id,
    signatoryIds: [env.people['approver@t.co']],
  })
  await acceptCheckOn(env, rev.body.id)
  const reg = await lead.get(`${P}/approval-register`)
  const row = reg.body.find((a: any) => a.id === apr.body.id)
  for (const bad of ['waive', 'select', 'confirm_basis', 'supersede']) {
    const res = await approver.post(`${P}/approval-records/${apr.body.id}/outcome`, {
      version: row.version, outcome: bad, rationale: 'x',
    })
    assert.equal(res.status, 400, `approval outcome '${bad}' rejected`)
  }
  // the valid one still works
  const ok = await approver.post(`${P}/approval-records/${apr.body.id}/outcome`, {
    version: row.version, outcome: 'approve', rationale: 'ok',
  })
  assert.equal(ok.status, 200)
})

// ---------- finding 2: MDL re-import cannot advance an existing revision past the gate ----------

test('HARDEN I-5: MDL re-import cannot force an existing revision to issued (bypass the gate)', async () => {
  const admin = await env.as('admin@t.co')
  // seed a fresh deliverable at in_work via import
  const csv1 = 'doc_no,title,package,discipline,owner,current_rev,state,due_date\n'
    + 'TST-RI-001,Reimport test,PKG-A,Process,eor@t.co,A,in work,2027-06-30'
  const r1 = await admin.postCsv(`${P}/import/mdl`, csv1)
  assert.equal(r1.body.accepted, 1)

  // re-import the SAME rev code but state=issued — must NOT flip the revision to issued
  const csv2 = 'doc_no,title,package,discipline,owner,current_rev,state,due_date\n'
    + 'TST-RI-001,Reimport test,PKG-A,Process,eor@t.co,A,issued,2027-06-30'
  const r2 = await admin.postCsv(`${P}/import/mdl`, csv2)
  assert.equal(r2.body.updated, 1)
  assert.ok(r2.body.conflicts.some((c: any) => /I-5|gated/i.test(c.reason)), 'state change reported as a gate conflict')

  const lead = await env.as('lead@t.co')
  const dels = await lead.get(`${P}/deliverables?view=master`)
  const row = dels.body.find((d: any) => d.docNo === 'TST-RI-001')
  assert.equal(row.state, 'in_work', 'revision was NOT forced to issued by import (I-5)')
})

// ---------- findings 6/8: self-supersession ----------

test('HARDEN I-10: a decision/approval cannot supersede itself', async () => {
  const lead = await env.as('lead@t.co')
  const pm = await env.as('pm@t.co')
  const dec = await lead.post(`${P}/decisions`, { title: 'self', statement: 'x', authorityId: env.people['pm@t.co'] })
  const p1 = await pm.post(`${P}/decisions/${dec.body.id}/progress`, { event: 'assign_preparer', version: dec.body.version, preparerId: env.people['eor@t.co'] })
  const p2 = await pm.post(`${P}/decisions/${dec.body.id}/progress`, { event: 'mark_pending', version: p1.body.version })
  const done = await pm.post(`${P}/decisions/${dec.body.id}/outcome`, { version: p2.body.version, outcome: 'select', rationale: 'x' })
  const self = await pm.post(`${P}/decisions/${dec.body.id}/supersede`, { version: done.body.version, replacementId: dec.body.id })
  assert.equal(self.status, 400)
  assert.match(self.body.error.message, /cannot supersede itself/)
})

// ---------- finding 4: instance admin cannot record a judgment as non-authority/non-signatory ----------

test('HARDEN I-6: instance admin cannot record an approval outcome as a non-signatory nor a decision as non-authority', async () => {
  const lead = await env.as('lead@t.co')
  const admin = await env.as('admin@t.co') // instance admin, NOT a signatory/authority here

  // approval: admin is not a signatory
  const del = await lead.post(`${P}/deliverables`, {
    packageId: env.packageId, docNo: 'TST-BG-001', title: 'Break-glass test', ownerId: env.people['eor@t.co'], dueDate: '2027-06-30',
  })
  const rev = await lead.post(`${P}/deliverables/${del.body.id}/revisions`, { revCode: 'A' })
  const apr = await lead.post(`${P}/approval-records`, {
    title: 'auth', approvalType: 'issue_authorization', appliesToType: 'revision', appliesToId: rev.body.id,
    signatoryIds: [env.people['approver@t.co']],
  })
  await acceptCheckOn(env, rev.body.id)
  const reg = await lead.get(`${P}/approval-register`)
  const row = reg.body.find((a: any) => a.id === apr.body.id)
  const adminTry = await admin.post(`${P}/approval-records/${apr.body.id}/outcome`, {
    version: row.version, outcome: 'approve', rationale: 'break glass',
  })
  assert.equal(adminTry.status, 403, 'instance admin is not a signatory (I-6)')

  // decision: admin is not the authority
  const dec = await lead.post(`${P}/decisions`, { title: 'd', statement: 'x', authorityId: env.people['pm@t.co'] })
  const pm = await env.as('pm@t.co')
  const p1 = await pm.post(`${P}/decisions/${dec.body.id}/progress`, { event: 'assign_preparer', version: dec.body.version, preparerId: env.people['eor@t.co'] })
  const p2 = await pm.post(`${P}/decisions/${dec.body.id}/progress`, { event: 'mark_pending', version: p1.body.version })
  const adminDec = await admin.post(`${P}/decisions/${dec.body.id}/outcome`, { version: p2.body.version, outcome: 'select', rationale: 'break glass' })
  assert.equal(adminDec.status, 403, 'instance admin is not the decision authority (I-6)')
})

// ---------- finding 9: log visibility ----------

test('HARDEN PEC-NFR-005: internal-log holds/decisions/interfaces do not leak titles to the viewer via package/overview', async () => {
  const lead = await env.as('lead@t.co')
  // an internal-log hold on a package deliverable
  await lead.post(`${P}/holds`, {
    title: 'SECRET internal hold', cause: 'vendor_data', ownerId: env.people['lead@t.co'], needBy: '2027-01-01',
    log: 'internal', targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
  })
  await lead.post(`${P}/interfaces`, {
    title: 'SECRET internal interface', givingParty: 'A', receivingParty: 'B',
    givingPackageId: env.packageId, log: 'internal',
  })

  const viewer = await env.as('viewer@t.co')
  const pkg = await viewer.get(`${P}/packages/${env.packageId}`)
  const blob = JSON.stringify(pkg.body)
  assert.ok(!blob.includes('SECRET'), 'no internal-log titles leak into package detail for the viewer')

  const ov = await viewer.get(`${P}/overview`)
  assert.ok(!JSON.stringify(ov.body.topBlockers).includes('SECRET'), 'no internal-log hold title in overview top blockers')

  // the lead (sees all logs) still gets them
  const leadPkg = await lead.get(`${P}/packages/${env.packageId}`)
  assert.ok(JSON.stringify(leadPkg.body).includes('SECRET'), 'internal-log records visible to internal roles')
})
