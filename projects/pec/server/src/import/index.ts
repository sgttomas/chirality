/**
 * Import/export contracts (PRD §16, SPEC §8).
 *
 * Behavior: validate row-by-row, never silently drop; reject report per row.
 * State seeding: imported records are CREATED AT their imported lifecycle state —
 * initial-state seeding, not a transition, outside the I-5 gates — with history
 * kind=import. Conditions gate subsequent transitions only. No synthetic issue events.
 * Re-import concurrency: a matched record updates only when its latest history entry is
 * itself an import entry; otherwise the row is a conflict unless force=true.
 * Round-trip: exports mirror the import schemas; RAIL export includes non-converted
 * intake items flagged unanchored.
 */

import type { Deliverable, Hold, IntakeItem, InterfaceItem, Log, PackageTracker, Revision, Risk, WorkItem } from '@pec/core'
import {
  HOLD_CAUSES, LOGS, SCHEDULE_ROW_TYPES, TRACKER_STAGE_STATES, ageWorkingDays, daysOverdue, isoWeekOf, isoWeeksFrom, lookahead, visibleLogs,
} from '@pec/core'
import { badRequest } from '../errors.ts'
import { nowIso, snakeToCamel } from '../repo.ts'
import type { Sx } from '../services/shared.ts'
import { parseTable, toCsv } from './csv.ts'
import { createRevision } from '../services/revisions.ts'

export interface ImportReport {
  contract: string
  accepted: number
  updated: number
  conflicts: Array<{ row: number; key: string; reason: string }>
  rejected: Array<{ row: number; errors: string[] }>
  intakeCreated: number
}

// ---------- shared helpers ----------

function personByNameOrEmail(sx: Sx, s: string): number | null {
  if (!s) return null
  const row = sx.db.prepare('SELECT id FROM person WHERE email = ? OR name = ?')
    .get(s, s) as { id: number } | undefined
  return row?.id ?? null
}

function normState(s: string): string {
  return s.trim().toLowerCase().replaceAll(' ', '_').replaceAll('-', '_')
}

const REV_STATES = new Map<string, Revision['state']>([
  ['in_work', 'in_work'], ['in_check', 'in_check'], ['check_accepted', 'check_accepted'],
  ['ready_for_approval', 'ready_for_approval'], ['approved', 'approved'], ['issued', 'issued'],
  ['returned_with_comments', 'returned_with_comments'], ['superseded', 'superseded'],
  ['ifr', 'issued'], ['ifa', 'issued'], ['ifc', 'issued'],
])

const WI_STATES = new Map<string, WorkItem['state']>([
  ['open', 'open'], ['in_work', 'in_work'], ['in_progress', 'in_work'], ['started', 'in_work'],
  ['closed', 'closed'], ['complete', 'closed'], ['completed', 'closed'], ['done', 'closed'],
  ['cancelled', 'cancelled'], ['canceled', 'cancelled'],
])

const DATE_RE = /^\d{4}-\d{2}-\d{2}$/

/** Latest history entry for a record is an import entry → safe to re-import (resolution 3). */
function lastChangeIsImport(sx: Sx, recordType: string, recordId: number): boolean {
  const rows = sx.db.prepare(
    'SELECT kind FROM history_entry WHERE record_type = ? AND record_id = ? ORDER BY id DESC LIMIT 1',
  ).all(recordType, recordId) as Array<{ kind: string }>
  return rows.length === 0 || rows[0]!.kind === 'import' || rows[0]!.kind === 'created'
}

function importHistory(sx: Sx, recordType: string, recordId: number, summary: string): void {
  sx.repo.history({
    projectId: sx.projectId, recordType: recordType as never, recordId,
    actorId: sx.session.personId, kind: 'import', summary, payload: null, authorityRef: null,
  })
}

// ---------- MDL ----------

