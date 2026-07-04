/**
 * PEC-NFR-003 (history-independence of the snapshot): repo.snapshot() reads the live record
 * tables (project/package/deliverable/revision/work_item/hold/decision/check/... ) but NEVER
 * touches history_entry (see repo.ts snapshot(), lines ~220-275 — there is no history_entry
 * SELECT anywhere in it). This file proves that empirically: with a MODEST live dataset but a
 * quarter-million history_entry rows, snapshot() — and a derived view built on top of it —
 * still render well under the 2s budget. If a future change reintroduced a history scan into
 * the snapshot path, the 250k rows would blow this out and the test would fail.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { randomBytes } from 'node:crypto'
import { openDb, withTx } from '../src/db.ts'
import { Repo, nowIso } from '../src/repo.ts'
import type { Sx } from '../src/services/shared.ts'
import { overviewView } from '../src/services/views.ts'

const LIVE = 1000        // deliverables / revisions / work-items (kept modest so the test is fast)
const HISTORY_ROWS = 250_000
const BUDGET_MS = 1500   // well under the 2s NFR budget

interface Seeded { db: ReturnType<typeof openDb>; repo: Repo; sx: Sx; pid: number; owner: number }

/** Seed one project: LIVE live records + HISTORY_ROWS history_entry rows (single bulk withTx). */
function seed(): Seeded {
  const db = openDb(join(tmpdir(), `pec-load-history-${randomBytes(6).toString('hex')}.db`))
  const repo = new Repo(db)
  const now = nowIso()

  const owner = repo.insert('person', {
    name: 'O', email: `o-${randomBytes(4).toString('hex')}@t.co`,
    passwordHash: 'x', isAdmin: 1, discipline: null, createdAt: now,
  })
  const pid = repo.insert('project', {
    code: `LOADH-${randomBytes(3).toString('hex')}`, name: 'LOADH', timezone: 'UTC',
    weekendDays: ['Sat', 'Sun'], holidays: [], thresholds: {}, config: {},
  })

  const pkgIds: number[] = []
  withTx(db, () => { for (let i = 0; i < 10; i++) pkgIds.push(repo.insert('package', { projectId: pid, code: `P${i}`, name: `p${i}`, leadId: owner })) })

  const revIds: number[] = []
  const delIds: number[] = []
  withTx(db, () => {
    for (let i = 0; i < LIVE; i++) {
      const d = repo.insert('deliverable', { projectId: pid, packageId: pkgIds[i % pkgIds.length]!, docNo: `D${i}`, title: `d${i}`, discipline: 'Process', deliverableType: 'drawing', ownerId: owner, dueDate: '2027-06-30' })
      delIds.push(d)
      revIds.push(repo.insert('revision', { projectId: pid, deliverableId: d, revCode: 'A', state: 'in_work', createdAt: now, createdBy: owner }))
    }
  })
  withTx(db, () => {
    for (let i = 0; i < LIVE; i++) {
      repo.insert('work_item', { projectId: pid, ref: `WI${i}`, title: `w${i}`, kind: 'action', log: 'internal', anchorType: 'revision', anchorId: revIds[i % revIds.length]!, packageId: pkgIds[i % pkgIds.length], ownerId: owner, state: 'open', needBy: '2027-01-01', createdBy: owner, createdAt: now })
    }
  })

  // ~250k history_entry rows, spread across the live records, in ONE transaction.
  // Uses a single prepared statement to keep insert cost low; snapshot() must ignore all of them.
  withTx(db, () => {
    const stmt = db.prepare(
      'INSERT INTO history_entry (project_id, record_type, record_id, at, actor_id, kind, summary, payload, authority_ref) VALUES (?,?,?,?,?,?,?,?,?)',
    )
    for (let i = 0; i < HISTORY_ROWS; i++) {
      const rid = delIds[i % delIds.length]!
      stmt.run(pid, 'deliverable', rid, now, owner, 'transition', `event ${i}`, null, null)
    }
  })

  const session = { personId: owner, name: 'O', email: 'o@t.co', isAdmin: true }
  const sx: Sx = { db, repo, projectId: pid, session, roles: [] as never }
  return { db, repo, sx, pid, owner }
}

function median(fn: () => unknown, runs = 5): number {
  fn() // warm
  const s: number[] = []
  for (let i = 0; i < runs; i++) {
    const t = process.hrtime.bigint()
    fn()
    s.push(Number((process.hrtime.bigint() - t) / 1000n) / 1000)
  }
  return s.sort((a, b) => a - b)[Math.floor(s.length / 2)]!
}

