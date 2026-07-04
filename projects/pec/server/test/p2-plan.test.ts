/**
 * P2 — Plan module, weekly commit, capacity, plan shifts with lead review, schedule import,
 * interface register aging, digests + severity, supersession links, package review pack.
 * PRD §12.4 (PEC-PLAN-*), PEC-MW-007, PEC-PKG-003/008/009, PEC-INT-002, PEC-NOT-002/003,
 * PEC-AUTH-005, §16 P2, I-9.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { isoWeekOf } from '@pec/core'
import { createTestEnv } from './harness.ts'
import { sweepProject } from '../src/services/sweep.ts'

const P = (env: { projectId: number }): string => `/api/projects/${env.projectId}`

test('plan items: pm plans work/checks/approvals; contributor denied; duplicates rejected (PEC-PLAN-001, I-9)', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const ic = await env.as('ic@t.co')
    const week = isoWeekOf(env.repo.snapshot(env.projectId).today)

    const wi = await pm.post(`${P(env)}/work-items`, {
      title: 'Draft PFD', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null,
    })
    assert.equal(wi.status, 200, JSON.stringify(wi.body))

    const denied = await ic.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi.body.id, horizon: 'now', week, plannedHours: 8,
    })
    assert.equal(denied.status, 403, 'contributors do not manage the plan (PRD §14)')

    const planned = await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi.body.id, horizon: 'now', week, plannedHours: 8, discipline: 'Process',
    })
    assert.equal(planned.status, 200, JSON.stringify(planned.body))
    assert.match(planned.body.ref, /^PLN-/)

    const dup = await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi.body.id, horizon: 'next', week, plannedHours: 4,
    })
    assert.equal(dup.status, 400, 'one placement per record — move it with a shift')

    // 'now' placement requires a week
    const wi2 = await pm.post(`${P(env)}/work-items`, {
      title: 'Another', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null,
    })
    const noWeek = await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi2.body.id, horizon: 'now', plannedHours: 4,
    })
    assert.equal(noWeek.status, 400)

    const view = await pm.get(`${P(env)}/plan`)
    assert.equal(view.status, 200)
    assert.equal(view.body.horizons.now.length, 1)
    assert.equal(view.body.horizons.now[0].itemRef, wi.body.ref)
    assert.equal(view.body.currentWeek, week)
  } finally {
    await env.close()
  }
})

test('plan shift: same-package applies with reason; reason required (PEC-PLAN-006)', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const week = isoWeekOf(env.repo.snapshot(env.projectId).today)
    const wi = await pm.post(`${P(env)}/work-items`, {
      title: 'Shiftable', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null,
    })
    const pi = await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi.body.id, horizon: 'now', week, plannedHours: 8,
    })

    const noReason = await pm.post(`${P(env)}/plan-items/${pi.body.id}/shift`, {
      version: pi.body.version, toHorizon: 'later', toWeek: null,
    })
    assert.equal(noReason.status, 400, 'every shift records its reason (PEC-PLAN-006)')

    const shifted = await pm.post(`${P(env)}/plan-items/${pi.body.id}/shift`, {
      version: pi.body.version, toHorizon: 'later', toWeek: null, reason: 'client review slipped',
    })
    assert.equal(shifted.status, 200, JSON.stringify(shifted.body))
    assert.equal(shifted.body.state, 'applied', 'within-package shifts apply immediately')
    assert.equal(shifted.body.crossPackage, false)

    const view = await pm.get(`${P(env)}/plan`)
    assert.equal(view.body.horizons.later.length, 1)
    assert.equal(view.body.shifts[0].reason, 'client review slipped')
  } finally {
    await env.close()
  }
})

test('cross-package shift proposes, notifies the affected lead, and applies only on review (PEC-PLAN-005/008)', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const week = isoWeekOf(env.repo.snapshot(env.projectId).today)

    // second package led by coord (any member can hold the lead seat for the test)
    const pkg2 = await pm.post(`${P(env)}/packages`, {
      code: 'PKG-B', name: 'Mechanical', leadId: env.people['coord@t.co'],
    })
    assert.equal(pkg2.status, 200, JSON.stringify(pkg2.body))
    // a risk owned at package B — linking it makes the shift cross-package
    const risk = await pm.post(`${P(env)}/risks`, {
      title: 'Vendor slip', packageId: pkg2.body.id, ownerId: env.people['lead@t.co'], state: 'open',
    })
    assert.equal(risk.status, 200, JSON.stringify(risk.body))

    const wi = await pm.post(`${P(env)}/work-items`, {
      title: 'Cross work', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null,
    })
    const pi = await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi.body.id, horizon: 'now', week, plannedHours: 8,
    })

    const noImpact = await pm.post(`${P(env)}/plan-items/${pi.body.id}/shift`, {
      version: pi.body.version, toHorizon: 'next', toWeek: week, reason: 'rebalance',
      links: [{ recordType: 'risk', recordId: risk.body.id }],
    })
    assert.equal(noImpact.status, 400, 'cross-package shifts need an impact statement (PEC-PLAN-005)')

    const proposed = await pm.post(`${P(env)}/plan-items/${pi.body.id}/shift`, {
      version: pi.body.version, toHorizon: 'next', toWeek: week, reason: 'rebalance',
      impactStatement: 'affects PKG-B vendor risk mitigation window',
      links: [{ recordType: 'risk', recordId: risk.body.id }],
    })
    assert.equal(proposed.status, 200, JSON.stringify(proposed.body))
    assert.equal(proposed.body.state, 'proposed')
    assert.equal(proposed.body.crossPackage, true)

    // plan item NOT moved yet
    let view = await pm.get(`${P(env)}/plan`)
    assert.equal(view.body.horizons.now.length, 1)

    // affected lead was notified for review
    const coord = await env.as('coord@t.co')
    const notifs = await coord.get(`${P(env)}/notifications`)
    assert.ok(notifs.body.some((n: any) => n.event === 'plan_shift_review'),
      'affected package lead notified (PEC-PLAN-005)')

    // ic (contributor) cannot review; the pm can (leads of affected packages + pm/EM)
    const ic = await env.as('ic@t.co')
    const deniedReview = await ic.post(`${P(env)}/plan-shifts/${proposed.body.id}/review`, {
      version: proposed.body.version, approve: true,
    })
    assert.equal(deniedReview.status, 403)

    const approved = await pm.post(`${P(env)}/plan-shifts/${proposed.body.id}/review`, {
      version: proposed.body.version, approve: true,
    })
    assert.equal(approved.status, 200, JSON.stringify(approved.body))
    assert.equal(approved.body.state, 'applied')

    view = await pm.get(`${P(env)}/plan`)
    assert.equal(view.body.horizons.next.length, 1, 'move applied after review')
  } finally {
    await env.close()
  }
})

test('weekly commit generates My Week: committedWeek stamped from the plan, owner notified, idempotent (PEC-PLAN-007, PEC-MW-007)', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const ic = await env.as('ic@t.co')
    const week = isoWeekOf(env.repo.snapshot(env.projectId).today)

    const wi = await pm.post(`${P(env)}/work-items`, {
      title: 'Committed work', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null,
    })
    await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi.body.id, horizon: 'now', week, plannedHours: 8,
    })

    // before the commit: not in My Week
    let mw = await ic.get(`${P(env)}/my-week`)
    assert.ok(!mw.body.committed.some((x: any) => x.workItem.id === wi.body.id))

    const denied = await ic.post(`${P(env)}/plan/commit`, { week })
    assert.equal(denied.status, 403, 'planners/pm commit plans (PRD §14)')

    const committed = await pm.post(`${P(env)}/plan/commit`, { week })
    assert.equal(committed.status, 200, JSON.stringify(committed.body))
    assert.equal(committed.body.committedWorkItems, 1)
    assert.equal(committed.body.period.state, 'committed')

    mw = await ic.get(`${P(env)}/my-week`)
    const item = mw.body.committed.find((x: any) => x.workItem.id === wi.body.id)
    assert.ok(item, 'weekly commit generated the My Week set')
    assert.match(item.whyInWeek, /planning commitment/, 'PEC-MW-005 provenance')

    const notifs = await ic.get(`${P(env)}/notifications`)
    const wc = notifs.body.filter((n: any) => n.event === 'week_committed')
    assert.equal(wc.length, 1)

    // re-commit: no duplicate stamps or notifications
    const again = await pm.post(`${P(env)}/plan/commit`, { week })
    assert.equal(again.status, 200)
    assert.equal(again.body.committedWorkItems, 0)
    assert.equal(again.body.notified, 0)
  } finally {
    await env.close()
  }
})

test('capacity: PUT capacity + overload surfaces in plan view, package health (PH-R3), S-CAP, and schedule pressure (PEC-PLAN-003/004, PEC-OV-008)', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const week = isoWeekOf(env.repo.snapshot(env.projectId).today)

    const wi = await pm.post(`${P(env)}/work-items`, {
      title: 'Heavy work', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null,
    })
    await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi.body.id, horizon: 'now', week, plannedHours: 46, discipline: 'Process',
    })
    const cap = await pm.put(`${P(env)}/plan/capacity`, { week, discipline: 'Process', hours: 40 })
    assert.equal(cap.status, 200, JSON.stringify(cap.body))

    const view = await pm.get(`${P(env)}/plan`)
    const cell = view.body.capacity.find((c: any) => c.week === week && c.discipline === 'Process')
    assert.equal(cell.pct, 115)
    assert.equal(cell.level, 'red')

    const pkgs = await pm.get(`${P(env)}/packages`)
    const row = pkgs.body.find((r: any) => r.id === env.packageId)
    assert.equal(row.health.ruleId, 'PH-R3', JSON.stringify(row.health))

    const overview = await pm.get(`${P(env)}/overview`)
    const sCap = overview.body.signals.find((s: any) => s.id === 'S-CAP')
    assert.equal(sCap.level, 'red')
    const pressure = overview.body.schedulePressure.find((wk: any) => wk.week === week)
    assert.equal(pressure.pct, 115, 'PEC-OV-008 schedule-pressure view')
    assert.equal(pressure.breaches[0].discipline, 'Process')

    // upsert overwrites
    const cap2 = await pm.put(`${P(env)}/plan/capacity`, { week, discipline: 'Process', hours: 92 })
    assert.equal(cap2.status, 200)
    const view2 = await pm.get(`${P(env)}/plan`)
    const cell2 = view2.body.capacity.find((c: any) => c.week === week && c.discipline === 'Process')
    assert.equal(cell2.capacityH, 92)
    assert.equal(cell2.level, 'none')
  } finally {
    await env.close()
  }
})

test('§16 P2 schedule import: row-level rejects, idempotent refresh, round-trip export, lookahead export', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const csv = [
      'activity_id,description,start,finish,package,deliverable_ref',
      'A100,Issue PFD,2027-01-04,2027-01-15,PKG-A,TST-PR-001',
      'A110,HAZOP prep,2027-01-11,2027-01-22,PKG-A,',
      'A120,Bad row,2027-02-01,2027-01-01,,',            // finish before start
      'A130,Unmatched map,2027-01-04,2027-01-08,,NOPE-1', // stated mapping must resolve
    ].join('\r\n')
    const rep = await admin.postCsv(`${P(env)}/import/schedule`, csv)
    assert.equal(rep.status, 200, JSON.stringify(rep.body))
    assert.equal(rep.body.accepted, 2)
    assert.equal(rep.body.rejected.length, 2)

    const again = await admin.postCsv(`${P(env)}/import/schedule`,
      'activity_id,description,start,finish\r\nA100,Issue PFD (rev),2027-01-04,2027-01-18')
    assert.equal(again.body.updated, 1, 're-import refreshes in place (import-owned data)')
    assert.equal(again.body.accepted, 0)

    const exported = await admin.get(`${P(env)}/export/schedule.csv`)
    assert.equal(exported.status, 200)
    assert.match(exported.body, /A100,Issue PFD \(rev\)/)
    assert.match(exported.body, /TST-PR-001/)

    const la = await admin.get(`${P(env)}/export/lookahead.csv`)
    assert.equal(la.status, 200)
    assert.match(String(la.body).split('\r\n')[0]!, /doc_no,title,package,due_date,\d{4}-W\d{2}/)
  } finally {
    await env.close()
  }
})

test('interface register: aging + giving/receiving filters (PEC-INT-002); aging feeds package health (PEC-PKG-008)', async () => {
  const env = await createTestEnv()
  try {
    const lead = await env.as('lead@t.co')
    const made = await lead.post(`${P(env)}/interfaces`, {
      title: 'Nozzle loads', givingParty: 'Process', receivingParty: 'Mechanical',
      givingPackageId: env.packageId, requiredInfo: 'loads table', needBy: '2020-01-01', state: 'open',
    })
    assert.equal(made.status, 200, JSON.stringify(made.body))

    const reg = await lead.get(`${P(env)}/interfaces?giving=${env.packageId}`)
    assert.equal(reg.status, 200)
    const row = reg.body.find((i: any) => i.id === made.body.id)
    assert.ok(row.overdueWd > 0, 'aging computed')
    assert.equal(row.aging, 'red', 'past escalation')
    assert.equal(row.givingPackageCode, 'PKG-A')

    const none = await lead.get(`${P(env)}/interfaces?receiving=${env.packageId}`)
    assert.ok(!none.body.some((i: any) => i.id === made.body.id), 'receiving filter excludes giving-side row')

    const pkgs = await lead.get(`${P(env)}/packages`)
    const pkgRow = pkgs.body.find((r: any) => r.id === env.packageId)
    assert.equal(pkgRow.health.ruleId, 'PH-R2', 'far past escalation is the P1 red rule; PH-A4 covers the aging tier')
  } finally {
    await env.close()
  }
})

test('PEC-NOT-002/003: sweep emits severity-tagged overdue notifications and weekly digests, idempotently', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    // decision 10 days overdue → authority digest + red severity (past decisionOverdueRedD=7)
    const dec = await pm.post(`${P(env)}/decisions`, {
      title: 'Late decision', statement: 'overdue', authorityId: env.people['pm@t.co'],
      needBy: '2020-01-01', packageId: env.packageId,
    })
    assert.equal(dec.status, 200)

    const first = sweepProject(env.db, env.projectId)
    assert.ok(first >= 2, `sweep emits the overdue event and digests (got ${first})`)
    const second = sweepProject(env.db, env.projectId)
    assert.equal(second, 0, 'sweep is idempotent per day/week')

    const notifs = await pm.get(`${P(env)}/notifications`)
    const overdue = notifs.body.find((n: any) => n.event === 'decision_past_need_by')
    assert.equal(overdue.severity, 'red', '§8.4 escalation drives severity (PEC-NOT-003)')
    const digest = notifs.body.find((n: any) => n.event === 'digest_judgments')
    assert.ok(digest, 'weekly judgments digest (PEC-NOT-002)')
    assert.equal(digest.severity, 'red')
    const leadNotifs = await (await env.as('lead@t.co')).get(`${P(env)}/notifications`)
    assert.ok(leadNotifs.body.some((n: any) => n.event === 'digest_package_review'),
      'package lead gets the package-review digest')
  } finally {
    await env.close()
  }
})

test('PEC-AUTH-005: superseding writes a first-class supersession link with the affected-record set', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const a = await pm.post(`${P(env)}/decisions`, {
      title: 'Units basis', statement: 'metric', authorityId: env.people['pm@t.co'],
      needBy: '2027-01-01',
      affected: [{ recordType: 'deliverable', recordId: env.deliverableId }],
    })
    assert.equal(a.status, 200, JSON.stringify(a.body))
    // decide it first — only decided decisions can be superseded (§7.6)
    const prepared = await pm.post(`${P(env)}/decisions/${a.body.id}/progress`, {
      event: 'assign_preparer', version: a.body.version, preparerId: env.people['lead@t.co'],
    })
    assert.equal(prepared.status, 200, JSON.stringify(prepared.body))
    const pending = await pm.post(`${P(env)}/decisions/${a.body.id}/progress`, {
      event: 'mark_pending', version: prepared.body.version,
    })
    assert.equal(pending.status, 200, JSON.stringify(pending.body))
    const decided = await pm.post(`${P(env)}/decisions/${a.body.id}/outcome`, {
      version: pending.body.version, outcome: 'confirm_basis', rationale: 'metric confirmed',
    })
    assert.equal(decided.status, 200, JSON.stringify(decided.body))
    const b = await pm.post(`${P(env)}/decisions`, {
      title: 'Units basis (revised)', statement: 'imperial', authorityId: env.people['pm@t.co'],
      needBy: '2027-01-01',
    })
    const sup = await pm.post(`${P(env)}/decisions/${a.body.id}/supersede`, {
      version: decided.body.version, replacementId: b.body.id,
    })
    assert.equal(sup.status, 200, JSON.stringify(sup.body))

    const link = env.db.prepare(
      "SELECT * FROM supersession_link WHERE record_type = 'decision' AND old_id = ?",
    ).get(a.body.id) as { new_id: number; affected: string } | undefined
    assert.ok(link, 'supersession link recorded')
    assert.equal(link!.new_id, b.body.id)
    const affected = JSON.parse(link!.affected) as Array<{ recordType: string; ref: string }>
    assert.ok(affected.some((x) => x.recordType === 'deliverable' && x.ref === 'TST-PR-001'),
      'affected-record set identified for review')

    // append-only: the link is a record of change, never deleted (PEC-NFR-002 posture)
    assert.throws(() => env.db.prepare('DELETE FROM supersession_link').run())
  } finally {
    await env.close()
  }
})

test('PEC-NFR-005: the plan view redacts and filters restricted-log work items per caller', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const week = isoWeekOf(env.repo.snapshot(env.projectId).today)
    const secret = await pm.post(`${P(env)}/work-items`, {
      title: 'SECRET internal action', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null, log: 'internal',
    })
    const open = await pm.post(`${P(env)}/work-items`, {
      title: 'Client-visible action', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null, log: 'client',
    })
    await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: secret.body.id, horizon: 'now', week, plannedHours: 8,
    })

    // pm sees all logs
    const pmView = await pm.get(`${P(env)}/plan`)
    assert.ok(JSON.stringify(pmView.body).includes('SECRET internal action'))

    // viewer defaults to package+client: title redacted in horizons, absent from plannable
    const viewer = await env.as('viewer@t.co')
    const vView = await viewer.get(`${P(env)}/plan`)
    assert.equal(vView.status, 200)
    assert.ok(!JSON.stringify(vView.body).includes('SECRET internal action'),
      'internal-log work-item title must not reach a restricted caller (PEC-NFR-005)')
    const row = vView.body.horizons.now.find((x: any) => x.itemId === secret.body.id)
    assert.equal(row.title, '[restricted log]', 'planned row stays (capacity truth) with the title redacted')
    assert.ok(vView.body.plannable.some((x: any) => x.itemId === open.body.id), 'client-log item still offered')
    assert.ok(!vView.body.plannable.some((x: any) => x.itemId === secret.body.id))

    // the package review pack follows the same rule (PEC-PKG-009)
    const dueSoon = await pm.put(`${P(env)}/work-items/${secret.body.id}`, {
      version: secret.body.version, needBy: '2020-01-01',
    })
    assert.equal(dueSoon.status, 200)
    const pack = await viewer.get(`${P(env)}/reports/package-pack/${env.packageId}`)
    assert.equal(pack.status, 200)
    assert.ok(!String(pack.body).includes('SECRET internal action'), 'pack filters restricted-log rows')
    const pmPack = await pm.get(`${P(env)}/reports/package-pack/${env.packageId}`)
    assert.ok(String(pmPack.body).includes('SECRET internal action'))
  } finally {
    await env.close()
  }
})

test('PEC-PLAN-005 hardening: origin lead cannot self-approve; stale reviews refuse to apply', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const lead = await env.as('lead@t.co') // leads PKG-A (origin)
    const week = isoWeekOf(env.repo.snapshot(env.projectId).today)

    // give checker@t.co the lead seat of a second package
    const pkg2 = await pm.post(`${P(env)}/packages`, {
      code: 'PKG-C', name: 'Civil', leadId: env.people['checker@t.co'],
    })
    env.db.prepare('INSERT INTO project_role (project_id, person_id, role) VALUES (?, ?, ?)')
      .run(env.projectId, env.people['checker@t.co']!, 'package_lead')
    const risk = await pm.post(`${P(env)}/risks`, {
      title: 'Civil risk', packageId: pkg2.body.id, ownerId: env.people['lead@t.co'], state: 'open',
    })

    const wi = await pm.post(`${P(env)}/work-items`, {
      title: 'Origin work', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null,
    })
    const pi = await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi.body.id, horizon: 'now', week, plannedHours: 8,
    })
    const proposed = await lead.post(`${P(env)}/plan-items/${pi.body.id}/shift`, {
      version: pi.body.version, toHorizon: 'next', toWeek: week, reason: 'rebalance',
      impactStatement: 'delays civil risk mitigation',
      links: [{ recordType: 'risk', recordId: risk.body.id }],
    })
    assert.equal(proposed.status, 200, JSON.stringify(proposed.body))
    assert.equal(proposed.body.state, 'proposed')
    assert.deepEqual(proposed.body.affectedPackageIds, [pkg2.body.id], 'affected = the foreign packages only')

    // the origin package's lead (also the proposer) cannot review it
    const selfReview = await lead.post(`${P(env)}/plan-shifts/${proposed.body.id}/review`, {
      version: proposed.body.version, approve: true,
    })
    assert.equal(selfReview.status, 403, JSON.stringify(selfReview.body))

    // meanwhile the plan item moves through a legitimate same-package shift…
    const fresh = await pm.get(`${P(env)}/plan`)
    const current = fresh.body.horizons.now.find((x: any) => x.id === pi.body.id)
    const moved = await pm.post(`${P(env)}/plan-items/${pi.body.id}/shift`, {
      version: current.version, toHorizon: 'later', toWeek: null, reason: 'parked pending inputs',
    })
    assert.equal(moved.status, 200, JSON.stringify(moved.body))

    // …so the earlier proposal is stale: the affected lead's approval must refuse to blind-apply
    const checkerLead = await env.as('checker@t.co')
    const staleApprove = await checkerLead.post(`${P(env)}/plan-shifts/${proposed.body.id}/review`, {
      version: proposed.body.version, approve: true,
    })
    assert.equal(staleApprove.status, 400, JSON.stringify(staleApprove.body))
    assert.match(staleApprove.body.error.message, /stale/)
  } finally {
    await env.close()
  }
})

test('PEC-NOT-002: a lead of several packages gets one package-review digest per package', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    // lead@t.co already leads PKG-A; give them a second package with its own overdue decision
    const pkg2 = await pm.post(`${P(env)}/packages`, {
      code: 'PKG-D', name: 'Second scope', leadId: env.people['lead@t.co'],
    })
    for (const pkgId of [env.packageId, pkg2.body.id]) {
      const d = await pm.post(`${P(env)}/decisions`, {
        title: `Overdue in pkg ${pkgId}`, statement: 'late', authorityId: env.people['pm@t.co'],
        needBy: '2020-01-01', packageId: pkgId,
      })
      assert.equal(d.status, 200)
    }
    sweepProject(env.db, env.projectId)
    const lead = await env.as('lead@t.co')
    const notifs = await lead.get(`${P(env)}/notifications`)
    const digests = notifs.body.filter((n: any) => n.event === 'digest_package_review')
    assert.equal(digests.length, 2, 'one digest per led package (PEC-NOT-002)')
    assert.equal(sweepProject(env.db, env.projectId), 0, 'still idempotent within the week')
  } finally {
    await env.close()
  }
})

test('PEC-OV-007: GET config serves thresholds merged with the shipped defaults', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const cfg = await admin.get(`${P(env)}/config`)
    assert.equal(cfg.status, 200)
    assert.equal(cfg.body.thresholds.capacityWarnPct, 100, 'effective default shown, not 0')
    assert.equal(cfg.body.thresholds.holdAgeRedWd, 14)
  } finally {
    await env.close()
  }
})

test('PEC-PKG-009: the weekly package review pack renders with capacity, lookahead, and issues', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const week = isoWeekOf(env.repo.snapshot(env.projectId).today)
    const wi = await pm.post(`${P(env)}/work-items`, {
      title: 'Pack work', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: null,
    })
    await pm.post(`${P(env)}/plan-items`, {
      itemType: 'work_item', itemId: wi.body.id, horizon: 'now', week, plannedHours: 8, discipline: 'Process',
    })
    await pm.put(`${P(env)}/plan/capacity`, { week, discipline: 'Process', hours: 40 })

    const pack = await pm.get(`${P(env)}/reports/package-pack/${env.packageId}`)
    assert.equal(pack.status, 200)
    const html = String(pack.body)
    assert.match(html, /Weekly package review pack/)
    assert.match(html, /PKG-A/)
    assert.match(html, /Six-week lookahead/)
    assert.match(html, /Capacity — current week/)
    assert.match(html, /TST-PR-001/)

    const missing = await pm.get(`${P(env)}/reports/package-pack/99999`)
    assert.equal(missing.status, 404)

    // the package detail view carries the capacity block too (PEC-PKG-003)
    const detail = await pm.get(`${P(env)}/packages/${env.packageId}`)
    assert.equal(detail.body.capacity.week, week)
    assert.ok(detail.body.capacity.rows.some((r: any) => r.discipline === 'Process' && r.packageLoadH === 8))
  } finally {
    await env.close()
  }
})
