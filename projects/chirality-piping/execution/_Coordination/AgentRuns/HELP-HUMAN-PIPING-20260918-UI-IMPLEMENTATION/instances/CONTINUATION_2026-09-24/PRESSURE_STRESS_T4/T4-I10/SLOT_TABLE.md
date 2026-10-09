# T4-I10: T4-U3's slot table, for T3's agreement

**Role.** TASK (Type 2) for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I10_U3_SLOT_TABLE.md`; terms `R4/BRIEFS/T4_WI_COMMON.md`; WI's added T3 constraints 1–5 (2026-10-09) folded in. Read-only on code; no build or test run.

**Basis.** Every `path:line` is **@ed012c7ccf** (T3's U3 head) unless a commit is named. I3's lines (@70e7f49ced) were re-located. b2 = `e582b61f9e`; main = `ec5d397359`. Abbreviations as the common terms, plus KD = `FK/src/structural/formation_check.rs`, SD = `P/core/solver/sparse_direct`, HR = `P/core/runner/headless`, RE = `P/core/reporting/result_export`, OA = `P/core/model_operations/operation_applier`, TS = `P/apps/desktop/src`. "Fact" is read from the cited bytes; **(inf)** marks inference or proposal. Run records: `_run_records/` (site census, b2 distances, friction arithmetic).

## 0. What changes the plan, a stop rule or a T3 condition

1. **SP-1 needs a declared exception, or D-4 narrows (WI/HELP_HUMAN).** D-4's precedence ("before `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`", plan §6) puts the legacy check ahead of the exact profile's component loop (`PP/src/pressure_runtime.rs:171-178`). Removing the joint validation rows (`validation.rs:1147-1162`, `:1317-1395`) also changes the diagnostics of **every** model containing an `expansion_joint`, in every version:
   - (i) refused envelopes, v2 included. No admitted v2 case changes, because v2 refuses every component, but SP-1 says "byte-identical except p < 0";
   - (ii) 0.1.0/0.2.0 app-authored joints that solve today become refused (D-4, intended);
   - (iii) annotation joints that solve today swap a warning for the disclosure.

   All three need declaring in the byte evidence.
2. **Two committed refused envelopes regenerate (SP-4 report, 3 files).** `P/fixtures/product_preview/invented_mechanics_result_preview_physics_1_{dense,sparse}.json` gain `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED` and lose `EXPANSION_JOINT_USER_STIFFNESS_REVIEWED`; their hashes in `preview_physics_fixture_generation.json:1038,:1066` move. They carry the `LIMITATIONS` strings (unchanged bytes). No successor pin, 07n or reviewed input moves. The plan's "T4-U3 lands with no re-pin" holds only for H-4's key and row kind.
3. **Correction to I3, I5 and annex A item 3:** `P/fixtures/results/invented/result_export_v0_2.json` needs **no** re-pin. Its only joint strings are model-input `completeness` values (`producer_cases[0|3].model.components[4]`). Only the HR assertion changes.
4. **T3 condition 4 constrains the decode.** `CapturedInvocation::parse` (`PP/src/lib.rs:2258`) runs before W1 admission (`:2263`). `PreviewComponent.objective_connector` therefore stays `Option<serde_json::Value>` (`:363`). `ObjectiveConnectorV1` is decoded in the gate, never in serde. A malformed connector then gets a code, not a parse error ahead of W1.
5. **T3's T8 test pins formed pushes to `PP/lib.rs`** (`PP/tests/s11f_site_test.rs:1475-1480`). The q_ref producer must therefore live in `lib.rs`, an exception to plan §4.3 item 8, unless T3 widens T8.
6. **SA's M03 text (`SA:1539`) is published for every mixed body, curved bends included.** Correcting "user/curved" changes curved-bend outputs, and by design fails T3's K5 test `SA/k5_tests.rs:1225` ("basis text … unchanged"). T3 decides.
7. **Not every joint shape is covered by the plan's recognition rule.** A joint with no connector, no pipe ref, no rates and no annotation mode falls outside it. Proposed: the legacy code with refs `[component]` (§4.2).
8. **Two slots I3's table missed:** the DEC-050/053 observation lane and the contact-seed predicate (S3, S7). F1b admission and the replaced span's recovery are separate slots too (S9, S20).

## 1. Common design (inf; one connector type in every old slot position)

- **FK `connector` module** (`FK/src/connector.rs`; a module, not a crate, so PP's `Cargo.lock` is unchanged). `ObjectiveConnector { node_i, node_j: FrameNode, a_i, a_j, q: [[f64;3];3] (columns = axes), k: sym 6×6, q_ref: [f64;6] }`, implementing JR §2:
  - `b()` and `global_stiffness()` = BᵀKB, finite-checked like today's `global_stiffness`;
  - `reference_load()` = +BᵀKq_ref, with its bound;
  - `recover(d)` → (q, g = K(q − q_ref), Bᵀg), using `ExactAccumulator` sums;
  - `force_scaled(b)`, `formation_roundoff()`, and an exact definiteness decision.
- **Same position, same order.** It replaces `UserStiffnessElement` in each parameter, field and loop where the user element sits today, so the dense order frames → connectors → blocks → springs is kept. With no connector, every admitted model without a joint keeps today's bits: no product path assembles the old element today (I3 §1.1: G11, M07, or FK's constructor refuses it).
- **v3 only (D-4).** A connector is admitted only through T4-U2a's seam on `3.0.0/exact_pressure_v3`. Topology is `replaces_span`; `untied`; `JointPressureModel = unpressurized`.
- **The builder has no silent `continue`.** Every connector that reaches `build_model` is either formed, or refused by code.

## 2. Slot table

I = implement; FC = fail closed (code and site given).

| # | Slot | Today: the old element | Decision; where emitted | Connector treatment (JR) |
|---|---|---|---|---|
| S1 | FK element, dense assembly | `FK/src/lib.rs:623-692` (struct, `new` needs 4 positive rates), `:1287-1332` (`assemble_global_stiffness[_with_user_elements]`), `:1740-1762` (6 uncoupled relative springs). Callers: `PP/src/lib.rs:3759-3774` (n ≤ 256 replay, tests), `PP/src/source_receipt.rs:312-317`, `NI/src/lib.rs:581-585` | I. The `_with_user_elements` API is deleted; `assemble_global_stiffness_with_connectors(n, frames, connectors)`. Callers passing `&[]` move to `assemble_global_stiffness` (bit-equal wrapper today, `:1291`) | Ke = BᵀKB, with Bt = Qᵀ[−I, S(aᵢ)+S(r)/2, I, −S(aⱼ)+S(r)/2] and Br = Qᵀ[0, −I, 0, I] (§2) |
| S2 | Sparse assembly (K1) | `FK/src/structural/sparse.rs:503-553` (scaled inputs), `:592-633` (`users` slot, formed after frames). `PP/src/lib.rs:3538-3545` | I. The parameter type becomes `&[ObjectiveConnector]`: of about 30 callers, those passing `&[]` compile unchanged, and dense/sparse parity stays bitwise | as S1 |
| S3 | DEC-050/053 observation lane (missed) | `PP/src/lib.rs:6382-6450` (user loop `:6440-6450`); callers `:6135-6143`, `:6256-6264` | I. Connector Ke entries appended after the frames. Observation only; it never selects a solution | as S1 |
| S4 | SA linear evidence ("NI-linear") | `SA:39-50` (`FormationPrimitives.users`), `:62-121`, `:492-548`, `:1136-1156` (`transform_roundoff`, `qualified=false`); `PP/src/lib.rs:6100-6107` | I | Ke with its formation allowance (two-stage Bᵀ(KB) bound and counts, as curved's H·K stages); edge `qualified=false` |
| S5 | NI nonlinear loop | `NI/src/lib.rs:243` (field), `:581-606`, `:1307-1313` (test-only); `PP/src/lib.rs:5755-5758` | FC: the field becomes `connectors`; NI `validate_input` refuses a non-empty list ("…not admitted to the nonlinear support loop until T5"). PP maps it to `NONLINEAR_SUPPORT_LOOP_BLOCKED` (`PP/src/lib.rs:6740-6746`). Unreachable: the exact profile refuses nonlinear supports (`pressure_runtime.rs:179-183`) | — |
| S6 | NI strict gap | `SA:2566-2577` (`!input.user_stiffness_elements.is_empty()`) | FC: the clause reads `connectors` (unreachable after S5); for the text, see §4.5 | — |
| S7 | Contact-seed trial (missed) | `PP/src/lib.rs:4435` `permits_contact_seed_trial(&e, built.user_stiffness_elements.is_empty() && …)` | FC: `built.connectors.is_empty() && …`, so no seed trial runs with a connector. Unreachable on the exact route | — |
| S8 | K2b census, force scaling | `FK/src/lib.rs:1101-1109` (`force_scaled`: 4 rates ×2^b), `:1198-1203` (`census.user`), doc `:1122-1125`; `SA:1613-1675`, `:1685-1700`, `:1784-1803` (`ForceScalingCase.users`), `:1825-1845`, `:1850-1915`; `PP/src/lib.rs:1454-1466` | I | `force_scaled`: the 21 K entries ×2^b exactly (`force_scaled_value`; non-normal values refused); B and q_ref do not scale. Census: K entries plus the formed Ke entries (as curved). BᵀKq_ref (and T4-U5's Bᵀg_p) are ledger terms, scaled with the case force (`load_term`; RV11-N4) |
| S9 | F1b admission | `PP/src/lib.rs:1558-1559`: family `user_stiffness_element`, checked first | FC: family `objective_connector` in the same position. Emits `NUMERICAL_INTEGRITY_UNRESOLVED` "range: family not admitted under force scaling: objective_connector" (`:1806-1810`), as for curved bends | — |
| S10 | K-D5 re-formation | KD `:70` (`users`), `:169-175` (lateral ≠ 0 → unavailable), `:255-258`, `:392-399` (body edges), `:637-661` (`user_matrix`); `SA:1546-1557`, `:1693-1700` | I. `FormationSource.connectors: Vec<ObjectiveConnector>`, so `FK/src/structural.rs` needs no new export. The lateral demotion is deleted. A `WideError` is `FormationCheckUnavailable`, as today | `connector_matrix`: r, S(·), Qᵀ and BᵀKB re-formed in Wide<2> at p = 128 from binary64 (xᵢ, xⱼ, aᵢ, aⱼ, Q, K), sharing nothing with the binary64 path; connectors are body-scale edges (§2) |
| S11 | K5/W4 | FK `rigid_body.rs:329-361` (`TieRefusal`, `user_element_tie`), `:263`; docs `:253-256`, `:299-301`, `:452-453`. `SA:7`, `:1344-1381` (`W4Unqualified::UserTie`), `:1413-1447`, `:1493` | I (link rule). The producer is deleted and the reduction kept (§4.1) | PD K → `links`: null(BᵀKB) = null(B) = the pair's 6 rigid modes (§2, "q=0 exactly"; rank B = 6). PSD → `W4Unqualified::ConnectorSemidefinite`, passed to the matrix gate. PD is decided exactly and libm-free (K5 Q4(b)); "PSD within the decoder's tolerance" is not PD |
| S12 | S11-G bodies, edges | `PP/src/lib.rs:1225-1251` (user edges `:1243-1248`); doc `formation_guard.rs:82-84` | I. Connector edge (nodeᵢ, nodeⱼ); the replaced pipe's edge is dropped (same pair, so the bodies are unchanged) | — |
| S13 | S11-G load row: q_ref term (new) | none | I. `add_connector_reference_loads` in `PP/lib.rs` (§0.5): `push_formed` per nonzero DOF, `Formation::Bounded` (a γ-count bound on \|B\|ᵀ\|K\|\|q_ref\|, rounded up), `self_equilibrated = true`. Stress-free (Kq_ref = 0) gives no terms | +BᵀKq_ref (§2; CONNECTOR_CONTRACT §3) |
| S14 | S11-G recovery R-b′ | `formation_guard.rs:332-340`: `RecoveryRecord` (straight ends only; priced) | Connector rows not covered, as curved (entity rule 2b); `RecoveryRecord` layout unchanged. T3 to agree | g = K(Bd − q_ref) and Bᵀg in FK with `ExactAccumulator` (S11-V1, E-sites) |
| S15 | S11 site tables | `FK/tests/s11_site_table.rs:194` (`add_relative_dof_stiffness`, 4); `PP/tests/s11f_site_test.rs:511` | I. FK: row removed; `FK/connector.rs` added to `SOURCES` with its rows. PP: the three hunks of §4.4 | — |
| S16 | Retained (W1) | `retained_memory.rs:755-756`, `:801-802` (`F::Components`), at `PP/src/lib.rs:2263`, before any joint code. Capture check `retained_product.rs:1557-1570` | FC (until T3-F2b): W1 refuses every component model. The refusal is private and the ordinary route publishes. The capture check keeps "unsupported producer present" with `built.connectors` (1 line, §4.4) | — |
| S17 | Source recovery | `source_recovery.rs:579-586` ("component, curved, user-matrix or release source family"); `source_receipt.rs:312-317` replay; `source_receipt/source.rs:376` `"user_elements":[]` | FC (until T3-F2b): the components clause already covers connectors. A Sensitive connector case publishes info `SOURCE_BLOCK_RECOVERY_UNAVAILABLE` (`PP/src/lib.rs:4384`). Text unchanged. The replay assembles connectors faithfully (unreachable). The payload key is unchanged (published payload bytes; a B7 candidate) | — |
| S18 | PP builder and gate | Gate `PP/src/lib.rs:2412-2417` → `preview_physics.rs:106-213` (3 codes). Builder `:7337-7338`, `:7482-7593` (14 `continue`s: 1 consumption filter, 13 silent skips; `EXPANSION_JOINT_MACRO_ELEMENT_INPUT_INVALID` `:7578-7593`); `BuiltModel.user_stiffness_elements` `:2050`. Exact loop `pressure_runtime.rs:157-178` | Legacy: FC (§4.2). Connector: I, through the seam. The gate moves into `validate_profile` and emits blocking codes only (it is re-called per case at `pressure_runtime.rs:434`). `BuiltModel.connectors` | decode → typed record; `replaces_span` excludes the pipe from `frame_elements`, as curved does (`:7211`, `:7326`) (§3) |
| S19 | Validation and review rows | `validation.rs:1147-1162`, `:1317-1395` (6 warnings, 1 info); count `PP/src/lib.rs:2779-2781`; producer `:11906-12005` | User review producer and joint rows deleted. The H-4 key stays and counts curved rows only. New info `EXPANSION_JOINT_ANNOTATION_ONLY` from `validation.rs` (emitted once) | Connector rows `connector_generalized_{translation,rotation,force,moment}_v1` and `connector_endpoint_{force,moment}_v1`, in T4-U2a's new `pressure-1` table only (JR §7) |
| S20 | Replaced-span recovery and loads (missed) | Straight recovery loops over `built.pipes` (skip pattern `macro_bend.is_none()`, `PP/src/lib.rs:4933`, `:5060`, `:5236`, `:5359`) | I. The replaced pipe produces no member rows, maxima, `RecoveryRecord` or self-weight. Any owned load, thermal, self-weight or station support → `JOINT_REPLACED_SPAN_LOAD_UNOWNED` | §3 |

## 3. Tests

**T3-owned (annex A and I5 §1.2, re-located).** D = delete, R = rewrite, M = mechanical.

| File | Test or helper | Action |
|---|---|---|
| `FK/tests/k5_constrained_bodies.rs` | `:943` K5-C `k5_c_user_tie_rule`; `:992` T4 tripwire; helper `:920` | D (the tripwire fires by design, `:988-990`) |
| | `:895` B10 (list `:904-912`) | R: drop `user_element_tie`, scan the definiteness function (question 4) |
| `FK/src/structural/formation_check_tests.rs` | `:69` (user part `:73-81`, `:128`) | R: `connector_matrix` with offsets, skew Q and coupled K, rigid null to p |
| `FK/tests/k2b_force_scaling.rs` | `:159`, `:288` (`:314`, `:323`), `:536`, `:583` | R (connector) |
| `FK/src/structural/sparse/tests.rs` | helpers `:93`, `:107`, `:129`, `:198`, `:238`; `:409` | R (connector parity and refusals) |
| `FK/tests/k1_k2a_interaction.rs` | `:21`, `:83` | M |
| `FK/tests/s11_site_table.rs` | `:194` and `SOURCES` | R (§4.4) |
| `SA/k5_tests.rs` | `:937`; helper `:233` | D |
| | `:506`, `:1106`, `:1225` (`:1226` if the text changes) | R: drop the joint case; add PD-link and PSD-unqualified cases |
| `SA/kd5_tests.rs` | `:631` (helper `:569`) | D. Add: a connector case not demoted at ordinary and UTM coordinates; a perturbed Ke demotes |
| `SA/k1_tests.rs` | `:816`, `:979`, `:1032`, `:1490`; helpers `:60-142`, `:477`, `:941`, `:1178` | M |
| `SA/k2b_tests.rs` | `:264`, `:1403` | M |
| `NI/src/s11k_tests.rs` | `:14`, `:861`, `:1264`, `:1354` | M |
| SD `src/structural/k1_tests.rs` | helpers `:30-312` | M |
| `PP/src/f1b_tests.rs` | `:2227` | R: family `objective_connector` from a v3 build |
| | helpers `:334`, `:365`, `:571`, `:909`, `:1586`, `:2012` | M |
| `PP/src/s11g_tests.rs` | `:2604` (`:2609-2612`) | M |
| `PP/src/source_receipt/tests.rs` | `:24` | M |
| `PP/tests/s11f_site_test.rs` | §4.4 | R |
| `PP/src/lib.rs` | U3's `:17393`, `:17409`, `:17471`, `:17543` | R to the legacy code. The tuples keep their shape, e.g. "no pipe" → refs `[C-150]`. `:17543` now sees the legacy code, because the gate blocks before the pipe build |
| `PP/src/retained_product_tests.rs` | `:2435` | unchanged (H-4) |

**Others.**
- **Deleted or rewritten:**
  - FK unit tests `FK/src/lib.rs:2110`, `:2129` (D).
  - `PP/tests/preview_physics_runtime.rs:1045`: R to legacy in both modes. Its lateral-0 and zero-length "not refused" boundaries become legacy refusals (D-4 has no stiffness exemption).
  - NI friction tests (§4.6).
  - NI fixtures `NI/src/lib.rs:3131`, `:3205`, `:3675`, `:3727`, `:5441` and tests `:3848`, `:4140`, `:4984` (M).
  - SA inline `:2978`, `:3030`, `:3166` (M).
  - HR `src/result_envelope_binding.rs:448-452` (widen `realized_joint_ids` to the legacy rule) and `:480`; HR `tests/preview_physics_admission.rs:276`.
  - Harness `k6/staged.rs:289`; `P/validation/benchmarks/nonlinear/src/lib.rs:1794-2034` (7) (M).
  - TS and OA authoring tests (J-B).
- **Added:**
  - FK connector tests (JR: J1, J2, the B oracle, 6 rigid modes, offsets, q_ref and preload, coupled H, reversal, the finite-rotation negative control, PSD/PD, exact `force_scaled`).
  - PP: legacy refusal for both populations, the residual shape, annotation not refused but disclosed, the v2 precedence, connector J1/J2 through PP, `JOINT_PRESSURE_INTERFACE_UNRESOLVED`, `JOINT_REPLACED_SPAN_LOAD_UNOWNED`, the replaced span absent from assembly and recovery, the S11-G edge, F1b, and the invented demo joint re-authored on v3 balancing (formerly 658.44 N·m).
  - HR in both modes; native ST.

## 4. Items 1–7

### 4.1 W4

T3's reduction stays: `assess_constrained_bodies` and `reduce_constrained_body` are untouched. Deleted: `user_element_tie`, `TieRefusal` and SA's `UserTie`. SA passes `&[]` ties. The K5 changes:
- **K5-C:** D.
- **T4 tripwire:** D; its successor is the PD-link proof in FK connector tests (rank B = 6, B·rigid = 0 in exact rationals).
- **B10:** list edit.
- **NI joint cases:** dropped, with connector cases added.

The FK K5 vector corpora (`k5_constrained/*`, `k5_scale.rs`) do not change.

### 4.2 No joint silently skipped (T3 item 6; WI constraint 1)

Every `expansion_joint` is classified, in this order, by one function called first in `validate_profile`.

| Shape | Outcome |
|---|---|
| `objective_connector` in a 0.1.0/0.2.0 document | `PREVIEW_CONTRACT_VERSION_MISMATCH` (existing, `pressure_runtime.rs:160-161`) |
| connector, version ≠ 1.0.0 | `OBJECTIVE_CONNECTOR_VERSION_UNSUPPORTED` (existing) |
| connector in a v2 document | `OBJECTIVE_CONNECTOR_NOT_IMPLEMENTED` + `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED` (the v2 codes are unchanged; the joint warnings go, §0.1) |
| v3 connector: a required field missing or invalid (nodes, Q not proper, offsets, H not PSD, Ls, provenance, reference state), or legacy fields alongside it | `OBJECTIVE_CONNECTOR_INPUT_INCOMPLETE` (new) |
| v3 connector: unknown or equal end nodes; `replaces_span` naming no pipe, a mismatched pair, a curved span, or a span already replaced; series or parallel topology | `OBJECTIVE_CONNECTOR_TOPOLOGY_UNRESOLVED` (new) |
| v3 connector: calibration basis / hardware absent / hardware ≠ untied | `JOINT_STIFFNESS_BASIS_UNSUPPORTED` / `JOINT_HARDWARE_NOT_DEFINED` / `JOINT_HARDWARE_LAW_UNSUPPORTED` (JR §5) |
| v3 connector: pressure model ≠ unpressurized, **or any case with non-empty `pressure_regions`** (presence is the inventory) | `JOINT_PRESSURE_INTERFACE_UNRESOLVED`, until T4-U5 |
| v3 connector whose replaced span owns a load, thermal or self-weight, or a station support | `JOINT_REPLACED_SPAN_LOAD_UNOWNED` |
| valid v3 connector | **admitted**, then S1–S20. An FK constructor refusal in the builder gives `OBJECTIVE_CONNECTOR_INPUT_INCOMPLETE` |
| no connector, `solver_consumption = not_solver_consumed` | **admitted as annotation**: analysed as pipe, with info `EXPANSION_JOINT_ANNOTATION_ONLY` on every result. In v2 still `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED` |
| no connector, carries `expansion_joint_pipe_ref` and/or any of the 4 rates; any other consumption, or none (D-4 populations a and b; app joints carry both, `componentIntent.ts:341-394`) | **`LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED`**, blocking, refs `[component, pipe]` (pipe omitted if there is no ref); first in the list, every version, and the exact loop skips that component |
| no connector, no pipe ref, no rates, not annotation (residual) | the same code, refs `[component]` (inf; to agree) |
| `objective_connector` on another kind | the existing three codes |

**Old → successor.**
- `JOINT_ELEMENT_STIFFNESS_INCOMPLETE` (`preview_physics.rs:145`) → legacy / `OBJECTIVE_CONNECTOR_INPUT_INCOMPLETE`.
- `JOINT_ELEMENT_MAPPING_UNRESOLVED` (`:181`) → legacy / `OBJECTIVE_CONNECTOR_TOPOLOGY_UNRESOLVED`.
- `JOINT_ELEMENT_EQUILIBRIUM_UNQUALIFIED` (`:207`) → legacy (a connector is objective by construction).
- `EXPANSION_JOINT_MACRO_ELEMENT_INPUT_INVALID` (`PP/src/lib.rs:7588`) → legacy / `OBJECTIVE_CONNECTOR_INPUT_INCOMPLETE`.
- `EXPANSION_JOINT_MECHANICS_INTERFACE_UNSUPPORTED` (a warning) → legacy (blocking) / `…ANNOTATION_ONLY` (info).
- The other five `EXPANSION_JOINT_*` warnings and the `…USER_STIFFNESS_REVIEWED` info → removed.

**Backstops behind the gate:**
- S5 → `NONLINEAR_SUPPORT_LOOP_BLOCKED`;
- S9 → `NUMERICAL_INTEGRITY_UNRESOLVED`;
- S10 → Sensitive (unavailable);
- S16 → W1 `F::Components`;
- S17 → `SOURCE_BLOCK_RECOVERY_UNAVAILABLE`.

No path drops a joint.

### 4.3 What must not change (T3's conditions; WI constraints 4–5)

- **PP `Cargo.lock`:** FK `connector` is a module; no crate is added.
- **Priced layouts:** `MemberRecord`, `RecoveryRecord`, `Preview{LoadCase,Node,Pipe,Support,PrimitiveLoad}`, `MechanicsEnvelope`/`Summary`, `ResultItem`, `Diagnostic`, `FrameElement`, `FrameNode`: none edited.
  - Connector data stays on `PreviewComponent`, which is unpriced (raw `Value`), and on the typed record and `BuiltModel.connectors` (unpriced; `BuiltModel` is priced by reference only).
  - `replaces_span` never goes on `PreviewPipe`.
  - No new `Summary` count.
- **`preview_physics::LIMITATIONS` (`:73-81`):** untouched. T4-U3 deletes `:106-213` in the same file. Connectors never publish on preview-physics-1.
- **`REVIEWED_INPUTS` (`build_identity.rs:148-163`; 17 at b2):** no file T4-U3 edits is listed. Connector kinds go only in T4-U2a's new `pressure-1` table (question 9). The readers' retired-code lists are **not** extended: historical results carry `JOINT_ELEMENT_*`.
- **`REGISTERED_PROFILES`:** unchanged, by the layout list above.
- **H-4:** the key stays (`PP/src/lib.rs:2779-2781` keeps the curved term; the blocked literal `:13320` is unchanged). The row kind stays readable in `previewService.ts:340`, `ReportPanel.tsx:334`, `:405`, `retainedPrecision.ts:110`, `RE/src/retained_precision.rs:2500`, `records.py:477-480` and `retained_precision.py:1150`. PP stops producing it.
- **W1 first (WI constraint 4):** nothing is added to the census, to `parse` or to `retained_memory.rs`. The gate runs in `run_linear_static_preview_observed` (`PP/src/lib.rs:2365`), after admission (`:2263`).

### 4.4 Overlap with b2 (`_run_records/b2_overlap.*`; distances in unchanged main lines)

| File | b2 | T4-U3 | Gap |
|---|---|---|---|
| `PP/src/lib.rs` | 13 hunks, main 2207–3455 (W1 dispatch) | ~21 sites; the nearest is `:3541` (main 3572) | ≥ 116. Place new `lib.rs` code outside @ed012c7ccf ≈ 2170–3430, e.g. the producer next to `push_exact_pressure_operands` (`:3897`) |
| `PP/src/retained_product.rs` | insert after main 1554 | **one hunk, `:1558`** (main 1560): `-  \|\| !built.user_stiffness_elements.is_empty()` / `+  \|\| !built.connectors.is_empty()` | **5** (merge-clean). Alternative: T3 adds a `BuiltModel` predicate in its next edit there |
| `PP/tests/s11f_site_test.rs` | insert after main 549 (@ed `:543`) | (a) PRODUCERS: insert after `:221`; (b) TABLE: replace row `:511` with `("PP/lib.rs", "add_connector_reference_loads", 0, "producer")`; (c) FORMATION_SITES: insert after `:1382` (`Formation::Bounded`, `Some(&["true"])`) | 324 / **36** / 847 |
| `PP/src/retained_product_tests.rs` | after main 2438 | none (H-4) | — |
| `RE/tests/preview_physics_contract.rs` | after main 830 | `:606` is a hand-built control; leave it (optional re-pin, gap 224) | — |
| `TS/services/previewService.ts`, `FK/src/structural.rs`, `retainedPrecision.ts` | b2 hunks | none | — |

No new PP module that pushes or folds, so `PRODUCT` (`s11f:42-87`) is unchanged. T4-U3 must re-merge against b2's actual diffs before landing (T3's claim 4).

### 4.5 Published texts (corrected under the published-text rule; none is pinned in a fixture at the basis)

| Text | Published | Pin | Proposal |
|---|---|---|---|
| `NI/src/lib.rs:1110`, `:1111`, `:1120` | NI result; HR diagnostics `NONLINEAR_ASSEMBLED_LOOP_{ASSUMPTION,LIMITATION}` (`HR/src/result_envelope_binding.rs:304-323`) whenever nonlinear supports run | historical REPRO only | `:1110` → "Objective connectors are not assembled by this loop; a model containing one is refused (T5)." `:1111` drops "and user-stiffness". `:1120` drops "User-stiffness and" |
| `SA:1539` M03 family text | every mixed (curved) body | `SA/k5_tests.rs:1226` (T3) | "…bodies containing curved elements or connectors…" (question 3) |
| `SA:2577` strict-gap reason | gap models on the pressure-free route | `NI/src/lib.rs:4780`, `:4922` (substring) | "mixed/curved/connector/affine" (question 3) |
| `source_recovery.rs:584` | info `SOURCE_BLOCK_RECOVERY_UNAVAILABLE` | none | unchanged |
| Joint validation `validation.rs:1159`, `:1326`, `:1338`, `:1350`, `:1362`, `:1374`, `:1392`; gate `preview_physics.rs:147`, `:183`, `:209`; review metadata `PP/src/lib.rs:11990`, `:11997` | refused envelopes; the review rows are never produced today | the two envelopes of §0.2 | deleted. New texts: the legacy message (plan §6) and the annotation disclosure |

**Docs:** `NI/README.md:11`, `CB/README.md:6`, and FK, PP and SA doc comments (S8, S10–S12).

**Re-pins outside T3's corpora:** HR `result_envelope_binding.rs:480` (with its predicate) and `tests/preview_physics_admission.rs:276`; the two envelopes plus the manifest (§0.2). Not `result_export_v0_2.json` (§0.3).

### 4.6 NI's four friction tests (plan §4.3 item 7)

**Fact.** The fixture `coupled_normal_friction_problem` (`NI/src/lib.rs:3580-3614`) feeds 4 call sites in 3 tests: `:3770` (`:3759`), `:3907` and `:3955` (`:3900`), `:4251` (`:4245`).

**What they pin.** Only node 1's translational block on the free Ux and the reacting Uy (Rx, Ry and Rz are restrained): k_a eeᵀ + k_l(I − eeᵀ), giving Kxx = 150 and Kxy = −50. `friction_basis.py` reproduces `:3761-3762` exactly in rationals.

**Replacement (inf).** An ordinary `FrameElement` on an off-axis chord, whose block is (EA/L)eeᵀ + (12EI_z/L³)(I − eeᵀ), with EA/L ≠ 12EI_z/L³ so the normal stays affine-coupled. Rational cosines, e.g. (3,4,0) with L = 5, keep the arithmetic exact. Same structure: sign flips, the zero coefficient and the cap.

**Expectations** are re-derived by a separate reference TASK in `fractions` from the frame's own section, frozen and then refuted, and are never read from the product. The script's frame values are illustrative only. Tolerance stays 1e-12.

### 4.7 Commit plan (each commit compiles; every joint is refused or solved)

1. **Legacy gate.** The joint classifier in `validate_profile`, where the exact loop skips refused joints; annotation disclosure; `refuse_unqualified_joint_elements` and the validation rows deleted. Re-pin U3's four tests, `preview_physics_runtime.rs:1045` and the HR tests; regenerate the two envelopes and the manifest. *Every joint except an annotation is now refused. The old builder is unreachable but compiles.*
2. **FK `connector` (J-A)**, with its unit tests. No consumer.
3. **Slot swap**, one mechanical commit, because FK API changes break dependants:
   - `UserStiffnessElement` → `ObjectiveConnector` in FK, SD, SA, NI, the harness, the benchmarks and the PP call sites (S1–S9, S12, S16–S17);
   - `BuiltModel.connectors` (empty);
   - connectors **fail closed** in W4 (unqualified) and K-D5 (unavailable);
   - NI refusal; F1b family;
   - delete the element, its census, `user_element_tie`, `TieRefusal`, `UserTie` and `add_relative_dof_stiffness`;
   - the user review-row producer deleted;
   - T3 tests D/R/M; friction tests; `retained_product.rs`; s11f row `:511` removed.
4. **K-D5 re-formation and the W4 link rule** (S10, S11), with their tests.
5. **PP live path (J-B):**
   - decode, seam admission, the connector codes and pressure refusal;
   - `replaces_span` (S20);
   - builder, producer and s11f (a)–(c), with (b)'s row taking `:511`'s place;
   - recovery rows, `pressure-1` kinds and the three readers;
   - J tests through PP.
6. **Published texts (§4.5)**, with declared byte evidence.
7. **Authoring:** OA/TS connector creation on v3; legacy creation retired; annotation only on 0.1.0/0.2.0; schema; desktop notice; e2e. Then docs and READMEs.
