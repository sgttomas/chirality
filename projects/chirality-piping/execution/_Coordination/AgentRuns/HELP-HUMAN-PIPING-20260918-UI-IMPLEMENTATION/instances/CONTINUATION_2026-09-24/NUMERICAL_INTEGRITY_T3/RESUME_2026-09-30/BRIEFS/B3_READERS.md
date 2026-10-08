# B3's readers: B3a (0.3.0 legacy) and B3b (`<physics-retained>`), per language, plus lane T's carriers

Read `R/BRIEFS/B1_COMMON.md` for records, Git and placeholders. Its host rules are replaced by this brief's.

**Owners:**
- I101: RS (`WT/b2-r`) and TS (`WT/b2-t`), and lane T's carriers in `WT/b2-t`;
- I100: PY (`WT/b2-p`).

Each lane is cut by ROOT from `b2` at `e67c364680`, which carries J1's statics, lane A's admission, lane K and B1 at I4′. **The production-first direction holds:** keep records short.

## The specification

- **I93's PLAN:**
  - §1.3 (B3a's readers: G8 admits exactly `pressure_contract == {version "1.0.0", mode "legacy_pressure_v1"}` for 0.3.0);
  - §1.4 (B3b's readers: S-G1's `<physics-retained>` branch, D2 §4.9.1 and §4.9.3: G0 identity, table and definition; G7 physics-1's base validator; G8 physics-source-1's `actual_materials` through S-C; G5b exact section truth);
  - §1.4's lane T row.
- **B3-D final for J1** (`R/I96/b3_d_01/`, revision 01): the readers' branch, which adds no new failure code, and RV116's rulings:
  - S-1: the route's definition hash at the four sites; in your lanes, RS `retained_precision.rs:487`, PY `:364` and TS `:170`;
  - B3D-10's tightenings with N-4's falsy-value mutation;
  - B3D-12: S-C's minimal exposure in the base `physics_source` readers.
- **The rulings:**
  - "RV116 (RV-D) accepts B3-D …";
  - "RV116 confirms B3-D's revision 01; …";
  - "I99's B3-W verified; B3's witnesses selected; …".

## Per language: B3a, then B3b

1. **The census over 07n first:** 0 changes is required (R5's rule). A change is a stop.
2. **B3a:** G8's namespace check admits exactly that contract value and nothing else.
   - Pin it on the producer-solved `m3l` successor once lane P's Part 1 lands. Until then, use synthetic receipts.
   - Mutations: the mode or version changed; a non-zero pressure load.
3. **B3b:** the `<physics-retained>` branch at G0, G7, G8 and G5b, as B3-D states, with the S-1 definition-hash fix.
   - Use synthetic receipts first, and the producer's `m3x` successor once lane P's Part 1 lands.
4. **The three readers agree** on every new shape's gate and code. A disagreement goes to ROOT, not into a per-reader declaration.

## Lane T (I101, in `WT/b2-t`)

The carriers:
- the successor branches in `P/schemas/results.v0.3.schema.yaml`, `analysis_run.v0.3.schema.json` and `stress_neutral_export.v0.3.schema.json` (D2 §4.9.6), including B3-D's `CARRIER_PROFILE_ENUMS.diff`, which J1 deferred to lane T;
- `outputPolicy.ts`'s exhaustive entry and its test;
- the TS `SourceContract` union;
- the T6S golden for the exact successor's derivative, with its RE test (decision 21).

## Evidence

- **Census:** 0 changes over 07n.
- **Suites against `b2` at `e67c364680`,** test by test: only added tests.
- **Mutants:** one per new check, each killed by an assertion.
- **The three readers' verdicts** on a shared set of new shapes, bound, unbound and transport.
- **Keep the RETURN short.**

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`), with fresh targets under `WT/targets/<id>-b3r-*`. **Other heavy commands** go through `WT/tools/t3_slot.sh`.
- **vitest** runs in an archive, as `T/IMPLEMENTATION/B1_I4/` shows.
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job.
- **Not allowed:** DEC-025 and installs.
- **Paths:** absolute paths only. Scratch goes in `WT/scratch/<id>_b3r/`.
- **Records:** placeholder paths only, no symlink, and no folder named `build`.

## Output

- **Commits** on your lane branches only. ROOT pushes and merges into `b2`.
- **The record:** `R/<id>/b3_readers_01/RETURN.md`, with `_run_records/` and SHA256SUMS.
- **Budget:**
  - RS 5–8 h, PY 4–6 h, TS 4–6 h;
  - lane T's carriers 5–8 h.
- **End your turn with:**
  - the heads;
  - the census;
  - the suites;
  - the mutants;
  - the three-reader agreement;
  - any stop.
