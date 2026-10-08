# I110: retiring the legacy pressure contract product-wide — inventory and removal plan

I110 is a TASK (Type 2) for WORKING_ITEMS (T3, Agent 1). The brief is `R/BRIEFS/U3_PRESSURE_RETIRE_01.md` (sha256 `29baf0185b6ba3ee5a8182fd3bf611355c83487334939f8895c42f82d813bcfb`, verified). It is read with `R/BRIEFS/B1_COMMON.md` and RR "Owner decisions: the legacy pressure contract is retired product-wide; T3 gains a WORKING_ITEMS manager". This round only read and probed; nothing was committed.

**Basis.** The basis is the product code of NUM `9cd61ba201`. It equals PR-B1's head `f4a0430412` (there is no product diff between them). WORKING_ITEMS reports that #1154 merged as main `7eae707bb7`; NUM `ccc087edb4` has no product diff from the basis.

B3a's sites are listed for completeness only. They were read on `b2` `72b3e5d9ea` and on `b2-p` `6d3d4cdca6`, `b2-r` `c845e899da` and `b2-t` `77aaaa61d1`.

The probes ran in a detached worktree `WT/t3-pret` at `9cd61ba201`. The worktree was restored afterwards, and `git diff` there is empty.

**Course corrections from WORKING_ITEMS during the task:**
1. Q5 (M07) moved to I111. This record does not analyse M07. It lists only the sites the two premises share.
2. M07 is with the owner. The following are held pending that ruling:
   - the historical scope file;
   - the joint bypass at `PP/src/preview_physics.rs:111-115`;
   - the four C-150 tests that run inside the scope:
     - O1 `current_composite_derived_normal_friction_and_reversal`;
     - O2 `valid_invented_model_exposes_nonlinear_support_loop_evidence_historical_pressure_premise`;
     - O3 `expansion_joint_user_stiffness_emits_macro_element_review_rows`;
     - O4 `expansion_joint_pressure_thrust_uses_user_effective_area_as_load_side_evidence_historical_pressure_premise`;
   - the browser's bundled precision-1 demo results (`previewService.ts:639-646`).

   Everything else is planned below.

## 1. Stop status

**On the recommended reading (D-1 A) there is no stop. If ROOT rules D-1 B, that is a stop.**

On the recommended reading, the `1.0.0/legacy_pressure_v1` label and the legacy pressure semantics retire, and model 0.1.0/0.2.0 stays as a pressure-free namespace:
- every accepted model class keeps a route;
- no disposition changes B0, B2-C or B3-D;
- no disposition weakens a check or changes a published contract.

If ROOT also retires 0.1.0/0.2.0 (D-1 B), Q2 finds accepted classes with no route and B0's D1.3 must change. That is a **stop**.

One degenerate class also loses its route as-is under D-2 A1: a component model whose only loads are zero-valued pressure primitives. Its result is identically zero, and it has a route once a real load is added. It is listed under D-2 for ROOT's view.

The M07 hold has a consequence for the plan. O2 and O4 run the legacy nonzero-pressure computation inside the scope, so that computation and the scope's pressure bypass can go only after the owner's ruling. The plan is therefore in two stages (§5). Stage 1 already stops every product path from reaching the legacy computation.

## 2. Decisions for ROOT

**D-1 (Q1). Do model 0.1.0/0.2.0 retire with the label?**
- Options:
  - **A**: keep 0.1.0/0.2.0 as the pressure-free namespace, with their pressure semantics removed (see D-2).
  - **B**: retire 0.1.0/0.2.0 too.
- Recommendation: **A**. Option B is a stop. It strands 107 committed documents (102 of them with zero pressure) and B1's whole retained domain (B0 D1.3).

**D-2. What happens to a zero-valued pressure primitive in a 0.1.0/0.2.0 document once the legacy path goes?**
- Options:
  - **A1**: refuse a pressure primitive of any value with the re-author code, as the exact profile already does for zero.
  - **A2**: ignore it silently.
  - **A3**: keep the legacy path for zero values.
- Recommendation: **A1**. No committed document has a zero-valued pressure primitive. The tests that zero the demo's pressures in memory would strip them instead. P3 shows those tests pass unchanged, with no re-pin. A load-free component model loses its as-is route (§1).

**D-3. What happens to `invented_mechanics_result.json`?** This is the demo's frozen result, computed with legacy nonzero pressure and joint C-150. It feeds 14 app unit-test files, 2 e2e specs, 6 Python tests, 2 RE sites and `core/product_preview/service.py`. Its precision-1 pair is held.
- Options:
  - **a**: keep it as historical data. The readers stay unchanged, and the oracle that regenerates it is deleted.
  - **b**: regenerate it from a pressure-free demo.
  - **c**: remove the technical-preview service that serves it.
