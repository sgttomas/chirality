/**
 * Package Tracker import contract (§16 sixth contract, D-PEC-13 as amended): the resolved
 * package is the idempotency key (owner amendment: "match the tracker entries with the
 * PKG-#### numbers ... Keep the CoA number but don't key on that"); tracking_no is plain,
 * non-unique, row-optional data. Covers v1 create + v2 always-refresh (import-owned),
 * within-file duplicate-package conflicts (first valid wins), closed stage vocabulary,
 * key-must-resolve with NO intake fallback, export round-trip, the proposal path behind
 * the extended CONTRACTS allowlist, and the old-shape → amended-shape table rebuild.
 * Synthetic fixtures only; tmpdir DBs only.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { randomBytes } from 'node:crypto'
import { DatabaseSync } from 'node:sqlite'
import { openDb, withTx } from '../src/db.ts'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'

let env: TestEnv
let P: string
const pkgIds: Record<string, number> = {}

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
  // the key must resolve to existing packages — seed a synthetic PKG-Tnn set
  withTx(env.db, () => {
    for (let i = 1; i <= 14; i++) {
      const code = `PKG-T${String(i).padStart(2, '0')}`
      pkgIds[code] = env.repo.insert('package', { projectId: env.projectId, code, name: code })
    }
  })
})
after(async () => { await env.close() })

/** The 25 contract columns, in contract order (import ≡ export ≡ template; order unchanged by the amendment). */
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

/** Just the header-required columns — the narrowest lawful tracker file (includes the key). */
const REQUIRED_HEADERS = HEADERS.filter((h) =>
  h === 'tracking_no' || h === 'package_name' || h === 'discipline' || h === 'area'
  || h === 'package' || h.startsWith('stage_'))

/** A fully populated synthetic row keyed on `pkg`; workbook-style (un-normalized) stage vocabulary. */
function row(pkg: string, over: TrackerRow = {}): TrackerRow {
  return {
    tracking_no: `CoA-${pkg}`, package_name: `Synthetic package ${pkg}`,
    discipline: 'Mechanical', area: '1-01 (North)',
    package_type_approved: 'No', package_type_proposed: 'PUMP',
    line_items: 'Pump; Motor', vendors_engaged: 'Vendor A; Vendor B',
    stage_budgetary_datasheet: 'Issued', stage_cost_estimate: 'Complete',
    stage_package_datasheet: 'Not Started', stage_package: 'Not Started',
    stage_rfq: 'Not Started', stage_review: 'Not Started', stage_vendor_bids: 'Not Started',
    stage_clarifications: 'Not Started', stage_evaluation: 'Not Started',
    stage_eng_req: 'Not Applicable', stage_po: 'Not Started', stage_databook: 'Not Started',
    package: pkg,
    ...over,
  }
}

const trackerCount = (): number => (env.db.prepare(
  'SELECT COUNT(*) AS n FROM package_tracker WHERE project_id = ?').get(env.projectId) as { n: number }).n
const intakeCount = (): number => (env.db.prepare(
  'SELECT COUNT(*) AS n FROM intake_item WHERE project_id = ?').get(env.projectId) as { n: number }).n
const dbRow = (pkg: string): Record<string, unknown> | undefined => env.db.prepare(
  'SELECT * FROM package_tracker WHERE project_id = ? AND package_id = ?')
  .get(env.projectId, pkgIds[pkg]!) as Record<string, unknown> | undefined

