/**
 * D-PEC-36 standard report payload coverage.
 * Pins factual-or-absent report shape, basis pointers, and discipline/package grouping.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'

const P = (env: { projectId: number }) => `/api/projects/${env.projectId}`

test('D-PEC-36: weekly project status supports package and discipline grouping with basis + absent figures', async () => {
  const env = await createTestEnv()
  try {
    const lead = await env.as('lead@t.co')
    const byPackage = await lead.get(`${P(env)}/reports/standard/weekly-project-status`)
    assert.equal(byPackage.status, 200)
    assert.equal(byPackage.body.name, 'weekly-project-status')
    assert.equal(byPackage.body.sections.groupBy, 'package')
    assert.ok(Array.isArray(byPackage.body.basis))
    assert.ok(byPackage.body.basis.some((b: any) => b.route.endsWith('/overview')))
    assert.ok(byPackage.body.absent.some((a: any) => /percent complete/.test(a.figure)))
    assert.match(byPackage.body.markdown, /Weekly project status/)

    const byDiscipline = await lead.get(`${P(env)}/reports/standard/weekly-project-status?groupBy=discipline`)
    assert.equal(byDiscipline.status, 200)
    assert.equal(byDiscipline.body.sections.groupBy, 'discipline')
    assert.ok(Array.isArray(byDiscipline.body.sections.groups))
    assert.ok(byDiscipline.body.sections.groups.length > 0)
  } finally {
    await env.close()
  }
})

test('D-PEC-36: package issue summary and deliverable completeness name basis and avoid unsupported claims', async () => {
  const env = await createTestEnv()
  try {
    const lead = await env.as('lead@t.co')
    const pkg = await lead.get(`${P(env)}/reports/standard/package-issue-summary`)
    assert.equal(pkg.status, 200)
    assert.equal(pkg.body.name, 'package-issue-summary')
    assert.ok(Array.isArray(pkg.body.sections.packages))
    assert.ok(pkg.body.basis[0].source.includes('packageDetailView'))
    assert.ok(pkg.body.absent.some((a: any) => /needs/.test(a.figure)))

    const mdl = await lead.get(`${P(env)}/reports/standard/deliverable-completeness`)
    assert.equal(mdl.status, 200)
    assert.equal(mdl.body.name, 'deliverable-completeness')
    assert.ok(Array.isArray(mdl.body.sections.deliverables))
    assert.ok(mdl.body.sections.deliverables.every((d: any) => d.basis.recordType === 'deliverable'))
    assert.ok(mdl.body.absent.some((a: any) => /percent complete/.test(a.figure)))
  } finally {
    await env.close()
  }
})

test('D-PEC-36: unknown standard report names are refused by name', async () => {
  const env = await createTestEnv()
  try {
    const lead = await env.as('lead@t.co')
    const res = await lead.get(`${P(env)}/reports/standard/not-a-report`)
    assert.equal(res.status, 400)
    assert.match(res.body.error.message, /unknown standard report/)
  } finally {
    await env.close()
  }
})