test('PEC-NFR-003: 250k history rows are actually present but snapshot ignores them', () => {
  const s = seed()
  try {
    const hist = s.db.prepare('SELECT COUNT(*) c FROM history_entry WHERE project_id = ?').get(s.pid) as { c: number }
    assert.equal(hist.c, HISTORY_ROWS, 'the heavy history table really was seeded')

    // Sanity: the snapshot returns the LIVE dataset (not the history rows) — proves it read the
    // record tables, so its speed below is a real result, not an empty-scan artifact.
    const snap = s.repo.snapshot(s.pid)
    assert.equal(snap.deliverables.length, LIVE)
    assert.equal(snap.revisions.length, LIVE)
    assert.equal(snap.workItems.length, LIVE)
    // ProjectSnapshot has no `history` field at all — it is not part of the snapshot contract.
    assert.equal((snap as unknown as Record<string, unknown>).history, undefined)
  } finally {
    s.db.close()
  }
})

test('PEC-NFR-003: repo.snapshot() median stays well under budget despite 250k history rows', () => {
  const s = seed()
  try {
    const t = median(() => s.repo.snapshot(s.pid))
    assert.ok(t <= BUDGET_MS, `snapshot ${t.toFixed(0)}ms must be <= ${BUDGET_MS}ms with ${HISTORY_ROWS} history rows present`)
  } finally {
    s.db.close()
  }
})

test('PEC-NFR-003: derived overviewView also renders under budget with 250k history rows', () => {
  const s = seed()
  try {
    const t = median(() => overviewView(s.sx))
    assert.ok(t <= BUDGET_MS, `overviewView ${t.toFixed(0)}ms must be <= ${BUDGET_MS}ms with ${HISTORY_ROWS} history rows present`)
  } finally {
    s.db.close()
  }
})

test('PEC-NFR-003: snapshot cost is independent of history volume (light vs heavy history are comparable)', () => {
  // Build a second project inside the SAME db with the same live dataset but almost no history,
  // then compare snapshot timings. History-independence means the heavy-history project is not
  // dramatically slower — its snapshot never scanned the extra rows.
  const s = seed()
  try {
    const now = nowIso()
    const owner2 = s.repo.insert('person', { name: 'O2', email: `o2-${randomBytes(4).toString('hex')}@t.co`, passwordHash: 'x', isAdmin: 1, discipline: null, createdAt: now })
    const pid2 = s.repo.insert('project', { code: `LOADL-${randomBytes(3).toString('hex')}`, name: 'LOADL', timezone: 'UTC', weekendDays: ['Sat', 'Sun'], holidays: [], thresholds: {}, config: {} })
    const pkg2: number[] = []
    withTx(s.db, () => { for (let i = 0; i < 10; i++) pkg2.push(s.repo.insert('package', { projectId: pid2, code: `P${i}`, name: `p${i}`, leadId: owner2 })) })
    const rev2: number[] = []
    withTx(s.db, () => {
      for (let i = 0; i < LIVE; i++) {
        const d = s.repo.insert('deliverable', { projectId: pid2, packageId: pkg2[i % pkg2.length]!, docNo: `D${i}`, title: `d${i}`, discipline: 'Process', deliverableType: 'drawing', ownerId: owner2, dueDate: '2027-06-30' })
        rev2.push(s.repo.insert('revision', { projectId: pid2, deliverableId: d, revCode: 'A', state: 'in_work', createdAt: now, createdBy: owner2 }))
      }
    })
    withTx(s.db, () => {
      for (let i = 0; i < LIVE; i++) {
        s.repo.insert('work_item', { projectId: pid2, ref: `WI${i}`, title: `w${i}`, kind: 'action', log: 'internal', anchorType: 'revision', anchorId: rev2[i % rev2.length]!, packageId: pkg2[i % pkg2.length], ownerId: owner2, state: 'open', needBy: '2027-01-01', createdBy: owner2, createdAt: now })
      }
    })

    const heavy = median(() => s.repo.snapshot(s.pid))   // 250k history rows
    const light = median(() => s.repo.snapshot(pid2))    // ~0 history rows
    // Both must be under budget, and the heavy one must not be an order of magnitude slower —
    // if a history scan crept into snapshot(), heavy would balloon relative to light.
    assert.ok(heavy <= BUDGET_MS, `heavy-history snapshot ${heavy.toFixed(0)}ms must be <= ${BUDGET_MS}ms`)
    assert.ok(light <= BUDGET_MS, `light-history snapshot ${light.toFixed(0)}ms must be <= ${BUDGET_MS}ms`)
    // Allow generous slack for timing noise on small absolute durations, but a real history
    // scan of 250k rows would be far more than a 6x factor over the ~0-history baseline.
    assert.ok(heavy <= Math.max(light * 6, light + 200),
      `history-independent: heavy ${heavy.toFixed(0)}ms should track light ${light.toFixed(0)}ms, not scale with 250k history rows`)
  } finally {
    s.db.close()
  }
})
