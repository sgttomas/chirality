# C4 CHANGE return — current-main sync

Status: **COMPLETE — CURRENT MAIN CONTAINED; TRANCHE RESTORED EXACTLY**

Run: `ROOT_FOUR_LANES_2026-08-02`

Plan: `ORCHESTRATION_PLAN_V13.md`

Role: `CHANGE` (Agent 1)

Completed evidence snapshot: `2026-08-03T20:36:01Z`

## Result

The existing branch `codex/root-four-lanes-20260802` now contains fetched
`origin/main@379b8b19b12b29eda4fa307e497499d6fe414f8a`. The complete pre-sync
continuation tranche was restored byte-identically with the same path set,
status, type, filesystem mode, size, and SHA-256 for every path. No staged or
unmerged path remains. A terminal `git ls-remote origin refs/heads/main` at
`2026-08-03T20:37:47Z` returned that same `379b8b19...` tip.

The remote basis advanced once during the first synchronization cycle. C4 did
not accept a stale ancestry result: it retained the first recovery object,
created a second checkpoint, fetched again, confirmed zero semantic path
overlap, integrated the newer tip, restored the exact checkpoint, and reran
the complete parity proof.

## Git evidence

| Item | Evidence |
|---|---|
| Pre-sync branch | `codex/root-four-lanes-20260802` |
| Pre-sync HEAD | `2b7a7d828e9173836e5b0a71fc015e4f45024215` |
| Initial fetched main | `a58512e67b4843cbfce4d03a0b1cc355ee87645e` |
| Initial divergence | 2 local-only / 10 main-only commits |
| First integration HEAD | `065988c8b7c91493059de0881591a2e685610164` |
| First integration parents | `2b7a7d828e9173836e5b0a71fc015e4f45024215`, `a58512e67b4843cbfce4d03a0b1cc355ee87645e` |
| Refreshed current main | `379b8b19b12b29eda4fa307e497499d6fe414f8a` |
| Second-cycle divergence | 3 local-only / 4 main-only commits before integration |
| Final integration HEAD | `ba576264793deba0708397874414b7482c243f89` |
| Final integration parents | `065988c8b7c91493059de0881591a2e685610164`, `379b8b19b12b29eda4fa307e497499d6fe414f8a` |
| Final ancestry | PASS: fetched `origin/main` is an ancestor of final HEAD |
| Upstream | `origin/codex/root-four-lanes-20260802@4337990334c3e339a02c54de811d9f238246d524`; unchanged and not pushed |

Both integrations used `git merge --no-edit origin/main`. No rebase, reset,
force operation, direct-main operation, push, or PR action occurred.

## Pre/post inventory parity

The deterministic inventory covered 172 paths: 17 tracked modifications and
155 untracked files. Precondition and terminal state both had zero staged and
zero unmerged paths.

| Evidence | Pre SHA-256 | Final SHA-256 | Verdict |
|---|---|---|---|
| Null-delimited porcelain status | `0507ccd69f90dc4c371597a93a26b54bcb516a3cdc2b91f26936691a58c0c169` | `0507ccd69f90dc4c371597a93a26b54bcb516a3cdc2b91f26936691a58c0c169` | byte-identical |
| Sorted dirty-path set | `81ce2ac1cdd2a73497341012117daefd5a4c6cf0b90bff6afd9ac9b3d477e3f3` | `81ce2ac1cdd2a73497341012117daefd5a4c6cf0b90bff6afd9ac9b3d477e3f3` | byte-identical |
| Type/mode/size/content-hash inventory | `ea336cf385a8e03bdf75800436a9ff847203308dd891c4c92b22ccce3b054e9d` | `ea336cf385a8e03bdf75800436a9ff847203308dd891c4c92b22ccce3b054e9d` | byte-identical |

All three direct `cmp` checks exited 0. The underlying command evidence is in
`/tmp/chirality-c4-current-main-sync-EPTEeSjB/`. Required C4 `RETURN.md` and
`STATUS.json` were written only after the 172-path parity proof; they are C4
evidence outputs, not synchronization drift.

## Semantic-overlap proof

- Initial current-main range: 427 changed paths, zero intersection with the
  preserved tranche. Changed-path-list SHA-256:
  `c48bcd9e27a7676493a6c966d2e2ca882b35cba681d5acf87ffa4606f87fc05b`.
- Main advance during C4: 117 changed paths, zero intersection with the
  preserved tranche. Changed-path-list SHA-256:
  `5110cd5a52860deb7564f2f7ec07a495bdb5c9c925ac538b6ab2bdaf49951e91`.
- Both empty-intersection files have SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

No semantic conflict was resolved or invented.

## Retained recovery objects

- C4 second checkpoint, used for final restore:
  `e527a7c91b06b589bcd39860a71782054f149628`.
- C4 initial preimage:
  `217cb694bb60b4122c7c55b5686a028f9dceaffb`.
- Previously retained recovery object, preserved unchanged:
  `74fb72eeba760e132edcb01b2b628af3353c5799`.

Each object resolves as a Git commit and remains present in the stash list. No
stash was dropped.

## Prohibitions observed

No candidate-tranche stage or commit, push, PR action, merge to `main`, rebase,
force operation, destructive reset, stash deletion, semantic edit, Task
Management action, runtime/client/project work, lifecycle/release/reliance act,
or foreign write occurred. W6 may perform its own exact-basis preflight from
this synchronized local state.
