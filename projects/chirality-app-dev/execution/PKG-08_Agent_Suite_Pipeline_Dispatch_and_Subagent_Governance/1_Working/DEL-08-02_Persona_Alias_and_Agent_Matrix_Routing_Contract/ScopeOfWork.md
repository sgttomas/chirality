---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-02
package_id: PKG-08
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@416b29033bbacb0bc3648d84033272b7ab4e6e11
project_scope_refs: [SOW-005, SOW-006, SOW-017]
package_objective_refs: [OBJ-001, OBJ-007]
---

# Scope of Work — DEL-08-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-08-02` in service of project scope [SOW-005, SOW-006, SOW-017] and package objectives [OBJ-001, OBJ-007].

- **OUT-001** — Persona alias, agent/session routing, and legacy matrix compatibility contract, with alias resolver, guarded session-selection, route/query, persona-resolution, and compatibility tests that keep canonical identity and navigation intent consistent without making a fixed matrix part of the target shell.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-08-02 Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract

> #### Datasheet: DEL-08-02 Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-08-02 |
> | DeliverableName | Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract |
> | PackageID | PKG-08 |
> | PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | UX_UI_SLICE |
> | ContextEnvelope | S |
> | ResponsibleParty | TBD |
> | Current Lifecycle State at Draft | INITIALIZED |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Scope summary | Keep UI aliases, canonical agent names, persona resolution, guarded dialogue/session selection, route/query mappings, and legacy matrix behavior consistent. | `_CONTEXT.md`; decomposition entry DEL-08-02; SCA-APP-004 |
> | Anticipated artifacts | Alias resolver tests; guarded session-selection tests; route/query fixtures; legacy matrix compatibility and unavailable-persona tests. | `_CONTEXT.md`; decomposition entry DEL-08-02 |
> | Covered scope items | SOW-005, SOW-006, SOW-017. | `_CONTEXT.md`; decomposition scope table |
> | Supported objectives | OBJ-001, OBJ-007. | `_CONTEXT.md`; decomposition entry DEL-08-02 |
> | UI alias map | `HELP -> HELP_HUMAN`; `ORCHESTRATE -> ORCHESTRATOR`; `AGENTS -> HELPS_HUMANS`; `DEPENDENCIES -> EVALUATION`. `AGGREGATE` and `RECONCILING` are not compatibility aliases: their former cells were re-pointed to the canonical Type 1 `REVIEW` and `RESEARCH` personas so no alias is needed. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026; D-APP-28 loop-first routing |
> | Legacy matrix rows | `NORMATIVE`, `OPERATIVE`, `EVALUATIVE` remain compatibility vocabulary, not a required target-shell layout. | `docs/TYPES.md` Section 4.1; SCA-APP-004 |
> | Legacy matrix columns | `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING` remain compatibility vocabulary, not a required target-shell layout. | `docs/TYPES.md` Section 4.2; SCA-APP-004 |
> | Legacy matrix routing destinations | During compatibility, `NORMATIVE` and `EVALUATIVE` preserve persona/session intent and `OPERATIVE` preserves governed PIPELINE dispatch intent. | D-APP-28/30/31 preserved compatibility; SCA-APP-004 |
> | Guarded dialogue/session selection | Selecting an already-recorded session may load a labelled read-only replay lens, but must not resume, merge with, or mutate the primary live dialogue; an in-flight selection that could clobber live state remains guarded. | SCA-APP-004; preserved D-APP-30 safety rule |
> | Persona filename target | Persona names resolve to `agents/AGENT_*.md`; missing personas return `PERSONA_NOT_FOUND`. | `docs/PRD.md` FR-025 |
> | Persona fallback | Empty or missing request/session persona falls back to the live hardcoded `WORKING_ITEMS` default; unknown non-empty labels pass through normalized for instruction-file resolution. | `docs/SPEC.md` Section 13.1; `frontend/src/lib/shell/persona-resolution.ts` |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Source authority state | REF-006 `docs/PRD.md` is MATCH under the D-APP-38 authority corpus v2. | `_REFERENCES.md`; D-APP-38 |
> | Governance posture | Unknown values remain `TBD`, and source conflicts must be surfaced rather than silently resolved. | `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |
> | Route shape constraint | Existing harness route shapes remain stable during SDK adoption and TurnEngine extraction. | `docs/SPEC.md` Section 17.1 |
> | Unsupported variants | Disabled or unsupported compatibility/pipeline variants remain visible as coming soon where the product contract requires them rather than disappearing. | `docs/PRD.md`; SCA-APP-004 |
> | Semantic non-ownership | DEL-08-02 does not own shell presentation, Work-plan authority, dispatch semantics, replay evidence, child-run parentage, lifecycle, or approval. | SCA-APP-004 semantic ownership partition |
> | Dependency register state | `Dependencies.csv` exists in v3.1 format with 13 ACTIVE extracted rows; declared upstream/downstream human edges remain TBD. | `_DEPENDENCIES.md` Compact Register; `Dependencies.csv` |
>

### CLM-005 — Construction

> ##### Construction
>
> | Construct | Required Datasheet Value |
> |---|---|
> | Alias resolver | MUST encode only sourced UI alias mappings unless amended by governance. |
> | Canonical agent name target | MUST resolve aliases and personas to canonical instruction-root agent names, with `agents/AGENT_<persona>.md` as the file contract. |
> | Legacy matrix compatibility fixture | MUST cover canonical 3x4 row/column vocabulary and row-intent/query behavior during the compatibility period without requiring the matrix in the target shell. |
> | Dialogue/session route fixture | MUST preserve canonical agent/session identity, unknown query parameters, and legacy selected agent/row/column context while enforcing guarded selection and live/replay separation. |
> | Pipeline route fixture | MUST distinguish operative category routing from loop-persona routing. |
> | Unspecified UI details | TBD until implementation evidence or human ruling defines exact component names, route query keys, and fixture file paths. |
> | P3 implementation path slot | F-001 remains a TBD implementation slot: selected module paths and fixture/test file paths for alias resolver, matrix mapping, route fixtures, and persona resolver must be filled when implementation begins. |
> | P3 route key slot | D-001 remains a TBD implementation slot: selected agent, row, and column context keys must be replaced with actual query-param or route-state names once chosen by code. |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Product boundaries and matrix/persona scope. |
> | REF-002 | `docs/CONTRACT.md` | Invariants for non-invention, routing governance, and agent boundaries. |
> | REF-003 | `docs/SPEC.md` | Runtime option fallback, persona composition, and API route stability. |
> | REF-004 | `docs/TYPES.md` | Authoritative alias and matrix vocabulary. |
> | REF-005 | `docs/PLAN.md` | Implementation sequencing context. |
> | REF-006 | `docs/PRD.md` | Product requirements; MATCH under D-APP-38 authority corpus v2. |
> | REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context. |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | DEL-08-02 scope, SOW links, objectives, artifacts. |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-08-02 Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract

> #### Specification: DEL-08-02 Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable specifies the routing and persona-resolution contract needed
> to keep UI aliases, canonical agent names, guarded dialogue/session
> selection, legacy route/query/matrix behavior, and persona resolution
> consistent for Chirality App vNext. The fixed matrix is compatibility
> presentation rather than the target information architecture.
>
> In scope:
>
> - Alias resolution from UI labels to canonical agent names.
> - Canonical matrix row, column, and cell vocabulary as legacy compatibility.
> - Compatibility routing from legacy matrix/query intent to persona/session or governed Pipeline intent.
> - Guarded selection of recorded dialogues/sessions without clobbering an in-flight primary session.
> - Route/query preservation for selected agent, row, column, session, and unknown parameters during compatibility.
> - Persona resolution to instruction-root `agents/AGENT_*.md` files.
> - Tests and fixtures for alias resolution, guarded selection, route/query behavior, persona resolution, and legacy matrix compatibility.
>
> Out of scope:
>
> - General SDK adapter mechanics.
> - Full prompt composition implementation owned by DEL-04-04, except for the persona-name contract shared with this deliverable.
> - Pipeline category and task-scope dispatch owned by DEL-08-03, except for row-level `OPERATIVE -> PIPELINE` routing.
> - Shell or Work/Agents Coordination Panel presentation, owned by DEL-02-01/02.
> - Transcript/replay reconstruction, owned by DEL-05-04.
> - Parent-child records and hierarchy, owned by DEL-08-05.
> - Project-plan/task status, lifecycle transition, approval, scheduling, direct child messaging, or editable agent graphs.
> - Dependency extraction authoring; the existing `Dependencies.csv` and `_DEPENDENCIES.md` are consumed as current dependency evidence for this deliverable.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | DEL-08-02-REQ-001 | The UI alias resolver MUST map `HELP` to `HELP_HUMAN`. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026 | Alias resolver unit test. |
> | DEL-08-02-REQ-002 | The UI alias resolver MUST map `ORCHESTRATE` to `ORCHESTRATOR`. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026 | Alias resolver unit test. |
> | DEL-08-02-REQ-003 | The UI alias resolver MUST NOT map `AGGREGATE` to `AGGREGATION`; `AGGREGATION` is a Type 2 task agent and must not boot as a top-level loop persona. | D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` Type 2 vocabulary | Negative alias resolver unit test and matrix guard test. |
> | DEL-08-02-REQ-004 | The UI alias resolver MUST NOT map `RECONCILING` to `RECONCILIATION`; the EVALUATIVE/REVIEWING matrix cell uses the Type 1 `RESEARCH` persona under the loop-first guard. | D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` matrix vocabulary | Negative alias resolver unit test and matrix guard test. |
> | DEL-08-02-REQ-005 | The UI alias resolver MUST map `AGENTS` to `HELPS_HUMANS`. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026 | Alias resolver unit test. |
> | DEL-08-02-REQ-006 | Legacy PORTAL matrix fixtures MUST preserve rows `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE` during the compatibility period. | `docs/TYPES.md` Section 4.1; SCA-APP-004 | Legacy matrix compatibility test. |
> | DEL-08-02-REQ-007 | Legacy PORTAL matrix fixtures MUST preserve columns `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING` during the compatibility period. | `docs/TYPES.md` Section 4.2; SCA-APP-004 | Legacy matrix compatibility test. |
> | DEL-08-02-REQ-008 | During compatibility, NORMATIVE matrix/query intent MUST preserve canonical Type 0/1 persona/session routing without making the matrix part of the target shell. | Preserved D-APP-28 routing; SCA-APP-004 | Route/query fixture test. |
> | DEL-08-02-REQ-009 | During compatibility, EVALUATIVE matrix/query intent MUST preserve canonical Type 0/1 persona/session routing without making the matrix part of the target shell. | Preserved D-APP-28 routing; SCA-APP-004 | Route/query fixture test. |
> | DEL-08-02-REQ-010 | During compatibility, OPERATIVE matrix/query intent MUST continue to route to the governed PIPELINE dispatch surface owned by DEL-08-03. | Preserved D-APP-31 dispatch; SCA-APP-004 | Route/query fixture test. |
> | DEL-08-02-REQ-011 | Legacy and target routing MUST preserve exact selected agent/session identity and compatible agent/row/column query context without transferring another session's draft, context, permissions, or interaction authority. | SCA-APP-004; preserved D-APP-30 guard | Route-state and session-isolation test. |
> | DEL-08-02-REQ-012 | Persona names MUST resolve to instruction files matching `agents/AGENT_*.md`. | `docs/PRD.md` FR-025; `docs/SPEC.md` Section 13.2 | Persona resolver test with existing and missing personas. |
> | DEL-08-02-REQ-013 | Missing personas MUST return `PERSONA_NOT_FOUND`. | `docs/PRD.md` FR-025 | Negative persona resolver test. |
> | DEL-08-02-REQ-014 | Request/session persona fallback MUST be deterministic: empty or missing UI persona resolves to `WORKING_ITEMS`, while unknown non-empty persona labels pass through normalized and fail later at instruction-file resolution if no matching `AGENT_*.md` exists. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` FR-023; current loop-first shell contract | Runtime option fallback and negative persona resolver tests. |
> | DEL-08-02-REQ-015 | Unknown runtime option keys MUST warn without silently mutating behavior. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` FR-024 | Runtime option warning test. |
> | DEL-08-02-REQ-016 | Unsupported or disabled matrix/pipeline variants MUST remain visible as coming soon rather than silently disappearing. | `docs/PRD.md` Section 7.2; `docs/PRD.md` FR-011 | UI fixture or interaction test. |
> | DEL-08-02-REQ-017 | The implementation MUST NOT invent additional alias mappings, matrix rows, columns, or canonical persona names without a governed source update. | `docs/CONTRACT.md` K-INVENT-1; `docs/TYPES.md` Sections 3.4 and 4 | Fixture completeness and snapshot tests. |
> | DEL-08-02-REQ-018 | Selecting a recorded session for inspection MUST be guarded against clobbering an in-flight primary session and MUST route only to a labelled read-only replay lens supplied by DEL-05-04. | SCA-APP-004; preserved D-APP-30 safety rule | Guarded-selection interaction test. |
> | DEL-08-02-REQ-019 | Session selection MUST NOT resume, merge with, mutate, or transfer the primary live dialogue's draft, attachments, explicit context, permissions, interruption state, session identity, or interaction authority. | SCA-APP-004 selected concept | Session-isolation test. |
> | DEL-08-02-REQ-020 | Route/query compatibility MUST preserve `agent`, `row`, `column`, Pipeline context keys, and unknown parameters during the compatibility period. | SCA-APP-004 compatibility ceiling | Deep-link and unknown-query regression. |
> | DEL-08-02-REQ-021 | Agent/session identity and selectable relationships MUST use recorded identifiers; missing, stale, conflicting, or unrecorded relationships MUST remain explicit rather than inferred. | SCA-APP-004 coordination-projection invariant | Projection/source-label test. |
> | DEL-08-02-REQ-022 | DEL-08-02 MUST NOT own shell presentation, Work-plan status, dispatch semantics, transcript/replay persistence, parent-child records, lifecycle, approval, scheduling, or direct child messaging. | SCA-APP-004 semantic ownership partition | Boundary review and negative interaction tests. |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Status |
> |---|---|---|
> | `docs/TYPES.md` Sections 3.4 and 4 | Authoritative vocabulary for alias and matrix terms. | Accessible; hash match. |
> | `docs/PRD.md` Sections 7.2, 7.4, 8.2, and 8.4 | Product requirements for matrix routing, workbench context, and persona resolution. | Current under the D-APP-38 authority corpus. |
> | `docs/SPEC.md` Section 13 | Runtime option fallback and persona composer contract. | Accessible; hash match. |
> | `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 | Governance constraints for unsupported facts and source conflicts. | Accessible; hash match. |
> | `docs/DIRECTIVE.md` Sections 2.8 and 4.1 | Product-owned persona/system-prompt and matrix navigation scope. | Accessible; hash match. |
>

