# I101: I-RS's and I-TS's harness pins for corpus 07n

TASK (Type 2), I101 (I-RS and I-TS), for ROOT (HELP_HUMAN, Agent 0), the return path. I made no delegation. 2026-10-08 UTC.

**Basis:**
- ROOT's message after SC: rulings 1–6 for this round; `B1_I4P_RS_TS.md` and `B1_SC.md`'s acceptance;
- SC's return, `R/I100/b1_sc_01/RETURN.md` (sha256 `a4bd24f9…885c`, verified);
- 07n, `P/fixtures/results/retained_precision_cases.json` (sha256 `ea113e7b…e283`, verified at SC's head `09fe4cc69b`).

**Placeholders:** WT, NUM, P, R; RE = `P/core/reporting/result_export`; RT = `RE/tests/retained_precision_contract.rs`; TT = `P/apps/desktop/src/features/results/retainedPrecision.test.ts`.

## Result

**HEAD = `901745f46b`** on `codex/piping-t3-b1-20261007` in `WT/b1`. It is two commits on SC's `09fe4cc69b`, tests only, and is not pushed:

| Commit | File | What |
|---|---|---|
| `90d8fbeea5` | RT (+799/−9) | **RS's pins.** `slice_outcomes` drops its 294 count and checks each slice's ids, in order, against `MUTATION_IDS` (all 534, literal); this is ruling 4 (I83 §7 item 8). `snapshot_07m` reads `[286..294]`. Must-pass: 78 entries, with an entry's own `expected_classifications` when stated. New: `snapshot_07n_counts_and_format`, `snapshot_07n_mutation_outcomes` (07n's 240 as one tallied slice), `snapshot_07n_unbound_and_transport_reads` |
| `901745f46b` | TT (+59/−7) | **TS's pins.** Must-pass uses `expected_classifications` when stated. The three 07l tests read 07m's prefixes. SR-TS repair 01's G2 list reads 07m's 294. New 07n block: counts and format, and each entry's unbound and transport reads (291 tests) |

- **Ruling 1:** both readers read `expected_unbound` (else `expected_unbound_by_reader.<reader>`), `expected_transport` and `expected_classifications`, as PY does.
- **Ruling 2:** both pin the 45 entries' declared form. Python equals TS equals the shared expectation; Rust gives its own code; all at G7; the unbound read is the same per reader.
- **Ruling 6:** no detail text is pinned, and no reader source changed. rustfmt adds no block on RT's changed lines (108 blocks, as before).

## Evidence

All runs are in `git archive` copies of P without `execution/`, with `node_modules` linked (lock `cmp`-equal) and the eight wasm assets copied, not built. Each was one heavy job.

| Check | SC head `09fe4cc69b` | HEAD `901745f46b` |
|---|---|---|
| RE, `cargo test --no-fail-fast` | 177 ok, **19 FAILED** (RT 60 of 79) | **199 ok, 0 failed** (RT 82; carriers 17) |
| Desktop vitest, whole suite | 3,934 passed, **20 failed** | **4,245 passed, 0 failed** (141 files) |
| `tsc --noEmit` | — | rc 0 |

- **Test by test:** the 19 RS and 20 TS failures now pass. The only other differences are additions: RS +3 (the three 07n tests), TS +291 (the counts test and 290 entry reads). Nothing else changed.
- **TT's count** is 1,102 (811 at SC). RT's is 82 (79 at SC).
- **Census** (RV113's harnesses, unchanged, at HEAD; RS and TS):
  - **07m: 0 changes** against I100's I4′ census, on 339 entries, every read in full (input digest; bound, unbound and transport; RS's standing);
  - **all 638 entries: 0 changes** against I100's census at SC's head, on gate, code, detail, eligibility, standing, publication digest and classifications.
- **T-12, TS's check of SP's several-notice bytes** (I85 `final/t12_bytes`; the sealed sums verified): **passes, both modes.** The checks:
  - each noticed envelope, plain and with the receipt detail, has exactly case-a's and case-c's notices added;
  - TS's base readers read each as the base: raw and transport contract `preview_physics`; the evidence check ok; standing `needs_recompute` with the same findings; the same binding refusals (none) and summary; an AnalysisRun record that builds and validates.

  The check is a scratch vitest harness, `harness/i101T12.test.ts`, never committed (`T12_TS.json`).

## Not done: ruling 3, RV108 N6(b), returned to ROOT

The old phrase "Rust and Python the reader's G0 code or their base header code" is pinned by **three** readers' tests, not RS's alone:
- RS `retained_precision_carriers.rs:861`;
- TS `retainedPrecisionIntegration.test.tsx:690`;
- **PY `tests/test_retained_precision_carriers.py:364`.**

Changing the fixture text with RS's pin alone would fail PY's and TS's tests, and PY's test file is outside my lane. I made the edit, found the third pin, and reverted it before committing. Nothing of it is on the branch.
- **The proposal:** `N6B_PROPOSED.diff` (fixture, RS, TS and PY pins), all ASCII, using RV108's wording "the reader's G0-G2 code or its base step's code". RS's pin also refuses the old phrase.
- **Checked in a scratch copy of HEAD with the patch applied:** RS's carrier test passes (17 of 17) and TS's integration test passes (180 of 180). PY's test was not run (it needs PY's checked binaries).
- **ROOT's call:** apply it as one commit (mine, PY's line included), or route PY's line to I-PY.

## Interpretation and notes for ROOT

1. **Ruling 4's "in the case file":** I pinned Rust's slice ids in RT, the Rust test file, as I83 §7 item 8 describes ("move the id check into the helper"). The pins are a literal `MUTATION_IDS` list that `slice_outcomes` checks per slice. I did not edit the shared corpus: 07n is append-only, and PY pins its key set. Tell me if you meant otherwise.
2. **The 07n tally:** `snapshot_07n_mutation_outcomes` tallies 07n's 240 by Rust's expectation, under 39 gate-and-code keys. A re-expected entry fails there even though the per-entry test follows the corpus.
3. **`WT/b1` holds ignored build leftovers that are not mine:** `apps/desktop/node_modules/`, `core/serialization/canonical_json/target/` and `core/units/target/`. I left them in place.

## Host

- Cargo went through `WT/tools/t3_cargo.sh` (`--locked --offline`, toolchain 1.97.1) into fresh targets under `WT/targets/i101-b1-sc-pins/`. vitest and tsc went through `WT/tools/t3_slot.sh`.
- One heavy job of mine at a time, in three chains: dev, evidence and the N6(b) check. My job-log lines are `host/cargo_jobs_i101.log`. Each chain had one waiter, its background completion, and none remain. I signalled no job.
- No install, wasm build, DEC-025, push or PY edit.
- The copies (with their links) and the targets are deleted. Scratch stays in `WT/scratch/i101_b1_sc_pins/`.
- **Records:** placeholder paths only; no symlink or `build` folder; no junit; screened with the host screen's patterns and the machine's names, `.gz` decompressed: 45 files (the folder, SHA256SUMS included), 0 hits, 5 names screened; `git status --ignored`: every file untracked, none ignored.
