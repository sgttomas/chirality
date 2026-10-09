# T4-I5 return: what T4-U1 and T4-U3's deletion change on T3's side

TASK T4-I5 (Type 2, research only), for T4's HELPS_HUMANS. Brief: `R4/BRIEFS/T4-I5_T3_RETAINED_IMPACT.md`.

- **Basis.** main `ec5d397359` + T3's U3 at `70e7f49ced`. U3 branched from `7eae707bb7`, so for files U3 did not touch (all of FK, NI, SD) the basis is main and is cited `@ec5d397359`; files U3 touched are cited `@70e7f49ced`. `b2` = `9f5cfbcd75` (`codex/piping-t3-b2-20261008`). T3's records: `WT/numerics` HEAD `a31c14e4d3`.
- **Labels.** `NI` = `P/core/solver/nonlinear_integration`; `SA` = `NI/src/structural_adapter.rs` (its tests `SA/…` = `NI/src/structural_adapter/…`); `CB` = `P/core/solver/curved_bend/src`; `FC` = `FK/src/structural/formation_check.rs`; `RE` = `P/core/reporting/result_export`; `RR` = `I/NUMERICAL_INTEGRITY_T3/ROOT_RULINGS_V1.md@a31c14e4d3`; `WG` = `P/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md@a31c14e4d3`.
- **Method.** `git show/grep/diff/log` only, read-only on `b2` and its lanes. No cargo. One `git merge-file` simulation on scratch copies (§5); it is not a product run. **Inference** is marked; everything else is read from the cited bytes.

## 0. Findings most likely to change T4's plan

1. **T4-U1 makes 2 T3 tests fail by design and deletes the premise of 2 more. These 4 are the required M31b/M31b0 kills.** RR:691-704 made those kills a merge condition. They are SA `kd5_tests.rs:419`, `:447` and PP `tests/formation_check_runtime.rs:379`. U1 removes the admissible-centre mismatch they rely on. **T3 must rule the mutant's disposition:** a new kill, or equivalence derived by construction (the M31b lesson, RR:1217). This is a T3 decision, not a re-pin.
2. **Whether `CSKEW_8_5` still demotes after U1 cannot be settled by reading.** Four T3 tests use it as a required curved true positive: SA `kd5_tests.rs:400`, NI `k1_tests.rs:336` and `:1313`. Each starts by asserting `actual > 1.0` or a demotion (k2b `:1312` uses it without asserting a demotion).
   - R5_4 attributes the breach to the non-objective chord (`DESIGN_NUMERICS/R5_4_CURVED.md:100-115`).
   - **Inference:** binary64 rounding of K at cond ≈ 6.4e7 may keep it near the criterion.
   - **A run is needed.** That belongs in U1's reference work.
3. **Deleting the W4 tie reduction re-derives most of FK's K5 suite, not just `user_element_tie`.** The ties carry most of the vectors:
   - 961 of 1,000 `b1_sample.txt` records, 23 of 29 `cases.txt` records and 222 of 301 `subnormal.txt` records;
   - plus `k5_scale.rs`'s tie chain of 10,000.

   That covers B1–B9 and B5-parameters (§1.2). The cheaper alternative keeps the reduction and deletes only its producer: `user_element_tie`, `TieRefusal` and SA's `UserTie`. Then only K5-C, the tripwire, B10's name list and NI's joint cases change. This is I3's D3, and it needs T3's choice.
4. **Neither change touches T3's retained route, `REVIEWED_INPUTS`, `REGISTERED_PROFILES`, a priced atom, `PINNED_RECORD` or M** (with H-4).
   - W1 admission refuses any model with components (`PP/src/retained_memory.rs:755-756`, `:801-802@70e7f49ced`).
   - W1 calls only `assess_rigid_body` (`FK/src/structural/retained/factor.rs:50`, `:201@ec5d397359`), which T4-U3 does not touch.
   - **Pass B still applies to both units,** because both edit files on the D1 call graph (inference, by analogy with U3 and PR-N).