### CLM-011 — Verification

> ##### Verification
>
> Required verification artifacts:
>
> - Alias resolver tests covering the active sourced aliases, removed Type-2 alias negative cases, and unknown alias pass-through behavior.
> - Legacy matrix compatibility tests covering all canonical rows, columns, and row destinations without requiring the matrix in the target shell.
> - Route fixtures proving legacy NORMATIVE/EVALUATIVE intent resolves to canonical personas/sessions and OPERATIVE intent reaches governed Pipeline dispatch.
> - Dialogue/session route-state tests proving exact selected identity and compatible query parameters survive while primary-session state remains isolated.
> - Guarded selected-session tests proving an in-flight primary dialogue is not clobbered and selected replay remains observational/read-only.
> - Persona resolver tests proving canonical `AGENT_*.md` lookup and `PERSONA_NOT_FOUND` for missing personas.
> - Runtime fallback tests proving default persona behavior and warning behavior for unknown option keys where this deliverable touches shared runtime option handling.
>
> Pass 3 evidence slots:
>
> | ItemID | Disposition | Required evidence |
> |---|---|---|
> | B-001 | Resolved by current implementation contract. Unknown UI alias labels pass through normalized and then fail at instruction-file resolution if no matching persona exists. | `frontend/src/__tests__/lib/persona-resolution.test.ts`. |
> | F-002 | Incorporated as audit evidence naming requirement. Verification records must identify concrete result files or command outputs for alias, matrix, route, workbench-context, persona, fallback, unknown-key, and unsupported-option checks. | Implementation-local test report paths or command output locations. |
> | D-001 | Resolved by loop-first launch state. Matrix launches preserve selected agent, row, and column in the mounted shell route-state contract. | `frontend/src/__tests__/lib/agent-matrix-launch.test.ts`. |
> | X-001 | Incorporated from current dependency evidence. `Dependencies.csv` and `_DEPENDENCIES.md` now provide extracted rows; declared human upstream/downstream edges remain TBD. | Dependency register validation and any later human edge ruling. |
> | C-001 | Resolved by D-APP-38. PRD-backed requirements are current under authority corpus v2 and remain separate from implementation proof. | `_REFERENCES.md` REF-006 records MATCH. |
>

