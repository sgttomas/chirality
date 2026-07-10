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
import type { AgentStatus, AgentStreamEvent } from './api.ts'
import { useScreenContext } from './context.tsx'

/** D-PEC-50: CSV/XLSX, ≤ 5 MiB (mirrors the sidecar proposal cap). */
const MAX_ATTACHMENT_BYTES = 5 * 1024 * 1024

interface Turn {
  id: string
  who: 'you' | 'agent'
  text?: string
  events?: AgentStreamEvent[]
}

/** D-PEC-21: how many prior turns ride each message (sidecar cap is 40) */
const MAX_HISTORY_TURNS = 20
/** stay under the sidecar's 8192-BYTE per-entry cap with headroom — measured
 * in UTF-8 bytes, not chars (a char-count clip overshoots on non-ASCII text) */
const MAX_HISTORY_ENTRY_BYTES = 7500

/** clip to a UTF-8 byte budget without splitting a code point */
function clipUtf8(text: string, maxBytes: number): string {
  const bytes = new TextEncoder().encode(text)
  if (bytes.length <= maxBytes) return text
  return new TextDecoder('utf-8').decode(bytes.slice(0, maxBytes)).replace(/�+$/, '')
}

/** flatten a turn to the text the model sees as conversation history */
function flattenTurn(t: Turn): { who: 'you' | 'agent'; text: string } {
  const text = t.who === 'you'
    ? t.text ?? ''
    : (t.events ?? []).map((e) => {
        switch (e.type) {
          case 'message.completed': return String(e.data.text ?? '')
          case 'tool.completed': return `[${String(e.data.act ?? e.data.toolName ?? 'tool')}] ${String(e.data.summary ?? 'completed')}`
          case 'tool.failed': return e.data.refused
            ? `[refused ${String(e.data.act ?? e.data.toolName ?? 'tool')}] ${String(e.data.reason ?? '')}`
            : `[failed ${String(e.data.act ?? e.data.toolName ?? 'tool')}] ${String(e.data.summary ?? e.data.reason ?? '')}`
          case 'turn.failed': return `[error ${String(e.data.code ?? 'TURN_FAILED')}] ${String(e.data.message ?? '')}`
          default: return ''
        }
      }).join('\n')
  return { who: t.who, text: clipUtf8(text, MAX_HISTORY_ENTRY_BYTES) }
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
  const [attachment, setAttachment] = useState<{ name: string; text: string } | { name: string; base64: string } | null>(null)
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
    if (!/\.(csv|xlsx)$/i.test(file.name)) { setDropError('Attach a .csv or .xlsx file'); return }
    if (file.size > MAX_ATTACHMENT_BYTES) { setDropError('The file exceeds the 5 MiB attachment cap'); return }
    if (/\.xlsx$/i.test(file.name)) {
      const bytes = new Uint8Array(await file.arrayBuffer())
      let binary = ''
      for (let i = 0; i < bytes.length; i += 0x8000) {
        binary += String.fromCharCode(...bytes.subarray(i, i + 0x8000))
      }
      setAttachment({ name: file.name, base64: btoa(binary) })
    } else {
      setAttachment({ name: file.name, text: await file.text() })
    }
  }

  const send = async () => {
    if (busy || (!message.trim() && !attachment)) return
    const outgoing = message.trim() || (attachment ? `(file: ${attachment.name})` : '')
    const userTurnId = crypto.randomUUID()
    const agentTurnId = crypto.randomUUID()
    setBusy(true)
    setThread((t) => [
      ...t,
      { id: userTurnId, who: 'you', text: outgoing + (attachment && message.trim() ? ` — ${attachment.name}` : '') },
      { id: agentTurnId, who: 'agent', events: [] },
    ])
    try {
      // D-PEC-21: the visible thread rides along as conversation memory
      // (thread state predates this send's own entries — exactly the prior turns)
      const history = thread.slice(-MAX_HISTORY_TURNS).map(flattenTurn)
      const body = {
        message,
        context: { route: screen.route, records: screen.records },
        ...(history.length > 0 ? { history } : {}),
        ...(attachment ? { attachment } : {}),
      }
      await agentMessage(pid, body, (event) => {
        setThread((turns) => turns.map((turn) => {
          if (turn.id !== agentTurnId) return turn
          const events = turn.events ?? []
          const last = events.at(-1)
          // Preserve every lifecycle transition while coalescing adjacent text
          // deltas so long answers do not create thousands of React nodes.
          if (event.type === 'model.delta' && last?.type === 'model.delta') {
            return {
              ...turn,
              events: [...events.slice(0, -1), {
                type: 'model.delta',
                data: { text: String(last.data.text ?? '') + String(event.data.text ?? '') },
              }],
            }
          }
          return { ...turn, events: [...events, event] }
        }))
      })
      setMessage('')
      setAttachment(null)
      loadStrip()
    } catch (e: any) {
      setThread((turns) => turns.map((turn) => turn.id === agentTurnId ? {
        ...turn,
        events: [...(turn.events ?? []), { type: 'turn.failed', data: { code: e.code ?? 'SEND_FAILED', message: e.message ?? String(e) } }],
      } : turn))
      if (e.code === 'AGENT_UNAVAILABLE' || e.code === 'AGENT_NOT_CONFIGURED') loadStatus()
    } finally {
      setBusy(false)
    }
  }

  const agentName = status?.agent?.name ?? 'agent'
  const agentProposals = (proposals ?? []).filter((row) => agentPersonId != null && row.createdBy === agentPersonId)
  // D-T0-21 O-B disclosure: the sidecar health field rides the proxy verbatim
  const access = status?.access ?? null
  const latestResolvedModel = [...thread].reverse()
    .flatMap((turn) => [...(turn.events ?? [])].reverse())
    .find((event) => event.type === 'adapter.initialized')?.data.model
  const resolvedModel = typeof latestResolvedModel === 'string' ? latestResolvedModel : status?.model

  return (
    <aside className="agent-panel" onDragOver={(e) => e.preventDefault()}
      onDrop={(e) => { e.preventDefault(); const f = e.dataTransfer.files?.[0]; if (f) void acceptFile(f) }}>
      <div className="agent-head">
        <div>
          {/* WF-8: the agent renders under the agent person's name, exactly as history records it */}
          <b>{status?.agent ? status.agent.name : 'pec agent'}</b>{' '}
          <span className="badge plain">{status?.engine ?? '—'}</span>{' '}
          {resolvedModel && <><span className="badge plain">{resolvedModel}</span>{' '}</>}
          {status?.engine === 'sdk' && !resolvedModel && <><span className="badge plain">model resolves on turn</span>{' '}</>}
          {/* D-T0-21 O-B: the active access basis is always shown; broad is loud */}
          {access && <span className={`badge ${access === 'broad' ? 'amber' : 'plain'}`}>{access} access</span>}{' '}
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
            Drop a dated MDL or package workbook to file an import proposal, or ask: “status”, “intake”,
            “triage INTK-1 as parked: &lt;grounds&gt;”, “what am I looking at”.
            Accept and apply stay in Admin, done by you.
          </p>
        )}
        {thread.map((t) => t.who === 'you'
          ? <div key={t.id} className="agent-msg you">{t.text}</div>
          : (
            <div key={t.id} className="agent-msg agent">
              <div className="agent-msg-name small muted">{agentName}</div>
              <AgentTurnView events={t.events ?? []} pid={pid} />
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
          placeholder="Message the agent… (paste CSV text or drop a .csv/.xlsx here)"
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); void send() } }}
          onPaste={(e) => {
            const f = e.clipboardData.files?.[0]
            if (f) { e.preventDefault(); void acceptFile(f) }
          }}
        />
        <div className="agent-compose-row">
          <label className="btn small secondary agent-file">
            attach workbook
            <input type="file" accept=".csv,.xlsx,text/csv,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" style={{ display: 'none' }}
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

