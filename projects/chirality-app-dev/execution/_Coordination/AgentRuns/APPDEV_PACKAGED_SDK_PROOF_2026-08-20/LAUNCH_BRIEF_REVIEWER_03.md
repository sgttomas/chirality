# Sealed TASK brief — fresh post-CI integrated review

- ChildInstanceId: `A2-DEL0904-PACKAGED-SDK-REVIEW-03`
- Parent: `WORKING_ITEMS / PKG-09`
- AgentType: `TASK`
- TaskSkill: `software-code-review`
- Model attribution: OpenAI Codex agents; exact builds not exposed.
- Accepted basis: `d8c47d9fbc459b32c053c844be0fa789fd1ffab2`.
- Landed node:
  `3a02eeedeb3561748d96b10f57a1aa7f5546eeb5`, PR #585.
- Frozen subject: all 34 paths and exact hashes in
  `POST_CI_FROZEN_DIFF_MANIFEST.md`; this is the complete initial committed
  node plus post-CI fan-in state.
- APP-HOLD preflight: `ALLOW`; DEL-09-04 `NOT_HELD`.

## Objective

Perform a fresh read-only software review over 100% of the frozen integrated
subject. Verify that the original workflow/test implementation remains sound,
the CI proof facts are internally consistent with the local temporary artifact
and live PR/run/job evidence, and the DEL-09-04 Remaining narrowing closes only
the packaged-SDK/DMG and premerge gap while retaining every genuinely unproved
item. Pay special attention to the read-only `RUNNER_TEMP` mounted-app root:
do not require `/Volumes`.

## Required checks

1. Recompute all 34 frozen hashes before semantic review.
2. Inspect the full accepted-basis-through-worktree diff and every frozen path.
3. Confirm both staged and mounted summaries say `status: pass` and
   `proofMode: scripted-no-live-provider`, bundle roots are distinct, packaged
   executable SHA values match, and aggregate identity is true.
4. Confirm the evidence does not imply live-provider/network proof, signing,
   notarization, distribution/publication, release readiness, lifecycle
   advancement, approval-SHA change, or owner-machine deployment.
5. Confirm Remaining text retains login-time `RunAtLoad`, packaged network-
   policy proof, and the owner-machine act while removing only proved scope.
6. Verify JSON parse, record consistency, receipt untouched, APP-HOLD/corpus
   claims, completion-log single-entry containment, and candidate-wide
   whitespace hygiene.

## Permissions and output

Read-only except for exactly:

- `REVIEWER_RETURN_03.md`
- `STATUS_REVIEW_POST_CI.json`

Do not modify product, deliverable, manager, plan, receipt, or existing record
bytes. Do not commit, push, open/update a PR, merge, sign, notarize, publish,
distribute, use credentials/providers, or access a live provider. Return
`PASS`, `PASS_WITH_FINDINGS`, or `FAIL`, exact coverage, actionable findings,
residual risks, and the two output paths. Do not delegate.
