/**
 * Packages — "What's stuck in my scope?" (Package Lead home, PRD §12.2).
 * The package is where ISSUES live: holds, interfaces, decisions, risks, and rolled-up
 * action items (deliverable tasks stay on the Deliverables page as workflow status).
 * Register with health + open-issue count (PEC-PKG-001); detail leads with the issues cockpit
 * (PEC-PKG-002/006/007), then the lead's action queue (PEC-PKG-005), then deliverables carrying
 * their workflow status (PEC-PKG-004). Pure projection of the server view — no rules here (SPEC §1).
 */

import { Link, useNavigate, useParams } from 'react-router-dom'
import { useState } from 'react'
import { api, p } from '../api.ts'
import { usePublishScreenContext } from '../agent/context.tsx'
import {
  Breadcrumb, ErrorBox, HealthBadge, RecordRef, RegisterTable, StateTag, WorkflowStages, fmtDate,
  useApp, useLoad, usePerson,
} from '../shared.tsx'
import type { Col } from '../shared.tsx'

// ---------- register (PEC-PKG-001) ----------

export function PackagesPage(): JSX.Element {
  const { pid } = useApp()
  const nav = useNavigate()
  const person = usePerson()
  const { data, error } = useLoad<any[]>(() => api.get(p(pid, 'packages')), [pid])
  // D-PEC-20 item 4: publish visible record ids (route + ids only, rider 5)
  usePublishScreenContext((data ?? []).map((r: any) => ({ recordType: 'package', ref: r.code, id: r.id })))

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const cols: Array<Col<any>> = [
    { key: 'code', label: 'Package', render: (r) => <><b>{r.code}</b> <span className="muted small">{r.name}</span></>, csv: (r) => `${r.code} ${r.name}` },
    { key: 'area', label: 'Area', render: (r) => r.area ?? <span className="muted">—</span>, csv: (r) => r.area },
    { key: 'type', label: 'Type', render: (r) => r.packageType ?? <span className="muted">—</span>, csv: (r) => r.packageType },
    { key: 'lead', label: 'Lead', render: (r) => <span className="small">{person(r.leadId)}</span>, csv: (r) => person(r.leadId) },
    { key: 'milestone', label: 'Milestone', render: (r) => r.milestone ?? <span className="muted">—</span>, csv: (r) => r.milestone },
    { key: 'health', label: 'Health', render: (r) => <HealthBadge explain={r.health} label={`package ${r.code}`} />, csv: (r) => String(r.health.value) },
    { key: 'issues', label: 'Open issues', render: (r) => r.openIssues > 0 ? <span className="badge amber">{r.openIssues}</span> : <span className="muted">0</span>, csv: (r) => r.openIssues },
    {
      key: 'mix', label: 'Issue mix', render: (r) => (
        <span className="small">
          {Object.entries(r.issueMix?.value?.byType ?? {}).filter(([, n]) => Number(n) > 0).map(([k, n]) => (
            <span key={k} className={`itype itype-${k}`} style={{ marginRight: '.2rem' }}>{k} {String(n)}</span>
          ))}
          {r.issueMix?.value?.worst && <span className="muted"> worst {r.issueMix.value.worst.ref}</span>}
        </span>
      ),
    },
    { key: 'onplan', label: 'On plan', render: (r) => <span className="mono">{r.onPlan}/{r.total}</span>, csv: (r) => `${r.onPlan}/${r.total}` },
  ]

  return (
    <div>
      <h1>Packages — what needs a call in my scope?</h1>
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

const ISSUE_LABEL: Record<string, string> = {
  hold: 'hold', interface: 'interface', decision: 'decision', risk: 'risk', action: 'action',
}

export function PackageDetailPage(): JSX.Element {
  const { pid } = useApp()
  const { id } = useParams()
  const person = usePerson()
  const nav = useNavigate()
  const [issueFilter, setIssueFilter] = useState('')
  const { data, error } = useLoad<any>(() => api.get(p(pid, 'packages/' + id)), [pid, id])

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const pkg = data.package
  const s = data.summary
  const holdsByCause = Object.entries(s.holdsByCause as Record<string, number>)
  const issues = issueFilter ? data.issues.filter((r: any) => r.type === issueFilter) : data.issues

  // The issues cockpit (PEC-PKG-002/006/007): every open issue, urgency-first.
  const issueCols: Array<Col<any>> = [
    { key: 'type', label: 'Type', render: (r) => <span className={`itype itype-${r.type}`}>{ISSUE_LABEL[r.type] ?? r.type}</span>, csv: (r) => r.type },
    { key: 'ref', label: 'Ref', render: (r) => <RecordRef recordType={r.recordType} id={r.id} recordRef={r.ref} />, csv: (r) => r.ref },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'detail', label: 'Detail', render: (r) => <span className="small muted">{r.detail}</span>, csv: (r) => r.detail },
    { key: 'owner', label: 'Owner', render: (r) => <span className="small">{r.ownerId != null ? person(r.ownerId) : '—'}</span>, csv: (r) => r.ownerId != null ? person(r.ownerId) : '' },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}{r.overdue && <span className="badge red" style={{ marginLeft: '.35rem' }}>overdue</span>}</span>, csv: (r) => r.needBy },
    {
      key: 'basis', label: 'Age / need-by basis',
      render: (r) => r.ageWd != null
        ? <span className="mono">{r.ageWd} wd old</span>
        : r.overdueWd != null
          ? <span className={r.overdueWd > 0 ? 'badge amber' : 'mono'}>{r.overdueWd} wd overdue</span>
          : <span className="muted small">—</span>,
      csv: (r) => r.ageWd != null ? `${r.ageWd} wd old` : r.overdueWd != null ? `${r.overdueWd} wd overdue` : '',
    },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} />, csv: (r) => r.state },
  ]

  // "Needs the lead this week" (PEC-PKG-005)
  const needsCols: Array<Col<any>> = [
    { key: 'kind', label: 'What', render: (r) => NEED_KIND_LABEL[r.kind] ?? r.kind, csv: (r) => NEED_KIND_LABEL[r.kind] ?? r.kind },
    { key: 'ref', label: 'Ref', render: (r) => <RecordRef recordType={r.recordType} id={r.id} recordRef={r.ref} />, csv: (r) => r.ref },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'due', label: 'Due', render: (r) => <span className="nowrap">{fmtDate(r.due)}</span>, csv: (r) => r.due },
  ]

  // Deliverables — WORKFLOW status (not issues), by nearest commitment (PEC-PKG-004)
  const delCols: Array<Col<any>> = [
    { key: 'docNo', label: 'Doc no', render: (r) => <Link to={`/p/${pid}/deliverables/${r.id}`} className="mono" onClick={(e) => e.stopPropagation()}>{r.docNo}</Link>, csv: (r) => r.docNo },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'owner', label: 'Owner', render: (r) => <span className="small">{person(r.ownerId)}</span>, csv: (r) => person(r.ownerId) },
    { key: 'status', label: 'Status (workflow)', render: (r) => <WorkflowStages workflow={r.workflow} />, csv: (r) => `${r.workflow.label} (${r.workflow.gatesClosed}/${r.workflow.gatesTotal})` },
    { key: 'due', label: 'Due', render: (r) => <span className="nowrap">{fmtDate(r.dueDate)}</span>, csv: (r) => r.dueDate },
    { key: 'milestone', label: 'Milestone', render: (r) => r.milestone ?? <span className="muted">—</span>, csv: (r) => r.milestone },
  ]

  return (
    <div>
      <Breadcrumb items={[
        { label: 'Packages', to: `/p/${pid}/packages` },
        { label: pkg.code },
      ]} />
      <h1>
        <span className="mono">{pkg.code}</span> {pkg.name}{' '}
        <span className="muted small">lead {person(pkg.leadId)}</span>{' '}
        <HealthBadge explain={data.health} label={`package ${pkg.code}`} />{' '}
        <button className="btn secondary small" title="print-friendly HTML; print to PDF (ADR-010)"
          onClick={() => window.open(p(pid, `reports/package-pack/${pkg.id}`), '_blank')}>
          ⎙ weekly review pack
        </button>
      </h1>

      {/* Summary: issues first — this is an issue-management view (PEC-PKG-002) */}
      <div className="cards">
        <div className="card kpi" style={{ cursor: 'default' }}>
          <b>{s.openIssues}</b>
          <span>open issues{s.overdueIssues > 0 && <> · <span className="badge red">{s.overdueIssues} overdue</span></>}</span>
          <div className="small muted" style={{ marginTop: '.25rem' }}>
            {s.openHolds} holds · {s.openInterfaces} interfaces · {s.openDecisions} decisions · {s.openRisks} risks · {s.openActionItems} actions
          </div>
          <div style={{ marginTop: '.35rem' }}>
            {Object.entries(s.issueMix.value.byType).filter(([, n]) => Number(n) > 0).map(([k, n]) => (
              <button key={k} className={`itype itype-${k}`} style={{ marginRight: '.25rem', border: 'none', cursor: 'pointer' }}
                onClick={() => setIssueFilter(issueFilter === k ? '' : k)}>
                {k} {String(n)}
              </button>
            ))}
          </div>
        </div>
        <div className="card kpi" style={{ cursor: 'default' }}>
          <b>{s.openHolds}</b>
          <span>active holds</span>
          <div style={{ marginTop: '.25rem' }}>
            {holdsByCause.length === 0
              ? <span className="muted small">none</span>
              : holdsByCause.map(([cause, n]) => (
                <span key={cause} className="badge hold" style={{ marginRight: '.25rem' }}>{cause.replaceAll('_', ' ')} {n}</span>
              ))}
          </div>
        </div>
        <div className="card kpi" style={{ cursor: 'default' }}>
          <b>{s.deliverablesOnPlan}</b>
          <span>deliverables on plan</span>
        </div>
        {/* PEC-PKG-003 (P2): this package's discipline load for the current planning period */}
        <div className="card kpi" style={{ cursor: 'default' }}>
          <b>{data.capacity.rows.reduce((a: number, r: any) => a + r.packageLoadH, 0)} h</b>
          <span>planned load {data.capacity.week}</span>
          <div style={{ marginTop: '.25rem' }}>
            {data.capacity.rows.length === 0
              ? <span className="muted small">no planned load</span>
              : data.capacity.rows.map((r: any) => (
                <span key={r.discipline}
                  className={`badge ${r.level === 'red' ? 'red' : r.level === 'warn' ? 'amber' : 'plain'}`}
                  style={{ marginRight: '.25rem' }}
                  title={`${r.discipline}: package ${r.packageLoadH} h of ${r.disciplineLoadH} h discipline load, capacity ${r.capacityH ?? '—'} h`}>
                  {r.discipline} {r.pct != null ? `${r.pct}%` : `${r.packageLoadH} h`}
                </span>
              ))}
          </div>
        </div>
      </div>

      {/* The cockpit: every open issue, urgency-first */}
      <h2>Open issues</h2>
      {issueFilter && <p className="section-note">Filtered to {issueFilter}. <button className="btn secondary small" onClick={() => setIssueFilter('')}>clear</button></p>}
      {issues.length === 0
        ? <p className="muted small">No open issues in this package.</p>
        : <RegisterTable cols={issueCols} rows={issues} exportName={`${pkg.code}-issues.csv`} />}

      {/* PEC-PKG-005: the lead's personal action queue */}
      <h2>Needs the lead this week</h2>
      {data.needsLead.length === 0
        ? <p className="muted small">Nothing needs the lead this week.</p>
        : <RegisterTable cols={needsCols} rows={data.needsLead} exportName={`${pkg.code}-needs-lead.csv`} />}

      {/* PEC-PKG-004: deliverables carry WORKFLOW status here; drill in for their tied issues */}
      <details style={{ marginTop: '1rem' }}>
        <summary style={{ cursor: 'pointer' }}>
          <b>Deliverables — workflow status</b>{' '}
          <span className="muted small">({data.deliverables.length}) · status is production-workflow progress; issues are above</span>
        </summary>
        <div style={{ marginTop: '.5rem' }}>
          <RegisterTable cols={delCols} rows={data.deliverables} exportName={`${pkg.code}-deliverables.csv`}
            onRowClick={(r) => nav(`/p/${pid}/deliverables/${r.id}`)} />
        </div>
      </details>

      <p className="section-note">
        Issues (holds, interfaces, decisions, risks, action items) are tracked at the package level.
        Deliverable status is workflow completeness — the gates a document has closed — shown on the
        Deliverables page. Health and ordering are server-derived (I-4); each table exports what is displayed.
      </p>
    </div>
  )
}
