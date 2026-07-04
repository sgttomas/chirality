/**
 * Plan — "What is committed, and can we do it?" (Planner home).
 * P1 placeholder: the Plan module (Now/Next/Later, six-week lookahead, capacity with
 * check/approval load) is Phase 2 scope (PRD §12.4, §21). P1 states the source rules
 * that drive My Week meanwhile (PEC-MW-007).
 */

import { api, p } from '../api.ts'
import { useApp, useLoad } from '../shared.tsx'

export function PlanPage(): JSX.Element {
  const { pid } = useApp()
  const { data } = useLoad(() => api.get(p(pid, 'plan')), [pid])
  return (
    <div>
      <h1>Plan — what is committed, and can we do it?</h1>
      <div className="card">
        <p><b>The Plan module arrives in Phase 2</b> (PRD §12.4): Now / Next / Later horizons,
        the six-week lookahead, capacity by discipline with check and approval hours loading
        capacity like any other work (I-9), plan-shift reasons, and lead review.</p>
        <p className="section-note">{data?.note ?? ''}</p>
        <p>Until then, <b>My Week</b> is driven by need-by dates plus the manual
        “commit to this week” flag on work items (PEC-MW-007), and the weekly commitments
        register exports from <span className="mono">export/commitments.csv</span>.</p>
      </div>
    </div>
  )
}
