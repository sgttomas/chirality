# RV127: the fresh independent review of U3 Stage 1 (the legacy pressure contract retired)

**Who:** RV127, TASK (Type 2), independent reviewer dispatched by WORKING_ITEMS for T3 (Agent 1), 2026-10-08 UTC. I wrote none of this code and did not delegate.
**Brief:** `R/BRIEFS/RV127_U3_STAGE1.md` (sha256 `e26283fa…9bd517e68`, verified), read with `R/BRIEFS/B1_COMMON.md` (`2d170307…15eb2c75`), NUM's `AGENTS.md` and `agents/AGENT_TASK.md`.
**Basis:** RR "Owner decisions: the legacy pressure contract is retired product-wide; …" and RR "U3 rulings on I110's pressure inventory: D-1 A, D-2 A1, D-3 held with M07"; the implementer's `R/I110/pressure_retire_01/` (RETURN `d6edc387…`, `inventory.json`) and `R/I110/pressure_retire_02/` (RETURN `91b645ab…`; its SHA256SUMS verify).

| Head | Base | What |
|---|---|---|
| `4c0d5d7c00` (`codex/piping-t3-pressure-retire-20261008`, `WT/t3-pret`) | main `7eae707bb7` (B) | 4 commits, 22 files (`79a5a7f316` refusals, `390c882619` oracle deletions, `28bc6a25e1` authoring, `4c0d5d7c00` refusal tests) |

**Placeholders:** `WT`, `NUM`, `P`, `PP`, `RE`, `T`, `R`, `RR` as in the brief. `A` = my archive copies `WT/rv127/{base,cand,probe}` (`git archive` of B and of the head, `P/execution` and `P/apps` excluded; `probe` = the head plus one probe-only test). `S` = `WT/scratch/rv127_u3/`. `E` = this folder's `_run_records/`. Line numbers are at the head unless marked B.

## Verdict: **FAIL** at `4c0d5d7c00`, on B-1 only: 1 BLOCKING, 1 SHOULD-FIX, 8 NOTE

- **Exact and pressure-free behaviour is byte-identical.** I read every `validate_profile` hunk and every route that reaches it. The exact contract's acceptance and checks are unchanged (§1). My own harness, run at B and at the head in the same debug build (the registered profile), compares 9 fields per row: ordinary envelope; the retained direct entry's publication and its kind (W1); the runner's serialized output, mechanics envelope, RE export document and export unavailability; the runner's retained headless output and document. **All 98 sample rows are equal:** 16 exact documents, 25 implicit pressure-free documents and 8 of B1's corpus, each in both modes. The B1 rows include W1, with 10 successors and 6 ordinary publications (§1.3). The 5 committed nonzero-pressure documents keep their refusal bytes as well (10 rows). My head hashes also equal I110's own release-build rows for every ordinary and runner mechanics envelope in the sample (98/98), and for W1 (16/16).
- **The refusals are complete.** The label, and a pressure primitive of any value (zero, −0.0, nonzero; category `pressure` or dimension `pressure`), are refused on all four entries: ordinary, retained direct, runner, and runner retained headless. The retained entry publishes the ordinary refusal byte for byte (26 probe rows, §2). No product route accepts the label. No user-model route reaches the legacy computation outside the held scope. The one remaining non-model route is noted in N-1.
- **B-1, BLOCKING:** one deletion is not pressure-only. Commit `390c882619` deleted a test whose thermal half the code itself marked "a current public check". The repair is a pressure-free thermal test, and I ran it on the head (§3).
- **S-1, SHOULD-FIX:** the nonzero primitive refusal keeps its old text. That text does not name `2.0.0/exact_straight_pressure_v2` and still frames the refusal as "nonzero". This departs from I110's own inventory and from D-4's re-authoring text.
- **The held items are untouched** (§5).

## Findings

