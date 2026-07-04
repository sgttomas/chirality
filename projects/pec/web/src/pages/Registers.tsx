/**
 * Registers — approvals (the authorization basis register, PRD §12.7), decisions
 * (PRD §12.9), risks (§12.10), interfaces (PEC-INT-001), and holds. Five server-truth
 * registers behind one tab bar. The web layer renders what the server returns and posts
 * events back (SPEC §1): every guard (signatory-only, authority-only, hold veto,
 * conditions) is enforced server-side and surfaced here via ErrorBox.
 */

import { useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api, p } from '../api.ts'
import {
  Drawer, ErrorBox, RegisterTable, StateTag, fmtDate, useApp, useLoad, usePerson,
} from '../shared.tsx'
import type { Col } from '../shared.tsx'

const TABS = [
  ['approvals', 'Approvals'],
  ['decisions', 'Decisions'],
  ['risks', 'Risks'],
  ['interfaces', 'Interfaces'],
  ['holds', 'Holds'],
] as const

export function RegistersPage(): JSX.Element {
  const { pid } = useApp()
  const params = useParams()
  const nav = useNavigate()
  const tab = params.tab ?? 'approvals'
  return (
    <div>
      <h1>Registers</h1>
      <div className="filters">
        {TABS.map(([k, label]) => (
          <button key={k} className={`btn small ${tab === k ? '' : 'secondary'}`}
            onClick={() => nav(`/p/${pid}/registers/${k}`)}>{label}</button>
        ))}
      </div>
      {tab === 'approvals' && <ApprovalsTab />}
      {tab === 'decisions' && <DecisionsTab />}
      {tab === 'risks' && <RisksTab />}
      {tab === 'interfaces' && <InterfacesTab />}
      {tab === 'holds' && <HoldsTab />}
    </div>
  )
}

// ================================================================ approvals

/**
 * PEC-AUTH-001: the Approval Register is the AUTHORIZATION BASIS register — it answers
 * why approval is required (source of authority), against what, who signs, and what was
 * decided. PEC-AUTH-002: requirement (state + prerequisites), readiness (latency from
 * ready_at) and outcome (decision ref) are three distinct visible facts.
 */
function ApprovalsTab(): JSX.Element {
  const { pid } = useApp()
  const person = usePerson()
  const { data, error } = useLoad(() => api.get(p(pid, 'approval-register')), [pid])
  const [creating, setCreating] = useState(false)
  const [outcomeFor, setOutcomeFor] = useState<any>(null)

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const cols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span> },
    {
      key: 'title', label: 'Title', render: (r) => <>
        {r.title}{r.holdPoint && <> <span className="badge red" title="hold point — work may not proceed past this approval">HP</span></>}
      </>,
    },
    { key: 'type', label: 'Type', render: (r) => <span className="small">{r.approvalType}</span> },
    // source of authority — prominent (PEC-AUTH-001: WHY approval is required)
    {
      key: 'authority', label: 'Source of authority', render: (r) =>
        r.authoritySource ? <b className="small">{r.authoritySource}</b> : <span className="muted small">unstated</span>,
    },
    { key: 'applies', label: 'Applies to', render: (r) => <span className="mono">{r.appliesToType}#{r.appliesToId}</span> },
    {
      key: 'signatories', label: 'Signatories', render: (r) =>
        <span className="small">{r.signatoryIds.map((id: number) => person(id)).join(', ')}</span>,
    },
    { key: 'due', label: 'Due', render: (r) => <span className="nowrap">{fmtDate(r.dueDate)}</span> },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} /> },
    {
      // approval latency from ready_at (§6.3 signal; warn > 5 wd, escalate > 10 wd defaults)
      key: 'latency', label: 'Latency (wd)', render: (r) => r.readyAt == null
        ? <span className="muted">—</span>
        : <span className={r.latencyWd > 10 ? 'badge red' : r.latencyWd > 5 ? 'badge amber' : 'mono'}>{r.latencyWd}</span>,
    },
    {
      // outcome is a Decision row linked back (OM-6) — shown distinct from readiness (PEC-AUTH-002)
      key: 'outcome', label: 'Outcome', render: (r) => r.outcome
        ? <><StateTag s={r.outcome} /> <span className="mono small">{r.outcomeDecisionRef}</span></>
        : <span className="muted small">—</span>,
    },
    {
      key: 'prereqs', label: 'Prerequisites', render: (r) => r.prerequisites.length === 0
        ? <span className="muted small">none</span>
        : <span className="small">{r.prerequisites.map((q: any) => (
          <span key={q.ref} className={`state ${q.state}`} style={{ marginRight: '.25rem' }}
            title={`${q.ref} [${q.severity}] ${q.description}`}>{q.state.replaceAll('_', ' ')}</span>
        ))}</span>,
      csv: (r) => r.prerequisites.map((q: any) => `${q.ref}:${q.state}`).join('; '),
    },
    {
      key: 'act', label: '', render: (r) => r.state === 'ready'
        ? <button className="btn small" onClick={() => setOutcomeFor(r)}>Record outcome</button>
        : null,
      csv: () => null,
    },
  ]

  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: '.75rem' }}>
        <p className="section-note" style={{ flex: 1 }}>
          Authorization basis register (PRD §12.7): why approval is required, under what
          authority, who signs, and what was decided. Only record-outcome closes a record
          (PEC-AUTH-004, server-enforced).
        </p>
        <button className="btn small" onClick={() => setCreating(true)}>+ New approval record</button>
      </div>
      <RegisterTable cols={cols} rows={data} exportName="approval-register.csv" />
      {creating && <NewApprovalDrawer onClose={() => setCreating(false)} />}
      {outcomeFor && <ApprovalOutcomeDrawer row={outcomeFor} onClose={() => setOutcomeFor(null)} />}
    </div>
  )
}

