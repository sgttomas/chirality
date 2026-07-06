/**
 * Admin — CSV import with a per-row accept/conflict/reject report (PRD §16, SPEC §8),
 * register exports (every register exports exactly what it displays), the per-project
 * governance thresholds editor (PEC-OV-007), and the people directory. All guards are
 * server-side: import and config writes require config.manage; a 403 renders as-is (SPEC §1).
 */

import { useState } from 'react'
import { PecApiError, api, p } from '../api.ts'
import { ErrorBox, useApp, useLoad } from '../shared.tsx'

export function AdminPage(): JSX.Element {
  return (
    <div>
      <h1>Admin</h1>
      <ProposalsSection />
      <ImportSection />
      <ExportSection />
      <ThresholdsSection />
      <PeopleSection />
    </div>
  )
}

// ================================================================ proposed imports (D-PEC-08)

interface ImportProposalRow {
  id: number
  ref: string
  contract: string
  sourceName: string | null
  sourceSha256: string
  sourceBytes: number
  state: 'draft' | 'ready_for_review' | 'accepted' | 'rejected' | 'applied'
  dryRunReport: (ImportReport & { error?: undefined }) | { error: string } | null
  applyReport: ImportReport | null
  rejectReason: string | null
  version: number
}

/** Proposals POST the CSV as a text body (like direct import); metadata rides the query. */
async function proposeCsv(pid: number, contract: string, csv: string, filename: string | null): Promise<ImportProposalRow> {
  const q = filename ? `?contract=${contract}&filename=${encodeURIComponent(filename)}` : `?contract=${contract}`
  const res = await fetch(p(pid, `import-proposals${q}`), {
    method: 'POST', credentials: 'same-origin',
    headers: { 'content-type': 'text/csv' }, body: csv,
  })
  const text = await res.text()
  let parsed: any = text
  try { parsed = JSON.parse(text) } catch { /* non-JSON error body */ }
  if (!res.ok) {
    const err = parsed?.error ?? { code: `HTTP_${res.status}`, message: text || res.statusText, details: null }
    throw new PecApiError({ status: res.status, ...err })
  }
  return parsed as ImportProposalRow
}

