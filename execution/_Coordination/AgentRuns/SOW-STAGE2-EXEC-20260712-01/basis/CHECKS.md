# B0 Check Summary

Verdict: `PASS`

| Check | Command/evidence | Result |
|---|---|---|
| synchronized refs | `git rev-parse refs/heads/main`; `git rev-parse refs/remotes/origin/main`; `git ls-remote origin refs/heads/main` | all `c5f5bbd6e636916a76c34a04295f6ddd2a3d0983` |
| accepted ancestors | `git merge-base --is-ancestor <plan-binding> refs/heads/main`; same for ruling | PASS/PASS |
| governed hashes | `sha256sum` over successor standard, TYPES patch, SPEC patch, evidence index | all exact |
| patch contexts | `git apply --unidiff-zero --check <patch>` | PASS/PASS |
| tracked membership | `git ls-files 'projects/chirality-app-dev/execution/**/1_Working/DEL-*/Datasheet.md' 'projects/chirality-piping/execution/**/1_Working/DEL-*/Datasheet.md'` then strip filename and C-sort | 154; digest exact |
| companions/SOW | test four companions and `_STATUS.md` per member; test `ScopeOfWork.md` absence | 0 missing; 0 SOW |
| lifecycle | first `**Current State:**` assertion in each `_STATUS.md` | 153 `IN_PROGRESS`; 1 named `ISSUED` |
| pilots | exact App PKG-07/Piping PKG-13 membership plus Stage-1 inventory/evidence-commit hash comparison | 10/10; sources, status, candidates exact |
| caller search | accepted original regex plus targeted `ScopeOfWork.md|SOW_V1|LEGACY_FOUR_DOC|PILOT_DUAL|MIGRATION_DUAL` regex, commit-bound with `git grep` | 5,414 union paths covered; 0 active unclassified |
| worktree containment | `git status --porcelain=v1 --untracked-files=normal` | tracked clean; only `.claude-worktrees/` and fresh run untracked |
| write scope | enumerate run outputs and compare against sealed brief | only authorized B0 targets |

No named invariant delta, blocker, conflict, waiver, repair, reclassification outside the accepted taxonomy, lifecycle mutation, Git mutation, or project/canon change occurred.
