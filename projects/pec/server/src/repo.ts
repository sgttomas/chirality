/**
 * Repository layer (ADR-003): the ONLY SQL surface. Every project-scoped query takes
 * project id from the route context. Optimistic concurrency on controlled records
 * (PEC-NFR-004); history inside the same transaction as the change (I-7).
 */

import type { Db } from './db.ts'
import { notFound, versionConflict } from './errors.ts'
import type {
  HistoryEntry, Notification, NotificationEvent, NotificationSeverity, ProjectSnapshot, RecordType,
} from '@pec/core'
import { DEFAULT_THRESHOLDS, localDate } from '@pec/core'

// ---------- naming ----------

export function camelToSnake(s: string): string {
  return s.replace(/[A-Z]/g, (m) => `_${m.toLowerCase()}`)
}
export function snakeToCamel(s: string): string {
  return s.replace(/_([a-z])/g, (_, c: string) => c.toUpperCase())
}

/** table per record type (check/condition tables carry a _record suffix to dodge SQL keywords) */
export const TABLE: Partial<Record<RecordType | string, string>> = {
  project: 'project', package: 'package', deliverable: 'deliverable', revision: 'revision',
  intake_item: 'intake_item', work_item: 'work_item', hold: 'hold', check: 'check_record',
  review_comment: 'review_comment', approval_record: 'approval_record', decision: 'decision',
  risk: 'risk', interface_item: 'interface_item', condition: 'condition_record',
  issue_event: 'issue_event', evidence: 'evidence', basis_reference: 'basis_reference',
  person: 'person',
  plan_item: 'plan_item', plan_shift: 'plan_shift', schedule_activity: 'schedule_activity',
  import_proposal: 'import_proposal',
}

/** ref prefixes per record type (ADR-008) */
const REF_PREFIX: Record<string, string> = {
  intake_item: 'INTK', work_item: 'WI', hold: 'HLD', check: 'CHK', review_comment: 'CMT',
  approval_record: 'APR', decision: 'DEC', risk: 'RSK', interface_item: 'INT',
  condition: 'COND', issue_event: 'EVT',
  plan_item: 'PLN', plan_shift: 'PLS',
  import_proposal: 'IPR',
}

const JSON_COLS: Record<string, string[]> = {
  project: ['weekend_days', 'holidays', 'thresholds', 'config'],
  check_record: ['checklist'],
  approval_record: ['signatory_ids'],
  issue_event: ['recipients', 'approval_record_ids', 'decision_ids'],
  checklist_template: ['items'],
  history_entry: ['payload'],
  audit_event: ['prior_value', 'new_value'],
  plan_shift: ['affected_package_ids'],
  supersession_link: ['affected'],
  import_proposal: ['dry_run_report', 'apply_report', 'source_extras'],
  // D-PEC-41 full-fidelity capture columns (verbatim unmapped source columns)
  package: ['source_payload'],
  deliverable: ['source_payload'],
  work_item: ['source_payload'],
}

const BOOL_COLS: Record<string, string[]> = {
  person: ['is_admin'],
  check_record: ['independence_warning'],
  approval_record: ['hold_point'],
  plan_shift: ['cross_package'],
}

type Row = Record<string, unknown>

function fromRow(table: string, row: Row): Row {
  const json = JSON_COLS[table] ?? []
  const bools = BOOL_COLS[table] ?? []
  const out: Row = {}
  for (const [k, v] of Object.entries(row)) {
    const key = snakeToCamel(k)
    if (json.includes(k)) out[key] = v == null ? null : JSON.parse(String(v))
    else if (bools.includes(k)) out[key] = v === 1 || v === true
    else out[key] = v
  }
  return out
}

function toCols(table: string, obj: Row): Row {
  const json = JSON_COLS[table] ?? []
  const out: Row = {}
  for (const [k, v] of Object.entries(obj)) {
    if (v === undefined) continue
    const col = camelToSnake(k)
    if (json.includes(col)) out[col] = v == null ? null : JSON.stringify(v)
    else if (typeof v === 'boolean') out[col] = v ? 1 : 0
    else out[col] = v as never
  }
  return out
}

export function nowIso(): string {
  return new Date().toISOString()
}

export class Repo {
  readonly db: Db

  constructor(db: Db) {
    this.db = db
  }

  // ---------- generic ----------

  nextRef(projectId: number, recordType: string): string {
    const prefix = REF_PREFIX[recordType]
    if (!prefix) throw new Error(`no ref prefix for ${recordType}`)
    this.db.prepare(
      'INSERT INTO seq (project_id, kind, next_val) VALUES (?, ?, 1) ON CONFLICT(project_id, kind) DO NOTHING',
    ).run(projectId, recordType)
    const row = this.db.prepare('SELECT next_val FROM seq WHERE project_id = ? AND kind = ?')
      .get(projectId, recordType) as Row
    this.db.prepare('UPDATE seq SET next_val = next_val + 1 WHERE project_id = ? AND kind = ?')
      .run(projectId, recordType)
    return `${prefix}-${String(row.next_val).padStart(4, '0')}`
  }

