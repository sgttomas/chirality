/**
 * The shell-level agent panel (D-PEC-17, brief §5): conversation thread over
 * the proxy routes, CSV drop/paste zone → proposals via the live seam, live
 * proposal status with lifecycle badges, triage queue summary, and the agent
 * person's name on every agent turn (WF-8).
 *
 * DELIBERATELY ABSENT (rider 4, GOV MINOR-4 — the panel-side pin): no accept,
 * apply, reject-of-others, or force control renders here, ever. Proposal
 * cards deep-link to the Admin "Proposed imports" section, where those remain
 * human acts under the human's own session.
 */

import { useCallback, useEffect, useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import { api, p } from '../api.ts'
import { useApp } from '../shared.tsx'
import { agentMessage, agentStatus } from './api.ts'
import type { AgentEvent, AgentStatus } from './api.ts'
import { useScreenContext } from './context.tsx'

/** RV-14: CSV only, ≤ 5 MiB (mirrors the server's proposal cap) */
const MAX_CSV_BYTES = 5 * 1024 * 1024

interface Turn {
  who: 'you' | 'agent'
  text?: string
  events?: AgentEvent[]
}

interface ProposalRow {
  id: number
  ref: string
  contract: string
  state: string
  createdBy: number
  dryRunReport: { accepted?: number; updated?: number; conflicts?: unknown[]; rejected?: unknown[]; intakeCreated?: number; error?: string } | null
}

/** topbar toggle + docked panel; renders only when the human holds agent.direct */
export function AgentDock(): JSX.Element | null {
  const { pid } = useApp()
  const [allowed, setAllowed] = useState(false)
  const [open, setOpen] = useState(false)
  useEffect(() => {
    let live = true
    setAllowed(false)
    api.get(p(pid, 'can/agent.direct'))
      .then((r) => { if (live) setAllowed(r.allowed === true) })
      .catch(() => { if (live) setAllowed(false) })
    return () => { live = false }
  }, [pid])
  if (!allowed) return null
  return (
    <>
      <button className="btn secondary" onClick={() => setOpen((o) => !o)}>
        {open ? 'Close agent' : 'Agent'}
      </button>
      {open && <AgentPanel onClose={() => setOpen(false)} />}
    </>
  )
}

function AgentPanel({ onClose }: { onClose(): void }): JSX.Element {
  const { pid, people } = useApp()
  const screen = useScreenContext()
  const [status, setStatus] = useState<AgentStatus | null>(null)
  const [statusError, setStatusError] = useState<string | null>(null)
  const [thread, setThread] = useState<Turn[]>([])
  const [message, setMessage] = useState('')
  const [attachment, setAttachment] = useState<{ name: string; text: string } | null>(null)
  const [busy, setBusy] = useState(false)
  const [dropError, setDropError] = useState<string | null>(null)
  const [proposals, setProposals] = useState<ProposalRow[] | null>(null)
  const [intakeOpen, setIntakeOpen] = useState<number | null>(null)
  const endRef = useRef<HTMLDivElement | null>(null)

  const loadStatus = useCallback(() => {
    agentStatus(pid).then(
      (s) => { setStatus(s); setStatusError(null) },
      (e) => { setStatus(null); setStatusError(e.message ?? String(e)) },
    )
  }, [pid])

  // live strip: the human's own session reads (the panel viewer holds
  // agent.direct ⇒ a register-handling role); the conversation acts stay the agent's
  const agentPersonId = status?.agent
    ? people.find((x) => x.email === status.agent!.email)?.id ?? null
    : null
  const loadStrip = useCallback(() => {
    api.get<ProposalRow[]>(p(pid, 'import-proposals'))
      .then((rows) => setProposals(rows))
      .catch(() => setProposals(null))
    api.get<unknown[]>(p(pid, 'intake'))
      .then((rows) => setIntakeOpen(rows.length))
      .catch(() => setIntakeOpen(null))
  }, [pid])

  useEffect(() => { loadStatus(); loadStrip() }, [loadStatus, loadStrip])

  useEffect(() => { endRef.current?.scrollIntoView({ block: 'end' }) }, [thread])

  const acceptFile = async (file: File) => {
    setDropError(null)
    if (!/\.csv$/i.test(file.name)) { setDropError('CSV only (RV-14): drop a .csv file'); return }
    if (file.size > MAX_CSV_BYTES) { setDropError('the file exceeds the 5 MiB CSV cap (RV-14)'); return }
    setAttachment({ name: file.name, text: await file.text() })
  }

  const send = async () => {
    if (busy || (!message.trim() && !attachment)) return
    const outgoing = message.trim() || (attachment ? `(file: ${attachment.name})` : '')
    setBusy(true)
    setThread((t) => [...t, { who: 'you', text: outgoing + (attachment && message.trim() ? ` — ${attachment.name}` : '') }])
    try {
      const body = {
        message,
        context: { route: screen.route, records: screen.records },
        ...(attachment ? { attachment } : {}),
      }
      const r = await agentMessage(pid, body)
      setThread((t) => [...t, { who: 'agent', events: r.events }])
      setMessage('')
      setAttachment(null)
      loadStrip()
    } catch (e: any) {
      setThread((t) => [...t, {
        who: 'agent',
        events: [{ type: 'turn:error', code: e.code ?? 'SEND_FAILED', message: e.message ?? String(e) }],
      }])
      if (e.code === 'AGENT_UNAVAILABLE' || e.code === 'AGENT_NOT_CONFIGURED') loadStatus()
    } finally {
      setBusy(false)
    }
  }

  const agentName = status?.agent?.name ?? 'agent'
  const agentProposals = (proposals ?? []).filter((row) => agentPersonId != null && row.createdBy === agentPersonId)

  return (
    <aside className="agent-panel" onDragOver={(e) => e.preventDefault()}
      onDrop={(e) => { e.preventDefault(); const f = e.dataTransfer.files?.[0]; if (f) void acceptFile(f) }}>
      <div className="agent-head">
        <div>
          {/* WF-8: the agent renders under the agent person's name, exactly as history records it */}
          <b>{status?.agent ? status.agent.name : 'pec agent'}</b>{' '}
          <span className="badge plain">{status?.engine ?? '—'}</span>{' '}
          {status && !status.configured && <span className="badge amber">not configured</span>}
          {status && status.configured && <span className="badge green">ready</span>}
        </div>
        <button className="closex" onClick={onClose} aria-label="close agent panel">✕</button>
      </div>

      {statusError && (
        <div className="error-box">
          The agent sidecar is not reachable: {statusError}
          {' '}<button className="btn small secondary" onClick={loadStatus}>retry</button>
        </div>
      )}

      <div className="agent-strip">
        <div className="small">
          <b>Agent proposals</b>{' '}
          {agentProposals.length === 0 && <span className="muted">none</span>}
          {agentProposals.map((row) => (
            <span key={row.id} className="agent-strip-item">
              <span className="mono">{row.ref}</span> <span className={`state ${row.state}`}>{row.state.replaceAll('_', ' ')}</span>
            </span>
          ))}
        </div>
        <div className="small">
          <b>Intake queue</b>{' '}
          {intakeOpen == null ? <span className="muted">—</span> : <span>{intakeOpen} open</span>}
        </div>
        {/* the human act lives in Admin, under the human's own session — the panel only links */}
        <Link className="small" to={`/p/${pid}/admin`}>Open Admin — Proposed imports (accept/apply)</Link>
      </div>

      <div className="agent-thread">
        {thread.length === 0 && (
          <p className="muted small">
            Drop a CSV to file an import proposal, or ask: “status”, “intake”,
            “triage INTK-1 as parked: &lt;grounds&gt;”, “what am I looking at”.
            Accept and apply stay in Admin, done by you.
          </p>
        )}
        {thread.map((t, i) => t.who === 'you'
          ? <div key={i} className="agent-msg you">{t.text}</div>
          : (
            <div key={i} className="agent-msg agent">
              <div className="agent-msg-name small muted">{agentName}</div>
              {(t.events ?? []).map((e, j) => <EventView key={j} e={e} pid={pid} />)}
            </div>
          ))}
        <div ref={endRef} />
      </div>

      {dropError && <div className="error-box">{dropError}</div>}
      {attachment && (
        <div className="agent-attachment small">
          📄 {attachment.name}
          <button className="btn small secondary" onClick={() => setAttachment(null)}>remove</button>
        </div>
      )}

      <div className="agent-compose">
        <textarea
          value={message}
          placeholder="Message the agent… (paste CSV text or drop a .csv here)"
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); void send() } }}
          onPaste={(e) => {
            const f = e.clipboardData.files?.[0]
            if (f) { e.preventDefault(); void acceptFile(f) }
          }}
        />
        <div className="agent-compose-row">
          <label className="btn small secondary agent-file">
            attach .csv
            <input type="file" accept=".csv,text/csv" style={{ display: 'none' }}
              onChange={(e) => { const f = e.target.files?.[0]; if (f) void acceptFile(f); e.target.value = '' }} />
          </label>
          <div className="spacer" />
          <button className="btn small" disabled={busy || (!message.trim() && !attachment)} onClick={() => void send()}>
            {busy ? 'sending…' : 'send'}
          </button>
        </div>
      </div>
    </aside>
  )
}

