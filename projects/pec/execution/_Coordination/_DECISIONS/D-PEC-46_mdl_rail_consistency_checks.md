# D-PEC-46 - PROPOSAL: MDL-RAIL consistency checks

**Status:** AWAITING_RULING
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-46
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-39/41/43 precedent.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes the R2 "MDL-RAIL consistency checks" row of the reporting-product
> standing plan. Source execution remains prohibited unless and until the owner
> rules this packet.

## Why this row exists

The product-direction findings record the owner's consistency rule: MDL
`on hold` status and RAIL hold-shaped issues must agree; discrepancies should
flag agent/PE review and be resolved by the intake/triage machinery. D-PEC-41
landed the contract-v2 facts and already emits per-row caught signals when an
MDL row says `working_status = On Hold` or a RAIL row says `STATUS = On Hold`.
What is still absent is a cross-record checker that compares the two sources,
creates a durable review surface, and gives the PE/agent a disposition trail.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| The standing plan's R2 row calls for MDL-RAIL consistency checks after contract v2: intake/triage catches MDL-status vs RAIL-issue disagreements, caught items carry a disposition trail, and agent response is configurable. | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` (R2 row; Open owner decision 5) |
| Findings define the on-hold consistency rule and classify agent response as automatic or human-prompted, configurable. | `_DomainEngines/proposals/pec/FINDINGS_2026-07-09_pec_product_interview.md` §§2, 4.3, 7 |
| MDL v2 imports store `working_status` and emit `mdl-on-hold` review signals; RAIL v2 imports store source issue facts and emit `rail-on-hold` review signals. These are row-local signals only. | `projects/pec/server/src/import/index.ts` |
| Work items already retain RAIL v2 `responsibleParty`, `sourceIssueType`, and verbatim `sourcePayload`; deliverables retain MDL v2 `workingStatus`. | `projects/pec/core/src/types.ts`; `projects/pec/server/src/db.ts` |
| Intake has a state/disposition trail and agent-readable triage path, while conversion remains a human act. | `projects/pec/core/src/types.ts`; `projects/pec/agent-sidecar/src/acts.ts` |

## Decision to rule

Whether to authorize one source tranche implementing cross-record consistency
checks:

1. **Checker:** compare applied MDL v2 deliverables whose `working_status`
   normalizes to `on hold` against applied RAIL v2 hold-shaped issue rows for
   the same package / deliverable basis where the source provides one. Compare
   the inverse as well: RAIL `on hold` issues with no corresponding MDL
   `on hold` basis.
2. **Caught review items:** discrepancies become deterministic, idempotent
   intake/review items only after the human-approved import proposal is
   applied. They carry source refs, the two source facts, and a rule id
   (`CONSIST-MDL-RAIL-HOLD`). They are never silently resolved and never block
   import.
3. **Disposition trail:** the review items use the existing intake states and
   dispositions. Conversion to project records remains a human act; the agent
   may summarize, open triage, or disposition only within its already ruled
   D-PEC-10/17 boundaries.
4. **Configurable agent response:** default policy is `prompt_human`. Any
   automatic response is limited to raising/summarizing caught matters; no
   automatic accept/apply, conversion, force, or record-state mutation. The
   policy home is named in the implementation (project config or sidecar
   config, as selected by the ruling) and is visible to the PE.
5. **Read/report surfacing:** standard reports and discipline/package views
   may count unresolved consistency items only where they drill to the intake
   item and name the rule id. Unsupported joins stay absent rather than
   guessed.
6. **Tests:** matching, inverse mismatch, idempotent re-import, package-only
   ambiguity, no-import-blocking behavior, disposition persistence, and
   agent-policy boundary pins.

**Not in scope:** direct correction of MDL or RAIL facts; automatic conversion
of intake items; editable computed status; `force=true`; new dependencies;
interfaces consistency; week-over-week status deltas.

## Fence (exact; STOP outside it)

O-A may touch only:

- `projects/pec/server/src/**` (consistency checker, intake creation/update,
  read/report surfacing)
- `projects/pec/core/src/**` (additive types/rule id if needed)
- `projects/pec/server/test/**`
- `projects/pec/agent-sidecar/**` (policy disclosure / bounded response only)
- `projects/pec/execution/_Coordination/REPORT_BASIS.md`
- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/**`

No `web/**` unless a separate ruling names a display surface; no tracked DB
files; no new runtime dependency; no direct-apply path.

## Options

- **O-A (recommended):** implement the full checker + intake/disposition
  trail + prompt-first agent policy described above.
- **O-B:** checker-only in import reports, no durable intake items. Lower
  risk, but it does not satisfy the owner's disposition-trail requirement.
- **O-C:** spec-only documentation of the consistency rule.
- **O-D:** defer.

## Verification plan (workplan step-4 bar)

PEC belt-and-braces; source tests listed above; scope containment subset of
the ruled fence; self-check / coord-check / `git diff --check`; adversarial
review that no unsupported join is guessed, imports are not blocked by caught
conditions, and the agent cannot perform reserved human acts.

## Rollback

Single revert of the tranche commit(s). Any additive schema/data migration is
ordinary rollback; caught review items are import-owned records and remain
auditable if created before rollback.

## Human ruling

**OPEN - decision is the owner's (K-AUTH-1).** Rule O-A / O-B / O-C / O-D.
