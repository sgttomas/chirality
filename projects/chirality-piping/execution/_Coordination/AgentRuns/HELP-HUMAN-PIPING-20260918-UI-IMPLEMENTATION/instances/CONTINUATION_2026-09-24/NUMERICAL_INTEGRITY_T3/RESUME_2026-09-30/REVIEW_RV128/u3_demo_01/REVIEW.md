# RV128: independent review of U3's demo-fixture lane (G10, D-3, RV127 S-1)

**Who:** RV128, TASK (Type 2), an independent reviewer dispatched by WORKING_ITEMS for T3 (Agent 1), 2026-10-08 UTC. I wrote none of the work under review and did not delegate.
**Brief:** `R/BRIEFS/RV128_U3_DEMO.md` (sha256 `66a94a42…6803ef5`, verified), read with `R/BRIEFS/B1_COMMON.md`, NUM's `AGENTS.md` and `agents/AGENT_TASK.md`.
**Candidate:** branch `codex/piping-t3-demo-fixtures-20261008` (`WT/t3-demo`), head `180bf9b26d` = `ff9d3b7d6e` (S-1) + `180bf9b26d` (demo model, fixtures, consumers) on `4c0d5d7c00`.
**Basis:** RR "Owner decision: M07's flawed joint element, option A; U3 Stage 2 released" (item 3), RR "U3 rulings on I110's pressure inventory" (D-1, D-2 A1, D-3), RR "U3 Stage 2 rulings" (item 4), RV127 S-1 (`R/REVIEW_RV127/u3_stage1_01/REVIEW.md`), I111's G10 (`R/I111/m07_premise_01/REPORT.md`), the implementer's record `R/I114/demo_fixtures_01/RETURN.md` (sha256 `f8e76eb3…6dec92f`; its SHA256SUMS verify) and I114's brief `R/BRIEFS/U3_DEMO_FIXTURES.md` (`df23a99c…6404be9`).
**Working copies:** `git archive` of the head and of `4c0d5d7c00` into `WT/rv128/{cand,base}`; a clone `WT/rv128/regen` for regeneration; `WT/rv128/merge` for a trial merge with I110's lane. Targets `WT/targets/rv128-{demo,wasm,pybins,merge}`; scratch `WT/scratch/rv128_demo/`. Every cargo went through `WT/tools/t3_cargo.sh` with `--locked --offline` (directly, or through the PATH shim `_run_records/cargo_shim.sh.txt`); vitest and pytest went through `WT/tools/t3_slot.sh`. No Git writes, no DEC-025, no installs; `node_modules` is a copy-on-write clone from `WT/t3-pret` (same lockfile, `0dd1616e…`); the wasm engine was built from my archive.

## Verdict

**PASS with two SHOULD-FIX items. 0 BLOCKING, 2 SHOULD-FIX, 7 NOTES.** The full vitest suite passes on the head's bytes (141 files, 4247 tests).

- **Provenance holds exactly.** I regenerated every replaced or regenerated fixture with the recorded recipe and generator, and separately by a direct `cargo run` of the example. All five product outputs and the derived carrier are byte-identical to the committed bytes. The two generation records differ only in `stderr_sha256`, which hashes cargo warnings that carry the checkout's absolute path (§1).
- **The model is valid and honest.** No joint, no pressure primitive, no pressure contract or regions; it solves (`MECHANICS_SOLVED`, `checks_passed`); it equals PP's joint-free model except its identity; its outputs equal the S11-K product pins except `model_ref` (§2).
- **The consumers' new expectations come from the product's output.** The 18 changed vitest files pass (699 tests, the same count I114 recorded), the 6 changed pytest files pass (277), PP `--test pressure_runtime` 15/15, RE `--test retained_precision_carriers` 17/17. No test was deleted (counts unchanged per file; three App tests and two others renamed). No tolerance was widened. Two coverage losses have no equivalent (S-1, S-2) (§3).
- **S-1 (RV127) is done:** one text for every value, naming `2.0.0/exact_straight_pressure_v2`; the refusal pair regenerated, with only the four messages changed (§4).

## Findings

