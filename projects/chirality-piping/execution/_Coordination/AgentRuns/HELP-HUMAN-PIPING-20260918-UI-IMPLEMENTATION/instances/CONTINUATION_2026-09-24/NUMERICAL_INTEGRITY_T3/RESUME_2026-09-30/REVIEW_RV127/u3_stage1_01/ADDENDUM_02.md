# RV127 addendum 02: U3's final deltas and the PR code commit

**Who:** RV127, TASK (Type 2), for WORKING_ITEMS (T3, Agent 1), 2026-10-09 UTC. I wrote none of this code and did not delegate.

**The request:** WORKING_ITEMS' message. Confirm three things:
- each change since ADDENDUM_01's `6b6543dc1e` is correct and within ROOT's rulings;
- exact and pressure-free bytes are identical apart from the declared text, on PR #1168's code commit;
- the merge resolution is right.

**Basis:**
- RR "U3 Stage 2 rulings: the 800 B profile re-pin, …", its sections on I114's lane, on RV127's Stage 2 review and on I110's round-4 stop;
- RR "Owner decisions: T4 starts now; …", its section "U3, T2's re-pin check, option (a)";
- RR "U3, T2's outcome under the extended check; …";
- `R/I110/pressure_retire_04/`, `_05/` and `_06/` (their SHA256SUMS verify);
- `T/IMPLEMENTATION/U3/` at `98733368f9`.

| Object | Commit |
|---|---|
| PR #1168 code commit | `8a12de28db`, parent main `ba500defa4` (main's PR-B1 and PR-N included) |
| PR #1168 head (package) | `98733368f9`; it adds only the 5 package files under `P/execution` |
| The retirement branch | `6b6543dc1e` → `fe657e3a68` (product) → `1d2ebdcb59` (package) |
| NUM's U3 merge | `d92d05a31c`, merging `1d2ebdcb59`; then `2fd24aedf1` absorbs main `ba500defa4`; NUM at `cfeb5b76fe` |

**Placeholders:** as in REVIEW.md.
- `A` is my archive copies `WT/rv127/{main,pr,main_pp,pr_pp}` of `ba500defa4` and `8a12de28db`. `main_pp` carries the PR's three G11 tests as probes.
- `E` = `_run_records/addendum_02/`.

## Verdict: **FAIL** at `8a12de28db`, on A2-B-1 only: 1 BLOCKING, 0 SHOULD-FIX, 4 NOTE

- **A2-B-1. The PR code is not NUM's U3 merge.**
  - It still carries three fixtures that I114's `180bf9b26d` deleted for G10/D-3, and NUM does not carry them:
    - `fixtures/product_preview/invented_mechanics_result.json`;
    - `invented_mechanics_result_precision_1_{dense,sparse}.json`.
  - These are the flawed-premise bundled results the owner ruled replaced or removed. The package's CHANGE_RECORD lists them as removed.
  - Git's rename detection hid the deletion: the retirement's diff shows each of the three as the source of a rename to a new demo file. A `git diff --name-only` path set therefore never lists them. That includes F2A_D1 `source_equality.py`, whose checks passed with 133 = 133.
- **Everything else holds:**
  - Each change since `6b6543dc1e` is correct and within the rulings (§1).
  - Exact, B1 and W1 bytes are identical. Pressure-free bytes differ only in the declared strings and their digests, with 0 other leaves (§2).
  - The T2 carrier check holds (§3).
  - The `lib.rs` merge resolution is right, and every other path both sides touched merges cleanly to the PR's blob (§4).

## Findings