function importMdl(sx: Sx, csv: string, force: boolean): ImportReport {
  const report: ImportReport = { contract: 'mdl', accepted: 0, updated: 0, conflicts: [], rejected: [], intakeCreated: 0 }
  const { headers, rows } = parseTable(csv)
  const required = ['doc_no', 'title', 'package', 'discipline', 'owner', 'current_rev', 'state', 'due_date']
  const missing = required.filter((h) => !headers.includes(h))
  if (missing.length > 0) throw badRequest(`MDL import missing required columns: ${missing.join(', ')} (§16)`)

  // §16 optional package-attribute columns (D-PEC-23): present headers refresh the
  // auto-created package record; processed once per package per run
  const hasPkgAttrs = ['package_name', 'area', 'package_type'].some((h) => headers.includes(h))
  const pkgAttrsApplied = new Set<number>()

  rows.forEach((row, i) => {
    const rowNo = i + 2
    const errors: string[] = []
    for (const col of ['doc_no', 'title', 'package', 'current_rev', 'state']) {
      if (!row[col]) errors.push(`${col} is required`)
    }
    const state = REV_STATES.get(normState(row.state ?? ''))
    if (row.state && !state) errors.push(`unrecognized state "${row.state}" (accepted: ${[...new Set(REV_STATES.values())].join(', ')})`)
    if (row.due_date && !DATE_RE.test(row.due_date)) errors.push(`due_date must be YYYY-MM-DD, got "${row.due_date}"`)
    const ownerId = row.owner ? personByNameOrEmail(sx, row.owner) : null
    if (row.owner && ownerId == null) errors.push(`owner "${row.owner}" matches no person (email or exact name)`)
    if (errors.length > 0) { report.rejected.push({ row: rowNo, errors }); return }

    // package: auto-create on first sight (adoption bridge)
    let pkg = sx.db.prepare('SELECT id, name, area, package_type FROM package WHERE project_id = ? AND code = ?')
      .get(sx.projectId, row.package ?? '') as { id: number; name: string; area: string | null; package_type: string | null } | undefined
    if (!pkg) {
      const pkgId = sx.repo.insert('package', {
        projectId: sx.projectId, code: row.package,
        name: row.package_name || row.package,
        area: row.area || null, packageType: row.package_type || null,
      })
      importHistory(sx, 'package', pkgId, `package ${row.package} created by MDL import`)
      pkg = { id: pkgId, name: row.package_name || row.package!, area: row.area || null, package_type: row.package_type || null }
      pkgAttrsApplied.add(pkgId)
    } else if (hasPkgAttrs && !pkgAttrsApplied.has(pkg.id)) {
      // optional columns update only when present (§16, schedule/tracker precedent) —
      // and only through the same import-ownership guard as every other record
      const attrs: Record<string, unknown> = {}
      if (headers.includes('package_name') && row.package_name && row.package_name !== pkg.name) attrs.name = row.package_name
      if (headers.includes('area') && (row.area || null) !== pkg.area) attrs.area = row.area || null
      if (headers.includes('package_type') && (row.package_type || null) !== pkg.package_type) attrs.packageType = row.package_type || null
      if (Object.keys(attrs).length > 0) {
        if (!lastChangeIsImport(sx, 'package', pkg.id) && !force) {
          report.conflicts.push({ row: rowNo, key: row.package!, reason: 'package edited in-app since last import; attributes not updated (deliverable row still processed); use force=true' })
        } else {
          sx.repo.systemUpdate('package', sx.projectId, pkg.id, attrs)
          importHistory(sx, 'package', pkg.id, `package ${row.package} attributes refreshed by MDL import`)
        }
      }
      pkgAttrsApplied.add(pkg.id)
    }

    const existing = sx.db.prepare('SELECT id, version FROM deliverable WHERE project_id = ? AND doc_no = ?')
      .get(sx.projectId, row.doc_no ?? '') as { id: number; version: number } | undefined
    const fields = {
      packageId: pkg.id, title: row.title, discipline: row.discipline || null,
      deliverableType: row.deliverable_type || null, ownerId,
      dueDate: row.due_date || null, milestone: row.milestone || null,
      issuePurposePlan: row.issue_purpose_plan || null, dcRef: row.edms_ref || null,
      clientNo: row.client_no || null, remarks: row.remarks || null,
    }
    if (existing) {
      if (!lastChangeIsImport(sx, 'deliverable', existing.id) && !force) {
        report.conflicts.push({ row: rowNo, key: row.doc_no!, reason: 'edited in-app since last import; re-run with force=true to overwrite (PEC-NFR-004)' })
        return
      }
      sx.repo.systemUpdate('deliverable', sx.projectId, existing.id, fields)
      importHistory(sx, 'deliverable', existing.id, `${row.doc_no} updated by MDL import`)
      // revision: new current_rev → create at imported state (seeding)
      const currentRev = sx.repo.list<Revision>('revision', sx.projectId,
        "deliverable_id = ? AND state != 'superseded'", [existing.id]).sort((a, b) => b.id - a.id)[0]
      if (!currentRev || currentRev.revCode !== row.current_rev) {
        // A new rev code → create at the imported state (initial-state seeding, outside the gates).
        const rev = createRevision(sx, { deliverableId: existing.id, revCode: row.current_rev! },
          { skipPermission: true, initialState: state })
        importHistory(sx, 'revision', rev.id, `${row.doc_no} rev ${row.current_rev} seeded at ${state} by MDL import`)
      } else if (currentRev.state !== state) {
        // The rev already exists in-system: its lifecycle state is under transition control.
        // Import must NEVER advance it past the issue gate (I-5, D-11) — it can only seed a
        // brand-new record. Metadata was still updated; the state field is ignored and reported.
        report.conflicts.push({
          row: rowNo, key: `${row.doc_no} rev ${row.current_rev}`,
          reason: `revision already exists in state '${currentRev.state}'; import will not force it to '${state}' — issue-affecting transitions must go through the gated workflow (I-5). Metadata updated.`,
        })
      }
      report.updated++
    } else {
      const id = sx.repo.insert('deliverable', { projectId: sx.projectId, docNo: row.doc_no, ...fields })
      importHistory(sx, 'deliverable', id, `${row.doc_no} created by MDL import (as-imported state ${state})`)
      const rev = createRevision(sx, { deliverableId: id, revCode: row.current_rev! },
        { skipPermission: true, initialState: state })
      importHistory(sx, 'revision', rev.id, `${row.doc_no} rev ${row.current_rev} seeded at ${state} by MDL import`)
      report.accepted++
    }
  })
  return report
}

// ---------- RAIL ----------

