# Attempts

1. `reconcile.py` initially addressed `WORK_GRAPH.json` human gates as
   `gates`; the live schema uses `human_gates`. The failed traceback was
   inspected, the owned reader was corrected, and the full audit was rerun.
2. The first control-preservation query included whole-project development
   changes outside the 154 deliverable directories. It was narrowed to the
   frozen member set, preserving the actual invariant: only the five
   representation paths changed inside any member directory.
3. The first App test attempt used a frontend-only disposable copy. Four of
   717 tests failed only because repository-level fixtures were absent; 708
   passed and five were skipped. Output is retained as `checks/app_tests.txt`.
4. R1 mounted fixtures one directory too shallow for tests that resolve the
   repository by the production frontend's path depth. Four fixture `ENOENT`
   failures remained; 709 passed and four were skipped. Output is retained as
   `checks/app_tests_r1.txt`.
5. R2 ran in the detached exact-main repository layout with only an ignored
   dependency symlink, removed immediately afterward. It passed 713 tests with
   four skips. The detached worktree remained clean.

No failed attempt changed project, lifecycle, dependency, rollback, H2, or
retirement state.