### CLM-012 — Documentation

> ##### Documentation
>
> This deliverable should produce or update:
>
> - Alias resolver tests.
> - Route fixtures.
> - Matrix mapping tests.
> - Any implementation-local notes needed to explain route-state keys if they change from the current loop-first launch contract.
> - Concrete verification evidence paths or command outputs for the checks listed in the Pass 3 evidence slots.
>
> Exact implementation file paths are TBD until the owning implementation slice selects or confirms the frontend/runtime module locations.

- **AC-001** — The DEL-08-02 contract is accepted when alias, persona, guarded session-selection, route/query, and legacy matrix compatibility tests demonstrate canonical identity and navigation consistency, strict primary-session isolation, exact recorded relationships, and the semantic non-ownership boundaries for SOW-005, SOW-006, and SOW-017.

## Production and Verification Method — Praxeology

### CLM-013 — Procedure: DEL-08-02 Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract

> #### Procedure: DEL-08-02 Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract
>

### CLM-014 — Purpose

> ##### Purpose
>
> Define the bounded procedure for producing, checking, and using the persona
> alias, guarded agent/session routing, and legacy matrix compatibility
> contract for DEL-08-02.
>

### CLM-015 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Deliverable context file `_CONTEXT.md` is available. | Satisfied. |
> | Reference record `_REFERENCES.md` is available. | Satisfied. |
> | Authoritative sources listed in `_REFERENCES.md` are locally accessible. | Satisfied; REF-006 is MATCH under the D-APP-38 authority corpus. |
> | Dependency register is available. | Satisfied for extracted rows: `Dependencies.csv` exists with 13 ACTIVE rows; declared human upstream/downstream edges remain TBD. |
> | ResponsibleParty assigned. | TBD. |
> | Exact implementation module paths for alias resolver, matrix fixture, and route tests are known. | TBD. |
>

