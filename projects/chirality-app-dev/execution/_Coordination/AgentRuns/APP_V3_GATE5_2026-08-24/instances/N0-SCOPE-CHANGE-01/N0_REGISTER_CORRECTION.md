# N0 — Corrected Companion-Register Candidate

**RunID:** `APP_V3_GATE5_2026-08-24`
**Node:** `N0`
**Role:** `SCOPE_CHANGE`
**Basis commit:** `cc196023a5532fe58955655c1144cd09ee88343a`
**Verdict:** `PASS_AWAITING_INDEPENDENT_REVIEW`

## Authorized transformation

The owner-approved A8-A correction was applied as a pure deterministic anchor correction to:

`projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase2b/CONTRACT_INVARIANT_COVERAGE_REGISTER_REGENERATED_CANDIDATE.csv`

The only transformation was replacement, in every `AppDecompositionBasis` cell, of:

`932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f`

with the true decomposition post-image:

`932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`

The existing `candidate-sha256=` label is retained exactly as authorized. No relabelling to an applied-state form was performed or required.

## Exact lineage

| Property | Pre-image | Corrected post-image |
| --- | --- | --- |
| Path | `Phase2b/CONTRACT_INVARIANT_COVERAGE_REGISTER_REGENERATED_CANDIDATE.csv` | `Phase5/CORRECTED_COMPANION_REGISTER_CANDIDATE.csv` |
| SHA-256 | `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0` | `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` |
| Bytes | `98230` | `98230` |
| Data rows | `83` | `83` |
| Invariant families | `50` | `50` |

Cause: Phase 2 introduced a non-resolving decomposition candidate identity into all 83 `AppDecompositionBasis` cells, and Phase 2b carried it forward verbatim. The correction changes exactly those 83 cells in exactly one column.

## Mechanical checks

- Corrected candidate SHA-256: `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` — PASS.
- Corrected candidate byte count: `98230` — PASS.
- Data-row count: `83` — PASS.
- Distinct `InvariantFamily` count: `50` — PASS.
- Incorrect identity occurrences in `AppDecompositionBasis`: `0` — PASS.
- True identity occurrences in `AppDecompositionBasis`: `83` — PASS.
- Changed cells: `83` across `83` rows — PASS.
- Changed columns: `AppDecompositionBasis` only — PASS.
- Header and every other cell: byte-semantic values identical — PASS.
- Candidate label form: `candidate-sha256=` present with the corrected identity in all 83 rows — PASS.

Candidate whitespace was run against basis `cc196023a5532fe58955655c1144cd09ee88343a` after candidate generation and before this hash-pinning record was created:

```text
PASS: candidate whitespace is clean (untracked binary/symlink paths safely skipped: 0).
```

## Immutable-history caveat

The superseded Phase-2 and Phase-2b candidate and transaction artifacts remain immutable historical evidence and were not edited:

- Phase-2 candidate: `f2d2e904d4f8b58da106fdcde7ed495146ea7d67de97f5b0535608879dab0079`.
- Phase-2 transaction: `ace737e599d8f7ec5bdefa47192e30a83f4c12112a032ffe0e0df834dda7ca84`.
- Phase-2b candidate: `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0`.
- Phase-2b transaction: `db1941c1c87ae7cd849dac3b32968a6911e74eaee8c56239725682e44b93603d`.

Those artifacts retain the incorrect historical anchor by design. The new Phase-5 candidate supersedes them for register application only; it does not rewrite their evidence lineage.

## Boundary

No live decomposition, contract, companion register, pointer, dependency record, Root, frontend, SOW, context, status, lifecycle, receipt, or Task Management surface was written by N0. N0 does not confer application, pointer, routing, activation, reliance, lifecycle, implementation, or release authority.
