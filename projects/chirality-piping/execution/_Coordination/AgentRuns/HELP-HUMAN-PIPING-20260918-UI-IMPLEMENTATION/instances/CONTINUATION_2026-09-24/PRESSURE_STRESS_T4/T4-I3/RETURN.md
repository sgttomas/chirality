# T4-I3 RETURN: the joint (M07) and the deletion PR

**Role and limits.** TASK (Type 2), research only, for T4's HELPS_HUMANS. Brief: `R4/BRIEFS/T4-I3_JOINT_DELETION.md`. Read-only: no build, no test run, no tracked file changed, no commit. Every code claim was read with `git show`/`git grep` at the cited commit.

**Basis and abbreviations.** U3 = `70e7f49ced` (T3 pressure retirement, the basis). DL = `9744ed7e69` (I114's demo lane, branched from U3's `4c0d5d7c00`, not yet in U3). RRc = `d7404b485d` (numerics HEAD at reading). Base = `ec5d397359`; JR and E are unchanged between Base and U3. Paths: `NI` = `P/core/solver/nonlinear_integration`, `SD` = `P/core/solver/sparse_direct`, `HR` = `P/core/runner/headless`, `ST` = `P/apps/desktop/src-tauri/src`, `TS` = `P/apps/desktop/src`, `OA` = `P/core/model_operations/operation_applier/src`, `JR` = `I/CORRECTNESS_DESIGN/JOINT_REFERENCE`, `RR` = `I/NUMERICAL_INTEGRITY_T3/ROOT_RULINGS_V1.md`, `I111` = `I/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I111/m07_premise_01/REPORT.md`, `E` = `P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260913-RESULTS-ENGINEERING-3D/instances/ENGINEERING`.

**Labels.** "Fact" means read in the source. "Inference" means my reasoning from those facts.

## 0. Findings most likely to change the plan

1. **This is a replacement, not a deletion (inference).** The old element occupies about 15 reviewed solver slots: dense, sparse and NI assembly, the K2b census and force scaling, the K-D5 re-formation, the K5/W4 tie, S11-G bodies, F1b admission, retained/source refusals, and NI strict-gap. The corrected joint needs each slot again, or a fail-closed refusal in it (§1.4). The PR that deletes the element must therefore carry the primitive and a per-slot decision. It touches about 38 Rust files.
2. **Avoidable re-pins (fact).** Removing or renaming `Summary.component_user_stiffness_macro_element_count` would:
   - touch 88 committed files, including 6 retained-precision successor pins;
   - shrink the priced profile atom `s(MechanicsEnvelope)` (`PP/src/retained_memory.rs:1746@U3`), which means a PINNED_RECORD re-pin.

   Removing the `component_user_stiffness_macro_element_review` row kind from the 9 semantic-contract fixtures would change `REVIEWED_INPUTS` (`PP/src/build_identity.rs:148-163@U3`). Those are hashed into `REGISTERED_PROFILES` (`PP/src/retained_memory.rs:976@U3`), so the registered build would go stale. Both can stay: the count also counts curved-bend rows (`PP/src/lib.rs:2777-2779@U3`). Adding new connector result kinds to those same fixtures triggers the same re-registration.
3. **No container exists today for the corrected joint (fact).**
   - `objective_connector` is accepted only in 0.3.0/0.4.0 documents (`PP/src/pressure_runtime.rs:157-168@U3`).
   - After U3, 0.3.0/0.4.0 documents are exact-contract only.
   - The exact profile refuses every component (`:171-177`) and requires E/ν.

   `E/contracts/CONNECTOR_CONTRACT_V1.md:7@Base`'s "no E/nu prerequisite" premise is therefore void. Before any connector can solve, T4 must lift the exact profile's component refusal for connectors.
4. **Pressure ownership conflict (fact plus inference).**
   - JR selects representation (A): element-owned cap pairs (`JR/CONTRACT.md:69@Base`).
   - The exact runtime is (B)-shaped: real-terminal caps (`transfers_to_wall`) plus per-member Poisson eigenloads, and no interior pairs (`PP/src/pressure_runtime.rs:1-5,327-344,669-760@U3`).
   - Adding JR's full `[-Pe,+Pe]` pair under the existing ledger is exactly the J4 double count.
   - So either the joint owns `p(Ae−Ai)` under (B), or the exact ledger is restructured to (A). This needs a ruling.
