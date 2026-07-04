/**
 * Shared input validation for controlled-record writes (PEC-NFR-010).
 * Malformed dates must be rejected at write time (400) — the derived-status layer
 * computes on read and must never crash on stored data (I-4). Defense in depth:
 * the calendar layer also tolerates a bad stored date, but writes never store one.
 */

import { badRequest } from './errors.ts'

const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/

/** Assert a value is a valid YYYY-MM-DD local date (or null/undefined). Returns the value or null. */
export function optDate(value: unknown, field: string): string | null {
  if (value == null || value === '') return null
  if (typeof value !== 'string' || !ISO_DATE.test(value)) {
    throw badRequest(`${field} must be a date in YYYY-MM-DD format (PEC-NFR-010), got: ${JSON.stringify(value)}`)
  }
  // reject impossible calendar dates (e.g. 2026-13-40)
  const d = new Date(`${value}T00:00:00Z`)
  if (Number.isNaN(d.getTime()) || d.toISOString().slice(0, 10) !== value) {
    throw badRequest(`${field} is not a real date: ${value}`)
  }
  return value
}

/** Assert a value is a valid non-empty date. */
export function reqDate(value: unknown, field: string): string {
  const d = optDate(value, field)
  if (d == null) throw badRequest(`${field} is required (PEC-NFR-010)`)
  return d
}