function ProposalsSection(): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const [contract, setContract] = useState('mdl')
  const [csv, setCsv] = useState('')
  const [fileName, setFileName] = useState<string | null>(null)
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)
  const [reload, setReload] = useState(0)
  const { data: rows, error: listError } = useLoad<ImportProposalRow[]>(
    () => api.get(p(pid, 'import-proposals')), [pid, reload])

  const onFile = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const f = e.target.files?.[0]
    if (!f) return
    setCsv(await f.text())
    setFileName(f.name)
  }

  const act = async (fn: () => Promise<unknown>, done: string) => {
    setBusy(true); setError(null)
    try {
      await fn()
      toast(done)
      setReload((n) => n + 1)
      refresh()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  const propose = (e: React.FormEvent) => {
    e.preventDefault()
    void act(async () => {
      const r = await proposeCsv(pid, contract, csv, fileName)
      setCsv(''); setFileName(null)
      return r
    }, 'Proposal created — review the dry-run below')
  }

  return (
    <div>
      <h2>Proposed imports (D-PEC-08)</h2>
      <p className="section-note">
        Upload → dry-run preview → accept (bound to the file's SHA-256) → apply. The
        dry-run runs the real §16 contract and rolls back; nothing changes until a
        human accepts and applies. If the registers change in between, the proposal
        goes stale and must be refreshed and re-accepted.
      </p>
      <form className="stack card" style={{ maxWidth: 640 }} onSubmit={propose}>
        <div className="row">
          <label>Contract
            <select value={contract} onChange={(e) => setContract(e.target.value)}>
              {CONTRACTS.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
            </select>
          </label>
          <label>CSV file {fileName && <span className="muted">({fileName})</span>}
            <input type="file" accept=".csv,text/csv" onChange={onFile} />
          </label>
        </div>
        <label>… or paste CSV (header row required, RFC 4180)
          <textarea value={csv} onChange={(e) => { setCsv(e.target.value); setFileName(null) }} />
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !csv.trim()}>Propose import</button>
        </div>
      </form>
      {listError && <ErrorBox error={{ message: listError }} />}
      {rows && rows.length > 0 && (
        <table className="reg" style={{ marginTop: '.6rem', maxWidth: 860 }}>
          <thead><tr><th>Ref</th><th>Contract</th><th>File</th><th>State</th><th>Dry-run</th><th /></tr></thead>
          <tbody>
            {rows.map((r) => <ProposalRow key={r.id} row={r} busy={busy} act={act} />)}
          </tbody>
        </table>
      )}
    </div>
  )
}

function ProposalRow({ row, busy, act }: {
  row: ImportProposalRow
  busy: boolean
  act: (fn: () => Promise<unknown>, done: string) => Promise<void>
}): JSX.Element {
  const { pid } = useApp()
  const [open, setOpen] = useState(false)
  const base = p(pid, `import-proposals/${row.id}`)
  const report = row.state === 'applied' ? row.applyReport : row.dryRunReport
  const summary = report == null ? '—'
    : 'error' in report && report.error ? `error: ${report.error}`
    : `${(report as ImportReport).accepted} create · ${(report as ImportReport).updated} update · ${(report as ImportReport).conflicts.length} conflicts · ${(report as ImportReport).rejected.length} rejected · ${(report as ImportReport).intakeCreated} to intake`
  return (
    <>
      <tr>
        <td className="mono">{row.ref}</td>
        <td className="mono">{row.contract}</td>
        <td className="small">{row.sourceName ?? '—'} <span className="muted mono">({row.sourceSha256.slice(0, 12)}…)</span></td>
        <td>{row.state}{row.state === 'rejected' && row.rejectReason && <span className="muted small"> — {row.rejectReason}</span>}</td>
        <td className="small">{summary}{report != null && !('error' in report && report.error) && (
          <> <button className="btn small secondary" onClick={() => setOpen(!open)}>{open ? 'hide' : 'detail'}</button></>
        )}</td>
        <td>
          {row.state === 'ready_for_review' && (
            <>
              {/* acceptance echoes the displayed hash + version: what you see is what you approve (RV-13) */}
              <button className="btn small" disabled={busy}
                onClick={() => void act(() => api.post(`${base}/accept`, { version: row.version, sha256: row.sourceSha256 }),
                  `${row.ref} accepted`)}>Accept</button>{' '}
              <button className="btn small secondary" disabled={busy}
                onClick={() => void act(() => api.post(`${base}/refresh`, { version: row.version }), `${row.ref} dry-run refreshed`)}>Refresh</button>
            </>
          )}
          {row.state === 'accepted' && (
            <button className="btn small" disabled={busy}
              onClick={() => void act(() => api.post(`${base}/apply`, { version: row.version }), `${row.ref} applied`)}>Apply</button>
          )}
          {(row.state === 'draft' || row.state === 'ready_for_review' || row.state === 'accepted') && (
            <>{' '}
              <button className="btn small secondary" disabled={busy}
                onClick={() => {
                  const reason = window.prompt('Reject reason?')
                  if (reason) void act(() => api.post(`${base}/reject`, { version: row.version, reason }), `${row.ref} rejected`)
                }}>Reject</button>
            </>
          )}
        </td>
      </tr>
      {open && report != null && !('error' in report && report.error) && (
        <tr><td colSpan={6}><ImportReportView report={report as ImportReport} /></td></tr>
      )}
    </>
  )
}

// ================================================================ import (PRD §16)

interface ImportReport {
  contract: string
  accepted: number
  updated: number
  conflicts: Array<{ row: number; key: string; reason: string }>
  rejected: Array<{ row: number; errors: string[] }>
  intakeCreated: number
}

/**
 * The api client speaks JSON; imports POST the CSV as a plain text/csv body (SPEC §7),
 * so this helper uses fetch directly and re-raises errors as PecApiError.
 */
async function importCsv(pid: number, contract: string, csv: string, force: boolean): Promise<ImportReport> {
  const res = await fetch(p(pid, `import/${contract}${force ? '?force=true' : ''}`), {
    method: 'POST',
    credentials: 'same-origin',
    headers: { 'content-type': 'text/csv' },
    body: csv,
  })
  const text = await res.text()
  let parsed: any = text
  try { parsed = JSON.parse(text) } catch { /* non-JSON error body */ }
  if (!res.ok) {
    const err = parsed?.error ?? { code: `HTTP_${res.status}`, message: text || res.statusText, details: null }
    throw new PecApiError({ status: res.status, ...err })
  }
  return parsed as ImportReport
}

const CONTRACTS = [
  ['mdl', 'MDL — master deliverables list'],
  ['rail', 'RAIL — rolling action item list'],
  ['decisions', 'Decision log'],
  ['risks', 'Risk register'],
  ['schedule', 'Schedule activities (P2 — feeds the lookahead)'],
] as const

function ImportSection(): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const [contract, setContract] = useState('mdl')
  const [csv, setCsv] = useState('')
  const [fileName, setFileName] = useState<string | null>(null)
  const [force, setForce] = useState(false)
  const [report, setReport] = useState<ImportReport | null>(null)
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const onFile = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const f = e.target.files?.[0]
    if (!f) return
    setCsv(await f.text())
    setFileName(f.name)
  }

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null); setReport(null)
    try {
      // per-row accept/conflict/reject report — rows are never silently dropped (PRD §16)
      const r = await importCsv(pid, contract, csv, force)
      setReport(r)
      toast(`${r.contract} import: ${r.accepted} created, ${r.updated} updated, ${r.conflicts.length} conflicts, ${r.rejected.length} rejected`)
      refresh()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <div>
      <h2>Import (PRD §16)</h2>
      <p className="section-note">
        Idempotent by key (doc_no / item_id / decision_id / risk_id). Rows edited in-app
        since the last import are reported as conflicts unless force is set — force
        overwrites and writes history (SPEC §8).
      </p>
      <form className="stack card" style={{ maxWidth: 640 }} onSubmit={submit}>
        <div className="row">
          <label>Contract
            <select value={contract} onChange={(e) => setContract(e.target.value)}>
              {CONTRACTS.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
            </select>
          </label>
          <label>CSV file {fileName && <span className="muted">({fileName})</span>}
            <input type="file" accept=".csv,text/csv" onChange={onFile} />
          </label>
        </div>
        <label>… or paste CSV (header row required, RFC 4180)
          <textarea value={csv} onChange={(e) => { setCsv(e.target.value); setFileName(null) }}
            placeholder="doc_no,title,package,discipline,owner,current_rev,state,due_date" />
        </label>
        <label style={{ flexDirection: 'row', alignItems: 'center', gap: '.4rem' }}>
          <input type="checkbox" checked={force} onChange={(e) => setForce(e.target.checked)} />
          Force — overwrite rows edited in-app since the last import (writes history)
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !csv.trim()}>Import</button>
        </div>
      </form>
      {report && <ImportReportView report={report} />}
    </div>
  )
}

