# RV126: RV-N, the fresh independent review of PR-N (the correctly rounded norm)

TASK (Type 2): an independent reviewer dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You wrote none of this code.** Read `R/BRIEFS/B1_COMMON.md` for the host, records and placeholder rules, with WORKING_ITEMS in ROOT's place.

## The candidate

- **PR-N's code commit `8dd64c1835`** on `codex/piping-t3-correct-norm-20261008` (`WT/pr-n`): one commit on main `7eae707bb7`, with 21 maintained files. A package commit (`T/IMPLEMENTATION/PR_N/`) follows, and WORKING_ITEMS will send you its head.
- **The implementer's records:** `R/I109/platform_norm_01/RETURN.md` (the norm, the oracle, the libm inventory, the moved bytes) and `R/I109/pr_n_01/RETURN.md` (the re-pins, glibc's reading, the D1 call sites).
- **The rulings:** RR "I109: a correctly rounded norm replaces libm `hypot` on published paths; …" and "RV125 confirms PR-B1's platform test repair; …" (A1-N1).

## Review, in priority order

1. **The norm's correctness** (`FK/src/correct_norm.rs`). Read the algorithm and its proof sketch, and the special cases (zeros, signed zeros, infinities, NaN, subnormals, overflow scaling) against `hypot`'s contract. **Check correct rounding independently:** write your own exact oracle (big-integer square root or `fractions`), with your own random and adversarial generator, at least 10⁶ cases including near-midpoint triples and the extreme exponents, and report misrounded results. Reuse I109's harness only to cross-check.
2. **Every call site** (the 30 product replacements and the rank screen): it has the right arity and semantics (3-norm against chain; the rank screen's thresholds take the **admission view**, so a changed decision would be a defect). No published-path `hypot` is left out, and nothing outside the published paths changed without reason.
3. **The re-pins:** each moved value is the correctly rounded norm of its own components, and each hash follows from the moved value. B1's glibc variants are gone with no pin weakened, u1 is unconditional, m08 uses `norm2`, and the ring check is tightened as RV125 A1-N1 asked.
4. **Scope truthfulness:** the commit message, the maintained comments and, later, the package claim no more than the evidence shows. That includes the platform-independence wording and the remaining libm calls (sin, cos, atan2, asin, exp, exp_m1).
5. **Your own spot checks,** in an archive copy: PP's and `result_export`'s suites, and the PY and TS reader suites that read the corpus.

## Host and output

- Your copy is a `git archive` of the head into `WT/rv126/`, with targets under `WT/targets/rv126*` and scratch in `WT/scratch/rv126_n/`. Delete the copies afterwards. Every cargo goes through `WT/tools/t3_cargo.sh`. No Git writes, installs, DEC-025, or RSS or solver-at-scale jobs.
- **The record:** `R/REVIEW_RV126/pr_n_01/REVIEW.md` plus SHA256SUMS. It gives the verdict (PASS or FAIL), the BLOCKING, SHOULD-FIX and NOTE counts, and a findings table with path:line, evidence and remedy. Placeholder paths only. If the host refuses the file, put its full content in your final message with the intended path; do not work around the refusal.
- After repairs, you confirm them. Time box: 4 h.

End your turn with:
- the verdict and counts, with one line per finding;
- your oracle's result;
- REVIEW's sha256;
- anything WORKING_ITEMS must bring to ROOT.
