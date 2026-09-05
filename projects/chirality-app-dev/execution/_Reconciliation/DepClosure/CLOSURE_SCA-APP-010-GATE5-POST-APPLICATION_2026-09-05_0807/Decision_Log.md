# Decision Log

`AUDIT = SCA-APP-010-GATE5-POST-APPLICATION` (second run, 0807, post D-APP-109 emission)

## DEC-001 — Write-root override and no pointer move

The sealed brief overrides `AGENT_AUDIT_DEP_CLOSURE.md`'s default `_Evaluation/DepClosure/` tool root and its `_LATEST.md` pointer-update step. This snapshot is written only under `projects/chirality-app-dev/execution/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0807/`; control output only to `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N11-AUDIT-DEP-CLOSURE/RETURN.md` and `STATUS.json`. No `_LATEST.md` anywhere was created or moved (`_Reconciliation/DepClosure/_LATEST.md` still names `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`); acceptance of any DepClosure snapshot is an owner act in this loop. No `_Evaluation/DepClosure/` path was created, and `tools/scaffolding/scaffold_tool_root.sh`, `create_snapshot_folder.sh`, and `update_latest_pointer.sh` were not invoked (the brief fixes the exact folder name and forbids the pointer move). The 0518 snapshot was read and left byte-identical.

## DEC-002 — Registered analyzer identity and single invocation

Invocation (from the repository root, exactly once, with `PYTHONDONTWRITEBYTECODE=1`; no probe or dry run preceded it):

```text
PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py projects/chirality-app-dev/execution --output-dir projects/chirality-app-dev/execution/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0807/Evidence
```

