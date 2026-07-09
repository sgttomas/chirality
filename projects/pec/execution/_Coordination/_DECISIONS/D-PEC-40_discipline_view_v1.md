# D-PEC-40 - PROPOSAL: Discipline view v1

**Status:** RULED 2026-07-09 (O-A).
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-40
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche packet
precedent: verified current state, decision to rule, exact fence, options,
verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded read-only reporting surface under the adopted
> reporting-product workplan. Source execution remains prohibited unless and
> until the owner rules this packet. Sources govern on any disagreement.

## Why this row exists

The owner requested a first-class discipline view: the live, drillable mirror
of the weekly discipline status report. It should give the PD a report-shaped
in-app perspective while keeping the report workflow outside the app and
keeping unsupported figures factual-or-absent.

D-PEC-40 is the second R0 packet from the reporting-product standing plan. It
does not wait for percent complete or period semantics to become perfect; it
renders the four report sections over existing data now and explicitly marks
period/% tiles absent until their source tranches land.

## Dependencies

D-PEC-40 depends on the landed D-PEC-25 drill spine and D-PEC-38 reporting
foundation. D-PEC-39 periods and future percent-complete/contract-v2 work
enrich the view but are not hard prerequisites: the view must degrade
honestly where data is absent. Source execution should start from a base that
includes the D-PEC-36 standard report conventions, or be rebased onto them
before closeout.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| The findings record names a first-class discipline view with four report sections plus a small metric band. | `_DomainEngines/proposals/pec/FINDINGS_2026-07-09_pec_product_interview.md` §5 |
| The standing plan names R0 "Discipline view v1" as specifiable now; periods/% enrich it but are soft dependencies. | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` |
| Existing deliverable data already carries discipline and type/kind fields used by register/report surfaces. | `projects/pec/server/src/services/views.ts`; `projects/pec/web/src/pages/Registers.tsx` |
| D-PEC-36 standard reports add discipline grouping at the payload/report convention layer. | `projects/pec/server/src/reports/standard.ts`; `projects/pec/execution/_Coordination/REPORT_BASIS.md` |

## Decision to rule

Whether to authorize one source tranche implementing D-PEC-40:

1. Add a read-only discipline route/page that lists disciplines and supports a
   per-discipline detail view.
2. For each discipline, render the report-shaped sections over existing data:
   - Activities: in-work deliverables grouped by deliverable type/kind, with
     links to the underlying deliverables;
   - Issuances: issued deliverables/events only where existing records support
     the claim, otherwise absent;
   - Needs: open needs-shaped actions/holds/decisions that can be tied to the
     discipline under current records, without inventing internal/client type;
   - Risks: open risks tied to the discipline where visible to the caller.
3. Add a compact metric band, factual-or-absent:
   - % complete by deliverable kind and week-over-week delta are absent until
     percent-complete and periods land;
   - issuance counts, needs aging, open risk count, and stalled flags carry
     basis pointers or are absent;
   - every number drills to contributing records where `RecordRef` supports
     the target.
4. Preserve the "reports live outside the app" boundary: this is an in-app
   drill-down/dashboard surface, not a report editor or issuance workflow.
5. Add tests for server view shape, redaction/visibility, absent figures,
   route rendering, keyboard/drill behavior, and no mutation.

**Not in scope:** creating or editing reports; `.docx` generation; percent
complete ingestion; period/snapshot model; revised MDL/RAIL contract v2;
needs internal/client typing; interfaces import contract; MDL-to-RAIL
consistency checks; drag/drop or task-management boards; professional/go-live
or issuance claims.

## Fence (exact; STOP outside it)

O-A may touch only:

- `projects/pec/server/src/services/views.ts`
- `projects/pec/server/src/api.ts`
- `projects/pec/server/test/**`
- `projects/pec/web/src/**`
- `projects/pec/execution/_Coordination/REPORT_BASIS.md`

No `core/**` unless the ruled implementation proves an existing read-only type
export is strictly necessary. No database schema/files, no tracked DB files,
no sidecar report-authoring changes, no root manifests, no dependencies, no
profile edits, and no mutation endpoints.

## Options

- **O-A (recommended):** read-only discipline view v1, server projection, web
  route/page, factual-or-absent metric band, drill links.
- **O-B:** O-A plus export-what-is-displayed CSV for the discipline view.
  This must remain display export only, not report issuance.
- **O-C:** server projection only; no web route yet.
- **O-D:** defer D-PEC-40.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Server tests for view shape, redaction/visibility, discipline grouping,
  absent figures, and contributing refs.
- Web tests/manual browser pass for desktop and narrow viewports: route loads,
  no blank pages/body overflow/overlap, keyboard reachable drill links, and
  no console errors.
- Scope containment: `git diff --name-only` is a subset of the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review: no unsupported %/period/client-needs figures, no
  report-editor/issuance workflow, no ADR-011 model reopening.

## Rollback

Single revert of the source tranche commit(s). No schema, data, dependency, or
runtime rollback is needed under O-A/O-B/O-C.

## Human ruling

**RULED: O-A** (owner in-session 2026-07-09, Ryan Tufts, verbatim): "I rule
O-A on both D-PEC-39 and D-PEC-40 but I'm not ready to provide those needed
MDL/RAIL templates." — Source execution authorized inside this packet's O-A
fence only: read-only discipline view v1, server projection, web route/page,
factual-or-absent metric band, drill links. O-B display CSV export not
authorized. % complete and period-scoped tiles degrade honestly until their
tranches land; the withheld Tier-P templates gate none of this packet.
