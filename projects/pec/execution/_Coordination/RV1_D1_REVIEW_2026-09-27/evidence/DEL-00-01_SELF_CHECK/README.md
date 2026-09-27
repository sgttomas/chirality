# Evidence — DEL-00-01 RV1 SELF_CHECK

Reviewer `REVIEW-SELF-DEL-00-01-20260927-RV1`, 2026-09-27. Every command ran
read-only against the repository worktree at `a1735cc3b` (branch
`claude/pec-rv1-d1-review`; `{REPO_ROOT}` below) with cwd `{REPO_ROOT}`,
interpreter `python3` (CPython 3.13.7) and `PYTHONDONTWRITEBYTECODE=1`. Every
output went to a private `$TMPDIR` outside the repository. No `git fetch`,
checkout, write or commit was made in the worktree; `git status --short` was
empty at start and end.

| File | Content | Exit codes |
|---|---|---|
| `00_hash_checks.out` | SHA-256 of instruction sources, briefs, authority, method basis (`git show 2f825f180:…`), bytes under review, deliverable records, prior snapshots, checklists, preflight, act run root, intake, current basis, tools; `git diff --stat 189f205ff HEAD` over the decomposition and PRD (empty) | 0 |
| `01_checklist_rederivation.out` | `derive_review_checklist.py` twice; hashes; `cmp` against the manager's checklist | 0, 0; cmp 0, 0 |
| `02_prior_checklist_diff.out` | derivation from the prior SOW (`git show 7c250e370^:…`), diff against the current derivation | derive 0; diff 1 (source hash only); comparison 0 |
| `03_validate_scope_of_work.out` | `validate_scope_of_work.py` on the deliverable | 0 (`PASS format=SOW_V1`) |
| `04_strict_registers.out` | `validate_decomposition_registers.py --strict projects/pec/execution` | 1 (0 errors, 26 `XRG-013` warnings; recorded baseline) |
| `05_selfcheck_checks.out` | `ledger_check.py` (independent `D-PEC-105` ledger rendering) and `selfcheck_checks.py` (identity check C1, matrix closure C2, TBD inventory C3, AC-002 element check C4, REQ-005 path C5, state/currency wording C6, runtime-boundary elements C7, whitespace C8) | 0, 0 |
| `06_git_and_grep.out` | file history, pre-act preimage hashes, write sets of `5942c5033` and `7c250e370`, the first-produced Context section, candidate-validation AC-002 note, packet path, archived headings, decomposition rows, PRD §13 row, AGENTS.md L175, K-RUNTIME-1, dependency rows naming DEL-00-01, DEL-01-05/DEL-01-01 anchors | 0 unless shown |
| `ledger_check.py`, `selfcheck_checks.py` | the two check scripts, as run (arguments: `{REPO_ROOT}` and `$TMPDIR`; the ledger check reads preimages written to `$TMPDIR/pre/` by `git show 7c250e370^:<path>`) | — |

Outputs are stored as produced, except that machine-absolute paths are replaced by
`{REPO_ROOT}` and `$TMPDIR`, the interpreter path by `python3`, and trailing
whitespace left by `cut -c` truncation (one line in `06_git_and_grep.out`) is
stripped.

Rerun: export a fresh `TMPDIR`; recreate `$TMPDIR/pre/ADRs.md` and
`$TMPDIR/pre/ScopeOfWork.md` with `git show 7c250e370^:<path>`; run each
command as shown in the `.out` files from `{REPO_ROOT}`.
