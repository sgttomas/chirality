# Owner requirement — synchronize before Runtime reference

Exact owner message:

> The Runtime build is proceeding in parallel to your work here, so if you need to refer to it you must always sync your worktree first so you can pull in the updates from origin/main.

This requirement applies before every further Runtime reference. CHANGE performs safe fetch/synchronization preserving the dirty App work, with overlap/source/dependency assessment before any required integration. The actual sync-v1 fetch was a no-op at ec491aee: this is point-in-time evidence, not continuous/background freshness. A later Runtime reference requires a new sync. No new publication or unrestricted history-rewriting authority is inferred.
