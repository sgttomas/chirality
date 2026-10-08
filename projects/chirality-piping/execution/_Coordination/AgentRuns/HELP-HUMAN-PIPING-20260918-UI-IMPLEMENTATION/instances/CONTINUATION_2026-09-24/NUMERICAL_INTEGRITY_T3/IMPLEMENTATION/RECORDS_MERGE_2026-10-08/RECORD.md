# Records-only PR #1114: squash-merged

**The merge.** [#1114](https://github.com/sgttomas/chirality/pull/1114) was squash-merged on 2026-10-08 at 04:26:34Z as `19280fb1ce`.
- **Its parent** is main `7b0170ed4d` (#1116). Main had moved twice since the cut on `f4358eb0be` (#1115 and #1116), both entirely under `projects/chirality-app-v4` (`_run_records/PARENTS.txt`).
- **Command:** `gh pr merge 1114 --squash --match-head-commit 8568fb2053`, with an explicit subject and body (`_run_records/SQUASH_BODY.txt`).
- **The squash's** `execution/` and policy file equal the PR head's.
- **NUM then absorbed main** at `e382f25ff9`. T3's rulings and work graph resolved to NUM's later appends, and NUM equals main outside `execution/`.

**The content.** NUM's `projects/chirality-piping/execution/` at `dc4ffdc7c8`:
- 1,108 added and 2 modified (the T3 rulings and the work graph), 0 deleted;
- E-17's two hash-bound entries appended to `projects/chirality-piping/validation/portability_policy.json`.

**Two commits:**
- `57f078b4c8`, NUM at `96cf68289f`;
- `8568fb2053`, the S-1 delta to NUM `dc4ffdc7c8`: RV109's ADDENDUM_01, E-18's two rewordings, the rulings and the work graph.

**Gates:**

| Gate | Result | Evidence |
|---|---|---|
| GEN-8 on the head | 1 passed (ROOT), and 1 passed (RV119, independently) | `_run_records/gen8.txt` |
| `validate_run_record_leaks.py` | PASS: 1,111 files against main at the time (1,109 against the PR's base, RV119), 0 credentials, 0 machine-local symlinks; one size warning | `_run_records/leaks.txt` |
| ROOT's host screen | Every hit read: pattern or rule text, the owner's own words, redacted placeholders, and the owner-kept line in I90's sealed script (S-1) | RR "RV119 passes #1114 with S-1; …" |
| Automatic CI on `8568fb2053` | 4/4 succeeded | `_run_records/CI_RUNS.txt` |
| Independent review | RV119: PASS (0/1/3) at `57f078b4c8`, then CONFIRMED at `8568fb2053` (ADDENDUM_01: 0/1/2) | `R/REVIEW_RV119/records_01/` |

**Not in the PR,** so they go with the next records PR:
- RV113's three confirmations. Its SR-PY addendum is held until RV113 removes the machine's names from its sanitizer before first commit.
- RV119's review and addendum.
- The handoff note and steer.
- This record.
- The rulings after `dc4ffdc7c8`.
