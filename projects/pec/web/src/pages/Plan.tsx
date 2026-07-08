/**
 * Plan — "What is committed, and can we do it?" (Planner home, PRD §12.4, P2).
 * Now/Next/Later horizons (PEC-PLAN-001), six-week lookahead (PEC-PLAN-002), capacity by
 * discipline with check/approval hours loading like work (PEC-PLAN-003, I-9), overcapacity
 * flags that can raise a Risk (PEC-PLAN-004), the shift workflow with reasons and lead
 * review (PEC-PLAN-005/006/008), and the weekly commit that generates My Week
 * (PEC-PLAN-007). All rules server-side; this page renders and posts (SPEC §1).
 */

import { useState } from 'react'
import { api, p } from '../api.ts'
import type { PecApiError } from '../api.ts'
import { Drawer, ErrorBox, RecordRef, RegisterTable, fmtDate, useApp, useLoad, usePerson } from '../shared.tsx'
import type { Col } from '../shared.tsx'

const HORIZONS = ['now', 'next', 'later'] as const
const CAP_COLOR: Record<string, string> = { red: 'red', warn: 'amber', none: 'green' }

interface PlanItemRow {
  id: number; ref: string; itemType: string; itemId: number; version: number
  horizon: string; week: string | null; discipline: string | null; plannedHours: number
  itemRef: string; title: string; responsibleId: number | null; needBy: string | null
  deliverableDocNo: string | null; packageCode: string | null; open: boolean
}

