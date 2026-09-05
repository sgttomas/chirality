# Decision Log

`AUDIT = SCC-DECOMPOSE-SCA-APP-010` (1034, after the D-APP-110 decompose move)

## DEC-001 — Write-root override and no pointer move

The sealed brief overrides `AGENT_AUDIT_DEP_CLOSURE.md`'s default `_Evaluation/DepClosure/` tool root and its `_LATEST.md` pointer-update step. This snapshot is written only under `projects/chirality-app-dev/execution/_Reconciliation/DepClosure/CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034/`; control output only to `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N16-AUDIT-DEP-CLOSURE/RETURN.md` and `STATUS.json`. No `_LATEST.md` anywhere was created or moved (`_Reconciliation/DepClosure/_LATEST.md` still names `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`); acceptance of any DepClosure snapshot is an owner act in this loop. No `_Evaluation/DepClosure/` path was created, and `tools/scaffolding/scaffold_tool_root.sh`, `create_snapshot_folder.sh`, and `update_latest_pointer.sh` were not invoked (the brief fixes the folder-name form and forbids the pointer move). The timestamp `2026-09-05_1034` is the `date +%Y-%m-%d_%H%M` value taken at the start of the run. The 0807 and 0518 snapshots and the `SCC_SAFE_MOVES_001` precedent were read and left byte-identical.

## DEC-002 — Registered analyzer identity and single invocation

Invocation (from the repository root, exactly once, with `PYTHONDONTWRITEBYTECODE=1`; no probe or dry run preceded it):

```text
PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py projects/chirality-app-dev/execution --output-dir projects/chirality-app-dev/execution/_Reconciliation/DepClosure/CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034/Evidence
```