interface ToolSnapshot {
  key: string
  name: string
  started?: AgentStreamEvent
  terminal?: AgentStreamEvent
}

function AgentTurnView({ events, pid }: { events: AgentStreamEvent[]; pid: number }): JSX.Element {
  if (events.length === 0) return <div className="agent-activity small"><span className="agent-pulse" /> connecting…</div>

  const lifecycle = events.filter((event) => event.type.startsWith('turn.')).at(-1)
  const init = events.filter((event) => event.type === 'adapter.initialized').at(-1)
  const budgetEvent = events.filter((event) => event.type.startsWith('tool.') && event.data.actBudget != null).at(-1)
  const budget = budgetEvent?.data.actBudget as { used?: number; max?: number; remaining?: number } | undefined
  const tools: ToolSnapshot[] = []
  for (const event of events) {
    if (event.type !== 'tool.started' && event.type !== 'tool.completed' && event.type !== 'tool.failed') continue
    const key = String(event.data.toolUseId ?? `${event.data.toolName ?? event.data.act ?? 'tool'}-${tools.length}`)
    let tool = tools.find((row) => row.key === key)
    if (!tool) {
      tool = { key, name: String(event.data.toolName ?? event.data.act ?? 'tool') }
      tools.push(tool)
    }
    if (event.type === 'tool.started') tool.started = event
    else tool.terminal = event
  }
  const completed = events.filter((event) => event.type === 'message.completed').at(-1)
  const response = completed
    ? String(completed.data.text ?? '')
    : events.filter((event) => event.type === 'model.delta').map((event) => String(event.data.text ?? '')).join('')
  const failed = lifecycle?.type === 'turn.failed'
  const stateLabel = lifecycle?.type === 'turn.completed' ? 'completed'
    : failed ? 'failed'
      : lifecycle?.type === 'turn.started' ? 'running'
        : 'accepted'

  return (
    <>
      <div className="agent-activity">
        <div className="agent-activity-head small">
          <span className={stateLabel === 'running' || stateLabel === 'accepted' ? 'agent-pulse' : ''} />
          <b>Turn {stateLabel}</b>
          {typeof init?.data.model === 'string' && <span className="badge plain">{init.data.model}</span>}
          {budget && <span className="badge plain">acts {budget.used ?? 0}/{budget.max ?? '—'} · {budget.remaining ?? '—'} left</span>}
        </div>
        {tools.map((tool) => {
          const terminal = tool.terminal
          const refused = terminal?.data.refused === true
          const label = terminal ? (refused ? 'refused' : terminal.type === 'tool.completed' ? 'completed' : 'failed') : 'running'
          return (
            <div key={tool.key} className={`agent-tool-row ${refused || label === 'failed' ? 'failed' : ''}`}>
              <span className={!terminal ? 'agent-pulse' : ''} />
              <span className="mono small">{tool.name}</span>
              <span className={`badge ${terminal?.type === 'tool.completed' ? 'green' : terminal ? 'red' : 'plain'}`}>{label}</span>
              {terminal && !refused && terminal.data.summary != null && <span className="small muted">{String(terminal.data.summary)}</span>}
            </div>
          )
        })}
      </div>
      {tools.map((tool) => {
        const event = tool.terminal
        if (!event) return null
        if (event.data.refused === true) {
          return <div key={`${tool.key}-detail`} className="agent-card agent-card-refused"><b className="small">refused ({String(event.data.act ?? tool.name)}):</b> <span className="small">{String(event.data.reason ?? '')}</span></div>
        }
        if (event.data.summary == null) return null
        return <EventView key={`${tool.key}-detail`} pid={pid} e={{
          type: 'act:result',
          act: String(event.data.act ?? tool.name),
          ok: event.type === 'tool.completed' && event.data.ok !== false,
          summary: String(event.data.summary),
          payload: event.data.payload,
        }} />
      })}
      {failed && <div className="error-box">{String(lifecycle?.data.code ?? 'TURN_FAILED')}: {String(lifecycle?.data.message ?? 'The turn failed.')}</div>}
      {response && <div className="agent-bubble agent-response-live">{response}{!completed && <span className="agent-caret" />}</div>}
    </>
  )
}

