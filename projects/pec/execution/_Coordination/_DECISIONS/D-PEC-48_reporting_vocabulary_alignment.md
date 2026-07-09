# D-PEC-48 - PROPOSAL: Reporting-vocabulary alignment

**Status:** RULED 2026-07-09 (O-A)
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-48
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-39/43/46 precedent.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes the R3 "Reporting-vocabulary alignment" row of the
> reporting-product standing plan. Source execution remains prohibited unless
> and until the owner rules this packet.

## Why this row exists

The product-direction findings record that the owner's client-facing
reporting vocabulary uses "issues" narrowly: action items and risks by
package, with status and percent complete. The existing app and ADR-011
cockpit use a broader five-type package union: holds, interfaces, decisions,
risks, and actions. The standing plan explicitly reconciles this as a
**display/reporting-vocabulary decision**, not a model change and not a
reopening of ADR-011.

D-PEC-40 and D-PEC-45 landed the discipline view and percent-complete display;
D-PEC-41 landed contract-v2 vocabulary. The prerequisites for a display-only
vocabulary alignment packet are therefore present. D-PEC-46/47 may later
enrich consistency and Needs wording, but they are not hard prerequisites for
renaming and grouping the already displayed facts honestly.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| Findings §4.5 says the owner tracks "issues" as action items and risks by package; the app's broader issue union remains a separate display/model concern. | `_DomainEngines/proposals/pec/FINDINGS_2026-07-09_pec_product_interview.md` §4.5 |
| The standing plan's R3 row is reporting-vocabulary alignment over display/reporting surfaces, without reopening ADR-011 or the cockpit union. | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` (R3 row; reconciliation 2) |
| Standard reports still emit package/discipline "Issues: holds, decisions, risks, actions" and package issue summaries under the broader union. | `projects/pec/server/src/reports/standard.ts` |
| Package and overview web surfaces label `Open issues` over the broader union, while also separately exposing holds, interfaces, decisions, risks, and actions. | `projects/pec/web/src/pages/Packages.tsx`; `projects/pec/web/src/pages/Overview.tsx` |
| Action & Hold Log is intentionally a workbench over open work items, holds, interfaces, decisions, risks, and intake; it should keep typed operational wording rather than be relabeled as the client-facing issue report. | `projects/pec/web/src/pages/LogHome.tsx`; `projects/pec/server/src/services/views.ts` |
| REPORT_BASIS currently names both the broad cockpit counts and the discipline-report Needs/Risks structure; any wording change must preserve rule ids and basis pointers. | `projects/pec/execution/_Coordination/REPORT_BASIS.md` |

## Decision to rule

Whether to authorize one display/reporting vocabulary tranche:

1. **Client-facing labels:** in reports and dashboard surfaces intended for
   sponsor/PD reading, reserve "issues" for the owner vocabulary:
   action items + risks. Show holds, decisions, and interfaces under explicit
   operational labels such as Holds, Decisions, Interfaces, or Review items.
2. **Broad cockpit preserved:** the internal package cockpit / Action & Hold
   Log may keep the broad typed union, but its labels must say "open records",
   "operational items", "cockpit rows", or equivalent when the set includes
   holds/decisions/interfaces. No source record disappears.
3. **REPORT_BASIS update:** document the vocabulary split: client-facing
   issue count vs operational union count, with rule ids/basis pointers
   unchanged or renamed only where tests prove compatibility.
4. **Standard reports:** weekly and package reports separate client-facing
   issue counts from Holds / Decisions / Interfaces / Needs where present.
   The Markdown drafts must not imply that decisions/interfaces are client
   "issues" unless the row is explicitly a risk/action item.
5. **Web display:** package/overview/discipline labels and CSV export names
   are updated where they currently present the broad union as "issues".
   Drill links and contributing refs remain unchanged.
6. **Tests / visual checks:** regression tests cover report payload labels and
   basis; visual pass covers Package detail, Overview, Discipline detail, and
   Action & Hold Log at desktop and narrow widths.

**Not in scope:** changing the underlying ADR-011 issue union; changing
record types, counts, permissions, filters, imports, or lifecycle states;
adding mutation/task-management behavior; D-PEC-32 issue-model completeness;
D-PEC-33 deep links; interfaces import; needs typing; MDL-RAIL consistency.

## Fence (exact; STOP outside it)

O-A may touch only:

- `projects/pec/server/src/reports/**`
- `projects/pec/server/src/services/views.ts` (label/payload naming only,
  no new write path)
- `projects/pec/server/test/**`
- `projects/pec/web/src/pages/Overview.tsx`
- `projects/pec/web/src/pages/Packages.tsx`
- `projects/pec/web/src/pages/Disciplines.tsx`
- `projects/pec/web/src/pages/LogHome.tsx`
- `projects/pec/web/src/shared.tsx` only if a shared display label helper is
  needed and no other tranche is touching it
- `projects/pec/execution/_Coordination/REPORT_BASIS.md`

No `core/**` schema/type changes; no import behavior; no tracked DB files; no
new dependency; no record-state mutation.

## Options

- **O-A (recommended):** align report/dashboard vocabulary as above while
  preserving the operational union and all drill paths.
- **O-B:** reports only; leave web dashboards unchanged. Lower risk, but the
  PD-facing app remains vocabulary-misaligned.
- **O-C:** documentation-only convention in REPORT_BASIS.
- **O-D:** defer.

## Verification plan (workplan step-4 bar)

PEC belt-and-braces; report tests proving the count buckets and labels;
scope containment subset of the ruled fence; self-check / coord-check /
`git diff --check`; visual pass on the named pages at desktop and narrow
viewports; adversarial review that no record category is hidden, no count is
invented, and ADR-011/cockpit semantics are not reopened.

## Rollback

Single revert of the tranche commit(s). Display labels and report payload
field names return to the prior wording; no data migration involved.

## Human ruling

**RULED: O-A** (owner in-session, Ryan Tufts, 2026-07-09, verbatim):

> D-PEC-48: O-A with the vocabulary: client-facing "issues" = action items +
> risks + holds; decisions segregated as decisions; interfaces their own
> relationship/status category; internal cockpit keeps typed operational
> labels. Supersedes-by-extension of findings §4.5, recorded in the packet.

Execution rider: this ruling supersedes-by-extension the narrower findings
§4.5 vocabulary. Client-facing "issues" means action items + risks + holds.
Decisions are segregated as decisions. Interfaces are their own relationship
and later status category. Internal cockpit/workbench surfaces keep typed
operational labels and must not hide source categories.