function NewApprovalDrawer({ onClose }: { onClose(): void }): JSX.Element {
  const { pid, people, refresh, toast } = useApp()
  const [title, setTitle] = useState('')
  const [approvalType, setApprovalType] = useState('')
  const [authoritySource, setAuthoritySource] = useState('')
  const [appliesToType, setAppliesToType] = useState('revision')
  const [appliesToId, setAppliesToId] = useState('')
  const [signatories, setSignatories] = useState<string[]>([])
  const [basisRef, setBasisRef] = useState('')
  const [dueDate, setDueDate] = useState('')
  const [holdPoint, setHoldPoint] = useState(false)
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    try {
      const r = await api.post(p(pid, 'approval-records'), {
        title, approvalType,
        authoritySource: authoritySource || undefined,
        appliesToType, appliesToId: Number(appliesToId),
        signatoryIds: signatories.map(Number),
        basisRef: basisRef || undefined,
        dueDate: dueDate || undefined,
        holdPoint,
      })
      toast(`${r.ref} created — prerequisites instantiated; readiness re-evaluates on every condition change`)
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title="New approval record" onClose={onClose}>
      <p className="section-note">
        Names the requirement and its source of authority up front (PEC-AUTH-001).
        Named signatories only in P1 (D-12).
      </p>
      <form className="stack" onSubmit={submit}>
        <label>Title *
          <input required value={title} onChange={(e) => setTitle(e.target.value)} />
        </label>
        <div className="row">
          <label>Approval type *
            <input required value={approvalType} onChange={(e) => setApprovalType(e.target.value)}
              placeholder="e.g. EOR sign-off, client hold point" />
          </label>
          <label>Source of authority
            <input value={authoritySource} onChange={(e) => setAuthoritySource(e.target.value)}
              placeholder="e.g. contract §4.2, AHJ permit" />
          </label>
        </div>
        <div className="row">
          <label>Applies to
            <select value={appliesToType} onChange={(e) => setAppliesToType(e.target.value)}>
              <option value="revision">revision</option>
              <option value="deliverable">deliverable</option>
              <option value="package">package</option>
            </select>
          </label>
          <label>Record id *
            <input required type="number" min={1} value={appliesToId} onChange={(e) => setAppliesToId(e.target.value)} />
          </label>
        </div>
        <p className="section-note" style={{ margin: 0 }}>
          The internal #id of the target record — shown in the “Applies to” column here and
          in detail-page URLs (e.g. deliverable 12 → /deliverables/12).
        </p>
        <label>Signatories * (named, D-12 — hold ⌘/Ctrl to select several)
          <select multiple size={Math.min(people.length, 8)} value={signatories}
            onChange={(e) => setSignatories(Array.from(e.target.selectedOptions, (o) => o.value))}>
            {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
          </select>
        </label>
        <div className="row">
          <label>Basis reference
            <input value={basisRef} onChange={(e) => setBasisRef(e.target.value)} placeholder="e.g. DBM-004" />
          </label>
          <label>Due date
            <input type="date" value={dueDate} onChange={(e) => setDueDate(e.target.value)} />
          </label>
        </div>
        <label style={{ flexDirection: 'row', alignItems: 'center', gap: '.4rem' }}>
          <input type="checkbox" checked={holdPoint} onChange={(e) => setHoldPoint(e.target.checked)} />
          Hold point — work may not proceed past this approval
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || signatories.length === 0 || !appliesToId}>Create</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

function ApprovalOutcomeDrawer({ row, onClose }: { row: any; onClose(): void }): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const [outcome, setOutcome] = useState('approve')
  const [rationale, setRationale] = useState('')
  const [newDueDate, setNewDueDate] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    try {
      // PEC-AUTH-004: record-outcome is the only closure path; the server enforces
      // signatory-only recording (D-12) and the hold veto — errors render below.
      await api.post(p(pid, `approval-records/${row.id}/outcome`), {
        version: row.version, outcome, rationale,
        newDueDate: outcome === 'defer' && newDueDate ? newDueDate : undefined,
      })
      toast(`${row.ref} outcome recorded: ${outcome} — written as a Decision (OM-6)`)
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title={<>Record outcome — <span className="mono">{row.ref}</span></>} onClose={onClose}>
      <p className="section-note">{row.title} · applies to <span className="mono">{row.appliesToType}#{row.appliesToId}</span></p>
      <form className="stack" onSubmit={submit}>
        <label>Outcome
          <select value={outcome} onChange={(e) => setOutcome(e.target.value)}>
            <option value="approve">approve</option>
            <option value="conditionally_accept">conditionally accept</option>
            <option value="reject">reject</option>
            <option value="defer">defer</option>
          </select>
        </label>
        <label>Rationale * (recorded on the outcome Decision)
          <textarea required value={rationale} onChange={(e) => setRationale(e.target.value)} />
        </label>
        {outcome === 'defer' && (
          <label>New due date (defer resets the due date; the record stays ready)
            <input type="date" value={newDueDate} onChange={(e) => setNewDueDate(e.target.value)} />
          </label>
        )}
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !rationale}>Record</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ================================================================ decisions

/** PEC-DEC-003 outcome vocabulary (PRD §12.9). */
const DECISION_OUTCOMES = [
  'select', 'approve', 'reject', 'defer', 'conditionally_accept', 'confirm_basis', 'waive', 'supersede',
] as const

/** PEC-DEC-001: the decision register with owner, authority, need-by, and outcome. */
function DecisionsTab(): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const person = usePerson()
  const { data, error } = useLoad(() => api.get(p(pid, 'decisions')), [pid])
  const [creating, setCreating] = useState(false)
  const [assignFor, setAssignFor] = useState<any>(null)
  const [outcomeFor, setOutcomeFor] = useState<any>(null)
  const [supersedeFor, setSupersedeFor] = useState<any>(null)
  const [actionError, setActionError] = useState<any>(null)
  const [busyId, setBusyId] = useState<number | null>(null)

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const markPending = async (r: any) => {
    setBusyId(r.id); setActionError(null)
    try {
      await api.post(p(pid, `decisions/${r.id}/progress`), { event: 'mark_pending', version: r.version })
      toast(`${r.ref} pending — authority notified (§4.6)`)
      refresh()
    } catch (err) { setActionError(err) } finally { setBusyId(null) }
  }

  const cols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span> },
    { key: 'title', label: 'Title', render: (r) => r.title },
    // kind chip: standalone / approval_outcome / waiver — one judgment record (OM-6)
    { key: 'kind', label: 'Kind', render: (r) => <span className="state">{r.kind.replaceAll('_', ' ')}</span> },
    { key: 'statement', label: 'Decision needed', render: (r) => <span className="small">{r.statement}</span> },
    { key: 'preparer', label: 'Preparer', render: (r) => <span className="small">{person(r.preparerId)}</span> },
    { key: 'authority', label: 'Authority', render: (r) => <span className="small">{person(r.authorityId)}</span> },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
    {
      // PEC-DEC-002: overdue undecided decisions flagged
      key: 'overdue', label: 'Overdue (d)', render: (r) => r.overdueDays > 0
        ? <span className="badge red">{r.overdueDays}</span>
        : <span className="muted">—</span>,
    },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} /> },
    { key: 'outcome', label: 'Outcome', render: (r) => r.outcome ? <StateTag s={r.outcome} /> : <span className="muted small">—</span> },
    { key: 'rationale', label: 'Rationale', render: (r) => <span className="small muted">{r.rationale}</span> },
    { key: 'links', label: 'Links', render: (r) => r.links.length > 0 ? r.links.length : <span className="muted">0</span> },
    {
      key: 'act', label: '', csv: () => null, render: (r) => {
        if (r.state === 'identified') return <button className="btn small" onClick={() => setAssignFor(r)}>Assign preparer</button>
        if (r.state === 'in_progress') return <button className="btn small" disabled={busyId === r.id} onClick={() => markPending(r)}>Mark pending</button>
        if (r.state === 'pending') return <button className="btn small" onClick={() => setOutcomeFor(r)}>Record outcome</button>
        if (r.state === 'decided') return <button className="btn small secondary" onClick={() => setSupersedeFor(r)}>Supersede</button>
        return null
      },
    },
  ]

  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: '.75rem' }}>
        <p className="section-note" style={{ flex: 1 }}>
          Every judgment is a Decision row — standalone, approval outcome, or waiver (OM-6).
          Only the named authority records an outcome (server-enforced, §7.6).
        </p>
        <button className="btn small" onClick={() => setCreating(true)}>+ New decision</button>
      </div>
      <ErrorBox error={actionError} />
      <RegisterTable cols={cols} rows={data} exportName="decision-register.csv" />
      {creating && <NewDecisionDrawer onClose={() => setCreating(false)} />}
      {assignFor && <AssignPreparerDrawer row={assignFor} onClose={() => setAssignFor(null)} />}
      {outcomeFor && <DecisionOutcomeDrawer row={outcomeFor} onClose={() => setOutcomeFor(null)} />}
      {supersedeFor && (
        <SupersedeDecisionDrawer row={supersedeFor} all={data} onClose={() => setSupersedeFor(null)} />
      )}
    </div>
  )
}