test('v1 import creates one row per package; stage vocabulary normalized; blank stage → null; NO intake', async () => {
  const admin = await env.as('admin@t.co')
  const intakeBefore = intakeCount()
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('PKG-T01'),
    row('PKG-T02', { stage_po: '', expected_delivery_date: '2026-11-30' }),
    row('PKG-T03', { stage_cost_estimate: ' in progress ' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 3)
  assert.equal(res.body.updated, 0)
  assert.equal(res.body.conflicts.length, 0)
  assert.equal(res.body.rejected.length, 0)
  assert.equal(res.body.intakeCreated, 0, 'no intake fallback by construction')
  assert.equal(trackerCount(), 3)
  assert.equal(intakeCount(), intakeBefore)

  const r1 = dbRow('PKG-T01')!
  assert.equal(r1.package_id, pkgIds['PKG-T01'], 'keyed on the resolved package')
  assert.equal(r1.tracking_no, 'CoA-PKG-T01', 'CoA number kept verbatim')
  assert.equal(r1.stage_budgetary_datasheet, 'issued')
  assert.equal(r1.stage_cost_estimate, 'complete')
  assert.equal(r1.stage_eng_req, 'not_applicable')
  assert.equal(r1.stage_databook, 'not_started')
  assert.equal(dbRow('PKG-T02')!.stage_po, null, 'blank stage stored null')
  assert.equal(dbRow('PKG-T02')!.expected_delivery_date, '2026-11-30')
  assert.equal(dbRow('PKG-T03')!.stage_cost_estimate, 'in_progress', 'case/spaces normalized')
})

test('v2 re-import matches on the package and refreshes in place — even a renumbered CoA is data, not the key', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('PKG-T01', { tracking_no: 'CoA-RENUMBERED', vendors_engaged: 'Vendor C', stage_rfq: 'In Progress' }),
    row('PKG-T02'),
    row('PKG-T03'),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 0)
  assert.equal(res.body.updated, 3)
  assert.equal(res.body.conflicts.length, 0)
  assert.equal(trackerCount(), 3, 're-import must not duplicate')
  const r1 = dbRow('PKG-T01')!
  assert.equal(r1.vendors_engaged, 'Vendor C', 'fields refreshed')
  assert.equal(r1.stage_rfq, 'in_progress')
  assert.equal(r1.tracking_no, 'CoA-RENUMBERED', 'CoA number refreshed like any field — never matched on')
})

test('within-file duplicate package: first occurrence wins; later occurrence is a conflict, never applied', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('PKG-T04', { package_name: 'First occurrence' }),
    row('PKG-T04', { package_name: 'Second occurrence', tracking_no: 'CoA-OTHER' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 1)
  assert.equal(res.body.conflicts.length, 1)
  assert.equal(res.body.conflicts[0].key, 'PKG-T04')
  assert.match(res.body.conflicts[0].reason, /duplicate package in file/)
  assert.equal(dbRow('PKG-T04')!.package_name, 'First occurrence', 'later occurrence never applied')
  const n = (env.db.prepare(
    'SELECT COUNT(*) AS n FROM package_tracker WHERE project_id = ? AND package_id = ?',
  ).get(env.projectId, pkgIds['PKG-T04']!) as { n: number }).n
  assert.equal(n, 1, 'exactly one row for the duplicated key')
})

test('unrecognized stage vocabulary and malformed dates reject the row — never coerced, never silent', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('PKG-T05', { stage_rfq: 'Waiting On Vendor' }),
    row('PKG-T06', { expected_delivery_date: '11/30/2026' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 0)
  assert.equal(res.body.rejected.length, 2)
  assert.match(res.body.rejected[0].errors.join('; '), /unrecognized stage_rfq "Waiting On Vendor"/)
  assert.match(res.body.rejected[1].errors.join('; '), /expected_delivery_date must be YYYY-MM-DD/)
  assert.equal(dbRow('PKG-T05'), undefined)
  assert.equal(dbRow('PKG-T06'), undefined)
})

test('the key must resolve: missing package and unresolvable package reject the row (no intake fallback)', async () => {
  const admin = await env.as('admin@t.co')
  const intakeBefore = intakeCount()
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('PKG-T07', { package: '' }),
    row('PKG-T07', { package: 'PKG-NOPE' }),
    row('PKG-T07'),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 1)
  assert.equal(res.body.rejected.length, 2)
  assert.match(res.body.rejected[0].errors.join('; '), /package is required/)
  assert.match(res.body.rejected[1].errors.join('; '), /package "PKG-NOPE" matches no package code/)
  assert.equal(res.body.intakeCreated, 0)
  assert.equal(intakeCount(), intakeBefore, 'rejected key gaps never land in intake')
  assert.equal(dbRow('PKG-T07')!.package_id, pkgIds['PKG-T07'], 'the valid row in the same file still lands')
})

