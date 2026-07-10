/**
 * Shared components: HealthBadge (always click-to-explain, I-4), ExplainDrawer,
 * RegisterTable (filter + export-what-is-displayed), ConditionsPanel (§5.5 payload),
 * HistoryTrail, useLoad hook, people directory, error surfaces for 409s.
 */

import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState } from 'react'
import type { CSSProperties, PointerEvent as ReactPointerEvent, ReactNode } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
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

// ---------- record → route resolution (I-4 drill-down lands on the source) ----------

/**
 * Map a contributing/record ref to the page where that record lives, or `null` when the type
 * has no stable URL home yet. Register/log-homed records land on the matching tab with a
 * `?ref=` highlight (see useHighlightRef + RegisterTable); a deliverable lands on its own
 * detail page. work_item / revision / review_comment / check exist only inside detail-page
 * drawers keyed by a parent id the ref doesn't carry, so they stay non-navigable for now.
 */
export function refRoute(pid: number | string, recordType: string, id: number, ref: string): string | null {
  const reg = (tab: string): string => `/p/${pid}/registers/${tab}?ref=${encodeURIComponent(ref)}`
  switch (recordType) {
    case 'package': return `/p/${pid}/packages/${id}`
    case 'deliverable': return `/p/${pid}/deliverables/${id}`
    case 'hold': return reg('holds')
    case 'decision': return reg('decisions')
    case 'risk': return reg('risks')
    case 'interface_item': return reg('interfaces')
    case 'approval_record': return reg('approvals')
    case 'intake_item': return `/p/${pid}/log?ref=${encodeURIComponent(ref)}`
    case 'plan_item': return `/p/${pid}/plan`
    default: return null
  }
}

export function RecordRef({ recordType, id, recordRef, label, onNavigate, stopPropagation = true }: {
  recordType: string
  id: number | null | undefined
  recordRef: string
  label?: ReactNode
  onNavigate?: () => void
  stopPropagation?: boolean
}): JSX.Element {
  const { pid } = useApp()
  const nav = useNavigate()
  const route = id == null ? null : refRoute(pid, recordType, id, recordRef)
  const content = label ?? recordRef
  if (!route) {
    return (
      <span className="mono muted" title={`${recordType.replaceAll('_', ' ')} has no routed source yet`}>
        {content}
      </span>
    )
  }
  return (
    <button
      type="button"
      className="reflink mono"
      title={`Open ${recordType.replaceAll('_', ' ')} ${recordRef}`}
      onClick={(e) => {
        if (stopPropagation) e.stopPropagation()
        onNavigate?.()
        nav(route)
      }}
    >
      {content}
    </button>
  )
}

/** The `?ref=` deep-link target from the current URL, used to flash+scroll a landed row. */
export function useHighlightRef(): string | undefined {
  const loc = useLocation()
  return new URLSearchParams(loc.search).get('ref') ?? undefined
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
  const close = () => setState(null)
  return (
    <ExplainCtx.Provider value={{ show: (title, explain) => setState({ title, explain }) }}>
      {children}
      {state && (
        <Drawer title={`Why: ${state.title}`} onClose={close}>
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
          <ResizableTable resizeKey="explain-contributing-records">
            <tbody>
              {state.explain.contributing.map((c, i) => {
                return (
                  <tr key={i}>
                    <td className="nowrap"><RecordRef recordType={c.recordType} id={c.id} recordRef={c.ref} onNavigate={close} /></td>
                    <td className="small muted">{c.recordType.replaceAll('_', ' ')}</td>
                    <td className="small">{c.why}</td>
                  </tr>
                )
              })}
            </tbody>
          </ResizableTable>
          <p className="small muted" style={{ marginTop: '.8rem' }}>
            Derived per PRD §8 — status is computed from records, never set by hand (I-4).
            Click a contributing record to open its source.
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
    <button className="card kpi" onClick={() => show(label, explain)} title={`${explain.ruleId} - drill down`}>
      <b>{value}</b>
      <span>{label}</span>
    </button>
  )
}

// ---------- drawer ----------

export function Drawer({ title, onClose, children }: { title: ReactNode; onClose(): void; children: ReactNode }): JSX.Element {
  const drawerRef = useRef<HTMLElement | null>(null)
  const previouslyFocused = useRef<HTMLElement | null>(null)

  useEffect(() => {
    previouslyFocused.current = document.activeElement instanceof HTMLElement ? document.activeElement : null
    const focusableSelector = [
      'a[href]',
      'button:not([disabled])',
      'textarea:not([disabled])',
      'input:not([disabled])',
      'select:not([disabled])',
      '[tabindex]:not([tabindex="-1"])',
    ].join(',')
    const focusFirst = () => {
      const first = drawerRef.current?.querySelector<HTMLElement>(focusableSelector)
      ;(first ?? drawerRef.current)?.focus()
    }
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault()
        onClose()
        return
      }
      if (e.key !== 'Tab' || !drawerRef.current) return
      const focusable = Array.from(drawerRef.current.querySelectorAll<HTMLElement>(focusableSelector))
        .filter((el) => !el.hasAttribute('disabled') && el.offsetParent !== null)
      if (focusable.length === 0) {
        e.preventDefault()
        drawerRef.current.focus()
        return
      }
      const first = focusable[0]!
      const last = focusable[focusable.length - 1]!
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault()
        last.focus()
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault()
        first.focus()
      }
    }
    window.addEventListener('keydown', onKey)
    window.setTimeout(focusFirst, 0)
    return () => {
      window.removeEventListener('keydown', onKey)
      previouslyFocused.current?.focus()
    }
  }, [onClose])
  return (
    <>
      <div className="drawer-veil" onClick={onClose} />
      <aside
        ref={drawerRef}
        className="drawer"
        role="dialog"
        aria-modal="true"
        aria-labelledby="drawer-title"
        tabIndex={-1}
      >
        <h1>{title}<button className="closex" onClick={onClose} aria-label="close">✕</button></h1>
        <span id="drawer-title" className="sr-only">{textOf(title)}</span>
        {children}
      </aside>
    </>
  )
}

