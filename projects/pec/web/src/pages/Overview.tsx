/**
 * Overview — "Is the project coherent?" (Sponsor / PM home, PRD §12.1).
 * KPIs with drill-down (PEC-OV-001/002), package rollup (PEC-OV-003),
 * Waiting-on-you split by threshold breach (PEC-OV-004, SPEC §6.5),
 * typed top blockers (PEC-OV-005), sponsor brief export (PEC-OV-006).
 */

import { Link, useNavigate } from 'react-router-dom'
import { api, p } from '../api.ts'
import {
  ErrorBox, HealthBadge, KpiCard, RegisterTable, StateTag, fmtDate, useApp, useLoad, usePerson,
} from '../shared.tsx'
import type { Col } from '../shared.tsx'

export function OverviewPage(): JSX.Element {
  const { pid } = useApp()
  const nav = useNavigate()
  const person = usePerson()
  const { data, error } = useLoad(() => api.get(p(pid, 'overview')), [pid])

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const holdsTotal = Object.values(data.kpis.holdsByCause.value as Record<string, number>)
    .reduce((a, b) => a + b, 0)

  const rollupCols: Array<Col<any>> = [
    { key: 'code', label: 'Package', render: (r) => <><b>{r.code}</b> <span className="muted small">{r.name}</span></> },
    { key: 'lead', label: 'Lead', render: (r) => <span className="small">{person(r.leadId)}</span> },
    { key: 'health', label: 'Health', render: (r) => <HealthBadge explain={r.health} label={`package ${r.code}`} /> },
    { key: 'onplan', label: 'On plan', render: (r) => <span className="mono">{r.onPlan}/{r.total}</span> },
    { key: 'holds', label: 'Holds', render: (r) => r.holds > 0 ? <span className="badge hold">{r.holds}</span> : <span className="muted">0</span> },
    { key: 'checks', label: 'Checks due', render: (r) => r.checksDue },
    { key: 'apprs', label: 'Approvals due', render: (r) => r.approvalsDue },
    { key: 'decs', label: 'Open decisions', render: (r) => r.openDecisions },
  ]

  const waitCols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span> },
    { key: 'kind', label: 'Kind', render: (r) => r.kind },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
    { key: 'age', label: 'Age (wd)', render: (r) => r.ageWd },
    {
      key: 'breach', label: 'Breach', render: (r) =>
        r.breach === 'none' ? <span className="muted small">within threshold</span> : <span className={`badge ${r.breach === 'red' ? 'red' : 'amber'}`}>{r.breach}</span>,
    },
    {
      key: 'blocks', label: 'Blocks', render: (r) => r.blocks.length === 0
        ? <span className="muted small">—</span>
        : <span className="small">{r.blocks.map((b: any) => `${b.recordType.replaceAll('_', ' ')} (${b.why})`).join('; ')}</span>,
    },
  ]

  return (
    <div>
      <h1>
        Overview — is the project coherent?{' '}
        <HealthBadge explain={data.health} label="project health" />
      </h1>

      <div className="cards">
        <KpiCard label="deliverables on plan" value={`${data.kpis.pctOnPlan.value}%`} explain={data.kpis.pctOnPlan} />
        <KpiCard label="active holds" value={holdsTotal} explain={data.kpis.holdsByCause} />
        <KpiCard label="open decisions" value={data.kpis.openDecisions.value} explain={data.kpis.openDecisions} />
        <KpiCard label="approvals in flight" value={data.kpis.approvalsInFlight.value} explain={data.kpis.approvalsInFlight} />
        <KpiCard label="worst forecast slip (wd)" value={data.kpis.scheduleForecastWd.value} explain={data.kpis.scheduleForecastWd} />
        <div className="card kpi" onClick={() => window.open(p(pid, 'reports/sponsor-brief'), '_blank')} title="print-friendly HTML; print to PDF (ADR-010)">
          <b>⎙</b><span>sponsor brief</span>
        </div>
      </div>

      <h2>Governance signals (§8.4)</h2>
      <div className="cards">
        {data.signals.map((s: any) => (
          <div key={s.id} className="card" style={{ minWidth: 180 }}>
            <span className={`badge ${s.level === 'red' ? 'red' : s.level === 'warn' ? 'amber' : 'green'}`}>
              {s.level === 'none' ? 'ok' : s.level}
            </span>{' '}
            <b className="small">{s.label}</b>
            <div className="small muted">{s.detail}</div>
            <div className="small muted">{s.threshold}</div>
          </div>
        ))}
      </div>

      <h2>Package rollup</h2>
      <RegisterTable cols={rollupCols} rows={data.packageRollup} exportName="package-rollup.csv"
        onRowClick={(r) => nav(`/p/${pid}/packages/${r.id}`)} />

      <h2>Waiting on you</h2>
      {data.waitingOnYou.breaching.length === 0 && data.waitingOnYou.other.length === 0
        ? <p className="muted small">Nothing is waiting on your decision or signature.</p>
        : (
          <>
            {data.waitingOnYou.breaching.length > 0 && (
              <RegisterTable cols={waitCols} rows={data.waitingOnYou.breaching} />
            )}
            {data.waitingOnYou.other.length > 0 && (
              <details style={{ marginTop: '.5rem' }}>
                <summary className="small muted">
                  {data.waitingOnYou.other.length} more within thresholds (PEC-OV-004 shows breaches first)
                </summary>
                <RegisterTable cols={waitCols} rows={data.waitingOnYou.other} />
              </details>
            )}
          </>
        )}

      <h2>Top blockers — typed by cause (PEC-OV-005)</h2>
      <RegisterTable
        exportName="top-blockers.csv"
        cols={[
          { key: 'ref', label: 'Hold', render: (r: any) => <span className="mono">{r.ref}</span> },
          { key: 'cause', label: 'Cause', render: (r: any) => <span className="badge hold">{r.cause.replaceAll('_', ' ')}</span> },
          { key: 'title', label: 'Title', render: (r: any) => r.title },
          { key: 'owner', label: 'Owner', render: (r: any) => person(r.ownerId) },
          { key: 'needBy', label: 'Need by', render: (r: any) => fmtDate(r.needBy) },
          { key: 'age', label: 'Age (wd)', render: (r: any) => r.ageWd },
          { key: 'blocks', label: 'Blocks', render: (r: any) => `${r.blocks} record(s)` },
        ]}
        rows={data.topBlockers}
      />
      <p className="section-note">
        Every value on this page drills down to its contributing records and the rule that
        classified it — click any badge or KPI (I-4). Registers: <Link to={`/p/${pid}/registers`}>approvals,
        decisions, risks, interfaces, intake</Link>.
      </p>
    </div>
  )
}
