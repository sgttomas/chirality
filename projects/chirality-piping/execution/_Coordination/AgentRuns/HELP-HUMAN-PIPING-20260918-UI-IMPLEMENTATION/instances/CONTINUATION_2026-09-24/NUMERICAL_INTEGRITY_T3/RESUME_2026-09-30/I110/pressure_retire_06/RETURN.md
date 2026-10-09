# I110 round 6: T2 under ROOT's exact check, the demo records regenerated, the evidence, and the U3 package

I110 is a TASK for WORKING_ITEMS (T3). The round-6 instructions came in a WORKING_ITEMS message carrying ROOT's ruling RR "Owner decisions: T4 starts now; the governance-documents PR is authorized" (its section "U3, T2's re-pin check, option (a)").

**Branch:** `codex/piping-t3-pressure-retire-20261008` in `WT/t3-pret`. The round started from `1e9724fb94`. Not pushed.

| Commit | What |
|---|---|
| `11a026b628` | T2 and its re-pins (product) |
| `fe657e3a68` | the two demo generation records, regenerated (product; **the final product head**) |
| `1d2ebdcb59` | the evidence package `IMPLEMENTATION/U3/` (records only; **the PR head**) |

## Stop

**No stop.** No check failed: (iii) holds for every re-pinned carrier, and the host accepted every package file.

Four points need WORKING_ITEMS' or ROOT's attention. Each is also in the package (CHANGE_RECORD §6 to §8).

1. **One re-pinned carrier is outside the ruled radius.** `P/fixtures/results/retained_precision_carrier_cases.json` pins the file hash of each fixture it names, one of which is `n05-sparse_interactive.raw.json` (`fixtures.source_blocks_n05_sparse.sha256`).
   - My round-5 radius missed it, so ROOT's ruling does not list it. The ruling says T2 "reaches no retained-precision successor or reader corpus".
   - This file is the carriers' standing-parity scenario set, not the reader corpus `retained_precision_cases.json`.
   - I recomputed that one hash from the resulting file, by the same rule as `generation.json`'s hashes. Nothing else in the file changes: no case, expectation or other pin.
   - Without the change, the RS, PY and TS fixture-integrity assertions fail.
   - It is in `11a026b628`. If ROOT treats the file as a reader corpus under ruling 4, it needs ROOT's confirmation before merge.
2. **The export documents need more than ROOT's two digests.** In the byte evidence, the 26 T2 rows' ordinary and mechanics envelopes pass ROOT's extended check exactly. Their runner export documents do not, because the document also binds its source with two product hashes:
   - the source checksum: RE `derivative::digest` of the mechanics envelope, at four places;
   - `derivative_hash`.

   With those also recomputed by their product rules from the normalized content, all 26 documents equal B. At the head without T2, the procedure reproduces each document unchanged. This is beyond the check as ROOT stated it, so it is listed for ROOT. The documents are harness outputs only: no committed file carries them.
3. **The branch conflicts with current main** `ec5d397359` (PR-N), in one place: `PP/src/lib.rs`'s imports.
   - Main adds `correct_norm::{norm2, norm3}`. The branch drops `exact_rounded_sum`, whose last use was the legacy pressure path.
   - Keeping both changes resolves it. PP compiles with the resolution (`cargo check --tests`), with the same warnings as main.
   - Every other file merges cleanly (`_run_records/merge_main_check.txt`).
