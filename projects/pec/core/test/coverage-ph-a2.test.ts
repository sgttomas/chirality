import { test } from 'node:test'
import assert from 'node:assert/strict'
import { packageStatus } from '../src/status.ts'
import * as fx from './fixtures.ts'

// TODAY = 2026-07-15 (Wed). PH-A2: a package-level decision (packageId == pkg.id) in an
// undecided state (identified | in_progress | pending) with need-by past → amber, ruleId 'PH-A2'.
// PH-A2 is only reached when the earlier red/amber rules (PH-R1/R2/A1) do not fire, so every
// case below keeps its single deliverable green (PH-A1 needs >= 20% pressured to fire).

/** A package with one green deliverable — no PH-R1/R2/A1 pressure of its own. */
function greenPackage() {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2026-08-01' })
  const rev = fx.revision({ deliverableId: d.id })
  return { p, d, rev }
}

test('PH-A2: package-level decision past need-by, state pending → amber with the decision contributing', () => {
  const { p, d, rev } = greenPackage()
  const dec = fx.decision({ packageId: p.id, state: 'pending', needBy: '2026-07-01' }) // 14 d past
  const snap = fx.snapshot({ packages: [p], deliverables: [d], revisions: [rev], decisions: [dec] })

  const s = packageStatus(snap, p)
  assert.equal(s.health.value, 'amber')
  assert.equal(s.health.ruleId, 'PH-A2')
  // I-4: the contributing set names the offending decision.
  assert.equal(s.health.contributing.length, 1)
  const c = s.health.contributing[0]!
  assert.equal(c.recordType, 'decision')
  assert.equal(c.id, dec.id)
  assert.equal(c.ref, dec.ref)
  assert.match(c.why, /state pending/)
  // the single deliverable is still green — proving PH-A1 did not fire ahead of PH-A2
  assert.equal(s.deliverableStatuses[0]!.health.value, 'green')
})

test('PH-A2: fires for identified and in_progress states too (all three undecided states)', () => {
  for (const state of ['identified', 'in_progress', 'pending'] as const) {
    const { p, d, rev } = greenPackage()
    const dec = fx.decision({ packageId: p.id, state, needBy: '2026-07-05' }) // 10 d past
    const snap = fx.snapshot({ packages: [p], deliverables: [d], revisions: [rev], decisions: [dec] })
    const s = packageStatus(snap, p)
    assert.equal(s.health.ruleId, 'PH-A2', `state ${state}: should trigger PH-A2`)
    assert.equal(s.health.value, 'amber', `state ${state}: amber`)
  }
})

test('PH-A2 negative: a decided decision past need-by does NOT trigger → package stays green', () => {
  const { p, d, rev } = greenPackage()
  const dec = fx.decision({ packageId: p.id, state: 'decided', needBy: '2026-07-01' }) // past but decided
  const snap = fx.snapshot({ packages: [p], deliverables: [d], revisions: [rev], decisions: [dec] })

  const s = packageStatus(snap, p)
  assert.equal(s.health.value, 'green')
  assert.equal(s.health.ruleId, 'PH-G')
})

test('PH-A2 negative: an undecided decision with a future need-by does NOT trigger → package stays green', () => {
  const { p, d, rev } = greenPackage()
  const dec = fx.decision({ packageId: p.id, state: 'pending', needBy: '2026-08-01' }) // future
  const snap = fx.snapshot({ packages: [p], deliverables: [d], revisions: [rev], decisions: [dec] })

  const s = packageStatus(snap, p)
  assert.equal(s.health.value, 'green')
  assert.equal(s.health.ruleId, 'PH-G')
})

test('PH-A2 scoping: an overdue undecided decision on ANOTHER package does not amber this package', () => {
  const { p, d, rev } = greenPackage()
  const other = fx.pkg()
  // overdue undecided decision, but pinned to the other package
  const dec = fx.decision({ packageId: other.id, state: 'pending', needBy: '2026-07-01' })
  const snap = fx.snapshot({ packages: [p, other], deliverables: [d], revisions: [rev], decisions: [dec] })

  const s = packageStatus(snap, p)
  assert.equal(s.health.value, 'green')
  assert.equal(s.health.ruleId, 'PH-G')
  // and the other package (which owns the decision, has no deliverables) does go amber via PH-A2
  const so = packageStatus(snap, other)
  assert.equal(so.health.ruleId, 'PH-A2')
  assert.equal(so.health.value, 'amber')
})
