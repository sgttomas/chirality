/**
 * Packages — "How is my scope?" (Package Lead home, PRD §12.2).
 * Register with health per package (PEC-PKG-001), detail with summary (PEC-PKG-002),
 * needs-the-lead-this-week (PEC-PKG-005), deliverables by nearest commitment (PEC-PKG-004),
 * package decisions (PEC-PKG-006), interface items (PEC-PKG-007).
 * Pure projection of packageDetailView — no rules here (SPEC §1).
 */

import { Link, useNavigate, useParams } from 'react-router-dom'
import { api, p } from '../api.ts'
import {
  ErrorBox, HealthBadge, RegisterTable, StateTag, fmtDate, useApp, useLoad, usePerson,
} from '../shared.tsx'
import type { Col } from '../shared.tsx'

// ---------- register (PEC-PKG-001) ----------

export function PackagesPage(): JSX.Element {
  const { pid } = useApp()
  const nav = useNavigate()
  const person = usePerson()
  const { data, error } = useLoad<any[]>(() => api.get(p(pid, 'packages')), [pid])

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const cols: Array<Col<any>> = [
    { key: 'code', label: 'Package', render: (r) => <><b>{r.code}</b> <span className="muted small">{r.name}</span></>, csv: (r) => `${r.code} ${r.name}` },
    { key: 'lead', label: 'Lead', render: (r) => <span className="small">{person(r.leadId)}</span>, csv: (r) => person(r.leadId) },
    { key: 'milestone', label: 'Milestone', render: (r) => r.milestone ?? <span className="muted">—</span>, csv: (r) => r.milestone },
    { key: 'health', label: 'Health', render: (r) => <HealthBadge explain={r.health} label={`package ${r.code}`} />, csv: (r) => String(r.health.value) },
    { key: 'onplan', label: 'On plan', render: (r) => <span className="mono">{r.onPlan}/{r.total}</span>, csv: (r) => `${r.onPlan}/${r.total}` },
  ]

  return (
    <div>
      <h1>Packages — how is my scope?</h1>
      {/* PEC-PKG-001: every package with derived health, click-to-explain (I-4) */}
      <RegisterTable cols={cols} rows={data} exportName="packages.csv"
        onRowClick={(r) => nav(`/p/${pid}/packages/${r.id}`)} />
    </div>
  )
}

// ---------- detail (PEC-PKG-002..007) ----------

const NEED_KIND_LABEL: Record<string, string> = {
  sign_off_due: 'sign-off due',
  decision_to_rule: 'decision to rule',
  hold_to_resolve: 'hold to resolve',
  interface_obligation: 'interface obligation',
}

