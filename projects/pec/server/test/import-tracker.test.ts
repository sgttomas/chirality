/**
 * Package Tracker import contract (§16 sixth contract, D-PEC-13): v1 create + v2
 * always-refresh (import-owned), within-file duplicate-key conflicts (first wins),
 * closed stage vocabulary (unrecognized rejects), stated-anchor-must-resolve with NO
 * intake fallback, export round-trip, and the proposal path behind the extended
 * CONTRACTS allowlist. Synthetic fixtures only.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'

let env: TestEnv
let P: string

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
})
after(async () => { await env.close() })

/** The 25 contract columns, in contract order (import ≡ export ≡ template). */
const HEADERS = [
  'tracking_no', 'package_name', 'discipline', 'area',
  'package_type_approved', 'package_type_proposed', 'line_items', 'vendors_engaged',
  'vendor_awarded', 'expected_delivery_date', 'cost_estimate_cad', 'comments',
  'stage_budgetary_datasheet', 'stage_cost_estimate', 'stage_package_datasheet', 'stage_package',
  'stage_rfq', 'stage_review', 'stage_vendor_bids', 'stage_clarifications', 'stage_evaluation',
  'stage_eng_req', 'stage_po', 'stage_databook', 'package',
] as const
type TrackerRow = Partial<Record<(typeof HEADERS)[number], string>>

function csvWith(headers: ReadonlyArray<(typeof HEADERS)[number]>, rows: TrackerRow[]): string {
  return [headers.join(','), ...rows.map((r) => headers.map((h) => r[h] ?? '').join(','))].join('\r\n')
}

function trackerCsv(rows: TrackerRow[]): string {
  return csvWith(HEADERS, rows)
}

/** Just the header-required columns — the narrowest lawful tracker file. */
const REQUIRED_HEADERS = HEADERS.filter((h) =>
  h === 'tracking_no' || h === 'package_name' || h === 'discipline' || h === 'area' || h.startsWith('stage_'))

/** A fully populated synthetic row; workbook-style (un-normalized) stage vocabulary. */
function row(trackingNo: string, over: TrackerRow = {}): TrackerRow {
  return {
    tracking_no: trackingNo, package_name: `Synthetic package ${trackingNo}`,
    discipline: 'Mechanical', area: '1-01 (North)',
    package_type_approved: 'No', package_type_proposed: 'PUMP',
    line_items: 'Pump; Motor', vendors_engaged: 'Vendor A; Vendor B',
    stage_budgetary_datasheet: 'Issued', stage_cost_estimate: 'Complete',
    stage_package_datasheet: 'Not Started', stage_package: 'Not Started',
    stage_rfq: 'Not Started', stage_review: 'Not Started', stage_vendor_bids: 'Not Started',
    stage_clarifications: 'Not Started', stage_evaluation: 'Not Started',
    stage_eng_req: 'Not Applicable', stage_po: 'Not Started', stage_databook: 'Not Started',
    ...over,
  }
}

const trackerCount = (): number => (env.db.prepare(
  'SELECT COUNT(*) AS n FROM package_tracker WHERE project_id = ?').get(env.projectId) as { n: number }).n
const intakeCount = (): number => (env.db.prepare(
  'SELECT COUNT(*) AS n FROM intake_item WHERE project_id = ?').get(env.projectId) as { n: number }).n
const dbRow = (trackingNo: string): Record<string, unknown> | undefined => env.db.prepare(
  'SELECT * FROM package_tracker WHERE project_id = ? AND tracking_no = ?')
  .get(env.projectId, trackingNo) as Record<string, unknown> | undefined

test('v1 import creates rows; stage vocabulary normalized; blank stage → null; blank anchor → null packageId, NO intake', async () => {
  const admin = await env.as('admin@t.co')
  const intakeBefore = intakeCount()
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('TRK-0001'),
    row('TRK-0002', { stage_po: '', expected_delivery_date: '2026-11-30' }),
    row('TRK-0003', { stage_cost_estimate: ' in progress ' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 3)
  assert.equal(res.body.updated, 0)
  assert.equal(res.body.conflicts.length, 0)
  assert.equal(res.body.rejected.length, 0)
  assert.equal(res.body.intakeCreated, 0, 'no intake fallback by construction')
  assert.equal(trackerCount(), 3)
  assert.equal(intakeCount(), intakeBefore, 'unanchored rows never land in intake')

  const r1 = dbRow('TRK-0001')!
  assert.equal(r1.package_id, null, 'blank anchor → register row with null packageId')
  assert.equal(r1.stage_budgetary_datasheet, 'issued')
  assert.equal(r1.stage_cost_estimate, 'complete')
  assert.equal(r1.stage_eng_req, 'not_applicable')
  assert.equal(r1.stage_databook, 'not_started')
  assert.equal(dbRow('TRK-0002')!.stage_po, null, 'blank stage stored null')
  assert.equal(dbRow('TRK-0002')!.expected_delivery_date, '2026-11-30')
  assert.equal(dbRow('TRK-0003')!.stage_cost_estimate, 'in_progress', 'case/spaces normalized')
})

test('v2 re-import always refreshes matched rows in place — import-owned, no duplication, no conflict guard', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('TRK-0001', { vendors_engaged: 'Vendor C', stage_rfq: 'In Progress' }),
    row('TRK-0002'),
    row('TRK-0003'),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 0)
  assert.equal(res.body.updated, 3)
  assert.equal(res.body.conflicts.length, 0)
  assert.equal(trackerCount(), 3, 're-import must not duplicate')
  const r1 = dbRow('TRK-0001')!
  assert.equal(r1.vendors_engaged, 'Vendor C', 'fields refreshed')
  assert.equal(r1.stage_rfq, 'in_progress')
})

