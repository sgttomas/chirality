# Source Pack: SRC-DEL-DEL-07-03-MATERIAL-COMPONENT-AND-RULE-PACK-EDITORS

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-03_Material, component, and rule-pack editors/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-03_Material, component, and rule-pack editors/Datasheet.md

### Datasheet: DEL-07-03 Material, component, and rule-pack editors

#### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-07-03 |
| Package ID | PKG-07 |
| Package | Graphical User Interface and Engineering Workflow |
| Type | UX_UI_SLICE |
| Current setup scope | Document/setup production only; no GUI source implementation |
| Register scope item | SOW-021 |
| Supported objective | OBJ-006 |
| Context envelope | L |
| Context risk | WATCH - confirm scope and split if editor scope expands |

Sources: `_CONTEXT.md` sections "Scope Coverage", "Objective Support", "Context Envelope"; `docs/_Registers/Deliverables.csv` row `DEL-07-03`; `docs/_Registers/ScopeLedger.csv` row `SOW-021`.

#### Attributes

| Attribute | Source-grounded value |
|---|---|
| Product surface | GUI editor workflow for materials, sections, components, load cases, supports, rule packs, and private libraries. |
| Deliverable focus | Private material editors, component editors, and rule-pack reference editors. |
| Related editor surfaces | Section, load-case, support/restraint, and private-library editing are part of SOW-021 and must remain visible in the workflow model even if later split. |
| Anticipated artifacts | Editor panels; validation UI tests. |
| GUI runtime baseline | Rust core/application services; Tauri 2 desktop shell; TypeScript/React/Vite GUI where GUI-facing. Exact dependency versions and component/state-management libraries remain TBD. |
| Mutation route | GUI mutations route through application-service commands; durable project state is separate from transient session, selection, and job-progress state. |
| Diagnostic route | Editor validation must surface result-envelope diagnostics and warning classes rather than silently normalizing missing or private data. |
| Data boundary | Code-specific and proprietary material, component, allowable, SIF/flexibility, and rule-pack values are user-supplied or private, not public defaults. |

Sources: `docs/SPEC.md` sections 1, 3, 6, 7; `execution/_Decomposition/SOFTWARE_DECOMP.md` sections 4, 8; `_CONTEXT.md` section "Architecture Basis Injection"; `docs/CONTRACT.md` invariants `OPS-K-DATA-1`, `OPS-K-DATA-2`, `OPS-K-DATA-3`, `OPS-K-RULE-3`, `OPS-K-PRIV-1`.

#### Conditions

| Condition | Required posture |
|---|---|
| Protected standards data | Do not include protected standards text, tables, examples, code-derived formulas, material allowables, SIF/flexibility tables, protected dimensional tables, or proprietary commercial data. |
| Missing data | Missing solve-required or rule-check-required values are explicit findings, never silent defaults. |
| Provenance | Materials, components, SIFs, flexibility factors, allowables, and rule-pack values carry provenance fields. |
| Units | Editor inputs, validation, imports, exports, and rule-pack references must be unit-aware and dimensionally checked. |
| Rule packs | Rule packs are versioned, checksummed, source-noted, marked public/private, and evaluated by sandboxed unit-aware logic outside this GUI setup deliverable. |
| Professional boundary | UI copy and workflow state must not claim certification, sealing, approval, authentication, or engineering code compliance for reliance. |
| Scope split risk | Multiple editors remain in one GUI domain for setup, but later implementation may require split work if the surface expands. |

Sources: `docs/CONTRACT.md` invariants `OPS-K-IP-1`, `OPS-K-DATA-1`, `OPS-K-DATA-2`, `OPS-K-DATA-3`, `OPS-K-UNIT-1`, `OPS-K-RULE-1`, `OPS-K-RULE-2`, `OPS-K-RULE-3`, `OPS-K-AUTH-1`; `docs/DIRECTIVE.md` sections 2, 3, 5; `docs/_Registers/ContextBudgetQA.csv` row `DEL-07-03`.

#### Construction

The editor workflow is a future GUI slice, but this setup pass records the intended construction boundaries:

| Work surface | Construction note |
|---|---|
| Material editor | Presents unit-bearing material fields and provenance/source status without shipping public protected allowables or proprietary material libraries. |
| Section editor | Presents user-entered or lawfully imported section dimensions/properties with provenance and unit checks; no protected dimensional defaults. |
| Component editor | Presents component type, geometry, user modifiers, manufacturer/user data references, and provenance/private status. |
| Load-case editor | Presents primitive and user-defined load case inputs with unit-aware validation; code-specific combinations remain user/rule-pack supplied. |
| Support/restraint editor | Presents support type, directions, stiffness/gap/friction fields, and active-state result hooks without hiding nonlinear uncertainty. |
| Rule-pack reference editor | Presents rule-pack identity, version, checksum, source notice, redistribution status, required inputs, and missing-input findings. |
| Private library editor | Presents private/local library references and provenance/redistribution status while preserving local-first/private-data posture. |
| Validation UX | Surfaces `SOLVE_BLOCKING`, `RULE_CHECK_BLOCKING`, `PROVENANCE_WARNING`, `ASSUMPTION_WARNING`, `NONLINEAR_WARNING`, and `IP_BOUNDARY_WARNING` classes when applicable. |

Sources: `docs/SPEC.md` sections 3, 6, 7; `docs/TYPES.md` sections 4, 7, 8; `execution/_Decomposition/SOFTWARE_DECOMP.md` architecture basis rows `AB-00-03`, `AB-00-05`, `AB-00-06`, `AB-00-07`.

#### References

