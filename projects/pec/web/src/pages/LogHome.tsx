/**
 * Action & Hold Log — Coordinator home: "Is anything falling through?" (PRD §12.5).
 * Tab 1 — the unified open-items register with typed filters (PEC-AHL-001).
 * Tab 2 — the triage queue (PEC-AHL-006): open triage, then disposition each intake
 * item into controlled records (PEC-AHL-004/005), statement kept verbatim (OM-3).
 * Every row and derivation is server-truth; this page renders and posts (SPEC §1).
 */

import { useMemo, useRef, useState } from 'react'
import { api, p } from '../api.ts'
import {
  Drawer, ErrorBox, RegisterTable, StateTag, fmtDate, useApp, useLoad, usePerson,
} from '../shared.tsx'
import type { Col } from '../shared.tsx'

// Option lists only (labels mirror SPEC §3.3/§3.4 enums) — all validation is server-side.
const HOLD_CAUSES = ['information', 'decision', 'approval', 'resource', 'client_input', 'interface', 'vendor_data', 'other'] as const
const WORK_ITEM_KINDS = ['action', 'coordination', 'risk_treatment', 'rework', 'other'] as const
const LOGS = ['package', 'internal', 'client'] as const
const DISPOSITIONS = ['converted', 'merged', 'duplicate', 'rejected', 'parked'] as const

export function LogPage(): JSX.Element {
  const [tab, setTab] = useState<'open' | 'triage'>('open')
  return (
    <div>
      <h1>Action &amp; Hold Log — is anything falling through?</h1>
      <div className="filters">
        <button className={`btn small${tab === 'open' ? '' : ' secondary'}`} onClick={() => setTab('open')}>
          All open items
        </button>
        <button className={`btn small${tab === 'triage' ? '' : ' secondary'}`} onClick={() => setTab('triage')}>
          Triage queue (intake)
        </button>
      </div>
      {tab === 'open' ? <OpenItemsTab /> : <TriageTab />}
    </div>
  )
}

// ---------- Tab 1: unified register (PEC-AHL-001) ----------

interface LogRow {
  recordType: string
  id: number
  ref: string
  title: string
  log: string
  packageId: number | null
  ownerId: number | null
  state: string
  ageWd: number
  needBy: string | null
  overdue: boolean
  holdCause: string | null
  anchorStatus: 'anchored' | 'unanchored'
}

