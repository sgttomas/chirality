---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-02
package_id: PKG-08
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
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
> | UI alias map | The sourced live aliases are HELP → HELP_HUMAN and AGENTS → HELPS_HUMANS. They create no additional roles; historical alias labels remain replay metadata. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026; D-APP-28 loop-first routing |
> | Legacy matrix rows | `NORMATIVE`, `OPERATIVE`, `EVALUATIVE` remain compatibility vocabulary, not a required target-shell layout. | `docs/TYPES.md` Section 4.1; SCA-APP-004 |
> | Legacy matrix columns | `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING` remain compatibility vocabulary, not a required target-shell layout. | `docs/TYPES.md` Section 4.2; SCA-APP-004 |
> | Legacy matrix routing destinations | Legacy matrix and Pipeline routes are historical compatibility after the 2026-09-09 removal. New selection follows the four-role registry; no matrix route is a current execution prerequisite. | D-APP-28/30/31 preserved compatibility; SCA-APP-004 |
> | Guarded dialogue/session selection | The user may continue a Codex conversation under D-GOV-43 item 5 or inspect preserved read-only history. Selection must preserve exact session identity and avoid clobbering another in-flight session or transferring draft, context, permissions or authority. | SCA-APP-004; preserved D-APP-30 safety rule |
> | Persona filename target | Selected roles resolve to the supplied canonical instruction basis. Missing or ineligible execution roles cannot acquire authority; historical labels remain historical. | `docs/PRD.md` FR-025 |
> | Persona fallback | New chats use HELP_HUMAN; direct entry is HELP_HUMAN, HELPS_HUMANS or WORKING_ITEMS. TASK is delegated only. Verify navigation fallback separately from execution eligibility. | `docs/SPEC.md` Section 13.1; `frontend/src/lib/shell/persona-resolution.ts` |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Source authority state | historical D-APP-38 source state; verify current candidate bytes. | `_REFERENCES.md`; D-APP-38 |
> | Governance posture | Unknown values remain `TBD`, and source conflicts must be surfaced rather than silently resolved. | `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |
> | Route shape constraint | Existing harness route shapes remain stable during SDK adoption and TurnEngine extraction. | `docs/SPEC.md` Section 17.1 |
> | Unsupported variants | Unsupported retained compatibility options must not initiate execution; removed legacy surfaces need not be recreated as coming-soon UI. | `docs/PRD.md`; SCA-APP-004 |
> | Semantic non-ownership | DEL-08-02 does not own shell presentation, Work-plan authority, dispatch semantics, replay evidence, child-run parentage, lifecycle, or approval. | SCA-APP-004 semantic ownership partition |
> | Dependency register state | `Dependencies.csv` exists in v3.1 format with 13 ACTIVE extracted rows; declared upstream/downstream human edges remain TBD. | `_DEPENDENCIES.md` Compact Register; `Dependencies.csv` |
>

### CLM-005 — Construction

> ##### Construction
>
> Construction must establish canonical role/session identity and preserve the user's navigation intent without granting execution authority. Current App `AGENTS.md` supplies the four-role operational basis; its use here is not a blanket D-GOV-42 exact-byte acceptance or an amendment of every older App clause.
>
> | Contract | Required outcome | Named verification hook and limit |
> |---|---|---|
> | Alias resolution | Use only sourced aliases and resolve to an eligible canonical role; aliases must not create additional roles or grant TASK direct-entry authority. | `frontend/src/__tests__/lib/persona-resolution.test.ts` checks the current HELP/AGENTS aliases, HELP_HUMAN default and three direct-entry roles. |
> | Persona identity | Preserve canonical role identity and the applicable instruction basis; missing or ineligible selections must not silently gain authority. | `frontend/src/__tests__/api/harness/routes.test.ts` and `frontend/src/__tests__/lib/persona-resolution.test.ts`; route and UI fallback subjects must be distinguished. |
> | Legacy navigation | Preserve compatibility only within the accepted retirement boundary. A fixed matrix is not required in the active shell; D-APP-108 Q3 is historical; the 2026-09-09 removal leaves matrix routes as preserved compatibility evidence. | `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` is compatibility evidence, not an active matrix acceptance check. |
> | Dialogue/session selection | Preserve exact selected identity, applicable query context and unknown parameters while guarding an in-flight primary session and retaining the adopted live/replay boundary. | `frontend/src/__tests__/lib/guarded-session-selection.test.ts` and `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`; live query-preservation and continuation/isolation verification remain open. |
> | Dispatch boundary | Navigation or selection may describe intent but must not grant dispatch, lifecycle or approval authority. Presentation-neutral dispatch remains owned by DEL-08-03. | `frontend/src/__tests__/lib/pipeline-dispatch-contract.test.ts` and `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`. |
>
> Implementation module names and query-key snapshots belong in those evidence records. The former F-001/D-001 implementation slots do not impose a recurring requirement to copy code paths or state keys into this deliverable. The updated requirement rows apply current role and continuation direction; lagging App authority-corpus clauses remain a separate owning amendment obligation.

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
> | REF-006 | `docs/PRD.md` | Product requirements; historical D-APP-38 source state; verify current candidate bytes. |
> | REF-007 | `../../workflows/software-decomp/WORKFLOW.md` | Decomposition method context. |
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
> | DEL-08-02-REQ-002 | New direct-entry selection MUST use the current four-role basis and sourced HELP/AGENTS aliases; historical ORCHESTRATE is not a new execution role. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026 | Alias resolver unit test. |
> | DEL-08-02-REQ-003 | TASK and historical Type 2 labels MUST NOT become direct-entry roles through aliases. | D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` Type 2 vocabulary | Negative alias resolver unit test and matrix guard test. |
> | DEL-08-02-REQ-004 | Historical RECONCILING and matrix labels MUST remain replay metadata and MUST NOT create execution roles. | D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` matrix vocabulary | Negative alias resolver unit test and matrix guard test. |
> | DEL-08-02-REQ-005 | The UI alias resolver MUST map `AGENTS` to `HELPS_HUMANS`. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026 | Alias resolver unit test. |
> | DEL-08-02-REQ-006 | Historical matrix row identity MUST remain readable in preserved records without requiring a live matrix. | `docs/TYPES.md` Section 4.1; SCA-APP-004 | Legacy matrix compatibility test. |
> | DEL-08-02-REQ-007 | Historical matrix column identity MUST remain readable in preserved records without requiring a live matrix. | `docs/TYPES.md` Section 4.2; SCA-APP-004 | Legacy matrix compatibility test. |
> | DEL-08-02-REQ-008 | Navigation MUST preserve the selected canonical eligible role and session identity without inferring execution authority from a historical NORMATIVE label. | Preserved D-APP-28 routing; SCA-APP-004 | Route/query fixture test. |
> | DEL-08-02-REQ-009 | Navigation MUST preserve selected role/session identity without inferring authority from a historical EVALUATIVE label. | Preserved D-APP-28 routing; SCA-APP-004 | Route/query fixture test. |
> | DEL-08-02-REQ-010 | Navigation MUST NOT revive a removed Pipeline route; presentation-neutral dispatch semantics remain owned by DEL-08-03. | Preserved D-APP-31 dispatch; SCA-APP-004 | Route/query fixture test. |
> | DEL-08-02-REQ-011 | Legacy and target routing MUST preserve exact selected agent/session identity and compatible agent/row/column query context without transferring another session's draft, context, permissions, or interaction authority. | SCA-APP-004; preserved D-APP-30 guard | Route-state and session-isolation test. |
> | DEL-08-02-REQ-012 | Selected execution roles MUST resolve to their supplied canonical instruction basis, preserving source identity and eligibility. | `docs/PRD.md` FR-025; `docs/SPEC.md` Section 13.2 | Persona resolver test with existing and missing personas. |
> | DEL-08-02-REQ-013 | A missing or ineligible role MUST NOT silently gain execution authority; record the actual resolution or denial result. | `docs/PRD.md` FR-025 | Negative persona resolver test. |
> | DEL-08-02-REQ-014 | New chats MUST default to HELP_HUMAN. Direct-entry eligibility follows the current four-role registry; UI fallback and execution admission MUST be checked separately. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` FR-023; current loop-first shell contract | Runtime option fallback and negative persona resolver tests. |
> | DEL-08-02-REQ-015 | Unknown runtime option keys MUST warn without silently mutating behavior. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` FR-024 | Runtime option warning test. |
> | DEL-08-02-REQ-016 | Unsupported retained controls MUST NOT initiate execution; removed legacy matrix/Pipeline surfaces are historical and are not required coming-soon controls. | `docs/PRD.md` Section 7.2; `docs/PRD.md` FR-011 | UI fixture or interaction test. |
> | DEL-08-02-REQ-017 | The implementation MUST NOT invent additional alias mappings, matrix rows, columns, or canonical persona names without a governed source update. | `docs/CONTRACT.md` K-INVENT-1; `docs/TYPES.md` Sections 3.4 and 4 | Fixture completeness and snapshot tests. |
> | DEL-08-02-REQ-018 | Session selection MUST guard against clobbering an in-flight session and distinguish user-selected Codex continuation from labelled read-only historical replay. | SCA-APP-004; preserved D-APP-30 safety rule | Guarded-selection interaction test. |
> | DEL-08-02-REQ-019 | Continuation MUST preserve the selected conversation identity; switching sessions MUST NOT merge or transfer another live dialogue’s draft, attachments, context, permissions, interruption state or interaction authority. | SCA-APP-004 selected concept | Session-isolation test. |
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
> | `docs/PRD.md` Sections 7.2, 7.4, 8.2, and 8.4 | Product requirements for matrix routing, workbench context, and persona resolution. | Historically reconciled under D-APP-38; verify current bytes. |
> | `docs/SPEC.md` Section 13 | Runtime option fallback and persona composer contract. | Accessible; hash match. |
> | `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 | Governance constraints for unsupported facts and source conflicts. | Accessible; hash match. |
> | `docs/DIRECTIVE.md` Sections 2.8 and 4.1 | Product-owned persona/system-prompt and matrix navigation scope. | Accessible; hash match. |
>