export function Breadcrumb({ items }: {
  items: Array<{ label: ReactNode; to?: string }>
}): JSX.Element {
  return (
    <nav className="breadcrumb" aria-label="breadcrumb">
      <ol>
        {items.map((item, i) => (
          <li key={i} aria-current={i === items.length - 1 ? 'page' : undefined}>
            {item.to && i !== items.length - 1 ? <Link to={item.to}>{item.label}</Link> : <span>{item.label}</span>}
          </li>
        ))}
      </ol>
    </nav>
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
    <ResizableTable resizeKey="history-trail">
      <tbody>
        {entries.map((h) => (
          <tr key={h.id}>
            <td className="mono nowrap small">{h.at.slice(0, 16).replace('T', ' ')}</td>
            <td className="small nowrap">{person(h.actorId)}</td>
            <td className="small"><span className="state">{h.kind}</span> {h.summary}</td>
          </tr>
        ))}
      </tbody>
    </ResizableTable>
  )
}

// ---------- register table with export-what-is-displayed ----------

const MIN_COLUMN_WIDTH = 72

/**
 * D-PEC-52: one resizing/containment primitive for every PEC table. Widths are
 * presentation-only, saved for this browser session, and never reach the API.
 */
export function ResizableTable({
  children, resizeKey, className = 'reg', style,
}: {
  children: ReactNode
  resizeKey: string
  className?: string
  style?: CSSProperties
}): JSX.Element {
  const tableRef = useRef<HTMLTableElement | null>(null)
  const suppressClick = useRef(false)
  const storageKey = `pec:table-widths:${resizeKey}`

  const headerCells = (): HTMLTableCellElement[] => {
    const table = tableRef.current
    const row = table?.tHead?.rows[0] ?? table?.tBodies[0]?.rows[0]
    return row ? Array.from(row.cells) as HTMLTableCellElement[] : []
  }
  const applyWidths = (widths: number[]): void => {
    const table = tableRef.current
    const cells = headerCells()
    if (!table || cells.length === 0 || widths.length !== cells.length) return
    cells.forEach((cell, index) => {
      const width = Math.max(MIN_COLUMN_WIDTH, Math.round(widths[index]))
      cell.style.width = `${width}px`
      cell.style.minWidth = `${width}px`
      cell.style.maxWidth = `${width}px`
    })
    table.style.tableLayout = 'fixed'
    table.style.width = `${widths.reduce((sum, width) => sum + Math.max(MIN_COLUMN_WIDTH, width), 0)}px`
  }
  const resetWidths = (): void => {
    const table = tableRef.current
    for (const cell of headerCells()) {
      cell.style.removeProperty('width')
      cell.style.removeProperty('min-width')
      cell.style.removeProperty('max-width')
    }
    table?.style.removeProperty('table-layout')
    table?.style.removeProperty('width')
    try { window.sessionStorage.removeItem(storageKey) } catch { /* storage may be unavailable */ }
  }

  useEffect(() => {
    try {
      const saved = window.sessionStorage.getItem(storageKey)
      if (saved) applyWidths(JSON.parse(saved) as number[])
    } catch { /* malformed/unavailable session storage falls back to automatic sizing */ }
  }, [storageKey])

  const edgeCell = (event: ReactPointerEvent<HTMLDivElement>): HTMLTableCellElement | null => {
    const target = event.target as HTMLElement
    const cell = target.closest('th, td') as HTMLTableCellElement | null
    if (!cell || !tableRef.current?.contains(cell)) return null
    const rect = cell.getBoundingClientRect()
    return Math.abs(event.clientX - rect.right) <= 8 ? cell : null
  }
  const beginResize = (event: ReactPointerEvent<HTMLDivElement>): void => {
    if (event.button !== 0) return
    const cell = edgeCell(event)
    if (!cell) return
    const cells = headerCells()
    const index = cells.indexOf(cell)
    if (index < 0 || !tableRef.current) return
    event.preventDefault()
    event.stopPropagation()
    const initialWidths = cells.map((candidate) => candidate.getBoundingClientRect().width)
    applyWidths(initialWidths)
    const startX = event.clientX
    const startWidth = initialWidths[index]
    const startTableWidth = initialWidths.reduce((sum, width) => sum + width, 0)
    let moved = false
    const previousCursor = document.body.style.cursor
    const previousSelection = document.body.style.userSelect
    document.body.style.cursor = 'col-resize'
    document.body.style.userSelect = 'none'
    const move = (pointer: PointerEvent): void => {
      const delta = pointer.clientX - startX
      if (Math.abs(delta) > 2) moved = true
      const width = Math.max(MIN_COLUMN_WIDTH, startWidth + delta)
      cell.style.width = `${width}px`
      cell.style.minWidth = `${width}px`
      cell.style.maxWidth = `${width}px`
      tableRef.current!.style.width = `${startTableWidth + width - startWidth}px`
    }
    const finish = (): void => {
      window.removeEventListener('pointermove', move)
      window.removeEventListener('pointerup', finish)
      window.removeEventListener('pointercancel', finish)
      document.body.style.cursor = previousCursor
      document.body.style.userSelect = previousSelection
      suppressClick.current = moved
      window.setTimeout(() => { suppressClick.current = false }, 0)
      const widths = headerCells().map((candidate) => candidate.getBoundingClientRect().width)
      try { window.sessionStorage.setItem(storageKey, JSON.stringify(widths)) } catch { /* presentation still works */ }
    }
    window.addEventListener('pointermove', move)
    window.addEventListener('pointerup', finish, { once: true })
    window.addEventListener('pointercancel', finish, { once: true })
  }
  const resetAtEdge = (event: ReactPointerEvent<HTMLDivElement>): void => {
    if (!edgeCell(event)) return
    event.preventDefault()
    event.stopPropagation()
    resetWidths()
  }

  return (
    <div className="table-scroll" onPointerDownCapture={beginResize}
      onDoubleClickCapture={resetAtEdge}
      onClickCapture={(event) => {
        if (!suppressClick.current) return
        suppressClick.current = false
        event.preventDefault()
        event.stopPropagation()
      }}>
      <table ref={tableRef} className={className} style={style}>{children}</table>
    </div>
  )
}

