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
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
  <Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>
  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
</Types>`

const ROOT_RELS = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>`

const DOC_RELS = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>
  <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
</Relationships>`

const STYLES = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Aptos" w:hAnsi="Aptos"/><w:sz w:val="21"/><w:color w:val="262626"/></w:rPr></w:rPrDefault></w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="0" w:after="180"/></w:pPr><w:rPr><w:b/><w:color w:val="0F4761"/><w:sz w:val="40"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:keepNext/><w:pPr><w:spacing w:before="260" w:after="100"/></w:pPr><w:rPr><w:b/><w:color w:val="0F4761"/><w:sz w:val="30"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/><w:keepNext/><w:pPr><w:spacing w:before="140" w:after="70"/></w:pPr><w:rPr><w:b/><w:color w:val="595959"/><w:sz w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/><w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr><w:ind w:left="540" w:hanging="270"/><w:spacing w:after="70"/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="BasisNote"><w:name w:val="Basis Note"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="100"/></w:pPr><w:rPr><w:i/><w:color w:val="737373"/><w:sz w:val="18"/></w:rPr></w:style>
</w:styles>`

const NUMBERING = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="singleLevel"/><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/><w:lvlJc w:val="left"/><w:pPr><w:tabs><w:tab w:val="num" w:pos="540"/></w:tabs><w:ind w:left="540" w:hanging="270"/></w:pPr><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/></w:rPr></w:lvl></w:abstractNum>
  <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>`

const HEADER = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:pPr><w:jc w:val="right"/></w:pPr><w:r><w:rPr><w:color w:val="737373"/><w:sz w:val="18"/></w:rPr><w:t>Weekly Status Update</w:t></w:r></w:p></w:hdr>`

