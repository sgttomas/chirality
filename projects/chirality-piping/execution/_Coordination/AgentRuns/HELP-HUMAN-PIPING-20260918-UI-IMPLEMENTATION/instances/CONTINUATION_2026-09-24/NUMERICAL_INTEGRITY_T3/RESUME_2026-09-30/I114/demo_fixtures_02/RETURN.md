# I114 round 2: the app's default session model is the valid demo, which solves (ROOT item 1; RV128 S-1, S-2, N-3, N-4, N-6, N-7)

**Who:** I114, TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), 2026-10-08 UTC. I did not delegate.
**Brief:** WORKING_ITEMS' round-2 message (ROOT's ruling in RR, "U3, I114's demo lane and WORKING_ITEMS' three items", items 1 to 3), then its additions from RV128's review (`R/REVIEW_RV128/u3_demo_01/REVIEW.md`, PASS 0/2/7). Round 1 is `R/I114/demo_fixtures_01/RETURN.md`.
**Placeholders:** `WT`, `NUM`, `P`, `PP`, `RE`, `R`, `RR` as in round 1's brief.

**Outcome: done. No stop.** One finding for WORKING_ITEMS: 8 e2e wheel-scroll tests in `b4-table-editing.spec.ts` fail on this host, and they fail the same way on the base `180bf9b26d` (§5).

## Head

Branch `codex/piping-t3-demo-fixtures-20261008` in `WT/t3-demo`. Not pushed (WORKING_ITEMS pushes).

| Commit | What |
|---|---|
| `9744ed7e69` (head) | Round 2, on top of `180bf9b26d`. 30 product files, no records. |

`WT/tools/t3_host_screen.py` on `180bf9b26d..9744ed7e69`: 30 files, 0 hits.

## 1. The default-model change (ROOT item 1)