function NewDecisionDrawer({ onClose }: { onClose(): void }): JSX.Element {
  const { pid, people, refresh, toast } = useApp()
  const packages = useLoad(() => api.get(p(pid, 'packages')), [pid])
  const [title, setTitle] = useState('')
  const [statement, setStatement] = useState('')
  const [authorityId, setAuthorityId] = useState('')
  const [preparerId, setPreparerId] = useState('')
  const [needBy, setNeedBy] = useState('')
  const [packageId, setPackageId] = useState('')
  const [optionsConsidered, setOptionsConsidered] = useState('')
  const [recommendation, setRecommendation] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    try {
      const r = await api.post(p(pid, 'decisions'), {
        title, statement,
        authorityId: Number(authorityId),
        preparerId: preparerId ? Number(preparerId) : undefined,
        needBy: needBy || undefined,
        packageId: packageId ? Number(packageId) : undefined,
        optionsConsidered: optionsConsidered || undefined,
        recommendation: recommendation || undefined,
      })
      toast(`${r.ref} identified`)
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title="New decision" onClose={onClose}>
      <p className="section-note">
        Title + what-must-be-decided are required (PEC-DEC-001). Preparer and authority are
        distinct on purpose (§4.6). Package-level decisions drive package health (PH-A2).
      </p>
      <form className="stack" onSubmit={submit}>
        <label>Title *
          <input required value={title} onChange={(e) => setTitle(e.target.value)} />
        </label>
        <label>What must be decided? *
          <textarea required value={statement} onChange={(e) => setStatement(e.target.value)} />
        </label>
        <div className="row">
          <label>Authority *
            <select required value={authorityId} onChange={(e) => setAuthorityId(e.target.value)}>
              <option value="">—</option>
              {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
            </select>
          </label>
          <label>Preparer
            <select value={preparerId} onChange={(e) => setPreparerId(e.target.value)}>
              <option value="">—</option>
              {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
            </select>
          </label>
        </div>
        <div className="row">
          <label>Need by
            <input type="date" value={needBy} onChange={(e) => setNeedBy(e.target.value)} />
          </label>
          <label>Package
            <select value={packageId} onChange={(e) => setPackageId(e.target.value)}>
              <option value="">—</option>
              {(packages.data ?? []).map((pk: any) => <option key={pk.id} value={pk.id}>{pk.code} — {pk.name}</option>)}
            </select>
          </label>
        </div>
        <label>Options considered
          <textarea value={optionsConsidered} onChange={(e) => setOptionsConsidered(e.target.value)} />
        </label>
        <label>Recommendation
          <textarea value={recommendation} onChange={(e) => setRecommendation(e.target.value)} />
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !authorityId}>Create</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

function AssignPreparerDrawer({ row, onClose }: { row: any; onClose(): void }): JSX.Element {
  const { pid, people, refresh, toast } = useApp()
  const [preparerId, setPreparerId] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    try {
      await api.post(p(pid, `decisions/${row.id}/progress`), {
        event: 'assign_preparer', version: row.version, preparerId: Number(preparerId),
      })
      toast(`${row.ref}: preparer assigned`)
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title={<>Assign preparer — <span className="mono">{row.ref}</span></>} onClose={onClose}>
      <form className="stack" onSubmit={submit}>
        <label>Preparer * (prepares the package; the authority decides — §4.6)
          <select required value={preparerId} onChange={(e) => setPreparerId(e.target.value)}>
            <option value="">—</option>
            {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
          </select>
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !preparerId}>Assign</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

function DecisionOutcomeDrawer({ row, onClose }: { row: any; onClose(): void }): JSX.Element {
  const { pid, people, refresh, toast } = useApp()
  const deliverables = useLoad(() => api.get(p(pid, 'deliverables?view=master')), [pid])
  const [outcome, setOutcome] = useState('select')
  const [rationale, setRationale] = useState('')
  const [fuTitle, setFuTitle] = useState('')
  const [fuOwnerId, setFuOwnerId] = useState('')
  const [fuNeedBy, setFuNeedBy] = useState('')
  const [fuAnchorId, setFuAnchorId] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    try {
      // PEC-DEC-003: outcome + rationale by the authority; follow-up work items are
      // created linked relation=follow_up server-side (§4.6).
      await api.post(p(pid, `decisions/${row.id}/outcome`), {
        version: row.version, outcome, rationale,
        followUps: fuTitle ? [{
          title: fuTitle, ownerId: Number(fuOwnerId), needBy: fuNeedBy || null,
          anchorType: 'deliverable', anchorId: Number(fuAnchorId),
        }] : undefined,
      })
      toast(`${row.ref} decided: ${outcome}`)
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title={<>Record outcome — <span className="mono">{row.ref}</span></>} onClose={onClose}>
      <p className="section-note">{row.title} — {row.statement}</p>
      <form className="stack" onSubmit={submit}>
        <label>Outcome (PEC-DEC-003)
          <select value={outcome} onChange={(e) => setOutcome(e.target.value)}>
            {DECISION_OUTCOMES.map((o) => <option key={o} value={o}>{o.replaceAll('_', ' ')}</option>)}
          </select>
        </label>
        <label>Rationale *
          <textarea required value={rationale} onChange={(e) => setRationale(e.target.value)} />
        </label>
        <h3>Follow-up work item (optional)</h3>
        <label>Title (leave blank for none)
          <input value={fuTitle} onChange={(e) => setFuTitle(e.target.value)} />
        </label>
        {fuTitle && (
          <>
            <div className="row">
              <label>Owner *
                <select value={fuOwnerId} onChange={(e) => setFuOwnerId(e.target.value)}>
                  <option value="">—</option>
                  {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
                </select>
              </label>
              <label>Need by
                <input type="date" value={fuNeedBy} onChange={(e) => setFuNeedBy(e.target.value)} />
              </label>
            </div>
            <label>Anchor deliverable * (work items are always anchored, I-2)
              <select value={fuAnchorId} onChange={(e) => setFuAnchorId(e.target.value)}>
                <option value="">—</option>
                {(deliverables.data ?? []).map((d: any) => (
                  <option key={d.id} value={d.id}>{d.docNo} — {d.title}</option>
                ))}
              </select>
            </label>
          </>
        )}
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !rationale || Boolean(fuTitle && (!fuOwnerId || !fuAnchorId))}>Record</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

function SupersedeDecisionDrawer({ row, all, onClose }: { row: any; all: any[]; onClose(): void }): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const [replacementId, setReplacementId] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)
  const candidates = all.filter((d) => d.id !== row.id && d.state !== 'superseded')

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    try {
      await api.post(p(pid, `decisions/${row.id}/supersede`), {
        version: row.version, replacementId: Number(replacementId),
      })
      toast(`${row.ref} superseded — remains visible, linked (I-10); affected owners notified`)
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title={<>Supersede — <span className="mono">{row.ref}</span></>} onClose={onClose}>
      <p className="section-note">
        Supersession requires the replacement decision (I-10); the old row stays visible and
        linked, and owners of affected records are flagged for basis drift.
      </p>
      <form className="stack" onSubmit={submit}>
        <label>Replacement decision *
          <select required value={replacementId} onChange={(e) => setReplacementId(e.target.value)}>
            <option value="">—</option>
            {candidates.map((d) => <option key={d.id} value={d.id}>{d.ref} — {d.title}</option>)}
          </select>
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !replacementId}>Supersede</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ================================================================ risks

/** PEC-RISK-001: risk register with cause, consequence, owner, P×I, mitigation, need-by. */
function RisksTab(): JSX.Element {
  const { pid } = useApp()
  const person = usePerson()
  const { data, error } = useLoad(() => api.get(p(pid, 'risks')), [pid])
  const [editing, setEditing] = useState<any>(null) // 'new' | row
  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const pxi = (r: any): number | null =>
    r.probability == null || r.impact == null ? null : r.probability * r.impact

  const cols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span> },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'cause', label: 'Cause', render: (r) => <span className="small">{r.cause}</span> },
    { key: 'consequence', label: 'Consequence', render: (r) => <span className="small">{r.consequence}</span> },
    { key: 'owner', label: 'Owner', render: (r) => <span className="small">{person(r.ownerId)}</span> },
    { key: 'p', label: 'P', render: (r) => r.probability ?? <span className="muted">—</span> },
    { key: 'i', label: 'I', render: (r) => r.impact ?? <span className="muted">—</span> },
    {
      key: 'pxi', label: 'P×I', csv: (r) => pxi(r), render: (r) => {
        const v = pxi(r)
        if (v == null) return <span className="muted">—</span>
        return <b className={v >= 15 ? 'badge red' : ''}>{v}</b>
      },
    },
    { key: 'mitigation', label: 'Mitigation', render: (r) => <span className="small">{r.mitigation}</span> },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} /> },
  ]

  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: '.75rem' }}>
        <p className="section-note" style={{ flex: 1 }}>
          Risks of change (PRD §12.10) — click a row to edit. Treatment actions are work
          items anchored to the risk.
        </p>
        <button className="btn small" onClick={() => setEditing('new')}>+ New risk</button>
      </div>
      <RegisterTable cols={cols} rows={data} exportName="risk-register.csv" onRowClick={(r) => setEditing(r)} />
      {editing && <RiskDrawer row={editing === 'new' ? null : editing} onClose={() => setEditing(null)} />}
    </div>
  )
}