test('within-file duplicate tracking_no: first occurrence wins; later occurrence is a conflict, never applied', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('TRK-0100', { package_name: 'First occurrence' }),
    row('TRK-0100', { package_name: 'Second occurrence' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 1)
  assert.equal(res.body.conflicts.length, 1)
  assert.equal(res.body.conflicts[0].key, 'TRK-0100')
  assert.match(res.body.conflicts[0].reason, /duplicate tracking_no in file/)
  assert.equal(dbRow('TRK-0100')!.package_name, 'First occurrence', 'later occurrence never applied')
  const n = (env.db.prepare(
    'SELECT COUNT(*) AS n FROM package_tracker WHERE project_id = ? AND tracking_no = ?',
  ).get(env.projectId, 'TRK-0100') as { n: number }).n
  assert.equal(n, 1, 'exactly one row for the duplicated key')
})

test('unrecognized stage vocabulary and malformed dates reject the row — never coerced, never silent', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('TRK-0200', { stage_rfq: 'Waiting On Vendor' }),
    row('TRK-0201', { expected_delivery_date: '11/30/2026' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 0)
  assert.equal(res.body.rejected.length, 2)
  assert.match(res.body.rejected[0].errors.join('; '), /unrecognized stage_rfq "Waiting On Vendor"/)
  assert.match(res.body.rejected[1].errors.join('; '), /expected_delivery_date must be YYYY-MM-DD/)
  assert.equal(dbRow('TRK-0200'), undefined)
  assert.equal(dbRow('TRK-0201'), undefined)
})

test('stated package anchor must resolve: match links, mismatch rejects (no intake fallback)', async () => {
  const admin = await env.as('admin@t.co')
  const intakeBefore = intakeCount()
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('TRK-0300', { package: 'PKG-A' }),
    row('TRK-0301', { package: 'PKG-NOPE' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 1)
  assert.equal(res.body.rejected.length, 1)
  assert.match(res.body.rejected[0].errors.join('; '), /package "PKG-NOPE" matches no package code/)
  assert.equal(res.body.intakeCreated, 0)
  assert.equal(intakeCount(), intakeBefore)
  assert.equal(dbRow('TRK-0300')!.package_id, env.packageId, 'resolved anchor sets the link')
  assert.equal(dbRow('TRK-0301'), undefined, 'unresolvable stated anchor never lands')
})

test('missing required columns refuse the whole file (§16)', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, 'tracking_no,package_name\r\nTRK-0900,No stages')
  assert.equal(res.status, 400)
  assert.match(res.body.error.message, /tracker import missing required columns/)
  assert.match(res.body.error.message, /stage_databook/)
})

test('export mirrors the import columns exactly and round-trips (§16)', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.get(`${P}/export/tracker.csv`)
  assert.equal(res.status, 200)
  const csv = String(res.body)
  const lines = csv.trim().split('\r\n')
  assert.equal(lines[0], HEADERS.join(','), 'export header ≡ import contract columns')
  assert.equal(lines.length - 1, trackerCount(), 'one line per tracker row')
  const anchored = lines.find((l) => l.startsWith('TRK-0300,'))!
  assert.equal(anchored.endsWith(',PKG-A'), true, 'anchor exports as the package code')

  // round-trip: re-importing the export refreshes every row and rejects nothing
  const before = trackerCount()
  const back = await admin.postCsv(`${P}/import/tracker`, csv)
  assert.equal(back.status, 200, JSON.stringify(back.body))
  assert.equal(back.body.updated, before)
  assert.equal(back.body.accepted, 0)
  assert.equal(back.body.rejected.length, 0)
  assert.equal(back.body.conflicts.length, 0)
  assert.equal(trackerCount(), before)
})

