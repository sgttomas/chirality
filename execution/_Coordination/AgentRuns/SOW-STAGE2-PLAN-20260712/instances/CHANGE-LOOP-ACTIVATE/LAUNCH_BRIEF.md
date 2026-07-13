# CHANGE Launch Brief — Activate and Publish Stage-2 Root Loop

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-PLAN-20260712`

## Human authorization

The owner directed "proceed accordingly" after the root reported the exact
required correction: integrate the accepted plan, add a Stage-2 standing
workplan, make loop selection unambiguous, update handoff/receipt, and publish
the result before the next session.

## Objective

Create an immutable loop-activation snapshot, bind it in root coordination,
then fast-forward and push `main` to the exact bound activation commit. Do not
dispatch Stage-2 implementation.

## Commit 1 — activation snapshot

On `codex/sow-stage2-plan` at parent
`b22a24fda994a8387a9bf2e04a2826dc311a36dd`, stage only:

- `execution/_Coordination/LOOP_INIT.md`;
- `execution/_Coordination/CURRENT_WORKPLAN.md`;
- `execution/_Coordination/WORKPLAN_2026-07-12_scope_of_work_stage2.md`;
- the plan-run `PLAN_ACCEPTANCE.md`, ORCHESTRATOR-LOOP amendment/return/status,
  and this CHANGE-LOOP-ACTIVATE launch/status.

Message: `governance: activate D-GOV-16 Stage-2 root loop`.

## Commit 2 — binding snapshot

After commit 1, add/update only:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-PLAN-20260712/LOOP_ACTIVATION_BINDING.md`;
- `execution/_Coordination/HANDOFF_STATE.md`;
- append-only `execution/_Coordination/LOOP_RECEIPTS.md`;
- this instance's `RETURN.md` and `STATUS.json`.

Bind the full commit-1 SHA and set the terminal maintenance state to
`STAGE2_LOOP_ACTIVE — READY_FOR_FRESH_EXECUTION_SESSION`. State explicitly
that no Stage-2 node ran and H1/H2 remain unapproved.

Message: `governance: bind Stage-2 root loop activation`.

## Main integration and push

After both commits validate:

1. verify local `main`, local `origin/main`, and remote `main` still equal
   `c9af689118e4e87f329e1ab4c6e71fea331b2674`;
2. verify the final activation commit is a strict descendant and the merge is
   fast-forward-only;
3. in `/Users/ryan/ai-env/projects/chirality`, fast-forward `main` to that
   exact final commit and push `main` to origin without force; and
4. verify local `main`, local `origin/main`, and remote main all equal the
   final activation commit.

Preserve `.claude-worktrees/`.

## Checks and prohibitions

- Validate the deterministic bootstrap pointer chain and target containment.
- Confirm `init/init-prompt.md` is unchanged.
- Confirm no changes under `docs/`, `projects/`, `agents/`, `skills/`, `tools/`,
  or `exports/` relative to plan binding.
- Both commits pass `git diff --check`; JSON statuses parse.
- No rebase, reset, force push, pilot merge, canon application, conversion,
  lifecycle act, H1/H2 approval, or Stage-2 child dispatch.
