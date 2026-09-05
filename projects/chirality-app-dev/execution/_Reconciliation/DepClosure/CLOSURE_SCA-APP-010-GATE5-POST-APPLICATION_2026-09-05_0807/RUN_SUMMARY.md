# Run Summary

`RUN_STATUS = WARNINGS`

`AUDIT = SCA-APP-010-GATE5-POST-APPLICATION` (second run, 0807, after the D-APP-109 emission)

`CLOSURE_VERDICT = WARNINGS`

## Outcome

The post-emission dependency corpus is fully readable and column-schema-valid: 52/52 registers, 654/654 populated evidence rows, 52/52 `IMPLEMENTS_NODE` anchors, and 148/148 active deliverable endpoints resolved. The thirteen carriers' `Dependencies.csv` and `_DEPENDENCIES.md` files match their pinned post-emission identities.

Graph: 48 nodes, 124 directed edges (0518 run 48 / 109; pre-extraction baseline 46 / 99). Delta versus the 0518 snapshot: exactly the fifteen held edges added (nineteen rows, H-001 to H-019), zero edges removed, zero rows removed or changed. The observed SCC set equals the fan-in simulation D-APP-109 accepted: `SCC-001` = `DEL-06-03;DEL-08-01` (2 nodes, 1 elementary cycle) and `SCC-002` = twenty nodes (`DEL-02-01;DEL-02-02;DEL-02-03;DEL-02-04;DEL-02-05;DEL-03-02;DEL-03-03;DEL-03-04;DEL-04-02;DEL-04-03;DEL-04-04;DEL-04-05;DEL-05-02;DEL-05-03;DEL-05-04;DEL-05-05;DEL-08-02;DEL-08-03;DEL-08-04;DEL-08-05`; 41 internal edges; 64 elementary cycles, enumerated completely within `MAX_CYCLES=10000`). The former nine-node SCC is a subset of `SCC-002`. Every one of the nineteen emitted rows carries `CYCLE_PARTICIPATING` and the D-APP-109 non-gating clause. Four bidirectional pairs as expected; isolates unchanged at 4 (`DEL-01-01`, `DEL-09-07`, `DEL-10-04`, `DEL-10-05`); no hubs.

Warnings: the recorded, owner-accepted SCC change (DC-001 twenty-node `SCC-002`, DC-002 two-node `SCC-001`), four pre-existing isolates (DC-003 to DC-006), canonical-enum non-conformance in the unchanged registers `DEL-05-01` and `DEL-05-05` (DC-011, DC-012), and the pre-existing absolute Root path in `DEL-08-01` `DEP-08-01-013`, unchanged (DC-013). No blocker; nothing upgraded. The SCC change is recorded under D-APP-109; every edge inside an unresolved SCC is non-gating until a recorded decompose, invert, merge, or cut move, and this audit proposes none.

## Key identities

- Basis commit: `f38f1448675b8e9f40f33932a11b7ffa4126fe69` (carries the 0518 registers) plus the uncommitted N8/N9 working tree.
- Post-emission registers: see `Brief.md` and `Evidence/refreshed_registers.json` (all thirteen `Dependencies.csv` and `_DEPENDENCIES.md` identities match; nine differ from `HEAD`, exactly the emitting carriers).
- Registered analyzer: `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91` (copy at `analyze_closure.py`).
- Accepted DAG: `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996` (verified live).
- Prior state: `_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0518/`; baseline `_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/Evidence/baseline_closure/`; accepted simulation `Evidence/fanin_simulation_v1/`.

## Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as AUDIT_DEP_CLOSURE, dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.

## Next action

HELP_HUMAN consumes this warning-bearing derivative package for amendment v1.2 node N11 and the run's `HANDOFF_STATE.md`. Acceptance of this snapshot (`_Reconciliation/DepClosure/_LATEST.md`) is the owner's act. The two SCCs go to the cycle-resolution workflow with the per-SCC options listed in `Dependency_Closure_Report.md` ("Resolution options for the owner"); the `DEP-08-01-013` pointer, the two enum non-conformances, and the four isolates remain owner-slate items. This audit grants no repair, activation, implementation, or release authority and makes no cut, merge, inversion, or linearization.
