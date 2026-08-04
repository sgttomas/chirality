# C5 CHANGE launch brief — current-main sync before closeout

- Parent: `HELP_HUMAN/ROOT_FOUR_LANES_2026-08-02`.
- Role: `CHANGE` Agent 1.
- Governing plan: `ORCHESTRATION_PLAN_V15.md` and `WORK_GRAPH_V15.json`.
- Pre-sync local HEAD: `ba576264793deba0708397874414b7482c243f89`.
- Local `origin/main`: `379b8b19b12b29eda4fa307e497499d6fe414f8a`.
- Independently observed live remote main:
  `0b69aabe000ea8ae78ca5a2134d734c40eba4972`.
- Independently observed live remote task branch:
  `4337990334c3e339a02c54de811d9f238246d524`.
- Current worktree summary: 17 modified tracked paths, 91 status-level
  untracked entries, zero staged paths, and zero unmerged paths.

## Objective

Repeat the proven C4 safe-sync method. Build an exact pre-sync inventory of
every dirty and untracked regular file, symlink, and directory-relevant path,
including status, type, mode, size, and SHA-256 where applicable. Preserve the
entire tranche recoverably; fetch the current remote refs; integrate exact
current `origin/main` into the existing branch without rebase or force; restore
the tranche; and prove exact pre/post parity and current-main ancestry.

## Authority and stops

The owner's standing direction to sync this worktree with `origin/main`
authorizes this bounded integration. Do not stage tranche paths, create a
tranche commit, push, update or merge PR #491, merge the task branch into
`main`, rebase, force, delete any stash/recovery material, resolve semantic
conflicts by judgment, or edit project/manager content. Stop on overlap,
conflict, lost path, type/mode/hash drift, staged/unmerged residue, or any
uncertain semantic effect.

## Durable return

Write only C5 `RETURN.md` and `STATUS.json` beside this brief. Report fetched
remote identities, resulting local HEAD, ancestry proof, exact pre/post
inventory counts and parity, overlap/conflict results, retained recovery
identities, Git status, forbidden-effect audit, and the exact condition for C6
release.
