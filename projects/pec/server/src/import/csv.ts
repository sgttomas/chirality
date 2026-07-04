/** RFC 4180 CSV parse/serialize (ADR-002: no deps; ours to test). */

export function parseCsv(text: string): string[][] {
  const rows: string[][] = []
  let row: string[] = []
  let field = ''
  let inQuotes = false
  let i = 0
  const src = text.replace(/^﻿/, '') // strip BOM
  while (i < src.length) {
    const ch = src[i]!
    if (inQuotes) {
      if (ch === '"') {
        if (src[i + 1] === '"') { field += '"'; i += 2; continue }
        inQuotes = false; i++; continue
      }
      field += ch; i++; continue
    }
    if (ch === '"') { inQuotes = true; i++; continue }
    if (ch === ',') { row.push(field); field = ''; i++; continue }
    if (ch === '\r') { i++; continue }
    if (ch === '\n') { row.push(field); rows.push(row); row = []; field = ''; i++; continue }
    field += ch; i++
  }
  if (field.length > 0 || row.length > 0) { row.push(field); rows.push(row) }
  return rows.filter((r) => !(r.length === 1 && r[0] === ''))
}

export function toCsv(headers: string[], rows: Array<Array<string | number | null | undefined>>): string {
  const esc = (v: string | number | null | undefined): string => {
    const s = v == null ? '' : String(v)
    return /[",\n\r]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s
  }
  return [headers.map(esc).join(','), ...rows.map((r) => r.map(esc).join(','))].join('\r\n') + '\r\n'
}

export interface ParsedTable {
  headers: string[]
  rows: Array<Record<string, string>>
}

/** Parse with a header row; header names lowercased/trimmed. */
export function parseTable(text: string): ParsedTable {
  const raw = parseCsv(text)
  if (raw.length === 0) return { headers: [], rows: [] }
  const headers = raw[0]!.map((h) => h.trim().toLowerCase())
  const rows = raw.slice(1).map((r) => {
    const obj: Record<string, string> = {}
    headers.forEach((h, idx) => { obj[h] = (r[idx] ?? '').trim() })
    return obj
  })
  return { headers, rows }
}
