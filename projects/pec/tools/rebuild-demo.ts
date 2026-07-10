/**
 * Rebuild the sponsor-demo database from date-prefixed XLSX inputs only.
 *
 * This deliberately uses the production workbook mapper and the governed
 * propose -> human accept -> apply services. Coverage is mandatory and is
 * supplied by the PE; this tool never infers it from filenames or mtime.
 */

import { copyFileSync, existsSync, mkdirSync, readdirSync, readFileSync, renameSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { basename, dirname, join, resolve, sep } from 'node:path'
import { DatabaseSync } from 'node:sqlite'
import type { Role } from '@pec/core'
import { parseXlsxWorkbook } from '../agent-sidecar/src/xlsx.ts'
import { adaptWorkbook } from '../agent-sidecar/src/structured-file.ts'
import { hashPassword } from '../server/src/auth.ts'
import { openDb, withTx } from '../server/src/db.ts'
import { parseTable } from '../server/src/import/csv.ts'
import { importContract } from '../server/src/import/index.ts'
import { Repo, nowIso } from '../server/src/repo.ts'
import { acceptProposal, applyProposal, createProposal } from '../server/src/services/proposals.ts'
import type { Sx } from '../server/src/services/shared.ts'

const rawDbPath = process.env.PEC_DB?.trim()
const inputDir = resolve(process.env.PEC_DEMO_INPUT_DIR?.trim() || join(import.meta.dirname, '..', 'pilot-scratch', 'input'))
const coverageStart = process.env.PEC_DEMO_COVERAGE_START?.trim()
const coverageEnd = process.env.PEC_DEMO_COVERAGE_END?.trim()

function pathIsInside(child: string, parent: string): boolean {
  const normalizedParent = parent.endsWith(sep) ? parent : `${parent}${sep}`
  return child === parent || child.startsWith(normalizedParent)
}

function requireDemoTarget(rawPath: string | undefined): string {
  if (!rawPath) throw new Error('PEC_DB is required; point it at a scratch/demo database.')
  const path = resolve(rawPath)
  const tempRoot = resolve(tmpdir())
  const hasDemoToken = path.split(/[\\/_.-]+/).some((part) => ['scratch', 'demo'].includes(part.toLowerCase()))
  if (!pathIsInside(path, tempRoot) && !hasDemoToken) {
    throw new Error(`Refusing to rebuild non-scratch/non-demo database target: ${path}`)
  }
  return path
}

function requireCoverage(): { start: string; end: string } {
  if (!coverageStart || !coverageEnd) {
    throw new Error('PEC_DEMO_COVERAGE_START and PEC_DEMO_COVERAGE_END are required; coverage is PE-declared and never inferred.')
  }
  if (!/^\d{4}-\d{2}-\d{2}$/.test(coverageStart) || !/^\d{4}-\d{2}-\d{2}$/.test(coverageEnd) || coverageEnd < coverageStart) {
    throw new Error('Demo coverage must be ordered YYYY-MM-DD dates.')
  }
  return { start: coverageStart, end: coverageEnd }
}

interface MappedInput {
  path: string
  filename: string
  contract: 'mdl' | 'rail'
  csv: string
  extras: Record<string, unknown>
}

function loadInputs(): MappedInput[] {
  const dated = readdirSync(inputDir)
    .filter((name) => /^\d{4}-\d{2}-\d{2}-.+\.xlsx$/i.test(name))
    .sort()
  if (dated.length === 0) throw new Error(`No date-prefixed .xlsx inputs found in ${inputDir}`)
  const mapped = dated.map((filename): MappedInput => {
    const path = join(inputDir, filename)
    const workbook = parseXlsxWorkbook(readFileSync(path))
    const result = adaptWorkbook(workbook, { filename })
    if (!result.ok) throw new Error(`${filename}: ${result.reason}`)
    if (result.contract !== 'mdl' && result.contract !== 'rail') {
      throw new Error(`${filename}: dated demo inputs must map to mdl or rail, got ${result.contract}`)
    }
    return {
      path,
      filename,
      contract: result.contract,
      csv: result.csv,
      extras: {
        sourceName: filename,
        sheets: workbook.sheets,
        mappedSheet: { name: result.sheetName, headerRowIndex: result.headerRowIndex },
      },
    }
  })
  // MDL establishes the package/deliverable universe before RAIL adds package issues.
  return mapped.sort((a, b) => (a.contract === b.contract ? a.filename.localeCompare(b.filename) : a.contract === 'mdl' ? -1 : 1))
}

interface PersonDef { key: string; name: string; email: string; roles: Role[]; isAdmin?: boolean; discipline?: string }

const dbPath = requireDemoTarget(rawDbPath)
const coverage = requireCoverage()
const inputs = loadInputs()
const rebuildPath = `${dbPath}.rebuild-${process.pid}`
for (const path of [rebuildPath, `${rebuildPath}-wal`, `${rebuildPath}-shm`]) rmSync(path, { force: true })

const sourceDisciplines = new Set<string>()
for (const input of inputs) {
  for (const row of parseTable(input.csv).rows) {
    if (row.discipline) sourceDisciplines.add(row.discipline)
    if (row.responsible_party) sourceDisciplines.add(row.responsible_party)
  }
}

const corePeople: PersonDef[] = [
  { key: 'sponsor', name: 'Project Sponsor', email: 'sponsor@twd.demo', roles: ['sponsor'] },
  { key: 'pm', name: 'Project Manager', email: 'pm@twd.demo', roles: ['pm'] },
  { key: 'dc', name: 'Document Control', email: 'dc@twd.demo', roles: ['document_controller'] },
  { key: 'agent', name: 'PEC Agent', email: process.env.PEC_AGENT_EMAIL?.trim() || 'agent@twd.demo', roles: ['coordinator'] },
  { key: 'admin', name: 'Demo Administrator', email: 'admin@twd.demo', roles: ['admin'], isAdmin: true },
]
const sourcePeople: PersonDef[] = [...sourceDisciplines].sort().map((name, index) => ({
  key: `source-${index}`,
  name,
  email: `${name.toLowerCase().replace(/[^a-z0-9]+/g, '.').replace(/^\.|\.$/g, '') || `discipline.${index}`}@twd.demo`,
  roles: ['discipline_lead'],
  discipline: name,
}))
const people = [...corePeople, ...sourcePeople.filter((candidate) => !corePeople.some((person) => person.name === candidate.name || person.email === candidate.email))]

const db = openDb(rebuildPath)
const repo = new Repo(db)
const personIds = new Map<string, number>()
let projectId = 0
let blankProjectId = 0

withTx(db, () => {
  for (const person of people) {
    personIds.set(person.key, repo.insert('person', {
      name: person.name,
      email: person.email,
      passwordHash: hashPassword(person.key === 'agent' ? (process.env.PEC_AGENT_PASSWORD?.trim() || 'pilot') : 'pilot'),
      isAdmin: person.isAdmin ?? false,
      discipline: person.discipline ?? null,
      createdAt: nowIso(),
    }))
  }
  projectId = repo.insert('project', {
    code: 'TWD',
    name: 'TWD Project',
    timezone: 'America/Edmonton',
  })
  blankProjectId = repo.insert('project', {
    code: 'TBL',
    name: 'TBL Workflow Demo',
    timezone: 'America/Edmonton',
  })
  for (const person of people) {
    for (const targetProjectId of [projectId, blankProjectId]) {
      for (const role of person.roles) {
        repo.insert('project_role', { projectId: targetProjectId, personId: personIds.get(person.key)!, role })
      }
    }
  }
})

function sx(key: string): Sx {
  const person = people.find((candidate) => candidate.key === key)!
  return {
    db,
    repo,
    projectId,
    session: {
      personId: personIds.get(key)!,
      name: person.name,
      email: person.email,
      isAdmin: person.isAdmin ?? false,
    },
    roles: person.roles,
  }
}

const results: Array<Record<string, unknown>> = []
for (const input of inputs) {
  const proposed = withTx(db, () => createProposal(sx('agent'), input.contract, input.csv, input.filename, coverage, input.extras))
  const dryRun = proposed.dryRunReport
  if (dryRun == null || 'error' in dryRun) throw new Error(`${input.filename}: dry-run failed: ${dryRun && 'error' in dryRun ? dryRun.error : 'no report'}`)
  if (dryRun.rejected.length > 0 || dryRun.conflicts.length > 0) {
    throw new Error(`${input.filename}: dry-run is not clean (${dryRun.conflicts.length} conflicts, ${dryRun.rejected.length} rejected)`)
  }
  const accepted = withTx(db, () => acceptProposal(sx('admin'), proposed.id, proposed.version, proposed.sourceSha256))
  const applied = withTx(db, () => applyProposal(sx('admin'), accepted.id, accepted.version, false))
  results.push({
    filename: input.filename,
    contract: input.contract,
    proposal: applied.ref,
    created: applied.applyReport?.accepted ?? 0,
    updated: applied.applyReport?.updated ?? 0,
    packageRows: applied.applyReport?.packageRows ?? 0,
    signals: applied.applyReport?.signals?.length ?? 0,
  })
}

// Re-import verification uses the real contracts inside rolled-back savepoints:
// zero creates/conflicts/rejects proves the same source updates in place.
for (const input of inputs) {
  db.exec('SAVEPOINT demo_reimport_check')
  try {
    const report = importContract(sx('admin'), input.contract, input.csv, false)
    if (report.accepted !== 0 || report.conflicts.length > 0 || report.rejected.length > 0) {
      throw new Error(`${input.filename}: re-import is not update-only (${report.accepted} creates, ${report.updated} updates, ${report.conflicts.length} conflicts, ${report.rejected.length} rejected)`)
    }
    const result = results.find((candidate) => candidate.filename === input.filename)!
    result.reimport = { created: report.accepted, updated: report.updated, packageRows: report.packageRows ?? 0 }
  } finally {
    db.exec('ROLLBACK TO demo_reimport_check')
    db.exec('RELEASE demo_reimport_check')
  }
}

db.exec('PRAGMA wal_checkpoint(TRUNCATE)')
const counts = Object.fromEntries(['project', 'package', 'deliverable', 'work_item', 'import_proposal'].map((table) => [
  table,
  (db.prepare(`SELECT COUNT(*) AS n FROM ${table}`).get() as { n: number }).n,
]))
const projectCounts = (db.prepare(`
  SELECT p.code,
    (SELECT COUNT(*) FROM package x WHERE x.project_id = p.id) AS packages,
    (SELECT COUNT(*) FROM deliverable x WHERE x.project_id = p.id) AS deliverables,
    (SELECT COUNT(*) FROM work_item x WHERE x.project_id = p.id) AS workItems,
    (SELECT COUNT(*) FROM import_proposal x WHERE x.project_id = p.id) AS importProposals
  FROM project p ORDER BY p.code
`).all() as Array<Record<string, unknown>>)
const tblCounts = projectCounts.find((candidate) => candidate.code === 'TBL')
if (!tblCounts || ['packages', 'deliverables', 'workItems', 'importProposals'].some((key) => tblCounts[key] !== 0)) {
  throw new Error(`TBL blank-project verification failed: ${JSON.stringify(tblCounts ?? null)}`)
}
const rebuiltQuickCheck = (db.prepare('PRAGMA quick_check').get() as { quick_check: string }).quick_check
if (rebuiltQuickCheck !== 'ok') throw new Error(`Rebuilt database quick_check failed: ${rebuiltQuickCheck}`)
db.close()

function inspectDatabase(path: string): { quickCheck: string; counts: Record<string, number> } {
  const inspected = new DatabaseSync(path, { readOnly: true })
  try {
    const quickCheck = (inspected.prepare('PRAGMA quick_check').get() as { quick_check: string }).quick_check
    const inspectedCounts = Object.fromEntries(['project', 'package', 'deliverable', 'work_item', 'import_proposal'].map((table) => [
      table,
      (inspected.prepare(`SELECT COUNT(*) AS n FROM ${table}`).get() as { n: number }).n,
    ]))
    return { quickCheck, counts: inspectedCounts }
  } finally {
    inspected.close()
  }
}

mkdirSync(dirname(dbPath), { recursive: true })
let backupPath: string | null = null
let backupVerification: ReturnType<typeof inspectDatabase> | null = null
if (existsSync(dbPath)) {
  const live = new DatabaseSync(dbPath)
  live.exec('PRAGMA wal_checkpoint(TRUNCATE)')
  live.close()
  const liveVerification = inspectDatabase(dbPath)
  const stamp = new Date().toISOString().replace(/[:.]/g, '-').replace('T', '_').replace('Z', '')
  const backupDir = join(dirname(dbPath), 'pilot-scratch', 'backups')
  mkdirSync(backupDir, { recursive: true })
  backupPath = join(backupDir, `${basename(dbPath, '.db')}-pre-rebuild-${stamp}.db`)
  copyFileSync(dbPath, backupPath)
  backupVerification = inspectDatabase(backupPath)
  if (backupVerification.quickCheck !== 'ok' || JSON.stringify(backupVerification.counts) !== JSON.stringify(liveVerification.counts)) {
    throw new Error(`Pre-rebuild backup verification failed: ${backupPath}`)
  }
}
for (const path of [dbPath, `${dbPath}-wal`, `${dbPath}-shm`]) rmSync(path, { force: true })
renameSync(rebuildPath, dbPath)
const rebuiltVerification = inspectDatabase(dbPath)
if (rebuiltVerification.quickCheck !== 'ok' || JSON.stringify(rebuiltVerification.counts) !== JSON.stringify(counts)) {
  throw new Error(`Installed demo database verification failed: ${dbPath}`)
}

console.log(JSON.stringify({
  ok: true,
  dbPath,
  backupPath,
  backupVerification,
  rebuiltVerification,
  inputDir,
  coverage,
  projectCounts,
  inputs: results,
  counts,
}, null, 2))