| ID | Class | Where | Evidence | Remedy |
|---|---|---|---|---|
| B-1 | **BLOCKING** (brief item 3: "each deletion is a pressure-only oracle"; I110's brief: a weakened check is a stop) | B `PP/src/lib.rs:22322-22369`, deleted in `390c882619`: `endpoint_section_cut_fixed_and_free_pressure_thermal_match_uniform_stations_historical_pressure_premise` | The test ran two premises. The pressure premise ran inside the historical scope. The thermal premise ran on the ordinary route, and B `:22341` says "The pressure-free thermal premise remains a current public check". For a fixed-fixed and a free (cantilever) thermal pipe, in both modes, it checked: end-i axial-normal stress = end-j = the three stations, and the fixed state is compressive. Nothing on the head replaces it. `fixed_fixed_thermal_load_applies_axial_fixed_end_correction` (`:19301`) checks only end-i in the default mode, fixed only. The p5 test (`:22285`) checks only station *forces*, fixed only. The free case and the endpoint/station *stress* uniformity are lost. `390c882619`'s message says "Deleted, each pressure-only", and I110's plan lists the test among the "pressure-only oracles". My probe (the thermal half verbatim, pressure branch dropped, `E/scripts/probe_thermal_half.rs.txt`) passes on the head: §3 | Restore the thermal half as a current pressure-free test, e.g. `endpoint_section_cut_fixed_and_free_thermal_match_uniform_stations`, outside the historical scope. That is +1 test in the outcome diff. Correct "each pressure-only" in the PR body or change record. Whether to recut the commit message is WORKING_ITEMS' call |
| S-1 | SHOULD-FIX (brief item 2; D-4) | `PP/src/pressure_runtime.rs:226-228` (the nonzero arm). I110's own inventory site `PP/src/pressure_runtime.rs:223` gives the disposition "edit message … re-author to 2.0.0/exact_straight_pressure_v2"; RETURN round 1 Q4 gives one re-author text for any primitive | A nonzero legacy primitive is refused with the pre-U3 text: "a fresh solve cannot publish the legacy nonzero pressure model; explicitly author exact pressure regions, closure paths and E/nu material inputs". It does not name `2.0.0/exact_straight_pressure_v2` (probe rows R2, R8 and every P row). Its "nonzero" framing now implies that a zero value is publishable, which A1 refuses. The other three refusal texts name the exact contract (§2). The implementer kept it so that "the demo's refusal envelopes keep their bytes". Those bytes are `P/fixtures/product_preview/invented_mechanics_result_preview_physics_1_{sparse,dense}.json` and their generation record `preview_physics_fixture_generation.json` `outputs[].sha256`. These are neither held nor exact-contract values | (a) Use one re-author text for any value, naming `2.0.0/exact_straight_pressure_v2`. Regenerate the two preview-physics-1 demo refusal fixtures with their recipe (`tools/serialization/generate_product_preview_mechanics.mjs`) and update the record. **Or** (b) WORKING_ITEMS accepts the deviation and records it in the PR body (the text does direct users to exact authoring) |
| N-1 | NOTE, **for ROOT** (scope statement) | `P/core/runner/headless/src/benchmark_binding.rs:1040-1048` → `P/validation/benchmarks/stress/src/lib.rs:576-590` → `P/core/loads/stress_recovery/src/lib.rs:929` (`pressure_membrane`) | The shipped CLI's `run-benchmark` (suite `stress`) still executes the legacy thin-wall hoop and longitudinal formula on a fixed invented fixture (`STRESS-PRESSURE-MEMBRANE-ORIGINAL`, inputs `PressureBasis(100, 3, 0.5)`). It reports the result as a passing benchmark. No user model reaches it. I110 places its removal in Stage 2, but it does not depend on M07. RR says that after Stage 1 "no product path reaches the legacy computation". That holds for model solves only | ROOT: either qualify the statement ("no model solve reaches …") or move this removal (benchmark, runner binding, hand calc, manual page) into Stage 1. It has no M07 dependency |
| N-2 | NOTE, **for ROOT** (public vocabulary) | `P/core/model_operations/operation_applier/src/lib.rs:4961-4973` | A new public operation diagnostic, `OP-PRESSURE-PRIMITIVE-RETIRED` (blocking). Its message names `PRESSURE_MODEL_REAUTHOR_REQUIRED`, and its remediation names `2.0.0/exact_straight_pressure_v2` and `pressure_regions`. D-4 ruled reuse for the product refusal only, and no registry of `OP-` codes exists outside the applier. It follows from the decision, but it is a new code | ROOT notes or accepts the new code. Alternatively it could reuse `OP-CREATE-PRIMITIVE-LOAD-PAYLOAD-INVALID` with the retirement text. No defect either way |
| N-3 | NOTE, **for ROOT** (D-3 held) | B `PP/src/lib.rs:20943` `generated_result_metadata_and_historical_quantization_match_legacy_fixture_historical_pressure_premise`, deleted in `390c882619` | This was the only test that tied `invented_mechanics_result.json` (D-3) to the code (the "legacy carrier check"). Deleting it is D-3 option (a)'s "the oracle that regenerates it is deleted" step. RR holds D-3 "unchanged in Stage 1". The fixture file is unchanged, and no D-3 option keeps a nonzero-pressure oracle | ROOT confirms that this deletion belongs to Stage 1 and does not prejudge D-3 |
| N-4 | NOTE (dead defensive gate) | `PP/src/source_recovery.rs:604-608` ("legacy source-blocks namespace requires model0.1/0.2 without pressure contract or regions") | Every input that reached this branch is now refused first by `validate_profile` (a non-exact 0.3.0 or 0.4.0 contract, or a contract or regions on 0.1.0/0.2.0), and `run_linear_static_preview_observed` returns before the solve (`PP/src/lib.rs:2394-2418`). Its only test was the old label test, which `79a5a7f316` replaced | Stage 2: remove it, or pin it at unit level. No action needed in Stage 1 |
| N-5 | NOTE (panel wording) | `P/apps/desktop/src/features/pressure-authoring/PressureAuthoringPanel.tsx:68-73` | (a) "retired" keys on `mode` alone. A `1.0.1/legacy_pressure_v1` document shows "retired; … re-authored", while the solver says `PRESSURE_CONTRACT_UNSUPPORTED`. Both refuse. (b) A 0.1.0/0.2.0 model that still carries legacy primitives, such as the bundled demo, shows "none (pressure-free; legacy pressure primitives are refused)". "Pressure-free" is D-1's word for the namespace, but a reader may take it as a statement about the model | Optional: also match `version === "1.0.0"`; say "none (pressure-free namespace; …)" |
| N-6 | NOTE (test coverage) | `PP/tests/pressure_runtime.rs:823` (ordinary only); retained `PP/src/source_receipt/tests.rs:456` and runner `…/openpipestress-runner.rs:1080` test the label only | Brief item 2 asks for "any pressure primitive in 0.1.0 and 0.2.0, on the ordinary, retained and runner routes". The behaviour is right on every entry (probe rows R4–R8, §2), but a zero-valued primitive is pinned only on the ordinary route. I110's plan asked for no more | Optional: add the zero-primitive document to the retained-entry and CLI refusal tests |
| N-7 | NOTE (pre-existing texts) | `PP/src/pressure_runtime.rs:117-120` (0.1.0/0.2.0 with any `pressure_contract`, the label included: `PREVIEW_CONTRACT_VERSION_MISMATCH`); `:131-137` (0.3.0 without a contract) | These refusals do not name the exact contract. A 0.2.0 document carrying the retired label gets "pressure contract namespaces require model document 0.3.0" rather than the retirement text. Not changed by this PR | Optional, Stage 2 or later |
| N-8 | NOTE (open verification) | `P/apps/desktop/e2e/r2-smoke.spec.ts:489-491` | The e2e spec was edited but not run on this host. The Mac cannot check PP `t13_committed_fallback_uz_is_byte_identical` or the runner's two load-reference frozen goldens; both fail identically at B and at the head here | The Linux CI dispatch of the head that I110 asked for. It must cover the actual candidate revision that merges |

## 1. Exact-pressure behaviour

### 1.1 The `validate_profile` hunks (`PP/src/pressure_runtime.rs:114-260`)

- **0.3.0 contract** (`:138-147`). Before, a non-matching pair was refused when it matched neither legacy nor exact. Now `declared == (1.0.0, legacy_pressure_v1)` gives `PRESSURE_MODEL_REAUTHOR_REQUIRED` (ref `pressure_contract`), and any other non-exact pair gives `PRESSURE_CONTRACT_UNSUPPORTED` (new text). For `(2.0.0, exact_straight_pressure_v2)` both conditions are false, so there is still no diagnostic. **Unchanged for exact.**
- **0.4.0** (`:122-129`), `is_exact` (`:80-86`), the objective-connector loop, the exact composition checks (`:170-208`) and the whole exact per-case branch (`:235-…`) are byte-identical to B.
- **Non-exact case loop** (`:210-234`). The `&& load.magnitude.value != 0.0` guard is gone, so a primitive with `category == "pressure" || dimension == "pressure"` is refused at any value. Values that compare equal to 0.0 (including −0.0) get the re-author text; NaN and nonzero get the old text (S-1). The `#[cfg(test)]` historical-scope bypass lines are textually unchanged. They now also cover zero, which keeps O1 and O3 (zeroed, in scope) unchanged.
- **Routes:**
  - `run_linear_static_preview_observed` (`PP/src/lib.rs:2394`) runs `validate_profile` first and returns the blocked envelope on any blocking finding (`:2416-2418`) before any solve. Every public entry dispatches to it: `run_linear_static_preview*`, `…_value_with_mode`, `…_with_retained_direct` and `…_with_retained_headless` (`:2153-2290`), and the runner (`run_preview_model_value*`).
  - `build_pressure_case_with_members` (`:442`) and the receipt replay (`PP/src/source_receipt.rs:162`) call it and stop on blocking or non-exact.
  - The legacy computation keys only on genuine pressure primitives: `genuine_pressure_element_target` (`PP/src/lib.rs:10840`) feeds `build_pressure_thrust_loads` (`:10801`) and `pressure_for_pipe` (`:13887`). So no model solve can reach it outside the `cfg(test)` scope.

### 1.2 The sample (`E/scripts/enumerate.py`, `select.py`; `E/sample_labels.json`)

I enumerated committed model documents independently, with `P/execution` and `P/apps` excluded; the inputs are byte-identical at B and at the head. I found E = 48, F = 178 (I110's 182 includes 4 app e2e documents), B1 = 32 (so 214 implicit pressure-free documents in all, matching I110), and 5 documents with nonzero legacy pressure. No committed document carries the label.

| Set | Documents | Spread |
|---|---|---|
| E | 16 | `PP/tests/fixtures`, `RE/tests/fixtures`, model operations, `load_reference`, `load_reference_source`, `physics_source` (including unicode and mixed units), qualification `first_static` and `load_reference` (6-node, multi-case) |
| F | 25 | the self-weight fixture, the preview-physics invented and unicode models, S11-F and S11-G cases (101 nodes), the model-operations corpus (combinations, range envelopes, bend and joint components, wind and seismic), the source blocks, `result_export_v0_2` producer cases |
| B1 | 8 | `retained_precision_cases` 0, 4, 6, 15, 17, 24; the L0 and W-C2 successor fixtures |
| P | 5 | the demo, the three `result_export_v0_2` pressure cases, the witness input |

### 1.3 Byte equality (`E/scripts/rv127_bytes.rs`, `run_bytes.sh`, `compare.py`; `E/bytes_{base,cand}.jsonl`, `E/compare.json`)

The harness was built in fresh targets `WT/targets/rv127-{base,cand}`, debug, through `WT/tools/t3_cargo.sh`. The build was admitted as the registered profile (admission `Registered/Unselected` on every row). There are 9 fields per row, listed in the verdict.

| Set | Rows (docs × 2 modes) | All 9 equal | Solved | W1 successor / ordinary | RE export documents |
|---|---|---|---|---|---|
| E | 32 | **32** | 32 | 0 / 32 | 28 |
| F | 50 | **50** | 26 | 2 / 48 | 18 |
| B1 | 16 | **16** | 16 | **10 / 6** | 6 |
| P (nonzero legacy, refused) | 10 | **10** | 0 | 0 / 10 | 0 |

- **Cross-check with I110's records** (`R/I110/pressure_retire_02/_run_records/bytes_hc_*.jsonl`, release build). My head ordinary hashes and runner mechanics hashes equal theirs on 98/98 rows, and my W1 kinds and hashes equal theirs on 16/16 B1 rows. RE export-document hashes differ between the two harnesses, because the document carries the runner run reference built from each harness's own `RunnerRequest`. They compare only within one harness, and within mine they are equal B-to-head.
- **B1's pins:** the B1 pin tests are in the 40-manifest suites, which pass unchanged (I110's outcome lists; §6).

## 2. The refusals

| Probe (`select.py`) | At B | At the head (all four entries) |
|---|---|---|
| R1: `physics_source/n05` (exact) relabelled `1.0.0/legacy_pressure_v1`, regions removed | **MECHANICS_SOLVED** (the legacy route) | `PRESSURE_MODEL_REAUTHOR_REQUIRED` [`pressure_contract`], the retirement text |
| R2: R1 plus a nonzero legacy primitive | refused (primitive) | refused (primitive, old text; and label) |
| R3: `1.0.1/legacy_pressure_v1` | `PRESSURE_CONTRACT_UNSUPPORTED` | the same code; the text names only the exact contract |
| R4/R5: a zero or −0.0 pressure primitive on B1 case 0 and on the preview-physics invented model | **MECHANICS_SOLVED** | `PRESSURE_MODEL_REAUTHOR_REQUIRED` [case, load], the zero text |
| R6: category `pressure`, dimension `force`, zero | `UNIT_INPUT_INVALID` | + `PRESSURE_MODEL_REAUTHOR_REQUIRED` |
| R7: category `hydrotest`, dimension `pressure`, zero | `HYDROTEST_PRESSURE_UNSUPPORTED` | + `PRESSURE_MODEL_REAUTHOR_REQUIRED` |
| R8: a nonzero primitive | refused | byte-identical to B (old text, S-1) |

- **The four entries agree.** On every probe row the retained direct entry publishes `ordinary`, with bytes equal to the ordinary envelope. The runner's mechanics envelope equals it as well, with export unavailability `SOURCE_NOT_SOLVED`, and the runner's retained headless entry gives `MODEL_INCOMPLETE`.
- **The texts** (distinct blocking messages over all probe rows):
  - label: "the 1.0.0/legacy_pressure_v1 pressure contract is retired; re-author the model to 2.0.0/exact_straight_pressure_v2 …" ✓;
  - zero primitive: "legacy pressure primitives are retired, zero values included; remove the primitive, or re-author the model to 2.0.0/exact_straight_pressure_v2 …" ✓;
  - unknown contract: "the supported pressure contract is 2.0.0/exact_straight_pressure_v2; …" ✓;
  - nonzero primitive: the pre-U3 text ✗ (S-1).
- **Readers at G8:** RS (`RE/tests/retained_precision_contract.rs:4730-4749`), PY (`P/tests/test_retained_precision_contract.py:1466-1471`) and TS (`retainedPrecision.test.ts:1291-1293`) each add the label at the milestone schema and at 0.3.0, refused at G8 `INVOCATION_MISMATCH`. Each reader's existing rule is "any non-null `pressure_contract`" (RS `:3519`, PY `:1503`, TS `:1143`). No reader re-author message was added, so B3-D's refusal table is unchanged.
- **App:**
  - The load-case manager no longer offers `pressure` (`LoadCaseManagerPanel.tsx:587-596`), and `primitiveLoadCategoryFromValue` is used only by the create draft (`:426`).
  - The panel texts are covered in §4.
  - src-tauri: a labelled 0.3.0 document opens with status `current` and no migration, and its solve is refused (`src-tauri/src/lib.rs:6892-6920`). The migration doc comment (`model_document_migration.rs:17-24`) is right.
- **Applier:**
  - `create_primitive_load` with category `pressure` is refused before any unit or target work (`:4961-4973`), at nonzero and zero (test `:10920-10957`).
  - Its now-unreachable pressure arms are removed.
  - The only primitive edits are `primitive_loads.N.magnitude.value` (`is_primitive_magnitude_path`, `:7957-7965`) and deletion, so a pressure primitive cannot be authored another way. An existing one can still be edited and deleted, as the plan says, and the solve refuses it at any value.
- **No route accepts the label:** across `P/core`, `P/apps/desktop/src{,-tauri}` and `P/tools` it appears only in the refusal constant, its tests and the panel text. The exact-evidence tamper test (`RE/tests/physics_contract.rs:97`) is unchanged.

## 3. Deleted and edited tests

| Change | Plan | Protected property kept? |
|---|---|---|
| 11 `*_historical_pressure_premise` tests deleted (all except O2 and O4) | §5 Stage 1.2 | **10 of 11 are pressure-only or have a pressure-free twin on the head:** <br>- `…endpoint_stress_components…` → `…_without_pressure` (`:15493`) <br>- `mixed_units…` → `…_without_pressure` (`:15430`) <br>- `…curved_endpoints_use_all_six_arc_resultants…` → `…_without_pressure` (`:15189`) <br>- `curved_bend_macro_span_pressure_reaches_nonlinear_loop…` → `curved_bend_macro_element_solves_assembled_nonlinear_loop` (`:23395`) <br>- thrust correction, thrust direction, genuine-pressure leaves, two-pressure sum and arc membrane: pressure physics only <br>- the D-3 carrier oracle (N-3) <br>**`endpoint_section_cut_fixed_and_free_pressure_thermal…` is not pressure-only (B-1)** |
| `curved_bend_pressure_load` helper | 1.2 | used only by the deleted tests |
| S11-F F10 (2 tests, `f10_pressure`, `pressure_joint`, `pressure`) | 1.2 | pressure folds inside the scope only |
| S11-G T6a: the pressure-thrust run dropped, `pressure` helper deleted | 1.2 / 1.3 | The floor-kill (M11) still holds through the two thermal runs with `fires_without_floor = true` |
| `f1b_w2_admission_refuses_a_zero_legacy_pressure_as_pressure_thrust` and its family arm | 1.2 | The `pressure_thrust_load` family is still pinned at unit level (`PP/src/f1b_tests.rs:2285-2288`), and the doc comment at `f1b_w2_runtime.rs:699-705` says so |
| `profile_dispatch_requires_explicit_regions_and_refuses_legacy_pressure` | 1.3 | Every earlier assertion is kept. Zero is now refused; the label is refused; `1.0.1` stays unsupported; a 0.2.0 document without primitives passes |
| the source-receipt label test → ordinary refusal; + a retained-entry test | 1.3 / 1.4 | "No source-block recovery" is still asserted. The "legacy source-blocks namespace" message is now unreachable (N-4) |
| `mechanical_fixture_for_test`: strip instead of zero for the 39 non-held purposes (`:14878-14897`); O1 and O3 keep zeroing | 1.3 | **No assertion of any user moves.** The only lib.rs `+` hunk is the helper; every other lib.rs hunk is a whole-function deletion. All 41 purposes exist (39 non-held + O1, O3), and I110's outcome lists show them all passing |
| 5 runner helpers: strip instead of zero | 1.3 | `preview_physics_admission.rs` now also strips by `dimension`. The binding test skips only `curved-pressure-full`, guarded by an `assert_eq!` on the case id; that case would be load-free. Its refusal is pinned by `public_nonzero_legacy_pressure_refuses_before_opaque_proof_or_export` (`result_envelope_binding.rs:608-623`), and the curved binding is still covered by `curved-tip-weight-full`. This deviates from the plan's "expects the refusal", and the commit message says so |
| applier: 2 tests (the refusal; the kN/m compound unit replaces kPa) | 1.3 | The thermal case and the missing-pipe case now use thermal. Compound-unit preservation is still exercised |
| `App.test` "queues and applies a pressure primitive" → "not offered" | 1.3 | The apply-route assertions it dropped are all carried by the thermal twin ("queues and applies a thermal primitive load…": summary counts, `session_state_only_not_yet_saved`, pending operations, `applied_operations=1`, `state=not_started`) |
| e2e smoke | 1.3 | The category is absent and the note is shown. Not run here (N-8) |

**Probe result (B-1's remedy).** I took the deleted test's thermal half verbatim, dropped the pressure branch, inserted it into `A/probe` (`tests::rv127_probe_endpoint_section_cut_fixed_and_free_thermal_match_uniform_stations`) and ran it on the head. It **passes** in both modes:
- fixed: end-i = −24.000000000000004 MPa (compressive), equal to end-j and every station;
- free: 4.1·10⁻¹⁵ MPa (dense) and −0 (sparse), equal at end-j and every station.

So the restored test needs no re-pin.

**My spot checks** in `A/probe` (PP `--lib` and integration, debug, `WT/targets/rv127-probe`; `E/probe_*.log`). **16/16 pass:**
- the probe;
- the edited dispatch test;
- both source-receipt label tests;
- T6a;
- O1, O2, O3 and O4;
- the scope restoration test;
- the three `_without_pressure` twins;
- `operation_authored_primitive_categories_map_to_preview_mechanics`, a strip user;
- `retired_legacy_pressure_is_refused_and_pressure_free_documents_solve`;
- `f1b_w2_admission_refuses_each_reachable_family_by_name`.

## 4. Public meaning

All within the owner's decision and D-1, except as flagged:
- **Product refusal code:** the existing `PRESSURE_MODEL_REAUTHOR_REQUIRED` (D-4) for the label and every primitive. Its texts are covered in §2, and S-1 applies.
- **`PRESSURE_CONTRACT_UNSUPPORTED`'s text** no longer names the retired contract. That is the plan.
- **Panel** (`PressureAuthoringPanel.tsx:68-73`):
  - a labelled model shows "legacy_pressure_v1 (retired; solves are refused until the model is re-authored to exact_straight_pressure_v2)";
  - a model without a contract shows "none (pressure-free; legacy pressure primitives are refused)";
  - "pressure-free" is RR D-1's own term; for the wording points see N-5.
- **Load-case manager note:** "Legacy pressure primitives are retired. Author pressure as exact pressure regions in the pressure mechanics profile."
- **Applier:** a new code, `OP-PRESSURE-PRIMITIVE-RETIRED`, which goes to ROOT as N-2.
- **Scope statement:** the remaining benchmark use of the legacy membrane formula goes to ROOT as N-1.

## 5. Held items

Untouched, by `git diff --stat B..head` and by reading:
- the historical scope file `PP/src/historical_pressure_reference.rs`;
- `PP/src/preview_physics.rs` (the joint bypass);
- O1–O4, `request_with_refused_joint` and `private_historical_pressure_scope_restores_public_refusal_and_rejects_exact`: no hunk touches them;
- `historical_pressure_preview(_with_mode)`;
- `previewService.ts` and every file under `P/fixtures`, including the precision-1 pair and `invented_mechanics_result.json`;
- `P/schemas`.

The scope's pressure-bypass lines are textually unchanged (§1.1). B0, B2-C and B3-D are untouched. No `PP/src/retained_*` file or reader source (RS, PY, TS) changes; the readers gain only test cases for their existing G8 rule.

## 6. I110's records

- I110's per-test outcome lists check out against their raw logs:
  - pytest: the PASSED/SKIPPED lines are identical at B and at the head, 4426 passed and 32 skipped. The JSON's 4353/8 counts are keyed differently.
  - vitest: I diffed 4245 → 4247 myself, and the only changes are the 4 listed.
  - src-tauri: 116 → 117, +1 listed.
  - 40 manifests: 2776 → 2765, the 21 listed changes.
- All 21 manifest changes are in the plan. Two caveats:
  - the binding test's skip (§3);
  - the B-1 deletion, which the plan lists but which is not pressure-only.
- I did not rerun the full suites. My spot checks are in §3.

## 7. Host

- Every cargo command went through `WT/tools/t3_cargo.sh` (`--locked --offline`), with targets in `WT/targets/rv127-{base,cand,probe}`.
- Scratch was `S`, with `TMPDIR` set to `S/tmp`.
- No Git writes, no DEC-025 and no installs. The candidate worktree was read only.
- The archive copies and targets were deleted afterwards; the small scratch folder is kept (§8).

## 8. Cleanup

- Deleted: `WT/rv127/` (base, cand, probe) and `WT/targets/rv127-{base,cand,probe}` (about 3.8 GB).
- Kept: `S` (3 MB: the scripts, the sample inputs and the raw logs), for the repair confirmation.
- `WT/t3-pret` was never written.

## Records

- `REVIEW.md` (this file)
- `_run_records/`:
  - `scripts/` (`enumerate.py`, `select.py`, `rv127_bytes.rs`, `compare.py`, `run_bytes.sh`, `run_probe.sh`, `probe_thermal_half.rs.txt`)
  - `bytes_base.jsonl`, `bytes_cand.jsonl`, `compare.json`, `sample_labels.json`, `inputs_sha256.txt`
  - `bytes_{base,cand}.log` and `probe_{lib,int}.log` (progress and result lines)
- `SHA256SUMS`

Paths use placeholders only.