function importRail(sx: Sx, csv: string, force: boolean): ImportReport {
  const report: ImportReport = { contract: 'rail', accepted: 0, updated: 0, conflicts: [], rejected: [], intakeCreated: 0 }
  const { headers, rows } = parseTable(csv)
  const required = ['item_id', 'statement', 'type', 'log', 'owner', 'need_by', 'status', 'raised_by', 'raised_date']
  const missing = required.filter((h) => !headers.includes(h))
  if (missing.length > 0) throw badRequest(`RAIL import missing required columns: ${missing.join(', ')} (§16)`)

  const WI_KINDS = new Set(['action', 'coordination', 'risk_treatment', 'rework', 'other', 'task'])

  rows.forEach((row, i) => {
    const rowNo = i + 2
    const errors: string[] = []
    for (const col of required) if (!row[col]) errors.push(`${col} is required`)
    const log = (row.log ?? '').toLowerCase() as Log
    if (row.log && !LOGS.includes(log)) errors.push(`log must be one of ${LOGS.join(', ')}`)
    const type = normState(row.type ?? '')
    const isHold = type === 'hold'
    const isInterface = type === 'interface'
    if (!isHold && !isInterface && !WI_KINDS.has(type)) {
      errors.push(`unrecognized type "${row.type}" (accepted: ${[...WI_KINDS].join(', ')}, hold, interface)`)
    }
    const ownerId = personByNameOrEmail(sx, row.owner ?? '')
    if (row.owner && ownerId == null) errors.push(`owner "${row.owner}" matches no person`)
    const raisedBy = personByNameOrEmail(sx, row.raised_by ?? '') ?? ownerId
    if (row.need_by && !DATE_RE.test(row.need_by)) errors.push('need_by must be YYYY-MM-DD')
    const wiState = isHold || isInterface ? null : WI_STATES.get(normState(row.status ?? ''))
    if (!isHold && !isInterface && row.status && !wiState) errors.push(`unrecognized status "${row.status}"`)
    if (isHold && !row.hold_cause) errors.push('hold rows require hold_cause (I-3)')
    if (isHold && row.hold_cause && !HOLD_CAUSES.includes(normState(row.hold_cause) as never)) {
      errors.push(`hold_cause must be one of ${HOLD_CAUSES.join(', ')}`)
    }
    if (errors.length > 0) { report.rejected.push({ row: rowNo, errors }); return }

    // anchor resolution
    const deliverable = row.deliverable_ref
      ? sx.db.prepare('SELECT id FROM deliverable WHERE project_id = ? AND doc_no = ?')
        .get(sx.projectId, row.deliverable_ref ?? '') as { id: number } | undefined
      : undefined

    // idempotency: item_id matches one of our refs → update path
    const table = isHold ? 'hold' : isInterface ? 'interface_item' : 'work_item'
    const existing = sx.db.prepare(`SELECT id, version FROM ${table} WHERE project_id = ? AND ref = ?`)
      .get(sx.projectId, row.item_id ?? '') as { id: number; version: number } | undefined
    if (existing) {
      if (!lastChangeIsImport(sx, table === 'hold' ? 'hold' : table === 'interface_item' ? 'interface_item' : 'work_item', existing.id) && !force) {
        report.conflicts.push({ row: rowNo, key: row.item_id!, reason: 'edited in-app since last import; use force=true' })
        return
      }
      if (table === 'work_item') {
        sx.repo.systemUpdate('work_item', sx.projectId, existing.id, {
          statement: row.statement, needBy: row.need_by || null, state: wiState,
          ...(headers.includes('area') ? { area: row.area || null } : {}),
          ...(wiState === 'closed' ? { closedAt: row.closed_date ? `${row.closed_date}T00:00:00Z` : nowIso() } : {}),
        })
      }
      importHistory(sx, table, existing.id, `${row.item_id} updated by RAIL import`)
      report.updated++
      return
    }

    if (!deliverable) {
      // RAIL anchors on deliverable_ref match only (PRD §16); everything else lands unanchored.
      // Idempotency (D-PEC-08, evidence-03 seam finding): a row that already landed as an
      // undispositioned intake item — matched by its verbatim "[item_id] " prefix — updates
      // that item's mutable fields instead of duplicating it. The statement itself is
      // trigger-frozen (OM-3): a changed statement is a conflict, never a silent rewrite.
      const prefix = `[${row.item_id}] `
      const priorIntake = sx.db.prepare(
        "SELECT id, version, statement_verbatim FROM intake_item WHERE project_id = ? AND state != 'dispositioned' AND substr(statement_verbatim, 1, ?) = ?",
      ).get(sx.projectId, prefix.length, prefix) as { id: number; version: number; statement_verbatim: string } | undefined
      if (priorIntake) {
        if (!lastChangeIsImport(sx, 'intake_item', priorIntake.id) && !force) {
          report.conflicts.push({ row: rowNo, key: row.item_id!, reason: 'edited in-app since last import; use force=true' })
          return
        }
        if (priorIntake.statement_verbatim !== `${prefix}${row.statement}`) {
          report.conflicts.push({
            row: rowNo, key: row.item_id!,
            reason: 'intake statement is preserved verbatim (OM-3) and the imported statement differs; disposition the existing intake item or use a new item_id. Other fields not updated.',
          })
          return
        }
        sx.repo.systemUpdate('intake_item', sx.projectId, priorIntake.id, {
          needBy: row.need_by || null, suggestedOwnerId: ownerId,
          anchorSuggestion: row.deliverable_ref || row.package || null, log,
          ...(headers.includes('area') ? { area: row.area || null } : {}),
        })
        importHistory(sx, 'intake_item', priorIntake.id, `updated from RAIL row ${row.item_id} (still unanchored)`)
        report.updated++
        return
      }
      // No resolvable anchor: the row lands as an intake item flagged unanchored (I-2).
      const ref = sx.repo.nextRef(sx.projectId, 'intake_item')
      const quickType = isHold ? 'hold' : isInterface ? 'interface' : 'action'
      const id = sx.repo.insert('intake_item', {
        projectId: sx.projectId, ref,
        statementVerbatim: `[${row.item_id}] ${row.statement}`,
        quickType, anchorSuggestion: row.deliverable_ref || row.package || null,
        needBy: row.need_by || null, suggestedOwnerId: ownerId,
        log, raisedBy: raisedBy ?? sx.session.personId,
        raisedAt: row.raised_date ? `${row.raised_date}T00:00:00Z` : nowIso(),
        state: 'raised', area: row.area || null,
      })
      importHistory(sx, 'intake_item', id, `${ref} created unanchored from RAIL row ${row.item_id} (anchor "${row.deliverable_ref ?? ''}" unmatched)`)
      report.intakeCreated++
      return
    }

    if (isHold) {
      // item_id is the idempotency key (re-import lookup binds `ref = item_id`, ~line 194);
      // store it so re-importing the same RAIL row updates instead of duplicating (§16).
      const holdRef = row.item_id!
      const currentRev = sx.repo.list<Revision>('revision', sx.projectId,
        "deliverable_id = ? AND state != 'superseded'", [deliverable!.id]).sort((a, b) => b.id - a.id)[0]
      const holdId = sx.repo.insert('hold', {
        projectId: sx.projectId, ref: holdRef, title: row.statement!.slice(0, 140),
        cause: normState(row.hold_cause!), statement: row.statement,
        ownerId: ownerId!, needBy: row.need_by,
        raisedBy: raisedBy ?? sx.session.personId,
        raisedAt: row.raised_date ? `${row.raised_date}T00:00:00Z` : nowIso(),
        state: normState(row.status ?? '') === 'closed' ? 'resolved' : 'active',
        log,
      })
      sx.repo.insert('hold_link', {
        holdId,
        targetType: currentRev ? 'revision' : 'deliverable',
        targetId: currentRev ? currentRev.id : deliverable!.id,
      })
      importHistory(sx, 'hold', holdId, `${holdRef} created from RAIL row ${row.item_id}, blocks ${row.deliverable_ref}`)
      report.accepted++
      return
    }
    if (isInterface) {
      const iref = row.item_id!
      const iid = sx.repo.insert('interface_item', {
        projectId: sx.projectId, ref: iref, title: row.statement!.slice(0, 140),
        givingParty: row.package ?? 'unknown', receivingParty: row.deliverable_ref ?? 'unknown',
        requiredInfo: row.statement, needBy: row.need_by || null, state: 'open', log,
      })
      importHistory(sx, 'interface_item', iid, `${iref} created from RAIL row ${row.item_id}`)
      report.accepted++
      return
    }

    const wiRef = row.item_id!
    const pkgId = deliverable
      ? (sx.repo.get<Deliverable>('deliverable', sx.projectId, deliverable.id)).packageId
      : null
    const wid = sx.repo.insert('work_item', {
      projectId: sx.projectId, ref: wiRef, title: row.statement!.slice(0, 140),
      statement: row.statement, kind: type === 'task' ? 'action' : type, log,
      anchorType: 'deliverable', anchorId: deliverable!.id, packageId: pkgId,
      ownerId: ownerId!, needBy: row.need_by, state: wiState, area: row.area || null,
      ...(wiState === 'closed' ? { closedAt: row.closed_date ? `${row.closed_date}T00:00:00Z` : nowIso(), closingStatement: row.notes || null } : {}),
      createdBy: raisedBy ?? sx.session.personId,
      createdAt: row.raised_date ? `${row.raised_date}T00:00:00Z` : nowIso(),
    })
    importHistory(sx, 'work_item', wid, `${wiRef} created from RAIL row ${row.item_id} at state ${wiState} (seeding)`)
    report.accepted++
  })
  return report
}

// ---------- decisions ----------

