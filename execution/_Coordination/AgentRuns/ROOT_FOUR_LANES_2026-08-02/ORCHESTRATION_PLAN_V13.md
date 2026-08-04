# HELP_HUMAN orchestration plan — plan version 13

Run ID: `ROOT_FOUR_LANES_2026-08-02`
Selection authority: `HUMAN`
Posture: `SEQUENTIAL_SYNC_THEN_MIXED`

## Sync gate

The owner's standing direction is to bring this worktree into sync with
`origin/main` before setting out. W6 preflight observed local HEAD
`2b7a7d828e9173836e5b0a71fc015e4f45024215` and current `origin/main`
`a58512e67b4843cbfce4d03a0b1cc355ee87645e`; the latter is not an ancestor of
the former. W6 must remain held until CHANGE proves current ancestry and
byte-identical dirty-tranche restoration.

## Nodes

| Node | Agent 1 | Objective | Stop |
|---|---|---|---|
| C4 | CHANGE | Fetch current `origin/main`, inventory and preserve the entire dirty/untracked continuation tranche, integrate current `origin/main` into the existing branch without rebase or force, restore the tranche byte-identically, and verify ancestry/containment. | No tranche commit, staging, push, PR update, merge to `main`, rebase, force operation, semantic edit, or stash deletion. |
| W6 | WORKING_ITEMS | Resume plan-v12 planning graph only after C4 returns a validated current-basis sync. | Remains held during C4. |

## Fan-in acceptance

C4 is acceptable only if the fetched `origin/main` is an ancestor of the new
local HEAD; every pre-sync dirty/untracked path and byte is restored exactly;
no staged or unmerged path remains; no worktree path is lost or added by the
sync except Git integration metadata; the recovery stash is retained; and no
push, PR, rebase, force, or candidate-tranche commit occurs. W6 then rechecks
all exact governed basis hashes before dispatch.
