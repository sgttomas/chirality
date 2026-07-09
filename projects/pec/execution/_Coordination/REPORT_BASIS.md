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

## Coverage declarations & period basis (D-PEC-39)

Coverage is DECLARED by the PE per uploaded document on the import-proposal
lane (`coverage_start`/`coverage_end` on `POST .../import-proposals`;
`server/src/services/proposals.ts`) and never inferred. Read side in
`server/src/services/periods.ts`:

| Figure | Rule id | Basis |
|---|---|---|
| coverage review signals | `COV-OVERLAP` / `COV-GAP` / `COV-UNDECLARED` (`GET /api/projects/:pid/coverage`) | applied import proposals' declared windows, per contract; caught for PE/agent review, never schema-prevented |
| period coverage basis | `PER-COV` (`GET /api/projects/:pid/period-status?start&end`) | applied coverage declarations intersecting the explicitly requested window; an uncovered window says so |
| issuances in period | `PER-ISSUED` | `issue_event.issued_at` within the window |
| issuance delta | `PER-ISSUED-DELTA` | issuances in the window minus the preceding equal-length window — timestamped records, not a snapshot model |
| work closed / holds raised / holds resolved / decisions decided / intake raised in period | `PER-CLOSED` / `PER-HOLD-RAISED` / `PER-HOLD-RESOLVED` / `PER-DECIDED` / `PER-INTAKE` | record timestamps within the window, visibility-filtered per log |

The weekly standard report accepts `period_start`/`period_end` (both or
neither; other standard reports refuse a period rather than ignore it);
under a declared period it carries `issuancesThisPeriod`, `issuanceDelta`,
and the `PER-COV` coverage basis, and its absent list keeps percent complete
(Tier-P contract v2) and non-issuance deltas absent. Periods are request
parameters or per-document declarations — never silently inferred. Window
membership convention: the UTC calendar day of the stored timestamp
(`ts.slice(0,10)`) is compared to the declared dates, matching the repo-wide
date convention.

## Discipline view v1 (D-PEC-40)

Routes `GET /api/projects/:pid/disciplines` and `GET .../disciplines/:name`
(`server/src/services/views.ts`, discipline section; web page
`web/src/pages/Disciplines.tsx`). Read-only mirror of the weekly discipline
report: Activities grouped by deliverable type · Issuances · Needs · Risks,
plus a factual-or-absent metric band.

| Figure | Rule id | Basis |
|---|---|---|
| activities in work | `DISC-ACT` | discipline deliverables whose workflow has not reached issued |
| open needs / needs aging | `DISC-NEEDS` / `DISC-NEEDS-AGE` | open work items + active holds anchored to discipline deliverables/revisions, visibility-filtered per log; internal-vs-client typing absent until its ruled tranche |
| open risks | `DISC-RISK` | open risks with a deliverable in the discipline — package-only risks carry no discipline basis and are not counted |
| issued this period / issuance delta | `DISC-ISSUED` / `DISC-ISSUED-DELTA` | issue events on discipline revisions within an explicitly requested window; detail names the `PER-COV` coverage basis; absent when no period is declared |
| % complete | `DISC-PCT` | PE-attested percent (contract v2 import, D-PEC-41; never derived or edited in-app): equal-weight mean over deliverable types with ≥1 attested document, each type the mean of its attested documents; detail names attested coverage (n/m) and excludes verbatim markers (e.g. "Next Phase"); absent when nothing is attested |

Absent by construction: week-over-week % delta and stalled-activity flags
(both need a period snapshot model, not ruled). No CSV export on this surface
(D-PEC-40 O-B not authorized); no mutation machinery ever ("dashboards, not
task managers").

## Contract v2 attested facts & caught signals (D-PEC-41)

Contract v2 imports (revised TWD templates; mapping of record in
`IMPORT_TEMPLATES/IMPORT_MAPPING.md` §contract-v2) carry PE-attested facts:
`percent_complete` (with verbatim non-numeric markers), `working_status`,
`target_completeness`, `project_phase`, RAIL `responsible_party` and verbatim
`issue_type`. Attested facts are import-only: never in-app editable, never
derived in-app (workplan reconciliation 1). Unmapped columns are captured
verbatim per the owner's fidelity direction (Receipt 75). Import dry-run/apply
reports carry caught review signals (`mdl-on-hold`, `rail-on-hold`,
`phase-cancelled`, `percent-marker`, vocabulary deviations) — surfaced for
PE/agent review, never silently coerced, never schema-blocked. Round-trip
registers: `mdl-v2`, `rail-v2` (export-what-was-provided parity).

## The rule this page reinforces

An answer about project state — the owner's, a report's, or the agent's —
names its basis by pointer (rule id, register, or Explain payload). A figure
computed on any other basis is labeled with that basis explicitly and is not
presented as the app's number.
