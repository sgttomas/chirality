/**
 * Import proposals (D-PEC-08): propose → dry-run → human accept (hash+version bound)
 * → apply, per the profile operation_proposal_contract lifecycle. Pins RV-13 binding
 * and staleness, RV-16 RBAC, RV-17 apply atomicity, RV-21 same-origin, and the RAIL
 * unanchored-intake idempotency repair (evidence-03 seam finding).
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createHash } from 'node:crypto'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'

let env: TestEnv
let P: string

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
})
after(async () => { await env.close() })

const sha = (s: string): string => createHash('sha256').update(s, 'utf8').digest('hex')

const MDL_CSV = [
  'doc_no,title,package,discipline,owner,current_rev,state,due_date',
  'TST-PR-101,P&ID Sheet 1,PKG-A,Process,eor@t.co,A,in_work,2027-01-31',
  'TST-PR-102,P&ID Sheet 2,PKG-A,Process,eor@t.co,A,in_work,2027-02-28',
].join('\r\n')

test('propose runs the dry-run, reports, and leaves the registers untouched', async () => {
  const dc = await env.as('dc@t.co')
  const res = await dc.postCsv(`${P}/import-proposals?contract=mdl&filename=mdl.csv`, MDL_CSV)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.state, 'ready_for_review')
  assert.equal(res.body.ref.startsWith('IPR-'), true)
  assert.equal(res.body.sourceSha256, sha(MDL_CSV))
  assert.equal(res.body.dryRunReport.accepted, 2)
  assert.equal(res.body.dryRunReport.rejected.length, 0)
  // the dry-run rolled back: nothing imported yet
  const count = env.db.prepare("SELECT COUNT(*) AS n FROM deliverable WHERE doc_no LIKE 'TST-PR-1%'").get() as { n: number }
  assert.equal(count.n, 0)
})

test('a non-contract-shaped CSV stays draft with the error recorded, never silently dropped', async () => {
  const dc = await env.as('dc@t.co')
  const res = await dc.postCsv(`${P}/import-proposals?contract=mdl`, 'wrong,headers\r\n1,2')
  assert.equal(res.status, 200)
  assert.equal(res.body.state, 'draft')
  assert.match(res.body.dryRunReport.error, /missing required columns/)
})

test('RBAC (RV-16): contributors and viewers cannot propose; proposers cannot accept', async () => {
  const ic = await env.as('ic@t.co')
  const viewer = await env.as('viewer@t.co')
  assert.equal((await ic.postCsv(`${P}/import-proposals?contract=mdl`, MDL_CSV)).status, 403)
  assert.equal((await viewer.get(`${P}/import-proposals`)).status, 403)

  const coord = await env.as('coord@t.co')
  const created = await coord.postCsv(`${P}/import-proposals?contract=mdl`, MDL_CSV)
  assert.equal(created.status, 200, 'coordinator proposes')
  const accept = await coord.post(`${P}/import-proposals/${created.body.id}/accept`,
    { version: created.body.version, sha256: created.body.sourceSha256 })
  assert.equal(accept.status, 403, 'coordinator does not accept')
  // withdraw own proposal to keep later watermarks clean
  const rej = await coord.post(`${P}/import-proposals/${created.body.id}/reject`,
    { version: created.body.version, reason: 'withdrawn by proposer (test)' })
  assert.equal(rej.status, 200)
  assert.equal(rej.body.state, 'rejected')
})

test('accept is hash- and version-bound (RV-13); stale proposals refuse; refresh re-arms', async () => {
  const admin = await env.as('admin@t.co')
  const created = await admin.postCsv(`${P}/import-proposals?contract=mdl`, MDL_CSV)
  assert.equal(created.status, 200)
  const id = created.body.id

  const wrongHash = await admin.post(`${P}/import-proposals/${id}/accept`,
    { version: created.body.version, sha256: 'deadbeef' })
  assert.equal(wrongHash.status, 400)
  assert.match(wrongHash.body.error.message, /sha256 mismatch/)

  const wrongVersion = await admin.post(`${P}/import-proposals/${id}/accept`,
    { version: 99, sha256: created.body.sourceSha256 })
  assert.equal(wrongVersion.status, 409)
  assert.equal(wrongVersion.body.error.code, 'VERSION_CONFLICT')

  // move the project: a direct in-app change advances the history watermark
  const lead = await env.as('lead@t.co')
  const wi = await lead.post(`${P}/work-items`, {
    title: 'watermark mover', kind: 'action', anchorType: 'deliverable', anchorId: env.deliverableId,
    ownerId: env.people['lead@t.co'], log: 'internal',
  })
  assert.equal(wi.status, 200, JSON.stringify(wi.body))

  const stale = await admin.post(`${P}/import-proposals/${id}/accept`,
    { version: created.body.version, sha256: created.body.sourceSha256 })
  assert.equal(stale.status, 409)
  assert.equal(stale.body.error.code, 'STALE_PROPOSAL')

  const refreshed = await admin.post(`${P}/import-proposals/${id}/refresh`, { version: created.body.version })
  assert.equal(refreshed.status, 200)
  assert.equal(refreshed.body.state, 'ready_for_review')

  const accepted = await admin.post(`${P}/import-proposals/${id}/accept`,
    { version: refreshed.body.version, sha256: refreshed.body.sourceSha256 })
  assert.equal(accepted.status, 200, JSON.stringify(accepted.body))
  assert.equal(accepted.body.state, 'accepted')
  assert.equal(accepted.body.acceptedSha256, sha(MDL_CSV))

  // RV-17 atomicity: a throw AFTER the real import (here: version conflict on the
  // lifecycle update) rolls the whole apply back — no half-applied registers.
  const badApply = await admin.post(`${P}/import-proposals/${id}/apply`, { version: 99 })
  assert.equal(badApply.status, 409)
  const mid = env.db.prepare("SELECT COUNT(*) AS n FROM deliverable WHERE doc_no LIKE 'TST-PR-1%'").get() as { n: number }
  assert.equal(mid.n, 0, 'failed apply left nothing behind')

  const applied = await admin.post(`${P}/import-proposals/${id}/apply`, { version: accepted.body.version })
  assert.equal(applied.status, 200, JSON.stringify(applied.body))
  assert.equal(applied.body.state, 'applied')
  assert.equal(applied.body.applyReport.accepted, 2)
  const done = env.db.prepare("SELECT COUNT(*) AS n FROM deliverable WHERE doc_no LIKE 'TST-PR-1%'").get() as { n: number }
  assert.equal(done.n, 2)

  // lifecycle trail: history kinds + audit events (RV-15)
  const hist = await admin.get(`${P}/history/import_proposal/${id}`)
  const kinds = (hist.body as Array<{ kind: string }>).map((h) => h.kind)
  for (const k of ['created', 'proposal_dry_run', 'proposal_accepted', 'proposal_applied']) {
    assert.equal(kinds.includes(k), true, `history has ${k}`)
  }
  const audits = env.db.prepare(
    'SELECT action FROM audit_event WHERE record_type = ? AND record_id = ? ORDER BY id',
  ).all('import_proposal', id) as Array<{ action: string }>
  assert.deepEqual(audits.map((a) => a.action), ['import_proposal_accept', 'import_proposal_apply'])

  // applying twice is refused
  const again = await admin.post(`${P}/import-proposals/${id}/apply`, { version: applied.body.version })
  assert.equal(again.status, 400)
})

test('list omits the raw CSV body; detail includes it (RV-19 read scope)', async () => {
  const admin = await env.as('admin@t.co')
  const list = await admin.get(`${P}/import-proposals`)
  assert.equal(list.status, 200)
  assert.equal(list.body.length > 0, true)
  assert.equal('sourceCsv' in list.body[0], false)
  const detail = await admin.get(`${P}/import-proposals/${list.body[0].id}`)
  assert.equal(typeof detail.body.sourceCsv, 'string')
})

test('cross-origin proposal mutations are refused (RV-21)', async () => {
  // authenticated session but a foreign Origin header
  const login = await fetch(`${env.base}/api/auth/login`, {
    method: 'POST', headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ email: 'admin@t.co', password: 'pilot' }),
  })
  const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0]!
  const res = await fetch(`${env.base}${P}/import-proposals?contract=mdl`, {
    method: 'POST',
    headers: { cookie, 'content-type': 'text/csv', origin: 'http://evil.example' },
    body: MDL_CSV,
  })
  assert.equal(res.status, 403)
  const body = await res.json() as { error: { code: string } }
  assert.equal(body.error.code, 'CROSS_ORIGIN')
  // same-origin passes
  const host = new URL(env.base).host
  const ok = await fetch(`${env.base}${P}/import-proposals?contract=mdl`, {
    method: 'POST',
    headers: { cookie, 'content-type': 'text/csv', origin: `http://${host}` },
    body: 'wrong,headers\r\n1,2',
  })
  assert.equal(ok.status, 200)
})

test('RAIL re-import updates the unanchored intake row instead of duplicating it (evidence-03 repair)', async () => {
  const admin = await env.as('admin@t.co')
  const railCsv = (needBy: string, statement = 'Chase vendor data') => [
    'item_id,statement,type,log,owner,need_by,status,raised_by,raised_date,deliverable_ref',
    `R-77,${statement},action,internal,eor@t.co,${needBy},open,pm@t.co,2026-07-01,NOPE-999`,
  ].join('\r\n')

  const first = await admin.postCsv(`${P}/import/rail`, railCsv('2026-08-01'))
  assert.equal(first.status, 200, JSON.stringify(first.body))
  assert.equal(first.body.intakeCreated, 1)

  const second = await admin.postCsv(`${P}/import/rail`, railCsv('2026-09-15'))
  assert.equal(second.status, 200)
  assert.equal(second.body.intakeCreated, 0, 're-import must not duplicate')
  assert.equal(second.body.updated, 1)

  const rows = env.db.prepare(
    "SELECT need_by FROM intake_item WHERE project_id = ? AND statement_verbatim LIKE '[R-77]%'",
  ).all(env.projectId) as Array<{ need_by: string }>
  assert.equal(rows.length, 1, 'exactly one intake row for R-77')
  assert.equal(rows[0]!.need_by, '2026-09-15', 'mutable fields refreshed')

  // a changed statement is a conflict — the verbatim statement is frozen (OM-3)
  const changed = await admin.postCsv(`${P}/import/rail`, railCsv('2026-09-15', 'A different statement'))
  assert.equal(changed.status, 200)
  assert.equal(changed.body.conflicts.length, 1)
  assert.match(changed.body.conflicts[0].reason, /verbatim/)
  assert.equal(changed.body.intakeCreated, 0)
})
