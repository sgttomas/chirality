import { test } from 'node:test'
import assert from 'node:assert/strict'
import { can, visibleLogs } from '../src/permissions.ts'
import type { PermissionContext } from '../src/permissions.ts'
import type { Role } from '../src/types.ts'

function ctx(roles: Role[], over: Partial<PermissionContext> = {}): PermissionContext {
  return { roles, isInstanceAdmin: false, ...over }
}

test('viewer is read-only everywhere (PRD §14)', () => {
  const v = ctx(['viewer'])
  assert.equal(can('project.read', v).allowed, true)
  for (const a of ['intake.raise', 'work_item.create', 'hold.raise', 'check.accept', 'decision.outcome'] as const) {
    assert.equal(can(a, v).allowed, false, a)
  }
})

test('anyone on the project may raise intake (PEC-AHL-003); config can restrict', () => {
  assert.equal(can('intake.raise', ctx(['contributor'])).allowed, true)
  assert.equal(can('intake.raise', ctx(['contributor'], { allowAnyoneRaiseIntake: false })).allowed, false)
  assert.equal(can('intake.raise', ctx(['coordinator'], { allowAnyoneRaiseIntake: false })).allowed, true)
})

test('only the assigned checker accepts checks and comment closures (I-6, PEC-CHK-002)', () => {
  assert.equal(can('check.accept', ctx(['pm'])).allowed, false, 'not even the pm')
  assert.equal(can('check.accept', ctx(['checker'], { isChecker: true })).allowed, true)
  assert.equal(can('comment.accept', ctx(['engineer_of_record'], { isChecker: false })).allowed, false)
  assert.equal(can('comment.accept', ctx(['contributor'], { isChecker: true })).allowed, true)
})

test('approval outcomes: named signatories only; document controllers never (PRD §14, D-12)', () => {
  assert.equal(can('approval.outcome', ctx(['approver'], { isSignatory: false })).allowed, false)
  assert.equal(can('approval.outcome', ctx(['approver'], { isSignatory: true })).allowed, true)
  assert.equal(can('approval.outcome', ctx(['document_controller'], { isSignatory: true })).allowed, false)
  assert.equal(can('decision.outcome', ctx(['document_controller'], { isAuthority: true })).allowed, false)
})

test('decision outcome requires the authority; preparing does not (PRD §14)', () => {
  assert.equal(can('decision.outcome', ctx(['pm'], { isAuthority: false })).allowed, false)
  assert.equal(can('decision.outcome', ctx(['contributor'], { isAuthority: true })).allowed, true)
  assert.equal(can('decision.progress', ctx(['contributor'], { isPreparer: true })).allowed, true)
})

test('waivers: strict types need pm/EM; config can override per type (I-8, SPEC §2.2)', () => {
  assert.equal(can('condition.waive', ctx(['package_lead'], { conditionType: 'check' })).allowed, false)
  assert.equal(can('condition.waive', ctx(['pm'], { conditionType: 'check' })).allowed, true)
  assert.equal(can('condition.waive', ctx(['package_lead'], { conditionType: 'resource' })).allowed, true)
  assert.equal(
    can('condition.waive', ctx(['coordinator'], {
      conditionType: 'check', waiverRoles: { check: ['coordinator'] },
    })).allowed,
    true, 'project config overrides the default waiver roles',
  )
})

test('issue events are document control or pm; DC cannot transition work (PRD §14)', () => {
  assert.equal(can('issue.record', ctx(['document_controller'])).allowed, true)
  assert.equal(can('issue.record', ctx(['engineer_of_record'])).allowed, false)
  assert.equal(can('deliverable.update', ctx(['document_controller'])).allowed, true, 'DC owns revision metadata')
})

test('system-driven transitions are never user-invokable', () => {
  assert.equal(can('revision.auto', ctx(['admin'])).allowed, false)
  assert.equal(can('approval.auto', ctx(['pm'])).allowed, false)
})

test('log visibility: viewer sees package+client by default; config overrides (PEC-NFR-005)', () => {
  assert.deepEqual(visibleLogs(['viewer'], undefined), ['package', 'client'])
  assert.deepEqual(visibleLogs(['contributor'], undefined), ['package', 'internal', 'client'])
  assert.deepEqual(visibleLogs(['viewer'], { viewer: ['client'] }), ['client'])
  assert.deepEqual(visibleLogs([], undefined), [])
})