### CLM-011 — Verification

> Apply the current role and navigation contract in CLM-003/009 under D-APP-131 P-06/P-11/P-22 and D-GOV-43 item 5. HELP_HUMAN is the new-chat default; HELP and AGENTS are sourced aliases; TASK is delegated only. Legacy matrix/Pipeline labels remain historical after the 2026-09-09 removal. Preserve selected identity, compatible query context and unknown query parameters, distinguish continuation from read-only replay, and prevent cross-session state or authority transfer.
>
> Named verification: `frontend/src/__tests__/lib/persona-resolution.test.ts`, `guarded-session-selection.test.ts` and `pkg08-compatibility-boundaries.test.ts`. These locations are hooks, not fresh results; live query-preservation and continuation/isolation evidence remain required. Preserve applicable unknown-option warning behavior without reviving an obsolete fallback chain. The former alias/default/matrix owner questions are settled for this record by the supplied four-role basis and prior continuation direction; amendments of lagging App corpus clauses remain with their owner, not a repeated vote. Current hash verification is required; D-APP-38 MATCH is historical. Record the candidate, applicable basis, actual result, and unresolved coverage in ScopeOfWork.md-linked evidence.

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
> Implementation evidence is named in CLM-005; record actual candidate-bound results rather than keeping selected paths as TBD.

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
> | Authoritative sources listed in `_REFERENCES.md` are locally accessible. | Satisfied; historical D-APP-38 source state; verify current candidate bytes. |
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

