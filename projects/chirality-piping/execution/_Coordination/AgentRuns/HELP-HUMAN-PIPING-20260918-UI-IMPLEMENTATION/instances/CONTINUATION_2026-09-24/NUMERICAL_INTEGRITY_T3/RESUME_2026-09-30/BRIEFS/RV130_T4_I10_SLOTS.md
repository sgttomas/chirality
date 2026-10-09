# RV130: T3's independent review of T4-I10's slot table (T4-U3, the objective connector)

Reviewer (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You are a fresh instance** and have not seen this design before. `R/BRIEFS/B1_COMMON.md`'s host and records rules apply, with WORKING_ITEMS in ROOT's place. You review; you do not edit T4's files or branch.

## What you review

T4-U3 replaces the refused user-stiffness joint (M07; owner option A) with an objective connector, in every slot the old joint held. Many slots are on T3's surfaces: W1, W4, K-D5, S11-G, F1b, the NI tests, the site tables, the readers' codes and the reviewed inputs.
- **The design:** on branch `codex/piping-t4-pressure-stress-20261009` at `471ad93f48`, read with `git show` (never check out or write T4's worktree). `R4` is `P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/PRESSURE_STRESS_T4/`.
  - `R4/T4-I10/SLOT_TABLE.md`, sha256 `57a565e36b551a3595636f54d5c3378cc1f4a6fb02aacdbfadbb659f39456e99`;
  - `R4/T4-I10/RETURN.md` (items 1–11 for T3);
  - `R4/T4-I10/_run_records/` (`sites`, `b2_overlap`, `friction_basis`) and `SHA256SUMS` (`e8e7db1a…`).
- **The code basis:** `ed012c7ccf` (main plus U3), and `b2` `e582b61f9e` for overlap.
- **T3's authority:**
  - RR "Owner decision: M07's flawed joint element, option A; …";
  - RR "T4 plan 01's annex A: T3's agreement recorded; …", with `R/I115/t4_annex_check_01/`;
  - the five T3 constraints sent to T4-I10:
    1. incomplete or unmapped joints stay refused, under today's codes or named successors, with an old-to-new code map;
    2. the W4 tie reduction stays and only its producer goes;
    3. edits stay out of `retained_product.rs` and `PP/tests/s11f_site_test.rs` where possible, with exact hunks where not;
    4. W1 refuses component models before any joint-specific code;
    5. `preview_physics::LIMITATIONS`, reviewed-input text, PP's `Cargo.lock` and the priced layouts stay byte-identical.
- **T4's rulings** (`R4/T4_RULINGS.md` at `1b682630e4`): SP-1 as a declared exception; the refused-demo files; annotation joints refused on the exact route; `replaces_span` topology only.

## The checks

1. **Slot coverage.** Is every place the old joint reaches in the code basis a slot in the table? Re-derive the sites independently (do not only re-run `sites.py`) and list any missed.
2. **No silent skip (item 8, §4.2).** Every joint shape gets either a named refusal or a solve; check the old-to-new code map and the backstops (NI, W1, source, K-D5).
3. **T3's constraints 1–5:** hold, or the exact hunk and why.
4. **The mathematics on T3's surfaces:**
   - W4 (item 4): is the positive-definite connector a link, so that null(BᵀKB) = null(B) = rigid modes? Is PD decided exactly and libm-free? Is the PSD case correctly unqualified? Do the deleted K5-C and tripwire have a successor of equal strength?
   - K-D5 (item 5): is the decode of K from (H, Ls), and of aᵢ = Qᵢ·offset, input representation outside EF? Are the required kills real (undemoted connector cases at ordinary and UTM coordinates; a perturbed Ke demotes)?
   - S11-G (item 6): is +BᵀKq_ref a formed `Formation::Bounded` term, self-equilibrated? Are connector rows rightly outside R-b′, recovered with `ExactAccumulator`, with `RecoveryRecord` unchanged?
   - F1b (item 7): does it fail closed at b ≠ 0?
   - Item 11: W1 first, with the connector `Option<Value>` through `parse`.
5. **Items 1, 2, 3, 9 and 10** (the `retained_product.rs:1558` hunk; the site tables and T8; the M03 and strict-gap texts; reviewed inputs and the readers' retired codes; the SP-4 files). Give the facts and a recommendation for each. WORKING_ITEMS decides.
6. **The `b2` overlap** (§4.4): re-measure it against `b2` `e582b61f9e`.

## Verdict and record

- **The verdict:** PASS, PASS WITH AMENDMENTS, or FAIL. List findings as BLOCKING, SHOULD-FIX or NOTE, and give a recommendation for each of items 1–11.
- **Records** go directly in `R/REVIEW_RV130/t4_i10_01/` in NUM (REVIEW.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a file, give its full content in your final message with its intended path; do not work around the refusal.
- **Host:**
  - Python through `WT/venv/bin/python`, and heavy jobs through `WT/tools/t3_slot.sh`.
  - Cargo is not needed. If you use it, it goes through `WT/tools/t3_cargo.sh`. #1168's DEC-025 holds the exclusive lock until about 04:15Z.
  - No DEC-025 and no installs, and never signal another job.
  - Scratch goes in `WT/scratch/rv130/`.
- **Budget:** about 3 h.

End your turn with:
- the verdict;
- the findings;
- items 1–11, each with a recommendation;
- the constraint check;
- the overlap.