### CLM-016 — Steps

> ##### Steps
>
> 1. Read `_CONTEXT.md` and confirm the deliverable identity is DEL-08-02 with ResponsibleParty left as TBD.
> 2. Read `_REFERENCES.md` and record source status, including the D-APP-38 authority-corpus state for REF-006.
> 3. Read the DEL-08-02 decomposition entry and confirm the deliverable scope, anticipated artifacts, SOW links, and objectives.
> 4. Extract the canonical alias map from `docs/TYPES.md` Section 3.4 and cross-check against `docs/PRD.md` FR-026.
> 5. Extract the canonical matrix row, column, and cell vocabulary from `docs/TYPES.md` Section 4.
> 6. Extract matrix routing acceptance from `docs/PRD.md` Section 7.2 and FR-008.
> 7. Extract loop-persona context behavior from `docs/PRD.md` Section 7.4 and FR-009 as interpreted by the D-APP-28 loop-first pivot.
> 8. Extract persona resolution and fallback requirements from `docs/PRD.md` FR-023 through FR-026 and `docs/SPEC.md` Section 13.
> 9. Build or update alias resolver tests for the active aliases and removed Type-2 alias negative cases.
> 10. Build or update matrix mapping tests for the canonical 3x4 row/column vocabulary.
> 11. Build or update route fixtures proving row-to-surface routing.
> 12. Build or update persona resolver tests for `agents/AGENT_*.md` lookup and `PERSONA_NOT_FOUND`.
> 13. Mark any unsupported behavior as TBD rather than inventing requirements.
> 14. Read the current dependency register when closure or fixture coverage depends on dependency state; do not create or rewrite `Dependencies.csv` during this four-document procedure.
> 15. Record selected module paths and fixture/test file paths for alias resolver, matrix mapping, route fixtures, and persona resolver.
> 16. Record the active loop-first route-state behavior for selected agent, row, and column.
> 17. Record unknown-alias behavior as normalized pass-through to instruction-file resolution and keep Type 2 alias removals covered by negative tests.
> 18. Verify guarded recorded-session selection against an in-flight primary dialogue.
> 19. Verify selected replay remains read-only and cannot receive or overwrite primary draft, context, permission, interruption, or identity state.
> 20. Verify legacy route/query/matrix inputs remain compatible and unknown query parameters are preserved.
> 21. Verify all displayed agent/session relationships use exact admitted identifiers and that missing relationships remain unknown.
>