> Apply the current role and navigation contract in CLM-003/009 under D-APP-131 P-06/P-11/P-22 and D-GOV-43 item 5. HELP_HUMAN is the new-chat default; HELP and AGENTS are sourced aliases; TASK is delegated only. Legacy matrix/Pipeline labels remain historical after the 2026-09-09 removal. Preserve selected identity, compatible query context and unknown query parameters, distinguish continuation from read-only replay, and prevent cross-session state or authority transfer.
>
> Named verification: `frontend/src/__tests__/lib/persona-resolution.test.ts`, `guarded-session-selection.test.ts` and `pkg08-compatibility-boundaries.test.ts`. These locations are hooks, not fresh results; live query-preservation and continuation/isolation evidence remain required. Preserve applicable unknown-option warning behavior without reviving an obsolete fallback chain. The former alias/default/matrix owner questions are settled for this record by the supplied four-role basis and prior continuation direction; amendments of lagging App corpus clauses remain with their owner, not a repeated vote. Current hash verification is required; D-APP-38 MATCH is historical. Record the candidate, applicable basis, actual result, and unresolved coverage in ScopeOfWork.md-linked evidence.

### CLM-018 — Records

> Apply the current role and navigation contract in CLM-003/009 under D-APP-131 P-06/P-11/P-22 and D-GOV-43 item 5. HELP_HUMAN is the new-chat default; HELP and AGENTS are sourced aliases; TASK is delegated only. Legacy matrix/Pipeline labels remain historical after the 2026-09-09 removal. Preserve selected identity, compatible query context and unknown query parameters, distinguish continuation from read-only replay, and prevent cross-session state or authority transfer.
>
> Named verification: `frontend/src/__tests__/lib/persona-resolution.test.ts`, `guarded-session-selection.test.ts` and `pkg08-compatibility-boundaries.test.ts`. These locations are hooks, not fresh results; live query-preservation and continuation/isolation evidence remain required. Preserve applicable unknown-option warning behavior without reviving an obsolete fallback chain. The former alias/default/matrix owner questions are settled for this record by the supplied four-role basis and prior continuation direction; amendments of lagging App corpus clauses remain with their owner, not a repeated vote. Current hash verification is required; D-APP-38 MATCH is historical. Record the candidate, applicable basis, actual result, and unresolved coverage in ScopeOfWork.md-linked evidence.

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

