# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

**Deliverable:** DEL-10-10 · **Package:** PKG-10 · **Instrument:** D-PEC-65 §3.1
**Agent:** sealed ephemeral Agent 2 (file-tool-only) · **File touched:** `Dependencies.csv`

## Rows dispositioned

| DependencyID | Class found | Disposition |
|---|---|---|
| DEP-10-10-001 | ANCHOR (read-only) | untouched |
| DEP-10-10-002 | ANCHOR (read-only) | untouched |
| DEP-10-10-003 | EVQ-001 duplication | REPAIRED |
| DEP-10-10-004 | EVQ-001 duplication | REPAIRED |

EXECUTION rows inspected: 2. Repaired: 2. Waived: 0. Blocked: 0.

## Cells changed

**DEP-10-10-003** (→ DEL-02-05; E-P73)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `SOW-064: P1 "ingests PEC v2's accepted full dependency DAG"; SOW-015: dependency registers into DependencyEdge` → `Deliverables.csv row DEL-02-05`
- `EvidenceQuote`: same duplicated text → ``Dependency register parser,`Dependencies.csv` and `WORK_GRAPH.json` into DependencyEdge.``
- Aptness: the register names DEL-02-05 as the parser that reads `Dependencies.csv` and `WORK_GRAPH.json` — the DAG's file form the `Statement` refers to.

**DEP-10-10-004** (→ DEL-03-01; E-P74)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `SOW-064 (as E-P73)` → `ScopeLedger.csv row SOW-010`
- `EvidenceQuote`: `SOW-064 (as E-P73)` → `Make the record tier rebuildable in full from sources by one command; store gitignored and safe to delete; presence tier expected lost on rebuild,PEC-RCN-001,PKG-03,DEL-03-01`
- Aptness: the span carries the one-command rebuild-from-sources obligation and its `DeliverableIDs` value `DEL-03-01`, warranting that the self-ingest of file sources runs through that reconciler.

## Statement edits

None.

## Waivers declared

None. Both rows were class (a); no EVQ-003/EVQ-004 finding exists in this register.

## Notes

- No rows added, deleted, or reordered; 29-column schema and quoting conventions preserved.
- DEL-10-10 is a C-08 standing node; that edge metadata was not touched.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MAJ-2** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-10-10-003` | `SourceRef` | `Deliverables.csv row DEL-02-05` | `Deliverables.csv row DEL-02-05 (Description column)` |
| `DEP-10-10-003` | `EvidenceQuote` | `Dependency register parser,``Dependencies.csv`` and ``WORK_GRAPH.json`` into DependencyEdge.` | ``Dependencies.csv`` and ``WORK_GRAPH.json`` into DependencyEdge. |
| `DEP-10-10-004` | `SourceRef` | `ScopeLedger.csv row SOW-010` | `ScopeLedger.csv row SOW-010 (ScopeItemStatement; DeliverableIDs names DEL-03-01)` |
| `DEP-10-10-004` | `EvidenceQuote` | `Make the record tier rebuildable in full from sources by one command; store gitignored and safe to delete; presence tier expected lost on rebuild,PEC-RCN-001,PKG-03,DEL-03-01` | `Make the record tier rebuildable in full from sources by one command; store gitignored and safe to delete; presence tier expected lost on rebuild` |

`EvidenceFile` unchanged on both rows (`execution/_Decomposition/Deliverables.csv`
and `execution/_Decomposition/ScopeLedger.csv` respectively).

Why: both superseded quotes were prose-splices across CSV field boundaries.
`-003` ran the `Name` column into the `Description` column; `-004` ran the
`ScopeItemStatement` on into `SourceRef`/`PackageID`/`DeliverableIDs`. Each quote
is now single-cell prose; where the `DeliverableIDs` binding carries the warrant
(`-004`), it is named in `SourceRef` as the locus detail.

**Verbatim check:** `-003`'s quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/Deliverables.csv`, row `DEL-02-05`,
`Description` column; `-004`'s is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-010`,
`ScopeItemStatement` column. Neither `SourceRef` carries a quoted span. Both rows
re-read post-edit: 29 columns intact.
