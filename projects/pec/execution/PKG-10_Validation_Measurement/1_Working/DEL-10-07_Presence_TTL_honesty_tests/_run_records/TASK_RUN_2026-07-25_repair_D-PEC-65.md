# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

**Deliverable:** DEL-10-07 · **Package:** PKG-10 · **Instrument:** D-PEC-65 §3.1
**Agent:** sealed ephemeral Agent 2 (file-tool-only) · **File touched:** `Dependencies.csv`

## Rows dispositioned

| DependencyID | Class found | Disposition |
|---|---|---|
| DEP-10-07-001 | ANCHOR (read-only) | untouched |
| DEP-10-07-002 | ANCHOR (read-only) | untouched |
| DEP-10-07-003 | EVQ-001 duplication | REPAIRED |

EXECUTION rows inspected: 1. Repaired: 1. Waived: 0. Blocked: 0.

## Cells changed

**DEP-10-07-003** (→ DEL-06-05; E-A24)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `SOW-062 note: "Tests SOW-030"` → `ScopeLedger.csv row SOW-030`
- `EvidenceQuote`: same duplicated text → `Carry TTLs and last-heartbeat age on presence records; never assert liveness beyond last heartbeat,PEC-PRS-005,PKG-06,DEL-06-05`
- Aptness: the span carries both the scope item's own statement (the TTL-honesty behaviour under test) and its `DeliverableIDs` value `DEL-06-05`, which is exactly the coverage fact the `Statement` asserts.

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
| `DEP-10-07-003` | `SourceRef` | `ScopeLedger.csv row SOW-030` | `ScopeLedger.csv row SOW-030 (ScopeItemStatement; DeliverableIDs names DEL-06-05)` |
| `DEP-10-07-003` | `EvidenceQuote` | `Carry TTLs and last-heartbeat age on presence records; never assert liveness beyond last heartbeat,PEC-PRS-005,PKG-06,DEL-06-05` | `Carry TTLs and last-heartbeat age on presence records; never assert liveness beyond last heartbeat` |

`EvidenceFile` unchanged (`execution/_Decomposition/ScopeLedger.csv`).

Why: the superseded quote was a prose-splice — it ran the `ScopeItemStatement`
through the CSV field boundary and on into `SourceRef`/`PackageID`/
`DeliverableIDs`, presenting machine columns as continuous source text. The quote
is now the statement prose alone; the `DeliverableIDs` binding that carries the
coverage warrant is named in `SourceRef` as the locus detail.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-030`,
`ScopeItemStatement` column. `SourceRef` carries no quoted span. Row re-read
post-edit: 29 columns intact.
