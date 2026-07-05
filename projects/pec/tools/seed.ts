/**
 * PEC demo seed — builds the "Aurora Gas Plant FEED" pilot project through the REAL
 * service layer (server/src/services/*), so history, notifications, conditions, and
 * derived status wiring are genuine (I-4, I-7): nothing here writes a derived value.
 *
 * Run from the repo root:  npm run seed
 * Fresh every run: deletes pec.db* first. All personas share the password "pilot".
 *
 * The only direct SQL is timestamp backdating (created_at / raised_at / ready_at) to
 * age records into the §6.3 signal thresholds — a seed-only concern, not a workflow.
 */

import { existsSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { dirname, join, resolve, sep } from 'node:path'
import { fileURLToPath } from 'node:url'

import { openDb, withTx } from '../server/src/db.ts'
import { Repo, nowIso } from '../server/src/repo.ts'
import { hashPassword } from '../server/src/auth.ts'
import type { Sx } from '../server/src/services/shared.ts'
import { createRevision, transitionRevision } from '../server/src/services/revisions.ts'
import {
  acceptCheck, addComment, createCheck, respondComment, startCheck, updateChecklist,
} from '../server/src/services/checks.ts'
import {
  createApprovalRecord, createCondition, createDecision, progressDecision,
  recordApprovalOutcome, waiveCondition,
} from '../server/src/services/decisions.ts'
import { createWorkItem, transitionWorkItem } from '../server/src/services/work.ts'
import { raiseHold } from '../server/src/services/holds.ts'
import { dispositionIntake, openTriage, raiseIntake } from '../server/src/services/intake.ts'
import { commitWeek, createPlanItem, shiftPlanItem, upsertCapacity } from '../server/src/services/plan.ts'
import { importContract } from '../server/src/import/index.ts'
import {
  createDeliverable, createInterface, createPackage, createRisk, updateInterface, updateRisk,
} from '../server/src/services/registers.ts'
import type { Check, ProjectCalendar, Role } from '@pec/core'
import { isWorkingDay, isoWeekOf, localDate } from '@pec/core'

// ---------- fresh database ----------

const here = dirname(fileURLToPath(import.meta.url))
const rawDbPath = process.env.PEC_DB?.trim()

function pathIsInside(child: string, parent: string): boolean {
  const normalizedParent = parent.endsWith(sep) ? parent : `${parent}${sep}`
  return child === parent || child.startsWith(normalizedParent)
}

function hasScratchOrDemoToken(path: string): boolean {
  return path
    .split(/[\\/_.-]+/)
    .some((part) => ['scratch', 'demo'].includes(part.toLowerCase()))
}

function assertDemoSeedTarget(rawPath: string | undefined): string {
  if (!rawPath) {
    throw new Error('PEC_DB is required for demo seeding; point it at a scratch/demo database.')
  }
  const dbPath = resolve(rawPath)
  const tempRoot = resolve(tmpdir())
  if (!pathIsInside(dbPath, tempRoot) && !hasScratchOrDemoToken(dbPath)) {
    throw new Error(`Refusing to seed non-scratch/non-demo database target: ${dbPath}`)
  }
  return dbPath
}

const dbPath = assertDemoSeedTarget(rawDbPath)
for (const p of [dbPath, `${dbPath}-wal`, `${dbPath}-shm`]) {
  if (existsSync(p)) rmSync(p)
}
const db = openDb(dbPath)
const repo = new Repo(db)

// ---------- calendar helpers (America/Chicago, Sat/Sun weekends — matches the project) ----------

const CAL: ProjectCalendar = { timezone: 'America/Chicago', weekendDays: ['Sat', 'Sun'], holidays: [] }
const TODAY = localDate(nowIso(), CAL.timezone)

function addDays(dateLocal: string, n: number): string {
  const d = new Date(`${dateLocal}T00:00:00Z`)
  d.setUTCDate(d.getUTCDate() + n)
  return d.toISOString().slice(0, 10)
}
/** Local date n calendar days from today (negative = past). */
const day = (n: number): string => addDays(TODAY, n)
/** UTC ISO timestamp n working days back from today (for backdating age signals). */
function workingDaysAgo(n: number): string {
  let cur = TODAY
  let count = 0
  while (count < n) {
    cur = addDays(cur, -1)
    if (isWorkingDay(cur, CAL)) count++
  }
  return `${cur}T12:00:00.000Z`
}
/** Seed-only timestamp backdating; the record content itself came through the services. */
function backdate(table: string, col: string, id: number, iso: string): void {
  db.prepare(`UPDATE ${table} SET ${col} = ? WHERE id = ?`).run(iso, id)
}

// ---------- 1. people (password "pilot" for all) ----------

interface PersonDef {
  key: string
  email: string
  name: string
  roles: Role[]
  discipline?: string
  isAdmin?: boolean
}

const PERSONS: PersonDef[] = [
  { key: 'sponsor', email: 'sponsor@aurora.dev', name: 'Sam Sponsor', roles: ['sponsor'] },
  { key: 'pm', email: 'pm@aurora.dev', name: 'Petra Manager', roles: ['pm'] },
  { key: 'em', email: 'em@aurora.dev', name: 'Elena Engmgr', roles: ['engineering_manager'] },
  { key: 'leadp', email: 'lead.process@aurora.dev', name: 'Priya Process', roles: ['package_lead'], discipline: 'Process' },
  { key: 'leadm', email: 'lead.mech@aurora.dev', name: 'Marco Mech', roles: ['package_lead'], discipline: 'Mechanical' },
  { key: 'eor', email: 'eor@aurora.dev', name: 'Erin Record', roles: ['engineer_of_record'], discipline: 'Process' },
  { key: 'checker', email: 'checker@aurora.dev', name: 'Charles Check', roles: ['checker', 'contributor'], discipline: 'Process' },
  { key: 'approver', email: 'approver@aurora.dev', name: 'Alice Approve', roles: ['approver'] },
  { key: 'planner', email: 'planner@aurora.dev', name: 'Paul Plan', roles: ['planner'] },
  { key: 'coord', email: 'coord@aurora.dev', name: 'Cody Coordinate', roles: ['coordinator'] },
  { key: 'dc', email: 'dc@aurora.dev', name: 'Dana Doc', roles: ['document_controller'] },
  { key: 'ic1', email: 'ic1@aurora.dev', name: 'Ivan Contributor', roles: ['contributor'], discipline: 'Mechanical' },
  { key: 'ic2', email: 'ic2@aurora.dev', name: 'Imogen Contributor', roles: ['contributor'], discipline: 'Instrumentation' },
  { key: 'viewer', email: 'viewer@aurora.dev', name: 'Vic View', roles: ['viewer'] },
  { key: 'admin', email: 'admin@aurora.dev', name: 'Ada Admin', roles: ['admin'], isAdmin: true },
]

const personId: Record<string, number> = {}
let projectId = 0

withTx(db, () => {
  for (const p of PERSONS) {
    personId[p.key] = repo.insert('person', {
      name: p.name, email: p.email, passwordHash: hashPassword('pilot'),
      isAdmin: p.isAdmin ?? false, discipline: p.discipline ?? null, createdAt: nowIso(),
    })
  }
  // ---------- 3. project + role assignments ----------
  projectId = repo.insert('project', {
    code: 'AUR', name: 'Aurora Gas Plant FEED', timezone: CAL.timezone,
  })
  for (const p of PERSONS) {
    for (const role of p.roles) {
      repo.insert('project_role', { projectId, personId: personId[p.key]!, role })
    }
  }
})

const P = (key: string): number => personId[key]!

/** Service context acting AS a persona — the same Sx shape the API layer builds. */
function as(key: string): Sx {
  const def = PERSONS.find((p) => p.key === key)!
  return {
    db, repo, projectId,
    session: { personId: P(key), name: def.name, email: def.email, isAdmin: def.isAdmin ?? false },
    roles: def.roles,
  }
}

/** Current version of a controlled record (services bump it on every write). */
const ver = (table: string, id: number): number =>
  repo.get<{ version: number }>(table, projectId, id).version

// ---------- 4. condition + checklist templates (D-11 defaults) ----------

let processChecklistId = 0
withTx(db, () => {
  const templates = [
    // D-11: issue-affecting transitions ship hard
    { name: 'check-before-issue', transition: 'revision.issue', type: 'check', severity: 'hard', description: 'Check accepted before issue', requiredArtifactName: null },
    // unpinned approval-type: satisfied by any decided-approved approval record applying to the revision (§5.3)
    { name: 'approval-before-issue', transition: 'revision.issue', type: 'approval', severity: 'hard', description: 'Approval outcome recorded before issue', requiredArtifactName: null },
    { name: 'transmittal-prereqs', transition: 'revision.issue', type: 'document_control', severity: 'hard', description: 'Transmittal reference and recipients recorded on the issue event', requiredArtifactName: null },
    { name: 'native-files', transition: 'revision.issue', type: 'evidence', severity: 'warn', description: 'Native files archived alongside the issued PDF', requiredArtifactName: 'native-files' },
  ]
  for (const t of templates) {
    repo.insert('condition_template', {
      projectId, name: t.name, deliverableType: null, issuePurpose: null, packageId: null,
      transition: t.transition, type: t.type, severity: t.severity,
      description: t.description, requiredArtifactName: t.requiredArtifactName,
    })
  }
  // PEC-CHK-001: checklist template keyed by discipline/type
  processChecklistId = repo.insert('checklist_template', {
    projectId, name: 'Process deliverable check', discipline: 'Process', deliverableType: null,
    items: [
      { text: 'Design basis revision referenced and current', category: 'basis' },
      { text: 'Stream numbers match the PFD/H&MB', category: 'consistency' },
      { text: 'Units consistent with the project units basis', category: 'consistency' },
      { text: 'Holds and assumptions flagged on the face of the document', category: 'completeness' },
      { text: 'Client numbering and title block per DC procedure', category: 'document control' },
    ],
  })
})

// ---------- 5. packages ----------

const pkgId: Record<string, number> = {}
withTx(db, () => {
  const S = as('pm')
  pkgId['PKG-P'] = createPackage(S, { code: 'PKG-P', name: 'Process', leadId: P('leadp'), milestone: 'Gate 3' }).id
  pkgId['PKG-M'] = createPackage(S, { code: 'PKG-M', name: 'Mechanical', leadId: P('leadm') }).id
  pkgId['PKG-PI'] = createPackage(S, { code: 'PKG-PI', name: 'Piping', leadId: P('leadm') }).id
  pkgId['PKG-EI'] = createPackage(S, { code: 'PKG-EI', name: 'Electrical & Instrumentation', leadId: P('leadp') }).id
})

// ---------- 6. deliverables (PEC-DEL-002) ----------

interface DelDef {
  docNo: string; title: string; pkg: string; discipline: string; dtype: string
  owner: string; due: number; milestone?: string; rev?: boolean
}

const DELIVERABLES: DelDef[] = [
  { docNo: 'AUR-P-001', title: 'Process design basis', pkg: 'PKG-P', discipline: 'Process', dtype: 'basis', owner: 'eor', due: 45, rev: true },
  { docNo: 'AUR-P-002', title: 'Process flow diagram (PFD)', pkg: 'PKG-P', discipline: 'Process', dtype: 'drawing', owner: 'eor', due: 21, milestone: 'Gate 3', rev: true },
  { docNo: 'AUR-P-003', title: 'Heat & material balance (H&MB)', pkg: 'PKG-P', discipline: 'Process', dtype: 'calculation', owner: 'ic1', due: 30, rev: true },
  { docNo: 'AUR-P-004', title: 'P&ID — process area, sheet 1', pkg: 'PKG-P', discipline: 'Process', dtype: 'drawing', owner: 'eor', due: 14, rev: true },
  { docNo: 'AUR-M-001', title: 'Pump datasheet P-101', pkg: 'PKG-M', discipline: 'Mechanical', dtype: 'datasheet', owner: 'ic1', due: 30, rev: true },
  { docNo: 'AUR-M-002', title: 'Compressor datasheet K-201', pkg: 'PKG-M', discipline: 'Mechanical', dtype: 'datasheet', owner: 'ic2', due: 60, rev: true },
  { docNo: 'AUR-M-003', title: 'Air cooler datasheet E-301', pkg: 'PKG-M', discipline: 'Mechanical', dtype: 'datasheet', owner: 'ic2', due: 75 },
  { docNo: 'AUR-PI-001', title: 'Piping line list', pkg: 'PKG-PI', discipline: 'Piping', dtype: 'list', owner: 'ic1', due: 40, rev: true },
  { docNo: 'AUR-PI-002', title: 'Stress critical line list', pkg: 'PKG-PI', discipline: 'Piping', dtype: 'list', owner: 'eor', due: -14, milestone: 'Gate 3', rev: true },
  { docNo: 'AUR-PI-003', title: 'Piping material specification', pkg: 'PKG-PI', discipline: 'Piping', dtype: 'specification', owner: 'ic2', due: 90 },
  { docNo: 'AUR-EI-001', title: 'One-line diagram', pkg: 'PKG-EI', discipline: 'Electrical', dtype: 'drawing', owner: 'eor', due: 50, rev: true },
  { docNo: 'AUR-EI-002', title: 'Instrument index', pkg: 'PKG-EI', discipline: 'Instrumentation', dtype: 'list', owner: 'ic1', due: 65, rev: true },
  { docNo: 'AUR-EI-003', title: 'Cable schedule', pkg: 'PKG-EI', discipline: 'Electrical', dtype: 'list', owner: 'ic2', due: 85 },
  { docNo: 'AUR-EI-004', title: 'Hazardous area classification', pkg: 'PKG-EI', discipline: 'Electrical', dtype: 'drawing', owner: 'eor', due: 35 },
]

const delId: Record<string, number> = {}
const revId: Record<string, number> = {}
withTx(db, () => {
  const S = as('dc') // document control maintains the MDL (§2.2)
  for (const d of DELIVERABLES) {
    delId[d.docNo] = createDeliverable(S, {
      packageId: pkgId[d.pkg]!, docNo: d.docNo, title: d.title, discipline: d.discipline,
      deliverableType: d.dtype, ownerId: P(d.owner), dueDate: day(d.due),
      milestone: d.milestone, issuePurposePlan: 'IFR',
    }).id
  }
})
// Revision A instantiates the D-11 template conditions on revision.issue (§5.2)
withTx(db, () => {
  const S = as('eor')
  for (const d of DELIVERABLES) {
    if (d.rev) revId[d.docNo] = createRevision(S, { deliverableId: delId[d.docNo]!, revCode: 'A' }).id
  }
})

const D = (docNo: string): number => delId[docNo]!
const R = (docNo: string): number => revId[docNo]!

// ---------- 7a. AUR-P-002: full happy chain to ISSUED (PEC-DEL-008, PEC-ARC-002, D-11) ----------

console.log('seeding: AUR-P-002 happy chain to issued …')
withTx(db, () => {
  const chk = createCheck(as('leadp'), { revisionId: R('AUR-P-002'), checkerId: P('checker'), templateId: processChecklistId })
  startCheck(as('checker'), chk.id, ver('check_record', chk.id))
  const fresh = repo.get<Check>('check_record', projectId, chk.id)
  updateChecklist(as('checker'), chk.id, fresh.version, fresh.checklist.map((i) => ({ ...i, done: true })))
  // PEC-AUTH-001: approval record created before check acceptance → auto prereqs (§4.5)
  const apr = createApprovalRecord(as('leadp'), {
    title: 'IFR authorization — AUR-P-002', approvalType: 'issue_authorization',
    authoritySource: 'Engineering procedure EP-04 (issue authorization)',
    appliesToType: 'revision', appliesToId: R('AUR-P-002'),
    signatoryIds: [P('approver')], dueDate: day(7),
  })
  // check acceptance satisfies the check-type conditions and readies the approval (§5.3)
  acceptCheck(as('checker'), chk.id, ver('check_record', chk.id))
  // PEC-AUTH-004: record-outcome is the only path to decided (creates the Decision, OM-6)
  recordApprovalOutcome(as('approver'), apr.id, {
    version: ver('approval_record', apr.id), outcome: 'approve',
    rationale: 'PFD is consistent with design basis rev A; authorized for IFR issue.',
  })
  // PEC-DEL-008: recording the issue event IS the transition; hard-gated (D-11)
  transitionRevision(as('dc'), R('AUR-P-002'), 'issue', {
    version: ver('revision', R('AUR-P-002')),
    issueEvent: { purpose: 'IFR', transmittalRef: 'TR-0001', recipients: ['Client DC'] },
  })
})
withTx(db, () => {
  // next revision supersedes A (I-10 chain preserved); B carries fresh template conditions
  const revB = createRevision(as('eor'), { deliverableId: D('AUR-P-002'), revCode: 'B' })
  revId['AUR-P-002'] = revB.id
  const w1 = createWorkItem(as('eor'), {
    title: 'Incorporate client IFR comments into PFD rev B', kind: 'rework',
    anchorType: 'deliverable', anchorId: D('AUR-P-002'), ownerId: P('eor'), needBy: day(7),
  })
  transitionWorkItem(as('eor'), w1.id, 'start', { version: ver('work_item', w1.id) })
  createWorkItem(as('eor'), {
    title: 'Update stream numbering per client standard',
    anchorType: 'deliverable', anchorId: D('AUR-P-002'), ownerId: P('ic1'), needBy: day(14),
  })
})

// ---------- 7b. AUR-P-004: in_check with aging review comments (OM-5, DH-A4 / S-CMT) ----------

console.log('seeding: AUR-P-004 check with aging comments …')
withTx(db, () => {
  const chk = createCheck(as('leadp'), { revisionId: R('AUR-P-004'), checkerId: P('checker'), templateId: processChecklistId })
  startCheck(as('checker'), chk.id, ver('check_record', chk.id))
  const c1 = addComment(as('checker'), {
    checkId: chk.id, responderId: P('eor'),
    text: 'PSV-1201 set pressure disagrees with design basis table 4-2 — confirm 21.5 barg.',
  })
  const c2 = addComment(as('checker'), {
    checkId: chk.id, responderId: P('eor'),
    text: 'Line 6"-P-1204 shows no isolation at battery limit; confirm against plot plan.',
  })
  const c3 = addComment(as('checker'), {
    checkId: chk.id, responderId: P('ic1'),
    text: 'Level bridle instrument tags duplicate AUR-EI-002 entries — reconcile numbering.',
  })
  respondComment(as('eor'), c1.id, ver('review_comment', c1.id),
    'Set pressure corrected to 21.5 barg per DBM table 4-2; markup attached to the check.')
  // age the two OPEN comments past the escalate threshold (§6.3: warn 5 / red 10 wd)
  backdate('review_comment', 'created_at', c2.id, workingDaysAgo(13))
  backdate('review_comment', 'created_at', c3.id, workingDaysAgo(13))
})

// ---------- 7c. AUR-M-001: approved but blocked by an aged vendor_data hold (OM-2, DH-R2 / S-HOLD) ----------

console.log('seeding: AUR-M-001 approved-but-blocked …')
withTx(db, () => {
  const chk = createCheck(as('leadm'), { revisionId: R('AUR-M-001'), checkerId: P('checker') })
  startCheck(as('checker'), chk.id, ver('check_record', chk.id))
  const apr = createApprovalRecord(as('leadm'), {
    title: 'Pump datasheet P-101 approval', approvalType: 'datasheet_approval',
    authoritySource: 'Engineering procedure EP-04',
    appliesToType: 'revision', appliesToId: R('AUR-M-001'),
    signatoryIds: [P('approver')], dueDate: day(-3),
  })
  acceptCheck(as('checker'), chk.id, ver('check_record', chk.id))
  recordApprovalOutcome(as('approver'), apr.id, {
    version: ver('approval_record', apr.id), outcome: 'approve',
    rationale: 'Datasheet accepted; vendor curve confirmation tracked separately.',
  })
})
withTx(db, () => {
  // I-3: typed cause, owner, and need-by required; blocks the revision → issue is hold-vetoed
  const hold = raiseHold(as('leadm'), {
    title: 'Awaiting certified vendor pump curves for P-101', cause: 'vendor_data',
    statement: 'Vendor has not returned certified performance curves; datasheet cannot issue without them.',
    ownerId: P('leadm'), needBy: day(-7),
    targets: [{ targetType: 'revision', targetId: R('AUR-M-001') }],
  })
  backdate('hold', 'raised_at', hold.id, workingDaysAgo(21)) // DH-R2 red + S-HOLD escalate (> 14 wd)
  // the warn evidence condition (native-files) stays open on this revision by design
})

// ---------- 7d. AUR-PI-002: overdue work items → forecast slip > 5 wd (DH-R1 → PH-R1 on Gate 3) ----------

console.log('seeding: AUR-PI-002 forecast slip …')
withTx(db, () => {
  const w1 = createWorkItem(as('leadm'), {
    title: 'Resolve stress model clashes on critical lines',
    anchorType: 'deliverable', anchorId: D('AUR-PI-002'), ownerId: P('eor'), needBy: day(-2),
  })
  transitionWorkItem(as('eor'), w1.id, 'start', { version: ver('work_item', w1.id) })
  createWorkItem(as('leadm'), {
    title: 'Confirm pipe support locations with civil',
    anchorType: 'deliverable', anchorId: D('AUR-PI-002'), ownerId: P('ic1'), needBy: day(-4),
  })
})

// ---------- 7e. pending decision gating AUR-P-003 issue (S-DEC red: blocks an issue transition) ----------

console.log('seeding: units-basis decision gating AUR-P-003 …')
let unitsDecisionRef = ''
withTx(db, () => {
  const dec = createDecision(as('pm'), {
    title: 'Confirm metric vs imperial units basis',
    statement: 'Client RFI-014: are datasheets and the H&MB to be issued in metric or imperial units? Blocks the H&MB issue.',
    authorityId: P('pm'), preparerId: P('leadp'), needBy: day(-10), packageId: pkgId['PKG-P']!,
  })
  progressDecision(as('leadp'), dec.id, 'mark_pending', { version: ver('decision', dec.id) })
  // hard decision-type condition pinned to the decision, gating the H&MB issue (§5.3)
  createCondition(as('pm'), {
    parentType: 'revision', parentId: R('AUR-P-003'), gatedTransition: 'revision.issue',
    type: 'decision', severity: 'hard', requiredRefType: 'decision', requiredRefId: dec.id,
    description: 'Units basis decision recorded before the H&MB issues',
    ownerId: P('ic1'), needBy: day(-10),
  })
  unitsDecisionRef = dec.ref
})

// ---------- 7f. client hold-point approval ready + aged (S-APPR red, PEC-AUTH-001) ----------

console.log('seeding: AUR-P-001 client hold point approval …')
withTx(db, () => {
  const apr = createApprovalRecord(as('pm'), {
    title: 'Client hold point — HAZOP actions closed', approvalType: 'client_hold_point',
    authoritySource: 'Contract Exhibit C — client hold points',
    appliesToType: 'revision', appliesToId: R('AUR-P-001'),
    signatoryIds: [P('approver')], dueDate: day(-5), holdPoint: true,
    defaultCheckPrereq: false, // hold point has no in-house check prerequisite → ready immediately
  })
  backdate('approval_record', 'ready_at', apr.id, workingDaysAgo(13)) // S-APPR escalate (> 10 wd)
})

// ---------- 7g. waived condition on AUR-M-002 (I-8: waiver is a Decision) ----------

console.log('seeding: AUR-M-002 waived condition …')
withTx(db, () => {
  const cond = createCondition(as('leadm'), {
    parentType: 'revision', parentId: R('AUR-M-002'), gatedTransition: 'revision.issue',
    type: 'evidence', severity: 'hard', requiredArtifactName: 'vendor-certification',
    description: 'Vendor certification package attached before issue', ownerId: P('ic2'),
  })
  waiveCondition(as('pm'), cond.id, {
    version: ver('condition_record', cond.id),
    rationale: 'Client accepted certification to follow with the IFC issue (client call 2026-06-30); exposure logged in the risk register.',
  })
})

// ---------- 7h. interfaces (PEC-PKG-007, OM-7; one overdue > 7 wd → PH-R2) ----------

console.log('seeding: interfaces …')
withTx(db, () => {
  const S = as('pm')
  createInterface(S, {
    title: 'Pump hydraulic data', givingParty: 'Process', receivingParty: 'Mechanical',
    givingPackageId: pkgId['PKG-P']!, receivingPackageId: pkgId['PKG-M']!,
    requiredInfo: 'Rated flow, differential head, and NPSHa for P-101 sizing',
    needBy: day(-14), // > 7 wd overdue → PH-R2 on both packages
  })
  createInterface(S, {
    title: 'Instrument air demand list', givingParty: 'Mechanical', receivingParty: 'E&I',
    givingPackageId: pkgId['PKG-M']!, receivingPackageId: pkgId['PKG-EI']!,
    requiredInfo: 'Continuous and peak instrument air demand per consumer', needBy: day(10),
  })
  const delivered = createInterface(S, {
    title: 'Electrical load list', givingParty: 'E&I', receivingParty: 'Process',
    givingPackageId: pkgId['PKG-EI']!, receivingPackageId: pkgId['PKG-P']!,
    requiredInfo: 'Connected and operating loads feeding the one-line diagram', needBy: day(-1),
  })
  updateInterface(S, delivered.id, ver('interface_item', delivered.id), { state: 'delivered' })
})

// ---------- 7i. risks (PEC-RISK-001) ----------

console.log('seeding: risks …')
withTx(db, () => {
  const high = createRisk(as('pm'), {
    title: 'Units-basis decision delay pushes H&MB past Gate 3',
    cause: `Client has not confirmed metric vs imperial basis (${unitsDecisionRef} pending)`,
    consequence: 'H&MB and every dependent datasheet slip past the Gate 3 date',
    packageId: pkgId['PKG-P']!, deliverableId: D('AUR-P-003'), ownerId: P('leadp'),
    probability: 4, impact: 5,
    mitigation: 'Escalate at the weekly client meeting; prepare dual-unit tables for the two critical sheets',
    needBy: day(7),
  })
  updateRisk(as('pm'), high.id, ver('risk', high.id), { state: 'mitigating' })
  createRisk(as('leadm'), {
    title: 'Vendor curves late for long-lead pumps',
    cause: 'Vendor engineering backlog', consequence: 'P-101 datasheet issue slips; hold ages further',
    packageId: pkgId['PKG-M']!, deliverableId: D('AUR-M-001'), ownerId: P('leadm'),
    probability: 3, impact: 4, mitigation: 'Weekly expediting call; escalate via procurement', needBy: day(10),
  })
  createRisk(as('em'), {
    title: 'August vacation season reduces checking capacity',
    cause: 'Concurrent checker leave', consequence: 'Check turnaround exceeds 5 wd on peak weeks',
    ownerId: P('em'), probability: 2, impact: 3,
    mitigation: 'Stagger checker leave; pre-book external checker for drawings', needBy: day(30),
  })
})

// ---------- 7j. intake (OM-3, PEC-AHL-003/-005; one aged → S-INTAKE red) ----------

console.log('seeding: intake …')
withTx(db, () => {
  const aged = raiseIntake(as('ic2'), {
    statement: 'Need vendor pump curves for the P-101 hydraulic check',
    quickType: 'need_information', anchorSuggestion: 'AUR-M-001', needBy: day(-5),
  })
  backdate('intake_item', 'raised_at', aged.id, workingDaysAgo(9)) // S-INTAKE escalate (> 5 wd)
  raiseIntake(as('ic2'), {
    statement: 'Units basis needs confirming before the H&MB tables are finalized',
    quickType: 'need_decision', anchorSuggestion: 'AUR-P-003',
  })
  raiseIntake(as('planner'), {
    statement: 'Stress critical line list is slipping against the Gate 3 date',
    quickType: 'risk_schedule', anchorSuggestion: 'AUR-PI-002',
  })
})
withTx(db, () => {
  // real triage path (PEC-AHL-005): coordinator converts to an anchored work item
  const t = raiseIntake(as('ic2'), {
    statement: 'Instrument index is missing tags from the package 2 P&IDs',
    quickType: 'action', anchorSuggestion: 'AUR-EI-002', suggestedOwnerId: P('ic1'),
  })
  openTriage(as('coord'), t.id, ver('intake_item', t.id))
  dispositionIntake(as('coord'), t.id, {
    version: ver('intake_item', t.id), disposition: 'converted',
    note: 'Converted to a work item on the instrument index',
    records: {
      workItems: [{
        title: 'Add package 2 P&ID tags to the instrument index',
        statement: 'Instrument index is missing tags from the package 2 P&IDs',
        anchorType: 'deliverable', anchorId: D('AUR-EI-002'), ownerId: P('ic1'), needBy: day(7),
      }],
    },
  })
})

// ---------- 7k. My Week material (PEC-MW-001/-007) ----------

console.log('seeding: My Week commitments …')
withTx(db, () => {
  // PEC-MW-007: manual commit to the current ISO week
  createWorkItem(as('leadp'), {
    title: 'Draft PFD rev B markups for squad check',
    anchorType: 'deliverable', anchorId: D('AUR-P-002'), ownerId: P('eor'), needBy: day(10),
    committedWeek: isoWeekOf(TODAY),
  })
  createWorkItem(as('leadp'), {
    title: 'Return H&MB basis notes to the process lead',
    anchorType: 'deliverable', anchorId: D('AUR-P-003'), ownerId: P('ic1'), needBy: TODAY,
  })
})

// ---------- 7l. P2 plan & capacity (PRD §12.4: PEC-PLAN-*, I-9, PEC-PLAN-007) ----------

console.log('seeding: plan, capacity, weekly commit …')
const week = isoWeekOf(TODAY)
withTx(db, () => {
  // capacity by discipline for the current week (PEC-PLAN-003)
  for (const [discipline, hours] of [['Process', 40], ['Mechanical', 40], ['Instrumentation', 32]] as const) {
    upsertCapacity(as('planner'), { week, discipline, hours })
  }
  // plan the open Process work: two work items + the AUR-P-004 check + the hold-point
  // approval — checking and approving load capacity like work (I-9). 42/40 h on Process
  // → S-CAP warn + PH-A3 on the amber tier without forcing the demo red.
  const openProcessItems = repo.list<{ id: number; ref: string }>('work_item', projectId,
    "state IN ('open','in_work') AND package_id = ? LIMIT 2", [pkgId['PKG-P']!])
  for (const w of openProcessItems) {
    createPlanItem(as('planner'), {
      itemType: 'work_item', itemId: w.id, horizon: 'now', week, plannedHours: 14, discipline: 'Process',
    })
  }
  const p004Check = repo.list<Check>('check_record', projectId, 'revision_id = ?', [R('AUR-P-004')])[0]
  if (p004Check) {
    createPlanItem(as('planner'), {
      itemType: 'check', itemId: p004Check.id, horizon: 'now', week, plannedHours: 8, discipline: 'Process',
    })
  }
  const holdPointApproval = repo.list<{ id: number }>('approval_record', projectId,
    "approval_type = 'client_hold_point' LIMIT 1")[0]
  if (holdPointApproval) {
    createPlanItem(as('planner'), {
      itemType: 'approval_record', itemId: holdPointApproval.id, horizon: 'now', week, plannedHours: 6, discipline: 'Process',
    })
  }
  // a backlog entry plus a reasoned shift into next week (PEC-PLAN-006)
  const pipingItem = repo.list<{ id: number; version: number }>('work_item', projectId,
    "state IN ('open','in_work') AND package_id = ? LIMIT 1", [pkgId['PKG-PI']!])[0]
  if (pipingItem) {
    const pi = createPlanItem(as('planner'), {
      itemType: 'work_item', itemId: pipingItem.id, horizon: 'later', week: null, plannedHours: 10, discipline: 'Mechanical',
    })
    shiftPlanItem(as('planner'), pi.id, {
      version: pi.version, toHorizon: 'next', toWeek: isoWeekOf(day(7)),
      reason: 'stress inputs land Friday; pulling the line-list rework into next week',
    })
  }
  // the weekly commit generates My Week (PEC-PLAN-007 / PEC-MW-007)
  commitWeek(as('planner'), week)
})
withTx(db, () => {
  // schedule import feeding the lookahead (§16 P2, D-04)
  const schedCsv = [
    'activity_id,description,start,finish,package,deliverable_ref',
    `SCH-1010,PFD update and squad check,${day(-7)},${day(11)},PKG-P,AUR-P-002`,
    `SCH-1020,Compressor datasheet finalization,${day(0)},${day(18)},PKG-M,AUR-M-001`,
    `SCH-1030,Stress critical line list rework,${day(3)},${day(25)},PKG-PI,AUR-PI-002`,
  ].join('\r\n')
  const rep = importContract(as('admin'), 'schedule', schedCsv, false)
  if (rep.rejected.length > 0) throw new Error(`schedule seed rejected: ${JSON.stringify(rep.rejected)}`)
})

// ---------- 8. summary ----------

const count = (table: string): number =>
  (db.prepare(`SELECT COUNT(*) AS n FROM ${table}`).get() as { n: number }).n

const COUNTS: Array<[string, string]> = [
  ['person', 'person'], ['package', 'package'], ['deliverable', 'deliverable'],
  ['revision', 'revision'], ['work_item', 'work_item'], ['hold', 'hold'],
  ['check', 'check_record'], ['review_comment', 'review_comment'],
  ['approval_record', 'approval_record'], ['decision', 'decision'],
  ['condition', 'condition_record'], ['condition_template', 'condition_template'],
  ['issue_event', 'issue_event'], ['interface_item', 'interface_item'], ['risk', 'risk'],
  ['intake_item', 'intake_item'], ['plan_item', 'plan_item'], ['plan_shift', 'plan_shift'],
  ['capacity_entry', 'capacity_entry'], ['schedule_activity', 'schedule_activity'],
  ['history_entry', 'history_entry'],
  ['audit_event', 'audit_event'], ['notification', 'notification'],
]

console.log('')
console.log('════════════════════════════════════════════════════════════════════')
console.log(' PEC demo seed — project AUR "Aurora Gas Plant FEED"  (project id 1)')
console.log('════════════════════════════════════════════════════════════════════')
console.log('')
console.log(' Personas (password for ALL: pilot)')
console.log(' ──────────────────────────────────')
for (const p of PERSONS) {
  console.log(`  ${p.email.padEnd(26)} ${p.name.padEnd(20)} ${p.roles.join(', ')}${p.isAdmin ? ' (instance admin)' : ''}`)
}
console.log('')
console.log(' Record counts')
console.log(' ─────────────')
for (const [label, table] of COUNTS) {
  console.log(`  ${label.padEnd(20)} ${String(count(table)).padStart(5)}`)
}
console.log('')
console.log(' Suggested demo walks')
console.log(' ────────────────────')
console.log('  1. pm@aurora.dev → Overview: project health is RED — click the badge and every')
console.log('     KPI for the rule + contributing records; drill S-HOLD (aged vendor_data hold),')
console.log('     S-DEC (units decision blocking AUR-P-003 issue), S-APPR, S-CMT, S-INTAKE;')
console.log('     PKG-PI is red via PH-R1 (Gate 3 deliverable AUR-PI-002 slipping).')
console.log('  2. eor@aurora.dev → My Week: overdue stress items, a committed-this-week item,')
console.log('     and the open check comment owed on AUR-P-004; try closing a blocked item.')
console.log('  3. coord@aurora.dev → Registers → Intake: three untriaged items (one aged red);')
console.log('     triage one into an anchored work item, then check the raiser notification.')
console.log('  4. planner@aurora.dev → Plan (P2): Process is at 105% this week (S-CAP warn, I-9 —')
console.log('     the check and hold-point approval load capacity); the week is committed, so')
console.log("     eor's My Week shows \"planning commitment\"; the lookahead mixes plan cells with")
console.log('     imported schedule activities; one reasoned shift sits in the plan-change log.')
console.log('')
console.log(` Database: ${dbPath}`)
console.log(' Start the app:  npm run dev   (server :4810, web :4811)')
console.log('')

db.close()
