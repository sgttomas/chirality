/**
 * Stub engine pins (D-PEC-17): determinism, intent routing, the never-
 * accept/apply structural scan, and — non-negotiable (GOV MAJOR-1) — the
 * `converted` / `merged` disposition-vocabulary refusals with NO disposition
 * call issued.
 */

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createStubEngine } from '../src/engine/stub.ts'
import type { ActResult, AgentEvent, AgentTurnInput, BoundActs } from '../src/engine/port.ts'

interface Call { act: string; args: unknown }

/** deterministic fake acts layer that records every call */
function fakeActs(overrides: Partial<Record<string, ActResult>> = {}): { acts: BoundActs; calls: Call[] } {
  const calls: Call[] = []
  const canned = (act: string): ActResult =>
    overrides[act] ?? { kind: 'result', act, ok: true, summary: `${act} done`, payload: { act } }
  const record = (act: string) => (args: unknown): Promise<ActResult> => {
    calls.push({ act, args })
    return Promise.resolve(canned(act))
  }
  const acts: BoundActs = {
    whoami: () => ({ personId: 16, name: 'PEC Agent', email: 'pec-agent@rehearsal.demo' }),
    proposeCsv: record('import.propose') as BoundActs['proposeCsv'],
    refreshProposal: record('import.refresh') as BoundActs['refreshProposal'],
    withdrawProposal: record('import.withdraw') as BoundActs['withdrawProposal'],
    proposalStatus: () => { calls.push({ act: 'import.status', args: {} }); return Promise.resolve(canned('import.status')) },
    triageItem: record('intake.triage') as BoundActs['triageItem'],
    intakeSummary: () => { calls.push({ act: 'intake.summary', args: {} }); return Promise.resolve(canned('intake.summary')) },
    readScreenContext: record('screen.read') as BoundActs['readScreenContext'],
    // D-PEC-20 read acts
    projectOverview: () => { calls.push({ act: 'read.overview', args: {} }); return Promise.resolve(canned('read.overview')) },
    readRegister: record('read.register') as BoundActs['readRegister'],
    recordHistory: record('read.history') as BoundActs['recordHistory'],
    explainRevision: record('read.explain') as BoundActs['explainRevision'],
    readReport: record('read.report') as BoundActs['readReport'],
    draftDocx: record('report.draftDocx') as BoundActs['draftDocx'],
  }
  return { acts, calls }
}

const turn = (message: string, extra: Partial<AgentTurnInput> = {}): AgentTurnInput =>
  ({ pid: 1, message, ...extra })

const MDL_CSV = 'doc_no,title,package,discipline,owner,current_rev,state,due_date\nD-1,T,P,X,,A,in_work,2027-01-01'
const engine = createStubEngine()

test('determinism: two identical turns yield deep-equal event arrays', async () => {
  const a = await engine.runTurn(turn('status please'), fakeActs().acts)
  const b = await engine.runTurn(turn('status please'), fakeActs().acts)
  assert.deepEqual(a, b)
  const c = await engine.runTurn(turn('hello there'), fakeActs().acts)
  const d = await engine.runTurn(turn('hello there'), fakeActs().acts)
  assert.deepEqual(c, d)
})

test('engine declares itself: subject stub, egress none', () => {
  assert.equal(engine.subject, 'stub')
  assert.equal(engine.egress, 'none')
})

test('propose via attachment routes to proposeCsv with the attachment text', async () => {
  const { acts, calls } = fakeActs()
  const events = await engine.runTurn(
    turn('please file this', { attachment: { name: 'mdl.csv', text: MDL_CSV } }), acts)
  assert.equal(calls.length, 1)
  assert.equal(calls[0]!.act, 'import.propose')
  assert.equal((calls[0]!.args as { csv: string }).csv, MDL_CSV)
  assert.equal((calls[0]!.args as { contract?: string }).contract, undefined, 'no contract named — detection is the acts layer\'s')
  assert.equal(events.some((e) => e.type === 'act:result'), true)
  // WF-8 attribution + human-act deep link on the filing reply
  const reply = events.find((e) => e.type === 'agent:reply') as { text: string }
  assert.match(reply.text, /\/p\/1\/admin/)
  assert.match(reply.text, /PEC Agent/)
})