function OpenItemsTab(): JSX.Element {
  const { pid, people } = useApp()
  const person = usePerson()
  const [log, setLog] = useState('')
  const [type, setType] = useState('')
  const [owner, setOwner] = useState('')
  const [cause, setCause] = useState('')
  const [overdue, setOverdue] = useState(false)
  const [anchored, setAnchored] = useState('')

  // PEC-AHL-001: the union of open work items, active holds, open interfaces, and
  // untriaged intake items is composed server-side; filters are query params only.
  const qs = useMemo(() => {
    const q = new URLSearchParams()
    if (log) q.set('log', log)
    if (type) q.set('type', type)
    if (owner) q.set('owner', owner)
    if (cause) q.set('cause', cause)
    if (overdue) q.set('overdue', 'true')
    if (anchored) q.set('anchored', anchored)
    return q.toString()
  }, [log, type, owner, cause, overdue, anchored])
  const { data, error } = useLoad<LogRow[]>(() => api.get(p(pid, qs ? `log?${qs}` : 'log')), [pid, qs])

  const cols: Array<Col<LogRow>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span> },
    { key: 'type', label: 'Type', render: (r) => <span className="small">{r.recordType.replaceAll('_', ' ')}</span> },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'log', label: 'Log', render: (r) => <span className="small muted">{r.log}</span> },
    { key: 'owner', label: 'Owner', render: (r) => <span className="small">{person(r.ownerId)}</span> },
    { key: 'age', label: 'Age (wd)', render: (r) => r.ageWd },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
    {
      key: 'overdue', label: 'Overdue',
      render: (r) => r.overdue ? <span className="badge red">overdue</span> : <span className="muted small">—</span>,
      csv: (r) => (r.overdue ? 'yes' : ''),
    },
    {
      key: 'cause', label: 'Hold cause',
      render: (r) => r.holdCause
        ? <span className="badge hold">{r.holdCause.replaceAll('_', ' ')}</span>
        : <span className="muted small">—</span>,
      csv: (r) => r.holdCause ?? '',
    },
    {
      // I-2: unanchored items stay visible and flagged — never hidden, never in rollups
      key: 'anchor', label: 'Anchor',
      render: (r) => r.anchorStatus === 'unanchored'
        ? <span className="badge amber">unanchored</span>
        : <span className="muted small">anchored</span>,
      csv: (r) => r.anchorStatus,
    },
  ]

  return (
    <div>
      <p className="section-note">
        One register: open work items, active holds, open interfaces, and untriaged intake
        items — typed rows, never mixed types in one field (PEC-AHL-001).
      </p>
      <div className="filters">
        <select value={log} onChange={(e) => setLog(e.target.value)}>
          <option value="">all logs</option>
          {LOGS.map((l) => <option key={l} value={l}>{l}</option>)}
        </select>
        <select value={type} onChange={(e) => setType(e.target.value)}>
          <option value="">all types</option>
          <option value="work_item">work item</option>
          <option value="hold">hold</option>
          <option value="interface_item">interface item</option>
          <option value="intake_item">intake item</option>
        </select>
        <select value={owner} onChange={(e) => setOwner(e.target.value)}>
          <option value="">any owner</option>
          {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
        </select>
        <select value={cause} onChange={(e) => setCause(e.target.value)}>
          <option value="">any hold cause</option>
          {HOLD_CAUSES.map((c) => <option key={c} value={c}>{c.replaceAll('_', ' ')}</option>)}
        </select>
        <label className="small">
          <input type="checkbox" checked={overdue} onChange={(e) => setOverdue(e.target.checked)} /> overdue only
        </label>
        <select value={anchored} onChange={(e) => setAnchored(e.target.value)}>
          <option value="">anchored + unanchored</option>
          <option value="true">anchored</option>
          <option value="false">unanchored</option>
        </select>
      </div>
      {error && <ErrorBox error={{ message: error }} />}
      {!data && !error && <p className="muted">loading…</p>}
      {data && <RegisterTable cols={cols} rows={data} exportName="action-hold-log.csv" />}
    </div>
  )
}

// ---------- Tab 2: triage queue (PEC-AHL-006) ----------

interface IntakeRow {
  id: number
  ref: string
  statementVerbatim: string
  quickType: string
  anchorSuggestion: string | null
  needBy: string | null
  suggestedOwnerId: number | null
  log: string
  raisedBy: number
  raisedAt: string
  state: string
  disposition: string | null
  dispositionNote: string | null
  mergedIntoIntakeId: number | null
  untriagedAgeWd: number
  version: number
  links: Array<{ record_type: string; record_id: number }>
}

/** Untriaged-intake-age signal defaults 2/5 wd (SPEC §6.3) — display only. */
function AgeBadge({ wd }: { wd: number }): JSX.Element {
  if (wd > 5) return <span className="badge red">{wd} wd</span>
  if (wd > 2) return <span className="badge amber">{wd} wd</span>
  return <span className="mono">{wd}</span>
}

