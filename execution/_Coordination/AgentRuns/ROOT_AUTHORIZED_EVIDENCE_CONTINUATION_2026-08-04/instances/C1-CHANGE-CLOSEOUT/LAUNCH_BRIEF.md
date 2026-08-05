# C1 launch brief — routine evidence-tranche publication

InstanceID: `C1-CHANGE-CLOSEOUT`

Role: `CHANGE` (Agent 1), managed by `HELP_HUMAN`

## Objective

Publish the exact validated evidence-only tranche through the standing
human-gated PR workflow. Create branch
`codex/root-evidence-continuation-2026-08-04` from exact current
`origin/main@cdc76a1d398231267f1379e7143b4de27abaa01b`, preserving the present
untracked tranche; validate and stage only the declared paths; commit, push,
open a PR to `main`, and report exact identities and check state. Do not merge.

## Declared tranche paths

- `execution/_Coordination/AgentRuns/ROOT_AUTHORIZED_EVIDENCE_CONTINUATION_2026-08-04/`
- `execution/_Evaluation/PI_0820_CONCORDANCE_2026-08-02_97678A8/g1b_refresh_2026-08-04/`
- `execution/_Coordination/LOOP_RECEIPTS.md`

No other path may be staged or committed. Preserve unrelated dirty work and
stop on any overlap, remote-main drift, branch collision, conflict, manifest
failure, receipt discontinuity, scope escape, or unexpected tracked delta.

## Required checks and return

Before commit: reproduce H1/H2/H3/H4 manifests, parse governed JSON/CSV,
validate candidate whitespace against `origin/main`, run `git diff --check`,
confirm Root register counts remain unchanged, confirm exact source paths and
no symlinks/absolute-path leakage, and record the independent Draft 2020-12
compiler gap as unexecuted rather than PASS.

Write `STATE_REPORT.md`, `RETURN.md`, and `STATUS.json` in this instance before
staging. Commit only after every required check passes; use a concise message
describing evidence continuation. Push the new branch and open one PR with a
body that states evidence-only scope, exact manifests, preserved holds,
unexecuted compiler gap, and merge ownership. Report the commit SHA, remote
branch, PR number/URL, remaining worktree state, and initial hosted-check
state. Do not rebase, force-push, merge, delete a branch, or infer semantic
acceptance.
