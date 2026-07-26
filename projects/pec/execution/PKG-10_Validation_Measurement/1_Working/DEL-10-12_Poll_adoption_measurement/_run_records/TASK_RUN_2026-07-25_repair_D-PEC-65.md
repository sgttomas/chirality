# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

**Deliverable:** DEL-10-12 · **Package:** PKG-10 · **Instrument:** D-PEC-65 §3.1
**Agent:** sealed ephemeral Agent 2 (file-tool-only) · **File touched:** `Dependencies.csv`

## Rows dispositioned

| DependencyID | Class found | Disposition |
|---|---|---|
| DEP-10-12-001 | ANCHOR (read-only) | untouched |
| DEP-10-12-002 | ANCHOR (read-only) | untouched |
| DEP-10-12-003 | EVQ-001 duplication | REPAIRED |
| DEP-10-12-004 | EVQ-001 duplication | REPAIRED |
| DEP-10-12-005 | EVQ-001 duplication | REPAIRED |

EXECUTION rows inspected: 3. Repaired: 3. Waived: 0. Blocked: 0.

## Cells changed

**DEP-10-12-003** (→ DEL-04-01; E-A22)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `SOW-060 note: "Measures uptake of SOW-004; arms limb 1 of the falsification clause"` → `ScopeLedger.csv row SOW-004`
- `EvidenceQuote`: same duplicated text → `PEC-ORI-001,PKG-04,DEL-04-01,OBJ-001`
- Aptness: the `Statement` is the coverage fact "SOW-004 is covered by DEL-04-01"; the `SOW-004` row's `DeliverableIDs` column carries `DEL-04-01`.

**DEP-10-12-004** (→ DEL-08-01; E-N08)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `SourceRef`: `SOW-060: sessions "consuming orientation" (served over the API)` → `§4 package table row PKG-08`
- `EvidenceQuote`: same duplicated text (whose "(served over the API)" clause was the seeder's own inference, not source text) → `The machine-consumer surface: Unix-socket binding, token-scoped access classes, p95 latency, versioned additive schema, compact citation-bearing responses, SSE subscription`
- Aptness: the accepted §4 package charter establishes PKG-08 — DEL-08-01's package, whose deliverable is the Unix-socket binding — as the machine-consumer surface, i.e. the surface on which API consumption occurs and can be instrumented.

**DEP-10-12-005** (→ DEL-07-03; E-P77)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `SOW-060: "eligible session starts / mode transitions consuming orientation"` → `ScopeLedger.csv row SOW-036`
- `EvidenceQuote`: same duplicated text → `Implement the harness hooks CLI bridge (session start/stop, status, scope declaration), declared and attributable`
- Aptness: the hooks CLI bridge (DEL-07-03's scope item) is what carries session start/stop, so poll instrumentation observing session starts depends on it — the `Statement`'s claim.

## Statement edits

None.

## Anomaly recorded, not changed

`DEP-10-12-004`'s `Statement` carries a refutation-round provenance prefix: `R3-F1: adoption instrumentation observes API consumption`. Unlike the `R3-F14`-style cells that state no claim at all, this one does state the dependency claim after the prefix, so it does not misstate the claim and was left byte-identical under the flagged-edits-only rule. Flagged here for the dispatcher in case the loop wants the provenance prefix stripped under a separate act.

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
| `DEP-10-12-003` | `SourceRef` | `ScopeLedger.csv row SOW-004` | `ScopeLedger.csv row SOW-004 (ScopeItemStatement; DeliverableIDs names DEL-04-01)` |
| `DEP-10-12-003` | `EvidenceQuote` | `PEC-ORI-001,PKG-04,DEL-04-01,OBJ-001` | `Serve per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes each with its unparking owner action` |

`EvidenceFile` unchanged (`execution/_Decomposition/ScopeLedger.csv`).

Why: the superseded quote was a raw CSV ID-tuple — a slice across the
`SourceRef`/`PackageID`/`DeliverableIDs`/`ObjectiveIDs` columns, not human source
prose. The row's `ScopeItemStatement` is now quoted; the `DeliverableIDs` binding
that carries the coverage warrant is named in `SourceRef` as the locus detail.
`DEP-10-12-004` and `DEP-10-12-005` were not in the finding set and are untouched,
as is the anomaly recorded above.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-004`,
`ScopeItemStatement` column. `SourceRef` carries no quoted span. Row re-read
post-edit: 29 columns intact.
