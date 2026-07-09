/**
 * Zero-dependency read-only `.xlsx` parser (D-PEC-42 O-A). `.xlsx` is ZIP +
 * SpreadsheetML; this module implements exactly the slice the upload lane
 * needs and REFUSES (thrown WorkbookError with a stated basis) anything it
 * cannot faithfully read — never a silent degrade (K-INVENT-1):
 *
 * - ZIP: end-of-central-directory + central directory only; stored (method 0)
 *   and deflate (method 8, `node:zlib` inflateRawSync). Encrypted entries,
 *   zip64 markers, and unknown compression methods throw.
 * - SpreadsheetML: workbook.xml sheet order, workbook rels for sheet targets,
 *   sharedStrings.xml (rich-text runs concatenated), styles.xml date-format
 *   detection (1900 date system; date-formatted numeric cells become ISO
 *   YYYY-MM-DD strings), cell types s/str/inlineStr/b/n/e. Formula cells use
 *   the cached <v> only; a formula with no cached value is blank — no
 *   evaluation, ever.
 * - Output: per sheet, a dense rows grid (string | number | null) faithful to
 *   the visual grid (sparse r= attributes honored, blank rows kept). The
 *   parser never guesses header rows — the adaptive mapper does that.
 */

import { inflateRawSync } from 'node:zlib'

/** A refusal basis from the workbook reader — always a stated reason, never a guess. */
export class WorkbookError extends Error {
  constructor(basis: string) {
    super(basis)
    this.name = 'WorkbookError'
  }
}

export type CellValue = string | number | null

export interface WorkbookSheet {
  name: string
  /** dense grid matching the visual sheet: rows of string | number | null */
  rows: CellValue[][]
}

export interface ParsedWorkbook {
  sheets: WorkbookSheet[]
}

// ---------------------------------------------------------------------------
// Minimal read-only ZIP
// ---------------------------------------------------------------------------

const EOCD_SIG = 0x06054b50
const CEN_SIG = 0x02014b50
const LOC_SIG = 0x04034b50
const ZIP64_MARK16 = 0xffff
const ZIP64_MARK32 = 0xffffffff

interface ZipEntry {
  name: string
  gpFlag: number
  method: number
  compressedSize: number
  uncompressedSize: number
  localHeaderOffset: number
}

function findEocd(buf: Buffer): number {
  // EOCD is 22 bytes + up to 65535 bytes of comment, from the end.
  const floor = Math.max(0, buf.length - 22 - 0xffff)
  for (let i = buf.length - 22; i >= floor; i--) {
    if (buf.readUInt32LE(i) === EOCD_SIG) return i
  }
  throw new WorkbookError('not a readable .xlsx: no ZIP end-of-central-directory record found')
}

function readZipEntries(buf: Buffer): ZipEntry[] {
  if (buf.length < 22) throw new WorkbookError('not a readable .xlsx: file is smaller than a ZIP archive')
  const eocd = findEocd(buf)
  const diskEntries = buf.readUInt16LE(eocd + 8)
  const totalEntries = buf.readUInt16LE(eocd + 10)
  const cdSize = buf.readUInt32LE(eocd + 12)
  const cdOffset = buf.readUInt32LE(eocd + 16)
  if (totalEntries === ZIP64_MARK16 || diskEntries === ZIP64_MARK16
    || cdSize === ZIP64_MARK32 || cdOffset === ZIP64_MARK32) {
    throw new WorkbookError('unsupported .xlsx: zip64 archive markers present — beyond this reader\'s limits')
  }
  if (cdOffset + cdSize > buf.length) {
    throw new WorkbookError('not a readable .xlsx: ZIP central directory lies outside the file')
  }
  const entries: ZipEntry[] = []
  let p = cdOffset
  for (let i = 0; i < totalEntries; i++) {
    if (p + 46 > buf.length || buf.readUInt32LE(p) !== CEN_SIG) {
      throw new WorkbookError('not a readable .xlsx: malformed ZIP central directory entry')
    }
    const gpFlag = buf.readUInt16LE(p + 8)
    const method = buf.readUInt16LE(p + 10)
    const compressedSize = buf.readUInt32LE(p + 20)
    const uncompressedSize = buf.readUInt32LE(p + 24)
    const nameLen = buf.readUInt16LE(p + 28)
    const extraLen = buf.readUInt16LE(p + 30)
    const commentLen = buf.readUInt16LE(p + 32)
    const localHeaderOffset = buf.readUInt32LE(p + 42)
    if (compressedSize === ZIP64_MARK32 || uncompressedSize === ZIP64_MARK32 || localHeaderOffset === ZIP64_MARK32) {
      throw new WorkbookError('unsupported .xlsx: zip64 entry sizes present — beyond this reader\'s limits')
    }
    const name = buf.subarray(p + 46, p + 46 + nameLen).toString('utf8')
    entries.push({ name, gpFlag, method, compressedSize, uncompressedSize, localHeaderOffset })
    p += 46 + nameLen + extraLen + commentLen
  }
  return entries
}

