import { test } from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, readFile, rm } from 'node:fs/promises'
import { join } from 'node:path'
import { tmpdir } from 'node:os'
import { buildDisciplineStatusDocx, parseDeclaredPeriod, writeDraftDocx } from '../src/docx-report.ts'

const CLARIFICATION = 'Needs and issues are tracked and reported by package. This includes decisions, risks, action items, clarifications, needs for information and resources etc. Status (i.e. working status, such as in progress or complete) and % complete are tracked by deliverable. Period declaration can happen in the agent sidecar via prompt. Yes I accept the honest absences.'

function syntheticDraft() {
  return buildDisciplineStatusDocx({
    project: { code: 'SYN', name: 'Synthetic Project' },
    period: { start: '2026-07-01', end: '2026-07-07' },
    generatedAt: '2026-07-09T00:00:00.000Z',
    compositionClarification: CLARIFICATION,
    disciplines: [{
      discipline: 'Process',
      band: {
        percentComplete: { value: 42.5, ruleId: 'DISC-PCT' },
      },
      sections: {
        activities: {
          groups: [{
            type: 'PFD',
            deliverables: [
              { docNo: 'SYN-PFD-001', title: 'Process flow diagram', workflow: { label: 'in work' }, percentComplete: 50 },
              { docNo: 'SYN-PFD-002', title: 'Future phase PFD', workflow: { label: 'in work' }, percentCompleteVerbatim: 'Next Phase' },
            ],
          }],
        },
        issuances: {
          rows: [{ ref: 'ISS-1', docNo: 'SYN-PFD-001', issuedAt: '2026-07-03T12:00:00.000Z', purpose: 'Issued for review' }],
        },
      },
    }, {
      discipline: 'Mechanical',
      sections: { activities: { groups: [] }, issuances: { rows: [] } },
    }],
    packageDetails: [{
      package: { code: 'SYN-PKG-001', name: 'Compressor' },
      summary: { openIssues: 2, openDecisions: 1, openInterfaces: 1 },
      issues: [
        { type: 'action', ref: 'SYN-PKG-001#1', title: 'Clarify seal plan', detail: 'Clarification', state: 'open', needBy: '2026-07-10' },
        { type: 'risk', ref: 'RSK-1', title: 'Vendor delay', detail: 'schedule', state: 'mitigating' },
      ],
      decisions: [{ ref: 'DEC-1', title: 'Select seal flush basis', state: 'pending', needBy: '2026-07-11' }],
      interfaces: [{ ref: 'INT-1', title: 'Process to mechanical data', giving: 'Process', receiving: 'Mechanical', state: 'open' }],
    }],
  })
}

test('D-PEC-44: docx writer emits template-conformant WordprocessingML with basis notes', () => {
  const draft = syntheticDraft()
  assert.ok(draft.bytes.subarray(0, 2).equals(Buffer.from('PK')), 'docx is a ZIP package')
  assert.match(draft.documentXml, /w:pStyle w:val="Title"/)
  assert.match(draft.documentXml, /w:pStyle w:val="Heading1"/)
  assert.match(draft.documentXml, /w:pStyle w:val="Subtitle"/)
  assert.match(draft.documentXml, /w:pStyle w:val="ListParagraph"/)
  assert.match(draft.documentText, /SYN-PFD-001 - Process flow diagram; in work; % 50% \(basis: DISC-ACT; DISC-PCT\)/)
  assert.match(draft.documentText, /SYN-PFD-002 - Future phase PFD; in work; % Next Phase \(basis: DISC-ACT; DISC-PCT\)/)
  assert.match(draft.documentText, /SYN-PKG-001#1 Clarify seal plan; Clarification; open; need-by 2026-07-10 \(basis: PKG-ISSUE-MIX\)/)
  assert.match(draft.documentText, /None recorded \(basis: DISC-ACT\)/)
  assert.match(draft.documentText, /None recorded \(basis: DISC-ISSUED\)/)
  assert.deepEqual(draft.figures, {
    disciplines: 2,
    inWorkDeliverables: 2,
    issuancesThisPeriod: 1,
    packageIssueRows: 2,
    packageDecisionRows: 1,
    packageInterfaceRows: 1,
  })
})

test('D-PEC-44: golden text stays factual-or-absent and package-scoped for needs/issues', () => {
  const draft = syntheticDraft()
  const goldenSubset = [
    'SYN Discipline Status Report Draft',
    'Declared period: 2026-07-01 to 2026-07-07 (basis: sidecar prompt; PER-COV)',
    `Composition clarification: ${CLARIFICATION}`,
    'Process',
    'Activities',
    'Discipline % complete: 42.5% (basis: DISC-PCT)',
    'By Package',
    'Needs & Issues',
    '- SYN-PKG-001: SYN-PKG-001#1 Clarify seal plan; Clarification; open; need-by 2026-07-10 (basis: PKG-ISSUE-MIX)',
    'Decisions',
    '- SYN-PKG-001: DEC-1 Select seal flush basis; pending; need-by 2026-07-11 (basis: PKG-DEC)',
    'Interfaces',
    '- SYN-PKG-001: INT-1 Process to mechanical data; Process -> Mechanical; open (basis: PKG-INT)',
  ].join('\n')
  for (const line of goldenSubset.split('\n')) {
    assert.ok(draft.documentText.includes(line), `missing golden line: ${line}`)
  }
})

test('D-PEC-44: period parser requires explicit dates; writer creates a .docx file', async () => {
  assert.deepEqual(parseDeclaredPeriod('generate docx report period 2026-07-01 to 2026-07-07'), {
    start: '2026-07-01',
    end: '2026-07-07',
  })
  assert.equal(parseDeclaredPeriod('generate docx report for this week'), null)
  const dir = await mkdtemp(join(tmpdir(), 'pec-docx-report-'))
  try {
    const draft = syntheticDraft()
    const path = await writeDraftDocx(dir, draft)
    assert.deepEqual(await readFile(path), draft.bytes)
  } finally {
    await rm(dir, { recursive: true, force: true })
  }
})
