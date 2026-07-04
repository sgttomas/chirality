/**
 * PEC-AHL-002 — "a log move is never silent."
 *
 * updateWorkItem() in server/src/services/work.ts writes a dedicated history entry
 * (kind: 'log_change') whenever a work item's log field actually changes, with a
 * summary recording the from→to logs. A PUT that leaves the log untouched must NOT
 * add such an entry.
 *
 * Route under test: PUT /api/projects/:pid/work-items/:id
 * History read via:  GET /api/projects/:pid/history/work_item/:id
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'

const P = (pid: number) => `/api/projects/${pid}`

/** Create a work item anchored to the seeded deliverable with an explicit log. */
async function makeWorkItem(env: Awaited<ReturnType<typeof createTestEnv>>, log: string) {
  const eor = await env.as('eor@t.co')
  const created = await eor.post(`${P(env.projectId)}/work-items`, {
    title: 'AHL-002 log-move coverage',
    anchorType: 'deliverable',
    anchorId: env.deliverableId,
    ownerId: env.people['eor@t.co'],
    needBy: null,
    log,
  })
  assert.equal(created.status, 200, `create failed: ${JSON.stringify(created.body)}`)
  return { eor, wi: created.body }
}

test('AHL-002: changing the log writes a log_change history entry naming from→to', async () => {
  const env = await createTestEnv()
  try {
    const { eor, wi } = await makeWorkItem(env, 'internal')
    assert.equal(wi.log, 'internal', 'seeded with internal log')

    // move internal -> package, sending the current version
    const put = await eor.put(`${P(env.projectId)}/work-items/${wi.id}`, {
      version: wi.version,
      log: 'package',
    })
    assert.equal(put.status, 200, `put failed: ${JSON.stringify(put.body)}`)
    assert.equal(put.body.log, 'package', 'log now package')

    const hist = await eor.get(`${P(env.projectId)}/history/work_item/${wi.id}`)
    assert.equal(hist.status, 200)
    assert.ok(Array.isArray(hist.body), 'history is an array')

    const logChanges = hist.body.filter((h: { kind: string }) => h.kind === 'log_change')
    assert.equal(logChanges.length, 1, 'exactly one log_change entry recorded')

    const entry = logChanges[0]
    assert.equal(entry.kind, 'log_change')
    // summary mentions both the from log and the to log (the move is never silent)
    assert.match(entry.summary, /internal/, 'summary names the from log')
    assert.match(entry.summary, /package/, 'summary names the to log')
    // from precedes to in the summary
    assert.ok(
      entry.summary.indexOf('internal') < entry.summary.indexOf('package'),
      `summary should read from→to (internal before package): ${entry.summary}`,
    )
    // it names the work item ref
    assert.match(entry.summary, new RegExp(wi.ref), 'summary names the work item ref')
  } finally {
    await env.close()
  }
})

test('AHL-002: a PUT that does not change the log adds no log_change entry', async () => {
  const env = await createTestEnv()
  try {
    const { eor, wi } = await makeWorkItem(env, 'internal')

    // edit a non-log field only; log stays internal
    const put = await eor.put(`${P(env.projectId)}/work-items/${wi.id}`, {
      version: wi.version,
      title: 'renamed but same log',
    })
    assert.equal(put.status, 200, `put failed: ${JSON.stringify(put.body)}`)
    assert.equal(put.body.log, 'internal', 'log unchanged')

    const hist = await eor.get(`${P(env.projectId)}/history/work_item/${wi.id}`)
    assert.equal(hist.status, 200)
    const logChanges = hist.body.filter((h: { kind: string }) => h.kind === 'log_change')
    assert.equal(logChanges.length, 0, 'no log_change entry for a non-log edit')

    // but the edit itself was still recorded (field_change), so history is not empty
    const fieldChanges = hist.body.filter((h: { kind: string }) => h.kind === 'field_change')
    assert.ok(fieldChanges.length >= 1, 'the title edit is recorded as a field_change')
  } finally {
    await env.close()
  }
})

test('AHL-002: PUT sending the same log value as current adds no log_change entry', async () => {
  const env = await createTestEnv()
  try {
    const { eor, wi } = await makeWorkItem(env, 'package')

    // explicitly send the same log value it already has — must be treated as no-op for log history
    const put = await eor.put(`${P(env.projectId)}/work-items/${wi.id}`, {
      version: wi.version,
      log: 'package',
      title: 'touch title too',
    })
    assert.equal(put.status, 200, `put failed: ${JSON.stringify(put.body)}`)
    assert.equal(put.body.log, 'package')

    const hist = await eor.get(`${P(env.projectId)}/history/work_item/${wi.id}`)
    assert.equal(hist.status, 200)
    const logChanges = hist.body.filter((h: { kind: string }) => h.kind === 'log_change')
    assert.equal(logChanges.length, 0, 'sending an unchanged log value is silent for log history')
  } finally {
    await env.close()
  }
})
