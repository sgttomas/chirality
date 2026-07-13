# CHANGE-C2G Sealed Launch Brief — v1

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Dependency: `C2F-R2 PASS`

## Objective and approval

Serially integrate the validated root consumer tranche, App runtime tranche,
and P2 consumer evidence through one run-scoped PR; merge it under blanket
human approval `amendments/HUMAN-STEER-001.md`; synchronize local main.

The owning workflows have supplied terminal PASS handoffs. Approval covers
the PR merge but not failed checks, extra paths, semantic reinterpretation,
force/history rewriting, destructive cleanup, deliverable conversion,
lifecycle action, release, H1/H2, or legacy retirement.

## Required basis and branch

- Require local `main`, `origin/main`, and remote main at
  `e150c972889d05a8fc270239451a35c7512dc9a9` before branch creation.
- Preserve the current validated dirty candidate while switching to a new
  branch `codex/sow-stage2-consumers` from that exact HEAD. Stop on branch or
  remote collision unless provably the same clean lane.
- PR base: `main`; one non-draft PR; repository-default permitted merge.

## Exact source tranches

Commit 1, root consumers (`feat: activate Scope-of-Work root consumers`):

- exactly the 48 current root source paths represented by
  `candidates/P2_ROOT/CALLER_MANIFEST.tsv` with `Status=UPDATED` and by the
  root current changed-path manifest, under `agents/`, current `docs/`,
  `skills/`, `tools/`, and `exports/chirality-app/export-manifest.csv`;
- no `execution/**` or `projects/**` path in this commit.

Commit 2, App runtime (`feat: activate Scope-of-Work App runtime`):

- exactly the four source paths in the initial C2A changed-path manifest:
  scanner, DocumentView, scanner tests, and route tests;
- no project execution/control/deliverable path in this commit.

Commit 3, evidence binding (`chore: bind Scope-of-Work consumer activation`):

- root run `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/**`;
- only C2F/C2F-R1/C2F-R2 packages under
  `execution/_Evaluation/SOW-STAGE2-EXEC-20260712-01/`,
  `execution/_Evaluation/Reviews/`, and
  `execution/_Reconciliation/DeliverableConcordance/`;
- only project runs `SOW-STAGE2-EXEC-20260712-01-C2A` and `...-C2A-R1` under
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/`.

Do not stage `.claude-worktrees/` or any other path.

## Required readiness and checks

1. Produce `INTEGRATION_READINESS.md` with exact state, source hashes, closure,
   derivative status, changed-path containment, no in-progress Git operation,
   and the three commit path sets.
2. Verify `snapshots/P2_CONSUMERS/MANIFEST.tsv` hashes, C2F-R2 three-manager
   PASS, `git diff --check`, exact ruled authority in all four seams, current
   root/App manifest counts and final hashes, and no forbidden path.
3. Use current-hash-bound producer/fan-in evidence for the full 792 root and
   713+4 App suites. Rerun bounded preintegration checks needed to detect
   staging/integration errors: root focused tests, agent/skill/entrypoint/path
   checks, App focused/typecheck, export profile, self-check, and exact
   manifest/containment. A failed required check stops the PR.
4. Make the three serial commits. Confirm the branch contains no fourth
   semantic tranche and working tree is clean except `.claude-worktrees/`.
5. Write `snapshots/P2_CONSUMERS/INTEGRATION_HANDOFF.md`, this instance's
   `PREINTEGRATION_CHECKS.md`, `RETURN.md`, and source-bound `STATUS.json`
   identifying the three source commits, parentage, hashes, rollback/revert
   instruction, blockers/reruns, derivative status, and B1 as next dependency.
   Amend commit 3 or add one final evidence-binding commit if necessary; do
   not alter commits 1 or 2.
6. Push branch, open one non-draft PR, verify remote changed paths/checks, and
   merge under HUMAN-STEER-001 without force/history rewrite.
7. Switch to local main, fast-forward/synchronize, verify local
   main/origin/main/remote main equality, divergence `+0/-0`, tracked-clean
   state except `.claude-worktrees/`, and exact live source hashes.

## Return

Return `PASS | PARTIAL | BLOCKED | DECISION_REQUIRED` with branch, source and
binding commits, PR URL/number, merge commit, synchronized main SHA, checks,
changed paths, remaining state, handoff, and next node. C2G PASS releases B1
only; no deliverable conversion, H1, H2, or retirement action.