test('propose with a named contract overrides detection', async () => {
  const { acts, calls } = fakeActs()
  await engine.runTurn(
    turn('file this as rail', { attachment: { name: 'x.csv', text: 'a,b\n1,2' } }), acts)
  assert.equal((calls[0]!.args as { contract?: string }).contract, 'rail')
})

test('ambiguous/unknown headers: the acts refusal becomes an ask naming the five contracts', async () => {
  const { acts, calls } = fakeActs({
    'import.propose': {
      kind: 'refused', act: 'import.propose',
      reason: 'the CSV headers match no §16 contract — name the contract (one of: mdl, rail, decisions, risks, schedule)',
    },
  })
  const events = await engine.runTurn(
    turn('file this', { attachment: { name: 'x.csv', text: 'a,b\n1,2' } }), acts)
  assert.equal(calls.length, 1)
  assert.equal(events.length, 1)
  assert.equal(events[0]!.type, 'agent:reply')
  assert.match((events[0] as { text: string }).text, /mdl, rail, decisions, risks, schedule/)
})

test('refresh IPR-n routes to refreshProposal', async () => {
  const { acts, calls } = fakeActs()
  await engine.runTurn(turn('refresh IPR-0002'), acts)
  assert.deepEqual(calls, [{ act: 'import.refresh', args: { ref: 'IPR-0002' } }])
})

test('withdraw without a reason asks; with a reason routes to withdrawProposal', async () => {
  const { acts, calls } = fakeActs()
  const ask = await engine.runTurn(turn('withdraw IPR-0003'), acts)
  assert.equal(calls.length, 0, 'no act without a reason')
  assert.equal(ask[0]!.type, 'agent:reply')
  assert.match((ask[0] as { text: string }).text, /reason/)

  await engine.runTurn(turn('withdraw IPR-0003 because superseded by v2'), acts)
  assert.deepEqual(calls, [{ act: 'import.withdraw', args: { ref: 'IPR-0003', reason: 'superseded by v2' } }])
})

test('triage with grounds routes to triageItem (open-triage+disposition live in acts)', async () => {
  const { acts, calls } = fakeActs()
  await engine.runTurn(turn('triage INTK-0002 as parked: awaiting the vendor data'), acts)
  assert.deepEqual(calls, [{
    act: 'intake.triage',
    args: { ref: 'INTK-0002', disposition: 'parked', grounds: 'awaiting the vendor data' },
  }])
})

test('triage without grounds surfaces the acts-layer "left for the owner" refusal', async () => {
  const { acts, calls } = fakeActs({
    'intake.triage': { kind: 'refused', act: 'intake.triage', reason: 'no grounds given — left for the owner' },
  })
  const events = await engine.runTurn(turn('triage INTK-0002 as parked'), acts)
  assert.equal(calls.length, 1)
  assert.equal((calls[0]!.args as { grounds: string }).grounds, '')
  assert.equal(events[0]!.type, 'act:refused')
  assert.match((events[0] as { reason: string }).reason, /left for the owner/)
})

test('open triage INTK-n routes to triageItem with no disposition', async () => {
  const { acts, calls } = fakeActs()
  await engine.runTurn(turn('open triage INTK-0005'), acts)
  assert.deepEqual(calls, [{ act: 'intake.triage', args: { ref: 'INTK-0005' } }])
})

