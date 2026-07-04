/**
 * Raise-an-item dialog — available on every screen, ≤ 8 fields (PEC-AHL-003).
 * Quick types = daily-habit Needs + Risks of Change + action, hold, interface.
 * The concern lands as an intake item, preserved verbatim (OM-3); the coordinator
 * routes it at triage — the raiser needs no routing knowledge.
 */

import { useState } from 'react'
import { api, p } from './api.ts'
import { Drawer, ErrorBox, useApp } from './shared.tsx'

const QUICK_TYPES = [
  ['need_information', 'Need: information'],
  ['need_decision', 'Need: decision'],
  ['need_approval', 'Need: approval'],
  ['need_resource', 'Need: resource'],
  ['risk_budget', 'Risk of change: budget'],
  ['risk_scope', 'Risk of change: scope'],
  ['risk_schedule', 'Risk of change: schedule'],
  ['action', 'Action'],
  ['hold', 'Hold'],
  ['interface', 'Interface'],
] as const

export function RaiseItemButton(): JSX.Element {
  const [open, setOpen] = useState(false)
  return (
    <>
      <button className="btn" onClick={() => setOpen(true)}>+ Raise an item</button>
      {open && <RaiseItemDialog onClose={() => setOpen(false)} />}
    </>
  )
}

function RaiseItemDialog({ onClose }: { onClose(): void }): JSX.Element {
  const { pid, people, refresh, toast } = useApp()
  const [statement, setStatement] = useState('')
  const [quickType, setQuickType] = useState('action')
  const [anchorSuggestion, setAnchorSuggestion] = useState('')
  const [needBy, setNeedBy] = useState('')
  const [suggestedOwnerId, setSuggestedOwnerId] = useState('')
  const [log, setLog] = useState('internal')
  const [error, setError] = useState<any>(null)
  const [busy, setBusy] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setBusy(true)
    setError(null)
    try {
      const r = await api.post(p(pid, 'intake'), {
        statement, quickType,
        anchorSuggestion: anchorSuggestion || undefined,
        needBy: needBy || undefined,
        suggestedOwnerId: suggestedOwnerId ? Number(suggestedOwnerId) : undefined,
        log,
      })
      toast(`${r.ref} raised — the coordinator will triage it`)
      refresh()
      onClose()
    } catch (err) {
      setError(err)
    } finally {
      setBusy(false)
    }
  }

  return (
    <Drawer title="Raise an item" onClose={onClose}>
      <p className="section-note">
        Say it in your own words — it is preserved verbatim and routed at triage. You do not need
        to know where it goes.
      </p>
      <form className="stack" onSubmit={submit}>
        <label>Type
          <select value={quickType} onChange={(e) => setQuickType(e.target.value)}>
            {QUICK_TYPES.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
          </select>
        </label>
        <label>What is the concern? *
          <textarea required value={statement} onChange={(e) => setStatement(e.target.value)}
            placeholder="e.g. Vendor pump curves for P-101A/B still missing; datasheet cannot be finalized" />
        </label>
        <label>Where does it belong? (suggestion — doc number, package, or free text)
          <input value={anchorSuggestion} onChange={(e) => setAnchorSuggestion(e.target.value)} placeholder="e.g. TST-ME-001 or PKG-M" />
        </label>
        <div className="row">
          <label>Needed by
            <input type="date" value={needBy} onChange={(e) => setNeedBy(e.target.value)} />
          </label>
          <label>Suggested owner
            <select value={suggestedOwnerId} onChange={(e) => setSuggestedOwnerId(e.target.value)}>
              <option value="">—</option>
              {people.map((pp) => <option key={pp.id} value={pp.id}>{pp.name}</option>)}
            </select>
          </label>
        </div>
        <label>Log
          <select value={log} onChange={(e) => setLog(e.target.value)}>
            <option value="internal">Internal</option>
            <option value="package">Package</option>
            <option value="client">Client / Project</option>
          </select>
        </label>
        <ErrorBox error={error} />
        <div className="row">
          <button className="btn" disabled={busy || !statement}>Raise</button>
          <button type="button" className="btn secondary" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </Drawer>
  )
}
