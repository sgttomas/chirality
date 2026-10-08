# RV121 (RV-K): independent code review of lane K: B3-K (J2k) and B2-K

TASK (Type 2), an independent reviewer dispatched by ROOT (HELP_HUMAN, Agent 0). ROOT is your return path, and you do not delegate. **You are a fresh instance and wrote none of this change.**

**You hold RV-K for lane K's code,** succeeding RV115, who reviewed the designs and is not resumable. You confirm I102's repairs afterwards. Keep your records so a later you can continue from the files alone.

## The candidate

- **The branch:** `codex/piping-t3-b2-k-20261008` in `WT/b2-k`, over main `601ba408e4`. It has three commits, all inside FK (`P/core/solver/frame_kernel`; 15 files, +3,704/−91):
  - `806424c6de`: Part 1, B3-K (J2k);
  - `f7494326f1`: Part 2, B2-K;
  - `ef51a2d295`: Part 2's added tests.
- **The return:** `R/I102/b2_k_01/RETURN.md` (`0d538ca1…`). Read it after forming your own view.

## The specification

- **Lane K's brief, `BRIEFS/B2_K_LANE.md`,** and every source it lists:
  - B2-KD (`R/I94/b2_kd_01/DESIGN.md`);
  - RV115's review and addenda (`R/REVIEW_RV115/b2_kd_01/`);
  - I96's B3-D kernel section;
  - B2-C (`R/I97/b2_c_01/`, REVISION_02 §2.2);
  - the RR sections the brief names.
- **The amendments are binding,** in the brief's order:
  - SF-1 to SF-4; R-1 to R-11; N-3 and N-6 to N-9;
  - SA-1; A-1;
  - SA4-1 (a) to (e) and B-2 (b);
  - Part 1's K3-1, K3-2 by option (a), K3-3 with SA-2 and NA-6, and NA-5.

## Review, in priority order

1. **The combination certificate's soundness, in the code.** Nothing published for a combination may lie outside its enclosure. Check each premise of KD §5.3 for a combination owner, the error terms of §5.4, and the composition of §5.5, against the code in `final_case.rs`, `product_certificate.rs` and `combine.rs`.
2. **Option (ii)'s formation in `project`, for combination owners only.** It is the exact 3-norm rounded once (SA4-1 (a) to (e), B-2 (b)), with case magnitudes byte-identical (K-13). Build your own exact oracle for the three added vectors and adversarial triples.
3. **SF-1's Run-capacity invariant:** no batch can reach `RunTrace::requested`'s `assert!`. Try adversarial orders.
4. **Part 1:**
   - K3-1 is additive;
   - K3-2 gives represented Z for every material;
   - the oracle change is exactly the three declared lines (fixture `467f8811…`, generator `d9618a32…` at `806424c6de`).
5. **The generator at Part 2.** It gains 351 lines. Confirm that running it at Part 2 reproduces the frozen fixture byte for byte, and that its new output is exactly the new combination vector file.
6. **The old API is byte-identical** (K-13, re-based on J2k), and no existing test changed except K-11's declared re-pin.
7. **The tests against KD §7's list as amended:** each listed test exists and asserts what the list says. Check I102's two "no reachable specimen" claims (K-01's ledger-refusal half; W05's `Refused`).
8. **I102's item 1:** C1, C4, C5 and C8 lose bending rows to DEF-O's projection rounding (the stress analogue of NC-1), and it says this is not a B2-K defect. Check that claim.
9. **Mutants:**
   - your own, on the certificate and the formation;
   - check I102's five equivalence or unreachability claims (p2m29, p2m30, p2m32, p2m33, p2m34).
10. **Suites against main:** FK, PP and every FK dependent, in fresh targets.

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`). **Other heavy commands** go through `WT/tools/t3_slot.sh`.
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job.
- **Use fresh targets per lockfile** under `WT/targets/rv121-*`. A shared target directory mixed serde_json builds for I102.
- **Copies** go by `git archive` into `WT/scratch/rv121_rvk/`.
- **Not allowed:** Git writes, DEC-025 and installs.
- **Records:** `R/REVIEW_RV121/b2_k_01/` (REVIEW.md, `evidence/`, SHA256SUMS). Placeholder paths only, no symlink, and no folder named `build`.

## Output

- **A verdict per part,** PASS or FAIL, with BLOCKING, SHOULD-FIX and NOTE counts.
- **Keep it short:** one line per finding, plus the evidence.
- **Budget:** 6–10 h.
- **End your turn with:**
  - the verdicts;
  - one line per finding;
  - REVIEW.md's sha256;
  - anything ROOT must rule on.
