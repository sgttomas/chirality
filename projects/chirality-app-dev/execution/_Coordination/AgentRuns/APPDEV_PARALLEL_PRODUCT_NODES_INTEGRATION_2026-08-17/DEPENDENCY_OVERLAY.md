# Transient Dependency Overlay

The integration checks use dependencies installed from the current App lockfile plus a temporary copy of the current worktree `runtime/` packages built under `/private/tmp`. Frontend `@chirality/*` dependency links are repointed only to that temporary built copy. No package manifest, lockfile, committed configuration, or root runtime source is edited.

All transient `frontend/node_modules`, build outputs, service logs, and temporary runtime copies are removed before handoff. Exact commands and outcomes are recorded in `CHECK_RESULTS.json`.

The proof ran over the combined node candidate rooted at base `44903bc69cf56d4ca794fe9629f26793a82bf1b3`. Its accepted node payloads are now immutable in PKG-08 commit `ac2cd801a06a0679bc86830c627218ccca78b658` and descendant PKG-05 commit `d563af0aa7d5935260864d7e6084262eaee0b3d4`; no dependency overlay is retained in either commit or this closeout candidate.
