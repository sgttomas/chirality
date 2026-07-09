import { CONTRACTS } from './contract-detect.ts'
import type { Contract } from './contract-detect.ts'

export interface MappingSummary {
  sourceFormat: string
  sourceHeaders: string[]
  canonicalHeaders: string[]
  contract: Contract
  rowCount: number
  omittedSourceHeaders: string[]
  requiredEmptyRows: Array<{ row: number; column: string }>
  notes: string[]
}

export type StructuredFileResult =
  | { ok: true; csv: string; contract: Contract; filename?: string; summary: MappingSummary }
  | { ok: false; reason: string; summary?: { sourceFormat: string; sourceHeaders: string[]; canonicalHeaders: string[] } }

const REQUIRED: Record<Contract, string[]> = {
  mdl: ['doc_no', 'title', 'package', 'discipline', 'owner', 'current_rev', 'state', 'due_date'],
  rail: ['item_id', 'statement', 'type', 'log', 'owner', 'need_by', 'status', 'raised_by', 'raised_date'],
  decisions: ['decision_id', 'title', 'statement', 'authority', 'need_by', 'status'],
  risks: ['risk_id', 'title', 'cause', 'consequence', 'owner', 'status'],
  schedule: ['activity_id', 'description', 'start', 'finish'],
  tracker: [
    'tracking_no', 'package_name', 'discipline', 'area',
    'stage_budgetary_datasheet', 'stage_cost_estimate', 'stage_package_datasheet',
    'stage_package', 'stage_rfq', 'stage_review', 'stage_vendor_bids',
    'stage_clarifications', 'stage_evaluation', 'stage_eng_req', 'stage_po',
    'stage_databook', 'package',
  ],
}

const OPTIONAL: Record<Contract, string[]> = {
  mdl: [
    'deliverable_type', 'milestone', 'issue_purpose_plan', 'edms_ref', 'client_no',
    'remarks', 'package_name', 'area', 'package_type',
  ],
  rail: ['item_id', 'deliverable_ref', 'hold_cause', 'area'],
  decisions: ['deliverable_ref', 'open_date', 'area', 'source'],
  risks: [
    'deliverable_ref', 'probability', 'impact', 'mitigation', 'need_by', 'category',
    'risk_type', 'treatment', 'residual_probability', 'residual_impact',
  ],
  schedule: [
    'package', 'deliverable_ref', 'row_type', 'outline_level', 'parent_activity_id',
    'percent_complete', 'duration_days', 'baseline_start', 'baseline_finish',
  ],
  tracker: ['vendors_engaged', 'vendor_awarded', 'expected_delivery_date', 'comments'],
}

const HEADER_ALIASES: Record<string, string> = {
  docno: 'doc_no',
  document_no: 'doc_no',
  document_number: 'doc_no',
  current_revision: 'current_rev',
  revision: 'current_rev',
  rev: 'current_rev',
  due: 'due_date',
  due_date: 'due_date',
  needby: 'need_by',
  need_by_date: 'need_by',
  itemid: 'item_id',
  decisionid: 'decision_id',
  riskid: 'risk_id',
  activityid: 'activity_id',
  trackingno: 'tracking_no',
  coa_no: 'tracking_no',
  coa_number: 'tracking_no',
  package_no: 'package',
  package_code: 'package',
  current_status: 'status',
  raisedby: 'raised_by',
  raiseddate: 'raised_date',
  open: 'open_date',
  opened: 'open_date',
  baseline_start_date: 'baseline_start',
  baseline_finish_date: 'baseline_finish',
  percent_done: 'percent_complete',
  pct_complete: 'percent_complete',
  duration: 'duration_days',
}

function canonicalHeader(raw: string): string {
  const normalized = raw.trim().replace(/^\uFEFF/, '').toLowerCase()
    .replace(/&/g, ' and ')
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '')
  return HEADER_ALIASES[normalized] ?? normalized
}

function splitLine(line: string, delimiter: string | RegExp): string[] {
  if (delimiter instanceof RegExp) return line.trim().split(delimiter)
  const cells: string[] = []
  let cur = ''
  let inQuotes = false
  for (let i = 0; i < line.length; i++) {
    const ch = line[i]!
    if (inQuotes) {
      if (ch === '"' && line[i + 1] === '"') { cur += '"'; i++ }
      else if (ch === '"') inQuotes = false
      else cur += ch
    } else if (ch === '"') inQuotes = true
    else if (ch === delimiter) { cells.push(cur); cur = '' }
    else cur += ch
  }
  cells.push(cur)
  return cells.map((c) => c.trim())
}

function chooseDelimiter(header: string): { delimiter: string | RegExp; format: string } {
  const candidates: Array<[string, string]> = [[',', 'csv'], ['\t', 'tsv'], ['|', 'pipe'], [';', 'semicolon']]
  let best = candidates[0]!
  let bestCount = 0
  for (const candidate of candidates) {
    const count = splitLine(header, candidate[0]).length
    if (count > bestCount) { best = candidate; bestCount = count }
  }
  if (bestCount <= 1 && /\S\s{2,}\S/.test(header)) return { delimiter: /\s{2,}/, format: 'fixed-gap text' }
  return { delimiter: best[0], format: best[1] }
}

