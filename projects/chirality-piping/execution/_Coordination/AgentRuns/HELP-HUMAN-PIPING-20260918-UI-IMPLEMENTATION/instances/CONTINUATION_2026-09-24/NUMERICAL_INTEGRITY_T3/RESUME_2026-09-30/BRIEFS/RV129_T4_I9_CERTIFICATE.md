# RV129: T3's independent review of T4-I9's arc load-vector certificate (T4-U1b)

Reviewer (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You are a fresh instance** and have not seen this design before. `R/BRIEFS/B1_COMMON.md`'s host and records rules apply, with WORKING_ITEMS in ROOT's place. You review; you do not edit T4's files or branch.

## What you review

T4 (pressure stress) proposes to replace, for certified arc load terms, S11-G's selected condition "CannotBound for curved consistent vectors" with a proved midpoint–radius enclosure. S11-G is T3's check, so T3 reviews it.
- **The design:** on branch `codex/piping-t4-pressure-stress-20261009` at `471ad93f48`, read with `git show` (never check out or write T4's worktree). `R4` is `P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/PRESSURE_STRESS_T4/`.
  - `R4/T4-I9/DESIGN.md`, sha256 `8b90584f827fb8ce6e4fa8f8be88c8b024f41ff2fbc6796ad0a2e89abdef9cb4`;
  - `R4/T4-I9/RETURN.md` (questions O-1 to O-13);
  - `R4/T4-I9/_run_records/` (the probe and the op count), and `SHA256SUMS` (`b196aad2…`).
- **The code basis:** `ed012c7ccf` (main plus U3), and `b2` `e582b61f9e` for overlap.
- **T3's authority:** RR "Selection: the S11-G design" and "S11-G after V1's S11G_CHECK" (item 3: SF-2), and T3's five constraints sent to T4 (RR "T4 plan 01's annex A: T3's agreement recorded; …", and `R/I115/t4_annex_check_01/`).
- **T4's rulings:** `R4/T4_RULINGS.md` at `1b682630e4`, section "T4-U1b's certificate design (T4-I9): …". HELP_HUMAN accepted R-1 in principle on three conditions, and **your review decides them**:
  - (a) whether the enclosure proof (L0–L7, Theorem 1) and the SF-2 reading hold;
  - (b) whether every failed precondition falls back to `CannotBound`, with a test that shows it;
  - (c) whether T15's new meaning is right.

  A gap in the proof voids R-1.

## The checks

1. **The proof.** Check L0–L7, Theorems 1 and 2, Lemma 3 and identities (I1)–(I4) line by line: every rounding-mode assumption, every `Wide<2>` precision claim at p = 128, every upward-rounded radius, and the inverse's residual condition (ρ < 1/2). Re-derive what you can independently. A step you cannot verify is a finding.
2. **The probe.** Re-run `arc_cert_probe.py` and `opcount.py` (Python, no cargo) and compare with the recorded stdout. Then test the enclosure yourself with your own independent reference: arbitrary precision, a different method from the design's, and cases the probe did not choose (small φ, near π, UTM coordinates, large k, mixed scales).
3. **SF-2 (O-1).** Is the design's R-SF2 the right reading of RR "S11-G after V1's S11G_CHECK" item 3? In particular, is libm acceptable where its effect on `v` is measured exactly and nothing relies on its accuracy?
4. **Fail-closed (condition b).** List every precondition, and say where each falls back to `CannotBound` and which planned test shows it.
5. **T15, T15c and M16's kill (condition c, O-7, R-2).** Is the new meaning right? Can a model whose certificate fails naturally be built (k = 1e40 is the candidate)? HELP_HUMAN wants that before any `#[cfg(test)]` seam.
6. **T3's technical questions:**
   - O-2: a new `Formation::Certified` variant, or `Exact { scale: 1 }` with `operand_bound = r`;
   - O-3: Lemma 3's c/(1 − c) excess, accepted as is or answered by a strengthened `CRITERION` (`formation_guard.rs` is on T3's unchanged list);
   - O-4: `atan_positive` as a first product caller, or K-D5's `included_angle`;
   - O-5 and O-6;
   - O-8: the rebuilt `ruling1` test, with the same assertions;
   - O-10: whether the certificate's loops, statically reachable under `solve_load_case` although W1 refuses curved models first, need TEXT (G5) loop rules and so a re-registration;
   - O-11: the FK `SOURCES` extension;
   - O-13: R-b′ and arc end rows.

   Give a recommendation for each, with its reason.
7. **T3's constraints.** Confirm that the design leaves unchanged: `LIMITATIONS`, reviewed inputs, PP's `Cargo.lock`, the priced layouts, `retained_product.rs`, `tests/s11f_site_test.rs`, `formation_guard.rs`, K-D5's `formation_check.rs`, SA and CB. Measure its distance from `b2`'s edits.

## Verdict and record

- **The verdict:** PASS, PASS WITH AMENDMENTS, or FAIL. List findings as BLOCKING, SHOULD-FIX or NOTE, and give a line on each of conditions (a), (b) and (c).
- **Records** go directly in `R/REVIEW_RV129/t4_i9_01/` in NUM (REVIEW.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a file, give its full content in your final message with its intended path; do not work around the refusal.
- **Host:**
  - Python through `WT/venv/bin/python`, and heavy jobs through `WT/tools/t3_slot.sh`.
  - Cargo is not needed. If you use it, it goes through `WT/tools/t3_cargo.sh`. #1168's DEC-025 holds the exclusive lock until about 04:15Z.
  - No DEC-025 and no installs, and never signal another job.
  - Scratch goes in `WT/scratch/rv129/`.
- **Budget:** about 3 h.

End your turn with:
- the verdict;
- conditions (a), (b) and (c);
- the findings;
- O-1 to O-13, each with a recommendation;
- the constraint check.
