/**
 * Regression tests for the 2026-07-04 issues reorientation:
 *   - a deliverable's summary status is workflow completeness (gates closed), not issue health;
 *   - the package detail is an operational cockpit: a unified, urgency-sorted list of holds,
 *     interfaces, decisions, risks, and rolled-up action items, plus a workflow deliverable rollup;
 *   - the package register's openIssues count is client-facing (holds, risks, actions) and log-scoped.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'
import { withTx } from '../src/db.ts'
import { nowIso } from '../src/repo.ts'

const PAST = '2020-01-01'   // always overdue
const FUTURE = '2030-12-31' // never overdue

test('deliverablesView: summary status is workflow completeness, not issue health', async () => {
  const env = await createTestEnv()
  const P = `/api/projects/${env.projectId}`
  try {
    const lead = await env.as('lead@t.co')
    const res = await lead.get(`${P}/deliverables?view=active`)
    const row = res.body.find((r: any) => r.id === env.deliverableId)
    assert.ok(row.workflow, 'row carries a workflow object')
    assert.equal('health' in row, false, 'no issue-driven health on the deliverable summary')
    assert.equal('holds' in row, false, 'no holds column on the summary')
    assert.equal(row.workflow.currentState, 'in_work', 'harness seeds a rev at in_work')
    assert.equal(row.workflow.gatesClosed, 0)
    assert.equal(row.workflow.stages.find((s: any) => s.state === 'current')?.key, 'checked')
  } finally { await env.close() }
})

test('deliverableDetailView carries workflow; deliverable detail still shows tied issues (drill-down)', async () => {
  const env = await createTestEnv()
  const P = `/api/projects/${env.projectId}`
  try {
    const lead = await env.as('lead@t.co')
    // a hold tied to the deliverable — visible on drill-down, not on the summary
    await lead.post(`${P}/holds`, {
      title: 'vendor data late', cause: 'vendor_data', ownerId: env.people['lead@t.co'], needBy: FUTURE,
      targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
    })
    const detail = await lead.get(`${P}/deliverables/${env.deliverableId}`)
    assert.ok(detail.body.workflow, 'detail carries workflow status')
    assert.ok(detail.body.openItems.holds.some((h: any) => h.title === 'vendor data late'),
      'the tied hold is available on drill-down')
  } finally { await env.close() }
})

test('packageDetailView: the operational cockpit unifies record types, urgency-first, with a workflow deliverable rollup', async () => {
  const env = await createTestEnv()
  const P = `/api/projects/${env.projectId}`
  try {
    // seed one of each issue type in the package, directly (bypassing per-type create flows)
    withTx(env.db, () => {
      const holdId = env.repo.insert('hold', {
        projectId: env.projectId, ref: 'HLD-1', title: 'blocking hold', cause: 'vendor_data',
        ownerId: env.people['lead@t.co'], needBy: FUTURE, raisedBy: env.people['lead@t.co'],
        raisedAt: nowIso(), state: 'active', log: 'package',
      })
      env.repo.insert('hold_link', { holdId, targetType: 'deliverable', targetId: env.deliverableId })
      env.repo.insert('decision', {
        projectId: env.projectId, ref: 'DEC-1', title: 'units basis', statement: 'metric or imperial?',
        authorityId: env.people['pm@t.co'], needBy: PAST, state: 'pending', packageId: env.packageId,
        log: 'package', createdAt: nowIso(), kind: 'standalone',
      })
      env.repo.insert('interface_item', {
        projectId: env.projectId, ref: 'INT-1', title: 'process → mech data', givingParty: 'Process',
        receivingParty: 'Mechanical', givingPackageId: env.packageId, needBy: PAST, state: 'open', log: 'package',
      })
      env.repo.insert('risk', {
        projectId: env.projectId, ref: 'RSK-1', title: 'schedule slip risk', cause: 'late data',
        consequence: 'delay', packageId: env.packageId, ownerId: env.people['lead@t.co'],
        probability: 4, impact: 5, needBy: FUTURE, state: 'mitigating',
      })
      env.repo.insert('work_item', {
        projectId: env.projectId, ref: 'WI-1', title: 'chase vendor', statement: null, kind: 'action',
        log: 'package', anchorType: 'deliverable', anchorId: env.deliverableId, packageId: env.packageId,
        ownerId: env.people['eor@t.co'], needBy: FUTURE, state: 'open',
        createdBy: env.people['lead@t.co'], createdAt: nowIso(),
      })
    })

    const lead = await env.as('lead@t.co')
    const detail = await lead.get(`${P}/packages/${env.packageId}`)
    const issues = detail.body.issues as any[]
    const types = new Set(issues.map((i) => i.type))
    for (const t of ['hold', 'interface', 'decision', 'risk', 'action']) {
      assert.ok(types.has(t), `cockpit includes a ${t} issue`)
    }
    assert.equal(detail.body.summary.openIssues, 3, 'client-facing issues are holds, risks, and actions')
    assert.equal(detail.body.summary.openOperationalItems, issues.length)
    assert.equal(detail.body.summary.overdueIssues, 0, 'the past-dated decision and interface are segregated, not client-facing issues')
    // urgency-first: overdue operational records sort ahead of non-overdue
    const firstNonOverdue = issues.findIndex((i) => !i.overdue)
    const lastOverdue = issues.map((i) => i.overdue).lastIndexOf(true)
    assert.ok(firstNonOverdue === -1 || lastOverdue < firstNonOverdue, 'all overdue issues precede non-overdue')
    // deliverable rollup carries workflow status, not issue health
    assert.ok(detail.body.deliverables[0].workflow, 'deliverable rollup carries workflow')
    assert.equal('health' in detail.body.deliverables[0], false)
    assert.ok(Array.isArray(detail.body.risks) && detail.body.risks.length === 1)
  } finally { await env.close() }
})

test('PEC-NFR-005: the register openIssues count is log-scoped and matches the cockpit for that user', async () => {
  const env = await createTestEnv()
  const P = `/api/projects/${env.projectId}`
  try {
    withTx(env.db, () => {
      // one internal-log action (hidden from the viewer), one package-log action, and one
      // RAIL-v2-style package issue imported as kind='other' (visible to all).
      for (const [ref, log] of [['WI-INT', 'internal'], ['WI-PKG', 'package']] as const) {
        env.repo.insert('work_item', {
          projectId: env.projectId, ref, title: `${log} action`, statement: null, kind: 'action', log,
          anchorType: 'deliverable', anchorId: env.deliverableId, packageId: env.packageId,
          ownerId: env.people['eor@t.co'], needBy: FUTURE, state: 'open',
          createdBy: env.people['lead@t.co'], createdAt: nowIso(),
        })
      }
      env.repo.insert('work_item', {
        projectId: env.projectId, ref: 'WI-OTH', title: 'source clarification needed', statement: null,
        kind: 'other', log: 'package', anchorType: 'package', anchorId: env.packageId, packageId: env.packageId,
        ownerId: env.people['eor@t.co'], needBy: FUTURE, state: 'open', sourceIssueType: 'Clarification',
        createdBy: env.people['lead@t.co'], createdAt: nowIso(),
      })
    })

    // lead sees all logs → both actions + the RAIL-v2 kind='other' row; register, detail,
    // and package-issue-summary counts stay identical.
    const lead = await env.as('lead@t.co')
    const leadReg = (await lead.get(`${P}/packages`)).body.find((p: any) => p.id === env.packageId)
    const leadDetail = await lead.get(`${P}/packages/${env.packageId}`)
    assert.equal(leadReg.openIssues, leadDetail.body.summary.openIssues, 'lead: register count == client-facing issue count')
    const leadReport = await lead.get(`${P}/reports/standard/package-issue-summary`)
    const leadReportRow = leadReport.body.sections.packages.find((p: any) => p.package.id === env.packageId)
    assert.equal(leadReportRow.clientIssues, leadReg.openIssues, 'lead: package-issue-summary count == register count')
    assert.equal(leadReg.openIssues, 3)
    const otherRow = leadDetail.body.issues.find((i: any) => i.ref === 'WI-OTH')
    assert.equal(otherRow?.detail, 'Clarification', 'cockpit row prefers the verbatim source issue type')

    // viewer does not see the internal log → only package-visible rows, and the count agrees
    const viewer = await env.as('viewer@t.co')
    const vReg = (await viewer.get(`${P}/packages`)).body.find((p: any) => p.id === env.packageId)
    const vDetail = await viewer.get(`${P}/packages/${env.packageId}`)
    assert.equal(vReg.openIssues, vDetail.body.summary.openIssues, 'viewer: register count == client-facing issue count')
    assert.equal(vReg.openIssues, 2, 'viewer sees only package-log rows, not the internal one')
    assert.ok(!JSON.stringify(vDetail.body.issues).includes('internal action'), 'internal-log title not leaked to viewer')
  } finally { await env.close() }
})
