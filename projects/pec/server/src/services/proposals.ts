/**
 * Import proposals (D-PEC-08): the §16 import contracts behind a propose → human
 * accept → apply gate, per the profile operation_proposal_contract lifecycle
 * (draft → ready_for_review → accepted → rejected/applied).
 *
 * The agent (or any register-handling role) proposes; a human with import authority
 * accepts — hash- and version-bound (RV-13) — and applies. The dry-run executes the
 * real importContract inside a savepoint that is rolled back, so the preview is the
 * live contract's own answer, never a reimplementation. Apply runs the import and
 * the lifecycle change in ONE transaction: a mid-apply throw rolls back both (RV-17).
 * The proposal pathway NEVER auto-applies.
 */

import { createHash } from 'node:crypto'
import { AppError, badRequest } from '../errors.ts'
import { nowIso } from '../repo.ts'
import type { Sx } from './shared.ts'
import { requireCan } from './shared.ts'
import type { ImportReport } from '../import/index.ts'
import { importContract } from '../import/index.ts'

const CONTRACTS = ['mdl', 'rail', 'decisions', 'risks', 'schedule', 'tracker'] as const
/** RV-14: CSV-only v1, size-capped well under the global body cap. */
const MAX_CSV_BYTES = 5 * 1024 * 1024

export interface ImportProposal {
  id: number
  projectId: number
  ref: string
  contract: string
  sourceName: string | null
  sourceSha256: string
  sourceBytes: number
  sourceCsv: string
  coverageStart: string | null
  coverageEnd: string | null
  /** D-PEC-41 full-fidelity capture: verbatim non-tabular source sheets/metadata (JSON) */
  sourceExtras: Record<string, unknown> | null
  state: 'draft' | 'ready_for_review' | 'accepted' | 'rejected' | 'applied'
  basisHistoryId: number | null
  dryRunReport: ImportReport | { error: string } | null
  dryRunAt: string | null
  acceptedBy: number | null
  acceptedAt: string | null
  acceptedSha256: string | null
  rejectedBy: number | null
  rejectedAt: string | null
  rejectReason: string | null
  appliedBy: number | null
  appliedAt: string | null
  applyReport: ImportReport | null
  createdBy: number
  createdAt: string
  version: number
}

const staleProposal = (details: unknown) => new AppError(409, 'STALE_PROPOSAL',
  'the project changed since this proposal\'s dry-run; refresh the dry-run and re-review (RV-13)', details)

function sha256(text: string): string {
  return createHash('sha256').update(text, 'utf8').digest('hex')
}

/** Project history watermark, excluding proposal bookkeeping itself (RV-13/RV-17). */
function watermark(sx: Sx): number {
  const row = sx.db.prepare(
    "SELECT COALESCE(MAX(id), 0) AS w FROM history_entry WHERE project_id = ? AND record_type != 'import_proposal'",
  ).get(sx.projectId) as { w: number }
  return row.w
}

function history(sx: Sx, id: number, kind: string, summary: string): void {
  sx.repo.history({
    projectId: sx.projectId, recordType: 'import_proposal', recordId: id,
    actorId: sx.session.personId, kind, summary, payload: null, authorityRef: null,
  })
}

/** Run the real import contract against a savepoint and roll it back (dry-run). */
function dryRun(sx: Sx, contract: string, csv: string): ImportReport {
  sx.db.exec('SAVEPOINT proposal_dry_run')
  try {
    return importContract(sx, contract, csv, false)
  } finally {
    sx.db.exec('ROLLBACK TO proposal_dry_run')
    sx.db.exec('RELEASE proposal_dry_run')
  }
}

const COVERAGE_DATE_RE = /^\d{4}-\d{2}-\d{2}$/

/**
 * D-PEC-39: coverage is DECLARED by the PE per uploaded document, never inferred.
 * Validation is shape-only (two well-formed, ordered dates); overlaps, gaps, and
 * retroactive corrections are review signals caught downstream (services/periods.ts),
 * never schema-prevented — retro-corrections are a normal part of the PE workflow.
 */
export interface CoverageDeclarationInput {
  start?: string | null
  end?: string | null
}

function validateCoverage(coverage: CoverageDeclarationInput | undefined): { start: string | null; end: string | null } {
  const start = coverage?.start || null
  const end = coverage?.end || null
  if (start == null && end == null) return { start: null, end: null }
  if (start == null || end == null) {
    throw badRequest('coverage declaration requires both coverage_start and coverage_end (D-PEC-39)')
  }
  for (const [name, v] of [['coverage_start', start], ['coverage_end', end]] as const) {
    if (!COVERAGE_DATE_RE.test(v)) throw badRequest(`${name} must be YYYY-MM-DD, got "${v}"`)
  }
  if (end < start) throw badRequest(`coverage_end ${end} is before coverage_start ${start}`)
  return { start, end }
}

