/**
 * Coverage: Sponsor brief render (PEC-OV-006).
 * GET /api/projects/:pid/reports/sponsor-brief returns print-friendly HTML derived
 * from projectStatus() (health, KPIs, package rollup, holds/risks/decisions, signals).
 * Source: server/src/reports/sponsor-brief.ts, route in server/src/api.ts.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'

const brief = (pid: number) => `/api/projects/${pid}/reports/sponsor-brief`

test('sponsor brief: 200 text/html with project identity and static section scaffold', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const res = await pm.get(brief(env.projectId))

    assert.equal(res.status, 200)
    // body stays text (harness only JSON-parses parseable responses); html is a string
    assert.equal(typeof res.body, 'string')
    const html = res.body as string

    // Non-trivial HTML document
    assert.match(html, /^<!doctype html>/i)
    assert.ok(html.length > 500, `expected non-trivial html, got ${html.length} chars`)

    // Project identity: name in <title>, code in <h1>
    assert.match(html, /<title>Sponsor brief — Test FEED<\/title>/)
    assert.match(html, /TST — Sponsor Brief/)

    // Every derived section the function emits (stable literal headers)
    assert.match(html, /Project health:/)
    assert.match(html, /deliverables on plan/)
    assert.match(html, /active holds/)
    assert.match(html, /open decisions/)
    assert.match(html, /approvals in flight/)
    assert.match(html, /worst forecast slip/)
    assert.match(html, /<h2>Package rollup<\/h2>/)
    assert.match(html, /<h2>Waiting on decisions \/ approvals<\/h2>/)
    assert.match(html, /<h2>Top holds<\/h2>/)
    assert.match(html, /<h2>Top risks<\/h2>/)
    assert.match(html, /<h2>Governance signals<\/h2>/)
    assert.match(html, /Derived per PRD §8/)
  } finally {
    await env.close()
  }
})

test('sponsor brief: content-type header is text/html; charset=utf-8', async () => {
  const env = await createTestEnv()
  try {
    // Use raw fetch to inspect the response header the route sets explicitly.
    const login = await fetch(`${env.base}/api/auth/login`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ email: 'pm@t.co', password: 'pilot' }),
    })
    assert.equal(login.status, 200)
    const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0]!
    const res = await fetch(`${env.base}${brief(env.projectId)}`, { headers: { cookie } })

    assert.equal(res.status, 200)
    assert.equal(res.headers.get('content-type'), 'text/html; charset=utf-8')
  } finally {
    await env.close()
  }
})

test('sponsor brief: empty governance signals render placeholder rows, not crash', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const html = (await pm.get(brief(env.projectId))).body as string

    // Fresh project: no holds/risks/waiting -> "none" placeholder rows are emitted.
    assert.match(html, /class="muted">none<\/td>/)
    // The active-holds KPI shows 0 before any hold is raised.
    assert.match(html, /<b>0<\/b>active holds/)
  } finally {
    await env.close()
  }
})

test('sponsor brief: reflects non-empty governance signals after a hold and decision', async () => {
  const env = await createTestEnv()
  try {
    const pm = await env.as('pm@t.co')
    const P = `/api/projects/${env.projectId}`

    // Raise a hold blocking the seeded deliverable (typed cause + owner + need-by are required).
    const holdRes = await pm.post(`${P}/holds`, {
      title: 'Await client datasheet',
      cause: 'client_input',
      ownerId: env.people['eor@t.co'],
      needBy: '2026-08-31',
      targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
    })
    assert.equal(holdRes.status, 200, JSON.stringify(holdRes.body))
    const holdRef: string = holdRes.body.ref
    assert.ok(holdRef, 'hold should have a ref')

    // Create a standalone decision so open-decisions KPI is non-zero.
    const decRes = await pm.post(`${P}/decisions`, {
      title: 'Select pump vendor',
      statement: 'Vendor A vs Vendor B for the main feed pumps.',
      authorityId: env.people['lead@t.co'],
    })
    assert.equal(decRes.status, 200, JSON.stringify(decRes.body))

    // Brief still renders (no throw), 200, and now reflects the new governance signals.
    const res = await pm.get(brief(env.projectId))
    assert.equal(res.status, 200)
    const html = res.body as string

    // Active-holds KPI incremented to 1 and the hold appears in the Top holds table.
    assert.match(html, /<b>1<\/b>active holds/)
    assert.ok(html.includes(holdRef), `expected hold ref ${holdRef} in brief`)
    assert.match(html, /client_input/)

    // Open-decisions KPI incremented to 1.
    assert.match(html, /<b>1<\/b>open decisions/)

    // Governance signals section is still present and the document is well-formed.
    assert.match(html, /<h2>Governance signals<\/h2>/)
    assert.match(html, /<\/body><\/html>$/)
  } finally {
    await env.close()
  }
})
