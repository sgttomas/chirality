import { test } from 'node:test'
import assert from 'node:assert/strict'
import { adaptStructuredFile } from '../src/structured-file.ts'
import { bindActs } from '../src/acts.ts'
import type { PecAgentClient, ProposalView } from '../src/pec-client.ts'

const proposal = (contract: string, sourceName: string | null): ProposalView => ({
  id: 7,
  ref: 'IPR-0007',
  contract,
  state: 'ready_for_review',
  version: 1,
  createdBy: 16,
  sourceName,
  sourceSha256: 'abc',
  dryRunReport: { accepted: 1, updated: 0, conflicts: [], rejected: [], intakeCreated: 0 },
})

test('D-PEC-35 mapper normalizes TSV headers to a contract-shaped CSV', () => {
  const text = [
    'Document No\tTitle\tPackage\tDiscipline\tOwner\tCurrent Revision\tState\tDue Date',
    'MDL-001\tPump list\tP-001\tMech\tpe@example.test\tA\tin_work\t2027-01-01',
  ].join('\n')
  const mapped = adaptStructuredFile(text, { filename: 'mdl.tsv' })
  assert.equal(mapped.ok, true)
  if (!mapped.ok) return
  assert.equal(mapped.contract, 'mdl')
  assert.equal(mapped.filename, 'mdl.csv')
  assert.match(mapped.csv, /^doc_no,title,package,discipline,owner,current_rev,state,due_date/)
  assert.equal(mapped.summary.sourceFormat, 'tsv')
  assert.deepEqual(mapped.summary.requiredEmptyRows, [])
})

test('D-PEC-35 mapper detects tracker contract instead of stopping at the five older contracts', () => {
  const text = [
    'tracking_no,package_name,discipline,area,stage_budgetary_datasheet,stage_cost_estimate,stage_package_datasheet,stage_package,stage_rfq,stage_review,stage_vendor_bids,stage_clarifications,stage_evaluation,stage_eng_req,stage_po,stage_databook,package',
    'COA-1,Pump Package,Mech,A1,done,done,done,done,done,done,done,done,done,done,done,done,P-001',
  ].join('\n')
  const mapped = adaptStructuredFile(text)
  assert.equal(mapped.ok, true)
  if (!mapped.ok) return
  assert.equal(mapped.contract, 'tracker')
})

test('D-PEC-35 mapper refuses missing required columns instead of guessing', () => {
  const mapped = adaptStructuredFile('title,package\nPump list,P-001', { contract: 'mdl' })
  assert.equal(mapped.ok, false)
  if (mapped.ok) return
  assert.match(mapped.reason, /missing required columns/)
  assert.match(mapped.reason, /doc_no/)
})

test('D-PEC-35 act files only normalized CSV and returns the mapping summary', async () => {
  const calls: Array<{ contract: string; csv: string; filename?: string }> = []
  const client = {
    whoami: () => ({ personId: 16, name: 'PEC Agent', email: 'agent@example.test' }),
    propose: async (_pid: number, contract: string, csv: string, filename?: string) => {
      calls.push({ contract, csv, filename })
      return { ok: true as const, value: proposal(contract, filename ?? null) }
    },
  } as unknown as PecAgentClient
  const acts = bindActs({ pid: 1, egress: 'none', access: 'enumerated', client })
  const result = await acts.proposeCsv({
    filename: 'mdl.tsv',
    csv: [
      'Document No\tTitle\tPackage\tDiscipline\tOwner\tCurrent Revision\tState\tDue Date',
      'MDL-001\tPump list\tP-001\tMech\tpe@example.test\tA\tin_work\t2027-01-01',
    ].join('\n'),
  })
  assert.equal(result.kind, 'result')
  assert.equal(calls.length, 1)
  assert.equal(calls[0]!.contract, 'mdl')
  assert.equal(calls[0]!.filename, 'mdl.csv')
  assert.match(calls[0]!.csv, /^doc_no,title,package,discipline,owner,current_rev,state,due_date/)
  assert.match((result as { summary: string }).summary, /mapping: tsv → mdl CSV/)
  assert.equal(((result as { payload: any }).payload.mapping.contract), 'mdl')
})

