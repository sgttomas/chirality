/**
 * Coverage for the Risk + Interface registers (PEC-RISK-001/002, PEC-INT-001, PEC-PKG-007),
 * exercised end-to-end through the HTTP API:
 *   - createRisk: required title + package/deliverable link + probability/impact 1-5 stored,
 *     surfaces in GET /risks; version-checked updateRisk changes state (open -> mitigating);
 *   - a risk-treatment work item anchored to the risk (anchorType 'risk') projects into
 *     GET /log and GET /my-week (PEC-RISK-002);
 *   - createInterface: giving/receiving party required (PEC-PKG-007) — missing party rejected;
 *     surfaces in GET /interfaces, GET /log, and the package cockpit GET /packages/{id};
 *   - a stale updateInterface is rejected with 409 VERSION_CONFLICT (PEC-NFR-004).
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { isoWeekOf } from '@pec/core'
import { createTestEnv } from './harness.ts'

test('createRisk: fields + package/deliverable link stored, surfaces in GET /risks; version-checked state change', async () => {
  const env = await createTestEnv()
  const P = `/api/projects/${env.projectId}`
  try {
    const pm = await env.as('pm@t.co')

    // required title is enforced (PEC-RISK-001)
    const bad = await pm.post(`${P}/risks`, { probability: 3, impact: 3 })
    assert.equal(bad.status, 400, 'missing title rejected')

    // probability/impact must be on the 1-5 scale (PEC-RISK-001) — as the CSV importer enforces
    const badScore = await pm.post(`${P}/risks`, { title: 'out of range', probability: 9, impact: 0 })
    assert.equal(badScore.status, 400, 'out-of-range probability/impact rejected')

    // create with package + deliverable link and probability/impact in 1-5
    const created = await pm.post(`${P}/risks`, {
      title: 'Long-lead compressor', cause: 'Vendor slot', consequence: 'Schedule slip',
      packageId: env.packageId, deliverableId: env.deliverableId,
      ownerId: env.people['lead@t.co'], probability: 4, impact: 5,
      mitigation: 'Expedite PO', needBy: '2027-03-01',
    })
    assert.equal(created.status, 200)
    assert.equal(created.body.state, 'open', 'new risks start open')
    assert.equal(created.body.probability, 4)
    assert.equal(created.body.impact, 5)
    assert.equal(created.body.packageId, env.packageId)
    assert.equal(created.body.deliverableId, env.deliverableId)
    assert.ok(created.body.ref, 'risk gets a ref')

    // appears in the risk register
    const list = await pm.get(`${P}/risks`)
    assert.equal(list.status, 200)
    const row = (list.body as any[]).find((r) => r.id === created.body.id)
    assert.ok(row, 'created risk appears in GET /risks')
    assert.equal(row.title, 'Long-lead compressor')

    // version-checked update: open -> mitigating
    const updated = await pm.put(`${P}/risks/${created.body.id}`, {
      version: created.body.version, state: 'mitigating',
    })
    assert.equal(updated.status, 200)
    assert.equal(updated.body.state, 'mitigating', 'state advanced')
    assert.equal(updated.body.version, created.body.version + 1, 'version bumped')

    // an invalid state is rejected
    const badState = await pm.put(`${P}/risks/${created.body.id}`, {
      version: updated.body.version, state: 'not_a_state',
    })
    assert.equal(badState.status, 400, 'invalid risk state rejected')
  } finally {
    await env.close()
  }
})

test('PEC-RISK-002: a risk-treatment work item anchored to the risk projects into GET /log and GET /my-week', async () => {
  const env = await createTestEnv()
  const P = `/api/projects/${env.projectId}`
  try {
    const pm = await env.as('pm@t.co')

    const risk = await pm.post(`${P}/risks`, {
      title: 'Corrosion under insulation', packageId: env.packageId,
      ownerId: env.people['lead@t.co'], probability: 3, impact: 4,
    })
    assert.equal(risk.status, 200)

    // work item anchored to the risk; committed to the current week so it lands in my-week
    const thisWeek = isoWeekOf(new Date().toISOString().slice(0, 10))
    const wi = await pm.post(`${P}/work-items`, {
      title: 'Add CUI inspection to scope', kind: 'risk_treatment',
      anchorType: 'risk', anchorId: risk.body.id,
      ownerId: env.people['lead@t.co'], needBy: null, committedWeek: thisWeek,
    })
    assert.equal(wi.status, 200)
    assert.equal(wi.body.anchorType, 'risk')
    assert.equal(wi.body.anchorId, risk.body.id)
    assert.equal(wi.body.kind, 'risk_treatment')
    // package is derived from the risk's package link (derivePackageId, risk branch)
    assert.equal(wi.body.packageId, env.packageId, 'work item inherits the risk package')

    // projects into the action/hold log as a work_item row
    const log = await pm.get(`${P}/log`)
    assert.equal(log.status, 200)
    const logRow = (log.body as any[]).find((r) => r.recordType === 'work_item' && r.id === wi.body.id)
    assert.ok(logRow, 'risk-treatment work item appears in GET /log')

    // projects into the owner's my-week (committed to this week)
    const lead = await env.as('lead@t.co')
    const mw = await lead.get(`${P}/my-week`)
    assert.equal(mw.status, 200)
    const committed = mw.body.committed as any[]
    const mwRow = committed.find((c) => c.workItem.id === wi.body.id)
    assert.ok(mwRow, 'risk-treatment work item appears in the owner my-week')
    assert.match(mwRow.whyInWeek, /committed to this week/)
    assert.equal(mwRow.deliverable, null, 'a risk anchor has no deliverable in my-week')
  } finally {
    await env.close()
  }
})

test('createInterface (PEC-PKG-007): giving/receiving party required; surfaces in /interfaces, /log, and the package cockpit', async () => {
  const env = await createTestEnv()
  const P = `/api/projects/${env.projectId}`
  try {
    const pm = await env.as('pm@t.co')

    // missing receiving party is rejected (PEC-PKG-007)
    const missing = await pm.post(`${P}/interfaces`, {
      title: 'Line list handoff', givingParty: 'Process',
    })
    assert.equal(missing.status, 400, 'interface without a receiving party rejected')
    assert.match(missing.body.error.message, /giving party, receiving party/)

    // valid create, linked to the package on both sides so it lands in the cockpit
    const iface = await pm.post(`${P}/interfaces`, {
      title: 'Line list handoff', givingParty: 'Process', receivingParty: 'Piping',
      givingPackageId: env.packageId, receivingPackageId: env.packageId,
      requiredInfo: 'Tagged line list rev A', needBy: '2027-04-01',
    })
    assert.equal(iface.status, 200)
    assert.equal(iface.body.state, 'open', 'new interfaces start open')
    assert.equal(iface.body.log, 'internal', 'default log is internal')
    assert.ok(iface.body.ref)

    // appears in GET /interfaces
    const reg = await pm.get(`${P}/interfaces`)
    assert.equal(reg.status, 200)
    assert.ok((reg.body as any[]).some((i) => i.id === iface.body.id), 'appears in GET /interfaces')

    // appears in the unified action/hold log as an interface_item row
    const log = await pm.get(`${P}/log`)
    const logRow = (log.body as any[]).find((r) => r.recordType === 'interface_item' && r.id === iface.body.id)
    assert.ok(logRow, 'open interface appears in GET /log')
    assert.equal(logRow.packageId, env.packageId)

    // appears in the package cockpit: as an issue row and in the interfaces register block
    const pkg = await pm.get(`${P}/packages/${env.packageId}`)
    assert.equal(pkg.status, 200)
    const issue = (pkg.body.issues as any[]).find((x) => x.recordType === 'interface_item' && x.id === iface.body.id)
    assert.ok(issue, 'open interface surfaces as an issue in the cockpit')
    assert.equal(issue.type, 'interface')
    assert.equal(issue.detail, 'Process → Piping', 'detail names both parties')
    assert.ok((pkg.body.interfaces as any[]).some((i) => i.id === iface.body.id), 'interface in the register block')
    assert.equal(pkg.body.summary.openInterfaces, 1, 'cockpit counts the open interface')
  } finally {
    await env.close()
  }
})

test('updateInterface: version-checked state change; stale update rejected with 409', async () => {
  const env = await createTestEnv()
  const P = `/api/projects/${env.projectId}`
  try {
    const pm = await env.as('pm@t.co')

    const iface = await pm.post(`${P}/interfaces`, {
      title: 'Datasheet handoff', givingParty: 'Mechanical', receivingParty: 'Electrical',
      givingPackageId: env.packageId,
    })
    assert.equal(iface.status, 200)
    const v0 = iface.body.version

    // first update succeeds and bumps the version (open -> agreed)
    const first = await pm.put(`${P}/interfaces/${iface.body.id}`, { version: v0, state: 'agreed' })
    assert.equal(first.status, 200)
    assert.equal(first.body.state, 'agreed')
    assert.equal(first.body.version, v0 + 1)

    // a second update using the now-stale version is a version conflict (PEC-NFR-004)
    const stale = await pm.put(`${P}/interfaces/${iface.body.id}`, { version: v0, state: 'delivered' })
    assert.equal(stale.status, 409, 'stale interface update rejected')
    assert.equal(stale.body.error.code, 'VERSION_CONFLICT')

    // an invalid interface state is rejected up front
    const badState = await pm.put(`${P}/interfaces/${iface.body.id}`, { version: first.body.version, state: 'nope' })
    assert.equal(badState.status, 400, 'invalid interface state rejected')
  } finally {
    await env.close()
  }
})