5. **The legacy population is mostly app-authored and solves today (fact).**
   - The desktop and the operation applier author joints without `mechanics_interface` (`TS/features/component-creation/componentIntent.ts:263-271@U3`; `OA/lib.rs:2424-2438@U3`).
   - Such a joint gets only the warning `EXPANSION_JOINT_MECHANICS_INTERFACE_UNSUPPORTED` (`PP/src/validation.rs:1147-1162@U3`).
   - It then solves with its pipe as an ordinary rigid frame (`PP/src/lib.rs:7324@U3`).

   Whether `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED` covers this population, or only the refused `mechanics_geometry_and_user_flexibility` joints, is an owner-level scope decision (§5).
6. **No multipoint constraint exists (fact).** Supports restrain global DOFs only (`PP/src/lib.rs:483@U3`). JR's ideal ties (`qt_x=0`, ideal rods) need a new constraint mechanism; elastic rods fit the element slot.
7. **Which PR "lands the corrected joint" (question).** The owner tied the deletion to that PR (`RR:16464@RRc`). JR's J-A has no production substitution (`JR/CONTRACT.md:144@Base`); J-B is the live path. HELP_HUMAN should state which one is meant. The PR's size and its gate set differ greatly between the two.

## 1. The deletion extent (Q1)

### 1.1 What is deleted, and why nothing published depends on it

Facts:
- FK `user_stiffness_local_matrix` is six uncoupled `add_relative_dof_stiffness` springs (`FK/src/lib.rs:1739-1760@U3`). `UserStiffnessElement::new` requires all four stiffnesses positive and finite (`:633-660`).
- PP builds the element between the two ends of the mapped pipe and keeps that pipe in parallel (`PP/src/lib.rs:7480-7574,7324@U3`).
- There is one solve gate, `refuse_unqualified_joint_elements` (`PP/src/lib.rs:2412@U3`; `PP/src/preview_physics.rs:106-211@U3`). It refuses:
  - missing values: `JOINT_ELEMENT_STIFFNESS_INCOMPLETE`;
  - an unresolved mapping: `JOINT_ELEMENT_MAPPING_UNRESOLVED`;
  - a nonzero lateral stiffness over a length: `JOINT_ELEMENT_EQUILIBRIUM_UNQUALIFIED`.
- A zero or invalid value passes the gate, and then FK's constructor refuses it as `EXPANSION_JOINT_MACRO_ELEMENT_INPUT_INVALID` (`PP/src/lib.rs:7555-7593@U3`).
- So no product path assembles the element. I111 §2 (`I111:16-28@RRc`) agrees.

Inference: the deletion changes no published output of an admitted model. The byte evidence can follow U3's form, "equal except declared refusal codes and texts" (`RR:16500-16504@RRc`).

### 1.2 Deletion list on U3

"Lines" are rough counts of enclosing blocks. In addition, about 390 directly matching lines sit in 38 Rust files.

