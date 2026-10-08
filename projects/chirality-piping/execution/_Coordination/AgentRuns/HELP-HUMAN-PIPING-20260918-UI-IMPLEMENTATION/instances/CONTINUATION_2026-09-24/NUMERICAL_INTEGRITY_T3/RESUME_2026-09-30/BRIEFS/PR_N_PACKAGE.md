# I109, round 3: PR-N's evidence package

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), your return path. `R/BRIEFS/B1_COMMON.md`'s rules apply, with WORKING_ITEMS in ROOT's place. Keep it short: the owner directs production first.

## The PR

- **PR-N's code commit `8dd64c1835`** on `codex/piping-t3-correct-norm-20261008` (`WT/pr-n`). It is one commit on main `7eae707bb7` with the 21 maintained files that NUM `ef8ab78473` changes. The commit message corrects one overclaim: on glibc, every committed pin holds; it does not say that no published value moves.
- **Its gates, running now:**
  - RV126 (RV-N, the fresh review);
  - I107 (Pass B), which RV124 confirms;
  - I112 (T9 and the both-entry gate);
  - Linux dispatch 37820998162 on `7bd84e0526`.

  After the package: hosted CI, the full-SHA dispatch, GEN-8, and the exact-head DEC-025 with src-tauri.

## The package, at `T/IMPLEMENTATION/PR_N/`, in the form of `T/IMPLEMENTATION/B1/`, scaled down

- **CHANGE_RECORD.md:**
  - §1, what changes and why. Cover the norm, the call sites, the rank screen and the re-pins, and give the exact list of moved values with their components.
  - §2, scope: what is and is not platform-independent after this PR (the remaining libm calls).
  - §3, the evidence: the oracle, the 40 manifests, glibc's runs, and the reader suites.
  - §4, the reviews and gates as rows. Leave each row's verdict pending until WORKING_ITEMS gives it.
  - §5, the D1 call sites.
- **PR_BODY.md:** a short PR description. End it with the line "🤖 Generated with [Claude Code](https://claude.com/claude-code)".
- **The citation index** for `check_citations.py`, and SHA256SUMS.

Run, and record in `R/I109/pr_n_package_01/`:
- `T/IMPLEMENTATION/F2A_D1/source_equality.py`, with `--int ef8ab78473 --main 7eae707bb7 --package <the package>`, against a scratch head made of the code commit plus the package;
- `check_citations.py`.

Write the package files in NUM at that path. WORKING_ITEMS commits them and makes the PR's package commit. **If the host refuses a package file, stop and say so at once,** with the file's full content in your final message; do not work around the refusal.

End your turn with:
- the package's file list and sums;
- the source-equality and citation results;
- any stop.
