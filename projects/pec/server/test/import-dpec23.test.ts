/**
 * D-PEC-23 — §16 optional-column extensions + schema-fit views.
 * Covers: mdl package attributes (package_name/area/package_type), rail area,
 * decisions open_date/area/source, risks classification + residual pair,
 * schedule WBS columns + the read-only schedule register, and the widened
 * register exports (round-trip §16). All fixtures synthetic.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'

const P = (env: TestEnv) => `/api/projects/${env.projectId}`

test('mdl: optional package attributes create and refresh the package; deliverables view carries type+area; area filter', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const v1 = [
      'doc_no,title,package,discipline,owner,current_rev,state,due_date,package_name,area,package_type',
      'TWD-001,Earthworks SOW,PKG-100,Civil,,A,in_work,,Earthworks,01,Standard Package',
      'TWD-002,Earthworks TDS,PKG-100,Civil,,A,in_work,,Earthworks,01,Standard Package',
    ].join('\r\n')
    const r1 = await admin.postCsv(`${P(env)}/import/mdl`, v1)
    assert.equal(r1.status, 200, JSON.stringify(r1.body))
    assert.equal(r1.body.accepted, 2)
    assert.equal(r1.body.rejected.length, 0)

    // the auto-created package carries the attribute columns
    const pkgs = await admin.get(`${P(env)}/packages`)
    const pkg = (pkgs.body as any[]).find((p) => p.code === 'PKG-100')
    assert.ok(pkg, 'package auto-created')
    assert.equal(pkg.name, 'Earthworks')
    assert.equal(pkg.area, '01')
    assert.equal(pkg.packageType, 'Standard Package')

    // deliverables view rows carry deliverableType + area; ?area= filters
    const all = await admin.get(`${P(env)}/deliverables`)
    const row = (all.body as any[]).find((d) => d.docNo === 'TWD-001')
    assert.equal(row.area, '01')
    const filtered = await admin.get(`${P(env)}/deliverables?area=01`)
    assert.ok((filtered.body as any[]).some((d) => d.docNo === 'TWD-001'))
    const none = await admin.get(`${P(env)}/deliverables?area=99`)
    assert.ok(!(none.body as any[]).some((d) => d.docNo === 'TWD-001'))

    // re-import with changed attributes refreshes the package (import-owned guard path)
    const v2 = [
      'doc_no,title,package,discipline,owner,current_rev,state,due_date,package_name,area,package_type',
      'TWD-001,Earthworks SOW,PKG-100,Civil,,A,in_work,,Earthworks for foundations,02,FEED Deliverable Package',
    ].join('\r\n')
    const r2 = await admin.postCsv(`${P(env)}/import/mdl`, v2)
    assert.equal(r2.body.updated, 1)
    const pkgs2 = await admin.get(`${P(env)}/packages`)
    const pkg2 = (pkgs2.body as any[]).find((p) => p.code === 'PKG-100')
    assert.equal(pkg2.name, 'Earthworks for foundations')
    assert.equal(pkg2.area, '02')
    assert.equal(pkg2.packageType, 'FEED Deliverable Package')

    // a file without the optional headers changes no package attribute (§16: update only when present)
    const v3 = [
      'doc_no,title,package,discipline,owner,current_rev,state,due_date',
      'TWD-001,Earthworks SOW,PKG-100,Civil,,A,in_work,',
    ].join('\r\n')
    await admin.postCsv(`${P(env)}/import/mdl`, v3)
    const pkgs3 = await admin.get(`${P(env)}/packages`)
    const pkg3 = (pkgs3.body as any[]).find((p) => p.code === 'PKG-100')
    assert.equal(pkg3.area, '02', 'absent optional headers must not wipe package attributes')

    // mdl export mirrors the widened contract
    const exp = await admin.get(`${P(env)}/export/mdl.csv`)
    const header = String(exp.body).split('\r\n')[0]!
    for (const h of ['package_name', 'area', 'package_type']) {
      assert.ok(header.split(',').includes(h), `mdl export header missing ${h}`)
    }
  } finally {
    await env.close()
  }
})

test('rail: optional area lands on anchored work items and unanchored intake; /log carries and filters it', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const csv = [
      'item_id,statement,type,log,owner,need_by,status,raised_by,raised_date,package,deliverable_ref,hold_cause,closed_date,notes,anchor_status,area',
      'TWD-R1,Confirm tie-in point,action,package,Ada Admin,2027-03-01,open,Ada Admin,2026-07-01,,TST-PR-001,,,,anchored,26020-01 - Deep Cut',
      'TWD-R2,Unanchored concern,action,package,Ada Admin,2027-03-01,open,Ada Admin,2026-07-01,,,,,,unanchored,Common',
    ].join('\r\n')
    const rep = await admin.postCsv(`${P(env)}/import/rail`, csv)
    assert.equal(rep.status, 200, JSON.stringify(rep.body))
    assert.equal(rep.body.accepted, 1)
    assert.equal(rep.body.intakeCreated, 1)

    const log = await admin.get(`${P(env)}/log`)
    const wi = (log.body as any[]).find((r) => r.ref === 'TWD-R1')
    assert.equal(wi.area, '26020-01 - Deep Cut')
    const intake = (log.body as any[]).find((r) => r.recordType === 'intake_item' && r.title.includes('TWD-R2'))
    assert.equal(intake.area, 'Common')

    const filtered = await admin.get(`${P(env)}/log?area=${encodeURIComponent('Common')}`)
    assert.ok((filtered.body as any[]).every((r) => r.area === 'Common'))
    assert.ok((filtered.body as any[]).some((r) => r.recordType === 'intake_item'))

    // rail export mirrors the widened contract
    const exp = await admin.get(`${P(env)}/export/rail.csv`)
    const header = String(exp.body).split('\r\n')[0]!
    assert.ok(header.split(',').includes('area'), 'rail export header missing area')
    assert.match(String(exp.body), /26020-01 - Deep Cut/)
  } finally {
    await env.close()
  }
})

test('decisions: open_date/area/source imported, validated, viewed, and round-tripped', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const csv = [
      'decision_id,title,statement,authority,need_by,status,preparer,outcome,rationale,decided_date,affected_refs,open_date,area,source',
      'TWD-D1,Inlet separation,Proceed with two-stage,Ada Admin,2027-01-15,decided,,select,,2026-03-30,,2026-03-05,26020-01 - Deep Cut,Client RAIL',
      'TWD-D2,Bad open date,Statement,Ada Admin,,identified,,,,,,not-a-date,,',
    ].join('\r\n')
    const rep = await admin.postCsv(`${P(env)}/import/decisions`, csv)
    assert.equal(rep.status, 200, JSON.stringify(rep.body))
    assert.equal(rep.body.accepted, 1)
    assert.equal(rep.body.rejected.length, 1)
    assert.match(rep.body.rejected[0].errors.join(' '), /open_date/)

    const reg = await admin.get(`${P(env)}/decisions`)
    const d = (reg.body as any[]).find((x) => x.ref === 'TWD-D1')
    assert.equal(d.openDate, '2026-03-05')
    assert.equal(d.area, '26020-01 - Deep Cut')
    assert.equal(d.source, 'Client RAIL')

    // export mirrors and re-importing the export updates in place (§16 round-trip)
    const exp = await admin.get(`${P(env)}/export/decisions.csv`)
    const header = String(exp.body).split('\r\n')[0]!
    for (const h of ['open_date', 'area', 'source']) {
      assert.ok(header.split(',').includes(h), `decisions export header missing ${h}`)
    }
    const again = await admin.postCsv(`${P(env)}/import/decisions`, exp.body as string)
    assert.equal(again.body.rejected.length, 0, JSON.stringify(again.body.rejected))
    assert.ok(again.body.updated >= 1, 're-importing the export updates the same row')
  } finally {
    await env.close()
  }
})

test('risks: classification + residual pair imported and validated; export mirrors', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const csv = [
      'risk_id,title,cause,consequence,owner,status,package,deliverable_ref,probability,impact,mitigation,need_by,category,risk_type,treatment,residual_probability,residual_impact',
      'TWD-RSK1,Vendor data late,Long-lead vendor,Schedule slip,Ada Admin,open,,,4,4,Expedite,2027-02-01,Supply Chain,Threat,Mitigate,2,3',
      'TWD-RSK2,Bad residual,c,q,Ada Admin,open,,,3,3,,,Technical,Threat,Accept,9,1',
    ].join('\r\n')
    const rep = await admin.postCsv(`${P(env)}/import/risks`, csv)
    assert.equal(rep.status, 200, JSON.stringify(rep.body))
    assert.equal(rep.body.accepted, 1)
    assert.equal(rep.body.rejected.length, 1)
    assert.match(rep.body.rejected[0].errors.join(' '), /residual_probability/)

    const reg = await admin.get(`${P(env)}/risks`)
    const r = (reg.body as any[]).find((x) => x.ref === 'TWD-RSK1')
    assert.equal(r.category, 'Supply Chain')
    assert.equal(r.riskType, 'Threat')
    assert.equal(r.treatment, 'Mitigate')
    assert.equal(r.residualProbability, 2)
    assert.equal(r.residualImpact, 3)

    const exp = await admin.get(`${P(env)}/export/risks.csv`)
    const header = String(exp.body).split('\r\n')[0]!
    for (const h of ['category', 'risk_type', 'treatment', 'residual_probability', 'residual_impact']) {
      assert.ok(header.split(',').includes(h), `risks export header missing ${h}`)
    }
  } finally {
    await env.close()
  }
})

test('schedule: WBS columns imported + validated; register view resolves; no silent wipe on narrower re-import', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const csv = [
      'activity_id,description,start,finish,package,deliverable_ref,row_type,outline_level,parent_activity_id,percent_complete,duration_days,baseline_start,baseline_finish',
      'SCH-1,TOU West Doe Complete,2026-01-28,2028-03-15,,,summary,0,,10,551,2026-01-28,2028-03-01',
      'SCH-2,Issue PFD,2026-02-02,2026-02-20,PKG-A,TST-PR-001,task,1,SCH-1,50,15,2026-02-02,2026-02-18',
      'SCH-3,FEED complete,2026-06-01,2026-06-01,,,milestone,1,SCH-1,0,0,,',
      'SCH-4,Bad type,2026-02-02,2026-02-20,,,phase,1,,,,,',
      'SCH-5,Bad pct,2026-02-02,2026-02-20,,,task,1,,150,,,',
    ].join('\r\n')
    const rep = await admin.postCsv(`${P(env)}/import/schedule`, csv)
    assert.equal(rep.status, 200, JSON.stringify(rep.body))
    assert.equal(rep.body.accepted, 3)
    assert.equal(rep.body.rejected.length, 2)
    const errs = rep.body.rejected.flatMap((x: any) => x.errors).join(' ')
    assert.match(errs, /row_type/)
    assert.match(errs, /percent_complete/)

    // the read-only schedule register resolves package/deliverable refs and keeps file order
    const reg = await admin.get(`${P(env)}/schedule`)
    assert.equal(reg.status, 200)
    const rows = reg.body as any[]
    assert.equal(rows.length, 3)
    assert.equal(rows[0].activityId, 'SCH-1')
    assert.equal(rows[0].rowType, 'summary')
    assert.equal(rows[0].outlineLevel, 0)
    const task = rows.find((x) => x.activityId === 'SCH-2')
    assert.equal(task.parentActivityId, 'SCH-1')
    assert.equal(task.percentComplete, 50)
    assert.equal(task.package, 'PKG-A')
    assert.equal(task.deliverableRef, 'TST-PR-001')
    assert.equal(task.baselineFinish, '2026-02-18')

    // a narrower re-import (no optional headers) refreshes dates but retains WBS columns (§16)
    const again = await admin.postCsv(`${P(env)}/import/schedule`,
      'activity_id,description,start,finish\r\nSCH-2,Issue PFD (rev),2026-02-02,2026-02-25')
    assert.equal(again.body.updated, 1)
    const reg2 = await admin.get(`${P(env)}/schedule`)
    const task2 = (reg2.body as any[]).find((x) => x.activityId === 'SCH-2')
    assert.equal(task2.finishDate, '2026-02-25')
    assert.equal(task2.rowType, 'task', 'absent optional headers must not wipe WBS columns')
    assert.equal(task2.percentComplete, 50)

    // export mirrors the widened contract and re-imports cleanly (§16 round-trip)
    const exp = await admin.get(`${P(env)}/export/schedule.csv`)
    const header = String(exp.body).split('\r\n')[0]!
    for (const h of ['row_type', 'outline_level', 'parent_activity_id', 'percent_complete',
      'duration_days', 'baseline_start', 'baseline_finish']) {
      assert.ok(header.split(',').includes(h), `schedule export header missing ${h}`)
    }
    const rt = await admin.postCsv(`${P(env)}/import/schedule`, exp.body as string)
    assert.equal(rt.body.rejected.length, 0, JSON.stringify(rt.body.rejected))
    assert.equal(rt.body.updated, 3)
  } finally {
    await env.close()
  }
})