| Area | Sites | ~Lines | Action |
|---|---|---|---|
| FK `src/lib.rs` | struct and impl 622-692; `force_scaled` 1100-1112; census `user()` 1197-1202 and doc 1124; `assemble_global_stiffness_with_user_elements` 1293-1325; local matrix 1739-1760; tests 2109-2140 | 165 | delete. Collapse the assembler API (about 18 callers, mostly `&[]`) |
| FK `src/rigid_body.rs` | import 261; `TieRefusal` and `user_element_tie` 327-361 | 40 | delete. The W4 tie reduction in `assess_constrained_bodies` and `reduce_constrained_body` (478, 693-835) has no other producer: a decision (§6 D3) |
| FK `structural/formation_check.rs` | `users` 70; lateral demotion 169-175; loops 255-256, 392; `user_matrix` 637-660 | 45 | replace with a connector re-formation, or name it `unavailable` |
| FK `structural/sparse.rs` | 40, 503-553 (force-scaled inputs), 592-640 (`users` parameter) | 25 | replace |
| FK tests | `sparse/tests.rs` 238-312, 409-445; `formation_check_tests.rs` 69-145; `tests/k2b_force_scaling.rs` 159-213, 288-345, 536-581; `tests/k5_constrained_bodies.rs` 909 and 918-1059 (including the T4 tripwire 990-1059); `tests/k1_k2a_interaction.rs` 21, 83; `tests/s11_site_table.rs:194` | 260 | delete or rewrite |
| NI `src/lib.rs` | field 243; assembly 581-603, 1310; **published text** 1110-1111, 1120; friction fixture 3580-3610 (used by 4 tests at 3770, 3907, 3955, 4251); test assemblies 3848, 4140, 4984 | 100 | The 4 friction tests need another coupling element and a re-derived expectation |
| NI `src/structural_adapter.rs` | 7, 18, 47-118, 496-548; `EvidenceParts` 1085-1160; W4 1369, 1414-1450; force scaling 1615-1700, 1787-1910; strict gap 2570 | 130 | replace |
| NI adapter tests | `k1_tests.rs` (816-851, 1028-1034); `k5_tests.rs` (243, 937-980); `kd5_tests.rs` (54-148, 567-642); `k2b_tests.rs`; `s11k_tests.rs` | 170 | rewrite |
| SD, performance harness, benchmark | `SD/src/structural/k1_tests.rs` (17-312); `P/core/solver/performance_harness/src/k6/staged.rs:289`; `P/validation/benchmarks/nonlinear/src/lib.rs` (7 constructors) | 40 | signature edits |
| PP non-test | imports 49, 51; S11-G edges 1240-1246; K2b case 1455; F1b family 1556-1557; `BuiltModel` field 2048; count 2777-2779; basis assembly 3539; dense assembly 3757-3770; contact seed 4433; NI input 5756; evidence 6102, 6136, 6257, 6383-6447; builder 7335-7336, 7415, 7480-7593; review rows 11904-12003. Also `preview_physics.rs:106-211`; `validation.rs:1147-1162,1317-1400,1771-1865`; `retained_product.rs:1558`; `source_recovery.rs:579`; `source_receipt.rs:312-316`; `source_receipt/source.rs:376` (`"user_elements":[]`, unpinned); `formation_guard.rs:83` | 600 | delete or replace. The refusal and validation are rewritten for the legacy code |
| PP tests | `lib.rs` 14319-14321, 15222-15240, 17391-~17600 (the G11 and M07 tests); `f1b_tests.rs` (346-2260, including the admission test 2217-2260); `s11g_tests.rs:2609`; `source_receipt/tests.rs:24`; `retained_product_tests.rs:2435`; `tests/preview_physics_runtime.rs:1032-1077`; `tests/s11f_site_test.rs:511`; `tests/f1b_w2_runtime.rs:702` | 330 | rewrite as legacy-refusal tests |
| HR, ST, reporting | `HR/src/lib.rs:1139-1141`; `HR/src/result_envelope_binding.rs:448-490`; `HR/tests/preview_physics_admission.rs:249-280`; `ST/lib.rs:7144-7147`; `P/core/reporting/result_export/tests/preview_physics_contract.rs:606` | 50 | re-pin the refusal code |
| TS | `features/report/ReportPanel.tsx` 334-371, 405-443, 500-511, 728-731; `services/previewService.ts:340-350`; `features/results/retainedPrecision.ts:110`; `features/component-creation/componentIntent.ts` 3, 210-227, 341-351, 371-394; `model-tree/ModelTree.tsx` 517-562, 1442-1519; `model-tree/PropertyInspector.tsx` 1353-1470; `App.test.tsx` (34 joint lines @DL); `e2e/r2-smoke.spec.ts`; `e2e/ui-foundation/full-cohort-controller.ts` | 300 | Reader rows can stay (historical). Legacy authoring is a decision (§5) |
| Python and schema | `P/core/analysis_runs/records.py:477-480,502`; `P/core/analysis_runs/retained_precision.py:1150`; RS `P/core/reporting/result_export/src/retained_precision.rs:2500-2503`; `P/schemas/component.schema.yaml:236-241,497-506` | 10 | keep for reading historical rows |
| Docs | `NI/README.md:11`; `P/core/solver/curved_bend/README.md:6`. Historical and immutable: `SMOKE.md:9584-9603`, `plans/*`, REPRO evidence | small | edit the live READMEs only |

