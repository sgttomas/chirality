# T4-I11: T4-U2's desktop authoring design (M02 minimal)

TASK T4-I11 (Type 2), for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I11_U2_AUTHORING_DESIGN.md` (`a2b2f404…`), terms `R4/BRIEFS/T4_WI_COMMON.md` (`7d44afd0…`). Design only: no tracked file changed, no cargo run.

- **Citations** are `path:line@ed012c7ccf`, abbreviated `@B`. Aliases: `AP` = `P/core/model_operations/operation_applier/src`, `DT` = `P/apps/desktop/src`, `ST` = `P/apps/desktop/src-tauri/src`; `P`, `PP`, `CB` as in the terms.
- **F** = fact read from the cited bytes; **I** = inference or proposal. Numbers marked "probe" come from `_run_records/tangency_probe.py` (standard-library emulation, not a product run).

## 0. Facts that shape the design

1. **No operation writes `mechanics_interface`** (F). Bend creation canonicalizes geometry only, with no `modifiers` or `mechanics_interface` (`AP/lib.rs:2420-2438,2521-2587@B`). Editable component paths include `modifiers.flexibility_factor_user_value.value` (`AP/lib.rs:672-678@B`), so k can already be set, but realization cannot.
2. **Existing geometry-only bends are corner markers, not arc spans** (F). The desktop sets `bend_pipe_ref` to the first straight incident at the node (`DT/features/component-creation/componentIntent.ts:68,115,159@B`). The demo marker `component:C-110` has no `bend_pipe_ref` (`P/fixtures/product_preview/invented_demo_model.json@B`). **I:** marking such a bend realized in place would turn a whole straight into an arc. PP refuses that only through the optional angle check (`PP/src/lib.rs:7792-7811@B`). Realizing a marker therefore needs tangent points.
3. **The arc's plane and side come from the span's `y_reference`** (F). The arc bows toward +`y_reference` projected off the chord (`PP/src/lib.rs:7817-7845@B`). `bend_plane_orientation` is read only by a warning condition (`PP/src/validation.rs:1560-1576@B`), the applier's creation check (`AP/lib.rs:2547-2559@B`) and the desktop's draft validity (`componentIntent.ts:186-194@B`).
4. **Tangency is only warned about, at 1e-6 rad, and only on preview-physics-1** (F; `PP/src/preview_physics.rs:502-546,812@B`). The exact route refuses every component (`PP/src/pressure_runtime.rs:171-177@B`). Its region check is a 64ε representation guard (`:27,1076-1111@B`).
5. **Pressure authoring is v2-only** (F). `pressure_profile` accepts only 0.3.0 with `2.0.0/exact_straight_pressure_v2` (`AP/pressure_authoring.rs:268-276@B`), and is locked on 0.4.0 (`:235-242`). Regions refuse p < 0 under every profile (`:165-167`). Six desktop and applier sites test `mode === "exact_straight_pressure_v2"` to mean "exact" (§6).
6. **The region member picker already lists every pipe** (F; `DT/features/pressure-authoring/PressureAuthoringPanel.tsx:110,130@B`). The text says "The solver checks continuity, straightness…" (`:127`).
7. **The browser cannot solve an edited model** (F; `DT/services/previewService.ts:50-56,739-744@B`). The applier runs natively and as wasm (`DT/services/wasmEngine/loadWasmEngine.ts@B`). The shared contract corpus runs every case through both (`DT/services/operationContractCorpus.test.ts@B`; `P/fixtures/model_operations/contract_corpus/`). So e2e can exercise authoring, save and reopen, but not the solve.
8. **Intents carry `author_type: "user" | "agent"`** (F; `DT/types.ts:884@B`). The applier never reads it (F, grep). "Agents never populate k" is not enforced today.

## 1. User flows

**F1. New document with a pressure profile.** Blank model (0.2.0) → Load cases → Pressure mechanics profile → choose `exact_pressure_v3` (the only offered choice) → Queue → Review/Apply. The document becomes 0.3.0 with `{version:"3.0.0", mode:"exact_pressure_v3"}`. A blank 0.4.0 document is created with v3 once 0.4.0 under v3 is admitted (§6 C). An existing v2 document opens unchanged and shows "2.0.0/exact_straight_pressure_v2 (straight pipe only; still solvable)". Re-selecting the profile upgrades it to v3 explicitly; nothing migrates.

**F2. Create a bend at a corner** (the L line). Author nodes A, C, B and pipes A–C and C–B as today. Select C → Geometry tools → **Insert bend at corner**. Enter R with unit, k, the source of k and labels (ids pre-proposed, as split does). Queue, then Review/Apply. The diff shows T1 and T2 created, both pipes shortened, arc pipe T1–T2 created, node C removed, and bend component created realized. Tangency holds by construction (§3).

**F3. Realize an existing bend.** Select the bend → Inspector → **Bend realization**:
- **Span bend** (its `bend_pipe_ref` is a true arc chord): enter k and its source → Queue *Realize bend*. The validation preview lists each end's measured kink before queuing.
- **Corner marker** (no span, or a span that is an incident straight): the form says so and offers *Insert bend at corner*, prefilled with the marker's R and k. The operation converts the marker in place: it keeps the id, label, SIF, source, provenance and rule-check consumption.

**F4. Enter k.** k is required on realization. It is blank unless the user's own value already exists, and no value is suggested. The hint reads: "k multiplies the bend's bending flexibility; k = 1 means no extra flexibility beyond the curved beam." Agents never populate k: the applier refuses agent-authored k writes (§2 O5). k remains editable afterwards through the existing inspector field.

**F5. Add the bend to a pressure region.** Load case → Pressure regions:
- members A–T1, T1–T2 (labelled "realized bend C-n, k = …") and T2–B;
- terminals A and B, `transfers_to_wall`;
- p, with a sign hint per profile.

Queue, then Review/Apply. Before solving, the operation outcome warns about any geometry-only bend span among the members.

**F6. Solve and inspect.** Solve (native) in sparse or dense mode. The Results panel shows the `pressure-1` rows through the generic table path (reader scope, T4-U2): N_w, S and membrane stress on the straights and at the arc stations in the tangent frame; hoop and radial rows withheld on arcs with their named reason; the case maximum withheld for cases with bends (until T4-U4); the D-3 limits in the limitations; the standing.

**F7. Save, reopen, export.** Save → close → Open: the model bytes are unchanged and open as current with no migration (`ST/model_document_migration.rs:137-152@B` and its 0.4.0 branch; neither reads `pressure_contract`). Solve again → Export result JSON → the RS and PY readers accept it.

**What the user sees on refusal.**

| Situation | Before solve (authoring) | At solve (PP, proposed v3 code; final names belong to T4-U2a/U2) |
|---|---|---|
| Geometry-only bend anywhere in a v3 model (D-2) | Inspector banner on the bend: "Geometry-only bend: analysed as a straight chord with no flexibility. The exact pressure contract refuses it. Realize this bend." Region editor label "geometry-only bend span: realize first", plus applier warning `OP-PRESSURE-REGION-BEND-NOT-REALIZED` | Blocking `EXACT_PRESSURE_BEND_NOT_REALIZED`, refs `[component, pipe?]`: "bend {c} is geometry-only (a straight chord with no flexibility); 3.0.0/exact_pressure_v3 admits realized curved bends only: realize this bend and enter its flexibility factor k (k = 1 means no extra flexibility). A corner marker needs tangent points: use Insert bend at corner." Under v2 every component keeps today's `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED` (SP-1); the panel adds "v2 is straight-only; select exact_pressure_v3 and realize the bend". |
| Kink above the tangency tolerance | Realize: blocking `OP-BEND-TANGENCY-EXCEEDED` at single-neighbour ends; warning at multi-neighbour ends. Corner insertion cannot produce one. | In a region, at a bend-adjacent junction: blocking `PRESSURE_REGION_MITRE_UNSUPPORTED`, refs `[region, node, pipe_in, pipe_out]`: "members {a} and {b} meet at {n} with a direction change of {θ} rad ({θ°}), above the 1e-3 rad tangency tolerance; a kink this large is a mitre, which this contract does not yet model. Make the bend tangent (Insert bend at corner places tangent points exactly) or end the region at {n}." A kink between two straights keeps `PRESSURE_REGION_NONCOLLINEAR` (§3). |
| p < 0 under v2 | Applier refuses the region (`OP-PRESSURE-PAYLOAD-INVALID`) with the message "2.0.0/exact_straight_pressure_v2 requires p ≥ 0; signed pressure needs 3.0.0/exact_pressure_v3, which does not assess external-pressure stability or collapse". Field hint "p ≥ 0 under v2". | A hand-edited document gets T4-U0's named v2 refusal. Under v3, p < 0 is admitted, with the stated limitation. |

## 2. Data writes and operations

**O1. Realize bend (new rich edit).**
- Intent: `("Component", "bend_realization")`, change kind `set_field`. Added to the rich-kind table (`AP/lib.rs:1210-1218@B`) through a new resolver `AP/bend_authoring.rs`, on the same pattern as `pressure_authoring` (`AP/pressure_authoring.rs:130-137,212-316@B`).
- `before`: the canonical projection `{solver_consumption, flexibility_factor_user_value, source_reference}`, or `not_present`.
- `after`: `{solver_consumption: "curved_bend_macro_element" | "mechanics_geometry_only", flexibility_factor_user_value: {value, unit: "none"}, source_reference}`.

| Path written | Value | Validation |
|---|---|---|
| `mechanics_interface.solver_consumption` | `curved_bend_macro_element` (or back to `mechanics_geometry_only`) | Target is a `bend`/`elbow`. `rule_check_consumption` is untouched. |
| `modifiers.flexibility_factor_user_value` | `{value: k, unit: "none"}` | Finite and > 0, the same rule PP enforces (`PP/src/lib.rs:7709-7735@B`). The author must be `user`. No threshold of the applier's own. |
| `modifiers.source_reference` | user text, written only if changed | Required when absent |
| read only: `geometry.bend_pipe_ref`, `bend_radius`, `bend_angle`, the span's nodes and `y_reference` | — | The span exists and the node is one of its ends. R > c/2. `y_reference` is not parallel to the chord. An authored angle agrees under PP's 1e-6 rule. Tangency, §3. |

Refusals (blocking unless marked):
- `OP-BEND-REALIZE-TARGET-INVALID`: not a bend.
- `OP-BEND-REALIZE-SPAN-MISSING`: span absent or unknown, or the node is not one of its ends.
- `OP-BEND-REALIZE-CORNER-MARKER`: no span, or R ≤ c/2. The message points to Insert bend at corner.
- `OP-BEND-GEOMETRY-INCONSISTENT`: angle mismatch, or plane undefined.
- `OP-BEND-TANGENCY-EXCEEDED`: blocking at a single-neighbour end; a warning at an end with two or more neighbours.
- `OP-BEND-FLEXIBILITY-USER-ENTRY-REQUIRED`: k missing, non-positive or non-finite, or `author_type ≠ user`.
- Existing `OP-BEFORE-VALUE-MISMATCH` and `OP-RICH-KIND-INVALID`.

Returning a bend to geometry-only skips the geometry checks.

**O2. Insert bend at corner (new compound geometry operation).** Change kind `insert_bend_at_corner`, operation kind `modify`, target `{Node, C}`. It needs the complete model hash, as split does (`AP/lib.rs:1186-1203@B`). It goes into `check_kinds` (`:2176-2257`), into a new `AP/bend_corner.rs` called from `geometry_operations::resolve_geometry` (`AP/geometry_operations.rs:654@B`), and into the TS union (`DT/types.ts:892-919@B`).
- `before`: the canonical corner context (C, both pipes, any marker).
- `after`: `{radius:{value,unit}, flexibility_factor:{value,unit:"none"}, flexibility_source_reference, new_nodes:[{id,label,provenance}×2], new_pipe:{id,label,provenance}, component:{id,label,provenance,geometry_source_reference} | {convert: <marker id>}}`.

Arithmetic (I; square roots only, in project length units, R converted through the existing catalog `AP/geometry_operations.rs:91@B`):
- `u_in = (C−X_in)/|·|`, `u_out = (X_out−C)/|·|`;
- `L_t = R·|u_in×u_out|/(1+u_in·u_out)`, which is R·tan(Φ/2);
- `T1 = C − L_t·u_in`, `T2 = C + L_t·u_out`.

| Write | Value |
|---|---|
| `nodes` | T1 and T2 created (the user's id, label and provenance); C removed |
| `pipe_segments` | The incoming pipe's C end becomes T1 and the outgoing pipe's becomes T2; ids, sections, materials and `y_reference` unchanged. New arc pipe T1→T2 copies the shared `section` and `material`, with `y_reference = u_in`, which projects to the corner-side normal (probe: within 1.2e-14 of the analytic direction). |
| `components` (new or converted) | `kind: bend`, `node: T1`, `geometry.bend_pipe_ref: arc`, `geometry.bend_radius: {R, user unit}`, `geometry.bend_geometry_source_reference`, `modifiers.flexibility_factor_user_value`, `modifiers.source_reference`, `mechanics_interface.solver_consumption: curved_bend_macro_element`. A converted marker keeps its other fields; its `bend_angle` must agree with Φ under PP's rule. |

Refusals:
- `OP-BEND-CORNER-NODE-INVALID`: C does not have exactly two incident pipes, or one of them is already a bend span.
- `OP-BEND-CORNER-ANGLE-INVALID`: Φ ≤ the tangency tolerance (collinear), or Φ ≥ π.
- `OP-BEND-CORNER-RADIUS-INVALID`: `L_t` ≥ either straight's length. The message gives the largest admissible R.
- `OP-BEND-CORNER-SECTION-MISMATCH`: the two pipes' `section` or `material` differ.
- `OP-BEND-CORNER-ATTACHMENT-UNSUPPORTED`: any reference to C, or to either pipe, in supports, loads, pressure regions, wind lists or other components. This is split's rule (`AP/geometry_operations.rs:249-314@B`); nothing is repartitioned and membership is never inferred.
- `OP-BEND-CORNER-ANGLE-CONFLICT`: a converted marker's angle disagrees.
- `OP-BEND-FLEXIBILITY-USER-ENTRY-REQUIRED`.
- Existing `OP-GEOMETRY-MODEL-HASH-REQUIRED`, `OP-TARGET-ALREADY-EXISTS` and the `OP-UNIT-*` codes.

**O3. `pressure_profile` (extended; `AP/pressure_authoring.rs:231-247,267-293@B`).**
- Accepted transitions:
  - none → 0.3.0 + v3;
  - 0.3.0 v2 → v3 (explicit upgrade);
  - 0.4.0 v2 → 0.4.0 v3, which changes the contract only and keeps the version.
- Unchanged values are no-ops.
- Refused with `OP-PRESSURE-PROFILE-SUCCESSOR-REQUIRED`: none → v2, and v3 → v2. Message: "new pressure authoring selects 3.0.0/exact_pressure_v3; v2 documents stay readable and solvable".
- Any version change on 0.4.0 keeps `OP-PRESSURE-PROFILE-SCHEMA-VERSION-LOCKED`.

**O4. `pressure_regions` (extended).**
- Signed p is allowed under v3. The v2 refusal keeps its code, with the message in §1.
- Members may be any pipe, as today.
- New warning `OP-PRESSURE-REGION-BEND-NOT-REALIZED` when a member is the span of a geometry-only bend.
- Topology stays the solver's.

**O5. k is user data.** Both new operations, and `set_field` on `modifiers.flexibility_factor_user_value.value`, refuse `author_type: "agent"` with `OP-BEND-FLEXIBILITY-USER-ENTRY-REQUIRED`.

**O6. Bend creation stays geometry-only.** It no longer requires `bend_plane_orientation` (`AP/lib.rs:2547-2559@B`; `componentIntent.ts:186-194,325@B`). An existing value is kept as a legacy note.

**`bend_plane_orientation`: recommend removal of the requirement, not consumption.** `y_reference` already fixes both the plane and the side, and T4-U1 forms the arc from d, R and that normal (plan §3.1). A parsed free-text plane such as "+Z" would be a second authority, and it cannot say which side the arc bows to. Tangency checks the plane: a wrong side or plane shows as a kink of about Φ.
- T4-U1 drops the field from `bend_geometry_missing` (`PP/src/validation.rs:1560-1576@B`), and also drops `bend_angle` from it for realized bends.
- T4-U2's authoring commits stop requiring the field in the applier and the desktop.
- The library-record schema (`P/schemas/component.schema.yaml:358@B`) is out of scope.

**One radius/angle authority: R plus the node geometry.** φ = 2·asin(c/2R) is derived and shown, and new operations never write `bend_angle`. An existing angle is user data: it is kept and checked with PP's existing rule (`PP/src/lib.rs:7792-7811@B`), at authoring and again at solve. The span's ends come from the nodes. The corner's angle Φ comes from the adjacent straights.

**Shared definitions (I).** T4-U1 defines the arc in CB as a pure function `arc_geometry(d, R, y_reference) -> {φ, t_i, t_j, n̂} | error`, using node differences and square roots only: t_i = cos(φ/2)d̂ + sin(φ/2)n̂ and t_j = cos(φ/2)d̂ − sin(φ/2)n̂. It also defines a `kink(a, t)` function. PP re-exports both, together with the tolerance constant and the angle-match constant, in a one-line `pub use` at the call site. The applier reaches them through its existing PP dependency (`P/core/model_operations/operation_applier/Cargo.toml@B`). So no Cargo manifest or lock changes, and authoring and solve share one definition.

## 3. Tangency

**Where it is checked.**
1. Insert bend at corner: exact by construction. Its tests assert it.
2. Realize bend: the applier evaluates the shared function at both span ends against the adjacent straights. It blocks above the tolerance when an end has one neighbour, and warns when it has more. The validation preview shows the angles before queuing.
3. Solve under v3: PP, in region traversal. This check is authoritative.
4. Preview-physics-1 stays untouched, with its 1e-6 rad warning. Changing it would move preview bytes (SP-4).

**Solve-time rule (proposal for T4-U2).** The region is split into straight runs joined at bend ends.
- **Each straight run** keeps today's 64ε collinearity guard and pre-cancelled ledger. So straight-only regions stay bit-equal to v2 (SP-1, H-2), and a kink between two straights is still `PRESSURE_REGION_NONCOLLINEAR`.
- **At each bend-adjacent junction**, the direction change θ is computed by `kink`:
  - θ ≤ α_tan: admitted, and carried exactly by the remainder `+pAi(t_in − t_out)` (H-2);
  - θ > α_tan: refused as a mitre until T4-U7.
- **Evidence records** α_tan and each junction's θ. The v3 approximation text states the rule.

**Proposed α_tan = 1.0e-3 rad (0.057°).** Reasons:
- **Representation never trips it.** Corner-inserted bends at UTM-scale coordinates (X = 7.3e6 m) carry representation kinks of:
  - 6.2e-10 rad for a 90° bend with R = 0.3 m;
  - 5.6e-8 rad for 5° with R = 0.05 m;
  - 1.7e-7 rad for 1° with R = 0.05 m.

  The node-relative and centre-based forms agree in magnitude (probe). That is a margin of at least 5e3. The 1e-6 warning threshold would leave a margin of about 5 for small bends at UTM, which is too tight for a refusal.
- **What it admits is negligible.** The admitted kink force pAi·θ is at most 7.1e-4 of a 90° bend's own wall resultant, and 1.1e-2 of a 5° bend's (probe). It is a rigid joint with no SIF. A mitre's SIF tends to 1 as its angle tends to 0 (I).
- **It is far below a code mitre.** It is about 50× below the 3° offset that ASME B31.3 ¶304.2.3 treats as not needing design as a miter. That is external knowledge, to be confirmed by T4-U2's reference TASK.
- **It suits hand entry with care.** Hand-entered coordinates at 0.1 mm pass for ordinary bends (9.1e-5 rad for 32°, R = 0.45 m). At 1 mm they fail (5.5e-3). Small bends need computed tangent points (2.2e-3 rad for 5°, R = 0.05 m, at 0.1 mm), which F2 provides.
- **It is tested.** T4-RV1 already balanced a 1e-3 kink with the remainder (`R4/T4-RV1/REVIEW.md:38`).

Whether kinks between two straights, up to α_tan, should also carry a remainder is a scope question on H-2 for ROOT (RETURN D-E). The recommendation is no for T4-U2.

## 4. UI (M02 minimal: no new element kind)

| Surface | Change | States and messages |
|---|---|---|
| Component panel, "New component" (`DT/features/model-tree/PropertyInspector.tsx:871-878@B`), and the viewport create form (`DT/features/viewport/PipeViewport.tsx:2876@B`) | Remove the "Plane orientation" input. Rename the bend's pipe picker "Bend span (arc chord)", with the hint "for a corner, use Insert bend at corner". | Creation stays geometry-only (a marker). |
| Geometry tools (`DT/features/geometry-tools/geometryDraft.ts:83@B`; `DT/App.tsx:501@B`) | New action "Insert bend at corner": R and unit, k, source of k, ids, labels and provenance, and an optional "convert marker" choice preselected when C carries one. | Disabled-reason texts: C needs exactly two incident pipes; attachments must be removed first (listed); the largest admissible R. The validation preview shows the diff rows. |
| Inspector, new "Bend realization" section (`DT/features/bend-authoring/BendRealizationForm.tsx`, mounted beside `MaterialTemperatureForm`, `PropertyInspector.tsx:559-568@B`) | Mode, R, derived φ, measured end kinks, k (required), source of k, Queue | (a) span bend, geometry-only: realize form. (b) corner marker: explanation and the "Insert bend at corner" button. (c) realized: "Realized curved bend: R, φ, k (source); k is in the stiffness, and the SIF multiplier no longer includes it" (`PP/src/lib.rs:11822@B`), with "Return to geometry-only". (d) a v3 document with a geometry-only bend: the D-2 banner (§1). |
| Inspector flags (`PropertyInspector.tsx:1389-1405@B`) and model view (`DT/features/model-workspace/modelView.ts:141-165@B`) | `BEND_GEOMETRY_INCOMPLETE` no longer needs the plane, nor the angle once realized. Add "Bend angle (derived)" for realized bends; show the plane as "Plane note (legacy, not used)". | — |
| Pressure authoring (`PressureAuthoringPanel.tsx:5,70-99,127,130,132@B`) | Profile choices `["exact_pressure_v3"]`. Mode text per contract. Region text per profile: v3 "continuity, tangency (straight runs collinear; bends realized; direction changes at bend ends above 1e-3 rad refused as mitres) and physical compatibility"; v2 keeps "straightness". Member labels: realized bend with k, or geometry-only span "realize first". Pressure hint: v2 "p ≥ 0"; v3 "signed; a negative value is a net external differential; external-pressure stability and collapse are not assessed". One notice: "the exact contract admits realized bends; tees, valves, joints and other fittings are refused by name". | Applier warnings and refusals appear in the existing queue feedback. |
| Exact-profile predicates (`DT/features/editor-contract/EditorContractPanel.tsx:210`, `DT/features/redaction-controls/RedactionExportControlsPanel.tsx:268`, `DT/features/project-validation/ProjectValidationPanel.tsx:641`, `AP/rich_authoring.rs:596-607@B`) | A shared `isExactPressureContract` (v2 or v3), in TS and in the applier | Behaviour is unchanged for v2. |

## 5. Tests

**Applier (Rust; plus contract-corpus cases run natively and in wasm).**
- O1:
  - writes exactly the three paths, every other byte equal;
  - stale `before`;
  - agent author refused;
  - k ≤ 0, NaN or missing;
  - non-bend target;
  - span missing;
  - a corner marker, and a desktop-made marker whose span is an incident straight;
  - angle mismatch;
  - y_reference parallel to the chord;
  - tangency: θ = 0 on the L passes; a 2e-3 kink blocks; a tee end warns;
  - return to geometry-only.
- O2:
  - axis-aligned L: exact T1 and T2, θ ≤ 1e-12;
  - skew 3D;
  - X = 7.3e6 m (θ ≤ 1e-6, then PP builds the arc with no `CURVED_BEND_*` diagnostic);
  - each refusal code;
  - marker conversion keeping its id, SIF, source and provenance;
  - attachments at C, a region member or a uniform load refused;
  - model hash required.
- O3: each transition, including the 0.4.0 contract-only upgrade.
- O4: v2 p < 0 refused; v3 p < 0 accepted; the not-realized warning.
- O5: an agent `set_field` on k refused.
- O6: creation without a plane.

**Desktop (vitest).**
- `BendRealizationForm`: states (a)–(d) and its exact intent payloads.
- Insert-bend draft intent.
- `componentIntent` validity without a plane.
- `PressureAuthoringPanel`: v3 picker, texts per profile, member labels, sign hint.
- `isExactPressureContract` at the four sites.
- Flags and the model view.
- `ResultsPanel` against a committed product-generated v3 L-bend result: rows, the withheld hoop with its reason, the D-3 limitations. This is reader scope, listed for completeness.

**e2e, new `e2e/bend-pressure-authoring.spec.ts`, in both projects (`chromium-desktop` 1440×920 and `chromium-compact` 1280×800, `P/apps/desktop/playwright.config.ts:67-88@B`).** Every action goes through visible controls:
- blank → v3 profile → E/ν material → A, C, B and two pipes → Insert bend at corner → Review/Apply;
- the tree shows T1, T2, the arc and the realized bend;
- regions over the three pipes;
- Save → reopen: model hash equal; Undo and Redo;
- a marker's in-place realization refused with the corner-marker message;
- v2 p < 0 refused with its message;
- solve gives the honest `BROWSER_SOLVE_BACKEND_REQUIRED_FOR_EDITED_MODEL`.

Add the spec to the `authoring` selection in `P/tools/ci/e2e_plan.py:174-187,231-234@B`, with its unittest. Compact coverage comes from the manual full dual-viewport dispatch, because PR runs limit compact to `COMPACT_SPECS` (`:43-46`).

**Save, reopen, export (native, in DEC-025's src-tauri suite).** A new ST test, patterned on `explicit_exact_model_round_trips_native_store_and_unit_metadata_without_migration` (`ST/lib.rs:6002@B`):
1. Start from a new fixture, `P/fixtures/model_operations/exact_pressure_v3_l_corner_model.json`.
2. `apply_operation` O2, then the regions.
3. Persist, load and evaluate: current, no migration.
4. Solve in both modes: `MECHANICS_SOLVED`, `pressure-1`, the bend family named in the formulation evidence, Passed at ordinary coordinates.
5. Export or transport; the RE reader accepts the result.
6. The model bytes are unchanged.

Then the same for the 0.4.0 twin.

**Native witness on the owner's Mac (T4-U2).** The packaged app at the merge head performs F1, F2, F4–F7 on the L, and must show:
1. the realized bend in the tree;
2. the solve in both modes, at Passed standing;
3. the arc rows in the tangent frame, and hoop and radial withheld with their reason;
4. the limitations naming the D-3 exclusions;
5. reopen with the same model hash;
6. the exported JSON accepted by the RS and PY readers (record its sha256);
7. the three refusals of §1, each with its message.

If the witness is not taken, record it as outstanding with what covers it meanwhile: the ST round-trip test, the vitest and the e2e. That follows the T0R, T1 and U4 precedent.

## 6. Sequencing, files and conflicts

| Step | Content | Depends on | Files |
|---|---|---|---|
| A1 | O2, insert bend at corner, with tests and corpus cases | T3's U3 merged (any T4 code) | `AP/bend_corner.rs` (new), `AP/geometry_operations.rs` (1 line), `AP/lib.rs` (`check_kinds`, dispatch), `DT/types.ts`, `P/fixtures/model_operations/contract_corpus/case_*` |
| A2 | Geometry-tools action for A1, with vitest | A1 | `DT/features/geometry-tools/{GeometryToolsPanel.tsx,geometryDraft.ts}` |
| A3 | O6, the plane requirement removed in the applier and desktop | T4-U1's PP `validation.rs` change (or in the same window) | `AP/lib.rs:2521-2587`, `componentIntent.ts`, `PropertyInspector.tsx`, `PipeViewport.tsx`, `modelView.ts`, their tests |
| A4 | O1 realize bend and O5, with tests and corpus cases | T4-U1's shared arc function (the tangency check) | `AP/bend_authoring.rs` (new), `AP/lib.rs` (rich-kind arm, resolver choice, agent guard) |
| A5 | `BendRealizationForm`, its inspector mount, vitest | A4 | `DT/features/bend-authoring/*` (new), `PropertyInspector.tsx` (mount only) |
| A6 | e2e part 1 (pressure-free: A1, A4, save and reopen), the `e2e_plan.py` selection | A2, A5 | `P/apps/desktop/e2e/bend-pressure-authoring.spec.ts`, `P/tools/ci/e2e_plan.py` and its test |
| B1 | O3 and O4, the exact predicate | T4-U2a's v3 identity constants | `AP/pressure_authoring.rs`, `AP/rich_authoring.rs`, corpus |
| B2 | Pressure-panel v3 and the shared predicate | B1 | `DT/features/pressure-authoring/*`, a new `pressureContract.ts`, the three panels above |
| C1 | e2e part 2 (v3 regions), the ST round-trip test, blank 0.4.0 under v3 (`DT/services/projectService.ts:540-550@B`), the native witness | T4-U2's PP admission and readers, and 0.4.0 under v3 | as listed in §5 |

Before T4-U2a, A1–A6 work against today's contract. Preview-physics-1 already solves realized bends, so pressure-free users gain arcs at once.

**Conflicts.**
- **T3's `b2` lanes** (`origin/codex/piping-t3-b2-20261008` `e582b61f9e`) touch the result readers, result export, stress-neutral, `analysisRunCompatibility.ts`, `ruleCheckService.ts` and `previewService.ts`. No authoring step touches any of them (F, `git diff --stat` from main `ec5d397359`).
- **`previewService.ts`** needs no authoring change. physics-1 registers nowhere in `validateCapturedSource` (`DT/services/previewService.ts:112-137@B`), so the `pressure-1` reader should not either. If T4-U2 must touch the file, rebase on `b2` first (its line 3 import and line 132).
- **T4-U3** (lane J) shares `componentIntent.ts`, `PropertyInspector.tsx`, `AP/lib.rs` (component creation), `PP/src/validation.rs` (the component block) and `DT/types.ts`. Keep T4-U2's logic in new files and its edits to these to separate small hunks. Whichever lands second rebases.
- **T4-U1** shares `validation.rs` and CB (the arc function).
- PP's `Cargo.lock`, the priced layouts and `preview_physics::LIMITATIONS` are untouched.
