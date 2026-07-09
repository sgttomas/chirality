/**
 * The invariant suite (SPEC §10): every PRD §5 invariant probed through the real HTTP
 * layer against a real database. Named I-1..I-10 so the traceability table can point here.
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

// ---------- I-1 one record, many views ----------

test('I-1: a work item created once appears in My Week, the log register, and the deliverable view — same ref, no copies', async () => {
  const lead = await env.as('lead@t.co')
  const eor = await env.as('eor@t.co')
  const wi = await lead.post(`${P}/work-items`, {
    title: 'Confirm design pressure', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'], needBy: '2026-01-05', // in the past → overdue → in My Week
  })
  assert.equal(wi.status, 200)
  const ref = wi.body.ref

  const myWeek = await eor.get(`${P}/my-week`)
  assert.ok(myWeek.body.committed.some((x: any) => x.workItem.ref === ref), 'projected into My Week')

  const log = await eor.get(`${P}/log`)
  assert.ok(log.body.some((x: any) => x.ref === ref), 'projected into the unified log register')

  const del = await eor.get(`${P}/deliverables/${env.deliverableId}`)
  assert.ok(del.body.openItems.workItems.some((x: any) => x.ref === ref), 'projected into the deliverable view')
})

// ---------- I-2 no unanchored planned work ----------

test('I-2: direct work-item creation without an anchor is rejected; untriaged intake is visible and flagged unanchored', async () => {
  const lead = await env.as('lead@t.co')
  const bad = await lead.post(`${P}/work-items`, {
    title: 'floating task', ownerId: env.people['eor@t.co'], needBy: '2027-01-01',
  })
  assert.equal(bad.status, 400)

  const ic = await env.as('ic@t.co')
  const intake = await ic.post(`${P}/intake`, { statement: 'Vendor data missing for pumps', quickType: 'need_information' })
  assert.equal(intake.status, 200)
  const log = await ic.get(`${P}/log`)
  const row = log.body.find((x: any) => x.ref === intake.body.ref)
  assert.ok(row, 'unanchored item visible in the log')
  assert.equal(row.anchorStatus, 'unanchored')
})

// ---------- I-3 holds are typed ----------

test('I-3: hold requires typed cause, owner, need-by, and ≥1 blocking link', async () => {
  const lead = await env.as('lead@t.co')
  const noCause = await lead.post(`${P}/holds`, {
    title: 'x', ownerId: env.people['lead@t.co'], needBy: '2027-01-01',
    targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
  })
  assert.equal(noCause.status, 400)
  const noOwner = await lead.post(`${P}/holds`, {
    title: 'x', cause: 'vendor_data', needBy: '2027-01-01',
    targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
  })
  assert.equal(noOwner.status, 400)
  const noNeedBy = await lead.post(`${P}/holds`, {
    title: 'x', cause: 'vendor_data', ownerId: env.people['lead@t.co'],
    targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
  })
  assert.equal(noNeedBy.status, 400)
  const noTargets = await lead.post(`${P}/holds`, {
    title: 'x', cause: 'vendor_data', ownerId: env.people['lead@t.co'], needBy: '2027-01-01', targets: [],
  })
  assert.equal(noTargets.status, 400)
  const ok = await lead.post(`${P}/holds`, {
    title: 'Vendor curves missing', cause: 'vendor_data', ownerId: env.people['lead@t.co'],
    needBy: '2027-01-01', targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
  })
  assert.equal(ok.status, 200)
  // cleanup: resolve so later health tests are unaffected
  const resolved = await lead.post(`${P}/holds/${ok.body.id}/resolve`, {
    version: ok.body.version, resolutionKind: 'information_received', note: 'received',
  })
  assert.equal(resolved.status, 200)
})

// ---------- I-4 derived + explainable ----------

test('I-4: overview KPIs and health carry ruleId + contributing records, never bare values', async () => {
  const pm = await env.as('pm@t.co')
  const ov = await pm.get(`${P}/overview`)
  assert.equal(ov.status, 200)
  assert.ok(ov.body.health.ruleId, 'health has a rule id')
  assert.ok(Array.isArray(ov.body.health.contributing), 'health has contributing records')
  for (const k of ['pctOnPlan', 'holdsByCause', 'openDecisions', 'approvalsInFlight', 'scheduleForecastWd']) {
    assert.ok(ov.body.kpis[k].ruleId, `${k} has ruleId`)
    assert.ok(Array.isArray(ov.body.kpis[k].contributing), `${k} has contributing`)
  }
})

// ---------- I-5 condition-gated transitions ----------

test('I-5: a work item with an open hard closure condition cannot close; the blocked attempt is recorded; satisfying the condition unblocks', async () => {
  const lead = await env.as('lead@t.co')
  const eor = await env.as('eor@t.co')
  const wi = await lead.post(`${P}/work-items`, {
    title: 'Update datasheet', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'], needBy: '2027-03-01',
  })
  const cond = await lead.post(`${P}/conditions`, {
    parentType: 'work_item', parentId: wi.body.id, gatedTransition: 'work_item.close',
    type: 'evidence', requiredArtifactName: 'updated-datasheet', severity: 'hard',
    description: 'Attach the updated datasheet',
  })
  assert.equal(cond.status, 200)

  const blocked = await eor.post(`${P}/work-items/${wi.body.id}/transition`, { event: 'close', version: wi.body.version })
  assert.equal(blocked.status, 409)
  assert.equal(blocked.body.error.code, 'CONDITIONS_OPEN')
  assert.ok(blocked.body.error.details.conditions.some((c: any) => c.state === 'open'), '409 lists the open conditions')

  const hist = await eor.get(`${P}/history/work_item/${wi.body.id}`)
  assert.ok(hist.body.some((h: any) => h.kind === 'transition_blocked'), 'prevented invalid closure recorded (§9 metric)')

  const ev = await eor.post(`${P}/records/work_item/${wi.body.id}/evidence`, { label: 'updated-datasheet', kind: 'attachment' })
  assert.equal(ev.status, 200)
  const closed = await eor.post(`${P}/work-items/${wi.body.id}/transition`, { event: 'close', version: wi.body.version })
  assert.equal(closed.status, 200)
  assert.equal(closed.body.state, 'closed')
})

// ---------- I-6 approval ≠ check ≠ decide ----------

test('I-6: check acceptance, approval basis, and approval outcome are three records; outcome is a linked Decision (OM-6)', async () => {
  const lead = await env.as('lead@t.co')
  const dc = await env.as('dc@t.co')
  const approver = await env.as('approver@t.co')

  // fresh deliverable + revision for a clean walk
  const del = await lead.post(`${P}/deliverables`, {
    packageId: env.packageId, docNo: 'TST-PR-002', title: 'P&ID', ownerId: env.people['eor@t.co'], dueDate: '2027-06-30',
  })
  const rev = await lead.post(`${P}/deliverables/${del.body.id}/revisions`, { revCode: 'A' })
  const apr = await lead.post(`${P}/approval-records`, {
    title: 'IFC authorization', approvalType: 'issue_authorization', authoritySource: 'Contract Exhibit C',
    appliesToType: 'revision', appliesToId: rev.body.id, signatoryIds: [env.people['approver@t.co']],
  })
  assert.equal(apr.status, 200)
  assert.equal(apr.body.state, 'prereqs_incomplete', 'check prerequisite instantiated and open')

  // cannot record outcome before ready
  const early = await approver.post(`${P}/approval-records/${apr.body.id}/outcome`, {
    version: apr.body.version, outcome: 'approve', rationale: 'looks fine',
  })
  assert.equal(early.status, 400, 'PEC-AUTH-004: no outcome before ready')

  await acceptCheckOn(env, rev.body.id)
  const aprReady = await lead.get(`${P}/approval-register`)
  const readyRow = aprReady.body.find((a: any) => a.id === apr.body.id)
  assert.equal(readyRow.state, 'ready', 'check acceptance satisfied the prerequisite (distinct fact)')

  // document controller cannot record the outcome even if listed
  const dcTry = await dc.post(`${P}/approval-records/${apr.body.id}/outcome`, {
    version: readyRow.version, outcome: 'approve', rationale: 'no',
  })
  assert.equal(dcTry.status, 403)

  const outcome = await approver.post(`${P}/approval-records/${apr.body.id}/outcome`, {
    version: readyRow.version, outcome: 'approve', rationale: 'design basis confirmed',
  })
  assert.equal(outcome.status, 200)
  assert.equal(outcome.body.state, 'decided')
  assert.ok(outcome.body.outcomeDecisionId, 'outcome is a linked Decision row')

  const decisions = await lead.get(`${P}/decisions`)
  const linked = decisions.body.find((d: any) => d.id === outcome.body.outcomeDecisionId)
  assert.equal(linked.kind, 'approval_outcome')
  assert.equal(linked.outcome, 'approve')
  assert.equal(linked.approvalRecordId, apr.body.id, 'Decision links back to the Approval Record basis')

  // the revision advanced to approved via distinct facts, not a merged flag
  const detail = await lead.get(`${P}/deliverables/${del.body.id}`)
  assert.equal(detail.body.currentRevision.state, 'approved')
  assert.equal(detail.body.facts.checkAccepted, true)
  assert.equal(detail.body.facts.approvalRecorded, true)
  assert.equal(detail.body.facts.issued, false)
})

// ---------- I-7 append-only history ----------

test('I-7: UPDATE/DELETE on history and audit tables are rejected by triggers; intake statement is frozen', async () => {
  // target rows that exist — BEFORE triggers only fire on matching rows
  env.repo.history({
    projectId: env.projectId, recordType: 'work_item', recordId: 1,
    actorId: env.people['admin@t.co']!, kind: 'progress', summary: 'tamper target', payload: null, authorityRef: null,
  })
  env.repo.audit({
    projectId: env.projectId, actorId: env.people['admin@t.co']!, action: 'config_change',
    recordType: 'project', recordId: env.projectId,
  })
  const hid = (env.db.prepare('SELECT MAX(id) AS id FROM history_entry').get() as { id: number }).id
  const aid = (env.db.prepare('SELECT MAX(id) AS id FROM audit_event').get() as { id: number }).id
  assert.throws(() => env.db.prepare('UPDATE history_entry SET summary = ? WHERE id = ?').run('tamper', hid),
    /append-only/)
  assert.throws(() => env.db.prepare('DELETE FROM history_entry WHERE id = ?').run(hid), /append-only/)
  assert.throws(() => env.db.prepare('UPDATE audit_event SET action = ? WHERE id = ?').run('tamper', aid),
    /append-only/)
  assert.throws(() => env.db.prepare('DELETE FROM audit_event WHERE id = ?').run(aid), /append-only/)

  const ic = await env.as('ic@t.co')
  const intake = await ic.post(`${P}/intake`, { statement: 'exact words as raised', quickType: 'action' })
  assert.throws(() => env.db.prepare('UPDATE intake_item SET statement_verbatim = ? WHERE id = ?')
    .run('edited words', intake.body.id), /verbatim/)
})

test('I-7/PEC-NFR-002: controlled records cannot be hard-deleted', async () => {
  const lead = await env.as('lead@t.co')
  const wi = await lead.post(`${P}/work-items`, {
    title: 'Delete target', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'], needBy: '2027-03-01',
  })
  assert.throws(() => env.db.prepare('DELETE FROM work_item WHERE id = ?').run(wi.body.id), /never hard-deleted/)
  assert.throws(() => env.db.prepare('DELETE FROM revision WHERE id = ?').run(env.revisionId), /never hard-deleted/)
  assert.throws(() => env.db.prepare('DELETE FROM deliverable WHERE id = ?').run(env.deliverableId), /never hard-deleted/)
})

// ---------- I-8 waivers are decisions ----------

test('I-8: waiving a condition creates a linked waiver Decision + audit event; unauthorized roles cannot waive', async () => {
  const lead = await env.as('lead@t.co')
  const pm = await env.as('pm@t.co')
  const wi = await lead.post(`${P}/work-items`, {
    title: 'Waiver target', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'], needBy: '2027-03-01',
  })
  const cond = await lead.post(`${P}/conditions`, {
    parentType: 'work_item', parentId: wi.body.id, gatedTransition: 'work_item.close',
    type: 'check', severity: 'hard', description: 'squad check',
  })
  // package lead cannot waive check-type conditions (strict set)
  const leadTry = await lead.post(`${P}/conditions/${cond.body.id}/waive`, {
    version: cond.body.version, rationale: 'nah',
  })
  assert.equal(leadTry.status, 403)

  const waived = await pm.post(`${P}/conditions/${cond.body.id}/waive`, {
    version: cond.body.version, rationale: 'informal squad check done on markup; accepted risk',
  })
  assert.equal(waived.status, 200)
  assert.equal(waived.body.condition.state, 'waived')
  assert.equal(waived.body.decision.kind, 'waiver')
  assert.equal(waived.body.decision.outcome, 'waive')
  assert.equal(waived.body.condition.waiverDecisionId, waived.body.decision.id)

  const audits = env.db.prepare("SELECT * FROM audit_event WHERE action = 'waiver' AND record_id = ?")
    .all(cond.body.id)
  assert.equal(audits.length, 1, 'waiver writes an audit event (PEC-NFR-001)')

  // no path sets waived without a decision: the only API is /waive, and DB shows the link
  const row = env.db.prepare('SELECT waiver_decision_id FROM condition_record WHERE id = ?')
    .get(cond.body.id) as { waiver_decision_id: number }
  assert.ok(row.waiver_decision_id > 0)
})

// ---------- I-10 supersession never deletes ----------

test('I-10: superseding a decision keeps it visible, links the replacement, and flags affected records', async () => {
  const pm = await env.as('pm@t.co')
  const lead = await env.as('lead@t.co')
  const d1 = await lead.post(`${P}/decisions`, {
    title: 'Use CS piping', statement: 'Carbon steel for utility headers',
    authorityId: env.people['pm@t.co'], packageId: env.packageId,
    affected: [{ recordType: 'deliverable', recordId: env.deliverableId }],
  })
  // walk to decided
  const p1 = await pm.post(`${P}/decisions/${d1.body.id}/progress`, { event: 'assign_preparer', version: d1.body.version, preparerId: env.people['eor@t.co'] })
  const p2 = await pm.post(`${P}/decisions/${d1.body.id}/progress`, { event: 'mark_pending', version: p1.body.version })
  const done = await pm.post(`${P}/decisions/${d1.body.id}/outcome`, { version: p2.body.version, outcome: 'select', rationale: 'cost' })
  assert.equal(done.status, 200)

  const d2 = await lead.post(`${P}/decisions`, {
    title: 'Use SS piping', statement: 'Stainless after corrosion review', authorityId: env.people['pm@t.co'],
  })
  const sup = await pm.post(`${P}/decisions/${d1.body.id}/supersede`, { version: done.body.version, replacementId: d2.body.id })
  assert.equal(sup.status, 200)
  assert.equal(sup.body.state, 'superseded')
  assert.equal(sup.body.supersededById, d2.body.id)

  const register = await pm.get(`${P}/decisions`)
  assert.ok(register.body.some((x: any) => x.id === d1.body.id), 'superseded decision remains visible')

  const delHist = await pm.get(`${P}/history/deliverable/${env.deliverableId}`)
  assert.ok(delHist.body.some((h: any) => h.kind === 'basis_superseded'), 'affected record flagged for review')
})

// ---------- concurrency (PEC-NFR-004) ----------

test('PEC-NFR-004: stale version writes are rejected with the intervening history', async () => {
  const lead = await env.as('lead@t.co')
  const wi = await lead.post(`${P}/work-items`, {
    title: 'Concurrent edit target', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'], needBy: '2027-03-01',
  })
  const first = await lead.put(`${P}/work-items/${wi.body.id}`, { version: wi.body.version, priority: 'high' })
  assert.equal(first.status, 200)
  const stale = await lead.put(`${P}/work-items/${wi.body.id}`, { version: wi.body.version, priority: 'low' })
  assert.equal(stale.status, 409)
  assert.equal(stale.body.error.code, 'VERSION_CONFLICT')
  assert.ok(Array.isArray(stale.body.error.details.intervening), 'shows the intervening change')
})

// ---------- RBAC probes (PEC-NFR-005) ----------

test('RBAC: viewer is read-only; checker acceptance is checker-only; decision outcome is authority-only', async () => {
  const viewer = await env.as('viewer@t.co')
  const read = await viewer.get(`${P}/overview`)
  assert.equal(read.status, 200)
  const write = await viewer.post(`${P}/intake`, { statement: 'x', quickType: 'action' })
  assert.equal(write.status, 403)

  const lead = await env.as('lead@t.co')
  const del = await lead.post(`${P}/deliverables`, {
    packageId: env.packageId, docNo: 'TST-PR-003', title: 'Line list', ownerId: env.people['eor@t.co'],
  })
  const rev = await lead.post(`${P}/deliverables/${del.body.id}/revisions`, { revCode: 'A' })
  const chk = await lead.post(`${P}/checks`, { revisionId: rev.body.id, checkerId: env.people['checker@t.co'] })
  const pmTry = await (await env.as('pm@t.co')).post(`${P}/checks/${chk.body.id}/accept`, { version: chk.body.version })
  assert.equal(pmTry.status, 403, 'not even the pm accepts a check (I-6)')
})

// ---------- hold veto (OM-2) ----------

test('OM-2: an active hold vetoes closure of a blocked work item and shows in the 409; resolution unblocks and notifies', async () => {
  const lead = await env.as('lead@t.co')
  const eor = await env.as('eor@t.co')
  const wi = await lead.post(`${P}/work-items`, {
    title: 'Blocked by vendor data', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'], needBy: '2027-04-01',
  })
  const hold = await lead.post(`${P}/holds`, {
    title: 'Awaiting vendor curves', cause: 'vendor_data', ownerId: env.people['lead@t.co'],
    needBy: '2027-02-01', targets: [{ targetType: 'work_item', targetId: wi.body.id }],
  })
  const blocked = await eor.post(`${P}/work-items/${wi.body.id}/transition`, { event: 'close', version: wi.body.version })
  assert.equal(blocked.status, 409)
  assert.ok(blocked.body.error.details.holdVeto.some((h: any) => h.ref === hold.body.ref))

  const resolved = await lead.post(`${P}/holds/${hold.body.id}/resolve`, {
    version: hold.body.version, resolutionKind: 'information_received', note: 'curves received via TR-104',
  })
  assert.equal(resolved.status, 200)
  const closed = await eor.post(`${P}/work-items/${wi.body.id}/transition`, { event: 'close', version: wi.body.version })
  assert.equal(closed.status, 200)

  const notes = await eor.get(`${P}/notifications`)
  assert.ok(notes.body.some((n: any) => n.event === 'hold_resolved_unblocked'), 'owner notified on unblock (§7.3)')
})

// ---------- issue gating end-to-end (PEC-DEL-007/008, D-11) ----------

test('D-11/I-5: revision cannot issue with open hard conditions; full chain check→approve→issue works; audit + archive ref written', async () => {
  const lead = await env.as('lead@t.co')
  const dc = await env.as('dc@t.co')
  const approver = await env.as('approver@t.co')

  const del = await lead.post(`${P}/deliverables`, {
    packageId: env.packageId, docNo: 'TST-PR-004', title: 'Heat & material balance',
    ownerId: env.people['eor@t.co'], dueDate: '2027-06-30',
  })
  const rev = await lead.post(`${P}/deliverables/${del.body.id}/revisions`, { revCode: '0' })

  // issue from in_work is not even a legal transition
  const premature = await dc.post(`${P}/revisions/${rev.body.id}/transition`, {
    event: 'issue', version: rev.body.version,
    issueEvent: { purpose: 'IFR', transmittalRef: 'TR-001', recipients: ['client'] },
  })
  assert.equal(premature.status, 400)

  const apr = await lead.post(`${P}/approval-records`, {
    title: 'IFR authorization', approvalType: 'issue_authorization',
    appliesToType: 'revision', appliesToId: rev.body.id, signatoryIds: [env.people['approver@t.co']],
  })
  await acceptCheckOn(env, rev.body.id)
  const reg = await lead.get(`${P}/approval-register`)
  const aprRow = reg.body.find((a: any) => a.id === apr.body.id)
  await approver.post(`${P}/approval-records/${apr.body.id}/outcome`, {
    version: aprRow.version, outcome: 'approve', rationale: 'ok to issue',
  })

  // add a hard doc-control condition template effect: manual hard condition on issue
  const cond = await lead.post(`${P}/conditions`, {
    parentType: 'revision', parentId: rev.body.id, gatedTransition: 'revision.issue',
    type: 'evidence', requiredArtifactName: 'client-distribution-list', severity: 'hard',
    description: 'Distribution list confirmed',
  })
  const rev2 = await lead.get(`${P}/deliverables/${del.body.id}`)
  assert.equal(rev2.body.currentRevision.state, 'approved')

  const blockedIssue = await dc.post(`${P}/revisions/${rev.body.id}/transition`, {
    event: 'issue', version: rev2.body.currentRevision.version,
    issueEvent: { purpose: 'IFR', transmittalRef: 'TR-002', recipients: ['client-dc'] },
  })
  assert.equal(blockedIssue.status, 409, 'hard condition blocks issue')
  assert.ok(blockedIssue.body.error.details.conditions.some((c: any) => c.ref === cond.body.ref))

  await dc.post(`${P}/records/revision/${rev.body.id}/evidence`, { label: 'client-distribution-list' })
  const issued = await dc.post(`${P}/revisions/${rev.body.id}/transition`, {
    event: 'issue', version: rev2.body.currentRevision.version,
    issueEvent: { purpose: 'IFR', transmittalRef: 'TR-002', recipients: ['client-dc'] },
  })
  assert.equal(issued.status, 200)
  assert.equal(issued.body.state, 'issued')

  const detail = await lead.get(`${P}/deliverables/${del.body.id}`)
  const chainRev = detail.body.revisionChain.find((r: any) => r.id === rev.body.id)
  assert.equal(chainRev.issueEvents.length, 1)
  assert.match(chainRev.issueEvents[0].archiveRef, /^ARC-TST-/, 'archive reference in the P1 chain (PEC-ARC-002)')

  const audits = env.db.prepare("SELECT * FROM audit_event WHERE action = 'issue' AND record_id = ?").all(rev.body.id)
  assert.equal(audits.length, 1, 'issue writes an audit event (PEC-NFR-001)')

  // "before this issues" explanation still renders post-issue with satisfied/waived states (I-4)
  const explain = await lead.get(`${P}/revisions/${rev.body.id}/explain?transition=revision.issue`)
  assert.ok(explain.body.conditions.every((c: any) => c.state !== 'open'))
})

// ---------- import contracts (§16) ----------

test('§16: MDL import validates row-by-row, seeds state, rejects bad rows with reasons; export round-trips', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [
    'doc_no,title,package,discipline,owner,current_rev,state,due_date,milestone',
    'TST-ME-001,Pump datasheet,PKG-M,Mechanical,eor@t.co,B,issued,2027-03-31,G2',
    'TST-ME-002,Compressor datasheet,PKG-M,Mechanical,eor@t.co,A,in work,2027-04-30,',
    'TST-ME-003,Bad row,PKG-M,Mechanical,nobody@nowhere.io,A,fabricated_state,not-a-date,',
  ].join('\n')
  const res = await admin.postCsv(`${P}/import/mdl`, csv)
  assert.equal(res.status, 200)
  assert.equal(res.body.accepted, 2)
  assert.equal(res.body.rejected.length, 1)
  const rejected = res.body.rejected[0]
  assert.equal(rejected.row, 4)
  assert.ok(rejected.errors.length >= 2, 'row-by-row reasons, never silently dropped')

  // imported issued row is SEEDED at issued — no synthetic issue event, history kind=import
  const lead = await env.as('lead@t.co')
  const dels = await lead.get(`${P}/deliverables?view=master`)
  const me1 = dels.body.find((d: any) => d.docNo === 'TST-ME-001')
  assert.equal(me1.state, 'issued')
  const hist = await lead.get(`${P}/history/deliverable/${me1.id}`)
  assert.ok(hist.body.some((h: any) => h.kind === 'import'))

  const out = await lead.get(`${P}/export/mdl.csv`)
  assert.equal(out.status, 200)
  assert.match(out.body, /doc_no,title,package/)
  assert.match(out.body, /TST-ME-001/)
  assert.match(out.body, /issued/)
})

test('§16: RAIL import anchors on doc_no match, else lands as unanchored intake; holds require cause', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [
    'item_id,statement,type,log,owner,need_by,status,raised_by,raised_date,package,deliverable_ref,hold_cause',
    'A-001,Update pump curves,action,internal,eor@t.co,2027-05-01,open,lead@t.co,2026-06-01,PKG-M,TST-ME-001,',
    'A-002,Chase client comment,action,client,eor@t.co,2027-05-01,open,lead@t.co,2026-06-01,,UNKNOWN-DOC,',
    'H-001,Vendor data hold,hold,internal,lead@t.co,2027-05-01,open,lead@t.co,2026-06-01,,TST-ME-001,vendor_data',
    'H-002,Cause-less hold,hold,internal,lead@t.co,2027-05-01,open,lead@t.co,2026-06-01,,TST-ME-001,',
  ].join('\n')
  const res = await admin.postCsv(`${P}/import/rail`, csv)
  assert.equal(res.status, 200)
  assert.equal(res.body.accepted, 2, 'anchored work item + hold')
  assert.equal(res.body.intakeCreated, 1, 'unmatched anchor lands as intake (I-2)')
  assert.equal(res.body.rejected.length, 1, 'hold without cause rejected (I-3)')

  const lead = await env.as('lead@t.co')
  const rail = await lead.get(`${P}/export/rail.csv`)
  assert.match(rail.body, /A-002.*unanchored|unanchored.*A-002/s, 'unanchored intake row round-trips in the export')
})

test('§16: RAIL interface rows require an explicit valid interface status', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [
    'item_id,statement,type,log,owner,need_by,status,raised_by,raised_date,package,deliverable_ref,hold_cause',
    'I-001,Process to mechanical data,interface,package,eor@t.co,2027-05-01,open,lead@t.co,2026-06-01,PKG-M,TST-ME-001,',
    'I-002,Invalid workflow status,interface,package,eor@t.co,2027-05-01,in_work,lead@t.co,2026-06-01,PKG-M,TST-ME-001,',
    'I-003,Missing interface status,interface,package,eor@t.co,2027-05-01,,lead@t.co,2026-06-01,PKG-M,TST-ME-001,',
  ].join('\n')
  const res = await admin.postCsv(`${P}/import/rail`, csv)
  assert.equal(res.status, 200)
  assert.equal(res.body.accepted, 1)
  assert.equal(res.body.rejected.length, 2)
  assert.match(res.body.rejected[0].errors.join(' '), /interface status must be one of/)
  assert.match(res.body.rejected[1].errors.join(' '), /status is required/)

  const reg = await admin.get(`${P}/interfaces`)
  const row = (reg.body as any[]).find((i) => i.ref === 'I-001')
  assert.equal(row.state, 'open')
})