function RiskDrawer({ row, onClose }: { row: any; onClose(): void }): JSX.Element {
  const { pid, people, refresh, toast } = useApp()
  const [title, setTitle] = useState(row?.title ?? '')
  const [cause, setCause] = useState(row?.cause ?? '')
  const [consequence, setConsequence] = useState(row?.consequence ?? '')
  const [ownerId, setOwnerId] = useState(row?.ownerId ? String(row.ownerId) : '')
  const [probability, setProbability] = useState(row?.probability ? String(row.probability) : '')
  const [impact, setImpact] = useState(row?.impact ? String(row.impact) : '')
  const [mitigation, setMitigation] = useState(row?.mitigation ?? '')
  const [needBy, setNeedBy] = useState(row?.needBy ?? '')
  const [state, setState] = useState(row?.state ?? 'open')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    const fields = {
      title, cause: cause || undefined, consequence: consequence || undefined,
      ownerId: ownerId ? Number(ownerId) : undefined,
      probability: probability ? Number(probability) : undefined,
      impact: impact ? Number(impact) : undefined,
      mitigation: mitigation || undefined, needBy: needBy || undefined,
    }
    try {
      if (row) {
        await api.put(p(pid, `risks/${row.id}`), { version: row.version, ...fields, state })
        toast(`${row.ref} updated`)
      } else {
        const r = await api.post(p(pid, 'risks'), fields)
        toast(`${r.ref} raised`)
      }
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title={row ? <>Edit risk — <span className="mono">{row.ref}</span></> : 'New risk'} onClose={onClose}>
      <form className="stack" onSubmit={submit}>
        <label>Title *
          <input required value={title} onChange={(e) => setTitle(e.target.value)} />
        </label>
        <label>Cause
          <input value={cause} onChange={(e) => setCause(e.target.value)} />
        </label>
        <label>Consequence
          <input value={consequence} onChange={(e) => setConsequence(e.target.value)} />
        </label>
        <div className="row">
          <label>Owner
            <select value={ownerId} onChange={(e) => setOwnerId(e.target.value)}>
              <option value="">—</option>
              {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
            </select>
          </label>
          <label>Probability (1–5)
            <select value={probability} onChange={(e) => setProbability(e.target.value)}>
              <option value="">—</option>
              {[1, 2, 3, 4, 5].map((n) => <option key={n} value={n}>{n}</option>)}
            </select>
          </label>
          <label>Impact (1–5)
            <select value={impact} onChange={(e) => setImpact(e.target.value)}>
              <option value="">—</option>
              {[1, 2, 3, 4, 5].map((n) => <option key={n} value={n}>{n}</option>)}
            </select>
          </label>
        </div>
        <label>Mitigation
          <textarea value={mitigation} onChange={(e) => setMitigation(e.target.value)} />
        </label>
        <div className="row">
          <label>Need by
            <input type="date" value={needBy ?? ''} onChange={(e) => setNeedBy(e.target.value)} />
          </label>
          {row && (
            <label>State
              <select value={state} onChange={(e) => setState(e.target.value)}>
                <option value="open">open</option>
                <option value="mitigating">mitigating</option>
                <option value="closed">closed</option>
              </select>
            </label>
          )}
        </div>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !title}>{row ? 'Save' : 'Create'}</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ================================================================ interfaces

/** PEC-INT-001: interface register — giving/receiving party, required info, need-by, state. */
function InterfacesTab(): JSX.Element {
  const { pid } = useApp()
  // PEC-INT-002 (P2): dedicated register with aging and giving/receiving filters
  const [giving, setGiving] = useState('')
  const [receiving, setReceiving] = useState('')
  const { data: packages } = useLoad<any[]>(() => api.get(p(pid, 'packages')), [pid])
  const { data, error } = useLoad(() => api.get(p(pid,
    `interfaces?giving=${giving}&receiving=${receiving}`)), [pid, giving, receiving])
  const [editing, setEditing] = useState<any>(null) // 'new' | row
  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const cols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span> },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'parties', label: 'Giving → receiving', render: (r) => <span className="small">{r.givingParty}{r.givingPackageCode ? ` (${r.givingPackageCode})` : ''} → {r.receivingParty}{r.receivingPackageCode ? ` (${r.receivingPackageCode})` : ''}</span> },
    { key: 'info', label: 'Required info', render: (r) => <span className="small">{r.requiredInfo}</span> },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
    {
      key: 'aging', label: 'Aging (wd overdue)', render: (r) => r.overdueWd > 0
        ? <span className={`badge ${r.aging === 'red' ? 'red' : 'amber'}`}>{r.overdueWd} wd</span>
        : <span className="muted small">—</span>,
      csv: (r) => r.overdueWd,
    },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} /> },
    { key: 'log', label: 'Log', render: (r) => <span className="small muted">{r.log}</span> },
  ]

  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: '.75rem' }}>
        <p className="section-note" style={{ flex: 1 }}>
          Cross-package information obligations (OM-7) — click a row to edit. Delivered/closed
          interfaces satisfy interface-type conditions (§5.3). Aging feeds package health
          (PEC-PKG-008).
        </p>
        <button className="btn small" onClick={() => setEditing('new')}>+ New interface</button>
      </div>
      <div className="filters">
        <label>giving package{' '}
          <select value={giving} onChange={(e) => setGiving(e.target.value)}>
            <option value="">any</option>
            {(packages ?? []).map((k: any) => <option key={k.id} value={k.id}>{k.code}</option>)}
          </select>
        </label>
        <label>receiving package{' '}
          <select value={receiving} onChange={(e) => setReceiving(e.target.value)}>
            <option value="">any</option>
            {(packages ?? []).map((k: any) => <option key={k.id} value={k.id}>{k.code}</option>)}
          </select>
        </label>
      </div>
      <RegisterTable cols={cols} rows={data} exportName="interface-register.csv" onRowClick={(r) => setEditing(r)} />
      {editing && <InterfaceDrawer row={editing === 'new' ? null : editing} onClose={() => setEditing(null)} />}
    </div>
  )
}

