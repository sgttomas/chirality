# change — method

## Method

A WORKING_ITEMS session follows a short flow; the mechanics of each step are ordinary Git competence and left to agent judgment.

1. **Initialize.** Resolve the repository, `EXECUTION_ROOT` when the project has one, and the session identity. Look for the repository's change conventions (project instruction file, project-scoped change skill, contributor documentation, required CI) and the authorization the user or those instructions actually give; record them with the defaults and assumptions used. Note whether the `_Change/` tool roots exist; create them only when a session log is requested.
2. **Collect state evidence (no local mutation).** Gather current branch and HEAD, upstream, staged/unstaged/untracked summaries, renames/deletions, ahead/behind status, existing worktrees, relevant task branches, and any in-progress Git operation. Fetching is permitted; do not otherwise mutate state while collecting.
3. **State Report.** Produce a decision-ready report with strict separation of Observations, Interpretations, Risks, and Options (see the contract's State Report structure). Default to low noise; show full diffs only when needed.
4. **Plan (if requested).** Write a Change Plan (files, edits, why; flag any destructive operation). For concurrency, classify `SHARED_CHECKOUT` vs `ISOLATED_WORKTREE` and, when isolating, produce a Worktree Lane Plan recording purpose, owner, base ref + SHA, scope paths, and expected closure/checks; check for name collisions and never base a new lane on a dirty worktree without explicit approval. For merges, summarize readiness in the existing pull request or closeout record, classifying each lane `READY` / `CONDITIONAL` / `BLOCKED` (never propose a merge for a `BLOCKED` lane except as a deliberate human-approved exception with risks stated). When the work reveals a workflow or tool design need, describe the observed friction and required behavior for HELPS_HUMANS. WORKING_ITEMS implements an accepted design only within its authorized undertaking.
5. **Check and review.** Run the repository's applicable registered checks against the actual candidate and review the final diff, including staged content, before committing or publishing. Reassess affected checks after any change to the candidate.
6. **Execute within authorization.** Stage only the scoped change. Commit when closeout is requested or the repository makes it routine. Push, open or update a pull request, and merge only under authorization the user or the repository's instructions actually grant, and only when that authorization's conditions hold (for example required CI and review covering the actual candidate, with no unresolved blocking findings). Verify the source HEAD when merging. Explicit holds prevent the action. Use the configured identity and truthful attribution, and report the pull-request, source, and merge revisions. When authorization stops short, stop at the last authorized step, state the assumption, and name the remaining action and the authority it needs. Destructive or history-rewriting actions always need separate explicit authorization; covered Git operations require no approval token.
7. **Optional session log.** If a log path under `{EXECUTION_ROOT}/_Change/` is provided, record session identity, conventions and authorization applied, assumptions, state report, any lane plan / readiness summary / merge result / design handoffs, actions executed, and resulting state.

## Recovery

If a check fails, review finds a blocking issue, or integration conflicts with other work, stop before publishing, report the state, and repair within scope or route the decision. If the session is interrupted, the next session restarts from step 2: Git state, not a prior report, is the basis for resuming.

---
