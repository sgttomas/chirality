/**
 * Time-driven notification sweep (review resolution 15; PEC-NOT-001 "item overdue",
 * "decision you own past need-by"). Working-day aware, idempotent per
 * (person, event, record, local day). Runs hourly and on login.
 */

import type { Decision, WorkItem } from '@pec/core'
import { daysOverdue, localDate } from '@pec/core'
import type { Db } from '../db.ts'
import { Repo, nowIso } from '../repo.ts'

export function sweepProject(db: Db, projectId: number): number {
  const repo = new Repo(db)
  const snap = repo.snapshot(projectId)
  const today = snap.today
  const tz = snap.project.calendar.timezone
  let emitted = 0

  const alreadyToday = (personId: number, event: string, recordType: string, recordId: number): boolean => {
    const rows = db.prepare(
      `SELECT at FROM notification WHERE project_id = ? AND person_id = ? AND event = ?
       AND record_type = ? AND record_id = ? ORDER BY id DESC LIMIT 1`,
    ).all(projectId, personId, event, recordType, recordId) as Array<{ at: string }>
    const last = rows[0]
    return last != null && localDate(last.at, tz) === today
  }

  const emit = (personId: number, event: 'item_overdue' | 'decision_past_need_by',
    recordType: string, recordId: number, recordRef: string, reason: string, nextAction: string, due: string | null) => {
    if (!personId || alreadyToday(personId, event, recordType, recordId)) return
    repo.insert('notification', {
      projectId, personId, at: nowIso(), event, recordType, recordId, recordRef,
      reason, nextAction, due, readAt: null,
    })
    emitted++
  }

  for (const w of snap.workItems as WorkItem[]) {
    if (w.state !== 'open' && w.state !== 'in_work') continue
    const over = daysOverdue(w.needBy, today)
    if (over > 0) {
      emit(w.ownerId, 'item_overdue', 'work_item', w.id, w.ref,
        `${w.ref} is ${over} day(s) past need-by`, 'update or close the item', w.needBy)
    }
  }
  for (const d of snap.decisions as Decision[]) {
    if (d.state !== 'identified' && d.state !== 'in_progress' && d.state !== 'pending') continue
    const over = daysOverdue(d.needBy, today)
    if (over > 0) {
      emit(d.authorityId, 'decision_past_need_by', 'decision', d.id, d.ref,
        `${d.ref} is ${over} day(s) past need-by; you are the authority`,
        'progress or record the decision', d.needBy)
    }
  }
  return emitted
}

export function sweepAll(db: Db): number {
  const projects = db.prepare('SELECT id FROM project').all() as Array<{ id: number }>
  let n = 0
  for (const p of projects) n += sweepProject(db, p.id)
  return n
}
