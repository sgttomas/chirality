# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-06-04 Live hierarchy edges |
| Package | PKG-06 Presence & Git Observation |
| Instrument | `D-PEC-65` §3.1 (RULED 2026-07-25) |
| Agent | sealed Agent 2 repair dispatch (file-tool-only) |
| File touched | `Dependencies.csv` (EXECUTION rows only) |

## Rows dispositioned

| DependencyID | Defect class | Disposition |
|---|---|---|
| DEP-06-04-001 | ANCHOR (read-only) | untouched |
| DEP-06-04-002 | ANCHOR (read-only) | untouched |
| DEP-06-04-003 | EVQ-001 (locus/quote duplication) | REPAIRED |
| DEP-06-04-004 | EVQ-001 (locus/quote duplication) | REPAIRED (+ Statement edit) |
| DEP-06-04-005 | EVQ-001 (locus/quote duplication) | REPAIRED |
| DEP-06-04-006 | EVQ-001 (locus/quote duplication) | REPAIRED |

## Cells changed

**DEP-06-04-003** (→ DEL-01-02 Presence-tier schema & entity model)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `DEL-01-02 defines HierarchyEdge` → `ScopeLedger.csv row SOW-002 (ScopeItemStatement)`
- `EvidenceQuote`: `DEL-01-02 defines HierarchyEdge` → `Implement the presence-tier entity model: Session, Worktree/GitRef, PresenceRecord, HierarchyEdge, ScopeClaim`
- Warrant: the cited ledger row assigns SOW-002 to DEL-01-02 and names
  `HierarchyEdge` as a presence-tier entity — the entity this deliverable
  instantiates.

**DEP-06-04-004** (→ DEL-06-01 Session presence records)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: duplicated quote text → `Deliverables.csv row DEL-06-04 (Description)`
- `EvidenceQuote`: duplicated locus text → `Parent-to-child session edges from daemon and hook feeds.`
- `Statement` (FLAGGED EDIT): `R3-F3` → `Hierarchy edges connect parent and child sessions whose records DEL-06-01 produces`
  - Reason: the seeded cell carried only a refutation-round finding tag and
    asserted no dependency claim at all; the rewrite states the claim the
    edge makes without changing its target, class, or maturity.

**DEP-06-04-005** (→ DEL-07-02 Daemon SSE subscriber bridge)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `SourceRef`: duplicated quote text → `SOFTWARE_DECOMP.md §2.1 SSOW row SOW-029`
- `EvidenceQuote`: duplicated locus text → `Maintain live parent→child hierarchy edges from daemon and hook feeds`
- Warrant: SOW-029 (this deliverable's own scope item) names the daemon feed
  as an input to hierarchy-edge maintenance; DEL-07-02 is that feed's bridge.

**DEP-06-04-006** (→ DEL-07-03 Hooks CLI bridge)
- `EvidenceFile`: PLAN exhibit → `docs/PRD.md`
- `SourceRef`: `SOW-029 (as E-P46)` → `PRD.md §9.4 requirement PEC-PRS-004`
- `EvidenceQuote`: `SOW-029 (as E-P46)` → `PEC shall maintain live parent→child hierarchy edges from daemon and hook feeds.`
- Warrant: the requirement of record names the hook feed as an input to
  hierarchy-edge maintenance; DEL-07-03 is that feed's bridge. Cited at the
  PRD locus (rather than repeating the SOW-029 locus used on -005) so the
  two sibling edges carry distinct, independently checkable loci.

## Statement edits flagged

1. **DEP-06-04-004** — before: `R3-F3`; after:
   `Hierarchy edges connect parent and child sessions whose records DEL-06-01 produces`.

Not edited: **DEP-06-04-003**'s `Statement`
(`R3-F3: DEL-06-04 creates HierarchyEdge instances`) retains its
refutation-round provenance prefix but does state the dependency claim, so
it was left untouched under the flagged-only rule.

## Waivers declared

None. All four rows carry real quotable accepted-truth evidence; EVQ-001
rows are never waivable in any case.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MAJ-6** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-06-04-004` | `SourceRef` | `Deliverables.csv row DEL-06-04 (Description)` | `Deliverables.csv row DEL-06-01 (Description)` |
| `DEP-06-04-004` | `EvidenceQuote` | `Parent-to-child session edges from daemon and hook feeds.` | `Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes); identity/lifecycle stay daemon-owned.` |

`EvidenceFile` unchanged (`execution/_Decomposition/Deliverables.csv`).
`Statement` unchanged — see the warrant confirmation below.

Why: the row's target is `DEL-06-01`, but the cited locus was this deliverable's
own `DEL-06-04` row — evidence about the consumer, not the producer. Re-grounded
on the target's own `Deliverables.csv` row, using the same span siblings
`DEP-06-03-003` and `DEP-08-05-004` already cite for `DEL-06-01`.

**Statement warrant, confirmed (not rewritten).** The `Statement` reads
"Hierarchy edges connect parent and child sessions whose records DEL-06-01
produces". The new quote states that `DEL-06-01` produces harness-reported
*session records*; this deliverable's own accepted description defines its
artifact as parent-to-child *session* edges. The producer/consumer relation the
`Statement` asserts is therefore warranted by the cited span together with the
row's own target identity, and it is left byte-identical. No silent rewrite.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/Deliverables.csv`, row `DEL-06-01`,
`Description` column, and is byte-identical to the span at `DEP-06-03-003`.
`SourceRef` carries no quoted span. Row re-read post-edit: 29 columns intact.
