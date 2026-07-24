# D-PEC-49 - RULED (closed as moot): Week-over-week deliverable progress

**Status:** RULED 2026-07-24 — closed as moot by D-PEC-58 (no option selected); see Closure section
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-49
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04).

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> Prepared at owner direction after the D-PEC-43/44/46/47/48 ruling slate.
> Source execution remains prohibited unless and until the owner rules this
> packet.

## Why this row exists

The owner clarified the reporting scope on 2026-07-09: PEC should account for
progress well over week in deliverables, compute progress from imported MDL
percent complete and reported dates, and defer resource loading over planned
duration. The app remains a reporting/drill-down tool: no manual in-app
progress edits and no task-management behavior.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| D-PEC-39 stores per-document coverage declarations on import proposals and period-scoped read/report basis. | `projects/pec/server/src/services/periods.ts`; `projects/pec/execution/_Coordination/REPORT_BASIS.md` |
| D-PEC-41 stores PE-attested MDL v2 `percent_complete` as import data, never derived or in-app editable. | `projects/pec/server/src/import/index.ts`; `projects/pec/server/src/db.ts` |
| D-PEC-40/45 display discipline and deliverable percent facts, but week-over-week percent delta remains absent because no period snapshot/progress history model is ruled. | `projects/pec/server/src/services/views.ts`; `projects/pec/execution/_Coordination/REPORT_BASIS.md` |
| The standing plan says stalled flags and week-over-week percent deltas need a future period snapshot model. | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` |

## Decision to rule

Whether to authorize one reporting-only source tranche:

1. **Progress history basis:** when an MDL import proposal with declared
   coverage is applied, record the imported deliverable percent values for
   that reporting window as immutable progress observations. Observations are
   derived from imported MDL facts plus declared coverage/reporting dates, not
   user edits.
2. **Week-over-week delta:** compute deliverable and discipline deltas by
   comparing observations across adjacent declared reporting windows. If the
   prior window or current imported value is absent, the delta is absent and
   says why.
3. **Report/view surfacing:** standard reports and discipline/deliverable
   drill-down may show percent change and "no movement" facts only when both
   compared observations exist and name their import proposal/coverage basis.
4. **No manual progress editing:** no web/API route may hand-set progress or
   alter observations outside the import-proposal apply path.
5. **Resource loading deferred:** planned-duration/resource-loaded progress
   calculation is explicitly future work and not modeled here.
6. **Tests:** observation creation on apply, idempotent re-apply/update
   behavior, absent-honest deltas, changed-percent deltas, marker-valued
   percent exclusion, and report/view basis naming.

**Not in scope:** resource loading; planned-duration weighting; manual
progress edits; task management; schedule forecasting; workflow state edits;
issuing reports; `.docx` generation.

## Fence (exact; STOP outside it)

O-A may touch only:

- `projects/pec/server/src/**` (observation storage/read-side/reporting)
- `projects/pec/core/src/**` (additive types if needed)
- `projects/pec/server/test/**`
- `projects/pec/web/src/pages/Disciplines.tsx`
- `projects/pec/web/src/pages/Deliverables.tsx`
- `projects/pec/execution/_Coordination/REPORT_BASIS.md`
- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/**`

No manual mutation route, no tracked DB files, no new dependency, no resource
loading model, no task-management surface.

## Options

- **O-A (recommended):** implement import-derived progress observations and
  period-to-period deltas as above.
- **O-B:** reports-only delta computation from current and immediately prior
  import proposal metadata, no stored observation table. Lower schema cost but
  weaker auditability.
- **O-C:** documentation-only convention; no source change.
- **O-D:** defer.

## Verification plan (workplan step-4 bar)

PEC belt-and-braces; tests listed above; visual pass on Disciplines and
Deliverables if `web/**` is touched; scope containment subset of the ruled
fence; self-check / coord-check / `git diff --check`; adversarial review that
no manual progress edit path exists and every delta names its import/coverage
basis.

## Rollback

Single revert of the tranche commit(s). Additive observation storage rolls
back by ordinary revert; imported MDL source facts remain unchanged.

## Human ruling

**OPEN - decision is the owner's (K-AUTH-1).** Rule O-A / O-B / O-C / O-D.


## Closure (2026-07-24)

Closed as moot by `D-PEC-58`: week-over-week deliverable progress derived from
MDL percent-complete imports belongs to the retired reporting product
(PRD v0.4/v1.0 lineage), superseded by the coordination-plane product
definition (PRD v2.0). No option (O-A..O-D) was selected. Revival against
coordination-plane (v2) entities requires a new register row
(residual-work convention).
