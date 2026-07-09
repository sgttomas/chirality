/**
 * Overview — "Is the project coherent?" (project reporting home, PRD §12.1).
 * KPIs with drill-down (PEC-OV-001/002), package rollup (PEC-OV-003),
 * Waiting-on-you split by threshold breach (PEC-OV-004, SPEC §6.5),
 * typed top blockers (PEC-OV-005), sponsor brief export (PEC-OV-006).
 */

import { Link, useNavigate } from 'react-router-dom'
import { api, p } from '../api.ts'
import type { Explain } from '../api.ts'
import {
  ErrorBox, HealthBadge, KpiCard, RecordRef, RegisterTable, fmtDate, refRoute, useApp,
  useExplain, useLoad, usePerson,
} from '../shared.tsx'
import type { Col } from '../shared.tsx'

/** Present a governance Signal (§8.4) through the shared explain drawer, mapping its level to a
 *  badge tone; the drawer's contributing rows are then click-through to source (I-4). */
function signalToExplain(s: any): Explain {
  return {
    value: s.level === 'red' ? 'red' : s.level === 'warn' ? 'amber' : 'green',
    ruleId: s.id,
    detail: s.detail,
    threshold: s.threshold,
    contributing: s.contributing,
  }
}

export function OverviewPage(): JSX.Element {
  const { pid } = useApp()
  const nav = useNavigate()
  const person = usePerson()
  const explain = useExplain()
  const { data, error } = useLoad(() => api.get(p(pid, 'overview')), [pid])

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const holdsTotal = Object.values(data.kpis.holdsByCause.value as Record<string, number>)
    .reduce((a, b) => a + b, 0)

  // navigate a row that carries its own record identity (recordType/id/ref) to its source
  const rowToSource = (r: any) => {
    const route = refRoute(pid, r.recordType, r.id, r.ref)
    if (route) nav(route)
  }

  const rollupCols: Array<Col<any>> = [
    { key: 'code', label: 'Package', render: (r) => <><b>{r.code}</b> <span className="muted small">{r.name}</span></> },
    { key: 'lead', label: 'Lead', render: (r) => <span className="small">{person(r.leadId)}</span> },
    { key: 'health', label: 'Health', render: (r) => <HealthBadge explain={r.health} label={`package ${r.code}`} /> },
    { key: 'onplan', label: 'On plan', render: (r) => <span className="mono">{r.onPlan}/{r.total}</span> },
    { key: 'issues', label: 'Open issues', render: (r) => r.openIssues > 0 ? <b>{r.openIssues}</b> : <span className="muted">0</span> },
    { key: 'holds', label: 'Holds', render: (r) => r.holds > 0 ? <span className="badge hold">{r.holds}</span> : <span className="muted">0</span> },
    { key: 'checks', label: 'Checks due', render: (r) => r.checksDue },
    { key: 'apprs', label: 'Approvals due', render: (r) => r.approvalsDue },
    { key: 'decs', label: 'Open decisions', render: (r) => r.openDecisions },
  ]

  const waitCols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <RecordRef recordType={r.recordType} id={r.id} recordRef={r.ref} /> },
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
        : <span className="small">{r.blocks.map((b: any, i: number) => {
          const route = refRoute(pid, b.recordType, b.id, b.ref)
          const label = `${b.recordType.replaceAll('_', ' ')} (${b.why})`
          return (
            <span key={i}>{i > 0 && '; '}{route
              ? <RecordRef recordType={b.recordType} id={b.id} recordRef={b.ref} label={label} />
              : label}</span>
          )
        })}</span>,
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
      </div>

      <div className="row" style={{ justifyContent: 'flex-end', marginTop: '.5rem' }}>
        <button className="btn secondary small" type="button"
          onClick={() => window.open(p(pid, 'reports/sponsor-brief'), '_blank')}
          title="print-friendly HTML; print to PDF (ADR-010)">
          Open sponsor brief
        </button>
      </div>

      <h2>Governance signals (§8.4)</h2>
      <div className="cards">
        {data.signals.map((s: any) => (
          <div key={s.id} className="card" style={{ minWidth: 180, cursor: 'pointer' }}
            title={`${s.id} — click to drill down to contributing records`}
            onClick={() => explain(s.label, signalToExplain(s))}>
            <span className={`badge ${s.level === 'red' ? 'red' : s.level === 'warn' ? 'amber' : 'green'}`}>
              {s.level === 'none' ? 'green' : s.level === 'warn' ? 'amber' : s.level}
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

      <h2>Schedule pressure — lookahead load vs capacity (PEC-OV-008)</h2>
      {data.schedulePressure.every((w: any) => w.loadH === 0 && w.capacityH === 0)
        ? <p className="muted small">No planned load or capacity yet — set both on the <Link to={`/p/${pid}/plan`}>Plan</Link> page.</p>
        : (
          <div className="cards">
            {data.schedulePressure.map((w: any) => (
              <Link key={w.week} to={`/p/${pid}/plan`} className="card" style={{ minWidth: 150, color: 'inherit' }}
                title="open the Plan page — load, capacity, and shifts by week">
                <b className="small">{w.week}</b>
                <div>{w.loadH} h / {w.capacityH} h</div>
                {w.pct != null
                  ? <span className={`badge ${w.level === 'red' ? 'red' : w.level === 'warn' ? 'amber' : 'green'}`}>{w.pct}%</span>
                  : <span className="muted small">no capacity baseline</span>}
                {w.breaches.map((b: any) => (
                  <div key={b.discipline} className="small muted">{b.discipline} {b.pct != null ? `${b.pct}%` : 'over'}</div>
                ))}
              </Link>
            ))}
          </div>
        )}

      <h2>Waiting on you</h2>
      {data.waitingOnYou.breaching.length === 0 && data.waitingOnYou.other.length === 0
        ? <p className="muted small">Nothing is waiting on your decision or signature.</p>
        : (
          <>
            {data.waitingOnYou.breaching.length > 0 && (
              <RegisterTable cols={waitCols} rows={data.waitingOnYou.breaching}
                onRowClick={rowToSource} />
            )}
            {data.waitingOnYou.other.length > 0 && (
              <details style={{ marginTop: '.5rem' }}>
                <summary className="small muted">
                  {data.waitingOnYou.other.length} more within thresholds (PEC-OV-004 shows breaches first)
                </summary>
                <RegisterTable cols={waitCols} rows={data.waitingOnYou.other}
                  onRowClick={rowToSource} />
              </details>
            )}
          </>
        )}

      <h2>Top blockers — typed by cause (PEC-OV-005)</h2>
      <RegisterTable
        exportName="top-blockers.csv"
        onRowClick={(r: any) => nav(refRoute(pid, 'hold', r.id, r.ref)!)}
        cols={[
          { key: 'ref', label: 'Hold', render: (r: any) => <RecordRef recordType="hold" id={r.id} recordRef={r.ref} /> },
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
        decisions, risks, interfaces, holds, Schedule, and Tracker</Link>.
      </p>
    </div>
  )
}
