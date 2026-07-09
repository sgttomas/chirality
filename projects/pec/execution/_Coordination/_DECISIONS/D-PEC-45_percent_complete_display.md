# D-PEC-45 - PROPOSAL: % complete display (deliverables + discipline tile)

**Status:** AWAITING_RULING
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-45
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04).

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> D-PEC-41 (O-A) landed PE-attested % complete in the model, API payloads,
> reports, and exports, but its fence excluded `web/**` — the values are not
> rendered anywhere. The owner asked in-session (2026-07-09): "Where the %
> complete for deliverables?" This packet is the display authorization.

## Decision to rule

Whether to authorize one read-only display tranche:

1. **Discipline detail** (`web/src/pages/Disciplines.tsx`): render the
   existing `band.percentComplete` (DISC-PCT) as a KPI tile alongside the
   other band tiles — drillable Explain, coverage-naming detail, absent when
   unattested (the payload already behaves this way; the tile is one line in
   the established KpiCard pattern). Show per-deliverable attested % (and
   verbatim markers, e.g. "Next Phase") as a column in the Activities tables.
2. **Deliverables register** (`web/src/pages/Deliverables.tsx`): a read-only
   "% complete" column showing the attested value or marker, blank when
   unattested — display only; no edit affordance exists or is added
   (reconciliation 1 stands: import is the only writer).

**Not in scope:** any mutation surface; week-over-week deltas (no snapshot
model); new aggregates (DISC-PCT already computed server-side per SPEC §1).

## Fence (exact; STOP outside it)

`projects/pec/web/src/**` only (display of already-served payload fields).
No server/core/sidecar changes, no new dependencies, no tracked DB files.

## Verification plan

pec belt-and-braces; visual pass on Disciplines detail + Deliverables at
~1280px and a narrow viewport with applied TWD data (tile drills, markers
render verbatim, unattested stays blank/absent); keyboard operability of the
new tile drill; scope ⊆ fence; self-check/coord-check/`git diff --check`.

## Rollback

Single revert.

## Human ruling

**OPEN — decision is the owner's (K-AUTH-1).** Rule O-A (both surfaces) /
O-B (discipline tile only) / O-C (defer).
