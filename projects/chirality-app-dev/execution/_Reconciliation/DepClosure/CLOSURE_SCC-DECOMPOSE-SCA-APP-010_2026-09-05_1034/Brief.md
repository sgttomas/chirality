# Brief — AUDIT_DEP_CLOSURE `SCC-DECOMPOSE-SCA-APP-010` (after the D-APP-110 decompose move)

## Sealed brief (verbatim)

Source: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N16-AUDIT-DEP-CLOSURE/LAUNCH_BRIEF.md`

# Sealed Brief — N16-AUDIT-DEP-CLOSURE — AUDIT_DEP_CLOSURE `SCC-DECOMPOSE-SCA-APP-010` after the D-APP-110 move

- **RunID:** `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` · **Node:** N16 · **InstanceID:** `N16-AUDIT-DEP-CLOSURE` · **Parent:** HELP_HUMAN (Agent 0) · **Authority:** owner ruling D-APP-110 (`execution/_Coordination/_DECISIONS/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md`) and `AMENDMENT_v1.3_SCC_DECOMPOSE.md` in this run folder.
- **Role:** `AUDIT_DEP_CLOSURE` (named dedicated Agent 2, D-GOV-13); read `agents/AGENT_AUDIT_DEP_CLOSURE.md` and `docs/CYCLE_DRIVEN_RESOLUTION.md` completely first; then the precedent `execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/Dependency_Closure_Report.md` (the "Move Basis" form this report must follow) and the 0807 snapshot of this run for continuity of form.
- **Repository root:** `/Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2`; branch `claude/sca-app-010-dependency-closure`; committed basis `7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985` plus the uncommitted N13/N14 working tree. No network; no state-changing git command; **no delegation**; read-only on every deliverable; helper scripts only in a private subfolder of your scratchpad. Role not mechanically enforced.
- **Registers to consume and identify explicitly:** `Evidence/n14_postwrite_identities.json` in this run folder (the ten carriers changed by N14, with SHA-256 of `Dependencies.csv` and `_DEPENDENCIES.md`); the move workbook `SCC_DECOMPOSE_RULINGS.csv`; `Evidence/scc_decompose/decompose_choice.json` and `search_log.txt`; the independent review `REVIEW_v1.3.md`.
- **Prior state:** the 0807 snapshot `execution/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0807/` (two SCCs, 124 strict edges) and the pre-extraction baseline `Evidence/baseline_closure/`.
- **RunLabel:** `SCC-DECOMPOSE-SCA-APP-010`. **Snapshot:** `execution/_Reconciliation/DepClosure/CLOSURE_SCC-DECOMPOSE-SCA-APP-010_<YYYY-MM-DD_HHMM>/**` (use `date +%Y-%m-%d_%H%M` at start). **ExecutionRoot:** `projects/chirality-app-dev/execution`; `SCOPE=ALL`; `FilterActiveOnly=true`; `NormalizeIds=true`.
- **Do not move any `_LATEST.md`.** Write only under the snapshot folder plus `instances/N16-AUDIT-DEP-CLOSURE/RETURN.md` and `STATUS.json`. Record the write-root override and the no-pointer-move rule in `Decision_Log.md`. LF, no trailing whitespace, final newline; convert the analyzer's CSV outputs to LF before manifesting; `MANIFEST.sha256` over every file in the snapshot.

## Required checks

1. Run the registered analyzer exactly once (`PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py projects/chirality-app-dev/execution --output-dir <snapshot>/Evidence`); record its SHA-256 (expected `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91`) and copy it to `<snapshot>/analyze_closure.py`.
2. Schema and endpoint checks as the role requires (the two pre-existing legacy `TargetType` failures in DEL-05-01 and DEL-05-05 are carried, unchanged).
3. **Move basis.** Report, in the `SCC-SAFE-MOVES-001` form, the seven rows decomposed from strict deliverable edges into document-scoped contract targets (`SCC_DECOMPOSE_RULINGS.csv`: `DependencyID`, prior strict edge, new `DOCUMENT` target), confirm each is `ACTIVE` with `TargetType=DOCUMENT`, empty `TargetDeliverableID`, the workbook's `TargetRefID` and `TargetLocation`, and a `Notes` clause naming D-APP-110; confirm no row was retired, cut, merged, or inverted and no `PREREQUISITE` row changed (diff every register against `git show 7eb4b0c7:<path>`).
4. **Closure.** Expected: strict active deliverable execution graph `scc_count = 0`, 48 nodes, 119 strict edges (124 minus five), `scc_summary.csv` header only, bidirectional pairs as the analyzer reports (state them), isolates and hubs as the role requires. Compare with the 0807 snapshot and the baseline; state that the strict graph is acyclic by construction after the move and that the thirteen other D-APP-109 rows are now strict edges gating per their `SatisfactionStatus` (their `Notes` carry the resolved clause).
5. Posture checks as in the 0807 run (E-018/E-020/E-032; descendant classes; Root-owned targets `EXTERNAL`/`TBD`; `DEP-08-01-013` unchanged).
6. Verdict `PASS`, `WARNINGS`, or `BLOCKER` with evidence; never upgrade. If the strict graph is acyclic and no new blocker exists, the verdict follows the precedent (`PASS` on closure with carried warnings listed).

## Outputs

`Brief.md` (verbatim plus normalized summary), `RUN_SUMMARY.md`, `QA_Report.md`, `Decision_Log.md`, `Dependency_Closure_Report.md` (with "Verdict", "Move Basis", "Metrics", and "Not claimed" sections in the precedent's form), `Dependency_Closure_IssueLog.csv`, `closure_summary.json`, `analyze_closure.py`, `Evidence/*` (LF), `MANIFEST.sha256`; `instances/N16-AUDIT-DEP-CLOSURE/RETURN.md` and `STATUS.json`. Attribution in `RUN_SUMMARY.md`: "Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as AUDIT_DEP_CLOSURE, dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched". State plainly that acceptance of this snapshot as the loop's DepClosure pointer is an owner act and that this audit grants no implementation, activation, or release authority.

## Dispatch note carried with the brief

The dispatching message from HELP_HUMAN restated the brief's constraints and added these particulars, which this audit follows:

- The committed basis is `7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985` plus the uncommitted N13/N14/N15 working tree.
- The registered analyzer emits no edge list; the strict edge set is derived from the registers exactly as the 0807 snapshot derived it (`Status=ACTIVE`, `DependencyClass=EXECUTION`, `TargetType=DELIVERABLE`, non-empty `TargetDeliverableID`; `UPSTREAM` gives From -> Target, `DOWNSTREAM` gives Target -> From) and written as `Evidence/edge_list.csv` in the 0807 form, so the delta against the 0807 `Evidence/edge_list.csv` is explicit: expected exactly the five decomposed edges removed and nothing added.
- Inputs now available beyond the sealed brief's list: `REVIEW_v1.3.md` (PASS, 0 BLOCKER / 0 MAJOR / 4 MINOR; its RW-001, RW-003, and RW-004 were repaired by HELP_HUMAN before this dispatch and RW-002 is carried), `Evidence/scc_decompose/*` (`search_log.txt` now records two minimum sets on full enumeration), and `Evidence/fanin_live_v1.3/` (the parent's own live analyzer check).
- Count wording: thirteen (not twelve) other D-APP-109 rows carry the resolved clause; nineteen rows were emitted under D-APP-109 and six of the seven re-targeted rows are among them, `DEP-04-05-010` being pre-existing.
- Every written file LF, no trailing whitespace, final newline; the analyzer's CSV outputs converted to LF before manifesting; `MANIFEST.sha256` over every file in the snapshot, generated last.

## Normalized summary

- Audit name: `SCC-DECOMPOSE-SCA-APP-010`; RunID `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, node N16, instance `N16-AUDIT-DEP-CLOSURE`; parent HELP_HUMAN (Agent 0); authority owner ruling D-APP-110 and `AMENDMENT_v1.3_SCC_DECOMPOSE.md`.
- Role: `AUDIT_DEP_CLOSURE`, named dedicated Agent 2 (D-GOV-13); no delegation; read-only on every deliverable; role not mechanically enforced.
- Basis: committed `7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985` on branch `claude/sca-app-010-dependency-closure` (verified equal to `HEAD` at run time) plus the uncommitted N13/N14/N15 working tree; the ten N14 carriers' register, index, and run-record identities are pinned in `Evidence/n14_postwrite_identities.json` and verified in `Evidence/refreshed_registers.json`.
- Inputs: `ExecutionRoot=projects/chirality-app-dev/execution`, `Scope=ALL`, `FilterActiveOnly=true`, `NormalizeIds=true`, `HUB_THRESHOLD=20` (analyzer default), `MAX_CYCLES=10000` (role default; not reached, no SCC exists).
- Prior state: the 0807 snapshot `_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0807/` (edge-level delta against its `Evidence/edge_list.csv`; row-level delta against the committed basis, which carries the 0807 registers), the pre-extraction baseline `_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/Evidence/baseline_closure/`, and the parent's live check `Evidence/fanin_live_v1.3/`.
- Move inputs: `SCC_DECOMPOSE_RULINGS.csv` (seven rows SD-001 to SD-007), `Evidence/scc_decompose/decompose_choice.json` and `search_log.txt`, `REVIEW_v1.3.md`.
- Method: one registered-analyzer invocation (`tools/coordination/analyze_dep_closure.py`, SHA-256 `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91`); independent re-derivation of the strict edge set, Tarjan SCC detection, and a Kahn topological sort as the acyclicity witness; edge-level delta against the 0807 edge list; row-level diff of all 52 registers against `git show 7eb4b0c7:<path>`; verification of the seven workbook rows and the thirteen resolved rows; ten-carrier identity verification; comparison with the parent's live fan-in check; canonical v3.1 validation of every register; the posture checks of the 0807 run.
- Content write root (override of the generic `_Evaluation/DepClosure/` root): this snapshot only, `_Reconciliation/DepClosure/CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034/**`.
- Control write root: `_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N16-AUDIT-DEP-CLOSURE/{RETURN.md,STATUS.json}` only.
- Prohibited: any `_LATEST.md` move, creation of `_Evaluation/DepClosure/`, modification of any register, deliverable file, decomposition, prior snapshot, `docs/**`, or Root surface, delegation, network, state-changing Git commands, and any proposed or performed cut, merge, inversion, or linearization.
- Return: `PASS`, `WARNINGS`, or `BLOCKER` with evidence; a blocking result is never upgraded; if the strict graph is acyclic and no new blocker exists, `PASS` on closure with carried warnings listed, as in the precedent.
