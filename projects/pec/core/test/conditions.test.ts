import { test } from 'node:test'
import assert from 'node:assert/strict'
import { evaluateCondition, evaluateGate, explainTransition } from '../src/conditions.ts'
import * as fx from './fixtures.ts'

test('check-type condition: satisfied by accepted check on parent revision (§5.3)', () => {
  const rev = fx.revision()
  const cond = fx.condition({ parentType: 'revision', parentId: rev.id, type: 'check' })
  const chk = fx.check({ revisionId: rev.id, state: 'in_check' })
  let snap = fx.snapshot({ revisions: [rev], conditions: [cond], checks: [chk] })
  assert.equal(evaluateCondition(snap, cond).effectiveState, 'open')

  snap = fx.snapshot({ revisions: [rev], conditions: [cond], checks: [{ ...chk, state: 'accepted' }] })
  const ev = evaluateCondition(snap, cond)
  assert.equal(ev.effectiveState, 'satisfied')
  assert.equal(ev.satisfier?.recordType, 'check')
})

test('reopened check flips a stored-satisfied condition back to open (defense in depth, §5.3)', () => {
  const rev = fx.revision()
  const chk = fx.check({ revisionId: rev.id, state: 'reopened' })
  const cond = fx.condition({
    parentType: 'revision', parentId: rev.id, type: 'check',
    state: 'satisfied', satisfiedByType: 'check', satisfiedById: chk.id,
  })
  const snap = fx.snapshot({ revisions: [rev], conditions: [cond], checks: [chk] })
  const ev = evaluateCondition(snap, cond)
  assert.equal(ev.effectiveState, 'open')
  assert.match(ev.note ?? '', /no longer valid/)
})

test('decision-type condition requires the pinned decision to be decided', () => {
  const dec = fx.decision({ state: 'pending' })
  const cond = fx.condition({ type: 'decision', requiredRefType: 'decision', requiredRefId: dec.id })
  let snap = fx.snapshot({ decisions: [dec], conditions: [cond] })
  assert.equal(evaluateCondition(snap, cond).effectiveState, 'open')
  snap = fx.snapshot({ decisions: [{ ...dec, state: 'decided', outcome: 'approve' }], conditions: [cond] })
  assert.equal(evaluateCondition(snap, cond).effectiveState, 'satisfied')
})

test('approval-type condition: only approve/conditionally_accept outcomes satisfy (§5.3)', () => {
  const outcome = fx.decision({ state: 'decided', outcome: 'reject', kind: 'approval_outcome' })
  const apr = fx.approval({ state: 'decided', outcomeDecisionId: outcome.id })
  const cond = fx.condition({ type: 'approval', requiredRefType: 'approval_record', requiredRefId: apr.id })
  let snap = fx.snapshot({ approvalRecords: [apr], decisions: [outcome], conditions: [cond] })
  assert.equal(evaluateCondition(snap, cond).effectiveState, 'open', 'rejected approval does not satisfy')

  snap = fx.snapshot({
    approvalRecords: [apr],
    decisions: [{ ...outcome, outcome: 'conditionally_accept' }],
    conditions: [cond],
  })
  assert.equal(evaluateCondition(snap, cond).effectiveState, 'satisfied')
})

test('evidence-type condition satisfied by named artifact on the parent (§5.3)', () => {
  const rev = fx.revision()
  const cond = fx.condition({
    parentType: 'revision', parentId: rev.id, type: 'evidence', requiredArtifactName: 'native-files',
  })
  let snap = fx.snapshot({ revisions: [rev], conditions: [cond] })
  assert.equal(evaluateCondition(snap, cond).effectiveState, 'open')
  snap = fx.snapshot({
    revisions: [rev], conditions: [cond],
    evidence: [fx.evidence({ recordType: 'revision', recordId: rev.id, label: 'native-files' })],
  })
  assert.equal(evaluateCondition(snap, cond).effectiveState, 'satisfied')
})

test('document_control condition satisfied by pending issue event payload at evaluation (§5.3)', () => {
  const rev = fx.revision({ state: 'approved' })
  const cond = fx.condition({ parentType: 'revision', parentId: rev.id, type: 'document_control' })
  const snap = fx.snapshot({ revisions: [rev], conditions: [cond] })
  assert.equal(evaluateCondition(snap, cond).effectiveState, 'open')
  assert.equal(
    evaluateCondition(snap, cond, { pendingIssueEvent: { transmittalRef: 'TR-001', recipients: ['client'] } }).effectiveState,
    'satisfied',
  )
  assert.equal(
    evaluateCondition(snap, cond, { pendingIssueEvent: { transmittalRef: 'TR-001', recipients: [] } }).effectiveState,
    'open', 'recipients required',
  )
})

