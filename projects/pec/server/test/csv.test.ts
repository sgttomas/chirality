import { test } from 'node:test'
import assert from 'node:assert/strict'
import { toCsv } from '../src/import/csv.ts'

test('toCsv neutralizes spreadsheet formula-leading fields on export', () => {
  const csv = toCsv(
    ['kind', 'value'],
    [
      ['equals', '=2+2'],
      ['plus', '+SUM(A1:A2)'],
      ['minus', '-10+20'],
      ['at', '@HYPERLINK("http://example.invalid")'],
      ['safe', 'plain text'],
    ],
  )

  assert.equal(csv, [
    'kind,value',
    "equals,'=2+2",
    "plus,'+SUM(A1:A2)",
    "minus,'-10+20",
    'at,"\'@HYPERLINK(""http://example.invalid"")"',
    'safe,plain text',
    '',
  ].join('\r\n'))
})
