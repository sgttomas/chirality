# QA Report — COV_SCA002_PRECHANGE

## Scan coverage

| Surface | Scanned | Method |
|---|---|---|
| `SOFTWARE_DECOMP.md` | full (63,480 bytes) | heading-bound semantic section parse |
| §4 Packages table | 11 rows | `PKG-\d{2}` row match |
| §5 Deliverables tables | 64 rows across 11 `### PKG-XX` subsections | `DEL-\d{2}-\d{2}` row match |
| §3 Objectives table | 6 rows | row match + range expansion (Decision_Log D-5) |
| §7 Coverage & Telemetry | 12 metric rows | metric-row match |
| `ScopeLedger.csv` | 94 rows | `csv.DictReader` |
| `Deliverables.csv` | 64 rows | `csv.DictReader` |
| `ContextBudgetQA.csv` | 64 rows | `csv.DictReader` |
| Package folders | 11 | `PKG-*` glob under execution root |
| Deliverable folders | 64 | `PKG-*/1_Working/DEL-*` glob |
| `_CONTEXT.md` | 64/64 | table-field parse |
| `_STATUS.md` | 64/64 | `**Current State:**` extraction |

## Section binding resolution

`AGENT_AUDIT_DECOMP.md` and `AGENT_SCOPE_CHANGE.md` both carry a
`SOFTWARE_DECOMP` binding table with **hard-coded section numbers that do not
match this document**. The protocols direct binding by semantic name and
heading text ("Bind by heading text when section numbers are absent"), which
is what was done. Resolution actually used:

| Semantic section | Binding table says | This document | Bound to |
|---|---|---|---|
| Ledger / Unit Ledger | §5 Scope Ledger | §5 is *Deliverables* | **§6 Scope Ledger** + `ScopeLedger.csv` (authoritative) |
| Primary Partitions | §3 Packages | §3 is *Objectives* | **§4 Packages** |
| Secondary Entities | §4 Deliverables | §4 is *Packages* | **§5 Deliverables** + `Deliverables.csv` (authoritative) |
| Objectives | via Scope Ledger `ObjectiveID(s)` | both exist | **§3 Objectives** (objective-side view) + `ScopeLedger.csv` `ObjectiveIDs` (item-side, authoritative) |
| Change Register | §8 Change Log | §8 is *Context Budget QA*; no "Change Log" heading exists | **§11 Decision Log** + **§12 Revision History** |
| Coverage Basis | `AUDIT_DECOMP` output | — | **§7 Coverage & Telemetry** + this run |

This is a **binding-table drift**, not a decomposition defect: the document
conforms to `AGENT_SOFTWARE_DECOMP.md`'s own phase-numbered layout, and every
semantic section resolves unambiguously by heading text. It is surfaced here
because any future agent that trusts the hard-coded numbers will parse the
wrong sections.

## Parse issues

None. Every declared entity parsed cleanly; no malformed table row, no
unresolvable ID, no encoding issue.

## Limits of this run

1. **Artifact presence is not meaningfully measurable.** `AnticipatedArtifacts`
   holds prose descriptions, not filenames. With all 64 deliverables `OPEN`
   and no production output, `artifact_presence_pct = 0.0` carries no quality
   signal.
2. **No prior `coverage_summary.json` exists** for delta computation — both
   SCA-001 baselines returned `FAILED_INPUTS`. Check 12 is `PARTIAL`.
3. **`OI-013` remains open.** No durable repo-native register validator exists;
   the original coverage/coupling assertions ran in a session-local generator
   that is not part of the package (§7, `DL-14`). This inline audit is a
   SCOPE_CHANGE-run baseline, not a standing build gate, and does not close
   `OI-013`.
4. **Semantic quality is out of scope.** This audit measures declaration-vs-
   filesystem coverage and internal register consistency. Whether a given
   objective attribution is *correct* is Gate 2/3 judgment, not an audit
   verdict.

## Corroborating deterministic check (outside the audit contract, recorded for Gate 1)

`python3 tools/coordination/analyze_dep_closure.py projects/pec/execution`:

```text
64 Dependencies.csv files, 255 rows, schema 64 valid / 0 invalid
ANCHOR 135 / EXECUTION 120; IMPLEMENTS_NODE 64 present, 0 missing
Evidence coverage 255/255; Graph 62 nodes / 120 edges
Orphans 2; SCCs (size > 1) 0; bidirectional pairs 0; ID normalizations 0
```

Matches the `D-PEC-62` landing values pinned in `D-PEC-64` §4.4 exactly. This
is the pre-change reading of the no-collateral-state-change check.
