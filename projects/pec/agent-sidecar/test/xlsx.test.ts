/**
 * D-PEC-42 O-A: zero-dependency .xlsx reader + its wiring into the
 * agent-adaptive upload lane. Fixtures are committed, TWD-shaped, synthetic
 * (test/support/make-fixtures.ts regenerates them). Adversarial cases refuse
 * with a stated basis — never a silent degrade.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { parseXlsxWorkbook, WorkbookError } from '../src/xlsx.ts'
import { adaptWorkbook } from '../src/structured-file.ts'
import { bindActs } from '../src/acts.ts'
import { createStubEngine } from '../src/engine/stub.ts'
import { buildZip } from './support/zip-writer.ts'
import type { PecAgentClient, ProposalView } from '../src/pec-client.ts'
import type { AgentTurnInput } from '../src/engine/port.ts'

const fixture = (name: string): Buffer =>
  readFileSync(new URL(`./fixtures/${name}`, import.meta.url))

const mdlBytes = fixture('twd-mdl-shaped.xlsx')
const railBytes = fixture('twd-rail-shaped-stored.xlsx')

// ---------------------------------------------------------------------------
// parser: grids
// ---------------------------------------------------------------------------

test('D-PEC-42 parser reads a deflate multi-sheet workbook to faithful dense grids', () => {
  const wb = parseXlsxWorkbook(mdlBytes)
  assert.deepEqual(wb.sheets.map((s) => s.name), ['Master Deliverables List', 'Rules of Credit', 'Lists'])
  const grid = wb.sheets[0]!.rows
  assert.equal(grid.length, 6)
  // rich-text shared string concatenated; title row padded with nulls
  assert.equal(grid[0]![0], 'Synthetic Deliverables Register (TWD-shaped fixture)')
  assert.deepEqual(grid[0]!.slice(1), new Array(8).fill(null))
  // header row sits at index 1 — the parser does NOT strip or guess it
  assert.deepEqual(grid[1], ['Document No', 'Title', 'Package', 'Discipline', 'Owner', 'Current Rev', 'State', 'Due Date', 'Remarks'])
  // data row: builtin date serial → ISO string; plain number stays a number
  assert.deepEqual(grid[2], ['MDL-0001', 'Synthetic pump datasheet', 'PKG-01', 'Mechanical', 'pe@example.test', 'A', 'in_work', '2026-07-09', 42])
  // cached formula value used verbatim; boolean → TRUE
  assert.equal(grid[3]![1], 'Synthetic valve list')
  assert.equal(grid[3]![7], '2026-08-01')
  assert.equal(grid[3]![8], 'TRUE')
  // blank row kept in the visual grid
  assert.deepEqual(grid[4], new Array(9).fill(null))
  // sparse row: r= refs honored, custom date format detected
  assert.equal(grid[5]![0], 'MDL-0003')
  assert.deepEqual(grid[5]!.slice(1, 7), new Array(6).fill(null))
  assert.equal(grid[5]![7], '2026-01-15')
})

test('D-PEC-42 parser reads non-tabular sheets verbatim (entities, numbers, uncached formula = blank)', () => {
  const wb = parseXlsxWorkbook(mdlBytes)
  const roc = wb.sheets[1]!.rows
  assert.equal(roc[0]![0], 'ENGINEERING & DESIGN')
  assert.equal(roc[1]![1], 30)
  // a formula cell with no cached <v> is blank — no evaluation, ever
  assert.equal(roc[2]![1], null)
  assert.deepEqual(wb.sheets[2]!.rows.map((r) => r[0]), ['Working Status', 'Not Started', 'In Progress', 'Complete'])
})

test('D-PEC-42 parser reads a stored-method workbook with inline strings and a metadata block', () => {
  const wb = parseXlsxWorkbook(railBytes)
  assert.deepEqual(wb.sheets.map((s) => s.name), ['RAIL', 'Lists'])
  const grid = wb.sheets[0]!.rows
  assert.equal(grid.length, 9)
  assert.equal(grid[0]![0], 'PACKAGES RAIL (synthetic fixture)')
  assert.equal(grid[1]![0], 'DATE / VERSION:')
  // the blank spacer row between metadata block and header survives
  assert.deepEqual(grid[5], new Array(9).fill(null))
  assert.deepEqual(grid[6], ['Item ID', 'Statement', 'Type', 'Log', 'Owner', 'Need By', 'Status', 'Raised By', 'Raised Date'])
  // rich-text inline string concatenated; date serial → ISO
  assert.equal(grid[7]![1], 'Confirm synthetic pump spec')
  assert.equal(grid[7]![5], '2026-07-20')
  // sparse trailing row
  assert.deepEqual(grid[8], ['RAIL-0002', null, 'decision', null, null, null, null, null, null])
})

// ---------------------------------------------------------------------------
// parser: refusals with a stated basis
// ---------------------------------------------------------------------------

test('D-PEC-42 parser refuses an encrypted-flag archive with a stated basis', () => {
  assert.throws(() => parseXlsxWorkbook(fixture('encrypted-flag.xlsx')),
    (e: unknown) => e instanceof WorkbookError && /encrypted/.test(e.message))
})

test('D-PEC-42 parser refuses non-zip bytes with a stated basis', () => {
  assert.throws(() => parseXlsxWorkbook(Buffer.from('doc_no,title\nMDL-1,not a workbook')),
    (e: unknown) => e instanceof WorkbookError && /end-of-central-directory/.test(e.message))
})

test('D-PEC-42 parser refuses zip64 markers with a stated basis', () => {
  const zip = buildZip([{ name: 'xl/workbook.xml', data: '<workbook/>' }])
  zip.writeUInt16LE(0xffff, zip.length - 22 + 10) // total-entries zip64 marker in the EOCD
  assert.throws(() => parseXlsxWorkbook(zip),
    (e: unknown) => e instanceof WorkbookError && /zip64/.test(e.message))
})

test('D-PEC-42 parser refuses unsupported compression methods with a stated basis', () => {
  const zip = buildZip([
    { name: 'xl/workbook.xml', data: '<workbook><sheets><sheet name="S" sheetId="1" r:id="rId1"/></sheets></workbook>', method: 12 },
  ])
  assert.throws(() => parseXlsxWorkbook(zip),
    (e: unknown) => e instanceof WorkbookError && /compression method 12/.test(e.message))
})

test('D-PEC-42 parser refuses the 1904 date system with a stated basis', () => {
  const zip = buildZip([
    {
      name: 'xl/workbook.xml',
      data: '<workbook><workbookPr date1904="1"/><sheets><sheet name="S" sheetId="1" r:id="rId1"/></sheets></workbook>',
    },
    { name: 'xl/worksheets/sheet1.xml', data: '<worksheet><sheetData/></worksheet>' },
  ])
  assert.throws(() => parseXlsxWorkbook(zip),
    (e: unknown) => e instanceof WorkbookError && /1904 date system/.test(e.message))
})

test('D-PEC-42 parser refuses a zip with no workbook part with a stated basis', () => {
  const zip = buildZip([{ name: 'hello.txt', data: 'not a workbook' }])
  assert.throws(() => parseXlsxWorkbook(zip),
    (e: unknown) => e instanceof WorkbookError && /no xl\/workbook\.xml/.test(e.message))
})

// ---------------------------------------------------------------------------
// mapping: the workbook feeds the SAME adaptive lane, header offset tolerated
// ---------------------------------------------------------------------------

test('D-PEC-42 mapper finds the offset header row and maps the tabular sheet to mdl', () => {
  const adapted = adaptWorkbook(parseXlsxWorkbook(mdlBytes), { filename: 'twd-mdl-shaped.xlsx' })
  assert.equal(adapted.ok, true)
  if (!adapted.ok) return
  assert.equal(adapted.contract, 'mdl')
  assert.equal(adapted.sheetName, 'Master Deliverables List')
  assert.equal(adapted.headerRowIndex, 1)
  assert.equal(adapted.filename, 'twd-mdl-shaped.csv')
  assert.match(adapted.csv, /^doc_no,title,package,discipline,owner,current_rev,state,due_date,remarks/)
  assert.match(adapted.csv, /MDL-0001.*2026-07-09,42/)
  assert.equal(adapted.summary.rowCount, 3) // the blank grid row is not a data row
  assert.equal(adapted.summary.sourceFormat, "xlsx sheet 'Master Deliverables List'")
  assert.ok(adapted.summary.notes.some((n) => /header row found at sheet row 2/.test(n)))
  assert.ok(adapted.summary.notes.some((n) => /Rules of Credit, Lists/.test(n)))
  // the sparse row's required-cell gaps are left for the dry-run, not guessed through
  assert.ok(adapted.summary.requiredEmptyRows.some((g) => g.column === 'title'))
})

test('D-PEC-42 mapper skips the metadata block and maps RAIL at header row 7', () => {
  const adapted = adaptWorkbook(parseXlsxWorkbook(railBytes), { filename: 'rail.xlsx' })
  assert.equal(adapted.ok, true)
  if (!adapted.ok) return
  assert.equal(adapted.contract, 'rail')
  assert.equal(adapted.sheetName, 'RAIL')
  assert.equal(adapted.headerRowIndex, 6)
  assert.match(adapted.csv, /^item_id,statement,type,log,owner,need_by,status,raised_by,raised_date/)
  assert.match(adapted.csv, /RAIL-0001,Confirm synthetic pump spec,action,rail,pe@example\.test,2026-07-20/)
})

test('D-PEC-42 mapper refuses a workbook with no contract-shaped sheet, naming the sheets scanned', () => {
  const wb = parseXlsxWorkbook(mdlBytes)
  const adapted = adaptWorkbook({ sheets: wb.sheets.filter((s) => s.name === 'Lists') })
  assert.equal(adapted.ok, false)
  if (adapted.ok) return
  assert.match(adapted.reason, /no sheet in the workbook \(Lists\)/)
  assert.match(adapted.reason, /name the contract/)
})

test('D-PEC-42 mapper honors an explicit sheet restriction', () => {
  const wb = parseXlsxWorkbook(mdlBytes)
  const wrongSheet = adaptWorkbook(wb, { sheet: 'Rules of Credit' })
  assert.equal(wrongSheet.ok, false)
  const noSuch = adaptWorkbook(wb, { sheet: 'Nope' })
  assert.equal(noSuch.ok, false)
  if (!noSuch.ok) assert.match(noSuch.reason, /no sheet named 'Nope'/)
})

// ---------------------------------------------------------------------------
// lane wiring: proposal-gated, verbatim workbook rides the result payload
// ---------------------------------------------------------------------------

const proposalView = (contract: string, sourceName: string | null): ProposalView => ({
  id: 9,
  ref: 'IPR-0009',
  contract,
  state: 'ready_for_review',
  version: 1,
  createdBy: 16,
  sourceName,
  sourceSha256: 'abc',
  dryRunReport: { accepted: 3, updated: 0, conflicts: [], rejected: [], intakeCreated: 0 },
})

function fakeClient(calls: Array<{ contract: string; csv: string; filename?: string }>): PecAgentClient {
  return {
    whoami: () => ({ personId: 16, name: 'PEC Agent', email: 'agent@example.test' }),
    propose: async (_pid: number, contract: string, csv: string, filename?: string) => {
      calls.push({ contract, csv, filename })
      return { ok: true as const, value: proposalView(contract, filename ?? null) }
    },
  } as unknown as PecAgentClient
}

test('D-PEC-42 act maps a .xlsx to the CSV proposal route and carries ALL sheets verbatim in the payload', async () => {
  const calls: Array<{ contract: string; csv: string; filename?: string }> = []
  const acts = bindActs({ pid: 1, egress: 'none', access: 'enumerated', client: fakeClient(calls) })
  const r = await acts.proposeCsv({ xlsxBase64: mdlBytes.toString('base64'), filename: 'twd-mdl-shaped.xlsx' })
  assert.equal(r.kind, 'result')
  assert.equal(calls.length, 1)
  assert.equal(calls[0]!.contract, 'mdl')
  assert.equal(calls[0]!.filename, 'twd-mdl-shaped.csv')
  assert.match(calls[0]!.csv, /^doc_no,title,package,discipline,owner,current_rev,state,due_date/)
  const payload = (r as { payload: any }).payload
  // full-fidelity carry: every sheet — including the non-tabular ones — verbatim
  assert.deepEqual(payload.workbook.sheets.map((s: { name: string }) => s.name),
    ['Master Deliverables List', 'Rules of Credit', 'Lists'])
  assert.equal(payload.workbook.sheets[1].rows[0][0], 'ENGINEERING & DESIGN')
  assert.deepEqual(payload.mappedSheet, { name: 'Master Deliverables List', headerRowIndex: 1 })
  assert.match((r as { summary: string }).summary, /Accept\/apply are human acts/)
})

test('D-PEC-42 act refuses an unreadable workbook with the parser basis and files nothing', async () => {
  const calls: Array<{ contract: string; csv: string; filename?: string }> = []
  const acts = bindActs({ pid: 1, egress: 'none', access: 'enumerated', client: fakeClient(calls) })
  const r = await acts.proposeCsv({
    xlsxBase64: fixture('encrypted-flag.xlsx').toString('base64'),
    filename: 'locked.xlsx',
  })
  assert.equal(r.kind, 'refused')
  assert.equal(calls.length, 0)
  assert.match((r as { reason: string }).reason, /locked\.xlsx was not filed — .*encrypted/)
})

test('D-PEC-42 stub engine routes a base64 .xlsx attachment through the same propose act', async () => {
  const calls: Array<{ contract: string; csv: string; filename?: string }> = []
  const acts = bindActs({ pid: 1, egress: 'none', access: 'enumerated', client: fakeClient(calls) })
  const input: AgentTurnInput = {
    pid: 1,
    message: 'here is the deliverables workbook, covering 2026-07-06 to 2026-07-12',
    attachment: { name: 'twd-mdl-shaped.xlsx', base64: mdlBytes.toString('base64') },
  }
  const events = await createStubEngine().runTurn(input, acts)
  assert.equal(calls.length, 1)
  assert.equal(calls[0]!.contract, 'mdl')
  const actResult = events.find((e) => e.type === 'act:result')
  assert.ok(actResult, 'expected an act:result event')
  assert.match((actResult as { summary: string }).summary, /IPR-0009 proposed \(mdl/)
})

test('multiline cell values survive the workbook → CSV → mapping round-trip intact (fix-forward pin)', () => {
  // an Excel Alt+Enter newline inside UPDATES must stay cell CONTENT — the naive
  // line-split truncated the row and silently shifted every later column
  const grid: Array<Array<string | number | null>> = [
    ['Package ID', 'Issue #', 'Package Discipline', 'PACKAGE', 'ISSUE TYPE', 'ISSUE DESCRIPTION', 'UPDATES', 'Responsible Party', 'STATUS', 'PRIORITY'],
    ['ML-PKG-1', 1, 'Electrical', 'Controls', 'Decision', 'Decide I/O', 'line one\nline two', 'Project Management', 'Not Started', 'Now'],
  ]
  const wb = { sheets: [{ name: 'RAIL', rows: grid }] }
  const adapted = adaptWorkbook(wb as never, { filename: 'ml.xlsx' })
  assert.equal(adapted.ok, true, JSON.stringify(adapted))
  if (!adapted.ok) return
  assert.equal(adapted.contract, 'rail')
  const records = adapted.csv.split('\r\n')
  // header + one data record — the newline stays inside the quoted cell
  assert.equal(adapted.summary.rowCount, 1)
  assert.match(adapted.csv, /"line one\nline two"/)
  const hdr = records[0]!.split(',')
  const dataRecord = adapted.csv.slice(records[0]!.length + 2)
  assert.ok(dataRecord.includes('Project Management'), dataRecord)
  assert.ok(dataRecord.includes('Not Started'), dataRecord)
  assert.equal(hdr.includes('responsible_party'), true)
})
