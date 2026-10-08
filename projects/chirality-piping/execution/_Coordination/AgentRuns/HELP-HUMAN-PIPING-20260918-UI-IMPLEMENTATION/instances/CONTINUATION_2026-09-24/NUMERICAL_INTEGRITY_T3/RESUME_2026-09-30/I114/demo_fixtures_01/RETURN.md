# I114: the app's demo results replaced with results from a valid demo model (G10, D-3, RV127 S-1)

**Who:** I114, TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), 2026-10-08 UTC. I did not delegate.
**Brief:** `R/BRIEFS/U3_DEMO_FIXTURES.md` (sha256 `df23a99c…6404be9`, verified), read with `R/BRIEFS/B1_COMMON.md`, NUM's `AGENTS.md` and `agents/AGENT_TASK.md`.
**Basis:** RR "Owner decisions: the legacy pressure contract is retired product-wide; …", RR "U3 rulings on I110's pressure inventory: …" (D-3), RR "Owner decision: M07's flawed joint element, option A; …" (item 3), RV127 S-1 (`R/REVIEW_RV127/u3_stage1_01/REVIEW.md`), I110's inventory (D-3 rows) and I111's G10.
**Placeholders:** `WT`, `NUM`, `P`, `PP`, `RE`, `R`, `RR` as in the brief.

**Outcome: replaced, not removed. No stop.**

## Head and commits

Branch `codex/piping-t3-demo-fixtures-20261008` in `WT/t3-demo`, from `4c0d5d7c00`. Not pushed (WORKING_ITEMS pushes).

| Commit | What |
|---|---|
| `ff9d3b7d6e` | RV127 S-1: one re-author text for every legacy primitive (`PP/src/pressure_runtime.rs`, the nonzero arm only; 5 lines become 1). `PP/tests/pressure_runtime.rs` pins a nonzero primitive with the same code, refs and text as zero. |
| `180bf9b26d` (head) | The demo model, the generator and recipe, the regenerated fixtures and records, and every consumer. 45 files. |

## 1. The model chosen

`P/fixtures/product_preview/invented_demo_model.json`, `project:invented-demo-loop-01`, "Invented Utility Loop Demo" (sha256 `797a4012…4875c111`).
- **What it is:** PP's joint-free test model (`PP/tests/fixtures/preview_physics_invented_model.json`): the invented loop without its four legacy pressure primitives and without joint C-150.
- **What differs from PP's model:** only the project id, name and description, and the model diagnostic's source path (`_run_records/crosscheck.out.json`: `demo_model_equals_pp_model_except_identity: true`).
- **Why its own id:** the session's default model (`invented_preview_model.json`, unchanged as the brief requires) keeps `project:invented-loop-01`. The reference view says "not a solve for the current model". A distinct id keeps the two from being conflated, and a mispairing is refused (`BROWSER_FIXTURE_MODEL_BINDING_MISMATCH`, `ANALYSIS-RUN-INPUT-MANIFEST-MODEL-MISMATCH`).
- **Why no exact pressure:** the view renders whatever rows it is given and does not need pressure. The exact contract would also refuse the demo's components, its nonlinear and constant-effort supports and its combination.
- **What it keeps of the old demo:** bend, branch, valve and terminal components, one-way and friction nonlinear supports, the spring hanger, constant effort, thermal and the user combination. The combination is withheld by the product (`NONLINEAR_COMBINATION_REQUIRES_SOLVE`), as for any model with nonlinear supports.
- **One independent tie:** the friction normal is 52.373281987314456 N. I111 (O6) cites 52.37 N for the joint-free model in the independent record (C-150 moved it to 40.91 N).

## 2. The generation

**The generator:** `PP/examples/preview_result.rs` now takes an optional model argument:
- `invented_preview_model`, the default, unchanged with no argument;
- `invented_demo_model`.

An unknown or extra argument still exits 2.

