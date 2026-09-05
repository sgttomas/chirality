# Decision Log

`AUDIT = SCA-APP-010-GATE5-POST-APPLICATION`

## DEC-001 — Human override of the generic tool root; no pointer move

The sealed brief overrides `AGENT_AUDIT_DEP_CLOSURE.md`'s default `_Evaluation/DepClosure/` tool root and its `_LATEST.md` pointer-update step. This snapshot is written only under `projects/chirality-app-dev/execution/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0518/`; control output only to `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N4-AUDIT-DEP-CLOSURE/RETURN.md` and `STATUS.json`. `_Reconciliation/DepClosure/_LATEST.md` still names `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z` and was not touched; acceptance of this snapshot is an owner act. No `_Evaluation/DepClosure/` path was created, and `tools/scaffolding/scaffold_tool_root.sh`, `create_snapshot_folder.sh`, and `update_latest_pointer.sh` were not invoked (the brief fixes the exact folder name and forbids the pointer move).

## DEC-002 — Registered analyzer identity and single output-producing invocation

Invocation (from the repository root, exactly once):

```text
PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py projects/chirality-app-dev/execution --output-dir projects/chirality-app-dev/execution/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0518/Evidence
```

Analyzer SHA-256 `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91` (matches the brief's expected identity and the copy preserved by the SCA-APP-008 audit); an exact copy is preserved as `analyze_closure.py` and its stdout as `Evidence/analyzer_stdout.txt`. Disclosure: before the snapshot folder existed, the analyzer was probed once as `python3 tools/coordination/analyze_dep_closure.py --help` to confirm its CLI; the script has no `--help` handling, treated the flag as an execution root, found zero registers, and wrote nothing. That probe produced no output file and is not the audited run.

## DEC-003 — Analyzer output gaps and normalization

The analyzer does not emit `cycles_sample.csv`. A deterministic supplement (`n4_supplement.py`, SHA-256 `8ebb1a9b5849b9b8bfa6f1cbc4557bf99afdec286c8bfe8ec55810dac82de4e4`, kept in the auditor's private scratchpad per the dispatch instruction and not part of this snapshot) re-derived the graph with the analyzer's own filters (`Status=ACTIVE`, `DependencyClass=EXECUTION`, `TargetType=DELIVERABLE`, `UPSTREAM` as from -> target, `DOWNSTREAM` as target -> from), enumerated every elementary cycle inside each Tarjan SCC by depth-first search from each member restricted to higher-ranked members (bound `MAX_CYCLES=10000`, not reached), and wrote `Evidence/cycles_sample.csv` (an edge carried by two rows lists both `DependencyID`s joined by `+`), `Evidence/edge_list.csv`, `Evidence/core_checks.json`, `Evidence/delta_vs_baseline.json`, `Evidence/delta_vs_sca_app_008.json`, `Evidence/refreshed_registers.json`, `Evidence/posture_checks.json`, and `Evidence/schema_validation.json`. The supplement's counts agree with the analyzer on every shared metric.

The analyzer writes its CSVs with CRLF line endings and `closure_summary.json` without a final newline. After parsing, each such file was normalized to LF with a final newline to satisfy the brief's whitespace rule; parsed values are unchanged and the analyzer-emitted and normalized SHA-256 values are recorded in `Evidence/normalization_lineage.json` and `QA_Report.md`. `closure_summary.json` at the snapshot root is a byte copy of the normalized `Evidence/closure_summary.json`.

## DEC-004 — `orphans.csv` interpretation

The analyzer's `orphans.csv` lists deliverables with no ACTIVE deliverable-to-deliverable EXECUTION edge in either direction. All 129 active deliverable endpoints resolve, so the 4 entries are isolates, not unresolved targets, and are logged as `ISOLATED_DELIVERABLE` warnings.

## DEC-005 — Basis reconstruction for the edge-level delta

The baseline package carries summary CSVs, not an edge list. To answer whether any SCC-internal edge was added or retired, the basis graph was reconstructed from `git show HEAD:<register>` for all 52 registers (read-only Git) and compared edge by edge with the working tree. The reconstruction reproduces the baseline snapshot's nodes (46), edges (99), isolates, and SCC exactly, which confirms the baseline was taken at the basis before any register changed.

## DEC-006 — Objective-relative DAG versus live register graph

The accepted SCA-APP-008 `DAG.md` (SHA-256 verified live) and the live register graph are distinct derivatives with opposite edge orientation conventions (see the report's orientation note). E-018, E-020, and E-032 are objective feedback edges inside accepted SCCs; the audit checks that no live row materializes them and that the accepted gating orientations are the only live rows between those pairs. The live nine-node `SCC-001` is not one of the accepted objective-relative SCCs and is reported independently, without mapping it onto them and without any move.

## DEC-007 — Canonical validator findings in unchanged registers

The brief requires every discovered register to be verified against v3.1. The registered analyzer checks columns only; `tools/validation/validate_dependencies_schema.py` additionally checks the Section 6.3 enums and rejects `TargetType=CODE` and `TargetType=DECISION` in `DEL-05-01` (`DEP-05-01-006`, `DEP-05-01-009`) and `DEL-05-05` (`DEP-05-05-009`, `DEP-05-05-010`). Both registers are byte-identical to the basis, were outside the SCA-APP-010 write set, and the rows are not DELIVERABLE-typed, so the graph is unaffected. Calibrated as `WARNING` (schema hygiene routed to the owner), not `BLOCKER` and not `SCHEMA_INVALID` exclusion, because the analyzer contract that defines edge inclusion passes the files and excluding them would silently drop `DEL-05-05` from `SCC-001`.

## DEC-008 — Root-path posture

Check 7 is read as: no refreshed row introduces a Root filesystem path, and Root-owned targets are carried as `EXTERNAL` with `TargetLocation=TBD`. That holds for every EXTERNAL row naming a Root target in the thirteen carriers. The two descendant-class EXTERNAL rows (`DEP-08-04-009/010`) point at the repo-relative App decomposition and pre-date the refresh; they are recorded as INFO. The pre-existing absolute Root path in `DEP-08-01-013` (`TargetType=DOCUMENT`) is byte-identical at basis, was preserved unchanged by amendment v1.1 C.3, and is already on the owner slate (HANDOFF_STATE.md R-004); it is logged as a `WARNING` for the owner, not as a refresh defect.

## DEC-009 — Held edge proposals are non-emitted

`HELD_EDGE_PROPOSALS.csv` (H-001 to H-019) and `AMENDMENT_v1.1_N1_PREVIEWS.md` were read. The held rows were removed from the N1 post-images before the N3 writes; they are not in any live register and their edges are not in the live graph (verified). They are reported as a non-emitted owner transaction and are not audited as edges, because emitting any subset would be a cut/merge decision that `docs/CYCLE_DRIVEN_RESOLUTION.md` reserves to the human and because SCA-APP-010 requires the SCC unchanged unless separately ruled.

## DEC-010 — Verdict calibration

`WARNINGS`: schema columns, anchors, evidence, endpoint resolution, refreshed-register identity, descendant classes, accepted orderings, Root-target posture, SCC parity, and held-proposal containment all pass; the pre-existing `SCC-001`, four isolates, two enum non-conformances, and one pre-existing Root path remain visible warnings. The SCA-APP-010 step-20 stop condition ("New blocker") is not triggered. No blocking result existed to upgrade or downgrade.