  insert(table: string, obj: Row): number {
    const cols = toCols(table, obj)
    const names = Object.keys(cols)
    const sql = `INSERT INTO ${table} (${names.join(',')}) VALUES (${names.map(() => '?').join(',')})`
    const res = this.db.prepare(sql).run(...names.map((n) => cols[n] as never))
    return Number(res.lastInsertRowid)
  }

  get<T = Row>(table: string, projectId: number | null, id: number): T {
    const row = projectId == null
      ? this.db.prepare(`SELECT * FROM ${table} WHERE id = ?`).get(id) as Row | undefined
      : this.db.prepare(`SELECT * FROM ${table} WHERE id = ? AND project_id = ?`).get(id, projectId) as Row | undefined
    if (!row) throw notFound(`${table} #${id}`)
    return fromRow(table, row) as T
  }

  maybeGet<T = Row>(table: string, projectId: number | null, id: number): T | null {
    try { return this.get<T>(table, projectId, id) } catch { return null }
  }

  list<T = Row>(table: string, projectId: number, where = '', params: unknown[] = []): T[] {
    const sql = `SELECT * FROM ${table} WHERE project_id = ? ${where ? `AND ${where}` : ''}`
    return (this.db.prepare(sql).all(projectId, ...(params as never[])) as Row[])
      .map((r) => fromRow(table, r) as T)
  }

  /**
   * Optimistic-concurrency update on a controlled record (PEC-NFR-004).
   * `expectedVersion` must match; on mismatch throws 409 with intervening history.
   */
  update(table: string, projectId: number, id: number, expectedVersion: number, patch: Row): void {
    const cols = toCols(table, patch)
    delete cols.id; delete cols.project_id; delete cols.version
    const names = Object.keys(cols)
    if (names.length === 0) return
    const sql = `UPDATE ${table} SET ${names.map((n) => `${n} = ?`).join(', ')}, version = version + 1
                 WHERE id = ? AND project_id = ? AND version = ?`
    const res = this.db.prepare(sql).run(...names.map((n) => cols[n] as never), id, projectId, expectedVersion)
    if (res.changes === 0) {
      const current = this.maybeGet(table, projectId, id)
      if (!current) throw notFound(`${table} #${id}`)
      const recordType = Object.entries(TABLE).find(([, t]) => t === table)?.[0] ?? table
      const intervening = this.historyFor(projectId, recordType, id, 10)
      throw versionConflict({ currentVersion: (current as Row).version, intervening })
    }
  }

  /** System update that does not take a user-supplied version (auto transitions); still bumps version. */
  systemUpdate(table: string, projectId: number, id: number, patch: Row): void {
    const cols = toCols(table, patch)
    delete cols.id; delete cols.project_id; delete cols.version
    const names = Object.keys(cols)
    if (names.length === 0) return
    const sql = `UPDATE ${table} SET ${names.map((n) => `${n} = ?`).join(', ')}, version = version + 1
                 WHERE id = ? AND project_id = ?`
    const res = this.db.prepare(sql).run(...names.map((n) => cols[n] as never), id, projectId)
    if (res.changes === 0) throw notFound(`${table} #${id}`)
  }

  // ---------- history / audit / notifications ----------

  history(entry: Omit<HistoryEntry, 'id' | 'at'> & { at?: string }): void {
    this.insert('history_entry', {
      projectId: entry.projectId, recordType: entry.recordType, recordId: entry.recordId,
      at: entry.at ?? nowIso(), actorId: entry.actorId, kind: entry.kind,
      summary: entry.summary, payload: entry.payload == null ? null : JSON.stringify(entry.payload),
      authorityRef: entry.authorityRef,
    })
  }

  /** Project-scoped by contract (PEC-NFR-007): history_entry carries project_id, so a
   *  foreign record id supplied on another project's route returns nothing. */
  historyFor(projectId: number, recordType: string, recordId: number, limit = 200): HistoryEntry[] {
    const rows = this.db.prepare(
      'SELECT * FROM history_entry WHERE project_id = ? AND record_type = ? AND record_id = ? ORDER BY id DESC LIMIT ?',
    ).all(projectId, recordType, recordId, limit) as Row[]
    return rows.map((r) => fromRow('history_entry', r) as unknown as HistoryEntry)
  }

  audit(a: {
    projectId: number; actorId: number; action: string; recordType: string; recordId: number;
    priorValue?: unknown; newValue?: unknown; authorityRef?: string | null
  }): void {
    this.insert('audit_event', {
      projectId: a.projectId, at: nowIso(), actorId: a.actorId, action: a.action,
      recordType: a.recordType, recordId: a.recordId,
      priorValue: a.priorValue == null ? null : JSON.stringify(a.priorValue),
      newValue: a.newValue == null ? null : JSON.stringify(a.newValue),
      authorityRef: a.authorityRef ?? null,
    })
  }