**The recipe** (`P/tools/serialization/generate_product_preview_mechanics.mjs`):
- Its default mode (`npm run generate:product-preview-mechanics`) now generates the demo set, and refuses to install anything but a solved result.
- `--preview-physics-1` generates the refused demo's envelopes.
- The precision-1 mode is gone. It could no longer succeed: the product emits preview-physics-1 for a fresh non-exact solve.
- Neither mode writes the other's files or either input model.
- The source inventory now lists both models and `fixtures/results/semantic_contract_v0_2.json`.

Every cargo call went through `WT/tools/t3_cargo.sh` with `--locked --offline`, via a PATH shim (`_run_records/cargo_shim.sh.txt`), with `CARGO_TARGET_DIR=WT/targets/i114-demo`.

**The outputs** (final run after every source edit; the bytes are identical to those the suites ran on):

| File | sha256 | What |
|---|---|---|
| `invented_demo_result_preview_physics_1_sparse.json` | `e577f491…5353d640` | product stdout; MECHANICS_SOLVED, checks_passed, 625 rows |
| `invented_demo_result_preview_physics_1_dense.json` | `1ca7993f…04c5cf34` | product stdout; MECHANICS_SOLVED, checks_passed, 627 rows |
| `invented_demo_result_legacy_0_1.json` | `ca3ecdb5…9c0a97ae` | historical-format carrier, derived (below); 513 rows |
| `demo_fixture_generation.json` | `c1362d67…a1204c` | the record |
| `invented_mechanics_result_preview_physics_1_{sparse,dense}.json` | `2cb29453…34837b12` (both) | the refused demo's envelopes; MODEL_INCOMPLETE, 0 rows |
| `preview_physics_fixture_generation.json` | `0557742a…7911bdf` | their record |

**Cross-checks** (`_run_records/crosscheck.py.txt`, output `crosscheck.out.json`):
- **Each demo output** equals the S11-K product-pinned `P/fixtures/results/preview_physics_invented_<mode>.json` byte for byte, except its one `model_ref` occurrence. The current product therefore reproduces the pinned joint-free output.
- **The carrier** equals its derivation exactly.
- **Both refusal envelopes** carry one re-author text, naming `2.0.0/exact_straight_pressure_v2`.

**The historical-format carrier.** The legacy 0.1.0 readers (the V02 analysis-run builder, saved-run history, the three languages' F-5 guard cases, the Python preview service) need a 0.1.0 document. The product cannot emit one. The recipe derives it from the sparse output:
- it removes the four 0.2.0 members (`producer`, `numerical_quality`, `formulation_basis`, `contract_evidence`);
- it sets `schema_version` to 0.1.0;
- it removes the rows whose kinds the 0.1.0 semantics (`semantic_contract_v0_2.json`) do not define. These are five preview-physics-1 kinds, 112 rows; the legacy reader refuses them (`ANALYSIS-RUN-RESULT-DIMENSION-UNDECLARED`);
- it sets the one headline whose row was removed (`max_open_formula_stress`) to null, so that no reference dangles.

No kept row, value or diagnostic changes. The edit is textual: every kept byte is the producer's. It is checked structurally before staging. The record and `DEMO_FIXTURES.md` label it as derived, not producer output.

## 3. The fixtures replaced or removed

- **Removed:**
  - `invented_mechanics_result.json` (D-3);
  - `invented_mechanics_result_precision_1_{sparse,dense}.json` (G10);
  - `precision_fixture_generation.json`.
- **Replaced** by the demo set above. The precision-1 pair's role (the browser's bundled reference) passes to the demo's preview-physics-1 pair. The legacy file's role (legacy-format reader input) passes to the carrier.
- **Regenerated:** the refused demo's envelopes, with S-1's text (only the four messages change), and their record.
- **Renamed:** `PRECISION_FIXTURES.md` becomes `DEMO_FIXTURES.md`, rewritten.
- **Unchanged:** `invented_preview_model.json` and every PP test fixture.

## 4. The consumers changed

- **The view** (`apps/desktop/src/services/previewService.ts`):
  - the reference inspection loads the demo model as its own model;
  - its results are the demo pair;
  - `validateBrowserMechanicsFixture` requires the preview-physics-1 contract and runs `validatePreviewPhysicsEvidence` (after the mode-binding check, and for a blocked envelope too);
  - `fixture_ref` names the new files.

  The session model, `loadPreviewModel` and the browser-solve refusal are unchanged. This is no design change: the reference context already carried its own model.
