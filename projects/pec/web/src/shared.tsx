/**
 * Shared components: HealthBadge (always click-to-explain, I-4), ExplainDrawer,
 * RegisterTable (filter + export-what-is-displayed), ConditionsPanel (§5.5 payload),
 * HistoryTrail, useLoad hook, people directory, error surfaces for 409s.
 */

import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'
import type { ReactNode } from 'react'
import { api } from './api.ts'
import type { Explain, Health, Me, ProjectRef } from './api.ts'

// ---------- session/context ----------

export interface AppCtx {
  me: Me
  projects: ProjectRef[]
  pid: number
  people: Array<{ id: number; name: string; email: string; discipline: string | null }>
  refreshKey: number
  refresh(): void
  toast(msg: string): void
}

export const AppContext = createContext<AppCtx | null>(null)
export function useApp(): AppCtx {
  const ctx = useContext(AppContext)
  if (!ctx) throw new Error('AppContext missing')
  return ctx
}

export function usePerson(): (id: number | null | undefined) => string {
  const { people } = useApp()
  const map = useMemo(() => new Map(people.map((p) => [p.id, p.name])), [people])
  return useCallback((id) => (id == null ? '—' : map.get(id) ?? `#${id}`), [map])
}

/** Load data with automatic reload when the app-wide refresh key bumps. */
export function useLoad<T>(fn: () => Promise<T>, deps: unknown[] = []): {
  data: T | null
  error: string | null
  reload(): void
} {
  const { refreshKey } = useApp()
  const [data, setData] = useState<T | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [localKey, setLocalKey] = useState(0)
  useEffect(() => {
    let live = true
    fn().then(
      (d) => { if (live) { setData(d); setError(null) } },
      (e) => { if (live) setError(e.message ?? String(e)) },
    )
    return () => { live = false }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [...deps, refreshKey, localKey])
  return { data, error, reload: () => setLocalKey((k) => k + 1) }
}

// ---------- explain drawer (I-4) ----------

interface ExplainState {
  title: string
  explain: Explain
}

const ExplainCtx = createContext<{ show(title: string, e: Explain): void } | null>(null)
export function useExplain(): (title: string, e: Explain) => void {
  const ctx = useContext(ExplainCtx)
  if (!ctx) throw new Error('ExplainCtx missing')
  return ctx.show
}

export function ExplainProvider({ children }: { children: ReactNode }): JSX.Element {
  const [state, setState] = useState<ExplainState | null>(null)
  return (
    <ExplainCtx.Provider value={{ show: (title, explain) => setState({ title, explain }) }}>
      {children}
      {state && (
        <Drawer title={`Why: ${state.title}`} onClose={() => setState(null)}>
          <p>
            <span className={`badge ${typeof state.explain.value === 'string' ? state.explain.value : 'plain'}`}>
              {typeof state.explain.value === 'object' ? 'value' : String(state.explain.value)}
            </span>{' '}
            <span className="explain-rule">{state.explain.ruleId}</span>
          </p>
          <p>{state.explain.detail}</p>
          {state.explain.threshold && <p className="small muted">Threshold: {state.explain.threshold}</p>}
          <h2>Contributing records</h2>
          {state.explain.contributing.length === 0 && <p className="muted small">none — nothing degrading this value</p>}
          <table className="reg">
            <tbody>
              {state.explain.contributing.map((c, i) => (
                <tr key={i}>
                  <td className="mono nowrap">{c.ref}</td>
                  <td className="small muted">{c.recordType.replaceAll('_', ' ')}</td>
                  <td className="small">{c.why}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <p className="small muted" style={{ marginTop: '.8rem' }}>
            Derived per PRD §8 — status is computed from records, never set by hand (I-4).
          </p>
        </Drawer>
      )}
    </ExplainCtx.Provider>
  )
}

export function HealthBadge({ explain, label }: { explain: Explain<Health> | Explain; label?: string }): JSX.Element {
  const show = useExplain()
  const v = String(explain.value)
  return (
    <button
      className={`badge ${v === 'green' || v === 'amber' || v === 'red' ? v : 'plain'}`}
      title={`${explain.ruleId}: ${explain.detail} — click for contributing records`}
      onClick={(e) => { e.stopPropagation(); show(label ?? 'health', explain as Explain) }}
    >
      {v}
    </button>
  )
}

export function KpiCard({ label, value, explain }: { label: string; value: ReactNode; explain: Explain }): JSX.Element {
  const show = useExplain()
  return (
    <div className="card kpi" onClick={() => show(label, explain)} title={`${explain.ruleId} — click to drill down`}>
      <b>{value}</b>
      <span>{label}</span>
    </div>
  )
}

// ---------- drawer ----------

export function Drawer({ title, onClose, children }: { title: ReactNode; onClose(): void; children: ReactNode }): JSX.Element {
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') onClose() }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [onClose])
  return (
    <>
      <div className="drawer-veil" onClick={onClose} />
      <aside className="drawer">
        <h1>{title}<button className="closex" onClick={onClose} aria-label="close">✕</button></h1>
        {children}
      </aside>
    </>
  )
}

// ---------- conditions panel (§5.5, PEC-DEL-004) ----------

export interface TransitionExplanation {
  gate: string
  permitted: boolean
  holdVeto: Array<{ ref: string; cause: string; title: string; ownerId: number }>
  conditions: Array<{
    ref: string; description: string; type: string; severity: string; state: string
    ownerId: number | null; needBy: string | null
    satisfiedBy: { ref: string; recordType: string; why: string } | null
    waiverDecisionRef: string | null; note: string | null
  }>
}

export function ConditionsPanel({ ex, title }: { ex: TransitionExplanation; title?: string }): JSX.Element {
  const person = usePerson()
  return (
    <div>
      <h2>{title ?? 'Before this issues'} {ex.permitted
        ? <span className="badge green">clear</span>
        : <span className="badge red">blocked</span>}</h2>
      {ex.holdVeto.length > 0 && ex.holdVeto.map((h) => (
        <div className="cond blocked_by_hold" key={h.ref}>
          <span className="badge hold">hold</span>{' '}
          <span className="mono">{h.ref}</span> {h.title} <span className="muted small">({h.cause}, owner {person(h.ownerId)})</span>
        </div>
      ))}
      {ex.conditions.length === 0 && ex.holdVeto.length === 0 && (
        <p className="muted small">No conditions attached to this transition.</p>
      )}
      {ex.conditions.map((c) => (
        <div className={`cond ${c.state}`} key={c.ref}>
          <span className={`state ${c.state}`}>{c.state.replaceAll('_', ' ')}</span>{' '}
          <b className="small">{c.severity === 'hard' ? '⛔' : '⚠︎'}</b>{' '}
          <span className="mono">{c.ref}</span> {c.description}
          <div className="small muted">
            {c.type} · owner {person(c.ownerId)} · need-by {c.needBy ?? '—'}
            {c.satisfiedBy && <> · satisfied by <span className="mono">{c.satisfiedBy.ref}</span> ({c.satisfiedBy.why})</>}
            {c.waiverDecisionRef && <> · waived by <span className="mono">{c.waiverDecisionRef}</span></>}
            {c.note && <> · {c.note}</>}
          </div>
        </div>
      ))}
    </div>
  )
}

// ---------- history trail (PEC-DEL-005) ----------

export function HistoryTrail({ entries }: { entries: Array<{ id: number; at: string; actorId: number; kind: string; summary: string }> }): JSX.Element {
  const person = usePerson()
  return (
    <table className="reg">
      <tbody>
        {entries.map((h) => (
          <tr key={h.id}>
            <td className="mono nowrap small">{h.at.slice(0, 16).replace('T', ' ')}</td>
            <td className="small nowrap">{person(h.actorId)}</td>
            <td className="small"><span className="state">{h.kind}</span> {h.summary}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}

// ---------- register table with export-what-is-displayed ----------

export interface Col<T> {
  key: string
  label: string
  render(row: T): ReactNode
  csv?(row: T): string | number | null
}

export function RegisterTable<T>({ cols, rows, exportName, onRowClick }: {
  cols: Array<Col<T>>
  rows: T[]
  exportName?: string
  onRowClick?(row: T): void
}): JSX.Element {
  const exportCsv = () => {
    const esc = (v: unknown) => {
      const s = v == null ? '' : String(v)
      return /[",\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s
    }
    const lines = [
      cols.map((c) => esc(c.label)).join(','),
      ...rows.map((r) => cols.map((c) => esc(c.csv ? c.csv(r) : textOf(c.render(r)))).join(',')),
    ]
    const blob = new Blob([lines.join('\r\n')], { type: 'text/csv' })
    const a = document.createElement('a')
    a.href = URL.createObjectURL(blob)
    a.download = exportName ?? 'register.csv'
    a.click()
    URL.revokeObjectURL(a.href)
  }
  return (
    <div>
      {exportName && (
        <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: '.35rem' }}>
          <button className="btn secondary small" onClick={exportCsv}>Export CSV ({rows.length} rows)</button>
        </div>
      )}
      <table className="reg">
        <thead><tr>{cols.map((c) => <th key={c.key}>{c.label}</th>)}</tr></thead>
        <tbody>
          {rows.map((r, i) => (
            <tr key={i} className={onRowClick ? 'clickable' : undefined} onClick={onRowClick ? () => onRowClick(r) : undefined}>
              {cols.map((c) => <td key={c.key}>{c.render(r)}</td>)}
            </tr>
          ))}
          {rows.length === 0 && <tr><td colSpan={cols.length} className="muted small">no records</td></tr>}
        </tbody>
      </table>
    </div>
  )
}

function textOf(node: ReactNode): string {
  if (node == null || typeof node === 'boolean') return ''
  if (typeof node === 'string' || typeof node === 'number') return String(node)
  if (Array.isArray(node)) return node.map(textOf).join(' ')
  if (typeof node === 'object' && 'props' in (node as any)) return textOf((node as any).props.children)
  return ''
}

// ---------- 409 error rendering ----------

export function ErrorBox({ error }: { error: any }): JSX.Element | null {
  if (!error) return null
  if (error.code === 'CONDITIONS_OPEN' && error.details) {
    return (
      <div className="error-box">
        <b>Transition blocked (I-5)</b> — the attempt was recorded with the open conditions:
        <ConditionsPanel ex={error.details} title="Open on this gate" />
      </div>
    )
  }
  if (error.code === 'VERSION_CONFLICT') {
    return (
      <div className="error-box">
        <b>Someone changed this record while you were editing (PEC-NFR-004).</b> Reload to see the
        intervening change; your write was not applied.
      </div>
    )
  }
  return <div className="error-box">{error.message ?? String(error)}</div>
}

export function fmtDate(d: string | null | undefined): string {
  return d ? d.slice(0, 10) : '—'
}

export function StateTag({ s }: { s: string }): JSX.Element {
  return <span className={`state ${s}`}>{s.replaceAll('_', ' ')}</span>
}