function importDecisions(sx: Sx, csv: string, force: boolean): ImportReport {
  const report: ImportReport = { contract: 'decisions', accepted: 0, updated: 0, conflicts: [], rejected: [], intakeCreated: 0 }
  const { headers, rows } = parseTable(csv)
  const required = ['decision_id', 'title', 'statement', 'authority', 'need_by', 'status']
  const missing = required.filter((h) => !headers.includes(h))
  if (missing.length > 0) throw badRequest(`decision import missing required columns: ${missing.join(', ')} (§16)`)
  const STATES = new Map([
    ['identified', 'identified'], ['in_progress', 'in_progress'], ['pending', 'pending'],
    ['pending_decision', 'pending'], ['decided', 'decided'], ['superseded', 'superseded'],
  ])
  rows.forEach((row, i) => {
    const rowNo = i + 2
    const errors: string[] = []
    for (const col of ['decision_id', 'title', 'statement', 'authority', 'status']) {
      if (!row[col]) errors.push(`${col} is required`)
    }
    const state = STATES.get(normState(row.status ?? ''))
    if (row.status && !state) errors.push(`unrecognized status "${row.status}"`)
    const authorityId = personByNameOrEmail(sx, row.authority ?? '')
    if (row.authority && authorityId == null) errors.push(`authority "${row.authority}" matches no person`)
    if (state === 'decided' && !row.outcome) errors.push('decided rows require outcome')
    if (row.open_date && !DATE_RE.test(row.open_date)) errors.push(`open_date must be YYYY-MM-DD, got "${row.open_date}"`)
    if (errors.length > 0) { report.rejected.push({ row: rowNo, errors }); return }
    // §16 optional columns (D-PEC-23): update only when the header is present
    const optCols: Record<string, unknown> = {}
    if (headers.includes('open_date')) optCols.openDate = row.open_date || null
    if (headers.includes('area')) optCols.area = row.area || null
    if (headers.includes('source')) optCols.source = row.source || null

    const existing = sx.db.prepare('SELECT id FROM decision WHERE project_id = ? AND ref = ?')
      .get(sx.projectId, row.decision_id ?? '') as { id: number } | undefined
    if (existing) {
      if (!lastChangeIsImport(sx, 'decision', existing.id) && !force) {
        report.conflicts.push({ row: rowNo, key: row.decision_id!, reason: 'edited in-app since last import; use force=true' })
        return
      }
      sx.repo.systemUpdate('decision', sx.projectId, existing.id, {
        title: row.title, statement: row.statement, needBy: row.need_by || null, state,
        outcome: row.outcome ? normState(row.outcome) : null, rationale: row.rationale || null,
        ...optCols,
      })
      importHistory(sx, 'decision', existing.id, `${row.decision_id} updated by decision-log import`)
      report.updated++
      return
    }
    // The external decision_id IS the idempotency key (the re-import lookup binds `ref = decision_id`,
    // index.ts ~309). Store it verbatim so re-imports match and update instead of duplicating (§16).
    const ref = row.decision_id!
    const id = sx.repo.insert('decision', {
      projectId: sx.projectId, ref, title: row.title, statement: row.statement,
      preparerId: row.preparer ? personByNameOrEmail(sx, row.preparer) : null,
      authorityId: authorityId!, needBy: row.need_by || null, state,
      outcome: row.outcome ? normState(row.outcome) : null, rationale: row.rationale || null,
      decidedAt: row.decided_date ? `${row.decided_date}T00:00:00Z` : null,
      kind: 'standalone', log: 'internal', createdAt: nowIso(), ...optCols,
    })
    importHistory(sx, 'decision', id, `${ref} created from decision-log row ${row.decision_id} at state ${state} (seeding)`)
    for (const affected of (row.affected_refs ?? '').split(';').map((s) => s.trim()).filter(Boolean)) {
      const d = sx.db.prepare('SELECT id FROM deliverable WHERE project_id = ? AND doc_no = ?')
        .get(sx.projectId, affected) as { id: number } | undefined
      if (d) sx.repo.insert('decision_link', { decisionId: id, recordType: 'deliverable', recordId: d.id, relation: 'affects' })
    }
    report.accepted++
  })
  return report
}

// ---------- risks ----------

function importRisks(sx: Sx, csv: string, force: boolean): ImportReport {
  const report: ImportReport = { contract: 'risks', accepted: 0, updated: 0, conflicts: [], rejected: [], intakeCreated: 0 }
  const { headers, rows } = parseTable(csv)
  const required = ['risk_id', 'title', 'cause', 'consequence', 'owner', 'status']
  const missing = required.filter((h) => !headers.includes(h))
  if (missing.length > 0) throw badRequest(`risk import missing required columns: ${missing.join(', ')} (§16)`)
  const STATES = new Map([['open', 'open'], ['mitigating', 'mitigating'], ['treating', 'mitigating'], ['closed', 'closed']])
  rows.forEach((row, i) => {
    const rowNo = i + 2
    const errors: string[] = []
    for (const col of ['risk_id', 'title', 'status']) if (!row[col]) errors.push(`${col} is required`)
    const state = STATES.get(normState(row.status ?? ''))
    if (row.status && !state) errors.push(`unrecognized status "${row.status}"`)
    const ownerId = row.owner ? personByNameOrEmail(sx, row.owner) : null
    if (row.owner && ownerId == null) errors.push(`owner "${row.owner}" matches no person`)
    for (const n of ['probability', 'impact', 'residual_probability', 'residual_impact'] as const) {
      if (row[n] && !/^[1-5]$/.test(row[n]!)) errors.push(`${n} must be 1-5`)
    }
    if (errors.length > 0) { report.rejected.push({ row: rowNo, errors }); return }

    const pkg = row.package
      ? sx.db.prepare('SELECT id FROM package WHERE project_id = ? AND code = ?').get(sx.projectId, row.package ?? '') as { id: number } | undefined
      : undefined
    const del = row.deliverable_ref
      ? sx.db.prepare('SELECT id FROM deliverable WHERE project_id = ? AND doc_no = ?').get(sx.projectId, row.deliverable_ref ?? '') as { id: number } | undefined
      : undefined
    const existing = sx.db.prepare('SELECT id FROM risk WHERE project_id = ? AND ref = ?')
      .get(sx.projectId, row.risk_id ?? '') as { id: number } | undefined
    const fields: Record<string, unknown> = {
      title: row.title, cause: row.cause || null, consequence: row.consequence || null,
      packageId: pkg?.id ?? null, deliverableId: del?.id ?? null, ownerId,
      probability: row.probability ? Number(row.probability) : null,
      impact: row.impact ? Number(row.impact) : null,
      mitigation: row.mitigation || null, needBy: row.need_by || null, state,
    }
    // §16 optional columns (D-PEC-23): update only when the header is present
    if (headers.includes('category')) fields.category = row.category || null
    if (headers.includes('risk_type')) fields.riskType = row.risk_type || null
    if (headers.includes('treatment')) fields.treatment = row.treatment || null
    if (headers.includes('residual_probability')) fields.residualProbability = row.residual_probability ? Number(row.residual_probability) : null
    if (headers.includes('residual_impact')) fields.residualImpact = row.residual_impact ? Number(row.residual_impact) : null
    if (existing) {
      if (!lastChangeIsImport(sx, 'risk', existing.id) && !force) {
        report.conflicts.push({ row: rowNo, key: row.risk_id!, reason: 'edited in-app since last import; use force=true' })
        return
      }
      sx.repo.systemUpdate('risk', sx.projectId, existing.id, fields)
      importHistory(sx, 'risk', existing.id, `${row.risk_id} updated by risk-log import`)
      report.updated++
    } else {
      // The external risk_id IS the idempotency key (re-import lookup binds `ref = risk_id`,
      // index.ts ~372). Store it verbatim so re-imports match and update instead of duplicating (§16).
      const ref = row.risk_id!
      const id = sx.repo.insert('risk', { projectId: sx.projectId, ref, ...fields })
      importHistory(sx, 'risk', id, `${ref} created from risk-log row ${row.risk_id} (seeding)`)
      report.accepted++
    }
  })
  return report
}