const FOOTER = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:color w:val="737373"/><w:sz w:val="18"/></w:rPr><w:t xml:space="preserve">Page </w:t></w:r><w:fldSimple w:instr="PAGE"><w:r><w:rPr><w:color w:val="737373"/><w:sz w:val="18"/></w:rPr><w:t>1</w:t></w:r></w:fldSimple><w:r><w:rPr><w:color w:val="737373"/><w:sz w:val="18"/></w:rPr><w:t xml:space="preserve"> of </w:t></w:r><w:fldSimple w:instr="NUMPAGES"><w:r><w:rPr><w:color w:val="737373"/><w:sz w:val="18"/></w:rPr><w:t>1</w:t></w:r></w:fldSimple></w:p></w:ftr>`

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

function hasMeaningfulProgress(d: { percentComplete?: number | null; percentCompleteVerbatim?: string | null }): boolean {
  if (d.percentComplete != null) return d.percentComplete > 0
  const marker = text(d.percentCompleteVerbatim).toLowerCase()
  return marker !== '' && marker !== '0' && marker !== '0%' && marker !== 'n/a' && marker !== '-'
}

function activityLines(discipline: DisciplineDetail): { lines: string[]; count: number; omitted: number } {
  const groups = discipline.sections?.activities?.groups ?? []
  const lines: string[] = []
  let count = 0
  let omitted = 0
  for (const group of groups) {
    const deliverables = (group.deliverables ?? []).filter(hasMeaningfulProgress)
    if (deliverables.length === 0) continue
    count += deliverables.length
    const byProgress = new Map<string, number>()
    for (const d of deliverables) byProgress.set(pct(d), (byProgress.get(pct(d)) ?? 0) + 1)
    const distribution = [...byProgress.entries()].map(([value, n]) => `${n} at ${value}`).join('; ')
    const examples = deliverables.slice(0, 4).map((d) => `${d.docNo} — ${text(d.title)}`).join('; ')
    const remaining = Math.max(0, deliverables.length - 4)
    omitted += remaining
    lines.push(`${group.type}: ${deliverables.length} active (${distribution}). ${examples}${remaining ? `; plus ${remaining} other${remaining === 1 ? '' : 's'}` : ''}.`)
  }
  return { lines: lines.length > 0 ? lines : ['No attested progress recorded.'], count, omitted }
}

function issuanceLines(discipline: DisciplineDetail, period: ReportPeriod | null): string[] {
  if (!period) return ['None recorded (basis: DISC-ISSUED; no period declared)']
  const rows = discipline.sections?.issuances?.rows ?? []
  if (rows.length === 0) return ['None recorded (basis: DISC-ISSUED)']
  return rows.map((r) =>
    `- ${r.ref}${r.docNo ? ` / ${r.docNo}` : ''}; ${r.issuedAt?.slice(0, 10) ?? 'date recorded'}; ${r.purpose ?? 'purpose recorded'} (basis: DISC-ISSUED)`)
}

function consolidatedPackageLines(packages: PackageDetail[], kind: 'issues' | 'decisions' | 'interfaces'): string[] {
  const grouped = new Map<string, { description: string; packages: string[]; refs: string[] }>()
  for (const pkg of packages) {
    const code = pkg.package?.code ?? 'package'
    const rows = kind === 'issues'
      ? (pkg.issues ?? []).filter((i) => i.type === 'hold' || i.type === 'risk' || i.type === 'action')
      : kind === 'decisions' ? (pkg.decisions ?? []) : (pkg.interfaces ?? [])
    for (const row of rows) {
      const issue = row as PackageIssue
      const decision = row as { ref: string; title: string; state?: string; needBy?: string | null }
      const iface = row as { ref: string; title: string; state?: string; giving?: string; receiving?: string; needBy?: string | null }
      const detail = kind === 'issues' ? (issue.detail ?? issue.type)
        : kind === 'interfaces' ? `${iface.giving ?? '?'} → ${iface.receiving ?? '?'}` : ''
      const description = `${text(row.title)}${detail ? ` — ${detail}` : ''}; ${row.state ?? 'state recorded'}${row.needBy ? `; need-by ${row.needBy}` : ''}`
      const key = `${kind}|${description.toLowerCase()}`
      const current = grouped.get(key) ?? { description, packages: [], refs: [] }
      if (!current.packages.includes(code)) current.packages.push(code)
      current.refs.push(decision.ref)
      grouped.set(key, current)
    }
  }
  return [...grouped.values()].map((g) => {
    const packageLabel = g.packages.length <= 4 ? g.packages.join(', ') : `${g.packages.slice(0, 4).join(', ')} +${g.packages.length - 4} others`
    const refLabel = g.refs.length === 1 ? g.refs[0] : `${g.refs.length} records`
    return `${packageLabel}: ${refLabel} — ${g.description}`
  })
}

export function buildDisciplineStatusDocx(input: DraftDocxInput): DraftDocxResult {
  const docLines: Array<{ style: string | null; text: string }> = []
  const add = (style: string | null, line: string): void => {
    docLines.push({ style, text: line })
  }
  add('Title', `${input.project.code} Weekly Status Update`)
  add('Subtitle', input.project.name)
  add(null, input.period
    ? `Reporting period: ${input.period.start} to ${input.period.end}`
    : 'Reporting period: not declared; period-scoped figures are shown as unavailable.')
  add('BasisNote', 'Prepared from the live PEC records. Deliverable status and attested progress are reported by discipline; needs, issues, decisions, and interfaces are reported by package.')

  let inWorkDeliverables = 0
  let issuancesThisPeriod: number | null = input.period ? 0 : null
  for (const discipline of input.disciplines) {
    add('Heading1', discipline.discipline)
    const pctBand = discipline.band?.percentComplete
    add(null, pctBand
      ? `Attested discipline progress: ${pctBand.value}%`
      : 'Attested discipline progress: unavailable')
    add('Subtitle', 'Activities')
    const activities = activityLines(discipline)
    inWorkDeliverables += activities.count
    for (const line of activities.lines) add(line === 'No attested progress recorded.' ? null : 'ListParagraph', line)

    add('Subtitle', 'Issuances this period')
    const issued = issuanceLines(discipline, input.period)
    if (input.period) issuancesThisPeriod! += issued.filter((l) => l.startsWith('- ')).length
    for (const line of issued.slice(0, 8)) add(line.startsWith('- ') ? 'ListParagraph' : null, line.replace(/^- /, '').replace(/ \(basis: DISC-ISSUED.*\)$/, ''))
    if (issued.length > 8) add('BasisNote', `${issued.length - 8} additional issuance records are available in PEC.`)
  }

  add('Heading1', 'By Package')
  add('Subtitle', 'Needs & Issues')
  const issuePackages = input.packageDetails.filter((p) => (p.summary?.openIssues ?? 0) > 0)
  const issueLines = consolidatedPackageLines(issuePackages, 'issues')
  for (const line of issueLines.length > 0 ? issueLines : ['None recorded.']) {
    add(line === 'None recorded.' ? null : 'ListParagraph', line)
  }
  add('Subtitle', 'Decisions')
  const decisionPackages = input.packageDetails.filter((p) => (p.summary?.openDecisions ?? 0) > 0)
  const decisionLines = consolidatedPackageLines(decisionPackages, 'decisions')
  for (const line of decisionLines.length > 0 ? decisionLines : ['None recorded.']) {
    add(line === 'None recorded.' ? null : 'ListParagraph', line)
  }
  add('Subtitle', 'Interfaces')
  const interfacePackages = input.packageDetails.filter((p) => (p.summary?.openInterfaces ?? 0) > 0)
  const interfaceLines = consolidatedPackageLines(interfacePackages, 'interfaces')
  for (const line of interfaceLines.length > 0 ? interfaceLines : ['None recorded.']) {
    add(line === 'None recorded.' ? null : 'ListParagraph', line)
  }

  const documentXml = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    ${docLines.map((l) => para(l.style, l.text)).join('\n    ')}
    <w:sectPr><w:headerReference w:type="default" r:id="rId3"/><w:footerReference w:type="default" r:id="rId4"/><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080" w:header="540" w:footer="540"/></w:sectPr>
  </w:body>
</w:document>`.replace('<w:document ', '<w:document xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" ')
  const bytes = buildZip([
    { name: '[Content_Types].xml', data: CONTENT_TYPES },
    { name: '_rels/.rels', data: ROOT_RELS },
    { name: 'word/_rels/document.xml.rels', data: DOC_RELS },
    { name: 'word/document.xml', data: documentXml },
    { name: 'word/styles.xml', data: STYLES },
    { name: 'word/numbering.xml', data: NUMBERING },
    { name: 'word/header1.xml', data: HEADER },
    { name: 'word/footer1.xml', data: FOOTER },
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
