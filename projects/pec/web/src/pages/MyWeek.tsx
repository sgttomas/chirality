/**
 * My Week — "What do I owe, and what am I waiting on?" (Individual Contributor home, PRD §12.6).
 * Committed items grouped by deliverable (PEC-MW-001), checks/comments owed to others (PEC-MW-002),
 * waiting-on-others (PEC-MW-003), in-place work item drawer (PEC-MW-004), why-in-week (PEC-MW-005),
 * overdue flagged equally for own and owed-to-others work (PEC-MW-006), manual commit-to-week
 * (PEC-MW-007). Notifications inbox: record, why, next action, due (PRD §12.14).
 */

import { useState } from 'react'
import { Link } from 'react-router-dom'
import { api, p } from '../api.ts'
import {
  ConditionsPanel, Drawer, ErrorBox, HistoryTrail, RecordRef, RegisterTable, StateTag, fmtDate,
  useApp, useLoad, usePerson,
} from '../shared.tsx'
import type { Col } from '../shared.tsx'

export function MyWeekPage(): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const person = usePerson()
  const [drawerItem, setDrawerItem] = useState<number | null>(null)
  const [respond, setRespond] = useState<any | null>(null)
  const { data, error } = useLoad(() => api.get(p(pid, 'my-week')), [pid])
  const { data: notifs } = useLoad(() => api.get(p(pid, 'notifications')), [pid])

  const markRead = async (id: number) => {
    try {
      await api.post(p(pid, `notifications/${id}/read`))
      toast('notification marked read')
      refresh()
    } catch (e: any) {
      toast(e.message ?? String(e))
    }
  }

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  // PEC-MW-001: committed items grouped by deliverable; non-anchored group last
  const groups = new Map<string, { deliverable: any | null; items: any[] }>()
  for (const it of data.committed) {
    const key = it.deliverable?.docNo ?? ''
    if (!groups.has(key)) groups.set(key, { deliverable: it.deliverable ?? null, items: [] })
    groups.get(key)!.items.push(it)
  }
  const ordered = [...groups.entries()].sort((a, b) =>
    a[0] === '' ? 1 : b[0] === '' ? -1 : a[0].localeCompare(b[0]))

  const committedCols: Array<Col<any>> = [
    { key: 'ref', label: 'Ref', render: (r) => <span className="mono">{r.workItem.ref}</span> },
    {
      key: 'title', label: 'Title', render: (r) => (
        <>
          {r.workItem.title}
          {/* PEC-MW-005: every item says why it is in the week */}
          <div className="small muted">{r.whyInWeek}</div>
        </>
      ),
    },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.workItem.state} /> },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.workItem.needBy)}</span> },
    {
      key: 'flags', label: 'Flags', render: (r) => (
        <>
          {/* PEC-MW-006: overdue flagged in red */}
          {r.overdue && <span className="badge red">overdue</span>}{' '}
          {r.blockedBy.map((h: any) => (
            <span key={h.ref} className="badge hold" title={h.title}>{h.ref} · {h.cause.replaceAll('_', ' ')}</span>
          ))}
          {!r.overdue && r.blockedBy.length === 0 && <span className="muted small">—</span>}
        </>
      ),
    },
  ]

  // PEC-MW-002: booked work owed to others — distinct from my own committed items
  const checkCols: Array<Col<any>> = [
    { key: 'ref', label: 'Check', render: (r) => <span className="mono">{r.checkRef}</span> },
    {
      key: 'del', label: 'Deliverable', render: (r) => r.deliverable
        ? <Link to={`/p/${pid}/deliverables/${r.deliverable.id}`}>{r.deliverable.docNo}</Link>
        : <span className="muted">—</span>,
    },
    { key: 'state', label: 'State', render: (r) => <StateTag s={r.state} /> },
    { key: 'open', label: 'Open comments', render: (r) => r.openComments > 0 ? <b>{r.openComments}</b> : <span className="muted">0</span> },
    {
      // PEC-MW-006: overdue-to-someone-else is flagged just like own overdue
      key: 'overdue', label: 'Overdue', render: (r) => r.overdue
        ? <span className="badge red">overdue</span> : <span className="muted small">—</span>,
    },
  ]

  const commentCols: Array<Col<any>> = [
    { key: 'ref', label: 'Comment', render: (r) => <span className="mono">{r.commentRef}</span> },
    { key: 'check', label: 'Check', render: (r) => <span className="mono">{r.checkRef}</span> },
    {
      key: 'del', label: 'Deliverable', render: (r) => r.deliverable
        ? <Link to={`/p/${pid}/deliverables/${r.deliverable.id}`}>{r.deliverable.docNo}</Link>
        : <span className="muted">—</span>,
    },
    { key: 'text', label: 'Comment text', render: (r) => <span className="small">{r.text}</span> },
    {
      key: 'age', label: 'Age (wd)', render: (r) => (
        <span className="nowrap">
          {r.ageWd}{' '}
          {r.overdue && <span className="badge red">overdue</span>}{/* PEC-MW-006 */}
        </span>
      ),
    },
    {
      key: 'act', label: '', render: (r) => r.deliverable
        ? <button className="btn secondary small" onClick={() => setRespond(r)}>Respond</button>
        : <span className="muted small">open from Deliverables</span>,
    },
  ]

  // PEC-MW-003: chase-able — shows who to chase; explicitly not counted as commitments
  const waitingCols: Array<Col<any>> = [
    { key: 'kind', label: 'Kind', render: (r) => <span className={`badge ${r.kind === 'hold' ? 'hold' : 'plain'}`}>{r.kind}</span> },
    { key: 'ref', label: 'Ref', render: (r) => <RecordRef recordType={r.kind} id={r.id} recordRef={r.ref} /> },
    { key: 'title', label: 'Title', render: (r) => r.title },
    { key: 'owner', label: 'Owner (chase)', render: (r) => person(r.ownerId) },
    { key: 'needBy', label: 'Need by', render: (r) => <span className="nowrap">{fmtDate(r.needBy)}</span> },
    { key: 'gates', label: 'Gates', render: (r) => <span className="muted small">{r.gates}</span> },
  ]

  // Every notification: record, why, next action, due (PRD §12.14); unread bold
  const nb = (r: any, node: JSX.Element): JSX.Element => (r.readAt == null ? <b>{node}</b> : node)
  const notifCols: Array<Col<any>> = [
    { key: 'at', label: 'When', render: (r) => nb(r, <span className="mono nowrap small">{r.at.slice(0, 16).replace('T', ' ')}</span>) },
    {
      key: 'event', label: 'Event', render: (r) => nb(r, (
        <span className="nowrap">
          <span className="state">{r.event}</span>{' '}
          {r.severity === 'red' && <span className="badge red">red</span>}
          {r.severity === 'warn' && <span className="badge amber">warn</span>}{/* PEC-NOT-003 */}
        </span>
      )),
    },
    { key: 'rec', label: 'Record', render: (r) => nb(r, <RecordRef recordType={r.recordType} id={r.recordId} recordRef={r.recordRef} />) },
    { key: 'why', label: 'Why', render: (r) => nb(r, <span className="small">{r.reason}</span>) },
    { key: 'next', label: 'Next action', render: (r) => nb(r, <span className="small">{r.nextAction}</span>) },
    { key: 'due', label: 'Due', render: (r) => nb(r, <span className="nowrap">{fmtDate(r.due)}</span>) },
    {
      key: 'read', label: '', render: (r) => r.readAt == null
        ? <button className="btn secondary small" onClick={() => markRead(r.id)}>mark read</button>
        : <span className="muted small">read</span>,
    },
  ]

  return (
    <div>
      <h1>My Week — {data.week}</h1>
      <p className="section-note">
        What you owe and what you are waiting on. P1: committed = manually committed to this week,
        overdue, or need-by falls this week (PEC-MW-007); Plan-driven weeks arrive in P2.
      </p>

      {/* PEC-MW-001: committed items grouped by deliverable */}
      <h2>Committed this week — grouped by deliverable</h2>
      {data.committed.length === 0 && (
        <p className="muted small">
          Nothing committed or falling due this week. Commit an item from its drawer (PEC-MW-007).
        </p>
      )}
      {ordered.map(([key, g]) => (
        <div key={key || '(none)'}>
          <h3>
            {g.deliverable
              ? (
                <>
                  <Link to={`/p/${pid}/deliverables/${g.deliverable.id}`}>{g.deliverable.docNo}</Link>{' '}
                  <span className="muted small">{g.deliverable.title}</span>
                </>
              )
              : <>Not deliverable-anchored</>}
          </h3>
          <RegisterTable cols={committedCols} rows={g.items}
            onRowClick={(r) => setDrawerItem(r.workItem.id)} />
        </div>
      ))}

      {/* PEC-MW-002: checks and comment responses owed to others — booked work */}
      <h2>Checks &amp; comment responses I owe others</h2>
      <p className="section-note">
        Booked work owed to someone else — kept distinct from your own items (PEC-MW-002).
      </p>
      <h3>Checks to perform</h3>
      {data.checksOwed.length === 0
        ? <p className="muted small">No checks are owed by you right now.</p>
        : <RegisterTable cols={checkCols} rows={data.checksOwed} />}
      <h3>Comment responses due</h3>
      {data.commentsOwed.length === 0
        ? <p className="muted small">No comment responses are due from you right now.</p>
        : <RegisterTable cols={commentCols} rows={data.commentsOwed} />}

      {/* PEC-MW-003: waiting on others — chase-able, not commitments */}
      <h2>Waiting on others</h2>
      {data.waitingOnOthers.length === 0
        ? <p className="muted small">No current waits on other people are blocking your week.</p>
        : <RegisterTable cols={waitingCols} rows={data.waitingOnOthers} />}

      <h2>Notifications</h2>
      {(notifs ?? []).length === 0
        ? <p className="muted small">No notifications are waiting for you.</p>
        : <RegisterTable cols={notifCols} rows={notifs ?? []} />}

      {/* PEC-MW-004: the work item drawer — act in place, no navigation */}
      {drawerItem != null && (
        <WorkItemDrawer id={drawerItem} week={data.week} onClose={() => setDrawerItem(null)} />
      )}
      {respond && <RespondDrawer row={respond} onClose={() => setRespond(null)} />}
    </div>
  )
}

