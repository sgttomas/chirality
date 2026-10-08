# Lane K (I102): B3-K, then B2-K, in the frame kernel

Read `R/BRIEFS/B1_COMMON.md` for the shared rules (records, Git, placeholders). Its host rules are replaced by this brief's. **You are I102, lane K's owner (I-K),** through RV-K's review and your repairs.

**Why now.** The owner has directed that production code comes first (2026-10-08). Lane K's work is in the frame kernel only, which B1 does not touch (B2-KD's Basis: "lane K's base at J0 is main's FK"). So it starts from main now, instead of at J0. ROOT merges it into `b2` when `b2` is cut after PR-B1.

## Where

- **`WT/b2-k`,** branch `codex/piping-t3-b2-k-20261008`, cut by ROOT from main.
- **Your fence:** FK (`P/core/solver/frame_kernel`), its tests and its oracle files.
- **Compile only, never edit:** PP and every other FK dependent.
- **Stop and return** if the work needs a change outside FK, beyond a compile fix that the design names.

## Part 1: B3-K (3–6 h)

The specification is RR "RV115's addendum accepts B3-K (K3-1, K3-2); the kernel items of B3-D ruled", with `R/I96/b3_d_01/DESIGN.md`'s kernel section and RV115's ADDENDUM_01.
- **K3-1:** `ProductMaterial::BaseENu { e, nu }` → `ExactENu`, additive.
- **K3-2, by option (a):** represented Z for every material. The declared oracle exception is exactly the three lines and two hashes that ruling 1 states. **Any other oracle byte change is a stop.**
- **K3-3:** the tests, with SA-2's controls and NA-6's ν = 0.3125 control.
- **Acceptance (NA-5), which is J2k:**
  - K3-3 passes;
  - FK's suite passes with only the declared oracle lines changed;
  - PP compiles and its suite passes;
  - every FK dependent compiles;
  - `profile_in_build_record` is in the build record.

**Commit Part 1 on its own, and tell ROOT the commit.** ROOT may have it reviewed while you continue.

## Part 2: B2-K (19–30 h)

The design is `R/I94/b2_kd_01/DESIGN.md`, accepted without a second round. It is amended by these RR sections, in order:
1. **"RV115 (RV-K) accepts B2-KD with amendments; R-1 to R-11 ruled":**
   - SF-1 to SF-4 (the exact Run-capacity check; the restrained-root operand; the product needing more than 53 bits; C6 asserted at the net enclosure);
   - R-1 to R-11 with RV115's conditions (R-3 and R-4: compile and test every FK dependent; `profile_in_build_record`);
   - N-3, N-6, N-7, N-8, and N-9 optionally.
2. **"RV115's addendum accepts B3-K …", ruling SA-1:** re-base your stop S-11 and the byte-identity test K-13 on Part 1's oracle.
3. **"RV118 confirms B2-C revision 01; …" (A-1):**
   - option (ii)'s formation is in FK's `ProductProofDraft::project`, for combination owners only. A combination's `displacement_magnitude` is RN64 of the exact 3-norm of its frozen published components (mm);
   - add the branch in KD §5.7, a K-09 diagnose check of the published bits, and K-13 byte identity for case magnitudes;
   - `R/I97/b2_c_01/REVISION_02.md` §2.2 gives the reference recipe. Its step-4 midpoint wording is superseded by item 4.
4. **"RV115 and RV118 confirm B2-C revision 02: …":**
   - SA4-1 (a) to (e) and B-2 (b);
   - the three added vectors, each expected at MIN_POSITIVE. `exact_norm_vectors.json` stays sealed: add the vectors in your own test data;
   - NA4-5: your RETURN states that the ordinary and retained routes now form combination magnitudes differently, up to about 2 ulps apart.

**B2-C** (`R/I97/b2_c_01/`, final for J1) is the contract your API serves. Do not change it. Return any conflict with it to ROOT.

**Stops:** KD §9.1's stop list, as SA-1 re-bases it, and the invariants RV115 added (SF-1).

## Evidence

- **Tests:** KD §7's test list, as amended, each test named in your RETURN, with SF-2's K-10 mutation and SF-4's K-08 assertion.
- **Byte identity:** the old API is byte-identical (K-13).
- **Mutants:** one per new check, each killed by an assertion. List the survivors and the reason for each.
- **Suites:** FK's full suite, PP's suite, and every FK dependent compiled, at each part's head. Compare against main's results; the only differences may be your added tests and Part 1's declared oracle lines.
- **Keep the RETURN short:** what changed, what passed, what is open. ROOT reads the code and the test output, not prose.

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`). **Other heavy commands** go through `WT/tools/t3_slot.sh <command>`.
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job.
- **Not allowed:** DEC-025, installs, and solver-at-scale runs beyond the tests.
- **Paths:** absolute paths only. Scratch goes in `WT/scratch/i102_b2_k/`, and targets in `WT/targets/i102-b2-k/`.
- **Records:** placeholder paths only, no symlink, and no folder named `build`.

## Output

- **Commits** on `codex/piping-t3-b2-k-20261008` in `WT/b2-k`: Part 1, then Part 2, each with a truthful message. ROOT pushes.
- **The record:** `R/I102/b2_k_01/RETURN.md`, with `_run_records/` and SHA256SUMS.
- **End your turn with:**
  - the heads, per part;
  - the test and suite results;
  - the mutants;
  - any stop or conflict for ROOT.