// GOV MAJOR-1 pin — non-negotiable
test('GOV MAJOR-1: `converted` is refused deterministically, directing the owner to the screen act — no disposition call issued', async () => {
  const { acts, calls } = fakeActs()
  const events = await engine.runTurn(turn('triage INTK-0001 as converted: make it a decision'), acts)
  assert.equal(calls.length, 0, 'NO act call — the refusal is the stub\'s own, before the acts layer')
  assert.equal(events.length, 1)
  assert.equal(events[0]!.type, 'act:refused')
  const reason = (events[0] as { reason: string }).reason
  assert.match(reason, /approval records/, 'names the reason conversion is closed')
  assert.match(reason, /on-screen/, 'directs the owner to perform the conversion on-screen')
  // determinism of the refusal itself
  const again = await engine.runTurn(turn('triage INTK-0001 as converted: make it a decision'), fakeActs().acts)
  assert.deepEqual(events, again)
})

test('GOV MAJOR-1: `merged` gets the outside-v1-vocabulary refusal — no disposition call issued', async () => {
  const { acts, calls } = fakeActs()
  const events = await engine.runTurn(turn('triage INTK-0003 as merged: same as INTK-0004'), acts)
  assert.equal(calls.length, 0)
  assert.equal(events[0]!.type, 'act:refused')
  assert.match((events[0] as { reason: string }).reason, /outside my v1 disposition vocabulary/)
})

test('unknown dispositions are refused with the vocabulary named', async () => {
  const { acts, calls } = fakeActs()
  const events = await engine.runTurn(turn('triage INTK-0003 as escalated: because'), acts)
  assert.equal(calls.length, 0)
  assert.equal(events[0]!.type, 'act:refused')
  assert.match((events[0] as { reason: string }).reason, /parked, duplicate, rejected/)
})

test('status intents route to proposalStatus / intakeSummary', async () => {
  const a = fakeActs()
  await engine.runTurn(turn('status'), a.acts)
  assert.equal(a.calls[0]!.act, 'import.status')

  const b = fakeActs()
  await engine.runTurn(turn('show me the intake queue'), b.acts)
  assert.equal(b.calls[0]!.act, 'intake.summary')
})

test('screen intent with context routes to readScreenContext', async () => {
  const { acts, calls } = fakeActs()
  const context = { route: '/p/1/deliverables/7', records: [{ recordType: 'deliverable', ref: 'TST-PR-001', id: 7 }] }
  await engine.runTurn(turn('what am I looking at?', { context }), acts)
  assert.deepEqual(calls, [{ act: 'screen.read', args: context }])
})

test('fallback: deterministic capability statement naming the human-act boundary', async () => {
  const { acts, calls } = fakeActs()
  const events = await engine.runTurn(turn('write me a poem'), acts)
  assert.equal(calls.length, 0)
  assert.equal(events.length, 1)
  assert.equal(events[0]!.type, 'agent:reply')
  const text = (events[0] as { text: string }).text
  assert.match(text, /Accept, apply, and reject-of-others happen in Admin, by you/)
})

test('structural scan: no event stream ever contains an accept/apply act', async () => {
  const inputs: AgentTurnInput[] = [
    turn('please file this', { attachment: { name: 'mdl.csv', text: MDL_CSV } }),
    turn('refresh IPR-0001'),
    turn('withdraw IPR-0001 because testing'),
    turn('triage INTK-0001 as parked: grounds'),
    turn('triage INTK-0001 as converted: grounds'),
    turn('status'), turn('intake'), turn('anything else at all'),
    turn('accept IPR-0001'), turn('apply IPR-0001'), turn('force apply IPR-0001'),
  ]
  for (const input of inputs) {
    const events: AgentEvent[] = await engine.runTurn(input, fakeActs().acts)
    for (const e of events) {
      const acted = e.type === 'act:result' || e.type === 'act:refused' ? e.act : ''
      assert.doesNotMatch(acted, /accept|apply/, `no accept/apply act for "${input.message}"`)
      // the whole serialized event never names an accept or apply act type
      assert.doesNotMatch(JSON.stringify(e), /"act":\s*"[^"]*(accept|apply)/, JSON.stringify(e))
    }
  }
})
