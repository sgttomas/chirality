/**
 * Disciplines — the live, drillable mirror of the weekly discipline status report
 * (D-PEC-40; findings §5). Read-only: an index of disciplines and a per-discipline
 * detail with the four report sections (Activities by deliverable kind · Issuances ·
 * Needs · Risks) plus a factual-or-absent metric band. Every tile drills (I-4);
 * % complete and undeclared-period tiles are absent and said to be absent.
 * Pure projection of the server view — no rules here (SPEC §1).
 */

import { Link, useNavigate, useParams, useSearchParams } from 'react-router-dom'
import { useState } from 'react'
import { api, p } from '../api.ts'
import { usePublishScreenContext } from '../agent/context.tsx'
import {
  Breadcrumb, ErrorBox, KpiCard, RecordRef, RegisterTable, StateTag, WorkflowStages, fmtDate,
  useApp, useLoad, usePerson,
} from '../shared.tsx'
import type { Col } from '../shared.tsx'

// ---------- index ----------

export function DisciplinesPage(): JSX.Element {
  const { pid } = useApp()
  const nav = useNavigate()
  const [search, setSearch] = useState('')
  const { data, error } = useLoad<any[]>(() => api.get(p(pid, 'disciplines')), [pid])
  usePublishScreenContext([])

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>
  const query = search.trim().toLowerCase()
  const visible = data.filter((row) => !query || row.discipline.toLowerCase().includes(query))

  const cols: Array<Col<any>> = [
    { key: 'discipline', label: 'Discipline', render: (r) => <b>{r.discipline}</b>, csv: (r) => r.discipline },
    { key: 'deliverables', label: 'Deliverables', render: (r) => <span className="mono">{r.deliverables}</span>, csv: (r) => r.deliverables },
    { key: 'inWork', label: 'In work', render: (r) => <span className="mono">{r.inWork}</span>, csv: (r) => r.inWork },
    { key: 'issued', label: 'Issue events (recorded)', render: (r) => <span className="mono">{r.issueEvents}</span>, csv: (r) => r.issueEvents },
    { key: 'needs', label: 'Open needs', render: (r) => r.openNeeds > 0 ? <span className="badge amber">{r.openNeeds}</span> : <span className="muted">0</span>, csv: (r) => r.openNeeds },
    { key: 'risks', label: 'Open risks', render: (r) => r.openRisks > 0 ? <span className="badge amber">{r.openRisks}</span> : <span className="muted">0</span>, csv: (r) => r.openRisks },
  ]

  return (
    <div>
      <h1>Disciplines — the weekly report, live</h1>
      <p className="section-note">
        Each row mirrors the weekly discipline status story. Open a discipline to drill its
        activities, issuances, needs, and risks; declare a period there for period-scoped figures.
      </p>
      <div className="filters"><label>Find discipline<input type="search" value={search} onChange={(e) => setSearch(e.target.value)} placeholder="discipline name" /></label><span className="small muted">{visible.length} of {data.length}</span></div>
      <RegisterTable cols={cols} rows={visible}
        onRowClick={(r) => nav(`/p/${pid}/disciplines/${encodeURIComponent(r.discipline)}`)} />
    </div>
  )
}

// ---------- detail ----------

