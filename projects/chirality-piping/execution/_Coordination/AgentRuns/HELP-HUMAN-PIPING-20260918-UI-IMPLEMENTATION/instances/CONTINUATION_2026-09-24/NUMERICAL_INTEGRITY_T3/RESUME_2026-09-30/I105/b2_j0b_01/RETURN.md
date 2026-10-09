# I105, J0b step 1: `b2` absorbs U3 (#1168's head)

TASK (Type 2), I105, for WORKING_ITEMS for T3 (Agent 1), the return path. I made no delegation. 2026-10-09 UTC.

**Basis:**
- `R/BRIEFS/B2_J0B.md` (sha256 `c7beaf0a…d2ed`, verified; NUM `b3fb7272f7`);
- WORKING_ITEMS' J0b message: merge #1168's head `37724dea27` now; `b2` does not move.

**Placeholders:** WT, P, R; PP = `P/core/product_physics`; RE = `P/core/reporting/result_export`.

**Step 2** (merging main after #1168 merges) waits for WORKING_ITEMS to name the main commit.

## Commits on `codex/piping-t3-b2-j0b-20261009` (WT/b2-j0b; not pushed)

| Commit | What |
|---|---|
| `163871eb3b` | merge of #1168's head `37724dea27` into `b2` `e582b61f9e`. Textually clean (merge base `ec5d397359`). `git show --cc` of the merge is empty |
| **`b446fb0cd6`** (head) | b2's `b2p_early_hook_refuses_combinations_outside_d14` (lane P) gets U3's `case_source` arity. U3 dropped the always-empty `pressure` parameter at every call in `retained_product_tests.rs`, but b2's new call still passed it, so the merged test crate did not compile. The same one-token edit; the inputs and checks are unchanged |

**Host screen:**
- `37724dea27..b446fb0cd6` (everything this branch adds over #1168): 0 hits, 79 files.
- `163871eb3b..b446fb0cd6`: 0 hits.
- `e582b61f9e..b446fb0cd6` gives 13 hits. All are in three `projects/chirality-app-v4` records from main's #1167, which are #1168's head bytes, unchanged (`merge/host_screen_range_summary.txt`).

## 1. The nine files changed on both sides (`merge/nine_u3.diff.gz`, `merge/nine_b2.diff.gz`)

| File | U3's side | b2's side | Why the merged result is right |
|---|---|---|---|
| `PP/src/lib.rs` | 100 hunks: removes the legacy computation (thrust builders and assembly, `pressure_for_pipe`, the hoop and longitudinal rows, `DerivedSection.membrane_radius`), the `exact_rounded_sum` import, and T2's limitation text | 13 hunks, all retained W1 plumbing (`W1Fallback`, `permitted_run`, `CaseSet`/`w1_case_ids`, `retained_w1`, `w1_transaction`, `retained_tests_hooks`), base lines 2207–3570 | U3 has no hunk in that range; its nearest end at base line 2151. b2's code references no removed item (searched). The two capture calls (`case_source` and `prepared_case_source`) carry U3's arity |
| `PP/src/retained_product.rs` | drops the `pressure` parameter of `case_source`/`capture_case_source`/`prepared_case_source`, the always-false `!pressure.is_empty()` scope disjunct, and `membrane_radius` in one `DerivedSection` literal | combinations, the B3b exact route, `support_observables`, `combination_call` | Different lines. The capture's refusal set is unchanged: the removed disjunct was always false |
| `PP/src/retained_product_tests.rs` | the trailing `&[]` dropped at 7 calls | adds `b2p_early_hook_refuses_combinations_outside_d14` (one call in the old arity); edits i51_c0's "combination" case | The merged text did not compile; `b446fb0cd6` applies U3's edit to b2's one call |
| `PP/src/retained_memory_law_tests.rs` | re-pins `PINNED_RECORD` (−800 B per phase, both modes) and its doc | B2-A's D1.4 tests, the B3a-drop and B3b tests, and J0a's M and MARGIN | b2 changes no profiled struct and holds no profile pin of its own. `profile_in_build_record` passes at the head, and the registered build's tests pass |
| `PP/tests/s11f_site_test.rs` | removes the E15/E16 legacy rows (producers, the rule-8 table, formation sites, module doc) | J0a's `combination_call` row | Disjoint. All 11 site tests pass, rule 8 included |
| RE `tests/retained_precision_contract.rs` | adds two rows to `b1_r2_g_model_scope_at_g8_invocation` (the label at the base schema, and at 0.3.0), expecting `gate("G8", "RETAINED_PRECISION_INVOCATION_MISMATCH")` | B3 reader tests elsewhere in the file | That table's expectation is unchanged in b2. b2's own B3a-drop table expects the same code for the 0.3.0-plus-label shape |
| `P/tests/test_retained_precision_contract.py` | the same two rows in `test_b1_repair02_model_scope_at_g8_invocation` (`INVOCATION`) | D31 (B3D-10, the B3a drop), DEF-O's H in `apply_mutation` | Different lines; both expect G8 `INVOCATION_MISMATCH` |
| TS `retainedPrecision.test.ts` | the same two rows in the "B1 SR-TS repair 01" C2 table (`INVOCATION`) | the B3 readers' tests and 07n's | Different lines; the same agreement |
| TS `previewService.ts` | the bundled demo model and results switched to the demo set, validated as preview-physics-1 (lines 624–730) | the import line and `validateCapturedSource`'s retained-route registration (`isRetainedRoute`) | Different functions, each independent of the other. vitest passes |

No change alters B2/B3 behaviour or U3's behaviour, and no design choice arose.

## 2. U3 and the B3a drop agree (`b3a/pp_probe_{h,u}.txt`, `probes/`)

**The probes:**
- **PP:** a scratch test module added only to the archive copies (`probes/i105_j0b_probe.rs`, never committed) runs the milestone with the label through the ordinary route and the retained Direct entry, both modes, at h and at u. Two variants: the label on the milestone's own schema 0.1.0, and m3l (0.3.0 plus the label).
- **Readers:** two shared shapes on `ordinary_prepared_synthetic` (`probes/reader_probes.json`): the label alone, and schema 0.3.0 plus the label. They run through RV113's RS and TS harnesses and I100's PY harness.

| Shape | PP ordinary route (h = u) | PP retained Direct entry at h | at u | RS, TS, PY bound (h = u, byte-identical outputs) |
|---|---|---|---|---|
| m3l: 0.3.0 + `1.0.0/legacy_pressure_v1` | `MODEL_INCOMPLETE`, 0 rows: `PRESSURE_MODEL_REAUTHOR_REQUIRED` (blocking, ref `pressure_contract`) | G-A D1.3 `Family(Namespace, PressureContract)`; no W1, no successor; publishes the ordinary refusal byte for byte | D1.3 `Family(Namespace, SchemaVersion)`, and the same publication | G8 `RETAINED_PRECISION_INVOCATION_MISMATCH` in all three |
| 0.1.0 + the label | `PREVIEW_CONTRACT_VERSION_MISMATCH` (blocking, ref `pressure_contract`; its text names the label as retired) | D1.3 `Family(Namespace, PressureContract)`; ordinary bytes | the same | G8 `RETAINED_PRECISION_INVOCATION_MISMATCH` in all three |

- **The gates agree.** D1.3 refuses first and both publish the ordinary refusal. At u, D1.3 has no 0.3.0 branch, so its fact for m3l is `SchemaVersion`; b2's B3 namespace adds the branches, so it is `PressureContract`, as B3a's drop states. U3's own test admits any Namespace fact (`Family(Namespace, _)`).
- **No refusal moved and no expected gate changed.** b2's `b3a_dropped_m3l_takes_the_ordinary_route` and `b3a_dropped_direct_entry_refuses_m3l` compare with the live ordinary bytes, which are now U3's refusal, and pass unchanged. So do `b3a_dropped_d1_3_refuses_the_legacy_pressure_contract_on_0_3_0`, the readers' B3a-drop tables and U3's three refusal tests.

## 3. T2 in b2's own files: 0 hits, 0 re-pins (`t2/`)

**The search** (`t2_search.py`) covered all 79 files b2 adds (12) or changes (67) over main, at b2's head and at the merged tree. It looked for:
- the old text and three fragments;
- JSON string values with escapes resolved;
- Rust and TS text with line continuations removed;
- the 34 old digests: `11a026b628`'s removed SHA-256 values plus the U3 package's `radius_sweep.txt` list;
- the SHA-256 of the old text, raw and JSON-quoted.

**Result:**
- **At the merged head:** 0 hits.
- **At `e582b61f9e`:** the only hit is the old text in `PP/src/lib.rs`'s `preview_formulation_basis`. That is main's own limitation, which the merge replaces with U3's T2.
- **Successors:** b2's emitted successors (J0a's 22 B2-P documents) carry `preview_physics`' limitations (T4, unchanged by ruling), not T2. Their pins pass at the head.
- **Elsewhere in the merged tree:** the old text remains only in the two `rejected_stress_range` captures, as ruled.
- **The three retired fixtures:** none of b2's files references them. The remaining references are historical docs, logs and sweeps; no test reads them (`retired_fixture_refs.txt`).

**Re-pins:** none needed. U3's re-pinned carriers (12 source-block raws, `generation.json`, the carrier-cases hash, f1b_w2's two constants) are read at the head by the PP, RE, PY and TS suites, all passing.