function InterfaceDrawer({ row, onClose }: { row: any; onClose(): void }): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const [title, setTitle] = useState(row?.title ?? '')
  const [givingParty, setGivingParty] = useState(row?.givingParty ?? '')
  const [receivingParty, setReceivingParty] = useState(row?.receivingParty ?? '')
  const [requiredInfo, setRequiredInfo] = useState(row?.requiredInfo ?? '')
  const [needBy, setNeedBy] = useState(row?.needBy ?? '')
  const [state, setState] = useState(row?.state ?? 'open')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    const fields = {
      title, givingParty, receivingParty,
      requiredInfo: requiredInfo || undefined, needBy: needBy || undefined,
    }
    try {
      if (row) {
        await api.put(p(pid, `interfaces/${row.id}`), { version: row.version, ...fields, state })
        toast(`${row.ref} updated`)
      } else {
        const r = await api.post(p(pid, 'interfaces'), fields)
        toast(`${r.ref} created`)
      }
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title={row ? <>Edit interface — <span className="mono">{row.ref}</span></> : 'New interface'} onClose={onClose}>
      <form className="stack" onSubmit={submit}>
        <label>Title *
          <input required value={title} onChange={(e) => setTitle(e.target.value)} />
        </label>
        <div className="row">
          <label>Giving party *
            <input required value={givingParty} onChange={(e) => setGivingParty(e.target.value)} />
          </label>
          <label>Receiving party *
            <input required value={receivingParty} onChange={(e) => setReceivingParty(e.target.value)} />
          </label>
        </div>
        <label>Required information
          <textarea value={requiredInfo} onChange={(e) => setRequiredInfo(e.target.value)} />
        </label>
        <div className="row">
          <label>Need by
            <input type="date" value={needBy ?? ''} onChange={(e) => setNeedBy(e.target.value)} />
          </label>
          {row && (
            <label>State
              <select value={state} onChange={(e) => setState(e.target.value)}>
                {['open', 'agreed', 'delivered', 'closed', 'cancelled'].map((s) => <option key={s} value={s}>{s}</option>)}
              </select>
            </label>
          )}
        </div>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !title || !givingParty || !receivingParty}>{row ? 'Save' : 'Create'}</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ================================================================ holds