// ---------- work item drawer (PEC-MW-004) ----------

function WorkItemDrawer({ id, week, onClose }: { id: number; week: string; onClose(): void }): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const person = usePerson()
  const { data, error } = useLoad(() => api.get(p(pid, 'work-items/' + id)), [pid, id])
  const [actionError, setActionError] = useState<any>(null)
  const [busy, setBusy] = useState(false)
  const [note, setNote] = useState('')
  const [evLabel, setEvLabel] = useState('')
  const [evContent, setEvContent] = useState('')
  const [transitionEvent, setTransitionEvent] = useState<string | null>(null)

  const run = async (fn: () => Promise<void>, msg: string) => {
    setBusy(true)
    setActionError(null)
    try {
      await fn()
      toast(msg)
      refresh()
    } catch (e) {
      // 409 CONDITIONS_OPEN / VERSION_CONFLICT render via ErrorBox — server-truth, no local rules
      setActionError(e)
    } finally {
      setBusy(false)
    }
  }

  // PEC-MW-007: P1 manual commit-to-week toggle
  const toggleCommit = () => {
    const w = data.workItem
    const next = w.committedWeek === week ? null : week
    void run(async () => {
      await api.put(p(pid, `work-items/${id}`), { version: w.version, committedWeek: next })
    }, next ? `${w.ref} committed to ${week}` : `${w.ref} removed from ${week}`)
  }

  const addProgress = (e: React.FormEvent) => {
    e.preventDefault()
    if (!note.trim()) return
    void run(async () => {
      await api.post(p(pid, `work-items/${id}/progress`), { note: note.trim() })
      setNote('')
    }, 'progress recorded')
  }

  const addEvidence = (e: React.FormEvent) => {
    e.preventDefault()
    if (!evLabel.trim()) return
    void run(async () => {
      await api.post(p(pid, `records/work_item/${id}/evidence`),
        { kind: 'note', label: evLabel.trim(), content: evContent.trim() || undefined })
      setEvLabel('')
      setEvContent('')
    }, 'evidence attached')
  }

  const w = data?.workItem
  return (
    <Drawer
      title={w ? <><span className="mono">{w.ref}</span> {w.title}</> : `work item #${id}`}
      onClose={onClose}
    >
      {error && <ErrorBox error={{ message: error }} />}
      {!data && !error && <p className="muted">loading…</p>}
      {data && (
        <>
          <p>
            <StateTag s={w.state} />{' '}
            <span className="small muted">
              anchor {String(w.anchorType).replaceAll('_', ' ')} #{w.anchorId}
              {' '}· owner {person(w.ownerId)}
              {' '}· priority {w.priority ?? '—'}{w.priorityProvenance ? ` (${w.priorityProvenance})` : ''}
              {' '}· need-by {fmtDate(w.needBy)}
            </span>
          </p>
          {w.statement && <p className="small">{w.statement}</p>}

          {/* Actions without navigation (PEC-MW-004): server-offered transitions only */}
          <div style={{ display: 'flex', gap: '.4rem', flexWrap: 'wrap' }}>
            {data.offeredTransitions.map((ev: string) => (
              <button key={ev} disabled={busy}
                className={`btn small ${ev === 'cancel' ? 'danger' : ev === 'close' ? '' : 'secondary'}`}
                onClick={() => setTransitionEvent(ev)}>
                {ev}
              </button>
            ))}
            {/* PEC-MW-007: manual commit toggle */}
            <button className="btn secondary small" disabled={busy} onClick={toggleCommit}>
              {w.committedWeek === week ? `uncommit from ${week}` : `commit to ${week}`}
            </button>
          </div>
          {w.committedWeek && w.committedWeek !== week && (
            <p className="small muted">committed week: {w.committedWeek}</p>
          )}
          <div style={{ marginTop: '.5rem' }}>
            <ErrorBox error={actionError} />
          </div>

          {data.blockedBy.length > 0 && (
            <>
              <h2>Blocked by</h2>
              {data.blockedBy.map((h: any) => (
                <div key={h.ref} className="cond blocked_by_hold">
                  <span className="badge hold">hold</span>{' '}
                  <span className="mono">{h.ref}</span> {h.title}{' '}
                  <span className="muted small">
                    ({String(h.cause).replaceAll('_', ' ')}, owner {person(h.ownerId)}, need-by {fmtDate(h.needBy)})
                  </span>
                </div>
              ))}
            </>
          )}

          <ConditionsPanel ex={data.closureConditions} title="Closure conditions" />

          <h2>Progress</h2>
          <form className="row" onSubmit={addProgress}>
            <input value={note} onChange={(e) => setNote(e.target.value)}
              placeholder="progress note — becomes history + evidence trail (PEC-DEL-005)"
              style={{ font: 'inherit', padding: '.38rem .5rem', border: '1px solid var(--line)', borderRadius: 4 }} />
            <button className="btn small" disabled={busy || !note.trim()} style={{ flex: 'none' }}>Add note</button>
          </form>

          <h2>Evidence</h2>
          {data.evidence.length === 0 && <p className="muted small">none attached</p>}
          {data.evidence.map((ev: any) => (
            <div key={ev.id} className="small">
              <span className="state">{ev.kind}</span> <b>{ev.label}</b>
              {ev.content && <span className="muted"> — {ev.content}</span>}
              <span className="muted"> · {person(ev.addedBy)} {fmtDate(ev.addedAt)}</span>
            </div>
          ))}
          <form className="row" style={{ marginTop: '.4rem' }} onSubmit={addEvidence}>
            <input value={evLabel} onChange={(e) => setEvLabel(e.target.value)} placeholder="label *"
              style={{ font: 'inherit', padding: '.38rem .5rem', border: '1px solid var(--line)', borderRadius: 4 }} />
            <input value={evContent} onChange={(e) => setEvContent(e.target.value)} placeholder="content / reference"
              style={{ font: 'inherit', padding: '.38rem .5rem', border: '1px solid var(--line)', borderRadius: 4 }} />
            <button className="btn small" disabled={busy || !evLabel.trim()} style={{ flex: 'none' }}>Attach</button>
          </form>

          <h2>History</h2>
          <HistoryTrail entries={data.history} />
          {transitionEvent && (
            <WorkItemTransitionDrawer
              item={w}
              event={transitionEvent}
              onClose={() => setTransitionEvent(null)}
              onDone={() => {
                setTransitionEvent(null)
                refresh()
              }}
            />
          )}
        </>
      )}
    </Drawer>
  )
}