Analyzer SHA-256 `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91` (matches the brief's expected identity and the copy preserved by the 0518 run); an exact copy is preserved as `analyze_closure.py` and its stdout as `Evidence/analyzer_stdout.txt`. No `__pycache__` was left under `tools/coordination/`.

## DEC-003 — Supplement script, its outputs, and LF normalization

The analyzer does not emit `cycles_sample.csv`, an edge list, or any delta. A deterministic supplement (`n11_supplement.py`, SHA-256 `520d4a100a46867ae4a447bf6e99c8d9df8a8d3a8e90352cbed6a8ad66747063`, kept in the auditor's private scratchpad subfolder per the dispatch instruction and not part of this snapshot) re-derived the graph with the analyzer's own filters (`Status=ACTIVE`, `DependencyClass=EXECUTION`, `TargetType=DELIVERABLE`, `UPSTREAM` as from -> target, `DOWNSTREAM` as target -> from) and wrote `Evidence/edge_list.csv`, `Evidence/cycles_sample.csv`, `Evidence/scc_detail.json`, `Evidence/core_checks.json`, `Evidence/delta_vs_0518.json`, `Evidence/delta_vs_baseline.json`, `Evidence/fanin_agreement.json`, `Evidence/emitted_rows.json`, `Evidence/refreshed_registers.json`, `Evidence/posture_checks.json`, `Evidence/schema_validation.json`, and `Evidence/normalization_lineage.json`. The supplement's counts agree with the analyzer on every shared metric. A second private helper (`n11_cycle_participation.py`, SHA-256 `55d9274d26b1178cb77232f8282f6896d697d02ac44eb04f0190d2b630644d16`, same scratchpad subfolder) derived `Evidence/cycle_edge_participation.csv` (cycles containing each SCC-internal edge) from the snapshot's own `cycles_sample.csv` and `edge_list.csv` for the report's structural observation.

The analyzer writes its CSVs with CRLF line endings and `closure_summary.json` without a final newline. After parsing, each such file was normalized to LF with a final newline to satisfy the brief's whitespace rule; parsed values are unchanged and the analyzer-emitted and normalized SHA-256 values are recorded in `Evidence/normalization_lineage.json` and `QA_Report.md`. `closure_summary.json` at the snapshot root is a byte copy of the normalized `Evidence/closure_summary.json`.

## DEC-004 — `orphans.csv` interpretation

The analyzer's `orphans.csv` lists deliverables with no ACTIVE deliverable-to-deliverable EXECUTION edge in either direction. All 148 active deliverable endpoints resolve, so the 4 entries are isolates, not unresolved targets, and are logged as `ISOLATED_DELIVERABLE` warnings, unchanged from the 0518 run.

## DEC-005 — Comparison basis for the 0518 delta

The 0518 snapshot preserves an edge list (`Evidence/edge_list.csv`) but not the registers. `HEAD` is `f38f1448675b8e9f40f33932a11b7ffa4126fe69`, the committed basis named in the brief, and the nine N9 carriers' `HEAD` registers hash to the identities pinned in the 0518 `Brief.md` (verified with read-only `git show HEAD:<path>`), so `HEAD` is the 0518 register state. The edge-level delta is computed against the 0518 edge list; the row-level delta is computed by `DependencyID` against `HEAD` for all 52 registers, comparing the graph-bearing fields (`FromDeliverableID`, `DependencyClass`, `Direction`, `TargetType`, `TargetDeliverableID`, `Status`) and every other field separately. Result: 19 rows added, 0 removed, 0 changed in any field.

## DEC-006 — SCC labels

The analyzer numbers SCCs in Tarjan discovery order over sorted nodes; in this run `SCC-001` is the two-node component `DEL-06-03;DEL-08-01` and `SCC-002` is the twenty-node component. The fan-in simulation the owner accepted uses the same labels. The former nine-node component was labelled `SCC-001` in the baseline and the 0518 run, and the emitted rows' `Notes` refer to the twenty-node component as "the enlarged SCC-001". This log records the mapping rather than renaming anything: former `SCC-001` (nine nodes) is a proper subset of live `SCC-002` (twenty nodes); live `SCC-001` is new. The report uses the analyzer's labels throughout and says "former nine-node SCC" where the older name is meant.

## DEC-007 — Cycle enumeration method and bound

Elementary cycles were enumerated inside each SCC with Johnson's algorithm in deterministic order (start vertices in sorted order; successors in sorted order), recording at most `MAX_CYCLES=10000` cycles and counting up to a ceiling of 1,000,000. Both bounds were far from reached: the two-node SCC has exactly 1 elementary cycle and the twenty-node SCC exactly 64, so `Evidence/cycles_sample.csv` is the complete set, not a sample. An independent depth-first enumeration by a different method (cycles keyed by their minimum-rank vertex) over `Evidence/edge_list.csv` reproduced both counts and both length histograms. Sizes are reported so that the twenty-node component gets human attention (hairball caution, `docs/CYCLE_DRIVEN_RESOLUTION.md` section 3); no cut, merge, inversion, or linearization is proposed or performed.

## DEC-008 — Canonical validator findings in unchanged registers

As in the 0518 run: `tools/validation/validate_dependencies_schema.py` rejects `TargetType=CODE` and `TargetType=DECISION` in `DEL-05-01` (`DEP-05-01-006`, `DEP-05-01-009`) and `DEL-05-05` (`DEP-05-05-009`, `DEP-05-05-010`). Both registers are byte-identical to `HEAD`, outside every SCA-APP-010 write set, and the rows are not DELIVERABLE-typed, so the graph is unaffected. Calibrated as `WARNING`, not `BLOCKER` and not `SCHEMA_INVALID` exclusion, because the analyzer contract that defines edge inclusion passes the files and excluding them would silently drop `DEL-05-05` from the twenty-node SCC.

## DEC-009 — Root-path posture

Check 6 is read as in the 0518 run: no emitted row introduces a Root filesystem path, and Root-owned targets are carried as `EXTERNAL` with `TargetLocation=TBD`. That holds for every Root-named EXTERNAL row in the thirteen carriers. The two descendant-class EXTERNAL rows (`DEP-08-04-009/010`) point at the repo-relative App decomposition and pre-date SCA-APP-010; INFO. The pre-existing absolute Root path in `DEP-08-01-013` (`TargetType=DOCUMENT`) is byte-identical to `HEAD` and already on the owner slate; `WARNING` for the owner, not a defect of this pass.

## DEC-010 — Objective-relative DAG versus live register graph

The accepted SCA-APP-008 `DAG.md` (SHA-256 `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996`, verified live) and the live register graph remain distinct derivatives with opposite orientation conventions. The audit checks, as before, that no live row materializes E-018, E-020, or E-032 and that only the accepted gating orientations exist. It additionally records that the E-018 and E-020 node pairs now lie inside live `SCC-002`, which is a consequence of the emitted edges (for example `DEL-02-02 -> DEL-05-04`, `DEL-02-02 -> DEL-08-04`, `DEL-02-02 -> DEL-08-05`), not of any new row between those pairs. This is reported as INFO for the owner's resolution packet; the live SCCs are not mapped onto the accepted objective-relative SCCs and no move is made.

## DEC-011 — Verdict calibration

`WARNINGS`. The recorded SCC change is an owner-accepted transaction under D-APP-109 with every cycle-participating row explicitly non-gating; per the brief and `docs/CYCLE_DRIVEN_RESOLUTION.md` it is WARNING-class with resolution routed to the cycle-resolution workflow, not a blocker. Schema columns, anchors, evidence, endpoint resolution, register identities, emitted-row conformance, fan-in agreement, descendant classes, Root-target posture, and the `DEP-08-01-013` pointer all pass. The pre-existing isolates, the two enum non-conformances, and the pre-existing Root path remain visible warnings. No blocking result existed to upgrade or downgrade.

## DEC-012 — Brief typo

The sealed brief's twenty-node list in Required check 3 omits `DEL-08-05`; the dispatching message identified this as a known typo and named `Evidence/fanin_simulation_v1/scc_summary.csv` as authoritative. The observed twenty-node SCC includes `DEL-08-05` and equals the simulation file exactly; the brief's nineteen-name list is therefore treated as a transcription slip, not as a discrepancy in the graph.