- `_CONTEXT.md` - sealed deliverable identity, architecture basis injection, and write-scope context.
- `_REFERENCES.md` - preparation reference index.
- `INIT.md` - bootstrap and project boundaries.
- `AGENTS.md` - OpenPipeStress agent index and dispatch rule.
- `docs/DIRECTIVE.md` - founding intent, product boundaries, and stop rules.
- `docs/CONTRACT.md` - invariant catalog.
- `docs/TYPES.md` - statuses, data provenance labels, and domain object vocabulary.
- `docs/SPEC.md` - architecture, domain object, rule-pack, GUI, report, and validation requirements.
- `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md` - Type 2 execution and deliverable document kit.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` - accepted revision 0.7 current decomposition basis.
- `docs/_Registers/Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv` - machine-readable deliverable, scope, and context records.

## Component: execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-03_Material, component, and rule-pack editors/Guidance.md

### Guidance: DEL-07-03 Material, component, and rule-pack editors

#### Purpose

This deliverable records the setup basis for GUI editors that let users create and review private materials, sections, components, load cases, supports, rule-pack references, and private libraries while keeping missing data, provenance, assumptions, and professional-boundary limits visible.

The core product value is not faster data entry by hidden defaults. The value is a reviewable workflow in which engineering inputs, sources, rule-pack readiness, and missing values are explicit before solving, checking, reporting, or sharing.

Sources: `docs/DIRECTIVE.md` sections 2 and 3; `docs/SPEC.md` section 7; `docs/_Registers/ScopeLedger.csv` row `SOW-021`.

#### Principles

1. Preserve the open/public boundary. GUI editors may expose fields for user code data, private library values, manufacturer data, SIFs, flexibility factors, allowables, and rule-pack formulas, but the public project must not supply protected values as defaults.
2. Make missing data actionable. A blank or unknown required value should produce a visible finding tied to solve readiness, rule-check readiness, provenance, assumption review, nonlinear uncertainty, or IP boundary risk.
3. Keep the GUI downstream of validation contracts. Editors should route changes through application-service commands and domain validation so adapters, plugins, and UI controls cannot bypass units, provenance, diagnostics, or public/private data boundaries.
4. Separate editing state from project truth. Transient UI concerns such as selection, local form state, unsaved edits, validation display, and job progress should not be confused with the durable persisted model.
5. Avoid professional overclaiming. Editor labels and workflow states may describe software findings and user-rule-check results; they must not declare professional compliance or approval.

Sources: `docs/CONTRACT.md` invariants `OPS-K-IP-1`, `OPS-K-DATA-1`, `OPS-K-DATA-2`, `OPS-K-UNIT-1`, `OPS-K-RULE-3`, `OPS-K-PRIV-1`, `OPS-K-AUTH-1`; `execution/_Decomposition/SOFTWARE_DECOMP.md` `AB-00-03`, `AB-00-05`, `AB-00-06`, `AB-00-07`.

#### Considerations

##### Editor grouping

The register places multiple editors in this deliverable because they share a GUI domain. That grouping is acceptable for setup, but implementation should watch for split triggers:

- materials/sections/components become a private library management product area;
- load cases/supports require a separate model-editing workflow;
- rule-pack references require a separate sandbox/completeness workflow;
- validation UI tests become broad enough to require a dedicated test deliverable.

Source: `docs/_Registers/ContextBudgetQA.csv` row `DEL-07-03`.

##### Missing data classes

The GUI should distinguish the reason a value matters. A solve-required missing physical input is different from a rule-check-required missing code value, weak provenance, user assumption, nonlinear convergence concern, or suspected IP/private-data exposure.

Source: `docs/SPEC.md` section 7.

##### Private libraries

Private material/component/rule-pack libraries are user-controlled assets. The editor workflow can reference and validate them, but setup artifacts should not create sample private libraries, commit vendor data, or imply redistribution rights.

Source: `docs/DIRECTIVE.md` section 6; `docs/CONTRACT.md` `OPS-K-PRIV-1`.

##### Implementation TBDs

The exact GUI component library, GUI state-management library, dependency versions, rule expression grammar/library, public API transport, import/export format list, and physical project package/container remain implementation-level `TBD` unless a later sealed brief or human ruling resolves them.

Source: `_CONTEXT.md` section "Architecture Basis Injection"; `execution/_Decomposition/SOFTWARE_DECOMP.md` section 8.2.

#### Trade-offs

| Trade-off | Guidance |
|---|---|
| One editor suite vs split deliverables | Keep setup unified under SOW-021, but split future implementation if scope becomes too broad for one bounded GUI slice. |
| Fast entry vs safe review | Prefer visible incompleteness and provenance checks over auto-filled engineering defaults. |
| Local form convenience vs validation authority | Local form state can improve usability, but durable mutation should pass through service commands and validation envelopes. |
| Public examples vs realistic libraries | Use invented/public-permissive examples only; do not publish protected or proprietary material/component/rule data. |
| Rule-pack editing vs rule-pack reference editing | This deliverable covers GUI references and required-input visibility; evaluator grammar and sandboxing remain PKG-06 responsibilities. |

#### Examples

No engineering examples with real code values are included in this setup pass.

Permitted illustrative patterns for future invented examples:

- A material form showing a density field as `TBD` with `UNKNOWN_SOURCE` until the user records provenance.
- A component form showing SIF/flexibility inputs as user-supplied fields with source status rather than public defaults.
- A rule-pack reference panel showing checksum, version, redistribution status, and missing required inputs before a rule-check status can be shown.

These are workflow examples only, not engineering values or code-check examples.

#### Semantic Lensing Application

Pass 3 applied the semantic lensing register as a worklist. Source rereads used for substantive updates:

| Lensing item | Source reread before update | Disposition |
|---|---|---|
| Clarify scope split risk for the multiple-editor surface | `_CONTEXT.md` Context Budget QA; `docs/_Registers/ContextBudgetQA.csv` row `DEL-07-03` | Incorporated into "Editor grouping" and Procedure split check. |
| Clarify application-service command and durable/transient state boundary | `_CONTEXT.md` Architecture Basis Injection; `execution/_Decomposition/SOFTWARE_DECOMP.md` `AB-00-03`, `AB-00-05` | Incorporated into Principles and Procedure. |
| Clarify private/protected data boundary | `docs/CONTRACT.md` `OPS-K-IP-1`, `OPS-K-DATA-1`, `OPS-K-PRIV-1`; `docs/DIRECTIVE.md` sections 3 and 6 | Incorporated into Private libraries and Requirements. |
| Clarify no professional compliance claim | `docs/CONTRACT.md` `OPS-K-AUTH-1`; `docs/TYPES.md` section 4 | Incorporated into Principles and Verification. |

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict identified during setup. | N/A | N/A | N/A | N/A | N/A |

## Component: execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-03_Material, component, and rule-pack editors/Procedure.md

### Procedure: DEL-07-03 Material, component, and rule-pack editors

#### Purpose

Define how the `DEL-07-03` setup artifacts are produced and checked, and record the operational boundaries that future implementation work must preserve for material, component, rule-pack, load/support, and private-library editors.

This procedure does not implement GUI code.

#### Prerequisites

| Prerequisite | Required source/evidence |
|---|---|
| Sealed deliverable context | `_CONTEXT.md` for `DEL-07-03` |
| Governing invariants | `docs/CONTRACT.md`, especially data, unit, rule-pack, privacy, IP, agent, and professional-boundary invariants |
| Decomposition/register identity | `execution/_Decomposition/SOFTWARE_DECOMP.md`; `docs/_Registers/Deliverables.csv`; `docs/_Registers/ScopeLedger.csv`; `docs/_Registers/ContextBudgetQA.csv` |
| Architecture basis constraints | `_CONTEXT.md` Architecture Basis Injection and `execution/_Decomposition/SOFTWARE_DECOMP.md` section 8 |
| Skill contracts | `skills/four-documents/SKILL.md`; `skills/semantic-matrix-build/SKILL.md`; `skills/lens-register/SKILL.md`; `skills/dependency-extract/SKILL.md` |
| Write scope | Only this deliverable folder and its descendants |

#### Steps

1. Confirm local scope.
   - Verify the target folder is `execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-03_Material, component, and rule-pack editors/`.
   - Verify `_STATUS.md` is in an overwrite-allowed setup state before four-document generation.
   - Do not read protected/private libraries or create `ISSUED` artifacts.

2. Run `four-documents` with `RUN_PASSES=P1_P2`.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the decomposition/register source slices.
   - Produce `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.
   - Keep default sections present in all four documents.
   - Mark unknown engineering values and implementation choices as `TBD`.
   - Update `_STATUS.md` from `OPEN` to `INITIALIZED` only if current state is `OPEN`.
   - Record the run in `_run_records/TASK_RUN_2026-04-30_1040_four-documents-p1-p2.md`.

