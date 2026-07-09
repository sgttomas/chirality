/**
 * CSV header → §16 import-contract detection (D-PEC-17). Header fingerprints
 * are sourced from the live required-column lists in
 * `server/src/import/index.ts` (importMdl/importRail/importDecisions/
 * importRisks/importSchedule) at authoring time — that file is the source of
 * truth; if it drifts, detection degrades to asking the user (never mis-files:
 * a mis-declared contract additionally fails the server's own contract
 * validation into `draft` state with the error recorded).
 */

export const CONTRACTS = ['mdl', 'rail', 'decisions', 'risks', 'schedule', 'tracker'] as const
export type Contract = (typeof CONTRACTS)[number]

/**
 * Required-column subsets sufficient to distinguish the five contracts
 * (each contract's key column + one contract-specific companion).
 * Source: server/src/import/index.ts required-column arrays (2026-07-06).
 */
const FINGERPRINTS: Record<Contract, string[]> = {
  mdl: ['doc_no', 'current_rev'],
  rail: ['item_id', 'statement', 'raised_by'],
  decisions: ['decision_id', 'authority'],
  risks: ['risk_id', 'consequence'],
  schedule: ['activity_id', 'start', 'finish'],
  tracker: ['tracking_no', 'package_name', 'package'],
}

export type Detection =
  | { contract: Contract }
  | { ambiguous: Contract[] }
  | { unknown: true }

/** Parse the CSV header row (RFC 4180 quoting) into lowercase column names. */
function headerColumns(csv: string): string[] {
  const line = csv.split(/\r?\n/, 1)[0] ?? ''
  const cols: string[] = []
  let cur = ''
  let inQuotes = false
  for (let i = 0; i < line.length; i++) {
    const ch = line[i]!
    if (inQuotes) {
      if (ch === '"' && line[i + 1] === '"') { cur += '"'; i++ }
      else if (ch === '"') inQuotes = false
      else cur += ch
    } else if (ch === '"') inQuotes = true
    else if (ch === ',') { cols.push(cur); cur = '' }
    else cur += ch
  }
  cols.push(cur)
  return cols.map((c) => c.trim().toLowerCase()).filter(Boolean)
}

export function detectContract(csv: string): Detection {
  const headers = new Set(headerColumns(csv))
  const matches = CONTRACTS.filter((c) => FINGERPRINTS[c].every((col) => headers.has(col)))
  if (matches.length === 1) return { contract: matches[0]! }
  if (matches.length > 1) return { ambiguous: matches }
  return { unknown: true }
}