// ---------- schedule activities (§16 P2, D-04: CSV/XER-derived, no live sync) ----------

function importSchedule(sx: Sx, csv: string, _force: boolean): ImportReport {
  const report: ImportReport = { contract: 'schedule', accepted: 0, updated: 0, conflicts: [], rejected: [], intakeCreated: 0 }
  const { headers, rows } = parseTable(csv)
  const required = ['activity_id', 'description', 'start', 'finish']
  const missing = required.filter((h) => !headers.includes(h))
  if (missing.length > 0) throw badRequest(`schedule import missing required columns: ${missing.join(', ')} (§16 P2)`)

  rows.forEach((row, i) => {
    const rowNo = i + 2
    const errors: string[] = []
    for (const col of required) if (!row[col]) errors.push(`${col} is required`)
    for (const col of ['start', 'finish'] as const) {
      if (row[col] && !DATE_RE.test(row[col]!)) errors.push(`${col} must be YYYY-MM-DD, got "${row[col]}"`)
    }
    if (row.start && row.finish && DATE_RE.test(row.start) && DATE_RE.test(row.finish) && row.finish < row.start) {
      errors.push('finish is before start')
    }
    // §16 optional WBS columns (D-PEC-23): validated when present, never silently coerced
    const rowType = row.row_type ? normState(row.row_type) : null
    if (rowType && !(SCHEDULE_ROW_TYPES as readonly string[]).includes(rowType)) {
      errors.push(`unrecognized row_type "${row.row_type}" (accepted: ${SCHEDULE_ROW_TYPES.join(', ')})`)
    }
    if (row.outline_level && !/^\d+$/.test(row.outline_level)) errors.push(`outline_level must be a non-negative integer, got "${row.outline_level}"`)
    if (row.percent_complete && !/^\d+$/.test(row.percent_complete)) errors.push(`percent_complete must be an integer 0-100, got "${row.percent_complete}"`)
    if (row.percent_complete && /^\d+$/.test(row.percent_complete) && Number(row.percent_complete) > 100) {
      errors.push(`percent_complete must be an integer 0-100, got "${row.percent_complete}"`)
    }
    if (row.duration_days && !/^\d+(\.\d+)?$/.test(row.duration_days)) errors.push(`duration_days must be a number, got "${row.duration_days}"`)
    for (const col of ['baseline_start', 'baseline_finish'] as const) {
      if (row[col] && !DATE_RE.test(row[col]!)) errors.push(`${col} must be YYYY-MM-DD, got "${row[col]}"`)
    }
    // package/deliverable mapping is optional, but a stated mapping must resolve —
    // silently dropping it would be a silent drop of data (§16)
    const pkg = row.package
      ? sx.db.prepare('SELECT id FROM package WHERE project_id = ? AND code = ?')
        .get(sx.projectId, row.package) as { id: number } | undefined
      : undefined
    if (row.package && !pkg) errors.push(`package "${row.package}" matches no package code`)
    const del = row.deliverable_ref
      ? sx.db.prepare('SELECT id FROM deliverable WHERE project_id = ? AND doc_no = ?')
        .get(sx.projectId, row.deliverable_ref) as { id: number } | undefined
      : undefined
    if (row.deliverable_ref && !del) errors.push(`deliverable_ref "${row.deliverable_ref}" matches no doc_no`)
    if (errors.length > 0) { report.rejected.push({ row: rowNo, errors }); return }

    // mapping columns update only when present in the CSV — a narrower re-import must not
    // silently wipe an earlier mapping (§16: nothing dropped without a report)
    const fields: Record<string, unknown> = {
      description: row.description, startDate: row.start, finishDate: row.finish,
    }
    if (headers.includes('package')) fields.packageId = pkg?.id ?? null
    if (headers.includes('deliverable_ref')) fields.deliverableId = del?.id ?? null
    if (headers.includes('row_type')) fields.rowType = rowType
    if (headers.includes('outline_level')) fields.outlineLevel = row.outline_level ? Number(row.outline_level) : null
    if (headers.includes('parent_activity_id')) fields.parentActivityId = row.parent_activity_id || null
    if (headers.includes('percent_complete')) fields.percentComplete = row.percent_complete ? Number(row.percent_complete) : null
    if (headers.includes('duration_days')) fields.durationDays = row.duration_days ? Number(row.duration_days) : null
    if (headers.includes('baseline_start')) fields.baselineStart = row.baseline_start || null
    if (headers.includes('baseline_finish')) fields.baselineFinish = row.baseline_finish || null
    const existing = sx.db.prepare('SELECT id FROM schedule_activity WHERE project_id = ? AND activity_id = ?')
      .get(sx.projectId, row.activity_id ?? '') as { id: number } | undefined
    if (existing) {
      // schedule rows are import-owned (no in-app edit path); re-import always refreshes
      sx.repo.systemUpdate('schedule_activity', sx.projectId, existing.id, fields)
      importHistory(sx, 'schedule_activity', existing.id, `${row.activity_id} refreshed by schedule import`)
      report.updated++
    } else {
      const id = sx.repo.insert('schedule_activity', {
        projectId: sx.projectId, activityId: row.activity_id, ...fields,
      })
      importHistory(sx, 'schedule_activity', id, `${row.activity_id} created by schedule import`)
      report.accepted++
    }
  })
  return report
}