function csvEscape(v: string): string {
  return /[",\r\n]/.test(v) ? `"${v.replaceAll('"', '""')}"` : v
}

function contractMatches(headers: Set<string>): Contract[] {
  return CONTRACTS.filter((contract) => REQUIRED[contract].every((h) => headers.has(h)))
}

function nearestContracts(headers: Set<string>): string {
  return CONTRACTS.map((contract) => {
    const missing = REQUIRED[contract].filter((h) => !headers.has(h))
    return `${contract}: missing ${missing.length === 0 ? 'none' : missing.join(', ')}`
  }).join('; ')
}

export function adaptStructuredFile(
  text: string,
  opts: { filename?: string; contract?: string } = {},
): StructuredFileResult {
  const rawLines = text.replace(/\r\n/g, '\n').replace(/\r/g, '\n').split('\n')
  const lines = rawLines.filter((line) => line.trim().length > 0)
  if (lines.length < 2) return { ok: false, reason: 'structured file needs a header row and at least one data row' }
  const { delimiter, format } = chooseDelimiter(lines[0]!)
  const sourceHeaders = splitLine(lines[0]!, delimiter)
  const canonicalHeaders = sourceHeaders.map(canonicalHeader)
  const headerSet = new Set(canonicalHeaders)
  let contract: Contract | undefined
  if (opts.contract) {
    const named = opts.contract.toLowerCase()
    if (!(CONTRACTS as readonly string[]).includes(named)) {
      return { ok: false, reason: `unknown contract '${opts.contract}' (one of: ${CONTRACTS.join(', ')})` }
    }
    contract = named as Contract
  } else {
    const matches = contractMatches(headerSet)
    if (matches.length === 1) contract = matches[0]!
    else if (matches.length > 1) {
      return { ok: false, reason: `the structured-file headers match more than one contract (${matches.join(', ')}) — name the contract` }
    } else {
      return {
        ok: false,
        reason: `the structured-file headers match no import contract — ${nearestContracts(headerSet)}`,
        summary: { sourceFormat: format, sourceHeaders, canonicalHeaders },
      }
    }
  }
  const missing = REQUIRED[contract].filter((h) => !headerSet.has(h))
  if (missing.length > 0) {
    return {
      ok: false,
      reason: `${contract} mapping is missing required columns: ${missing.join(', ')} — ask the owner for these fields or name a different contract`,
      summary: { sourceFormat: format, sourceHeaders, canonicalHeaders },
    }
  }
  const rows = lines.slice(1).map((line) => splitLine(line, delimiter))
  const normalizedRows = rows.map((row) => canonicalHeaders.map((_, i) => row[i] ?? ''))
  const requiredEmptyRows: Array<{ row: number; column: string }> = []
  for (const [idx, row] of normalizedRows.entries()) {
    for (const col of REQUIRED[contract]) {
      const pos = canonicalHeaders.indexOf(col)
      if (pos >= 0 && !row[pos]?.trim()) requiredEmptyRows.push({ row: idx + 2, column: col })
    }
  }
  const recognized = new Set([...REQUIRED[contract], ...OPTIONAL[contract]])
  const omittedSourceHeaders = canonicalHeaders.filter((h) => !recognized.has(h))
  const csv = [
    canonicalHeaders.map(csvEscape).join(','),
    ...normalizedRows.map((row) => row.map(csvEscape).join(',')),
  ].join('\r\n')
  const filename = opts.filename ? opts.filename.replace(/\.[^.]+$/, '.csv') : undefined
  return {
    ok: true,
    csv,
    contract,
    filename,
    summary: {
      sourceFormat: format,
      sourceHeaders,
      canonicalHeaders,
      contract,
      rowCount: normalizedRows.length,
      omittedSourceHeaders,
      requiredEmptyRows,
      notes: [
        'accept/apply remain human Admin acts',
        requiredEmptyRows.length > 0
          ? 'rows with empty required cells are left for the server dry-run to reject with row numbers'
          : 'all required cells are non-empty at mapping time',
      ],
    },
  }
}

export function mappingSummaryText(summary: MappingSummary): string {
  const omitted = summary.omittedSourceHeaders.length > 0
    ? `omitted source columns: ${summary.omittedSourceHeaders.join(', ')}`
    : 'no source columns omitted'
  const empty = summary.requiredEmptyRows.length > 0
    ? `${summary.requiredEmptyRows.length} required-cell gap(s) will dry-run as rejects`
    : 'no required-cell gaps found before dry-run'
  return `mapping: ${summary.sourceFormat} → ${summary.contract} CSV; ${summary.rowCount} row(s); ${omitted}; ${empty}`
}