export function createProposal(sx: Sx, contract: string, csv: string, sourceName: string | null,
  coverage?: CoverageDeclarationInput, extras?: Record<string, unknown> | null): ImportProposal {
  requireCan(sx, 'import.propose', {})
  if (!(CONTRACTS as readonly string[]).includes(contract)) {
    throw badRequest(`unknown import contract: ${contract} (${CONTRACTS.join(', ')})`)
  }
  if (!csv.trim()) throw badRequest('CSV body required')
  const bytes = Buffer.byteLength(csv, 'utf8')
  if (bytes > MAX_CSV_BYTES) throw badRequest(`CSV exceeds the ${MAX_CSV_BYTES / 1024 / 1024} MiB proposal cap (RV-14)`)
  // D-PEC-41: verbatim capture of non-tabular source content (workbook sheets/metadata) —
  // stored against the proposal, size-capped like the CSV; display stays selective.
  const extrasJson = extras && Object.keys(extras).length > 0 ? extras : null
  if (extrasJson != null && Buffer.byteLength(JSON.stringify(extrasJson), 'utf8') > MAX_CSV_BYTES) {
    throw badRequest(`source extras exceed the ${MAX_CSV_BYTES / 1024 / 1024} MiB proposal cap (RV-14)`)
  }
  const cov = validateCoverage(coverage)

  const ref = sx.repo.nextRef(sx.projectId, 'import_proposal')
  const id = sx.repo.insert('import_proposal', {
    projectId: sx.projectId, ref, contract,
    sourceName, sourceSha256: sha256(csv), sourceBytes: bytes, sourceCsv: csv,
    coverageStart: cov.start, coverageEnd: cov.end, sourceExtras: extrasJson,
    state: 'draft', createdBy: sx.session.personId, createdAt: nowIso(),
  })
  history(sx, id, 'created', `${ref} proposed (${contract}, ${bytes} bytes, sha256 ${sha256(csv).slice(0, 12)}…, `
    + `${cov.start ? `coverage ${cov.start}..${cov.end}` : 'no coverage declared'})`)

  // Dry-run immediately; a non-contract-shaped CSV keeps the proposal in draft with the
  // error recorded — never silently dropped (§16 posture).
  refreshDryRunInternal(sx, id, ref, contract, csv)
  return getProposal(sx, id)
}

function refreshDryRunInternal(sx: Sx, id: number, ref: string, contract: string, csv: string): void {
  let report: ImportReport | { error: string }
  let ok = true
  try {
    report = dryRun(sx, contract, csv)
  } catch (e) {
    ok = false
    report = { error: e instanceof Error ? e.message : String(e) }
  }
  sx.repo.systemUpdate('import_proposal', sx.projectId, id, {
    state: ok ? 'ready_for_review' : 'draft',
    dryRunReport: report, dryRunAt: nowIso(), basisHistoryId: watermark(sx),
    // a refreshed dry-run voids any prior acceptance (RV-13): re-review from the new basis
    acceptedBy: null, acceptedAt: null, acceptedSha256: null,
  })
  history(sx, id, 'proposal_dry_run', ok
    ? `${ref} dry-run computed (${(report as ImportReport).accepted} would create, ${(report as ImportReport).updated} would update, ${(report as ImportReport).conflicts.length} conflicts, ${(report as ImportReport).rejected.length} rejected, ${(report as ImportReport).intakeCreated} to intake)`
    : `${ref} dry-run failed: ${(report as { error: string }).error}`)
}

export function refreshDryRun(sx: Sx, id: number, expectedVersion: number): ImportProposal {
  requireCan(sx, 'import.propose', {})
  const p = getProposal(sx, id)
  if (p.state === 'rejected' || p.state === 'applied') {
    throw badRequest(`proposal ${p.ref} is ${p.state}; terminal states cannot be refreshed`)
  }
  // burn the caller's version first so a concurrent edit surfaces as 409 (PEC-NFR-004)
  sx.repo.update('import_proposal', sx.projectId, id, expectedVersion, { dryRunAt: nowIso() })
  refreshDryRunInternal(sx, id, p.ref, p.contract, p.sourceCsv)
  return getProposal(sx, id)
}

