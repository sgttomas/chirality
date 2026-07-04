/**
 * Weekly package review pack (PEC-PKG-009, PRD §15 P2): the package review meeting's
 * one-page print-friendly HTML — health, issues cockpit, needs-the-lead, deliverable
 * workflow, capacity/discipline load (PEC-PKG-003), package lookahead slice
 * (PEC-PLAN-002), interfaces with aging (PEC-PKG-008), and recent plan shifts
 * (PEC-PLAN-006). PDF via browser print (ADR-010).
 */

import {
  ageWorkingDays, capacityView, daysOverdue, isoWeekOf, isoWeeksFrom, lookahead,
  packageStatus, resolvePlanItem, workflowCompleteness, workingDaysOverdue,
} from '@pec/core'
import { notFound } from '../errors.ts'
import type { Sx } from '../services/shared.ts'

function esc(s: unknown): string {
  return String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]!))
}

const COLOR: Record<string, string> = { green: '#1a7f37', amber: '#b58105', red: '#c92a2a', warn: '#b58105', none: '#57606a' }

export function packagePack(sx: Sx, packageId: number): string {
  const snap = sx.repo.snapshot(sx.projectId)
  const pkg = snap.packages.find((p) => p.id === packageId)
  if (!pkg) throw notFound(`package #${packageId}`)
  const st = packageStatus(snap, pkg)
  const cal = snap.project.calendar
  const today = snap.today
  const week = isoWeekOf(today)
  const weeks = isoWeeksFrom(today, 6)
  const th = snap.project.thresholds

  const badge = (h: string): string =>
    `<span style="color:${COLOR[h] ?? '#333'};font-weight:700;text-transform:uppercase">${esc(h)}</span>`

  const dels = snap.deliverables.filter((d) => d.packageId === pkg.id)
  const delIds = new Set(dels.map((d) => d.id))
  const revIds = new Set(snap.revisions.filter((r) => delIds.has(r.deliverableId)).map((r) => r.id))

  const holds = snap.holds.filter((h) => h.state === 'active'
    && snap.holdLinks.some((l) => l.holdId === h.id && (
      (l.targetType === 'deliverable' && delIds.has(l.targetId))
      || (l.targetType === 'revision' && revIds.has(l.targetId))
      || (l.targetType === 'work_item' && snap.workItems.some((w) => w.id === l.targetId && w.packageId === pkg.id))
    )))
    .map((h) => ({ ...h, ageWd: ageWorkingDays(h.raisedAt, today, cal) }))
    .sort((a, b) => b.ageWd - a.ageWd)

  const decisions = snap.decisions.filter((d) => d.packageId === pkg.id
    && d.state !== 'decided' && d.state !== 'superseded')
    .map((d) => ({ ...d, overdue: daysOverdue(d.needBy, today) }))
    .sort((a, b) => b.overdue - a.overdue)

  const interfaces = snap.interfaces.filter((i) =>
    (i.givingPackageId === pkg.id || i.receivingPackageId === pkg.id)
    && i.state !== 'closed' && i.state !== 'cancelled')
    .map((i) => ({ ...i, overdueWd: workingDaysOverdue(i.needBy, today, cal) }))
    .sort((a, b) => b.overdueWd - a.overdueWd)

  const risks = snap.risks.filter((r) =>
    (r.packageId === pkg.id || (r.deliverableId != null && delIds.has(r.deliverableId))) && r.state !== 'closed')
    .sort((a, b) => ((b.probability ?? 0) * (b.impact ?? 0)) - ((a.probability ?? 0) * (a.impact ?? 0)))

  const openItems = snap.workItems.filter((w) =>
    (w.state === 'open' || w.state === 'in_work') && w.packageId === pkg.id
    && daysOverdue(w.needBy, today) > 0)
    .sort((a, b) => (a.needBy ?? '9999').localeCompare(b.needBy ?? '9999'))

  // capacity: this package's current-week load per discipline (PEC-PKG-003)
  const capRows = capacityView(snap, [week]).map((cell) => {
    const pkgHours = cell.planItemIds.reduce((sum, piId) => {
      const pi = snap.planItems.find((x) => x.id === piId)
      if (!pi) return sum
      return resolvePlanItem(snap, pi)?.packageId === pkg.id ? sum + pi.plannedHours : sum
    }, 0)
    return { ...cell, pkgHours }
  }).filter((r) => r.pkgHours > 0 || r.level !== 'none')

  const la = lookahead(snap, weeks).filter((r) => r.deliverable.packageId === pkg.id)

  const shifts = snap.planShifts
    .filter((s) => {
      if (s.affectedPackageIds.includes(pkg.id)) return true
      const pi = snap.planItems.find((x) => x.id === s.planItemId)
      return pi != null && resolvePlanItem(snap, pi)?.packageId === pkg.id
    })
    .sort((a, b) => b.id - a.id)
    .slice(0, 10)

  const cell = (c: { state: string; detail: string } | null): string =>
    c ? `<td style="color:${c.state === 'hold' ? COLOR.red : c.state === 'issue' ? COLOR.green : '#1b1f24'}">${esc(c.state)}<div class="muted">${esc(c.detail)}</div></td>` : '<td></td>'

  return `<!doctype html><html><head><meta charset="utf-8">
<title>Package review pack — ${esc(pkg.code)}</title>
<style>
  body{font:14px/1.5 -apple-system,Segoe UI,Helvetica,Arial,sans-serif;color:#1b1f24;margin:2rem auto;max-width:64rem;padding:0 1rem}
  h1{font-size:1.4rem;border-bottom:2px solid #1b1f24;padding-bottom:.4rem}
  h2{font-size:1.05rem;margin-top:1.6rem}
  table{border-collapse:collapse;width:100%;margin:.5rem 0}
  th,td{border:1px solid #d0d7de;padding:.35rem .6rem;text-align:left;font-size:.85rem;vertical-align:top}
  th{background:#f6f8fa}
  .muted{color:#57606a;font-size:.8rem}
  @media print { body{margin:0} h2{break-after:avoid} }
</style></head><body>
<h1>${esc(pkg.code)} — Weekly package review pack <span class="muted">(${esc(today)}, ${esc(week)})</span></h1>
<p>Package health: ${badge(st.health.value)} <span class="muted">— ${esc(st.health.ruleId)}: ${esc(st.health.detail)}</span><br>
Lead: person #${esc(pkg.leadId ?? '—')} · deliverables on plan ${st.onPlanCount}/${st.totalCount}</p>

<h2>Open holds (${holds.length})</h2>
<table><tr><th>Ref</th><th>Cause</th><th>Title</th><th>Owner needs by</th><th>Age (wd)</th></tr>
${holds.map((h) => `<tr><td>${esc(h.ref)}</td><td>${esc(h.cause)}</td><td>${esc(h.title)}</td><td>${esc(h.needBy ?? '—')}</td><td>${h.ageWd}</td></tr>`).join('')
    || '<tr><td colspan="5" class="muted">none</td></tr>'}
</table>

<h2>Open decisions (${decisions.length})</h2>
<table><tr><th>Ref</th><th>Title</th><th>State</th><th>Need by</th><th>Overdue (d)</th></tr>
${decisions.map((d) => `<tr><td>${esc(d.ref)}</td><td>${esc(d.title)}</td><td>${esc(d.state)}</td><td>${esc(d.needBy ?? '—')}</td><td>${d.overdue || ''}</td></tr>`).join('')
    || '<tr><td colspan="5" class="muted">none</td></tr>'}
</table>

<h2>Interfaces with aging (PEC-PKG-008)</h2>
<table><tr><th>Ref</th><th>Title</th><th>Giving → receiving</th><th>Need by</th><th>State</th><th>Overdue (wd)</th></tr>
${interfaces.map((i) => `<tr><td>${esc(i.ref)}</td><td>${esc(i.title)}</td><td>${esc(i.givingParty)} → ${esc(i.receivingParty)}</td><td>${esc(i.needBy ?? '—')}</td><td>${esc(i.state)}</td><td>${i.overdueWd > th.interfaceOverdueRedWd ? badge('red') : i.overdueWd > 0 ? badge('warn') : ''} ${i.overdueWd || ''}</td></tr>`).join('')
    || '<tr><td colspan="6" class="muted">none</td></tr>'}
</table>

<h2>Overdue action items (${openItems.length})</h2>
<table><tr><th>Ref</th><th>Title</th><th>Owner</th><th>Need by</th></tr>
${openItems.map((w) => `<tr><td>${esc(w.ref)}</td><td>${esc(w.title)}</td><td>person #${esc(w.ownerId)}</td><td>${esc(w.needBy ?? '—')}</td></tr>`).join('')
    || '<tr><td colspan="4" class="muted">none</td></tr>'}
