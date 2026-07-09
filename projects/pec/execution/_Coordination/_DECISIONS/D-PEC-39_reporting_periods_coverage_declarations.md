# D-PEC-39 - PROPOSAL: Reporting periods and coverage declarations

**Status:** RULED 2026-07-09 (O-A).
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-39
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche packet
precedent: verified current state, decision to rule, exact fence, options,
verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded model/read-side tranche under the adopted
> reporting-product workplan. Source execution remains prohibited unless and
> until the owner rules this packet. Sources govern on any disagreement.

## Why this row exists

The owner's recurring weekly/aggregate report needs period-scoped facts:
"issuances this week", week-over-week movement, newly raised risks, stalled
deliverables, and report coverage. The product interview records that the PE
declares the covered dates per uploaded document, and that overlaps, gaps, and
retroactive corrections should be caught and resolved with the PE rather than
blocked by schema rigidity.

D-PEC-39 is the first R0 packet from the reporting-product standing plan. It
creates the coverage-declaration and period-read basis that later report,
discipline, percent-complete, and `.docx` work can compose over.

## Dependencies

No owner-provided template is a hard prerequisite for this packet: period
semantics are specifiable now, and later revised templates refine import
columns rather than authorizing this model. Source execution should start from
a base that includes the D-PEC-35 upload lane and D-PEC-36/37 reporting
machinery, or be rebased onto them before closeout, because this tranche
touches the same reporting/upload story.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| The standing plan names R0 "Reporting periods & coverage declarations" as specifiable now, with no hard owner-prerequisite row. | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` |
| The findings record says dates are declared per uploaded document, and overlaps/gaps/corrections are caught for agent/PE resolution rather than schema-prevented. | `_DomainEngines/proposals/pec/FINDINGS_2026-07-09_pec_product_interview.md` §§4.1, 7 |
| Existing standard reports intentionally call period-scoped figures absent because no period/snapshot model exists yet. | `projects/pec/server/src/reports/standard.ts`; `projects/pec/execution/_Coordination/REPORT_BASIS.md` |
| The current import-proposal lane is proposal-gated; agent direct apply/force remains outside the human-act boundary. | `projects/pec/agent-sidecar/src/acts.ts`; `projects/pec/agent-sidecar/src/pec-client.ts`; `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md` |

## Decision to rule

Whether to authorize one source tranche implementing D-PEC-39:

1. Add a period/coverage model for imported source documents:
   - coverage start date and coverage end date declared per uploaded document
     or import proposal;
   - source document identity sufficient to tie period facts back to the
     proposal/import event;
   - append-only history/audit treatment consistent with existing import
     proposal and controlled-record conventions.
2. Add read-side projections that surface:
   - coverage declarations by source document/proposal;
   - overlaps, gaps, and retroactive corrections as review signals for the PE
     and agent;
   - period-scoped counts where existing records support them, with
     `Explain`-style basis and contributing refs.
3. Enrich standard-report payloads only where a factual period basis exists.
   Unsupported period figures remain absent and explicitly named as absent.
4. Keep upload proposal-gated. The agent may propose/report/ask; human
   accept/apply remains the boundary.
5. Add tests for schema migration, proposal/import coverage capture,
   overlap/gap/correction detection, report absent-to-present behavior, and
   no destructive mutation of prior period records.

**Not in scope:** revised MDL/RAIL contract v2; binary XLSX parsing; percent
complete ingestion; `.docx` generation; first-class discipline view UI;
interfaces import contract; needs internal/client typing; MDL-to-RAIL
consistency checks; automatic agent remediation policy; professional/go-live
or issuance claims.

## Fence (exact; STOP outside it)

O-A may touch only:

- `projects/pec/core/src/**`
- `projects/pec/server/src/**`
- `projects/pec/server/test/**`
- `projects/pec/agent-sidecar/**` only where required to carry coverage
  declarations through proposal-gated upload acts
- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/**`
- `projects/pec/execution/_Coordination/REPORT_BASIS.md`

No `web/**` under O-A except if the owner explicitly selects an option that
opens a read-only display surface. No tracked DB files, no root manifests, no
new dependencies, no profile edits, and no direct import/apply/force path.

## Options

- **O-A (recommended):** model + read-side period/coverage basis, proposal-lane
  declaration capture, report payload enrichment, no web UI.
- **O-B:** O-A plus a minimal read-only Admin/reporting display for coverage
  declarations and period review signals. The ruling must name the opened web
  files.
- **O-C:** coordination/spec-only period semantics; no source change.
- **O-D:** defer D-PEC-39.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Server/core tests for schema migration, capture, idempotent re-import,
  overlap/gap/correction signals, report basis pointers, and no destructive
  mutation.
- Sidecar tests if proposal payloads change.
- Browser visual pass only if O-B opens web surfaces; otherwise API/report
  tests are primary.
- Scope containment: `git diff --name-only` is a subset of the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review: every period-scoped figure names its coverage basis or
  is absent; overlaps/gaps are caught, not silently coerced or blocked; no
  owner-template columns are guessed.

## Rollback

Single revert of the source tranche commit(s), plus ordinary schema migration
rollback only if the ruled implementation adds one. Scratch verification data
must stay scratch-only and uncommitted.

## Human ruling

**RULED: O-A** (owner in-session 2026-07-09, Ryan Tufts, verbatim): "I rule
O-A on both D-PEC-39 and D-PEC-40 but I'm not ready to provide those needed
MDL/RAIL templates." — Source execution authorized inside this packet's O-A
fence only (no web surface). The Tier-P revised MDL/RAIL templates remain
withheld: contract v2 and all template-dependent rows stay parked; nothing in
this tranche may guess template columns (K-INVENT-1).