### CLM-017 — Verification

> ##### Verification
>
> | Check | Expected Result |
> |---|---|
> | Alias map completeness | Active aliases and removed Type-2 alias negative cases are covered by tests. |
> | Alias map conservatism | No unsourced aliases are asserted as requirements. |
> | Matrix vocabulary | Rows and columns match `docs/TYPES.md` and PRD FR-007. |
> | Route destination | NORMATIVE/EVALUATIVE produce loop-persona intent; OPERATIVE routes to PIPELINE. |
> | Loop context | Selected agent, row, and column are preserved from route state or query parameters. |
> | Persona lookup | Canonical persona names resolve to `agents/AGENT_*.md`; missing personas return `PERSONA_NOT_FOUND`. |
> | Unknown fields | Unknown runtime option keys warn rather than mutating behavior. |
> | Source state | REF-006 is current under D-APP-38; future authority-doc edits require corpus bump/apply. |
> | Dependency register | Existing `Dependencies.csv` and `_DEPENDENCIES.md` are consumed as evidence; this procedure does not create or rewrite them. |
> | P3 evidence capture | F-002 records concrete test result files or command output locations for alias, matrix, route, workbench-context, persona, fallback, unknown-key, and unsupported-option checks. |
> | Acceptance transition | Source-state E-001 is closed by D-APP-38; implementation proof remains independently required. |
>