</table>

<h2>Risks (${risks.length})</h2>
<table><tr><th>Ref</th><th>Title</th><th>P×I</th><th>Mitigation</th></tr>
${risks.map((r) => `<tr><td>${esc(r.ref)}</td><td>${esc(r.title)}</td><td>${(r.probability ?? 0)}×${(r.impact ?? 0)}</td><td class="muted">${esc(r.mitigation ?? '—')}</td></tr>`).join('')
    || '<tr><td colspan="4" class="muted">none</td></tr>'}
</table>

<h2>Capacity — current week (PEC-PKG-003, I-9)</h2>
<table><tr><th>Discipline</th><th>Package load (h)</th><th>Discipline load (h)</th><th>Capacity (h)</th><th>%</th><th>Level</th></tr>
${capRows.map((r) => `<tr><td>${esc(r.discipline)}</td><td>${r.pkgHours}</td><td>${r.loadH}</td><td>${r.capacityH ?? '—'}</td><td>${r.pct ?? '—'}</td><td>${r.level === 'none' ? '' : badge(r.level)}</td></tr>`).join('')
    || '<tr><td colspan="6" class="muted">no planned load this week</td></tr>'}
</table>

<h2>Six-week lookahead (PEC-PLAN-002)</h2>
<table><tr><th>Deliverable</th>${weeks.map((w) => `<th>${esc(w)}</th>`).join('')}</tr>
${la.map((r) => `<tr><td>${esc(r.deliverable.docNo)}<div class="muted">${esc(r.deliverable.title)}</div></td>${r.cells.map(cell).join('')}</tr>`).join('')
    || `<tr><td colspan="${weeks.length + 1}" class="muted">no deliverables</td></tr>`}
