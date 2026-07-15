# CHANGE-CLEAN-REPAIR Attempts

- Preflight test discovery initially targeted the nonexistent directory
  `tools/scope_of_work/tests`; Python returned `ImportError` and changed no
  repository state. The registered suite at
  `tools/scope_of_work/test_scope_of_work_tools.py` then passed.
- The first atomic-commit loop used `path` as a zsh variable, shadowing zsh's
  executable-search array. It failed before staging or committing any path.
  The corrected loop used `filepath` and completed all 57 commits.
- The first disposable App test copy contained only `frontend/`; four tests
  failed because repository-level `agents/`, `docs/`, and `.github` fixtures
  were absent. The complete-layout disposable rerun passed all 713 executed
  tests with four integration tests skipped. The failed attempt and its output
  remain retained.
- A final census spot-check initially searched for a nonexistent
  `schema_version: SOW_V1` field and assumed all eight PKG-00 exemptions had
  `ScopeOfWork.md` files. It reported a false 0/146 result and changed no
  state. The corrected production-schema marker
  `schema: chirality-deliverable-sow/v1` counts 146/146; the eight exclusions
  remain bound by the accepted reconciliation census.