function TriageTab(): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const person = usePerson()
  const [triaging, setTriaging] = useState<IntakeRow | null>(null)
  const [actionError, setActionError] = useState<any>(null)
  const [busyId, setBusyId] = useState<number | null>(null)
  // server sorts by untriagedAgeWd desc — oldest concern first (PEC-AHL-006)
  const { data: queue, error } = useLoad<IntakeRow[]>(() => api.get(p(pid, 'intake')), [pid])
  const { data: done } = useLoad<IntakeRow[]>(() => api.get(p(pid, 'intake?state=dispositioned')), [pid])

  const openTriage = async (r: IntakeRow) => {
    setBusyId(r.id)
    setActionError(null)
    try {
      await api.post(p(pid, `intake/${r.id}/open-triage`), { version: r.version })
      toast(`${r.ref} — triage opened`)
      refresh()
    } catch (err) {
      setActionError(err)
    } finally {
      setBusyId(null)
    }
  }

  const cols: Array<Col<IntakeRow>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.ref}</span> },
    {
      // OM-3: the verbatim statement IS the record — shown in full, never truncated
      key: 'stmt', label: 'Statement (verbatim)',
      render: (r) => <span style={{ whiteSpace: 'pre-wrap' }}>{r.statementVerbatim}</span>,
    },
    { key: 'type', label: 'Quick type', render: (r) => <span className="small">{r.quickType.replaceAll('_', ' ')}</span> },
    { key: 'raisedBy', label: 'Raised by', render: (r) => <span className="small">{person(r.raisedBy)}</span> },
    { key: 'age', label: 'Age (wd)', render: (r) => <AgeBadge wd={r.untriagedAgeWd} /> },
    {
      key: 'anchor', label: 'Suggested anchor',
      render: (r) => r.anchorSuggestion ? <span className="small">{r.anchorSuggestion}</span> : <span className="muted small">—</span>,
    },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} /> },
    {
      key: 'act', label: '',
      render: (r) => r.state === 'raised'
        ? <button className="btn small" disabled={busyId === r.id} onClick={() => openTriage(r)}>Open triage</button>
        : r.state === 'in_triage'
          ? <button className="btn small" onClick={() => { setActionError(null); setTriaging(r) }}>Disposition</button>
          : null,
      csv: (r) => r.state,
    },
  ]

  if (error) return <ErrorBox error={{ message: error }} />
  if (!queue) return <p className="muted">loading…</p>

  return (
    <div>
      <p className="section-note">
        Everything raised lands here verbatim; nothing is lost between raise and routing
        (PEC-AHL-006). Triage converts, merges, or parks — with a note, never silently.
      </p>
      <ErrorBox error={actionError} />
      <RegisterTable cols={cols} rows={queue} />

      {/* Dispositioned trail with back-links to created records (PEC-AHL-005) */}
      <details style={{ marginTop: '1rem' }}>
        <summary className="small muted">Dispositioned ({done?.length ?? 0})</summary>
        <table className="reg" style={{ marginTop: '.4rem' }}>
          <tbody>
            {(done ?? []).map((d) => (
              <tr key={d.id}>
                <td className="mono nowrap">{d.ref}</td>
                <td className="small">{d.statementVerbatim}</td>
                <td><StateTag s={d.disposition ?? 'dispositioned'} /></td>
                <td className="small muted">
                  {d.dispositionNote ?? '—'}
                  {d.mergedIntoIntakeId != null && <> · merged into intake #{d.mergedIntoIntakeId}</>}
                </td>
                <td className="small mono">
                  {d.links.length > 0
                    ? d.links.map((l) => `${l.record_type.replaceAll('_', ' ')} #${l.record_id}`).join(', ')
                    : '—'}
                </td>
              </tr>
            ))}
            {(done ?? []).length === 0 && <tr><td colSpan={5} className="muted small">no dispositioned items</td></tr>}
          </tbody>
        </table>
      </details>

      {triaging && (
        <TriageDrawer
          item={triaging}
          others={queue.filter((x) => x.id !== triaging.id).map((x) => ({ id: x.id, ref: x.ref }))}
          onClose={() => setTriaging(null)}
        />
      )}
    </div>
  )
}

// ---------- Disposition drawer — the core coordinator tool (PEC-AHL-004/005) ----------

interface DraftBase { key: number }
interface WiDraft extends DraftBase {
  kind: 'work_item'
  title: string; statement: string; anchorType: 'deliverable' | 'package'; anchorId: string
  ownerId: string; needBy: string; wiKind: string; log: string
}
interface HoldDraft extends DraftBase {
  kind: 'hold'
  title: string; cause: string; statement: string; ownerId: string; needBy: string; deliverableId: string
}
interface RiskDraft extends DraftBase {
  kind: 'risk'
  title: string; cause: string; consequence: string; ownerId: string
  probability: string; impact: string; needBy: string
}
interface DecisionDraft extends DraftBase {
  kind: 'decision'
  title: string; statement: string; authorityId: string; needBy: string; packageId: string
}
interface InterfaceDraft extends DraftBase {
  kind: 'interface'
  title: string; givingParty: string; receivingParty: string; requiredInfo: string; needBy: string
}
type Draft = WiDraft | HoldDraft | RiskDraft | DecisionDraft | InterfaceDraft