function extractEntry(buf: Buffer, entry: ZipEntry): Buffer {
  // GP bit 0 = encrypted; bit 6 = strong encryption.
  if ((entry.gpFlag & 0x0001) !== 0 || (entry.gpFlag & 0x0040) !== 0) {
    throw new WorkbookError(`unsupported .xlsx: entry '${entry.name}' is encrypted — encrypted workbooks are not readable here`)
  }
  const p = entry.localHeaderOffset
  if (p + 30 > buf.length || buf.readUInt32LE(p) !== LOC_SIG) {
    throw new WorkbookError(`not a readable .xlsx: malformed ZIP local header for '${entry.name}'`)
  }
  const nameLen = buf.readUInt16LE(p + 26)
  const extraLen = buf.readUInt16LE(p + 28)
  const start = p + 30 + nameLen + extraLen
  const data = buf.subarray(start, start + entry.compressedSize)
  if (data.length !== entry.compressedSize) {
    throw new WorkbookError(`not a readable .xlsx: truncated data for ZIP entry '${entry.name}'`)
  }
  if (entry.method === 0) return Buffer.from(data)
  if (entry.method === 8) {
    try {
      return inflateRawSync(data)
    } catch {
      throw new WorkbookError(`not a readable .xlsx: deflate stream for '${entry.name}' failed to inflate`)
    }
  }
  throw new WorkbookError(`unsupported .xlsx: entry '${entry.name}' uses compression method ${entry.method} (only stored and deflate are readable)`)
}

// ---------------------------------------------------------------------------
// Minimal XML helpers (regex-scoped to SpreadsheetML's shapes; no DOM)
// ---------------------------------------------------------------------------

function decodeXml(text: string): string {
  return text.replace(/&(#x?[0-9a-fA-F]+|[a-z]+);/g, (whole, body: string) => {
    if (body.startsWith('#x') || body.startsWith('#X')) return String.fromCodePoint(parseInt(body.slice(2), 16))
    if (body.startsWith('#')) return String.fromCodePoint(parseInt(body.slice(1), 10))
    switch (body) {
      case 'amp': return '&'
      case 'lt': return '<'
      case 'gt': return '>'
      case 'quot': return '"'
      case 'apos': return "'"
      default: return whole
    }
  })
}

function attrOf(tag: string, name: string): string | undefined {
  const m = new RegExp(`(?:^|\\s)${name}="([^"]*)"`).exec(tag)
  return m ? decodeXml(m[1]!) : undefined
}

/** concatenate every <t>…</t> in a fragment (plain text AND rich-text runs) */
function textRuns(fragment: string): string {
  let out = ''
  const re = /<(?:\w+:)?t(?:\s[^>]*)?>([\s\S]*?)<\/(?:\w+:)?t>|<(?:\w+:)?t(?:\s[^>]*)?\/>/g
  let m: RegExpExecArray | null
  while ((m = re.exec(fragment)) !== null) out += decodeXml(m[1] ?? '')
  return out
}

// ---------------------------------------------------------------------------
// SpreadsheetML extraction
// ---------------------------------------------------------------------------

/** builtin numFmtIds Excel renders as dates (1900 system; ECMA-376 §18.8.30) */
const BUILTIN_DATE_FMT_IDS = new Set([
  14, 15, 16, 17, 22, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 57, 58,
])

/** does a custom format code render as a date? (day/month/year tokens outside quotes/brackets) */
function isDateFormatCode(code: string): boolean {
  const bare = code.replace(/\[[^\]]*\]/g, '').replace(/"[^"]*"/g, '').replace(/\\./g, '')
  return /[dy]/i.test(bare) || (/m/i.test(bare) && !/[hs]/i.test(bare))
}

/** cellXfs index → is-date-format, from styles.xml (absent styles → nothing is a date) */
function dateStyleFlags(stylesXml: string | null): boolean[] {
  if (stylesXml == null) return []
  const custom = new Map<number, string>()
  const numFmtRe = /<(?:\w+:)?numFmt\s[^>]*\/?>/g
  let m: RegExpExecArray | null
  while ((m = numFmtRe.exec(stylesXml)) !== null) {
    const id = Number(attrOf(m[0], 'numFmtId') ?? '')
    const code = attrOf(m[0], 'formatCode')
    if (Number.isFinite(id) && code != null) custom.set(id, code)
  }
  const cellXfsMatch = /<(?:\w+:)?cellXfs(?:\s[^>]*)?>([\s\S]*?)<\/(?:\w+:)?cellXfs>/.exec(stylesXml)
  if (!cellXfsMatch) return []
  const flags: boolean[] = []
  const xfRe = /<(?:\w+:)?xf(?:\s[^>]*)?\/?>/g
  while ((m = xfRe.exec(cellXfsMatch[1]!)) !== null) {
    const fmtId = Number(attrOf(m[0], 'numFmtId') ?? '0')
    const code = custom.get(fmtId)
    flags.push(BUILTIN_DATE_FMT_IDS.has(fmtId) || (code != null && isDateFormatCode(code)))
  }
  return flags
}

