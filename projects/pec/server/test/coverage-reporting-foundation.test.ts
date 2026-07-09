/**
 * D-PEC-38 reporting-foundation fix-forward coverage.
 * Pins the server-truth projections and validation paths that the reporting UI renders.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'

const P = (env: { projectId: number }) => `/api/projects/${env.projectId}`

test('D-PEC-38: config validation rejects unknown, negative, and warn>escalate threshold overrides', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const cfg = await admin.get(`${P(env)}/config`)
    assert.equal(cfg.status, 200)
    const version = cfg.body.version

    const unknown = await admin.put(`${P(env)}/config`, { version, thresholds: { noSuchThreshold: 1 } })
    assert.equal(unknown.status, 400)
    assert.match(unknown.body.error.message, /noSuchThreshold/)

    const negative = await admin.put(`${P(env)}/config`, { version, thresholds: { holdAgeWarnWd: -1 } })
    assert.equal(negative.status, 400)
    assert.match(negative.body.error.message, /holdAgeWarnWd/)

    const inverted = await admin.put(`${P(env)}/config`, { version, thresholds: { holdAgeWarnWd: 99, holdAgeRedWd: 14 } })
    assert.equal(inverted.status, 400)
    assert.match(inverted.body.error.message, /holdAgeWarnWd.*holdAgeRedWd/)
  } finally {
    await env.close()
  }
})

test('D-PEC-38: can/:action rejects unknown actions by name', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const res = await admin.get(`${P(env)}/can/not.real`)
    assert.equal(res.status, 400)
    assert.match(res.body.error.message, /not\.real/)
  } finally {
    await env.close()
  }
})

test('D-PEC-38: logSummaryView carries Explain-shaped dashboard metrics and hold package attribution', async () => {
  const env = await createTestEnv()
  try {
    const lead = await env.as('lead@t.co')
    const hold = await lead.post(`${P(env)}/holds`, {
      title: 'Vendor data missing',
      cause: 'vendor_data',
      ownerId: env.people['lead@t.co'],
      needBy: '2026-01-05',
      log: 'package',
      targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
    })
    assert.equal(hold.status, 200, JSON.stringify(hold.body))

    const log = await lead.get(`${P(env)}/log?type=hold`)
    assert.equal(log.status, 200)
    const row = log.body.find((r: any) => r.id === hold.body.id)
    assert.ok(row, 'hold row appears in log')
    assert.equal(row.packageId, env.packageId, 'hold package derives from hold link target')

    const summary = await lead.get(`${P(env)}/log-summary`)
    assert.equal(summary.status, 200)
    for (const key of ['total', 'byType', 'overdue', 'agingBuckets', 'untriagedIntake', 'holdsByCause']) {
      assert.equal(typeof summary.body[key].ruleId, 'string', `${key} has ruleId`)
      assert.ok(Array.isArray(summary.body[key].contributing), `${key} has contributing refs`)
    }
    assert.equal(summary.body.holdsByCause.value.vendor_data, 1)
    assert.equal(typeof summary.body.untriagedIntake.value.count, 'number')
    assert.ok('oldestWd' in summary.body.untriagedIntake.value)
  } finally {
    await env.close()
  }
})

test('D-PEC-38: admin people/activity projections carry server-derived capability and evidence shapes', async () => {
  const env = await createTestEnv()
  try {
    const admin = await env.as('admin@t.co')
    const people = await admin.get(`${P(env)}/admin/people`)
    assert.equal(people.status, 200)
    assert.ok(Array.isArray(people.body.people))
    assert.ok(people.body.people.some((p: any) => p.email === 'admin@t.co' && p.roles.includes('admin')))
    const adminRole = people.body.roleCapabilities.find((r: any) => r.role === 'admin')
    const viewerRole = people.body.roleCapabilities.find((r: any) => r.role === 'viewer')
    assert.ok(adminRole.capabilities.some((c: any) => c.action === 'config.manage'))
    assert.ok(viewerRole.capabilities.some((c: any) => c.action === 'project.read'))
    assert.ok(!viewerRole.capabilities.some((c: any) => c.action === 'config.manage'))

    const activity = await admin.get(`${P(env)}/admin/activity`)
    assert.equal(activity.status, 200)
    assert.equal(activity.body.evidence.database, 'active PEC project database')
    assert.ok(Array.isArray(activity.body.events))
  } finally {
    await env.close()
  }
})