type DisplayEvent =
  | { type: 'agent:reply'; text: string }
  | { type: 'act:result'; act: string; ok: boolean; summary: string; payload?: unknown }
  | { type: 'act:refused'; act: string; reason: string }
  | { type: 'turn:error'; code: string; message: string }

function EventView({ e, pid }: { e: DisplayEvent; pid: number }): JSX.Element {
  switch (e.type) {
    case 'agent:reply':
      return <div className="agent-bubble">{e.text}</div>
    case 'act:result': {
      const payload = (e.payload ?? {}) as {
        ref?: string; state?: string; contract?: string
        filename?: string; downloadBase64?: string
        title?: string
        generatedForProject?: { code?: string; name?: string; today?: string }
        absent?: Array<{ figure?: string; reason?: string }>
        sections?: {
          projectHealth?: { value?: string }
          groups?: unknown[]
          packages?: Array<{ package?: { id?: number; code?: string; name?: string }; clientIssues?: number; holds?: number; risks?: number; actions?: number }>
          byWorkflow?: Record<string, number>
          deliverables?: unknown[]
        }
        figures?: { disciplines?: number; inWorkDeliverables?: number; issuancesThisPeriod?: number | null; packageIssueRows?: number; packageDecisionRows?: number; packageInterfaceRows?: number }
        report?: { accepted?: number; updated?: number; conflicts?: unknown[]; rejected?: unknown[]; intakeCreated?: number; error?: string } | null
      }
      const downloadHref = payload.filename && payload.downloadBase64
        ? `data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,${payload.downloadBase64}`
        : null
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
          {payload.figures && (
            <div className="small muted">
              {payload.figures.disciplines ?? 0} disciplines · {payload.figures.inWorkDeliverables ?? 0} active deliverables ·{' '}
              {payload.figures.issuancesThisPeriod == null ? 'issuances unavailable' : `${payload.figures.issuancesThisPeriod} issuances`} ·{' '}
              {payload.figures.packageIssueRows ?? 0} package issues
            </div>
          )}
          {payload.title && payload.sections && <StandardReportPreview payload={payload} pid={pid} />}
          {downloadHref && (
            <a className="btn small" href={downloadHref} download={payload.filename}>Download {payload.filename}</a>
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

function StandardReportPreview({ payload, pid }: {
  payload: {
    title?: string
    generatedForProject?: { code?: string; name?: string; today?: string }
    absent?: Array<{ figure?: string; reason?: string }>
    sections?: {
      projectHealth?: { value?: string }
      groups?: unknown[]
      packages?: Array<{ package?: { id?: number; code?: string; name?: string }; clientIssues?: number; holds?: number; risks?: number; actions?: number }>
      byWorkflow?: Record<string, number>
      deliverables?: unknown[]
    }
  }
  pid: number
}): JSX.Element {
  const sections = payload.sections ?? {}
  const issuePackages = (sections.packages ?? []).filter((row) => (row.clientIssues ?? 0) > 0)
  return (
    <div className="agent-report-preview small">
      <b>{payload.title}</b>
      <div className="muted">
        {payload.generatedForProject?.code}{payload.generatedForProject?.name ? ` — ${payload.generatedForProject.name}` : ''}
        {payload.generatedForProject?.today ? ` · ${payload.generatedForProject.today}` : ''}
      </div>
      {sections.projectHealth && (
        <div>Project health: <span className={`badge ${sections.projectHealth.value === 'red' ? 'red' : sections.projectHealth.value === 'amber' ? 'amber' : 'green'}`}>{sections.projectHealth.value}</span>{' '}
          · {sections.groups?.length ?? 0} report groups · <Link to={`/p/${pid}/overview`}>open Overview</Link>
        </div>
      )}
      {issuePackages.length > 0 && (
        <div>
          {issuePackages.length} package{issuePackages.length === 1 ? '' : 's'} with open issues:{' '}
          {issuePackages.slice(0, 6).map((row, index) => (
            <span key={row.package?.id ?? index}>{index > 0 && ', '}{row.package?.id
              ? <Link to={`/p/${pid}/packages/${row.package.id}`}>{row.package.code}</Link>
              : row.package?.code}</span>
          ))}
          {issuePackages.length > 6 && ` +${issuePackages.length - 6} more`} · <Link to={`/p/${pid}/packages`}>open Packages</Link>
        </div>
      )}
      {sections.byWorkflow && (
        <div>
          {Object.entries(sections.byWorkflow).map(([state, count]) => <span key={state} className="badge plain" style={{ marginRight: '.3rem' }}>{state} {count}</span>)}
          <Link to={`/p/${pid}/deliverables`}>open Deliverables</Link>
        </div>
      )}
      {(payload.absent?.length ?? 0) > 0 && <div className="muted">{payload.absent!.length} figure(s) unavailable; the report states each absence.</div>}
    </div>
  )
}