**Not the joint (fact).** These must not be swept up by a text search:
- `mechanics_consumption=linear_spring_primitive_user_stiffness` belongs to springs and hangers (DEC-049; `PP/src/lib.rs:17620@U3`).
- The curved-bend macro-element.

### 1.3 Re-pins and gates the deletion PR may trigger

All facts at U3 unless marked.

1. The summary key (finding 2). It appears in 88 files: 47 under `P/fixtures/product_preview`, 20 under `P/fixtures/results` (including the six `retained_precision_*_successor_*.json` and `retained_precision_cases.json` ×26), 3 result-export test fixtures, and 2 witnesses. RR's rule applies: report the blast radius before touching successor pins (`RR:16504@RRc`).
2. The semantic-contract row kind and the `REVIEWED_INPUTS` registration (finding 2).
3. The S11 site tables: remove `FK/tests/s11_site_table.rs:194` and `PP/tests/s11f_site_test.rs:511`. New connector formation and recovery sites must be listed. Recovery sums use `ExactAccumulator` under S11-V1 (`RR:55@RRc`).
4. The refused-demo envelopes `P/fixtures/product_preview/invented_mechanics_result_preview_physics_1_{sparse,dense}.json` carry C-150's `EXPANSION_JOINT_USER_STIFFNESS_REVIEWED` info diagnostic. They are blocked by pressure first. They regenerate, through `preview_physics_fixture_generation.json` (@DL), if the joint validation text changes.
5. `P/fixtures/results/invented/result_export_v0_2.json` has 2 producer cases with the realized C-150 (`straight-full`, `blocked`). The HR test pins `JOINT_ELEMENT_EQUILIBRIUM_UNQUALIFIED` on them (`HR/src/result_envelope_binding.rs:476-484`).
6. NI's assumption and limitation strings are published as HR envelope diagnostics whenever nonlinear supports run (`HR/src/result_envelope_binding.rs:298-323`). Only historical REPRO evidence pins them. They name "user-stiffness macro-elements", so the RR text test applies (`RR:16500@RRc`).
7. The component libraries `P/fixtures/component/invented_{,section_}component_library_valid.json` carry 3 flexibility joints each. `P/validation/witness/inputs/tp_runner_015_final_cli_solve_input.json:294` is historical.
8. Adding joint pressure participation to `PreviewLoadCase` would move the `s(PreviewLoadCase)` atom (`PP/src/retained_memory.rs:1777`). That is a profile re-pin conditional on Pass B, T9 and the both-entry gate, as in U3 (`RR:16494-16496@RRc`).
9. The changed solver crates need the full T3 gate set: independent review, hosted CI, DEC-025, and the fixture stop rule (I111 §5(b), `I111:55-58@RRc`).

### 1.4 Slot table for the corrected element (inference)

| Slot | Today (user element) | Corrected joint: implement, or fail closed |
|---|---|---|
| Dense and sparse assembly | `PP/src/lib.rs:3757-3770,6380-6447`; `FK/structural/sparse.rs:592` | Implement Ke = BᵀKB. `StiffnessBlock` (`FK/structural/sparse.rs:559`) is an existing generic 12×12 slot |
| K-D5 | re-formed with lateral = 0, otherwise demoted (`formation_check.rs:169-175,637-660`) | A Wide<2> B/Ke re-formation, or `unavailable`. D5C-2 forbids silence (`RR:227@RRc`), so absence demotes every joint case from Passed |
| K2b | census and `force_scaled` | Scale K, gp and the qref residual, or refuse at the F1b admission family |
| K5/W4 | a tie {Δu=0, Δθ=0} (`rigid_body.rs:344`) | Positive-definite K means the null space is rigid motion, so the joint is an objective **link**, like a frame (`NI/src/structural_adapter.rs:1436-1437`). Semidefinite K means unqualified |
| NI | `user_stiffness_elements` | A new field. The explicit `CurvedBendStiffnessElement` slot (`NI/src/lib.rs:170-216`) is fail-closed (W4 `CurvedExplicit`, strict-gap unsupported) |
| S11-G bodies | edges (`PP/src/lib.rs:1240-1246`) | Add the edge |
| Retained and source recovery | refuse (`retained_product.rs:1558`; `source_recovery.rs:579`) | Keep refusing |

