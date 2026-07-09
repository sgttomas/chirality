# PEC reporting surfaces — basis reference

> **Epistemic status: reference page — owner-adopted 2026-07-07 (item B-3 of
> `_DomainEngines/proposals/pec/BRIEF_2026-07-07_workflow_simplification.md`),
> under the owner priority "reinforce only reporting on what is factual and
> has a clear basis."** Doc-only; on any disagreement the cited code governs.

Every reporting surface is server-computed from the project snapshot; the web
renders payload fields untransformed. Every KPI ships as an Explain payload
(rule id + detail + contributing records), visibility-redacted per log
(`server/src/services/views.ts`). A reported figure's basis is therefore
always inspectable: its rule id and its contributing records.

## Overview KPIs

Route `GET /api/projects/:pid/overview` (`server/src/api.ts:118`); computed
in `core/src/status.ts:543-571`, assembled at
`server/src/services/views.ts:87-95`.

| Figure | Rule id | Basis |
|---|---|---|
| deliverables on plan (%) | `KPI-ONPLAN` (`status.ts:549`) | round(green deliverables / all deliverables × 100); contributing lists every non-green deliverable with its health rule |
| active holds | `KPI-HOLDS` (`status.ts:556`) | count of holds with state `active`, grouped by cause |
| open decisions | `KPI-DEC` (`status.ts:560`) | decisions in `identified` / `in_progress` / `pending` |
| approvals in flight | `KPI-APPR` (`status.ts:564`) | approval records in `required` / `prereqs_incomplete` / `ready` |
| schedule forecast (wd) | `KPI-SCHED` (`status.ts:568`) | worst forecast slip in working days across deliverables |
| project health | `status.ts:543` | worst package, escalated on signal breach (§8.4) |

## Register CSV exports

Route `GET /api/projects/:pid/export/:register` (`api.ts:327-332`);
`exportRegister` switch at `server/src/import/index.ts:605`. Registers:
`mdl`, `rail`, `decisions`, `risks`, `approvals`, `interfaces`, `intake`,
`commitments`, `log`, `schedule`, `tracker`, `lookahead`. Each is a direct
serialization of current records — no derived figures beyond resolving ids to
codes/names.

## Reports

- **Sponsor brief** (`api.ts:333-336`; payload in
  `server/src/services/views.ts`, sponsor section): summary counts —
  `deliverablesOnPlan` as `onPlanCount/totalCount`, open issues (with overdue
  split), holds by cause, open interfaces / decisions / risks / action items —
  plus current-week capacity rows. Counts come from the same snapshot the
  registers export.
- **Package pack** (`api.ts:337-340`): package health (same rule basis as
  the overview rollup), the open-issue cockpit, and per-deliverable workflow
  status.
- **Revision explain** (`api.ts:178-181`; `explainTransition`,
  `core/src/conditions.ts:277`): the gate's conditions with the contributing
  records — the basis payload itself.
- **Standard reports** (`GET /api/projects/:pid/reports/standard/:report`;
  `server/src/reports/standard.ts`): JSON payloads plus a Markdown draft
  string for sidecar use. Names: `weekly-project-status`,
  `package-issue-summary`, `deliverable-completeness`. Weekly status supports
  `groupBy=package` and `groupBy=discipline`; all payloads carry `basis[]`
  pointers and `absent[]` entries for unsupported figures. Period-scoped
  issuances, percent complete, week-over-week deltas, client/internal needs
  typing, and `.docx` output stay absent until their ruled tranches land.
- **User-defined reports** (sidecar D-PEC-37 mode,
  `agent-sidecar/src/user-report.ts`): prompt requests are routed only to
  bounded PEC read/report acts. The sidecar may draft over the standard report
  payloads above, but it refuses professional/go-live/issuance claims, hidden
  data requests, unsupported forecasts, and mutations. Unsupported requested
  figures are reported as absent rather than synthesized.

## The rule this page reinforces

An answer about project state — the owner's, a report's, or the agent's —
names its basis by pointer (rule id, register, or Explain payload). A figure
computed on any other basis is labeled with that basis explicitly and is not
presented as the app's number.
