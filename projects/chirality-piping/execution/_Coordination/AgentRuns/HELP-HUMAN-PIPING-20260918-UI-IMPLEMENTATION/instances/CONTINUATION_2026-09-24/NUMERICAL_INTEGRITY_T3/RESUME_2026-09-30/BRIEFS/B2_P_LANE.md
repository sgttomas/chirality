# Lane P (I-P for B2/B3): the producer: B3b-P (the exact route), then B2-P (combinations)

Read `R/BRIEFS/B1_COMMON.md` for records, Git and placeholders. Its host rules are replaced by this brief's. You own lane P through RV-P2's rounds and your repairs.

**Why now.** The owner has directed that production code comes first (2026-10-08). `b2` is built ahead of PR-B1 from three things:
- lane A (J1's statics and the B3a, B2 and B3b admission, under RV-Q2's review);
- lane K (B3-K and B2-K, accepted);
- B1 at I4′.

ROOT merges reviewed repairs into `b2` as they land.

## Where

- **`WT/b2`,** branch `codex/piping-t3-b2-20261008`, at `e67c364680`. You work on this branch, as SP worked on `b1`. ROOT merges other lanes into it only at a clean commit of yours, after telling you.
- **Your files** (I93 PLAN §1.2.7 and §1.4, lane P rows):
  - `PP/lib.rs` (the retained section);
  - `PP/retained_product.rs`, `PP/retained_wire.rs`, `PP/retained_receipt.rs`, `PP/retained_tests_hooks/grant2.rs`;
  - `PP/retained_facade_tests.rs`, `PP/retained_product_tests.rs`, `PP/retained_wire_tests.rs`;
  - `PP-tests/s11f_site_test.rs` (rule-8 rows) and `PP-tests/retained_precision_admission.rs` (expected sections);
  - the new successor fixtures.
- **Not yours:** admission (`retained_memory.rs` and its law tests: lane A), FK (lane K), the readers, the schemas and the corpus. If you need a change there, stop and return.
- **Never touched without a stop:** PLAN §1.2.7's list, including any c = 1 or B1 multi-case successor byte and the ordinary route's behaviour.

## Part 1: B3b-P, the exact route under `physics-retained-1`

- **The specification:**
  - PLAN §1.4 (producer);
  - B3-D final for J1 (`R/I96/b3_d_01/`, revision 01): `RP-PREPARED-EXACT-DUAL-v1`, the row recipes, and the producer requirements P-2 (exact-block budget parity, with `fields` as a pin) and P-4 (W1 never calls the pressure-runtime builders);
  - the definition-hash sites of RV116's S-1 (PP `retained_wire.rs` uses the route's definition hash, not DEF-O's);
  - RR "RV116 (RV-D) accepts B3-D …" and "RV116 confirms B3-D's revision 01; …".
- **Witnesses** (RR "I99's B3-W verified; B3's witnesses selected; …"):
  - `m3x`: the exact successor, pinned in both modes, with new fixtures `retained_precision_exact_successor_{sparse_interactive,dense_scrutiny}.json`;
  - n05 and n06: coexistence, with exact ordinary bytes;
  - `m3x_mix_anchor`: the mixed base;
  - `m3l` for B3a: the producer is expected to need no change. Confirm it.
- **Tests and mutants** as B3-D lists them.

## Part 2: B2-P, combinations

- **The specification:**
  - PLAN §1.2.4 (producer) and §1.2.6 (witnesses);
  - B2-C final for J1 (`R/I97/b2_c_01/`: CONTRACT, REVISION_01, REVISION_02);
  - B2-K's API as merged (lane K, `R/I102/b2_k_01/RETURN.md`);
  - RR "RV118 (RV-C) accepts B2-C with amendments; …" (S-4 (a) and (b), C-1 to C-16);
  - RR "RV118 confirms B2-C revision 01; …" (A-1: (ii)'s formation is in FK's `project`. B2-P keeps the observables stage);
  - RR "RV115 and RV118 confirm B2-C revision 02: …".
- **Its parts:**
  - T-9b and T-9c in `w1_transaction`;
  - operand preparation (C3a);
  - combination attempts and their freeze;
  - the staging overlays;
  - in the wire: `combinations[]`, `CombinationSource`, the mechanics Call, Group imports, `operand_preparations[]`, `execution_order` and `owner_refs` of kind `combination`, and the ordinal mapping;
  - the receipt projection for combination Runs;
  - the hooks: `fail_operand_preparation`, `fail_combination_call`, and a freeze fault.
- **Witnesses** (RR "I98's B2-W verified; …"):
  - **W-CB1 rebased on 1·A + 0.5·B** (`r7_cb1_halfb.json`), with A + B kept as a labelled cancellation pin;
  - W-CB2;
  - W-CB3 v1;
  - W-CB4, split per RV118's S-5 as B2-C states;
  - W-CB5.

  Use the private driver first, then the Direct entry, as B1's pattern. New fixtures: `retained_precision_combination_successor_{sparse_interactive,dense_scrutiny}.json` (W-CB1 or W-CB3, whichever selects).
- **NA4-5:** your RETURN states that the ordinary and retained routes now form combination magnitudes differently, up to about 2 ulps apart.
- **Mutants:** the disposition rule, the operand-source mapping, imports, R-COMB-1's producer side, the failure set and the ordinal mapping.

## Evidence

- **Byte identity:** every c = 1 and B1 multi-case pin is byte-identical, and so are the coexistence bytes.
- **Suites against `b2` at `e67c364680`,** test by test: PP, the runner and FK's dependents compiled. The only differences are your added tests and the pins you are directed to move.
- **Readers:** they will refuse your new successors until the readers' lanes land. Pin what the readers do today, and say so. RS's precommit gates publication, so new successors fall back to the ordinary bytes with a notice until then.
- **Mutants:** one per new check, each killed by an assertion.
- **Keep the RETURN short.**

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`), with fresh targets under `WT/targets/i105-b2-p*`, one per lockfile. **Other heavy commands** go through `WT/tools/t3_slot.sh`.
- **No RSS or timing measurements:** those are SQ2's, run exclusively.
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job.
- **Not allowed:** DEC-025 and installs.
- **Paths:** absolute paths only. Scratch goes in `WT/scratch/i105_b2_p/`.
- **Records:** placeholder paths only, no symlink, and no folder named `build`.

## Output

- **Commits** on `codex/piping-t3-b2-20261008` in `WT/b2`. Commit Part 1 before you start Part 2, and tell ROOT its commit. ROOT pushes.
- **The record:** `R/I105/b2_p_01/RETURN.md`, with `_run_records/` and SHA256SUMS.
- **Budget:** Part 1, 12–18 h; Part 2, 20–30 h. If your context runs low, commit a clean, compiling state, write what remains, and return.
- **End each turn with:**
  - the heads;
  - the pins and suites;
  - the mutants;
  - any stop.