function ImportReportView({ report }: { report: ImportReport }): JSX.Element {
  return (
    <div style={{ marginTop: '.6rem', maxWidth: 640 }}>
      <div className="ok-box">
        <b>{report.contract}</b>: {report.accepted} created · {report.updated} updated
        {report.intakeCreated > 0 && <> · {report.intakeCreated} unmatched row(s) landed as unanchored intake (I-2)</>}
        {report.conflicts.length === 0 && report.rejected.length === 0 && <> · no conflicts, nothing rejected</>}
      </div>
      {report.conflicts.length > 0 && (
        <>
          <h3>Conflicts ({report.conflicts.length}) — edited in-app since last import</h3>
          <table className="reg">
            <thead><tr><th>Row</th><th>Key</th><th>Reason</th></tr></thead>
            <tbody>
              {report.conflicts.map((c) => (
                <tr key={`${c.row}-${c.key}`}>
                  <td className="mono">{c.row}</td>
                  <td className="mono">{c.key}</td>
                  <td className="small">{c.reason}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
      {report.rejected.length > 0 && (
        <>
          <h3>Rejected ({report.rejected.length}) — never silently dropped</h3>
          <table className="reg">
            <thead><tr><th>Row</th><th>Errors</th></tr></thead>
            <tbody>
              {report.rejected.map((r) => (
                <tr key={r.row}>
                  <td className="mono">{r.row}</td>
                  <td className="small">{r.errors.join('; ')}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  )
}

// ================================================================ export

const EXPORTS = [
  ['mdl', 'MDL'],
  ['rail', 'RAIL'],
  ['decisions', 'Decisions'],
  ['risks', 'Risks'],
  ['approvals', 'Approvals'],
  ['interfaces', 'Interfaces'],
  ['intake', 'Intake'],
  ['commitments', 'Weekly commitments'],
  ['schedule', 'Schedule activities'],
  ['lookahead', 'Six-week lookahead'],
] as const

function ExportSection(): JSX.Element {
  const { pid } = useApp()
  return (
    <div>
      <h2>Export</h2>
      <p className="section-note">
        Exports mirror the import schemas so a register round-trips (SPEC §8); the RAIL
        export includes non-converted intake items flagged unanchored. Commitments is the
        individual weekly commitments report (PRD §15).
      </p>
      <div className="filters">
        {EXPORTS.map(([name, label]) => (
          <button key={name} className="btn small secondary"
            onClick={() => window.open(p(pid, `export/${name}.csv`))}>{label} (.csv)</button>
        ))}
        <button className="btn small secondary" title="print-friendly HTML; print to PDF (ADR-010)"
          onClick={() => window.open(p(pid, 'reports/sponsor-brief'))}>⎙ Sponsor brief</button>
      </div>
    </div>
  )
}

// ================================================================ thresholds (PEC-OV-007)

/** Every §8.4 governance threshold, per-project overridable (PEC-OV-007). */
const THRESHOLD_KEYS: ReadonlyArray<readonly [string, string]> = [
  ['holdAgeWarnWd', 'Hold age — warn (wd)'],
  ['holdAgeRedWd', 'Hold age — escalate (wd)'],
  ['decisionOverdueWarnD', 'Decision overdue — warn (d)'],
  ['decisionOverdueRedD', 'Decision overdue — escalate (d)'],
  ['approvalLatencyWarnWd', 'Approval latency — warn (wd)'],
  ['approvalLatencyRedWd', 'Approval latency — escalate (wd)'],
  ['commentAgeWarnWd', 'Check-comment age — warn (wd)'],
  ['commentAgeRedWd', 'Check-comment age — escalate (wd)'],
  ['untriagedWarnWd', 'Untriaged intake age — warn (wd)'],
  ['untriagedRedWd', 'Untriaged intake age — escalate (wd)'],
  ['unanchoredWarnCount', 'Unanchored items — warn (count)'],
  ['unanchoredRedCount', 'Unanchored items — escalate (count)'],
  ['unanchoredRedAgeD', 'Unanchored item age — escalate (d)'],
  ['forecastSlipAmberWd', 'Forecast slip — amber up to (wd)'],
  ['schedulePressureWarnD', 'Schedule pressure — warn (d)'],
  ['schedulePressureRedD', 'Schedule pressure — escalate (d)'],
  ['interfaceOverdueRedWd', 'Interface overdue — escalate (wd)'],
  ['interfaceOverdueWarnWd', 'Interface overdue — warn (wd, P2)'],
  ['capacityWarnPct', 'Capacity load — warn (%, P2)'],
  ['capacityRedPct', 'Capacity load — escalate (%, P2)'],
]

function ThresholdsSection(): JSX.Element {
  const { pid } = useApp()
  const { data, error } = useLoad(() => api.get(p(pid, 'config')), [pid])
  return (
    <div>
      <h2>Governance thresholds (§8.4, PEC-OV-007)</h2>
      {error && <ErrorBox error={{ message: error }} />}
      {!data && !error && <p className="muted">loading…</p>}
      {data && <ThresholdsForm key={data.version} project={data} />}
    </div>
  )
}

function ThresholdsForm({ project }: { project: any }): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const [th, setTh] = useState<Record<string, number>>({ ...project.thresholds })
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    try {
      // optimistic concurrency on the project row (PEC-NFR-004); 403 for non-admins renders below
      await api.put(p(pid, 'config'), { version: project.version, thresholds: th })
      toast('Thresholds saved — audit event written (PEC-NFR-001)')
      refresh()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <form className="stack card" onSubmit={submit} style={{ maxWidth: 860 }}>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(230px, 1fr))', gap: '.5rem .8rem' }}>
        {THRESHOLD_KEYS.map(([k, label]) => (
          <label key={k}>{label}
            <input type="number" value={th[k] ?? 0}
              onChange={(e) => setTh({ ...th, [k]: Number(e.target.value) })} />
          </label>
        ))}
      </div>
      <ErrorBox error={error} />
      <div>
        <button className="btn" disabled={busy}>Save thresholds</button>
      </div>
      <p className="section-note" style={{ margin: 0 }}>
        Config changes write an audit event (PEC-NFR-001). Signals recompute on read from
        these values — derived status is never stored (I-4). Warn-tier breaches floor
        project health at amber; escalate-tier breaches make it red (§6.3).
      </p>
    </form>
  )
}

// ================================================================ people

function PeopleSection(): JSX.Element {
  const { people } = useApp()
  return (
    <div>
      <h2>People &amp; roles</h2>
      <table className="reg" style={{ maxWidth: 640 }}>
        <thead><tr><th>Name</th><th>Email</th><th>Discipline</th></tr></thead>
        <tbody>
          {people.map((pp) => (
            <tr key={pp.id}>
              <td>{pp.name}</td>
              <td className="mono">{pp.email}</td>
              <td className="small">{pp.discipline ?? <span className="muted">—</span>}</td>
            </tr>
          ))}
          {people.length === 0 && <tr><td colSpan={3} className="muted small">no people</td></tr>}
        </tbody>
      </table>
      <p className="section-note">
        Firm directory, read-only here. Project role assignments are managed by an instance
        admin (SPEC §2.1); every role check is enforced server-side per route (PEC-NFR-005).
      </p>
    </div>
  )
}
