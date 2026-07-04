import { test } from 'node:test'
import assert from 'node:assert/strict'
import { deliverableStatus, myWeek, packageStatus, projectStatus, waitingOnYou, workflowCompleteness } from '../src/status.ts'
import * as fx from './fixtures.ts'

// TODAY = 2026-07-15 (Wed)

// ---------- workflow completeness (deliverable status = production-workflow progress) ----------

type WorkflowKey = 'drafted' | 'checked' | 'approved' | 'issued'

test('workflowCompleteness: no revision → nothing started, 0%', () => {
  const d = fx.deliverable()
  const snap = fx.snapshot({ deliverables: [d] })
  const w = workflowCompleteness(snap, d)
  assert.equal(w.currentState, 'no_revision')
  assert.equal(w.gatesClosed, 0)
  assert.equal(w.pct, 0)
  assert.ok(w.stages.every((s) => s.state === 'pending'))
})

test('workflowCompleteness: maps each revision state to closed gates + a single current stage', () => {
  const cases: Array<[string, number, WorkflowKey | null]> = [
    ['in_work', 0, 'checked'],
    ['in_check', 0, 'checked'],
    ['check_accepted', 1, 'approved'],
    ['ready_for_approval', 1, 'approved'],
    ['approved', 2, 'issued'],
    ['issued', 3, null],
  ]
  for (const [state, gatesClosed, current] of cases) {
    const d = fx.deliverable()
    const rev = fx.revision({ deliverableId: d.id, state: state as never })
    const w = workflowCompleteness(fx.snapshot({ deliverables: [d], revisions: [rev] }), d)
    assert.equal(w.gatesClosed, gatesClosed, `${state}: gatesClosed`)
    assert.equal(w.stages.find((s) => s.state === 'current')?.key ?? null, current, `${state}: current stage`)
    assert.equal(w.stages[0]!.state, 'done', `${state}: drafted always done when a revision exists`)
    assert.equal(w.stages.filter((s) => s.state === 'done').length, gatesClosed + 1, `${state}: done count`)
  }
})

test('workflowCompleteness: issued is 100% with every stage done and none current', () => {
  const d = fx.deliverable()
  const rev = fx.revision({ deliverableId: d.id, state: 'issued' })
  const w = workflowCompleteness(fx.snapshot({ deliverables: [d], revisions: [rev] }), d)
  assert.equal(w.pct, 100)
  assert.equal(w.label, 'issued')
  assert.ok(w.stages.every((s) => s.state === 'done'))
  assert.equal(w.stages.find((s) => s.state === 'current'), undefined)
})

test('workflowCompleteness: returned-with-comments reopens the workflow (no closed gates, flagged)', () => {
  const d = fx.deliverable()
  const rev = fx.revision({ deliverableId: d.id, state: 'returned_with_comments' })
  const w = workflowCompleteness(fx.snapshot({ deliverables: [d], revisions: [rev] }), d)
  assert.equal(w.returned, true)
  assert.equal(w.gatesClosed, 0)
  assert.equal(w.stages.find((s) => s.state === 'current')?.key, 'checked')
})

test('workflowCompleteness: status is independent of holds and overdue items (issues live at the package)', () => {
  const d = fx.deliverable({ dueDate: '2026-01-01' }) // long overdue
  const rev = fx.revision({ deliverableId: d.id, state: 'approved' })
  const h = fx.hold()
  const link = { id: fx.id(), holdId: h.id, targetType: 'deliverable' as const, targetId: d.id }
  const overdueItem = fx.workItem({ anchorType: 'deliverable', anchorId: d.id, needBy: '2026-01-01', state: 'open' })
  const snap = fx.snapshot({ deliverables: [d], revisions: [rev], holds: [h], holdLinks: [link], workItems: [overdueItem] })
  const w = workflowCompleteness(snap, d)
  // workflow status reflects only gate progress — the hold and overdue item do not touch it
  assert.equal(w.gatesClosed, 2)
  assert.equal(w.label, 'approved — awaiting issue')
  // the issue-driven view still exists (for package/overview rollup) and is NOT green here
  assert.notEqual(deliverableStatus(snap, d).health.value, 'green')
})

test('DH-G: green when no hold, no overdue, no slip (§8.2)', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2026-08-01' })
  const rev = fx.revision({ deliverableId: d.id })
  const snap = fx.snapshot({ packages: [p], deliverables: [d], revisions: [rev] })
  const s = deliverableStatus(snap, d)
  assert.equal(s.health.value, 'green')
  assert.equal(s.health.ruleId, 'DH-G')
})