function EventView({ e, pid }: { e: AgentEvent; pid: number }): JSX.Element {
  switch (e.type) {
    case 'agent:reply':
      return <div className="agent-bubble">{e.text}</div>
    case 'act:result': {
      const payload = (e.payload ?? {}) as {
        ref?: string; state?: string; contract?: string
        report?: { accepted?: number; updated?: number; conflicts?: unknown[]; rejected?: unknown[]; intakeCreated?: number; error?: string } | null
      }
      return (
        <div className={`agent-card ${e.ok ? '' : 'agent-card-warn'}`}>
          <div className="small">
            <span className="badge plain">{e.act}</span>{' '}
            {payload.ref && <span className="mono">{payload.ref}</span>}{' '}
            {payload.state && <span className={`state ${payload.state}`}>{payload.state.replaceAll('_', ' ')}</span>}
          </div>
          <div className="agent-bubble">{e.summary}</div>
          {payload.report && !payload.report.error && (
            <div className="small muted">
              dry-run: {payload.report.accepted ?? 0} create · {payload.report.updated ?? 0} update ·{' '}
              {(payload.report.conflicts ?? []).length} conflicts · {(payload.report.rejected ?? []).length} rejected ·{' '}
              {payload.report.intakeCreated ?? 0} to intake {/* RV-18: full report incl. intakeCreated */}
            </div>
          )}
          {payload.ref && (
            <Link className="small" to={`/p/${pid}/admin`}>review in Admin (accept/apply is yours)</Link>
          )}
        </div>
      )
    }
    case 'act:refused':
      // the refusal reason renders VERBATIM
      return <div className="agent-card agent-card-refused"><b className="small">refused ({e.act}):</b> <span className="small">{e.reason}</span></div>
    case 'turn:error':
      return <div className="error-box">{e.code}: {e.message}</div>
  }
}
