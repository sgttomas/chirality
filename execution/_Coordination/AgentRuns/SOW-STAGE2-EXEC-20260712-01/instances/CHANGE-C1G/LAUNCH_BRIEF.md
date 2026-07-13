# CHANGE-C1G Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Dependency: `C1V_PASS`

## Objective and approval

Integrate only the independently validated exact-canon tranche through one
run-scoped PR, bind its exact source commit, merge it, and resynchronize local
main. The owning workflow has handed off validated semantic edits. Human steer
`amendments/HUMAN-STEER-001.md` gives blanket approval to merge PRs throughout
this goal; no additional merge-confirmation round is required after readiness
passes.

This approval does not cover failed checks, extra paths, semantic edits,
force/history rewriting, destructive cleanup, consumer/project/lifecycle
work, H1, or H2.

## Basis, source, and exact scope

- Require local `main`, `origin/main`, and remote main at
  `c5f5bbd6e636916a76c34a04295f6ddd2a3d0983` before branch creation.
- Candidate and validated hashes are in
  `snapshots/P1_CANON/VALIDATION_HANDOFF.md`.
- C1V handoff is
  `execution/_Evaluation/SOW-STAGE2-EXEC-20260712-01/C1V/HANDOFF.md`.
- Branch: `codex/sow-stage2-canon` (stop on collision unless it is provably
  the same clean run lane).
- PR base: `main`.

Allowed semantic file changes are exactly:

- `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`;
- `docs/TYPES.md`;
- `docs/SPEC.md`.

Allowed evidence additions/updates are exactly this execution run directory
and `execution/_Evaluation/SOW-STAGE2-EXEC-20260712-01/C1V/`. Do not stage or
mutate `.claude-worktrees/` or any other path.

## Required execution

1. Produce an Integration Readiness Report from live Git/PR state and verify
   basis, source hashes, closure/handoff, changed-path containment, and no
   in-progress Git operation.
2. Create/switch the run branch from the exact basis. Apply the candidate to
   the three live canon paths with `apply_patch`; do not reinterpret content.
3. Verify live hashes equal the validated candidate hashes and the diff has
   only the three canon paths plus allowed run/evaluation evidence.
4. Run `git diff --check`, exact comparisons, path-anchor validation,
   instruction-entrypoint validation, agent-instruction validation, and the
   governance self-check. Record exact results.
5. Commit the exact canon plus preintegration run/evaluation evidence as
   commit 1 with message `governance: activate D-GOV-16 exact canon`.
6. Write
   `snapshots/P1_CANON/INTEGRATION_HANDOFF.md` and this instance's terminal
   records binding commit 1, its parent, exact three canon hashes, validation
   evidence, derivative status, rollback/revert instruction, blockers/reruns,
   and next dependency. Commit those binding records as commit 2 with message
   `governance: bind D-GOV-16 exact canon activation`.
7. Push the branch, open one non-draft PR, verify the remote changed-path set
   and checks/readiness, and merge it under HUMAN-STEER-001 without force or
   history rewriting. Use the repository-default permitted merge method.
8. Switch to local `main`, fast-forward/synchronize it to remote main, confirm
   local main/origin/main/remote main equality, live canon hashes, divergence
   `+0/-0`, and clean tracked state. Preserve `.claude-worktrees/` untouched.

If GitHub or branch protection requires a different non-destructive merge
mechanism, use the permitted repository-default mechanism and record it. Stop
on source-SHA drift, extra path, check failure, conflict, auth/protection
failure, or any need to amend content.

## Return

Return `PASS`, `PARTIAL`, `BLOCKED`, or `DECISION_REQUIRED` with branch, both
source commits, PR URL/number, merge commit, synchronized main SHA, checks,
changed paths, remaining dirty state, handoff path, and next released node.
C1G PASS releases C2R and C2A preparation only; it is not consumer fan-in,
conversion authority, H1, or H2.