</table>

<h2>Deliverables — workflow status</h2>
<table><tr><th>Doc no</th><th>Title</th><th>Due</th><th>Workflow</th></tr>
${dels.map((d) => {
    const wf = workflowCompleteness(snap, d)
    return `<tr><td>${esc(d.docNo)}</td><td>${esc(d.title)}</td><td>${esc(d.dueDate ?? '—')}</td><td>${esc(wf.label)} (${wf.gatesClosed}/${wf.gatesTotal} gates)</td></tr>`
  }).join('') || '<tr><td colspan="4" class="muted">none</td></tr>'}
</table>

<h2>Recent plan shifts (PEC-PLAN-006)</h2>
<table><tr><th>Ref</th><th>Move</th><th>Reason</th><th>State</th></tr>
${shifts.map((s) => `<tr><td>${esc(s.ref)}</td><td>${esc(s.fromHorizon)}${s.fromWeek ? `/${esc(s.fromWeek)}` : ''} → ${esc(s.toHorizon)}${s.toWeek ? `/${esc(s.toWeek)}` : ''}</td><td>${esc(s.reason)}</td><td>${esc(s.state)}</td></tr>`).join('')
    || '<tr><td colspan="4" class="muted">none</td></tr>'}
</table>

<p class="muted">Derived per PRD §8/§12.4; every value drills down to contributing records in the application (I-4). Print to PDF for the review meeting (ADR-010).</p>
</body></html>`
}