export interface Col<T> {
  key: string
  label: string
  render(row: T): ReactNode
  csv?(row: T): string | number | null
  /** Value used by the direct table sort control; falls back to CSV/display text. */
  sortValue?(row: T): string | number | null | undefined
  sortable?: boolean
}

export function RegisterTable<T>({
  cols, rows, exportName, onRowClick, highlightRef, rowRef, wide, stickyFirstColumn,
}: {
  cols: Array<Col<T>>
  rows: T[]
  exportName?: string
  onRowClick?(row: T): void
  /** ref of a row to flash + scroll into view on mount (deep-link landing, see useHighlightRef) */
  highlightRef?: string
  /** how to read a row's ref for highlight matching */
  rowRef?(row: T): string
  /** contain wide register tables inside their region instead of widening the page */
  wide?: boolean
  /** keep the first identifying column visible while horizontally scrolling wide registers */
  stickyFirstColumn?: boolean
}): JSX.Element {
  const flashRow = useRef<HTMLTableRowElement | null>(null)
  const [sortKey, setSortKey] = useState<string | null>(null)
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc')
  const sortedRows = useMemo(() => {
    if (!sortKey) return rows
    const col = cols.find((candidate) => candidate.key === sortKey)
    if (!col) return rows
    const value = (row: T): string | number | null | undefined => col.sortValue?.(row)
      ?? col.csv?.(row) ?? textOf(col.render(row))
    const compare = (a: T, b: T): number => {
      const av = value(a)
      const bv = value(b)
      if (av == null || av === '') return bv == null || bv === '' ? 0 : 1
      if (bv == null || bv === '') return -1
      if (typeof av === 'number' && typeof bv === 'number') return av - bv
      return String(av).localeCompare(String(bv), undefined, { numeric: true, sensitivity: 'base' })
    }
    return rows.map((row, index) => ({ row, index }))
      .sort((a, b) => (compare(a.row, b.row) || a.index - b.index) * (sortDirection === 'asc' ? 1 : -1))
      .map(({ row }) => row)
  }, [cols, rows, sortDirection, sortKey])
  useEffect(() => {
    if (highlightRef && flashRow.current) {
      flashRow.current.scrollIntoView({ block: 'center', behavior: 'smooth' })
    }
  }, [highlightRef, rows])
  const exportCsv = () => {
    const esc = (v: unknown) => {
      const s = v == null ? '' : String(v)
      return /[",\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s
    }
    const lines = [
      cols.map((c) => esc(c.label)).join(','),
      ...sortedRows.map((r) => cols.map((c) => esc(c.csv ? c.csv(r) : textOf(c.render(r)))).join(',')),
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
          <button className="btn secondary small" onClick={exportCsv}>Export CSV ({sortedRows.length} rows)</button>
        </div>
      )}
      <ResizableTable resizeKey={`register:${exportName ?? cols.map((col) => col.key).join('|')}`}
        style={wide ? { minWidth: '980px' } : undefined}>
        <thead><tr>{cols.map((c, idx) => {
          const active = sortKey === c.key
          const sortable = c.sortable !== false
          return (
          <th key={c.key} aria-sort={active ? (sortDirection === 'asc' ? 'ascending' : 'descending') : 'none'}
            className={stickyFirstColumn && idx === 0 ? 'sticky-first' : undefined}
            style={stickyFirstColumn && idx === 0 ? {
            left: 0, zIndex: 3,
          } : undefined}>{sortable ? (
            <button type="button" className={`table-sort${active ? ' active' : ''}`} onClick={() => {
              if (active) setSortDirection((direction) => direction === 'asc' ? 'desc' : 'asc')
              else { setSortKey(c.key); setSortDirection('asc') }
            }}>
              {c.label}<span aria-hidden="true">{active ? (sortDirection === 'asc' ? ' ▲' : ' ▼') : ' ⇅'}</span>
            </button>
          ) : c.label}</th>
          )
        })}</tr></thead>
        <tbody>
          {sortedRows.map((r, i) => {
            const hit = highlightRef != null && rowRef?.(r) === highlightRef
            const cls = [onRowClick ? 'clickable' : '', hit ? 'row-flash' : ''].filter(Boolean).join(' ')
            return (
              <tr key={i} ref={hit ? flashRow : undefined} className={cls || undefined}
                role={onRowClick ? 'button' : undefined}
                tabIndex={onRowClick ? 0 : undefined}
                onClick={onRowClick ? () => onRowClick(r) : undefined}
                onKeyDown={onRowClick ? (e) => {
                  if (e.target !== e.currentTarget) return
                  if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault()
                    onRowClick(r)
                  }
                } : undefined}>
                {cols.map((c, idx) => (
                  <td key={c.key} className={stickyFirstColumn && idx === 0 ? 'sticky-first' : undefined}
                    style={stickyFirstColumn && idx === 0 ? {
                    position: 'sticky', left: 0, zIndex: 1, background: 'var(--surface)',
                  } : undefined}>{c.render(r)}</td>
                ))}
              </tr>
            )
          })}
          {rows.length === 0 && <tr><td colSpan={cols.length} className="muted small">no records</td></tr>}
        </tbody>
      </ResizableTable>
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

// ---------- workflow completeness (deliverable status = production-workflow progress) ----------

export interface WorkflowInfo {
  currentState: string
  revCode: string | null
  stages: Array<{ key: string; label: string; state: 'done' | 'current' | 'pending' }>
  gatesClosed: number
  gatesTotal: number
  pct: number
  label: string
  returned: boolean
  superseded: boolean
}

/** Compact gate-progress indicator: drafted → checked → approved → issued. */
export function WorkflowStages({ workflow, showLabel = true }: { workflow: WorkflowInfo; showLabel?: boolean }): JSX.Element {
  const w = workflow
  return (
    <span className={`wf${w.superseded ? ' superseded' : ''}`}
      title={`${w.label}${w.revCode ? ` · rev ${w.revCode}` : ''} · ${w.gatesClosed}/${w.gatesTotal} gates closed`}>
      <span className="wf-dots" aria-hidden>
        {w.stages.map((s) => <span key={s.key} className={`wf-dot ${s.state}`} title={s.label} />)}
      </span>
      {showLabel && <span className="wf-label small">{w.label}</span>}
    </span>
  )
}
