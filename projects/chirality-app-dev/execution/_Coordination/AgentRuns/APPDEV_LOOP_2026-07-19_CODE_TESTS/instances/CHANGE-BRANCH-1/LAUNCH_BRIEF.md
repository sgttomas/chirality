# CHANGE-BRANCH-1 — Sealed Launch Brief v1

> Reconstructed from the platform-native sealed brief/return, repository
> evidence, and Agent-0 fan-in; not a byte-verbatim runtime export.

- **RunID:** `APPDEV_LOOP_2026-07-19_CODE_TESTS`
- **InstanceID:** `CHANGE-BRANCH-1`
- **Role:** CHANGE
- **Parent:** HELP_HUMAN
- **Brief version:** 1

## Objective

In the existing selected worktree, create and switch to branch
`codex/app-dev-authorized-code-tests-20260719` at the exact clean base
`ad7f5c891a17ba1f98b33b1b2072572afbf51bce`.

## Scope

- Read: Git metadata needed to verify repository root, current branch, exact
  HEAD, and worktree cleanliness.
- Write: only the branch ref and `HEAD` necessary to create/switch the branch.
- Prohibited: worktree/file edits, commit, push, fetch, merge, rebase, reset,
  stash, and any history rewrite.

## Return contract

Return exact branch name, exact HEAD, `git status` cleanliness, actions taken,
or a concrete blocker. Do not infer a broader approval gate.

The rejected v1 blocker and the scope-preserving v2 clarification are recorded
in `../../amendments/CHANGE-BRANCH-1/v2.md` and `RETURN.md`.
