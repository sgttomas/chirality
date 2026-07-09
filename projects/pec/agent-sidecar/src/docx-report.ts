import { mkdir, writeFile } from 'node:fs/promises'
import { join } from 'node:path'
import { deflateRawSync } from 'node:zlib'

export interface ReportPeriod {
  start: string
  end: string
}

export interface DraftDocxInput {
  project: { code: string; name: string }
  period: ReportPeriod | null
  generatedAt: string
  compositionClarification: string
  disciplines: DisciplineDetail[]
  packageDetails: PackageDetail[]
}

export interface DraftDocxResult {
  filename: string
  documentXml: string
  documentText: string
  bytes: Buffer
  figures: {
    disciplines: number
    inWorkDeliverables: number
    issuancesThisPeriod: number | null
    packageIssueRows: number
    packageDecisionRows: number
    packageInterfaceRows: number
  }
}

interface DisciplineDetail {
  discipline: string
  period?: ReportPeriod | null
  band?: Record<string, { value: number; ruleId: string; detail?: string }>
  sections?: {
    activities?: {
      groups?: Array<{
        type: string
        deliverables: Array<{
          docNo: string
          title: string
          workflow?: { label?: string; currentState?: string }
          percentComplete?: number | null
          percentCompleteVerbatim?: string | null
        }>
      }>
    }
    issuances?: {
      rows?: Array<{ ref: string; docNo?: string; issuedAt?: string; purpose?: string; transmittalRef?: string }>
    }
  }
  absent?: Array<{ figure: string; reason: string }>
}

interface PackageIssue {
  type: string
  ref: string
  title: string
  detail?: string
  state?: string
  needBy?: string | null
}

interface PackageDetail {
  package?: { code: string; name: string }
  summary?: {
    openIssues?: number
    openHolds?: number
    openRisks?: number
    openActionItems?: number
    openDecisions?: number
    openInterfaces?: number
  }
  issues?: PackageIssue[]
  decisions?: Array<{ ref: string; title: string; state?: string; needBy?: string | null }>
  interfaces?: Array<{ ref: string; title: string; state?: string; giving?: string; receiving?: string; needBy?: string | null }>
}

const CONTENT_TYPES = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>`

const ROOT_RELS = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>`

const DOC_RELS = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>`

const STYLES = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
  <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="32"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/><w:rPr><w:i/><w:sz w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/><w:pPr><w:ind w:left="720"/></w:pPr></w:style>
</w:styles>`

const CRC_TABLE = (() => {
  const table = new Uint32Array(256)
  for (let n = 0; n < 256; n++) {
    let c = n
    for (let k = 0; k < 8; k++) c = (c & 1) !== 0 ? 0xedb88320 ^ (c >>> 1) : c >>> 1
    table[n] = c >>> 0
  }
  return table
})()

function crc32(buf: Buffer): number {
  let crc = 0xffffffff
  for (const byte of buf) crc = (CRC_TABLE[(crc ^ byte) & 0xff]! ^ (crc >>> 8)) >>> 0
  return (crc ^ 0xffffffff) >>> 0
}

function buildZip(entries: Array<{ name: string; data: Buffer | string }>): Buffer {
  const locals: Buffer[] = []
  const centrals: Buffer[] = []
  let offset = 0
  for (const entry of entries) {
    const raw = Buffer.isBuffer(entry.data) ? entry.data : Buffer.from(entry.data, 'utf8')
    const compressed = deflateRawSync(raw)
    const crc = crc32(raw)
    const name = Buffer.from(entry.name, 'utf8')

    const local = Buffer.alloc(30)
    local.writeUInt32LE(0x04034b50, 0)
    local.writeUInt16LE(20, 4)
    local.writeUInt16LE(0, 6)
    local.writeUInt16LE(8, 8)
    local.writeUInt16LE(0, 10)
    local.writeUInt16LE(0, 12)
    local.writeUInt32LE(crc, 14)
    local.writeUInt32LE(compressed.length, 18)
    local.writeUInt32LE(raw.length, 22)
    local.writeUInt16LE(name.length, 26)
    local.writeUInt16LE(0, 28)
    locals.push(local, name, compressed)

    const central = Buffer.alloc(46)
    central.writeUInt32LE(0x02014b50, 0)
    central.writeUInt16LE(20, 4)
    central.writeUInt16LE(20, 6)
    central.writeUInt16LE(0, 8)
    central.writeUInt16LE(8, 10)
    central.writeUInt16LE(0, 12)
    central.writeUInt16LE(0, 14)
    central.writeUInt32LE(crc, 16)
    central.writeUInt32LE(compressed.length, 20)
    central.writeUInt32LE(raw.length, 24)
    central.writeUInt16LE(name.length, 28)
    central.writeUInt16LE(0, 30)
    central.writeUInt16LE(0, 32)
    central.writeUInt16LE(0, 34)
    central.writeUInt16LE(0, 36)
    central.writeUInt32LE(0, 38)
    central.writeUInt32LE(offset, 42)
    centrals.push(central, name)
    offset += local.length + name.length + compressed.length
  }
  const centralBuf = Buffer.concat(centrals)
  const eocd = Buffer.alloc(22)
  eocd.writeUInt32LE(0x06054b50, 0)
  eocd.writeUInt16LE(0, 4)
  eocd.writeUInt16LE(0, 6)
  eocd.writeUInt16LE(entries.length, 8)
  eocd.writeUInt16LE(entries.length, 10)
  eocd.writeUInt32LE(centralBuf.length, 12)
  eocd.writeUInt32LE(offset, 16)
  eocd.writeUInt16LE(0, 20)
  return Buffer.concat([...locals, centralBuf, eocd])
}

