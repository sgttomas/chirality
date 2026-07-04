import { test } from 'node:test'
import assert from 'node:assert/strict'
import {
  addWorkingDays, ageWorkingDays, calendarDaysBetween, daysOverdue, isWorkingDay,
  isoWeekOf, localDate, weekdayOf, workingDaysBetween,
} from '../src/calendar.ts'
import type { ProjectCalendar } from '../src/types.ts'

const cal: ProjectCalendar = { timezone: 'UTC', weekendDays: ['Sat', 'Sun'], holidays: ['2026-07-01'] }

test('localDate respects timezone (PEC-NFR-010)', () => {
  // 2026-07-15T02:00Z is still 2026-07-14 in Houston
  assert.equal(localDate('2026-07-15T02:00:00Z', 'America/Chicago'), '2026-07-14')
  assert.equal(localDate('2026-07-15T02:00:00Z', 'UTC'), '2026-07-15')
})

test('weekday and working day with holidays', () => {
  assert.equal(weekdayOf('2026-07-11'), 'Sat')
  assert.equal(isWorkingDay('2026-07-11', cal), false)
  assert.equal(isWorkingDay('2026-07-13', cal), true) // Monday
  assert.equal(isWorkingDay('2026-07-01', cal), false) // holiday
})

test('workingDaysBetween counts (a, b] working days only', () => {
  // Fri 2026-07-10 → Mon 2026-07-13: 1 working day
  assert.equal(workingDaysBetween('2026-07-10', '2026-07-13', cal), 1)
  // Mon → Fri same week: 4
  assert.equal(workingDaysBetween('2026-07-13', '2026-07-17', cal), 4)
  // b <= a → 0
  assert.equal(workingDaysBetween('2026-07-13', '2026-07-13', cal), 0)
  assert.equal(workingDaysBetween('2026-07-13', '2026-07-10', cal), 0)
  // holiday excluded: Jun 30 → Jul 2 spans holiday Jul 1
  assert.equal(workingDaysBetween('2026-06-30', '2026-07-02', cal), 1)
})

test('addWorkingDays lands on working days', () => {
  assert.equal(addWorkingDays('2026-07-10', 1, cal), '2026-07-13') // Fri + 1wd = Mon
  assert.equal(addWorkingDays('2026-07-13', 5, cal), '2026-07-20')
})

test('isoWeekOf', () => {
  assert.equal(isoWeekOf('2026-07-15'), '2026-W29')
  assert.equal(isoWeekOf('2026-01-01'), '2026-W01')
})

test('overdue helpers', () => {
  assert.equal(daysOverdue('2026-07-10', '2026-07-15'), 5)
  assert.equal(daysOverdue('2026-07-16', '2026-07-15'), 0)
  assert.equal(daysOverdue(null, '2026-07-15'), 0)
  assert.equal(calendarDaysBetween('2026-07-10', '2026-07-15'), 5)
  assert.equal(ageWorkingDays('2026-07-10T12:00:00Z', '2026-07-15', cal), 3)
})