- Recommendation: **a** in this PR. Settle it with the held precision-1 pair after the M07 ruling.

**D-4. Which refusal code?**
- Options: reuse `PRESSURE_MODEL_REAUTHOR_REQUIRED`, or add a new `PRESSURE_CONTRACT_RETIRED`.
- Recommendation: reuse it. It is an existing public code that already means "re-author to exact". The text is in Q4.

## 3. Inventory (`inventory.json`, 219 sites; path:line, kind, premise, disposition, class, stage)

Premise counts:

| Premise | Sites | Meaning |
|---|---|---|
| implicit | 84 | 0.1.0/0.2.0 pressure primitives |
| pressure | 74 | legacy computation or the scope's pressure part |
| label | 41 | 34 of these are B3a sites on b2 |
| shared | 15 | used by both scope premises |
| exact | 4 | listed for contrast |
| M07 | 1 | |

Stage counts:

| Stage | Sites |
|---|---|
| 1 | 87 |
| 2 (after the M07 ruling) | 41 |
| held | 15 |
| D-3 | 6 |
| keep | 36 |
| B3a, dropped on b2 | 34 |

Execution records are excluded as history. No schema, document or fixture names the label: `model.schema.yaml` does not describe `pressure_contract` at all, a gap that predates this work. On NUM the label appears in exactly four places:
- the acceptance at `PP/src/pressure_runtime.rs:138`;
- its message at `:142`;
- one test mutation at `PP/src/source_receipt/tests.rs:422`;
- one tamper test at `RE/tests/physics_contract.rs:97`.

| area | acceptance | refusal | computation | scope | test | fixture | golden | schema-enum | reader-branch | ui-path | operation | benchmark | doc | type/field | b3a | all |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PP | 5 | 3 | 23 | 7 | 79 | 1 |  | 1 |  |  |  |  | 1 | 1 |  | 121 |
| solver | 1 |  | 2 |  |  |  |  |  |  |  |  |  |  | 1 |  | 4 |
| loads |  |  | 6 |  |  |  |  |  |  |  |  |  |  |  |  | 6 |
| runner |  |  |  |  | 8 |  |  |  |  |  |  | 2 |  |  |  | 10 |
| RE |  |  |  |  | 1 |  |  |  | 2 |  |  |  |  |  |  | 3 |
| python |  |  |  |  | 6 |  |  |  | 2 | 1 |  |  |  |  |  | 9 |
| app | 1 |  |  |  | 3 |  |  |  | 1 | 9 |  |  |  |  |  | 14 |
| ops |  |  |  |  | 2 |  |  |  |  |  | 3 |  |  |  |  | 5 |
| fixtures |  |  |  |  |  | 3 | 3 |  |  |  |  |  |  |  |  | 6 |
| schemas |  |  |  |  |  |  |  | 2 |  |  |  |  |  |  |  | 2 |
| docs |  |  |  |  |  |  |  |  |  |  |  | 1 | 4 |  |  | 5 |
| b2 (B3a) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 34 | 34 |
| **all** | 7 | 3 | 31 | 7 | 99 | 4 | 3 | 3 | 5 | 10 | 3 | 3 | 5 | 2 | 34 | **219** |

| area | becomes a refusal | remove | delete the test | edit | keep | held | D-3 | B3a |
|---|---|---|---|---|---|---|---|---|
| PP | 3 | 21 | 22 | 52 | 11 | 12 |  |  |
| solver |  | 2 |  |  | 2 |  |  |  |
| loads |  | 6 |  |  |  |  |  |  |
| runner |  | 1 |  | 6 | 3 |  |  |  |
| RE |  |  |  |  | 3 |  |  |  |
| python |  |  |  | 1 | 4 |  | 4 |  |
| app | 1 | 4 |  | 1 | 7 | 1 |  |  |
| ops | 1 | 1 |  | 2 | 1 |  |  |  |
| fixtures |  |  |  |  | 3 | 2 | 1 |  |
| schemas |  |  |  |  | 2 |  |  |  |
| docs |  | 3 |  | 1 |  |  | 1 |  |
| b2 (B3a) |  |  |  |  |  |  |  | 34 |
| **all** | 5 | 38 | 22 | 63 | 36 | 15 | 6 | 34 |

There are no "re-author to exact" dispositions: no committed fixture needs re-authoring.

## 4. Answers

