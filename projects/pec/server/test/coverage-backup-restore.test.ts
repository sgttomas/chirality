/**
 * PEC-NFR-009 — backup and restore, RPO ≤ 24 h, tested restore.
 *
 * Exercises tools/backup.ts as a child process (the exact artifact an operator runs),
 * against a scratch database — this is the automated "tested restore" the NFR asks for.
 * The remaining human step (one rehearsal against the real pilot DB) is scripted in
 * docs/PILOT.md and tools/pilot-drill.ts.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { spawnSync } from 'node:child_process'
import { DatabaseSync } from 'node:sqlite'
import { existsSync, mkdirSync, mkdtempSync, readdirSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { openDb, withTx } from '../src/db.ts'
import { Repo, nowIso } from '../src/repo.ts'

const TOOL = join(import.meta.dirname, '..', '..', 'tools', 'backup.ts')
const BACKUP_NAME = /^pec-\d{8}-\d{6}\.db$/

function runTool(env: Record<string, string>, ...args: string[]): { status: number; stdout: string; stderr: string } {
  const r = spawnSync(process.execPath, ['--disable-warning=ExperimentalWarning', TOOL, ...args], {
    env: { ...process.env, ...env },
    encoding: 'utf8',
  })
  return { status: r.status ?? -1, stdout: r.stdout ?? '', stderr: r.stderr ?? '' }
}

function personEmails(dbPath: string): string[] {
  const db = new DatabaseSync(dbPath, { readOnly: true })
  try {
    return (db.prepare('SELECT email FROM person ORDER BY email').all() as Array<{ email: string }>)
      .map((r) => r.email)
  } finally {
    db.close()
  }
}

test('PEC-NFR-009: backup → mutate → restore round-trip; prior database preserved aside', () => {
  const dir = mkdtempSync(join(tmpdir(), 'pec-nfr009-'))
  try {
    const dbPath = join(dir, 'pilot.db')
    const backupDir = join(dir, 'backups')
    const env = { PEC_DB: dbPath, PEC_BACKUP_DIR: backupDir }

    // A live database with a known record.
    const db = openDb(dbPath)
    const repo = new Repo(db)
    withTx(db, () => repo.insert('person', {
      name: 'Before Backup', email: 'before@pilot.co', passwordHash: 'x',
      isAdmin: false, discipline: null, createdAt: nowIso(),
    }))

    // Backup runs while the server-side connection is still open (WAL-safe VACUUM INTO).
    const bk = runTool(env)
    assert.equal(bk.status, 0, `backup failed: ${bk.stderr}`)
    const files = readdirSync(backupDir).filter((f) => BACKUP_NAME.test(f))
    assert.equal(files.length, 1, `expected one backup file, got ${files.join(', ')}`)

    // The backup itself is a healthy database containing the record.
    assert.deepEqual(personEmails(join(backupDir, files[0]!)), ['before@pilot.co'])

    // Mutate after the backup, then stop the "server".
    withTx(db, () => repo.insert('person', {
      name: 'After Backup', email: 'after@pilot.co', passwordHash: 'x',
      isAdmin: false, discipline: null, createdAt: nowIso(),
    }))
    db.close()
    // A leftover WAL sidecar must be moved aside with the database, never left to
    // corrupt the restored file (close() checkpoints the real one; simulate a crash).
    writeFileSync(`${dbPath}-wal`, 'stale sidecar')

    const rs = runTool(env, 'restore', files[0]!)
    assert.equal(rs.status, 0, `restore failed: ${rs.stderr}`)

    // Restored contents are the backup: the post-backup mutation is gone.
    assert.deepEqual(personEmails(dbPath), ['before@pilot.co'])
    // The pre-restore database is preserved, not deleted (PEC-NFR-002 spirit) — with both rows.
    assert.ok(existsSync(`${dbPath}.pre-restore`), 'live db moved aside to .pre-restore')
    assert.deepEqual(personEmails(`${dbPath}.pre-restore`), ['after@pilot.co', 'before@pilot.co'])
    assert.ok(existsSync(`${dbPath}.pre-restore-wal`), 'wal sidecar moved aside too')
    assert.ok(!existsSync(`${dbPath}-wal`), 'no stale wal next to the restored db')
  } finally {
    rmSync(dir, { recursive: true, force: true })
  }
})

test('PEC-NFR-009: restore refuses a corrupt backup and leaves the live database untouched', () => {
  const dir = mkdtempSync(join(tmpdir(), 'pec-nfr009-'))
  try {
    const dbPath = join(dir, 'pilot.db')
    const backupDir = join(dir, 'backups')
    const env = { PEC_DB: dbPath, PEC_BACKUP_DIR: backupDir }

    const db = openDb(dbPath)
    const repo = new Repo(db)
    withTx(db, () => repo.insert('person', {
      name: 'Live', email: 'live@pilot.co', passwordHash: 'x',
      isAdmin: false, discipline: null, createdAt: nowIso(),
    }))
    db.close()

    mkdirSync(backupDir, { recursive: true })
    writeFileSync(join(backupDir, 'pec-20200101-000000.db'), 'this is not a sqlite database')

    const rs = runTool(env, 'restore', 'pec-20200101-000000.db')
    assert.notEqual(rs.status, 0, 'restore of a corrupt backup must fail')
    assert.deepEqual(personEmails(dbPath), ['live@pilot.co'], 'live database untouched')
    assert.ok(!existsSync(`${dbPath}.pre-restore`), 'live database was never moved aside')
  } finally {
    rmSync(dir, { recursive: true, force: true })
  }
})

test('PEC-NFR-009: restore of an unknown backup name fails without touching anything', () => {
  const dir = mkdtempSync(join(tmpdir(), 'pec-nfr009-'))
  try {
    const dbPath = join(dir, 'pilot.db')
    const env = { PEC_DB: dbPath, PEC_BACKUP_DIR: join(dir, 'backups') }
    const db = openDb(dbPath)
    db.close()
    const rs = runTool(env, 'restore', 'pec-19990101-000000.db')
    assert.notEqual(rs.status, 0)
    assert.match(rs.stderr, /backup not found/)
  } finally {
    rmSync(dir, { recursive: true, force: true })
  }
})

test('backup prunes to the newest 14 (daily run ≈ two weeks of RPO ≤ 24 h coverage)', () => {
  const dir = mkdtempSync(join(tmpdir(), 'pec-nfr009-'))
  try {
    const dbPath = join(dir, 'pilot.db')
    const backupDir = join(dir, 'backups')
    const env = { PEC_DB: dbPath, PEC_BACKUP_DIR: backupDir }

    const db = openDb(dbPath)
    db.close()

    // 16 older dailies already on disk (prune sorts by name; fixed-width stamp = time order).
    mkdirSync(backupDir, { recursive: true })
    for (let i = 1; i <= 16; i++) {
      writeFileSync(join(backupDir, `pec-202401${String(i).padStart(2, '0')}-120000.db`), '')
    }
    const before = readdirSync(backupDir).filter((f) => BACKUP_NAME.test(f)).sort()
    assert.equal(before.length, 16)

    const bk = runTool(env)
    assert.equal(bk.status, 0, `backup failed: ${bk.stderr}`)

    const after = readdirSync(backupDir).filter((f) => BACKUP_NAME.test(f)).sort()
    assert.equal(after.length, 14, 'pruned to the newest 14')
    // The fresh backup (today's stamp sorts last) survived; the oldest dailies did not.
    assert.ok(after[after.length - 1]!.startsWith(`pec-${new Date().getFullYear()}`))
    assert.ok(!after.includes(before[0]!), 'oldest backup pruned')
    assert.ok(!after.includes(before[1]!), 'second-oldest backup pruned')
    assert.ok(!after.includes(before[2]!), 'third-oldest backup pruned')
  } finally {
    rmSync(dir, { recursive: true, force: true })
  }
})