  notify(n: {
    projectId: number; personId: number; event: NotificationEvent; recordType: string;
    recordId: number; recordRef: string; reason: string; nextAction: string; due?: string | null
    /** PEC-NOT-003: §8.4 thresholds drive severity; producers default to 'info' */
    severity?: NotificationSeverity
  }): void {
    if (!n.personId) return
    this.insert('notification', {
      ...n, at: nowIso(), due: n.due ?? null, severity: n.severity ?? 'info', readAt: null,
    })
  }

  notificationsFor(projectId: number, personId: number, unreadOnly = false): Notification[] {
    const rows = this.db.prepare(
      `SELECT * FROM notification WHERE project_id = ? AND person_id = ?
       ${unreadOnly ? 'AND read_at IS NULL' : ''} ORDER BY id DESC LIMIT 200`,
    ).all(projectId, personId) as Row[]
    return rows.map((r) => fromRow('notification', r) as unknown as Notification)
  }

  // ---------- snapshot (ADR-004) ----------

  snapshot(projectId: number): ProjectSnapshot {
    const projRow = this.db.prepare('SELECT * FROM project WHERE id = ?').get(projectId) as Row | undefined
    if (!projRow) throw notFound(`project #${projectId}`)
    const p = fromRow('project', projRow)
    const project = {
      id: p.id as number, code: p.code as string, name: p.name as string,
      calendar: {
        timezone: p.timezone as string,
        weekendDays: (p.weekendDays as string[]) ?? ['Sat', 'Sun'],
        holidays: (p.holidays as string[]) ?? [],
      },
      thresholds: { ...DEFAULT_THRESHOLDS, ...(p.thresholds as object) },
      config: {
        holdCauses: [], issuePurposes: ['IFR', 'IFA', 'IFC'], logVisibility: {},
        waiverRoles: {}, allowAnyoneRaiseIntake: true,
        ...(p.config as object),
      },
      version: p.version as number,
    }
    const all = <T>(table: string): T[] =>
      (this.db.prepare(`SELECT * FROM ${table} WHERE project_id = ?`).all(projectId) as Row[])
        .map((r) => fromRow(table, r) as T)

    // Link tables carry no project_id; scope them through the parent's project so the scan is
    // bounded to this project and never reads another tenant's links (PEC-NFR-007, PEC-NFR-003).
    const holds = all<ProjectSnapshot['holds'][number]>('hold')
    const holdLinks = (this.db.prepare(
      'SELECT hl.* FROM hold_link hl JOIN hold h ON h.id = hl.hold_id WHERE h.project_id = ?',
    ).all(projectId) as Row[])
      .map((r) => fromRow('hold_link', r) as unknown as ProjectSnapshot['holdLinks'][number])
    const decisions = all<ProjectSnapshot['decisions'][number]>('decision')
    const decisionLinks = (this.db.prepare(
      'SELECT dl.* FROM decision_link dl JOIN decision d ON d.id = dl.decision_id WHERE d.project_id = ?',
    ).all(projectId) as Row[])
      .map((r) => fromRow('decision_link', r) as unknown as ProjectSnapshot['decisionLinks'][number])
    const packageRows = all<ProjectSnapshot['packages'][number]>('package')
    const packageDisciplineRows = this.db.prepare(
      `SELECT package_id, discipline FROM package_discipline
       WHERE project_id = ? GROUP BY package_id, discipline
       ORDER BY discipline`,
    ).all(projectId) as Array<{ package_id: number; discipline: string }>
    const disciplinesByPackage = new Map<number, string[]>()
    for (const row of packageDisciplineRows) {
      const values = disciplinesByPackage.get(row.package_id) ?? []
      values.push(row.discipline)
      disciplinesByPackage.set(row.package_id, values)
    }
    const packages = packageRows.map((pkg) => ({
      ...pkg,
      disciplines: disciplinesByPackage.get(pkg.id)
        ?? (pkg.discipline ? [pkg.discipline] : []),
    }))

    return {
      project: project as ProjectSnapshot['project'],
      packages,
      deliverables: all('deliverable'),
      revisions: all('revision'),
      workItems: all('work_item'),
      holds, holdLinks,
      checks: all('check_record'),
      reviewComments: all('review_comment'),
      approvalRecords: all('approval_record'),
      decisions, decisionLinks,
      risks: all('risk'),
      interfaces: all('interface_item'),
      intakeItems: all('intake_item'),
      conditions: all('condition_record'),
      issueEvents: all('issue_event'),
      evidence: all('evidence'),
      planItems: all('plan_item'),
      planPeriods: all('plan_period'),
      capacityEntries: all('capacity_entry'),
      scheduleActivities: all('schedule_activity'),
      planShifts: all('plan_shift'),
      today: localDate(nowIso(), project.calendar.timezone),
    }
  }
}
