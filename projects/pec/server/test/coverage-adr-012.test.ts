/**
 * ADR-012 — Overview adopts the client-facing issues framing without breaking PEC-NFR-005:
 * the package rollup's openIssues is the same log-scoped holds+risks+actions count the
 * Packages register shows, per caller. Also covers the explanation carry-through end to end:
 * a package-health drill-down reaches the underlying hold record, not just a deliverable label.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'

test('ADR-012: overview packageRollup.openIssues matches the packages register, per caller (PEC-NFR-005)', async () => {
  const env = await createTestEnv()
  try {
    const P = `/api/projects/${env.projectId}`
    const lead = await env.as('lead@t.co')

    // Three operational rows in three logs: an internal hold, an internal package decision,
    // and a client-log action item. Viewer sees package+client logs only.
    const hold = await lead.post(`${P}/holds`, {
      title: 'Vendor data outstanding', cause: 'vendor_data', ownerId: env.people['lead@t.co'],
      needBy: '2027-01-15', log: 'internal',
      targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
    })
    assert.equal(hold.status, 200, JSON.stringify(hold.body))
    const dec = await lead.post(`${P}/decisions`, {
      title: 'Units basis', statement: 'Confirm units basis', authorityId: env.people['pm@t.co'],
      needBy: '2027-01-15', packageId: env.packageId, log: 'internal',
    })
    assert.equal(dec.status, 200, JSON.stringify(dec.body))
    const wi = await lead.post(`${P}/work-items`, {
      title: 'Client comment consolidation', anchorType: 'deliverable', anchorId: env.deliverableId,
      ownerId: env.people['ic@t.co'], needBy: '2027-01-20', log: 'client', kind: 'action',
    })
    assert.equal(wi.status, 200, JSON.stringify(wi.body))

    for (const email of ['pm@t.co', 'viewer@t.co']) {
      const client = await env.as(email)
      const overview = await client.get(`${P}/overview`)
      assert.equal(overview.status, 200)
      const packages = await client.get(`${P}/packages`)
      assert.equal(packages.status, 200)
      const rollupRow = overview.body.packageRollup.find((r: any) => r.id === env.packageId)
      const registerRow = packages.body.find((r: any) => r.id === env.packageId)
      assert.equal(rollupRow.openIssues, registerRow.openIssues,
        `${email}: Overview and Packages must show the same openIssues count`)
    }

    // pm sees the internal hold + client action as issues; the decision is segregated.
    // viewer defaults to package+client → the internal hold drops out.
    const pmView = await (await env.as('pm@t.co')).get(`${P}/overview`)
    const viewerView = await (await env.as('viewer@t.co')).get(`${P}/overview`)
    const pmCount = pmView.body.packageRollup.find((r: any) => r.id === env.packageId).openIssues
    const viewerCount = viewerView.body.packageRollup.find((r: any) => r.id === env.packageId).openIssues
    assert.equal(pmCount, 2, 'pm issue count includes hold + client action item; decision is segregated')
    assert.equal(viewerCount, 1, 'viewer sees only the client-log action item')
  } finally {
    await env.close()
  }
})

test('ADR-012: package-health drill-down reaches the hold record itself through the API', async () => {
  const env = await createTestEnv()
  try {
    const P = `/api/projects/${env.projectId}`
    const lead = await env.as('lead@t.co')
    const hold = await lead.post(`${P}/holds`, {
      title: 'Missing survey data', cause: 'information', ownerId: env.people['lead@t.co'],
      needBy: '2027-01-15',
      targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
    })
    assert.equal(hold.status, 200, JSON.stringify(hold.body))

    const packages = await lead.get(`${P}/packages`)
    const row = packages.body.find((r: any) => r.id === env.packageId)
    assert.equal(row.health.ruleId, 'PH-A1', JSON.stringify(row.health))
    const holdRef = row.health.contributing.find((c: any) => c.recordType === 'hold')
    assert.ok(holdRef, 'contributing records include the hold (cockpit-visible), not only the deliverable')
    assert.match(holdRef.why, /TST-PR-001/, 'carried-through ref names the pressured deliverable')
    const delRef = row.health.contributing.find((c: any) => c.recordType === 'deliverable')
    assert.match(delRef.why, /active hold/, 'deliverable ref states the pressure in plain terms')
  } finally {
    await env.close()
  }
})