test('missing required columns refuse the whole file (§16) — package is header-required', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, 'tracking_no,package_name\r\nCoA-1,No stages')
  assert.equal(res.status, 400)
  assert.match(res.body.error.message, /tracker import missing required columns/)
  assert.match(res.body.error.message, /stage_databook, package \(§16\)/)

  // tracking_no stays header-required even though it is no longer the key
  const noCoaHeader = await admin.postCsv(
    `${P}/import/tracker`,
    csvWith(
      REQUIRED_HEADERS.filter((h) => h !== 'tracking_no'),
      [{ package: 'PKG-T01', package_name: 'Synthetic package one' }],
    ),
  )
  assert.equal(noCoaHeader.status, 400)
  assert.match(noCoaHeader.body.error.message, /tracking_no/)
})

test('export mirrors the import columns exactly and round-trips (§16)', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.get(`${P}/export/tracker.csv`)
  assert.equal(res.status, 200)
  const csv = String(res.body)
  const lines = csv.trim().split('\r\n')
  assert.equal(lines[0], HEADERS.join(','), 'export header ≡ import contract columns (order unchanged)')
  assert.equal(lines.length - 1, trackerCount(), 'one line per tracker row')
  assert.equal(lines.some((l) => l.endsWith(',PKG-T01')), true, 'the key exports as the package code')

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
  const csv = trackerCsv([row('PKG-T08')])
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
  assert.equal(dbRow('PKG-T08'), undefined, 'dry-run rolled back — nothing landed')

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
  assert.equal(dbRow('PKG-T08')!.package_id, pkgIds['PKG-T08'])
})

test('tracker register view serves the imported rows read-only', async () => {
  const viewer = await env.as('viewer@t.co')
  const res = await viewer.get(`${P}/tracker`)
  assert.equal(res.status, 200)
  assert.equal(res.body.length, trackerCount())
  const r = res.body.find((t: { packageId: number }) => t.packageId === pkgIds['PKG-T01'])
  assert.equal(r.trackingNo, 'CoA-RENUMBERED')
  assert.equal(r.stageBudgetaryDatasheet, 'issued')
})

test('a narrower re-import whose header omits optional columns retains their values (§16: no silent wipe)', async () => {
  const admin = await env.as('admin@t.co')
  const v1 = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('PKG-T09', { vendors_engaged: 'Vendor Z', comments: 'keep me' }),
  ]))
  assert.equal(v1.status, 200, JSON.stringify(v1.body))
  assert.equal(v1.body.accepted, 1)
  const before = dbRow('PKG-T09')!
  assert.equal(before.vendors_engaged, 'Vendor Z')
  assert.equal(before.comments, 'keep me')

  // v2: header-required columns only (they include the key); a stage changes
  const v2 = await admin.postCsv(`${P}/import/tracker`, csvWith(REQUIRED_HEADERS, [
    row('PKG-T09', { stage_rfq: 'In Progress' }),
  ]))
  assert.equal(v2.status, 200, JSON.stringify(v2.body))
  assert.equal(v2.body.updated, 1)
  assert.equal(v2.body.rejected.length, 0)
  const after = dbRow('PKG-T09')!
  assert.equal(after.stage_rfq, 'in_progress', 'header-required column refreshed')
  assert.equal(after.vendors_engaged, 'Vendor Z', 'absent optional column retained, not wiped')
  assert.equal(after.comments, 'keep me', 'absent optional column retained, not wiped')
  assert.equal(Number(after.version), Number(before.version) + 1, 'refresh bumps the version')
})

test('blank package_name rejects; a blank tracking_no still lands — plain data, not the key (owner amendment)', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('PKG-T10', { package_name: '' }),
    row('PKG-T11', { tracking_no: '' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.rejected.length, 1)
  assert.match(res.body.rejected[0].errors.join('; '), /package_name is required/)
  assert.equal(res.body.accepted, 1)
  assert.equal(dbRow('PKG-T10'), undefined, 'rejected row never lands')
  assert.equal(dbRow('PKG-T11')!.tracking_no, null, 'CoA-less row lands with tracking_no null')
})

