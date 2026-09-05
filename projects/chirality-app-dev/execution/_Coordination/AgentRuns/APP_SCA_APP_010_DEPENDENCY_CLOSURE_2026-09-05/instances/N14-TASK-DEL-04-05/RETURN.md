# RETURN — N14-TASK-DEL-04-05 (TASK + dependency-extract, D-APP-110 decompose)

**STATUS:** PASS

- **RunID:** `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` · **Node:** N14 · **Parent:** HELP_HUMAN.
- **Basis:** HEAD `7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985` (equals the brief's pin); carrier identities matched the brief pre-write (`Dependencies.csv` `a850ded5…06ae7`, `_DEPENDENCIES.md` `35b90b2b…21152`); decomposition found at the pinned identity `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`.
- **Authority read:** D-APP-110 ruling, `AMENDMENT_v1.3_SCC_DECOMPOSE.md`, `SCC_DECOMPOSE_RULINGS.csv` (row SD-001), precedent `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z` and rows `DEP-03-01-005` / `DEP-05-02-011`.

## Task A — re-targeted: `DEP-04-05-010` (SD-001)

- `TargetType=DOCUMENT`; `TargetPackageID` and `TargetDeliverableID` cleared; `TargetRefID=DEL-02-05-KEY_STATUS_CONTRACT`; `TargetName=Stored key-status and safe key-source contract (ui, env, none; UI safeStorage precedence)`; `TargetLocation=execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/ScopeOfWork.md#CLM-003`; `LastSeen=2026-09-05`; `Notes` appended with the brief's decompose clause (GraphEdge `DEL-04-05->DEL-02-05`, ContractAnchor as given in the workbook, previous target `DEL-02-05`).
- Contract anchor verified before writing: DEL-02-05 `ScopeOfWork.md` line 112 `### CLM-003 — Attributes` (rows `Key status values | ui, env, none` and `API key precedence`), and CLM-010 `DEL-02-05-R03` at line 231.
- All other fields unchanged (`DependencyClass`, `AnchorType`, `Direction=UPSTREAM`, `DependencyType=INTERFACE`, `Statement`, `EvidenceFile`, `SourceRef`, `EvidenceQuote`, `Explicitness`, maturities, `SatisfactionStatus=TBD`, `Confidence`, `Origin`, `FirstSeen`, `Status=ACTIVE`).

## Task B — Notes-updated: none

The carrier holds no other D-APP-109 rows; no `RESOLVED 2026-09-05` note was appended.

## Post-write identities

| File | SHA-256 |
|---|---|
| `Dependencies.csv` | `aec128ecb0369228520327eafe46a609facb6df3ec360bc5e3f3dcb42db2776a` |
| `_DEPENDENCIES.md` | `d7ddb6c94f5366535362617891d2f0d41475ccd5e9229f1d9880aca7b1c1e695` |
| `_run_records/TASK_RUN_2026-09-05_1013.md` | `eabddb332416c00fc84a4676880e30842d6a4833e09d2482ccdb5c933f20bf2d` |

## Validator results (Function 5)

- `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py <carrier>/Dependencies.csv` — VALID; 29 columns (29 required + 0 extension); 13 data rows.
- `python3 tools/validation/validate_enum.py TARGET_TYPE DOCUMENT` — VALID.
- `DependencyID` unique (13/13), ID order kept; exactly one ACTIVE `IMPLEMENTS_NODE`; `TargetDeliverableID` empty on every DOCUMENT row.
- `git diff --check` clean; `git diff --numstat`: `Dependencies.csv` 1 added / 1 removed (the single re-targeted line), `_DEPENDENCIES.md` 20 / 2. LF only, no trailing whitespace, final newline on all written files.
- Counts unchanged: ACTIVE 11 / RETIRED 2; ACTIVE ANCHOR 6 / EXECUTION 5; SatisfactionStatus PENDING 1 / SATISFIED 7 / TBD 3.

## `_DEPENDENCIES.md` changes

- Register-table target for `DEP-04-05-010` now `DEL-02-05-KEY_STATUS_CONTRACT`; counts line annotated (no per-target-type tally is kept, so no count changes).
- New `## Run Notes - 2026-09-05 D-APP-110 SCC decompose` section: one `DECOMPOSE under D-APP-110 (SD-001)` bullet, one Task B summary bullet, decomposition identity, anchor check, Function 5 results.
- One `## Run History` row: `2026-09-05T10:13-0600 (D-APP-110 decompose) | UPDATE | CONSERVATIVE | found at the pinned identity SHA-256 c7c05169…771e61 | none; … | ANCHOR=6; EXECUTION=5; ACTIVE=11; RETIRED=2`.
- New `## Downstream Handoff Notes`: the carrier no longer holds cycle-participating rows; every row gates per its `SatisfactionStatus`.

## Files written (nothing else)

- `<carrier>/Dependencies.csv`, `<carrier>/_DEPENDENCIES.md`, `<carrier>/_run_records/TASK_RUN_2026-09-05_1013.md`, `instances/N14-TASK-DEL-04-05/RETURN.md`, `instances/N14-TASK-DEL-04-05/STATUS.json`. Helper scripts live only in a private scratchpad subfolder.

## Notes for the parent

- ASSUMPTION recorded in the run record: `CHIRALITY_INSTRUCTION_ROOT` was unset in this runtime; `INSTRUCTION_ROOT` resolved to `REPO_ROOT` because the sealed brief names this checkout as the tree owning `agents/`, `skills/`, and `tools/`.
- Sibling N14 carriers (DEL-02-04, DEL-02-05, DEL-03-02, DEL-08-01, DEL-08-04) and packet files showed as modified in the working tree during this run; they were not touched by this instance.
- No state-changing git command, no network, no delegation. Attribution: Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (D-APP-110 decompose), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
