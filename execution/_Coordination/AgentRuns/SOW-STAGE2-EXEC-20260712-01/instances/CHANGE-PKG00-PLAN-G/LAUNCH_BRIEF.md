# CHANGE-PKG00-PLAN-G Sealed Launch Brief

Role: `CHANGE` Agent 1. Parent run: `SOW-STAGE2-EXEC-20260712-01`.

## Objective

Perform routine validated Git closeout for the human's Piping PKG-00 Stage-2
planning amendment, the preserved original P1 decision evidence, and the
accepted revised P1 preflight. Work from `main` with expected entry
`HEAD == origin/main == 69ac259a7113d5a838fb22aa2e84df0e0f109713`.

## Exact stage scope

- `execution/_Coordination/WORKPLAN_2026-07-12_scope_of_work_stage2.md`
- `execution/_Coordination/LOOP_RECEIPTS.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/ORCHESTRATION_PLAN.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/WORK_GRAPH.json`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/amendments/HUMAN-STEER-PKG00-EXCLUSION-001.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/ORCHESTRATOR-P1-B0/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/ORCHESTRATOR-P1-B0-R1/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P1/preflight/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P1/preflight-r1/**`
- this CHANGE instance's own `LAUNCH_BRIEF.md`, `STATUS.json`, and `RETURN.md`

Stage no other path. In particular do not inspect, stage, modify, stash,
reset, clean, or otherwise act on `.claude-worktrees/**` or the four unrelated
dirty audit paths under `domains/piping-design/_Sources/{MWK_1956,Pipe-Stress-Engineering}/audit/`.

## Required validation

Confirm JSON parse and diff hygiene; the revised snapshot manifest hash
`3fad35f47088b1f1968bd2f8cef8b2fed3659891a4e96abffac88521fbb8ed77`;
the preserved predecessor manifest hash
`540848214dfc8185427c782b2cf7462b6658aa121f7171c52488192fbff7037a`;
22 revised members; 198 live bindings; 17 package-direction rows; zero
outbound-contradiction rows; and that the staged inventory is an exact subset
of the stage scope above.

If ready, create one routine commit with message
`Amend Stage-2 plan to retain Piping PKG-00 context` and push `main` to its
existing upstream. This is planning/control-plane evidence only: no project,
lifecycle, H1/H2, conversion, or dependency-truth mutation is authorized.
Return exact commit/push evidence, remaining dirty paths, checks, blockers,
and handoff. Do not create, merge, or delete a branch or PR.
