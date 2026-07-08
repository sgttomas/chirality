# D-PEC-29 - PROPOSAL: Packages/Deliverables issue linkage

**Status:** AWAITING_RULING.
**Date prepared:** 2026-07-08
**Decision ID:** D-PEC-29
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded source tranche under the adopted reporting-first PEC
> UI/UX redesign plan. Source execution remains prohibited unless and until the
> owner rules this packet. Sources govern on any disagreement.

## Why this row exists

The owner direction names two reporting axes: issues tracked at package level
and completeness tracked at deliverable level. D-PEC-29 links those axes: it
adds issue-mix context to Packages, brings deliverable risks into the
deliverable detail open-items view, and makes package/deliverable movement
through the UI interrogable through the D-PEC-25 drill spine.

The T0 design specification pins the scope in
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
§5, §6, and §11B P6-P8.

## Dependencies

D-PEC-29 source execution depends on D-PEC-25 being ruled and executed first,
because its UI links and cross-record rows rely on the shared `<RecordRef>`
drill spine. D-PEC-27 is a soft dependency for richer issue summaries, but
D-PEC-29 can execute independently once 25 lands by using package/detail
payloads already present plus the projections named here.

## Verified current state

| Fact | Source |
|---|---|
| `openIssueCount` already counts holds, interfaces, decisions, risks, and action items per package. | `projects/pec/server/src/services/views.ts:171-192` |
| `packagesView` currently exposes collapsed `openIssues` but not issue mix or worst-issue basis. | `projects/pec/server/src/services/views.ts:194-205` |
| `packageDetailView.summary` and `issues[]` already carry package issue details and summary counts. | `projects/pec/server/src/services/views.ts:313-330` |
| `packageDetailView.issues[]` includes hardcoded interface/risk `ageWd: 0`; D-PEC-27 owns the factual-basis repair when `views.ts` is first touched. | `projects/pec/server/src/services/views.ts:251-280`; T0 §11B/P4 |
| `needsLead[]` already carries `recordType`, `id`, and `ref` for lead queue rows. | `projects/pec/server/src/services/views.ts:282-296` |
| `deliverableDetailView.openItems` has work items, checks, comments, holds, approval records, and decision dependencies, but no risks key. | `projects/pec/server/src/services/views.ts:419-439` |
| Package issue rows still use `issueHref`, which routes too coarsely and is superseded by D-PEC-25. | `projects/pec/web/src/pages/Packages.tsx:78-83`; T0 §5(d) |
| Deliverable open-item tables render cross-record refs as inert monospace text today. | `projects/pec/web/src/pages/Deliverables.tsx:240-291`; T0 §6(d) |

## Decision to rule

Whether to authorize one source tranche implementing D-PEC-29 package and
deliverable issue linkage:

1. **Package register issue mix:** add server-computed `issueMix` to
   `packagesView`: by-type counts and worst issue, each with an Explain-shaped
   basis over the same membership as `openIssueCount`.
2. **Package detail controls:** add issue-mix / worst-issue chips beside the
   existing issue count and wire summary chips to filter the existing package
   cockpit rather than creating a duplicate issue store.
3. **Deliverable detail risks:** add `openItems.risks` to
   `deliverableDetailView` for open risks with `deliverableId` equal to the
   deliverable, and render them as a typed open-items table.
4. **Breadcrumbs and package links:** use the D-PEC-24 breadcrumb primitive
   and D-PEC-25 drill spine so Package and Deliverable detail pages move
   predictably between package, deliverable, and register homes.
5. **MDL Package cell link/filter:** make the Deliverables register package
   cell link to the package detail or package-filtered view without changing
   the MDL contract.
6. **Optional related-records projection:** only if the owner selects O-B,
   add a read-only `relatedRecordsView` route over existing link tables
   (`holdLinks`, `decisionLinks`, conditions, and risk package/deliverable
   references). It returns typed edges only; no mutation.
7. **No model-extension default:** interface/decision deliverable foreign keys
   and wider hold target attribution remain D-PEC-32 / slate item 5, not this
   packet.

**Not in scope:** D-PEC-27 Log dashboard implementation; D-PEC-32 model
changes; interface/decision deliverable foreign keys; in-app issue mutation;
task boards; bulk edit; import behavior; new dependencies; database migration
unless O-B explicitly requires a read-only route over existing tables (no new
table).

## Fence (exact; STOP outside it)

Base O-A fence:

- `projects/pec/server/src/services/views.ts`
- `projects/pec/web/src/pages/Packages.tsx`
- `projects/pec/web/src/pages/Deliverables.tsx`
- `projects/pec/web/src/shared.tsx`

Additional O-B-only fence if `relatedRecordsView` is ruled in:

- `projects/pec/server/src/api.ts`

No `core/**`, no database migration, no `agent-sidecar/**`, no root manifests,
no profile, no Log/Admin/Plan/Register source edits, no decision/register file
edits during execution except the post-run receipt.

## Options

- **O-A (recommended):** package issue mix, deliverable risks, breadcrumbs,
  package links, and cockpit filters; defer `relatedRecordsView`.
- **O-B:** O-A plus the optional read-only `relatedRecordsView` route/panel.
- **O-C:** package issue mix only; defer deliverable risks and related-records
  work.
- **O-D:** defer D-PEC-29.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Server tests for `packagesView.issueMix` and `deliverableDetailView.openItems.risks`;
  O-B adds route tests for `relatedRecordsView`.
- Browser visual pass on Packages register/detail and Deliverables register/detail
  at about 1280 px desktop and one narrow/mobile viewport: no blank pages,
  overlap, or broken filters.
- Drill pass: package issue chips filter to the cockpit; deliverable risks
  route to the Risks register; package cells navigate to package context;
  non-routable drawer-only records degrade per D-PEC-25.
- Scope containment: `git diff --name-only` is a subset of the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review of count membership, visibility/redaction, no duplicate
  issue truth, and no D-PEC-32 model work slipping into this tranche.

## Rollback

Single revert of the source tranche commit(s). No schema/data rollback is
needed; O-B's read-only route, if ruled, reverts with the UI.

## Human ruling

AWAITING_RULING. No source implementation is authorized by this packet until
the owner records a ruling.