- **Python service** (`P/core/product_preview/service.py`):
  - its default model is the demo model and its frozen result is the carrier;
  - `_selected_result_refs` now tolerates a null headline (it raised on one).
- **App unit tests (18 files):**
  - `App.test.tsx`;
  - `previewService.test.ts`;
  - `HistoricalRunContext.test.tsx`, `retainedPrecisionIntegration.test.tsx`, `KnownSemanticNotices.test.tsx`, `sourceBlockRecovery.test.ts`;
  - `HandoffPanel.test.tsx`, `HeadlessRunnerPanel.test.tsx`;
  - `reportPackageRequest.test.ts`, `renderedReport.test.tsx`;
  - `resultExportAdapter.test.ts`, `physicsResultExport.test.ts`, `ResultExportPanel.test.tsx`;
  - `StressNeutralExportPanel.test.tsx`, `rendererIntegration.test.tsx`;
  - `NativePackagePanel.test.ts`, `LocalFeaHandoffPanel.test.tsx`, `retainedPrecisionAnalysisRun.test.ts`.

  (`NativePackagePanel`, `LocalFeaHandoffPanel`, `renderedReport` and `ResultExportPanel` were not in I110's list: they paired the bundled reference with the session model, or pinned its precision-1 standing.)
- **e2e:** `e2e/r2-smoke.spec.ts` and `e2e/gui-workflow-validation.spec.ts`.
- **Python tests (6 files):** `test_product_preview_service.py`, `test_analysis_run_records.py`, `test_results_schema.py`, `test_retained_precision_carriers.py`, `test_analysis_run_compatibility.py`, `test_preview_physics_consumer_contract.py`. The last gains a record-truth test for the demo set and pins the single re-author text.
- **RE:** `RE/tests/retained_precision_carriers.rs` (the legacy include and the path map), and `P/fixtures/results/retained_precision_carrier_cases.json`:
  - the `legacy_preview_0_1` path and sha change;
  - `token_last_row_only` targets row 512 instead of 829;
  - the format stays v4.
- **src-tauri:** one test reads the carrier (`src-tauri/src/lib.rs:5072`).
- **Docs:** `docs/validation_manual/index.md`. The historical logs (`SMOKE.md`, `PLAN_COMPLETION_LOG.md`, evidence and witness records) are left as history.

**How the expectations were updated:** every changed expectation was read from the product's output. Sources:
- the fixtures (the Python computations in `crosscheck`);
- two temporary vitest probes that rendered the product's panels on the new pair (`_run_records/i114_probe*.test.tsx.txt`, outputs `probe.json` and `probe2.json`; deleted before commit);
- the failure readouts.

**Where a test's subject was the flawed data:**
- `App.test` "retains historical component, pressure-thrust, hanger and review-package numeric oracles" became the demo's oracles: no SIF×k rows, no joint and no thrust; hanger evidence and package counts kept.
- `test_product_preview_service.py`'s pressure-hoop, C-150 thrust and combination-row assertions became absence assertions. Its stale nonlinear basis strings became the product's current text.

**Where a precision-1 document is the subject** (precision-1 is still read as historical): the tests use `P/fixtures/results/precision_connected_ui_mechanics_{sparse,dense}.json`, actual precision-1 output with no joint and no pressure. This applies to `physicsResultExport`, `KnownSemanticNotices`, `test_analysis_run_compatibility.py` and `test_preview_physics_consumer_contract.py`.
- KnownSemanticNotices's SIF×k label test now supplies its records directly, since no precision-1 fixture carries SIF×k rows.
- `rendererIntegration`'s comparison-dimension test uses the actual unicode-id preview-physics-1 output, which has combination rows.

## 5. The suites (all on the head's bytes)

| Suite | Result |
|---|---|
| vitest, full (`WT/tools/t3_slot.sh`) | **4247/4247**, 141 files (`vitest_full_per_file.tsv`). The count equals I110's candidate. |
| e2e `r2-smoke` + `gui-workflow-validation`, on this Mac (Chrome, `CI=1`, one worker, port 5174 checked free) | **30/30**, both projects (`e2e_r2_smoke_gui_workflow.log`). The host can run them. |
| pytest `P/tests`, full (`-n 6`, under the slot, with the checked-JSON and units binaries set) | **4428 passed, 32 skipped** (I110's 4426 + this branch's two new parametrized cases). Run before one docstring-only edit to `service.py`. |
| RE, full (`cargo test`) | **199 passed**, 0 failed, 13 targets (`re_full.log`) |
| PP touched by S-1 | `--test pressure_runtime` 15/15, `--test preview_physics_runtime` 26/26, `--lib` filtered (`retired_legacy_pressure`, `endpoint_section_cut_mixed_hydrotest`, `pressure_runtime::`) 16/16 (`pp_s1_tests.log`) |
| src-tauri, the one edited test | 1/1 (`src_tauri_one_test.log`) |

The wasm engine for vitest was built from this tree with `scripts/build-wasm-engine.mjs` through the shim (`WT/targets/i114-wasm`). `node_modules` is a copy-on-write clone from `WT/t3-pret` (same lockfile).

## 6. Stops, and what WORKING_ITEMS should carry

**No stop.** The view works with the valid model.

1. **The merge with I110 stales both generation records.** Each record hashes the whole PP dependency closure, including PP's tests and RE. After merging I110's branch, re-run both recipe modes (`npm run generate:product-preview-mechanics`, then `--preview-physics-1`) and commit the records.
   - The outputs should come back byte-identical unless the product's output changes.
   - My change to `PP/src/pressure_runtime.rs` touches only the nonzero arm. I110 deletes the `#[cfg(test)]` scope lines just above, and one unchanged line separates the two hunks.
2. **The session's default model** (browser fallback and native `load_preview_model`) is still `invented_preview_model.json`, as the brief requires. A native solve of the app's out-of-the-box model is therefore refused (legacy pressure and joint). Switching the default to the demo model would be a separate decision.
3. **The carrier is a derived document.** If ROOT prefers no derived historical-format fixture, the alternative is to delete the legacy-format reader tests.
4. **Comparison workspace:**
   - The bundled reference's comparison is now empty: the demo's combination is withheld, giving 0 pairs and 309 reference-only rows. The App tests assert the empty state.
   - Comparison delta display stays covered in `rendererIntegration.test.tsx`.
   - **Found in passing:** `buildPreviewComparison` on preview-physics-1 combination rows (the unicode-id output) throws `ANALYSIS-RUN-RESULT-DIMENSION-UNDECLARED` (`support_reaction_force_magnitude_v2`). The comparison workspace does not yet handle preview-physics-1 combination rows. Not changed here.
5. **`App.test`'s MODEL_INCOMPLETE workflow test** now uses the product's actual refusal envelope for the session model (0 rows) instead of a status-flipped reference. The preview-physics-1 reader rightly refuses a blocked status that still carries rows.
6. **`reportPackageRequest`'s cross-layer component-provenance oracle** (shared with RE's report-package wire) stays on the session model. Its legacy record is the carrier bound to that model's id; only the session name in that fixture depends on the model.

## Records

- `RETURN.md` (this file)
- `_run_records/`:
  - `crosscheck.py.txt`, `crosscheck.out.json`;
  - `i114_probe.test.tsx.txt`, `i114_probe2.test.tsx.txt`, `probe.json`, `probe2.json`;
  - `cargo_shim.sh.txt`;
  - `generation_final_genF.stdout`, `generation_final_genF--preview-physics-1.stdout`, `generation_final_stderr.sha256`;
  - `vitest_full_per_file.tsv`, `e2e_r2_smoke_gui_workflow.log`, `pytest_full.log`, `re_full.log`, `pp_s1_tests.log`, `src_tauri_one_test.log`.
- `SHA256SUMS`

Scratch is `WT/scratch/i114_demo/`. Targets are `WT/targets/i114-{demo,wasm,tauri}`. Paths use placeholders only.
