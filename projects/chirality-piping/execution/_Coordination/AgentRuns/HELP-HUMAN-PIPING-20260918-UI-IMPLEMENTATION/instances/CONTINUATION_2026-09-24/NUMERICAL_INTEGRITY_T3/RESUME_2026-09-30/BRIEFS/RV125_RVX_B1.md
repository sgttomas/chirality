# RV125: RV-X, the fresh independent complete-diff review of PR-B1

TASK (Type 2): an independent reviewer dispatched by ROOT (HELP_HUMAN, Agent 0). ROOT is your return path, and you do not delegate. **You wrote none of this code. Earlier reviews feed your ledger; they do not replace your own reading.** Read `R/BRIEFS/B1_COMMON.md` for the host, records and placeholder rules.

## The candidate

- **PR-B1:** `codex/piping-t3-pr-b1-20261008` (`WT/pr-b1`), cut from main `6c821d9ccf`.
  - Commit 1, `8248921552`, holds the 33 maintained files that NUM `a41eea7b5f` changes.
  - Commit 2, SK's evidence package at `T/IMPLEMENTATION/B1/`, lands later; ROOT will send you its head.
  - **Start on commit 1 now.**
- **The plan:** PLAN_v2 (`R/I84/b1_plan_01/PLAN_v2.md`) and its gate set. Every B1 ruling in RR from "B1's PLAN_v2 accepted; …" through "R6b: …".
- **The slice reviews:** RV-P (RV109), RV-R (RV113, RV120), RV-Q (RV112, RV124) and the SA reviews, under `R/REVIEW_RV*/`.

## Review, in priority order

1. **Source equality.** Rerun `T/IMPLEMENTATION/F2A_D1/source_equality.py --repo WT/pr-b1 --pr <head> --int a41eea7b5f --main 6c821d9ccf --work WT/scratch/rv125_b1_x/seq`. No execution records are allowed in commit 1.
2. **The complete diff against main, read in full.**
   - Build a ledger mapping each file and hunk group to the review that covered it, with the reviewed commit.
   - **Read yourself every hunk that no review covered, or that changed after its review.** Merges of main and repair rounds are the usual source.
   - Look for correctness defects first: case indexing across C = 3, custody of per-case state, failure atomicity, ordinal mapping, the wire and receipt for several cases, and the readers' agreement.
3. **Scope truthfulness.** Maintained comments, and later the PR body and CHANGE_RECORD, say exactly what is public:
   - the Direct entry in the registered dev/test build only, with M = 11,274,289,152 B;
   - C ≤ 3 at S3;
   - the readers and 07n.

   What stays closed: product callers and public activation (B8); Stale builds; any supported-machine statement; B2, B3, S-I2, F2b and F3. No maintained text may claim more.
4. **M and the registration.** `threshold_bytes` and its comment agree with SQ's QUAL_B1 and RR R6b. The reviewed profile inputs and PP's `Cargo.lock` are unchanged except as recorded.
5. **Your own spot checks,** in an archive copy:
   - a three-case input through the Direct entry in the registered build, in both modes, against SP's pinned bytes;
   - one Stale build giving the ordinary bytes;
   - the three readers on the multi-case successor, with and without its invocation;
   - a pressure input refused at D1.5.

## Host

- **Your copy:** a `git archive` of the PR head into `WT/rv125/`, with targets under `WT/targets/rv125*` and logs in `WT/scratch/rv125_b1_x/`. Delete the copies afterwards.
- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`). **Other heavy commands** go through `WT/tools/t3_slot.sh`. One heavy job at a time. Never signal another job.
- vitest runs in an archive, as `T/IMPLEMENTATION/B1_I4/` shows.
- **Not allowed:** Git writes, installs, DEC-025, and RSS or solver-at-scale jobs.

## Output

- **The record:** `R/REVIEW_RV125/b1_x_01/REVIEW.md` plus SHA256SUMS:
  - a verdict, PASS or FAIL;
  - BLOCKING, SHOULD-FIX and NOTE counts;
  - a findings table with path:line, evidence and remedy;
  - the ledger.

  Use placeholder paths only.
- **After repairs,** you confirm them.
- **Time box:** 5 h.
- **End your turn with:**
  - the verdict and counts, with one line per finding;
  - the report's sha256;
  - anything ROOT must rule on.