/**
 * 1900-system Excel date serial → ISO YYYY-MM-DD. Serials 1–59 count from
 * 1899-12-31; 61+ count from 1899-12-30 (absorbing Excel's fictitious
 * 1900-02-29 at serial 60, which is emitted as Excel displays it).
 */
function serialToIsoDate(serial: number): string {
  const days = Math.floor(serial)
  if (days === 60) return '1900-02-29'
  const epochMs = days < 60 ? Date.UTC(1899, 11, 31) : Date.UTC(1899, 11, 30)
  const d = new Date(epochMs + days * 86_400_000)
  const pad = (n: number): string => String(n).padStart(2, '0')
  return `${d.getUTCFullYear()}-${pad(d.getUTCMonth() + 1)}-${pad(d.getUTCDate())}`
}

/** shared strings in order; each <si> concatenates its rich-text runs */
function parseSharedStrings(xml: string | null): string[] {
  if (xml == null) return []
  const out: string[] = []
  const re = /<(?:\w+:)?si(?:\s[^>]*)?>([\s\S]*?)<\/(?:\w+:)?si>/g
  let m: RegExpExecArray | null
  while ((m = re.exec(xml)) !== null) out.push(textRuns(m[1]!))
  return out
}

/** "BC7" → zero-based column index 54 */
function colIndexOf(cellRef: string): number {
  let col = 0
  for (const ch of cellRef) {
    const c = ch.charCodeAt(0)
    if (c >= 65 && c <= 90) col = col * 26 + (c - 64)
    else break
  }
  return col - 1
}

interface SheetTarget { name: string; entryName: string }

