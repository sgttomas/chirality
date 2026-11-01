# change — method

## Method

A WORKING_ITEMS session follows a short flow; the mechanics of each step are ordinary Git competence and left to agent judgment.

1. **Initialize.** Resolve the repository, `EXECUTION_ROOT` when the project has one, and the session identity. Look for the repository's change conventions (project instruction file, project-scoped change skill, contributor documentation, required CI) and the authorization the user or those instructions actually give; record them with the defaults and assumptions used. Note whether the `_Change/` tool roots exist; create them only when a session log is requested.
2. **Collect state evidence (no local mutation).** Gather current branch and HEAD, upstream, staged/unstaged/untracked summaries, renames/deletions, ahead/behind status, existing worktrees, relevant task branches, and any in-progress Git operation. Fetching is permitted; do not otherwise mutate state while collecting.
3. **State Report.** Produce a decision-ready report with strict separation of Observations, Interpretations, Risks, and Options (see the contract's State Report structure). Default to low noise; show full diffs only when needed.
4. **Plan (if requested).** Write a Change Plan (files, edits, why; flag any destructive operation). For concurrency, classify `SHARED_CHECKOUT` vs `ISOLATED_WORKTREE` and, when isolating, produce a Worktree Lane Plan recording purpose, owner, base ref + SHA, scope paths, and expected closure/checks; check for name collisions and never base a new lane on a dirty worktree without explicit approval. For merges, summarize readiness in the existing pull request or closeout record, classifying each lane `READY` / `CONDITIONAL` / `BLOCKED` (never propose a merge for a `BLOCKED` lane except as a deliberate human-approved exception with risks stated). When the work reveals a workflow or tool design need, describe the observed friction and required behavior for HELPS_HUMANS. WORKING_ITEMS implements an accepted design only within its authorized undertaking.
5. **Check and review.** Run the repository's applicable registered checks against the actual candidate and review the final diff, including staged content, before committing or publishing. Reassess affected checks after any change to the candidate.
6. **Execute within authorization.** Stage only the scoped change. Commit when closeout is requested or the repository makes it routine. Push, open or update a pull request, and merge only under authorization the user, or repository instructions the user owns or has adopted, actually grant, and only when that authorization's conditions hold (for example required CI and review covering the actual candidate, with no unresolved blocking findings). Verify the source HEAD when merging. Explicit holds prevent the action. Use the configured identity and truthful attribution, and report the pull-request, source, and merge revisions. When authorization stops short, stop at the last authorized step, state the assumption, and name the remaining action and the authority it needs. Destructive or history-rewriting actions always need separate explicit authorization; covered Git operations require no approval token.
7. **Optional session log.** If a log path under `{EXECUTION_ROOT}/_Change/` is provided, record session identity, conventions and authorization applied, assumptions, state report, any lane plan / readiness summary / merge result / design handoffs, actions executed, and resulting state.

## Select the holding and its connected uses

Before editing, identify the holding's purpose, allowed scope, destination and
selected source revision. Read the relevant existing material and the tool's
actual usage contract before choosing commands. A missing tool or dependency is
an explicit limit: inspect files directly where that answers the question, or
hold the dependent operation. Do not invent an equivalent executable capability.

For an addition or revision, retain required resources and source identity and
check the result in its intended use. For organization, relocation or retirement,
inspect actual incoming references, consumers and generated indexes; path matches
are leads, not proof that all uses were found. Establish the replacement or
historical standing and recoverable basis before changing paths. Distinguish
removing a working copy from deleting unique or uncommitted work. Preserve that
work and resolve missing deletion authority before removal. Check affected links,
discovery and consumers after the change; leave unexamined uses explicit.

For conflicting claims or connected changes, compare source meaning, actual
behavior, evidence and the work's owning material (its locality where the
repository has one). Where the repository maintains deliverable commitments,
work material and dependency documents, use the selected library's
[bounded reconciliation](../../bounded-reconciliation/WORKFLOW.md) for that
same-change comparison. This route does not add another audit.
Use the repository's publication and consumer-update guidance for version basis,
change accounts, dependencies, limitations and independent adoption. Identify
its actual location through repository conventions. If unavailable, report the
missing route before claiming publication readiness; a merge is not a release.

When the holding is a maintenance instruction, use the preceding applicable
[create-workflow](../../create-workflow/WORKFLOW.md) method for a reusable workflow
revision. Preserve the selected origin and previous revision through Git or the
library's authorized retention mechanism. Keep the old entry/method usable until
the replacement is checked and adopted. Check both the changed holding and the
means used to maintain it. Proposed text cannot authorize its own adoption or
retroactively govern its review.

## Recovery

If a check fails, review finds a blocking issue, or integration conflicts with
other work, hold the affected integration and repair within scope, route it to
its owner, or return the reserved decision. A clearly labelled draft may be
shared for review within actual authority; failed checks remain visible.

After interruption, restart from step 2 and read the work's owning material
(its locality where the repository has one), current steering and actual review
record together. Establish the selected source basis, usable completed and
partial work, applicable checks, open conditions, next
needed action and current authority. Inspect uncommitted/ignored work and any
active operation before repeating a command whose confirmation was lost. A prior
report cannot substitute for actual state, and Git state alone does not establish
purpose, suitability or authority to resume. Historical work creates no backlog.
Keep at most one replaceable recovery note only if these sources are insufficient.

For an exceptional operation needing exclusive custody, use an existing
coordination or locking mechanism. In its existing assignment or review record,
name the holder, exact item and reserved operation, who may resolve interruption,
and the conditions for release or transfer. Keep normal readers on last
checked-in material. Disjoint assignments and an acknowledged reservation can
coordinate cooperating workers; they do not prevent another process from writing.
If stronger exclusion is necessary but unavailable, hold that operation and
expose the missing capability instead of claiming a lock.

On interruption, preserve the item and inspect actual partial work and active
operations. The authorized maintainer decides whether to resume, transfer or
release; silence or elapsed time grants no disposal authority. Resolve uncertain
ownership before overlapping writes. On completion or authorized transfer, update
the existing coordination record so the next worker can tell who may proceed.
Check that retained work and reader access survived. Before claiming enforcement,
exercise the applicable release/recovery behavior and state its observed limits.
Reuse passing evidence where its basis and conditions support the actual claim;
this does not require a fresh exercise for every custody use. Procedural
coordination or a walkthrough cannot establish a host-enforced guarantee.

---
