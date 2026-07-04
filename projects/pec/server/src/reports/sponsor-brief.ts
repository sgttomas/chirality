/**
 * Sponsor brief (PRD §15, PEC-OV-006): Overview snapshot as print-friendly HTML.
 * P1 satisfies the PDF format via browser print-to-PDF (ADR-010).
 */

import { ageWorkingDays, projectStatus, waitingOnYou } from '@pec/core'
import type { Sx } from '../services/shared.ts'

function esc(s: unknown): string {
  return String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]!))
}

const COLOR: Record<string, string> = { green: '#1a7f37', amber: '#b58105', red: '#c92a2a' }

export function sponsorBrief(sx: Sx): string {
  const snap = sx.repo.snapshot(sx.projectId)
  const st = projectStatus(snap)
  const cal = snap.project.calendar
  const waiting = waitingOnYou(snap, sx.session.personId)
  const holds = snap.holds.filter((h) => h.state === 'active')
    .map((h) => ({ ...h, ageWd: ageWorkingDays(h.raisedAt, snap.today, cal) }))
    .sort((a, b) => b.ageWd - a.ageWd).slice(0, 8)
  const risks = snap.risks.filter((r) => r.state !== 'closed')
    .sort((a, b) => ((b.probability ?? 0) * (b.impact ?? 0)) - ((a.probability ?? 0) * (a.impact ?? 0)))
    .slice(0, 8)

  const badge = (h: string): string =>
    `<span style="color:${COLOR[h] ?? '#333'};font-weight:700;text-transform:uppercase">${esc(h)}</span>`

  return `<!doctype html><html><head><meta charset="utf-8">
<title>Sponsor brief — ${esc(snap.project.name)}</title>
<style>
  body{font:14px/1.5 -apple-system,Segoe UI,Helvetica,Arial,sans-serif;color:#1b1f24;margin:2rem auto;max-width:60rem;padding:0 1rem}
  h1{font-size:1.4rem;border-bottom:2px solid #1b1f24;padding-bottom:.4rem}
  h2{font-size:1.05rem;margin-top:1.6rem}
  table{border-collapse:collapse;width:100%;margin:.5rem 0}
  th,td{border:1px solid #d0d7de;padding:.35rem .6rem;text-align:left;font-size:.85rem}
  th{background:#f6f8fa}
  .kpi{display:inline-block;border:1px solid #d0d7de;border-radius:6px;padding:.6rem 1rem;margin:.25rem;text-align:center}
  .kpi b{display:block;font-size:1.3rem}
  .muted{color:#57606a;font-size:.8rem}
  @media print { body{margin:0} .kpi{break-inside:avoid} }
</style></head><body>
<h1>${esc(snap.project.code)} — Sponsor Brief <span class="muted">(${esc(snap.today)})</span></h1>
<p>Project health: ${badge(st.health.value)} <span class="muted">— ${esc(st.health.detail)}</span></p>
<div>
  <span class="kpi"><b>${st.kpis.pctOnPlan.value}%</b>deliverables on plan</span>
  <span class="kpi"><b>${Object.values(st.kpis.holdsByCause.value).reduce((a, b) => a + b, 0)}</b>active holds</span>
  <span class="kpi"><b>${st.kpis.openDecisions.value}</b>open decisions</span>
  <span class="kpi"><b>${st.kpis.approvalsInFlight.value}</b>approvals in flight</span>
  <span class="kpi"><b>${st.kpis.scheduleForecastWd.value} wd</b>worst forecast slip</span>
</div>

<h2>Package rollup</h2>
<table><tr><th>Package</th><th>Health</th><th>On plan</th><th>Rule</th></tr>
${st.packageStatuses.map((p) => `<tr><td>${esc(p.pkg.code)} — ${esc(p.pkg.name)}</td><td>${badge(p.health.value)}</td><td>${p.onPlanCount}/${p.totalCount}</td><td class="muted">${esc(p.health.ruleId)}: ${esc(p.health.detail)}</td></tr>`).join('')}
</table>

<h2>Waiting on decisions / approvals</h2>
<table><tr><th>Ref</th><th>Kind</th><th>Title</th><th>Need by</th><th>Age (wd)</th><th>Breach</th></tr>
${waiting.map((w) => `<tr><td>${esc(w.ref)}</td><td>${esc(w.kind)}</td><td>${esc(w.title)}</td><td>${esc(w.needBy ?? '—')}</td><td>${w.ageWd}</td><td>${esc(w.breach)}</td></tr>`).join('')
    || '<tr><td colspan="6" class="muted">none</td></tr>'}
</table>

<h2>Top holds</h2>
<table><tr><th>Ref</th><th>Cause</th><th>Title</th><th>Owner needs by</th><th>Age (wd)</th></tr>
${holds.map((h) => `<tr><td>${esc(h.ref)}</td><td>${esc(h.cause)}</td><td>${esc(h.title)}</td><td>${esc(h.needBy ?? '—')}</td><td>${h.ageWd}</td></tr>`).join('')
    || '<tr><td colspan="5" class="muted">none</td></tr>'}
</table>

<h2>Top risks</h2>
<table><tr><th>Ref</th><th>Title</th><th>P×I</th><th>Mitigation</th></tr>
${risks.map((r) => `<tr><td>${esc(r.ref)}</td><td>${esc(r.title)}</td><td>${(r.probability ?? 0)}×${(r.impact ?? 0)}</td><td class="muted">${esc(r.mitigation ?? '—')}</td></tr>`).join('')
    || '<tr><td colspan="4" class="muted">none</td></tr>'}
</table>

<h2>Governance signals</h2>
<table><tr><th>Signal</th><th>Level</th><th>Detail</th><th>Threshold</th></tr>
${st.signals.map((s) => `<tr><td>${esc(s.label)}</td><td>${esc(s.level)}</td><td>${esc(s.detail)}</td><td class="muted">${esc(s.threshold)}</td></tr>`).join('')}
</table>
<p class="muted">Derived per PRD §8; every value drills down to contributing records in the application (I-4). Print this page to PDF for distribution (ADR-010).</p>
</body></html>`
}
