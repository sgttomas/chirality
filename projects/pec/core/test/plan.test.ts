/**
 * P2 planning & capacity derivations (PRD §12.4, §8.3/§8.4 P2 rules, I-9).
 * TODAY is 2026-07-15 (Wednesday) → current ISO week 2026-W29 (Mon 2026-07-13 .. Sun 2026-07-19).
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import {
  capacityBreaches, capacityView, deliverableStatus, isValidIsoWeek, isoWeekMonday, isoWeekOf,
  isoWeekSunday, isoWeeksFrom, lookahead, myWeek, packageStatus, planHorizons, projectSignals,
  projectStatus,
} from '../src/index.ts'
import * as fx from './fixtures.ts'

test('calendar: ISO week inverse helpers round-trip (Monday/Sunday, weeks-from)', () => {
  assert.equal(isoWeekOf('2026-07-15'), '2026-W29')
  assert.equal(isoWeekMonday('2026-W29'), '2026-07-13')
  assert.equal(isoWeekSunday('2026-W29'), '2026-07-19')
  assert.equal(isoWeekOf(isoWeekMonday('2026-W01')), '2026-W01')
  assert.throws(() => isoWeekMonday('2027-W53'), /invalid ISO week/, '2027 has 52 ISO weeks')
  assert.deepEqual(isoWeeksFrom('2026-07-15', 3), ['2026-W29', '2026-W30', '2026-W31'])
})

test('planHorizons resolves work items, checks, and approvals to their responsible people (PEC-PLAN-001)', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id })
  const rev = fx.revision({ deliverableId: d.id })
  const w = fx.workItem({ anchorType: 'deliverable', anchorId: d.id, packageId: p.id, ownerId: 7 })
  const chk = fx.check({ revisionId: rev.id, checkerId: 8 })
  const apr = fx.approval({ appliesToType: 'revision', appliesToId: rev.id, signatoryIds: [9] })
  const snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], workItems: [w], checks: [chk], approvalRecords: [apr],
    planItems: [
      fx.planItem({ itemType: 'work_item', itemId: w.id, horizon: 'now', week: '2026-W29' }),
      fx.planItem({ itemType: 'check', itemId: chk.id, horizon: 'next', week: '2026-W30' }),
      fx.planItem({ itemType: 'approval_record', itemId: apr.id, horizon: 'later', week: null }),
    ],
  })
  const h = planHorizons(snap)
  assert.equal(h.now.length, 1)
  assert.equal(h.now[0]!.responsibleId, 7)
  assert.equal(h.now[0]!.deliverable?.id, d.id)
  assert.equal(h.next[0]!.responsibleId, 8)
  assert.equal(h.next[0]!.packageId, p.id, 'check attributes to the package via its revision')
  assert.equal(h.later[0]!.responsibleId, 9)
})

test('I-9: check and approval hours load capacity like work hours; levels per §8.4 P2 thresholds', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id })
  const rev = fx.revision({ deliverableId: d.id })
  const w = fx.workItem({ anchorType: 'deliverable', anchorId: d.id, packageId: p.id })
  const chk = fx.check({ revisionId: rev.id })
  const apr = fx.approval({ appliesToType: 'revision', appliesToId: rev.id })
  const base = {
    packages: [p], deliverables: [d], revisions: [rev], workItems: [w], checks: [chk], approvalRecords: [apr],
    capacityEntries: [fx.capacity({ week: '2026-W29', discipline: 'Process', hours: 40 })],
  }
  const snap = fx.snapshot({
    ...base,
    planItems: [
      fx.planItem({ itemType: 'work_item', itemId: w.id, plannedHours: 8, discipline: 'Process' }),
      fx.planItem({ itemType: 'check', itemId: chk.id, plannedHours: 30, discipline: 'Process' }),
      fx.planItem({ itemType: 'approval_record', itemId: apr.id, plannedHours: 8, discipline: 'Process' }),
    ],
  })
  const cells = capacityView(snap, ['2026-W29'])
  assert.equal(cells.length, 1)
  const c = cells[0]!
  assert.equal(c.loadH, 46, 'work 8 + check 30 + approval 8 all load (I-9)')
  assert.deepEqual(c.byType, { work_item: 8, check: 30, approval_record: 8 })
  assert.equal(c.pct, 115)
  assert.equal(c.level, 'red', '> 110% escalates (§8.4 capacity row)')

  // accepted/closed underlying records stop loading capacity
  const snapDone = fx.snapshot({
    ...base,
    checks: [{ ...chk, state: 'accepted' as const }],
    planItems: [
      fx.planItem({ itemType: 'work_item', itemId: w.id, plannedHours: 8, discipline: 'Process' }),
      fx.planItem({ itemType: 'check', itemId: chk.id, plannedHours: 30, discipline: 'Process' }),
    ],
  })
  const c2 = capacityView(snapDone, ['2026-W29'])[0]!
  assert.equal(c2.loadH, 8, 'accepted check no longer loads')
  assert.equal(c2.level, 'none')
})

test('PH-R3/PH-A3: current-week capacity breach in a discipline the package draws on (§8.3 P2)', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2027-01-01' })
  const rev = fx.revision({ deliverableId: d.id })
  const w = fx.workItem({ anchorType: 'deliverable', anchorId: d.id, packageId: p.id })
  const mk = (hours: number) => fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], workItems: [w],
    capacityEntries: [fx.capacity({ week: isoWeekOf('2026-07-15'), discipline: 'Process', hours: 40 })],
    planItems: [fx.planItem({ itemType: 'work_item', itemId: w.id, week: isoWeekOf('2026-07-15'), plannedHours: hours, discipline: 'Process' })],
  })
  const red = packageStatus(mk(46), p)
  assert.equal(red.health.value, 'red')
  assert.equal(red.health.ruleId, 'PH-R3')
  assert.ok(red.health.contributing.some((c) => c.recordType === 'plan_item'), 'plan items contribute')

  const amber = packageStatus(mk(42), p)
  assert.equal(amber.health.value, 'amber')
  assert.equal(amber.health.ruleId, 'PH-A3') // 105%: > 100, <= 110

  const ok = packageStatus(mk(30), p)
  assert.equal(ok.health.ruleId, 'PH-G')
})

test('S-CAP: capacity signal escalates project health (§8.4 P2)', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2027-01-01' })
  const rev = fx.revision({ deliverableId: d.id })
  const w = fx.workItem({ anchorType: 'deliverable', anchorId: d.id, packageId: p.id })
  const snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], workItems: [w],
    capacityEntries: [fx.capacity({ week: isoWeekOf('2026-07-15'), discipline: 'Process', hours: 40 })],
    planItems: [fx.planItem({ itemType: 'work_item', itemId: w.id, week: isoWeekOf('2026-07-15'), plannedHours: 46, discipline: 'Process' })],
  })
  const sig = projectSignals(snap).find((s) => s.id === 'S-CAP')!
  assert.equal(sig.level, 'red')
  assert.equal(projectStatus(snap).health.value, 'red')
  assert.equal(capacityBreaches(snap).length, 1)
  // breaches are current-week only
  const future = fx.snapshot({
    ...snap,
    planItems: [fx.planItem({ itemType: 'work_item', itemId: w.id, week: '2026-W32', plannedHours: 46, discipline: 'Process' })],
    capacityEntries: [fx.capacity({ week: '2026-W32', discipline: 'Process', hours: 40 })],
  })
  assert.equal(capacityBreaches(future).length, 0, 'a future-week overload is not the current-week rule')
})

test('lookahead: cell priority hold > issue > approve > check > work; schedule import feeds work (PEC-PLAN-002)', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2026-07-16' }) // due falls in current week
  const rev = fx.revision({ deliverableId: d.id })
  const chk = fx.check({ revisionId: rev.id })
  const weeks = ['2026-W29', '2026-W30', '2026-W31']

  // no hold: current week shows the due date as Issue
  let snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], checks: [chk],
    planItems: [fx.planItem({ itemType: 'check', itemId: chk.id, week: '2026-W30' })],
    scheduleActivities: [fx.scheduleActivity({ deliverableId: d.id, startDate: '2026-07-27', finishDate: '2026-07-31' })],
  })
  let row = lookahead(snap, weeks).find((r) => r.deliverable.id === d.id)!
  assert.equal(row.cells[0]?.state, 'issue')
  assert.equal(row.cells[1]?.state, 'check')
  assert.equal(row.cells[2]?.state, 'work', 'schedule activity spanning W31 → work')

  // an active hold takes priority in the current week, typed by cause
  const h = fx.hold({ cause: 'vendor_data' })
  snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], checks: [chk],
    holds: [h], holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'deliverable', targetId: d.id })],
  })
  row = lookahead(snap, weeks).find((r) => r.deliverable.id === d.id)!
  assert.equal(row.cells[0]?.state, 'hold')
  assert.match(row.cells[0]!.detail, /vendor_data/, 'hold-by-cause (PEC-PLAN-002)')
})

test('plan-sourced forecast: planned week ends and schedule finishes drive slip (SPEC §6.1 P2)', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2026-07-16' })
  const rev = fx.revision({ deliverableId: d.id })
  const w = fx.workItem({ anchorType: 'deliverable', anchorId: d.id, packageId: p.id }) // no need-by
  const snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], workItems: [w],
    planItems: [fx.planItem({ itemType: 'work_item', itemId: w.id, week: '2026-W31' })],
  })
  const s = deliverableStatus(snap, d)
  assert.equal(s.forecastDate, isoWeekSunday('2026-W31'), 'forecast = Sunday of the latest planned week')
  assert.ok(s.forecastSlipWd > 5, `slip ${s.forecastSlipWd} wd`)
  assert.equal(s.health.ruleId, 'DH-R1')
})

test('PH-A4: interface aging below escalation feeds package health amber (PEC-PKG-008)', () => {
  const p = fx.pkg()
  const i = fx.interfaceItem({ receivingPackageId: p.id, needBy: '2026-07-10', state: 'open' }) // 3 wd overdue
  const snap = fx.snapshot({ packages: [p], interfaces: [i] })
  const s = packageStatus(snap, p)
  assert.equal(s.health.value, 'amber')
  assert.equal(s.health.ruleId, 'PH-A4')
  assert.equal(s.health.contributing[0]!.recordType, 'interface_item')
})

test('capacity edge cases: threshold compares the raw ratio; zero-hour baseline with load is red', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id })
  const rev = fx.revision({ deliverableId: d.id })
  const w = fx.workItem({ anchorType: 'deliverable', anchorId: d.id, packageId: p.id })
  // 1104/1000 = 110.4% — rounds to 110 but must escalate (> 110 on the raw ratio)
  let snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], workItems: [w],
    capacityEntries: [fx.capacity({ hours: 1000 })],
    planItems: [fx.planItem({ itemType: 'work_item', itemId: w.id, plannedHours: 1104 })],
  })
  let c = capacityView(snap, ['2026-W29'])[0]!
  assert.equal(c.pct, 110)
  assert.equal(c.level, 'red', 'raw 110.4% escalates even though it rounds to 110')

  // explicit zero-hour capacity with planned load = unbounded overload, not "no baseline"
  snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], workItems: [w],
    capacityEntries: [fx.capacity({ hours: 0 })],
    planItems: [fx.planItem({ itemType: 'work_item', itemId: w.id, plannedHours: 8 })],
  })
  c = capacityView(snap, ['2026-W29'])[0]!
  assert.equal(c.pct, null)
  assert.equal(c.level, 'red')
})

test('calendar: isValidIsoWeek rejects phantom W53 in 52-week ISO years', () => {
  assert.equal(isValidIsoWeek('2026-W53'), true, '2026 is a 53-week ISO year')
  assert.equal(isoWeekOf(isoWeekMonday('2026-W53')), '2026-W53')
  assert.equal(isValidIsoWeek('2025-W53'), false, '2025 has 52 ISO weeks')
  assert.equal(isValidIsoWeek('2026-W00'), false)
  assert.equal(isValidIsoWeek('2026-W54'), false)
})

test('plan-sourced forecast: schedule finishes stop forecasting once the deliverable is issued', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2026-07-16' })
  const rev = fx.revision({ deliverableId: d.id, state: 'issued' })
  const snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev],
    scheduleActivities: [fx.scheduleActivity({ deliverableId: d.id, startDate: '2026-07-20', finishDate: '2026-08-14' })],
  })
  const s = deliverableStatus(snap, d)
  assert.equal(s.forecastSlipWd, 0, 'an issued deliverable is not kept red by a stale schedule row')
  assert.equal(s.health.ruleId, 'DH-G')
})

test('myWeek: plan-committed items say so (PEC-PLAN-007 / PEC-MW-005)', () => {
  const week = isoWeekOf('2026-07-15')
  const manual = fx.workItem({ ownerId: 1, committedWeek: week, commitSource: 'manual' })
  const planned = fx.workItem({ ownerId: 1, committedWeek: week, commitSource: 'plan' })
  const snap = fx.snapshot({ workItems: [manual, planned] })
  const mw = myWeek(snap, 1)
  const whyOf = (id: number): string => mw.committed.find((x) => x.workItem.id === id)!.whyInWeek
  assert.match(whyOf(manual.id), /manual/)
  assert.match(whyOf(planned.id), /planning commitment/)
})
