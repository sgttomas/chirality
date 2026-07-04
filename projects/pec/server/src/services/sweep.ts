/**
 * Time-driven notification sweep (review resolution 15; PEC-NOT-001 "item overdue",
 * "decision you own past need-by"). Working-day aware, idempotent per
 * (person, event, record, local day). Runs hourly and on login.
 *
 * P2 additions: §8.4 escalation thresholds drive notification severity (PEC-NOT-003),
 * and weekly role digests — one per person per ISO week — summarize planning, package
 * review, overdue judgments, open holds, and comment aging (PEC-NOT-002).
 */

import type {
  Decision, NotificationEvent, NotificationSeverity, ProjectSnapshot, Role, WorkItem,
} from '@pec/core'
import {
  ageWorkingDays, capacityBreaches, commentIsOpen, daysOverdue, isoWeekOf, localDate,
} from '@pec/core'
import type { Db } from '../db.ts'
import { Repo, nowIso } from '../repo.ts'

export function sweepProject(db: Db, projectId: number): number {
  const repo = new Repo(db)
  const snap = repo.snapshot(projectId)
  const today = snap.today
  const th = snap.project.thresholds
  const cal = snap.project.calendar
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
    recordType: string, recordId: number, recordRef: string, reason: string, nextAction: string,
    due: string | null, severity: NotificationSeverity) => {
    if (!personId || alreadyToday(personId, event, recordType, recordId)) return
    repo.insert('notification', {
      projectId, personId, at: nowIso(), event, recordType, recordId, recordRef,
      reason, nextAction, due, severity, readAt: null,
    })
    emitted++
  }

  for (const w of snap.workItems as WorkItem[]) {
    if (w.state !== 'open' && w.state !== 'in_work') continue
    const over = daysOverdue(w.needBy, today)
    if (over > 0) {
      emit(w.ownerId, 'item_overdue', 'work_item', w.id, w.ref,
        `${w.ref} is ${over} day(s) past need-by`, 'update or close the item', w.needBy,
        over > th.decisionOverdueRedD ? 'red' : 'warn')
    }
  }
  for (const d of snap.decisions as Decision[]) {
    if (d.state !== 'identified' && d.state !== 'in_progress' && d.state !== 'pending') continue
    const over = daysOverdue(d.needBy, today)
    if (over > 0) {
      // PEC-NOT-003: the §8.4 decision row drives severity (warn > 0 d, escalate > red threshold)
      emit(d.authorityId, 'decision_past_need_by', 'decision', d.id, d.ref,
        `${d.ref} is ${over} day(s) past need-by; you are the authority`,
        'progress or record the decision', d.needBy,
        over > th.decisionOverdueRedD ? 'red' : 'warn')
    }
  }

  emitted += sweepDigests(db, repo, snap, projectId)
  return emitted
}

// ---------- weekly role digests (PEC-NOT-002) ----------

interface DigestLine {
  count: number
  worst: NotificationSeverity
  text: string
}

/**
 * One digest notification per person per digest type per ISO week (idempotent). Content is
 * role-driven: weekly planning (planner/pm), package review (leads), overdue
 * decisions/approvals (authorities/signatories), open holds (hold owners), comment aging
 * (responders). Severity carries the worst §8.4 breach in the digest (PEC-NOT-003).
 */