## 2. Joint authoring and refusals today (Q2)

**Model fields (fact; `PP/src/lib.rs:358-475@U3`).**
- `kind:"expansion_joint"`, `node`.
- `geometry`: `expansion_joint_pipe_ref` (the finite span is the mapped pipe), `effective_area` (Quantity), `movement_limit`, `hardware_reference` (string only), `manufacturer_reference`, `pressure_thrust_reference` (string), `expansion_joint_source_reference`.
- `modifiers`: `{axial,lateral,angular,torsional}_stiffness_user_value`, `source_reference`.
- `mechanics_interface.solver_consumption`.
- `objective_connector: Option<serde_json::Value>`, untyped and reserved.
- There are no typed ties, preload or `qref`, frames, offsets, pressure participation or topology.

The schema's `solver_consumption` enumeration includes `not_solver_consumed`, which nothing implements (`P/schemas/component.schema.yaml:497-506@U3`). The TS type mirrors the legacy fields (`TS/types.ts:38-55@U3`). The PRD still lists four scalar stiffnesses and "pressure thrust" (`P/docs/PRD.md:653-664@U3`). That is a capability text for the governance-documents PR to consider.

**Refusal map (fact, @U3).**

| Case | Outcome |
|---|---|
| A component in an exact (0.3.0/0.4.0) document | `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`, blocking (`pressure_runtime.rs:171-177`) |
| `objective_connector` present | `PREVIEW_CONTRACT_VERSION_MISMATCH` in 0.1.0/0.2.0, `OBJECTIVE_CONNECTOR_VERSION_UNSUPPORTED` or `OBJECTIVE_CONNECTOR_NOT_IMPLEMENTED` (`:157-168`) |
| Consumption ≠ flexibility (including absent) | Warning `EXPANSION_JOINT_MECHANICS_INTERFACE_UNSUPPORTED` (`validation.rs:1147-1162`). Solves, with the pipe as a frame |
| Flexibility with a value missing | `JOINT_ELEMENT_STIFFNESS_INCOMPLETE` (G11; `preview_physics.rs:120-150`) |
| Flexibility with no pipe, an unknown pipe or node, or a node not on the pipe | `JOINT_ELEMENT_MAPPING_UNRESOLVED` (`:152-187`) |
| Flexibility with lateral ≠ 0 over a nonzero length | `JOINT_ELEMENT_EQUILIBRIUM_UNQUALIFIED` (`:188-209`) |
| Flexibility with lateral = 0, or any value ≤ 0 or non-finite | `EXPANSION_JOINT_MACRO_ELEMENT_INPUT_INVALID` from FK's constructor (`lib.rs:7555-7593`) |
| Joint pipe without `y_reference` | the pipe's own `PIPE_ORIENTATION_INPUT_MISSING` (`preview_physics.rs:152-157`) |

There are also warnings for missing or invalid geometry, mapping and stiffness, and the info `EXPANSION_JOINT_USER_STIFFNESS_REVIEWED` (`validation.rs:1317-1398`). Its text still cites "load-side pressure-thrust handling evidence" (`:1392`), which the RR text test applies to.

