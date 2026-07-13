# C2A-R1 Manager Check Results

Verdict: `PASS`

## Focused scanner and runtime seam

Command: `npx vitest run` over the frozen project route, working-root route,
read MCP, mutating MCP, dependencies-register, workspace API, and contract
scanner test files.

- exit: `0`;
- test files: `7 passed`;
- tests: `76 passed`;
- scanner cases: `15 passed`.

## Registered and required checks

| Check | Result | Durable evidence |
|---|---|---|
| full frontend test | PASS — 97 files passed, 1 skipped; 713 tests passed, 4 skipped | `FINAL_AFFECTED_CHECK_RESULTS.json` |
| frontend typecheck | PASS | `FINAL_AFFECTED_CHECK_RESULTS.json` |
| practitioner self-check | PASS, exit 0 | `POST_REVIEW_CHECK_RESULTS.json` |
| frontend build + Electron typecheck | PASS | `POST_REVIEW_CHECK_RESULTS.json` |
| practitioner pytest | PASS — 264 passed | `POST_REVIEW_CHECK_RESULTS.json` |
| owned-server frontend premerge | PASS — Section 8 8/8; Section 9 report-only 16/16 | `FINAL_PREMERGE_CHECK_RESULTS.json` |

The owned Next server listened only on loopback for the registered premerge
check and was stopped immediately afterward; a post-check listener query was
empty. No substrate fallback was needed.

The self-check's pre-existing `REVIEW`, `WARN`, `INFO`, and `NOT_APPLICABLE`
observations remained non-blocking; the command exited `0` and reported no
C2A-R1-specific regression.

## Containment and hygiene

- `validate_change_scope.py` over the explicit source list: PASS, zero
  violations against the exact two allowed source paths;
- `git diff --check -- <two source paths>`: PASS;
- exact current SHA-256 identities are recorded in `CHANGED_PATHS.tsv`;
- unrelated dirty paths were preserved and `.claude-worktrees` was untouched;
- no Git, lifecycle, deliverable, receipt, release, H1, H2, or legacy-retirement
  action occurred.