test('duplicate-vs-validation precedence: a rejected occurrence never claims the key; the first VALID one wins', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('PKG-T12', { stage_rfq: 'Bogus', package_name: 'First occurrence invalid' }),
    row('PKG-T12', { package_name: 'Second valid wins' }),
    row('PKG-T12', { package_name: 'Third occurrence' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.rejected.length, 1, 'invalid first occurrence is a reject, not a conflict')
  assert.match(res.body.rejected[0].errors.join('; '), /unrecognized stage_rfq/)
  assert.equal(res.body.accepted, 1)
  assert.equal(res.body.conflicts.length, 1)
  assert.equal(res.body.conflicts[0].key, 'PKG-T12')
  assert.match(res.body.conflicts[0].reason, /duplicate package in file/)
  assert.equal(dbRow('PKG-T12')!.package_name, 'Second valid wins', 'first valid occurrence claims the key')
  const n = (env.db.prepare(
    'SELECT COUNT(*) AS n FROM package_tracker WHERE project_id = ? AND package_id = ?',
  ).get(env.projectId, pkgIds['PKG-T12']!) as { n: number }).n
  assert.equal(n, 1)
})

test('duplicate tracking_no values on DIFFERENT packages both land — tracking_no is not the key (owner amendment)', async () => {
  const admin = await env.as('admin@t.co')
  const res = await admin.postCsv(`${P}/import/tracker`, trackerCsv([
    row('PKG-T13', { tracking_no: 'CoA-SHARED' }),
    row('PKG-T14', { tracking_no: 'CoA-SHARED' }),
  ]))
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 2)
  assert.equal(res.body.conflicts.length, 0, 'a repeated CoA number is never a conflict')
  assert.equal(res.body.rejected.length, 0)
  assert.equal(dbRow('PKG-T13')!.tracking_no, 'CoA-SHARED')
  assert.equal(dbRow('PKG-T14')!.tracking_no, 'CoA-SHARED')
})

test('openDb rebuilds an old-shape package_tracker (tracking_no-keyed) to the amended shape', () => {
  const path = join(tmpdir(), `pec-trk-mig-${randomBytes(6).toString('hex')}.db`)
  // pin the pre-amendment shape: nullable package_id, UNIQUE on tracking_no
  const old = new DatabaseSync(path)
  old.exec(`
CREATE TABLE package_tracker (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL,
  tracking_no TEXT NOT NULL,
  package_name TEXT NOT NULL,
  discipline TEXT, area TEXT, package_type_approved TEXT, package_type_proposed TEXT,
  line_items TEXT, vendors_engaged TEXT, vendor_awarded TEXT, expected_delivery_date TEXT,
  cost_estimate_cad TEXT, comments TEXT,
  stage_budgetary_datasheet TEXT, stage_cost_estimate TEXT, stage_package_datasheet TEXT,
  stage_package TEXT, stage_rfq TEXT, stage_review TEXT, stage_vendor_bids TEXT,
  stage_clarifications TEXT, stage_evaluation TEXT, stage_eng_req TEXT, stage_po TEXT,
  stage_databook TEXT,
  package_id INTEGER,
  version INTEGER NOT NULL DEFAULT 1,
  UNIQUE(project_id, tracking_no)
);
INSERT INTO package_tracker (project_id, tracking_no, package_name) VALUES (1, 'OLD-1', 'legacy row');`)
  old.close()

  const db = openDb(path)
  const col = (name: string) => (db.prepare('PRAGMA table_info(package_tracker)').all() as
    Array<{ name: string; notnull: number }>).find((c) => c.name === name)
  assert.equal(col('package_id')!.notnull, 1, 'package_id NOT NULL at the amended shape')
  assert.equal(col('tracking_no')!.notnull, 0, 'tracking_no nullable at the amended shape')
  const n = (db.prepare('SELECT COUNT(*) AS n FROM package_tracker').get() as { n: number }).n
  assert.equal(n, 0, 'old-shape rows dropped — import-owned and reproducible by re-import')
  // the unique key is (project_id, package_id)
  const uniq = (db.prepare('PRAGMA index_list(package_tracker)').all() as
    Array<{ name: string; unique: number }>).filter((i) => i.unique === 1)
  assert.equal(uniq.length, 1)
  const idxCols = db.prepare(`PRAGMA index_info(${uniq[0]!.name})`).all() as Array<{ name: string }>
  assert.deepEqual(idxCols.map((c) => c.name).sort(), ['package_id', 'project_id'])
  db.close()

  // idempotent: reopening at the amended shape is a no-op
  const again = openDb(path)
  const col2 = (again.prepare('PRAGMA table_info(package_tracker)').all() as
    Array<{ name: string; notnull: number }>).find((c) => c.name === 'package_id')
  assert.equal(col2!.notnull, 1)
  again.close()
})