### CLM-018 — Records

> ##### Records
>
> Required records for this document kit:
>
> - `Datasheet.md`
> - `Specification.md`
> - `Guidance.md`
> - `Procedure.md`
> - `_run_records/TASK_RUN_2026-05-20_1614.md`
> - `_run_records/TASK_RUN_2026-05-23_W37_four-documents-p3.md`
>
> Future implementation records:
>
> - Alias resolver tests.
> - Route fixtures.
> - Matrix mapping tests.
> - D-APP-38 source-state ruling and any future authority-corpus bump/apply evidence.
> - F-001 path selections for implementation modules and fixture/test files.
> - F-002 evidence artifact names or command output locations.
> - X-001 follow-up accepted dependency edge ruling if human-declared upstream/downstream edges change.

- **VER-001** — Review the preserved legacy source and execute its specified alias resolver, matrix mapping, route, loop-context, persona-resolution, fallback, unknown-key, unsupported-option, source-state, dependency-register, and evidence-capture checks; record concrete test or command-output evidence.

## Governing Values and Decisions — Axiology

### CLM-019 — Guidance: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

> #### Guidance: DEL-08-02 Persona Alias and Agent Matrix Routing Contract
>

### CLM-020 — Purpose

> ##### Purpose
>
> This deliverable exists to keep Chirality's visible agent matrix, UI aliases, canonical agent instruction names, and persona routing behavior aligned. It is a small UX/UI routing slice, but it protects a larger governance boundary: users select familiar UI labels and matrix cells, while the runtime must resolve those selections into canonical instruction-root agents and governed execution surfaces.
>

### CLM-021 — Principles

> ##### Principles
>
> 1. Treat `docs/TYPES.md` as the vocabulary source for aliases, matrix rows, matrix columns, and cell labels.
> 2. Treat `docs/PRD.md` as the product acceptance source for matrix routing, loop context, and persona resolution under the D-APP-38 authority corpus.
> 3. Keep alias resolution deterministic and complete for the active sourced alias set.
> 4. Do not create friendly aliases, hidden aliases, or fallback canonical names without a governed source update.
> 5. Preserve the difference between loop-persona routing and PIPELINE operative category routing.
> 6. Keep disabled or unsupported options visible when the product requirement says they should be visible as coming soon.
> 7. Keep runtime behavior warning-based for unknown option keys rather than letting unknown keys silently change behavior.
>

### CLM-022 — Considerations

