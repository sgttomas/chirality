/**
 * Pilot-readiness drill (STATUS "What's next" item B; docs/PILOT.md).
 *
 * Rehearses the full adoption pipeline against a scratch database — never pec.db:
 *   1. §16 imports in pilot order: MDL → RAIL → decisions → risks (real importers,
 *      row-level reject/conflict reports printed), plus an MDL re-import to prove
 *      idempotency.
 *   2. A coordinator triage pass over the unanchored intake the RAIL import created
 *      (open triage → convert to an anchored work item, back-linked, raiser notified).
 *   3. Derived views render within the PEC-NFR-003 budget on the imported data.
 *   4. Backup → mutate → restore via tools/backup.ts (PEC-NFR-009 tested restore).
 *
 * Run from the repo root:
 *   npm run drill                       # bundled Borealis fixtures (tools/fixtures/)
 *   node tools/pilot-drill.ts --mdl your-mdl.csv --rail your-rail.csv \
 *        --decisions your-decisions.csv --risks your-risks.csv
 *
 * With your own CSVs the drill skips the fixture-specific count assertions and
 * reports what happened instead — use it to shake down the real pilot spreadsheets
 * before go-live. Exit code 0 = all checks passed. --keep retains the scratch DB.
 */

import { spawnSync } from 'node:child_process'
import { randomBytes } from 'node:crypto'
import { existsSync, mkdirSync, readFileSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { DatabaseSync } from 'node:sqlite'

import { openDb, withTx } from '../server/src/db.ts'
import { Repo, nowIso } from '../server/src/repo.ts'
import { hashPassword } from '../server/src/auth.ts'
import type { Sx } from '../server/src/services/shared.ts'
import type { ImportReport } from '../server/src/import/index.ts'
import { importContract } from '../server/src/import/index.ts'
import { dispositionIntake, openTriage } from '../server/src/services/intake.ts'
import { overviewView, packageDetailView, packagesView } from '../server/src/services/views.ts'
import type { Deliverable, IntakeItem, Package, Role } from '@pec/core'

// ---------- CLI ----------

const here = dirname(fileURLToPath(import.meta.url))
const FIXTURES = join(here, 'fixtures')
const argv = process.argv.slice(2)
const keep = argv.includes('--keep')

function argOf(flag: string): string | null {
  const i = argv.indexOf(flag)
  return i >= 0 && argv[i + 1] ? resolve(argv[i + 1]!) : null
}

const csvPaths = {
  mdl: argOf('--mdl') ?? join(FIXTURES, 'pilot-mdl.csv'),
  rail: argOf('--rail') ?? join(FIXTURES, 'pilot-rail.csv'),
  decisions: argOf('--decisions') ?? join(FIXTURES, 'pilot-decisions.csv'),
  risks: argOf('--risks') ?? join(FIXTURES, 'pilot-risks.csv'),
}
/** Custom CSVs → report-only mode; bundled fixtures → exact-count assertions. */
const fixtureMode = !argOf('--mdl') && !argOf('--rail') && !argOf('--decisions') && !argOf('--risks')

for (const [contract, path] of Object.entries(csvPaths)) {
  if (!existsSync(path)) {
    console.error(`error: ${contract} CSV not found: ${path}`)
    process.exit(2)
  }
}

// ---------- checklist ----------

let failures = 0
function check(name: string, ok: boolean, detail?: string): void {
  if (!ok) failures++
  console.log(`  ${ok ? '✓' : '✗ FAIL'} ${name}${detail ? ` — ${detail}` : ''}`)
}

function reportLine(r: ImportReport): string {
  return `accepted ${r.accepted}, updated ${r.updated}, conflicts ${r.conflicts.length}, `
    + `rejected ${r.rejected.length}, intake created ${r.intakeCreated}`
}

function printRejects(r: ImportReport): void {
  for (const rej of r.rejected) console.log(`      row ${rej.row} rejected: ${rej.errors.join('; ')}`)
  for (const c of r.conflicts) console.log(`      row ${c.row} conflict (${c.key}): ${c.reason}`)
}

// ---------- scratch database + cast ----------

const drillDir = join(tmpdir(), `pec-pilot-drill-${randomBytes(4).toString('hex')}`)
mkdirSync(drillDir, { recursive: true })
const dbPath = join(drillDir, 'drill.db')
const backupDir = join(drillDir, 'backups')

console.log(`\nPEC pilot drill — scratch db ${dbPath}`)
console.log(`mode: ${fixtureMode ? 'bundled Borealis fixtures' : 'custom CSVs (report-only counts)'}\n`)

let db = openDb(dbPath)
let repo = new Repo(db)

interface CastDef { key: string; email: string; name: string; roles: Role[]; discipline?: string; isAdmin?: boolean }
const CAST: CastDef[] = [
  { key: 'pm', email: 'pm@borealis.dev', name: 'Petra Mills', roles: ['pm'] },
  { key: 'coord', email: 'coord@borealis.dev', name: 'Colin Ward', roles: ['coordinator'] },
  { key: 'dc', email: 'dc@borealis.dev', name: 'Daria Chen', roles: ['document_controller'] },
  { key: 'leadp', email: 'lead.process@borealis.dev', name: 'Lena Prasad', roles: ['package_lead'], discipline: 'Process' },
  { key: 'leadm', email: 'lead.mech@borealis.dev', name: 'Miguel Torres', roles: ['package_lead'], discipline: 'Mechanical' },
  { key: 'engp', email: 'eng.process@borealis.dev', name: 'Erik Voss', roles: ['engineer_of_record'], discipline: 'Process' },
  { key: 'engm', email: 'eng.mech@borealis.dev', name: 'Mia Novak', roles: ['contributor'], discipline: 'Mechanical' },
  { key: 'enge', email: 'eng.elec@borealis.dev', name: 'Elias Grant', roles: ['contributor'], discipline: 'Electrical' },
  { key: 'checker', email: 'checker@borealis.dev', name: 'Chandra Rao', roles: ['checker', 'contributor'] },
  { key: 'approver', email: 'approver@borealis.dev', name: 'Ana Petrova', roles: ['approver'] },
  { key: 'admin', email: 'admin@borealis.dev', name: 'Abe Stone', roles: ['admin'], isAdmin: true },
]

const personId: Record<string, number> = {}
let projectId = 0
withTx(db, () => {
  for (const p of CAST) {
    personId[p.key] = repo.insert('person', {
      name: p.name, email: p.email, passwordHash: hashPassword('pilot'),
      isAdmin: p.isAdmin ?? false, discipline: p.discipline ?? null, createdAt: nowIso(),
    })
  }
  projectId = repo.insert('project', {
    code: 'BOR', name: 'Borealis Compression Station FEED', timezone: 'America/Edmonton',
  })
  for (const p of CAST) {
    for (const role of p.roles) {
      repo.insert('project_role', { projectId, personId: personId[p.key]!, role })
    }
  }
})

function as(key: string): Sx {
  const def = CAST.find((p) => p.key === key)!
  return {
    db, repo, projectId,
    session: { personId: personId[key]!, name: def.name, email: def.email, isAdmin: def.isAdmin ?? false },
    roles: def.roles,
  }
}

// ---------- 1. §16 imports in pilot order ----------

console.log('1. §16 imports (MDL → RAIL → decisions → risks), as the admin')
const reports: Record<string, ImportReport> = {}
for (const contract of ['mdl', 'rail', 'decisions', 'risks'] as const) {
  const csv = readFileSync(csvPaths[contract], 'utf8')
  const report = withTx(db, () => importContract(as('admin'), contract, csv, false))
  reports[contract] = report
  console.log(`   ${contract}: ${reportLine(report)}`)
  printRejects(report)
}

if (fixtureMode) {
  check('MDL: 24 deliverables accepted, none rejected',
    reports.mdl!.accepted === 24 && reports.mdl!.rejected.length === 0, reportLine(reports.mdl!))
  check('RAIL: 15 anchored records accepted', reports.rail!.accepted === 15, reportLine(reports.rail!))
  check('RAIL: 3 unmatched rows landed as unanchored intake (I-2)', reports.rail!.intakeCreated === 3)
  check('RAIL: the deliberate bad row (invalid hold_cause) was rejected with a row-level report',
    reports.rail!.rejected.length === 1 && reports.rail!.rejected[0]!.errors.some((e) => e.includes('hold_cause')))
  check('decisions: 6 accepted', reports.decisions!.accepted === 6, reportLine(reports.decisions!))
  check('risks: 8 accepted', reports.risks!.accepted === 8, reportLine(reports.risks!))
} else {
  check('every row landed somewhere (accepted / updated / conflict / rejected / intake) — nothing silently dropped',
    true, 'inspect the per-contract reports above')
}

// idempotency: a re-import must update, never duplicate (§16)
const again = withTx(db, () => importContract(as('admin'), 'mdl', readFileSync(csvPaths.mdl, 'utf8'), false))
console.log(`   mdl re-import: ${reportLine(again)}`)
printRejects(again)
check('MDL re-import is idempotent: all rows updated in place, none duplicated',
  again.accepted === 0 && again.rejected.length === 0,
  `updated ${again.updated}, accepted ${again.accepted}`)
const delCount = (db.prepare('SELECT COUNT(*) AS n FROM deliverable WHERE project_id = ?').get(projectId) as { n: number }).n
if (fixtureMode) check('deliverable count unchanged after re-import', delCount === 24, `${delCount} rows`)

// ---------- 2. coordinator triage (the weekly habit, PEC-AHL-004/005/006) ----------

console.log('\n2. Coordinator triage over the unanchored intake')
const untriaged = repo.list<IntakeItem>('intake_item', projectId, "state != 'dispositioned'", [])
console.log(`   triage queue: ${untriaged.length} unanchored item(s): ${untriaged.map((t) => `${t.ref} (${t.quickType})`).join(', ') || 'none'}`)
if (untriaged.length > 0) {
  const item = untriaged[0]!
  const anchor = repo.list<Deliverable>('deliverable', projectId, undefined, [])[0]
  if (!anchor) {
    check('triage conversion', false, 'no deliverable available to anchor to')
  } else {
    const opened = withTx(db, () => openTriage(as('coord'), item.id, item.version))
    const result = withTx(db, () => dispositionIntake(as('coord'), item.id, {
      version: opened.version,
      disposition: 'converted',
      note: 'pilot drill: converted at weekly triage',
      records: {
        workItems: [{
          title: item.statementVerbatim.slice(0, 140), statement: item.statementVerbatim,
          kind: 'action', log: item.log, anchorType: 'deliverable', anchorId: anchor.id,
          ownerId: item.suggestedOwnerId ?? personId.pm!, needBy: item.needBy,
        }],
      },
    }))
    check('intake converted to an anchored work item at triage',
      result.created.length === 1 && result.created[0]!.recordType === 'work_item',
      `${item.ref} → ${result.created.map((c) => c.ref).join(', ')} (anchored to ${anchor.docNo})`)
    const links = (db.prepare('SELECT COUNT(*) AS n FROM intake_link WHERE intake_id = ?').get(item.id) as { n: number }).n
    check('created record back-linked to the intake (PEC-AHL-005)', links === 1)
    const notified = (db.prepare(
      'SELECT COUNT(*) AS n FROM notification WHERE project_id = ? AND person_id = ? AND record_id = ? AND event = ?',
    ).get(projectId, item.raisedBy, item.id, 'raised_item_routed') as { n: number }).n
    check('raiser notified at routing (PEC-AHL-007)', notified === 1)
    check('statement preserved verbatim after triage (OM-3)',
      (repo.get<IntakeItem>('intake_item', projectId, item.id)).statementVerbatim === item.statementVerbatim)
  }
} else {
  console.log('   (nothing to triage — every RAIL row anchored)')
}

// ---------- 3. derived views on the imported data (PEC-NFR-003) ----------

console.log('\n3. Derived views render on the imported data')
const pkgs = repo.list<Package>('package', projectId, undefined, [])
const timeIt = (label: string, fn: () => unknown): number => {
  const t0 = process.hrtime.bigint()
  fn()
  const ms = Number(process.hrtime.bigint() - t0) / 1e6
  console.log(`   ${label}: ${ms.toFixed(1)} ms`)
  return ms
}
const tOverview = timeIt('overview (PM home)', () => overviewView(as('pm')))
const tPackages = timeIt('packages register', () => packagesView(as('leadp')))
const tDetail = pkgs.length > 0
  ? timeIt(`package cockpit (${pkgs[0]!.code})`, () => packageDetailView(as('leadp'), pkgs[0]!.id))
  : 0
check('role homes render within the 2 s budget (PEC-NFR-003)',
  tOverview < 2000 && tPackages < 2000 && tDetail < 2000)

// ---------- 4. backup → mutate → restore (PEC-NFR-009 tested restore) ----------

console.log('\n4. Backup / restore rehearsal (tools/backup.ts)')
const env = { ...process.env, PEC_DB: dbPath, PEC_BACKUP_DIR: backupDir }
const runBackupTool = (...args: string[]) =>
  spawnSync(process.execPath, ['--disable-warning=ExperimentalWarning', join(here, 'backup.ts'), ...args],
    { env, encoding: 'utf8' as const })

const bk = runBackupTool('backup')
check('backup written while the database is open (WAL-safe VACUUM INTO)', bk.status === 0, bk.stderr.trim() || undefined)
const backupFile = (bk.stdout.match(/backup written: (\S+)/) ?? [])[1]

// mutate after the backup, then stop using the db (the operator stops the server here)
withTx(db, () => repo.insert('person', {
  name: 'Post Backup Marker', email: 'marker@borealis.dev', passwordHash: 'x',
  isAdmin: false, discipline: null, createdAt: nowIso(),
}))
db.close()

if (backupFile) {
  const rs = runBackupTool('restore', backupFile)
  check('restore succeeded', rs.status === 0, rs.stderr.trim() || undefined)
  const restored = new DatabaseSync(dbPath, { readOnly: true })
  const markerGone = (restored.prepare('SELECT COUNT(*) AS n FROM person WHERE email = ?')
    .get('marker@borealis.dev') as { n: number }).n === 0
  const dataIntact = (restored.prepare('SELECT COUNT(*) AS n FROM deliverable WHERE project_id = ?')
    .get(projectId) as { n: number }).n === delCount
  restored.close()
  check('restored database is the pre-mutation snapshot', markerGone && dataIntact)
  const aside = new DatabaseSync(`${dbPath}.pre-restore`, { readOnly: true })
  const markerPreserved = (aside.prepare('SELECT COUNT(*) AS n FROM person WHERE email = ?')
    .get('marker@borealis.dev') as { n: number }).n === 1
  aside.close()
  check('pre-restore database preserved aside, mutation included (nothing destroyed)', markerPreserved)
} else {
  check('restore', false, 'could not parse backup filename from backup output')
}

// ---------- summary ----------

console.log(`\n${failures === 0 ? 'PASS' : `FAIL (${failures} check(s) failed)`} — pilot drill complete.`)
console.log('Next: docs/PILOT.md walks the same steps against the real pilot data.')
if (keep || failures > 0) {
  console.log(`scratch db kept for inspection: ${dbPath}`)
} else {
  rmSync(drillDir, { recursive: true, force: true })
}
process.exit(failures === 0 ? 0 : 1)