export function PackageDetailPage(): JSX.Element {
  const { pid } = useApp()
  const { id } = useParams()
  const person = usePerson()
  const nav = useNavigate()
  const { data, error } = useLoad<any>(() => api.get(p(pid, 'packages/' + id)), [pid, id])

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const pkg = data.package
  const holdsByCause = Object.entries(data.summary.holdsByCause as Record<string, number>)

  // "Needs the lead this week" (PEC-PKG-005)
  const needsCols: Array<Col<any>> = [
    { key: 'kind', label: 'What', render: (r) => NEED_KIND_LABEL[r.kind] ?? r.kind, csv: (r) => NEED_KIND_LABEL[r.kind] ?? r.kind },
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span>, csv: (r) => r.ref },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'due', label: 'Due', render: (r) => <span className="nowrap">{fmtDate(r.due)}</span>, csv: (r) => r.due },
  ]

  // Deliverables ordered by nearest commitment — server sorts (PEC-PKG-004)
  const delCols: Array<Col<any>> = [
    { key: 'docNo', label: 'Doc no', render: (r) => <Link to={`/p/${pid}/deliverables/${r.id}`} className="mono" onClick={(e) => e.stopPropagation()}>{r.docNo}</Link>, csv: (r) => r.docNo },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'owner', label: 'Owner', render: (r) => <span className="small">{person(r.ownerId)}</span>, csv: (r) => person(r.ownerId) },
    { key: 'rev', label: 'Rev / state', render: (r) => <><span className="mono">{r.revCode ?? '—'}</span> <StateTag s={r.state} /></>, csv: (r) => `${r.revCode ?? ''} ${r.state}` },
    { key: 'due', label: 'Due', render: (r) => <span className="nowrap">{fmtDate(r.dueDate)}</span>, csv: (r) => r.dueDate },
    { key: 'milestone', label: 'Milestone', render: (r) => r.milestone ?? <span className="muted">—</span>, csv: (r) => r.milestone },
    { key: 'health', label: 'Health', render: (r) => <HealthBadge explain={r.health} label={r.docNo} />, csv: (r) => String(r.health.value) },
    { key: 'open', label: 'Open items', render: (r) => r.openItems, csv: (r) => r.openItems },
    { key: 'holds', label: 'Holds', render: (r) => r.holds > 0 ? <span className="badge hold">{r.holds}</span> : <span className="muted">0</span>, csv: (r) => r.holds },
    { key: 'slip', label: 'Slip (wd)', render: (r) => r.forecastSlipWd > 0 ? <span className={`badge ${r.forecastSlipWd > 5 ? 'red' : 'amber'}`}>{r.forecastSlipWd}</span> : <span className="muted">0</span>, csv: (r) => r.forecastSlipWd },
  ]

  // Package decisions (PEC-PKG-006)
  const decCols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span>, csv: (r) => r.ref },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} />, csv: (r) => r.state },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span>, csv: (r) => r.needBy },
    { key: 'overdue', label: 'Overdue', render: (r) => r.overdueDays > 0 ? <span className="badge red">{r.overdueDays} d</span> : <span className="muted small">—</span>, csv: (r) => r.overdueDays },
    { key: 'affected', label: 'Affected', render: (r) => `${r.affected} record(s)`, csv: (r) => r.affected },
  ]

  // Interface items (PEC-PKG-007)
  const intCols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span>, csv: (r) => r.ref },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'parties', label: 'Giving → receiving', render: (r) => <span className="small">{r.giving} → {r.receiving}</span>, csv: (r) => `${r.giving} → ${r.receiving}` },
    { key: 'info', label: 'Required info', render: (r) => <span className="small">{r.requiredInfo ?? '—'}</span>, csv: (r) => r.requiredInfo },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span>, csv: (r) => r.needBy },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} />, csv: (r) => r.state },
  ]

  return (
    <div>
      <h1>
        <span className="mono">{pkg.code}</span> {pkg.name}{' '}
        <span className="muted small">lead {person(pkg.leadId)}</span>{' '}
        <HealthBadge explain={data.health} label={`package ${pkg.code}`} />
      </h1>

      {/* Summary: on-plan, holds by cause, open interfaces, open decisions (PEC-PKG-002) */}
      <div className="cards">
        <div className="card kpi" style={{ cursor: 'default' }}>
          <b>{data.summary.deliverablesOnPlan}</b>
          <span>deliverables on plan</span>
        </div>
        <div className="card kpi" style={{ cursor: 'default' }}>
          <b>{holdsByCause.reduce((a, [, n]) => a + n, 0)}</b>
          <span>active holds</span>
          <div style={{ marginTop: '.25rem' }}>
            {holdsByCause.length === 0
              ? <span className="muted small">none</span>
              : holdsByCause.map(([cause, n]) => (
                <span key={cause} className="badge hold" style={{ marginRight: '.25rem' }}>
                  {cause.replaceAll('_', ' ')} {n}
                </span>
              ))}
          </div>
        </div>
        <div className="card kpi" style={{ cursor: 'default' }}>
          <b>{data.summary.openInterfaces}</b>
          <span>open interfaces</span>
        </div>
        <div className="card kpi" style={{ cursor: 'default' }}>
          <b>{data.summary.openDecisions}</b>
          <span>open decisions</span>
        </div>
      </div>

      {/* PEC-PKG-005 */}
      <h2>Needs the lead this week</h2>
      {data.needsLead.length === 0
        ? <p className="muted small">Nothing needs the lead this week.</p>
        : <RegisterTable cols={needsCols} rows={data.needsLead} exportName={`${pkg.code}-needs-lead.csv`} />}

      {/* PEC-PKG-004: server-ordered by nearest commitment */}
      <h2>Deliverables — by nearest commitment</h2>
      <RegisterTable cols={delCols} rows={data.deliverables} exportName={`${pkg.code}-deliverables.csv`}
        onRowClick={(r) => nav(`/p/${pid}/deliverables/${r.id}`)} />

      {/* PEC-PKG-006 */}
      <h2>Package decisions</h2>
      <RegisterTable cols={decCols} rows={data.decisions} exportName={`${pkg.code}-decisions.csv`} />

      {/* PEC-PKG-007 */}
      <h2>Interface items</h2>
      <RegisterTable cols={intCols} rows={data.interfaces} exportName={`${pkg.code}-interfaces.csv`} />

      <p className="section-note">
        Health and ordering are server-derived with explanations (I-4) — click any badge for the
        rule and contributing records. Each table exports exactly what is displayed.
      </p>
    </div>
  )
}
