# SWBPIPE completeness and reconciliation map

**Basis:** `origin/main` at `fe8eef76ac` (2026-10-26). This is a replaceable
current-state record for the owner and the work plan. Replace it when the
basis moves materially; do not append to it. It replaces the map at
`8a8a8b2584` (2026-10-23), with the edits made to it in place since; Git holds
that version.

It answers three questions:
- Which intended outcomes does the product deliver today?
- Which deliverables' documents have drifted from the code?
- What must come before development testing, the owner's hands-on use and
  validation?

It is not a release assessment. Classifications are facts read from code and
tests at the basis, with the targeted checks in §5. They are not acceptance:
acceptance, issuance and release remain the owner's (F-PIP-3). The native smoke
and the hands-on probe were not re-run for this map; §1's native evidence is
carried from `8a8a8b2584` and from the native-smoke results recorded in the
pull requests named below (§5).

Standard claim fence applies (claims taxonomy per DEC-081).

**Classes**
- **D:** delivered, with evidence (code a user reaches, and tests).
- **R:** delivered, but the deliverable's ScopeOfWork, Design or
  `deliverable.yaml` does not match the code.
- **P:** partial or missing.
- **O:** out of scope for v0.1 by a cited owner ruling.

A Must requirement met only on one solve route, only headless, or only as a
schema is P. The owner's rulings OD-1 to OD-6 (§4.2) settle the scope questions
an earlier map left open; rows cite them where they apply.

**Two solve routes** recur throughout:
- **PF:** the pressure-free route, a model with no `pressure_contract`.
- **EX:** the exact pressure route, `3.0.0/exact_pressure_v3`.