4. **The first demo regeneration was not routed per call.** It ran the recipe under one T3 slot (`t3_slot.sh`); the recipe's own cargo calls used `--offline --locked` but did not go through `t3_cargo.sh` one by one.
   - I reran both modes in `WT/t3-pret-hb` at `fe657e3a68`, with a PATH shim (I114's method) that sends every cargo call through `t3_cargo.sh`.
   - The rerun reproduced every output and both records byte for byte: no tracked file changed.

## 1. T2

The text is changed at PP `preview_formulation_basis`, limitation [1]:
- **old:** "Pressure thrust and pressure stress retain the existing preview formulation and capability qualifications; pressure formulation qualification remains open."
- **new:** "Pressure is not solved on this profile: legacy pressure inputs are refused, and pressure is solved only on the exact straight-pressure profile, under that profile's own qualifications."

**The per-file check** is `_run_records/t2_per_file_check.txt`, OVERALL PASS. It is computed from Git objects, `1e9724fb94` against `11a026b628`, together with the probe's reports (`_run_records/t2_probe/`).

**The baseline,** at the head without T2, holds for all 12 raws:
- the product rule (PP `source_receipt::hash`, RFC 8785 via the product's canonical-JSON crate) reproduces both committed digests;
- the head reproduces the committed bytes. 2 files are in struct order and 10 have sorted keys.

| Carrier | (i) string, (ii) digests | (iii) equals the head's output | Verdict |
|---|---|---|---|
| 12 source-block raws (6 main, 6 `ui/`) | 3 leaves per file: the string, `publication_sha256` and `receipt_sha256` | 12/12 byte for byte; the committed file is exactly the base with (i) and (ii) applied | PASS |
| the Rust pin, 2 SHA constants (`f1b_w2_exact_block_selection_of_a_range_triggered_case_publishes_mains_bytes`) | sparse `d953a683…` → `aaabc777…`; dense `10d312a1…` → `7db0edaf…` | 2/2 | PASS. Its doc comment says that it was re-pinned, and how |
| `generation.json` | 12 raw-file hashes recomputed from the resulting files | each equals its file; the request hashes and every other member are unchanged | PASS |
| `retained_precision_carrier_cases.json` (stop note 1) | 1 file hash recomputed from the resulting file | equals the file; no other byte changes | PASS |
| `precision_connected_ui_mechanics_{sparse,dense}.json` | a string-only edit; the base with only the string replaced equals the committed file | — | PASS |
| 2 `rejected_stress_range` raws and `ORACLE.json` | unchanged | — | as captured |

After the commit, only the two historical captures carry the old string.

**(iv) The readers verify every carrier.**
- Targeted, before the full suites:
  - PP `--test f1b_w2_runtime`: 14/14;
  - the source-block, consumer-contract and carrier pytest files: 311 passed, 11 skipped;
  - the 15 vitest files that read these carriers: 625/625.
- The full suites pass (§3).
- **RV128 A1-N-4's 4 tests**, after the merge: `physicsResultExport` and `KnownSemanticNotices` (38/38), and `test_analysis_run_compatibility.py` and `test_preview_physics_consumer_contract.py` (198 passed) (`_run_records/a1n4_*.log`).

## 2. The demo generation records, regenerated

`npm run generate:product-preview-mechanics`, then `-- --preview-physics-1`, at `11a026b628`. Both exit 0. The check is `_run_records/demo_regeneration_check.txt` (OVERALL PASS).
- **Fixture outputs:** all 5 are byte-identical to the committed files (the demo pair, the legacy carrier, and the refused pair).
- **The records** differ from I114's only in `source_input_files`, `source_input_files_after` and `inventory_json_sha256`:
  - 27 changed entries, plus `historical_pressure_reference.rs`, now absent;
  - each old value equals the file at `9744ed7e69`, and each new value equals the file at `11a026b628`.
- **Unchanged:** outputs, commands, statuses, row counts, tools, dependencies, recipe, generator and input models.
- The records no longer hash stderr, so they compare exactly.
- They are committed in `fe657e3a68`. The shim rerun (stop note 4) reproduced them.

## 3. The evidence

B is main `7eae707bb7` (round 2's B records). The candidate is `fe657e3a68`. The details are in `_run_records/outcome_and_byte_diff.json`, `test_name_diff.txt`, `manifests_cand.txt` and `declared_text_check.txt`.

| Suite | B | Candidate | Changes |
|---|---|---|---|
| 40 manifests | 2,776 ok / 3 FAILED / 80 ignored | 2,755 / 3 / 80 | 57 (39 removed, 18 added). Equal, name for name, to the source `#[test]` diff; no outcome flips |
| src-tauri | 116 | 118 | +2 (I110's label test; I114's `default_session_model_solves_in_both_modes`) |
| pytest `P/tests` | 4,426 passed, 32 skipped | 4,428 passed, 32 skipped | +2 (I114) |
| vitest | 4,245 | 4,250 (4,249 passed, 1 todo, 0 failed), 141 files | 17 renames and additions |
| e2e: r2-smoke, gui-workflow-validation, result-compatibility, ui-foundation | — | **118/118** | bundled chrome-headless-shell (build 1223), CI=1, one worker |

- The 3 FAILED are the known Mac failures at both sides: `t13…` and the runner's two load-reference goldens.
- The wasm build exits 0.

**Bytes.** The harness is round 6's (`scripts/i110_bytes_harness.rs`) and the classifier is `scripts/compare_ext.py`.

| Set | Rows | Result |
|---|---|---|
| E | 96 | 96 equal |
| F | 364 | 332 equal. 6 declared-only: T1 2 rows, V1 4 rows. 26 T2 rows: ordinary and mechanics envelopes pass ROOT's extended check; the documents as in stop note 2 |
| B1 | 64 | 64 equal |
| W1 | 64 | 64 equal (34 successors, 30 ordinary) |

- No output is "other".
- The receipt rule reproduces the digests of every candidate envelope that carries a receipt, and the document rules reproduce each document's own source checksum and derivative hash.
- T4's proposed text appears nowhere.
- **H-1:** the `-0.0` counts equal round 5's head on all 524 rows.

## 4. The package and its checks

The package is `T/IMPLEMENTATION/U3/` in `1d2ebdcb59`, in PR_N's form:

| File | sha256 |
|---|---|
| `CHANGE_RECORD.md` | `8ad9da6c4adda18267adcc2ab038e625a1372c1fda1cc6b1f8ad67b2aa05494a` |
| `PR_BODY.md` | `76f7ce207cbe888ddfc59db5dd6a5fe824c2cfef80c2ff2438a95f607d8f42d8` |
| `citations.json` | `04df27ebf343162774b1c447d09ca0cf67c69abd4c74e9b5e70258dbd69275c6` |
| `SHA256SUMS` | verifies all three |

- `PR_BODY.md` ends with the "Generated with Claude Code" line.
- `citations.json` pins `num_commit` = NUM `a31c14e4d3`.
- The maintained diff adds no record, RR or code-line citation. Its one token is a generator-class false positive: a `core/units/_run_records/…` path in the demo record's source inventory, indexed with a note.

**The checks** used main's `IMPLEMENTATION/F2A_D1/` tools:
- **`source_equality.py`: PASS** (checks 1 to 5; `_run_records/source_equality.{out,json}`).
  - PR side: the scratch head `6de499ceec`, which is `1d2ebdcb59` with main `ec5d397359` merged.
  - INT side: the scratch head `0ff3f3bb5c`, which is NUM `a31c14e4d3` with `1d2ebdcb59` merged.
  - `--main ec5d397359`.
  - Results: |S| = 133; 133 equal in blob and mode; 4 execution files, all in the package, whose SHA256SUMS verify.
  - Both scratch heads carry the same lib.rs resolution (stop note 3). The branch as cut from `7eae707bb7` cannot pass check 1 against a NUM that has absorbed PR-N until main is merged into it.
- **`check_citations.py`: PASS,** in two runs: base `7eae707bb7` with head `1d2ebdcb59`, and base `ec5d397359` with head `6de499ceec`. Each run resolved 2 citations, with 0 ambiguous and 0 unresolved (`_run_records/check_citations.out`).
- WORKING_ITEMS reruns both against its NUM commit.

## Records

- `RETURN.md`;
- `_run_records/`:
  - the checks named above;
  - `heads.txt`;
  - the byte JSONL files;
  - the T2 probe's reports and rows;
  - the e2e and regeneration stdout;
  - `merge_main_check.txt`;
  - `scripts/`;
- `SHA256SUMS`.

Paths use placeholders only.