**Joint-bearing demo and fixtures after U3 (fact).**
- `invented_preview_model.json` (C-150 and legacy pressure) stays as PP's refusal fixture (`RR:16507@RRc`).
- Its refusal envelopes are the preview-physics-1 pair.
- DL removes `invented_mechanics_result.json` and the precision-1 pair. DL's `invented_demo_model.json` is joint-free and becomes the app default (`ST/lib.rs:1538-1571@DL`; `P/fixtures/product_preview/DEMO_FIXTURES.md@DL`).
- Also: `result_export_v0_2.json` (2 cases); the component libraries; the derived `PP/tests/fixtures/preview_physics_invented_model.json` (joint removed); inline joints in PP, NI, HR and OA tests (OA `lib.rs:8892-8920,13208`).

## 3. The joint reference, mapped to code (Q3)

**Specified element (fact; `JR/CONTRACT.md@Base`).**
- §2 (17-44): a symmetric-midpoint small-rotation connector.
  - `qt=Qᵀ[(vj−vi)−θc×r]` with `vk=uk+θk×ak`, and `qr=Qᵀ(θj−θi)`.
  - `Bt=Qᵀ[−I, S(ai)+S(r)/2, I, −S(aj)+S(r)/2]`, `Br=Qᵀ[0,−I,0,I]`.
  - `g=K(q−qref)`, `Ke=BᵀKB`, and the RHS `+BᵀKqref`.
  - End actions `Mi=−(ai+r/2)×F−M`, `Mj=(aj−r/2)×F+M`.
  - Explicit proper Q and distinct nodes.
  - The parameters are H=DᵀKD (21 entries) with an authored Ls.
- §3 (46-52): `replaces_span`, series or parallel topology. The replaced span is removed everywhere. Its loads need an owner or block.
- §5 (75-116): ties are `collective_centerline_axial_constraint_v1` or `explicit_axial_rods_v1` (bilateral linear or ideal), solved by exact constraint, never a penalty. `JointPressureModel`, `JointHardware` and `JointPressureParticipation`. The proposed codes are `JOINT_PRESSURE_INTERFACE_UNRESOLVED`, `…AREA_MISSING`, `JOINT_STIFFNESS_BASIS_UNSUPPORTED`, `JOINT_HARDWARE_NOT_DEFINED`, `…LAW_UNSUPPORTED` and `JOINT_REPLACED_SPAN_LOAD_UNOWNED`.
- The record shape is `ObjectiveConnectorV1` (`E/contracts/CONNECTOR_CONTRACT_V1.md:18-38,99-107@Base`). The result kinds are `connector_generalized_*_v1` and `connector_endpoint_*_v1` (`:123`).

**Slices (fact, `JR/CONTRACT.md:144-148`).**
- J-A: the primitive in FK. It "preserv[es] historical UserStiffnessElement", which the owner's M07 A supersedes (`RR:16464@RRc`).
- J-B: live topology and authoring.
- J-C: pressure and ties.

**`LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED` (fact).** `JR/CONTRACT.md:52`. Proposed in `E/contracts/CONNECTOR_CONTRACT_V1.md:9-11` (no automatic remapping; legacy data stays editable). Under it, `OBJECTIVE_CONNECTOR_NOT_IMPLEMENTED` holds until release (`:13`).

**Reference values (fact, to freeze).**
- J1 (`JR/CONTRACT.md:122`): r=.3ex and K=diag[2e5,8e4,1.2e5,600,900,1200]. With uj_y=1 mm: g_y=80 N, U=.04 J, Fi_y=−80, Fj_y=+80, Mi_z=Mj_z=−12 N·m. A common ω mode gives zero. The raw-difference mutant gives 240 N and .36 J.
- J2 (`:124`): θj_z=.01 with uj_y=1.5 mm gives qt=0, g_mz=12 and U=.06. With uj_y=0: qt_y=−1.5 mm and g_y=−120.
- J3 (`:126-136`; refutation A-D `JR/INDEPENDENT_REFUTATION.md:144-192`):
  - anchored untied: q=(800−50π)/(2e5+1.375e7π) ≈1.4815e-5 m, Tb≈2.963 N, Nw≈−404.34 N, S≈−797.04 N;
  - anchored ideal tie: Tt=800−50π≈642.92 N, Nw=75π;
  - free untied: q=.004 m, Tb=800 N, Nw=125π, S=0;
  - free tied: Tt=800 N;
  - finite rod 2e7: q=800/2.02e7 m.