function xml(s: unknown): string {
  return String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&apos;')
}

function text(s: unknown): string {
  return String(s ?? '').replace(/\s+/g, ' ').trim()
}

function para(style: string | null, body: string): string {
  const pPr = style ? `<w:pPr><w:pStyle w:val="${style}"/></w:pPr>` : ''
  return `<w:p>${pPr}<w:r><w:t xml:space="preserve">${xml(body)}</w:t></w:r></w:p>`
}

function pct(d: { percentComplete?: number | null; percentCompleteVerbatim?: string | null }): string {
  if (d.percentComplete != null) return `${d.percentComplete}%`
  if (d.percentCompleteVerbatim) return d.percentCompleteVerbatim
  return 'percent absent'
}

function activityLines(discipline: DisciplineDetail): string[] {
  const groups = discipline.sections?.activities?.groups ?? []
  const lines: string[] = []
  for (const group of groups) {
    const deliverables = group.deliverables ?? []
    if (deliverables.length === 0) continue
    lines.push(`${group.type} (basis: DISC-ACT):`)
    for (const d of deliverables) {
      const basis = d.percentComplete != null || d.percentCompleteVerbatim ? 'DISC-ACT; DISC-PCT' : 'DISC-ACT'
      lines.push(`- ${d.docNo} - ${text(d.title)}; ${d.workflow?.label ?? d.workflow?.currentState ?? 'workflow recorded'}; % ${pct(d)} (basis: ${basis})`)
    }
  }
  return lines.length > 0 ? lines : ['None recorded (basis: DISC-ACT)']
}

function issuanceLines(discipline: DisciplineDetail, period: ReportPeriod | null): string[] {
  if (!period) return ['None recorded (basis: DISC-ISSUED; no period declared)']
  const rows = discipline.sections?.issuances?.rows ?? []
  if (rows.length === 0) return ['None recorded (basis: DISC-ISSUED)']
  return rows.map((r) =>
    `- ${r.ref}${r.docNo ? ` / ${r.docNo}` : ''}; ${r.issuedAt?.slice(0, 10) ?? 'date recorded'}; ${r.purpose ?? 'purpose recorded'} (basis: DISC-ISSUED)`)
}

function packageLines(pkg: PackageDetail, kind: 'issues' | 'decisions' | 'interfaces'): string[] {
  const code = pkg.package?.code ?? 'package'
  if (kind === 'issues') {
    const rows = (pkg.issues ?? []).filter((i) => i.type === 'hold' || i.type === 'risk' || i.type === 'action')
    return rows.length > 0
      ? rows.map((i) => `- ${code}: ${i.ref} ${text(i.title)}; ${i.detail ?? i.type}; ${i.state ?? 'state recorded'}${i.needBy ? `; need-by ${i.needBy}` : ''} (basis: PKG-ISSUE-MIX)`)
      : [`${code}: None recorded (basis: PKG-ISSUE-MIX)`]
  }
  if (kind === 'decisions') {
    const rows = pkg.decisions ?? []
    return rows.length > 0
      ? rows.map((d) => `- ${code}: ${d.ref} ${text(d.title)}; ${d.state ?? 'state recorded'}${d.needBy ? `; need-by ${d.needBy}` : ''} (basis: PKG-DEC)`)
      : [`${code}: None recorded (basis: PKG-DEC)`]
  }
  const rows = pkg.interfaces ?? []
  return rows.length > 0
    ? rows.map((i) => `- ${code}: ${i.ref} ${text(i.title)}; ${i.giving ?? '?'} -> ${i.receiving ?? '?'}; ${i.state ?? 'state recorded'}${i.needBy ? `; need-by ${i.needBy}` : ''} (basis: PKG-INT)`)
    : [`${code}: None recorded (basis: PKG-INT)`]
}