5. **One trap for U1:** any change to `preview_physics::LIMITATIONS` hits T3's whole corpus radius, the same as the deferred `:75` wording. For example, `:77`'s "Endpoint force rows are in the chord frame" (`@70e7f49ced`) is in 20 files at U3 (8 successor pins, 07n, the schema) and 22 at `b2` (10 successor pins). U1 should leave these texts unchanged, or join T3's generation.
6. **`b2` has no textual overlap** with either change (simulated merges are clean; §5). It does widen H-4's deferred radius: once `b2` merges, the summary key is in 92 files (88 at U3), and the row kind is in 10 reviewed semantic contracts (9 at U3).
7. **The H-4 renames do not depend on T4-U3's deletion.**
   - The key also counts curved rows.
   - G11 already refuses every flexibility joint, so the user row kind is never produced.

   T3 can therefore run them in the wave that carries `preview_physics.rs:75` (RR:16518: J0b or PR-B2's wave if cheap, otherwise B7), and T4-U3 then lands with no re-pin.

## 1. Tests (Q1)

### 1.1 T4-U1 (objective formation; `center` removed; `CurvedFormation` takes d, R, n̂; SA's trace uses the actual chord)

The constructor has **21 call sites in 9 files** at `@70e7f49ced`. I2 found 19 in 8; it missed `P/validation/benchmarks/mechanics/src/lib.rs:3345` and `:3650`. Status key: **F** = fails by design; **P** = premise unconstructible (delete or rewrite); **R** = reference re-derived (meaning kept); **M** = mechanical (signature) only.

| T3 test (owner unit) | Asserts today | U1 |
|---|---|---|
| PP `tests/formation_check_runtime.rs:358` `kd5_large_coordinate_pp_route_elbow_is_published_accurately_and_not_demoted` (K-D5) | X≈5e5 elbow: `actual < 0.5` against `u_int` derived from PP's binary64 centre (`:250-264`); Passed on both entries, both modes | **R** (expected to pass) |
| PP `…:379` `kd5_very_large_coordinate_pp_route_elbow_demotes_on_both_entries` (K-D5, the product-level M31b killer, `:384-385`) | Precondition `actual > 1.0` (`:388`); SENSITIVE on both entries and modes | **F** → becomes a UTM control (C2) with re-derived `u_int` (`:270-286`) |
| SA `kd5_tests.rs` + generated `kd5_models.rs` (7 bend models carry a binary64 centre: E1, E6, CSKEW_8_5, CSKEW_30_RADIUS_MISMATCH, CPLANAR_60, CSKEW_30_N122, PP_UTM_2; run record `kd5_models.py`) | — | regenerate inputs and `u_int` |
| SA `kd5_tests.rs:378` E1/E6 | Passed, `actual < 0.5`, unchanged | **R** |
| SA `:400` `…at_kx_8_5_demotes_in_both_modes` | Passed, `actual > 1.0`, demoted, EF/actual within 1e-3 | **undetermined** (finding 2) |
| SA `:419` `kd5_curved_intended_element_uses_the_actual_chord` | Centre moved 6.5e-10 R; `actual > 0.7`; demoted (M31b) | **P** |
| SA `:447` `kd5_admissible_centre_mismatch_demotes_where_the_product_chord_hides_the_error` | CPLANAR_60 and CSKEW_30_N122 at the radius tolerance: `actual > 1.0`, demoted (the M31b/M31b0 kill) | **P** |
| SA `:484` PP_UTM_2; `:504`; `:523` | Not demoted; order-independent; unmatched, explicit and one-ulp slots fail closed | **R**; **M**; **M** |
| NI `k1_tests.rs` KD5 corpus `:183-197` (13 models, including the 3 **P** models); `:336` (CSKEW_8_5 demotes in both representations); `:1313` RV8-3 (F122 and CSKEW_8_5 demote); `rv8_bend` `:1153-1170` | — | corpus loses 3 models; `:336` and `:1313` depend on finding 2; the rest **M** |
| NI `k2b_tests.rs` corpus `:40-53`; `:1312` (uses CSKEW_8_5; no demotion assert) | — | corpus −3; **R** |
| NI `k5_tests.rs` (K5): `bend()` `:75-80`, `curved_mechanism` `:189`, `curved_only` `:219`, `from_kd5` `:262-293`, `kd5_curved` `:295-307` (includes the 3) → `:1078`, `:1203` | W4 witnesses are geometric | `:1078` and `:1203` lose 3 models; the rest **M** |
| FK `structural/formation_check_tests.rs:69` (curved part `:104-117`: `center`) and `:276` (`center`-based "collinear radial vectors" and "near π" AngleDomain cases, `:283-296`) | Rigid null space to p; arctangent domain errors fail closed | **R** at `:69`; **P/R** at `:276` (the domain triggers become \|d\| ≷ 2R) |
| PP `tests/k5_curved_mechanism_runtime.rs:148`, `:207`, `:225`, `:250` (K5) | Mechanism witness or refusal on the PP route | **R** (geometry-only witness; inference) |
| PP `s11g_tests.rs:1747` `t15_curved_uniform_load_is_cannot_bound` | Curved uniform load is CannotBound → Sensitive | unchanged by U1 (changes only with U2's bound) |
| PP `s11g_tests.rs:2380`; `s11f_tests.rs:1600`, `:1605`, `:1650`, `:1688` (`f8_curved_*`) | Expectations are taken from the product's own built element (for example `s11g:2422`) | rerun, expected to pass |
| FK `tests/s11_site_table.rs` (scans `CB/lib.rs` `:82-83` and FC `:91-92`; CB rows `:275-283`) and PP `tests/s11f_site_test.rs` (scans CB `:141`; curved rows `:166-168`, `:219`, `:508-536`) | Exact per-function accumulation counts | fail where U1 adds an accumulation in a listed function; re-listed under S11 |

M31b/M31b0 (finding 1): RR:691 "must be killed by a required test before merge". The required kills are RR:703-704, which are SA `:447` and PP `:379`.

Not T3's, but affected by U1: CB `rigid_body_modes_produce_zero_force`, `rotated_geometry_transforms_stiffness_congruently` and the CB constructor sites; PP `tests/preview_physics_runtime.rs:854`, `:913` (T0R); PP `lib.rs` `curved_bend_macro_element_*` (I2 §1.7).

### 1.2 T4-U3's deletion (element, W4 tie reduction, plumbing; H-4 keeps the key and the row kind)

| T3 test | Asserts today | U3 |
|---|---|---|
| FK `tests/k5_constrained_bodies.rs` (K5) `:943` K5-C `k5_c_user_tie_rule`; `:992` `k5_t4_tripwire_user_tie_space_is_the_represented_null_space` | The tie rule; the user local matrix equals Σ k_d(e_d − e_{d+6})(…)ᵀ bit for bit | **delete** (the tripwire is meant to fire, `:978-991`) |
| same file: B1 `:340`, B2 `:381` and `:392`, B3 `:417`, B4 `:432`, B5 `:488`, B6 `:560`, B7 `:573`, B9 `:705` (3 of its 7 cases are tied), B5-parameters `:1073` (SUBNORMAL tally 301 / P→U 24), B8 `:588` (tie checks `:640`, `:644`), B10 `:895` (scanned names include `user_element_tie`, `reduce_constrained_body`) | Exact status, witnesses and invariances of the **tie reduction**, on tie-bearing vectors | if the reduction is deleted: regenerate `k5_constrained/` (`gen_k5_vectors.py`, `b1_sample.txt`, `b1_summary.txt`, `cases.txt`, `subnormal.txt`, `subnormal_summary.txt`, `SHA256SUMS`) or delete; if only the producer goes: B10's list only |
| FK `tests/k5_scale.rs` | Memory of `assess_constrained_bodies` on a 10,000-tie chain | delete or rewrite (with the reduction) |
| NI `k5_tests.rs`: `joint_mechanism` `:233-260`; `:506` (case "user-element tie"), `:937` `k5_user_elements_tie_only_with_positive_stiffnesses`, `:1106`, `:1225` ("joint companion"); `AssemblyEvidence::new(…, users, …)` `:976` | W4 tie outcomes | `:937` **delete**; the other three drop their joint case; **M** |
| NI `kd5_tests.rs:631` `kd5_expansion_joint_with_zero_lateral_does_not_demote_and_nonzero_lateral_fails_closed` (`joint_model` `:569-629`; `Built.users` `:55`) | Lateral = 0 re-forms; lateral ≠ 0 is `unavailable` | **delete** or replace with the connector's re-formation |
| FK `formation_check_tests.rs:69` (user part `:73-81`, `user_matrix` `:131`) | The joint's rigid null space | user half **deleted** (or BᵀKB) |
| FK `tests/k2b_force_scaling.rs:159`, `:288`, `:583`; FK `structural/sparse/tests.rs:409` (+ `:238-312`); FK `tests/k1_k2a_interaction.rs:21`, `:83`; FK `tests/s11_site_table.rs:194` (`add_relative_dof_stiffness`, 4) | User census and scaling; sparse refusals; site row | rewrite / **M** / row removed |
| NI `k1_tests.rs:816`, `:1490`; `k2b_tests.rs:1403`; NI `src/s11k_tests.rs:861`; SD `src/structural/k1_tests.rs` helpers | User slots in the K1/K2b/S11-K evidence | **M** / joint parts dropped |
| PP `f1b_tests.rs:2227` `f1b_admission_names_each_family` (asserts `"user_stiffness_element"`, `:2245-2249`); `s11g_tests.rs:2605` t21 (`assemble_global_stiffness_with_user_elements`, `:2609-2612`); `tests/f1b_w2_runtime.rs:707`; `tests/s11f_site_test.rs:511`; `source_receipt/tests.rs:24`; `retained_product_tests.rs:2435` (a `Summary` literal) | Family name; assembler API; site row; literal | rewrite / **M** / row removed / unchanged under H-4 |
| PP `lib.rs:17391`, `:17407`, `:17469`, `:17541@70e7f49ced` (added by U3: G11 and the mapping refusals) | `JOINT_ELEMENT_*` codes | re-pin to `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED` |

The non-T3 sites (HR, ST, TS, Python and docs) are in I3 §1.2.

## 2. Pins and fixtures (Q2)

- **T4-U1: no committed corpus pin changes.**
  - No committed fixture holds an arc row: `arc_chord_frame` occurs only in source, tests, `schemas/results.v0.3.schema.yaml` and the two semantic contracts, at both U3 and `b2`.
  - The 8 successor pins at U3 and the 14 at `b2` hold no curved content. Nor does 07n (`fixtures/results/retained_precision_cases.json`: 0 occurrences).
  - `fixtures/results/invented/result_export_v0_2.json:1236-1265` holds two curved review rows marked `EXACT_ORIGINAL_PRODUCER_ROW_SNAPSHOT_NOT_NEW_RUNTIME`. They are not regenerated.
  - What does change is test-embedded: the generated `kd5_models.rs` and its `kd5_models.py`, and the `u_int` literals in `formation_check_runtime.rs:250-286`.
  - The condition is finding 5: no change to `LIMITATIONS`.
- **T4-U3 with H-4:** 0 of the key's files (88 at U3, 92 at `b2`; the 92 include 10 successor pins and 07n ×26), and 0 reviewed inputs.
  - **Refusal-code re-pins outside T3's corpora:** `P/core/runner/headless/src/result_envelope_binding.rs:448-490`, `…/tests/preview_physics_admission.rs:249-280`, `RE/tests/preview_physics_contract.rs:606`, and `result_export_v0_2.json` (2 producer cases) (I3 §1.3).
  - **Two candidate texts with no pins:** NI's assumption and limitation strings (`NI/src/lib.rs:1110-1111`, `:1120`) and the M03 mixed-family text (`SA:1539`, "…bodies containing user/curved elements…"). No committed fixture pins either at `b2`.
  - At `70e7f49ced`, the M03 text sits in `invented_mechanics_result_precision_1_{dense,sparse}.json`, and three demo files carry count 4. At U3's later head `fe657e3a68`, neither appears in any fixture (the demo lane).
- **`PINNED_RECORD` and the challenge literals** (`PP/src/retained_memory_law_tests.rs:1194-1197`, `PP/tests/retained_memory_challenge.rs:36-39@70e7f49ced`): unchanged by either unit (§3).
- **DEC-025:** there is no committed baseline. Each exact-head run uses a fresh main baseline (RR:13059, :13346). The manifests will show the added and removed test names of §1, which must match the declared lists.

## 3. Registered profile and M (Q3)

- **`REVIEWED_INPUTS`.** 14 entries at U3 (`PP/src/build_identity.rs:148-163@70e7f49ced`):
  - `Cargo.lock` (PP's);
  - `schemas/physics_source_recovery.schema.json`, `schemas/retained_precision_mp_v2.schema.json`, `schemas/source_block_recovery.schema.json`;
  - `fixtures/results/retained_precision_prepared_ordinary_v1.json`;
  - nine semantic contracts: `semantic_contract_v0_2.json` and the `v0_3_` ones for `preview_physics_retained_1`, `precision_1`, `physics_1`, `load_reference_1`, `load_reference_source_1`, `preview_physics_1`, `physics_source_1` and `source_blocks_1`.

  `b2` appends 3, for 17 in all (`build_identity.rs:149-170@9f5cfbcd75`): `retained_precision_prepared_combination_v1.json`, `retained_precision_prepared_exact_v1.json` and `semantic_contract_v0_3_physics_retained_1.json`.

  **No file either unit changes is a reviewed input.** The semantic contracts carry only kind, unit and dimension descriptors (for example `preview_physics_1` rows 24 and 41-44). The prepared definitions list `curved_members` only as an exclusion. `Cargo.lock` changes only if T4 adds a crate dependency.
- **`REGISTERED_PROFILES`** (`PP/src/retained_memory.rs:972-992@70e7f49ced`) holds the identity, the reviewed-input text, the reader layouts and M = 11,274,289,152 B. **No priced atom names a type that holds a curved element, a user element or `BuiltModel` by value.**
  - The PP atom types are listed at `:1660-1835`, for example `s(MechanicsEnvelope)` `:1746`.
  - `BuiltModel` (`PP/src/lib.rs:2043-2055@70e7f49ced`) appears only by reference (`retained_memory.rs:2396`).
  - FK's `retained_resource.rs` exports no `rigid_body` or `formation_check` type.
- **Result:** no atom, `PINNED_RECORD` or M change (fact for the atom list). Pass B (`g7_pass.sh`, RR:10598-10623) is the gate that confirms TEXT and forms (inference that it will).
- **Without H-4:** removing the summary field shrinks `s(MechanicsEnvelope)`, which means a `PINNED_RECORD` re-pin. Removing the row kind from the 9 reviewed semantic contracts (10 at `b2`) makes the registered build Stale, which means re-registration.

## 4. The retained and source routes' outputs (Q4)

- **Retained (W1): no output changes.**
  - Admission runs before the ordinary solve (`PP/src/lib.rs:2261@70e7f49ced`) and refuses on `F::Components` for any component. Its refusal is private evidence (`:2258-2260`).
  - The capture check (`retained_product.rs:1557-1560@70e7f49ced`, "unsupported producer present") is internal.
  - W1's only K5-family call is `assess_rigid_body`. T4-U3 deletes `TieRefusal`, `user_element_tie` (`FK/src/rigid_body.rs:331-361`) and the reduction in `assess_constrained_bodies`/`reduce_constrained_body` (`:480`, `:695@ec5d397359`). Their callers are SA (`:1440`, `:1493`) and tests only.
- **Source route: the refusal text stays** (`source_recovery.rs:579-585@70e7f49ced`, "component, curved, user-matrix or release source family"; not pinned anywhere). **What changes is whether it is reached.** The attempt runs only when a case is Sensitive, errs, or has a load-row finding (`lib.rs:1190-1196`, `:4286-4319`). A failed attempt publishes an info `SOURCE_BLOCK_RECOVERY_UNAVAILABLE` with the failure text (`:4378-4384`).
  - **U1:** curved cases that K-D5 demotes today (UTM scale) become Passed, so the source attempt and that diagnostic disappear for them (inference from the trigger). No committed fixture has such a model.
  - **U3 under D-4:** app-authored joints are blocked before solving (`lib.rs:2412-2415`), so no source attempt runs.
  - Readers need nothing: codes are free strings (I3 §5).

## 5. `b2` (Q5)

- **`b2`'s shape.**
  - Its merge base with main is `ec5d397359`. It does not contain U3.
  - The lanes `b2-a` `ea5625ad04`, `b2-k` `e22fd799bc`, `b2-p` `27c45da2ba`, `b2-r` `d86c0805c6` and `b2-t` `dc6b7359ba` are all ancestors of `b2`'s head, and every worktree is clean, so `b2`'s diff covers them.
  - That diff changes 78 files outside records.
  - It does not touch CB, FC, SA, NI or any FK test that U1 or U3 edits.
- **Shared files: all textually disjoint.** Line numbers are at `ec5d397359`.

| File | `b2` hunks | T4 sites | Result |
|---|---|---|---|
| `PP/src/lib.rs` | `2207-3567` (W1 dispatch) | U3 `2810-2812`, `2874`, `3557-3572`; U1 `1432-1459`, `6162-6216`, `7928`… | disjoint. A simulated edit of all 130 user/curved lines merges cleanly |
| `PP/src/retained_product.rs` | insert after `1554` | `1560` | simulated merge clean |
| `PP/src/retained_product_tests.rs` | insert after `2438` | `2435` (no edit under H-4) | clean |
| `RE/tests/preview_physics_contract.rs` | after `830` | `606` | disjoint |
| `P/apps/desktop/src/services/previewService.ts` | `3`, `132` | `340-383` | disjoint |
| `FK/src/structural.rs` | `25-48` | `62-65` (`CurvedFormation` export) | disjoint |

  - **Only if H-4 is reversed:** `RE/src/retained_precision.rs:2500-2503`, `retainedPrecision.ts:110` (a `b2` hunk at `:101`) and `P/core/analysis_runs/retained_precision.py:1150`. These would also be disjoint.
- **Semantic overlap.**
  - `b2` adds no code that calls any API T4 changes (grep of `b2`'s added lines).
  - It does add the key to 4 new successor pins and the 5 joint/curved row kinds to its new reviewed input `semantic_contract_v0_3_physics_retained_1.json`. That is finding 6.
  - B3's exact W1 route also refuses components (`retained_memory.rs:872-873`, `:930-931@9f5cfbcd75`), so T4's v3 connectors and bends stay outside it. This is fail-safe.

## 6. The next corpus generation (Q6)

- **Scheduled order (facts).**
  - RR:11948: U8 → B0 → B1/B6 → PR-B1 → B2/B3 → B4 (if ruled) → PR-B2 → **B7** (the release identity) → B8. Breadth reaches main in two PRs (RR:11928).
  - **J0 is split** (`I/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/BRIEFS/B2_J0A.md:8-9@a31c14e4d3`). J0a is done (`b2` `9f5cfbcd75`, the six B2-P pins re-taken). J0b is "a smaller absorb once U3 merges".
  - **Then:** SQ2 (its brief is still to write; WG:723), J1's package, and PR-B2 with its re-pin wave and re-qualification. Every PP build on `b2` stays Stale until SQ2's registration (RR:14619).
  - **B7:** "registered once"; the milestone's bytes and verdicts are re-established on it (WG:586). It needs PR-B2.
  - **Timing:** the records give no dates. B2/B3's planning estimate is 206–329 agent-hours after PR-B1, plus revisions (WG:585).
- **The `:75` wording.** RR:16518 assigns the deferred `preview_physics.rs:75` wording to "J0b or PR-B2's re-pin wave if cheap there, otherwise B7". Its radius is 28 pins, 8 successors, all of 07n and the schema's const arrays.
- **Where H-4's renames should go (inference and recommendation).**
  - **J0b** is an absorb, not a re-pin wave.
  - **PR-B2's wave** re-pins `b2`'s corpora and re-registers the profile (SQ2), so it can carry both the key rename (bytes only: 92 files including 07n, with no atom change) and the row-kind removal (10 reviewed inputs, so a registration). B7 can too.
  - **The renames need not wait for T4-U3** (finding 7), and PR-B2 is expected to precede T4-U3 (inference from the order above and T4's plan §7). So the single wave is: **the key rename and row-kind disposition join the `:75` wording in PR-B2's wave if T3 judges it cheap; otherwise all three go together at B7.**
  - **T4 should add one item to that list:** any U1 change to `preview_physics::LIMITATIONS`, which is better avoided.

## 7. Evidence

- **Merge simulation:** `git merge-file -p T4sim base b2` on `ec5d397359`/`9f5cfbcd75` copies of `PP/src/lib.rs` and `PP/src/retained_product.rs`. Exit 0, 0 conflict markers.
- **Counts:** `git grep -c`/`-l` on the commits named.
- **Wider consultation:** T3's R5_4 and the J0a brief, read only.