function TriageDrawer({ item, others, onClose }: {
  item: IntakeRow
  others: Array<{ id: number; ref: string }>
  onClose(): void
}): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const person = usePerson()
  const [disposition, setDisposition] = useState<string>('converted')
  const [note, setNote] = useState('')
  const [mergedInto, setMergedInto] = useState('')
  const [drafts, setDrafts] = useState<Draft[]>([])
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)
  const keyRef = useRef(1)

  // Anchor pickers (PEC-AHL-005): doc list + packages, both server-provided
  const { data: dels } = useLoad<any[]>(() => api.get(p(pid, 'deliverables?view=master')), [pid])
  const { data: pkgs } = useLoad<any[]>(() => api.get(p(pid, 'packages')), [pid])

  const nk = () => keyRef.current++
  const addDraft = (d: Draft) => setDrafts((ds) => [...ds, d])
  const replace = (next: Draft) => setDrafts((ds) => ds.map((x) => (x.key === next.key ? next : x)))
  const remove = (key: number) => setDrafts((ds) => ds.filter((x) => x.key !== key))
  const suggestedOwner = item.suggestedOwnerId != null ? String(item.suggestedOwnerId) : ''

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true)
    setError(null)
    try {
      // Mutations always carry the version read (PEC-NFR-004)
      const body: Record<string, unknown> = { version: item.version, disposition, note: note || undefined }
      if (disposition === 'merged') body.mergedIntoIntakeId = Number(mergedInto)
      if (disposition === 'converted') {
        // One intake item → any number of controlled records, atomically (PEC-AHL-005)
        body.records = {
          workItems: drafts.filter((d): d is WiDraft => d.kind === 'work_item').map((d) => ({
            title: d.title, statement: d.statement || undefined, kind: d.wiKind, log: d.log,
            anchorType: d.anchorType, anchorId: Number(d.anchorId),
            ownerId: Number(d.ownerId), needBy: d.needBy || null,
          })),
          holds: drafts.filter((d): d is HoldDraft => d.kind === 'hold').map((d) => ({
            title: d.title, cause: d.cause, statement: d.statement || undefined,
            ownerId: Number(d.ownerId), needBy: d.needBy,
            targets: [{ targetType: 'deliverable', targetId: Number(d.deliverableId) }],
          })),
          risks: drafts.filter((d): d is RiskDraft => d.kind === 'risk').map((d) => ({
            title: d.title, cause: d.cause || undefined, consequence: d.consequence || undefined,
            ownerId: d.ownerId ? Number(d.ownerId) : undefined,
            probability: d.probability ? Number(d.probability) : undefined,
            impact: d.impact ? Number(d.impact) : undefined,
            needBy: d.needBy || undefined,
          })),
          decisions: drafts.filter((d): d is DecisionDraft => d.kind === 'decision').map((d) => ({
            title: d.title, statement: d.statement, authorityId: Number(d.authorityId),
            needBy: d.needBy || undefined, packageId: d.packageId ? Number(d.packageId) : undefined,
          })),
          interfaces: drafts.filter((d): d is InterfaceDraft => d.kind === 'interface').map((d) => ({
            title: d.title, givingParty: d.givingParty, receivingParty: d.receivingParty,
            requiredInfo: d.requiredInfo || undefined, needBy: d.needBy || undefined,
          })),
        }
      }
      const r = await api.post(p(pid, `intake/${item.id}/triage`), body)
      toast(disposition === 'converted'
        ? `${item.ref} converted → ${(r.created as Array<{ ref: string }>).map((c) => c.ref).join(', ')}`
        : `${item.ref} dispositioned: ${disposition}`)
      refresh()
      onClose()
    } catch (err) {
      setError(err) // 409 VERSION_CONFLICT / validation errors render via ErrorBox
    } finally {
      setBusy(false)
    }
  }

  return (
    <Drawer title={`Triage ${item.ref}`} onClose={onClose}>
      {/* OM-3: the concern as raised stays visible verbatim while building records */}
      <div className="card" style={{ marginBottom: '.7rem', background: '#fbfcfd' }}>
        <div className="small muted">
          {item.quickType.replaceAll('_', ' ')} · raised by {person(item.raisedBy)} · {fmtDate(item.raisedAt)}
          {' '}· need-by {fmtDate(item.needBy)} · suggested owner {person(item.suggestedOwnerId)}
          {item.anchorSuggestion && <> · suggested anchor: {item.anchorSuggestion}</>}
        </div>
        <p style={{ margin: '.35rem 0 0', whiteSpace: 'pre-wrap' }}>{item.statementVerbatim}</p>
      </div>

      <form className="stack" onSubmit={submit}>
        {/* PEC-AHL-004: every disposition is recorded — nothing vanishes from the queue */}
        <label>Disposition
          <select value={disposition} onChange={(e) => setDisposition(e.target.value)}>
            {DISPOSITIONS.map((d) => <option key={d} value={d}>{d}</option>)}
          </select>
        </label>
        {disposition === 'merged' && (
          <label>Merged into *
            <select required value={mergedInto} onChange={(e) => setMergedInto(e.target.value)}>
              <option value="">—</option>
              {others.map((o) => <option key={o.id} value={o.id}>{o.ref}</option>)}
            </select>
          </label>
        )}
        <label>Note
          <input value={note} onChange={(e) => setNote(e.target.value)} placeholder="why this disposition" />
        </label>

        {disposition === 'converted' && (
          <>
            <h2 style={{ margin: '.4rem 0 0' }}>Records to create (PEC-AHL-005)</h2>
            <p className="section-note" style={{ margin: 0 }}>
              One intake item may become several controlled records; each is back-linked and
              the raiser is notified at routing and closure (PEC-AHL-007).
            </p>
            {drafts.map((d) => {
              switch (d.kind) {
                case 'work_item':
                  return <WiEditor key={d.key} d={d} dels={dels ?? []} pkgs={pkgs ?? []} onChange={replace} onRemove={() => remove(d.key)} />
                case 'hold':
                  return <HoldEditor key={d.key} d={d} dels={dels ?? []} onChange={replace} onRemove={() => remove(d.key)} />
                case 'risk':
                  return <RiskEditor key={d.key} d={d} onChange={replace} onRemove={() => remove(d.key)} />
                case 'decision':
                  return <DecisionEditor key={d.key} d={d} pkgs={pkgs ?? []} onChange={replace} onRemove={() => remove(d.key)} />
                case 'interface':
                  return <InterfaceEditor key={d.key} d={d} onChange={replace} onRemove={() => remove(d.key)} />
              }
            })}
            <div style={{ display: 'flex', gap: '.4rem', flexWrap: 'wrap' }}>
              <button type="button" className="btn secondary small" onClick={() => addDraft({
                kind: 'work_item', key: nk(), title: '', statement: item.statementVerbatim,
                anchorType: 'deliverable', anchorId: '', ownerId: suggestedOwner,
                needBy: item.needBy ?? '', wiKind: 'action', log: item.log || 'internal',
              })}>+ Work item</button>
              <button type="button" className="btn secondary small" onClick={() => addDraft({
                kind: 'hold', key: nk(), title: '', cause: 'information', statement: item.statementVerbatim,
                ownerId: suggestedOwner, needBy: item.needBy ?? '', deliverableId: '',
              })}>+ Hold</button>
              <button type="button" className="btn secondary small" onClick={() => addDraft({
                kind: 'risk', key: nk(), title: '', cause: '', consequence: '',
                ownerId: suggestedOwner, probability: '3', impact: '3', needBy: item.needBy ?? '',
              })}>+ Risk</button>
              <button type="button" className="btn secondary small" onClick={() => addDraft({
                kind: 'decision', key: nk(), title: '', statement: item.statementVerbatim,
                authorityId: '', needBy: item.needBy ?? '', packageId: '',
              })}>+ Decision</button>
              <button type="button" className="btn secondary small" onClick={() => addDraft({
                kind: 'interface', key: nk(), title: '', givingParty: '', receivingParty: '',
                requiredInfo: '', needBy: item.needBy ?? '',
              })}>+ Interface</button>
            </div>
          </>
        )}

        <ErrorBox error={error} />
        <div className="row">
          <button
            className="btn"
            disabled={busy
              || (disposition === 'converted' && drafts.length === 0)
              || (disposition === 'merged' && !mergedInto)}
          >
            Record disposition
          </button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ---------- record builders (PEC-AHL-005) ----------

const cardStack: React.CSSProperties = { display: 'flex', flexDirection: 'column', gap: '.45rem' }

function DraftHead({ label, onRemove }: { label: string; onRemove(): void }): JSX.Element {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <b className="small">{label}</b>
      <button type="button" className="btn secondary small" onClick={onRemove}>remove</button>
    </div>
  )
}

