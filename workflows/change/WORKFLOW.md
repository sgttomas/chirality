---
name: change
description: Prepare and close a coherent Git change in any repository, isolating the work when warranted, checking and reviewing the diff, and committing, pushing, opening a PR, or merging only as far as the user or the repository actually authorizes.
---

# change

Prepare and close a coherent Git change with inspectable evidence, preserving
unrelated work and the human's existing decision rights. The method is
repository-agnostic. A repository's own conventions specialize it where they
exist.

WORKING_ITEMS coordinates this undertaking and may assign bounded contributions
to TASK.

## Method

1. Inspect the working tree, branch, upstream, in-progress Git operations,
   other worktrees, ownership of pending changes, and the accepted scope of the
   change.
2. Isolate the change proportionately: stay in the shared checkout when write
   scopes are disjoint; use a branch or branch-and-worktree lane when the human
   asks or isolation materially reduces risk. Warn about overlapping lanes.
3. Prepare the change and resolve integration issues while preserving
   unrelated work.
4. Run the repository's applicable registered checks and review the final diff
   before committing or publishing.
5. Close out within authorization. Commit when closeout is requested or the
   repository makes it routine. Push, open or update a pull request, or merge
   only when the user or the repository's instructions actually grant it. Otherwise stop at the last authorized step, state that assumption, and
   name what remains.
6. Present a truthful State Report of the resulting state.

## Authorization and repository conventions

Selecting this workflow grants no Git authority. Without an authorization the
user or the repository's instructions actually give, do not push, open or
update a pull request, or merge. Repository conventions, such as a project
`AGENTS.md`, contributor guide, or project-scoped change skill, specialize
branch naming, the integration branch, required checks and review, merge
strategy, standing Git authorization, and downstream notices. They cannot
weaken this method's invariants, and a grant in one repository does not carry
to another. Host permissions still bound every operation.

## Resources

Load [inputs, modes, and output contracts](resources/contract.md) when framing
the assignment. Use [the detailed method](resources/method.md) for the current
stage.
