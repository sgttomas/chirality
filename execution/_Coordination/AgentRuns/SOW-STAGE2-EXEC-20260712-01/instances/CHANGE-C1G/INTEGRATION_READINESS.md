# C1G Integration Readiness Report

Date: 2026-07-13
Status: `READY`
Source branch: `codex/sow-stage2-canon` (not yet created at this checkpoint)
Integration branch: `main`
Required basis: `c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`

## Observations

- Local `HEAD`, local `main`, `origin/main`, and remote
  `refs/heads/main` all resolve to the required basis.
- `main...origin/main` divergence is `+0/-0` and the merge base is the exact
  required basis.
- No local branch, remote branch, or open/closed PR named
  `codex/sow-stage2-canon` exists.
- The three live canon paths are clean in both the index and worktree and
  retain the validated live-before SHA-256 values.
- Candidate SHA-256 values reproduce the C1V handoff exactly: standard
  `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f`,
  TYPES `5094610af55d18982658ea589be95a60fac9c89ca611846fc57279b494c6d2ae`,
  and SPEC `915c3b59d35afff5e489c9c387f09c17a6e4c307fd5e91cd81a8960d97a91e27`.
- C1V is closed `PASS` with zero findings. Its handoff names this CHANGE C1G
  integration as the next action and requires rerun only on basis, identity,
  candidate, path-set, or required-check drift.
- The only dirty state is untracked run/evaluation evidence and the pre-existing
  `.claude-worktrees/` directory. The latter is explicitly excluded and will
  remain untouched.
- No merge, rebase, cherry-pick, revert, or bisect operation is in progress.

## Interpretation and risks

The exact validated tranche is mechanically and governably ready for its
run-scoped branch and PR. The controls are source-SHA binding, exact path-set
containment, rerunning every required validation after activation, and never
staging `.claude-worktrees/` or paths outside the authorized run/evaluation
evidence and three canon files.

## Readiness verdict

`READY`. Human steer `amendments/HUMAN-STEER-001.md` provides standing approval
to merge this run-scoped PR after its exact source SHA, remote changed-path set,
checks, and merge readiness pass.
