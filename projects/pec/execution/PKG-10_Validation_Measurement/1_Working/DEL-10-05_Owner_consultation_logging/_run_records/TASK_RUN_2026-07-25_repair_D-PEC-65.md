# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

**Deliverable:** DEL-10-05 · **Package:** PKG-10 · **Instrument:** D-PEC-65 §3.1
**Agent:** sealed ephemeral Agent 2 (file-tool-only) · **File touched:** `Dependencies.csv`

## Rows dispositioned

| DependencyID | Class found | Disposition |
|---|---|---|
| DEP-10-05-001 | ANCHOR (read-only) | untouched |
| DEP-10-05-002 | ANCHOR (read-only) | untouched |
| DEP-10-05-003 | EVQ-001 duplication | REPAIRED |
| DEP-10-05-004 | EVQ-001 duplication | REPAIRED |
| DEP-10-05-005 | EVQ-001 duplication | REPAIRED |

EXECUTION rows inspected: 3. Repaired: 3. Waived: 0. Blocked: 0.

## Cells changed

**DEP-10-05-003** (→ DEL-01-04; E-A26)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `SOW-085 note: "grounded in SOW-057 self-observability"` → `ScopeLedger.csv row SOW-057`
- `EvidenceQuote`: same duplicated text → `PEC-SVC-006,PKG-01,DEL-01-04,OBJ-006`
- Aptness: the `Statement` is the coverage fact "SOW-057 is covered by DEL-01-04"; the `SOW-057` row's `DeliverableIDs` column carries `DEL-01-04`.

**DEP-10-05-004** (→ DEL-04-01; E-P75)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `DEL-10-05: "Orientation-read ... logging"` → `Deliverables.csv row DEL-10-05 Description column`
- `EvidenceQuote`: same duplicated (and elided) text → `Orientation-read and dashboard-consultation logging sufficient to evaluate the P2 exit test`
- Aptness: replaces an ellipsis-bearing pseudo-quote with the contiguous register text; it names orientation-read logging as this deliverable's own obligation, warranting the dependency on the orientation return.

**DEP-10-05-005** (→ DEL-09-01; E-P76)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `DEL-10-05: "dashboard-consultation logging"` → `ScopeLedger.csv row SOW-085`
- `EvidenceQuote`: same duplicated text → `Log orientation-read and dashboard-consultation activity sufficient to evaluate the §12 P2 exit test`
- Aptness: the scope item itself names dashboard-consultation activity as a logged surface, which is the `Statement`'s claim.

## Statement edits

None.

## Waivers declared

None. All three rows were class (a); no EVQ-003/EVQ-004 finding exists in this register.

## Notes

No rows added, deleted, or reordered; 29-column schema and quoting conventions preserved.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MAJ-2** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-10-05-003` | `SourceRef` | `ScopeLedger.csv row SOW-057` | `ScopeLedger.csv row SOW-057 (ScopeItemStatement; DeliverableIDs names DEL-01-04)` |
| `DEP-10-05-003` | `EvidenceQuote` | `PEC-SVC-006,PKG-01,DEL-01-04,OBJ-006` | `Log PEC's own reconcile runs and ingest activity, inspectable (self-observability)` |

`EvidenceFile` unchanged (`execution/_Decomposition/ScopeLedger.csv`).

Why: the superseded quote was a raw CSV ID-tuple — a slice across the
`SourceRef`/`PackageID`/`DeliverableIDs`/`ObjectiveIDs` columns, not human source
prose. The row's `ScopeItemStatement` is now quoted; the `DeliverableIDs` binding
that carries the coverage warrant is named in `SourceRef` as the locus detail.
`DEP-10-05-004` and `DEP-10-05-005` were not in the finding set and are untouched.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-057`,
`ScopeItemStatement` column. `SourceRef` carries no quoted span. Row re-read
post-edit: 29 columns intact.
