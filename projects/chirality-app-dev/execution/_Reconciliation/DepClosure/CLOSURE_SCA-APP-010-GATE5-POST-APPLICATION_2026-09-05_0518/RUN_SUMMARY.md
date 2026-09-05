# Run Summary

`RUN_STATUS = WARNINGS`

`AUDIT = SCA-APP-010-GATE5-POST-APPLICATION`

`CLOSURE_VERDICT = WARNINGS`

## Outcome

The post-application dependency corpus is fully readable and column-schema-valid: 52/52 registers, 635/635 populated evidence rows, 52/52 `IMPLEMENTS_NODE` anchors, and 129/129 active deliverable endpoints resolved. The thirteen refreshed registers match their pinned identities.

Graph: 48 nodes, 109 directed edges (baseline 46 / 99); 10 edges added by the refresh, none retired, none SCC-internal. `SCC-001` (nine nodes: `DEL-02-05;DEL-03-02;DEL-03-03;DEL-03-04;DEL-04-03;DEL-04-05;DEL-05-02;DEL-05-03;DEL-05-05`) has membership identical to the baseline and to the SCA-APP-008 audit, with the same 10 elementary cycles; no new SCC and no new cycle. Isolates 6 -> 4 (`DEL-01-01`, `DEL-09-07`, `DEL-10-04`, `DEL-10-05`). One bidirectional pair, no hubs.

Warnings: the pre-existing nine-node SCC (DC-001), four isolated deliverables (DC-002 to DC-005), canonical-enum non-conformance in the unchanged registers `DEL-05-01` and `DEL-05-05` (DC-007, DC-008), and the pre-existing absolute Root path in `DEL-08-01` `DEP-08-01-013` (DC-009). The 19 held edge proposals (H-001 to H-019) are non-emitted and absent from the live graph. No blocker.

## Key identities

- Basis commit: `d66395d101143df68d956984f7ab93f5027418ec`; applied decomposition v3.2: `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`.
- Refreshed registers: see `Brief.md` and `Evidence/refreshed_registers.json` (all thirteen `Dependencies.csv` and `_DEPENDENCIES.md` identities match).
- Registered analyzer: `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91` (copy at `analyze_closure.py`).
- Accepted DAG: `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996`.
- Baseline: `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/Evidence/baseline_closure/`; prior audit: `SCA-APP-008-GATE5-POST-APPLICATION_2026-08-24`.

## Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as AUDIT_DEP_CLOSURE, dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.

## Next action

HELP_HUMAN consumes this warning-bearing derivative package for SCA-APP-010 `OWNER_ACTION_MATRIX.csv` step 20 / `DOWNSTREAM_HANDOFFS.csv` row 4 and the run's `HANDOFF_STATE.md`. Acceptance of this snapshot (`_Reconciliation/DepClosure/_LATEST.md`) is the owner's act. The held proposals, the `DEP-08-01-013` pointer, the two enum non-conformances, and the four isolates are owner-slate items; `SCC-001` remains with the cycle-resolution workflow. This audit grants no repair, activation, implementation, or release authority.
