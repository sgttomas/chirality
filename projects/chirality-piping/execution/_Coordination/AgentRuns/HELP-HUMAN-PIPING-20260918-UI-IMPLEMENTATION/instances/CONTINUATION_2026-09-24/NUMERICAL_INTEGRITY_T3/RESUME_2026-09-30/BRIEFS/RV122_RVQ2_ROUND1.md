# RV122 (RV-Q2), round 1: independent review of lane A: J1's statics package and the B3a, B2 and B3b admission

TASK (Type 2), an independent reviewer dispatched by ROOT (HELP_HUMAN, Agent 0). ROOT is your return path, and you do not delegate. **You are a fresh instance and wrote none of this change.** Build your own oracles.

**You hold RV-Q2 for B2/B3** (I93 PLAN §2.5). This is round 1, and you confirm its repairs. RV118 (B2-C) and RV116 (B3-D) are not resumable, so the statics' fidelity to their selected designs is yours too. Keep your records so a later you can continue from the files alone.

## The candidate

- **The branch:** `codex/piping-t3-b2-a-20261008` in `WT/b2-a`, over `b1` at I4′ (`8d46b045e2`), with four commits:
  - `cd7bc9b363`: J1, the statics package and the interim `reviewed_inputs` re-pin;
  - `3cc71f2e60`: B3a-A;
  - `a76bbd4477`: B2-A;
  - `e96355ef8f`: B3b-A, provisional on B1's M.

  22 files, +3,425/−107.
- **The return:** `R/I103/b2_a_01/RETURN.md`, with `statics_j1.diff` and SHA256SUMS. Read it after forming your own view.

## The specification

- **Lane A's brief,** `BRIEFS/B2_A_LANE.md`.
- **The plan:** I93's PLAN §1.2.2, §1.2.4 (PP admission), §1.2.7, §1.3 and §1.4; REVISION_01 §1.3 and §1.4 (the J1 package and its acceptance).
- **The contracts, final for J1:**
  - B2-C (`R/I97/b2_c_01/`, the D1.4 text and statics);
  - B3-D (`R/I96/b3_d_01/` revision 01, the D1.3 and D1.5 texts and statics);
  - B3-S ruling 4: no combination on the exact route.

## Review, in priority order

1. **J1 is complete and mechanical:**
   - each static is byte-equal to its selected file;
   - `REVIEWED_INPUTS` is 17, with its array lengths and `build.rs`;
   - the interim re-pin is re-derived correctly, and nothing else is re-pinned (identity, layouts, `threshold_bytes`, the generated profile, the caps);
   - the PTABLE cascade is constants only, in the 12 files.

   **Contest or accept I103's three stated differences** from REVISION_01 §1.4 (B2-C §11's DEF-C additions, the law test's `include_str!` scope, `CARRIER_PROFILE_ENUMS.diff` deferred to lane T).
2. **The expressions are right:**
   - D1.3's branches L and L3 for B3a, against PLAN §1.3 and B3-D's refusal map;
   - D1.4 for B2: z ≤ 2, C_eq ≤ 3, terms ≤ 3, range operands ≤ 3, `CombinationIds` (C-9), the six new D1.9 rows, `CombinationsCapacity`, the census of combination strings;
   - G-C as C_eq·P_final and C_eq·(3m+1)·Text(err);
   - G-B and T-3 (e) unchanged;
   - B3b's branch E, D1.4's and D1.5's exact clauses (no combinations; regions `Some([])`).

   Check each against B2-C's and B3-D's texts. **A bound that admits more than the contract is BLOCKING.**
3. **Nothing priced changes:** the generated profile block is byte-identical at every head, and so is the priced report layout. Check I103's claim that each combination's array facts sit beside the report.
4. **Byte identity:** every c = 1 and B1 multi-case pin is unchanged. **m3l's new notice on the Direct entry** (RS refuses it at G8 until the readers' B3a work) is expected, and pinned. Admitted combinations, m3x, n05 and n06 keep the exact ordinary bytes.
5. **The out-of-domain oracles and the runner's literal,** re-based to C_eq + 1.
6. **Mutants:**
   - your own, on every new bound and branch;
   - check I103's B2A-13 equivalence claim.
7. **Suites against I4′,** test by test: PP, the runner, RE, PY and TS.

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`), with fresh targets under `WT/targets/rv122-*`, one per lockfile. **Other heavy commands** go through `WT/tools/t3_slot.sh`.
- **vitest** runs in an archive as `T/IMPLEMENTATION/B1_I4/` shows.
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job.
- **Copies** go by `git archive` into `WT/scratch/rv122_rvq2/`.
- **Not allowed:** Git writes, DEC-025 and installs.
- **Records:** `R/REVIEW_RV122/b2_a_01/` (REVIEW.md, `evidence/`, SHA256SUMS). Placeholder paths only, no symlink, and no folder named `build`.

## Output

- **A verdict,** PASS or FAIL, with BLOCKING, SHOULD-FIX and NOTE counts.
- **Keep it short:** one line per finding, plus the evidence.
- **Budget:** 5–8 h.
- **End your turn with:**
  - the verdict;
  - one line per finding;
  - REVIEW.md's sha256;
  - anything ROOT must rule on.