> Apply the current role and navigation contract in CLM-003/009 under D-APP-131 P-06/P-11/P-22 and D-GOV-43 item 5. HELP_HUMAN is the new-chat default; HELP and AGENTS are sourced aliases; TASK is delegated only. Legacy matrix/Pipeline labels remain historical after the 2026-09-09 removal. Preserve selected identity, compatible query context and unknown query parameters, distinguish continuation from read-only replay, and prevent cross-session state or authority transfer.
>
> Named verification: `frontend/src/__tests__/lib/persona-resolution.test.ts`, `guarded-session-selection.test.ts` and `pkg08-compatibility-boundaries.test.ts`. These locations are hooks, not fresh results; live query-preservation and continuation/isolation evidence remain required. Preserve applicable unknown-option warning behavior without reviving an obsolete fallback chain. The former alias/default/matrix owner questions are settled for this record by the supplied four-role basis and prior continuation direction; amendments of lagging App corpus clauses remain with their owner, not a repeated vote. Current hash verification is required; D-APP-38 MATCH is historical. Record the candidate, applicable basis, actual result, and unresolved coverage in ScopeOfWork.md-linked evidence.

### CLM-022 — Considerations

> Apply the current role and navigation contract in CLM-003/009 under D-APP-131 P-06/P-11/P-22 and D-GOV-43 item 5. HELP_HUMAN is the new-chat default; HELP and AGENTS are sourced aliases; TASK is delegated only. Legacy matrix/Pipeline labels remain historical after the 2026-09-09 removal. Preserve selected identity, compatible query context and unknown query parameters, distinguish continuation from read-only replay, and prevent cross-session state or authority transfer.
>
> Named verification: `frontend/src/__tests__/lib/persona-resolution.test.ts`, `guarded-session-selection.test.ts` and `pkg08-compatibility-boundaries.test.ts`. These locations are hooks, not fresh results; live query-preservation and continuation/isolation evidence remain required. Preserve applicable unknown-option warning behavior without reviving an obsolete fallback chain. The former alias/default/matrix owner questions are settled for this record by the supplied four-role basis and prior continuation direction; amendments of lagging App corpus clauses remain with their owner, not a repeated vote. Current hash verification is required; D-APP-38 MATCH is historical. Record the candidate, applicable basis, actual result, and unresolved coverage in ScopeOfWork.md-linked evidence.

### CLM-023 — Trade-offs

