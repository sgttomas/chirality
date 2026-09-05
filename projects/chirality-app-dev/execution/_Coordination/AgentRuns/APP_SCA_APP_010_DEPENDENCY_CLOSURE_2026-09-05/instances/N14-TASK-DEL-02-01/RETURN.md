# RETURN — N14-TASK-DEL-02-01 — DEP-02-01-010 decomposed under D-APP-110 (SD-002)

## Status

`PASS`. Workbook row SD-002 (`DEP-02-01-010`, DEL-02-01 -> DEL-02-04, UPSTREAM INTERFACE) is re-targeted to the DOCUMENT contract node `DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1` at the DEL-02-04 Scope of Work anchor with the decompose clause appended to `Notes`; every other row byte-identical; `_DEPENDENCIES.md` reconciled; Function 5 passes; nothing outside the sealed write set was touched. Task B: none for this carrier.

## Gate

- HEAD `7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985` (equal to the brief's required commit); the carrier's register carried no diff against it before this run.
- Pre-image `Dependencies.csv` `8d5315713a86732e44b4a9287e8632be03347d50ceb1d2ed7889c2b90cc8883e` — matched.
- Pre-image `_DEPENDENCIES.md` `f6a50a4513cc2d5895d81fe93a4b9ee45e43714f1a16234adf7c188b52e2c517` — matched.
- Contract anchor: DEL-02-04 `ScopeOfWork.md` (SHA-256 `2ebfe14aa3bf354b79111c5e0d4bc81b3e10e8292195d8c8aad5464a7f99cc8c`, read-only) carries `## SCA-APP-010 Gate-5 Current Contract (Controlling)` at L68 and acceptance obligation 1 (additive v1 fields under the existing schema string) at L99 — present.
- Decomposition SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` — FOUND at the pinned identity; DEL-02-04 applied row L310.

## Re-targeted (Task A)

| DependencyID | Ruling | Prior strict edge | New TargetType / TargetRefID | TargetLocation | Unchanged |
|---|---|---|---|---|---|
| `DEP-02-01-010` | SD-002 | DEL-02-01 -> DEL-02-04 (DELIVERABLE `DEL-02-04`, PKG-02) | DOCUMENT `DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1` "Additive v1 workspace-state field contract (per-view widths, expand state, chat annotations, known folders, chat rung, declined triggers)" | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` | class, direction, type, Statement, evidence, quote, EXPLICIT, SEMANTIC_READY, TBD, TBD, HIGH, EXTRACTED, FirstSeen, ACTIVE |

`TargetPackageID` and `TargetDeliverableID` cleared; `LastSeen=2026-09-05`; `Notes` = prior text verbatim + ` DECOMPOSE 2026-09-05 under D-APP-110 (SD-002): replaced the coarse deliverable edge DEL-02-01->DEL-02-04 with the document-scoped contract DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 (DEL-02-04 \`ScopeOfWork.md\` SCA-APP-010 Gate-5 Current Contract, acceptance obligation 1 (additive v1 fields under the existing schema string) and applied row L310 outputs); the deliverable relation to DEL-02-04 is preserved here as evidence; the strict deliverable graph is acyclic after the move (docs/CYCLE_DRIVEN_RESOLUTION.md section 2.3).`

## Notes-updated (Task B)

None (the brief lists none; `DEP-02-01-010` was this carrier's only D-APP-109 emission and it is the re-targeted row).

## Post-write identities

- `Dependencies.csv`: `b3fcca9e2ab6e5ee288a80fbf7e1b8f5869030b76edbb801070c27088808f2b1` (14 rows; header and 13 other rows byte-identical to the pre-image; only the `DEP-02-01-010` line differs from `HEAD`)
- `_DEPENDENCIES.md`: `58c4a9b24432d8b5af18015cefa7a6205c7b26ba881633ddbda11c44304f39f5`
- Run record: `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-01_Desktop_Shell_and_Matrix_Navigation/_run_records/TASK_RUN_2026-09-05_1014.md` — `eae0fd78aaa82bf102247732f812375b708e7b50582027abad4b5d25e540b68b`

## Census

Unchanged: 14 total / 14 ACTIVE / 0 RETIRED / 4 ANCHOR / 10 EXECUTION. Satisfaction 9 TBD / 4 NOT_APPLICABLE / 1 PENDING. Types INTERFACE 6, OTHER 4, HANDOVER 2, PREREQUISITE 1, CONSTRAINT 1. Target types DELIVERABLE 6 (was 7), DOCUMENT 1 (was 0), REQUIREMENT 3, UNKNOWN 2, PACKAGE 1, EXTERNAL 1; `_DEPENDENCIES.md` keeps no target-type tally, so no count in that file changed.

## Function 5

- `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py`: `VALID` — 29 columns (29 required + 0 extension), 14 data rows.
- `python3 tools/validation/validate_enum.py`: `TARGET_TYPE DOCUMENT` VALID (the changed value); the other nine enum values on the row re-checked VALID; 0 invalid.
- Exactly one ACTIVE `IMPLEMENTS_NODE` (`DEP-02-01-001`); unique, ascending `DependencyID`s; `FromDeliverableID=DEL-02-01` on every row; every ACTIVE row has `EvidenceFile` + `SourceRef`; `Status=CANDIDATE` absent; DOCUMENT row has empty `TargetDeliverableID` and `TargetPackageID`.
- `git diff --check`: clean. LF only, no trailing whitespace, final newline on both register files.
- [WARNING] PROJECT_ID_FORMAT_PROFILE (unchanged from prior runs): the generic three-digit `validate_id_format.sh` profile rejects the accepted App two-digit IDs; no ID changed.

## `_DEPENDENCIES.md` changes

Compact-register row for `DEP-02-01-010` now `DOCUMENT DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 Additive v1 workspace-state field contract (...)` (DEL-03-01 / DEL-05-02 precedent form); new Run Notes subsection `### 2026-09-05 D-APP-110 decompose of DEP-02-01-010 (UPDATE)` with the `DECOMPOSE under D-APP-110 (SD-002): DEP-02-01-010 now targets DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1` bullet and the Task B "none required" bullet; Run History row `2026-09-05T10:14-0600 (D-APP-110 decompose)` appended (`ANCHOR=4; EXECUTION=10; TOTAL=14`); Downstream Handoff Notes rewritten: no cycle-participating row, every row gates per its `SatisfactionStatus`, DEP-02-04-017 (SD-003) cross-reference, N16 snapshot as the authoritative post-move record. Summary and Lifecycle Summary unchanged; dated history bullets unchanged.

## Not written

`_CONTEXT.md`, `_STATUS.md`, `MEMORY.md`, `ScopeOfWork.md`, `_REFERENCES.md`, the DEL-02-04 Scope of Work (opened read-only), every other carrier, every other instance folder, the workbook. No network; no state-changing git command; no descendant launched.

## Conventions and notes

- ASSUMPTION: `CHIRALITY_INSTRUCTION_ROOT` unset; the sealed-brief repository root served as instruction root (as in N1, N3, and N9).
- The row's prior `CYCLE_PARTICIPATING` clause is preserved verbatim as dated history; the appended `DECOMPOSE` clause supersedes it.
- HGD-1, HGD-2, HGD-3 and FC-1 to FC-3 unchanged and still on the owner slate. Acceptance of the N16 closure snapshot as the DepClosure pointer remains a separate owner act.

## Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (D-APP-110 decompose), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