export function acceptProposal(sx: Sx, id: number, expectedVersion: number, echoedSha256: string): ImportProposal {
  requireCan(sx, 'import.accept', {})
  const p = getProposal(sx, id)
  if (p.state !== 'ready_for_review') throw badRequest(`proposal ${p.ref} is ${p.state}; only ready_for_review proposals can be accepted`)
  // RV-13: acceptance is bound to the exact content the human reviewed
  if (echoedSha256 !== p.sourceSha256) {
    throw badRequest(`sha256 mismatch: acceptance must echo the proposal's source hash (RV-13)`,
      { expected: p.sourceSha256 })
  }
  const w = watermark(sx)
  if (p.basisHistoryId !== w) throw staleProposal({ basisHistoryId: p.basisHistoryId, currentWatermark: w })
  sx.repo.update('import_proposal', sx.projectId, id, expectedVersion, {
    state: 'accepted', acceptedBy: sx.session.personId, acceptedAt: nowIso(), acceptedSha256: echoedSha256,
  })
  history(sx, id, 'proposal_accepted', `${p.ref} accepted by ${sx.session.email} (sha256 ${echoedSha256.slice(0, 12)}…)`)
  sx.repo.audit({
    projectId: sx.projectId, actorId: sx.session.personId, action: 'import_proposal_accept',
    recordType: 'import_proposal', recordId: id,
    newValue: { ref: p.ref, contract: p.contract, sourceSha256: p.sourceSha256 },
  })
  return getProposal(sx, id)
}

export function rejectProposal(sx: Sx, id: number, expectedVersion: number, reason: string): ImportProposal {
  const p = getProposal(sx, id)
  // proposers may withdraw their own; import authority may reject any (RV-16)
  if (p.createdBy === sx.session.personId) requireCan(sx, 'import.propose', {})
  else requireCan(sx, 'import.accept', {})
  if (p.state === 'rejected' || p.state === 'applied') throw badRequest(`proposal ${p.ref} is already ${p.state}`)
  if (!reason.trim()) throw badRequest('reject reason required')
  sx.repo.update('import_proposal', sx.projectId, id, expectedVersion, {
    state: 'rejected', rejectedBy: sx.session.personId, rejectedAt: nowIso(), rejectReason: reason,
  })
  history(sx, id, 'proposal_rejected', `${p.ref} rejected: ${reason}`)
  return getProposal(sx, id)
}

export function applyProposal(sx: Sx, id: number, expectedVersion: number, force: boolean): ImportProposal {
  requireCan(sx, 'import.accept', {})
  const p = getProposal(sx, id)
  if (p.state !== 'accepted') throw badRequest(`proposal ${p.ref} is ${p.state}; only accepted proposals can be applied`)
  const w = watermark(sx)
  if (p.basisHistoryId !== w) throw staleProposal({ basisHistoryId: p.basisHistoryId, currentWatermark: w })
  // Real import + lifecycle change in the SAME transaction (the route tx): a throw
  // anywhere rolls back both, so there is no half-applied state (RV-17).
  const report = importContract(sx, p.contract, p.sourceCsv, force)
  sx.repo.update('import_proposal', sx.projectId, id, expectedVersion, {
    state: 'applied', appliedBy: sx.session.personId, appliedAt: nowIso(), applyReport: report,
  })
  history(sx, id, 'proposal_applied', `${p.ref} applied (${report.accepted} created, ${report.updated} updated, ${report.conflicts.length} conflicts, ${report.rejected.length} rejected, ${report.intakeCreated} to intake)${force ? ' [force]' : ''}`)
  sx.repo.audit({
    projectId: sx.projectId, actorId: sx.session.personId, action: 'import_proposal_apply',
    recordType: 'import_proposal', recordId: id,
    newValue: { ref: p.ref, contract: p.contract, sourceSha256: p.sourceSha256, force, report: {
      accepted: report.accepted, updated: report.updated,
      conflicts: report.conflicts.length, rejected: report.rejected.length, intakeCreated: report.intakeCreated,
    } },
  })
  return getProposal(sx, id)
}

export function getProposal(sx: Sx, id: number): ImportProposal {
  requireCan(sx, 'import.propose', {}) // read side rides propose rights (RV-16/RV-19)
  return sx.repo.get<ImportProposal>('import_proposal', sx.projectId, id)
}

export function listProposals(sx: Sx): Array<Omit<ImportProposal, 'sourceCsv'>> {
  requireCan(sx, 'import.propose', {})
  return sx.repo.list<ImportProposal>('import_proposal', sx.projectId)
    .sort((a, b) => b.id - a.id)
    .map(({ sourceCsv: _csv, ...rest }) => rest)
}

/**
 * Same-origin guard for browser-reachable proposal mutations (RV-21): when an Origin
 * header is present its host must match the request Host. Cookie-less API clients and
 * same-origin fetches pass unchanged.
 */
export function requireSameOrigin(originHeader: string | undefined, hostHeader: string | undefined): void {
  if (originHeader == null || originHeader === '') return
  const refuse = () => new AppError(403, 'CROSS_ORIGIN', 'cross-origin request refused (RV-21)')
  if (originHeader === 'null') throw refuse()
  let originHost: string
  try { originHost = new URL(originHeader).host } catch { throw refuse() }
  if (!hostHeader || originHost !== hostHeader) throw refuse()
}
