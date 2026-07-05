import { test } from 'node:test'
import assert from 'node:assert/strict'
import { spawnSync } from 'node:child_process'
import { DatabaseSync } from 'node:sqlite'
import { existsSync, mkdtempSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'

const PEC_ROOT = join(import.meta.dirname, '..', '..')

function runSeed(envPatch: Record<string, string | undefined> = {}): { status: number; stdout: string; stderr: string } {
  const env = { ...process.env }
  for (const [key, value] of Object.entries(envPatch)) {
    if (value === undefined) delete env[key]
    else env[key] = value
  }
  const r = spawnSync(process.execPath, ['--disable-warning=ExperimentalWarning', 'tools/seed.ts'], {
    cwd: PEC_ROOT,
    env,
    encoding: 'utf8',
  })
  return { status: r.status ?? -1, stdout: r.stdout ?? '', stderr: r.stderr ?? '' }
}

test('seed.demo refuses to run without an explicit PEC_DB', () => {
  const r = runSeed({ PEC_DB: undefined })
  assert.notEqual(r.status, 0)
  assert.match(r.stderr, /PEC_DB is required for demo seeding/)
})

test('seed.demo refuses a non-scratch/non-demo PEC_DB target', () => {
  const dbPath = join(PEC_ROOT, 'pec.db')
  const r = runSeed({ PEC_DB: dbPath })
  assert.notEqual(r.status, 0)
  assert.match(r.stderr, /Refusing to seed non-scratch\/non-demo database target/)
})

test('seed.demo honors PEC_DB for scratch/demo targets', () => {
  const dir = mkdtempSync(join(tmpdir(), 'pec-seed-demo-'))
  try {
    const dbPath = join(dir, 'demo.db')
    const r = runSeed({ PEC_DB: dbPath })
    assert.equal(r.status, 0, `seed failed: ${r.stderr}`)
    assert.ok(existsSync(dbPath), 'seeded database was created at PEC_DB')

    const db = new DatabaseSync(dbPath, { readOnly: true })
    try {
      const project = db.prepare('SELECT code, name FROM project').get() as { code: string; name: string }
      assert.equal(project.code, 'AUR')
      assert.equal(project.name, 'Aurora Gas Plant FEED')
      const admin = db.prepare('SELECT email FROM person WHERE is_admin = 1').get() as { email: string }
      assert.equal(admin.email, 'admin@aurora.dev')
    } finally {
      db.close()
    }
  } finally {
    rmSync(dir, { recursive: true, force: true })
  }
})
