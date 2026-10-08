# I109, round 4: PR-N's repair round 01 (RV126's S-1 and notes)

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), your return path. `R/BRIEFS/B1_COMMON.md`'s rules apply, with WORKING_ITEMS in ROOT's place.

**The basis.** RV126's review of #1163, `R/REVIEW_RV126/pr_n_01/REVIEW.md` (`3ca41a9e…`). The PR branch is `codex/piping-t3-correct-norm-20261008` in `WT/pr-n`, head `dab19291a8`. Commit there; WORKING_ITEMS pushes, and mirrors the product files into NUM.

## Rules for this round

- **Production files (PP, FK and stress_recovery `src`):** comment-only edits, each hunk line-neutral (the same number of lines), so the release builds are unchanged and Pass B, T9 and the both-entry gate carry over. If an item cannot be done line-neutrally, say so and leave it.
- **Test files and the package** may change freely.
- **One repair commit for code and tests, and one for the package.** Messages must be truthful. The repair commit's message states S-1's correction, since the code commit's message is not recut.

## Items now

- **S-1:** reword `PP/src/lib.rs:38`, CHANGE_RECORD.md:23 and PR_BODY.md. The magnitudes formerly formed with libm `hypot` are now correctly rounded norms. `source_receipt::scaled_norm` and `displacement_magnitude` are deterministic IEEE but not correctly rounded, and are unchanged.
- **N-1:** the header of `PP/tests/preview_physics_runtime.rs` should say that m08's expectation uses FK's `correct_norm::norm2`, which is verified against an exact oracle.
- **N-3:** CHANGE_RECORD.md:25. 30 of the 32 product `hypot` calls now call the norm: every one that reaches published bytes, a receipt or diagnostic text, plus the rank screen (admission) and `elastic_section` (no caller).
- **N-4:** the platform claim holds given a correctly rounded `fma`, hardware or the platform's own. Cite RV126's wasm32 = aarch64 result.
- **N-6:** cite the four TS files RV126 ran (1,314 passed), or name `retainedPrecision.test.ts` alone for your own run.
- **N-7:** record dispatch 37820998162 (success, numerical cargo suite included, 21 files equal to the code commit) and the full-SHA dispatch 37824479785 on `dab19291a8` (success).
- **N-8:** exact constants in `FK/tests/retained_k4/product_final_case_tests.rs:342` (13, 0, 4·2⁻¹⁰⁷⁴), or `norm3`.

## Items held for ROOT's B-1 ruling

N-2 (the two FK comments in `rigid_body.rs`) and N-5 (the rank screen's published node motions in the package) depend on whether the rank screen stays. WORKING_ITEMS sends the ruling; do them in this round if it arrives before you finish, otherwise leave them.

## Checks and records

- After the edits, run PP, FK, `result_export` and the PY/TS corpus readers in fresh targets.
- Rerun `source_equality.py` and `check_citations.py` against the new head, with `--int` the NUM commit WORKING_ITEMS gives you; if none is given yet, use a scratch head as before.
- Records go in `R/I109/pr_n_repair_01/` (RETURN.md, SHA256SUMS), placeholder paths only.
- If the host refuses a file, put its full content in your final message with its intended path.

End your turn with:
- the commits;
- the line-neutrality check per production hunk;
- the suites;
- any stop.
