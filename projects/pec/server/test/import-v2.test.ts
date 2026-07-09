/**
 * MDL/RAIL import contract v2 (D-PEC-41 O-A). Pins:
 * - additive schema migration (v2 columns appear on pre-D-PEC-41 DBs);
 * - v2 shape detection rides the same contract ids; v1 files keep working;
 * - MDL identity: deliverable_id wins, else deterministic derivation with
 *   collision-group qualification; residual duplicates are conflicts;
 * - attested fields are captured (incl. verbatim percent markers), never
 *   in-app editable, and create NO revision records (factual-or-absent);
 * - unmapped columns are captured verbatim (owner fidelity direction,
 *   Receipt 75); non-tabular content rides proposal source_extras;
 * - RAIL v2: package placeholder rows create no issue records; issue rows
 *   are package-anchored work items with verbatim attested type/party;
 *   On Hold / phase-cancelled land as caught signals, never coerced;
 * - discipline view % complete (DISC-PCT) is attested-only, equal-weight by
 *   deliverable type, names its coverage, and is absent when unattested;
 * - round-trip exports mdl-v2 / rail-v2 reproduce provided columns.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { randomBytes } from 'node:crypto'
import { DatabaseSync } from 'node:sqlite'
import { openDb } from '../src/db.ts'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'

let env: TestEnv
let P: string

before(async () => {
  env = await createTestEnv()
  P = `/api/projects/${env.projectId}`
})
after(async () => { await env.close() })

const MDL_V2_HDR = 'package,deliverable_type,area,project_phase,discipline,package_type,package_name,deliverable_id,target_completeness,working_status,percent_complete,custom_note'
const RAIL_V2_HDR = 'package,issue_no,discipline,area,phase,coa_tracking_number,package_type,package_name,issue_type,statement,updates,responsible_party,status,priority,assigned_date,original_target_date,current_target_date,actual_completion_date'

test('migration: a pre-D-PEC-41 database gains the v2 columns additively', () => {
  const path = join(tmpdir(), `pec-mig41-${randomBytes(6).toString('hex')}.db`)
  const old = new DatabaseSync(path)
  old.exec(`CREATE TABLE deliverable (
    id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL, package_id INTEGER NOT NULL,
    doc_no TEXT NOT NULL, title TEXT NOT NULL, version INTEGER NOT NULL DEFAULT 1)`)
  old.close()
  const db = openDb(path)
  const cols = (db.prepare('PRAGMA table_info(deliverable)').all() as Array<{ name: string }>).map((c) => c.name)
  for (const c of ['project_phase', 'target_completeness', 'working_status', 'percent_complete', 'percent_complete_verbatim', 'source_payload']) {
    assert.ok(cols.includes(c), `deliverable.${c} missing after migration`)
  }
  const wiCols = (db.prepare('PRAGMA table_info(work_item)').all() as Array<{ name: string }>).map((c) => c.name)
  for (const c of ['responsible_party', 'source_issue_type', 'source_payload']) {
    assert.ok(wiCols.includes(c), `work_item.${c} missing after migration`)
  }
  const ipCols = (db.prepare('PRAGMA table_info(import_proposal)').all() as Array<{ name: string }>).map((c) => c.name)
  assert.ok(ipCols.includes('source_extras'), 'import_proposal.source_extras missing')
  db.close()
})

test('mdl v2: derived identity, attested capture, verbatim payload, no revisions, signals', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [
    MDL_V2_HDR,
    'V2-PKG-1,Scope of Work,01,30%,Process,Equipment,Inlet separator,,IFQ,In Progress,25,vendor pending',
    'V2-PKG-1,Technical Datasheet,01,30%,Process,Equipment,Inlet separator,,IFQ,Not Set,Next Phase,',
    // collision group: same package+type, distinguished by package_name
    'V2-PKG-2,RFQ,01,30%,Electrical,Equipment,Transformer TXP-1,,IFQ,Not Started,0,',
    'V2-PKG-2,RFQ,01,30%,Electrical,Equipment,Transformer TXP-2,,IFQ,On Hold,10,',
    // provided deliverable_id wins
    'V2-PKG-2,Calculation,01,30%,Electrical,Equipment,Transformer TXP-1,V2-CALC-01,IFQ,Complete,100,',
    // out-of-range percent → row rejection
    'V2-PKG-3,List,01,30%,Civil,Equipment,Roads,,IFQ,Not Set,150,',
  ].join('\r\n')
  const res = await admin.postCsv(`${P}/import/mdl`, csv)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 5)
  assert.equal(res.body.rejected.length, 1)
  assert.match(res.body.rejected[0].errors[0], /0\.\.100/)

  const dels = env.db.prepare(
    "SELECT doc_no, title, working_status, percent_complete, percent_complete_verbatim, project_phase, target_completeness, source_payload FROM deliverable WHERE project_id = ? AND doc_no LIKE 'V2-%' ORDER BY doc_no",
  ).all(env.projectId) as Array<Record<string, unknown>>
  const byDoc = Object.fromEntries(dels.map((d) => [d.doc_no as string, d]))
  // derived identity: pure per-row function incl. the package_name segment
  assert.ok(byDoc['V2-PKG-1-SCOPE-OF-WORK-INLET-SEPARATOR'], `derived doc_no missing: ${Object.keys(byDoc).join(', ')}`)
  // marker captured verbatim, numeric null
  const marker = byDoc['V2-PKG-1-TECHNICAL-DATASHEET-INLET-SEPARATOR']!
  assert.equal(marker.percent_complete, null)
  assert.equal(marker.percent_complete_verbatim, 'Next Phase')
  // collision group qualified by package_name slug
  assert.ok(byDoc['V2-PKG-2-RFQ-TRANSFORMER-TXP-1'])
  assert.ok(byDoc['V2-PKG-2-RFQ-TRANSFORMER-TXP-2'])
  // provided deliverable_id wins
  assert.ok(byDoc['V2-CALC-01'])
  // attested fields + verbatim unmapped column
  const sow = byDoc['V2-PKG-1-SCOPE-OF-WORK-INLET-SEPARATOR']!
  assert.equal(sow.working_status, 'In Progress')
  assert.equal(sow.percent_complete, 25)
  assert.equal(sow.project_phase, '30%')
  assert.equal(sow.target_completeness, 'IFQ')
  // dual capture: unmapped columns AND the per-row values that map first-row-wins
  // onto the package record (nothing dropped, fidelity direction)
  assert.deepEqual(JSON.parse(sow.source_payload as string),
    { area: '01', custom_note: 'vendor pending', package_name: 'Inlet separator', package_type: 'Equipment' })
  // factual-or-absent: no revision facts in v2 → no revision records
  const revCount = env.db.prepare(
    "SELECT COUNT(*) AS n FROM revision r JOIN deliverable d ON d.id = r.deliverable_id WHERE d.project_id = ? AND d.doc_no LIKE 'V2-%'",
  ).get(env.projectId) as { n: number }
  assert.equal(revCount.n, 0)
  // caught signals: on-hold + percent marker
  const kinds = (res.body.signals ?? []).map((s: { kind: string }) => s.kind)
  assert.ok(kinds.includes('mdl-on-hold'), `signals: ${JSON.stringify(res.body.signals)}`)
  assert.ok(kinds.includes('percent-marker'))
})

test('mdl v2: idempotent re-import updates; within-file duplicates conflict', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [
    MDL_V2_HDR,
    'V2-PKG-1,Scope of Work,01,30%,Process,Equipment,Inlet separator,,IFQ,In Progress,40,vendor confirmed',
    'V2-PKG-1,Scope of Work,01,30%,Process,Equipment,Inlet separator,,IFQ,In Progress,40,vendor confirmed',
  ].join('\r\n')
  const res = await admin.postCsv(`${P}/import/mdl`, csv)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.updated, 1)
  assert.equal(res.body.conflicts.length, 1)
  assert.match(res.body.conflicts[0].reason, /duplicate identity within file/)
  const d = env.db.prepare('SELECT percent_complete FROM deliverable WHERE project_id = ? AND doc_no = ?')
    .get(env.projectId, 'V2-PKG-1-SCOPE-OF-WORK-INLET-SEPARATOR') as { percent_complete: number }
  assert.equal(d.percent_complete, 40)
})

test('attested fields are not in-app editable (reconciliation 1)', async () => {
  const admin = await env.as('admin@t.co')
  const row = env.db.prepare('SELECT id, version FROM deliverable WHERE project_id = ? AND doc_no = ?')
    .get(env.projectId, 'V2-PKG-1-SCOPE-OF-WORK-INLET-SEPARATOR') as { id: number; version: number }
  // a patch carrying ONLY attested fields is refused outright (nothing editable in it)
  const res = await admin.put(`${P}/deliverables/${row.id}`,
    { version: row.version, percentComplete: 99, workingStatus: 'Complete' })
  assert.equal(res.status, 400, JSON.stringify(res.body))
  const d = env.db.prepare('SELECT percent_complete, working_status FROM deliverable WHERE id = ?')
    .get(row.id) as { percent_complete: number; working_status: string }
  assert.equal(d.percent_complete, 40)
  assert.equal(d.working_status, 'In Progress')
  // a mixed patch applies the editable field and silently-never the attested ones
  const res2 = await admin.put(`${P}/deliverables/${row.id}`,
    { version: row.version, remarks: 'note', percentComplete: 99 })
  assert.equal(res2.status, 200, JSON.stringify(res2.body))
  const d2 = env.db.prepare('SELECT percent_complete, remarks FROM deliverable WHERE id = ?')
    .get(row.id) as { percent_complete: number; remarks: string }
  assert.equal(d2.percent_complete, 40)
  assert.equal(d2.remarks, 'note')
})

test('rail v2: placeholders refresh packages only; issue rows land package-anchored with verbatim attested facts', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [
    RAIL_V2_HDR,
    // placeholder: package identity only → no issue record
    'V2-PKG-9,1,Electrical,,30%,,Equipment,UPS package,,,,,,,,,,',
    // decision issue, discipline-valued responsible party (no person match)
    'V2-PKG-8,1,Electrical,,30%,26020-01-PT-1,Documentation,Controls integration,Decision,Decide remote I/O approach,Need client philosophy,Project Management,Not Started,Now,2026-07-07,2026-07-14,2026-07-21,',
    // on-hold risk on a cancelled phase → two caught signals
    'V2-PKG-8,2,Electrical,,Cancelled,,Documentation,Controls integration,Risk,Rework risk if philosophy changes,,Electrical,On Hold,Next,2026-07-07,,2026-07-28,',
    // completed action closes with its actual date
    'V2-PKG-8,3,Electrical,,30%,,Documentation,Controls integration,Action,Issue vendor query,,Electrical,Complete,Now,2026-07-01,2026-07-03,2026-07-03,2026-07-04',
  ].join('\r\n')
  const res = await admin.postCsv(`${P}/import/rail`, csv)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 3)
  assert.equal(res.body.packageRows, 1)
  assert.equal(res.body.intakeCreated, 0)

  const pkg = env.db.prepare('SELECT id, discipline FROM package WHERE project_id = ? AND code = ?')
    .get(env.projectId, 'V2-PKG-9') as { id: number; discipline: string }
  assert.equal(pkg.discipline, 'Electrical')
  const noIssues = env.db.prepare('SELECT COUNT(*) AS n FROM work_item WHERE project_id = ? AND ref LIKE ?')
    .get(env.projectId, 'V2-PKG-9#%') as { n: number }
  assert.equal(noIssues.n, 0)

  const wi = env.db.prepare(
    'SELECT anchor_type, package_id, state, need_by, responsible_party, source_issue_type, kind, source_payload FROM work_item WHERE project_id = ? AND ref = ?',
  ).get(env.projectId, 'V2-PKG-8#1') as Record<string, unknown>
  assert.equal(wi.anchor_type, 'package')
  assert.equal(wi.state, 'open')
  assert.equal(wi.need_by, '2026-07-21') // current target wins
  assert.equal(wi.responsible_party, 'Project Management')
  assert.equal(wi.source_issue_type, 'Decision')
  assert.equal(wi.kind, 'other')
  const pay = JSON.parse(wi.source_payload as string)
  assert.equal(pay.status, 'Not Started')
  assert.equal(pay.coa_tracking_number, '26020-01-PT-1')
  assert.equal(pay.original_target_date, '2026-07-14')

  const closed = env.db.prepare('SELECT state, closed_at, kind FROM work_item WHERE project_id = ? AND ref = ?')
    .get(env.projectId, 'V2-PKG-8#3') as { state: string; closed_at: string; kind: string }
  assert.equal(closed.state, 'closed')
  assert.equal(closed.kind, 'action')
  assert.ok(closed.closed_at.startsWith('2026-07-04'))

  const kinds = (res.body.signals ?? []).map((s: { kind: string; key: string }) => `${s.kind}:${s.key}`)
  assert.ok(kinds.includes('rail-on-hold:V2-PKG-8#2'), JSON.stringify(res.body.signals))
  assert.ok(kinds.includes('phase-cancelled:V2-PKG-8#2'))
})

test('rail v2: re-import updates idempotently under the import-ownership guard', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [
    RAIL_V2_HDR,
    'V2-PKG-8,1,Electrical,,30%,26020-01-PT-1,Documentation,Controls integration,Decision,Decide remote I/O approach,Client philosophy received,Project Management,In Progress,Now,2026-07-07,2026-07-14,2026-07-21,',
  ].join('\r\n')
  const res = await admin.postCsv(`${P}/import/rail`, csv)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.updated, 1)
  const wi = env.db.prepare('SELECT state, source_payload FROM work_item WHERE project_id = ? AND ref = ?')
    .get(env.projectId, 'V2-PKG-8#1') as { state: string; source_payload: string }
  assert.equal(wi.state, 'in_work')
  assert.equal(JSON.parse(wi.source_payload).updates, 'Client philosophy received')
})

test('rail v2: explicit needs_audience imports, rejects invalid values, and round-trips', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [
    `${RAIL_V2_HDR},needs_audience`,
    'V2-PKG-8,1,Electrical,,30%,26020-01-PT-1,Documentation,Controls integration,Decision,Decide remote I/O approach,Client philosophy received,Project Management,In Progress,Now,2026-07-07,2026-07-14,2026-07-21,,client',
    'V2-PKG-8,4,Electrical,,30%,,Documentation,Controls integration,Action,Classify this incorrectly,,Electrical,Not Started,Now,2026-07-07,2026-07-14,2026-07-21,,external',
  ].join('\r\n')
  const res = await admin.postCsv(`${P}/import/rail`, csv)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.updated, 1)
  assert.equal(res.body.rejected.length, 1)
  assert.match(res.body.rejected[0].errors[0], /needs_audience must be internal or client/)

  const wi = env.db.prepare('SELECT needs_audience FROM work_item WHERE project_id = ? AND ref = ?')
    .get(env.projectId, 'V2-PKG-8#1') as { needs_audience: string }
  assert.equal(wi.needs_audience, 'client')

  const pkg = await admin.get(`${P}/reports/standard/package-issue-summary`)
  const row = pkg.body.sections.packages.find((r: any) => r.package.code === 'V2-PKG-8')
  assert.ok(row.needsSplit.client >= 1, JSON.stringify(row.needsSplit))

  const rail = await admin.get(`${P}/export/rail-v2.csv`)
  assert.match(String(rail.body).split('\r\n')[0]!, /needs_audience/)
  assert.match(String(rail.body), /client/)
})

test('standard report surfaces MDL-RAIL hold discrepancies without intake records', async () => {
  const admin = await env.as('admin@t.co')
  const weekly = await admin.get(`${P}/reports/standard/weekly-project-status`)
  assert.equal(weekly.status, 200, JSON.stringify(weekly.body))
  const check = weekly.body.sections.consistencyChecks.mdlRailHoldDiscrepancies
  assert.equal(check.ruleId, 'CONSIST-MDL-RAIL-HOLD')
  assert.ok(check.count >= 2, JSON.stringify(check))
  assert.match(weekly.body.markdown, /MDL\/RAIL hold discrepancies/)
  const intake = env.db.prepare(
    "SELECT COUNT(*) AS n FROM intake_item WHERE project_id = ? AND statement_verbatim LIKE '%CONSIST-MDL-RAIL-HOLD%'",
  ).get(env.projectId) as { n: number }
  assert.equal(intake.n, 0)
})

test('discipline view: % complete is attested-only, equal-weight by type, absent when unattested (DISC-PCT)', async () => {
  const admin = await env.as('admin@t.co')
  const detail = await admin.get(`${P}/disciplines/${encodeURIComponent('Process')}`)
  assert.equal(detail.status, 200, JSON.stringify(detail.body))
  const band = detail.body.band
  assert.ok(band.percentComplete, JSON.stringify(band))
  assert.equal(band.percentComplete.ruleId, 'DISC-PCT')
  // Process discipline: Scope of Work type has one attested doc at 40%; the
  // marker-valued Technical Datasheet type has no attested doc → excluded.
  assert.equal(band.percentComplete.value, 40)
  // Process holds the harness-seeded TST-PR-001 (unattested), the attested Scope of
  // Work (40) and the marker-valued Technical Datasheet → 1/3 attested, one type counted
  assert.match(band.percentComplete.detail, /attested 1\/3 deliverables/)
  assert.ok(band.percentComplete.contributing.length === 1)
  const absent = detail.body.absent.map((a: { figure: string }) => a.figure)
  assert.ok(absent.some((f: string) => f.includes('week-over-week % complete delta')), JSON.stringify(absent))

  // a discipline with no attested % stays absent and says so
  const civil = await admin.get(`${P}/disciplines/${encodeURIComponent('Structural')}`)
  if (civil.status === 200) {
    assert.equal(civil.body.band.percentComplete, undefined)
  }
})

test('round-trip: mdl-v2 and rail-v2 exports reproduce provided columns incl. markers and payload', async () => {
  const admin = await env.as('admin@t.co')
  const mdl = await admin.get(`${P}/export/mdl-v2.csv`)
  assert.equal(mdl.status, 200)
  const mdlText = mdl.body as unknown as string
  const hdr = String(mdlText).split('\r\n')[0]!
  for (const col of ['package', 'deliverable_type', 'working_status', 'percent_complete', 'custom_note']) {
    assert.ok(hdr.includes(col), `mdl-v2 export header missing ${col}: ${hdr}`)
  }
  assert.match(String(mdlText), /Next Phase/) // verbatim marker round-trips
  assert.match(String(mdlText), /vendor confirmed/) // verbatim payload round-trips

  const rail = await admin.get(`${P}/export/rail-v2.csv`)
  assert.equal(rail.status, 200)
  const railText = String(rail.body)
  const railHdr = railText.split('\r\n')[0]!
  for (const col of ['package', 'issue_no', 'issue_type', 'responsible_party', 'status', 'coa_tracking_number']) {
    assert.ok(railHdr.includes(col), `rail-v2 export header missing ${col}: ${railHdr}`)
  }
  assert.match(railText, /V2-PKG-8,1/)
  assert.match(railText, /Not Set|In Progress/) // verbatim source status, not the app state token
  assert.match(railText, /26020-01-PT-1/)
})

test('proposal lane: JSON body carries verbatim non-tabular extras (source_extras)', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [MDL_V2_HDR, 'V2-PKG-1,Scope of Work,01,30%,Process,Equipment,Inlet separator,,IFQ,In Progress,45,'].join('\r\n')
  const extras = {
    'Rules of Credit': [['ENGINEERING & DESIGN', '%'], ['Initial Engineering Input', 10]],
    'metadata': { 'PROJECT NAME:': 'scratch' },
  }
  const created = await admin.post(`${P}/import-proposals?contract=mdl&filename=v2.xlsx`, { csv, extras })
  assert.equal(created.status, 200, JSON.stringify(created.body))
  assert.equal(created.body.state, 'ready_for_review', JSON.stringify(created.body.dryRunReport))
  const got = await admin.get(`${P}/import-proposals/${created.body.id}`)
  assert.deepEqual(got.body.sourceExtras, extras)
})

test('v1 mdl/rail shapes keep working unchanged (additive contract)', async () => {
  const admin = await env.as('admin@t.co')
  const v1 = [
    'doc_no,title,package,discipline,owner,current_rev,state,due_date',
    'V1-DOC-1,Sheet,PKG-A,Process,eor@t.co,A,in_work,2027-01-31',
  ].join('\r\n')
  const res = await admin.postCsv(`${P}/import/mdl`, v1)
  assert.equal(res.status, 200, JSON.stringify(res.body))
  assert.equal(res.body.accepted, 1)
  // v1 still seeds a revision (unchanged behavior)
  const n = env.db.prepare(
    'SELECT COUNT(*) AS n FROM revision r JOIN deliverable d ON d.id = r.deliverable_id WHERE d.doc_no = ?',
  ).get('V1-DOC-1') as { n: number }
  assert.equal(n.n, 1)
})

// ---------------------------------------------------------------------------
// adversarial-review fix-forward pins (2026-07-09)
// ---------------------------------------------------------------------------

test('mdl v2: a later provided deliverable_id ADOPTS the derived-identity record (no duplicate register)', async () => {
  const admin = await env.as('admin@t.co')
  const base = 'MIG-PKG-1,Scope of Work,01,30%,Process,Equipment,Separator,'
  const first = [MDL_V2_HDR, `${base},IFQ,In Progress,10,`].join('\r\n')
  const r1 = await admin.postCsv(`${P}/import/mdl`, first)
  assert.equal(r1.body.accepted, 1)
  const withId = [MDL_V2_HDR,
    'MIG-PKG-1,Scope of Work,01,30%,Process,Equipment,Separator,MIG-SOW-001,IFQ,In Progress,20,'].join('\r\n')
  const r2 = await admin.postCsv(`${P}/import/mdl`, withId)
  assert.equal(r2.body.updated, 1, JSON.stringify(r2.body))
  assert.equal(r2.body.accepted, 0)
  const rows = env.db.prepare("SELECT doc_no, percent_complete FROM deliverable WHERE project_id = ? AND doc_no LIKE 'MIG-%'")
    .all(env.projectId) as Array<{ doc_no: string; percent_complete: number }>
  assert.equal(rows.length, 1)
  assert.equal(rows[0]!.doc_no, 'MIG-SOW-001')
  assert.equal(rows[0]!.percent_complete, 20)
})

test('rail v2: reopening a completed issue sheds the stale closure timestamp', async () => {
  const admin = await env.as('admin@t.co')
  const closed = [RAIL_V2_HDR,
    'RO-PKG-1,1,Electrical,,30%,,Equipment,UPS,Action,Issue vendor query,,Electrical,Complete,Now,2026-07-01,2026-07-03,2026-07-03,2026-07-04'].join('\r\n')
  await admin.postCsv(`${P}/import/rail`, closed)
  const reopened = [RAIL_V2_HDR,
    'RO-PKG-1,1,Electrical,,30%,,Equipment,UPS,Action,Issue vendor query,,Electrical,In Progress,Now,2026-07-01,2026-07-03,2026-07-10,'].join('\r\n')
  const r = await admin.postCsv(`${P}/import/rail`, reopened)
  assert.equal(r.body.updated, 1, JSON.stringify(r.body))
  const wi = env.db.prepare('SELECT state, closed_at FROM work_item WHERE project_id = ? AND ref = ?')
    .get(env.projectId, 'RO-PKG-1#1') as { state: string; closed_at: string | null }
  assert.equal(wi.state, 'in_work')
  assert.equal(wi.closed_at, null)
  // the parity export no longer reports an actual completion date for it
  const rail = await admin.get(`${P}/export/rail-v2.csv`)
  const line = String(rail.body).split('\r\n').find((l: string) => l.startsWith('RO-PKG-1,1'))!
  assert.ok(!line.includes('2026-07-04'), line)
})

test('rail v2: placeholder rows with a blank issue_no still refresh the package', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [RAIL_V2_HDR, 'BL-PKG-1,,Civil,,30%,,Equipment,Culverts,,,,,,,,,,'].join('\r\n')
  const r = await admin.postCsv(`${P}/import/rail`, csv)
  assert.equal(r.body.packageRows, 1, JSON.stringify(r.body))
  assert.equal(r.body.rejected.length, 0)
  const pkg = env.db.prepare('SELECT discipline FROM package WHERE project_id = ? AND code = ?')
    .get(env.projectId, 'BL-PKG-1') as { discipline: string }
  assert.equal(pkg.discipline, 'Civil')
})

test('a malformed v1 mdl file (doc_no dropped, current_rev present) fails loudly as v1, never silently imports as v2', async () => {
  const admin = await env.as('admin@t.co')
  const csv = [
    'title,package,discipline,owner,current_rev,state,due_date,deliverable_type',
    'Sheet,PKG-A,Process,eor@t.co,A,in_work,2027-01-31,Scope of Work',
  ].join('\r\n')
  const res = await admin.postCsv(`${P}/import/mdl`, csv)
  assert.equal(res.status, 400, JSON.stringify(res.body))
})

test('rail-v2 export emits only verbatim source values in source-faithful columns', async () => {
  const admin = await env.as('admin@t.co')
  // an issue with ONLY an original target and no source status beyond vocabulary
  const csv = [RAIL_V2_HDR,
    'VB-PKG-1,1,Civil,,30%,,Equipment,Culverts,Action,Confirm culvert sizing,,Civil,Not Started,Now,,2026-08-01,,'].join('\r\n')
  await admin.postCsv(`${P}/import/rail`, csv)
  const rail = await admin.get(`${P}/export/rail-v2.csv`)
  const text = String(rail.body)
  const hdr = text.split('\r\n')[0]!.split(',')
  const line = text.split('\r\n').find((l: string) => l.startsWith('VB-PKG-1,1'))!.split(',')
  const col = (name: string): string => line[hdr.indexOf(name)] ?? ''
  assert.equal(col('original_target_date'), '2026-08-01')
  assert.equal(col('current_target_date'), '') // need_by fallback is NOT presented as a provided current target
  assert.equal(col('status'), 'Not Started')   // verbatim vocabulary, never the app state token
  assert.equal(col('actual_completion_date'), '')
})