test('DH-A1: any active hold in the sphere → amber, with contributing hold (I-4)', () => {
  const d = fx.deliverable({ dueDate: '2026-08-01' })
  const rev = fx.revision({ deliverableId: d.id })
  const h = fx.hold({ raisedAt: '2026-07-14T00:00:00Z', cause: 'vendor_data' })
  const snap = fx.snapshot({
    deliverables: [d], revisions: [rev], holds: [h],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'revision', targetId: rev.id })],
  })
  const s = deliverableStatus(snap, d)
  assert.equal(s.health.value, 'amber')
  assert.equal(s.health.ruleId, 'DH-A1')
  assert.equal(s.health.contributing[0]?.recordType, 'hold')
})

test('DH-R2: hold older than escalation threshold → red (§8.2)', () => {
  const d = fx.deliverable({ dueDate: '2026-08-01' })
  const rev = fx.revision({ deliverableId: d.id })
  const h = fx.hold({ raisedAt: '2026-06-01T00:00:00Z' }) // > 14 wd before TODAY
  const snap = fx.snapshot({
    deliverables: [d], revisions: [rev], holds: [h],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'deliverable', targetId: d.id })],
  })
  const s = deliverableStatus(snap, d)
  assert.equal(s.health.value, 'red')
  assert.equal(s.health.ruleId, 'DH-R2')
})

test('DH-A3/DH-R1: forecast slip from need-by dates (P1 forecast, §6.1)', () => {
  const d = fx.deliverable({ dueDate: '2026-07-17' })
  const rev = fx.revision({ deliverableId: d.id })
  // open item needs until Tue 2026-07-21 → slip 2 wd → amber
  const w = fx.workItem({ anchorType: 'revision', anchorId: rev.id, needBy: '2026-07-21', state: 'in_work' })
  let snap = fx.snapshot({ deliverables: [d], revisions: [rev], workItems: [w] })
  let s = deliverableStatus(snap, d)
  assert.equal(s.forecastSlipWd, 2)
  assert.equal(s.health.value, 'amber')
  assert.equal(s.health.ruleId, 'DH-A3')

  // need-by far out → slip > 5 wd → red
  snap = fx.snapshot({ deliverables: [d], revisions: [rev], workItems: [{ ...w, needBy: '2026-07-31' }] })
  s = deliverableStatus(snap, d)
  assert.ok(s.forecastSlipWd > 5)
  assert.equal(s.health.ruleId, 'DH-R1')
})

test('DH-A2: overdue open condition → amber; DH-R3: breached hard condition on milestone deliverable → red', () => {
  const d = fx.deliverable({ dueDate: '2026-09-01' })
  const rev = fx.revision({ deliverableId: d.id })
  const cond = fx.condition({ parentType: 'revision', parentId: rev.id, needBy: '2026-07-10', severity: 'hard', type: 'resource' })
  let snap = fx.snapshot({ deliverables: [d], revisions: [rev], conditions: [cond] })
  assert.equal(deliverableStatus(snap, d).health.ruleId, 'DH-A2')

  const dm = { ...d, milestone: 'Gate 3' }
  snap = fx.snapshot({ deliverables: [dm], revisions: [rev], conditions: [cond] })
  const s = deliverableStatus(snap, dm)
  assert.equal(s.health.value, 'red')
  assert.equal(s.health.ruleId, 'DH-R3')
})

test('DH-A4: aging open check comments → amber (§8.2)', () => {
  const d = fx.deliverable({ dueDate: '2026-09-01' })
  const rev = fx.revision({ deliverableId: d.id })
  const chk = fx.check({ revisionId: rev.id, state: 'comments_open' })
  const cmt = fx.comment({ checkId: chk.id, createdAt: '2026-07-01T00:00:00Z' }) // ~10 wd old
  const snap = fx.snapshot({ deliverables: [d], revisions: [rev], checks: [chk], reviewComments: [cmt] })
  const s = deliverableStatus(snap, d)
  assert.equal(s.health.value, 'amber')
  assert.equal(s.health.ruleId, 'DH-A4')
})

test('PH-A1: >= 20% amber/red deliverables → amber package (§8.3)', () => {
  const p = fx.pkg()
  const ds = Array.from({ length: 5 }, () => fx.deliverable({ packageId: p.id, dueDate: '2026-09-01' }))
  const revs = ds.map((d) => fx.revision({ deliverableId: d.id }))
  const h = fx.hold()
  const snap = fx.snapshot({
    packages: [p], deliverables: ds, revisions: revs, holds: [h],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'deliverable', targetId: ds[0]!.id })],
  })
  const s = packageStatus(snap, p)
  assert.equal(s.health.value, 'amber')
  assert.equal(s.health.ruleId, 'PH-A1') // 1/5 = 20%
})