Analyzer SHA-256 `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91` (matches the brief's expected identity and the copies preserved by the 0518 and 0807 runs); an exact copy is preserved as `analyze_closure.py` and its stdout as `Evidence/analyzer_stdout.txt`. No `__pycache__` was left under `tools/coordination/`. The parent's own live check (`Evidence/fanin_live_v1.3/`) is a separate earlier invocation by HELP_HUMAN, not by this audit; this audit compares against it and does not count it.

## DEC-003 — Supplement script, its outputs, and LF normalization

The analyzer does not emit an edge list, `cycles_sample.csv`, or any delta. A deterministic supplement (`n16_supplement.py`, SHA-256 `cf61f8f4b2bac7f91f614c2e9e2afb63affb9e6c3f454231e228fa901527c9de`, kept in the auditor's private scratchpad subfolder per the dispatch instruction and not part of this snapshot) re-derived the graph with the analyzer's own filters (`Status=ACTIVE`, `DependencyClass=EXECUTION`, `TargetType=DELIVERABLE`, non-empty `TargetDeliverableID`, `UPSTREAM` as from -> target, `DOWNSTREAM` as target -> from) and wrote `Evidence/edge_list.csv` (0807 form: `From,To,DependencyIDs,SCCInternal`), `Evidence/cycles_sample.csv` (header only), `Evidence/scc_detail.json` (empty list), `Evidence/topological_order.csv`, `Evidence/core_checks.json`, `Evidence/delta_vs_0807.json`, `Evidence/delta_vs_baseline.json`, `Evidence/move_basis.json`, `Evidence/resolved_rows.json`, `Evidence/refreshed_registers.json`, `Evidence/fanin_agreement.json`, `Evidence/posture_checks.json`, `Evidence/schema_validation.json`, and `Evidence/normalization_lineage.json`. The supplement's counts agree with the analyzer on every shared metric (`Evidence/core_checks.json` `analyzerAgreement`, all true). The supplement was iterated three times during the run to correct its own classifier and check wording; the recorded identity is that of the final version, whose outputs are the ones in this snapshot. It read the registers, the committed basis through read-only `git show 7eb4b0c7:<path>`, the run-folder inputs named in the brief, and the 0807 and baseline evidence; it wrote nothing outside the snapshot.

The analyzer writes its CSVs with CRLF line endings and `closure_summary.json` without a final newline. After parsing, each such file was normalized to LF with a final newline to satisfy the brief's whitespace rule; parsed values are unchanged and the analyzer-emitted and normalized SHA-256 values are recorded in `Evidence/normalization_lineage.json` and `QA_Report.md`. The lineage was captured on the first supplement pass and preserved unchanged across the later passes (the files were already LF by then). `closure_summary.json` at the snapshot root is a byte copy of the normalized `Evidence/closure_summary.json`.

## DEC-004 — `orphans.csv` interpretation

The analyzer's `orphans.csv` lists deliverables with no ACTIVE deliverable-to-deliverable EXECUTION edge in either direction. All 141 active deliverable endpoints resolve, so the 4 entries are isolates, not unresolved targets, and are logged as `ISOLATED_DELIVERABLE` warnings, unchanged from the 0518 and 0807 runs. Re-targeting a row to a `DOCUMENT` node removes it from the strict graph by design; the re-targeting created no new isolate because `DEL-02-04` and `DEL-08-01` keep other strict edges.

## DEC-005 — Comparison basis for the 0807 delta

The 0807 snapshot preserves an edge list (`Evidence/edge_list.csv`) but not the registers. `HEAD` is `7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985`, the committed basis named in the brief, and deriving the strict edge set from `git show 7eb4b0c7:<path>` over all 52 registers reproduces the 0807 edge list exactly (every edge and every carrying `DependencyID`), so the basis is the 0807 register state. The edge-level delta is computed against the 0807 edge list; the row-level delta is computed by `DependencyID` against the basis for all 52 registers, comparing every field. Result: 0 rows added, 0 removed, 7 rows changed in target fields (plus `Notes`, and `LastSeen` on `DEP-04-05-010` only), 13 rows changed in `Notes` only, 0 rows otherwise changed.

## DEC-006 — Edge list derived, not emitted

Because the registered analyzer emits no edge list, this audit's `Evidence/edge_list.csv` is the supplement's derivation in the 0807 form, so that the delta against the 0807 `Evidence/edge_list.csv` is explicit and file-to-file: expected and observed, exactly the five decomposed edges removed and nothing added. The `SCCInternal` column is present for form and is empty on every row.

## DEC-007 — Reading of "no `PREREQUISITE` row changed"

Four of the thirteen resolved rows (`DEP-02-04-015`, `DEP-02-04-016`, `DEP-02-05-014`, `DEP-02-05-015`) are `PREREQUISITE` rows and changed in `Notes` only, receiving the resolved clause that D-APP-110 ruling 3 requires of every remaining D-APP-109 row. The brief's check 3 ("no `PREREQUISITE` row changed") is read, consistently with the ruling's selection rule ("every `PREREQUISITE` row stays a strict deliverable edge") and the amendment ("no `PREREQUISITE` row changed" alongside "update the `Notes` of the other D-APP-109 rows"), as: no `PREREQUISITE` row was re-targeted, retired, inverted, reclassified, or changed in any graph-bearing or target field. That holds (`Evidence/delta_vs_0807.json` `prerequisiteRowsRetargetedOrGraphChanged=0`); the four Notes-only edits are listed separately (`prerequisiteRowsNotesOnly`) so a reader who wants the stricter reading can see exactly what changed.

## DEC-008 — Canonical validator findings in unchanged registers

As in the 0518 and 0807 runs: `tools/validation/validate_dependencies_schema.py` rejects `TargetType=CODE` and `TargetType=DECISION` in `DEL-05-01` (`DEP-05-01-006`, `DEP-05-01-009`) and `DEL-05-05` (`DEP-05-05-009`, `DEP-05-05-010`). Both registers are byte-identical to the basis, outside every SCA-APP-010 and N14 write set, and the rows are not DELIVERABLE-typed, so the graph is unaffected. Calibrated as `WARNING`, not `BLOCKER` and not `SCHEMA_INVALID` exclusion, because the analyzer contract that defines edge inclusion passes the files and excluding them would silently drop `DEL-05-05`'s strict edges. All ten N14 carriers pass the canonical validator, including their new `DOCUMENT` rows.

## DEC-009 — Root-path posture

Check 5 is read as in the 0807 run: no re-targeted row introduces a Root filesystem path (all seven new `TargetLocation` values are repo-relative `ScopeOfWork.md` anchors), and Root-owned targets are carried as `EXTERNAL` with `TargetLocation=TBD`. That holds for every Root-named EXTERNAL row in the fourteen swept carriers (the thirteen of the 0807 run plus `DEL-04-05`). The two descendant-class EXTERNAL rows (`DEP-08-04-009/010`) point at the repo-relative App decomposition and pre-date SCA-APP-010; INFO. The pre-existing absolute Root path in `DEP-08-01-013` (`TargetType=DOCUMENT`) is byte-identical to the basis in every field and already on the owner slate; `WARNING` for the owner, not a defect of this pass.

## DEC-010 — Objective-relative DAG versus live register graph

The accepted SCA-APP-008 `DAG.md` (SHA-256 `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996`, verified live) and the live register graph remain distinct derivatives with opposite orientation conventions. The audit checks, as before, that no live row materializes E-018, E-020, or E-032 and that only the accepted gating orientations exist. It records that the E-018 and E-020 node pairs, which the 0807 run found enclosed by its `SCC-002`, now lie inside no live SCC; that is a consequence of the decompose move, not of any row between those pairs. No mapping between the accepted DAG's SCCs and the (now empty) live SCC set is asserted.

## DEC-011 — Verdict calibration

Closure verdict `PASS`; `RUN_STATUS = WARNINGS`. The strict active deliverable execution graph is acyclic (analyzer `scc_count = 0`, supplement Tarjan and Kahn agree), the move was applied exactly as ruled with no row retired, cut, merged, or inverted, and no new blocker or warning exists. Per the brief's check 6 and the `SCC-SAFE-MOVES-001` precedent, the closure verdict is `PASS` with the carried warnings listed. `RUN_STATUS` uses the role's own vocabulary (`OK | WARNINGS | FAILED_INPUTS`) and is `WARNINGS` because pre-existing warnings remain visible in the corpus (four isolates, two enum non-conformances, one absolute Root path), all carried from the 0518 and 0807 runs and none touched by the move. Nothing was upgraded or downgraded.

## DEC-012 — Count wording

The dispatching message corrected the count that several v1.3 documents originally gave as "twelve": thirteen other D-APP-109 rows carry the resolved clause. This audit verifies the arithmetic directly: nineteen rows were emitted under D-APP-109 (`HELD_EDGE_PROPOSALS.csv` H-001 to H-019); six of the seven re-targeted rows are among them (`DEP-02-01-010`, `DEP-02-02-022`, `DEP-02-04-017`, `DEP-02-04-018`, `DEP-02-04-019`, `DEP-06-03-014`); `DEP-04-05-010` is pre-existing; 19 - 6 = 13, and the thirteen Notes-only rows in the registers equal the `notesUpdated` sets in `Evidence/n14_postwrite_identities.json` and `carrier_work.json` (`Evidence/resolved_rows.json`). The report and this log use "thirteen" throughout. The one remaining occurrence of "twelve" in the run folder's `VALIDATION_EVIDENCE.md` (line 86) is the RW-004 repair description quoting the corrected miscount, not an uncorrected count (outside this audit's write scope; noted in `QA_Report.md`).

## DEC-013 — Alternative minimum set and necessity

`Evidence/scc_decompose/search_log.txt` (with the RW-001 repair line) records that full enumeration finds two minimum five-edge eligible sets, the alternative opening the two-node SCC from the `DEP-08-01-018` side. This audit did not re-run the exhaustive search (REVIEW_v1.3 did, and the brief does not ask for it); it verified the weaker but sufficient property that each of the five applied edges is necessary: restoring any one of them alone to the live strict graph re-creates an SCC (sizes 16, 2, 4, 9, and 2 respectively; `Evidence/move_basis.json` `eachDecomposedEdgeNecessary`). The choice between the two minimum sets is the parent's recorded rationale under the owner's directed move and is recorded here as INFO (DC-015), not adjudicated.

## DEC-014 — `CYCLE_PARTICIPATING` marker retained in superseded text

The nineteen D-APP-109 rows still carry the literal `CYCLE_PARTICIPATING` marker and the emission-time non-gating sentence in `Notes`; N14 appended the `DECOMPOSE` or `RESOLVED` clause rather than rewriting history, as its brief required. Every such marker is followed by a clause naming D-APP-110 (`Evidence/resolved_rows.json` `cycleParticipatingRowsWithoutDAPP110Supersession=[]`), and no row in the corpus carries an unsuperseded non-gating clause. The 0807 run's statement "the nineteen are exactly the `CYCLE_PARTICIPATING` rows in the corpus" therefore still holds as a marker count, while no row is non-gating. Recorded as INFO (DC-016); no register change proposed.

## DEC-015 — Carried review finding RW-002

`REVIEW_v1.3.md` RW-002 (MINOR; carried by the dispatch) notes pre-existing `Notes` sentences in `DEP-02-04-017/018/019` that now read against the live `TargetRefID` and the appended `DECOMPOSE` clause. This audit confirms the observation (the sentences are present and the appended clause supersedes them) and records it as INFO (DC-014) with no graph effect and no repair; the exact repair is RW-002's, for a later authorized Notes refresh.

## DEC-016 — Working-tree observations outside the audit's inputs

`git status` shows, beyond the ten carriers' registers and indexes and their ten new `_run_records/TASK_RUN_2026-09-05_*.md` files, the run folder's v1.3 files (amendment, workbook, `Evidence/scc_decompose/*`, `Evidence/n14_postwrite_identities.json`, `Evidence/fanin_live_v1.3/*`, `Evidence/validation/v1.3/`, `REVIEW_v1.3.md`, the N14/N15/N16 instance folders, and HELP_HUMAN's edits to `ORCHESTRATION_PLAN.md`, `VALIDATION_EVIDENCE.md`, `HANDOFF_STATE.md`), the D-APP-110 ruling record, and one `_REGISTER.md` row. None of these is an analyzer input; of them this audit read only the files the brief and the dispatch name. `tools/validation/__pycache__/` exists with timestamps from 2026-09-04, before this run, is gitignored, and was not written by this audit (the canonical validator was invoked with `PYTHONDONTWRITEBYTECODE=1`).
