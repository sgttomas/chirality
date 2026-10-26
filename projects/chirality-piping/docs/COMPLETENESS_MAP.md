# SWBPIPE completeness and reconciliation map

**Basis:** `origin/main` at `8a8a8b2584` (2026-10-23) for the reviews, the
native smoke and the probe (§5, §6). §1, the rows of §2, §2.7, §2.8, §3 and §4
were reconciled with `main` at `df14318ec7` (2026-10-26), which includes the
merges since the basis (`git log --merges 8a8a8b2584..df14318ec7`), among them
W-4 (#1582) and the owner's rulings and readings of 2026-10-23 on §3 rows 6–15,
PRD §14.4 topology, FR-MOD-007 and FR-RULE-003. This is a replaceable
current-state record for the owner and the work plan. Replace it when the
basis moves materially; do not append to it. It replaces the map at
`7a780551f0`; Git holds that version.

It answers three questions:
- Which intended outcomes does the product deliver today?
- Which deliverables' documents have drifted from the code?
- What must come before development testing, the owner's hands-on use and
  validation?

It is not a release assessment. Classifications are facts read from code, tests,
one native smoke run and one hands-on probe (§5). They are not acceptance:
acceptance, issuance and release remain the owner's (F-PIP-3).

Standard claim fence applies (claims taxonomy per DEC-081).

**Classes**
- **D:** delivered, with evidence (code a user reaches, and tests).
- **R:** delivered, but the deliverable's ScopeOfWork, Design or
  `deliverable.yaml` does not match the code.
- **P:** partial or missing.
- **O:** out of scope for v0.1 by a cited owner ruling.

A Must requirement met only on one solve route, only headless, or only as a
schema is P. The owner's rulings OD-1 to OD-6 (§4.2) settle the scope questions
the previous map left open; rows cite them where they apply.

**Two solve routes** recur throughout:
- **PF:** the pressure-free route, a model with no `pressure_contract`.
- **EX:** the exact pressure route, `3.0.0/exact_pressure_v3`.

**Not on main, so not counted here (in flight):** the open pull requests in
§4.3 ("In flight"). They are as listed on 2026-10-26; refresh them, and give
the merge of any that has merged, whenever this map is refreshed.

## 1. What a user can do today

Working in the macOS desktop app on invented data, a user can do the following.
The native smoke and the hands-on probe (§5) exercised the from-blank path in
the real app at `8a8a8b2584`; later capabilities cite their pull requests and
the native smoke runs recorded there.

- **Projects:** open a model document, open the bundled demo, or start a blank
  project. A blank project opens a units dialog first (SI, US customary or a
  custom unit per key). The Project page changes a unit later; the length unit
  is fixed once nodes exist (#1627). A model document, stored project or saved
  state without project units is refused by name at open, and the entity
  editors refuse a missing unit key by name instead of assuming one (#1631).
  Only a model or project change supersedes a pending New Blank; a superseded
  one is named (`NEW-BLANK-SUPERSEDED`) with the stored blank's name and id
  and the List Local Projects route (#1640).
- **Authoring:** place nodes and pipes in the 3D viewport, assign materials and
  sections, and add bends, expansion joints, supports, load cases and
  combinations. Rigid components take a user stiffness scale with its source
  note, and a weight and centre of gravity (W-15, #1604, #1608). Split, copy,
  rotate, mirror and reconnect pipes. Every edit is a validated, diffed and
  undoable operation.
  - The probe authored a cantilever from blank in the native app: node,
    material, pipe, fixed support, load case and a 350 N tip force. It solved
    natively, saved, reopened in a fresh process and solved again identically.
    The tip displacement (1.3703 mm) agrees with PL³/3EI.
- **Solving:** solve on either route.
  - PF covers linear and nonlinear supports, wind, seismic and combinations.
  - EX covers pressure, load/reference states, imposed support motion and
    objective-connector joints, and admits valve, flange, rigid and specialty
    components (#1604).
  - Before solving, both routes warn about disconnected parts, coincident or
    near-duplicate nodes and invalid tees (W-8). The near-duplicate tolerance
    is 5 mm unless the user sets another in the Project page's Model settings.
  - A load case whose authored loads are not applied is refused by name
    instead of solving to zeros (#1568).
  - A memory refusal of a native solve names, on the Solve panel and in the
    exported Solve job JSON, where it was refused, its exact code and the retry
    path (#1638).
- **Results:** read displacements, element-local and global end forces,
  reactions and stresses, each with a numerical-integrity standing and a
  per-case numerical health indicator. View the deformed shape, colour members
  by a result quantity, and show support reaction arrows.
- **Saving:** save the project to the local store and reopen it. File › Save
  Model Document… saves the canonical model document to a file (W-6a, #1588),
  and File › Save Handoff… writes a verified handoff directory package (W-6b,
  #1600). A stored project or state that the open paths refuse can still be
  exported as a model document for repair, without adopting it (#1631).
- **History:** save, open, label and delete named immutable model states;
  record runs against a saved state; compare two states, two runs, or load
  cases and combinations within one run (W-12, §2.5).
- **Rule packs:** author a private rule pack in format 0.5.0, with stress
  categories, required load cases and load-case mappings (#1629). Validation
  reports static unit findings per check, and a pack of another format version
  is refused by name. Each check runs once per mapped load case or combination,
  and the demo pack gives `RULE_INPUTS_INCOMPLETE` with the missing inputs
  named.
- **Reports:** render a calculation report for a PF result as a local private
  document. Tick "Include known private values in this local rendered report"
  and the render shows a preview and its canonical SHA-256, with Save canonical
  HTML and Print / PDF. The document carries rule-pack references, user-rule
  check outcomes, software and solver versions, the generation time, run
  settings and coordinate systems. Save Report Package saves a local private
  package for a Current PF result (W-18 b2, #1616).
- **Libraries:** import private material, section and component libraries, and
  apply their records to model entities (#1566).
- **Exports:** export result JSON and stress-neutral JSON on both routes, each
  behind local-private intent. PF results also export the PCF and MBF package
  documents (redacted), the adapter SDK and framework envelopes, a local FEA
  packet, a native package review manifest and a preview handoff JSON. The
  byte-exact downstream outputs (stress-neutral CSV, glTF review geometry, PCF
  text and MBF text) are withheld by the desktop, because session values are
  private (`ControlledExportLink.tsx`).

The biggest gaps:

1. **No shareable report, no EX report or report package.** A public render of
   any session stays `blocked=true`, because session provenance is hard-coded
   private (`renderableReportInput.ts` `sessionProvenance`). EX results are
   refused for every report and the report package (ruling 10A). W-11 slices
   (a) (#1632) and (b) (#1637) build the exact-route sections and admission
   behind that gate; opening it returns to the owner. The per-report user
   release (W-18b) is designed (#1622) and not built. The report lacks
   materials, sections and library records; W-11 slice (c) adds them (#1639,
   open). Affected: FR-REP-001..004.
2. **Saved-state and run comparisons are view-only; selected within-run comparison context is packaged.** Model states, run history and comparison are in v0.1 by OD-1. Named immutable states are in the desktop (W-12 S1, #1589): save, open, label and delete, kept only in the SQLite store. Runs are recorded against states (W-12 S2, #1596), with the model’s rule packs resolved at solve (#1602). Two saved states are compared in the desktop (W-12 S3a, #1605), and two runs (W-12 S3b, #1617). “Within this run” lets the user choose the load case and combination (W-12 S3c). The report line and JSON, preview handoff summary, export review and design-workspace downloads, and the saved local-private report package for a Current pressure-free result (W-18b2) carry the chosen comparison context. A combination whose rows include a kind with no declared dimension is refused by name (`ANALYSIS-RUN-RESULT-DIMENSION-UNDECLARED`); those consumers carry its bases, run and reason in a `comparison_unavailable` record. The saved `.swbhandoff` carries no comparison. Mapping editor, tolerance profiles, graphical diffs and DEL-14-05 comparison-output export remain v0.2. Affected: FR-CMP-001..004, -006, FR-GUI-007.
3. **Rigid components: no eccentric reducer offset.** OD-2 chose DEC-045
   stiffness scaling. W-15 slices a and d (#1604) apply it on both routes,
   admit valve, flange, rigid and specialty components on EX, and identify
   body stress rows as reference-section results. Slice b (#1608) applies
   component weight at the centre of gravity. The eccentric reducer offset
   (slice c, §12.3) remains, with no open pull request. Affected:
   FR-SOL-004/012.
4. **Canonical model export: no run references.** File › Save Model Document…
   saves the canonical model document (W-6a, #1588). File › Save Handoff…
   writes a verified handoff package whose rule-pack references are resolved
   as the solve resolves them (W-6b, #1600; #1613). Runs are not referenced in
   v0.1 (`AnalysisRunRef` const), and the hanger library kind has no schema
   value. Both saves read referenced libraries from the store without a memory
   lease; #1641 (open) meters them. Affected: FR-HAND-001/002.
5. **Model document slots.** The model document is 0.7.0 (#1564), and the
   schema describes it. Tags, notes, unresolved assumptions and open issues,
   rule-pack references, lines, constraints, equipment interfaces and structured
   entity provenance with `library_ref` have slots, checked by one document
   validator, and the desktop authors them (#1565). Library records apply to
   model entities with their provenance (#1566). Lines, constraints and
   equipment interfaces are typed records without evaluation. Affected:
   FR-MOD-001/002/004/005/006.
6. **Mechanics gaps on one route.**
   - Combinations are refused on EX (FR-SOL-009), with no open pull request.
   - Imposed displacement is refused on PF (FR-SOL-006); the owner ruled to
     build it there in two stages. Stage 1 is #1615 and the stage 2 design
     #1618, both open.
7. **W-17, remaining: project units and one stale message.** Two load-case
   fields still fall back to a fixed unit when the stored value has none: the modulus-basis solve
   temperature to `K` and the seismic gravity acceleration to `m/s^2`
   (`PropertyInspector.tsx:2237,2247`), and the matching grid columns use
   those units (`ModelTree.tsx` `modulus-basis-temperature`,
   `seismic-gravity`). A DEL-02-02 design for these temperature and
   acceleration units is queued. The CAEPIPE MBF and local FEA export panels
   fall back to fixed units when a project key is missing
   (`CaepipeMbfExportPanel.tsx:331,382-383`;
   `LocalFeaHandoffPanel.tsx:540-546`). Before them in the queue: a failed
   state listing in Save Handoff can overwrite a newer status message, because
   its catch (`workspaceSession.ts:2552`) does not check that the session is
   unchanged, as the success path does (`:2558`). Since #1640, a selection or
   unapplied typing no longer cancels a pending New Blank. Whether to add a
   command that deletes a stored project is an owner question (§4.2). Affected:
   §10.1 step 1.

## 2. Outcome table

Each row gives the PRD requirement (`docs/PRD.md` line), its priority and
class, the evidence, and the deliverables. Paths are under
`projects/chirality-piping/`. "Desktop `lib.rs`" is `apps/desktop/src-tauri/src/lib.rs`;
"PP `lib.rs`" is `core/product_physics/src/lib.rs`.

### 2.1 Model, schema, design knowledge (PRD §10.1, §11.1–11.2, §13)

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| FR-MOD-001 (476) | Must | P | **Store:** desktop `lib.rs` `save_local_project` (`:2580`), `open_local_project` (`:2515`). **Tests:** desktop `lib.rs` `local_project_store_uses_sqlite_fts5_and_round_trips_model_snapshot` (`:6678`), `save_local_project_round_trips_every_slot_and_refuses_malformed_slots` (`:7943`); `e2e/b3b-project-persistence.spec.ts`. **Schema:** `schemas/model.schema.yaml` describes the 0.7.0 document; `tests/test_model_document_schema.py` `test_current_documents_validate_against_the_format` (`:256-260`) validates the bundled demo and e2e documents against it | DEL-02-05, DEL-02-01, DEL-00-04 | Tags, notes, assumptions and rule-pack references have 0.7.0 slots (#1564) and are authored in the desktop (#1565). File › Save Model Document… saves the document to a file (W-6a, #1588). Nothing validates against the schema at run time. |
| FR-MOD-002 (477) | Must | P | Typed entities in PP `lib.rs:367,382,449,578,657` | DEL-02-01 | Lines, constraints and equipment interfaces have 0.7.0 slots as typed records without evaluation (#1564), authored in the Model tree and the Model records tab (#1565). |
| FR-MOD-003 (478) | Must | D | Identity changes refused: `operation_applier/src/rich_authoring.rs:1092`, test `:864`; `atomic_batch.rs:690`; reconnect keeps ids (`pipe_reconnect.rs`) | DEL-02-01, DEL-16-06 | No all-operations id-survival test. |
| FR-MOD-004 (479) | Must | P | Only `project.name` and entity `label` | DEL-02-01 | Tags and notes have 0.7.0 slots (#1564), authored in the inspector for every entity and the project (#1565). |
| FR-MOD-005 (480) | Must | P | Library records carry structured provenance: `core/library_import/library_import_document/src/lib.rs:339-402`. Library insert and apply set the entity's `provenance_record` with `library_ref` (record digest `library_version`): `apps/desktop/src/features/library/libraryApply.ts`; tests `libraryApply.test.ts`, `operation_applier/tests/library_apply.rs` | DEL-03-01, DEL-03-07 | 0.7.0 adds a structured `provenance_record` with `library_ref` (#1564). Applying library records (#1566): entities written from a library carry a combined `provenance_record`, and the store check warns on unresolved or changed records (`check_model_library_refs`). |
| FR-MOD-006 (481) | Must | P | `unresolved_assumptions` exists in `schemas/physical_transform_model.schema.yaml`, `model_state.schema.json:364` and `handoff_package.schema.json:477`, not in the desktop model document | DEL-02-01, DEL-13-01 | 0.7.0 adds the slot (#1564); the Model records tab enters, resolves and rejects them (#1565). State-level assumptions are labels on a saved state, carried into its `ModelStateRecord` (W-12 S1, #1589). Run-level assumptions are labels on a recorded run, shown with it; analysis_run 0.3 has no assumption slot (W-12 S2, #1596). |
| FR-MOD-007 (482) | Must | D (bounded) | On the live solve path the product derives its analytical model (`BuiltModel`, PP `lib.rs:2261`; `build_model` `:7930`) from the supported canonical-document fields and records diagnostics (PP `lib.rs:2635-2739`) | DEL-13-04, DEL-04-07 | Owner reading (2026-10-23, accepted): D bounded to this derivation. The richer PKG-13 transform contract (`core/model_transform/physical_to_analytical/contract.py`, test-only) stays deferred under OD-1. |
| FR-KNOW-001 (488) | Must | O | OD-3 (DEL-13-01 SOW:15). Desktop `lib.rs:1773` returns a bundled fixture; `KnowledgePanel.tsx` has no inputs | DEL-13-01 | |
| FR-KNOW-002 (489) | Must | D | W-8: `core/product_physics/src/topology.rs:46`, called once at PP `lib.rs:2739` on the shared path of both routes; `MODEL_TOPOLOGY_DISCONNECTED` (`topology.rs:136`), `BRANCH_TOPOLOGY_INVALID` (`validation.rs:1310-1320`); unsupported parts still refused (PP `lib.rs:15412`); EX pressure-region topology (`pressure_runtime.rs:1538,1548,1595`). **Tests:** `tests/topology_checks_runtime.rs` (9). **Desktop:** Diagnostics panel (`App.test.tsx:10907`) | DEL-04-06 | Findings are warnings; PRD §14.4 lists topology under "blocking for model validity" (§6). Tests use PF requests only. The bundled demo no longer declares the malformed tee C-120 and raises no topology warning; the refused demo `invented_preview_model.json` still declares it. |
| FR-KNOW-003 (490) | Should | O | OD-1/OD-3 (DEL-13-03 SOW:15). `core/constraints/validation/engine.py`, Python only | DEL-13-03, DEL-13-02 | |
| FR-KNOW-004 (491) | Should | O | OD-1/OD-3 (DEL-13-02 SOW:15). `schemas/constraint.schema.json` | DEL-13-02 | |
| FR-KNOW-005 (492) | Could | O | PRD §13.3 "In future releases"; OD-1 defers further PKG-16 features; DEL-16-04:3 "v0.2 R7" | (R7) | |
| §10.1 step 1, select units (415) | — | D | W-17 (a): `features/project-units/ProjectUnitsDialog.tsx`, mounted in `App.tsx`; `projectService.ts` (`PROJECT_UNIT_KEYS`, `SI_PROJECT_UNITS`, `US_CUSTOMARY_PROJECT_UNITS`, `PROJECT-UNITS-INCOMPLETE`). **Tests:** `ProjectUnitsDialog.test.tsx`, `projectUnitSelection.test.ts`; e2e `confirmProjectUnits`. Observed natively (§5) | DEL-02-02 | Changing units after creation (slice b, #1627): `set_project_unit` (`operation_applier/src/project_units_authoring.rs`; tests `operation_applier/tests/project_unit_authoring.rs`) and the Project units section on the Project page (`features/project-units/ProjectUnitsSection.tsx`). Length is locked once nodes exist; no stored value is converted (DEL-02-02 Design §2.7–§2.8). Missing units (#1631): a document without `project.units` is refused by name on every open path (model document, local project, saved state), and the entity editors refuse a missing key by name instead of assuming a unit (`features/project-units/missingProjectUnit.ts`; `missingProjectUnitEditors.test.tsx`; DEL-02-02 Design §3). A refused stored project or state can be exported as a model document for repair (`src-tauri/src/stored_model_document_export.rs`; `storedDocumentExport.test.tsx`). The e2e confirms SI only. New Blank (#1640): only a model or project change supersedes a pending create (`workspaceSession.ts` `modelCommitEpochRef`); a superseded one is named `NEW-BLANK-SUPERSEDED` with the stored blank's name and id and the List Local Projects route; tests `App.projectHandlers.test.tsx`. Remaining (§1 item 7, W-17 rest): the Save Handoff state-list catch, the load fields' `K` and `m/s^2` defaults and the export panels' unit fallbacks. |

### 2.2 Desktop GUI and operations (PRD §11.3, §11.8, §14)

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| R2 exit (1572) | — | D | W-4 (#1582): the native smoke authors a cantilever from blank through the GUI (`native-smoke/driver.js`, `authorFromBlank`), solves natively, checks the tip deflection against PL³/3EI within 1e-9, saves in place, reopens in a fresh process and re-solves to the same rows, value and model hash (`run.mjs`, "from blank" checks) | DEL-07-11, DEL-07-01/02/05/07 | The browser journey still ends at `BROWSER_SOLVE_BACKEND_REQUIRED_FOR_EDITED_MODEL`, by design. One model shape and the SI preset only. Since #1634 the smoke builds what it launches (content stamps for the WASM engines and the app binary, `scripts/engineSourceStamp.mjs`, `appBinaryBinding.mjs`), holds a per-worktree build lock (`worktreeBuildLock.mjs`), and reports a failed solve or memory refusal by name instead of timing out (`native-smoke/driver.js`); 135 of 135 checks passed on #1634's head. Since #1640 the driver waits for the blank's session before authoring (`native-smoke/driver.js` `awaitBlankProject`; `driver.test.mjs`). |
| FR-GUI-001 (498) | Must | D | `PipeViewport.tsx:1289-1291` (nodes, supports, components); deformed shape `:1306-1310`; rotation glyphs `:1313`; reaction arrows `:1315-1317`; result colour `:1323-1327`; load arrows `:1332`; labels `:1374-1429`; legend `:2456`. **Tests:** `e2e/result-overlays.spec.ts:158` (PR core lane), `PipeViewport.overlays.test.tsx`, `c3-viewport-visibility.spec.ts`, `rotation-glyph.spec.ts` | DEL-07-01, DEL-07-05 | Overlays are off by default. Colour is one value per member. Reaction arrows come from global-frame rows only. The D-72 orbit qualification with result colour has not run. §14.2 bend arcs, corridors and no-go volumes are not drawn. |
| FR-GUI-002 (499) | Must | P | `ModelTree.tsx` (`GRID_ENTITY_TYPES`; the Tree layout's `treeRecords` slot) | DEL-07-02 | Lines show in the Tree layout's Lines section (W-13 S2a, #1565; placed by #1612). States and runs are navigated in the History panel (W-12), not the model tree. |
| FR-GUI-003 (500) | Must | P | `PropertyInspector.tsx:1276,1291,1311`; `typedInspector.test.tsx` | DEL-07-02 | No dependencies, linked assumptions or dependent rule-pack inputs. |
| FR-GUI-004 (501) | Must | D | Create, modify, move, delete (refuses while any record names the pipe; `tests/pipe_delete_dependents.rs`); split, copy, rotate, mirror (`geometry_operations.rs`); reconnect (`operation_applier/src/pipe_reconnect.rs`, `tests/pipe_reconnect.rs`, `e2e/pipe-reconnect.spec.ts:52`; UI `GeometryToolsPanel.tsx:65-88`) | DEL-07-01, DEL-16-06 | Declared v0.1 limitation (DEL-16-06 SOW:79): reconnect refuses component-bearing and pressure-region pipes. All four demo pipes are refused. |
| FR-GUI-005 (502) | Should | D | `workspaceSession.ts` (depth 25); `e2e/b3a-session-status.spec.ts` | DEL-00-05, DEL-07-11 | Session-only. |
| FR-GUI-006 (503) | Must | D | `MissingDataBlockingPanel.tsx:24,148-181`; `App.test.tsx`; `e2e/gui-workflow-validation.spec.ts:110` | DEL-07-04 | Topology findings are warnings, not blocking. |
| FR-GUI-007 (504) | Should | P | `ComparisonPanel.tsx`; `previewService.ts` (`single_run_load_basis_review`); `StateComparisonView.tsx`; `RunComparisonView.tsx`; `withinRunComparison.ts` | DEL-07-08, DEL-14-05 | A saved-state comparison view (W-12 S3a: table of changed entities and field paths) and a run comparison view (W-12 S3b: mapped rows with deltas, `not_compared` reasons, context deltas and unmatched rows) sit beside the within-run deltas, whose load case and combination the user selects (W-12 S3c). No graphical overlays (FR-CMP-009, v0.2). |
| FR-AGENT-001 (568) | Should | D | `OfflineProposalIntakePanel.tsx` → `atomic_batch.rs:285-345` | DEL-16-01, DEL-16-06 | The live provider is O (D-22/DEC-041). |
| FR-AGENT-002 (569) | Should | D | `atomic_batch.rs:8,112`; tests `:529,593,690,746,806` | DEL-16-02, DEL-16-06 | |
| FR-AGENT-003 (570) | Should | D | Diff review and explicit Apply (`workspaceSession.ts:1345,1496`) | DEL-07-08, DEL-16-06 | No e2e for offline intake. |
| FR-AGENT-004 (571) | Should | P | Rationale and source required (`atomic_batch.rs:326-341`) | DEL-16-03, DEL-16-04 | No assumptions or constraints-considered keys; receipts are session-only. |
| FR-AGENT-005 (572) | Must | O | OD-5: the claim scan stays R7 (DEL-16-04:3, SOW:383). Boundary flags fixed and tamper-checked (`atomic_batch.rs:196-204,424-440`) | DEL-16-04 | The scanner is headless only (SOW:136). |

### 2.3 Solver and mechanics (PRD §11.4, §12, §22.2–22.3)

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| FR-SOL-001 (510) | Must | D | `core/solver/frame_kernel/src/lib.rs:17,1591`; t3_r1 references | DEL-04-01 | Both routes. |
| FR-SOL-002 (511) | Must | P | `validation/benchmarks/mechanics/src/lib.rs:934,963,1693`; W9-A (both routes), W9-C | DEL-04-01, DEL-09-01 | Beams, frames, transforms and thermal pass on both routes. The imposed-displacement benchmark (W9-C, route witness `core/product_physics/tests/w9_solver_benchmarks.rs` `w9_c_l_frame_anchor_settlement_exact_route`, `:413`) runs on EX only, because PF refuses support motion (FR-SOL-006). #1615 (open) runs the settlement benchmark on PF. |
| FR-SOL-003 (512) | Must | D | `core/solver/straight_pipe`; `self_weight.rs:505-512`; `STRESS-*` | DEL-04-02, DEL-05-03 | PF Euler–Bernoulli; EX adds Timoshenko. |
| FR-SOL-004 (513) | Must | P | DEC-045 stiffness scaling of the mapped member on both routes (PP `rigid_component.rs`, `lib.rs` member formation; W-15 a+d, #1604); EX admits valve, flange, rigid and specialty and refuses reducers in pressure regions (`exact_admission.rs`); rigid-link benchmark against independent references (`validation/references/` W-15 package; `tests/w15_rigid_scaling_benchmarks.rs`) | DEL-03-05 | Offsets exist only on connectors and tie rods; the eccentric reducer offset is slice c (with the 0.8.0 document). |
| FR-SOL-005 (514) | Must | D | `core/solver/linear_supports`; PP `lib.rs:2741`; EX admits linear restraints and springs (`exact_admission.rs:295-305`) | DEL-04-03 | Both routes. |
| FR-SOL-006 (515) | Must | P | EX applies support motion (W9-C route witness `core/product_physics/tests/w9_solver_benchmarks.rs` `w9_c_l_frame_anchor_settlement_exact_route`, `:413`). PF refuses support-targeted loads (`preview_physics.rs` `imposed_displacement_refusal`, `:1093`; diagnostic `IMPOSED_DISPLACEMENT_REQUIRES_LOAD_STATE_MODEL`, `:1136`) | DEL-04-03, DEL-04-07, DEL-05-01, DEL-05-05 | Owner (OD-6 row 2): build on PF in two stages (`DEL-04-07 Design/pressure-contract.md`, "Imposed displacement on the pressure-free route"). Stage 1 is #1615 (open; DEL-04-03 Design `pf-imposed-displacement.md`); the stage 2 design is #1618 (open, stacked on #1615). |
| FR-SOL-007 (516) | Must | D | Straight pipes and realized bends publish twelve global end rows per member and case (`element_global_end_force_v1`, `element_global_end_moment_v1`) beside their `element_local` rows on PF and EX, each F = Rᵀ f from the published local end rows (PP `lib.rs:12350` `append_element_global_end_results`, called at `:6551`); the readers check them (`result_export/src/global_end_evidence.rs`); tests `core/product_physics/tests/global_end_actions_runtime.rs` (both routes and modes: rotation, nodal balance, bend ends, EX wall axial, PF combinations, readers) and `tests/test_global_end_verifier.py`. Connectors publish global end actions (`:4511`) | DEL-04-01 | Design `global-end-actions.md` (REQ-004, the transform). Source-recovery publications omit the rows by the named rule `global_end_rows_published`. The dormant retained route carries them as named not-covered rows, re-registered in DEL-04-08 §8.20. |
| FR-SOL-008 (517) | Must | D | `core/loads/stress_recovery`; `tests/t4_u6_section_bases.rs:270` | DEL-05-03 | Pressure stresses exist where pressure exists (EX). |
| FR-SOL-009 (518) | Must | P | `core/loads/load_case_algebra`; `preview_physics_runtime.rs:597,682,709` | DEL-05-02 | EX refuses every combination (`pressure_runtime.rs:337-343`; `exact_admission.rs:229`). |
| FR-SOL-010 (519) | Should | D | `core/solver/curved_bend`; DEC-070 | DEL-03-03, DEL-04-07 | |
| FR-SOL-011 (520) | Should | P | SIF → intensified measure (`preview_physics.rs:321-347`); `BRANCH_TOPOLOGY_INVALID` (W-8) | DEL-03-04 | Branch flexibility is not assembled (PP `lib.rs:12861`). EX refuses tees (`exact_admission.rs:205`). |
| FR-SOL-012 (521) | Should | P | As FR-SOL-004: rigid and semi-rigid behaviour by the user's scale, with user dimensions and source notes; component weight at the centre of gravity as a nodal weight force plus r × F moments, replacing the mapped member's distributed self-weight (`self_weight.rs`; W-15 slice b, #1608; R10 convention, owner 2026-10-24) | DEL-03-05 | The eccentric reducer offset remains (slice c). |
| FR-SOL-013 (522) | Should | D | `frame_kernel/src/connector.rs`, `tie_rod.rs`, `joint.rs:727`; `tests/connector_pp_paths.rs` | DEL-03-06 | EX only. `movement_limit` is normalized, not enforced (PP `lib.rs:9378`). |
| FR-SOL-014 (523) | Should | P | `core/solver/nonlinear_supports`; `references/kd5_nonlinear`; the native demo converges | DEL-04-04, DEL-04-07, DEL-09-03 | PF only. Rotational gap and friction refused (`validation.rs:88,100`). |
| FR-SOL-015 (524) | Must | D | `NUMERICAL_INTEGRITY_*` (PP `lib.rs:1198-1230`); health indicator `operation_applier/src/numerical_health.rs`, `ResultsPanel.tsx:97-130`, status bar and Solve panel, with tests (#1544). Observed natively on both routes (§5) | DEL-04-06, DEL-05-04, DEL-07-05 | |
| §12.3 reducers (no row before) | — | P | No eccentric offset vector in `core/product_physics/src` | DEL-03-05 | Part of W-15. |
| §12.5 load types (no row before) | — | P | Wind, seismic and hydrotest categories (PP `lib.rs:14333-14335`) | DEL-05-01 | EX refuses `equivalent_static`; imposed rotations and nozzle movement follow FR-SOL-006. |
| §12.8 near-duplicate nodes (775) | — | D | W-8 with #1574: `NODE_COINCIDENT`, `NODE_NEAR_DUPLICATE` within an absolute tolerance, 5 mm unless `model_settings.node_proximity_tolerance` sets another (`topology.rs:148,281`; read through `PreviewModel::node_proximity_tolerance_m`); a malformed value is refused by name (`validation.rs` `validate_model_settings`); tests `topology_checks_runtime.rs:143,182,193`. The desktop's Project page sets and resets it (`ModelSettingsSection.tsx`; applier `set_model_setting`/`clear_model_setting`, `model_settings_authoring.rs`); through-solve tests `operation_applier/tests/model_settings_authoring.rs`, src-tauri `a_tolerance_set_through_the_apply_command_changes_which_nodes_warn` | DEL-04-06, DEL-02-01 | REQ-04-06-012 (owner) is met on both routes, and a desktop user can see the effective value ("5 mm (default)") and change it. |
| §12.8 verified bounds (783) | — | O | Owner, 2026-10-23: "no verified bounds in v0.1; the retained-precision method stays dormant and owner-held." (`DEL-04-08 Design/b7-plan.md:34`; SOW:336, AX-004) | DEL-04-08 | Dormant code is in `product_physics/src/retained_*.rs`. |
| §22.2 benchmarks (1403) | — | P | 14 of 14: tip force, tip moment, fixed-fixed thermal, simply supported under weight (W9-B, both routes), inclined member, L-frame (W9-A, both routes), U-loop, torsion, anchor displacement (W9-C, EX only), spring, gap, friction, branch, rigid link (W-15, both routes, #1604) | DEL-09-01..03 | Anchor displacement on PF waits for FR-SOL-006 stage 1 (#1615, open). |
| §22.3 stress benchmarks (1422) | — | D | `validation/benchmarks/stress/src/lib.rs:489,513,546,570`; pressure hoop and longitudinal stress in the frozen references `validation/references/t4_u6` (EX); t4_u4b; the suite's pressure family `STRESS-PRESSURE-HOOP-LONGITUDINAL-ORIGINAL` (W-20, #1599: Lamé hoop and radial, closed-end, open-end and restrained membrane, on both section bases, through the exact-pressure preview entry) | DEL-09-02 | The headless runner has no binding for the pressure family (its comparison is the suite's relative check), so it fails closed there. |

### 2.4 Rule packs, reporting, handoff and export (PRD §11.5, §11.7, §11.9, §16–19)

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| FR-RULE-001 (530) | Must | D | Format 0.5.0 (#1629): `schemas/rule_pack.schema.yaml`; validator `core/rules/rule_pack_document/src/format.rs`; per-basis runner `rule_check_runner/src/lib.rs`; row selection `src-tauri/src/rule_solver_selection.rs`; authoring `RulePackManagerPanel.tsx`, `DeclarationsEditor.tsx`, `CheckDefinitionsEditor.tsx`. **Tests:** `rule_pack_document/tests/format_0_5_0.rs`, `rule_check_runner/tests/bases_run.rs`, `rule_solver_selection_tests.rs`, `RulePackManagerPanel.format.test.tsx`, `e2e/r2-smoke.spec.ts` | DEL-06-01, DEL-07-03 | Stress categories, required load cases and load-case mappings (§17.2; owner, 2026-10-24, option A) live in the pack and name the model's own load-case ids. One outcome per check and mapped load case; a missing, unsolved or unselectable basis is incomplete. Other format versions are refused by name, without migration (DEL-06-01 Design `rule-pack-0.5.0.md`). |
| FR-RULE-002 (531) | Must | D | `rule_pack_document/src/lib.rs:1184` calls `check_rule_pack_units` (`:1482`); UI `RulePackManagerPanel.tsx:503-560`; run time `rule_check_runner/src/lib.rs:1286`. **Tests:** `tests/unit_check.rs`, `RulePackManagerPanel.unitCheck.test.tsx`, desktop `lib.rs:8452,8499` | DEL-06-02 | Static findings do not block save or run; an inconsistent check still blocks when it runs. A dimensionless limit declared `1` does not match a ratio formula's `ratio`. |
| FR-RULE-003 (532) | Must | D | `rule_check_runner/src/lib.rs` (`aggregate_rank`, `status_counts`); desktop `RuleCheckRunPanel.tsx` headline; renderer `user_rule_check_aggregate_headline`. Tests: runner unit tests and `tests/point_path_non_finite_run.rs`, `report_renderer/tests/render.rs`, `RuleCheckRunPanel.test.tsx` ("FR-RULE-003 pack headline"); observed natively on both routes (§5) | DEL-06-03 | W-19 (#1585): while any check is incomplete the pack headlines "INCOMPLETE — n check(s) failed; m check(s) blocked", with each check listed (owner reading, 2026-10-23; DEL-06-03 Design `pack-aggregate-incomplete.md`). A check with missing inputs is never evaluated. Under format 0.5.0 the rule applies over per-load-case outcomes, and the counts count them (#1629). |
| FR-RULE-004 (533) | Must | D | `rulePackService.ts:241-284` (private by default); local SQLite | DEL-06-04 | No pack file export. |
| FR-RULE-005 (534) | Must | D | `LibraryManagerPanel.tsx`; desktop `lib.rs:8593`; `tests/test_library_import_provenance.py`; `LibraryApplySection.tsx`, `libraryApply.ts`, applier `library_apply.rs`; tests `libraryApply.test.ts`, `operation_applier/tests/library_apply.rs` | DEL-03-01, DEL-03-07 | Records feed rule checks (desktop `lib.rs:3029`). Applying them to model entities (#1566): stored material and section records insert as new entities or apply to the selected one through one reviewed batch with one undo (material E/ν or E/G mode; a section apply updates its bound pipes). |
| FR-RULE-006 (535) | Should | D | Same panel, component kind; `libraryApply.ts` `buildComponentApply` | DEL-03-02, DEL-03-07 | Applying records (#1566): stored component records apply to an existing component of the matching kind by a fixed source-kind table (apply only; no insert). |
| FR-RULE-007 (536) | Must | D | `tests/test_invented_example_models.py`; `examples/rule_packs/invented_demo.yaml` | DEL-11-04, DEL-06-05 | |
| FR-REP-001 (578) | Must | P | W-3: local-private render (`RenderedReportPanel.tsx`, `reportRenderService.ts`); rule-pack refs, user-rule outcomes, versions, date, settings and coordinate systems (`renderableReportInput.ts`; renderer test `render.rs` `report_context_renders_prd_19_2_identity_settings_and_coordinate_rows`, `:326`). Observed natively (§5). W-18 b2 (#1616): Save Report Package for a Current PF result (`reportPackageRequest.ts`) | DEL-08-01, DEL-08-06 | A public render is blocked for every session (provenance hard-coded private, `renderableReportInput.ts` `sessionProvenance`); the per-report user release (W-18b) is designed (#1622), not built. EX refused for the render and the package (10A); W-11 (a) (#1632) and (b) (#1637) build its sections and admission behind the gate. `assumptions: []`; build id and model coordinates "not recorded"; library refs are W-11 (c) (#1639, open). |
| FR-REP-002 (579) | Must | P | Rule-check section `report_renderer/src/lib.rs:845-904`; §19.3 notice and human-review record `:954-990`; test `render.rs:390` | DEL-08-01 | Reached only in the local-private PF render. |
| FR-REP-003 (580) | Must | P | Provenance notes for session, components and spring hangers (`renderableReportInput.ts` `provenance_notes`, `:560-563`) | DEL-08-03 | Materials, sections and library records absent. W-11 (c) adds them on every route (#1639, open; DEL-08-01 Design `exact-route-report-sections.md` §4). |
| FR-REP-004 (581) | Should | P | Within-run comparison summary: the Comparison line (`ReportPanel.tsx` `reportComparisonLine`, `:224-229`) and the JSON comparison fields (`reportComparisonFields`, `:679`); package placement `stateComparisonHandoffSections.ts:220-238` | DEL-08-06 | No comparison section in the renderer. The local private package for a Current PF result (#1616) carries the selected within-run comparison (#1619) in `state_comparison_handoff_records[].sections.comparison_sections`, or records `comparison_unavailable` beside `sections`; `handoff_sections` is empty. EX packages remain refused. |
| FR-REP-005 (582) | Must | D | `core/reporting/protected_content_linter`; `tests/test_report_protected_content_linter.py` | DEL-08-05 | |
| §19.1 report types (no row before) | — | P | — | DEL-08-06 | No state-comparison, run-comparison or handoff-manifest report a user can reach. |
| FR-HAND-001 (558) | Must | P | W-6a: File › Save Model Document… saves the canonical model document on either route with no solve (`modelDocumentSave.ts`, `model_document_save.rs`); `HandoffPanel.tsx:211-283`, `NativePackagePanel.tsx:217-229` produce preview documents; `core/handoff/exporter/workflow.py:57` is called only by tests | DEL-15-01, DEL-15-03, DEL-17-03, DEL-07-12 | W-6b: File › Save Handoff… writes a verified directory package (model member plus schema manifest) on a saved model state (`handoff_package.rs`, `handoffPackageSave.ts`). Runs are not referenced in v0.1 (`AnalysisRunRef` const). A stored project or state refused at open exports through the recovery export (#1631). Both saves read referenced libraries without a memory lease; #1641 (open) meters them. The preview panel needs a solved PF result; EX refused (10A). |
| FR-HAND-002 (559) | Must | P | W-6b manifest: model hash, units manifest, entity ids, library and rule-pack references, warnings, diagnostics and unresolved assumptions from the document (`handoff_package.rs`; rule-pack references resolved as the solve resolves them, with their exclusion warnings); witness `tests/test_handoff_package_witness.py`; verifier and tamper checks | DEL-15-01 | Hanger library kind has no schema value (`TBD`); run references are empty. |
| §16.1–16.3 handoff contents and workflow (no row before) | — | P | — | DEL-15-01 | Export hash, model hash, rule-pack manifest and entity manifests in schema form (W-6b); the basis model state (W-12 S1); state names, tags and notes (W-12). Run references wait for an `AnalysisRunRef` contract edit. |
| FR-HAND-003 (560) | Should | P | `HandoffPanel.tsx:243` `target_field_coverage: "TBD"` | DEL-15-02 | |
| FR-HAND-004 (561) | Should | P | Loss reports (`HandoffPanel.tsx:187`, PCF) | DEL-15-02, DEL-17-07 | PF only. |
| FR-HAND-005 (562) | Could | D | PCF, MBF, adapter and SDK panels (`App.tsx:1009-1017`); observed natively (§5) | DEL-17-04/07/08/09 | The MBF target version is `TBD` (`CaepipeMbfExportPanel.tsx:38`). |
| Result JSON, stress-neutral | — | D | `App.tsx:1007-1008`; `exactOutputTwins.test.tsx`; observed natively (§5) | DEL-08-04, DEL-17-06 | Both carry the run record's rule-pack exclusion diagnostics (#1602), without duplicating producer diagnostics. Open issues (#1613): the result-export validator does not check diagnostics; the generic stress-neutral validator binds the witness-withholding findings to the package's own provenance, as the Python validator does (the desktop path binds it to the builder's). |
| Local FEA handoff | — | O | DEC-078 (D-12 O-B): FR-025 post-beta (DEL-10-03 SOW:486) | DEL-10-03 | A gated panel exists. |

### 2.5 States, runs, comparison, V&V (PRD §11.6, §15, §21–22)

FR-CMP-001..004 and -006 are in v0.1 by OD-1 (unit W-12, design
`DEL-14-01/Design/desktop-states-runs-comparison.md`). FR-CMP-005, -007, -008, -009
and -010 remain in v0.2 R3 under that design and PRD §24. FR-CMP-011 is not an
MVP requirement (PRD §15.6).

| ID (PRD line) | Pri | Class | Evidence | Deliverables | Notes |
|---|---|---|---|---|---|
| FR-CMP-001 (542) | Must | P | **Store:** desktop `src-tauri/src/model_states.rs` (store v12: `model_states`, `model_state_labels`, immutability triggers; save, list, read, label edit, delete), with its tests there. **UI:** `features/history/HistoryPanel.tsx`, `useModelStateHistory.ts`; `modelStateHistory.session.test.tsx`. **Record:** `model_state.schema.json` record with Python-pinned record hash; `tests/test_model_state_record_parity.py` | DEL-14-01, DEL-07-08 | Save, reopen, tag and delete named immutable states in the desktop (W-12 S1, #1589); SQLite-only, with history export open under OI-015. |
| FR-CMP-002 (543) | Must | D | **Store:** desktop `src-tauri/src/analysis_runs.rs` (store v13, Record Run, list, read, label edit, delete) with `analysis_runs_tests.rs`. **UI:** `features/history/HistoryPanel.tsx`; `recordRun.session.test.tsx`. **Record:** `analysisRunCompatibility.ts` recorded form, `core/analysis_runs/compatibility.py`, `tests/test_recorded_run_record.py`. **Rule packs:** `services/modelRulePackResolution.ts`; `features/workspace/solveRulePacks.session.test.tsx`; fixtures `persistence/transient_run_input_rule_packs.json`, `recorded_run_witness_rule_packs.json` | DEL-14-02, DEL-07-08 | Record Run (W-12 S2, #1596) stores an immutable v0.3 revision tied to a saved state (`{ModelState, id}`), checked against the stored input manifest's model payload. The manifest binds the solver, settings, units and load cases, and many runs can be recorded per state. Library refs come from the shared `library_ref` walk. Rule-pack refs come from the manifest's `active_rule_packs`: at solve the session resolves the model's `rule_pack_refs` against the local rule-pack store (`modelRulePackResolution.ts`), in the model's order; an unresolved or changed reference is excluded and recorded as a run-record diagnostic (`MODEL-RULE-PACK-REF-UNRESOLVED`, `MODEL-RULE-PACK-REF-CHECKSUM-MISMATCH`), kept by the recorded revision under its hash (#1602). The result export, the stress-neutral package and the handoff preview carry them in their own diagnostics, each once (`services/rulePackRefDiagnostics.ts`); Save Handoff resolves the references by the same rules (`handoff_package.rs` `rule_pack_ref_exclusion`, vectors `fixtures/handoff/rule_pack_ref_resolution_vectors.json`). |
| FR-CMP-003 (544) | Must | D | `features/comparison/stateComparison.ts`, `StateComparisonView.tsx`; History panel Compare… (`features/history/`); tests `stateComparison.test.ts`, `compareStates.test.tsx`; parity with `core/comparison/model_state/engine.py` on `fixtures/comparison/model_state_comparison_golden.json` (`tests/test_model_state_comparison_parity.py`) | DEL-14-03, DEL-07-08 | The desktop compares two saved states of one project (W-12 S3a): added, removed, changed and unchanged entities by stable id per family, nested field paths, `unit_changed` without conversion, and a native size admission. View-only; comparison export is v0.2 (FR-CMP-010). |
| FR-CMP-004 (545) | Must | D | `features/comparison/runComparison.ts`, `runComparisonSides.ts`, `RunComparisonView.tsx`; History panel Compare… (`features/history/`); native `admit_analysis_run_comparison` (`src-tauri/src/analysis_runs.rs`); tests `runComparison.test.ts`, `compareRuns.test.tsx`; parity with `core/comparison/analysis_run/engine.py` on `fixtures/comparison/analysis_run_comparison_golden.json` (`tests/test_analysis_run_comparison_parity.py`) | DEL-14-04, DEL-07-08 | The desktop compares two recorded runs of one project, or one and the session's current run (W-12 S3b). Rows map automatically on the reference identity plus row metadata. A mapped pair gets a right − left delta only with equal units, both envelopes `integrity_checked`, the same result semantic identity and a family the reference compares; otherwise it is `not_compared` with the reason. Settings, load-basis and solve-diagnostic differences and unmatched rows are listed. No unit conversion or tolerance; view-only, with comparison export v0.2 (FR-CMP-010). |
| FR-CMP-005, -007 (546, 548) | Should | P | `schemas/comparison_mapping.schema.json`; `model_state/engine.py:232` | DEL-14-05 | No editor. |
| FR-CMP-006 (547) | Must | D | `features/comparison/stateComparison.ts`; `features/comparison/runComparison.ts`; reference `analysis_run/engine.py:229` | DEL-14-03/04 | Automatic mapping in the desktop: states by stable id per family (W-12 S3a), runs by the reference row identity plus row metadata (W-12 S3b). No manual mapping (FR-CMP-005/007, v0.2). |
| FR-CMP-008, -009, -010 (549-551) | Should | P | `schemas/comparison_tolerance.schema.json`; `ComparisonPanel.tsx:55-70` | DEL-14-05, DEL-08-06 | No profiles, overlays or CSV. |
| FR-CMP-011 (552) | Could | P | `schemas/caepipe_external_run.schema.json` | DEL-14-05 | §15.6: not MVP. |
| §21.3 human acceptance (1385) | — | D | `docs/claims_registry.md:6,184-186` | DEL-01-04 | No acceptance workflow, as required. |
| §22.4 regression (1435) | Must | P | `tools/release/run_evidence_sweep.py:163`; last sweep `validation/evidence/sweeps/SWEEP_20260924T162044Z_b9dda2addccc.json` | DEL-00-08, DEL-09-05, DEL-10-04 | The cited sweep predates desktop states and recorded runs (W-12). The sweep is optional release preparation; the hosted `harness` is the merge check. |
| §22.5 prover correlation (1455) | — | O | DEC-080: activation is a future owner-gated row | DEL-09-04, PKG-15 | The schema lacks the §22.5 fields. |
| R6 reproduction (1636) | — | P | Current runnable procedure `docs/validation_manual/headless_runner_reproduction.md:47-193` (W-2); last bundle still `validation/evidence/reproduction/REPRO_DEL0904_20260720T074714Z_a5235340aae3/` | DEL-09-04 | No fresh bundle (the heavy half of W-2). |

### 2.6 Data boundary, local operation (PRD §20)

| ID | Class | Evidence | Deliverables |
|---|---|---|---|
| Public boundary and provenance (§20.1–20.2, no row before) | D (repository level) | `tools/release/run_release_candidate_scan.py`, `export_public_openpipestress.py`; `tests/test_release_candidate_scan.py`, `tests/test_export_public_openpipestress.py` | DEL-12-05, DEL-10-04 |
| Local-first, private paths (§20.3–20.4) | D | SQLite store in Application Support; no `fetch`, `XMLHttpRequest`, `WebSocket` or `sendBeacon` in non-test `apps/desktop/src`, and no HTTP client crate in `src-tauri/Cargo.toml` | DEL-12-01, DEL-12-04 |
| Telemetry (§20.5) | D | `telemetryPolicyService.ts`; `tests/security/test_telemetry_policy.py` | DEL-12-03 |
| Unit system (MVP) | D | `core/units`; `unitConversion.ts`; `ProjectUnitsDialog.tsx` | DEL-02-02 |

`tauri.conf.json:23` sets `"csp": null`. No outbound path was found in code, but
the webview has no network policy.

### 2.7 Class counts, MVP (PRD §23) and milestones (§24)

**Class counts.** The #1539 map at `7a780551f0` had 48 P, 28 D, 3 O and no R.
This map has 35 P, 41 D (including one bounded and one at repository level),
8 O and no R, over 84 rows:
- **P → D (12):** FR-GUI-001 (#1556), FR-GUI-004 (#1563), FR-KNOW-002 (#1559),
  §10.1 step 1 (#1569), the R2 exit (W-4, #1582, after the basis), §12.8
  near-duplicate nodes (the desktop tolerance control, #1593, after the basis),
  FR-CMP-002 (W-12 S2, #1596, with its rule-pack references from #1602),
  FR-CMP-003 (W-12 S3a, #1605), FR-CMP-004 and -006 (W-12 S3b, #1617),
  FR-SOL-007 (W-7, #1581) and FR-RULE-001 (W-17, #1629).
- **D → P (1):** FR-SOL-002. Its acceptance criterion includes imposed
  displacements, which pass on EX only; the route rule now applies (Codex, §6).
  (FR-RULE-003 moved D → P by the owner's reading of 2026-10-23 and back to D
  with W-19, #1585.)
- **P → O (5):** FR-KNOW-001, -003, -004 and -005 (OD-1/OD-3); FR-AGENT-005
  (OD-5).
- **P → D (bounded) (1):** FR-MOD-007, by the owner's reading of 2026-10-23.
- **New rows (5):** §12.3 reducers, §12.5 load types, §16.1–16.3 and §19.1 (P);
  §20.1–20.2 (D).
- **Reason changed, class kept:** FR-CMP-001..006 lose "scope unclear" (OD-1);
  FR-SOL-015 now includes the health indicator.

**§23 MVP items:**
- **Implemented:** 27 of 28 items, 26 with desktop paths and the initial
  validation suite headless (`ValidationEvidencePanel` shows an inventory and
  does not run it). Imposed displacement works on EX only; combinations on PF
  only. Rigid elements
  are DEC-045 stiffness scaling with component weight on both routes (W-15 a, b
  and d: #1604, #1608), without the eccentric reducer offset (W-15 c).
  Canonical model package export is File › Save Model Document… (W-6a, #1588)
  and File › Save Handoff… (W-6b, #1600), without run references.
- **Partly available in the desktop:** basic report generation. The local private PF
  render (W-3) and the local private PF report package (W-18 b2, #1616) exist;
  EX reports stay behind the gate (W-11 a and b: #1632, #1637), and no report
  is shareable (W-18b designed, #1622).

**§24 milestones, factually.** Each entry says which of the milestone's
deliverables exist. Milestone judgment is the owner's; this map records none.
- **R0:** its deliverables exist: the model schema and unit system, the
  straight element, the linear solver, the headless runner's command line, and
  the cantilever and fixed-fixed thermal benchmarks (§2.1, §2.3).
- **R1:** partly. Rigid elements are DEC-045 stiffness scaling with component
  weight (W-15 a, b and d: #1604, #1608), and §22.2 has the rigid link (#1604);
  the eccentric reducer offset remains (W-15 c). Imposed displacement passes
  on EX only (FR-SOL-002; #1615, open).
- **R2:** DEC-035 (D-14) advanced the target stage to R3 while reserving the
  R2 milestone judgment for the human (`execution/_Decomposition/SOFTWARE_DECOMP.md:645`).
  The native smoke now runs a GUI-authored model through solve, review, save
  and reopen (W-4).
- **R3 (States, Runs, Comparison):** partly. States, run history and basic state and run comparison are in the desktop (v0.1 by OD-1; W-12 S1–S3c). Mapping editor/manual mappings, tolerance profiles, graphical diffs and comparison export remain in v0.2 R3.
- **R4** and **R5:** DEC-048 (D-23) accepted exit evidence for target-stage
  advancement; DEC-054 (D-27) accepted a conditional R4 gate, with §16.2/§16.5
  evidence obligations remaining (`SOFTWARE_DECOMP.md:658,664`). These
  historical rulings do not establish current milestone acceptance. A report
  is obtainable only as a local private PF document or package (W-3; W-18 b2,
  #1616).
- **R6:** partly. Design knowledge is deferred (OD-3); no fresh reproduction
  bundle. File › Save Handoff… writes a verified handoff package (W-6b, #1600).
- **R7:** partly. Offline proposals are delivered; candidate generation is
  absent.

### 2.8 Coverage gaps in the deliverable set

**No user outcome reaches these deliverables directly.** They provide
architecture, governance or contract basis:
- DEL-00-01, DEL-00-02, DEL-00-04, DEL-00-07;
- DEL-01-01, DEL-01-03;
- DEL-02-03, DEL-02-04;
- DEL-10-01, DEL-11-03, DEL-12-05, DEL-17-01;
- DEL-15-04 and DEL-17-05 (external-prover loop, owner-gated).

**No deliverable owns these outcomes:**
- **Formats and stores:** the desktop project store (partly DEL-12-01).
- **Model and inspector:** inspector dependencies and assumptions.
- **Records:** the §22.5 correlation-record fields; the R3 exit review.

Since the previous map, DEL-02-01 owns the desktop model document format
(#1554), DEL-04-06 owns topology and near-duplicate node checks (W-8,
REQ-04-06-012), DEL-02-01 owns the "lines" entity (Design
`model-document-0.7.0.md` §3.2, W-13), and DEL-03-05 owns the rigid link and component weight (its
`deliverable.yaml` names `rigid_component.rs`, `self_weight.rs` and the W-15
tests) and designs the eccentric reducer offset (Design
`rigid-component-stiffness-scaling.md` §4).

## 3. Reconciliation drift

The W-1 sweep (#1540–#1546, #1550, #1557, #1560, #1575) fixed the previous
map's pointer and ScopeOfWork items, including those for DEL-06-01, DEL-07-01..08,
DEL-08-01/02/05, DEL-15-01/03, DEL-17-03/04/07/08, DEL-02-01, DEL-02-05,
DEL-03-04/05/08, DEL-05-05, DEL-09-01..03, DEL-14-01/03..05, DEL-16-04, DEL-01-04
and DEL-11-02/03/05. W-2 (#1543) fixed the validation manual items. The rows
below are what remains or is new at this basis.

**Fixed with the re-baseline (#1580)** [fix]:
- `docs/user_guide/index.md`: said the rendered report is always blocked and
  that a blank project starts in SI. It now describes the local-private render,
  its content, and the units dialog.
- DEL-03-05 SOW Attributes: "Realization also includes the DEC-045 product
  route … with candidate-bound evidence" contradicted the current-implementation
  paragraph; it now says the route validates but does not apply the scaling.
  The paragraph's basis and `validation.rs` line range are current.
- DEL-02-02 `deliverable.yaml`: `code_paths` add `features/project-units/**`
  and `projectService.ts` (its checks already listed the tests).
- DEL-15-02 `deliverable.yaml`: `code_paths` add `HandoffPanel.tsx` and
  `PcfExportPanel.tsx` (the loss reports).
- DEL-12-01 `deliverable.yaml`: `code_paths` add `tauri.conf.json` (the CSP
  setting).

- `DEL-02-01/Design/model-document-0.7.0.md:51-52` said `schemas/model.schema.yaml`
  "describes an older shape … The bundled demo fails it with 11 errors", stale
  since #1554. It now records that state as before S1a.
- `DEL-02-02/Design/project-unit-selection.md` §1 "Where things stand" ("Blank
  projects fix SI", "No `angle` key is written") described the state before
  slice (a). It is now headed as the starting point, with one sentence on what
  slice (a) changed. Without this, the §10.1 row would be R (Codex, §6).
  #1565 and #1566 edit other hunks of these two files.

**Done in #1574** [fix]: `DEL-04-06/Design/model-topology-checks.md` and
REQ-04-06-012's verification row (SOW:189) carry the implemented wording.

**Still open** [fix]:
- **Release-notes draft** (`docs/RELEASE_NOTES_v0.1.0_DRAFT.md`, release lane;
  release is parked):
  - `:102` "Rendering is refused when the public-report redaction control would
    have to withhold values." The public render is blocked for every session,
    and the local-private render (with rule-check and run context) is not
    mentioned.
  - `:106` lists glTF review geometry under "For pressure-free results also".
    `exactCurrentPanels.test.tsx:7-8,153-157` offers it for exact Current
    results too. The §5 probe saw no glTF action on either route, because the
    byte-exact downloads are withheld.
- **Pointers:** DEL-10-04 lists `software-workflow.json` and `tools/ci/**` but
  not the root `.github/workflows/piping-*.yml`. DEL-07-02/05/08 still list the
  unused `core/gui/*` reference modules beside the desktop paths. DEL-13-03
  names only Python for connectivity; the product check is DEL-04-06's.
- **Corpus-wide retired paths:** "Sources:" prose and the line-12
  "Reconciliation evidence" prose of 81 SOWs cite `execution/_Reconciliation/…`
  without annotation. These are outside #1550 and row 26 of the previous table.
  Identification and Attributes boilerplate stays as written (Agent 0,
  2026-10-23).

**Dependency declarations** (`python3 -m tools.deliverables --project
projects/chirality-piping check` at `df14318ec7`). No structural errors. The
`unknown` list had 14 needs whose supplier the tool cannot observe; this
change resolves one, and 13 remain. These are facts about the declarations,
not about whether any condition is met.

[fix] DEL-02-02 `needs[12]` named `doc:core/units module contract`, a path left
`TBD` because the module layout was not fixed. The contract is
`core/units/README.md` ("OpenPipeStress Unit Core Contract"), which DEL-02-02
`ScopeOfWork.md:65` names as the unit catalog's current realization. The need
now names that path; its condition is unchanged apart from the note.

Recorded, not resolved; each would need a condition or target that the
evidence does not give:

| Need | Target | Why it stays unknown |
|---|---|---|
| DEL-01-01 `needs[5]`, DEL-12-05 `needs[14]` | `doc:docs/DIRECTIVE.md` | Retired in `48584391de` ("archive reviewed obsolete docs"); Git holds it. Its founding intent, stop rules and governance baseline have no single successor document; `docs/PROFESSIONAL_BOUNDARY.md`, `docs/IP_AND_DATA_BOUNDARY.md` and Root `docs/PRODUCT_BOUNDARIES.md` each carry part. Choosing among them changes the need's meaning. |
| DEL-01-01 `needs[7]` | `doc:docs/AGENTIC_DEVELOPMENT_WORKFLOW.md` | Removed in `48584391de` (an earlier version in `cc1b91c5b8`); Root `AGENTS.md` and the loop now govern agent work. No document carries its "draft until human gate acceptance" condition as written. |
| DEL-17-07 `needs[12]` | `doc:plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md` | Retired in `349a2ab338` ("archive legacy coordination files"); DEL-17-07's ScopeOfWork still cites its section 5. No successor is named. |
| DEL-17-07 `needs[13]`, DEL-17-08 `needs[13]` | public URLs (CAEPIPE PCF translator; Khronos glTF 2.0) | The tool resolves project paths only; a URL is never observed. Recording them as `external:` would be more accurate and would still be unknown. |
| DEL-01-02 `needs[6]`, `[7]`; DEL-01-04 `needs[7]`, `[8]`; DEL-02-02 `needs[8]` | `external:` human, legal or project-authority review | Human acts by design; the DEL-02-02 note says the target is "intentionally unresolved to avoid inventing an authority". |
| DEL-17-05 `needs[10]` | `external:CAEPIPE-EXECUTABLE` | A user-provided licensed executable, by design. |
| DEL-02-02 `needs[11]` | `unknown` (downstream unit consumers) | A class of consumers, not one target. The 40 deliverables that declare a need on DEL-02-02 are its native consumers, derived by `neighborhood DEL-02-02`. |

**Dependency cycle.** One strongly connected group of nine: DEL-04-07,
DEL-04-08, DEL-05-02, DEL-08-01, DEL-08-04, DEL-08-05, DEL-09-05, DEL-10-04
and DEL-10-05 (the same group as at `7a780551f0` and `8a8a8b2584`). Edges are
supplier → consumer, with the consumer's need index:
- **Core, mutual by design:** DEL-04-07 ↔ DEL-04-08 (04-07 `needs[11]`,
  `[26]`; 04-08 `needs[1]`), DEL-04-07 ↔ DEL-05-02 (04-07 `needs[10]`, `[25]`;
  05-02 `needs[0]`) and DEL-04-08 ↔ DEL-05-02 (05-02 `needs[1]`; 04-08
  `needs[5]`). The product solve hosts the retained method's
  dispatcher, the retained tables mirror the ordinary route's semantics, and
  the base reader reads both (DEL-04-08 Design `b7-plan.md`). These are
  co-designed interfaces; the cycle among the three is intended.
- **Outer ring:** DEL-04-07, DEL-05-02, DEL-04-08 → DEL-08-04 (`needs[12]`,
  `[13]`, `[14]`) → DEL-08-01 (`needs[14]`) → DEL-08-05 (`needs[9]`) →
  DEL-09-05 (`needs[7]`) → DEL-10-04 (`needs[7]`) → DEL-10-05 (`needs[3]`;
  also DEL-08-04, DEL-04-07, DEL-05-02, DEL-04-08 → DEL-10-05, `needs[2]`,
  `[10]`, `[11]`, `[12]`) → DEL-04-08 (`needs[9]`, non-gating).
- **The one closing edge.** Only DEL-10-05 → DEL-04-08 (`needs[9]`: "The
  headless runner hosts the reader's CLI binding (`openpipestress-runner
  read`). Python product code takes the reader's verdict through it.") returns
  from the ring to the core. Without it the group is the three-member core.
  The edge is true (`b7-plan.md` "Product callers"), but the dependency it
  states belongs to the Python product callers (`core/analysis_runs/`,
  DEL-14-02, whose `deliverable.yaml` names `core/analysis_runs/compatibility.py`
  and declares no need on DEL-10-05), not to DEL-04-08's own method. Proposal,
  not applied: move it to DEL-14-02 as a need on DEL-10-05 (computed over the
  declared edges, that leaves only the three-member core and forms no new
  cycle), or keep it and record the ring as intended. Question for Agent 0.

**Owner-reserved text (exact old → new).** These change commitment,
scope or acceptance wording. "Rec." is the recommendation.

| # | Location | Old | New | Reason | Rec. |
|---|---|---|---|---|---|
| 1 | `apps/desktop/native-smoke/expected.json`, milestone `sparse_interactive.rows` | `98` | `113` | #1461 (T4-U4b/U5b) adds 15 σ±/shear rows per member per case (`DEL-04-07 Design/u4b-u5b-implementation.md:296`); milestone: 1 member × 1 case | Applied (owner, 2026-10-24: "I accept your recommendations for each of these three: G10, W-12, W-18.") Then `113` → `125` with W-7 (#1581: 12 global end rows per member per case; owner, 2026-10-25: "I approve W-7's native-smoke values"). |
| 2 | same, milestone `dense_scrutiny.rows` | `99` | `113` | #1461 +15; #1387 (B7 E14) deleted the dense parity row, −1 (`DEL-04-08 Design/b7-plan.md:292`) | Applied (owner, 2026-10-24: "I accept your recommendations for each of these three: G10, W-12, W-18.") Then `113` → `125` with W-7 (#1581: 12 global end rows per member per case; owner, 2026-10-25: "I approve W-7's native-smoke values"). |
| 3 | same, milestone `sparse_interactive.probe_entered` | `"Entered: 0.09426732782247198 mm"` | `"Entered: 0.09426732782247199 mm"` | #1387 (B7 E15): one correctly rounded `norm3` (`b7-plan.md:293`); one unit in the last printed digit. The dense value is unchanged | Applied (owner, 2026-10-24: "I accept your recommendations for each of these three: G10, W-12, W-18.") |
| 4 | same, demo `sparse_interactive.rows` | `625` | `745` | #1461 +120 (4 members × 2 cases × 15) | Applied (owner, 2026-10-24: "I accept your recommendations for each of these three: G10, W-12, W-18.") Then `745` → `841` with W-7 (#1581: 12 global end rows × 4 members × 2 cases; owner, 2026-10-25: "I approve W-7's native-smoke values"). Then `841` → `837` with the C-120 fix (#1620: its 4 intensified rows removed; owner, 2026-10-25: "Both decisions I approve your recommended options."). |
| 5 | same, demo `dense_scrutiny.rows` | `627` | `745` | #1461 +120; #1387 −2 parity rows (one per case) | Applied (owner, 2026-10-24: "I accept your recommendations for each of these three: G10, W-12, W-18.") Then `745` → `841` with W-7 (#1581: 12 global end rows × 4 members × 2 cases; owner, 2026-10-25: "I approve W-7's native-smoke values"). Then `841` → `837` with the C-120 fix (#1620: its 4 intensified rows removed; owner, 2026-10-25: "Both decisions I approve your recommended options."). |
| 6 | DEL-09-01 SOW:69 | "The future mechanics benchmark suite must stay aligned…" | "The mechanics benchmark suite must stay aligned…" | The suite exists (`validation/benchmarks/mechanics`, W-9) | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 7 | DEL-09-01 SOW:135 | "This deliverable specifies setup evidence for a future mechanics benchmark suite covering…" | "This deliverable specifies the contract and evidence basis for the implemented mechanics benchmark suite covering…" | as #6 | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 8 | DEL-09-02 SOW:81 | "This setup kit defines the future benchmark-suite boundary only. It does not create benchmark source files, implement tests, …" | "The original setup kit defined the benchmark-suite boundary only. It did not create benchmark source files, implement tests, …; the suite now exists in `validation/benchmarks/stress`." | the suite exists | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 9 | DEL-09-02 SOW:126 | "This deliverable specifies setup evidence for a future stress recovery benchmark suite. It covers benchmark planning for…" | "This deliverable specifies the contract and evidence basis for the stress recovery benchmark suite in `validation/benchmarks/stress`. Its required coverage remains …; implemented fixture coverage is recorded in the suite's fixture inventory." | as #8 | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 10 | DEL-09-03 SOW:108 | "…the setup surface for a future nonlinear support regression suite…" | "…the contract and evidence basis for the implemented nonlinear support regression suite…" | conflicts with its own current-implementation paragraph | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 11 | DEL-08-03 SOW:81 | "The future report section is expected to be a report-renderer subsection…" | "The report section is a report-renderer subsection…" | ships, as its `:99` says | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 12 | DEL-08-06 SOW:343 | "ASSUMPTION: the future implementation should assemble sections…" | "ASSUMPTION: the implementation should assemble sections…" | `report_package` exists | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 13 | DEL-06-02 SOW:77 (Determinism) | "Future implementation must produce repeatable results…" | "The implementation must produce repeatable results…" | evaluator ships | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 14 | DEL-14-02 SOW:170, :320 | the "PRD v0.2 … not locally accessible" source row / "the PRD source text was not locally read in this task" bullet | Source "PRD analysis-run requirements", status "Current primary source: docs/PRD.md §§8.7, 11.6 (FR-CMP-002), and 15.2", with resolution guidance / "Use `docs/PRD.md` §§8.7, 11.6 (FR-CMP-002), and 15.2 for analysis-run requirements; retain explicit TBDs…" | `docs/PRD.md` is present | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 15 | DEL-14-01 SOW:342 (DEL-14-01:3); DEL-15-01 SOW:387 (DEL-15-01:2) | "(stage-gated: v0.2 R3) " / "(stage-gated: v0.2 R6; Owner ruling," | deleted / "(Owner ruling," | the tag and the ruling read as mixed signals | Applied (owner, 2026-10-23: "I approve items 6-15 in the form above.") |
| 16 | DEL-15-01 SOW:183 (V-02) | "Confirm all non-trivial schema requirements trace to `_CONTEXT.md`, decomposition, …" | "… trace to `_CONTEXT.md` (retired in `497a8d81e4`; see Git history), decomposition, …" | the row-26 annotation, in a verification check cell | Apply — **Applied** (Agent 0, 2026-10-24, under the row-26 rule; #1582) |

**Previous table, now closed.** Rows 1, 3–21, 23, 24 and 26 are applied. Row 2
stays not applied by the owner's ruling (FR-SOL-006 is built on PF instead), and
row 22 stays Leave. Row 25 (`expected.json`) is rows 1–5 above, now with each
cause named.

**Owner readings recorded** (owner, 2026-10-23: "I accept your other
recommendations for the matters you needed from me"):
- **PRD §14.4 topology:** "topology invalid" is topology that prevents the
  mechanics being formed (unknown pipe endpoints, unsupported parts, invalid EX
  pressure-region chains), which already blocks. W-8's other findings are
  warnings and REQ-04-06-012 stands (DEL-04-06 Design `model-topology-checks.md`).
  Two follow-ons go to the numerical lane: the malformed-branch warning will say
  the component's branch stress factors are still applied, and the bundled
  demo's malformed tee C-120 is fixed.
- **FR-MOD-007:** D, bounded to the live derivation of `BuiltModel`; the PKG-13
  transform contract stays deferred (§2.1).
- **FR-RULE-003:** the aggregate headlines INCOMPLETE while any check is
  incomplete (DEL-06-03 Design `pack-aggregate-incomplete.md`; built in W-19).

**Further SOW wording, applied** (owner, 2026-10-23: "I approve the 24 items as
above (14 as drafted, 9 amended, and the :110/:117 alternative in place of
:114)"): stale "future" and setup-only wording in DEL-09-01, DEL-09-02,
DEL-09-03, DEL-08-03, DEL-08-06 and DEL-06-02, with still-open `TBD`s, held
choices and obligations for new cases kept.

**Owner notes (not text changes):**
- DEL-04-03 R01 (imposed displacement) states a ruled commitment that the
  code does not yet fully meet on PF. It is disclosed, and the work is in
  flight (FR-SOL-006 stages: #1615 and #1618, open). REQ-04-06-012 (5 mm the
  user can change) now has its desktop control (#1593).
- DEL-13-03-R1 (deferred PKG-13) still commits connectivity, which DEL-04-06
  now delivers.

## 4. Proposed work plan

### 4.1 Ready for development testing now

These outcomes have a desktop path that development testing can exercise
today. Most are class D; where the row is P, the item names the part that
exists:
- **Model and project:** open, save and reopen model documents and projects;
  choose project units at creation and change them later; refusal of
  documents without project units, and the recovery export (#1627, #1631).
- **Authoring:** nodes, pipes, materials, sections, bends, joints, supports,
  load cases and combinations; split, copy, rotate, mirror and reconnect; undo
  and redo; the 0.7.0 document slots (W-13). A from-blank model solves
  natively (§5).
- **Rigid components (FR-SOL-004/012, P):** stiffness scaling and component
  weight on both routes (W-15 a, b and d); not the eccentric reducer offset.
- **Solving:** PF solve, including nonlinear supports, wind, seismic and
  combinations; EX solve; pre-solve topology warnings; refusal of load cases
  that apply nothing; named memory refusals (#1638).
- **Results:** results table, standing, numerical health indicator,
  diagnostics, deformed shape, result colour and reaction arrows.
- **History:** model states, recorded runs, and state, run and within-run
  comparison (W-12).
- **Reports (FR-REP-001, P):** the local-private rendered report and report
  package for PF results.
- **Proposals and data:** offline proposals; libraries and applying their
  records.
- **Rule packs:** format 0.5.0 authoring, static unit check and per-load-case
  rule-check runs.
- **Model export (FR-HAND-001/002, P):** Save Model Document and Save Handoff;
  runs are not referenced.
- **Exports:** result JSON and stress-neutral JSON (both routes); PCF and MBF
  package documents and the other PF export panels. Stress-neutral CSV, glTF,
  PCF text and MBF text are withheld by the desktop.
- **Boundaries:** local-only storage and telemetry.

The native smoke's stale `expected.json` values (§3 rows 1–5) are applied,
with the later W-7 and C-120 values. The smoke passed 135 of 135 checks on the
heads of #1627, #1631 and #1634 (as their pull requests record).

These are **not ready**: shareable or EX reports and EX report packages, the
eccentric reducer offset, EX combinations, PF imposed displacement (#1615,
open) and run references in the handoff package.

### 4.2 Owner decisions that shape the plan

These are reserved because they concern v0.1 scope, commitments or a hold.

**OD-1 to OD-5 decided.** Owner, 2026-10-23: "I approve OD-1 through OD-5 as
you recommended." Each outcome is in the row's **Decided** entry. OD-6 was
decided the same day (option B), and rows 2 and 23 of the §3 table were then
ruled separately (see the OD-6 row).

| # | Decision | Consequence |
|---|---|---|
| OD-1 | Does D-11's "W7 — Forward horizon v0.2" placement (PKG-13/14/15/16/17) mean outside software 0.1.0, despite PRD §23 listing states, runs tied to states, state and run comparison, and canonical model export in the MVP? | **In:** unit W-12 (L) and W-6 come before validation. **Out:** a ruling, and PRD §23 and the release-notes text follow it. Either answer also settles OD-3 for PKG-13. **Decided:** states, run history, state and run comparison and canonical model export are in v0.1 (W-12, W-6). PKG-15 handoff stays in for model export. PKG-13, further PKG-16 agent features and further PKG-17 export formats are deferred to v0.2; the DEL-16-01/02 offline intake and the DEL-16-06 operation-application seam ship as built. PRD §23 stays as written. |
| OD-2 | Rigid elements (FR-SOL-004, Must, MVP) | **Options:** build DEC-045's stiffness scaling (M); build a dedicated rigid element and offsets, which reopens DEC-045 (L); or defer by ruling. **Decided:** implement DEC-045 stiffness scaling (W-15). |
| OD-3 | Design-knowledge entry and constraint validation (FR-KNOW-001, Must; R6) in v0.1? Settled with OD-1 if the W7 reading applies. | **In:** W-14 (L). **Out:** a ruling. **Decided:** design knowledge is deferred to v0.2. |
| OD-4 | Which model format is canonical: the desktop 0.6.0 document or `schemas/model.schema.yaml`? (FR-MOD-001/004/006) | Fixes the target for W-13, a new document version under the one-version rule. **Decided:** the desktop model document is canonical, and `schemas/model.schema.yaml` is updated to describe it (W-13). |
| OD-5 | Viewport result overlays and reaction arrows (FR-GUI-001, Must); the R7 staging of the FR-AGENT-005 claim scan (DEL-16-04:3) | Each is either an S–M unit or a ruling. **Decided:** viewport overlays and reaction arrows are built now; FR-AGENT-005 stays R7. |
| OD-6 | Owner-reserved text in §3 | Apply as proposed, amend, or leave. **Decided (owner, 2026-10-23, "OD‑6, option B (I want to discuss 2 and 23 more)."):** the 22 Apply rows are applied. Owner, 2026-10-23: "Row 2 I approve option A and Row 23 I approve your recommendation." Row 2 is not applied (the requirement stays; imposed displacement is to be built on the pressure-free route, linear first, then with nonlinear supports); row 23 is applied. |

Also decided on 2026-10-23 and recorded in the governing text: the 5 mm
node-proximity tolerance, user-settable (REQ-04-06-012); no verified bounds in
v0.1 (`DEL-04-08 Design/b7-plan.md`); the W-10 reconnect limitation
(DEL-16-06 SOW:79).

**Owner question (Agent 0, 2026-10-26):** a command to delete a stored local
project, such as a blank orphaned by a superseded New Blank (#1640's "Open").
Neither the PRD nor any ScopeOfWork commits to one, so it would be a scope
addition. Until it is decided, a stored blank stays in the store and is
reached through List Local Projects.

Opening exact-route reports and handoff needs no new decision to start. Ruling
10A already directs DEL-08-01 to design their limitation sections. Opening the
surfaces afterwards returns to the owner.

### 4.3 Units

The lane is heavy where builds or numerical checks are needed and light for
documents. Heavy work that changes numerical meaning or persistence needs
targeted regression checks and independent scrutiny (Root `AGENTS.md`).

**Done on main** (evidence; the owner's acceptance is separate):

| # | Unit | Evidence |
|---|---|---|
| W-1 | Pointer and ScopeOfWork reconciliation sweep | #1540–#1546, #1550, #1557, #1560, #1575; remaining drift in §3 |
| W-3 | Rendered report for local private sessions, with §19.2 content | #1553 (+#1555); observed natively (§5) |
| W-5 | Memory-pool headroom (transient free-queue dip) | #1547; the demo result-JSON save succeeded in the smoke and the probe (§5); headroom counting reclaimable file-backed and purgeable pages, and the growth and take re-samples (owner, 2026-10-26), are #1636 |
| W-8 | Pre-solve topology and near-duplicate warnings | #1559; the absolute 5 mm, model-settable tolerance and the branch warning's applied-factor statement are #1574; the desktop control that sets and resets the tolerance is #1593 |
| W-9 | Missing benchmarks: L-frame, simply supported weight, anchor settlement | #1548; the rigid link is W-15 (#1604) |
| W-10 | Pipe reconnect | #1563, with its declared limitation |
| — | Viewport result colour and reaction arrows (OD-5) | #1556 |
| — | Numerical health indicator (FR-SOL-015 display) | #1544 |
| — | Refusal of load cases that apply nothing (silent zero) | #1568 |
| — | Strict inputs: no silent drops of authored input or combination rows (PF closed records, `UNKNOWN_MODEL_FIELD`; duplicate terms and withheld combination rows named) | #1573 |
| W-17 (part) | Project units at creation; static rule-pack unit check | #1569, #1570 |
| W-17 (b) | Changing project units after creation: `set_project_unit` and the Project units section | #1627 |
| W-17 (rule packs) | Rule-pack format 0.5.0: stress categories, load-case mappings and required load cases; per-load-case outcomes, also in the report | #1629 |
| W-2 (part) | Validation manual current procedure, user guide, SMOKE note | #1543; the user guide updated again in #1580 after W-3 and W-17 |
| W-19 | Rule-check aggregate headlines INCOMPLETE while any check is incomplete (FR-RULE-003) | #1585 |
| W-7 | Global-frame element-end forces (FR-SOL-007): twelve global end rows per member and case on PF and EX, their readers and verifiers; the retained route's re-registration (DEL-04-08 §8.20) | #1581 |
| W-13 S1b | Model document 0.7.0: the new member slots, one document validator, `model_settings.node_proximity_tolerance` (default 5 mm) | #1564; native smoke with no change beyond the five stale `expected.json` values (§3 rows 1–5) |
| W-13 S2a | Authoring for the 0.7.0 slots: lines, assumptions and open issues, constraints, equipment interfaces, rule-pack references, tags, notes and provenance records; validator findings in the desktop | #1565 |
| W-13 S2b, W-17 (part) | Applying library records to model entities: material (E/ν or E/G), section (propagated to bound pipes) and component records, with `provenance_record`/`library_ref` and the store's unresolved/changed-record warnings | #1566 |
| W-12 S3a | Comparing two saved model states in the desktop: fail-closed flattening of every 0.7.0 member, stable-id classification, field paths, parity with the reference engine | #1605 |
| W-12 S3b | Comparing two runs in the desktop: automatic row mapping, the whole-run standing gate, deltas with units, context and diagnostic deltas, exactness and S2-era refusals, parity with the reference engine | #1617 |
| W-12 S3c | "Within this run" selects its load case and combination from the bases with result rows, held to the current run | #1619 |
| W-12 S2 | Analysis runs recorded against saved model states (store v13, Record Run with a checked manifest and model binding, run labels, recorded-form validators in TS and Python), with stored-length read admission for states and runs | #1596 |
| W-12 S1 | Named immutable model states in the desktop (store v12, Save/Open State, History panel with labels); one unsaved-changes guard for Open Project, New, Open Model Document and Open State | #1589 |
| W-20 | Pressure stress benchmark family in the DEL-09-02 suite | #1599 |
| W-4 | From-blank native journey and the output gates as permanent native-smoke checks | #1582: 25 checks, all passing on its head; no `expected.json` change |
| W-6a | File › Save Model Document…: the canonical model document on either route, with no solve (FR-HAND-001) | #1588; dialog focus #1614 |
| W-6b | File › Save Handoff…: a verified handoff directory package with its manifest on a saved model state; rule-pack references resolved as the solve resolves them (FR-HAND-001/002) | #1600; export diagnostics #1613 |
| W-15 a+d | DEC-045 stiffness scaling on both routes, EX admission of valve, flange, rigid and specialty components, reference-section identification of body stress rows, rigid-link benchmark | #1604 |
| W-15 b | Component weight at the centre of gravity as a nodal weight force plus r × F moments (R10) | #1608 |
| W-18 a, b1, b2 | Report package 2.0.0 over current results: the Rust producer, reader and runner witness; native admission and disposition screening of the save; Save Report Package for a Current PF result, exact routes refused | #1597, #1606, #1616; ingress lease #1621 |
| W-18b (design) | Per-report user release of the user's own project data: the design only; nothing built, no release recorded | #1622 |
| W-11 (design, a, b) | Exact-route report sections: the design; slice (a), the statement table, renderer sections and dormant package checks; slice (b), the desktop exact sections, admission and native source binding. All behind the gate | #1628, #1632, #1637 |
| W-17 (units at open) | A model document, stored project or saved state without project units is refused by name at open; the entity editors refuse a missing key by name; the recovery export of a refused stored project or state | #1631: 135 of 135 native-smoke checks on its head |
| W-17 (native smoke) | The smoke builds what it launches (WASM engine and app binary content stamps), holds a per-worktree build lock, and reports a failed solve or memory refusal by name instead of timing out | #1634: 135 of 135 on its head |
| W-17 (New Blank) | Only a model or project change supersedes a pending New Blank; a superseded one is named `NEW-BLANK-SUPERSEDED` with the stored blank's name and id and the List Local Projects route; the smoke driver waits for the blank's session | #1640 (merged as `9d51a4e744`) |
| W-17 (solve refusals) | The Solve panel and the Solve job JSON name each memory refusal's point, exact code and retry path; "available memory" wording as #1636 counts it | #1638 |
| — | Bundled demo without the malformed tee C-120 | #1620 |

**In flight** (open pull requests on 2026-10-26, rechecked after #1640 merged;
refresh at each map update, and give the merge of any that has merged):

| PR | Unit | Rows it addresses |
|---|---|---|
| #1615 | W-16 a: imposed displacement on PF, stage 1, linear (draft, waiting for its D3 re-pricing turn) | FR-SOL-006, FR-SOL-002, §22.2 |
| #1618 | W-16 stage 2 design: imposed displacement with nonlinear supports (stacked on #1615) | FR-SOL-006 |
| #1639 | W-11 (c): material, section, component, support and library records in reports on every route (behind the exact-route gate) | FR-REP-003, FR-REP-001 |
| #1641 | Numerical lane (routed from W-17): the library reads of Save Model Document and Save Handoff are metered | FR-HAND-001 |
| #1625 | Exact unit factor-sum rule for the constant-effort combination gate | none (a PF combination gate, DEL-05-02) |
| #1630 | Closing the nested PF input records | none (follows #1573, strict inputs) |
| #1567 | DBM concordance review | none |

**Remaining:**

| # | Unit | Size | Kind | Lane | Depends on | Open PR | Owner? |
|---|---|---|---|---|---|---|---|
| W-2 (rest) | Fresh R6 reproduction bundle at the validation basis, with the current procedure | S | run | heavy | the validation basis | none | Acceptance of the reproduction is the owner's |
| W-11 (rest) | Slice (c), FR-REP-003 on every route; then opening the exact-route reports | M (c), about 0.3k (opening) (DEL-08-01 Design `exact-route-report-sections.md` §6) | desktop + Rust | heavy | (a) and (b), done | #1639 (c) | Opening returns to the owner |
| W-15 c | Eccentric reducer offset with the 0.8.0 model document (§12.3) | S–M | numerical + schema | heavy, scrutiny | the 0.8.0 document coordination | none | No |
| W-16 | Combinations on EX (FR-SOL-009); imposed displacement on PF, stage 1 linear, then stage 2 with nonlinear supports (FR-SOL-006, owner's row-2 ruling; its PF benchmarks also close FR-SOL-002); `equivalent_static` on EX (§12.5) | M | numerical | heavy, scrutiny | — | #1615 (stage 1), #1618 (stage 2 design); none for EX combinations or `equivalent_static` | No |
| W-17 (rest) | First, guard the Save Handoff state-list failure catch (`workspaceSession.ts:2552`) as its success path is guarded (`:2558`), so a stale failure cannot overwrite a newer status message. Then a DEL-02-02 design for the temperature and acceleration units of the load fields (the `K` and `m/s^2` defaults, `PropertyInspector.tsx:2237,2247` and the grid columns) and the export panels' unit fallbacks (`CaepipeMbfExportPanel.tsx`, `LocalFeaHandoffPanel.tsx`) | not sized | desktop; design + desktop | desktop | — | none | No |
| — (numerical lane) | Metering the `load_library` reads of Save Model Document and Save Handoff (routed from W-17) | not sized | Rust | heavy | #1631's metered reader | #1641 | No |
| W-18b | Per-report user release of the user's own project data (a shareable path): build the merged design, five slices (r1)–(r3) (DEL-08-01 Design `report-user-release.md` §8) | about 4.35k lines (§8) | desktop + Rust | heavy | W-18 a–b2, done | none | Shareable path decided (owner, 2026-10-24, option B: a per-report user release) |
| W-14 | Design-knowledge entry and constraint validation | — | — | — | — | none | Deferred to v0.2 (OD-3) |

**Sequencing:**
- **Before development testing broadens:** the G10 values (§3 rows 1–5) are
  applied by the owner's ruling, so the native smoke proves itself without known
  failures (W-4 is done). The §3 [fix] remainder can go with it.
- **Before the owner's hands-on use:** W-6 and W-18 (a)–(b2) (a model the
  owner can export and a local private report package) are on main, as are
  W-3, W-5 and the W-13 slices (#1564–#1566).
- **Before validation:** W-15 c, W-16 (#1615, #1618) and W-11 (c, #1639, then
  opening). W-15 a, b and d are on main (#1604, #1608). The R6 reproduction
  bundle (W-2) is then made at the validation basis.

## 5. Checks run for this map

**Read-only TASK reviews.** Three reviewed the PRD areas against code and tests
at `8a8a8b2584`. Codex then spot-checked a sample of placements independently
(§6). `python3 -m tools.deliverables --project projects/chirality-piping check`
reported no structural errors and one cycle, a strongly connected group of nine
deliverables (DEL-04-07, DEL-04-08, DEL-05-02, DEL-08-01, DEL-08-04, DEL-08-05,
DEL-09-05, DEL-10-04, DEL-10-05). The same cycle exists at `7a780551f0`. The
check at `df14318ec7`, its unknown needs and the cycle's edges are in §3
("Dependency declarations").

**Native smoke at `8a8a8b2584`.** A fresh build in a heavy-work tree through
`t3_slot.sh`, then `node apps/desktop/native-smoke/run.mjs --skip-build`. 73 of
83 checks passed.
- **All 10 FAILs are stale `expected.json` values,** each failing once on open
  and once after reopen: milestone rows 98→113 (sparse) and 99→113 (dense),
  milestone N1 `…198`→`…199` (sparse), demo rows 625→745 and 627→745. Causes
  are in §3 rows 1–5.
- **Passed:** refusals by name; both routes' fixtures on both solver modes;
  model-hash proofs; the save, replace and stale-base prompts; the demo result
  export (W-5); reopen in a fresh process.

**Hands-on probe.** It used the same build, with an untracked probe driver in
place of `driver.js` and a throwaway HOME.

| Step | Observed |
|---|---|
| Demo (PF) solve | completed, 745 rows, `checks_passed`; "Numerical health: checks passed" |
| Demo render, no local-private selection | `context=public_report; decisions=18082; blocked=true`; no preview, no hash |
| Demo render, local-private selected | canonical HTML SHA-256 shown; "export gates passed"; preview with the LOCAL PRIVATE notice, the software/solver/run section, the numerical-health line and three "not recorded" values; Save canonical HTML and Print offered |
| Report package | Save disabled; `REPORT-PACKAGE-FRESH-RESULT-UNAVAILABLE` |
| Demo rule checks (bundled pack) | `RULE_INPUTS_INCOMPLETE`, missing inputs named |
| Demo result JSON save (W-5) | saved, 3,636,709 bytes |
| Demo exports | result export, PCF, MBF, adapter SDK, adapter framework, local FEA, native package and handoff offered; stress-neutral CSV and glTF not offered |
| EX model `fixtures/model_operations/exact_pressure_authoring_model.json` solve | completed, 297 rows, `checks_passed` |
| EX render | refused, `PRESSURE-2-OUTPUT-NOT-YET-AVAILABLE` |
| EX rule checks | run; `RULE_INPUTS_INCOMPLETE` |
| EX exports | result and stress-neutral JSON links only (behind local-private intent); MBF and the rest refused or not offered |
| From blank (W-17, R2) | units dialog (SI, US customary, custom) → node, material, pipe, fixed support, load case and 350 N tip force through the GUI → native solve, 89 rows, `checks_passed`, tip displacement 1.3703288675916625 mm (PL³/3EI ≈ 1.370 mm) → Save Local Project in place → fresh process: reopened, solved again, the same rows and value |

The probe's first run used New Local Project for the save; the store already
held the blank project, so the app asked before replacing it, as designed. The
second run saved in place.

## 6. Independent spot-check

Codex (GPT-6.1-Sol, xhigh, read-only, branch head `289f9039ba` over basis
`8a8a8b2584`) checked 19 placements independently, 7 of them changed class.

- **Confirmed (18)** (FR-MOD-007 and FR-RULE-003 were later re-classed by the
  owner's readings, §3): FR-KNOW-002 (D), FR-MOD-007, FR-KNOW-001 and
  FR-AGENT-005 (O), FR-GUI-001 and FR-GUI-004 (D), FR-MOD-001 (P), FR-SOL-015
  (D), FR-REP-001 (P), FR-RULE-002 (D), FR-SOL-006, -007 and -009 (P),
  FR-HAND-002 and FR-CMP-001 (P), §12.8 near-duplicate nodes (P), §22.2 13 of
  14 (P), FR-RULE-005 (D).
- **Refuted (1):** §10.1 step 1 as D. The DEL-02-02 Design still described
  blank projects as offering no choice, so under the class rules it was R. This
  change corrects that Design text, and the row is D on this branch.
- **Further corrections, folded in:**
  - FR-SOL-002 moves D → P. Its acceptance includes imposed displacements,
    which pass on EX only.
  - The FR-MOD-006 evidence named one schema as the only home of
    `unresolved_assumptions`; it is also in the model-state and handoff
    schemas.
- **`expected.json`:** all five causes are plausible from the records and
  fixtures (15 rows per member per case; parity row removal; `norm3`
  rounding). Codex could not run the app; the observed values come from the
  native smoke in §5.