const HOLD_CAUSES = [
  'information', 'decision', 'approval', 'resource', 'client_input', 'interface', 'vendor_data', 'other',
] as const

const HOLD_RESOLUTION_KINDS = [
  'decision_recorded', 'information_received', 'resource_assigned', 'approval_recorded', 'other',
] as const

/** Hold register (OM-2, I-3): typed cause, owner, need-by, age, and what each hold blocks. */
function HoldsTab(): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const person = usePerson()
  const { data, error } = useLoad(() => api.get(p(pid, 'holds')), [pid])
  const [raising, setRaising] = useState(false)
  const [resolving, setResolving] = useState<any>(null)
  const [actionError, setActionError] = useState<any>(null)
  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const withdraw = async (r: any) => {
    const reason = window.prompt(`Withdraw ${r.ref} — reason (recorded):`)
    if (!reason) return
    setActionError(null)
    try {
      await api.post(p(pid, `holds/${r.id}/withdraw`), { version: r.version, reason })
      toast(`${r.ref} withdrawn — blocked records released`)
      refresh()
    } catch (err) { setActionError(err) }
  }

  const cols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span> },
    { key: 'cause', label: 'Cause', render: (r) => <span className="badge hold">{r.cause.replaceAll('_', ' ')}</span> },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'owner', label: 'Owner', render: (r) => <span className="small">{person(r.ownerId)}</span> },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
    {
      // hold age signal (§6.3; warn > 7 wd, escalate > 14 wd defaults)
      key: 'age', label: 'Age (wd)', render: (r) =>
        <span className={r.ageWd > 14 ? 'badge red' : r.ageWd > 7 ? 'badge amber' : 'mono'}>{r.ageWd}</span>,
    },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} /> },
    {
      key: 'targets', label: 'Blocks', render: (r) =>
        <span className="small">{r.targets.map((t: any) => `${t.targetType.replaceAll('_', ' ')}#${t.targetId}`).join(', ')}</span>,
      csv: (r) => r.targets.map((t: any) => `${t.targetType}#${t.targetId}`).join('; '),
    },
    {
      key: 'act', label: '', csv: () => null, render: (r) => r.state === 'active'
        ? (
          <span className="nowrap">
            <button className="btn small" onClick={() => setResolving(r)}>Resolve</button>{' '}
            <button className="btn small secondary" onClick={() => withdraw(r)}>Withdraw</button>
          </span>
        )
        : null,
    },
  ]

  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: '.75rem' }}>
        <p className="section-note" style={{ flex: 1 }}>
          A hold is a first-class blocking record — typed cause, owner, need-by all required
          (I-3). “Blocked” on targets is derived from these links, never stored.
        </p>
        <button className="btn small" onClick={() => setRaising(true)}>+ Raise hold</button>
      </div>
      <ErrorBox error={actionError} />
      <RegisterTable cols={cols} rows={data} exportName="hold-register.csv" />
      {raising && <RaiseHoldDrawer onClose={() => setRaising(false)} />}
      {resolving && <ResolveHoldDrawer row={resolving} onClose={() => setResolving(null)} />}
    </div>
  )
}

