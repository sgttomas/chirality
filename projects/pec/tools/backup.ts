/**
 * Backup / restore for the PEC SQLite database (SPEC §12 Operations, PEC-NFR-009).
 *
 * Usage:
 *   node tools/backup.ts                  # same as `backup`
 *   node tools/backup.ts backup           # WAL-safe snapshot → backups/pec-YYYYMMDD-HHMMSS.db
 *   node tools/backup.ts restore <file>   # restore a backup over pec.db (stop the server first)
 *
 * `backup` uses SQLite's `VACUUM INTO`, which writes a consistent single-file
 * snapshot even while the server holds the database open in WAL mode — no wal/shm
 * sidecar files to copy, no torn pages. The newest 14 backups are kept (a daily
 * run keeps two weeks of RPO ≤ 24 h coverage); older ones are pruned.
 *
 * `restore` never destroys the live database: it is moved aside to
 * `pec.db.pre-restore` (with its -wal/-shm sidecars) before the chosen backup is
 * copied into place. Restart the server afterwards so it reopens the new file.
 *
 * Honors PEC_DB (same variable the server uses, server/src/index.ts); defaults to
 * <repo>/pec.db. Backups land in PEC_BACKUP_DIR or <repo>/backups.
 */

import { DatabaseSync } from 'node:sqlite'
import {
  copyFileSync, existsSync, mkdirSync, readdirSync, renameSync, statSync, unlinkSync,
} from 'node:fs'
import { basename, dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const root = join(here, '..') // tools/ → repo root
const DB_PATH = process.env.PEC_DB ?? join(root, 'pec.db')
const BACKUP_DIR = process.env.PEC_BACKUP_DIR ?? join(root, 'backups')
const KEEP = 14
const BACKUP_NAME = /^pec-\d{8}-\d{6}\.db$/

function usage(): never {
  console.error('usage: node tools/backup.ts [backup|restore <file>]')
  process.exit(2)
}

function fail(msg: string): never {
  console.error(`error: ${msg}`)
  process.exit(1)
}

/** Local-time YYYYMMDD-HHMMSS, matching the pruning pattern. */
function stamp(now: Date): string {
  const p = (n: number, w = 2): string => String(n).padStart(w, '0')
  return `${now.getFullYear()}${p(now.getMonth() + 1)}${p(now.getDate())}`
    + `-${p(now.getHours())}${p(now.getMinutes())}${p(now.getSeconds())}`
}

function fmtSize(bytes: number): string {
  if (bytes >= 1024 * 1024) return `${(bytes / (1024 * 1024)).toFixed(1)} MiB`
  if (bytes >= 1024) return `${(bytes / 1024).toFixed(1)} KiB`
  return `${bytes} B`
}

/** Keep the newest KEEP backups; the fixed-width timestamp makes name order = time order. */
function prune(): void {
  const files = readdirSync(BACKUP_DIR)
    .filter((f) => BACKUP_NAME.test(f))
    .sort()
    .reverse()
  for (const f of files.slice(KEEP)) {
    unlinkSync(join(BACKUP_DIR, f))
    console.log(`pruned old backup: ${f}`)
  }
}

function doBackup(): void {
  if (!existsSync(DB_PATH)) fail(`database not found: ${DB_PATH}`)
  mkdirSync(BACKUP_DIR, { recursive: true })
  const target = join(BACKUP_DIR, `pec-${stamp(new Date())}.db`)
  if (existsSync(target)) unlinkSync(target) // same-second rerun: VACUUM INTO refuses existing targets

  // VACUUM INTO reads a consistent snapshot through the normal connection, so it is
  // WAL-safe against a live server (PEC-NFR-009).
  const db = new DatabaseSync(DB_PATH)
  try {
    db.prepare('VACUUM INTO ?').run(target)
  } finally {
    db.close()
  }

  const size = statSync(target).size
  console.log(`backup written: ${target} (${fmtSize(size)})`)
  prune()
}

function doRestore(nameArg: string | undefined): void {
  if (!nameArg) usage()
  // Accept a path as given, or a bare filename looked up in the backup directory.
  let source = resolve(nameArg)
  if (!existsSync(source)) source = join(BACKUP_DIR, basename(nameArg))
  if (!existsSync(source)) fail(`backup not found: ${nameArg} (looked in ${BACKUP_DIR})`)
  if (resolve(source) === resolve(DB_PATH)) fail('refusing to restore the live database onto itself')

  // Sanity: the backup must be a readable, intact SQLite file before we touch pec.db.
  const check = new DatabaseSync(source, { readOnly: true })
  try {
    const row = check.prepare('PRAGMA integrity_check').get() as Record<string, string>
    const verdict = Object.values(row)[0]
    if (verdict !== 'ok') fail(`backup failed integrity_check: ${verdict}`)
  } finally {
    check.close()
  }

  // Move the current database aside — never deleted (in the spirit of PEC-NFR-002).
  if (existsSync(DB_PATH)) {
    renameSync(DB_PATH, `${DB_PATH}.pre-restore`)
    console.log(`current database moved aside: ${DB_PATH}.pre-restore`)
  }
  for (const ext of ['-wal', '-shm']) {
    if (existsSync(DB_PATH + ext)) renameSync(DB_PATH + ext, `${DB_PATH}.pre-restore${ext}`)
  }

  copyFileSync(source, DB_PATH)
  console.log(`restored: ${source} → ${DB_PATH}`)
  console.log('')
  console.log('Next steps:')
  console.log('  1. If the PEC server was running during the restore, stop it now — it must')
  console.log('     not keep writing to the replaced file.')
  console.log('  2. Restart the server:  npm start   (or npm run dev:server)')
  console.log(`  3. Verify, then keep or remove ${basename(DB_PATH)}.pre-restore* as you see fit.`)
}

const [cmd = 'backup', arg] = process.argv.slice(2)
if (cmd === 'backup' && arg === undefined) doBackup()
else if (cmd === 'restore') doRestore(arg)
else usage()
