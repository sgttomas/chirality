# Brief AR: independent review of PR #1094 (App v4 reading sentence; Agent User Manual alignment; piping entry pointers)

TASK (Type 2), an independent reviewer for HELP_HUMAN (ROOT), run `ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`. You return to ROOT and do not delegate. **You wrote none of the reviewed text**: AM drafted the AUM edits, and ROOT applied them and wrote the rest.

## The candidate

PR https://github.com/sgttomas/chirality/pull/1094, branch `codex/root-loopinit-aum-alignment-20261005`, at the head named in your dispatch. It was cut from main `a2addb20d2`, which then merged main `87661be164` (#1092).

## Basis

- **The owner's direction and ROOT's rulings:** `RUN2/OWNER_DECISIONS.md` and `RUN2/RULINGS.md`.
- **The drafted edits:** `RUN2/AUM_EDITS.md`.
- **Piping's binding-form LOOP_INIT** (merged in #1092), and its run `projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING-LOOP-INIT-20261005/`. Its `CONSISTENCY_EDITS.md` §B and §C1 list the edits this PR carries.
- **The bundled workflows** `construct-local-work-graph`, which #1093 revised, and `bounded-reconciliation`.
- **The Field Book.**
- **Root `AGENTS.md`.**

## Review, in priority order

1. **App v4's LOOP_INIT:**
   - exactly one sentence changes, as the owner directed;
   - the notice to App v4 is accurate, including its three pinned hashes and the claim that no test compares them;
   - nothing else in App v4's live instructions conflicts.
2. **The AUM Markdown:**
   - every edit E1–E17 is applied exactly, and nothing else changed (diff against main);
   - each edited statement is true at the new basis `87661be164`;
   - each re-pointed citation lands on text that carries the cited rule. Verify a substantial sample, verbatim;
   - no `[Piping loop §…]` citation remains;
   - every link resolves;
   - App v3, Runtime and PEC statements that the edits touched are still true;
   - nothing the edits should have caught remains. Search for statements about piping's or App v4's LOOP_INIT that are now false;
   - ROOT's rulings 3–6 on the scope are sound.
3. **The AUM HTML:**
   - it is the renderer's output for the Markdown at the head, with basis date 2026-10-05 and revision `87661be164`. Reproduce it with `python3 docs/alignment-manual/render_manual.py`, using the same arguments and the in-place output path, and compare bytes;
   - the README's render command records that basis, and the Field Book's command is unchanged.
4. **Piping's pointer edits:** B1–B3 and the contributor guide's row 8 are minimal and true.
5. **The manifest:**
   - G4 passes, in CI mode and in diff mode against main with `--tranche ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`;
   - the authorization quote matches `OWNER_DECISIONS.md`;
   - the notice disposition and rationale are true.
6. **The piping run's records carried here:** LR's Addendum B and RULINGS Addendum C. Check they equal NUM's at its head; NUM is the T3 integration branch, `WT/numerics`.
7. **Portability and publication:**
   - GEN-8 on the head;
   - no new machine-absolute paths;
   - no credentials;
   - the entrypoint validator passes.

## Host and method

- **Your copy:** read-only, in `WT/aum-pr`, the PR worktree. Do not modify it. Logs go in `WT/scratch/ar_aum_01/`.
- **The render:** write it to a scratch output under `WT/scratch/ar_aum_01/`. Only the source-link line will differ, because it is relative to the output path; account for that.
- **What you may run:** the GEN-8 pytest, the two validators and the renderer.
- No cargo, no other tests, no Git writes, no installs, and nothing in the system temp directory.

## Output

- **The report:** `RUN2/reviews/AR-AUM.md` plus `RUN2/reviews/SHA256SUMS`, with placeholder paths only. It contains:
  - a verdict, READY or REPAIR;
  - counts of BLOCKING, MAJOR, MINOR and NOTE findings;
  - each finding with its evidence and fix.
- **Time box:** 75 minutes.
- **End your turn** with the verdict, the counts, one line per finding, the report's sha256, and anything ROOT must rule on.