test('waived stands as stored with waiver decision ref (I-8); superseded passes gate (I-10)', () => {
  const waiver = fx.decision({ state: 'decided', outcome: 'waive', kind: 'waiver' })
  const cond = fx.condition({ state: 'waived', waiverDecisionId: waiver.id })
  const sup = fx.condition({ state: 'superseded' })
  const snap = fx.snapshot({ decisions: [waiver], conditions: [cond, sup] })
  const ev = evaluateCondition(snap, cond)
  assert.equal(ev.effectiveState, 'waived')
  assert.equal(ev.waiverDecisionRef, waiver.ref)
  const gate = evaluateGate(snap, cond.parentType, cond.parentId, cond.gatedTransition)
  assert.equal(gate.permitted, true, 'waived + superseded conditions pass the gate')
})

test('hard blocks, warn does not (D-11)', () => {
  const rev = fx.revision()
  const hard = fx.condition({ parentType: 'revision', parentId: rev.id, severity: 'hard', type: 'resource' })
  const warn = fx.condition({ parentType: 'revision', parentId: rev.id, severity: 'warn', type: 'resource' })
  const snap = fx.snapshot({ revisions: [rev], conditions: [hard, warn] })
  const gate = evaluateGate(snap, 'revision', rev.id, 'revision.issue')
  assert.equal(gate.permitted, false)
  assert.equal(gate.hardOpen.length, 1)
  assert.equal(gate.warnOpen.length, 1)

  const warnOnly = fx.snapshot({ revisions: [rev], conditions: [warn] })
  assert.equal(evaluateGate(warnOnly, 'revision', rev.id, 'revision.issue').permitted, true,
    'warn conditions never block')
})

test('active hold on the record vetoes a holdVeto transition (OM-2)', () => {
  const rev = fx.revision({ state: 'approved' })
  const h = fx.hold()
  const snap = fx.snapshot({
    revisions: [rev], holds: [h],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'revision', targetId: rev.id })],
  })
  const gate = evaluateGate(snap, 'revision', rev.id, 'revision.issue', { holdVeto: true })
  assert.equal(gate.permitted, false)
  assert.equal(gate.holdVeto[0]?.id, h.id)

  // resolved hold no longer vetoes
  const snap2 = fx.snapshot({
    revisions: [rev], holds: [{ ...h, state: 'resolved' }],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'revision', targetId: rev.id })],
  })
  assert.equal(evaluateGate(snap2, 'revision', rev.id, 'revision.issue', { holdVeto: true }).permitted, true)
})

test('condition itself under hold shows blocked_by_hold and still blocks (§5.5)', () => {
  const rev = fx.revision()
  const cond = fx.condition({ parentType: 'revision', parentId: rev.id, type: 'resource' })
  const h = fx.hold({ cause: 'vendor_data' })
  const snap = fx.snapshot({
    revisions: [rev], conditions: [cond], holds: [h],
    holdLinks: [fx.holdLink({ holdId: h.id, targetType: 'condition', targetId: cond.id })],
  })
  const ev = evaluateCondition(snap, cond)
  assert.equal(ev.effectiveState, 'blocked_by_hold')
  assert.equal(evaluateGate(snap, 'revision', rev.id, 'revision.issue').permitted, false)
})

test('explainTransition renders the before-this-issues panel payload (PEC-DEL-004)', () => {
  const rev = fx.revision()
  const chk = fx.check({ revisionId: rev.id, state: 'accepted' })
  const satisfied = fx.condition({ parentType: 'revision', parentId: rev.id, type: 'check' })
  const open = fx.condition({
    parentType: 'revision', parentId: rev.id, type: 'evidence',
    requiredArtifactName: 'comment-sheet', ownerId: 7, needBy: '2026-07-20',
  })
  const snap = fx.snapshot({ revisions: [rev], checks: [chk], conditions: [satisfied, open] })
  const ex = explainTransition(snap, 'revision', rev.id, 'revision.issue')
  assert.equal(ex.permitted, false)
  assert.equal(ex.conditions.length, 2)
  const sat = ex.conditions.find((c) => c.type === 'check')!
  assert.equal(sat.state, 'satisfied')
  assert.equal(sat.satisfiedBy?.recordType, 'check')
  const op = ex.conditions.find((c) => c.type === 'evidence')!
  assert.equal(op.state, 'open')
  assert.equal(op.ownerId, 7)
  assert.equal(op.needBy, '2026-07-20')
})