test('PH-R1: red deliverable with milestone → red package; PH-R2 late interface → red', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2026-07-01', milestone: 'G2' })
  const rev = fx.revision({ deliverableId: d.id })
  const w = fx.workItem({ anchorType: 'deliverable', anchorId: d.id, needBy: '2026-07-30' }) // big slip
  let snap = fx.snapshot({ packages: [p], deliverables: [d], revisions: [rev], workItems: [w] })
  assert.equal(packageStatus(snap, p).health.ruleId, 'PH-R1')

  const i = fx.interfaceItem({ receivingPackageId: p.id, needBy: '2026-06-15', state: 'open' })
  snap = fx.snapshot({ packages: [p], interfaces: [i] })
  assert.equal(packageStatus(snap, p).health.ruleId, 'PH-R2')
})

test('ADR-012: PH-A1 drill-down states the pressure and carries the underlying issue records', () => {
  const p = fx.pkg()
  const ds = Array.from({ length: 5 }, () => fx.deliverable({ packageId: p.id, dueDate: '2026-09-01' }))
  const revs = ds.map((d) => fx.revision({ deliverableId: d.id }))
  const h = fx.hold()
  const snap = fx.snapshot({
    packages: [p], deliverables: ds, revisions: revs, holds: [h],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'deliverable', targetId: ds[0]!.id })],
  })
  const s = packageStatus(snap, p)
  assert.equal(s.health.ruleId, 'PH-A1')
  const delRef = s.health.contributing.find((c) => c.recordType === 'deliverable' && c.id === ds[0]!.id)
  assert.ok(delRef, 'the pressured deliverable is listed')
  assert.ok(delRef!.why.includes('active hold'), `plain-language pressure, got "${delRef!.why}"`)
  const holdRef = s.health.contributing.find((c) => c.recordType === 'hold' && c.id === h.id)
  assert.ok(holdRef, 'the hold itself contributes — drill-down lands on a cockpit-visible record')
  assert.ok(holdRef!.why.includes(ds[0]!.docNo), 'carried-through ref names its deliverable')
})

test('ADR-012: PH-R1 drill-down carries the escalated hold behind the red milestone deliverable', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2026-09-01', milestone: 'G2' })
  const rev = fx.revision({ deliverableId: d.id })
  const h = fx.hold({ raisedAt: '2026-06-01T00:00:00Z' }) // > holdAgeRedWd before TODAY → DH-R2
  const snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], holds: [h],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'deliverable', targetId: d.id })],
  })
  const s = packageStatus(snap, p)
  assert.equal(s.health.ruleId, 'PH-R1')
  const delRef = s.health.contributing.find((c) => c.recordType === 'deliverable' && c.id === d.id)!
  assert.ok(delRef.why.includes('milestone G2'), 'milestone linkage stated')
  assert.ok(s.health.contributing.some((c) => c.recordType === 'hold' && c.id === h.id),
    'the escalated hold is a contributing record')
})

test('project health: escalate-tier signal breach is a red contribution (§8.4 table)', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2026-09-01' })
  const rev = fx.revision({ deliverableId: d.id })
  // green package, but an intake item untriaged for > 5 wd → S-INTAKE red → project red
  const old = fx.intake({ raisedAt: '2026-07-01T00:00:00Z' })
  const snap = fx.snapshot({ packages: [p], deliverables: [d], revisions: [rev], intakeItems: [old] })
  const s = projectStatus(snap)
  assert.equal(s.health.value, 'red')
  assert.equal(s.health.ruleId, 'PJ-ESC')
  const intakeSignal = s.signals.find((x) => x.id === 'S-INTAKE')!
  assert.equal(intakeSignal.level, 'red')
  assert.ok(s.health.contributing.some((c) => c.recordType === 'intake_item'), 'drill-down includes the intake item')
})

test('S-DEC: overdue decision blocking an issue transition is red regardless of days (§8.4)', () => {
  const dec = fx.decision({ state: 'pending', needBy: '2026-07-14' }) // 1 day over → warn normally
  const rev = fx.revision()
  const cond = fx.condition({
    parentType: 'revision', parentId: rev.id, gatedTransition: 'revision.issue',
    type: 'decision', requiredRefType: 'decision', requiredRefId: dec.id, severity: 'hard',
  })
  const snap = fx.snapshot({ decisions: [dec], revisions: [rev], conditions: [cond] })
  const sig = projectStatus(snap).signals.find((s) => s.id === 'S-DEC')!
  assert.equal(sig.level, 'red')
  assert.match(sig.contributing[0]!.why, /blocks an issue transition/)
})

