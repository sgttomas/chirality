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
    assert.ok(pkg.body.sections.packages.every((r: any) => r.needsSplit
      && typeof r.needsSplit.internal === 'number'
      && typeof r.needsSplit.client === 'number'
      && typeof r.needsSplit.unclassified === 'number'))

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

test('D-PEC-36: package and discipline hold counts only count holds linked to the counted group', async () => {
  const env = await createTestEnv()
  try {
    const pkgB = env.repo.insert('package', {
      projectId: env.projectId, code: 'PKG-B', name: 'Utilities', leadId: env.people['lead@t.co'],
    })
    const delB = env.repo.insert('deliverable', {
      projectId: env.projectId, packageId: pkgB, docNo: 'TST-UT-001', title: 'Utility PFD',
      discipline: 'Utilities', deliverableType: 'drawing', ownerId: env.people['eor@t.co'], dueDate: '2027-06-30',
    })
    const lead = await env.as('lead@t.co')
    const holdA = await lead.post(`${P(env)}/holds`, {
      title: 'Process vendor data hold', cause: 'vendor_data', ownerId: env.people['lead@t.co'],
      needBy: '2027-01-31', log: 'package',
      targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
    })
    assert.equal(holdA.status, 200, JSON.stringify(holdA.body))
    const holdB = await lead.post(`${P(env)}/holds`, {
      title: 'Utilities vendor data hold', cause: 'vendor_data', ownerId: env.people['lead@t.co'],
      needBy: '2027-01-31', log: 'package',
      targets: [{ targetType: 'deliverable', targetId: delB }],
    })
    assert.equal(holdB.status, 200, JSON.stringify(holdB.body))

    const pkg = await lead.get(`${P(env)}/reports/standard/package-issue-summary`)
    assert.equal(pkg.status, 200)
    const pkgA = pkg.body.sections.packages.find((r: any) => r.package.code === 'PKG-A')
    const pkgBRow = pkg.body.sections.packages.find((r: any) => r.package.code === 'PKG-B')
    assert.equal(pkgA.holds, 1)
    assert.equal(pkgBRow.holds, 1)
    assert.deepEqual(pkgA.contributing.filter((c: any) => c.recordType === 'hold').map((c: any) => c.id), [holdA.body.id])
    assert.deepEqual(pkgBRow.contributing.filter((c: any) => c.recordType === 'hold').map((c: any) => c.id), [holdB.body.id])

    const discipline = await lead.get(`${P(env)}/reports/standard/weekly-project-status?groupBy=discipline`)
    assert.equal(discipline.status, 200)
    const process = discipline.body.sections.groups.find((g: any) => g.key === 'Process')
    const utilities = discipline.body.sections.groups.find((g: any) => g.key === 'Utilities')
    assert.equal(process.issues.holds, 1)
    assert.equal(utilities.issues.holds, 1)
  } finally {
    await env.close()
  }
})

test('D-PEC-36: standard reports preserve log visibility and redact restricted contributing refs', async () => {
  const env = await createTestEnv()
  try {
    const lead = await env.as('lead@t.co')
    const internal = await lead.post(`${P(env)}/holds`, {
      title: 'SECRET internal hold', cause: 'vendor_data', ownerId: env.people['lead@t.co'],
      needBy: '2027-01-31', log: 'internal',
      targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
    })
    assert.equal(internal.status, 200, JSON.stringify(internal.body))
    const visible = await lead.post(`${P(env)}/holds`, {
      title: 'Visible package hold', cause: 'vendor_data', ownerId: env.people['lead@t.co'],
      needBy: '2027-01-31', log: 'package',
      targets: [{ targetType: 'deliverable', targetId: env.deliverableId }],
    })
    assert.equal(visible.status, 200, JSON.stringify(visible.body))

    const viewer = await env.as('viewer@t.co')
    const pkg = await viewer.get(`${P(env)}/reports/standard/package-issue-summary`)
    assert.equal(pkg.status, 200)
    assert.ok(!JSON.stringify(pkg.body).includes('SECRET'), 'restricted hold title does not leak')
    const pkgA = pkg.body.sections.packages.find((r: any) => r.package.code === 'PKG-A')
    assert.equal(pkgA.holds, 1)
    assert.ok(pkgA.contributing.some((c: any) => c.recordType === 'hold' && c.id === visible.body.id))
    assert.ok(!pkgA.contributing.some((c: any) => c.recordType === 'hold' && c.id === internal.body.id))

    const weekly = await viewer.get(`${P(env)}/reports/standard/weekly-project-status`)
    assert.equal(weekly.status, 200)
    const restrictedKpiRef = weekly.body.sections.kpis.holdsByCause.contributing
      .find((c: any) => c.recordType === 'hold' && c.id === internal.body.id)
    assert.ok(restrictedKpiRef, 'shared KPI derivation retains the restricted ref')
    assert.equal(restrictedKpiRef.why, '[restricted log]')
    const visibleKpiRef = weekly.body.sections.kpis.holdsByCause.contributing
      .find((c: any) => c.recordType === 'hold' && c.id === visible.body.id)
    assert.equal(visibleKpiRef.why, 'vendor_data')
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
