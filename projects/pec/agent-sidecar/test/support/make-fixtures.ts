/**
 * One-off generator for the committed D-PEC-42 fixture workbooks under
 * test/fixtures/ (run: `node --disable-warning=ExperimentalWarning
 * test/support/make-fixtures.ts`). The fixtures are SHAPE-matched to the
 * owner's TWD templates (multi-sheet, title/metadata rows above the header,
 * date serials, vocabulary sheets) but every value is synthetic — no real
 * project content (F-PEC-3).
 */

import { writeFileSync, mkdirSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { buildZip } from './zip-writer.ts'
import type { ZipWriteEntry } from './zip-writer.ts'

const outDir = fileURLToPath(new URL('../fixtures/', import.meta.url))

/** Excel 1900-system serial for a UTC date (serials ≥ 61 count from 1899-12-30) */
const serial = (y: number, m: number, d: number): number =>
  (Date.UTC(y, m - 1, d) - Date.UTC(1899, 11, 30)) / 86_400_000

const XMLDECL = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
const SS_NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
const REL_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
const PKG_REL_NS = 'http://schemas.openxmlformats.org/package/2006/relationships'

const contentTypes = (sheetCount: number, withShared: boolean): string => XMLDECL
  + `<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">`
  + `<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>`
  + `<Default Extension="xml" ContentType="application/xml"/>`
  + `<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>`
  + Array.from({ length: sheetCount }, (_, i) =>
    `<Override PartName="/xl/worksheets/sheet${i + 1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>`).join('')
  + `<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>`
  + (withShared ? `<Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/>` : '')
  + `</Types>`

const rootRels = XMLDECL
  + `<Relationships xmlns="${PKG_REL_NS}">`
  + `<Relationship Id="rId1" Type="${REL_NS}/officeDocument" Target="xl/workbook.xml"/>`
  + `</Relationships>`

const workbookXml = (names: string[]): string => XMLDECL
  + `<workbook xmlns="${SS_NS}" xmlns:r="${REL_NS}"><sheets>`
  + names.map((n, i) => `<sheet name="${n}" sheetId="${i + 1}" r:id="rId${i + 1}"/>`).join('')
  + `</sheets></workbook>`

const workbookRels = (sheetCount: number, withShared: boolean): string => XMLDECL
  + `<Relationships xmlns="${PKG_REL_NS}">`
  + Array.from({ length: sheetCount }, (_, i) =>
    `<Relationship Id="rId${i + 1}" Type="${REL_NS}/worksheet" Target="worksheets/sheet${i + 1}.xml"/>`).join('')
  + `<Relationship Id="rId${sheetCount + 1}" Type="${REL_NS}/styles" Target="styles.xml"/>`
  + (withShared ? `<Relationship Id="rId${sheetCount + 2}" Type="${REL_NS}/sharedStrings" Target="sharedStrings.xml"/>` : '')
  + `</Relationships>`

/** styles: xf 0 = general, xf 1 = builtin date (14), xf 2 = custom date format */
const stylesXml = XMLDECL
  + `<styleSheet xmlns="${SS_NS}">`
  + `<numFmts count="1"><numFmt numFmtId="164" formatCode="yyyy\\-mm\\-dd"/></numFmts>`
  + `<cellXfs count="3">`
  + `<xf numFmtId="0" fontId="0" fillId="0" borderId="0"/>`
  + `<xf numFmtId="14" fontId="0" fillId="0" borderId="0" applyNumberFormat="1"/>`
  + `<xf numFmtId="164" fontId="0" fillId="0" borderId="0" applyNumberFormat="1"/>`
  + `</cellXfs></styleSheet>`

const sheetXml = (rows: string): string => XMLDECL
  + `<worksheet xmlns="${SS_NS}"><sheetData>${rows}</sheetData></worksheet>`

// ---------------------------------------------------------------------------
// Fixture 1: twd-mdl-shaped.xlsx — deflate; multi-sheet; shared strings incl.
// a rich-text title; title row above the header; date serials (builtin +
// custom formats); numbers; a cached-formula cell; a boolean; a fully blank
// row; a sparse row; non-tabular Rules of Credit + Lists sheets.
// ---------------------------------------------------------------------------

const mdlShared: string[] = [
  /* 0 (rich text, emitted specially below) */ 'Synthetic Deliverables Register (TWD-shaped fixture)',
  /* 1-9 headers */ 'Document No', 'Title', 'Package', 'Discipline', 'Owner', 'Current Rev', 'State', 'Due Date', 'Remarks',
  /* 10+ data */ 'MDL-0001', 'Synthetic pump datasheet', 'PKG-01', 'Mechanical', 'pe@example.test', 'A', 'in_work',
  'MDL-0002', 'PKG-02', 'B', 'issued', 'MDL-0003',
  /* 22 */ 'ENGINEERING & DESIGN', 'Issued for Review', 'Issued for Construction', 'Working Status', 'Not Started', 'In Progress', 'Complete',
]

const mdlSharedXml = XMLDECL
  + `<sst xmlns="${SS_NS}" count="${mdlShared.length}" uniqueCount="${mdlShared.length}">`
  // index 0 is a rich-text run pair the reader must concatenate
  + `<si><r><t xml:space="preserve">Synthetic Deliverables Register </t></r><r><rPr><b/></rPr><t>(TWD-shaped fixture)</t></r></si>`
  + mdlShared.slice(1).map((s) => `<si><t xml:space="preserve">${s.replace(/&/g, '&amp;')}</t></si>`).join('')
  + `</sst>`

const ss = (ref: string, idx: number): string => `<c r="${ref}" t="s"><v>${idx}</v></c>`

const mdlSheet1 = sheetXml(
  // row 1: title only (rich-text shared string)
  `<row r="1">${ss('A1', 0)}</row>`
  // row 2: the real header row (offset header — title row above it)
  + `<row r="2">${[1, 2, 3, 4, 5, 6, 7, 8, 9].map((i, c) => ss(`${'ABCDEFGHI'[c]}2`, i)).join('')}</row>`
  // row 3: full data row; H3 = builtin-format date serial; I3 = plain number
  + `<row r="3">${ss('A3', 10)}${ss('B3', 11)}${ss('C3', 12)}${ss('D3', 13)}${ss('E3', 14)}${ss('F3', 15)}${ss('G3', 16)}`
  + `<c r="H3" s="1"><v>${serial(2026, 7, 9)}</v></c><c r="I3"><v>42</v></c></row>`
  // row 4: cached formula string (B4), boolean (I4)
  + `<row r="4">${ss('A4', 17)}<c r="B4" t="str"><f>CONCATENATE("Synthetic"," valve list")</f><v>Synthetic valve list</v></c>`
  + `${ss('C4', 18)}${ss('D4', 13)}${ss('E4', 14)}${ss('F4', 19)}${ss('G4', 20)}`
  + `<c r="H4" s="1"><v>${serial(2026, 8, 1)}</v></c><c r="I4" t="b"><v>1</v></c></row>`
  // row 5: entirely absent (blank row in the visual grid)
  // row 6: sparse row — only A6 and H6 carry values (H6 = custom-format date)
  + `<row r="6">${ss('A6', 21)}<c r="H6" s="2"><v>${serial(2026, 1, 15)}</v></c></row>`,
)

const mdlSheet2 = sheetXml(
  `<row r="1">${ss('A1', 22)}</row>`
  + `<row r="2">${ss('A2', 23)}<c r="B2"><v>30</v></c></row>`
  // formula with NO cached value → blank (no evaluation, ever)
  + `<row r="3">${ss('A3', 24)}<c r="B3"><f>1-B2</f></c></row>`,
)

const mdlSheet3 = sheetXml(
  `<row r="1">${ss('A1', 25)}</row><row r="2">${ss('A2', 26)}</row>`
  + `<row r="3">${ss('A3', 27)}</row><row r="4">${ss('A4', 28)}</row>`,
)

const mdlEntries: ZipWriteEntry[] = [
  { name: '[Content_Types].xml', data: contentTypes(3, true) },
  { name: '_rels/.rels', data: rootRels },
  { name: 'xl/workbook.xml', data: workbookXml(['Master Deliverables List', 'Rules of Credit', 'Lists']) },
  { name: 'xl/_rels/workbook.xml.rels', data: workbookRels(3, true) },
  { name: 'xl/styles.xml', data: stylesXml },
  { name: 'xl/sharedStrings.xml', data: mdlSharedXml },
  { name: 'xl/worksheets/sheet1.xml', data: mdlSheet1 },
  { name: 'xl/worksheets/sheet2.xml', data: mdlSheet2 },
  { name: 'xl/worksheets/sheet3.xml', data: mdlSheet3 },
]

// ---------------------------------------------------------------------------
// Fixture 2: twd-rail-shaped-stored.xlsx — every entry STORED (method 0);
// inline strings only (incl. a rich-text run pair, no sharedStrings part);
// RAIL-shaped: sheet title row, metadata-label block, blank row, header at
// row 7, data from row 8, a sparse trailing row.
// ---------------------------------------------------------------------------

const is = (ref: string, text: string): string =>
  `<c r="${ref}" t="inlineStr"><is><t xml:space="preserve">${text.replace(/&/g, '&amp;')}</t></is></c>`

const railHeader = ['Item ID', 'Statement', 'Type', 'Log', 'Owner', 'Need By', 'Status', 'Raised By', 'Raised Date']

const railSheet1 = sheetXml(
  `<row r="1">${is('A1', 'PACKAGES RAIL (synthetic fixture)')}</row>`
  + `<row r="2">${is('A2', 'DATE / VERSION:')}${is('B2', '2026-07-09 / 0')}</row>`
  + `<row r="3">${is('A3', 'PROJECT NAME:')}${is('B3', 'Synthetic Project')}</row>`
  + `<row r="4">${is('A4', 'PROJECT NO.:')}${is('B4', '00000')}</row>`
  + `<row r="5">${is('A5', 'DOC NO.:')}${is('B5', 'SYN-RAIL-000')}</row>`
  // row 6: blank
  + `<row r="7">${railHeader.map((h, c) => is(`${'ABCDEFGHI'[c]}7`, h)).join('')}</row>`
  // row 8: data — B8 is a rich-text inline string; F8 a builtin-format date serial
  + `<row r="8">${is('A8', 'RAIL-0001')}`
  + `<c r="B8" t="inlineStr"><is><r><t xml:space="preserve">Confirm synthetic </t></r><r><rPr><i/></rPr><t>pump spec</t></r></is></c>`
  + `${is('C8', 'action')}${is('D8', 'rail')}${is('E8', 'pe@example.test')}`
  + `<c r="F8" s="1"><v>${serial(2026, 7, 20)}</v></c>`
  + `${is('G8', 'open')}${is('H8', 'pe@example.test')}${is('I8', '2026-07-01')}</row>`
  // row 9: sparse — only A9 and C9
  + `<row r="9">${is('A9', 'RAIL-0002')}${is('C9', 'decision')}</row>`,
)

const railSheet2 = sheetXml(
  `<row r="1">${is('A1', 'ISSUE TYPE')}</row><row r="2">${is('A2', 'Decision')}</row>`
  + `<row r="3">${is('A3', 'Information')}</row><row r="4">${is('A4', 'Action')}</row>`,
)

const railEntries: ZipWriteEntry[] = [
  { name: '[Content_Types].xml', data: contentTypes(2, false), method: 0 },
  { name: '_rels/.rels', data: rootRels, method: 0 },
  { name: 'xl/workbook.xml', data: workbookXml(['RAIL', 'Lists']), method: 0 },
  { name: 'xl/_rels/workbook.xml.rels', data: workbookRels(2, false), method: 0 },
  { name: 'xl/styles.xml', data: stylesXml, method: 0 },
  { name: 'xl/worksheets/sheet1.xml', data: railSheet1, method: 0 },
  { name: 'xl/worksheets/sheet2.xml', data: railSheet2, method: 0 },
]

// ---------------------------------------------------------------------------
// Fixture 3: encrypted-flag.xlsx — every entry carries GP bit 0 (encrypted);
// the reader must refuse with a stated basis. (The "compressed" bytes are the
// plain deflate stream — the flag alone is the refusal trigger.)
// ---------------------------------------------------------------------------

const encryptedEntries: ZipWriteEntry[] = mdlEntries.map((e) => ({ ...e, gpFlag: 0x0001 }))

mkdirSync(outDir, { recursive: true })
writeFileSync(`${outDir}twd-mdl-shaped.xlsx`, buildZip(mdlEntries))
writeFileSync(`${outDir}twd-rail-shaped-stored.xlsx`, buildZip(railEntries))
writeFileSync(`${outDir}encrypted-flag.xlsx`, buildZip(encryptedEntries))
console.log(`wrote 3 fixture workbooks to ${outDir}`)
