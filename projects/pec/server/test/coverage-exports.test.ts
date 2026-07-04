/**
 * §15 register exports — GET /export/:register.
 * Covers approvals, interfaces, intake, commitments, and the NEW unified log export.
 * The route (api.ts) strips a trailing .csv and calls exportRegister() (import/index.ts),
 * which returns text/csv mirroring the register schemas. The `log` case applies
 * log-visibility filtering (PEC-NFR-005): a viewer must not see internal-log rows.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { withTx } from '../src/db.ts'
import { nowIso } from '../src/repo.ts'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'

const P = (env: TestEnv) => `/api/projects/${env.projectId}`

/** Parse a CSV response: first line is the header row, remaining lines the body. */
function splitCsv(text: string): { header: string; body: string } {
  const idx = text.indexOf('\r\n')
  return idx < 0
    ? { header: text.trim(), body: '' }
    : { header: text.slice(0, idx), body: text.slice(idx + 2) }
}

async function fetchExport(env: TestEnv, email: string, register: string) {
  const client = await env.as(email)
  return client.get(`${P(env)}/export/${register}`)
}

test('approvals export: 200 text/csv, documented header, seeded ref appears', async () => {
  const env = await createTestEnv()
  try {
    withTx(env.db, () => {
      env.repo.insert('approval_record', {
        projectId: env.projectId, ref: 'APR-9001', title: 'HAZOP sign-off',
        approvalType: 'technical', authoritySource: 'company',
        appliesToType: 'revision', appliesToId: env.revisionId,
        signatoryIds: [env.people['approver@t.co']], dueDate: '2027-01-15',
        state: 'required', createdAt: nowIso(),
      })
    })

    const res = await fetchExport(env, 'admin@t.co', 'approvals.csv')
    assert.equal(res.status, 200)
    // content-type asserted via the fact JSON.parse failed (body stays a raw string)
    assert.equal(typeof res.body, 'string')
    const { header, body } = splitCsv(res.body as string)
    for (const col of ['approval_id', 'title', 'type', 'authority_source', 'applies_to',
      'signatories', 'due_date', 'state', 'outcome', 'outcome_decision']) {
      assert.ok(header.split(',').includes(col), `missing column ${col} in "${header}"`)
    }
    assert.match(body, /APR-9001/)
    // applies_to is rendered as "<type>#<id>"
    assert.match(body, new RegExp(`revision#${env.revisionId}`))
  } finally {
    await env.close()
  }
})

test('interfaces export: 200, documented header, seeded interface ref appears', async () => {
  const env = await createTestEnv()
  try {
    withTx(env.db, () => {
      env.repo.insert('interface_item', {
        projectId: env.projectId, ref: 'INT-9002', title: 'Battery limits at unit boundary',
        givingParty: 'Process', receivingParty: 'Piping', givingPackageId: env.packageId,
        requiredInfo: 'tie-in coordinates', needBy: '2027-02-01', state: 'open', log: 'package',
      })
    })

    const res = await fetchExport(env, 'admin@t.co', 'interfaces.csv')
    assert.equal(res.status, 200)
    const { header, body } = splitCsv(res.body as string)
    for (const col of ['interface_id', 'title', 'giving_party', 'receiving_party',
      'giving_package', 'receiving_package', 'required_info', 'need_by', 'state', 'log']) {
      assert.ok(header.split(',').includes(col), `missing column ${col} in "${header}"`)
    }
    assert.match(body, /INT-9002/)
  } finally {
    await env.close()
  }
})

test('intake export: 200, documented header, item raised via POST /intake appears', async () => {
  const env = await createTestEnv()
  try {
    const coord = await env.as('coord@t.co')
    const raised = await coord.post(`${P(env)}/intake`, {
      statement: 'Verify vendor nozzle loads on E-101',
      quickType: 'action', log: 'package',
    })
    assert.equal(raised.status, 200)
    const ref: string = raised.body.ref
    assert.ok(ref, 'raise returned no ref')

    const res = await fetchExport(env, 'admin@t.co', 'intake.csv')
    assert.equal(res.status, 200)
    const { header, body } = splitCsv(res.body as string)
    for (const col of ['intake_id', 'statement', 'quick_type', 'log', 'raised_by',
      'raised_date', 'state', 'disposition', 'anchor_suggestion', 'need_by']) {
      assert.ok(header.split(',').includes(col), `missing column ${col} in "${header}"`)
    }
    assert.ok(body.includes(ref), `intake ref ${ref} not in body`)
    assert.match(body, /Verify vendor nozzle loads/)
  } finally {
    await env.close()
  }
})

