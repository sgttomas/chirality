/**
 * Working-day calendar math (PEC-NFR-010).
 * Dates are stored UTC; "working days" are computed on local dates in the project timezone
 * against the project calendar (weekend days + holidays).
 */

import type { ProjectCalendar } from './types.ts'

const DAY_MS = 86_400_000
const MAX_SPAN_DAYS = 3660 // guard against runaway loops on bad data (~10 years)

/** Local date (YYYY-MM-DD) of a UTC instant in the given timezone. */
export function localDate(utcIso: string, timezone: string): string {
  const d = new Date(utcIso)
  if (Number.isNaN(d.getTime())) throw new Error(`invalid date: ${utcIso}`)
  // en-CA yields YYYY-MM-DD
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: timezone, year: 'numeric', month: '2-digit', day: '2-digit',
  }).format(d)
}

/** Short en weekday name ('Mon'...) of a local date string. */
export function weekdayOf(dateLocal: string): string {
  const d = parseLocal(dateLocal)
  return new Intl.DateTimeFormat('en-US', { weekday: 'short', timeZone: 'UTC' }).format(d)
}

function parseLocal(dateLocal: string): Date {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(dateLocal)) throw new Error(`invalid local date: ${dateLocal}`)
  return new Date(`${dateLocal}T00:00:00Z`)
}

/** True when a string is a well-formed YYYY-MM-DD local date. */
export function isValidLocalDate(dateLocal: string | null | undefined): dateLocal is string {
  if (dateLocal == null || !/^\d{4}-\d{2}-\d{2}$/.test(dateLocal)) return false
  const d = new Date(`${dateLocal}T00:00:00Z`)
  return !Number.isNaN(d.getTime()) && d.toISOString().slice(0, 10) === dateLocal
}

function fmtLocal(d: Date): string {
  return d.toISOString().slice(0, 10)
}

export function isWorkingDay(dateLocal: string, cal: ProjectCalendar): boolean {
  if (cal.holidays.includes(dateLocal)) return false
  return !cal.weekendDays.includes(weekdayOf(dateLocal))
}

/** Next local date (calendar day). */
export function nextDay(dateLocal: string): string {
  return fmtLocal(new Date(parseLocal(dateLocal).getTime() + DAY_MS))
}

/** Calendar days from a to b (b - a); negative when b < a. */
export function calendarDaysBetween(aLocal: string, bLocal: string): number {
  return Math.round((parseLocal(bLocal).getTime() - parseLocal(aLocal).getTime()) / DAY_MS)
}

/**
 * Working days from a to b: the number of working days in (a, b].
 * 0 when b <= a. Symmetric convention: an item due yesterday checked today has age 1
 * if today is a working day.
 */
export function workingDaysBetween(aLocal: string, bLocal: string, cal: ProjectCalendar): number {
  if (calendarDaysBetween(aLocal, bLocal) <= 0) return 0
  let count = 0
  let cur = aLocal
  let steps = 0
  while (cur !== bLocal) {
    if (++steps > MAX_SPAN_DAYS) return count // clamp; callers treat as "very large"
    cur = nextDay(cur)
    if (isWorkingDay(cur, cal)) count++
  }
  return count
}

/** Add n working days (n >= 0) to a local date; result is a working day when n > 0. */
export function addWorkingDays(dateLocal: string, n: number, cal: ProjectCalendar): string {
  let cur = dateLocal
  let added = 0
  let steps = 0
  while (added < n) {
    if (++steps > MAX_SPAN_DAYS) break
    cur = nextDay(cur)
    if (isWorkingDay(cur, cal)) added++
  }
  return cur
}

/** ISO week string 'YYYY-Www' for a local date. */
export function isoWeekOf(dateLocal: string): string {
  const d = parseLocal(dateLocal)
  // ISO week algorithm on UTC date
  const day = (d.getUTCDay() + 6) % 7 // Mon=0
  const thursday = new Date(d.getTime() + (3 - day) * DAY_MS)
  const yearStart = new Date(Date.UTC(thursday.getUTCFullYear(), 0, 1))
  const week = Math.floor((thursday.getTime() - yearStart.getTime()) / DAY_MS / 7) + 1
  return `${thursday.getUTCFullYear()}-W${String(week).padStart(2, '0')}`
}

function isoWeekMondayUnchecked(year: number, num: number): string {
  // ISO week 1 contains Jan 4; step back to that week's Monday, then forward (num-1) weeks.
  const jan4 = new Date(Date.UTC(year, 0, 4))
  const day = (jan4.getUTCDay() + 6) % 7 // Mon=0
  const week1Monday = new Date(jan4.getTime() - day * DAY_MS)
  return fmtLocal(new Date(week1Monday.getTime() + (num - 1) * 7 * DAY_MS))
}

/**
 * True when a string is a real ISO week 'YYYY-Www' — including the round-trip check, so
 * W53 is accepted only in 53-week ISO years (a phantom '2025-W53' would otherwise be
 * stored and then vanish from every weekly view).
 */
export function isValidIsoWeek(week: string | null | undefined): week is string {
  if (week == null || !/^\d{4}-W\d{2}$/.test(week)) return false
  const n = Number(week.slice(6))
  if (n < 1 || n > 53) return false
  return isoWeekOf(isoWeekMondayUnchecked(Number(week.slice(0, 4)), n)) === week
}

/** Monday (local date) of an ISO week 'YYYY-Www' — inverse of isoWeekOf. */
export function isoWeekMonday(week: string): string {
  if (!isValidIsoWeek(week)) throw new Error(`invalid ISO week: ${week}`)
  return isoWeekMondayUnchecked(Number(week.slice(0, 4)), Number(week.slice(6)))
}

/** Sunday (local date) of an ISO week — the latest date the week covers. */
export function isoWeekSunday(week: string): string {
  return fmtLocal(new Date(parseLocal(isoWeekMonday(week)).getTime() + 6 * DAY_MS))
}

/** The n consecutive ISO weeks starting with the week containing `dateLocal` (lookahead columns). */
export function isoWeeksFrom(dateLocal: string, n: number): string[] {
  const start = parseLocal(dateLocal)
  const weeks: string[] = []
  for (let i = 0; i < n; i++) {
    weeks.push(isoWeekOf(fmtLocal(new Date(start.getTime() + i * 7 * DAY_MS))))
  }
  return weeks
}

/**
 * Age in working days of a UTC timestamp as of `todayLocal`.
 */
export function ageWorkingDays(utcIso: string, todayLocal: string, cal: ProjectCalendar): number {
  return workingDaysBetween(localDate(utcIso, cal.timezone), todayLocal, cal)
}

/**
 * Days overdue (calendar) of a local need-by date as of today; 0 when not overdue.
 * Tolerant of a malformed stored date (returns 0) so derived status never crashes (I-4);
 * writes are separately validated to reject bad dates (PEC-NFR-010).
 */
export function daysOverdue(needByLocal: string | null, todayLocal: string): number {
  if (!isValidLocalDate(needByLocal)) return 0
  const d = calendarDaysBetween(needByLocal, todayLocal)
  return d > 0 ? d : 0
}

/** Working days overdue of a local need-by date as of today; 0 when not overdue (tolerant). */
export function workingDaysOverdue(
  needByLocal: string | null, todayLocal: string, cal: ProjectCalendar,
): number {
  if (!isValidLocalDate(needByLocal)) return 0
  return workingDaysBetween(needByLocal, todayLocal, cal)
}