/** sheet order + resolved worksheet entry names from workbook.xml + its rels */
function resolveSheets(workbookXml: string, relsXml: string | null): SheetTarget[] {
  const relTargets = new Map<string, string>()
  if (relsXml != null) {
    const re = /<(?:\w+:)?Relationship\s[^>]*\/?>/g
    let m: RegExpExecArray | null
    while ((m = re.exec(relsXml)) !== null) {
      const id = attrOf(m[0], 'Id')
      const target = attrOf(m[0], 'Target')
      if (id != null && target != null) relTargets.set(id, target)
    }
  }
  const sheets: SheetTarget[] = []
  const sheetRe = /<(?:\w+:)?sheet\s[^>]*\/?>/g
  let m: RegExpExecArray | null
  let ordinal = 0
  while ((m = sheetRe.exec(workbookXml)) !== null) {
    ordinal += 1
    const name = attrOf(m[0], 'name') ?? `Sheet${ordinal}`
    const rid = attrOf(m[0], 'r:id') ?? attrOf(m[0], 'id')
    const target = rid != null ? relTargets.get(rid) : undefined
    const fallback = `worksheets/sheet${ordinal}.xml`
    const resolved = (target ?? fallback).replace(/^\//, '')
    const entryName = resolved.startsWith('xl/') ? resolved : `xl/${resolved}`
    sheets.push({ name, entryName })
  }
  if (sheets.length === 0) throw new WorkbookError('not a readable .xlsx: workbook.xml declares no sheets')
  return sheets
}

/** one worksheet XML → dense grid (sparse r= refs honored; blank rows kept) */
function parseSheetGrid(xml: string, shared: string[], dateStyles: boolean[]): CellValue[][] {
  const sparse = new Map<number, Map<number, CellValue>>()
  let maxRow = -1
  let maxCol = -1
  const rowRe = /<(?:\w+:)?row(?:\s[^>]*)?(?:\/>|>([\s\S]*?)<\/(?:\w+:)?row>)/g
  let rowMatch: RegExpExecArray | null
  let rowCursor = -1
  while ((rowMatch = rowRe.exec(xml)) !== null) {
    const rowTag = /^<[^>]*>/.exec(rowMatch[0])![0]
    const declared = attrOf(rowTag, 'r')
    const rowIdx = declared != null ? Number(declared) - 1 : rowCursor + 1
    if (!Number.isInteger(rowIdx) || rowIdx < 0) {
      throw new WorkbookError('not a readable .xlsx: worksheet row has an unreadable r= reference')
    }
    rowCursor = rowIdx
    const body = rowMatch[1] ?? ''
    const cells = new Map<number, CellValue>()
    const cellRe = /<(?:\w+:)?c(?:\s[^>]*)?(?:\/>|>([\s\S]*?)<\/(?:\w+:)?c>)/g
    let cellMatch: RegExpExecArray | null
    let colCursor = -1
    while ((cellMatch = cellRe.exec(body)) !== null) {
      const cellTag = /^<[^>]*>/.exec(cellMatch[0])![0]
      const ref = attrOf(cellTag, 'r')
      const colIdx = ref != null ? colIndexOf(ref) : colCursor + 1
      if (colIdx < 0) throw new WorkbookError('not a readable .xlsx: worksheet cell has an unreadable r= reference')
      colCursor = colIdx
      const value = parseCellValue(cellTag, cellMatch[1] ?? '', shared, dateStyles)
      if (value !== null) {
        cells.set(colIdx, value)
        if (colIdx > maxCol) maxCol = colIdx
      }
    }
    if (cells.size > 0) sparse.set(rowIdx, cells)
    if (rowIdx > maxRow) maxRow = rowIdx
  }
  const grid: CellValue[][] = []
  for (let r = 0; r <= maxRow; r++) {
    const row: CellValue[] = new Array<CellValue>(maxCol + 1).fill(null)
    const cells = sparse.get(r)
    if (cells) for (const [c, v] of cells) row[c] = v
    grid.push(row)
  }
  return grid
}

function parseCellValue(cellTag: string, body: string, shared: string[], dateStyles: boolean[]): CellValue {
  const type = attrOf(cellTag, 't') ?? 'n'
  if (type === 'inlineStr') {
    const is = /<(?:\w+:)?is(?:\s[^>]*)?>([\s\S]*?)<\/(?:\w+:)?is>/.exec(body)
    return is ? textRuns(is[1]!) : null
  }
  const vMatch = /<(?:\w+:)?v(?:\s[^>]*)?>([\s\S]*?)<\/(?:\w+:)?v>/.exec(body)
  // a formula cell with no cached <v> is blank — cached values only, no evaluation
  if (!vMatch) return null
  const raw = decodeXml(vMatch[1]!)
  if (type === 's') {
    const idx = Number(raw)
    const hit = shared[idx]
    if (hit === undefined) throw new WorkbookError(`not a readable .xlsx: shared-string index ${raw} has no entry`)
    return hit
  }
  if (type === 'str' || type === 'e') return raw
  if (type === 'b') return raw.trim() === '1' ? 'TRUE' : 'FALSE'
  // numeric (t="n" or untyped)
  const num = Number(raw)
  if (!Number.isFinite(num)) {
    throw new WorkbookError(`not a readable .xlsx: numeric cell carries a non-numeric value '${raw}'`)
  }
  const styleIdx = Number(attrOf(cellTag, 's') ?? '-1')
  if (styleIdx >= 0 && dateStyles[styleIdx] === true && num >= 1) return serialToIsoDate(num)
  return num
}

/**
 * Parse a `.xlsx` workbook to sheets of dense value grids. Throws
 * WorkbookError with a stated basis for anything unreadable or outside this
 * reader's declared limits.
 */
export function parseXlsxWorkbook(bytes: Uint8Array): ParsedWorkbook {
  const buf = Buffer.isBuffer(bytes) ? bytes : Buffer.from(bytes)
  const entries = readZipEntries(buf)
  const byName = new Map(entries.map((e) => [e.name, e]))
  const readText = (name: string): string | null => {
    const entry = byName.get(name)
    return entry ? extractEntry(buf, entry).toString('utf8') : null
  }
  const workbookXml = readText('xl/workbook.xml')
  if (workbookXml == null) {
    throw new WorkbookError('not a readable .xlsx: no xl/workbook.xml entry (is this really a workbook?)')
  }
  if (/<(?:\w+:)?workbookPr\s[^>]*date1904="(?:1|true)"/.test(workbookXml)) {
    throw new WorkbookError('unsupported .xlsx: 1904 date system — only the 1900 date system is readable here')
  }
  const shared = parseSharedStrings(readText('xl/sharedStrings.xml'))
  const dateStyles = dateStyleFlags(readText('xl/styles.xml'))
  const targets = resolveSheets(workbookXml, readText('xl/_rels/workbook.xml.rels'))
  const sheets: WorkbookSheet[] = targets.map((t) => {
    const xml = readText(t.entryName)
    if (xml == null) throw new WorkbookError(`not a readable .xlsx: sheet '${t.name}' points at missing entry '${t.entryName}'`)
    return { name: t.name, rows: parseSheetGrid(xml, shared, dateStyles) }
  })
  return { sheets }
}