test('KPIs carry explanations with contributing records (PEC-OV-001/002)', () => {
  const p = fx.pkg()
  const d = fx.deliverable({ packageId: p.id, dueDate: '2026-09-01' })
  const rev = fx.revision({ deliverableId: d.id })
  const h = fx.hold({ cause: 'decision', raisedAt: '2026-07-14T00:00:00Z' })
  const snap = fx.snapshot({
    packages: [p], deliverables: [d], revisions: [rev], holds: [h],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'deliverable', targetId: d.id })],
  })
  const s = projectStatus(snap)
  assert.equal(s.kpis.holdsByCause.value['decision'], 1)
  assert.equal(s.kpis.holdsByCause.contributing[0]?.ref, h.ref)
  assert.equal(s.kpis.pctOnPlan.value, 0)
  assert.ok(s.kpis.pctOnPlan.contributing.length > 0)
})

test('waitingOnYou: pending decisions for authority + ready approvals for signatory, with blocks (PEC-OV-004)', () => {
  const me = 42
  const dec = fx.decision({ state: 'pending', authorityId: me, needBy: '2026-07-01' })
  const apr = fx.approval({ state: 'ready', signatoryIds: [me], readyAt: '2026-07-14T00:00:00Z' })
  const rev = fx.revision()
  const cond = fx.condition({
    parentType: 'revision', parentId: rev.id, gatedTransition: 'revision.issue',
    type: 'decision', requiredRefType: 'decision', requiredRefId: dec.id,
  })
  const snap = fx.snapshot({ decisions: [dec], approvalRecords: [apr], revisions: [rev], conditions: [cond] })
  const w = waitingOnYou(snap, me)
  assert.equal(w.length, 2)
  const wd = w.find((x) => x.kind === 'decision')!
  assert.equal(wd.breach, 'red') // 14 days past need-by > 7
  assert.equal(wd.blocks[0]?.recordType, 'revision')
  assert.equal(waitingOnYou(snap, 99).length, 0)
})

test('myWeek: manual commit, need-by, overdue reasons; checks and comments owed; waiting on others (PEC-MW-*)', () => {
  const me = 7
  const d = fx.deliverable({ ownerId: me })
  const rev = fx.revision({ deliverableId: d.id })
  const committed = fx.workItem({ ownerId: me, committedWeek: '2026-W29', anchorType: 'deliverable', anchorId: d.id })
  const thisWeek = fx.workItem({ ownerId: me, needBy: '2026-07-17', anchorType: 'deliverable', anchorId: d.id })
  const overdue = fx.workItem({ ownerId: me, needBy: '2026-07-10', anchorType: 'deliverable', anchorId: d.id })
  const notMine = fx.workItem({ ownerId: 99, needBy: '2026-07-15' })
  const laterItem = fx.workItem({ ownerId: me, needBy: '2026-09-01' })
  const chk = fx.check({ checkerId: me, revisionId: rev.id, state: 'in_check' })
  const cmt = fx.comment({ responderId: me, checkId: chk.id })
  const h = fx.hold({ ownerId: 3 })
  const snap = fx.snapshot({
    deliverables: [d], revisions: [rev],
    workItems: [committed, thisWeek, overdue, notMine, laterItem],
    checks: [chk], reviewComments: [cmt], holds: [h],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'work_item', targetId: overdue.id })],
  })
  const mw = myWeek(snap, me)
  assert.equal(mw.week, '2026-W29')
  assert.equal(mw.committed.length, 3)
  assert.match(mw.committed.find((x) => x.workItem.id === committed.id)!.whyInWeek, /manual/)
  assert.match(mw.committed.find((x) => x.workItem.id === thisWeek.id)!.whyInWeek, /falls this week/)
  const od = mw.committed.find((x) => x.workItem.id === overdue.id)!
  assert.equal(od.overdue, true)
  assert.equal(od.blockedBy.length, 1, 'blocked overlay visible in My Week')
  assert.equal(mw.checksOwed.length, 1)
  assert.equal(mw.checksOwed[0]!.openComments, 1)
  assert.equal(mw.commentsOwed.length, 1)
  assert.ok(mw.waitingOnOthers.some((x) => x.kind === 'hold'), 'hold gating my work is chase-able')
})
