# CHANGE Launch Brief — Bind Stage-2 Plan Snapshot

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-PLAN-20260712`

## Objective

Commit the validated plan-only package on `codex/sow-stage2-plan`, then bind
that immutable commit in a second closeout commit. Do not merge or push the
plan branch and do not release Stage-2 execution.

## Accepted basis and scope

- Branch basis: synchronized
  `main@c9af689118e4e87f329e1ab4c6e71fea331b2674`.
- Plan return:
  `instances/ORCHESTRATOR-PLAN/RETURN.md`, verdict `PASS`.
- Stage only
  `execution/_Coordination/AgentRuns/SOW-STAGE2-PLAN-20260712/**` for the first
  commit. Preserve `.claude-worktrees/`.

## Commit 1 — plan snapshot

Commit the complete validated run directory with message:

`governance: present D-GOV-16 Stage-2 orchestration plan`

## Commit 2 — binding handoff

After commit 1:

1. add `SNAPSHOT_BINDING.md` under the run directory naming commit 1 and the
   six ORCHESTRATOR output hashes;
2. update root `execution/_Coordination/HANDOFF_STATE.md` to
   `STAGE2_PLAN_PRESENTED_AWAITING_ACCEPTANCE`, naming synchronized main,
   plan branch/snapshot, no-dispatch state, blockers, and rerun requirements;
3. append a concise plan-presentation receipt to
   `execution/_Coordination/LOOP_RECEIPTS.md`;
4. write this instance's terminal `RETURN.md` and `STATUS.json`.

Commit only those binding/coordination files with message:

`governance: bind D-GOV-16 Stage-2 plan snapshot`

## Checks and prohibitions

- Confirm plan arithmetic 10 + 143 + 1 = 154 and traceability 10/10.
- Confirm only the run directory plus the two root coordination files change
  relative to basis.
- Confirm no canon, project, agent, skill, tool, export, pilot, lifecycle, or
  remote ref changes.
- Each commit must pass `git diff --check`; worktree must be clean except the
  preserved `.claude-worktrees/` path.
- No merge, push, rebase, reset, worktree cleanup, or Stage-2 dispatch.
