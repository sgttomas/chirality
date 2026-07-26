# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

**Deliverable:** DEL-10-04 · **Package:** PKG-10 · **Instrument:** D-PEC-65 §3.1
**Agent:** sealed ephemeral Agent 2 (file-tool-only) · **File touched:** `Dependencies.csv`

## Rows dispositioned

| DependencyID | Class found | Disposition |
|---|---|---|
| DEP-10-04-001 | ANCHOR (read-only) | untouched |
| DEP-10-04-002 | ANCHOR (read-only) | untouched |
| DEP-10-04-003 | EVQ-001 duplication | REPAIRED |

EXECUTION rows inspected: 1. Repaired: 1. Waived: 0. Blocked: 0.

## Cells changed

**DEP-10-04-003** (→ DEL-04-03; E-A21)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `SOW-059 note: "Method + any needed instrumentation; measures SOW-007"` → `ScopeLedger.csv row SOW-007`
- `EvidenceQuote`: same duplicated text → `PEC-ORI-004,PKG-04,DEL-04-03,OBJ-001`
- Aptness: the `Statement` is the coverage fact "SOW-007 is covered by DEL-04-03". The direct warrant is the authoritative assignment register: the `SOW-007` row's `SourceRef`/`PackageID`/`DeliverableIDs`/`ObjectiveIDs` span carries `DEL-04-03` in the `DeliverableIDs` column. The edge's motivating note (SOW-059 "measures SOW-007") remains true and corroborating but does not itself state the coverage claim, so it was not used as the quote.

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
| `DEP-10-04-003` | `SourceRef` | `ScopeLedger.csv row SOW-007` | `ScopeLedger.csv row SOW-007 (ScopeItemStatement; DeliverableIDs names DEL-04-03)` |
| `DEP-10-04-003` | `EvidenceQuote` | `PEC-ORI-004,PKG-04,DEL-04-03,OBJ-001` | `Attach a citation (file path, anchor, and/or SHA) to every claim in an orientation response` |

`EvidenceFile` unchanged (`execution/_Decomposition/ScopeLedger.csv`).

Why: the superseded quote was a raw CSV ID-tuple — a slice across the
`SourceRef`/`PackageID`/`DeliverableIDs`/`ObjectiveIDs` columns, not human source
prose. The row's `ScopeItemStatement` is now quoted; the `DeliverableIDs` binding
that carries the coverage warrant is named in `SourceRef` as the locus detail.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-007`,
`ScopeItemStatement` column. `SourceRef` carries no quoted span. Row re-read
post-edit: 29 columns intact.