test('proposal path: contract=tracker passes the allowlist — propose → dry-run → accept → apply', async () => {
  const coord = await env.as('coord@t.co')
  const csv = trackerCsv([row('TRK-0400', { package: 'PKG-A' })])
  const created = await coord.postCsv(`${P}/import-proposals?contract=tracker&filename=tracker.csv`, csv)
  assert.equal(created.status, 200, JSON.stringify(created.body))
  assert.equal(created.body.contract, 'tracker')
  assert.equal(created.body.state, 'ready_for_review')
  assert.equal(created.body.ref.startsWith('IPR-'), true)
  // dry-run report shape: the live contract's own answer, rolled back
  assert.equal(created.body.dryRunReport.contract, 'tracker')
  assert.equal(created.body.dryRunReport.accepted, 1)
  assert.deepEqual(created.body.dryRunReport.conflicts, [])
  assert.deepEqual(created.body.dryRunReport.rejected, [])
  assert.equal(created.body.dryRunReport.intakeCreated, 0)
  assert.equal(dbRow('TRK-0400'), undefined, 'dry-run rolled back — nothing landed')

  const admin = await env.as('admin@t.co')
  const accepted = await admin.post(`${P}/import-proposals/${created.body.id}/accept`,
    { version: created.body.version, sha256: created.body.sourceSha256 })
  assert.equal(accepted.status, 200, JSON.stringify(accepted.body))
  assert.equal(accepted.body.state, 'accepted')

  const applied = await admin.post(`${P}/import-proposals/${created.body.id}/apply`,
    { version: accepted.body.version })
  assert.equal(applied.status, 200, JSON.stringify(applied.body))
  assert.equal(applied.body.state, 'applied')
  assert.equal(applied.body.applyReport.accepted, 1)
  assert.equal(dbRow('TRK-0400')!.package_id, env.packageId)
})

test('tracker register view serves the imported rows read-only', async () => {
  const viewer = await env.as('viewer@t.co')
  const res = await viewer.get(`${P}/tracker`)
  assert.equal(res.status, 200)
  assert.equal(res.body.length, trackerCount())
  const r = res.body.find((t: { trackingNo: string }) => t.trackingNo === 'TRK-0300')
  assert.equal(r.packageId, env.packageId)
  assert.equal(r.stageBudgetaryDatasheet, 'issued')
})

test('a narrower re-import whose header omits optional columns retains their values (§16: no silent wipe)', async () => {
  const admin = await env.as('admin@t.co')
  const v1 = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('TRK-0500', { vendors_engaged: 'Vendor Z', comments: 'keep me' }),
  ]))
  assert.equal(v1.status, 200, JSON.stringify(v1.body))
  assert.equal(v1.body.accepted, 1)
  const before = dbRow('TRK-0500')!
  assert.equal(before.vendors_engaged, 'Vendor Z')
  assert.equal(before.comments, 'keep me')

  // v2: header-required columns only; a stage changes, the optional columns are absent
  const v2 = await admin.postCsv(`${P}/import/tracker`, csvWith(REQUIRED_HEADERS, [
    row('TRK-0500', { stage_rfq: 'In Progress' }),
  ]))
  assert.equal(v2.status, 200, JSON.stringify(v2.body))
  assert.equal(v2.body.updated, 1)
  assert.equal(v2.body.rejected.length, 0)
  const after = dbRow('TRK-0500')!
  assert.equal(after.stage_rfq, 'in_progress', 'header-required column refreshed')
  assert.equal(after.vendors_engaged, 'Vendor Z', 'absent optional column retained, not wiped')
  assert.equal(after.comments, 'keep me', 'absent optional column retained, not wiped')
  assert.equal(Number(after.version), Number(before.version) + 1, 'refresh bumps the version')
})

test('blank row-required fields reject the row; valid rows in the same file still apply', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('', { package_name: 'No key' }),
    row('TRK-0601', { package_name: '' }),
    row('TRK-0600'),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.rejected.length, 2)
  assert.match(res.body.rejected[0].errors.join('; '), /tracking_no is required/)
  assert.match(res.body.rejected[1].errors.join('; '), /package_name is required/)
  assert.equal(res.body.accepted, 1)
  assert.equal(dbRow('TRK-0601'), undefined, 'rejected row never lands')
  assert.equal(dbRow('TRK-0600')!.package_name, 'Synthetic package TRK-0600')
})

test('duplicate-vs-validation precedence: a rejected occurrence never claims the key; the first VALID one wins', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('TRK-0700', { stage_rfq: 'Bogus', package_name: 'First occurrence invalid' }),
    row('TRK-0700', { package_name: 'Second valid wins' }),
    row('TRK-0700', { package_name: 'Third occurrence' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.rejected.length, 1, 'invalid first occurrence is a reject, not a conflict')
  assert.match(res.body.rejected[0].errors.join('; '), /unrecognized stage_rfq/)
  assert.equal(res.body.accepted, 1)
  assert.equal(res.body.conflicts.length, 1)
  assert.equal(res.body.conflicts[0].key, 'TRK-0700')
  assert.match(res.body.conflicts[0].reason, /duplicate tracking_no in file/)
  assert.equal(dbRow('TRK-0700')!.package_name, 'Second valid wins', 'first valid occurrence claims the key')
  const n = (env.db.prepare(
    'SELECT COUNT(*) AS n FROM package_tracker WHERE project_id = ? AND tracking_no = ?',
  ).get(env.projectId, 'TRK-0700') as { n: number }).n
  assert.equal(n, 1)
})
