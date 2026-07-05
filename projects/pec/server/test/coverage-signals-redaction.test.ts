/**
 * PEC-NFR-005 / SPEC §2.2 — Overview governance signals must redact contributing refs that
 * point at records outside the caller's visible logs, the same way KPI/health payloads do.
 * Regression guard for the leak where overviewView returned status.signals unredacted: a
 * restricted-log record's `why` statement reached callers who cannot see that log, while the
 * ref itself (type + ref) is correctly retained (SPEC §2.2 redacts to type+ref, not dropped).
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'

test('signals: S-DEC contributing why is redacted for a restricted-log decision, kept for full-visibility (PEC-NFR-005)', async () => {
  const env = await createTestEnv()
  try {
    const P = `/api/projects/${env.projectId}`
    const lead = await env.as('lead@t.co')

    // An internal-log decision already past need-by → fires S-DEC with a log-scoped contributing ref.
    const dec = await lead.post(`${P}/decisions`, {
      title: 'Confidential units basis', statement: 'Settle the confidential units basis',
      authorityId: env.people['pm@t.co'], needBy: '2020-01-01', packageId: env.packageId, log: 'internal',
    })
    assert.equal(dec.status, 200, JSON.stringify(dec.body))

    const sDec = (body: any) => body.signals.find((s: any) => s.id === 'S-DEC')

    // pm sees all three logs → the real "N d past need-by" statement.
    const pmOv = await (await env.as('pm@t.co')).get(`${P}/overview`)
    assert.equal(pmOv.status, 200)
    const pmRef = sDec(pmOv.body).contributing.find((c: any) => c.id === dec.body.id)
    assert.ok(pmRef, 'pm sees the decision in S-DEC contributing')
    assert.match(pmRef.why, /past need-by/, 'full-visibility caller gets the real statement')

    // viewer defaults to package+client logs → internal decision is restricted: ref kept, why omitted.
    const vOv = await (await env.as('viewer@t.co')).get(`${P}/overview`)
    assert.equal(vOv.status, 200)
    const vRef = sDec(vOv.body).contributing.find((c: any) => c.id === dec.body.id)
    assert.ok(vRef, 'the ref is retained for the restricted record (type + ref, not dropped)')
    assert.equal(vRef.recordType, 'decision')
    assert.equal(vRef.why, '[restricted log]', 'the statement is redacted for the restricted log')
  } finally {
    await env.close()
  }
})