// ---------- Package Tracker (§16 sixth contract, D-PEC-13 as amended) ----------
// One row per package: the `package` column is row-required and must resolve to an existing
// package.code — the idempotency key (owner amendment: "match the tracker entries with the
// PKG-#### numbers"). The CoA tracking number is kept verbatim as plain, non-unique data.

/** The 12 procurement-stage columns, in contract order (CSV columns ≡ export columns). */
const TRACKER_STAGE_COLS = [
  'stage_budgetary_datasheet', 'stage_cost_estimate', 'stage_package_datasheet', 'stage_package',
  'stage_rfq', 'stage_review', 'stage_vendor_bids', 'stage_clarifications', 'stage_evaluation',
  'stage_eng_req', 'stage_po', 'stage_databook',
] as const

const TRACKER_OPTIONAL_COLS = [
  'package_type_approved', 'package_type_proposed', 'line_items', 'vendors_engaged',
  'vendor_awarded', 'expected_delivery_date', 'cost_estimate_cad', 'comments',
] as const

function importTracker(sx: Sx, csv: string, _force: boolean): ImportReport {
  const report: ImportReport = { contract: 'tracker', accepted: 0, updated: 0, conflicts: [], rejected: [], intakeCreated: 0 }
  const { headers, rows } = parseTable(csv)
  // tracking_no stays header-required (the weekly file always carries it, and the check
  // catches column drift early) but is row-optional
  const required = ['tracking_no', 'package_name', 'discipline', 'area', ...TRACKER_STAGE_COLS, 'package']
  const missing = required.filter((h) => !headers.includes(h))
  if (missing.length > 0) throw badRequest(`tracker import missing required columns: ${missing.join(', ')} (§16)`)

  const seen = new Set<string>()
  rows.forEach((row, i) => {
    const rowNo = i + 2
    const errors: string[] = []
    for (const col of ['package_name', 'package']) if (!row[col]) errors.push(`${col} is required`)
    const stages: Record<string, string | null> = {}
    for (const col of TRACKER_STAGE_COLS) {
      if (!row[col]) { stages[col] = null; continue } // blank stored null
      const v = normState(row[col]!)
      if (!(TRACKER_STAGE_STATES as readonly string[]).includes(v)) {
        // unrecognized stage values reject the row — never silently coerced (D-PEC-13)
        errors.push(`unrecognized ${col} "${row[col]}" (accepted: ${TRACKER_STAGE_STATES.join(', ')})`)
        continue
      }
      stages[col] = v
    }
    if (row.expected_delivery_date && !DATE_RE.test(row.expected_delivery_date)) {
      errors.push(`expected_delivery_date must be YYYY-MM-DD, got "${row.expected_delivery_date}"`)
    }
    // the package IS the idempotency key (owner amendment): row-required, must resolve —
    // an unresolvable key is a data gap and rejects the row, never silently dropped (§16).
    // NO intake fallback (ruled divergence from RAIL): intakeCreated stays 0 by construction.
    const pkg = row.package
      ? sx.db.prepare('SELECT id FROM package WHERE project_id = ? AND code = ?')
        .get(sx.projectId, row.package) as { id: number } | undefined
      : undefined
    if (row.package && !pkg) errors.push(`package "${row.package}" matches no package code`)
    if (errors.length > 0) { report.rejected.push({ row: rowNo, errors }); return }

    // within-file duplicate keys: the first valid occurrence wins; later ones are conflicts,
    // never applied, never silent (D-PEC-13)
    if (seen.has(row.package!)) {
      report.conflicts.push({ row: rowNo, key: row.package!, reason: 'duplicate package in file; first occurrence applied, this one skipped' })
      return
    }
    seen.add(row.package!)

    // optional columns update only when present in the CSV — a narrower re-import must not
    // silently wipe earlier data (§16: nothing dropped without a report)
    const fields: Record<string, unknown> = {
      trackingNo: row.tracking_no || null, // kept verbatim; plain data, never keyed on
      packageName: row.package_name, discipline: row.discipline || null, area: row.area || null,
    }
    for (const col of TRACKER_STAGE_COLS) fields[snakeToCamel(col)] = stages[col]
    for (const col of TRACKER_OPTIONAL_COLS) {
      if (headers.includes(col)) fields[snakeToCamel(col)] = row[col] || null
    }

    const existing = sx.db.prepare('SELECT id FROM package_tracker WHERE project_id = ? AND package_id = ?')
      .get(sx.projectId, pkg!.id) as { id: number } | undefined
    if (existing) {
      // tracker rows are import-owned (no in-app edit path); re-import always refreshes
      sx.repo.systemUpdate('package_tracker', sx.projectId, existing.id, fields)
      importHistory(sx, 'package_tracker', existing.id, `${row.package} tracker row refreshed by tracker import`)
      report.updated++
    } else {
      const id = sx.repo.insert('package_tracker', {
        projectId: sx.projectId, packageId: pkg!.id, ...fields,
      })
      importHistory(sx, 'package_tracker', id, `${row.package} tracker row created by tracker import`)
      report.accepted++
    }
  })
  return report
}

export function importContract(sx: Sx, contract: string, csv: string, force: boolean): ImportReport {
  switch (contract) {
    case 'mdl': return importMdl(sx, csv, force)
    case 'rail': return importRail(sx, csv, force)
    case 'decisions': return importDecisions(sx, csv, force)
    case 'risks': return importRisks(sx, csv, force)
    case 'schedule': return importSchedule(sx, csv, force)
    case 'tracker': return importTracker(sx, csv, force)
    default: throw badRequest(`unknown import contract: ${contract} (mdl, rail, decisions, risks, schedule, tracker)`)
  }
}

// ---------- exports (mirror import schemas; round-trip §16) ----------

function personName(sx: Sx, id: number | null): string {
  if (id == null) return ''
  const row = sx.db.prepare('SELECT email FROM person WHERE id = ?').get(id) as { email: string } | undefined
  return row?.email ?? ''
}

