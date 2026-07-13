# CHANGE Launch Brief — Publish and Bind D-GOV-16 Ruling

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `D-GOV16-RULING-20260712`
ALLOW_EXECUTION: `TRUE`
CLOSEOUT_MODE: scoped local commits; no push because this isolated branch has
no upstream and integration is outside this ruling-publication run.

## Objective

Create a non-merging publication commit for the validated exact D-GOV-16
ruling tranche, then a binding commit that replaces every current
`PENDING_PUBLICATION` pointer with the first commit's full SHA.

## Accepted input

- Branch/worktree:
  `codex/sow-stage1-execution` at
  `/Users/ryan/ai-env/projects/chirality-sow-stage1-execution`.
- Pre-publication HEAD:
  `6fcd1a6d06031b43a33d793064c8fb1f43457e63`.
- HELPS_HUMANS return:
  `execution/_Coordination/AgentRuns/D-GOV16-RULING-20260712/instances/HELPS-RULING/RETURN.md`.
- Root validation: exact proposal hashes, both patch apply checks, JSON,
  containment, and `git diff --check` PASS.

## Commit 1 — publication

Stage only the current ruling-publication tranche:

- D-GOV-16 decision and register;
- D-GOV-16 package README only (not its four exact-byte artifacts);
- root and Stage-1 handoffs and append-only receipt;
- the complete `D-GOV16-RULING-20260712` run records, including this brief.

Suggested message: `governance: publish D-GOV-16 ruling`.

## Commit 2 — binding

After commit 1, replace `PENDING_PUBLICATION` on current authority/handoff
surfaces with commit 1's exact full SHA. Update the D-GOV-16 register row to
name that published SHA. Append a short SHA-binding receipt or correction only
if required by the existing append-only ledger contract. Update this run's
handoff/return/status so the terminal state is
`D-GOV-16_RULED_STAGE2_PLAN_REQUIRED` and names commit 1 as the ruling
publication snapshot.

Suggested message: `governance: bind D-GOV-16 ruling publication`.

## Required checks

- Exact four proposal artifact hashes unchanged.
- D-GOV-16 items 1–10 unchanged from proposed snapshot.
- No diff in `docs/TYPES.md`, `docs/SPEC.md`, `projects/**`, `agents/**`,
  `skills/**`, or `tools/**`.
- Both exact patches pass `git apply --unidiff-zero --check`.
- Each new commit passes `git diff --check`.
- Branch clean; `main` and `origin/main` remain at the synchronized pre-run
  SHA; no merge, push, PR, rebase, reset, or Stage-2 implementation.

## Return

Write `RETURN.md` and `STATUS.json` under this instance. Report both commit
SHAs, branch divergence, validation, remaining stop, and any blocker.