test('D-PEC-35 act refuses unmappable text before any proposal call', async () => {
  let called = false
  const client = {
    whoami: () => ({ personId: 16, name: 'PEC Agent', email: 'agent@example.test' }),
    propose: async () => {
      called = true
      return { ok: true as const, value: proposal('mdl', 'x.csv') }
    },
  } as unknown as PecAgentClient
  const acts = bindActs({ pid: 1, egress: 'none', access: 'enumerated', client })
  const result = await acts.proposeCsv({ filename: 'notes.txt', csv: 'thing | note\none | unclear' })
  assert.equal(result.kind, 'refused')
  assert.equal(called, false)
  assert.match((result as { reason: string }).reason, /match no import contract/)
})

// ---------------------------------------------------------------------------
// Contract v2 shapes (D-PEC-41): same contract ids, revised TWD template headers
// ---------------------------------------------------------------------------

test('D-PEC-41 mdl v2 shape detects and maps with the TWD verbatim headers', () => {
  const text = [
    'Area #\tProject Phase\tDiscipline\tPackage ID\tPackage Type\tPackage Name\tDeliverable ID\tDeliverable Type\tTarget Completeness\tWorking Status\t% Complete',
    '01\t30%\tElectrical\t26020-PKG-019\tEquipment\t4160V Switchgear\t\tRFQ\tIFQ\tIn Progress\t5',
  ].join('\n')
  const mapped = adaptStructuredFile(text, { filename: 'Deliverables_Status.tsv' })
  assert.equal(mapped.ok, true, JSON.stringify(mapped))
  if (mapped.ok) {
    assert.equal(mapped.contract, 'mdl')
    assert.match(mapped.csv, /^area,project_phase,discipline,package,package_type,package_name,deliverable_id,deliverable_type,target_completeness,working_status,percent_complete/)
    assert.match(mapped.csv, /26020-PKG-019/)
    assert.equal(mapped.summary.omittedSourceHeaders.length, 0)
  }
})

test('D-PEC-41 rail v2 shape maps Package ID vs PACKAGE (name) without collision', () => {
  const text = [
    'Package ID\tIssue #\tPackage Discipline\tArea\tPhase\tCoA Tracking Number\tPackage Type\tPACKAGE\tISSUE TYPE\tISSUE DESCRIPTION\tUPDATES\tResponsible Party\tSTATUS\tPRIORITY\tASSIGNED DATE\tORIGINAL TARGET COMPLETION DATE\tCURRENT TARGET COMPLETION DATE\tACTUAL COMPLETION DATE',
    '26020-PKG-008\t1\tElectrical\t\t30%\t\tDocumentation\tControls integration\tDecision\tDecide remote I/O approach\tNeed philosophy\tProject Management\tNot Started\tNow\t2026-07-07\t2026-07-14\t2026-07-14\t',
  ].join('\n')
  const mapped = adaptStructuredFile(text, { filename: 'RAIL_Packages.tsv' })
  assert.equal(mapped.ok, true, JSON.stringify(mapped))
  if (mapped.ok) {
    assert.equal(mapped.contract, 'rail')
    const hdr = mapped.csv.split('\r\n')[0]!
    assert.match(hdr, /(^|,)package(,|$)/)
    assert.match(hdr, /package_name/)
    assert.match(hdr, /issue_no/)
    assert.match(hdr, /original_target_date/)
    assert.match(hdr, /percent_complete|statement/) // statement mapped from ISSUE DESCRIPTION
    assert.equal(mapped.summary.omittedSourceHeaders.length, 0)
  }
})

test('D-PEC-41 v1 shapes still map unchanged (additive)', () => {
  const text = [
    'doc_no,title,package,discipline,owner,current_rev,state,due_date',
    'D-1,Sheet,P-1,Mech,pe@example.test,A,in_work,2027-01-01',
  ].join('\n')
  const mapped = adaptStructuredFile(text)
  assert.equal(mapped.ok, true)
  if (mapped.ok) assert.equal(mapped.contract, 'mdl')
})
