/**
 * Deliverables — the Engineer-of-Record home (PRD §12.3, deepest screen).
 * MDL register with filters (PEC-DEL-001); detail with distinct facts (PEC-DEL-009, I-6),
 * "before this issues" (PEC-DEL-004), open items across record types (PEC-DEL-003),
 * inline checking (PRD §12.8, PEC-CHK-003), revision chain + issue events
 * (PEC-DEL-006/008, PEC-ARC-002), one evidence/history stream (PEC-DEL-005).
 * No business rules here: the server decides every guard; we render its answers (SPEC §1).
 */

import { useEffect, useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import { api, p } from '../api.ts'
import { usePublishScreenContext } from '../agent/context.tsx'
import {
  Breadcrumb, ConditionsPanel, Drawer, ErrorBox, HistoryTrail, RecordRef, RegisterTable, ResizableTable, StateTag,
  WorkflowStages, fmtDate, useApp, useLoad, usePerson,
} from '../shared.tsx'
import type { Col } from '../shared.tsx'

const REVISION_STATES = [
  'in_work', 'in_check', 'check_accepted', 'ready_for_approval',
  'approved', 'issued', 'returned_with_comments', 'superseded',
]
const WORK_ITEM_KINDS = ['action', 'coordination', 'risk_treatment', 'rework', 'other']
const EVIDENCE_KINDS = ['attachment', 'markup', 'comment_sheet', 'transmittal', 'link', 'note']

// ---------- register (PEC-DEL-001) ----------

export function DeliverablesPage(): JSX.Element {
  const { pid } = useApp()
  const nav = useNavigate()
  const person = usePerson()
  const [pkgF, setPkgF] = useState('')
  const [discF, setDiscF] = useState('')
  const [areaF, setAreaF] = useState('')
  const [stateF, setStateF] = useState('')
  const [viewF, setViewF] = useState('active')
  const [searchF, setSearchF] = useState('')

  const { data: pkgs } = useLoad<any[]>(() => api.get(p(pid, 'packages')), [pid])

  // PEC-DEL-001: MDL views — filter server-side; render what comes back
  const qs = new URLSearchParams()
  if (pkgF) qs.set('package', pkgF)
  if (discF) qs.set('discipline', discF)
  if (areaF) qs.set('area', areaF)
  if (stateF) qs.set('state', stateF)
  qs.set('view', viewF)
  const { data, error } = useLoad<any[]>(
    () => api.get(p(pid, `deliverables?${qs.toString()}`)),
    [pid, pkgF, discF, areaF, stateF, viewF],
  )
  // D-PEC-20 item 4: publish visible record ids (route + ids only, rider 5)
  usePublishScreenContext((data ?? []).map((r: any) => ({ recordType: 'deliverable', ref: r.docNo, id: r.id })))

  const pkgCode = (id: number | null) =>
    pkgs?.find((x: any) => x.id === id)?.code ?? (id != null ? `#${id}` : '—')
  const query = searchF.trim().toLowerCase()
  const visible = (data ?? []).filter((row) => !query || `${row.docNo} ${row.title} ${row.discipline ?? ''} ${row.area ?? ''}`.toLowerCase().includes(query))

  // Status = workflow completeness (which gates are closed). Issues live at the package level.
  const cols: Array<Col<any>> = [
    { key: 'docNo', label: 'Doc no', render: (r) => <Link className="mono" to={`/p/${pid}/deliverables/${r.id}`}>{r.docNo}</Link>, csv: (r) => r.docNo },
    { key: 'title', label: 'Title', render: (r) => r.title },
    {
      key: 'pkg', label: 'Package', render: (r) => r.packageId
        ? <Link className="mono" to={`/p/${pid}/packages/${r.packageId}`} onClick={(e) => e.stopPropagation()}>{pkgCode(r.packageId)}</Link>
        : <span className="muted">—</span>,
    },
    { key: 'area', label: 'Area', render: (r) => r.area ?? '—' },
    { key: 'disc', label: 'Discipline', render: (r) => r.discipline ?? '—' },
    { key: 'type', label: 'Type', render: (r) => r.deliverableType ?? '—' },
    { key: 'owner', label: 'Owner', render: (r) => <span className="small">{person(r.ownerId)}</span> },
    { key: 'rev', label: 'Rev', render: (r) => <span className="mono">{r.revCode ?? '—'}</span>, csv: (r) => r.revCode ?? '' },
    { key: 'status', label: 'Status (workflow)', render: (r) => <WorkflowStages workflow={r.workflow} />, csv: (r) => `${r.workflow.label} (${r.workflow.gatesClosed}/${r.workflow.gatesTotal})` },
    // D-PEC-45: PE-attested % (contract v2 import), display-only; markers verbatim; blank when unattested
    { key: 'pct', label: '% complete', render: (r) => <span className="nowrap">{r.percentComplete != null ? `${r.percentComplete}%` : r.percentCompleteVerbatim ?? '—'}</span>, csv: (r) => r.percentComplete ?? r.percentCompleteVerbatim ?? '' },
    { key: 'due', label: 'Due', render: (r) => <span className="nowrap">{fmtDate(r.dueDate)}</span> },
    { key: 'milestone', label: 'Milestone', render: (r) => r.milestone ?? '—' },
  ]

  return (
    <div>
      <h1>Deliverables — the master deliverable list</h1>
      <div className="filters">
        <label>Find deliverable<input type="search" value={searchF} onChange={(e) => setSearchF(e.target.value)} placeholder="document number or title" /></label>
        <label>Package<select value={pkgF} onChange={(e) => setPkgF(e.target.value)}>
          <option value="">all packages</option>
          {(pkgs ?? []).map((x: any) => <option key={x.id} value={x.id}>{x.code} — {x.name}</option>)}
        </select></label>
        <label>Discipline<input placeholder="all disciplines" value={discF} onChange={(e) => setDiscF(e.target.value)} /></label>
        <label>Area<input placeholder="all areas" value={areaF} onChange={(e) => setAreaF(e.target.value)} /></label>
        <label>Workflow state<select value={stateF} onChange={(e) => setStateF(e.target.value)}>
          <option value="">any state</option>
          {REVISION_STATES.map((s) => <option key={s} value={s}>{s.replaceAll('_', ' ')}</option>)}
          <option value="no_revision">no revision</option>
        </select></label>
        <label>View<select value={viewF} onChange={(e) => setViewF(e.target.value)}>
          <option value="active">active</option>
          <option value="master">master</option>
          <option value="issued">issued</option>
        </select></label>
        {data && <span className="small muted">{visible.length} of {data.length}</span>}
      </div>
      {error && <ErrorBox error={{ message: error }} />}
      {!data ? <p className="muted">loading…</p> : (
        <RegisterTable cols={cols} rows={visible} exportName="mdl-view.csv" wide stickyFirstColumn
          onRowClick={(r) => nav(`/p/${pid}/deliverables/${r.id}`)} />
      )}
    </div>
  )
}

// ---------- detail ----------

// PEC-DEL-009 / I-6: eight distinct facts, never merged into one flag
const FACT_LABELS: Array<[string, string]> = [
  ['workComplete', 'work complete'],
  ['checkAccepted', 'check accepted'],
  ['approvalRecorded', 'approval recorded'],
  ['authorizedForIssue', 'authorized for issue'],
  ['issued', 'issued'],
  ['returnedWithComments', 'returned with comments'],
  ['superseded', 'superseded'],
  ['archived', 'archived'],
]

export function DeliverableDetailPage(): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const { id } = useParams()
  const person = usePerson()
  const { data, error } = useLoad<any>(() => api.get(p(pid, `deliverables/${id}`)), [pid, id])
  const { data: pkgs } = useLoad<any[]>(() => api.get(p(pid, 'packages')), [pid])
  const [actionError, setActionError] = useState<any>(null)
  const [issueOpen, setIssueOpen] = useState(false)
  const [approvalOpen, setApprovalOpen] = useState(false)
  const [workItemOpen, setWorkItemOpen] = useState(false)
  const [evidenceOpen, setEvidenceOpen] = useState(false)
  const [openCheckId, setOpenCheckId] = useState<number | null>(null)

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const d = data.deliverable
  const rev = data.currentRevision
  // openItems is [] when there is no revision (server shape)
  const oi = Array.isArray(data.openItems) ? null : data.openItems
  const pkg = pkgs?.find((x: any) => x.id === d.packageId)
  const revCodeById = new Map<number, string>(data.revisionChain.map((r: any) => [r.id, r.revCode]))

  // PEC-DEL-007: manual revision moves — the server offers them; we only post the event
  const transition = async (event: string) => {
    setActionError(null)
    try {
      await api.post(p(pid, `revisions/${rev.id}/transition`), { event, version: rev.version })
      toast(`${d.docNo} rev ${rev.revCode}: ${event.replaceAll('_', ' ')} recorded`)
      refresh()
    } catch (e) { setActionError(e) }
  }

  const newRevision = async () => {
    const revCode = window.prompt('New revision code (e.g. B, C, 1):')
    if (!revCode) return
    setActionError(null)
    try {
      await api.post(p(pid, `deliverables/${d.id}/revisions`), { revCode })
      toast(`rev ${revCode} created — prior revision superseded, conditions instantiated`)
      refresh()
    } catch (e) { setActionError(e) }
  }

  const openCheck = openCheckId != null && oi ? oi.checks.find((c: any) => c.id === openCheckId) : null

  const meta: Array<[string, React.ReactNode]> = [
    ['Package', pkg ? `${pkg.code} — ${pkg.name}` : (d.packageId != null ? `#${d.packageId}` : '—')],
    ['Discipline', d.discipline ?? '—'],
    ['Owner', person(d.ownerId)],
    ['DC ref', d.dcRef ?? '—'],
    ['Client no', d.clientNo ?? '—'],
    ['Milestone', d.milestone ?? '—'],
    ['Due', fmtDate(d.dueDate)],
    ['Issue purpose plan', d.issuePurposePlan ?? '—'],
  ]

  return (
    <div>
      <Breadcrumb items={[
        { label: 'Deliverables', to: `/p/${pid}/deliverables` },
        ...(pkg ? [{ label: pkg.code, to: `/p/${pid}/packages/${pkg.id}` }] : []),
        { label: d.docNo },
      ]} />
      {/* 1 — header + metadata (PEC-DEL-002) */}
      <h1>
        <span className="mono">{d.docNo}</span> — {d.title}
        {rev && <> <span className="mono small muted">rev {rev.revCode}</span> <StateTag s={rev.state} /></>}
      </h1>
      {/* deliverable status = workflow completeness (gates closed); issues appear below as drill-down context */}
      <div style={{ margin: '.2rem 0 .4rem' }}><WorkflowStages workflow={data.workflow} /></div>
      <div className="card" style={{ display: 'grid', gridTemplateColumns: 'repeat(4, minmax(140px, 1fr))', gap: '.5rem .9rem' }}>
        {meta.map(([label, value]) => (
          <div key={label as string}>
            <div className="small muted">{label}</div>
            <div className="small">{value}</div>
          </div>
        ))}
      </div>

      {/* 2 — distinct facts strip (PEC-DEL-009, I-6): eight facts, never merged */}
      <h2>Distinct facts</h2>
      <div className="cards">
        {FACT_LABELS.map(([key, label]) => (
          <span key={key} className="card" style={{ padding: '.3rem .6rem', display: 'inline-flex', gap: '.4rem', alignItems: 'center' }}>
            <span className={`badge ${data.facts[key] ? 'green' : 'plain'}`}>{data.facts[key] ? 'yes' : 'no'}</span>
            <span className="small">{label}</span>
          </span>
        ))}
      </div>

      {/* 3 — before this issues (PEC-DEL-004) + manual transitions (PEC-DEL-007) */}
      {rev && data.beforeIssue && (
        <>
          <h2>Before this issues — rev {rev.revCode}</h2>
          <div className="card">
            <ConditionsPanel ex={data.beforeIssue} />
            <div className="row" style={{ marginTop: '.6rem', justifyContent: 'flex-start', flex: 'none' }}>
              {data.offeredTransitions.includes('rework') && (
                <button className="btn secondary small" style={{ flex: 'none' }} onClick={() => transition('rework')}>Rework (back to in work)</button>
              )}
              {data.offeredTransitions.includes('issue') && (
                <button className="btn small" style={{ flex: 'none' }} onClick={() => { setActionError(null); setIssueOpen(true) }}>Record issue event…</button>
              )}
              {data.offeredTransitions.includes('return_comments') && (
                <button className="btn secondary small" style={{ flex: 'none' }} onClick={() => transition('return_comments')}>Returned with comments</button>
              )}
            </div>
          </div>
        </>
      )}
      {!rev && (
        <p className="section-note">No revision yet — create one to start work (conditions instantiate from templates, §5.2).</p>
      )}
      <ErrorBox error={actionError} />

      <div className="row" style={{ margin: '.7rem 0', justifyContent: 'flex-start' }}>
        <button className="btn secondary small" style={{ flex: 'none' }} onClick={newRevision}>New revision</button>
        {rev && <>
          <button className="btn secondary small" style={{ flex: 'none' }} onClick={() => setApprovalOpen(true)}>New approval record</button>
          <button className="btn secondary small" style={{ flex: 'none' }} onClick={() => setWorkItemOpen(true)}>Add work item</button>
          <button className="btn secondary small" style={{ flex: 'none' }} onClick={() => setEvidenceOpen(true)}>Add evidence</button>
        </>}
      </div>

      {/* 4 — open items across record types (PEC-DEL-003) */}
      {oi && (
        <>
          <h2>Work items</h2>
          <RegisterTable cols={[
            { key: 'ref', label: 'Ref', render: (r: any) => <RecordRef recordType="work_item" id={r.id} recordRef={r.ref} /> },
            { key: 'title', label: 'Title', render: (r: any) => r.title },
            { key: 'owner', label: 'Owner', render: (r: any) => <span className="small">{person(r.ownerId)}</span> },
            { key: 'needBy', label: 'Need by', render: (r: any) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
            { key: 'state', label: 'State', render: (r: any) => <StateTag s={r.state} /> },
          ]} rows={oi.workItems} />

          {/* checks: three distinct facts per row (PEC-CHK-003) + inline check actions (PRD §12.8) */}
          <h2>Checks</h2>
          <RegisterTable cols={[
            { key: 'ref', label: 'Ref', render: (r: any) => <RecordRef recordType="check" id={r.id} recordRef={r.ref} /> },
            { key: 'checker', label: 'Checker', render: (r: any) => <span className="small">{person(r.checkerId)}{r.independenceWarning && <span className="badge amber" title="checker is the deliverable owner (PEC-CHK-004)"> independence</span>}</span> },
            { key: 'state', label: 'Checker acceptance', render: (r: any) => <StateTag s={r.state} /> },
            { key: 'checklist', label: 'Checklist', render: (r: any) => <span className="mono">{r.checklistDone}/{r.checklistTotal}</span> },
            { key: 'comments', label: 'Comments', render: (r: any) => <span className="mono">{r.openComments} open / {r.totalComments}</span> },
            { key: 'open', label: '', render: (r: any) => <button className="btn secondary small" onClick={(e) => { e.stopPropagation(); setOpenCheckId(r.id) }}>open</button> },
          ]} rows={oi.checks} />

          <h2>Review comments</h2>
          <RegisterTable cols={[
            { key: 'ref', label: 'Ref', render: (r: any) => <RecordRef recordType="review_comment" id={r.id} recordRef={r.ref} /> },
            { key: 'text', label: 'Comment', render: (r: any) => <span className="small">{r.text}</span> },
            { key: 'responder', label: 'Responder', render: (r: any) => <span className="small">{person(r.responderId)}</span> },
            { key: 'disp', label: 'Disposition', render: (r: any) => <StateTag s={r.disposition} /> },
          ]} rows={oi.comments} />

          <h2>Holds</h2>
          <RegisterTable cols={[
            { key: 'badge', label: '', render: () => <span className="badge hold">hold</span> },
            { key: 'ref', label: 'Ref', render: (r: any) => <RecordRef recordType="hold" id={r.id} recordRef={r.ref} /> },
            { key: 'cause', label: 'Cause', render: (r: any) => r.cause.replaceAll('_', ' ') },
            { key: 'title', label: 'Title', render: (r: any) => r.title },
            { key: 'owner', label: 'Owner', render: (r: any) => <span className="small">{person(r.ownerId)}</span> },
            { key: 'needBy', label: 'Need by', render: (r: any) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
          ]} rows={oi.holds} />

          <h2>Approval records</h2>
          <RegisterTable cols={[
            { key: 'ref', label: 'Ref', render: (r: any) => <RecordRef recordType="approval_record" id={r.id} recordRef={r.ref} /> },
            { key: 'title', label: 'Title', render: (r: any) => r.title },
            { key: 'state', label: 'State', render: (r: any) => <StateTag s={r.state} /> },
            { key: 'sign', label: 'Signatories', render: (r: any) => <span className="small">{r.signatoryIds.map((s: number) => person(s)).join(', ')}</span> },
          ]} rows={oi.approvalRecords} />

          <h2>Decision dependencies</h2>
          <RegisterTable cols={[
            { key: 'ref', label: 'Ref', render: (r: any) => <RecordRef recordType="decision" id={r.id} recordRef={r.ref} /> },
            { key: 'title', label: 'Title', render: (r: any) => r.title },
            { key: 'state', label: 'State', render: (r: any) => <StateTag s={r.state} /> },
          ]} rows={oi.decisionDependencies} />

          <h2>Risks</h2>
          <RegisterTable cols={[
            { key: 'ref', label: 'Ref', render: (r: any) => <RecordRef recordType="risk" id={r.id} recordRef={r.ref} /> },
            { key: 'title', label: 'Title', render: (r: any) => r.title },
            { key: 'owner', label: 'Owner', render: (r: any) => <span className="small">{person(r.ownerId)}</span> },
            { key: 'needBy', label: 'Need by', render: (r: any) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
            { key: 'state', label: 'State', render: (r: any) => <StateTag s={r.state} /> },
          ]} rows={oi.risks} />
        </>
      )}

      {/* 6 — revision chain, oldest → newest (PEC-DEL-006); issue events (PEC-DEL-008, PEC-ARC-002) */}
      <h2>Revision chain</h2>
      <ResizableTable resizeKey="deliverable-revision-chain">
        <thead><tr><th>Rev</th><th>State</th><th>Created</th><th>Superseded by</th><th>Issue events</th></tr></thead>
        <tbody>
          {data.revisionChain.map((r: any) => (
            <tr key={r.id}>
              <td className="mono">{r.revCode}</td>
              <td><StateTag s={r.state} /></td>
              <td className="nowrap small">{fmtDate(r.createdAt)}</td>
              <td className="mono small">{r.supersededBy != null ? `rev ${revCodeById.get(r.supersededBy) ?? '#' + r.supersededBy}` : '—'}</td>
              <td>
                {r.issueEvents.length === 0 && <span className="muted small">—</span>}
                {r.issueEvents.map((e: any) => (
                  <div key={e.ref} className="small">
                    <span className="mono">{e.ref}</span> {e.purpose} · transmittal <span className="mono">{e.transmittalRef}</span>
                    {' '}· to {e.recipients.join(', ')} · {fmtDate(e.issuedAt)} · archive <span className="mono">{e.archiveRef}</span>
                  </div>
                ))}
              </td>
            </tr>
          ))}
          {data.revisionChain.length === 0 && <tr><td colSpan={5} className="muted small">no revisions</td></tr>}
        </tbody>
      </ResizableTable>

      {/* 9 — evidence trail + history: one stream of record (PEC-DEL-005) */}
      <h2>Evidence</h2>
      <RegisterTable cols={[
        { key: 'label', label: 'Label', render: (r: any) => r.label },
        { key: 'kind', label: 'Kind', render: (r: any) => <StateTag s={r.kind} /> },
        { key: 'where', label: 'Where', render: (r: any) => r.urlOrPath ? <a href={r.urlOrPath} target="_blank" rel="noreferrer" className="small">{r.urlOrPath}</a> : <span className="small muted">{r.content ?? '—'}</span> },
        { key: 'by', label: 'Added by', render: (r: any) => <span className="small">{person(r.addedBy)}</span> },
        { key: 'at', label: 'At', render: (r: any) => <span className="nowrap small">{fmtDate(r.addedAt)}</span> },
      ]} rows={data.evidence} />

      <h2>History — updates and history are the same stream (PEC-DEL-005)</h2>
      <HistoryTrail entries={data.history} />

      {/* drawers */}
      {issueOpen && rev && (
        <IssueDrawer pid={pid} revision={rev} docNo={d.docNo} onClose={() => setIssueOpen(false)} />
      )}
      {approvalOpen && rev && (
        <ApprovalDrawer pid={pid} revisionId={rev.id} onClose={() => setApprovalOpen(false)} />
      )}
      {workItemOpen && rev && (
        <WorkItemDrawer pid={pid} revisionId={rev.id} onClose={() => setWorkItemOpen(false)} />
      )}
      {evidenceOpen && rev && (
        <EvidenceDrawer pid={pid} revisionId={rev.id} onClose={() => setEvidenceOpen(false)} />
      )}
      {openCheck && oi && (
        <CheckDrawer pid={pid} check={openCheck}
          comments={oi.comments.filter((c: any) => c.checkId === openCheck.id)}
          onClose={() => setOpenCheckId(null)} />
      )}
    </div>
  )
}

// ---------- issue drawer (PEC-DEL-007/008): recording the issue event IS the transition ----------

function IssueDrawer({ pid, revision, docNo, onClose }: {
  pid: number; revision: any; docNo: string; onClose(): void
}): JSX.Element {
  const { refresh, toast } = useApp()
  const [purpose, setPurpose] = useState('IFR')
  const [transmittalRef, setTransmittalRef] = useState('')
  const [recipients, setRecipients] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true)
    setError(null)
    try {
      await api.post(p(pid, `revisions/${revision.id}/transition`), {
        event: 'issue',
        version: revision.version,
        issueEvent: {
          purpose, transmittalRef,
          recipients: recipients.split(',').map((r) => r.trim()).filter(Boolean),
        },
      })
      toast(`${docNo} rev ${revision.revCode} issued (${purpose})`)
      refresh()
      onClose()
    } catch (err) {
      // 409 CONDITIONS_OPEN renders the open conditions; the blocked attempt is recorded server-side
      setError(err)
    } finally {
      setBusy(false)
    }
  }

  return (
    <Drawer title={`Issue ${docNo} rev ${revision.revCode}`} onClose={onClose}>
      <p className="section-note">
        Hard-gated (D-11): every hard condition on the issue gate must be satisfied or waived.
        The transmittal and recipients are the issue record (PEC-DEL-008).
      </p>
      <form className="stack" onSubmit={submit}>
        <label>Purpose
          <select value={purpose} onChange={(e) => setPurpose(e.target.value)}>
            <option value="IFR">IFR — issued for review</option>
            <option value="IFA">IFA — issued for approval</option>
            <option value="IFC">IFC — issued for construction</option>
            <option value="other">other</option>
          </select>
        </label>
        <label>Transmittal reference *
          <input required value={transmittalRef} onChange={(e) => setTransmittalRef(e.target.value)} placeholder="e.g. TR-0042" />
        </label>
        <label>Recipients (comma-separated) *
          <input required value={recipients} onChange={(e) => setRecipients(e.target.value)} placeholder="e.g. Client DC, Vendor X" />
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !transmittalRef || !recipients.trim()}>Record issue event</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ---------- approval record drawer (PEC-AUTH-001) ----------

function ApprovalDrawer({ pid, revisionId, onClose }: { pid: number; revisionId: number; onClose(): void }): JSX.Element {
  const { people, refresh, toast } = useApp()
  const [title, setTitle] = useState('')
  const [approvalType, setApprovalType] = useState('')
  const [authoritySource, setAuthoritySource] = useState('')
  const [signatoryIds, setSignatoryIds] = useState<string[]>([])
  const [dueDate, setDueDate] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true)
    setError(null)
    try {
      const r = await api.post(p(pid, 'approval-records'), {
        title, approvalType,
        authoritySource: authoritySource || undefined,
        appliesToType: 'revision', appliesToId: revisionId,
        signatoryIds: signatoryIds.map(Number),
        dueDate: dueDate || undefined,
      })
      toast(`${r.ref} created — signatories are notified when prerequisites complete`)
      refresh()
      onClose()
    } catch (err) {
      setError(err)
    } finally {
      setBusy(false)
    }
  }

  return (
    <Drawer title="New approval record" onClose={onClose}>
      <p className="section-note">
        Approval is a record with named signatories (D-12); the outcome is only reached by
        recording it — never by task completion (PEC-AUTH-004).
      </p>
      <form className="stack" onSubmit={submit}>
        <label>Title *
          <input required value={title} onChange={(e) => setTitle(e.target.value)} />
        </label>
        <label>Approval type *
          <input required value={approvalType} onChange={(e) => setApprovalType(e.target.value)} placeholder="e.g. EM sign-off" />
        </label>
        <label>Authority source (why approval is required)
          <input value={authoritySource} onChange={(e) => setAuthoritySource(e.target.value)} placeholder="e.g. contract §4.2" />
        </label>
        <label>Signatories * (ctrl/cmd-click for several)
          <select multiple size={Math.min(8, people.length)} value={signatoryIds}
            onChange={(e) => setSignatoryIds(Array.from(e.target.selectedOptions).map((o) => o.value))}>
            {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
          </select>
        </label>
        <label>Due date
          <input type="date" value={dueDate} onChange={(e) => setDueDate(e.target.value)} />
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !title || !approvalType || signatoryIds.length === 0}>Create</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ---------- work item drawer (anchored to the current revision, I-2) ----------

function WorkItemDrawer({ pid, revisionId, onClose }: { pid: number; revisionId: number; onClose(): void }): JSX.Element {
  const { people, refresh, toast } = useApp()
  const [title, setTitle] = useState('')
  const [statement, setStatement] = useState('')
  const [ownerId, setOwnerId] = useState('')
  const [needBy, setNeedBy] = useState('')
  const [kind, setKind] = useState('action')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true)
    setError(null)
    try {
      const r = await api.post(p(pid, 'work-items'), {
        anchorType: 'revision', anchorId: revisionId,
        title, statement: statement || undefined,
        ownerId: Number(ownerId), needBy: needBy || null, kind,
      })
      toast(`${r.ref} created, anchored to this revision`)
      refresh()
      onClose()
    } catch (err) {
      setError(err)
    } finally {
      setBusy(false)
    }
  }

  return (
    <Drawer title="Add work item" onClose={onClose}>
      <form className="stack" onSubmit={submit}>
        <label>Title *
          <input required value={title} onChange={(e) => setTitle(e.target.value)} />
        </label>
        <label>Statement
          <textarea value={statement} onChange={(e) => setStatement(e.target.value)} />
        </label>
        <div className="row">
          <label>Owner *
            <select required value={ownerId} onChange={(e) => setOwnerId(e.target.value)}>
              <option value="">—</option>
              {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
            </select>
          </label>
          <label>Need by
            <input type="date" value={needBy} onChange={(e) => setNeedBy(e.target.value)} />
          </label>
        </div>
        <label>Kind
          <select value={kind} onChange={(e) => setKind(e.target.value)}>
            {WORK_ITEM_KINDS.map((k) => <option key={k} value={k}>{k.replaceAll('_', ' ')}</option>)}
          </select>
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !title || !ownerId}>Create</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ---------- evidence drawer (PEC-DEL-005; evidence-type conditions satisfy on match, §5.3) ----------

function EvidenceDrawer({ pid, revisionId, onClose }: { pid: number; revisionId: number; onClose(): void }): JSX.Element {
  const { refresh, toast } = useApp()
  const [label, setLabel] = useState('')
  const [kind, setKind] = useState('attachment')
  const [urlOrPath, setUrlOrPath] = useState('')
  const [content, setContent] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true)
    setError(null)
    try {
      await api.post(p(pid, `records/revision/${revisionId}/evidence`), {
        label, kind,
        urlOrPath: urlOrPath || undefined,
        content: content || undefined,
      })
      toast('evidence attached to the revision')
      refresh()
      onClose()
    } catch (err) {
      setError(err)
    } finally {
      setBusy(false)
    }
  }

  return (
    <Drawer title="Add evidence" onClose={onClose}>
      <form className="stack" onSubmit={submit}>
        <label>Label *
          <input required value={label} onChange={(e) => setLabel(e.target.value)} placeholder="matches required artifact name to satisfy evidence conditions" />
        </label>
        <label>Kind
          <select value={kind} onChange={(e) => setKind(e.target.value)}>
            {EVIDENCE_KINDS.map((k) => <option key={k} value={k}>{k.replaceAll('_', ' ')}</option>)}
          </select>
        </label>
        <label>URL or path
          <input value={urlOrPath} onChange={(e) => setUrlOrPath(e.target.value)} />
        </label>
        <label>Content / note
          <textarea value={content} onChange={(e) => setContent(e.target.value)} />
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !label}>Attach</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ---------- check drawer — where checking happens (PRD §12.8, PEC-CHK-002/003/004) ----------

function CheckDrawer({ pid, check, comments, onClose }: {
  pid: number; check: any; comments: any[]; onClose(): void
}): JSX.Element {
  const { people, refresh, toast } = useApp()
  const person = usePerson()
  const [checklist, setChecklist] = useState<any[]>(check.checklist)
  const [responses, setResponses] = useState<Record<number, string>>({})
  const [newResponderId, setNewResponderId] = useState('')
  const [newText, setNewText] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  // server truth after each mutation: refresh() reloads the page data and this re-syncs
  useEffect(() => { setChecklist(check.checklist) }, [check.id, check.version])

  const run = async (fn: () => Promise<unknown>, msg: string) => {
    setBusy(true)
    setError(null)
    try {
      await fn()
      toast(msg)
      refresh()
    } catch (err) {
      // 403/400/409 are server verdicts — we only surface them (SPEC §1)
      setError(err)
    } finally {
      setBusy(false)
    }
  }

  const setItem = (i: number, patch: Record<string, unknown>) =>
    setChecklist((cl) => cl.map((it, j) => (j === i ? { ...it, ...patch } : it)))

  const reopenComment = (c: any) => {
    const reason = window.prompt('Reopen reason:')
    if (!reason) return
    void run(() => api.post(p(pid, `comments/${c.id}/reopen`), { version: c.version, reason }),
      `${c.ref} reopened`)
  }
  const reopenCheck = () => {
    const reason = window.prompt('Reopen reason:')
    if (!reason) return
    void run(() => api.post(p(pid, `checks/${check.id}/reopen`), { version: check.version, reason }),
      `${check.ref} reopened`)
  }

  return (
    <Drawer title={<>Check <span className="mono">{check.ref}</span> <StateTag s={check.state} /></>} onClose={onClose}>
      {/* PEC-CHK-004: independence is warned in P1, never silently merged away */}
      {check.independenceWarning && (
        <div className="error-box" style={{ marginBottom: '.6rem' }}>
          <b>Independence warning (PEC-CHK-004):</b> the checker is the deliverable owner.
          Recorded on the check; a hard block is configurable later.
        </div>
      )}
      <p className="small muted">
        Checker: {person(check.checkerId)} · three distinct facts — checklist completion,
        comment closure, checker acceptance — are tracked separately (PEC-CHK-003).
      </p>

      <div className="row" style={{ justifyContent: 'flex-start', marginBottom: '.6rem' }}>
        {check.state === 'open' && (
          <button className="btn small" style={{ flex: 'none' }} disabled={busy}
            onClick={() => void run(() => api.post(p(pid, `checks/${check.id}/start`), { version: check.version }), `${check.ref} started`)}>
            Start check
          </button>
        )}
        {(check.state === 'in_check' || check.state === 'comments_closed') && (
          <button className="btn small" style={{ flex: 'none' }} disabled={busy}
            onClick={() => void run(() => api.post(p(pid, `checks/${check.id}/accept`), { version: check.version }), `${check.ref} accepted`)}>
            Accept check
          </button>
        )}
        {check.state === 'accepted' && (
          <button className="btn secondary small" style={{ flex: 'none' }} disabled={busy} onClick={reopenCheck}>
            Reopen check
          </button>
        )}
      </div>

      <h2>Checklist</h2>
      {checklist.length === 0 && <p className="muted small">no checklist items (template-free check)</p>}
      {checklist.map((it, i) => (
        <div key={i} style={{ display: 'flex', gap: '.5rem', alignItems: 'flex-start', margin: '.3rem 0' }}>
          <input type="checkbox" checked={!!it.done} onChange={(e) => setItem(i, { done: e.target.checked })} />
          <div style={{ flex: 1 }}>
            <div className="small">{it.text}{it.category && <span className="muted"> · {it.category}</span>}</div>
            <input style={{ width: '100%', font: 'inherit', fontSize: '.78rem', padding: '.2rem .4rem', border: '1px solid var(--line)', borderRadius: 4 }}
              placeholder="note" value={it.note ?? ''} onChange={(e) => setItem(i, { note: e.target.value || null })} />
          </div>
        </div>
      ))}
      {checklist.length > 0 && (
        <button className="btn secondary small" disabled={busy}
          onClick={() => void run(() => api.put(p(pid, `checks/${check.id}/checklist`), { version: check.version, checklist }),
            'checklist saved')}>
          Save checklist ({checklist.filter((i) => i.done).length}/{checklist.length} done)
        </button>
      )}

      {/* comments closed individually by the checker, never in bulk (PEC-CHK-002) */}
      <h2>Comments</h2>
      {comments.length === 0 && <p className="muted small">no comments on this check</p>}
      {comments.map((c) => (
        <div key={c.id} className="cond" style={{ borderLeftColor: c.disposition === 'accepted_closed' ? 'var(--green)' : undefined }}>
          <span className="mono">{c.ref}</span> <StateTag s={c.disposition} />{' '}
          <span className="small">{c.text}</span>
          <div className="small muted">responder {person(c.responderId)}{c.response && <> · response: {c.response}</>}</div>
          <div className="row" style={{ justifyContent: 'flex-start', marginTop: '.25rem' }}>
            {(c.disposition === 'open' || c.disposition === 'reopened') && (
              <>
                <input style={{ flex: 1, font: 'inherit', fontSize: '.78rem', padding: '.2rem .4rem', border: '1px solid var(--line)', borderRadius: 4 }}
                  placeholder="response" value={responses[c.id] ?? ''}
                  onChange={(e) => setResponses((m) => ({ ...m, [c.id]: e.target.value }))} />
                <button className="btn secondary small" style={{ flex: 'none' }} disabled={busy || !(responses[c.id] ?? '').trim()}
                  onClick={() => void run(() => api.post(p(pid, `comments/${c.id}/respond`), { version: c.version, response: responses[c.id] }),
                    `${c.ref} responded`)}>
                  Respond
                </button>
              </>
            )}
            {c.disposition === 'responded' && (
              <>
                <button className="btn small" style={{ flex: 'none' }} disabled={busy}
                  onClick={() => void run(() => api.post(p(pid, `comments/${c.id}/accept`), { version: c.version }),
                    `${c.ref} accepted closed`)}>
                  Accept closure
                </button>
                <button className="btn secondary small" style={{ flex: 'none' }} disabled={busy} onClick={() => reopenComment(c)}>
                  Reopen
                </button>
              </>
            )}
            {c.disposition === 'accepted_closed' && (
              <button className="btn secondary small" style={{ flex: 'none' }} disabled={busy} onClick={() => reopenComment(c)}>
                Reopen
              </button>
            )}
          </div>
        </div>
      ))}

      <h3>Add comment</h3>
      <form className="stack" onSubmit={(e) => {
        e.preventDefault()
        void run(async () => {
          await api.post(p(pid, `checks/${check.id}/comments`), { responderId: Number(newResponderId), text: newText })
          setNewText('')
        }, 'comment raised — responder notified')
      }}>
        <div className="row">
          <label>Responder *
            <select required value={newResponderId} onChange={(e) => setNewResponderId(e.target.value)}>
              <option value="">—</option>
              {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
            </select>
          </label>
        </div>
        <label>Comment *
          <textarea required value={newText} onChange={(e) => setNewText(e.target.value)} />
        </label>
        <div className="row">
          <button className="btn small" disabled={busy || !newText || !newResponderId} style={{ flex: 'none' }}>Add comment</button>
        </div>
      </form>

      <ErrorBox error={error} />
    </Drawer>
  )
}