> ##### Considerations
>
> The active alias contract covers UI labels that resolve to Type 0/1 personas:
>
> | UI Alias | Canonical Agent |
> |---|---|
> | `HELP` | `HELP_HUMAN` |
> | `ORCHESTRATE` | `ORCHESTRATOR` |
> | `AGENTS` | `HELPS_HUMANS` |
> | `DEPENDENCIES` | `EVALUATION` |
>
> Removed labels are deliberately not compatibility aliases:
>
> | UI Label | Former target | Current treatment |
> |---|---|---|
> | `AGGREGATE` | `AGGREGATION` | Not aliased; `AGGREGATION` is a Type 2 task agent. The NORMATIVE/REVIEWING cell uses `REVIEW`. |
> | `RECONCILING` | `RECONCILIATION` | Not aliased; the EVALUATIVE/REVIEWING cell uses `RESEARCH`. |
>
> The matrix contract currently covers these row destinations:
>
> | Row | Destination |
> |---|---|
> | `NORMATIVE` | Loop-persona intent |
> | `OPERATIVE` | PIPELINE |
> | `EVALUATIVE` | Loop-persona intent |
>
> The matrix cells from `docs/TYPES.md` use UI-facing labels and wildcard category labels. Loop-persona routing resolves persona-style cells only to Type 0/1 personas. PIPELINE routing preserves operative categories such as `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*` as pipeline category intent rather than forcing them through persona resolution.
>

### CLM-023 — Trade-offs

> ##### Trade-offs
>
> | Topic | Preferred Direction | Rationale | Open Detail |
> |---|---|---|---|
> | Alias strictness | Use only active Type 0/1 alias mappings. | Prevents hidden routing behavior and supports stable tests. | Unknown non-empty labels pass through normalized and then rely on instruction-file lookup. |
> | Matrix fixtures | Snapshot the canonical 3x4 vocabulary. | Protects UI navigation from drift across docs, fixtures, and implementation. | Exact fixture filenames are TBD. |
> | Loop context | Preserve agent, row, and column route context. | PRD requires active agent context and route state continuity. | Current route-state tests cover the mounted shell launch contract. |
> | Pipeline distinction | Keep operative cells as pipeline categories. | TYPES and PRD route OPERATIVE to PIPELINE rather than loop-persona routing. | Category enum spelling is covered by Pipeline tests. |
> | PRD source state | Use PRD content under D-APP-38. | `_REFERENCES.md` REF-006 now records MATCH under authority corpus v2. | Future authority-doc edits require corpus bump/apply. |
> | Dependency picture | Treat current extracted dependency rows as available context, while preserving declared human upstream/downstream edges as TBD. | `_DEPENDENCIES.md` records the dependency-extract run and 13 ACTIVE rows. | X-001 remains open only for later accepted human edge rulings, not because `Dependencies.csv` is absent. |
>

### CLM-024 — Examples

> ##### Examples
>
> Sourced examples:
>
> - Selecting the `HELP` alias should resolve to canonical `HELP_HUMAN`.
> - Selecting a NORMATIVE matrix cell should focus the mounted loop with Type 0/1 agent context.
> - Selecting an OPERATIVE matrix cell should route to PIPELINE with category context.
> - A missing persona should surface `PERSONA_NOT_FOUND`.
>
> Unsupported examples remain TBD:
>
> - Whether future aliases should be added by a governed source update.
>

### CLM-025 — Pass 3 Disposition Guidance

> ##### Pass 3 Disposition Guidance
>
> | ItemID | Guidance disposition |
> |---|---|
> | B-001 | Resolved by implementation: unknown non-empty labels pass through normalized, then `PERSONA_NOT_FOUND` is produced if no matching instruction file exists. |
> | C-001 | Resolved by D-APP-38 authority corpus v2; REF-006 is MATCH in `_REFERENCES.md`. |
> | E-001 | Resolved for source-state by D-APP-38; implementation proof remains separate from source proof. |
>

### CLM-026 — Conflict Table

> ##### Conflict Table
>
> The former PRD hash mismatch is resolved for this tranche by D-APP-38 and the current `_REFERENCES.md` REF-006 MATCH state.
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | C-001 | Former PRD source-state conflict resolved. | `_REFERENCES.md` REF-006 | D-APP-38 authority corpus v2 | Specification requirements and standards; Guidance principles and trade-offs | Use PRD content under the current authority corpus; keep implementation proof separate. | D-APP-38 accepted current authority corpus |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-005 SOW-006 SOW-017 OBJ-001 OBJ-007 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
