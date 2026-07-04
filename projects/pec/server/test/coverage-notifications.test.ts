/**
 * PEC-NOT-001: notification producers + sweep idempotency.
 *
 * Covers:
 *  (1) Producers fire and reach the intended recipient (read via GET /notifications):
 *      - creating/assigning a work item to eor@t.co emits event 'assigned' on that work_item;
 *      - raising a hold on the seeded deliverable (owned by eor@t.co) emits
 *        'hold_blocks_your_record' to the deliverable owner.
 *  (2) Sweep idempotency: an overdue open work item makes sweepProject emit 'item_overdue'
 *      to the owner once per (person, event, record, local-day). Logging the owner in a
 *      second time (which re-runs sweepProject) does NOT duplicate that notification.
 *
 * Source of truth read before writing:
 *   server/src/services/work.ts   (createWorkItem -> notify 'assigned')
 *   server/src/services/holds.ts  (raiseHold -> notify 'hold_blocks_your_record')
 *   server/src/services/sweep.ts  (sweepProject; alreadyToday dedup on person+event+record+local-day)
 *   server/src/api.ts             (login runs sweepProject per project; GET .../notifications)
 *   server/src/repo.ts            (notify insert; notificationsFor; today = localDate(now, tz))
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'

const N = (env: { projectId: number }) => `/api/projects/${env.projectId}/notifications`
const WORK = (env: { projectId: number }) => `/api/projects/${env.projectId}/work-items`
const HOLDS = (env: { projectId: number }) => `/api/projects/${env.projectId}/holds`

test('producer: assigning a work item to eor emits an "assigned" notification to that owner', async () => {
  const env = await createTestEnv()
  try {
    const lead = await env.as('lead@t.co')
    const eor = await env.as('eor@t.co')

    // Anchor to the seeded deliverable; owner is eor@t.co (the recipient we assert on).
    const created = await lead.post(WORK(env), {
      title: 'Draft the PFD callouts',
      anchorType: 'deliverable',
      anchorId: env.deliverableId,
      ownerId: env.people['eor@t.co'],
      needBy: '2027-01-31',
    })
    assert.equal(created.status, 200, JSON.stringify(created.body))
    const wid = created.body.id as number
    assert.ok(wid > 0)

    const notes = await eor.get(N(env))
    assert.equal(notes.status, 200)
    const assigned = (notes.body as any[]).filter(
      (n) => n.event === 'assigned' && n.recordType === 'work_item' && n.recordId === wid,
    )
    assert.equal(assigned.length, 1, 'owner should receive exactly one "assigned" notification for the new item')
    assert.equal(assigned[0].personId, env.people['eor@t.co'], 'notification is addressed to the owner')
    assert.equal(assigned[0].recordRef, created.body.ref, 'notification carries the work item ref')

    // A non-recipient (the lead) does not get this owner-targeted notification.
    const leadNotes = await lead.get(N(env))
    assert.equal(leadNotes.status, 200)
    assert.ok(
      !(leadNotes.body as any[]).some((n) => n.event === 'assigned' && n.recordId === wid),
      'the assigner is not the recipient of the assigned notification',
    )
  } finally {
    await env.close()
  }
})

test('producer: raising a hold on eor\'s deliverable notifies the deliverable owner (hold_blocks_your_record)', async () => {
  const env = await createTestEnv()
  try {
    const lead = await env.as('lead@t.co') // raiser != target owner, so owner gets notified
    const eor = await env.as('eor@t.co')

    const hold = await lead.post(HOLDS(env), {
      title: 'Vendor data missing',
      cause: 'vendor_data',
      ownerId: env.people['lead@t.co'],
      needBy: '2026-08-01',
      targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
    })
    assert.equal(hold.status, 200, JSON.stringify(hold.body))
    assert.ok(hold.body.id > 0)

    const notes = await eor.get(N(env))
    assert.equal(notes.status, 200)
    const blocking = (notes.body as any[]).filter(
      (n) => n.event === 'hold_blocks_your_record'
        && n.recordType === 'deliverable' && n.recordId === env.deliverableId,
    )
    assert.equal(blocking.length, 1, 'the deliverable owner is notified their record is blocked')
    assert.equal(blocking[0].personId, env.people['eor@t.co'])
    assert.match(String(blocking[0].reason), /blocks your record/)
  } finally {
    await env.close()
  }
})

test('sweep idempotency: an overdue work item notifies the owner once, not again on a second login/sweep', async () => {
  const env = await createTestEnv()
  try {
    const lead = await env.as('lead@t.co')

    // Create an OPEN item whose need-by is in the past (today's real local date is well after
    // 2020), so sweepProject's daysOverdue(...) > 0 branch fires 'item_overdue' for the owner.
    const created = await lead.post(WORK(env), {
      title: 'Overdue deliverable action',
      anchorType: 'deliverable',
      anchorId: env.deliverableId,
      ownerId: env.people['eor@t.co'],
      needBy: '2020-01-01',
    })
    assert.equal(created.status, 200, JSON.stringify(created.body))
    const wid = created.body.id as number

    const overdueCount = async () => {
      const eor = await env.as('eor@t.co') // env.as caches, so re-run the login route directly to sweep again
      const res = await eor.get(N(env))
      assert.equal(res.status, 200)
      return (res.body as any[]).filter(
        (n) => n.event === 'item_overdue' && n.recordType === 'work_item' && n.recordId === wid,
      )
    }

    // First login for eor drives the initial sweep.
    const first = await overdueCount()
    assert.equal(first.length, 1, 'sweep emits exactly one item_overdue for the owner on first run')
    assert.equal(first[0].personId, env.people['eor@t.co'])

    // Re-run the login route (a fresh sweep for the same local day) via a direct login call —
    // env.as() caches the client so it would not re-hit /auth/login.
    const relogin = await fetch(`${env.base}/api/auth/login`, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ email: 'eor@t.co', password: 'pilot' }),
    })
    assert.equal(relogin.status, 200, 'second login (re-sweep) succeeds')

    // The (person, event, record, local-day) dedup key must suppress a duplicate.
    const second = await overdueCount()
    assert.equal(second.length, 1, 'a second same-day sweep must NOT duplicate the item_overdue notification')
    assert.equal(second[0].id, first[0].id, 'same notification row, not a new one')
  } finally {
    await env.close()
  }
})
