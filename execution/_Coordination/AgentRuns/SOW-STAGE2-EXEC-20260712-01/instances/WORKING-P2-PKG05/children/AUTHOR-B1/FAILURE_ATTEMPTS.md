# Retained attempts and safe mechanical repair

- Harness attempt 1 failed before candidate conversion because the accepted reusable harness asserted the literal branch name `main` even though this isolated worktree was correctly bound to the accepted commit on `codex/sow-i1-closeout`.
- The complete trace and exit are retained in `harness-attempt-1.*`.
- Repair: removed only the branch-name assertion from the locally owned wrapper while retaining exact `HEAD` and `origin/main` commit assertions. This changed no source, candidate semantics, authority, lifecycle, or acceptance criterion.
- Harness attempt 2 passed all five members without registered-tool retry or candidate remediation; its outputs and exit are retained in `harness-attempt-2.*`.
