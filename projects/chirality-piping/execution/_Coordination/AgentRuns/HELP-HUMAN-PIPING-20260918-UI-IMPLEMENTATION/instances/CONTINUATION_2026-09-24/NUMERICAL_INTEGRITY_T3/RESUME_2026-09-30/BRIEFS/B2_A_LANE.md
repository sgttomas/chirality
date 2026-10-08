# Lane A (I-A for B2/B3): J1's statics package, then the admission (B3a-A, B2-A, B3b-A)

Read `R/BRIEFS/B1_COMMON.md` for records, Git and placeholders. Its host rules are replaced by this brief's. You own lane A through RV-Q2's round 1 and your repairs.

**Why now.** The owner has directed that production code comes first (2026-10-08). Lane A forks from B1's `b1` at I4′ instead of from `b2` after PR-B1 (J0). It needs B1's S3 admission (SA), which `b1` carries.
- At J0, ROOT merges lane A into `b2`, and you resolve any overlap with SQ's re-pins in `retained_memory.rs` and the law tests.
- **Until then, nothing of lane A reaches NUM or main.**

## Where

- **`WT/b2-a`,** branch `codex/piping-t3-b2-a-20261008`, cut by ROOT from `b1` at I4′ (`{I4′ commit}`).
- **Your files** (PLAN §1.2.7's lane A and statics rows, and REVISION_01 §1.3's lane A rows):
  - SCHEMA;
  - PTABLE;
  - the combination definition and the exact definition;
  - `semantic_contract_v0_3_physics_retained_1.json`;
  - `PP/build_identity.rs` and `P/core/product_physics/build.rs`;
  - `PP/retained_memory.rs`, outside the generated block;
  - `PP/retained_memory_law_tests.rs`;
  - `P/core/runner/headless/tests/retained_precision_admission.rs`.
- **J1's hash cascade** may also change the constants in the 12 files PLAN §1.2.7 lists. It changes constants only.
- **Never touched without a stop:** PLAN §1.2.7's list (FK, the base readers, the ordinary route, physics-1's table bytes, any c = 1 or B1 successor byte, the visibility of a D1 `src` item).

## The basis

- **The plan:** `R/I93/b2b3_plan_01/PLAN.md` §1.2.2, §1.2.4 (PP admission), §1.2.7, §1.3 and §1.4; and REVISION_01.md §1.3 and §1.4.
- **The contracts, final for J1:**
  - B2-C, `R/I97/b2_c_01/`: CONTRACT, REVISION_01 and REVISION_02. The merged J1 SCHEMA is `statics/retained_precision_mp_v2.schema.json` (`abf3225c…`, with `statics/SCHEMA_J1.diff`). PTABLE r2 (`b2b4a54d…`) and DEF-C r2 (`3cebce55…`, H `d3fde142…`) are in `statics/r2/`;
  - B3-D, `R/I96/b3_d_01/`: its revision 01 and `statics/r1/`.
- **The rulings:**
  - "B2/B3 R1: …";
  - "I93's REVISION_01 accepted; …" (decisions 28 to 31);
  - "I95's B3-S: …" (rulings 1 to 5);
  - "RV116 (RV-D) accepts B3-D …";
  - "RV116 confirms B3-D's revision 01; …";
  - "RV118 (RV-C) accepts B2-C with amendments; …";
  - "RV115 and RV118 confirm B2-C revision 02: …".

## Part 1: J1's package (REVISION_01 §1.4), as one commit

1. **The statics:**
   - SCHEMA, with B2's `$defs` and B3b's enum value;
   - PTABLE revised;
   - the combination definition;
   - the physics-retained-1 table;
   - the exact definition.

   Each is byte-equal to its selected `statics/` file, or the difference is stated and is mechanical.
2. **`REVIEWED_INPUTS`** goes from 14 to 17, with `encode_reviewed_inputs`' array length and `build.rs`'s digest array.
3. **The interim re-pin:** `REGISTERED_PROFILES[0].reviewed_inputs`, re-derived from the new files' sha256 in order. Leave alone the identity text, `reader_layouts`, `threshold_bytes`, the generated profile, the caps, and every successor and corpus byte.
4. **The two law tests** at 17.
5. **PTABLE's hash cascade,** constants only, in the 12 files.
- **Acceptance (§1.4), in a Registered build:**
  - every c = 1 pin and B1's multi-case pins are byte-identical;
  - these pass:
    - `the_registered_profile_is_the_only_permit_source`;
    - the Direct-entry facade tests;
    - the two law tests;
    - the three readers' suites;
    - the carrier schema tests.
- **A failure is a stop.** Return to ROOT.
- **Also write `statics_j1.diff`** with its sums, for RV-Q2.

## Part 2: the admission

- **B3a-A:** D1.3 for 0.3.0 `legacy_pressure_v1` (PLAN §1.3), with its law tests and oracles.
- **B2-A:** D1.4 with C_eq and terms (B2-C's D1.4 text), and the new `cap_rows` (`Combinations`, `CombinationTerms`, `CaseEquivalents`). Also:
  - G-C's `EnvelopeResults ≤ C_eq·P_final`;
  - `RetainedErrorTextBytes ≤ C_eq·(3m+1)·Text(err)`;
  - G-B and T-3 (e) unchanged;
  - law tests;
  - mutants on the C_eq bound, the term bound and combination counting;
  - the out-of-domain oracles re-based to C_eq + 1, including the runner's literal and its tie test.
- **B3b-A:** D1.3 and D1.5 for the exact route.
  - It refuses any combination on the exact route (B3-S ruling 4).
  - **It is provisional on B1's M:** B3-S prices it within a 10.5 GiB M, and R6b sets M.
  - Commit it separately, and ROOT holds it if R6b selects less.
- **The interim's honesty** (REVISION_01 §1.4): until SQ2, this registered dev/test build admits combinations and the legacy contract priced on B1's S3 profile. It has no product caller.

## Evidence

- **Suites against `b1` at I4′,** test by test: PP, the runner, RE, PY, TS and the carrier schema tests. The only differences are your added tests and the J1 re-pins.
- **Byte identity:** every c = 1 and B1 multi-case pin is byte-identical.
- **Mutants:** one per new check, each killed by an assertion.
- **Keep the RETURN short.**

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`), in fresh targets under `WT/targets/<id>-b2-a*`, one per lockfile. **Other heavy commands** go through `WT/tools/t3_slot.sh`.
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job.
- **Not allowed:** DEC-025 and installs.
- **vitest** runs as `T/IMPLEMENTATION/B1_I4/` shows: in an archive, never in a worktree.
- **Paths:** absolute paths only. Scratch goes in `WT/scratch/<id>_b2_a/`.
- **Records:** placeholder paths only, no symlink, and no folder named `build`.

## Output

- **Commits** on `codex/piping-t3-b2-a-20261008` in `WT/b2-a`: J1 (one commit), then B3a-A and B2-A, then B3b-A. ROOT pushes.
- **The record:** `R/<id>/b2_a_01/RETURN.md`, with `_run_records/` and SHA256SUMS.
- **Budget:** J1, 2–4 h; the admission, 8–13 h.
- **End your turn with:**
  - the heads per part;
  - the acceptance results;
  - the suites;
  - the mutants;
  - any stop.