| ID | Class | Where | Evidence | Remedy |
|---|---|---|---|---|
| A2-B-1 | **BLOCKING** (the PR is not the reviewed source; contrary to the owner's G10/D-3 decision) | `P/fixtures/product_preview/invented_mechanics_result.json` and `invented_mechanics_result_precision_1_{dense,sparse}.json` at `8a12de28db` | **The three files:** `git diff --name-status 8a12de28db cfeb5b76fe` outside `P/execution` is exactly three `D` lines. The same holds against `2fd24aedf1`. Their blobs at the PR equal main's (`cf0aa1ce…`, `cb3a6554…`, `6817e6aa…`). `180bf9b26d` deleted them on the retirement branch. **Why path sets missed it:** the retirement diff reports them as renames (R060, R055, R052) to `invented_demo_result_preview_physics_1_sparse.json`, `…_dense.json` and `invented_demo_result_legacy_0_1.json`. With default rename detection, the retirement's and the PR's `--name-only` sets are equal (133 = 133). With `--no-renames` they differ in exactly these three paths (`E/pr_vs_num_tree.txt`). **The consequence:** no product code reads them. But they are the bundled results computed with the flawed joint and legacy pressure. The precision pair also still carries the retired T2 text. So the PR ships what G10/D-3 removes. It also contradicts the package: CHANGE_RECORD's list of bundled results removed, `radius_sweep.txt`'s header ("equal to the U3 PR's maintained files"), and WORKING_ITEMS' "the code equals NUM's U3 merge" | Delete the three files in the PR (recut `8a12de28db`, or add a commit), then rerun the source-equality check with renames off (A2-N-1). Correct the package's equality statements to cite that run |
| A2-N-1 | NOTE (tooling) | `T/IMPLEMENTATION/F2A_D1/source_equality.py`, `names()` (`git diff --name-only`) | With rename detection on, a renamed file's source deletion is listed under its destination only. Checks 1 and 2 cannot see a rename source that the PR fails to delete, and that is what happened in A2-B-1 | Use `git diff --no-renames --name-only` in `names()`. The same applies to any other path-set or sweep tool |
| A2-N-2 | NOTE (test strength) | `P/core/runner/headless/src/benchmark_binding.rs`, `RETIRED_PRESSURE_HALVES` in `mechanics_whole_suite_is_24_cases_192_values_and_preserves_original_11_91` | For MECH-TP-PHYS-008/009, the original-projection drift check drops from full equality with the frozen run to status plus value names. The values are still checked against the updated expected values (status `executed_and_matched`). But the unchanged thermal value is no longer compared with the frozen projection | Optional: assert `thermal_axial_force` equals the frozen value, and each total equals the frozen total minus the retired 9.0 N |
| A2-N-3 | NOTE (erratum to ADDENDUM_01 §6) | FK `src/lib.rs:650-653` (`UserStiffnessElement::new`) | ADDENDUM_01 said that a lateral = 0 flexibility joint "still reaches the element". In fact the constructor requires all four stiffness values to be finite and positive, so such a joint is refused (`EXPANSION_JOINT_MACRO_ELEMENT_INPUT_INVALID`). With M07 and G11, no flexibility joint forms an element. RR's "after 1–3 nothing reaches it" holds | None; this corrects my record |
| A2-N-4 | NOTE (my run's limits) | `RE/tests/retained_precision_carriers.rs` `u6_doc_hidden_seams_have_no_product_callers` | It fails in my archive copy only because the copy excludes `P/apps`, and the test scans `apps/desktop/src-tauri/src/lib.rs`. It is not a product failure. With it skipped, the RS reader passes: carriers 16/16, source blocks 15/15, physics source 7/7. I did not rerun the PY and TS readers, the full suites or the e2e; those rest on I110's round-6 records and CI | None |

## 1. The changes since `6b6543dc1e`

| Commit | What | Check |
|---|---|---|
| `16ce82f573`, `d9782e16c9` | G11 extended. `JOINT_ELEMENT_MAPPING_UNRESOLVED` covers no pipe, an unknown pipe, an unknown node, and a node off the pipe, checked before M07. A1-N-4: the lateral value is set to 0 so that M07 cannot mask the defect | **Fail first, then pass.** I ran the PR's three tests verbatim at main (`E/t_main_g11.log`). Missing stiffness gives all four cases `MECHANICS_SOLVED`, with 3/2/2/2 "consumed" rows. Unresolved mapping gives all four cases `MECHANICS_SOLVED`, with 0/3/3/3 rows. Both tests fail. The pipe-orientation and unknown-end test passes at main, because the pipe itself is already refused by name (`PIPE_ORIENTATION_INPUT_MISSING`, `PIPE_ENDPOINT_UNKNOWN`); ruling 3 accepts that (no silent skip). All three pass at the PR. Within RR Stage 2 ruling 3 |
| `7a0873eb5c` | A1-S-2, parts (a) to (c) | **(a)** The generator entry, page and hand calculation drop the deleted test and the pressure ranges. **(b)** The README is updated. **(c)** The witness loses MILLTOL's two values. **Reproduction:** the PR's CLI with `--explicit-local-private-intent` gives payloads equal to both committed DEL-10-05 witnesses (single-case and multi-case; `E/cli_*.json`). Without the flag it exits 1 and writes no file |
| `4aad4f42fa` (T1, T3), `5dc62d764c` (V1), `11a026b628` (T2) | The published texts now state the treatment truthfully | **T1, T3 and V1** are true at the PR: no bend or joint carries pressure, and the joint has no thrust. **T2** is true where it is published: the profile publishes it only with source-block recovery, and exact source recovery requires empty regions. **T4** (`preview_physics.rs:75`) is unchanged, as ruled, and MECH-TP-PHYS-008's id is kept. Within ruling 4 and its round-4 sections |
| `5bc6f269da` | A1-S-1: `primitive_loads`' `Pressure` arm and MECH-TP-PHYS-008/009's pressure halves removed | **No exact-route caller.** At `ba500defa4`, `prepare_straight_pipe_axial_effects` is called only by its own tests and by the mechanics benchmarks; PP never calls it. A pressure load now gets `UnsupportedTargetForCategory`. **Totals:** 12 → 3 N; the suite has 192 values. **Tests:** `primitive_loads` 49/49 and mechanics benchmarks 39/39. A2-N-2 notes the relaxed frozen-projection check. Within ROOT's A1-S-1 ruling |
| `70e7f49ced` | The DEL-10-05 procedure passes the local-private intent | Reproduced (above). A documentation truth fix |
| `1e9724fb94` | Merge of I114's lane (RV128 confirmed) | Two conflict hunks (`git show --cc`). **`pressure_runtime.rs`:** the bypass removal plus I114's single re-author text (S-1). **`validation_manual/index.md`:** both sides' rows. Both are right |
| `11a026b628` | T2 re-pins under the extended check | §3 |
| `fe657e3a68` | Demo records regenerated | Against `1e9724fb94`, only `source_input_files`, `source_input_files_after` and `inventory_json_sha256` change in both records |
| Merge with main | `lib.rs` imports | §4 |

## 2. Bytes on the PR code commit (`E/bytes_{main,pr}.jsonl`, `E/compare_a2.json`)

**The setup:**
- My harness v3 (`E/scripts/rv127_bytes_v3.rs`) compares 9 fields as before and also dumps every output, in debug, in the registered profile.
- The base is main `ba500defa4`; the candidate is `8a12de28db`.
- The sample (`E/sample_labels.json`) is REVIEW.md's, plus every source-block request, contract-corpus case 67 (V1), result_export producer case 1 (T1) and the numerical-sensitive torsion model.
- Every input is byte-identical in both trees.

**The classifier** (`E/scripts/compare_a2.py`) compares each differing output leaf by leaf. A leaf is "declared" when main's string with the declared replacements applied equals the PR's string. It is a digest when it is a digest-named key with digest values. Anything else is "other".

| Set | Rows (docs × 2 modes) | Equal on all 9 fields | Declared strings and digests only | Other |
|---|---|---|---|---|
| E | 32 | **32** | 0 | **0** |
| B1 | 16 | **16** (W1: 10 successors, 6 ordinary) | 0 | **0** |
| F | 74 | 42 | **32** | **0** |
| P (nonzero legacy, refused) | 10 | 0 | 0 | 10: S-1's single text, the retirement itself |
| R (REVIEW.md's refusal probes) | 26 | 0 | 0 | 26: the retirement itself (refusals, the R3 text) |

**The 32 F rows:**
- **T2, 24 rows:** the 12 source-block requests, each in both modes. In every row the declared leaf is the only non-digest difference: the ordinary result and the runner's mechanics differ in it plus 2 digests, the runner output in it plus 3, and the source-block document in it plus 7.
- **T2, 2 rows:** the numerical-sensitive torsion model (source-block recovery selected), with the same shape.
- **V1, 4 rows:** case 67, base and applied: the declared message, plus one runner-output digest.
- **T1, 2 rows:** producer case 1, the curved bend: the declared basis, plus one runner-output digest.

No sample row publishes T3, the joint row: no joint forms an element. Signed zeros are exercised: rows with `-0.0` are E 32/32, F 46/74 and B1 12/16. Bytes are equal, so H-1 still holds.

## 3. The T2 carriers (ROOT's option (a))

**Shape and content of the 12 raws:**
- Each of the 12 raws (6 main, 6 `ui/`) differs from main in exactly 3 leaves: `limitations[1]`, `publication_sha256` and `receipt_sha256`. This is steps (i) and (ii).
- Each committed raw equals, as JSON, the PR's own fresh output for its request in its mode: 12/12. This is step (iii) at value level. The files are pretty-printed, so the bytes differ in formatting only.
- The baseline at main reproduces each of main's committed raws the same way: 12/12.

**Hashes and pins:**
- All 24 of `generation.json`'s entries match their files at the PR.
- `retained_precision_carrier_cases.json`'s `source_blocks_n05_sparse.sha256` equals the re-pinned file's hash (ROOT's item 1).
- The Rust pin's two constants pass: PP `--test f1b_w2_runtime` 14/14, and `f1b_w2_exact_block_selection_of_a_range_triggered_case_publishes_mains_bytes` among them.
- The UI precision pair is a string-only edit of main, with one occurrence each.

**The sweep at the PR code commit, outside `P/execution`:**
- the 12 old raw hashes: 0 hits;
- the 4 retired SHA constants (the 2 re-pinned ones and the 2 from the deleted zero-pressure pin): 0 hits.

The old T2 text remains only in the two `rejected_stress_range` captures, which are ruled historical, and in the two precision files of A2-B-1.

**Readers (step (iv)):** the RS reader verifies the carriers (A2-N-4).

## 4. The merge resolution (`E/merge3_check.txt`)

**Method:** for the 7 paths that both main (since `7eae707bb7`) and the retirement changed, I ran `git merge-file` with the retirement `fe657e3a68` as ours, `7eae707bb7` as base and main `ba500defa4` as theirs.
- **6 merge cleanly,** to exactly the PR's blob:
  - `stress_recovery/src/lib.rs`;
  - `pressure_runtime.rs`;
  - `preview_physics.rs`;
  - `retained_memory_law_tests.rs`;
  - `retained_product.rs`;
  - `test_retained_precision_contract.py`.
- **PP `src/lib.rs` has one conflict, in the imports.** The PR keeps main's I109 comment and `correct_norm::{norm2, norm3}`, and takes the retirement's `exact_sum::ExactAccumulator` without `exact_rounded_sum`. That is right:
  - main's only `lib.rs` uses of `exact_rounded_sum` (`:5306`, `:11482`, `:13913`) were the legacy pressure path, which is now removed;
  - `pressure_sum.rs` uses it by path;
  - PP builds and its tests pass at the PR (`E/t_pr_pp_*.log`).
- NUM's `d92d05a31c` shows the same single hunk (`git show --cc`), and `2fd24aedf1` merges cleanly.
- **Apart from A2-B-1,** the PR's code tree equals NUM's: a `--no-renames` diff outside `P/execution` shows only those three paths.

**The B1 profile pin at the PR** equals the retirement's (−800 B). `profile_in_build_record` and `challenge_bounds_are_the_profile` are asserted in the registered build and pass.

## 5. Spot checks at the PR (`E/t_pr_*.log`)

| Suite | Result |
|---|---|
| PP `--lib`: the three G11 tests, profile record and challenge bounds, curved-bend rows (T1), dispatch, N-6 and label refusals, B-1, N-4, M07 refusal, the demo refusal | 14/14 |
| PP `--test f1b_w2_runtime --test pressure_runtime` | 14/14, 15/15 |
| RE (the RS reader; one scan test skipped, A2-N-4) | carriers 16/16, `source_blocks` 15/15, `physics_source_contract` 7/7 |
| `primitive_loads` | 49/49 |
| mechanics benchmarks | 39/39 |

## 6. Host

- **Commands:** every cargo command went through `WT/tools/t3_cargo.sh` (`--locked --offline`), in fresh targets `WT/targets/rv127-a2-*`, with `TMPDIR` under `S`.
- **No Git writes.** `WT/t3-pret` and `WT/u3-pr` were read only.
- **Deleted afterwards:** the archive copies, the targets and the output dumps (467 MB). `S` is kept for the confirmation of A2-B-1's repair.

## Records (`_run_records/addendum_02/`)

- **`scripts/`:**
  - `select2.py`;
  - `rv127_bytes_v3.rs`;
  - `run_bytes3.sh`;
  - `run_a2_tests.sh`;
  - `compare_a2.py`;
  - `probe_g11_before_main.rs.txt`.
- **Byte evidence:**
  - `bytes_{main,pr}.jsonl`;
  - `compare_a2.json`;
  - `sample_labels.json`.
- **Tree and merge evidence:**
  - `pr_vs_num_tree.txt`;
  - `merge3_check.txt`.
- **CLI outputs:** `cli_benchmark_{single,multi}_case.json`.
- **Logs** (progress and result lines only): `bytes_*.log` and `t_*.log`.

Sums are in the folder's `SHA256SUMS`. Paths use placeholders only.