function WorkItemTransitionDrawer({
  item, event, onClose, onDone,
}: { item: any; event: string; onClose(): void; onDone(): void }): JSX.Element {
  const { pid, toast } = useApp()
  const [reason, setReason] = useState('')
  const [closingStatement, setClosingStatement] = useState('')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)
  const reasonRequired = event === 'cancel' || event === 'reopen'

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (reasonRequired && !reason.trim()) {
      setError({ message: `a reason is required to ${event}` })
      return
    }
    setBusy(true); setError(null)
    try {
      await api.post(p(pid, `work-items/${item.id}/transition`), {
        event,
        version: item.version,
        reason: reasonRequired ? reason.trim() : undefined,
        closingStatement: event === 'close' && closingStatement.trim() ? closingStatement.trim() : undefined,
      })
      toast(`${item.ref}: ${event} recorded`)
      onDone()
    } catch (err) { setError(err) } finally { setBusy(false) }
  }

  return (
    <Drawer title={<>{event} — <span className="mono">{item.ref}</span></>} onClose={onClose}>
      <p className="section-note">{item.title}</p>
      <form className="stack" onSubmit={submit}>
        {event === 'close' && (
          <label>Closing statement
            <textarea value={closingStatement} onChange={(e) => setClosingStatement(e.target.value)}
              placeholder="optional" />
          </label>
        )}
        {reasonRequired && (
          <label>Reason *
            <textarea required value={reason} onChange={(e) => setReason(e.target.value)} />
          </label>
        )}
        {!reasonRequired && event !== 'close' && (
          <p className="section-note">This transition records the server-offered event without additional fields.</p>
        )}
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || (reasonRequired && !reason.trim())}>{event}</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}