- J4 and the negative controls (`CONTRACT.md:138`; refutation 194-200): a double count leaves the anchored-tie q and reactions unchanged but makes Tt=800+75π.
- B oracle: Fi=(−2,3,−5), Mi=(−42/5,87/5,−43/5), Fj, Mj (`refutation:226-233`).
- Finite rotation: qt=[L(cosφ−1), L(sinφ−φ), 0] (`:52-58`).
- The historical `E/verification/ANALYTICAL_ORACLES_V1.json` "connector" holds 13 groups (six components, coupled H 4/1/9 → .075 J, scale, offsets, reversal, PSD, topologies, mutations).

**Mapping to existing primitives.** Fact for each "nearest primitive" and for each "gap" being absent; inference for the reuse.

| Behaviour | Nearest primitive @U3 | Gap |
|---|---|---|
| B, Ke, offsets | `curved_bend` `equilibrium_transfer` and `assemble_macro_stiffness` (`P/core/solver/curved_bend/src/lib.rs:821-845`): a 6×6 law plus a rigid chord transfer. The midpoint law equals an end-referenced law with K′=AᵀKA when there are no offsets (inference). FK `transform_global_stiffness` (`FK/src/lib.rs:1278`) uses `y_reference` axes (`:525`) | a new FK primitive with explicit Q and attachment offsets. No rigid-offset or rigid-link primitive exists |
| H/Ls parameters | none | a typed parameter decoder (`CONNECTOR_CONTRACT_V1.md:93`) |
| qref residual, gp load | the FK load ledger, with F1b refusing a non-nodal term (`PP/src/lib.rs:1571`) | a new ledger term kind, plus admission and scaling |
| `replaces_span` | curved-bend chord exclusion (`PP/src/lib.rs:7209,7324,7613`) | load-ownership blocking; series and parallel |
| Ties | global-DOF restraints only (`PP/src/lib.rs:483`) | a linear MPC (elimination or a multiplier), with its W4, K-D5 and recovery treatment. Elastic rods are elements |
| Recovery and publication | curved-bend end recovery and review rows | new kinds through ROOT's registry (`JR/RETURN.md:17`), which triggers the re-registration in §1.3.2 |
| Authoring | the reserved `objective_connector` | typed serde, TS and OA (J-B) |

## 4. Pressure on joints (Q4)

**JR (fact).**
- Generalized load `gp=[pAe,0…]` with RHS `Bᵀgp`.
- `Nw=Tb+Tt−p(Ae−Ai)` at an equal-bore coaxial interface.
- (A) element pairs, selected; (B) real caps plus `[-(Pe−Pi),+(Pe−Pi)]`, the independent check. Never real caps plus a full Pe pair (`JR/CONTRACT.md:54-73@Base`).
- The first composition is equal bore, common p, straight and coaxial. The joint has no Poisson term. Ae is authored, never from the bore.
- `unpressurized` rejects nonzero participation.
- The pipe-only region schema must reject joints until it is extended (`:114`).

**The exact contract as built (fact, @U3).**
- A region is one acyclic chain of `member_pipe_ids`, with its terminals as the only degree-one nodes (`pressure_runtime.rs:1018-1042`).
- Each terminal is `transfers_to_wall` or `separately_supported_or_compensated` (`:340-344`).
- Caps go only at transferring terminals, into a separate `cap_loads` ledger. Poisson eigenloads go per member (`:1-5,453,669-760`).
- The basis label is `internal_differential_zero_external_v1` (`:23`); JR proposes `internal_increment_zero_external_v1`.
- Per-member bores may differ (test at `:1267`).