3. Run `semantic-matrix-build`.
   - Read `_CONTEXT.md`, `_STATUS.md`, the four production documents, and `_REFERENCES.md`.
   - Write `_SEMANTIC.md` with canonical matrices A/B, derived matrices C/F/D/K/G/X/T/E, interpretation work, audit result, and matrix summary.
   - Audit final interpreted cells for algebra leaks, operator leaks, and long uninterpreted expansions.
   - On audit pass, set or verify `_STATUS.md` as `SEMANTIC_READY`.
   - Record the run in `_run_records/TASK_RUN_2026-04-30_1041_semantic-matrix-build.md`.

4. Run `lens-register`.
   - Read `_SEMANTIC.md`, `_CONTEXT.md`, `_STATUS.md`, the four production documents, and `_REFERENCES.md`.
   - Write `_SEMANTIC_LENSING.md` only.
   - Include lens coverage for every cell in matrices A, B, C, F, D, X, and E.
   - Record warranted gaps, questions, or conflicts only when supported by production-document evidence or explicit absence.
   - Record the run in `_run_records/TASK_RUN_2026-04-30_1042_lens-register.md`.

5. Run `four-documents` with `RUN_PASSES=P3_ONLY`.
   - Treat `_SEMANTIC_LENSING.md` as a candidate worklist, not an authority.
   - Before every substantive enrichment, reread the target section and the source slice supporting the change.
   - Do not regress `_STATUS.md`; if it is already `SEMANTIC_READY`, leave it as-is.
   - Record source rereads in `Guidance.md` and in `_run_records/TASK_RUN_2026-04-30_1043_four-documents-p3.md`.

6. Run `dependency-extract`.
   - Use `Specification.md` as the anchor document and `Procedure.md`, `Guidance.md`, and `Datasheet.md` as execution documents.
   - Create or refresh `Dependencies.csv` with v3.1 columns.
   - Refresh `_DEPENDENCIES.md` with declared lists preserved, extracted summary, run notes, run history, lifecycle summary, and handoff notes.
   - Run local validation commands for schema, enums, and ID formats.
   - Record the run in `_run_records/TASK_RUN_2026-04-30_1044_dependency-extract.md`.

7. Final setup check.
   - Confirm required artifacts exist.
   - Confirm no file outside the assigned deliverable folder changed because of this session.
   - Confirm no `ISSUED` artifact was created.
   - Confirm `_STATUS.md` says `SEMANTIC_READY` only if semantic and dependency gates passed.

#### Verification

Run these checks from the repository root:

```sh
tools/validation/check_min_viable_fileset.sh "execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-03_Material, component, and rule-pack editors"
python3 tools/validation/validate_dependencies_schema.py "execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-03_Material, component, and rule-pack editors/Dependencies.csv"
tools/validation/validate_id_format.sh DEL DEL-07-03
tools/validation/validate_id_format.sh PKG PKG-07
```

Additional checks:

- Ensure `_SEMANTIC.md` contains matrices A, B, C, F, D, K, G, X, T, E and an audit pass note.
- Ensure `_SEMANTIC_LENSING.md` contains lens coverage for matrices A, B, C, F, D, X, E.
- Ensure `Dependencies.csv` ACTIVE rows include `EvidenceFile` and `SourceRef`.
- Ensure no text claims code compliance, certification, sealing, approval, or professional reliance.
- Ensure no protected standards data or proprietary library content appears in the documents.

#### Records

Records produced by this setup run:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_STATUS.md`
- `_run_records/*.md`

## Component: execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-03_Material, component, and rule-pack editors/Specification.md

### Specification: DEL-07-03 Material, component, and rule-pack editors

#### Scope

This deliverable specifies the setup documentation for future GUI editor panels and validation UI tests covering material, section, component, load-case, support/restraint, rule-pack reference, and private-library editing within `PKG-07`.

In scope:

- Editor workflow requirements for user/private engineering data entry and review.
- Missing-data, provenance, unit, rule-pack-reference, and private-library validation expectations.
- Boundaries between GUI editing, application-service commands, domain schemas, rule-pack evaluation, diagnostics, and private data handling.
- Setup artifacts only: document kit, semantic artifacts, dependencies, run records, and status evidence.

Out of scope:

- GUI source implementation, tests, package manifests, schemas, or repo-level documentation.
- Bundled protected standards content, proprietary material/component/rule data, or silent engineering defaults.
- Selection of exact GUI component libraries, state libraries, rule expression grammar/library, dependency versions, public API transport, or physical project package/container.
- Any claim that the GUI certifies, seals, approves, authenticates, or declares engineering code compliance.

Sources: `_CONTEXT.md` sections "Description", "Anticipated Artifacts", "Architecture Basis Injection"; `docs/_Registers/Deliverables.csv` row `DEL-07-03`; `docs/_Registers/ScopeLedger.csv` row `SOW-021`; `docs/CONTRACT.md` invariants `OPS-K-IP-1`, `OPS-K-DATA-1`, `OPS-K-AUTH-1`, `OPS-K-AGENT-4`.

#### Requirements

| Req ID | Requirement | Source |
|---|---|---|
| DEL-07-03-R-001 | The setup artifacts shall preserve `DEL-07-03` as the sole production unit and shall not expand into GUI source implementation. | `_CONTEXT.md`; `AGENTS.md` dispatch rule; `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md` section 4 |
| DEL-07-03-R-002 | The editor workflow shall expose materials, sections, components, load cases, supports, rule packs, and private libraries as editable/reviewable GUI concepts under SOW-021. | `docs/_Registers/ScopeLedger.csv` row `SOW-021`; `docs/SPEC.md` section 7 |
| DEL-07-03-R-003 | The material editor shall require provenance/source status for material records and shall not provide protected public material allowables or code tables. | `docs/TYPES.md` sections 7 and 8; `docs/CONTRACT.md` `OPS-K-DATA-1`, `OPS-K-DATA-3`, `OPS-K-IP-1` |
| DEL-07-03-R-004 | The section and component editors shall treat dimensions, weights, centers of gravity, SIFs, flexibility factors, stiffnesses, and proprietary catalog values as user-supplied or lawfully imported data with provenance. | `docs/SPEC.md` sections 3 and 4.3; `docs/DIRECTIVE.md` section 3 |
| DEL-07-03-R-005 | The load-case editor shall support unit-aware editor input for load cases while leaving code-specific load combinations to user project inputs or rule packs. | `docs/SPEC.md` sections 3 and 5; `docs/CONTRACT.md` `OPS-K-UNIT-1`, `OPS-K-DATA-1` |
| DEL-07-03-R-006 | The support/restraint editor shall surface fields needed to represent support/restraint behavior and shall not hide nonlinear active-state uncertainty or non-convergence findings. | `docs/SPEC.md` sections 3, 4.4, and 7 |
| DEL-07-03-R-007 | The rule-pack reference editor shall expose rule-pack identity, version, checksum, source notice, redistribution status, required inputs, and missing required-input findings. | `docs/SPEC.md` section 6; `docs/CONTRACT.md` `OPS-K-RULE-1`, `OPS-K-RULE-2`, `OPS-K-RULE-3` |
| DEL-07-03-R-008 | Editor mutations shall be modeled as application-service command interactions, not direct bypasses of domain validation, unit checks, provenance checks, or public/private data boundaries. | `docs/SPEC.md` section 1; `execution/_Decomposition/SOFTWARE_DECOMP.md` `AB-00-02`, `AB-00-03`, `AB-00-07` |
| DEL-07-03-R-009 | Editor state shall separate durable project/model data from transient session, selection, validation, and job-progress state; exact state-management library remains TBD. | `_CONTEXT.md` "Still TBD"; `execution/_Decomposition/SOFTWARE_DECOMP.md` `AB-00-05` |
| DEL-07-03-R-010 | Editor validation shall surface missing data early using diagnostic/result-envelope warning classes and shall not silently introduce engineering defaults. | `docs/SPEC.md` section 7; `execution/_Decomposition/SOFTWARE_DECOMP.md` `AB-00-06`; `docs/CONTRACT.md` `OPS-K-DATA-2` |
| DEL-07-03-R-011 | Private material, component, project, and rule-pack data shall remain local/user-controlled by default and shall not be committed or transmitted publicly by this deliverable. | `docs/CONTRACT.md` `OPS-K-PRIV-1`; `docs/DIRECTIVE.md` sections 3 and 6 |
| DEL-07-03-R-012 | UI wording and output states shall distinguish editable user data, mechanics solve readiness, user-rule-check readiness, and human professional review without implying code compliance. | `docs/TYPES.md` section 4; `docs/DIRECTIVE.md` section 2.2; `docs/CONTRACT.md` `OPS-K-AUTH-1`, `OPS-K-MECH-2` |
| DEL-07-03-R-013 | The future implementation brief shall split this deliverable or request human approval if the editor scope becomes too broad for one bounded GUI slice. | `_CONTEXT.md` "Context Budget QA"; `docs/_Registers/ContextBudgetQA.csv` row `DEL-07-03` |

#### Standards

No protected engineering code or standards text is used as an authority in this setup artifact. Governing standards for this setup pass are the public project governance and decomposition documents listed in `_REFERENCES.md`, especially `docs/CONTRACT.md`, `docs/TYPES.md`, `docs/SPEC.md`, and `execution/_Decomposition/SOFTWARE_DECOMP.md`.

Any future editor behavior that depends on an engineering code, owner standard, vendor catalog, material allowable, SIF/flexibility value, or rule formula shall treat that content as user-supplied/private unless redistribution rights and provenance are documented. Source location for future standards data is `TBD` and must not be inferred here.

#### Verification

| Verification ID | Requirement(s) | Verification approach |
|---|---|---|
| DEL-07-03-V-001 | R-001 | Confirm changed paths remain within the assigned deliverable folder and no `ISSUED` path exists. |
| DEL-07-03-V-002 | R-002 to R-007 | Review the four-document kit for all editor surface names: materials, sections, components, load cases, supports, rule packs, and private libraries. |
| DEL-07-03-V-003 | R-003 to R-007, R-010 | Confirm all missing engineering values are `TBD`, user-supplied, or provenance-marked rather than defaulted. |
| DEL-07-03-V-004 | R-008 to R-009 | Confirm application-service command routing and durable/transient state split are recorded as constraints, with exact state library `TBD`. |
| DEL-07-03-V-005 | R-010 to R-012 | Confirm warning classes and professional-boundary text are present and no compliance/certification claim appears. |
| DEL-07-03-V-006 | R-013 | Confirm scope split risk is visible in the datasheet, guidance, procedure, and `_STATUS.md`/run records where applicable. |
| DEL-07-03-V-007 | Dependency setup | Validate `Dependencies.csv` with `tools/validation/validate_dependencies_schema.py` and enum/ID checks. |
| DEL-07-03-V-008 | Semantic setup | Confirm `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, and run records exist, and `_STATUS.md` is `SEMANTIC_READY` only after setup gates pass. |

#### Documentation

Required deliverable-local setup artifacts:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-04-30_1040_four-documents-p1-p2.md`
- `_run_records/TASK_RUN_2026-04-30_1041_semantic-matrix-build.md`
- `_run_records/TASK_RUN_2026-04-30_1042_lens-register.md`
- `_run_records/TASK_RUN_2026-04-30_1043_four-documents-p3.md`
- `_run_records/TASK_RUN_2026-04-30_1044_dependency-extract.md`

Future implementation artifacts named by the register remain anticipated, not implemented here: editor panels and validation UI tests.