> Apply the current role and navigation contract in CLM-003/009 under D-APP-131 P-06/P-11/P-22 and D-GOV-43 item 5. HELP_HUMAN is the new-chat default; HELP and AGENTS are sourced aliases; TASK is delegated only. Legacy matrix/Pipeline labels remain historical after the 2026-09-09 removal. Preserve selected identity, compatible query context and unknown query parameters, distinguish continuation from read-only replay, and prevent cross-session state or authority transfer.
>
> Named verification: `frontend/src/__tests__/lib/persona-resolution.test.ts`, `guarded-session-selection.test.ts` and `pkg08-compatibility-boundaries.test.ts`. These locations are hooks, not fresh results; live query-preservation and continuation/isolation evidence remain required. Preserve applicable unknown-option warning behavior without reviving an obsolete fallback chain. The former alias/default/matrix owner questions are settled for this record by the supplied four-role basis and prior continuation direction; amendments of lagging App corpus clauses remain with their owner, not a repeated vote. Current hash verification is required; D-APP-38 MATCH is historical. Record the candidate, applicable basis, actual result, and unresolved coverage in ScopeOfWork.md-linked evidence.

### CLM-024 — Examples

> Apply the current role and navigation contract in CLM-003/009 under D-APP-131 P-06/P-11/P-22 and D-GOV-43 item 5. HELP_HUMAN is the new-chat default; HELP and AGENTS are sourced aliases; TASK is delegated only. Legacy matrix/Pipeline labels remain historical after the 2026-09-09 removal. Preserve selected identity, compatible query context and unknown query parameters, distinguish continuation from read-only replay, and prevent cross-session state or authority transfer.
>
> Named verification: `frontend/src/__tests__/lib/persona-resolution.test.ts`, `guarded-session-selection.test.ts` and `pkg08-compatibility-boundaries.test.ts`. These locations are hooks, not fresh results; live query-preservation and continuation/isolation evidence remain required. Preserve applicable unknown-option warning behavior without reviving an obsolete fallback chain. The former alias/default/matrix owner questions are settled for this record by the supplied four-role basis and prior continuation direction; amendments of lagging App corpus clauses remain with their owner, not a repeated vote. Current hash verification is required; D-APP-38 MATCH is historical. Record the candidate, applicable basis, actual result, and unresolved coverage in ScopeOfWork.md-linked evidence.

### CLM-025 — Pass 3 Disposition Guidance

> Apply the current role and navigation contract in CLM-003/009 under D-APP-131 P-06/P-11/P-22 and D-GOV-43 item 5. HELP_HUMAN is the new-chat default; HELP and AGENTS are sourced aliases; TASK is delegated only. Legacy matrix/Pipeline labels remain historical after the 2026-09-09 removal. Preserve selected identity, compatible query context and unknown query parameters, distinguish continuation from read-only replay, and prevent cross-session state or authority transfer.
>
> Named verification: `frontend/src/__tests__/lib/persona-resolution.test.ts`, `guarded-session-selection.test.ts` and `pkg08-compatibility-boundaries.test.ts`. These locations are hooks, not fresh results; live query-preservation and continuation/isolation evidence remain required. Preserve applicable unknown-option warning behavior without reviving an obsolete fallback chain. The former alias/default/matrix owner questions are settled for this record by the supplied four-role basis and prior continuation direction; amendments of lagging App corpus clauses remain with their owner, not a repeated vote. Current hash verification is required; D-APP-38 MATCH is historical. Record the candidate, applicable basis, actual result, and unresolved coverage in ScopeOfWork.md-linked evidence.

### CLM-026 — Conflict Table

> Apply the current role and navigation contract in CLM-003/009 under D-APP-131 P-06/P-11/P-22 and D-GOV-43 item 5. HELP_HUMAN is the new-chat default; HELP and AGENTS are sourced aliases; TASK is delegated only. Legacy matrix/Pipeline labels remain historical after the 2026-09-09 removal. Preserve selected identity, compatible query context and unknown query parameters, distinguish continuation from read-only replay, and prevent cross-session state or authority transfer.
>
> Named verification: `frontend/src/__tests__/lib/persona-resolution.test.ts`, `guarded-session-selection.test.ts` and `pkg08-compatibility-boundaries.test.ts`. These locations are hooks, not fresh results; live query-preservation and continuation/isolation evidence remain required. Preserve applicable unknown-option warning behavior without reviving an obsolete fallback chain. The former alias/default/matrix owner questions are settled for this record by the supplied four-role basis and prior continuation direction; amendments of lagging App corpus clauses remain with their owner, not a repeated vote. Current hash verification is required; D-APP-38 MATCH is historical. Record the candidate, applicable basis, actual result, and unresolved coverage in ScopeOfWork.md-linked evidence.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-005 SOW-006 SOW-017 OBJ-001 OBJ-007 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
