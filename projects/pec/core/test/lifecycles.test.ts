import { test } from 'node:test'
import assert from 'node:assert/strict'
import {
  LIFECYCLE_RECORDS, TRANSITIONS, findTransition, statesOf, transitionsFrom,
} from '../src/lifecycles.ts'
import {
  APPROVAL_STATES, CHECK_STATES, DECISION_STATES, HOLD_STATES, INTAKE_STATES,
  REVISION_STATES, WORK_ITEM_STATES,
} from '../src/types.ts'

test('every lifecycle state named in types is reachable in the transition tables', () => {
  const expected: Record<string, readonly string[]> = {
    intake_item: INTAKE_STATES,
    work_item: WORK_ITEM_STATES,
    hold: HOLD_STATES,
    check: CHECK_STATES,
    approval_record: APPROVAL_STATES,
    decision: DECISION_STATES,
    revision: REVISION_STATES,
  }
  for (const rec of LIFECYCLE_RECORDS) {
    const inTables = new Set(statesOf(rec))
    for (const s of expected[rec]!) {
      // 'reopened' (check) and terminal states appear; every declared state must exist in the machine
      assert.ok(inTables.has(s), `${rec}: state '${s}' missing from transition tables`)
    }
  }
})

test('PRD §7.2 work item: closed only via close (condition-gated), reopen path exists', () => {
  const close = findTransition('work_item', 'close', 'in_work')
  assert.ok(close)
  assert.equal(close.gate, 'work_item.close', 'close must be condition-gated (I-5)')
  assert.equal(close.holdVeto, true, 'active hold vetoes closure (OM-2)')
  assert.ok(findTransition('work_item', 'reopen', 'closed'), 'closed → reopened (supersession/checker rejection)')
  // No path from cancelled
  assert.equal(transitionsFrom('work_item', 'cancelled').length, 0, 'cancelled is terminal')
})

test('PRD §7.3 hold: active → resolved/withdrawn, both terminal', () => {
  assert.ok(findTransition('hold', 'resolve', 'active'))
  assert.ok(findTransition('hold', 'withdraw', 'active'))
  assert.equal(transitionsFrom('hold', 'resolved').length, 0)
  assert.equal(transitionsFrom('hold', 'withdrawn').length, 0)
})

test('PRD §7.4 check: acceptance requires no open comments; not reachable from comments_open', () => {
  const accept1 = findTransition('check', 'accept', 'in_check')
  const accept2 = findTransition('check', 'accept', 'comments_closed')
  assert.ok(accept1 && accept2)
  assert.ok(accept1.requires.includes('no_open_comment'))
  assert.equal(findTransition('check', 'accept', 'comments_open'), undefined,
    'cannot accept with comments open')
  assert.equal(findTransition('check', 'accept', 'open'), undefined)
})

test('PRD §7.5 approval record: decided only via record_outcome from ready (PEC-AUTH-004)', () => {
  const toDecided = TRANSITIONS.filter((t) => t.record === 'approval_record' && t.to === 'decided')
  assert.equal(toDecided.length, 1)
  assert.equal(toDecided[0]!.event, 'record_outcome')
  assert.deepEqual(toDecided[0]!.from, ['ready'])
  assert.ok(toDecided[0]!.sideEffects.includes('create_outcome_decision'), 'outcome is a Decision (OM-6)')
  assert.ok(toDecided[0]!.sideEffects.includes('audit_event'), 'approval outcomes write audit events (PEC-NFR-001)')
})

test('PRD §7.6 decision: identified → in_progress → pending → decided → superseded', () => {
  assert.ok(findTransition('decision', 'assign_preparer', 'identified'))
  assert.ok(findTransition('decision', 'mark_pending', 'in_progress'))
  assert.ok(findTransition('decision', 'record_outcome', 'pending'))
  assert.ok(findTransition('decision', 'supersede', 'decided'))
  assert.equal(findTransition('decision', 'record_outcome', 'identified'), undefined,
    'no shortcut from identified to decided')
})

test('PRD §7.7 revision: issue is hard-gated and only from approved (D-11, I-5)', () => {
  const issue = TRANSITIONS.filter((t) => t.record === 'revision' && t.event === 'issue')
  assert.equal(issue.length, 1)
  assert.deepEqual(issue[0]!.from, ['approved'])
  assert.equal(issue[0]!.gate, 'revision.issue')
  assert.equal(issue[0]!.holdVeto, true)
  assert.ok(issue[0]!.sideEffects.includes('create_issue_event'))
  // rework loops are expected without ceremony
  assert.ok(findTransition('revision', 'rework', 'in_check'))
  // no direct in_work → issued
  assert.equal(findTransition('revision', 'issue', 'in_work'), undefined)
})

test('there is no generic "done" event on any record (I-5)', () => {
  for (const t of TRANSITIONS) {
    assert.notEqual(t.event, 'done')
    assert.notEqual(t.event, 'complete')
  }
})

test('intake disposition preserves flow: raised → in_triage → dispositioned, terminal', () => {
  assert.ok(findTransition('intake_item', 'open_triage', 'raised'))
  assert.ok(findTransition('intake_item', 'disposition', 'in_triage'))
  assert.equal(transitionsFrom('intake_item', 'dispositioned').length, 0)
})
