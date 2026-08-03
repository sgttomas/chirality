---
amendment_id: SCA-004
doc_kind: scope_change.preview_validation
gate: 3
created: 2026-08-03
status: non_mutating_pass
---

# SCA-004 Gate 3 preview validation

## Result

`PASS` — the exact preview is internally reciprocal and is anchored to the
accepted revision 1.3 bytes. This is a non-mutating simulation; no live
postimage exists and no Gate 4 or Gate 5 act is inferred.

## Baseline and synchronization

| Check | Result |
|---|---|
| Worktree branch | `codex/pec-dpec-packets-20260802` |
| Worktree HEAD | `7249281e1f84ba5abee3c31c2fea3736b22000d3` |
| `origin/main` observed ref | `7249281e1f84ba5abee3c31c2fea3736b22000d3` |
| Branch contains `origin/main` | `PASS` |
| Accepted decomposition preimage | revision 1.3 at SHA-256 `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| Accepted Gate 2 impact | SHA-256 `df366142e47063b452e43fc90958b839bba6ab0709f556f336e32d52e9556661` |

## Semantic binding

| Required semantic section | Bound heading/surface | Result |
|---|---|---|
| Change Register | `## 11. Decision Log` and `## 12. Revision History` | `PASS` |
| Unit Ledger | `## 6. Scope Ledger` → authoritative `ScopeLedger.csv` | `PASS` |
| Primary Partitions | `## 4. Packages` | `PASS` |
| Secondary Entities | `## 5. Deliverables` → authoritative `Deliverables.csv` | `PASS` |
| Objectives | `## 3. Objectives` plus `ScopeLedger.csv.ObjectiveIDs` | `PASS` |
| Coverage / Telemetry | `## 7. Coverage & Telemetry` | `PASS` |
| Open Issues | `## 10. Open Issues` | `PASS` |

No section was resolved by numeric position alone.

## Exact preimage assertions

- `SOW-077` exists exactly once in `ScopeLedger.csv` as `TBD`, with empty
  package/deliverable/objective/decision fields and `OpenIssue=TRUE`.
- `SOW-094` exists exactly once as `IN → PKG-01 → DEL-01-06 → OBJ-004`, with
  `OpenIssue=FALSE`.
- `DEL-01-06` exists exactly once, covers only `SOW-094`, and preserves the
  stable name `Loop registry (local config default)`.
- The exact old markdown rows and CSV rows quoted in `Amendment_Preview.md`
  match the accepted preimage.

## In-memory successor simulation

Only `SOW-077`, `SOW-094`, and `DEL-01-06` were changed in the simulated
register dictionaries. The resulting assertions are:

| Assertion | Simulated result |
|---|---|
| Scope rows | `94` |
| Status counts | `72 IN / 14 OUT / 8 TBD` |
| SOW-077 lineage | `PKG-01 / DEL-01-06 / OBJ-004` |
| SOW-077 open flag | `FALSE` |
| DEL-01-06 coverage | `SOW-077;SOW-094` |
| Reciprocal ledger/deliverable mapping | `PASS` |
| PKG-01 mapped scope count | `8` |
| OBJ-004 mapped scope count | `11` |
| IN rows without package / deliverable | `0 / 0` |
| IN rows without objective | `11` |
| Packages / deliverables / objectives | `11 / 64 / 6` |
| Context Envelope population | `S 28 / M 34 / L 2 / XL 0` — unchanged |
| Execution dependency edges / SCCs | `119 / 0` — no previewed edge change |
| Open / resolved issues | `10 / 3` |

## Variant invariants and amendment boundary

| Check | Result |
|---|---|
| Stable IDs | `PASS` — no ID changes |
| Package-discipline isolation | `PASS` — registry contract/config remains PKG-01 |
| Artifact-kind deliverable granularity | `PASS` — DEL-01-06 remains one BACKEND_FEATURE_SLICE |
| Parent closure | `NOT TRIGGERED` — no package/parent change |
| Source behavior | `NO_CHANGE` |
| Estimate/schedule class | `NO_CHANGE` |
| Supersession binding | `NOT REQUIRED` — D-PEC-78 answers an open PRD question rather than overriding an admitted fact |
| Gate 3 write scope | `PASS` — preview/evidence package only |

The pre-change AUDIT_DECOMP snapshot remains
`execution/_Evaluation/DecompCoverage/COV_SCA004_PRECHANGE_2026-08-02_2327/`:
0 blockers, one unrelated non-blocking DEL-08-02 artifact-location warning,
and full structural coverage. Its accepted pointer was not moved.

## Stop condition

The exact preview awaits owner Gate 3 approval. No propagation plan has been
prepared, Gate 4 is not open, and no live decomposition, pointer, metadata,
downstream, source, lifecycle, register, or foreign-loop byte was changed.
