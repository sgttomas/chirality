# Independent pre-commit verification brief

**RunID:** `APPDEV_LOOP_ENTRY_ROLE_CLEANUP_2026-07-17`

**Parent:** app-dev standing-loop operator

**Child kind:** independent read-only verifier

**Authority:** owner direction recorded in app-dev loop Receipt 62; D-APP-60
calibrated verification requirement

## Objective

Attempt to refute the proposed app-dev launcher and development-loop
instruction-separation tranche. Return only `COMMIT-SAFE` or `BLOCK`, followed
by concise evidence for any blocking defect.

## Sealed claims to refute

1. The root catalog's app-dev launcher and the project-local launcher are
   equivalent and select `HELP_HUMAN` without preselecting downstream agents.
2. Current app-dev loop surfaces no longer duplicate generic agent topology,
   work-graph, fan-out/fan-in, model-assignment, or managed-delegation rules.
3. Project-specific authority, discovery, fences, validation, receipts, and
   D-APP-60 verification remain binding; the frozen D-APP-60 record and
   superseded workplans are untouched.
4. The entrypoint validator enforces the new separation for any project whose
   local launcher selects `HELP_HUMAN`, without requiring the parallel piping
   change to land first.
5. Receipt 62 is structurally valid, truthfully attributes the owner's chat
   direction, and makes no unperformed verification claim.
6. Changes are confined to the owner-authorized root launcher/validator
   integration surfaces and app-dev instruction/evidence surfaces; no piping,
   domain-engine, runtime-source, authority-corpus, decision, dependency, or
   lifecycle state is changed.

## Read scope and evidence

- `git diff` and `git status` in the active worktree;
- changed files only, plus root `AGENTS.md`, canonical agent instructions,
  D-APP-60, and current app-dev loop authorities as needed to test the claims;
- existing validation output may be checked but must not be accepted without
  inspecting the relevant source and diff.

## Tools and write boundary

Read-only inspection and deterministic checks are allowed. No repository write
is authorized. Do not amend, stage, commit, push, or open a PR.

## Acceptance contract

- Return `BLOCK` if any claim is false, any requirement is weakened or moved
  into an unauthorized surface, any historical/frozen record changed, or any
  receipt statement anticipates an event that has not occurred.
- Otherwise return `COMMIT-SAFE`.
- Do not propose optional improvements in place of the binary verdict.