**Q1: implicit legacy documents.** As to pressure, 0.1.0/0.2.0 documents are the legacy contract in substance.
- They take the same `!exact` branch of `validate_profile` as labelled 0.3.0 documents, meet the same nonzero refusal, and use the same legacy computation for any pressure primitive that passes. Today only zero values pass.
- The label changes no physics. It only keeps a labelled document out of source-block recovery and out of the retained route, both of which admit 0.1.0/0.2.0 only.

But 0.1.0/0.2.0 is also the only namespace for:
- components;
- nonlinear and constant-effort supports;
- combinations and `equivalent_static`;
- B1's retained domain (D1.3);
- source-block recovery;
- the app's blank document (0.2.0) and its 0.1.0→0.2.0 migration.

Who reads and writes these documents:
- **Committed model documents:** 219 (198 at 0.1.0, 21 at 0.2.0):
  - model-operations corpus: 110;
  - result fixtures: 39, including B1's 32-document retained corpus;
  - PP tests: 45;
  - product-preview fixtures: 19;
  - app e2e: 4;
  - loads: 1;
  - witness: 1.
- **The app** writes 0.2.0 for every new blank document.
- **Qualification** has none: all 30 of its documents are exact.

Recommendation: D-1 A with D-2 A1. After retirement, 0.1.0/0.2.0 then carry no pressure semantics at all.

**Q2: capability left after retirement.** The exact contract refuses today:
- every component (bends, tees/branches, expansion joints, fittings, metadata-only records);
- nonlinear and constant-effort supports;
- every combination;
- `equivalent_static`;
- any pressure primitive, including zero;
- a case without `pressure_regions`;
- stable-suffix ID collisions;
- a material without the explicit `homogeneous_isotropic_E_nu_v1` basis and Poisson ratio (G is then derived, so an independently authored G is not honoured);
- ambiguous coincident rigid support attribution;
- objective connectors, which are refused everywhere.

Label-carrying documents: 0 in the committed fixtures, 0 among the app's authoring defaults (the app never writes the label), and 0 in the qualification corpus.

Under D-1 A, no committed document loses its route. A labelled document that uses an exact-refused feature has no exact route; none is committed. Its only route is a rewrite as 0.2.0 without the label, and the app cannot make that rewrite because it has no down-migration.

Under D-1 B (the stop):
- 107 committed 0.1.0/0.2.0 documents use an exact-refused feature:
  - by feature: components 98, combinations 99, nonlinear 6, constant-effort 6, `equivalent_static` 2;
  - 5 of them also carry nonzero pressure;
  - by area: model operations 93, result fixtures 7, product preview 2, PP tests 2, app e2e 2, witness 1.
- B1's 32-document corpus would lose the retained route.
- The app's blank document would need an exact default.

**Q3: the app.**

Today:
- A new blank document is 0.2.0 with no contract. The load-state blank (`blankLoadStateModel`) is 0.4.0 with the exact contract.
- `model_document_migration.rs` migrates 0.1.0→0.2.0 as a no-op and keeps 0.3.0 and 0.4.0 unchanged. No app path writes the label.
- `PressureAuthoringPanel` offers only `exact_straight_pressure_v2`. It shows 0.1.0/0.2.0 as pressure mode "legacy".
- The load-case manager offers a "pressure" primitive, and the applier creates it.

After retirement (A, A1):
- New documents are unchanged.
- The manager no longer offers the pressure primitive, and the applier refuses one.
- The panel shows 0.1.0/0.2.0 as "no pressure contract".
- A labelled 0.3.0 document opens unchanged. Its solve is refused with the re-author text, and the panel's queue-profile path re-authors it to exact.
- The bundled demo stays refused, as it is today.

**Q4: the refusal.** One site, `PP/src/pressure_runtime.rs` `validate_profile`, serves all three routes:
- the ordinary route calls it;
- the retained route refuses the label at D1.3 (`F::PressureContract`) and then runs the same ordinary route;
- the runner uses both entries.

Proposed refusals:
- 0.3.0 with `1.0.0/legacy_pressure_v1`: `PRESSURE_MODEL_REAUTHOR_REQUIRED` (blocking, ref `pressure_contract`).
- Any pressure primitive in a 0.1.0/0.2.0 document: the same code (refs: case and load).
- Text: "the 1.0.0/legacy_pressure_v1 pressure contract and legacy pressure primitives are retired; re-author the model to 2.0.0/exact_straight_pressure_v2 with explicit pressure_regions (an explicit [] for an unpressurized case) and E/nu materials".
- Other contracts keep `PRESSURE_CONTRACT_UNSUPPORTED`, with text that names only the exact contract.

