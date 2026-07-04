/**
 * PEC-CHK-004: check independence warning.
 * createCheck sets independence_warning=true iff the assigned checker is the
 * deliverable owner (server/src/services/checks.ts:35). It is a WARN only (P1):
 * the check is still created, never blocked. The flag surfaces on the returned
 * check, via GET /checks/{id} (check.independenceWarning), and on the deliverable
 * detail check rows (openItems.checks[].independenceWarning).
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'

// The seeded deliverable is owned by eor@t.co; lead@t.co has check.create.
test('checker == deliverable owner → independence_warning true, check still created', async () => {
  const env = await createTestEnv()
  try {
    const P = `/api/projects/${env.projectId}`
    const lead = await env.as('lead@t.co')

    const created = await lead.post(`${P}/checks`, {
      revisionId: env.revisionId,
      checkerId: env.people['eor@t.co'], // the deliverable owner
    })

    // WARN only: the check is created (200), not blocked.
    assert.equal(created.status, 200, JSON.stringify(created.body))
    assert.equal(created.body.independenceWarning, true)
    assert.equal(created.body.checkerId, env.people['eor@t.co'])
    assert.equal(created.body.state, 'open')
  } finally {
    await env.close()
  }
})

test('GET /checks/{id} surfaces independenceWarning true for owner-as-checker', async () => {
  const env = await createTestEnv()
  try {
    const P = `/api/projects/${env.projectId}`
    const lead = await env.as('lead@t.co')

    const created = await lead.post(`${P}/checks`, {
      revisionId: env.revisionId,
      checkerId: env.people['eor@t.co'],
    })
    assert.equal(created.status, 200, JSON.stringify(created.body))

    const detail = await lead.get(`${P}/checks/${created.body.id}`)
    assert.equal(detail.status, 200, JSON.stringify(detail.body))
    assert.equal(detail.body.check.independenceWarning, true)
  } finally {
    await env.close()
  }
})

test('checker != deliverable owner → independence_warning false', async () => {
  const env = await createTestEnv()
  try {
    const P = `/api/projects/${env.projectId}`
    const lead = await env.as('lead@t.co')

    const created = await lead.post(`${P}/checks`, {
      revisionId: env.revisionId,
      checkerId: env.people['checker@t.co'], // NOT the owner
    })
    assert.equal(created.status, 200, JSON.stringify(created.body))
    assert.equal(created.body.independenceWarning, false)

    const detail = await lead.get(`${P}/checks/${created.body.id}`)
    assert.equal(detail.status, 200, JSON.stringify(detail.body))
    assert.equal(detail.body.check.independenceWarning, false)
  } finally {
    await env.close()
  }
})

test('deliverable detail check rows carry independenceWarning per check', async () => {
  const env = await createTestEnv()
  try {
    const P = `/api/projects/${env.projectId}`
    const lead = await env.as('lead@t.co')

    // One warned check (owner as checker). Creating it moves the revision
    // in_work → in_check; both checks live on the same revision.
    const warned = await lead.post(`${P}/checks`, {
      revisionId: env.revisionId,
      checkerId: env.people['eor@t.co'],
    })
    assert.equal(warned.status, 200, JSON.stringify(warned.body))
    // One clean check (independent checker).
    const clean = await lead.post(`${P}/checks`, {
      revisionId: env.revisionId,
      checkerId: env.people['checker@t.co'],
    })
    assert.equal(clean.status, 200, JSON.stringify(clean.body))

    const detail = await lead.get(`${P}/deliverables/${env.deliverableId}`)
    assert.equal(detail.status, 200, JSON.stringify(detail.body))

    const rows: Array<{ id: number; independenceWarning: boolean }> = detail.body.openItems.checks
    const warnedRow = rows.find((r) => r.id === warned.body.id)
    const cleanRow = rows.find((r) => r.id === clean.body.id)

    assert.ok(warnedRow, 'warned check row present on deliverable detail')
    assert.ok(cleanRow, 'clean check row present on deliverable detail')
    assert.equal(warnedRow!.independenceWarning, true)
    assert.equal(cleanRow!.independenceWarning, false)
  } finally {
    await env.close()
  }
})