export function PlanPage(): JSX.Element {
  const { pid, toast, refresh } = useApp()
  const person = usePerson()
  const { data, error } = useLoad<any>(() => api.get(p(pid, 'plan')), [pid])
  const [drawer, setDrawer] = useState<null | { kind: 'add' } | { kind: 'shift'; item: PlanItemRow } | { kind: 'capacity' }>(null)
  const [busy, setBusy] = useState(false)
  const [actionError, setActionError] = useState<PecApiError | null>(null)

  if (error) return <ErrorBox error={{ message: error }} />
  if (!data) return <p className="muted">loading…</p>

  const currentPeriod = data.periods.find((x: any) => x.week === data.currentWeek)
  const committed = currentPeriod?.state === 'committed'

  const commitWeek = async (): Promise<void> => {
    setBusy(true); setActionError(null)
    try {
      const r = await api.post<any>(p(pid, 'plan/commit'), { week: data.currentWeek })
      toast(`week ${r.week} committed — ${r.committedWorkItems} item(s) stamped into My Week, ${r.notified} notified (PEC-PLAN-007)`)
      refresh()
    } catch (e) { setActionError(e as PecApiError) } finally { setBusy(false) }
  }

  const reviewShift = async (shift: any, approve: boolean): Promise<void> => {
    setActionError(null)
    try {
      await api.post(p(pid, `plan-shifts/${shift.id}/review`), { version: shift.version, approve })
      toast(`${shift.ref} ${approve ? 'approved — move applied' : 'rejected'}`)
      refresh()
    } catch (e) { setActionError(e as PecApiError) }
  }

  const raiseCapacityRisk = async (cell: any): Promise<void> => {
    setActionError(null)
    try {
      const r = await api.post<any>(p(pid, 'risks'), {
        title: `Capacity overload — ${cell.discipline} ${cell.week}`,
        cause: `committed load ${cell.loadH} h vs capacity ${cell.capacityH} h (${cell.pct}%)`,
        consequence: 'committed work will not complete in the week; schedule pressure',
        state: 'open', probability: 4, impact: 3,
        mitigation: 'rebalance the plan or add capacity',
      })
      toast(`${r.ref} raised from the overload (PEC-PLAN-004)`)
      refresh()
    } catch (e) { setActionError(e as PecApiError) }
  }

  const horizonCol = (h: (typeof HORIZONS)[number]): JSX.Element => (
    <div className="card" style={{ flex: 1, minWidth: 240 }} key={h}>
      <h3 style={{ marginTop: 0 }}>
        {h === 'now' ? 'Now' : h === 'next' ? 'Next' : 'Later'}{' '}
        <span className="muted small">{h === 'now' ? 'named owner + confirmed capacity' : h === 'next' ? 'queued' : 'unscheduled backlog'}</span>
      </h3>
      {data.horizons[h].length === 0 && <p className="muted small">nothing here</p>}
      {data.horizons[h].map((it: PlanItemRow) => (
        <div key={it.id} className="cond" style={{ marginBottom: '.4rem' }}>
          <div>
            <RecordRef recordType={it.itemType} id={it.itemId} ref={it.itemRef} /> <b>{it.title}</b>{' '}
            {!it.open && <span className="badge plain">done</span>}
          </div>
          <div className="small muted">
            {it.itemType.replaceAll('_', ' ')} · {it.plannedHours} h {it.discipline ?? '—'}
            {it.week ? ` · ${it.week}` : ''} · {person(it.responsibleId)}
            {it.deliverableDocNo ? ` · ${it.deliverableDocNo}` : ''}
            {it.packageCode ? ` · ${it.packageCode}` : ''}
          </div>
          <button className="btn small secondary" onClick={() => setDrawer({ kind: 'shift', item: it })}>
            shift…
          </button>
        </div>
      ))}
    </div>
  )

  const shiftCols: Array<Col<any>> = [
    { key: 'ref', label: 'Shift', render: (s) => <span className="mono">{s.ref}</span> },
    { key: 'item', label: 'Item', render: (s) => <span className="small">{s.itemRef} {s.title}</span> },
    {
      key: 'move', label: 'Move', render: (s) => (
        <span className="small nowrap">{s.fromHorizon}{s.fromWeek ? `/${s.fromWeek}` : ''} → {s.toHorizon}{s.toWeek ? `/${s.toWeek}` : ''}</span>
      ),
    },
    { key: 'reason', label: 'Reason (PEC-PLAN-006)', render: (s) => <span className="small">{s.reason}{s.impactStatement ? <span className="muted"> — {s.impactStatement}</span> : null}</span> },
    { key: 'x', label: 'Cross-pkg', render: (s) => s.crossPackage ? <span className="badge amber">{s.affectedPackages.join(', ')}</span> : <span className="muted small">no</span> },
    {
      key: 'state', label: 'State', render: (s) => s.state === 'proposed'
        ? (
          <span className="nowrap">
            <span className="badge amber">proposed</span>{' '}
            <button className="btn small" onClick={() => void reviewShift(s, true)}>approve</button>{' '}
            <button className="btn small danger" onClick={() => void reviewShift(s, false)}>reject</button>
          </span>
        )
        : <span className={`badge ${s.state === 'applied' ? 'green' : 'plain'}`}>{s.state}</span>,
    },
    { key: 'by', label: 'By', render: (s) => <span className="small">{person(s.createdBy)} {fmtDate(s.createdAt)}</span> },
  ]

  return (
    <div>
      <h1>Plan — what is committed, and can we do it?</h1>
      {actionError && <ErrorBox error={actionError} />}

      <div className="row" style={{ alignItems: 'center', gap: '.6rem', margin: '.5rem 0', flexWrap: 'wrap' }}>
        <b>Week {data.currentWeek}</b>
        {committed
          ? <span className="badge green">committed {fmtDate(currentPeriod.committedAt)}</span>
          : <span className="badge amber">not committed</span>}
        <button className="btn" disabled={busy} onClick={() => void commitWeek()}>
          {committed ? 'Re-commit week' : 'Commit week'} → generates My Week
        </button>
        <button className="btn secondary" onClick={() => setDrawer({ kind: 'add' })}>Plan a record…</button>
        <button className="btn secondary" onClick={() => setDrawer({ kind: 'capacity' })}>Set capacity…</button>
        <button className="btn secondary" onClick={() => window.open(p(pid, 'export/lookahead.csv'))}>Export lookahead</button>
      </div>

      <h2>Now / Next / Later (PEC-PLAN-001)</h2>
      <div className="row" style={{ gap: '.6rem', alignItems: 'stretch', flexWrap: 'wrap' }}>
        {HORIZONS.map(horizonCol)}
      </div>

      <h2>Capacity by discipline (PEC-PLAN-003) <span className="muted small">check &amp; approval hours load capacity (I-9)</span></h2>
      <div style={{ overflowX: 'auto' }}>
        <table className="reg">
          <thead>
            <tr>
              <th>Week</th><th>Discipline</th><th>Load (h)</th><th>Work / check / approve</th>
              <th>Capacity (h)</th><th>%</th><th></th>
            </tr>
          </thead>
          <tbody>
            {data.capacity.length === 0 && <tr><td colSpan={7} className="muted">no planned load — plan records and set capacity</td></tr>}
            {data.capacity.map((c: any) => (
              <tr key={`${c.week}|${c.discipline}`}>
                <td className="nowrap">{c.week}{c.week === data.currentWeek ? ' ←' : ''}</td>
                <td>{c.discipline}</td>
                <td>{c.loadH}</td>
                <td className="small muted">{c.byType.work_item} / {c.byType.check} / {c.byType.approval_record}</td>
                <td>{c.capacityH ?? <span className="muted">not set</span>}</td>
                <td>{c.pct != null
                  ? <span className={`badge ${CAP_COLOR[c.level]}`}>{c.pct}%</span>
                  : c.level !== 'none'
                    ? <span className={`badge ${CAP_COLOR[c.level]}`} title="load against a zero-hour capacity baseline">over</span>
                    : <span className="muted">—</span>}</td>
                <td>
                  {c.level !== 'none' && (
                    <button className="btn small secondary" title="overcapacity may create or link a Risk (PEC-PLAN-004)"
                      onClick={() => void raiseCapacityRisk(c)}>raise risk</button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <h2>Six-week lookahead (PEC-PLAN-002)</h2>
      <p className="section-note">
        Rows are deliverables; cells derive from the plan and the schedule import — Hold-by-cause,
        Issue (due week), Approve, Check, Work. {data.scheduleActivityCount > 0
          ? `${data.scheduleActivityCount} schedule activities imported.`
          : 'No schedule activities imported yet (Admin → Import → schedule).'}
      </p>
      <div style={{ overflowX: 'auto' }}>
        <table className="reg">
          <thead>
            <tr><th>Deliverable</th>{data.weeks.map((w: string) => <th key={w} className="nowrap">{w}</th>)}</tr>
          </thead>
          <tbody>
            {data.lookahead.filter((r: any) => r.cells.some((c: any) => c != null)).map((r: any) => (
              <tr key={r.deliverableId}>
                <td className="nowrap">
                  <span className="mono">{r.docNo}</span>
                  <div className="small muted">{r.packageCode} · due {fmtDate(r.dueDate)}</div>
                </td>
                {r.cells.map((c: any, i: number) => (
                  <td key={i}>
                    {c && (
                      <span className={`badge ${c.state === 'hold' ? 'red' : c.state === 'issue' ? 'green' : c.state === 'approve' ? 'amber' : 'plain'}`}
                        title={c.detail}>
                        {c.state}
                      </span>
                    )}
                  </td>
                ))}
              </tr>
            ))}
            {data.lookahead.every((r: any) => r.cells.every((c: any) => c == null)) && (
              <tr><td colSpan={1 + data.weeks.length} className="muted">nothing planned or scheduled in the next six weeks</td></tr>
            )}
          </tbody>
        </table>
      </div>

      <h2>Plan-change log (PEC-PLAN-005/006)</h2>
      <RegisterTable cols={shiftCols} rows={data.shifts} exportName="plan-shifts.csv" />

      {drawer?.kind === 'add' && (
        <AddPlanItemDrawer plannable={data.plannable} currentWeek={data.currentWeek} onClose={() => setDrawer(null)} />
      )}
      {drawer?.kind === 'shift' && (
        <ShiftDrawer item={drawer.item} currentWeek={data.currentWeek} onClose={() => setDrawer(null)} />
      )}
      {drawer?.kind === 'capacity' && (
        <CapacityDrawer currentWeek={data.currentWeek} onClose={() => setDrawer(null)} />
      )}
    </div>
  )
}

function AddPlanItemDrawer({ plannable, currentWeek, onClose }: {
  plannable: Array<{ itemType: string; itemId: number; ref: string; label: string }>
  currentWeek: string
  onClose: () => void
}): JSX.Element {
  const { pid, toast, refresh } = useApp()
  const [itemType, setItemType] = useState('work_item')
  const [key, setKey] = useState('')
  const [horizon, setHorizon] = useState('now')
  const [week, setWeek] = useState(currentWeek)
  const [hours, setHours] = useState('8')
  const [discipline, setDiscipline] = useState('')
  const [error, setError] = useState<PecApiError | null>(null)
  const [busy, setBusy] = useState(false)
  const options = plannable.filter((x) => x.itemType === itemType)

  const submit = async (): Promise<void> => {
    setBusy(true); setError(null)
    try {
      const [t, id] = key.split(':')
      const r = await api.post<any>(p(pid, 'plan-items'), {
        itemType: t, itemId: Number(id), horizon,
        week: horizon === 'later' ? null : week,
        plannedHours: Number(hours) || 0,
        discipline: discipline || undefined,
      })
      toast(`${r.ref} planned`)
      refresh(); onClose()
    } catch (e) { setError(e as PecApiError) } finally { setBusy(false) }
  }

  return (
    <Drawer title="Plan a record (PEC-PLAN-001, I-9)" onClose={onClose}>
      <div className="stack">
        {error && <ErrorBox error={error} />}
        <label>What loads the week
          <select value={itemType} onChange={(e) => { setItemType(e.target.value); setKey('') }}>
            <option value="work_item">work item</option>
            <option value="check">check (I-9)</option>
            <option value="approval_record">approval (I-9)</option>
          </select>
        </label>
        <label>Record
          <select value={key} onChange={(e) => setKey(e.target.value)}>
            <option value="">— pick —</option>
            {options.map((o) => <option key={`${o.itemType}:${o.itemId}`} value={`${o.itemType}:${o.itemId}`}>{o.label}</option>)}
          </select>
        </label>
        <label>Horizon
          <select value={horizon} onChange={(e) => setHorizon(e.target.value)}>
            <option value="now">now</option><option value="next">next</option><option value="later">later (backlog)</option>
          </select>
        </label>
        {horizon !== 'later' && (
          <label>Week (ISO, e.g. {currentWeek})
            <input value={week} onChange={(e) => setWeek(e.target.value)} />
          </label>
        )}
        <label>Planned hours
          <input type="number" min="0" value={hours} onChange={(e) => setHours(e.target.value)} />
        </label>
        <label>Discipline <span className="muted small">(defaults from the responsible person)</span>
          <input value={discipline} onChange={(e) => setDiscipline(e.target.value)} placeholder="Process" />
        </label>
        <button className="btn" disabled={busy || !key} onClick={() => void submit()}>Plan it</button>
      </div>
    </Drawer>
  )
}

function ShiftDrawer({ item, currentWeek, onClose }: {
  item: PlanItemRow
  currentWeek: string
  onClose: () => void
}): JSX.Element {
  const { pid, toast, refresh } = useApp()
  const { data: risks } = useLoad<any[]>(() => api.get(p(pid, 'risks')), [pid])
  const [toHorizon, setToHorizon] = useState(item.horizon)
  const [toWeek, setToWeek] = useState(item.week ?? currentWeek)
  const [reason, setReason] = useState('')
  const [impact, setImpact] = useState('')
  const [riskId, setRiskId] = useState('')
  const [error, setError] = useState<PecApiError | null>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (): Promise<void> => {
    setBusy(true); setError(null)
    try {
      const r = await api.post<any>(p(pid, `plan-items/${item.id}/shift`), {
        version: item.version, toHorizon,
        toWeek: toHorizon === 'later' ? null : toWeek,
        reason, impactStatement: impact || undefined,
        links: riskId ? [{ recordType: 'risk', recordId: Number(riskId) }] : undefined,
      })
      toast(r.state === 'proposed'
        ? `${r.ref} proposed — affected leads asked to review (PEC-PLAN-005)`
        : `${r.ref} applied`)
      refresh(); onClose()
    } catch (e) { setError(e as PecApiError) } finally { setBusy(false) }
  }

  return (
    <Drawer title={`Shift ${item.itemRef} (PEC-PLAN-005/006/008)`} onClose={onClose}>
      <div className="stack">
        {error && <ErrorBox error={error} />}
        <p className="small muted">
          {item.horizon}{item.week ? `/${item.week}` : ''} → … Every shift records its reason;
          cross-package impacts need an impact statement and lead review.
        </p>
        <label>To horizon
          <select value={toHorizon} onChange={(e) => setToHorizon(e.target.value)}>
            <option value="now">now</option><option value="next">next</option><option value="later">later</option>
          </select>
        </label>
        {toHorizon !== 'later' && (
          <label>To week
            <input value={toWeek} onChange={(e) => setToWeek(e.target.value)} />
          </label>
        )}
        <label>Reason (required)
          <input value={reason} onChange={(e) => setReason(e.target.value)} placeholder="why the plan is changing" />
        </label>
        <label>Impact statement <span className="muted small">(milestones, capacity, affected deliverables — required when crossing packages)</span>
          <textarea value={impact} onChange={(e) => setImpact(e.target.value)} rows={2} />
        </label>
        <label>Link an affected risk <span className="muted small">(PEC-PLAN-008, optional)</span>
          <select value={riskId} onChange={(e) => setRiskId(e.target.value)}>
            <option value="">—</option>
            {(risks ?? []).filter((r: any) => r.state !== 'closed').map((r: any) => (
              <option key={r.id} value={r.id}>{r.ref} — {r.title}</option>
            ))}
          </select>
        </label>
        <button className="btn" disabled={busy || !reason} onClick={() => void submit()}>Shift</button>
      </div>
    </Drawer>
  )
}

function CapacityDrawer({ currentWeek, onClose }: { currentWeek: string; onClose: () => void }): JSX.Element {
  const { pid, toast, refresh } = useApp()
  const [week, setWeek] = useState(currentWeek)
  const [discipline, setDiscipline] = useState('')
  const [hours, setHours] = useState('40')
  const [error, setError] = useState<PecApiError | null>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (): Promise<void> => {
    setBusy(true); setError(null)
    try {
      await api.put(p(pid, 'plan/capacity'), { week, discipline, hours: Number(hours) || 0 })
      toast(`capacity set: ${discipline} ${week} = ${hours} h`)
      refresh(); onClose()
    } catch (e) { setError(e as PecApiError) } finally { setBusy(false) }
  }

  return (
    <Drawer title="Set capacity (PEC-PLAN-003)" onClose={onClose}>
      <div className="stack">
        {error && <ErrorBox error={error} />}
        <label>Week<input value={week} onChange={(e) => setWeek(e.target.value)} /></label>
        <label>Discipline<input value={discipline} onChange={(e) => setDiscipline(e.target.value)} placeholder="Process" /></label>
        <label>Available hours<input type="number" min="0" value={hours} onChange={(e) => setHours(e.target.value)} /></label>
        <button className="btn" disabled={busy || !discipline} onClick={() => void submit()}>Save</button>
      </div>
    </Drawer>
  )
}