Readers:
- On NUM, the RS, TS and PY retained readers already refuse any non-null `pressure_contract` in the carried request as G8 `INVOCATION_MISMATCH` (`RE/src/retained_precision.rs:3519`, `retainedPrecision.ts:1143`, `retained_precision.py:1503`). The plan adds one label case to each.
- A reader re-author message would change B3-D's refusal table, so none is proposed.
- The exact evidence reader already refuses the label as a tampered `profile_mode` (`RE/tests/physics_contract.rs:97`).

**Q5: M07.** Moved to I111, now with the owner. The shared sites are marked `held` in `inventory.json`.

**Q6: the old branches.**
- `codex/piping-pressure-stress-20260924` (`af4120ba52`) holds no live work that main lacks:
  - Its commit message calls it an "authorized local checkpoint only". Main's `22452ecd14` ("Checkpoint joined pressure and source-recovery integration", from the same lane) supersedes it.
  - 16 of its 21 product files are byte-identical to blobs in main's history.
  - The other five were reworked on main: fixtures moved out of `execution/`, version 0.2.0, formatting.
- `codex/piping-result-compatibility-pressure-20260914` (#788, merged 2026-09-15) is fully in main: its head `4201035cb0` is an ancestor of main.
- Neither branch needs any action beyond optional deletion.

## 5. Removal plan (D-1 A, D-2 A1, D-3 a, D-4 reuse)

The base B is main `7eae707bb7`. The work is one PR with Stage 1. Stage 2 follows the owner's M07 ruling, in the same PR if the ruling lands first, or else as a follow-up.

### Stage 1, independent of M07

1. **Refusal.**
   - In `pressure_runtime.rs`:
     - refuse the label;
     - refuse a pressure primitive of any value in a non-exact document;
     - update the two texts.
   - The test-only scope bypass stays (held). It now covers zero values too, so O1–O4 run unchanged.
   - The operation applier's `create_primitive_load` refuses the pressure category.
   - `LoadCaseManagerPanel` drops the pressure category.
   - `PressureAuthoringPanel` text changes.
2. **Tests removed** (pressure-only oracles; their premise is retired):
   - 11 `*_historical_pressure_premise` tests in `PP/src/lib.rs` (all except O2 and O4);
   - `curved_bend_pressure_load`;
   - S11-F F10: 2 tests and 3 helpers;
   - S11-G T6a's pressure run, and its helper;
   - `f1b_w2_admission_refuses_a_zero_legacy_pressure_as_pressure_thrust` and its family builder.
3. **Tests edited:**
   - `profile_dispatch_requires_explicit_regions_and_refuses_legacy_pressure`: zero is now refused, and the label case is added.
   - `legacy_model_three_retains_ordinary_route_without_old_source_namespace` becomes the label refusal.
   - `mechanical_fixture_for_test` strips the demo's pressures instead of zeroing them, for its 39 non-held users. O1 and O3 keep zeroing.
   - 5 runner helpers strip instead of zeroing.
   - The runner test `qualified_actual_solved_documents_match_explicit_library_and_bind_model_identity` expects the refusal for `curved-pressure-full`.
   - The applier's two pressure-primitive tests become refusals.
   - `App.test.tsx`'s pressure-primitive test becomes "not offered".
4. **Tests added** (one per route and reader, plus the app):
   - **Ordinary** (`PP/tests/pressure_runtime.rs`): a labelled model with zero pressure, with and without a combination, is refused; a 0.2.0 zero-valued primitive is refused; 0.2.0 without primitives solves.
   - **Retained:** a labelled model on the direct entry gives the D1.3 report and the ordinary refusal.
   - **Runner:** a CLI solve of a labelled model is refused.
   - **Readers RS, TS, PY:** one label case each, refused as G8 `INVOCATION_MISMATCH`.
   - **App:** src-tauri opens a labelled 0.3.0 document unchanged, and its solve is refused; vitest checks the panel shows the label and queues exact.
   - **Applier:** the pressure-primitive refusal.
5. **Docs:**
   - the migration doc comment;
   - the panel text.

   T4's row notice is WORKING_ITEMS's.

### Stage 2, after the M07 ruling

1. O2 and O4 lose their pressure premise: they are deleted or converted, as the ruling directs. The scope file (`run()`, or all of it) goes per the ruling, along with:
   - the pressure bypass in `pressure_runtime.rs`;
   - `historical_pressure_preview` (and `_with_mode`);
   - the scope part of `private_historical_pressure_scope_restores_public_refusal_and_rejects_exact`.
2. **Remove the legacy computation:**
   - in `PP/src/lib.rs`:
     - the thrust types and builders, and their assembly;
     - the bend radial thrust;
     - the joint thrust review rows and `EXPANSION_JOINT_PRESSURE_THRUST_APPLIED`;
     - `pressure_for_pipe`;
     - the hoop and longitudinal rows and `include_pressure_longitudinal`;
     - the W2 `pressure_thrust_load` family;
     - the `pressure` parameter of `recover_section_stress`;
   - the always-empty pressure plumbing in `source_recovery.rs`, `source_receipt.rs` and `retained_product.rs` (B1 code; byte-identical);
   - the edits to `f1a_tests.rs` and `f1b_tests.rs`;
   - the `stress_recovery` crate's `PressureBasis`, membrane and fields;
   - `curved_bend`'s radial-pressure API (its zero-thrust test callers move to the plain form);
   - `STRESS-PRESSURE-MEMBRANE-ORIGINAL`: the benchmark, its runner binding, the hand calc and the manual page.
3. **Kept:**
   - `component_pressure_thrust_load_count`, always 0 (it is a public summary field);
   - the exact retain list;
   - the preview-physics-1 kind lists and the result schemas (published);
   - the primitive `pressure` category (it must parse so that it can be refused by name);
   - the joint's `pressure_thrust_reference` field (model data; route it to T4).
4. **Hazard H-1, signed zero.** The legacy term enters sums as `+ unwrap_or(0.0)` (`lib.rs:10533`, `:12075-12082`). Deleting it would let a −0.0 axial value through where +0.0 is published today. Keep an explicit `+ 0.0` unless the consumer is sign-insensitive. The byte evidence decides.

### Fixtures

- None is re-authored or deleted.
- `invented_preview_model.json` stays as the refused demo.
- `result_export_v0_2.json` and the witness input stay unchanged.
- D-3 and the held precision-1 pair wait for their rulings.

### Evidence that exact behaviour is byte-identical (each stage, against B)

1. **Per-test outcomes.** Compare test name → outcome at B and at the candidate across the T3 gate set (the 40 manifests, src-tauri, vitest, `P/tests` pytest). They must be identical except for the listed removals, edits and additions.
2. **Exact envelopes.** Run all 48 committed exact model documents (30 qualification, 7 physics-source, 7 load-reference(-source), 4 others) through the ordinary entry and the runner, in both modes. The SHA-256 of the envelopes and of the RE export documents must be equal at B and at the candidate. Compare on the same host: on this Mac, B itself already fails three frozen-golden byte tests (PP `t13_committed_fallback_uz_is_byte_identical`, a known platform failure, and two runner load-reference tests), so the frozen goldens are checked on Linux CI.
3. **Implicit documents.** The 214 committed 0.1.0/0.2.0 documents without pressure primitives must produce byte-equal ordinary envelopes. B1's 32-document corpus must produce byte-equal results through W1, with B1's pins unchanged.
4. **DEC-025.** The exact-head DEC-025 at the candidate.

### Size

| Stage | Hours |
|---|---|
| Stage 1 | about 16: refusal and UI/applier 4, test removals and edits 3, new tests 3, evidence harness and runs 5, review 1–2 |
| Stage 2 | about 13: legacy computation removal 7, O2/O4 and scope per the ruling 1–2, evidence 3, review 1–2 |
| Total | 27–31 |

## 6. Probes (`_run_records/`)

All probes are PP `--lib` plus 19 integration targets (792 tests), or the runner crate (87 tests). The probe edits were never committed (`probe_p2_p3_runner.diff`).

| Run | Change | Result |
|---|---|---|
| Baseline | none | PP: 739 pass, 52 ignored, 1 fail (`t13…`, the known Mac platform failure). Runner: 85 pass, 2 fail (load-reference frozen goldens, Mac) |
| P2 | Label refused; any pressure primitive refused; scope pressure bypass removed | 60 PP tests flip. 40 are users of the zeroing fixture, including O1 and O3. 17 are historical-scope tests. The other 3 are the label test, the zero-dispatch test and the W2 zero-thrust test |
| P3 | P2, with the fixture stripping instead of zeroing; runner helpers stripped | 20 PP flips remain, exactly the 17 scope tests plus those 3. O1 and O3 pass without any pressure bypass. Runner: 1 flip (`curved-pressure-full`, whose only load was pressure) |

Note that a strict A1 refuses even a load-free model's zero primitive (§1).

## Records

This folder contains:
- `RETURN.md`
- `inventory.json`
- `_run_records/`: scripts, logs with placeholder paths, outcomes, `models_scan.json`, the probe diff
- `SHA256SUMS`

WORKING_ITEMS commits it.
