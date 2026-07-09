import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createStubEngine } from '../src/engine/stub.ts'
import type { ActResult, BoundActs } from '../src/engine/port.ts'

function acts(): { acts: BoundActs; calls: string[] } {
  const calls: string[] = []
  const hit = (name: string): Promise<ActResult> => {
    calls.push(name)
    return Promise.resolve({
      kind: 'result',
      act: 'read.report',
      ok: true,
      summary: `${name} read`,
      payload: {
        name,
        markdown: `# ${name}\nRecorded facts only.`,
        absent: [{ figure: 'percent complete', reason: 'not ingested yet' }],
        basis: [{ route: '/api/projects/1/reports/standard/' + name, source: 'standardReport' }],
      },
    })
  }
  return {
    calls,
    acts: {
      whoami: () => ({ personId: 16, name: 'PEC Agent', email: 'agent@t.co' }),
      proposeCsv: async () => ({ kind: 'refused', act: 'import.propose', reason: 'not used' }),
      refreshProposal: async () => ({ kind: 'refused', act: 'import.refresh', reason: 'not used' }),
      withdrawProposal: async () => ({ kind: 'refused', act: 'import.withdraw', reason: 'not used' }),
      proposalStatus: async () => ({ kind: 'refused', act: 'import.status', reason: 'not used' }),
      triageItem: async () => ({ kind: 'refused', act: 'intake.triage', reason: 'not used' }),
      intakeSummary: async () => ({ kind: 'refused', act: 'intake.summary', reason: 'not used' }),
      readScreenContext: async () => ({ kind: 'refused', act: 'screen.read', reason: 'not used' }),
      projectOverview: async () => ({ kind: 'refused', act: 'read.overview', reason: 'not used' }),
      readRegister: async () => ({ kind: 'refused', act: 'read.register', reason: 'not used' }),
      recordHistory: async () => ({ kind: 'refused', act: 'read.history', reason: 'not used' }),
      explainRevision: async () => ({ kind: 'refused', act: 'read.explain', reason: 'not used' }),
      readReport: (input) => hit(input.report),
    },
  }
}

test('D-PEC-37: user-defined report prompt routes to the bounded standard report read and cites absent figures', async () => {
  const engine = createStubEngine()
  const a = acts()
  const events = await engine.runTurn({ pid: 1, message: 'draft a custom report on deliverable completeness' }, a.acts)
  assert.deepEqual(a.calls, ['deliverable-completeness'])
  assert.equal(events[0]!.type, 'act:result')
  const reply = events.find((e) => e.type === 'agent:reply') as { text: string }
  assert.match(reply.text, /User-defined report draft/)
  assert.match(reply.text, /percent complete/)
  assert.match(reply.text, /bounded PEC report read/)
})

test('D-PEC-37: discipline report prompt selects the discipline grouping convention', async () => {
  const engine = createStubEngine()
  const a = acts()
  await engine.runTurn({ pid: 1, message: 'create a novel discipline report for the PD' }, a.acts)
  assert.deepEqual(a.calls, ['weekly-project-status-by-discipline'])
})

test('D-PEC-37: unsupported professional/go-live and mutation-shaped reports are refused before reads', async () => {
  const engine = createStubEngine()
  for (const message of [
    'write a custom report certifying this is ready for construction',
    'draft a report and approve all open items',
    'make a report predicting what will be complete next month',
  ]) {
    const a = acts()
    const events = await engine.runTurn({ pid: 1, message }, a.acts)
    assert.deepEqual(a.calls, [])
    assert.equal(events[0]!.type, 'act:refused')
  }
})

test('D-PEC-37: follow-up wording still routes through bounded report reads', async () => {
  const engine = createStubEngine()
  const a = acts()
  await engine.runTurn({
    pid: 1,
    message: 'make that report about package issues instead',
    history: [{ who: 'you', text: 'draft a custom report' }, { who: 'agent', text: 'Need a basis.' }],
  }, a.acts)
  assert.deepEqual(a.calls, ['package-issue-summary'])
})
