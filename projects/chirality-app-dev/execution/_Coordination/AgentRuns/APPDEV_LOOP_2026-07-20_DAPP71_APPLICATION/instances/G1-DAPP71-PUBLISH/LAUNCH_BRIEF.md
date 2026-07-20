# G1-DAPP71-PUBLISH Launch Brief

- **Role:** CHANGE (Agent 1; load and obey `agents/AGENT_CHANGE.md`)
- **Parent/dispatcher:** HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-20_DAPP71_APPLICATION`
- **Branch:** `codex/app-dev-dapp71-application-20260720`
- **Basis commit:** `3346120cb7c765aa7a230ee4c579ecd14f2cb022`
- **Integration branch:** `main`
- **Release update:** `../../updates/v3.md`
- **Release-update SHA-256:**
  `0f5c9e81dc31c82f53ce7c87e31f9d31dcda0cdcbfd9270457d225d8665fee55`
- **Released STATUS SHA-256:**
  `50b5b607d7201d9ee01496fca7f68cde2789ede73a219a233bd4c5b06ac75f15`
- **Closeout mode:** commit, push, ready PR, required-check wait, normal merge
  commit, remote verification
- **Merge authority:** user's standing approval for this session permits
  self-merge
- **File edits / new receipt:** prohibited

## Objective

Publish the exact accepted D-APP-71 application and its complete control and
evaluation evidence. Fetch and recheck `origin/main`; stage only the frozen
publication population; commit and push the current branch; create a ready PR
to `main`; wait until every required check is green; and, only while the PR is
head-stable, conflict-free, authority-safe, and exactly contained, merge it
using the repository's normal merge-commit method. Verify the resulting remote
main merge commit and its parents.

Do not repair or edit content. Do not append Receipt-83. The released
`STATUS.json` is an immutable release token and remains `READY_RELEASED` in the
published commit; report terminal CHANGE evidence to HELP_HUMAN through the
managed return, not by creating or modifying another file.

## Frozen accepted fan-in

Require V1 terminal `ACCEPT` and reproduce:

- RETURN `845a9fff090b1e480b1acd3670ed040f6079bad2690768b5757b1ba52ed5ec9a`;
- HANDOFF `356a2d6a31089ddb62ea09b15022346b10ed82ddbedff96fc7524ad471835086`;
- STATUS `3904c445bd6e2adca6452fbe3106d1f8c530c69e7293ef43329626849b35dd89`;
- evaluation manifest
  `e26270e685857ba55af05a7f369712ea3dcde9e4def5957e122fada48debef85`.

Require the exact 30-path pre-release population, every individual path/hash,
state population `3 modified + 27 untracked + 0 staged`, sorted path-list hash
`cdf529b2034c3474028a2f8e62ea7ece861523a8b0ee813fff130a1f8c286710`,
and sorted content-manifest hash
`4d20cedd3edd8bd7982eeb6a1aa8779c69a545ce976dc658ce925286f23d83eb`
from `updates/v3.md`. Do not substitute a directory-level status summary for
the 30 individual hashes.

The final publication population is exactly those 30 paths plus:

1. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOOP_2026-07-20_DAPP71_APPLICATION/updates/v3.md`;
2. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOOP_2026-07-20_DAPP71_APPLICATION/instances/G1-DAPP71-PUBLISH/LAUNCH_BRIEF.md`;
3. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOOP_2026-07-20_DAPP71_APPLICATION/instances/G1-DAPP71-PUBLISH/STATUS.json`.

At activation, compute and freeze all three release-control hashes in the
terminal return. Before staging, require exactly 33 paths total: three
modified, 30 untracked non-ignored, zero staged, no rename/deletion, and no
ignored/generated path in the publication set. Any extra, missing, or changed
path returns `BLOCK`.

## Mandatory preflight and validation

1. Resolve the repo root, load `AGENTS.md`, `agents/AGENT_CHANGE.md`, this
   brief, and v3. Require the exact branch and basis HEAD; verify no merge,
   rebase, cherry-pick, bisect, or other Git operation is in progress.