test('commitments export: a work item due this week appears with why_in_week=need-by', async () => {
  const env = await createTestEnv()
  try {
    const today = env.repo.snapshot(env.projectId).today // localized real "today"
    withTx(env.db, () => {
      env.repo.insert('work_item', {
        projectId: env.projectId, ref: 'WI-9003', title: 'Close out RFI-42',
        kind: 'action', log: 'package', anchorType: 'deliverable', anchorId: env.deliverableId,
        packageId: env.packageId, ownerId: env.people['eor@t.co'], needBy: today,
        state: 'in_work', createdBy: env.people['eor@t.co'], createdAt: nowIso(),
      })
    })

    const res = await fetchExport(env, 'admin@t.co', 'commitments.csv')
    assert.equal(res.status, 200)
    const { header, body } = splitCsv(res.body as string)
    for (const col of ['week', 'owner', 'item_id', 'title', 'deliverable_ref',
      'need_by', 'state', 'why_in_week']) {
      assert.ok(header.split(',').includes(col), `missing column ${col} in "${header}"`)
    }
    assert.match(body, /WI-9003/)
    // its need-by lands in-week, so the reason column reads "need-by"
    assert.match(body, /need-by/)
    // deliverable_ref back-reference resolves to the seeded doc_no
    assert.match(body, /TST-PR-001/)
  } finally {
    await env.close()
  }
})

test('log export: header + a hold appears; visibility filtering (PEC-NFR-005)', async () => {
  const env = await createTestEnv()
  try {
    const eorId = env.people['eor@t.co']
    withTx(env.db, () => {
      // an active hold on the internal log (should show for admin, hidden from viewer)
      env.repo.insert('hold', {
        projectId: env.projectId, ref: 'HLD-9100', title: 'Awaiting soil report',
        cause: 'missing_input', statement: 'Geotech data outstanding',
        ownerId: eorId, needBy: '2027-03-01', raisedBy: eorId, raisedAt: nowIso(),
        state: 'active', log: 'internal',
      })
      // one internal-log work item and one package-log work item (both open → on the log)
      env.repo.insert('work_item', {
        projectId: env.projectId, ref: 'WI-INTERNAL', title: 'Internal-only follow-up',
        kind: 'action', log: 'internal', anchorType: 'deliverable', anchorId: env.deliverableId,
        packageId: env.packageId, ownerId: eorId, state: 'open',
        createdBy: eorId, createdAt: nowIso(),
      })
      env.repo.insert('work_item', {
        projectId: env.projectId, ref: 'WI-PACKAGE', title: 'Package-visible follow-up',
        kind: 'action', log: 'package', anchorType: 'deliverable', anchorId: env.deliverableId,
        packageId: env.packageId, ownerId: eorId, state: 'open',
        createdBy: eorId, createdAt: nowIso(),
      })
    })

    // admin sees all three logs → both work items and the internal hold present
    const adminRes = await fetchExport(env, 'admin@t.co', 'log.csv')
    assert.equal(adminRes.status, 200)
    const admin = splitCsv(adminRes.body as string)
    for (const col of ['item_id', 'type', 'title', 'log', 'package', 'owner', 'state',
      'age_wd', 'need_by', 'overdue', 'hold_cause', 'anchor_status']) {
      assert.ok(admin.header.split(',').includes(col), `missing column ${col} in "${admin.header}"`)
    }
    assert.ok(admin.body.includes('HLD-9100'), 'admin log missing the hold')
    assert.ok(admin.body.includes('WI-INTERNAL'), 'admin log missing the internal work item')
    assert.ok(admin.body.includes('WI-PACKAGE'), 'admin log missing the package work item')

    // viewer default visibility = package + client (NOT internal): internal rows filtered out
    const viewerRes = await fetchExport(env, 'viewer@t.co', 'log.csv')
    assert.equal(viewerRes.status, 200)
    const viewer = splitCsv(viewerRes.body as string)
    assert.ok(viewer.body.includes('WI-PACKAGE'), 'viewer should see the package-log row')
    assert.ok(!viewer.body.includes('WI-INTERNAL'), 'viewer must NOT see the internal-log work item (PEC-NFR-005)')
    assert.ok(!viewer.body.includes('HLD-9100'), 'viewer must NOT see the internal-log hold (PEC-NFR-005)')
  } finally {
    await env.close()
  }
})