export function buildDisciplineStatusDocx(input: DraftDocxInput): DraftDocxResult {
  const docLines: Array<{ style: string | null; text: string }> = []
  const add = (style: string | null, line: string): void => {
    docLines.push({ style, text: line })
  }
  add('Title', `${input.project.code} Discipline Status Report Draft`)
  add(null, `Project: ${input.project.name} (basis: project record)`)
  add(null, input.period
    ? `Declared period: ${input.period.start} to ${input.period.end} (basis: sidecar prompt; PER-COV)`
    : 'Declared period: none. Period-scoped sections state absence honestly (basis: D-PEC-39).')
  add(null, `Generated: ${input.generatedAt}`)
  add(null, `Composition clarification: ${input.compositionClarification}`)

  let inWorkDeliverables = 0
  let issuancesThisPeriod: number | null = input.period ? 0 : null
  for (const discipline of input.disciplines) {
    add('Heading1', discipline.discipline)
    add('Subtitle', 'Activities')
    for (const line of activityLines(discipline)) {
      if (line.startsWith('- ')) inWorkDeliverables += 1
      add(line.startsWith('- ') ? 'ListParagraph' : null, line)
    }
    const pctBand = discipline.band?.percentComplete
    if (pctBand) add(null, `Discipline % complete: ${pctBand.value}% (basis: ${pctBand.ruleId})`)
    else add(null, 'Discipline % complete: None recorded (basis: DISC-PCT)')

    add('Subtitle', 'Issuances this period')
    const issued = issuanceLines(discipline, input.period)
    if (input.period) issuancesThisPeriod! += issued.filter((l) => l.startsWith('- ')).length
    for (const line of issued) add(line.startsWith('- ') ? 'ListParagraph' : null, line)
  }

  add('Heading1', 'By Package')
  add('Subtitle', 'Needs & Issues')
  const issuePackages = input.packageDetails.filter((p) => (p.summary?.openIssues ?? 0) > 0)
  const issueLines = issuePackages.flatMap((p) => packageLines(p, 'issues'))
  for (const line of issueLines.length > 0 ? issueLines : ['None recorded (basis: PKG-ISSUE-MIX)']) {
    add(line.startsWith('- ') ? 'ListParagraph' : null, line)
  }
  add('Subtitle', 'Decisions')
  const decisionPackages = input.packageDetails.filter((p) => (p.summary?.openDecisions ?? 0) > 0)
  const decisionLines = decisionPackages.flatMap((p) => packageLines(p, 'decisions'))
  for (const line of decisionLines.length > 0 ? decisionLines : ['None recorded (basis: PKG-DEC)']) {
    add(line.startsWith('- ') ? 'ListParagraph' : null, line)
  }
  add('Subtitle', 'Interfaces')
  const interfacePackages = input.packageDetails.filter((p) => (p.summary?.openInterfaces ?? 0) > 0)
  const interfaceLines = interfacePackages.flatMap((p) => packageLines(p, 'interfaces'))
  for (const line of interfaceLines.length > 0 ? interfaceLines : ['None recorded (basis: PKG-INT)']) {
    add(line.startsWith('- ') ? 'ListParagraph' : null, line)
  }

  const documentXml = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    ${docLines.map((l) => para(l.style, l.text)).join('\n    ')}
    <w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>
  </w:body>
</w:document>`
  const bytes = buildZip([
    { name: '[Content_Types].xml', data: CONTENT_TYPES },
    { name: '_rels/.rels', data: ROOT_RELS },
    { name: 'word/_rels/document.xml.rels', data: DOC_RELS },
    { name: 'word/document.xml', data: documentXml },
    { name: 'word/styles.xml', data: STYLES },
  ])
  const safePeriod = input.period ? `${input.period.start}_to_${input.period.end}` : 'no-period'
  const filename = `${input.project.code}-discipline-status-${safePeriod}.docx`
  const packageIssueRows = issuePackages.reduce((sum, p) =>
    sum + (p.issues ?? []).filter((i) => i.type === 'hold' || i.type === 'risk' || i.type === 'action').length, 0)
  return {
    filename,
    documentXml,
    documentText: docLines.map((l) => l.text).join('\n'),
    bytes,
    figures: {
      disciplines: input.disciplines.length,
      inWorkDeliverables,
      issuancesThisPeriod,
      packageIssueRows,
      packageDecisionRows: decisionPackages.reduce((sum, p) => sum + (p.decisions?.length ?? 0), 0),
      packageInterfaceRows: interfacePackages.reduce((sum, p) => sum + (p.interfaces?.length ?? 0), 0),
    },
  }
}

export function parseDeclaredPeriod(message: string): ReportPeriod | null {
  const m = /\b(?:period|covering|coverage|from)\s+(\d{4}-\d{2}-\d{2})\s*(?:\.\.|to|through|-)\s*(\d{4}-\d{2}-\d{2})\b/i.exec(message)
  if (!m) return null
  return { start: m[1]!, end: m[2]! }
}

export async function writeDraftDocx(outDir: string, draft: DraftDocxResult): Promise<string> {
  await mkdir(outDir, { recursive: true })
  const path = join(outDir, draft.filename)
  await writeFile(path, draft.bytes)
  return path
}