2. Reproduce all v3 subject/control/evaluation hashes, the three release
   controls, the exact 33-path population, and zero staged state. Require
   `frontend/electron/preload.ts` unchanged at
   `189b0d30bd8f6daf84862e14cfc3ec68c2c211b5c123283c7108c50c3b750ba0`.
3. Run, without producing publishable generated artifacts:
   - `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .`;
   - from `projects/chirality-app-dev`,
     `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status`;
   - `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py --repo-root . self-check`;
   - `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tools/validation`
     and require exactly `123 passed`;
   - `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tools/practitioner_harness`
     and require exactly `311 passed`.
4. Require receipt validation PASS, corpus v9 8/8 no-drift, self-check exit
   zero at the existing 3 REVIEW / 6 WARN baseline, `git diff --check` PASS,
   per-untracked-file no-index whitespace PASS, and no generated/ignored path
   entering the publication population. Frontend gates remain skipped because
   runtime source is unchanged; verify that rationale.
5. Fetch `origin main` and record pre-publish `origin/main`. If it differs from
   the basis, inspect every intervening commit/path and perform a merge-tree or
   equivalent conflict check. Return `BLOCK` if any change overlaps a frozen
   path, changes the governing instruction/authority basis, supersedes
   D-APP-71, creates a semantic/merge conflict, or makes safe integration
   uncertain. Do not rebase or merge main into the source branch.

## Exact staging and commit

- Stage by explicit pathspec only: the 30 v3 paths plus the three release
  controls. Never use `git add -A`, `git add .`, a broad glob, or an unresolved
  generated list.
- After staging, require exactly 33 staged paths and no unstaged or untracked
  non-ignored path. Rehash every staged blob and require equality to its
  frozen worktree hash. Require `git diff --cached --check` PASS and rerun the
  exact containment comparison.
- Commit once with a concise message such as
  `Apply D-APP-71 preload coordination lead`. Do not amend, rebase, or create a
  merge commit on the task branch.
- Require the commit to contain exactly the 33 paths and revalidate the commit
  tree hashes. Push the current branch normally with no force option. Record
  commit SHA and remote branch SHA equality.

## Ready PR and guarded normal merge

1. Create one ready-for-review PR from the exact source branch/commit to
   `main` (or reuse only an already-existing open PR whose base, head branch,
   head SHA, scope, and non-draft state match exactly). The PR description
   must identify D-APP-71 Option 2, coordination-only semantics, the retained
   three boundaries, derivative/evaluation evidence, checks, runtime-test skip
   rationale, and no lifecycle/release/hard-fence effect. Do not make a release
   readiness or professional claim.
2. Wait for every required repository check to finish. Any failure,
   cancellation, pending timeout, missing required check, or ambiguous branch
   protection state returns `BLOCK`; do not merge or bypass checks.
3. Immediately before merge, fetch/requery `origin/main`, PR head/base,
   mergeability, required checks, review/authority state, and exact head SHA.
   Re-run advance/overlap/conflict safety if main moved. Do not proceed if the
   source head changed, the PR is draft, checks are not all green, mergeability
   is not clean, or authority/scope is uncertain.
4. Merge the exact PR/head using the normal merge-commit method (`--merge` or
   repository equivalent), never squash or rebase. Do not enable auto-merge.
5. Fetch remote main and prove the new merge commit has exactly two parents:
   first, the immediately pre-merge `origin/main`; second, the exact task
   commit. Prove `origin/main` equals the merge commit, the PR is `MERGED`, and
   the source branch/worktree is clean. Report PR URL/number, task commit,
   check results, merge SHA/parents, and any remote-main movement.

## Failure and absolute prohibitions

On any mismatch or unsafe condition, return `BLOCK` with exact evidence and
the smallest next action. Do not repair files, add a receipt, stage a partial
set, resolve semantic conflicts, bypass checks, or broaden authority.

No content edit; no Receipt-83; no squash; no rebase; no force push; no branch
delete; no cleanup; no ignored-file deletion; no worktree removal; no reset,
checkout-overwrite, amend, history rewrite, release/publication act, lifecycle
act, hard-fence crossing, or waiver. No action after a successful verified
merge other than reporting the terminal evidence.