export function DisciplineDetailPage(): JSX.Element {
  const { pid } = useApp()
  const { name } = useParams()
  const person = usePerson()
  const [searchParams, setSearchParams] = useSearchParams()
  const start = searchParams.get('start') ?? ''
  const end = searchParams.get('end') ?? ''
  const [draftStart, setDraftStart] = useState(start)
  const [draftEnd, setDraftEnd] = useState(end)
  const discipline = name ?? ''
  const qs = start && end ? `?start=${start}&end=${end}` : ''
  const { data, error } = useLoad<any>(
    () => api.get(p(pid, `disciplines/${encodeURIComponent(discipline)}${qs}`)), [pid, discipline, qs])
  usePublishScreenContext(((data?.sections?.activities?.groups ?? []) as any[])
    .flatMap((g: any) => g.deliverables.map((d: any) => ({ recordType: 'deliverable', ref: d.docNo, id: d.id }))))

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const band = data.band as Record<string, { value: number; ruleId: string; detail: string; contributing: unknown[] }>

  const issuanceCols: Array<Col<any>> = [
    { key: 'ref', label: 'Issue ref', render: (r) => <RecordRef recordType="issue_event" id={r.id} recordRef={r.ref} />, csv: (r) => r.ref },
    { key: 'docNo', label: 'Deliverable', render: (r) => <Link to={`/p/${pid}/deliverables/${r.deliverableId}`} className="mono" onClick={(e) => e.stopPropagation()}>{r.docNo}</Link>, csv: (r) => r.docNo },
    { key: 'purpose', label: 'Purpose', render: (r) => <StateTag s={r.purpose} />, csv: (r) => r.purpose },
    { key: 'transmittal', label: 'Transmittal', render: (r) => <span className="mono small">{r.transmittalRef}</span>, csv: (r) => r.transmittalRef },
    { key: 'issuedAt', label: 'Issued', render: (r) => <span className="nowrap">{fmtDate(r.issuedAt)}</span>, csv: (r) => r.issuedAt },
  ]

  const needCols: Array<Col<any>> = [
    { key: 'type', label: 'Type', render: (r) => <span className={`itype itype-${r.type}`}>{r.type}</span>, csv: (r) => r.type },
    { key: 'ref', label: 'Ref', render: (r) => <RecordRef recordType={r.recordType} id={r.id} recordRef={r.ref} />, csv: (r) => r.ref },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'owner', label: 'Owner', render: (r) => <span className="small">{r.ownerId != null ? person(r.ownerId) : '—'}</span>, csv: (r) => r.ownerId != null ? person(r.ownerId) : '' },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}{r.overdue && <span className="badge red" style={{ marginLeft: '.35rem' }}>overdue</span>}</span>, csv: (r) => r.needBy },
    { key: 'age', label: 'Age', render: (r) => <span className="mono">{r.ageWd} wd</span>, csv: (r) => r.ageWd },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} />, csv: (r) => r.state },
  ]

  const riskCols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <RecordRef recordType="risk" id={r.id} recordRef={r.ref} />, csv: (r) => r.ref },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'score', label: 'Score', render: (r) => r.probability != null && r.impact != null ? <span className="mono">P{r.probability}×I{r.impact}</span> : <span className="muted small">score absent</span>, csv: (r) => r.probability != null && r.impact != null ? `P${r.probability}xI${r.impact}` : '' },
    { key: 'owner', label: 'Owner', render: (r) => <span className="small">{r.ownerId != null ? person(r.ownerId) : '—'}</span>, csv: (r) => r.ownerId != null ? person(r.ownerId) : '' },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span>, csv: (r) => r.needBy },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} />, csv: (r) => r.state },
  ]

  const applyPeriod = (e: React.FormEvent) => {
    e.preventDefault()
    if (draftStart && draftEnd) setSearchParams({ start: draftStart, end: draftEnd })
  }
  const clearPeriod = () => {
    setDraftStart('')
    setDraftEnd('')
    setSearchParams({})
  }

  return (
    <div>
      <Breadcrumb items={[
        { label: 'Disciplines', to: `/p/${pid}/disciplines` },
        { label: discipline },
      ]} />
      <h1>{discipline} — discipline status</h1>

      <form className="row" onSubmit={applyPeriod} aria-label="Reporting period">
        <label>Period start<input type="date" value={draftStart} onChange={(e) => setDraftStart(e.target.value)} /></label>
        <label>Period end<input type="date" value={draftEnd} onChange={(e) => setDraftEnd(e.target.value)} /></label>
        <button className="btn" type="submit" disabled={!draftStart || !draftEnd}>Apply period</button>
        {data.period && <button className="btn secondary" type="button" onClick={clearPeriod}>Clear period</button>}
      </form>
      <p className="small muted">
        {data.period
          ? `Figures below are period-scoped to ${data.period.start}..${data.period.end} where marked.`
          : 'No period declared — period-scoped tiles are absent (D-PEC-39).'}
      </p>

      <div className="kpi-row">
        <KpiCard label="activities in work" value={band.activitiesInWork!.value} explain={band.activitiesInWork as any} />
        <KpiCard label="open needs" value={band.openNeeds!.value} explain={band.openNeeds as any} />
        <KpiCard label="oldest need (wd)" value={band.needsAging!.value} explain={band.needsAging as any} />
        <KpiCard label="open risks" value={band.openRisks!.value} explain={band.openRisks as any} />
        {band.percentComplete && <KpiCard label="% complete (attested)" value={`${band.percentComplete.value}%`} explain={band.percentComplete as any} />}
        {band.issuedInPeriod && <KpiCard label="issued this period" value={band.issuedInPeriod.value} explain={band.issuedInPeriod as any} />}
        {band.issuanceDelta && <KpiCard label="issuance delta" value={`${band.issuanceDelta.value >= 0 ? '+' : ''}${band.issuanceDelta.value}`} explain={band.issuanceDelta as any} />}
      </div>

      {data.absent.length > 0 && (
        <div className="card">
          <h2>Absent figures (factual-or-absent)</h2>
          <ul className="small">
            {data.absent.map((a: any) => (
              <li key={a.figure}><b>{a.figure}</b> — {a.reason} <span className="muted">(needs: {a.needed})</span></li>
            ))}
          </ul>
        </div>
      )}

      <h2>Activities <span className="muted small">({data.sections.activities.basis})</span></h2>
      {(data.sections.activities.groups as any[]).length === 0 && <p className="muted">No in-work deliverables in this discipline.</p>}
      {(data.sections.activities.groups as any[]).map((g: any) => (
        <div key={g.type}>
          <h3 className="small">{g.type} <span className="muted">({g.deliverables.length})</span></h3>
          <RegisterTable
            cols={[
              { key: 'docNo', label: 'Doc no', render: (r: any) => <Link to={`/p/${pid}/deliverables/${r.id}`} className="mono" onClick={(e) => e.stopPropagation()}>{r.docNo}</Link>, csv: (r: any) => r.docNo },
              { key: 'title', label: 'Title', render: (r: any) => r.title },
              { key: 'owner', label: 'Owner', render: (r: any) => <span className="small">{person(r.ownerId)}</span>, csv: (r: any) => person(r.ownerId) },
              { key: 'workflow', label: 'Workflow', render: (r: any) => <WorkflowStages workflow={r.workflow} />, csv: (r: any) => r.workflow.label },
              // D-PEC-45: PE-attested % (contract v2 import), display-only; markers verbatim
              { key: 'pct', label: '% complete', render: (r: any) => <span className="nowrap">{r.percentComplete != null ? `${r.percentComplete}%` : r.percentCompleteVerbatim ?? '—'}</span>, csv: (r: any) => r.percentComplete ?? r.percentCompleteVerbatim ?? '' },
              { key: 'due', label: 'Due', render: (r: any) => <span className="nowrap">{fmtDate(r.dueDate)}</span>, csv: (r: any) => r.dueDate },
            ] as Array<Col<any>>}
            rows={g.deliverables}
          />
        </div>
      ))}

      <h2>Issuances{data.period ? ` (${data.period.start}..${data.period.end})` : ' (all recorded)'} <span className="muted small">({data.sections.issuances.basis})</span></h2>
      {(data.sections.issuances.rows as any[]).length === 0
        ? <p className="muted">No recorded issue events{data.period ? ' in the declared period' : ''} for this discipline.</p>
        : <RegisterTable cols={issuanceCols} rows={data.sections.issuances.rows} />}

      <h2>Needs <span className="muted small">({data.sections.needs.basis})</span></h2>
      {(data.sections.needs.rows as any[]).length === 0
        ? <p className="muted">No open needs for this discipline.</p>
        : <RegisterTable cols={needCols} rows={data.sections.needs.rows} />}

      <h2>Risks <span className="muted small">({data.sections.risks.basis})</span></h2>
      {(data.sections.risks.rows as any[]).length === 0
        ? <p className="muted">No open discipline-attributed risks.</p>
        : <RegisterTable cols={riskCols} rows={data.sections.risks.rows} />}
    </div>
  )
}