function PersonSelect({ value, required, onChange }: {
  value: string; required?: boolean; onChange(v: string): void
}): JSX.Element {
  const { people } = useApp()
  return (
    <select required={required} value={value} onChange={(e) => onChange(e.target.value)}>
      <option value="">—</option>
      {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
    </select>
  )
}

function WiEditor({ d, dels, pkgs, onChange, onRemove }: {
  d: WiDraft; dels: any[]; pkgs: any[]; onChange(d: Draft): void; onRemove(): void
}): JSX.Element {
  return (
    <div className="card" style={cardStack}>
      <DraftHead label="Work item" onRemove={onRemove} />
      <label>Title *
        <input required value={d.title} onChange={(e) => onChange({ ...d, title: e.target.value })} />
      </label>
      <label>Statement (prefilled from the intake statement)
        <textarea value={d.statement} onChange={(e) => onChange({ ...d, statement: e.target.value })} />
      </label>
      <div className="row">
        {/* I-2: direct creation requires an anchor — deliverable or package */}
        <label>Anchor type
          <select value={d.anchorType} onChange={(e) => onChange({ ...d, anchorType: e.target.value as 'deliverable' | 'package', anchorId: '' })}>
            <option value="deliverable">deliverable</option>
            <option value="package">package</option>
          </select>
        </label>
        <label>Anchor *
          <select required value={d.anchorId} onChange={(e) => onChange({ ...d, anchorId: e.target.value })}>
            <option value="">—</option>
            {d.anchorType === 'deliverable'
              ? dels.map((x) => <option key={x.id} value={x.id}>{x.docNo} — {x.title}</option>)
              : pkgs.map((x) => <option key={x.id} value={x.id}>{x.code} — {x.name}</option>)}
          </select>
        </label>
      </div>
      <div className="row">
        <label>Owner *
          <PersonSelect required value={d.ownerId} onChange={(v) => onChange({ ...d, ownerId: v })} />
        </label>
        <label>Need by
          <input type="date" value={d.needBy} onChange={(e) => onChange({ ...d, needBy: e.target.value })} />
        </label>
      </div>
      <div className="row">
        <label>Kind
          <select value={d.wiKind} onChange={(e) => onChange({ ...d, wiKind: e.target.value })}>
            {WORK_ITEM_KINDS.map((k) => <option key={k} value={k}>{k.replaceAll('_', ' ')}</option>)}
          </select>
        </label>
        <label>Log
          <select value={d.log} onChange={(e) => onChange({ ...d, log: e.target.value })}>
            {LOGS.map((l) => <option key={l} value={l}>{l}</option>)}
          </select>
        </label>
      </div>
    </div>
  )
}

function HoldEditor({ d, dels, onChange, onRemove }: {
  d: HoldDraft; dels: any[]; onChange(d: Draft): void; onRemove(): void
}): JSX.Element {
  return (
    <div className="card" style={cardStack}>
      <DraftHead label="Hold" onRemove={onRemove} />
      <label>Title *
        <input required value={d.title} onChange={(e) => onChange({ ...d, title: e.target.value })} />
      </label>
      <div className="row">
        <label>Cause *
          <select required value={d.cause} onChange={(e) => onChange({ ...d, cause: e.target.value })}>
            {HOLD_CAUSES.map((c) => <option key={c} value={c}>{c.replaceAll('_', ' ')}</option>)}
          </select>
        </label>
        {/* I-3: owner + need-by required at creation */}
        <label>Owner *
          <PersonSelect required value={d.ownerId} onChange={(v) => onChange({ ...d, ownerId: v })} />
        </label>
        <label>Need by *
          <input required type="date" value={d.needBy} onChange={(e) => onChange({ ...d, needBy: e.target.value })} />
        </label>
      </div>
      <label>Statement
        <textarea value={d.statement} onChange={(e) => onChange({ ...d, statement: e.target.value })} />
      </label>
      <label>Blocks deliverable * (a hold blocks ≥1 record)
        <select required value={d.deliverableId} onChange={(e) => onChange({ ...d, deliverableId: e.target.value })}>
          <option value="">—</option>
          {dels.map((x) => <option key={x.id} value={x.id}>{x.docNo} — {x.title}</option>)}
        </select>
      </label>
    </div>
  )
}

function RiskEditor({ d, onChange, onRemove }: {
  d: RiskDraft; onChange(d: Draft): void; onRemove(): void
}): JSX.Element {
  return (
    <div className="card" style={cardStack}>
      <DraftHead label="Risk" onRemove={onRemove} />
      <label>Title *
        <input required value={d.title} onChange={(e) => onChange({ ...d, title: e.target.value })} />
      </label>
      <div className="row">
        <label>Cause
          <input value={d.cause} onChange={(e) => onChange({ ...d, cause: e.target.value })} />
        </label>
        <label>Consequence
          <input value={d.consequence} onChange={(e) => onChange({ ...d, consequence: e.target.value })} />
        </label>
      </div>
      <div className="row">
        <label>Owner
          <PersonSelect value={d.ownerId} onChange={(v) => onChange({ ...d, ownerId: v })} />
        </label>
        <label>Probability (1–5)
          <select value={d.probability} onChange={(e) => onChange({ ...d, probability: e.target.value })}>
            {['1', '2', '3', '4', '5'].map((n) => <option key={n} value={n}>{n}</option>)}
          </select>
        </label>
        <label>Impact (1–5)
          <select value={d.impact} onChange={(e) => onChange({ ...d, impact: e.target.value })}>
            {['1', '2', '3', '4', '5'].map((n) => <option key={n} value={n}>{n}</option>)}
          </select>
        </label>
        <label>Need by
          <input type="date" value={d.needBy} onChange={(e) => onChange({ ...d, needBy: e.target.value })} />
        </label>
      </div>
    </div>
  )
}

function DecisionEditor({ d, pkgs, onChange, onRemove }: {
  d: DecisionDraft; pkgs: any[]; onChange(d: Draft): void; onRemove(): void
}): JSX.Element {
  return (
    <div className="card" style={cardStack}>
      <DraftHead label="Decision" onRemove={onRemove} />
      <label>Title *
        <input required value={d.title} onChange={(e) => onChange({ ...d, title: e.target.value })} />
      </label>
      <label>Decision-needed statement *
        <textarea required value={d.statement} onChange={(e) => onChange({ ...d, statement: e.target.value })} />
      </label>
      <div className="row">
        <label>Authority *
          <PersonSelect required value={d.authorityId} onChange={(v) => onChange({ ...d, authorityId: v })} />
        </label>
        <label>Need by
          <input type="date" value={d.needBy} onChange={(e) => onChange({ ...d, needBy: e.target.value })} />
        </label>
        <label>Package
          <select value={d.packageId} onChange={(e) => onChange({ ...d, packageId: e.target.value })}>
            <option value="">—</option>
            {pkgs.map((x) => <option key={x.id} value={x.id}>{x.code} — {x.name}</option>)}
          </select>
        </label>
      </div>
    </div>
  )
}

function InterfaceEditor({ d, onChange, onRemove }: {
  d: InterfaceDraft; onChange(d: Draft): void; onRemove(): void
}): JSX.Element {
  return (
    <div className="card" style={cardStack}>
      <DraftHead label="Interface item" onRemove={onRemove} />
      <label>Title *
        <input required value={d.title} onChange={(e) => onChange({ ...d, title: e.target.value })} />
      </label>
      <div className="row">
        <label>Giving party *
          <input required value={d.givingParty} onChange={(e) => onChange({ ...d, givingParty: e.target.value })} />
        </label>
        <label>Receiving party *
          <input required value={d.receivingParty} onChange={(e) => onChange({ ...d, receivingParty: e.target.value })} />
        </label>
      </div>
      <div className="row">
        <label>Required information
          <input value={d.requiredInfo} onChange={(e) => onChange({ ...d, requiredInfo: e.target.value })} />
        </label>
        <label>Need by
          <input type="date" value={d.needBy} onChange={(e) => onChange({ ...d, needBy: e.target.value })} />
        </label>
      </div>
    </div>
  )
}
