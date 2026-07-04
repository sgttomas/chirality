/**
 * Session auth (ADR-007): scrypt password hashes, DB-backed sessions,
 * httpOnly SameSite=Lax cookie. SSO (SAML/OIDC) is the P2 swap behind this module.
 */

import { randomBytes, scryptSync, timingSafeEqual } from 'node:crypto'
import type { Db } from './db.ts'
import { nowIso } from './repo.ts'
import { unauthorized } from './errors.ts'
import type { Role } from '@pec/core'

const SESSION_TTL_MS = 7 * 24 * 3600 * 1000
export const COOKIE_NAME = 'pec_session'

export function hashPassword(password: string): string {
  const salt = randomBytes(16).toString('hex')
  const hash = scryptSync(password, salt, 64).toString('hex')
  return `${salt}:${hash}`
}

export function verifyPassword(password: string, stored: string): boolean {
  const [salt, hash] = stored.split(':')
  if (!salt || !hash) return false
  const candidate = scryptSync(password, salt, 64)
  const expected = Buffer.from(hash, 'hex')
  return candidate.length === expected.length && timingSafeEqual(candidate, expected)
}

export interface SessionInfo {
  personId: number
  name: string
  email: string
  isAdmin: boolean
}

export function createSession(db: Db, personId: number): string {
  const token = randomBytes(32).toString('hex')
  db.prepare('INSERT INTO session (token, person_id, created_at, expires_at) VALUES (?, ?, ?, ?)')
    .run(token, personId, nowIso(), new Date(Date.now() + SESSION_TTL_MS).toISOString())
  return token
}

export function destroySession(db: Db, token: string): void {
  db.prepare('DELETE FROM session WHERE token = ?').run(token)
}

export function sessionFromToken(db: Db, token: string | undefined): SessionInfo | null {
  if (!token) return null
  const row = db.prepare(
    `SELECT s.person_id, s.expires_at, p.name, p.email, p.is_admin
     FROM session s JOIN person p ON p.id = s.person_id WHERE s.token = ?`,
  ).get(token) as { person_id: number; expires_at: string; name: string; email: string; is_admin: number } | undefined
  if (!row) return null
  if (row.expires_at < nowIso()) {
    destroySession(db, token)
    return null
  }
  return { personId: row.person_id, name: row.name, email: row.email, isAdmin: row.is_admin === 1 }
}

export function requireSession(db: Db, token: string | undefined): SessionInfo {
  const s = sessionFromToken(db, token)
  if (!s) throw unauthorized()
  return s
}

export function rolesFor(db: Db, projectId: number, personId: number): Role[] {
  const rows = db.prepare('SELECT role FROM project_role WHERE project_id = ? AND person_id = ?')
    .all(projectId, personId) as Array<{ role: Role }>
  return rows.map((r) => r.role)
}

export function login(db: Db, email: string, password: string): { token: string; session: SessionInfo } | null {
  const row = db.prepare('SELECT id, password_hash FROM person WHERE email = ?')
    .get(email) as { id: number; password_hash: string } | undefined
  if (!row || !verifyPassword(password, row.password_hash)) return null
  const token = createSession(db, row.id)
  return { token, session: requireSessionById(db, row.id) }
}

function requireSessionById(db: Db, personId: number): SessionInfo {
  const p = db.prepare('SELECT id, name, email, is_admin FROM person WHERE id = ?')
    .get(personId) as { id: number; name: string; email: string; is_admin: number }
  return { personId: p.id, name: p.name, email: p.email, isAdmin: p.is_admin === 1 }
}