**The switch.**
- **Browser fallback:** `P/apps/desktop/src/services/previewService.ts` now has one fixture loader, `invented_demo_model.json`. It serves both the session model (`loadPreviewModel`'s fallback) and the bundled reference's model.
- **Native:** in `P/apps/desktop/src-tauri/src/lib.rs`, `load_preview_model` and `resolve_solve_model_payload(None)` read `invented_demo_model.json`. The agent-proposal fallback `model_ref` is `project:invented-demo-loop-01`.
- **Other references:** `ReviewGeometryPanel.tsx`'s source-basis ref and the two e2e benchmark route matchers (`benchmark-harness.ts`, `load-availability-diagnostic.mjs`, and the README line) name the demo model.
- **PP is untouched:** `invented_preview_model.json` stays as PP's refusal fixture. PP's tests are unchanged.

**The solve check:** the new native test `default_session_model_solves_in_both_modes` (src-tauri). It checks:
- the default model's id is `project:invented-demo-loop-01`;
- `resolve_solve_model_payload(None)` returns that model;
- in both `SparseInteractive` and `DenseScrutiny`, the solve gives `MECHANICS_SOLVED`, `numerical_quality.status == checks_passed`, no blocking diagnostic, non-empty result rows, and the preview-physics-1 semantic contract;
- the default solve command `run_preview_mechanics(None)` gives the same.

The job and run tests that used to assert the refused default now assert the same solved shape (`assert_bundled_demo_solved`), and the model-operation tests edit the demo. src-tauri: 118/118 on the final bytes.

**The browser.**
- The browser has no solver. Its solve of the default model is now refused as `BROWSER_SOLVE_BACKEND_REQUIRED_REFERENCE_ONLY`, because the session model equals the reference's model. An edited model is still refused as `…_FOR_EDITED_MODEL`.
- `sourceBlockRecovery.test.ts` pins both codes.

**The demo's load-case labels (RV128 N-3).**
- They no longer name the removed pressure. L-100 is "Invented operating gravity, occasional and thermal preview"; L-200 is "Invented alternate gravity and occasional preview".
- Only `invented_demo_model.json` changed; PP's model is untouched. Its description and `DEMO_FIXTURES.md` say that the labels differ from PP's model.
- Both recipe modes were regenerated afterwards (§3).

## 2. Tests whose expectations follow from the default model

Every changed value is the product's rendered output on the demo.
- **How each value was read:** most come from the failure's received value. Where vitest truncated it, I read it in one of two ways:
  - a one-off probe that wrote the rendered unit-policy text to a scratch file, then was reverted;
  - one run of the long render test with its `expect` calls turned into `expect.soft`, then reverted (`_run_records/vitest_render_test_soft_probe.log`).
- **Identity:** the project id is `project:invented-demo-loop-01`, also in tree-row ids, `project_ref`, input-manifest refs and "Reference model:". The titlebar reads "Invented Utility Loop Demo". The L-100 label is new (App, r2-smoke).
- **Counts:**

  | Count | Was | Now |
  |---|---|---|
  | Entities | 27 | 26 |
  | `stable_ids` | 26 | 25 |
  | Viewport buttons | 21 | 20 |
  | Primitive loads | 9 / 10 / 8 | 5 / 6 / 4 |
  | L-100 `primitives=` | 5 / 6 / 4 | 3 / 4 / 2 |
  | Unit witnesses | 75 | 72 |
  | Unit-bearing records | 44 / 45 | 34 / 41 |
  | Editors | 7 | 6 |
  | Ready editors | 6 | 5 |

  The editor contract lists one editor per component, and C-150 is gone. The L-100 category list is `weight, occasional, thermal`.
- **The bundled reference in e2e:** 625 sparse and 627 dense rows; 10 displacement rows on the same 5 nodes. This covers `ui-foundation.spec.ts`, `ui-foundation-dist.spec.ts`, `result-compatibility.spec.ts` and `result-compatibility-dist.spec.ts`. These pins had been stale since round 1, which changed the reference.
- **Retargeted to a demo primitive:** the magnitude test and its two siblings (`App.deadControls`, `App.shell`) used `load:L-100-P`, which no longer exists. They now use `load:L-100-T`, the thermal primitive at the same index 2: `current=12.5 degC` becomes `{"value":20,"unit":"degC"}`, rendered as `thermal; 20 degC`.
- **C-150's viewport step:** it now asserts that the demo has no `viewport-select-component:C-150`.
- **Kept on the refused model, deliberately:**
  - **The MODEL_INCOMPLETE workflow test** opens `invented_preview_model.json` as its session model through the native `load_preview_model` mock. Its real refusal envelope therefore stays paired with its own model. It still asserts the re-author text.
  - **The component-provenance cross-layer oracle** (`reportPackageRequest.test.ts`) imports the invented preview model, the model it was made for. The oracle file is unchanged.
  - **`previewService.test.ts`'s model-binding mismatch** now uses the invented preview model as the other model. The session and the reference are now the same model.
- **e2e session pins:** `gui-workflow-validation.spec.ts` reads the demo as its model fixture and reopens `project-index-open-project:invented-demo-loop-01`. `docs/validation_manual/index.md` names the demo for that workflow.

No test was deleted. No tolerance changed.

## 3. RV128's additions

| Item | What I did |
|---|---|
| **S-1** | **Added.** `P/apps/desktop/src/features/results/ResultsPanel.test.tsx`: "details a preview-physics-1 combination row with its recovery basis and every source result". It renders `ResultsPanel` on `P/fixtures/results/preview_physics_unicode_ids_sparse.json` and selects `result:combination:combination-Σ:force:pipe-α-β:axial`. It asserts the recovery basis `explicit_user_linear_combination; combination:combination:Σ` and each of its two source refs (`result:force:pipe-α-β:axial`, `result:loadcase:load-𝔫:force:pipe-α-β:axial`), checks that the "not a combined result" text is absent, and checks that the source is not mutated. |
| **S-2** | **Marked as a known gap; no real input exists.** In the Tier3 display test (`App.test.tsx`, "Tier3 display in the actual application"), the vacuous display-unit assertions are removed. The test keeps the empty-state summary, the combination-gate notice and the immutability check, and is renamed to say so. An explicit `it.todo` names the gap: "converts real comparison deltas through display-unit changes (known gap: T6, results and comparison)". Its comment cites RR's ruling item 2. See the note below this table for why no real input exists. |
| **N-3** | **Done** (§1); both modes regenerated. |
| **N-4** | **Made consistent.** The recipe declares `component_stress_modifier_count` as the count of `component_equal_factor_intensified_bending_stress_v1` rows, which is the producer's own definition (`PP/src/preview_physics.rs`, `component_stress_modifier_count = intensified.len()`). A nonzero count of a removed kind is now withheld (null) and listed in `nulled_summary_members`, like the `max_open_formula_stress` headline. The carrier differs from round 1 in that one line (`8` becomes `null`). The shared case file's pin follows it (`P/fixtures/results/retained_precision_carrier_cases.json`, `legacy_preview_0_1.sha256` = `4d3bc14f…5804e051`). `test_generated_bundled_demo_output_is_recorded_truthfully` now asserts both nulled members. |
| **N-6** | **Done.** `DEMO_FIXTURES.md` says "four changes". The fourth bullet names both withheld members, and the bullet says that the Python preview service returns the carrier as its frozen mechanics result. `service.py`'s `run_preview_mechanics` docstring describes the derived carrier and says that it is not a solve of the given model. |
| **N-7** | **Dropped.** The records no longer carry `stderr_sha256`. The recipe passes cargo's stderr through and says why it records no hash of it, and `DEMO_FIXTURES.md` says the same. The record test asserts that no output has a stderr hash. |

**Why S-2 has no real input:**
- The demo's combination is withheld, so it has 0 pairs.
- On the unicode-ids output's published combination, `buildPreviewComparison` throws `ANALYSIS-RUN-RESULT-DIMENSION-UNDECLARED` under that output's ids, and finds 0 pairs under the default ids. These are RV128's probe results; I did not rerun them.
- A kind-filtered subset would not be the product's output. It would also pin the first-source pairing that T6 is to repair.

## 4. Regeneration and checks

Both recipe modes were run after the last edit to anything in their inventory. Every cargo went through `WT/tools/t3_cargo.sh --locked --offline` via the shim (`_run_records/cargo_shim.sh.txt`), with `CARGO_TARGET_DIR=WT/targets/i114-demo`.

| File | sha256 | Change from `180bf9b26d` |
|---|---|---|
| `invented_demo_model.json` | `3a600a8b…1b51cd14` | two labels and the description |
| `invented_demo_result_preview_physics_1_sparse.json` | `e577f491…5353d640` | none (byte-identical) |
| `invented_demo_result_preview_physics_1_dense.json` | `1ca7993f…04c5cf34` | none |
| `invented_demo_result_legacy_0_1.json` | `4d3bc14f…5804e051` | `component_stress_modifier_count` becomes null (N-4) |
| `invented_mechanics_result_preview_physics_1_{sparse,dense}.json` | `2cb29453…34837b12` | none |
| `demo_fixture_generation.json` | `3e0736b1…05fc3338` | input sha, recipe sha, nulled members, no stderr hash |
| `preview_physics_fixture_generation.json` | `52ef0d93…015f4e99` | recipe sha, inventory entry, no stderr hash |
| `retained_precision_carrier_cases.json` | `b8e380c6…38adb943` | the carrier's pin only |

**Current-bytes check:** every one of the 403 inventory entries, every output and the recipe hash match the committed bytes in both records.

**Cross-check** (`_run_records/crosscheck.py.txt`, output `crosscheck.out.json`), every check true:
- each demo output equals the S11-K pin except its `model_ref`;
- the carrier equals its derivation;
- the demo model equals PP's model except its identity fields and labels;
- each refusal envelope carries one re-author text;
- the nulled count equals the removed intensified rows (8);
- no record hashes stderr.

## 5. Suites (on the final bytes; the head's bytes for everything after the commit)

| Suite | Result |
|---|---|
| src-tauri, full (`t3_cargo.sh test`) | 118 passed, including `default_session_model_solves_in_both_modes` |
| vitest, full (141 files) | 4249 tests: 4248 passed, 0 failed, 1 todo (the S-2 known gap); per file in `_run_records/vitest_full_per_file.tsv` |
| `tsc --noEmit -p tsconfig.json` and `tsc -b --noEmit` (src, tests included) | clean |
| pytest, full (`-n 6`) | 4428 passed, 32 skipped |
| RE `--test retained_precision_carriers` | 17/17 |
| e2e, dev lane, full (501 tests, 2 workers, before the last fixes) | 471 passed, 20 skipped, 10 failed: 2 stale reference counts in `result-compatibility.spec.ts` (then fixed) and the 8 B4 wheel tests below |
| e2e, `b4-table-editing` + `result-compatibility`, rerun | 44 passed; the same 8 B4 tests fail |
| e2e, the same B4 spec on the base `180bf9b26d` (an archive with cloned `node_modules`) | **the same 8 fail, at the same two assertions**; 42 passed |
| e2e, r2-smoke + gui-workflow + result-compatibility + ui-foundation, both projects, final bytes | 118/118 passed. The 2-worker run ended with 4 Playwright worker-teardown errors outside any test (the config documents this load behaviour); the 1-worker rerun on the head `9744ed7e69`: 118/118, exit 0 |
| e2e, production dist lane (`playwright.dist.config.ts`, fresh `vite build`) | 53/53 |

**The 8 B4 failures are not this lane's.**
- The tests are "B4 compact drawer {model,both} {comfortable,compact} 180" and "B4 classic scrollbar compact {comfortable,compact} {5,160}".
- Each fails where a mouse wheel over the table body should scroll it: `scrollTop > 0` never holds (lines 704 and 843).
- The classic-scrollbar tests load their own model, not the default.
- All 8 fail identically on `180bf9b26d`.
- This looks like a host or browser behaviour. It should be routed separately.

## 6. Notes for WORKING_ITEMS

1. **The merge with I110** still requires re-running both recipe modes on the merge commit and committing the records. If RV128's N-5 text changes, the outputs change too, and with them the carrier. If the carrier changes, update `legacy_preview_0_1.sha256` in `retained_precision_carrier_cases.json`. The records no longer carry the stderr hash, so they compare across checkouts.
2. **Comparison coverage:** apart from the Tier3 test, the other empty-state comparison assertions RV128 judged "partly meaningful" are unchanged. They pin the true empty summary and the gate. The real-data pairing, delta and conversion coverage is T6's, per the `it.todo`.
3. **One generic product text is unchanged:** `HandoffPanel.tsx`'s `id_basis`, "model entity IDs and computed result IDs from the invented preview model". It describes any session model's ids and names no fixture, so I left it.
4. **Scratch:** `WT/scratch/i114_demo/` holds the base archive `base180/` and the Playwright outputs; targets are `WT/targets/i114-{demo,tauri,wasm}`. Nothing outside these was written, apart from `WT/t3-demo` and these records.

## Records

- `RETURN.md` (this file), `SHA256SUMS`
- `_run_records/`:
  - `crosscheck.py.txt`, `crosscheck.out.json`, `cargo_shim.sh.txt`;
  - `generation_demo.stdout`, `generation_refused.stdout`;
  - `vitest_full_per_file.tsv`, `vitest_render_test_soft_probe.log`;
  - `pytest_full.log`, `pytest_changed_files.log`, `src_tauri_full.log`, `re_retained_precision_carriers.log`;
  - `e2e_dev_full_501.log`, `e2e_dev_b4_result_compat_rerun.log`, `e2e_base_180bf9b26d_b4.log`, `e2e_dev_final_4specs_w2.log`, `e2e_dev_final_4specs_w1.log`, `e2e_dist_53.log`.

Logs are copied with placeholder paths (`P`, `WT`) and without ANSI codes. Paths use placeholders only.