| ID | Class | Where | Evidence | Remedy |
|---|---|---|---|---|
| S-1 | SHOULD-FIX (brief item 3: no assertion removed without an equivalent) | `P/apps/desktop/src/App.test.tsx:10420-10431` (head) replacing B `:10422-10459`; the untested branch is `P/apps/desktop/src/features/results/ResultsPanel.tsx:393-401` | B selected `result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial` and asserted its recovery basis (`explicit_user_linear_combination`, `combination:combination:C-OPER-ALT`) and its source refs (`result:force:pipe-P-120:axial`, `result:loadcase:load-L-200:…:axial`). The head asserts only the combination gate notice. No vitest or e2e test on the head asserts `explicit_user_linear_combination` or a non-empty `selected-result-source-refs` (grep: B 1 file, head 0); every remaining source-refs assertion is the "not a combined result" branch (`App.test.tsx:10340`). An equivalent exists now: my probe (`_run_records/rv128_probe2.test.tsx.txt`) renders `ResultsPanel` on the actual preview-physics-1 output `P/fixtures/results/preview_physics_unicode_ids_sparse.json`, selects a combination axial-force row, and passes both assertions | Add that test (a combination row of the unicode-ids output: recovery basis and every source ref), as `rendererIntegration.test.tsx` already does for comparison dimensions with the same fixture |
| S-2 | SHOULD-FIX (brief item 3, empty states; I114 §6.4); the defect is pre-existing, not this branch's code | Empty states: `App.test.tsx:1073-1079`, `:8211`, `:10788-10789`, `:13951-13968`; `P/apps/desktop/e2e/r2-smoke.spec.ts:140`. Defect: `P/apps/desktop/src/services/previewService.ts:418-423` (hard-coded `load:L-100` / `combination:C-OPER-ALT`), `:409-414` (the throw), reached from `P/apps/desktop/src/features/workspace/resultsSessionState.ts:107-110` | B pinned real-data comparisons (261 pairs; matched units MPa, N, N*m, mm, rad; the Tier3 test converted deltas to US and back). The head pins 0 pairs and 309 reference-only rows everywhere, so `buildPreviewComparison`'s pairing, delta and unit-equality path has no real-data test left (`rendererIntegration.test.tsx` uses hand-built comparison objects). The Tier3 test's display-unit assertions (`:13964-13966`) are now vacuous: with no rows, "no converted cell" and "text unchanged" hold trivially. No current-product output can restore the coverage: my probe (`_run_records/probe1.out.json`) shows `buildPreviewComparison` on the actual unicode-ids output throws `ANALYSIS-RUN-RESULT-DIMENSION-UNDECLARED` (`support_reaction_force_magnitude_v2`) under that output's basis ids, and under the app's default ids after renaming only the ids. The magnitude row's sources are combination component rows, so the builder would also pair a combination row against a combination row of another quantity. The app calls it in a `useMemo` for any current solved result, and the tree has no error boundary, so a native solve of a linear model using the demo's ids would throw during render | For this branch: state the interim gap in the PR body. Route a repair to WORKING_ITEMS as its own item: declare or exclude the v2 kinds, pair only against left-basis sources, stop hard-coding the basis ids, and add a real-data test on the unicode-ids output (non-empty pairs, matched units, and the Tier3 display conversion) |
| N-1 | NOTE (coverage) | `P/apps/desktop/src/services/previewService.test.ts:404-439`; `P/tests/test_analysis_run_records.py:359-363`; mapping at `previewService.ts:340-352` | The source-dimension tests no longer exercise `component_user_stiffness_macro_element_review` (B asserted C-150's axial/lateral as `linear_stiffness`, angular/torsional as `rotational_stiffness`). Only the refused joint element emits that kind, so this follows M07 option A; the mapping stays in code untested | Optional: pin the mapping on a synthetic row, or delete it with the element in T4's PR |
| N-2 | NOTE (test pairing) | `P/apps/desktop/src/features/report/reportPackageRequest.test.ts:80-82`, `:119` | `legacyProvenanceSession` rebinds the carrier's `model_ref` to the session model, so a demo-model result is paired with the refused session model. Disclosed (I114 §6.6); the projection under test reads only the model's component provenance | Optional: move the component-provenance oracle to the demo model if its components carry the needed provenance |
| N-3 | NOTE (model honesty) | `P/fixtures/product_preview/invented_demo_model.json:497`, `:551` (same in `PP/tests/fixtures/preview_physics_invented_model.json`) | The two load cases are labelled "… gravity and pressure preview" but carry no pressure. Inherited, because the demo must equal PP's model except its identity; the results and the reference panel do not show the labels | Optional: relabel both fixtures in a lane allowed to touch PP's fixtures |
| N-4 | NOTE (carrier) | `P/fixtures/product_preview/invented_demo_result_legacy_0_1.json:16` | The carrier keeps `component_stress_modifier_count: 8`; its 0.1.0 row set has no row of that meaning (the 8 `component_equal_factor_intensified_bending_stress_v1` rows are removed). A count, not a reference, so the dangling-reference check does not catch it | Record it in `DEMO_FIXTURES.md`, or null the count in the derivation as for `max_open_formula_stress` |
| N-5 | NOTE, for WORKING_ITEMS and ROOT (RR Stage 2 ruling 4) | `PP/src/preview_physics.rs:75` → `formulation_basis.limitations[1]` of every preview-physics-1 output | "Nonzero pressure is refused on this route, …" keeps the "nonzero" framing that RV127 S-1 removed from the refusal: under D-2 A1 a zero primitive is refused too. It is now shown in the bundled demo. Not this lane's file. 22 committed files carry it, including the demo pair, the S11-K pins, the unicode-ids output, two retained successor fixtures and `schemas/results.v0.3.schema.yaml` | Assess under ruling 4 in I110's lane. If it changes, the retained successor pins change, so the blast radius goes to ROOT first; the demo pair is regenerated with the recipe |
| N-6 | NOTE (wording) | `P/fixtures/product_preview/DEMO_FIXTURES.md:5`; `P/core/product_preview/service.py:63-70` | "with three changes:" introduces four bullets. "for tests of readers of the legacy 0.1.0 result format" omits that the Python preview service returns the carrier as its frozen mechanics result | Say "four changes" and name the service |
| N-7 | NOTE (records) | `demo_fixture_generation.json` and `preview_physics_fixture_generation.json`, `outputs[].stderr_sha256` | stderr holds cargo warnings with the checkout's absolute path, so the hash differs in every checkout (`cc15cd55…` at I114, `6f6d37ea…` in `WT/rv128/regen`) while every output is equal. Only a hash is recorded, not the path | Compare outputs, not record bytes, when re-checking the post-merge regeneration |

## 1. Provenance (brief item 1)

**The recipe.** Both modes were run in `WT/rv128/regen` (`node tools/serialization/generate_product_preview_mechanics.mjs`, then `--preview-physics-1`), exit 0. Results are in `_run_records/regeneration.out.txt`:

| File | Committed = regenerated |
|---|---|
| `invented_demo_result_preview_physics_1_sparse.json` (`e577f491…`) | equal |
| `invented_demo_result_preview_physics_1_dense.json` (`1ca7993f…`) | equal |
| `invented_demo_result_legacy_0_1.json` (`ca3ecdb5…`) | equal |
| `invented_mechanics_result_preview_physics_1_{sparse,dense}.json` (`2cb29453…`, both) | equal |
| `demo_fixture_generation.json`, `preview_physics_fixture_generation.json` | equal except the two `stderr_sha256` lines each (N-7); the 403-entry source inventory, tools (cargo/rustc 1.97.1, node v24.18.0), dependencies and output hashes are identical |

**The direct run.** `t3_cargo.sh run --offline --locked --quiet --manifest-path PP/Cargo.toml --example preview_result -- <mode> <model>` for both modes and both models reproduces the same four sha256 values. With no argument it gives the refused sparse envelope, and an unknown or extra argument exits 2.

**The ties.**
- Each demo output equals the S11-K product pin `P/fixtures/results/preview_physics_invented_<mode>.json` byte for byte after its one `model_ref` occurrence is renamed. That pin is tested on the product in RE (`preview_physics_contract.rs`), PY and TS.
- The carrier equals my own derivation from the sparse output (`_run_records/carrier_check.py.txt`, `.out.txt`): the four members removed, schema 0.1.0, 112 rows of five kinds removed, one headline nulled, key order kept. Textually only two lines are not verbatim producer lines: the `schema_version` line and the nulled headline.
- **Generator** (`PP/examples/preview_result.rs`): both models are `include_str!`, and the no-argument default is unchanged. The precision-1 recipe mode is removed because it could no longer succeed: a fresh non-exact solve is preview-physics-1. The forbidden-destination set now covers both input models and the other mode's files.

## 2. The model (brief item 2)

`_run_records/model_check.py.txt` / `.out.txt`:
- **What it contains.** Components C-110 bend, C-120 branch, C-130 valve and C-140 terminal; no `expansion_joint`. No primitive load of category or dimension `pressure` (L-100: weight, occasional, thermal; L-200: weight, occasional). No `pressure_contract` and no `pressure_regions`.
- **What differs from `PP/tests/fixtures/preview_physics_invented_model.json`:** exactly `project.id`, `project.name`, `project.description` and `diagnostics[0].source`. Key order is equal.
- **Joint and thrust text in its outputs:** neither output mentions C-150, a joint or a thrust row. Its friction normal, 52.373281987314456 N, agrees with I111's independent joint-free 52.37 N. The friction reaction is 0.5237328200600512 N, which is 1.87·10⁻¹⁰ N above 0.01·N (the accepted same-iterate law).
- **The view is truthful.** `HistoricalRunContext.tsx:349-358` titles it "Bundled reference — not a solve for the current model" and shows "Reference model: project:invented-demo-loop-01". The provenance has `fresh_invocation_performed: false` and `current_use_eligible: false`. `loadBundledMechanicsReference` binds the results to the demo model (`previewService.ts:721-743`), and `validateBrowserMechanicsFixture` now requires preview-physics-1 and runs the preview-physics reader on solved and blocked envelopes. A browser solve of the demo model is refused as an edited model (`sourceBlockRecovery.test.ts:241-250`). The distinct id is what makes the panel's model line meaningful.

## 3. The consumers (brief item 3)

**Runs on the head's bytes.**

| Suite | Result |
|---|---|
| vitest, 18 changed files | 18 files, 699 tests passed (I114's per-file counts for the same files sum to 699) |
| vitest, full | 141 files, 4247 tests passed (equals I114's full run) |
| pytest, 6 changed files (checked-JSON, binary64 and units binaries built from my archive) | 277 passed |
| PP `--test pressure_runtime` | 15/15 |
| RE `--test retained_precision_carriers` | 17/17 |

**Where the expectations come from.**
- The new numbers in r2-smoke's source oracle, which I did not run as e2e, recompute exactly from the fixture bytes: 513, 6, 100 and 1 for the carrier; 625, 102, 102 and 2 for the reference. Both give 5 nodes, 7.635384 mm, one linked mm row, and the hanger row as the only stiffness-unit row.
- The App and panel counts are rendered from the product bytes, and the tests pass on them.

**The remaining hand-built inputs**, each disclosed or justified:
- `sourceBlockRecovery.test.ts`'s synthetic ordinary wrapper drops the five preview-only kinds and `contract_evidence`;
- `KnownSemanticNotices.test.tsx` supplies three SIF×k records, because no precision-1 fixture carries them;
- `reportPackageRequest.test.ts` rebinds `model_ref` (N-2).

**No tolerance widened.** The friction-law checks went from "the fixture's 6-digit value equals round(μN, 6)" to "round(reaction, 6) equals round(μN, 6)". The precision is the same, and the full-precision values are now pinned exactly as well (`previewService.test.ts:170-188`; `test_product_preview_service.py:203-207`).

**Changed refusal codes.**
- `previewService.test.ts`'s unit-contradiction case now expects `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`. `SOURCE_UNIT_CONTRADICTION` stays pinned in `reportPackageRequest.test.ts:333`.
- `ResultExportPanel.test.tsx` now refuses on `CURRENT_NATIVE_INVOCATION_REQUIRED`. `CURRENT_NUMERICAL_INTEGRITY_NEEDS_RECOMPUTE` stays pinned in five places.

**Empty-state and absence assertions, judged.**

| Assertion | Still meaningful? |
|---|---|
| Comparison: `App.test.tsx:1073-1079`, `:8211`, `:10788-10789`, `:13957-13961`; `r2-smoke.spec.ts:140` (0 pairs, 309 reference-only, no matched units) | **Partly.** They pin the gate notice and the true empty summary for a withheld combination. They no longer test pairing or deltas, and `:13964-13966` (display conversion) is vacuous (S-2) |
| Combination filter "0 of 625" plus the gate notice (`App.test.tsx:10427-10430`) | Yes for the gate; the combined-row detail is lost (S-1) |
| `component_stress_modifier_count` 0 and evidence `[]` (`App.test.tsx:10694-10695`) | Yes: under T0R the SIF×k evidence is historical precision-1 only, and intensified rows are reported separately (`ReportPanel.tsx:525-541`) |
| User-stiffness, thrust and joint counts 0 (`App.test.tsx:10737-10740`); no `pressure`, `C-150` or `result:combination:` ids (`test_product_preview_service.py:80`, `:89`, `:100`, `:290`; `test_results_schema.py:450-451`; `test_analysis_run_records.py:279`, `:363`; `previewService.test.ts:438`; `r2-smoke.spec.ts` "no hoop, thrust or joint-stiffness rows") | Yes: they pin that the flawed joint and the legacy pressure are gone |
| MODEL_INCOMPLETE workflow test on the actual 0-row refusal envelope (`App.test.tsx:14698-14735`) | Yes, and stronger: product bytes instead of a status-flipped reference, and it asserts the re-author text. The "blocked status with rows" overlay case stays covered at `:14673-14697` |

**No dangling consumer.** On the head, the removed files are named only in historical logs (`SMOKE.md`, `PLAN_COMPLETION_LOG.md`, evidence sweeps) and in `DEMO_FIXTURES.md`'s removal note. No test checks the generation records' source inventories.

## 4. S-1 (brief item 4)

- `PP/src/pressure_runtime.rs:216-227`: one text for any value (zero, −0.0, NaN, nonzero), naming `2.0.0/exact_straight_pressure_v2`.
- `PP/tests/pressure_runtime.rs:868-884` pins a 1.2e6 primitive with the same code, refs and message as zero, so a split arm would fail it.
- The refusal pair differs from B in exactly the four `PRESSURE_MODEL_REAUTHOR_REQUIRED` messages. It is regenerated byte-identically, and pinned by `test_generated_unchanged_demo_output_is_recorded_truthfully` (single text naming the contract) and `App.test.tsx:14729-14732`.
- The old text survives only in execution records and comments.

## 5. I114's notes for WORKING_ITEMS (§6)

1. **Stale records after the merge with I110.** Agreed, and tested.
   - **The trial merge.** I applied the candidate's diff (`--no-renames`) to an archive of I110's current local head `16ce82f573`; it applied cleanly. Then I ran both recipe modes (`_run_records/trial_merge_i110.out.txt`).
   - **The outputs:** all five product outputs and the carrier are byte-identical to the candidate's.
   - **The records:** the source inventories change in 25 entries (24 changed, `historical_pressure_reference.rs` removed), and the stderr hashes change.
   - **What follows:** re-run both modes on the actual merge commit and commit the records. A ruling-4 text change (N-5) would change the outputs as well, so the re-run comes after the final Stage 2 head.
2. **The app's default session model is still the refused demo.** A correct reading of I114's brief, but a product question.
   - Out of the box, the native app solves a model the product refuses (four re-author refusals). Meanwhile the browser shows the joint and pressure model on the canvas, next to a reference computed from a different model.
   - The reference panel is truthful about that, and the default is not a defect of this branch.
   - **My view:** load the demo model as the app's default session model in a follow-up decided by ROOT. `invented_preview_model.json` stays for PP's tests and the refusal pair. The out-of-the-box solve would then succeed and agree with the reference.
   - It touches the session-model pins in App, e2e and the R2 rehearsal, so it is its own change.
3. **The derived carrier.** Acceptable.
   - It is mechanically derived, labelled, recorded with its derivation, and checked structurally in the recipe and in PY. My independent derivation equals it.
   - Deleting the 0.1.0 reader tests instead would remove the F-5 guard, saved-run and V02 coverage for a format the readers still accept.
   - Minor: N-4 and N-6.
4. **The comparison workspace throws on preview-physics-1 combination rows.** Confirmed, and wider than a missing declaration (S-2):
   - the throw;
   - a wrong pairing behind it;
   - hard-coded basis ids;
   - render-time reachability without an error boundary.
   It is pre-existing and not caused here, but it is why the comparison coverage could not be kept. Route it.

## Not done

- I did not run e2e. I114 ran 30/30 on this Mac, and I recomputed r2-smoke's source oracles from the bytes.
- I did not rebuild src-tauri: the one edited test only swaps its fixture name.
- I did not run full pytest or full RE.
- The probes ran in my archive copy and were deleted after use; their sources are in `_run_records/`.

- **Scope is the committed head only.** At about 2026-10-08T23:00Z, `WT/t3-demo` had 21 uncommitted modified files that I did not make: my only operations there were Git reads with `GIT_OPTIONAL_LOCKS=0`. They include `invented_demo_model.json`, both generation records, `DEMO_FIXTURES.md`, `previewService.ts`, `App.test.tsx`, src-tauri `lib.rs` and the e2e specs. The newest is stamped 22:59:58Z. This review covers `180bf9b26d` through its archive, not those edits. A new head needs its own check, at least §1's regeneration and the changed tests.

## Records

- `REVIEW.md` (this file), `SHA256SUMS`
- `_run_records/`:
  - `regeneration.out.txt`, `trial_merge_i110.out.txt`;
  - `model_check.py.txt`, `model_check.out.txt`, `carrier_check.py.txt`, `carrier_check.out.txt`;
  - `rv128_probe.test.ts.txt`, `probe1.out.json`, `rv128_probe2.test.tsx.txt`;
  - `cargo_shim.sh.txt`;
  - `suites.summary.txt`, `vitest_full.summary.txt`.

Paths use placeholders only.