**Not on main, so not counted here:** the open pull requests in §4.3 ("In
flight"), as listed by `gh pr list --state open` on 2026-10-26.

## 1. What a user can do today

Working in the macOS desktop app on invented data, a user can do the following.

- **Projects:** open a model document, open the bundled demo, or start a blank
  project. A blank project opens a units dialog first (SI, US customary or a
  custom unit per key). The Project page changes a unit later; the length unit
  is fixed once nodes exist (#1627). A model document, stored project or saved
  state without project units is refused by name at open, and the entity
  editors refuse a missing unit key by name instead of assuming one (#1631).
  New entries take their defaults from the project units (#1644). A pending New
  Blank is superseded only by a model or project change, and is then named
  (#1640).
- **Authoring:** place nodes and pipes in the 3D viewport, assign materials and
  sections, and add bends, expansion joints, supports, load cases and
  combinations. Rigid components take a user stiffness scale with its source
  note, and a weight and centre of gravity (W-15, #1604, #1608). A load case
  can impose a displacement or rotation on a rigid support DOF (W-16 stage 1,
  #1615). Split, copy, rotate, mirror and reconnect pipes. Every edit is a
  validated, diffed and undoable operation.
- **Solving:** solve on either route.
  - PF covers linear and nonlinear supports, wind, seismic, combinations and,
    in models without nonlinear supports, imposed support displacement
    (#1615).
  - EX covers pressure, load/reference states, imposed support motion
    (`boundary_motion`) and objective-connector joints, and admits valve,
    flange, rigid and specialty components (#1604).
  - Before solving, both routes warn about disconnected parts, coincident or
    near-duplicate nodes and invalid tees (W-8). The near-duplicate tolerance
    is 5 mm unless the user sets another in the Project page's Model settings.
  - A load case whose authored loads are not applied is refused by name
    instead of solving to zeros (#1568); unknown or malformed input records
    are refused by name, nested records included (#1573, #1630).
  - A memory refusal names where it was refused, its exact code and the retry
    path (#1638).
- **Results:** read displacements, element-local and global end forces,
  reactions and stresses, each with a numerical-integrity standing and a
  per-case numerical health indicator (#1544). View the deformed shape, colour
  members by a result quantity, and show support reaction arrows (#1556).
- **Saving:** save the project to the local store and reopen it. File › Save
  Model Document… saves the canonical model document (W-6a, #1588); File › Save
  Handoff… writes a verified handoff directory package on a saved state (W-6b,
  #1600, #1613). A refused stored project or state can be exported as a model
  document for repair (#1631).
- **History:** save, open, label and delete named immutable model states;
  record runs against a saved state; compare two states, two runs, or load
  cases and combinations within one run (W-12: #1589, #1596, #1602, #1605,
  #1617, #1619).
- **Rule packs:** author a private rule pack in format 0.5.0, with stress
  categories, required load cases and load-case mappings (#1629). Validation
  reports static unit findings per check, and a pack of another format version
  is refused by name. Each check runs once per mapped load case or combination,
  and the demo pack gives `RULE_INPUTS_INCOMPLETE` with the missing inputs
  named.
- **Reports:** render a calculation report for a PF result, or for an eligible
  EX (`pressure-2` or `pressure-source-1`) result, as a local private document
  (W-3; W-11 opened by the owner on 2026-10-26, #1648). Tick "Include known
  private values in this local rendered report" and the render shows a preview
  and its canonical SHA-256, with Save canonical HTML and Print / PDF. Save
  Report Package saves a local private package for the same results (W-18 b2,
  #1616; W-11, #1648). The report carries rule-pack references, user-rule
  check outcomes, software and solver versions, the generation time, run
  settings, coordinate systems, and provenance records for materials,
  sections, components, supports and library references (W-11 (c), #1639). An
  EX report carries no numerical-health lines.
- **Libraries:** import private material, section and component libraries, and
  apply their records to model entities (#1566).
- **Exports:** export result JSON and stress-neutral JSON on both routes, each
  behind local-private intent. PF results also export the PCF and MBF package
  documents (redacted), the adapter SDK and framework envelopes, a local FEA
  packet, a native package review manifest and a preview handoff JSON. PCF and
  `.mbf` lengths convert exactly from `m`, `mm`, `in` and `ft`; other units
  and missing project units are refused by name (#1644, #1646). The byte-exact
  downstream outputs (stress-neutral CSV, glTF review geometry, PCF text and
  MBF text) are withheld by the desktop, because session values are private
  (`ControlledExportLink.tsx:40-49,141-147`). The desktop MBF text is a
  placeholder record subset that the target tool does not import (#1652; user
  guide §12).

**Native evidence.** The from-blank path (units dialog, GUI authoring, native
solve, save, reopen in a fresh process, identical re-solve; tip displacement
1.3703 mm against PL³/3EI) was observed by the hands-on probe at `8a8a8b2584`.
Later capabilities rest on the native-smoke runs their pull requests record:
135 of 135 on #1615's and #1634's heads, and 136 of 136 on #1648's (the exact
render, its hash and gates, and the exact package save).

The biggest gaps:

1. **No shareable report.** A public render of any session stays
   `blocked=true`, because session provenance is hard-coded private
   (`renderableReportInput.ts:125-135`, `sessionProvenance`). The per-report
   user release (W-18b) is designed (#1622) and not built. The report JSON
   packet, report lint, the handoff preview, the headless runner and the other
   unopened surfaces still refuse EX results (`outputPolicy.ts:91`; DEL-08-01
   Design `exact-route-report-sections.md` §5.4). The report's `assumptions`
   is empty (`renderableReportInput.ts:836`), and its limitation ids name the
   producer's fixed run name (§6.3 observation 2). Affected: FR-REP-001, -004.
2. **Mechanics gaps on one route.**
   - Combinations are refused on EX (FR-SOL-009; `exact_admission.rs:240-241`,
     `pressure_runtime.rs:343-347`), with no open pull request.
   - `equivalent_static` (wind, seismic) is refused on EX
     (`pressure_runtime.rs:372-376`).
   - PF refuses imposed displacement in a model with nonlinear supports
     (`IMPOSED_DISPLACEMENT_WITH_NONLINEAR_SUPPORTS`, `imposed_motion.rs:33`);
     stage 2 is designed (#1618) and in draft (#1654).
   - EX refuses tees (`exact_admission.rs:217`) and reducers in pressure
     regions.
3. **Rigid components: no eccentric reducer offset.** W-15 slices a, b and d
   are on main (#1604, #1608). Slice c (§12.3, with model document 0.8.0) is in
   draft (#1649). Affected: FR-SOL-004/012.
4. **Canonical model export: no run references.** Runs are not referenced in
   v0.1 (`AnalysisRunRef` const), and the hanger library kind has no schema
   value. Affected: FR-HAND-001/002, §16.
5. **MBF export is not yet usable with the validator solver.** The desktop
   MBF text is a placeholder subset with target version `TBD-17-01-001`
   (`CaepipeMbfExportPanel.tsx:53,139`) that the target tool does not import;
   the SI writer of the correlation pilot (#1652) is not used by the desktop;
   the text download is withheld (gap above). Affected: FR-HAND-005 (Could),
   §22.5.
6. **States and runs outside the model tree; no history export.** States and
   runs are navigated in the History panel, not the model tree (FR-GUI-002).
   History export is open (OI-015; FR-CMP-001). Comparison is view-only;
   mapping editor, tolerance profiles, graphical diffs and comparison export
   remain v0.2.

## 2. Outcome table

Each row gives the PRD requirement (`docs/PRD.md` line), its priority and
class, the evidence, and the deliverables. Paths are under
`projects/chirality-piping/`. "Desktop `lib.rs`" is `apps/desktop/src-tauri/src/lib.rs`;
"PP `lib.rs`" is `core/product_physics/src/lib.rs`. Line numbers are as
carried from the earlier map unless the row changed; function names are given
where lines move.

### 2.1 Model, schema, design knowledge (PRD §10.1, §11.1–11.2, §13)

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| FR-MOD-001 (476) | Must | P | **Store:** desktop `lib.rs` `save_local_project`, `open_local_project`. **Tests:** desktop `lib.rs` `local_project_store_uses_sqlite_fts5_and_round_trips_model_snapshot`, `save_local_project_round_trips_every_slot_and_refuses_malformed_slots`; `e2e/b3b-project-persistence.spec.ts`. **File:** Save Model Document (`modelDocumentSave.ts`, `model_document_save.rs`; W-6a, #1588). **Schema:** `schemas/model.schema.yaml` describes the 0.7.0 document; `tests/test_model_document_schema.py` validates the bundled demo and e2e documents against it | DEL-02-05, DEL-02-01, DEL-00-04 | Tags, notes, assumptions and rule-pack references have 0.7.0 slots (#1564), authored in the desktop (#1565). Positional-form records are refused by Save Model Document and the recovery export (`MODEL-DISPOSITION-RECORD-MALFORMED`, #1651). Nothing validates against the schema at run time. |
| FR-MOD-002 (477) | Must | P | Typed entities in PP `lib.rs:367,382,449,578,657`; 0.7.0 records for lines, constraints and equipment interfaces (#1564) | DEL-02-01 | Lines, constraints and equipment interfaces are typed records without evaluation, authored in the Model tree and the Model records tab (#1565). Class carried; see §4.3 W-22. |
| FR-MOD-003 (478) | Must | D | Identity changes refused: `operation_applier/src/rich_authoring.rs:1092`, test `:864`; `atomic_batch.rs:690`; reconnect keeps ids (`pipe_reconnect.rs`) | DEL-02-01, DEL-16-06 | No all-operations id-survival test. |
| FR-MOD-004 (479) | Must | P | `project.name`, entity `label`, and the 0.7.0 `tags` and `notes` authored in the inspector for every entity and the project (#1564, #1565); state and run labels (W-12 S1, S2) | DEL-02-01 | Class carried; see §4.3 W-22. |
| FR-MOD-005 (480) | Must | P | Library records carry structured provenance: `core/library_import/library_import_document/src/lib.rs:339-402`. Library insert and apply set the entity's `provenance_record` with `library_ref` (record digest `library_version`): `apps/desktop/src/features/library/libraryApply.ts`; tests `libraryApply.test.ts`, `operation_applier/tests/library_apply.rs` | DEL-03-01, DEL-03-07 | Entities written from a library carry a combined `provenance_record`, and the store check warns on unresolved or changed records (`check_model_library_refs`). Library save, import and apply refuse unreadable dispositions (#1653). |
| FR-MOD-006 (481) | Must | P | `unresolved_assumptions` in the 0.7.0 document (#1564), `model_state.schema.json:364` and `handoff_package.schema.json:477` | DEL-02-01, DEL-13-01 | The Model records tab enters, resolves and rejects assumptions and open issues (#1565). State-level assumptions are labels on a saved state (W-12 S1); run-level ones are labels on a recorded run; analysis_run 0.3 has no assumption slot (W-12 S2). The report does not carry them (`assumptions: []`). |
| FR-MOD-007 (482) | Must | D (bounded) | On the live solve path the product derives its analytical model (`BuiltModel`, PP `lib.rs:2261`; `build_model` `:7930`) from the supported canonical-document fields and records diagnostics | DEL-13-04, DEL-04-07 | Owner reading (2026-10-23, accepted): D bounded to this derivation. The richer PKG-13 transform contract (`core/model_transform/physical_to_analytical/contract.py`, test-only) stays deferred under OD-1. |
| FR-KNOW-001 (488) | Must | O | OD-3 (DEL-13-01 SOW:15). Desktop `lib.rs:1773` returns a bundled fixture; `KnowledgePanel.tsx` has no inputs | DEL-13-01 | |
| FR-KNOW-002 (489) | Must | D | W-8: `core/product_physics/src/topology.rs:46`, on the shared path of both routes; `MODEL_TOPOLOGY_DISCONNECTED`, `BRANCH_TOPOLOGY_INVALID`; unsupported parts still refused; EX pressure-region topology (`pressure_runtime.rs`). **Tests:** `tests/topology_checks_runtime.rs`. **Desktop:** Diagnostics panel | DEL-04-06 | Findings are warnings; PRD §14.4 "topology invalid" is read as topology that prevents the mechanics being formed (owner reading, §3). Tests use PF requests only. The bundled demo no longer declares the malformed tee C-120 (#1620). |
| FR-KNOW-003 (490) | Should | O | OD-1/OD-3 (DEL-13-03 SOW:15). `core/constraints/validation/engine.py`, Python only | DEL-13-03, DEL-13-02 | |
| FR-KNOW-004 (491) | Should | O | OD-1/OD-3 (DEL-13-02 SOW:15). `schemas/constraint.schema.json` | DEL-13-02 | |
| FR-KNOW-005 (492) | Could | O | PRD §13.3 "In future releases"; OD-1 defers further PKG-16 features; DEL-16-04:3 "v0.2 R7" | (R7) | |
| §10.1 step 1, select units (415) | — | D | W-17 (a): `features/project-units/ProjectUnitsDialog.tsx`; `projectService.ts` (`PROJECT_UNIT_KEYS`, `SI_PROJECT_UNITS`, `US_CUSTOMARY_PROJECT_UNITS`, `PROJECT-UNITS-INCOMPLETE`). **Tests:** `ProjectUnitsDialog.test.tsx`, `projectUnitSelection.test.ts`; e2e `confirmProjectUnits`. Observed natively at `8a8a8b2584` (§5) | DEL-02-02 | Change after creation (#1627): `set_project_unit` and the Project units section; length locked once nodes exist; no stored value converted. Missing units refused at every open path, editors refuse a missing key (#1631). Defaults from project units: solve temperature, seismic gravity composed as `<length>/s^2`, component stiffness units; export missing-key refusals `MBF-/PCF-/LOCAL-FEA-PROJECT-UNIT-MISSING` (#1644; DEL-02-02 Design `project-unit-selection.md` §7). The e2e confirms SI only. |

### 2.2 Desktop GUI and operations (PRD §11.3, §11.8, §14)

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| R2 exit (1572) | — | D | W-4 (#1582): the native smoke authors a cantilever from blank through the GUI (`native-smoke/driver.js`, `authorFromBlank`), solves natively, checks the tip deflection against PL³/3EI within 1e-9, saves in place, reopens in a fresh process and re-solves to the same rows, value and model hash | DEL-07-11, DEL-07-01/02/05/07 | One model shape and the SI preset only. Since #1634 the smoke builds what it launches, holds a per-worktree build lock and reports a failed solve or memory refusal by name; since #1640 it waits for the blank's session. 136 of 136 on #1648's head. |
| FR-GUI-001 (498) | Must | D | `PipeViewport.tsx` (nodes, supports, components, deformed shape, rotation glyphs, reaction arrows, result colour, load arrows, labels, legend). **Tests:** `e2e/result-overlays.spec.ts`, `PipeViewport.overlays.test.tsx`, `c3-viewport-visibility.spec.ts`, `rotation-glyph.spec.ts` | DEL-07-01, DEL-07-05 | #1556. Overlays are off by default. Colour is one value per member. Reaction arrows come from global-frame rows only. §14.2 bend arcs, corridors and no-go volumes are not drawn. |
| FR-GUI-002 (499) | Must | P | `ModelTree.tsx` (`GRID_ENTITY_TYPES`; the Tree layout's records) | DEL-07-02 | Lines show in the Tree layout (#1565, #1612). States and runs are navigated in the History panel (W-12), not the model tree. |
| FR-GUI-003 (500) | Must | P | `PropertyInspector.tsx`; `typedInspector.test.tsx` | DEL-07-02 | No dependencies, linked assumptions or dependent rule-pack inputs. |
| FR-GUI-004 (501) | Must | D | Create, modify, move, delete (refuses while any record names the pipe; `tests/pipe_delete_dependents.rs`); split, copy, rotate, mirror (`geometry_operations.rs`); reconnect (`operation_applier/src/pipe_reconnect.rs`, `tests/pipe_reconnect.rs`, `e2e/pipe-reconnect.spec.ts`; UI `GeometryToolsPanel.tsx`) | DEL-07-01, DEL-16-06 | Declared v0.1 limitation (DEL-16-06 SOW:79): reconnect refuses component-bearing and pressure-region pipes. |
| FR-GUI-005 (502) | Should | D | `workspaceSession.ts` (depth 25); `e2e/b3a-session-status.spec.ts` | DEL-00-05, DEL-07-11 | Session-only. |
| FR-GUI-006 (503) | Must | D | `MissingDataBlockingPanel.tsx`; `App.test.tsx`; `e2e/gui-workflow-validation.spec.ts` | DEL-07-04 | Topology findings are warnings, not blocking. |
| FR-GUI-007 (504) | Should | P | `ComparisonPanel.tsx`; `StateComparisonView.tsx`; `RunComparisonView.tsx`; `withinRunComparison.ts` | DEL-07-08, DEL-14-05 | State, run and within-run comparison views (W-12 S3a–S3c). No graphical overlays (FR-CMP-009, v0.2). |
| FR-AGENT-001 (568) | Should | D | `OfflineProposalIntakePanel.tsx` → `atomic_batch.rs:285-345` | DEL-16-01, DEL-16-06 | The live provider is O (D-22/DEC-041). |
| FR-AGENT-002 (569) | Should | D | `atomic_batch.rs:8,112`; tests `:529,593,690,746,806` | DEL-16-02, DEL-16-06 | |
| FR-AGENT-003 (570) | Should | D | Diff review and explicit Apply (`workspaceSession.ts`) | DEL-07-08, DEL-16-06 | No e2e for offline intake. |
| FR-AGENT-004 (571) | Should | P | Rationale and source required (`atomic_batch.rs:326-341`) | DEL-16-03, DEL-16-04 | No assumptions or constraints-considered keys; receipts are session-only. |
| FR-AGENT-005 (572) | Must | O | OD-5: the claim scan stays R7 (DEL-16-04:3, SOW:383). Boundary flags fixed and tamper-checked (`atomic_batch.rs:196-204,424-440`) | DEL-16-04 | The scanner is headless only (SOW:136). |

### 2.3 Solver and mechanics (PRD §11.4, §12, §22.2–22.3)

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| FR-SOL-001 (510) | Must | D | `core/solver/frame_kernel/src/lib.rs:17,1591`; t3_r1 references | DEL-04-01 | Both routes. |
| FR-SOL-002 (511) | Must | D | `validation/benchmarks/mechanics/src/lib.rs`; W9-A (both routes) and W9-C on both routes (`core/product_physics/tests/w9_solver_benchmarks.rs` `w9_c_l_frame_anchor_settlement_preview_route` `:429`, `…_exact_route` `:434`); nozzle movement against `validation/references/w16_imposed_motion/` with PF/EX parity (`tests/w16_imposed_motion.rs`) | DEL-04-01, DEL-09-01 | Beams, frames, transforms, thermal and imposed displacement pass on both routes; PF takes the settlement as a support-targeted primitive (W-16 stage 1, #1615). |
| FR-SOL-003 (512) | Must | D | `core/solver/straight_pipe`; `self_weight.rs`; `STRESS-*` | DEL-04-02, DEL-05-03 | PF Euler–Bernoulli; EX adds Timoshenko. |
| FR-SOL-004 (513) | Must | P | DEC-045 stiffness scaling of the mapped member on both routes (PP `rigid_component.rs`; W-15 a+d, #1604); EX admits valve, flange, rigid and specialty, and reducers outside pressure regions (`exact_admission.rs:8-31`, `EXACT_PRESSURE_REDUCER_IN_REGION`); rigid-link benchmark against independent references (`validation/references/w15_rigid_scaling/`; `tests/w15_rigid_scaling_benchmarks.rs`) | DEL-03-05 | Offsets exist only on connectors and tie rods; the eccentric reducer offset is W-15 c (#1649, draft). |
| FR-SOL-005 (514) | Must | D | `core/solver/linear_supports`; EX admits linear restraints and springs (`exact_admission.rs`) | DEL-04-03 | Both routes. |
| FR-SOL-006 (515) | Must | P | EX applies `boundary_motion`. PF maps a support-targeted `imposed_displacement` primitive into the prescribed reduction in both solver modes (PP `imposed_motion.rs`; DEL-04-03 Design `pf-imposed-displacement.md`); authored in the desktop (`LoadCaseManagerPanel.tsx:631,1713`). Tests `tests/w16_imposed_motion.rs` (22); EX refuses the primitive by name (`EXACT_IMPOSED_DISPLACEMENT_PRIMITIVE_UNSUPPORTED`, `imposed_motion.rs:26`) | DEL-04-03, DEL-04-07, DEL-05-01, DEL-05-05 | Owner (OD-6 row 2): two stages (`DEL-04-07 Design/pressure-contract.md`). Stage 1 is on main (#1615). Stage 2: PF refuses motion with nonlinear supports (`IMPOSED_DISPLACEMENT_WITH_NONLINEAR_SUPPORTS`); designed (#1618), in draft (#1654). |
| FR-SOL-007 (516) | Must | D | Twelve global end rows per member and case beside the `element_local` rows on PF and EX (PP `lib.rs` `append_element_global_end_results`); readers `result_export/src/global_end_evidence.rs`; tests `core/product_physics/tests/global_end_actions_runtime.rs`, `tests/test_global_end_verifier.py` | DEL-04-01 | W-7 (#1581). Source-recovery publications omit the rows by the named rule `global_end_rows_published`. |
| FR-SOL-008 (517) | Must | D | `core/loads/stress_recovery`; `tests/t4_u6_section_bases.rs` | DEL-05-03 | Pressure stresses exist where pressure exists (EX). |
| FR-SOL-009 (518) | Must | P | `core/loads/load_case_algebra`; `preview_physics_runtime.rs` | DEL-05-02 | EX refuses every combination (`pressure_runtime.rs:343-347`; `exact_admission.rs:240-241`). The PF constant-effort combination gate uses an exact unit factor-sum rule (#1625). |
| FR-SOL-010 (519) | Should | D | `core/solver/curved_bend`; DEC-070 | DEL-03-03, DEL-04-07 | |
| FR-SOL-011 (520) | Should | P | SIF → intensified measure (`preview_physics.rs`); `BRANCH_TOPOLOGY_INVALID` (W-8) | DEL-03-04 | Branch flexibility is not assembled. EX refuses tees (`exact_admission.rs:217`). |
| FR-SOL-012 (521) | Should | P | As FR-SOL-004; component weight at the centre of gravity as a nodal weight force plus r × F moments, replacing the mapped member's distributed self-weight (`self_weight.rs`; W-15 b, #1608; R10 convention, owner 2026-10-24); tests `tests/w15_component_weight.rs`, `w15_component_weight_benchmarks.rs` | DEL-03-05 | The eccentric reducer offset remains (W-15 c). |
| FR-SOL-013 (522) | Should | D | `frame_kernel/src/connector.rs`, `tie_rod.rs`, `joint.rs`; `tests/connector_pp_paths.rs` | DEL-03-06 | EX only. `movement_limit` is normalized, not enforced. |
| FR-SOL-014 (523) | Should | P | `core/solver/nonlinear_supports`; `references/kd5_nonlinear`; the native demo converges | DEL-04-04, DEL-04-07, DEL-09-03 | PF only. Rotational gap and friction refused (`validation.rs`). |
| FR-SOL-015 (524) | Must | D | `NUMERICAL_INTEGRITY_*` (PP `lib.rs`); health indicator `operation_applier/src/numerical_health.rs`, `ResultsPanel.tsx`, status bar and Solve panel, with tests (#1544). Observed natively on both routes at `8a8a8b2584` | DEL-04-06, DEL-05-04, DEL-07-05 | An EX report omits numerical-health lines; its standing line names an integrity warning when the diagnostics carry one (#1648). |
| §12.3 reducers | — | P | No eccentric offset vector in `core/product_physics/src` at the basis | DEL-03-05 | W-15 c (#1649, draft, with model document 0.8.0). |
| §12.5 load types | — | P | Wind, seismic and hydrotest categories (PP `lib.rs`) | DEL-05-01 | EX refuses `equivalent_static` (`pressure_runtime.rs:372-376`). Imposed rotations and nozzle movement: see FR-SOL-006. |
| §12.8 near-duplicate nodes (775) | — | D | `NODE_COINCIDENT`, `NODE_NEAR_DUPLICATE` within 5 mm unless `model_settings.node_proximity_tolerance` sets another (`topology.rs`); malformed value refused (`validation.rs` `validate_model_settings`); tests `topology_checks_runtime.rs`. Desktop control (`ModelSettingsSection.tsx`; #1593) with through-solve tests | DEL-04-06, DEL-02-01 | REQ-04-06-012 (owner) is met on both routes. |
| §12.8 verified bounds (783) | — | O | Owner, 2026-10-23: "no verified bounds in v0.1; the retained-precision method stays dormant and owner-held." (`DEL-04-08 Design/b7-plan.md:34`; SOW:336, AX-004) | DEL-04-08 | Dormant code is in `product_physics/src/retained_*.rs`. |
| §22.2 benchmarks (1403) | — | D | 14 of 14: tip force, tip moment, fixed-fixed thermal, simply supported under weight (W9-B), inclined member, L-frame (W9-A), U-loop, torsion, anchor displacement (W9-C, both routes since #1615), spring, gap, friction, branch, rigid link (W-15, both routes, #1604); `tests/w9_solver_benchmarks.rs`, `tests/w15_rigid_scaling_benchmarks.rs` (§5) | DEL-09-01..03 | Each runs on the routes that admit its families; gap, friction and branch are PF only, as those families are. |
| §22.3 stress benchmarks (1422) | — | D | `validation/benchmarks/stress/src/lib.rs`; pressure hoop and longitudinal stress in `validation/references/t4_u6` (EX); t4_u4b; the pressure family `STRESS-PRESSURE-HOOP-LONGITUDINAL-ORIGINAL` (W-20, #1599) | DEL-09-02 | The headless runner has no binding for the pressure family, so it fails closed there. |

### 2.4 Rule packs, reporting, handoff and export (PRD §11.5, §11.7, §11.9, §16–19)

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| FR-RULE-001 (530) | Must | D | Format 0.5.0 (#1629): `schemas/rule_pack.schema.yaml`; validator `core/rules/rule_pack_document/src/format.rs`; per-basis runner `rule_check_runner/src/lib.rs`; row selection `src-tauri/src/rule_solver_selection.rs`; authoring `RulePackManagerPanel.tsx`, `DeclarationsEditor.tsx`, `CheckDefinitionsEditor.tsx`. **Tests:** `rule_pack_document/tests/format_0_5_0.rs`, `rule_check_runner/tests/bases_run.rs`, `rule_solver_selection_tests.rs`, `RulePackManagerPanel.format.test.tsx`, `e2e/r2-smoke.spec.ts` | DEL-06-01, DEL-07-03 | Stress categories, required load cases and load-case mappings (§17.2; owner, 2026-10-24, option A) name the model's own load-case ids. Other format versions are refused by name, without migration. Positional-form records leave the rule check unreachable (pinned, #1651). |
| FR-RULE-002 (531) | Must | D | `rule_pack_document/src/lib.rs` `check_rule_pack_units`; UI `RulePackManagerPanel.tsx`; run time `rule_check_runner/src/lib.rs`. **Tests:** `tests/unit_check.rs`, `RulePackManagerPanel.unitCheck.test.tsx` | DEL-06-02 | Static findings do not block save or run; an inconsistent check still blocks when it runs. |
| FR-RULE-003 (532) | Must | D | `rule_check_runner/src/lib.rs` (`aggregate_rank`, `status_counts`); `RuleCheckRunPanel.tsx` headline; renderer `user_rule_check_aggregate_headline`; tests runner, `report_renderer/tests/render.rs`, `RuleCheckRunPanel.test.tsx` | DEL-06-03 | W-19 (#1585): "INCOMPLETE — n check(s) failed; m check(s) blocked" while any check is incomplete (owner reading, 2026-10-23). Counts are per load-case outcome under 0.5.0. |
| FR-RULE-004 (533) | Must | D | `rulePackService.ts` (private by default); local SQLite | DEL-06-04 | No pack file export. |
| FR-RULE-005 (534) | Must | D | `LibraryManagerPanel.tsx`; `tests/test_library_import_provenance.py`; `LibraryApplySection.tsx`, `libraryApply.ts`, applier `library_apply.rs`; tests `libraryApply.test.ts`, `operation_applier/tests/library_apply.rs` | DEL-03-01, DEL-03-07 | Records feed rule checks and apply to model entities (#1566). Library reads by Save Model Document and Save Handoff are metered (#1641). |
| FR-RULE-006 (535) | Should | D | Same panel, component kind; `libraryApply.ts` `buildComponentApply` | DEL-03-02, DEL-03-07 | Apply only; no insert. |
| FR-RULE-007 (536) | Must | D | `tests/test_invented_example_models.py`; `examples/rule_packs/invented_demo.yaml` | DEL-11-04, DEL-06-05 | |
| FR-REP-001 (578) | Must | P | Local-private render (`RenderedReportPanel.tsx`, `reportRenderService.ts`) for PF and eligible EX results (`outputPolicy.ts:91` `EXACT_ADMITTED_SURFACES`; `src-tauri/src/report_render_exact.rs:53`); report package for the same (`reportPackageRequest.ts`; `report_package/src/document_form.rs`; W-18 b2 #1616, W-11 #1648); rule-pack refs, user-rule outcomes, versions, date, settings, coordinate systems and run identity (`renderableReportInput.ts`). Tests `report_renderer` and `report_package` suites (§5) | DEL-08-01, DEL-08-06 | A public render is blocked for every session (`renderableReportInput.ts:125-135`); W-18b is designed (#1622), not built. `assumptions: []` (`:836`); build id and model coordinates "not recorded"; limitation ids name the producer's fixed run name. The report JSON packet and report lint refuse EX. |
| FR-REP-002 (579) | Must | D | Rule-check section and §19.3 notice with the human-review record in `report_renderer/src/lib.rs`; tests `report_renderer/tests/render.rs` | DEL-08-01 | Reached in the local-private render and package on both routes (#1648). |
| FR-REP-003 (580) | Must | D | Provenance records for the session, components, spring hangers, materials, sections and supports with a `provenance_record`, and the model's library references with the store's findings (W-11 (c), #1639; `renderableReportInput.ts` `subjectProvenance` `:421`, `libraryReferences` `:459`; renderer Library Records). Tests: `renderedReport.test.tsx` FR-REP-003 blocks, `report_renderer/tests/render.rs` (`a_library_reference_record_is_judged_by_the_section_rules_and_the_disposition_rule`), `tests/test_report_sections_provenance_records.py` | DEL-08-03 | Reached in the local-private render and package on both routes (#1648). A `quarantined` or `rejected` review status, or a `protected_suspected` redistribution status, refuses the render and the package; an `unknown` or `TBD` status shows a non-blocking warning in a local-private report and blocks elsewhere (owner ruling "C1 b, C2 a", 2026-10-26). Owner, 2026-10-26: "For FR-REP-003 I approve option D." (DEL-08-01 Design `exact-route-report-sections.md` §0); the options are not recorded in the repository, and this class is read from the code. |
| FR-REP-004 (581) | Should | P | Within-run comparison summary: the Comparison line and JSON comparison fields (`ReportPanel.tsx` `reportComparisonLine`, `reportComparisonFields`); package placement `stateComparisonHandoffSections.ts` | DEL-08-06 | No comparison section in the renderer. The local-private package for a Current PF result carries the chosen within-run comparison or a `comparison_unavailable` record (#1616, #1619); the EX package was not checked for this map. |
| FR-REP-005 (582) | Must | D | `core/reporting/protected_content_linter`; `tests/test_report_protected_content_linter.py` | DEL-08-05 | |
| §19.1 report types | — | P | — | DEL-08-06 | No state-comparison, run-comparison or handoff-manifest report a user can reach. |
| FR-HAND-001 (558) | Must | P | W-6a Save Model Document on either route with no solve (`modelDocumentSave.ts`, `model_document_save.rs`); W-6b Save Handoff (`handoff_package.rs`, `handoffPackageSave.ts`); `HandoffPanel.tsx`, `NativePackagePanel.tsx` preview documents; `core/handoff/exporter/workflow.py` is called only by tests | DEL-15-01, DEL-15-03, DEL-17-03, DEL-07-12 | Runs are not referenced in v0.1 (`AnalysisRunRef` const). The preview handoff panel refuses EX (`outputPolicy.ts:91`). |
| FR-HAND-002 (559) | Must | P | W-6b manifest: model hash, units manifest, entity ids, library and rule-pack references, warnings, diagnostics and unresolved assumptions (`handoff_package.rs`); witness `tests/test_handoff_package_witness.py`; verifier and tamper checks | DEL-15-01 | Hanger library kind has no schema value (`TBD`); run references are empty. |
| §16.1–16.3 handoff contents and workflow | — | P | — | DEL-15-01 | Export hash, model hash, rule-pack and entity manifests (W-6b); the basis model state (W-12 S1). Run references wait for an `AnalysisRunRef` contract edit. |
| FR-HAND-003 (560) | Should | P | `HandoffPanel.tsx` `target_field_coverage: "TBD"` | DEL-15-02 | |
| FR-HAND-004 (561) | Should | P | Loss reports (`HandoffPanel.tsx`, PCF) | DEL-15-02, DEL-17-07 | PF only. |
| FR-HAND-005 (562) | Could | D | PCF, MBF, adapter and SDK panels; observed natively at `8a8a8b2584`. SI MBF writer `core/handoff/caepipe_mbf/si_writer.py` (#1652; `MBF_VERSION = "15.10"`, `:29`), tests `tests/test_caepipe_mbf_si_writer.py` | DEL-17-04/07/08/09 | The criterion is architectural ("allows later … exporters"). The desktop MBF panel writes a placeholder subset with target version `TBD-17-01-001` and components omitted (`CaepipeMbfExportPanel.tsx:53,139`); the target tool does not import it (#1652; user guide §12). The SI writer is used only by the correlation pilot and refuses non-SI quantities. W-21 (§4.3). |
| Result JSON, stress-neutral | — | D | Result export and stress-neutral panels; `exactOutputTwins.test.tsx`; observed natively at `8a8a8b2584` | DEL-08-04, DEL-17-06 | Both carry the run record's rule-pack exclusion diagnostics (#1602, #1613). |
| Local FEA handoff | — | O | DEC-078 (D-12 O-B): FR-025 post-beta (DEL-10-03 SOW:486) | DEL-10-03 | A gated panel exists; it declares result units from the rows it labels (#1644). |

### 2.5 States, runs, comparison, V&V (PRD §11.6, §15, §21–22)

FR-CMP-001..004 and -006 are in v0.1 by OD-1 (unit W-12, design
`DEL-14-01/Design/desktop-states-runs-comparison.md`). FR-CMP-005, -007, -008, -009
and -010 remain in v0.2 R3 under that design and PRD §24. FR-CMP-011 is not an
MVP requirement (PRD §15.6).

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| FR-CMP-001 (542) | Must | P | **Store:** desktop `src-tauri/src/model_states.rs` (store v12). **UI:** `features/history/HistoryPanel.tsx`, `useModelStateHistory.ts`; `modelStateHistory.session.test.tsx`. **Record:** `model_state.schema.json`; `tests/test_model_state_record_parity.py` | DEL-14-01, DEL-07-08 | Save, reopen, tag, delete and compare (W-12 S1, S3a). SQLite-only; history export open under OI-015. |
| FR-CMP-002 (543) | Must | D | **Store:** `src-tauri/src/analysis_runs.rs` (store v13) with `analysis_runs_tests.rs`. **UI:** `HistoryPanel.tsx`; `recordRun.session.test.tsx`. **Record:** `analysisRunCompatibility.ts`, `core/analysis_runs/compatibility.py`, `tests/test_recorded_run_record.py`. **Rule packs:** `services/modelRulePackResolution.ts` | DEL-14-02, DEL-07-08 | Record Run (W-12 S2, #1596) stores an immutable v0.3 revision tied to a saved state, with the model's rule packs resolved at solve and exclusions recorded as diagnostics (#1602). |
| FR-CMP-003 (544) | Must | D | `features/comparison/stateComparison.ts`, `StateComparisonView.tsx`; tests `stateComparison.test.ts`, `compareStates.test.tsx`; parity `tests/test_model_state_comparison_parity.py` | DEL-14-03, DEL-07-08 | W-12 S3a (#1605). View-only; comparison export is v0.2 (FR-CMP-010). |
| FR-CMP-004 (545) | Must | D | `features/comparison/runComparison.ts`, `RunComparisonView.tsx`; native `admit_analysis_run_comparison`; tests `runComparison.test.ts`, `compareRuns.test.tsx`; parity `tests/test_analysis_run_comparison_parity.py` | DEL-14-04, DEL-07-08 | W-12 S3b (#1617). No unit conversion or tolerance; view-only. |
| FR-CMP-005, -007 (546, 548) | Should | P | `schemas/comparison_mapping.schema.json`; `model_state/engine.py` | DEL-14-05 | No editor. |
| FR-CMP-006 (547) | Must | D | `stateComparison.ts`; `runComparison.ts`; reference `analysis_run/engine.py` | DEL-14-03/04 | Automatic mapping only (FR-CMP-005/007, v0.2). |
| FR-CMP-008, -009, -010 (549-551) | Should | P | `schemas/comparison_tolerance.schema.json`; `ComparisonPanel.tsx` | DEL-14-05, DEL-08-06 | No profiles, overlays or CSV. |
| FR-CMP-011 (552) | Could | P | `schemas/caepipe_external_run.schema.json`; desktop `CaepipeExternalHarnessPanel.tsx` (profile and surface `TBD`) | DEL-14-05 | §15.6: not MVP. |
| §21.3 human acceptance (1385) | — | D | `docs/claims_registry.md` | DEL-01-04 | No acceptance workflow, as required. |
| §22.4 regression (1435) | Must | P | `tools/release/run_evidence_sweep.py`; last sweep `validation/evidence/sweeps/SWEEP_20260924T162044Z_b9dda2addccc.json` | DEL-00-08, DEL-09-05, DEL-10-04 | The cited sweep predates W-12, W-15, W-16 and W-11. The sweep is optional release preparation; the hosted `harness` is the merge check. |
| §22.5 prover correlation (1455) | — | P | Activated by the owner on 2026-10-26 (DEL-17-05 Design `caepipe-correlation-pilot.md` §1). Pilot (#1652): harness `core/handoff/caepipe_external/harness.py`, parser `print_csv.py`, comparison record `correlation.py` with the §22.5 fields, runner `tools/caepipe_correlation/run_pilot.py`, eight invented cases and a series under `validation/caepipe_correlation/`; tests `tests/test_caepipe_correlation.py`, `test_caepipe_print_csv_parser.py`, `test_caepipe_data_boundary.py`, `test_caepipe_private_correlation.py` (skips without the private corpus) | DEL-17-05, DEL-17-04, DEL-09-04 | Developer route only, opt-in and private; results are private reference data and no public record states agreement (Design §8). Tolerances are per-case `ASSUMPTION`s; the governed external-oracle tolerance class is `TBD` (owner). Breadth waits for the owner's full-licence decision (Design §1: "Once that's assured, I will pay for the full license allowing us to do more extensive validation work."). Remaining items: Design §10. |
| R6 reproduction (1636) | — | P | Procedure `docs/validation_manual/headless_runner_reproduction.md` (W-2); last bundle `validation/evidence/reproduction/REPRO_DEL0904_20260720T074714Z_a5235340aae3/` | DEL-09-04 | No fresh bundle (W-2 rest). |

### 2.6 Data boundary, local operation (PRD §20)

| ID | Class | Evidence | Deliverables |
|---|---|---|---|
| Public boundary and provenance (§20.1–20.2) | D (repository level) | `tools/release/run_release_candidate_scan.py`, `export_public_openpipestress.py`; `tests/test_release_candidate_scan.py`, `tests/test_export_public_openpipestress.py`; CAEPIPE data-boundary guard `tests/test_caepipe_data_boundary.py` (#1652) | DEL-12-05, DEL-10-04 |
| Local-first, private paths (§20.3–20.4) | D | SQLite store in Application Support; no `fetch`, `XMLHttpRequest`, `WebSocket` or `sendBeacon` in non-test `apps/desktop/src`, and no HTTP client crate in `src-tauri/Cargo.toml` (carried from `8a8a8b2584`) | DEL-12-01, DEL-12-04 |
| Telemetry (§20.5) | D | `telemetryPolicyService.ts`; `tests/security/test_telemetry_policy.py` | DEL-12-03 |
| Unit system (MVP) | D | `core/units`; `unitConversion.ts`; `ProjectUnitsDialog.tsx`; project-unit defaults and export refusals (#1644, #1646) | DEL-02-02 |

`tauri.conf.json` sets `"csp": null`. No outbound path was found in code, but
the webview has no network policy.

### 2.7 Class counts, MVP (PRD §23) and milestones (§24)

**Class counts.** Over 84 rows, this map has 32 P, 45 D (one bounded, one at
repository level), 7 O and no R. The rows of the map at `8a8a8b2584`, as
edited in place to the basis, count 34 P, 42 D, 8 O (its own summary line
read 35 P / 41 D and was stale). Changes:
- **P → D (3):**
  - FR-REP-002: the content is reached on both routes since the owner opened
    EX reports (#1648).
  - FR-REP-003: material, section, component, support and library records on
    every route (W-11 (c), #1639), reached on both routes (#1648).
  - §22.2: all 14 benchmarks exist; anchor displacement runs on PF since
    #1615, which was the row's one missing route.
- **O → P (1):** §22.5, activated by the owner on 2026-10-26; a pilot exists
  (#1652) but is developer-only, with governed tolerances `TBD`.
- **Reason changed, class kept:** FR-SOL-002 (D: both routes since #1615, an
  in-place edit of the earlier map); FR-SOL-006 (P: stage 1 built, stage 2
  open); FR-REP-001 (P: EX opened; the remaining gaps are public render,
  assumptions and run identity); FR-HAND-005 (D: the desktop MBF text is a
  placeholder, W-21).

**§23 MVP items:**
- **Implemented:** 27 of 28 items, 26 with desktop paths and the initial
  validation suite headless (`ValidationEvidencePanel` shows an inventory and
  does not run it). Imposed displacement works on EX and, without nonlinear
  supports, on PF; combinations on PF only. Rigid elements are DEC-045
  stiffness scaling with component weight on both routes, without the
  eccentric reducer offset. Canonical model package export is Save Model
  Document and Save Handoff, without run references.
- **Partly available in the desktop:** basic report generation. The rendered
  report and the report package exist for PF and eligible EX results, local
  private only; no report is shareable (W-18b designed, #1622).

**§24 milestones, factually.** Each entry says which of the milestone's
deliverables exist. Milestone judgment is the owner's; this map records none.
- **R0:** the model schema and unit system, the straight element, the linear
  solver, the headless runner's command line, and the cantilever and
  fixed-fixed thermal benchmarks exist.
- **R1:** partly. Rigid elements are stiffness scaling with weight (W-15 a, b,
  d); §22.2 has all 14 cases; imposed displacement passes on both routes; the
  eccentric reducer offset remains (W-15 c).
- **R2:** DEC-035 (D-14) advanced the target stage to R3 while reserving the
  R2 milestone judgment for the human (`execution/_Decomposition/SOFTWARE_DECOMP.md:645`).
  The native smoke runs a GUI-authored model through solve, review, save and
  reopen (W-4).
- **R3 (States, Runs, Comparison):** partly. States, run history and basic
  state and run comparison are in the desktop (W-12). Mapping editor,
  tolerance profiles, graphical diffs and comparison export remain in v0.2 R3.
- **R4** and **R5:** DEC-048 (D-23) accepted exit evidence for target-stage
  advancement; DEC-054 (D-27) accepted a conditional R4 gate, with §16.2/§16.5
  evidence obligations remaining (`SOFTWARE_DECOMP.md:658,664`). These
  historical rulings do not establish current milestone acceptance. A report
  is obtainable only as a local private document or package.
- **R6:** partly. Design knowledge is deferred (OD-3); no fresh reproduction
  bundle; Save Handoff writes a verified handoff package (W-6b); the
  external-prover correlation pilot exists (#1652).
- **R7:** partly. Offline proposals are delivered; candidate generation is
  absent.

### 2.8 Coverage gaps in the deliverable set

**No user outcome reaches these deliverables directly.** They provide
architecture, governance or contract basis:
- DEL-00-01, DEL-00-02, DEL-00-04, DEL-00-07;
- DEL-01-01, DEL-01-03;
- DEL-02-03, DEL-02-04;
- DEL-10-01, DEL-11-03, DEL-12-05, DEL-17-01;
- DEL-15-04 and DEL-17-05 (external-prover loop; DEL-17-05 now has a developer
  pilot, #1652).

**No deliverable owns these outcomes:**
- **Formats and stores:** the desktop project store (partly DEL-12-01).
- **Model and inspector:** inspector dependencies and assumptions.
- **Records:** the R3 exit review. (The §22.5 record fields are now carried
  by DEL-17-05's `correlation.py`, #1652.)

DEL-02-01 owns the desktop model document format and the "lines" entity;
DEL-04-06 owns topology and near-duplicate node checks; DEL-03-05 owns the
rigid link and component weight and designs the eccentric reducer offset.

## 3. Reconciliation drift

The W-1 sweep (#1540–#1546, #1550, #1557, #1560, #1575) and the re-baseline
(#1580) fixed the earlier pointer and ScopeOfWork items. The rows below are
what remains or is new at this basis.

**Fixed in this change** [fix]:
- **Release-notes draft** (`docs/RELEASE_NOTES_v0.1.0_DRAFT.md`): the
  statements found false at this basis are corrected: reports (public render,
  local-private render on both routes, the report package), exact-route
  admissions, imposed displacement on PF, rigid-component stiffness and
  weight, states, runs and comparison, model export, viewport overlays, unit
  handling, the withheld byte-exact downloads (glTF among them, on both
  routes) and the MBF placeholder. The earlier map's two release-notes items
  (`:102`, `:106`) are among them.

**Still open** [fix]:
- **Pointers:** DEL-10-04 lists `software-workflow.json` and `tools/ci/**` but
  not the root `.github/workflows/piping-*.yml`. DEL-07-02/05/08 still list
  the unused `core/gui/*` reference modules beside the desktop paths. DEL-13-03
  names only Python for connectivity; the product check is DEL-04-06's.
- **Corpus-wide retired paths:** 67 ScopeOfWork files still contain
  `execution/_Reconciliation/` (grep at this basis, annotated and
  unannotated together). Identification and Attributes boilerplate stays as
  written (Agent 0, 2026-10-23).
- **DEL-17-04 REQ-001** keeps the MBF target version `TBD` until
  source-confirmed or approved as a bounded profile; the pilot writes
  `VERSION 15.10` per the public import page (DEL-17-05 Design §2). Settling
  it for the desktop export is part of W-21; the wording change is
  acceptance-criterion text and follows the wording grant or the owner.

**Dependency declarations** (`python3 -m tools.deliverables --project
projects/chirality-piping check` at the basis): 107 deliverables, no
structural errors, 14 unknown needs, and one cycle, the strongly connected
group of nine (DEL-04-07, DEL-04-08, DEL-05-02, DEL-08-01, DEL-08-04,
DEL-08-05, DEL-09-05, DEL-10-04, DEL-10-05), as at `7a780551f0` and
`8a8a8b2584`. Draft #1642 analyses the unknowns and the cycle's one closing
edge (DEL-10-05 → DEL-04-08 `needs[9]`) and proposes resolving DEL-02-02
`needs[12]`; none of that is on main.

**Owner-reserved text (exact old → new), all applied.** The earlier map's
table of sixteen rows is closed: rows 1–5 (`native-smoke/expected.json`) were
applied by the owner (2026-10-24: "I accept your recommendations for each of
these three: G10, W-12, W-18."), then moved with W-7 (2026-10-25: "I approve
W-7's native-smoke values") and the C-120 fix (2026-10-25: "Both decisions I
approve your recommended options."); rows 6–15 were applied (2026-10-23: "I
approve items 6-15 in the form above."); row 16 was applied by Agent 0 under
the row-26 rule (#1582). Git holds the exact old and new texts. No
owner-reserved text is proposed at this basis.

**Owner readings recorded** (owner, 2026-10-23: "I accept your other
recommendations for the matters you needed from me"):
- **PRD §14.4 topology:** "topology invalid" is topology that prevents the
  mechanics being formed, which already blocks. W-8's other findings are
  warnings and REQ-04-06-012 stands (DEL-04-06 Design `model-topology-checks.md`).
- **FR-MOD-007:** D, bounded to the live derivation of `BuiltModel`; the
  PKG-13 transform contract stays deferred (§2.1).
- **FR-RULE-003:** the aggregate headlines INCOMPLETE while any check is
  incomplete (built in W-19).

**Owner notes (not text changes):**
- DEL-04-03 R01 (imposed displacement) states a ruled commitment that PF meets
  only without nonlinear supports; stage 2 is disclosed and in draft (#1654).
- DEL-13-03-R1 (deferred PKG-13) still commits connectivity, which DEL-04-06
  now delivers.

## 4. Proposed work plan

The phase is a drive to finish (owner, 2026-10-26: "we are nearing a level of
maturity where there needs to be a concerted drive towards goals and finishing
things to a practical level. Continuous improvement goes after."). The plan
therefore finishes open units first, then closes the remaining Must gaps to a
practical level, then the validation path; improvements wait in their own list.

### 4.1 Ready for development testing now

These outcomes have a desktop path that development testing can exercise
today. Most are class D; where the row is P, the item names the part that
exists:
- **Model and project:** open, save and reopen model documents and projects;
  choose project units at creation and change them later; unit defaults and
  missing-unit refusals; the recovery export.
- **Authoring:** nodes, pipes, materials, sections, bends, joints, supports,
  load cases and combinations; split, copy, rotate, mirror and reconnect; undo
  and redo; the 0.7.0 document slots. A from-blank model solves natively.
- **Rigid components (FR-SOL-004/012, P):** stiffness scaling and component
  weight on both routes; not the eccentric reducer offset.
- **Solving:** PF solve, including nonlinear supports, wind, seismic,
  combinations and imposed support displacement without nonlinear supports;
  EX solve; pre-solve topology warnings; named refusals.
- **Results:** results table, standing, numerical health indicator,
  diagnostics, deformed shape, result colour and reaction arrows.
- **History:** model states, recorded runs, and state, run and within-run
  comparison.
- **Reports (FR-REP-001, P):** the local-private rendered report and report
  package for PF and eligible EX results.
- **Proposals and data:** offline proposals; libraries and applying their
  records.
- **Rule packs:** format 0.5.0 authoring, static unit check and per-load-case
  rule-check runs.
- **Model export (FR-HAND-001/002, P):** Save Model Document and Save Handoff;
  runs are not referenced.
- **Exports:** result JSON and stress-neutral JSON (both routes); PCF and MBF
  package documents and the other PF export panels. Stress-neutral CSV, glTF,
  PCF text and MBF text are withheld by the desktop; the MBF text is a
  placeholder (W-21).
- **Boundaries:** local-only storage and telemetry.

These are **not ready**: shareable reports; EX report JSON packet, handoff
preview and other EX export panels; EX combinations and `equivalent_static`;
PF imposed displacement with nonlinear supports; the eccentric reducer
offset; run references in the handoff package; an MBF the validator solver
imports from the desktop.

### 4.2 Owner decisions that shape the plan

These are reserved because they concern v0.1 scope, commitments or a hold.

**OD-1 to OD-6 decided.** Owner, 2026-10-23: "I approve OD-1 through OD-5 as
you recommended." OD-6 was decided the same day ("OD‑6, option B (I want to
discuss 2 and 23 more).", then "Row 2 I approve option A and Row 23 I approve
your recommendation.").

| # | Decision | Consequence |
|---|---|---|
| OD-1 | Does D-11's "W7 — Forward horizon v0.2" placement (PKG-13/14/15/16/17) mean outside software 0.1.0, despite PRD §23? | **Decided:** states, run history, state and run comparison and canonical model export are in v0.1 (W-12, W-6). PKG-15 handoff stays in for model export. PKG-13, further PKG-16 agent features and further PKG-17 export formats are deferred to v0.2; the DEL-16-01/02 offline intake and the DEL-16-06 operation-application seam ship as built. PRD §23 stays as written. |
| OD-2 | Rigid elements (FR-SOL-004, Must, MVP) | **Decided:** implement DEC-045 stiffness scaling (W-15). |
| OD-3 | Design-knowledge entry and constraint validation (FR-KNOW-001, Must; R6) in v0.1? | **Decided:** design knowledge is deferred to v0.2. |
| OD-4 | Which model format is canonical? | **Decided:** the desktop model document is canonical, and `schemas/model.schema.yaml` describes it (W-13). |
| OD-5 | Viewport result overlays and reaction arrows; the R7 staging of the FR-AGENT-005 claim scan | **Decided:** overlays and reaction arrows built (#1556); FR-AGENT-005 stays R7. |
| OD-6 | Owner-reserved text in the earlier §3 table | **Decided:** applied, except row 2 (imposed displacement is built on PF instead, linear first, then with nonlinear supports). |

Also decided and recorded in the governing text: the 5 mm node-proximity
tolerance, user-settable (REQ-04-06-012); no verified bounds in v0.1; the W-10
reconnect limitation; the W-18b shareable path (owner, 2026-10-24, option B: a
per-report user release); the W-11 opening (owner, 2026-10-26: "My two
decisions are to approve your recommendations in both cases. Proceed
accordingly." and "#1648 I approve option A. For FR-REP-003 I approve option
D."); the provenance dispositions (owner, 2026-10-26: "C1 b, C2 a"); the
correlation pilot's activation (owner, 2026-10-26, DEL-17-05 Design §1).

**Open, for the owner:**

| # | Decision | Consequence |
|---|---|---|
| OD-7 | Should the desktop offer the `.mbf` text for download (W-21)? Today `ControlledExportLink.tsx` withholds it, as every byte-exact downstream output, while session values are classified private. | **Offer:** a route that admits the text under explicit local-private intent (or another context the owner names), with its own disposition screening; the user can then hand a desktop model to the validator solver. **Keep withheld:** the MBF reaches the validator only through the developer pilot. Either way W-21's writer work proceeds. |
| OD-8 | The full-licence decision for the external prover, and the governed external-oracle tolerance class (DEL-17-05 Design §1, §10) | Until then the corpus stays small and tolerances stay per-case `ASSUMPTION`s; §22.5 stays P. |
| OD-9 | A command to delete a stored local project (raised by Agent 0 on 2026-10-26 in draft #1642; DEL-07-11 Design `model-document-open-and-native-smoke.md:181-182`) | Neither the PRD nor any ScopeOfWork commits to one, so it would be a scope addition. Until decided, a stored blank stays in the store. |
| — | Opening further EX surfaces (the report JSON packet, the handoff preview and others; DEL-08-01 Design §5.4) | Opening returns to the owner, as the W-11 opening did. |

### 4.3 Units

The lane is heavy where builds or numerical checks are needed and light for
documents. Heavy work that changes numerical meaning or persistence needs
targeted regression checks and independent scrutiny (Root `AGENTS.md`).

**Done on main** (evidence; the owner's acceptance is separate):

| # | Unit | Evidence |
|---|---|---|
| W-1 | Pointer and ScopeOfWork reconciliation sweep | #1540–#1546, #1550, #1557, #1560, #1575; remaining drift in §3 |
| W-2 (part) | Validation manual current procedure, user guide, SMOKE note | #1543, #1580 |
| W-3 | Rendered report for local private sessions, with §19.2 content | #1553 (+#1555) |
| W-4 | From-blank native journey and the output gates as permanent native-smoke checks | #1582; driver hardening #1634, #1640 |
| W-5 | Memory-pool headroom | #1547; reclaimable and purgeable pages and the re-samples #1636; report-package ingress lease #1621; library-read lease #1641; named memory refusals #1638 |
| W-6a, W-6b | Save Model Document; Save Handoff with its manifest, rule-pack references resolved as the solve resolves them | #1588, #1600, #1613; dialogs #1614; stale-status guard #1643 |
| W-7 | Global-frame element-end forces (FR-SOL-007) | #1581 |
| W-8 | Pre-solve topology and near-duplicate warnings; 5 mm settable tolerance and its desktop control | #1559, #1574, #1593 |
| W-9 | L-frame, simply supported weight, anchor settlement benchmarks | #1548 |
| W-10 | Pipe reconnect | #1563 |
| W-11 | Exact-route reports: design, slices (a)–(c) with FR-REP-003 on every route, and the opening of the rendered report and report package for `pressure-2` and `pressure-source-1` | #1628, #1632, #1637, #1639, #1648; array-form refusals #1650 |
| W-12 | States, runs and comparison in the desktop (S1, S2, S3a–S3c) with rule-pack resolution | #1589, #1596, #1602, #1605, #1617, #1619; closeout #1624 |
| W-13 | Model document 0.7.0, its authoring and library apply | #1554, #1564, #1565, #1566 |
| W-15 a, b, d | DEC-045 stiffness scaling on both routes, EX admission, reference-section identification, rigid-link benchmark; component weight at the centre of gravity | #1604, #1608 |
| W-16 stage 1 | Imposed displacement on PF, linear only, with its independent reference | #1615; stage 2 design #1618 |
| W-17 | Units at creation and after; rule-pack unit check; rule-pack format 0.5.0; units refused at open; defaults from project units and export unit refusals; exact `in`/`ft` MBF and PCF lengths; positional-form and disposition refusals | #1569, #1570, #1627, #1629, #1631, #1644, #1646, #1651, #1653 |
| W-18 a, b1, b2 | Report package 2.0.0 over current results; native admission and screening; Save Report Package | #1597, #1606, #1616 |
| W-18b (design) | Per-report user release: design only, nothing built, no release recorded | #1622 |
| W-19 | Rule-check aggregate INCOMPLETE headline | #1585 |
| W-20 | Pressure stress benchmark family | #1599 |
| — | Numerical health indicator; viewport colour and reaction arrows; silent-zero refusal; strict inputs, flat and nested; constant-effort factor-sum gate; demo without C-120 | #1544, #1556, #1568, #1573, #1630, #1625, #1620 |
| — | External-prover correlation pilot: SI MBF writer, harness, parser, three-way comparison, invented cases (DEL-17-04/05) | #1652 |

**In flight** (open pull requests on 2026-10-26):

| PR | Unit | Rows it addresses |
|---|---|---|
| #1649 (draft) | W-15 c: eccentric reducer offset with model document 0.8.0 | FR-SOL-004, -012, §12.3 |
| #1654 (draft) | W-16 stage 2: imposed displacement with nonlinear supports on PF | FR-SOL-006 |
| #1655 (draft) | W-11 follow-on: exact report readability (Diagnostics evidence block, units display, run-name note; observations 1–3) | FR-REP-001 |
| #1657 | DEL-17-05 / IP boundary proposal: interoperate openly, evaluate privately; check retargeted; feature survey | §22.5 |
| #1642 (draft) | An earlier in-place reconciliation of this map at `df14318ec7`, with the dependency-declaration analysis (§3) | this map (superseded in part by this replacement) |
| #1567 (draft) | DBM concordance review | none |

**Remaining**, in finishing order:

| Order | # | Unit | Size | Kind | Lane | Depends on | Owner? |
|---|---|---|---|---|---|---|---|
| 1 | W-15 c | Eccentric reducer offset with model document 0.8.0 (§12.3) | S–M | numerical + schema | heavy, scrutiny | #1649 | No |
| 1 | W-16 stage 2 | PF imposed displacement with nonlinear supports | M | numerical | heavy, scrutiny | #1654 | No |
| 1 | W-11 follow-on | Report readability, observations 1–3 | S | desktop + Rust | heavy | #1655 | No |
| 2 | W-16 rest | Combinations on EX (FR-SOL-009, Must); `equivalent_static` on EX (§12.5) | M | numerical | heavy, scrutiny | — | No |
| 2 | W-23 | Report content to the FR-REP-001 criterion: carry the model's assumptions and the recorded run's identity into the report and package | S–M | desktop + Rust | heavy | W-11 | No |
| 2 | W-24 | Run references in the handoff package (`AnalysisRunRef` contract edit; FR-HAND-002, §16) and the hanger library kind's schema value | S–M | schema + desktop | heavy | W-6b, W-12 | Contract edit only if it changes a commitment |
| 2 | W-22 | Re-review of the Must P rows whose remaining gap the map does not state (FR-MOD-002, -004, -005, -006; FR-GUI-002, -003; FR-CMP-001), against code and tests, with an independent check | S | review | light | — | No |
| 3 | W-21 | **MBF export to practical use with the validator solver** (owner-approved addition, 2026-10-26): settle the target version for the desktop export (DEL-17-04 REQ-001; the pilot uses 15.10) and its record coverage; move the desktop `.mbf` builder onto the SI writer's record subset (Design §10), with the exact `in`/`ft` conversions of #1646 in place of the writer's SI-only refusal; add the omitted component records and the writer breadth listed in Design §10 as the corpus needs them; OD-7 decides whether the desktop offers the text for download. Done in #1652: the SI writer, harness, parser, comparison record and pilot cases. Waiting on OD-8: full-licence coverage and governed tolerances | M | Python + desktop | heavy | #1652; OD-7 for the download | OD-7, OD-8 |
| 3 | W-18b | Per-report user release (a shareable path): build the design's slices (DEL-08-01 Design `report-user-release.md` §8), re-deriving its drafts against the W-11 opening | about 4.35k lines | desktop + Rust | heavy | W-18 a–b2, W-11 | Decided (option B); the release act stays the user's per report |
| 3 | W-2 (rest) | Fresh R6 reproduction bundle at the validation basis | S | run | heavy | the validation basis | Acceptance of the reproduction is the owner's |
| — | W-14 | Design-knowledge entry and constraint validation | — | — | — | — | Deferred to v0.2 (OD-3) |

Order 1 finishes open work; order 2 closes Must gaps; order 3 is the
validation path and the shareable report.

**After the finishing drive (continuous improvement):**
- the §3 pointer and retired-path items;
- #1642's dependency-declaration proposals;
- the correlation lane's carried review findings (#1652 "Open": the public
  observation check's parsing items; independent full-solution assertions for
  the L-bend and branch shear values) and the batch-route CSV once a build
  provides it;
- comparison export, mapping editor, tolerance profiles and graphical diffs
  (v0.2 R3).

## 5. Checks run for this map

At `fe8eef76ac`, in this change's worktree:
- `python3 -m tools.deliverables --project projects/chirality-piping check`,
  before and after the edit: 107 deliverables, 0 errors, 14 unknown needs, the
  one nine-member cycle; unchanged by this change.
- `python3 tools/software_workflow/select_affected_checks.py
  projects/chirality-piping/software-workflow.json docs/COMPLETENESS_MAP.md
  docs/RELEASE_NOTES_v0.1.0_DRAFT.md`: no registered checks are selected for
  these paths.
- `cargo test --release` in `core/product_physics` for `w16_imposed_motion`
  (22 passed), `w9_solver_benchmarks` (7), `w15_component_weight` (19) and
  `w15_rigid_scaling_benchmarks` (7).
- `cargo test --release` in `core/reporting/report_renderer` and
  `core/reporting/report_package`: 201 passed, none failed, across both.
- `pytest` on `tests/test_caepipe_mbf_si_writer.py`,
  `test_caepipe_print_csv_parser.py`, `test_caepipe_correlation.py`,
  `test_caepipe_data_boundary.py`, `test_caepipe_private_correlation.py` and
  `test_model_document_schema.py`: 132 passed, 1 skipped (the private
  correlation check, without the corpus).
- `python3 tools/validation/validate_claims_language.py` after the edit: valid
  (485 files scanned).
- Greps and reads of the code cited in §1–§2 (admission sets, refusal codes,
  withheld routes, the MBF panel's `TBD` values, the report's provenance and
  assumptions), and `gh pr list --state open` for §4.3.

The correlation lane's public-observation check
(`tools/caepipe_correlation/check_public_observations.py`) needs its private
terms file and was not run; this map states no observation of the external
prover and no correlation result.

**Not re-run:** the native smoke, the hands-on probe, the desktop vitest and
Playwright suites, and the full Rust and Python suites. §1's native evidence
is carried from the probe at `8a8a8b2584` (from-blank authoring, native solve,
save, reopen, identical re-solve) and from the native-smoke results recorded
in #1615, #1634 and #1648.

## 6. Independent spot-check

None for this replacement. The class changes in §2.7 rest on the code and
checks above; an independent read of them is part of W-22. The earlier map's
spot-check (Codex, over `8a8a8b2584`) is in Git.
