# RV132: confirm I107's Pass B on #1168 (U3), in RV124's role

Reviewer (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You are a fresh instance.** `R/BRIEFS/B1_COMMON.md`'s host and records rules apply, with WORKING_ITEMS in ROOT's place.

## What you confirm

**The candidate:** PR #1168 (U3, the legacy pressure contract retired product-wide), branch `codex/piping-t3-pressure-retire-pr-20261009`.
- **Head:** `37724dea27`.
- **Code commit:** `8a12de28db`, cut from main `ba500defa4`.
- **Pass B ran on `8a12de28db`.** Outside the execution records, the only code-tree change from there to the head is `ed012c7ccf`, which deletes the three retired fixtures `invented_mechanics_result.json` and its two `_precision_1_` forms (RV127 A2-B-1).

**I107's Pass B:** `R/I107/u3_passb_01/`, RETURN.md sha256 `8fd9fc5d1c5fd4c1ff0b25d49632a51782839775f6c3c3d34acce375988cfe01`, with SHA256SUMS. VERDICT: DELTAS TO READ, exit 6. Every equality gate that compares with SQ's records or with main is traced by a reading, and I107 reports every reading as 0.

**The precedent:** RV124's confirmation of PR-N's Pass B, `R/REVIEW_RV124/pr_n_passb_01/CONFIRM.md`. Follow its method and form. The Pass B brief is `R/BRIEFS/U3_SB.md`.

## The checks

1. **Each "reading 0" trace.** For every gate at 6, re-run or re-derive the reading that traces it: `forms_u3`, `noncand_u3` and `controls_u3` in the pass, and `law_u3`, `outcomes_u3` (PP and the runner) and `challenge_u3` after it. Confirm that each reading is 0, or name what is not.
   - Use I107's tools with cargo skipped, retargeted to your scratch, as RV124 did.
   - If you rerun the line map or the delta tool mechanically, refresh I65's fingerprints first (RV124 C-N1).
2. **The delta:** 133 files and 327 rows, all classified, with 129 entries (125 production, 4 qualification) and 0 refused.
   - Reproduce the inventory independently.
   - Check a sample of each kind (R, S, W, F, T, A, H, Z, Q) against the code, with every F, H, Z and Q row read in full.
   - Check that S, H and Z rest on premise P0 (every legacy pressure primitive is refused first), and that P0 holds in the code.
3. **The 800 B account.** Every phase in both modes is exactly 800 B lower: 9 × 32 B for `(&str, StressRecoveryResult)` (192 → 160) and 64 × 8 B for `(String, DerivedSection)` (88 → 80).
   - Check the layouts and the coefficients.
   - Check that the committed GENERATED PROFILE blocks are unchanged, and that they over-price rather than under-price U3's code.
   - Check this against RR "U3 Stage 2 rulings: the 800 B profile re-pin, …".
4. **TEXT, the one reading left:** T2's corrected limitation text adds 116 B requested in `preview_formulation_basis`.
   - Read it against RR "Owner decisions: T4 starts now; …", paragraph "U3, T2's re-pin check, option (a)", and RR "U3, T2's outcome under the extended check; …".
   - Say whether the 116 B is exactly the string's growth.
   - Say whether it stays within the priced text budget (the committed profile and M = 11,274,289,152 B), and whether any re-registration follows.
5. **Carry-over to `37724dea27`.** Under RR "#1168: RV127's A2-B-1 … which gates carry", decide whether Pass B carries from `8a12de28db` across `ed012c7ccf`. In particular:
   - no product or test code reads the three deleted fixtures;
   - no Pass B gate input changes;
   - `git diff --no-renames 8a12de28db 37724dea27` outside `P/execution` is exactly the three deletions.
6. **I107's notes (a) to (c).** Note (a) says the PR keeps the three fixtures that NUM deleted. `ed012c7ccf` deleted them on the PR after I107's run. Confirm that the head no longer has them.

## Verdict and record

- **The verdict:** CONFIRMED, or NOT CONFIRMED with the reason. Give findings as BLOCKING, SHOULD-FIX or NOTE, and say plainly whether Pass B carries to `37724dea27`.
- **Records** go directly in `R/REVIEW_RV132/u3_passb_01/` in NUM: CONFIRM.md, `evidence/` and SHA256SUMS. Use placeholder paths only. If the host refuses a file, give its full content in your final message with its intended path; do not work around the refusal.
- **Host:**
  - Git reads only, and no Git writes.
  - No cargo and no measurement. Python goes through `WT/venv/bin/python` (with `-I` when it reads repository files), and heavy jobs through `WT/tools/t3_slot.sh`.
  - No DEC-025 and no installs, and never signal another job.
  - Scratch goes in `WT/scratch/rv132/`. Read I107's scratch only.
- **Budget:** about 1.5–2 h.

End your turn with:
- the verdict;
- each reading's result;
- the delta check;
- the 800 B account;
- TEXT;
- the carry-over;
- the findings.
