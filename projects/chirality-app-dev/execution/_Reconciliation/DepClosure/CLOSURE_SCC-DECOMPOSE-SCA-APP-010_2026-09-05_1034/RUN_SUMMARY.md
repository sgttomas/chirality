# Run Summary

`RUN_STATUS = WARNINGS`

`AUDIT = SCC-DECOMPOSE-SCA-APP-010` (1034, after the D-APP-110 decompose move)

`CLOSURE_VERDICT = PASS`

## Outcome

The strict active deliverable execution graph is acyclic after the D-APP-110 decompose move: the registered analyzer reports `scc_count = 0` with `scc_summary.csv` header only, and the independent re-derivation agrees (0 non-trivial SCCs by Tarjan; a Kahn topological order covering all 48 connected nodes). The dependency corpus is fully readable and column-schema-valid: 52/52 registers, 654/654 populated evidence rows, 52/52 `IMPLEMENTS_NODE` anchors, and 141/141 active deliverable endpoints resolved. The ten N14 carriers' `Dependencies.csv`, `_DEPENDENCIES.md`, and run-record files match their pinned post-write identities.

Graph: 48 nodes, 119 directed edges (0807 run 48 / 124; 0518 run 48 / 109; pre-extraction baseline 46 / 99). Delta versus the 0807 snapshot: exactly the five workbook edges removed (`DEL-02-01 -> DEL-02-04`, `DEL-02-02 -> DEL-02-04`, `DEL-02-03 -> DEL-02-04`, `DEL-04-05 -> DEL-02-05`, `DEL-06-03 -> DEL-08-01`), zero edges added, zero rows added or removed, zero rows retired or inverted. Move basis: the seven workbook rows (`DEP-04-05-010`, `DEP-02-01-010`, `DEP-02-04-017`, `DEP-02-04-019`, `DEP-02-02-022`, `DEP-02-04-018`, `DEP-06-03-014`) are `ACTIVE` with `TargetType=DOCUMENT`, empty `TargetDeliverableID`, the workbook's `TargetRefID` and `TargetLocation`, and a `Notes` clause naming D-APP-110; each decomposed edge is necessary (restoring any one re-creates a cycle); no `PREREQUISITE` row was re-targeted. The thirteen other D-APP-109 rows are strict edges of the acyclic graph gating per their `SatisfactionStatus` (PENDING x10, TBD x3), their `Notes` carrying the resolved clause; six re-targeted emitted rows plus those thirteen are exactly the nineteen H-001 to H-019, `DEP-04-05-010` being pre-existing. Bidirectional pairs: none (the 0807 run's four all dissolved); isolates unchanged at 4 (`DEL-01-01`, `DEL-09-07`, `DEL-10-04`, `DEL-10-05`); no hubs. The result equals the parent's live check `Evidence/fanin_live_v1.3/` field for field.

Warnings, all carried from the 0518 and 0807 runs and untouched by the move: four pre-existing isolates (DC-002 to DC-005), canonical-enum non-conformance in the unchanged registers `DEL-05-01` and `DEL-05-05` (DC-006, DC-007), and the pre-existing absolute Root path in `DEL-08-01` `DEP-08-01-013` (DC-008). No blocker; nothing upgraded or downgraded. The closure verdict follows the `SCC-SAFE-MOVES-001` precedent: `PASS` on closure with the carried warnings listed; `RUN_STATUS` is `WARNINGS` in the role's vocabulary because those warnings remain visible (`Decision_Log.md` DEC-011).

## Key identities

- Basis commit: `7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985` (equal to `HEAD` at run time; carries the 0807 registers) plus the uncommitted N13/N14/N15 working tree.
- Post-move registers: `Evidence/n14_postwrite_identities.json` in the run folder and `Evidence/refreshed_registers.json` here (all ten `Dependencies.csv`, `_DEPENDENCIES.md`, and run-record identities match; exactly these ten registers differ from the basis).
- Registered analyzer: `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91` (copy at `analyze_closure.py`), invoked exactly once.
- Accepted DAG: `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996` (verified live).
- Prior state: `_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0807/`; baseline `_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/Evidence/baseline_closure/`; parent live check `Evidence/fanin_live_v1.3/`; move workbook `SCC_DECOMPOSE_RULINGS.csv`; review `REVIEW_v1.3.md` (PASS, 0/0/4).

## Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as AUDIT_DEP_CLOSURE, dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.

## Next action

HELP_HUMAN consumes this derivative package for amendment v1.3 node N17 fan-in, `HANDOFF_STATE.md` (replacing the snapshot-name placeholder with `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`), `VALIDATION_EVIDENCE.md`, and the run-folder `MANIFEST.sha256`. Acceptance of this snapshot as the loop's DepClosure pointer (`_Reconciliation/DepClosure/_LATEST.md`) is an owner act; this audit did not move it. The `DEP-08-01-013` pointer, the two enum non-conformances, and the four isolates remain owner-slate items. This audit grants no implementation, activation, selection, release, repair, or pointer-movement authority and makes no cut, merge, inversion, or linearization. Rerun this audit after any later recorded move, decomposition revision, or scope change.
