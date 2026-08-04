# N2 validation

Verdict: `PASS`

- Direct CSV parse: live `27` with exactly `OPEN=16`, `DEFERRED=11`;
  archive `95` with exactly `CLOSED=95`.
- Receipt 90 M6 expected counts: exact match.
- Tracked diff containment: exactly
  `execution/_Coordination/HANDOFF_STATE.md`.
- Handoff diff: one stale three-line count clause replaced by one current
  three-line clause; no other hunk.
- JSON control plane: `jq empty` PASS.
- Whitespace: `git diff --check` PASS.
- Worktree: assigned RunID untracked plus the one authorized tracked handoff
  modification; no unrelated tracked edit.