export function exportRegister(sx: Sx, register: string): string {
  const snap = sx.repo.snapshot(sx.projectId)
  const pkgCode = (id: number | null): string => snap.packages.find((p) => p.id === id)?.code ?? ''
  const docNo = (id: number | null): string => snap.deliverables.find((d) => d.id === id)?.docNo ?? ''

  switch (register) {
    case 'mdl': {
      const headers = ['doc_no', 'title', 'package', 'discipline', 'owner', 'current_rev', 'state', 'due_date',
        'milestone', 'issue_purpose_plan', 'edms_ref', 'client_no', 'remarks', 'deliverable_type',
        'package_name', 'area', 'package_type']
      const rows = snap.deliverables.map((d) => {
        const revs = snap.revisions.filter((r) => r.deliverableId === d.id && r.state !== 'superseded').sort((a, b) => b.id - a.id)
        const cur = revs[0]
        const pkg = snap.packages.find((p) => p.id === d.packageId)
        return [d.docNo, d.title, pkgCode(d.packageId), d.discipline, personName(sx, d.ownerId),
          cur?.revCode ?? '', cur?.state ?? '', d.dueDate, d.milestone, d.issuePurposePlan,
          d.dcRef, d.clientNo, d.remarks, d.deliverableType,
          pkg?.name ?? '', pkg?.area ?? '', pkg?.packageType ?? '']
      })
      return toCsv(headers, rows)
    }
    case 'rail': {
      const headers = ['item_id', 'statement', 'type', 'log', 'owner', 'need_by', 'status', 'raised_by', 'raised_date',
        'package', 'deliverable_ref', 'hold_cause', 'closed_date', 'notes', 'anchor_status', 'area']
      const rows: Array<Array<string | null>> = []
      for (const w of snap.workItems as WorkItem[]) {
        rows.push([w.ref, w.statement ?? w.title, w.kind, w.log, personName(sx, w.ownerId), w.needBy, w.state,
          personName(sx, w.createdBy), w.createdAt.slice(0, 10),
          pkgCode(w.packageId), w.anchorType === 'deliverable' ? docNo(w.anchorId) : '', '',
          w.closedAt?.slice(0, 10) ?? '', w.closingStatement ?? '', 'anchored', w.area ?? ''])
      }
      for (const h of snap.holds as Hold[]) {
        if (h.state === 'withdrawn') continue
        const link = snap.holdLinks.find((l) => l.holdId === h.id)
        const anchor = link?.targetType === 'deliverable' ? docNo(link.targetId)
          : link?.targetType === 'revision' ? docNo(snap.revisions.find((r) => r.id === link.targetId)?.deliverableId ?? null) : ''
        rows.push([h.ref, h.statement ?? h.title, 'hold', h.log, personName(sx, h.ownerId), h.needBy,
          h.state === 'active' ? 'open' : 'closed', personName(sx, h.raisedBy), h.raisedAt.slice(0, 10),
          '', anchor, h.cause, h.resolvedAt?.slice(0, 10) ?? '', h.resolutionNote ?? '', 'anchored', ''])
      }
      for (const i of snap.interfaces as InterfaceItem[]) {
        if (i.state === 'cancelled' || i.state === 'closed') continue
        rows.push([i.ref, i.title, 'interface', i.log, '', i.needBy, i.state, '', '',
          pkgCode(i.givingPackageId), '', '', '', i.requiredInfo ?? '', 'anchored', ''])
      }
      // non-converted intake rows, flagged unanchored (round-trip completeness)
      for (const t of snap.intakeItems as IntakeItem[]) {
        if (t.state === 'dispositioned') continue
        rows.push([t.ref, t.statementVerbatim, t.quickType, t.log, personName(sx, t.suggestedOwnerId), t.needBy,
          'raised', personName(sx, t.raisedBy), t.raisedAt.slice(0, 10),
          '', t.anchorSuggestion ?? '', '', '', '', 'unanchored', t.area ?? ''])
      }
      return toCsv(headers, rows)
    }
    case 'decisions': {
      const headers = ['decision_id', 'title', 'statement', 'authority', 'need_by', 'status',
        'preparer', 'outcome', 'rationale', 'decided_date', 'affected_refs', 'open_date', 'area', 'source']
      const rows = snap.decisions.map((d) => [
        d.ref, d.title, d.statement, personName(sx, d.authorityId), d.needBy, d.state,
        personName(sx, d.preparerId), d.outcome ?? '', d.rationale ?? '', d.decidedAt?.slice(0, 10) ?? '',
        snap.decisionLinks.filter((l) => l.decisionId === d.id && l.recordType === 'deliverable')
          .map((l) => docNo(l.recordId)).filter(Boolean).join(';'),
        d.openDate ?? '', d.area ?? '', d.source ?? '',
      ])
      return toCsv(headers, rows)
    }
    case 'risks': {
      const headers = ['risk_id', 'title', 'cause', 'consequence', 'owner', 'status',
        'package', 'deliverable_ref', 'probability', 'impact', 'mitigation', 'need_by',
        'category', 'risk_type', 'treatment', 'residual_probability', 'residual_impact']
      const rows = (snap.risks as Risk[]).map((r) => [
        r.ref, r.title, r.cause, r.consequence, personName(sx, r.ownerId), r.state,
        pkgCode(r.packageId), docNo(r.deliverableId), r.probability?.toString() ?? '',
        r.impact?.toString() ?? '', r.mitigation, r.needBy,
        r.category ?? '', r.riskType ?? '', r.treatment ?? '',
        r.residualProbability?.toString() ?? '', r.residualImpact?.toString() ?? '',
      ])
      return toCsv(headers, rows)
    }
    case 'approvals': {
      const headers = ['approval_id', 'title', 'type', 'authority_source', 'applies_to', 'signatories',
        'due_date', 'state', 'outcome', 'outcome_decision']
      const rows = snap.approvalRecords.map((a) => {
        const outcome = a.outcomeDecisionId != null ? snap.decisions.find((d) => d.id === a.outcomeDecisionId) : null
        return [a.ref, a.title, a.approvalType, a.authoritySource,
          `${a.appliesToType}#${a.appliesToId}`, a.signatoryIds.map((s) => personName(sx, s)).join(';'),
          a.dueDate, a.state, outcome?.outcome ?? '', outcome?.ref ?? '']
      })
      return toCsv(headers, rows)
    }
    case 'interfaces': {
      const headers = ['interface_id', 'title', 'giving_party', 'receiving_party', 'giving_package',
        'receiving_package', 'required_info', 'need_by', 'state', 'log']
      const rows = (snap.interfaces as InterfaceItem[]).map((i) => [
        i.ref, i.title, i.givingParty, i.receivingParty, pkgCode(i.givingPackageId),
        pkgCode(i.receivingPackageId), i.requiredInfo, i.needBy, i.state, i.log,
      ])
      return toCsv(headers, rows)
    }
    case 'intake': {
      const headers = ['intake_id', 'statement', 'quick_type', 'log', 'raised_by', 'raised_date',
        'state', 'disposition', 'anchor_suggestion', 'need_by']
      const rows = (snap.intakeItems as IntakeItem[]).map((t) => [
        t.ref, t.statementVerbatim, t.quickType, t.log, personName(sx, t.raisedBy),
        t.raisedAt.slice(0, 10), t.state, t.disposition ?? '', t.anchorSuggestion, t.needBy,
      ])
      return toCsv(headers, rows)
    }
    case 'commitments': {
      // individual weekly commitments (PRD §15; ADR-010)
      const week = isoWeekOf(snap.today)
      const headers = ['week', 'owner', 'item_id', 'title', 'deliverable_ref', 'need_by', 'state', 'why_in_week']
      const rows: Array<Array<string | null>> = []
      for (const w of snap.workItems as WorkItem[]) {
        if (w.state !== 'open' && w.state !== 'in_work') continue
        const why = w.committedWeek === week
          ? (w.commitSource === 'plan' ? 'planning commitment' : 'manual commitment')
          : (w.needBy != null && (w.needBy <= snap.today || isoWeekOf(w.needBy) === week)) ? 'need-by' : null
        if (!why) continue
        rows.push([week, personName(sx, w.ownerId), w.ref, w.title,
          w.anchorType === 'deliverable' ? docNo(w.anchorId) : '', w.needBy, w.state, why])
      }
      return toCsv(headers, rows)
    }
    case 'log': {
      // Unified Action & Hold Log export, filtered to the caller's visible logs (§7, PEC-NFR-005) —
      // mirrors the displayed log register (ADR-010: export exactly what is shown).
      const logs = visibleLogs(sx.roles, snap.project.config.logVisibility)
      const cal = snap.project.calendar
      const today = snap.today
      const headers = ['item_id', 'type', 'title', 'log', 'package', 'owner', 'state',
        'age_wd', 'need_by', 'overdue', 'hold_cause', 'anchor_status']
      interface LR {
        type: string; ref: string; title: string; log: Log; pkgId: number | null
        ownerId: number | null; state: string; ageWd: number; needBy: string | null
        overdue: boolean; cause: string | null; anchor: string
      }
      const lrows: LR[] = []
      for (const w of snap.workItems as WorkItem[]) {
        if (w.state !== 'open' && w.state !== 'in_work') continue
        lrows.push({ type: 'work_item', ref: w.ref, title: w.title, log: w.log, pkgId: w.packageId, ownerId: w.ownerId, state: w.state, ageWd: ageWorkingDays(w.createdAt, today, cal), needBy: w.needBy, overdue: daysOverdue(w.needBy, today) > 0, cause: null, anchor: 'anchored' })
      }
      for (const h of snap.holds as Hold[]) {
        if (h.state !== 'active') continue
        lrows.push({ type: 'hold', ref: h.ref, title: h.title, log: h.log, pkgId: null, ownerId: h.ownerId, state: h.state, ageWd: ageWorkingDays(h.raisedAt, today, cal), needBy: h.needBy, overdue: daysOverdue(h.needBy, today) > 0, cause: h.cause, anchor: 'anchored' })
      }
      for (const i of snap.interfaces as InterfaceItem[]) {
        if (i.state !== 'open' && i.state !== 'agreed') continue
        lrows.push({ type: 'interface_item', ref: i.ref, title: i.title, log: i.log, pkgId: i.givingPackageId ?? i.receivingPackageId, ownerId: null, state: i.state, ageWd: 0, needBy: i.needBy, overdue: daysOverdue(i.needBy, today) > 0, cause: null, anchor: 'anchored' })
      }
      for (const t of snap.intakeItems as IntakeItem[]) {
        if (t.state === 'dispositioned') continue
        lrows.push({ type: 'intake_item', ref: t.ref, title: t.statementVerbatim.slice(0, 120), log: t.log, pkgId: null, ownerId: t.suggestedOwnerId, state: t.state, ageWd: ageWorkingDays(t.raisedAt, today, cal), needBy: t.needBy, overdue: daysOverdue(t.needBy, today) > 0, cause: null, anchor: 'unanchored' })
      }
      const rows = lrows
        .filter((r) => logs.includes(r.log))
        .sort((a, b) => b.ageWd - a.ageWd)
        .map((r) => [r.ref, r.type, r.title, r.log, pkgCode(r.pkgId), personName(sx, r.ownerId),
          r.state, String(r.ageWd), r.needBy, r.overdue ? 'yes' : 'no', r.cause, r.anchor])
      return toCsv(headers, rows)
    }
    case 'schedule': {
      // mirrors the §16 P2 schedule import for round-trip
      const headers = ['activity_id', 'description', 'start', 'finish', 'package', 'deliverable_ref',
        'row_type', 'outline_level', 'parent_activity_id', 'percent_complete', 'duration_days',
        'baseline_start', 'baseline_finish']
      const rows = snap.scheduleActivities.map((a) => [
        a.activityId, a.description, a.startDate, a.finishDate,
        pkgCode(a.packageId), docNo(a.deliverableId),
        a.rowType ?? '', a.outlineLevel?.toString() ?? '', a.parentActivityId ?? '',
        a.percentComplete?.toString() ?? '', a.durationDays?.toString() ?? '',
        a.baselineStart ?? '', a.baselineFinish ?? '',
      ])
      return toCsv(headers, rows)
    }
    case 'tracker': {
      // mirrors the §16 tracker import for round-trip (D-PEC-13); tracker rows are
      // import-owned and stay out of the snapshot — direct table read
      const headers = ['tracking_no', 'package_name', 'discipline', 'area',
        'package_type_approved', 'package_type_proposed', 'line_items', 'vendors_engaged',
        'vendor_awarded', 'expected_delivery_date', 'cost_estimate_cad', 'comments',
        ...TRACKER_STAGE_COLS, 'package']
      const rows = sx.repo.list<PackageTracker>('package_tracker', sx.projectId).map((t) => [
        t.trackingNo, t.packageName, t.discipline, t.area,
        t.packageTypeApproved, t.packageTypeProposed, t.lineItems, t.vendorsEngaged,
        t.vendorAwarded, t.expectedDeliveryDate, t.costEstimateCad, t.comments,
        t.stageBudgetaryDatasheet, t.stageCostEstimate, t.stagePackageDatasheet, t.stagePackage,
        t.stageRfq, t.stageReview, t.stageVendorBids, t.stageClarifications, t.stageEvaluation,
        t.stageEngReq, t.stagePo, t.stageDatabook, pkgCode(t.packageId),
      ])
      return toCsv(headers, rows)
    }
    case 'lookahead': {
      // six-week lookahead (PRD §15 P2): rows deliverables, one column per week (PEC-PLAN-002)
      const weeks = isoWeeksFrom(snap.today, 6)
      const headers = ['doc_no', 'title', 'package', 'due_date', ...weeks]
      const rows = lookahead(snap, weeks).map((r) => [
        r.deliverable.docNo, r.deliverable.title, pkgCode(r.deliverable.packageId),
        r.deliverable.dueDate,
        ...r.cells.map((c) => (c ? `${c.state}: ${c.detail}` : '')),
      ])
      return toCsv(headers, rows)
    }
    default:
      throw badRequest(`unknown register export: ${register}`)
  }
}