function RaiseHoldDrawer({ onClose }: { onClose(): void }): JSX.Element {
  const { pid, people, refresh, toast } = useApp()
  const deliverables = useLoad(() => api.get(p(pid, 'deliverables?view=master')), [pid])
  const [title, setTitle] = useState('')
  const [cause, setCause] = useState('information')
  const [statement, setStatement] = useState('')
  const [ownerId, setOwnerId] = useState('')
  const [needBy, setNeedBy] = useState('')
  const [targetIds, setTargetIds] = useState<string[]>([])
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    try {
      const r = await api.post(p(pid, 'holds'), {
        title, cause, statement: statement || undefined,
        ownerId: Number(ownerId), needBy,
        targets: targetIds.map((id) => ({ targetType: 'deliverable', targetId: Number(id) })),
      })
      toast(`${r.ref} raised — owners of blocked records notified`)
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title="Raise hold" onClose={onClose}>
      <p className="section-note">
        Typed cause, owner, need-by, and at least one blocked record are required at
        creation (I-3) — the server rejects anything less.
      </p>
      <form className="stack" onSubmit={submit}>
        <label>Title *
          <input required value={title} onChange={(e) => setTitle(e.target.value)} />
        </label>
        <label>Cause
          <select value={cause} onChange={(e) => setCause(e.target.value)}>
            {HOLD_CAUSES.map((c) => <option key={c} value={c}>{c.replaceAll('_', ' ')}</option>)}
          </select>
        </label>
        <label>Statement
          <textarea value={statement} onChange={(e) => setStatement(e.target.value)} />
        </label>
        <div className="row">
          <label>Owner * (chases the resolution)
            <select required value={ownerId} onChange={(e) => setOwnerId(e.target.value)}>
              <option value="">—</option>
              {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
            </select>
          </label>
          <label>Need by *
            <input required type="date" value={needBy} onChange={(e) => setNeedBy(e.target.value)} />
          </label>
        </div>
        <label>Blocks deliverables * (hold ⌘/Ctrl to select several)
          <select multiple size={Math.min((deliverables.data ?? []).length || 4, 10)} value={targetIds}
            onChange={(e) => setTargetIds(Array.from(e.target.selectedOptions, (o) => o.value))}>
            {(deliverables.data ?? []).map((d: any) => (
              <option key={d.id} value={d.id}>{d.docNo} — {d.title}</option>
            ))}
          </select>
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !ownerId || !needBy || targetIds.length === 0}>Raise</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

function ResolveHoldDrawer({ row, onClose }: { row: any; onClose(): void }): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const [resolutionKind, setResolutionKind] = useState('information_received')
  const [note, setNote] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true); setError(null)
    try {
      // §4.3: resolution names the resolving fact; owners of unblocked records are notified
      await api.post(p(pid, `holds/${row.id}/resolve`), {
        version: row.version, resolutionKind, note: note || undefined,
      })
      toast(`${row.ref} resolved (${resolutionKind.replaceAll('_', ' ')})`)
      refresh(); onClose()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title={<>Resolve — <span className="mono">{row.ref}</span></>} onClose={onClose}>
      <p className="section-note">{row.title} <span className="badge hold">{row.cause.replaceAll('_', ' ')}</span></p>
      <form className="stack" onSubmit={submit}>
        <label>Resolving fact (§7.3)
          <select value={resolutionKind} onChange={(e) => setResolutionKind(e.target.value)}>
            {HOLD_RESOLUTION_KINDS.map((k) => <option key={k} value={k}>{k.replaceAll('_', ' ')}</option>)}
          </select>
        </label>
        <label>Note
          <textarea value={note} onChange={(e) => setNote(e.target.value)} />
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy}>Resolve</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}