// ---------- respond to a review comment (PEC-MW-002) ----------

/**
 * commentsOwed rows carry no version; optimistic concurrency (PEC-NFR-004) requires the
 * comment's current version. Resolve it server-truthfully through the deliverable detail's
 * openItems.comments — no duplicated rules, no extra route.
 */
function RespondDrawer({ row, onClose }: { row: any; onClose(): void }): JSX.Element {
  const { pid, refresh, toast } = useApp()
  const person = usePerson()
  const { data, error } = useLoad(() => api.get(p(pid, 'deliverables/' + row.deliverable.id)), [pid, row.deliverable.id])
  const comment = data?.openItems?.comments?.find?.((c: any) => c.id === row.commentId)
  const [response, setResponse] = useState('')
  const [err, setErr] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!comment || !response.trim()) return
    setBusy(true)
    setErr(null)
    try {
      await api.post(p(pid, `comments/${row.commentId}/respond`),
        { version: comment.version, response: response.trim() })
      toast(`${row.commentRef} responded — closure is accepted by the checker only (PEC-CHK-002)`)
      refresh()
      onClose()
    } catch (e2) {
      setErr(e2)
    } finally {
      setBusy(false)
    }
  }

  return (
    <Drawer title={<>Respond — <span className="mono">{row.commentRef}</span></>} onClose={onClose}>
      <p className="small muted">
        on <span className="mono">{row.checkRef}</span> · {row.deliverable.docNo} · age {row.ageWd} wd
        {comment && <> · originator {person(comment.originatorId)}</>}
      </p>
      <p className="small">{row.text}</p>
      {error && <ErrorBox error={{ message: error }} />}
      {!data && !error && <p className="muted">loading…</p>}
      {data && !comment && (
        <p className="section-note">
          This comment is not open on the current revision of {row.deliverable.docNo} — open it from
          the Deliverables screen to respond.
        </p>
      )}
      <form className="stack" onSubmit={submit}>
        <label>Response *
          <textarea required value={response} onChange={(e) => setResponse(e.target.value)}
            placeholder="what was changed, or why no change is needed" />
        </label>
        <ErrorBox error={err} />
        <div className="row">
          <button className="btn" disabled={busy || !comment || !response.trim()}>Respond</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}