## 4. Suites and census

The three sides:
- **h:** `b446fb0cd6`;
- **u:** `37724dea27`;
- **b:** `e582b61f9e`, J0a's evidence: PP at `e582b61f9e`; the other suites and the census at `9f5cfbcd75`, which differs only in PP's s11f test file.

h and u ran in archive copies, one heavy job at a time. The comparison is test by test (`suites/SUITES_CMP.json`, `census/CENSUS_CMP.json`).

| Suite | b | u | **h** |
|---|---|---|---|
| PP, all targets | 796 ok, 79 ignored | 732 ok, 79 ignored | **785 ok, 0 failed, 79 ignored** |
| runner | 87 ok | 89 ok | **89 ok** |
| RE | 213 ok | 199 ok | **213 ok** |
| vitest | 4,288 passed | 4,249 passed, 1 todo | **4,292 passed, 1 todo** |
| tsc | rc 0 | rc 0 | **rc 0** |
| PY reader set | 2,730 passed, 30 skipped | 2,312 passed, 30 skipped | **2,732 passed, 30 skipped** |

**No test changes outcome on either comparison.** Every difference is U3 arriving or b2's own work:
- **Against b** (each added test exists at u, and each removed test is absent at u):
  - **PP:** +11 U3 tests (the three legacy-label and zero-primitive refusals, G11's three joint tests, the realized-joint refusal, the demo refusal, the thermal half restored, `non_exact_source_blocks_gate…`, `pressure_runtime`'s retirement test). −22 U3 removals (the 11 `*_historical_pressure_premise` tests and their kin, S-11F's F10 pair, the historical scope's two tests, f1b_w2's zero-legacy admission, `legacy_model_three_retains_ordinary_route…`, `current_composite_derived_normal_friction_and_reversal`, `expansion_joint_user_stiffness_emits_macro_element_review_rows`, `pressure_thrust_on_macro_span…`).
  - **Runner:** +3, −1 (the mechanics suite goes from 25/206 to 24/192; two CLI refusals).
  - **vitest:** +11, −6 (U3's and I114's renames and additions; the T6 todo).
  - **PY:** +2 (I114's demo record-truth test, both modes).
  - **RE:** no change. U3's rows are inside an existing test.
- **Against u** (each added test exists at b):
  - PP +54, RE +14, vitest +44, PY +420: b2's own.
  - Removed: PP `b1_sa_runner_oracle_literal_is_load_cases_plus_one` (B2-A's re-base, kept as `b2_a_runner_oracle_literal_is_case_equivalents_plus_one`), and vitest D31 (renamed by the B3 readers). Both are as in J0a.

**Census: 0 changes in all 18 comparisons.** RV113's RS and TS harnesses and I100's PY harness, unchanged and hash-checked, ran over:
- 07m (339 entries);
- B1's 07n (638);
- 07n-N (main's and U3's corpus, 638).

Whole records were compared entry by entry, at h against b and against u, in RS, TS and PY.

## 5. Dispatch request

Please push `codex/piping-t3-b2-j0b-20261009` at **`b446fb0cd6`** and dispatch Linux CI on it. After #1168 merges, name the main commit and I merge it as step 2.

## Stops and open points

None.

## Host

- **Jobs:**
  - Every cargo run went through `WT/tools/t3_cargo.sh --locked --offline` with toolchain 1.97.1, using targets `WT/targets/i105-j0b-*`.
  - Every other heavy job went through `t3_slot.sh`.
  - One heavy job ran at a time, and the first queued behind #1168's exclusive DEC-025. I signalled no other job.
  - No DEC-025, no installs, and no RSS or timing measurements.
- **Copies:** vitest ran in archive copies, with `node_modules` linked after a `cmp` of `package-lock.json` (unchanged by U3), and the wasm assets copied, never built.
- **Junit:** host attributes were removed.
- **Records:** written here directly, with placeholders only. The records screen (host-screen patterns, `.gz` decompressed) found 0 hits. `SHA256SUMS` covers every file.