**Composition (inference).**
1. A replaced span breaks the chain. The connector must become a chain edge through `JointPressureParticipation`, never a member or a closure.
2. With today's (B) ledger, the joint contributes `p(Ae−Ai)` at its attachments, with Ai from the adjacent `SourceAnnulus` (`PP/src/lib.rs:2044`). Equality of the adjacent bores is required.
3. Adopting JR's (A) means re-owning the exact ledger per element: a contract change to verified exact pressure code.
4. Wall recovery stays the pipe law, and the cap ledger is never subtracted (`pressure_runtime.rs:3-5`). This matches JR §4.
5. Ties carry Tt as a constraint multiplier, which needs the MPC.
6. Joint thermal behaviour needs its own law (`JR/CONTRACT.md:136`).
7. J3's free and anchored cases fit as exact-contract fixtures. J4 must inspect Tt, not only the reactions.

## 5. A legacy finite-span joint (Q5)

**Recognition (fact plus inference).** A legacy joint is a `kind:"expansion_joint"` record without `objective_connector`, carrying `expansion_joint_pipe_ref` and/or the four scalar stiffnesses. There are two populations:
- (a) `solver_consumption = mechanics_geometry_and_user_flexibility`. These are refused today by the four codes in §2, which all describe the element being deleted.
- (b) no or other consumption. These solve as a rigid pipe with a warning. This is every app-authored joint.

JR says a missing consumption field "cannot silently mean a working bellows", and that a geometry-only annotation needs an "explicit non-mechanical mode with visible meaning" (`JR/CONTRACT.md:52`). Whether (b) is refused, or kept through an explicit `not_solver_consumed`, is a decision (D1).

No migration rewrites a joint, following the pressure precedent (`ST/model_document_migration.rs:17-36@U3`). All legacy fields are `Option`, so documents stay readable and saveable.

**Per route (fact for the plumbing; inference for the requirements).**

| Route | Today | Needed for `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED` |
|---|---|---|
| PP, all entries | one gate, `PP/src/lib.rs:2412` | Replace the four codes with one blocking code, refs `[component, pipe]`. Decide whether it runs before `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED` in exact documents, so the message says "re-author". Remove `EXPANSION_JOINT_MACRO_ELEMENT_INPUT_INVALID` |
| HR CLI | inherits PP | Add tests in both modes (pattern `HR/src/bin/openpipestress-runner.rs:1077-1107`). Re-pin `result_envelope_binding.rs:476-484` and `tests/preview_physics_admission.rs:249-280` |
| ST native | inherits PP. The default model is joint-free @DL | Add a native test (pattern `ST/lib.rs:6894-6916`) |
| Browser | no solve; reference-only bundled results | The message is not reached. Authoring still creates (b) joints (`componentIntent.ts`; OA `lib.rs:2401-2420,2702-2870`) |
| Authoring | none | Retire it as OA does for pressure (`OP-PRESSURE-PRIMITIVE-RETIRED`, `OA/lib.rs:4966`), or replace it with connector authoring (J-B) |
| Desktop message | generic diagnostics | An inspector notice like `TS/features/pressure-authoring/PressureAuthoringPanel.tsx:69-81` |
| Readers RS, PY, TS | rows only | Nothing: codes are free strings, and no code registry was found |
| Python service | frozen demo result @DL | No change |

**Message content (inference).** Name the component and pipe. State that a finite-span joint with four scalar rates cannot be solved and is not converted. Ask for an objective connector with explicit attachments and axes, a 6×6 work matrix with its basis, a topology, hardware and a pressure model.

## 6. Decisions for T4's plan

- **D1.** The scope of the legacy refusal: population (a) only, or (a)+(b). Under (a)+(b), the app's joint authoring must also be retired or replaced.
- **D2.** Keep the summary key and the semantic row kinds, or re-pin: 88 files, the MechanicsEnvelope atom, and re-registration of the reviewed inputs.
- **D3.** Delete the W4 tie reduction along with the element, or keep it.
- **D4.** For each slot in §1.4: implement, or fail closed.
- **D5.** Pressure ownership, (B) or (A). The chain extension. The basis label.
- **D6.** The connector container: 0.3.0/0.4.0 exact only (E/ν and lifting the component refusal), or something else.
- **D7.** Ties: build an MPC now, or start with untied plus elastic rods.
- **D8.** Which PR "lands the corrected joint": J-A or J-B (finding 7).
- **D9.** Whether NI's four friction tests take a new coupling element, and with what independent expectation.