function sweepDigests(db: Db, repo: Repo, snap: ProjectSnapshot, projectId: number): number {
  const today = snap.today
  const week = isoWeekOf(today)
  const th = snap.project.thresholds
  const cal = snap.project.calendar
  const tz = snap.project.calendar.timezone
  let emitted = 0

  const alreadyThisWeek = (personId: number, event: string): boolean => {
    const rows = db.prepare(
      `SELECT at FROM notification WHERE project_id = ? AND person_id = ? AND event = ?
       ORDER BY id DESC LIMIT 1`,
    ).all(projectId, personId, event) as Array<{ at: string }>
    const last = rows[0]
    return last != null && isoWeekOf(localDate(last.at, tz)) === week
  }

  const emitDigest = (personId: number, event: NotificationEvent, line: DigestLine, nextAction: string): void => {
    if (!personId || line.count === 0 || alreadyThisWeek(personId, event)) return
    repo.insert('notification', {
      projectId, personId, at: nowIso(), event,
      recordType: 'project', recordId: projectId, recordRef: `${snap.project.code} ${week}`,
      reason: line.text, nextAction, due: null, severity: line.worst, readAt: null,
    })
    emitted++
  }

  const roleHolders = (role: Role): number[] =>
    (db.prepare('SELECT person_id FROM project_role WHERE project_id = ? AND role = ?')
      .all(projectId, role) as Array<{ person_id: number }>).map((r) => r.person_id)

  // planner digest: capacity breaches + uncommitted planned weeks
  {
    const breaches = capacityBreaches(snap)
    const uncommitted = snap.planItems.filter((pi) => pi.week === week).length > 0
      && !snap.planPeriods.some((p) => p.week === week && p.state === 'committed')
    const parts: string[] = []
    if (breaches.length > 0) {
      parts.push(`capacity: ${breaches.map((b) => `${b.discipline} ${b.pct}%`).join(', ')}`)
    }
    if (uncommitted) parts.push(`week ${week} is planned but not committed (PEC-PLAN-007)`)
    const line: DigestLine = {
      count: parts.length,
      worst: breaches.some((b) => b.level === 'red') ? 'red' : breaches.length > 0 ? 'warn' : 'info',
      text: `weekly planning digest — ${parts.join('; ') || 'nothing pressing'}`,
    }
    for (const pid of [...roleHolders('planner'), ...roleHolders('pm')]) {
      emitDigest(pid, 'digest_planning', line, 'open the Plan page')
    }
  }

  // package-review digest: open issues per lead's packages
  for (const pkg of snap.packages) {
    if (pkg.leadId == null) continue
    const pkgDelIds = new Set(snap.deliverables.filter((d) => d.packageId === pkg.id).map((d) => d.id))
    const pkgRevIds = new Set(snap.revisions.filter((r) => pkgDelIds.has(r.deliverableId)).map((r) => r.id))
    const holds = snap.holds.filter((h) => h.state === 'active'
      && snap.holdLinks.some((l) => l.holdId === h.id && (
        (l.targetType === 'deliverable' && pkgDelIds.has(l.targetId))
        || (l.targetType === 'revision' && pkgRevIds.has(l.targetId))
        || (l.targetType === 'work_item' && snap.workItems.some((w) => w.id === l.targetId && w.packageId === pkg.id))
      ))).length
    const overdueDecs = snap.decisions.filter((d) => d.packageId === pkg.id
      && (d.state === 'identified' || d.state === 'in_progress' || d.state === 'pending')
      && daysOverdue(d.needBy, today) > 0)
    const lateIfaces = snap.interfaces.filter((i) =>
      (i.givingPackageId === pkg.id || i.receivingPackageId === pkg.id)
      && (i.state === 'open' || i.state === 'agreed') && daysOverdue(i.needBy, today) > 0)
    const count = overdueDecs.length + lateIfaces.length
    if (count === 0 && holds === 0) continue
    const line: DigestLine = {
      count: Math.max(count, holds > 0 ? 1 : 0),
      worst: overdueDecs.some((d) => daysOverdue(d.needBy, today) > th.decisionOverdueRedD) ? 'red'
        : count > 0 ? 'warn' : 'info',
      text: `package review digest ${pkg.code} — ${holds} open hold(s), ${overdueDecs.length} overdue `
        + `decision(s), ${lateIfaces.length} late interface(s); weekly pack: reports/package-pack/${pkg.id}`,
    }
    emitDigest(pkg.leadId, 'digest_package_review', line, 'run the weekly package review (PEC-PKG-009)')
  }

  // judgments digest: overdue decisions (authority) + aging ready approvals (signatories)
  {
    const byPerson = new Map<number, { decs: number; apprs: number; worst: NotificationSeverity }>()
    const bump = (pid: number, kind: 'decs' | 'apprs', sev: NotificationSeverity): void => {
      const e = byPerson.get(pid) ?? { decs: 0, apprs: 0, worst: 'info' as NotificationSeverity }
      e[kind]++
      if (sev === 'red' || (sev === 'warn' && e.worst === 'info')) e.worst = sev
      byPerson.set(pid, e)
    }
    for (const d of snap.decisions) {
      if (d.state !== 'identified' && d.state !== 'in_progress' && d.state !== 'pending') continue
      const over = daysOverdue(d.needBy, today)
      if (over > 0 && d.authorityId) bump(d.authorityId, 'decs', over > th.decisionOverdueRedD ? 'red' : 'warn')
    }
    for (const a of snap.approvalRecords) {
      if (a.state !== 'ready' || !a.readyAt) continue
      const age = ageWorkingDays(a.readyAt, today, cal)
      if (age <= th.approvalLatencyWarnWd) continue
      for (const pid of a.signatoryIds) bump(pid, 'apprs', age > th.approvalLatencyRedWd ? 'red' : 'warn')
    }
    for (const [pid, e] of byPerson) {
      emitDigest(pid, 'digest_judgments', {
        count: e.decs + e.apprs, worst: e.worst,
        text: `judgments digest — ${e.decs} overdue decision(s), ${e.apprs} approval(s) waiting on you past threshold`,
      }, 'see Waiting on you (Overview)')
    }
  }

  // holds digest: open holds by owner
  {
    const byOwner = new Map<number, { n: number; worst: NotificationSeverity }>()
    for (const h of snap.holds) {
      if (h.state !== 'active' || !h.ownerId) continue
      const age = ageWorkingDays(h.raisedAt, today, cal)
      const sev: NotificationSeverity = age > th.holdAgeRedWd ? 'red' : age > th.holdAgeWarnWd ? 'warn' : 'info'
      const e = byOwner.get(h.ownerId) ?? { n: 0, worst: 'info' as NotificationSeverity }
      e.n++
      if (sev === 'red' || (sev === 'warn' && e.worst === 'info')) e.worst = sev
      byOwner.set(h.ownerId, e)
    }
    for (const [pid, e] of byOwner) {
      emitDigest(pid, 'digest_holds', {
        count: e.n, worst: e.worst,
        text: `holds digest — ${e.n} open hold(s) you own`,
      }, 'resolve or chase your holds (Action & Hold Log)')
    }
  }

  // comment-aging digest: open review comments by responder
  {
    const byResponder = new Map<number, { n: number; worst: NotificationSeverity }>()
    for (const c of snap.reviewComments) {
      if (!commentIsOpen(c) || !c.responderId) continue
      const age = ageWorkingDays(c.createdAt, today, cal)
      if (age <= th.commentAgeWarnWd) continue
      const sev: NotificationSeverity = age > th.commentAgeRedWd ? 'red' : 'warn'
      const e = byResponder.get(c.responderId) ?? { n: 0, worst: 'info' as NotificationSeverity }
      e.n++
      if (sev === 'red' || e.worst === 'info') e.worst = sev
      byResponder.set(c.responderId, e)
    }
    for (const [pid, e] of byResponder) {
      emitDigest(pid, 'digest_comments', {
        count: e.n, worst: e.worst,
        text: `comment aging digest — ${e.n} check comment(s) awaiting your response past threshold`,
      }, 'respond from My Week')
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
