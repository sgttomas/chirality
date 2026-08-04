# C4 CHANGE launch brief — sync current origin/main and restore tranche

Role: `CHANGE` (Agent 1)
Node: `C4`
Plan: `ORCHESTRATION_PLAN_V13.md`

## Objective

Safely bring the existing branch `codex/root-four-lanes-20260802` to contain
the current fetched `origin/main` while preserving the entire dirty and
untracked continuation tranche byte-identically. The user previously directed
sync before setting out. Do not rebase or force-push.

## Required method and evidence

1. Read `agents/AGENT_CHANGE.md` in full and inspect branch/upstream/worktree.
2. Fetch current `origin/main`; record its exact SHA and divergence.
3. Create a deterministic pre-sync inventory of every dirty/untracked path,
   type, mode where relevant, and content hash; verify zero staged/unmerged
   paths or fail closed.
4. Preserve all dirty/untracked bytes using a recoverable stash or equivalent
   CHANGE-approved mechanism; retain the recovery object after restoration.
5. Integrate fetched `origin/main` into the existing branch with no rebase,
   force, direct `main` push, or destructive reset. Resolve no semantic
   conflict by invention; stop if exact tranche overlap prevents automatic
   preservation.
6. Restore the complete candidate tranche and prove exact pre/post inventory
   parity, current-main ancestry, clean index/unmerged state, branch identity,
   and retained recovery object.
7. Write C4 `RETURN.md` and `STATUS.json` with exact SHAs, counts, hashes,
   commands/evidence location, and prohibitions observed.

## Hard stops

No candidate-tranche staging or commit, push, PR action, merge to `main`,
rebase, force operation, stash deletion, semantic edit, Task Management,
runtime/client/project, lifecycle/release/reliance, or foreign write. Preserve
the previously retained recovery stash and create/retain a new one if the
method requires it.
