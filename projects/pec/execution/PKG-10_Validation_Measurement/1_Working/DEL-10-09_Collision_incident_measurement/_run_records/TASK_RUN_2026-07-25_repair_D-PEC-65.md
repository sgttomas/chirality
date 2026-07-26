# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

**Deliverable:** DEL-10-09 · **Package:** PKG-10 · **Instrument:** D-PEC-65 §3.1
**Agent:** sealed ephemeral Agent 2 (file-tool-only) · **File touched:** `Dependencies.csv`

## Rows dispositioned

| DependencyID | Class found | Disposition |
|---|---|---|
| DEP-10-09-001 | ANCHOR (read-only) | untouched |
| DEP-10-09-002 | ANCHOR (read-only) | untouched |
| DEP-10-09-003 | EVQ-001 duplication | REPAIRED |

EXECUTION rows inspected: 1. Repaired: 1. Waived: 0. Blocked: 0.

## Cells changed

**DEP-10-09-003** (→ DEL-06-06; E-A25)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `SOW-084 note: "Measures effectiveness of SOW-031"` → `ScopeLedger.csv row SOW-031`
- `EvidenceQuote`: same duplicated text → `PEC-PRS-006,PKG-06,DEL-06-06,OBJ-003,,FALSE,Carries PEC-K-06`
- Aptness: the `Statement` is the coverage fact "SOW-031 is covered by DEL-06-06"; the `SOW-031` row's `DeliverableIDs` column carries `DEL-06-06`. The same locus and quote are used at DEP-10-06-003, which asserts the identical coverage fact — this is the same register fact, not a copied placeholder.

## Statement edits

None.

## Waivers declared

None. The row was class (a); no EVQ-003/EVQ-004 finding exists in this register.

## Notes

No rows added, deleted, or reordered; 29-column schema and quoting conventions preserved.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MAJ-2** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-10-09-003` | `SourceRef` | `ScopeLedger.csv row SOW-031` | `ScopeLedger.csv row SOW-031 (ScopeItemStatement; DeliverableIDs names DEL-06-06)` |
| `DEP-10-09-003` | `EvidenceQuote` | `PEC-PRS-006,PKG-06,DEL-06-06,OBJ-003,,FALSE,Carries PEC-K-06` | `Detect and surface advisory overlaps (write scopes, shared branches, same merge target) without ever blocking` |

`EvidenceFile` unchanged (`execution/_Decomposition/ScopeLedger.csv`).

Why: the superseded quote was a raw CSV ID-tuple spanning seven columns
(`SourceRef` through `Notes`), not human source prose. The row's
`ScopeItemStatement` is now quoted; the `DeliverableIDs` binding that carries the
coverage warrant is named in `SourceRef` as the locus detail. The locus and quote
remain deliberately identical to `DEP-10-06-003`'s: both rows assert the same
register coverage fact.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-031`,
`ScopeItemStatement` column. `SourceRef` carries no quoted span. Row re-read
post-edit: 29 columns intact.
