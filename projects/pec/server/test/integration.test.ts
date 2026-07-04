/**
 * Integration coverage for P1 behaviors the invariant suite doesn't reach:
 * intake conversion fan-out + raiser notifications (PEC-AHL-005/007), multi-project
 * isolation (PEC-NFR-007), check three-facts + comment sub-lifecycle (PEC-CHK-002/003),
 * decision-gated issue (§9), and the decisions/risks importers (§16).
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'
import { withTx } from '../src/db.ts'
import { Repo, nowIso } from '../src/repo.ts'
import { hashPassword } from '../src/auth.ts'

let env: TestEnv
let P: string

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
})
after(async () => { await env.close() })

// ---------- intake conversion fan-out (PEC-AHL-005/007) ----------

test('PEC-AHL-005/007: one intake converts into multiple back-linked records; raiser notified at routing', async () => {
  const ic = await env.as('ic@t.co')
  const coord = await env.as('coord@t.co')
  const intake = await ic.post(`${P}/intake`, {
    statement: 'Vendor data missing AND a units decision is needed', quickType: 'need_information',
  })
  assert.equal(intake.status, 200)
  const verbatim = intake.body.statementVerbatim

  await coord.post(`${P}/intake/${intake.body.id}/open-triage`, { version: intake.body.version })
  const conv = await coord.post(`${P}/intake/${intake.body.id}/triage`, {
    version: intake.body.version + 1, disposition: 'converted', note: 'split',
    records: {
      workItems: [{ title: 'Chase vendor', anchorType: 'deliverable', anchorId: env.deliverableId, ownerId: env.people['eor@t.co'], needBy: '2027-01-01' }],
      holds: [{ title: 'Vendor data', cause: 'vendor_data', ownerId: env.people['lead@t.co'], needBy: '2027-01-01', targets: [{ targetType: 'deliverable', targetId: env.deliverableId }] }],
      decisions: [{ title: 'Units basis', statement: 'metric vs imperial', authorityId: env.people['pm@t.co'] }],
      risks: [{ title: 'Schedule risk from vendor delay' }],
    },
  })
  assert.equal(conv.status, 200)
  assert.equal(conv.body.created.length, 4, 'work item + hold + decision + risk')
  const types = conv.body.created.map((c: any) => c.recordType).sort()
  assert.deepEqual(types, ['decision', 'hold', 'risk', 'work_item'])

  // statement preserved verbatim after conversion (OM-3)
  const dispositioned = await coord.get(`${P}/intake?state=dispositioned`)
  const item = dispositioned.body.find((x: any) => x.id === intake.body.id)
  assert.equal(item.statementVerbatim, verbatim)
  assert.equal(item.links.length, 4, 'every created record is back-linked (PEC-AHL-005)')

  // raiser notified at routing (PEC-AHL-007)
  const notes = await ic.get(`${P}/notifications`)
  assert.ok(notes.body.some((n: any) => n.event === 'raised_item_routed' && n.recordRef === intake.body.ref))
})

// ---------- multi-project isolation (PEC-NFR-007) ----------

test('PEC-NFR-007: records are invisible and unreachable across project boundaries', async () => {
  // second project + membership for the same admin
  const repo = new Repo(env.db)
  const pid2 = withTx(env.db, () => repo.insert('project', {
    code: 'TST2', name: 'Other FEED', timezone: 'UTC',
    weekendDays: ['Sat', 'Sun'], holidays: [], thresholds: {}, config: {},
  }))
  withTx(env.db, () => {
    env.db.prepare('INSERT INTO project_role (project_id, person_id, role) VALUES (?, ?, ?)')
      .run(pid2, env.people['admin@t.co']!, 'admin')
  })
  const admin = await env.as('admin@t.co')

  // a work item in project 1 must not be fetchable through project 2's route
  const lead = await env.as('lead@t.co')
  const wi = await lead.post(`${P}/work-items`, {
    title: 'p1 only', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'], needBy: '2027-01-01',
  })
  const cross = await admin.get(`/api/projects/${pid2}/work-items/${wi.body.id}`)
  assert.equal(cross.status, 404, 'project 2 route cannot read a project 1 record')

  // project 2 overview sees none of project 1's deliverables
  const ov2 = await admin.get(`/api/projects/${pid2}/deliverables`)
  assert.equal(ov2.body.length, 0)
  const ov1 = await admin.get(`${P}/deliverables`)
  assert.ok(ov1.body.length > 0)

  // a non-member of project 2 is refused entirely
  const nonMember = await env.as('eor@t.co')
  const refused = await nonMember.get(`/api/projects/${pid2}/overview`)
  assert.equal(refused.status, 403)
})

// ---------- check three distinct facts + comment sub-lifecycle (PEC-CHK-002/003) ----------

test('PEC-CHK-003: checklist completion, comment closure, and acceptance are three separate facts; comment reopen works', async () => {
  const lead = await env.as('lead@t.co')
  const checker = await env.as('checker@t.co')
  const eor = await env.as('eor@t.co')

  const del = await lead.post(`${P}/deliverables`, {
    packageId: env.packageId, docNo: 'TST-CH-001', title: 'Checkable', ownerId: env.people['ic@t.co'], dueDate: '2027-06-30',
  })
  const rev = await lead.post(`${P}/deliverables/${del.body.id}/revisions`, { revCode: 'A' })
  const chk = await lead.post(`${P}/checks`, { revisionId: rev.body.id, checkerId: env.people['checker@t.co'] })
  let v = chk.body.version
  const started = await checker.post(`${P}/checks/${chk.body.id}/start`, { version: v })
  v = started.body.version

  // add a comment → check goes comments_open; acceptance blocked while it is open
  const cmt = await checker.post(`${P}/checks/${chk.body.id}/comments`, { responderId: env.people['eor@t.co'], text: 'fix the tag numbers' })
  const detail1 = await lead.get(`${P}/checks/${chk.body.id}`)
  assert.equal(detail1.body.check.state, 'comments_open')
  assert.equal(detail1.body.facts.commentsClosed, false)
  const blocked = await checker.post(`${P}/checks/${chk.body.id}/accept`, { version: detail1.body.check.version })
  assert.equal(blocked.status, 400, 'cannot accept with an open comment (PEC-CHK-003)')

  // respond + accept-close the comment; reopen it; re-close
  const responded = await eor.post(`${P}/comments/${cmt.body.id}/respond`, { version: cmt.body.version, response: 'done, tags corrected' })
  const closed = await checker.post(`${P}/comments/${cmt.body.id}/accept`, { version: responded.body.version })
  assert.equal(closed.body.disposition, 'accepted_closed')
  const reopened = await checker.post(`${P}/comments/${cmt.body.id}/reopen`, { version: closed.body.version, reason: 'still wrong on sheet 2' })
  assert.equal(reopened.body.disposition, 'reopened')
  const detail2 = await lead.get(`${P}/checks/${chk.body.id}`)
  assert.equal(detail2.body.check.state, 'comments_open', 'reopen drove the check back')

  // re-respond, re-close, then accept the check with an INCOMPLETE checklist (facts stay distinct)
  const r2 = await eor.post(`${P}/comments/${cmt.body.id}/respond`, { version: reopened.body.version, response: 'fixed sheet 2 too' })
  await checker.post(`${P}/comments/${cmt.body.id}/accept`, { version: r2.body.version })
  const detail3 = await lead.get(`${P}/checks/${chk.body.id}`)
  const accepted = await checker.post(`${P}/checks/${chk.body.id}/accept`, { version: detail3.body.check.version })
  assert.equal(accepted.status, 200)
  assert.equal(accepted.body.state, 'accepted')
  const detail4 = await lead.get(`${P}/checks/${chk.body.id}`)
  assert.equal(detail4.body.facts.checkerAccepted, true)
  assert.equal(detail4.body.facts.checklistComplete, false, 'acceptance did not force checklist completion — three distinct facts')
})

// ---------- decision-gated issue (§9) ----------

test('§9: a decision-type hard condition gates revision.issue until the decision is decided', async () => {
  const lead = await env.as('lead@t.co')
  const pm = await env.as('pm@t.co')
  const dc = await env.as('dc@t.co')

  const del = await lead.post(`${P}/deliverables`, {
    packageId: env.packageId, docNo: 'TST-DG-001', title: 'Decision-gated', ownerId: env.people['eor@t.co'], dueDate: '2027-06-30',
  })
  const rev = await lead.post(`${P}/deliverables/${del.body.id}/revisions`, { revCode: 'A' })
  const dec = await lead.post(`${P}/decisions`, { title: 'Basis', statement: 'confirm basis', authorityId: env.people['pm@t.co'] })
  const cond = await lead.post(`${P}/conditions`, {
    parentType: 'revision', parentId: rev.body.id, gatedTransition: 'revision.issue',
    type: 'decision', requiredRefType: 'decision', requiredRefId: dec.body.id, severity: 'hard',
    description: 'Basis decision made',
  })

  // fast-forward the revision to approved (no approval records → check acceptance carries it)
  const chk = await lead.post(`${P}/checks`, { revisionId: rev.body.id, checkerId: env.people['checker@t.co'] })
  const checker = await env.as('checker@t.co')
  const st = await checker.post(`${P}/checks/${chk.body.id}/start`, { version: chk.body.version })
  await checker.post(`${P}/checks/${chk.body.id}/accept`, { version: st.body.version })
  const d1 = await lead.get(`${P}/deliverables/${del.body.id}`)
  assert.equal(d1.body.currentRevision.state, 'approved')

  const blocked = await dc.post(`${P}/revisions/${rev.body.id}/transition`, {
    event: 'issue', version: d1.body.currentRevision.version,
    issueEvent: { purpose: 'IFR', transmittalRef: 'TR-DG', recipients: ['client'] },
  })
  assert.equal(blocked.status, 409)
  assert.ok(blocked.body.error.details.conditions.some((c: any) => c.ref === cond.body.ref && c.state === 'open'))

  // decide it → condition satisfies → issue proceeds
  const p1 = await pm.post(`${P}/decisions/${dec.body.id}/progress`, { event: 'assign_preparer', version: dec.body.version, preparerId: env.people['eor@t.co'] })
  const p2 = await pm.post(`${P}/decisions/${dec.body.id}/progress`, { event: 'mark_pending', version: p1.body.version })
  await pm.post(`${P}/decisions/${dec.body.id}/outcome`, { version: p2.body.version, outcome: 'confirm_basis', rationale: 'metric confirmed' })
  const d2 = await lead.get(`${P}/deliverables/${del.body.id}`)
  const issued = await dc.post(`${P}/revisions/${rev.body.id}/transition`, {
    event: 'issue', version: d2.body.currentRevision.version,
    issueEvent: { purpose: 'IFR', transmittalRef: 'TR-DG', recipients: ['client'] },
  })
  assert.equal(issued.status, 200)
  assert.equal(issued.body.state, 'issued')
})

// ---------- decisions & risks importers (§16) ----------

test('§16: decision-log and risk-log imports validate row-by-row and round-trip on export', async () => {
  const admin = await env.as('admin@t.co')
  const decCsv = [
    'decision_id,title,statement,authority,need_by,status,outcome,rationale',
    'D-100,Coating spec,Choose external coating,pm@t.co,2027-01-01,decided,select,3LPE selected',
    'D-101,No authority row,statement here,ghost@nowhere.io,2027-01-01,pending,,',
    'D-102,Decided-no-outcome,x,pm@t.co,2027-01-01,decided,,',
  ].join('\n')
  const dres = await admin.postCsv(`${P}/import/decisions`, decCsv)
  assert.equal(dres.status, 200)
  assert.equal(dres.body.accepted, 1)
  assert.equal(dres.body.rejected.length, 2, 'unknown authority + decided-without-outcome rejected')

  const riskCsv = [
    'risk_id,title,cause,consequence,owner,status,probability,impact',
    'R-100,Long-lead compressor,Vendor slot,Schedule slip,lead@t.co,open,4,5',
    'R-101,Bad probability,x,y,lead@t.co,open,9,3',
  ].join('\n')
  const rres = await admin.postCsv(`${P}/import/risks`, riskCsv)
  assert.equal(rres.body.accepted, 1)
  assert.equal(rres.body.rejected.length, 1, 'probability out of 1-5 rejected')

  const lead = await env.as('lead@t.co')
  const decOut = await lead.get(`${P}/export/decisions.csv`)
  assert.match(decOut.body, /D-100|Coating spec/)
  const riskOut = await lead.get(`${P}/export/risks.csv`)
  assert.match(riskOut.body, /Long-lead compressor/)
})
