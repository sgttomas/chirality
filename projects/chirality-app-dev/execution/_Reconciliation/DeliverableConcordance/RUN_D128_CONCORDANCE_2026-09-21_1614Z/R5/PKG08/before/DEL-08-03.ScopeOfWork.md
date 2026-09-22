---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-03
package_id: PKG-08
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-007, SOW-026]
package_objective_refs: [OBJ-001, OBJ-007]
---

# Scope of Work — DEL-08-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-08-03` in service of project scope [SOW-007, SOW-026] and package objectives [OBJ-001, OBJ-007].

- **OUT-001** — Presentation-neutral DECOMP/PREP/TASK/AUDIT dispatch semantics, category/task-scope interpretation, dynamic scope, and disabled-option rules with selector, contextual-consumer, knowledge-type discovery, and regression evidence.

## SCA-APP-010 Gate-5 Current Contract (Controlling)

The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied
2026-09-04 at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged
as `7795b0972cac147869607d994173753e4a2fc232`; active pointer moved as
`311a2f0b811d55315d6eb623130cad0be1417565`) makes the centre dialogue the
invariant primary surface and seats the prompted specification ladder. Where any
earlier current-contract section or older clause in this document disagrees with
the applied row below, this section controls. Earlier sections, clauses, and
evidence remain dated compatibility history and are not deleted.

### Current responsibility

`DEL-08-03 Pipeline Category and Task Scope Dispatch` (UX_UI_SLICE, applied decomposition row L370):

Own presentation-neutral DECOMP/PREP/TASK/AUDIT lane semantics,
category/task-scope interpretation, dynamic scope, and disabled-option rules for
contextual Run consumers.

Applied row notes: Semantic dispatch owner; the contextual Pipeline presentation
is retired from the active shell by SCA-APP-010 (code retained), so no active
presentation consumer exists; any later consumer may not infer plans/tasks from
conversational prose.

Applied row outputs: Dispatch contract tests; Pipeline selector tests;
knowledge-type discovery; dynamic-scope and disabled-option handling.

### Current acceptance obligations

1. DECOMP/PREP/TASK/AUDIT lane semantics, category and task-scope interpretation, dynamic scope, and disabled-option rules remain presentation-neutral and owned here.
2. The contextual Pipeline presentation is retired from the active shell by SCA-APP-010 (code retained); no active presentation consumer exists.
3. Any later consumer may not infer plans or tasks from conversational prose.

### Seating and rulings

Remaining items seated under D-APP-108 (2026-09-04): none (record-only). Ruled
questions applied here: SOW-007 presentation retirement (G2-CONFIRM). Alignment
writes WI-056, WI-057, WI-058, WI-059, WI-060 performed in run
`APP_SCA_APP_010_SEATING_2026-09-04`; dependency writes DEP-023, DEP-024 await
the registered dependency-extract pass after owner acceptance of this alignment.
No lifecycle, Checking Approval SHA, dependency-acceptance, product, or release
act is implied.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-08-03 Pipeline Category and Task Scope Dispatch

> #### Datasheet: DEL-08-03 Pipeline Category and Task Scope Dispatch
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
> | PackageID | PKG-08 |
> | PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
> | DeliverableID | DEL-08-03 |
> | DeliverableName | Pipeline Category and Task Scope Dispatch |
> | ResponsibleParty | TBD |
> | Type | UX_UI_SLICE |
> | ContextEnvelope | M |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Scope | Own presentation-neutral DECOMP/PREP/TASK/AUDIT lane semantics, category/task-scope interpretation, dynamic scope, and disabled-option rules for contextual Run consumers. | `_CONTEXT.md`; decomposition entry; SCA-APP-004 |
> | Package scope | Agent instruction conformance, matrix/pipeline dispatch, Type 2 subagent governance and child records. | `_CONTEXT.md`; decomposition PKG-08 row |
> | Inclusion criteria | Agent OS behavior and delegation. | `_CONTEXT.md`; decomposition PKG-08 row |
> | Exclusions | General SDK adapter mechanics. | `_CONTEXT.md`; decomposition PKG-08 row |
> | Covered scope items | SOW-007, SOW-026 | `_CONTEXT.md`; decomposition entry |
> | Supported objectives | OBJ-001, OBJ-007 | `_CONTEXT.md`; decomposition entry |
> | Anticipated artifacts | Dispatch contract tests; Pipeline selector and contextual-consumer tests; knowledge-type discovery; dynamic-scope and disabled-option handling | `_CONTEXT.md`; decomposition entry |
> | Pipeline categories | `DECOMP*`, `PREP*`, `TASK*`, `AUDIT*` | `docs/TYPES.md` Section 4.4 |
> | TASK scope modes | `DELIVERABLES`, `KNOWLEDGE_TYPES` | `docs/TYPES.md` Section 4.4 |
> | Knowledge type options | `Datasheet`, `Specification`, `Guidance`, `Procedure`, `Dependencies`, `References`, `Context`, `Status`, `Semantic`, `Memory` | `docs/TYPES.md` Section 4.4 |
> | Disabled option meaning | Visible but non-selectable coming-soon or unsupported variant. | `docs/TYPES.md` Section 4.4 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | PIPELINE category controls | The PIPELINE surface exposes `DECOMP`, `PREP`, `TASK`, and `AUDIT` category controls. | `docs/PRD.md` FR-011 |
> | Unsupported options | Unsupported options remain visible and disabled as coming soon. | `docs/PRD.md` FR-011; success metric 7 |
> | TASK selector split | PIPELINE `TASK` uses split selectors for task agent and scope. | `docs/PRD.md` FR-012 |
> | TASK scope requirement | Scope mode is `DELIVERABLES` or `KNOWLEDGE_TYPES`; target deliverable is required for knowledge-type mode. | `docs/PRD.md` FR-012 |
> | Dynamic reset | Root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets clear invalid selection state. | `docs/PRD.md` FR-013 |
> | Knowledge bucket detection | Datasheet, Specification, Guidance, and Procedure are supported as first-class knowledge buckets. | `docs/PRD.md` FR-049 |
> | Working-root scope API | `/api/project/deliverables` scans deliverables and knowledge types for the active root. | `docs/SPEC.md` Section 17.2; D-APP-56 R4-P21 |
> | Presentation ownership | DEL-02-02 presents re-hosted Workbench/Pipeline and Coordination Panel consumers; DEL-08-03 remains semantic dispatch owner. | SCA-APP-004 semantic ownership partition |
> | Work projection boundary | A Work-panel item may display an explicitly recorded dispatch/task basis with provenance and currency, but conversational prose is never silently converted into a plan/task and runtime completion is not project acceptance. | SCA-APP-004 coordination-projection invariant |
> | Child-record boundary | DEL-08-05 remains the unchanged owner of child-run parentage, assignment, return, and artifact records. | SCA-APP-004 no-change set |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component / Surface | Expected Role | Status |
> |---|---|---|
> | Pipeline category selector | Selects operative lane for `DECOMP`, `PREP`, `TASK`, or `AUDIT`. | `frontend/src/components/pipeline/pipeline-surface.tsx` |
> | Category option list | Shows documented options for selected lane; unsupported variants are disabled. | `frontend/src/components/pipeline/pipeline-surface.tsx`; `frontend/src/__tests__/components/pipeline-surface.test.ts` |
> | TASK agent selector | Selects the bounded task agent or skill route. | `frontend/src/components/pipeline/pipeline-surface.tsx` |
> | TASK scope mode selector | Switches between deliverable scope and knowledge-type scope. | `frontend/src/components/pipeline/pipeline-surface.tsx` |
> | Dynamic deliverable scan | Provides valid deliverable targets from the active working root. | `frontend/src/components/pipeline/pipeline-surface.tsx`; `frontend/src/lib/workspace/filesystem.ts` |
> | Knowledge-type discovery | Detects document-kit and metadata buckets from deliverable content. | `frontend/src/lib/workspace/filesystem.ts`; `frontend/src/__tests__/api/project/deliverables-route.test.ts` |
> | Invalid-selection reset | Clears stale or disabled selections after root or scope changes. | `frontend/src/components/pipeline/pipeline-surface.tsx`; `frontend/src/__tests__/components/pipeline-surface.test.ts`; `frontend/src/__tests__/lib/task-scope-selection.test.ts` |
> | Tests | Cover pipeline selector behavior, knowledge-type discovery, and disabled option handling. | `frontend/src/__tests__/components/pipeline-surface.test.ts`; `frontend/src/__tests__/lib/task-scope-selection.test.ts` |
>

### CLM-006 — Implementation Slots

> ##### Implementation Slots
>
> | Slot | Required Record | Current Disposition |
> |---|---|---|
> | Category selector component path | Confirmed frontend component or module path for PIPELINE `DECOMP`, `PREP`, `TASK`, and `AUDIT` controls. | `frontend/src/components/pipeline/pipeline-surface.tsx` |
> | Category option source | Confirmed data source or fixture for category-specific option lists. | Local option arrays in `pipeline-surface.tsx`, tested by `frontend/src/__tests__/components/pipeline-surface.test.ts`. |
> | TASK selector component path | Confirmed component or state module for task-agent selector and scope selector. | `frontend/src/components/pipeline/pipeline-surface.tsx` |
> | Scope scan integration path | Confirmed API client, hook, or mock boundary for `/api/project/deliverables`. | `pipeline-surface.tsx` consumes scan data; API mapping is covered by `frontend/src/__tests__/api/project/deliverables-route.test.ts`. |
> | Knowledge discovery fixture path | Confirmed fixture or test-data path covering document-kit buckets and any exposed metadata buckets. | `frontend/src/__tests__/api/project/deliverables-route.test.ts`; `frontend/src/__tests__/lib/task-scope-selection.test.ts`. |
> | Reset test fixture path | Confirmed fixture path for root-change, removed-deliverable, disabled-marker, and stale-target reset cases. | `frontend/src/__tests__/components/pipeline-surface.test.ts`; `frontend/src/__tests__/lib/task-scope-selection.test.ts`. |
>

### CLM-007 — Dependency Edge Snapshot

> ##### Dependency Edge Snapshot
>
> | Edge Type | Current Evidence | Disposition |
> |---|---|---|
> | Accepted upstream anchors | `_DEPENDENCIES.md` lists active anchors for DEL-08-03, SOW-007, SOW-026, OBJ-001, and OBJ-007. | Use as context; satisfaction remains TBD until dependency closure accepts the register. |
> | Accepted upstream interfaces and constraints | `_DEPENDENCIES.md` lists active execution rows for `docs/TYPES.md` Section 4.4, `docs/SPEC.md` Section 17.2, `docs/CONTRACT.md` Section 1.8, and `docs/PRD.md` Section 8.2. | Use as current extracted evidence under D-APP-38 and REF-006 `MATCH`. |
> | Downstream handoff | `_DEPENDENCIES.md` lists a downstream handoff to pipeline selector, knowledge-type discovery, and disabled option tests, with consumer target unresolved. | Consumer deliverable remains TBD. |
>

### CLM-008 — References

> ##### References
>
> | RefID | Path | Use |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Agent and working-root governance context |
> | REF-002 | `docs/CONTRACT.md` | Agent/subagent governance invariants |
> | REF-003 | `docs/SPEC.md` | Scope API and file contract surfaces |
> | REF-004 | `docs/TYPES.md` | Pipeline category, task scope, knowledge-type, and disabled-option vocabulary |
> | REF-005 | `docs/PLAN.md` | Runtime roadmap and retired-scope boundaries |
> | REF-006 | `docs/PRD.md` | Product requirements for matrix, pipeline, scope, and knowledge buckets; current under D-APP-38 authority corpus |
> | REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | SOFTWARE_DECOMP method and deliverable sizing context |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Accepted deliverable entry and objective/scope mapping |
>

### CLM-009 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | B-001 | Converted to explicit implementation slots for selector, option-list, scope-scan, knowledge-discovery, reset-fixture, and test-path records. |
> | B-002 | Incorporated as a dependency edge snapshot that preserves accepted extracted rows as context while leaving closure status and downstream consumer target TBD. |
>

### CLM-010 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-134 supersedes run-scoped dependency deferral wording: the extracted derivative register exists and is live.

## Completion and Reliance Basis — Epistemology

### CLM-011 — Specification: DEL-08-03 Pipeline Category and Task Scope Dispatch

> #### Specification: DEL-08-03 Pipeline Category and Task Scope Dispatch
>

### CLM-012 — Scope

> ##### Scope
>
> This deliverable specifies presentation-neutral PIPELINE category and TASK
> scope dispatch behavior for Chirality App vNext. DEL-02-02 may present these
> semantics in contextual Run, Workbench, Pipeline, or Work-panel surfaces,
> but presentation does not transfer dispatch authority.
>
> In scope:
>
> - PIPELINE category selection for `DECOMP`, `PREP`, `TASK`, and `AUDIT`.
> - Category-specific option presentation, including disabled unsupported options.
> - TASK split selectors for task agent and scope.
> - Dynamic TASK scope from deliverables and knowledge-type buckets.
> - Invalid-selection reset behavior when the active working root or scanned scope changes.
> - Tests for pipeline selector behavior, knowledge-type discovery, and disabled option handling.
> - Contract and regression evidence proving contextual consumers preserve the same dispatch semantics and do not synthesize work from conversation.
>
> Out of scope:
>
> - General SDK adapter mechanics.
> - Type 2 subagent runtime governance bridge implementation, except where selector behavior must not expand authority.
> - Dependency extraction or modification for this deliverable run; the existing `Dependencies.csv` remains unchanged.
> - Retired unified pipeline run-record or broader PKG-08 hardening scope unless a governed amendment reactivates it.
> - Work/Agents Coordination Panel shell presentation, project-plan authority, runtime checklist truth, lifecycle/approval status, replay persistence, parent-child records, scheduling, direct child messaging, or editable agent graphs.
>

### CLM-013 — Requirements

> ##### Requirements
>
> | ID | Requirement | Priority / Status | Source |
> |---|---|---|---|
> | DEL-08-03-REQ-001 | The PIPELINE UI shall expose operative category controls for `DECOMP`, `PREP`, `TASK`, and `AUDIT`. | P0 | `docs/PRD.md` FR-011 |
> | DEL-08-03-REQ-002 | Category controls shall present documented category-specific options for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*`; the implementation record shall name the option-list source or fixture used for each category. | P0 | `docs/PRD.md` FR-011; `docs/TYPES.md` Section 4.4 |
> | DEL-08-03-REQ-003 | Unsupported PIPELINE variants shall remain visible, shall carry disabled or coming-soon semantics, and shall be unable to initiate execution. | P0 | `docs/PRD.md` FR-011; `docs/TYPES.md` Section 4.4; `docs/PRD.md` success metric 7 |
> | DEL-08-03-REQ-004 | PIPELINE `TASK` shall use split selectors for task agent and scope. | P0 | `docs/PRD.md` FR-012 |
> | DEL-08-03-REQ-005 | TASK scope mode shall support `DELIVERABLES` and `KNOWLEDGE_TYPES`. | P0 | `docs/PRD.md` FR-012; `docs/TYPES.md` Section 4.4 |
> | DEL-08-03-REQ-006 | Knowledge-type mode shall require a target deliverable. | P0 | `docs/PRD.md` FR-012 |
> | DEL-08-03-REQ-007 | Dynamic scope scan shall reset invalid selection state when roots change, deliverables disappear, knowledge markers are disabled, or knowledge targets become stale. | P1 | `docs/PRD.md` FR-013 |
> | DEL-08-03-REQ-008 | Knowledge-type discovery shall support document-kit files as first-class knowledge buckets: Datasheet, Specification, Guidance, and Procedure. | P1 | `docs/PRD.md` FR-049 |
> | DEL-08-03-REQ-009 | Knowledge-type discovery shall align with the canonical `KnowledgeTypeOption` vocabulary when metadata buckets are exposed. | P1 | `docs/TYPES.md` Section 4.4 |
> | DEL-08-03-REQ-010 | Scope scanning shall use the active working-root scope surface rather than hard-coded project assumptions, with evidence showing a call, mock contract, or fixture for `/api/project/deliverables`. | P0 | `docs/SPEC.md` Section 17.2; `docs/PRD.md` FR-013; D-APP-56 R4-P21 |
> | DEL-08-03-REQ-011 | Dispatch behavior shall not expand agent authority or bypass Type 2 governance constraints; pass evidence shall show selector state cannot bypass write-scope, sealed-context, no-ghost-input, approval-reference, or fail-closed delegation gates. | P0 | `docs/CONTRACT.md` K-WRITE-1, K-SEAL-1, K-GHOST-1, K-SUBAGENT-1 |
> | DEL-08-03-REQ-012 | Selector tests shall cover pipeline selector behavior, knowledge-type discovery, disabled option handling, and invalid-selection reset fixtures for root change, removed deliverable, disabled marker, and stale knowledge target. | P1 | Decomposition anticipated artifacts; `docs/PRD.md` FR-013 |
> | DEL-08-03-REQ-013 | Dispatch semantics MUST remain presentation-neutral: re-hosted or contextual consumers owned by DEL-02-02 MUST use the same DECOMP/PREP/TASK/AUDIT taxonomy, category options, task-scope rules, dynamic-scope validation, and disabled states. | P0 | SCA-APP-004; SOW-007 |
> | DEL-08-03-REQ-014 | A Work/Agents consumer MUST display only explicitly recorded dispatch/task sources with provenance, status basis, and currency; it MUST NOT convert conversational prose or UI grouping into a structured plan/task. | P0 | SCA-APP-004 coordination-projection invariant |
> | DEL-08-03-REQ-015 | Runtime task/check completion MUST remain distinct from governed project-plan completion, deliverable lifecycle state, approval, issuance, or professional reliance. | P0 | `docs/CONTRACT.md` K-FS-1, K-NOMEM-1, K-BIND-1; SCA-APP-004 |
> | DEL-08-03-REQ-016 | DEL-08-03 MUST NOT own Coordination Panel presentation, general plan authority, replay persistence, child-run parentage, scheduling, direct child messaging, or lifecycle transition. | P0 | SCA-APP-004 semantic ownership partition |
>

### CLM-014 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Evidence |
> |---|---|---|
> | Chirality `PipelineCategory` vocabulary | Defines operative category terms for dispatch. | `docs/TYPES.md` Section 4.4 |
> | Chirality `TaskScopeMode` vocabulary | Defines valid TASK scope modes. | `docs/TYPES.md` Section 4.4 |
> | Chirality `KnowledgeTypeOption` vocabulary | Defines knowledge bucket labels available for discovery. | `docs/TYPES.md` Section 4.4 |
> | Chirality disabled-option vocabulary | Defines visible but non-selectable options. | `docs/TYPES.md` Section 4.4 |
> | PRD Matrix, Workbench, and Pipeline requirements | Defines product behavior for PIPELINE and TASK selectors. | `docs/PRD.md` Section 8.2 |
> | SPEC workspace API contract | Defines scope scan endpoint purpose. | `docs/SPEC.md` Section 17.2 |
> | Agent/subagent governance invariants | Constrain dispatch behavior from expanding authority. | `docs/CONTRACT.md` Section 1.8 |
>

### CLM-015 — Verification

> ##### Verification
>
> | Requirement IDs | Verification Approach | Expected Evidence |
> |---|---|---|
> | DEL-08-03-REQ-001, DEL-08-03-REQ-002 | UI/unit tests for category selector rendering and option lists, with the option-list source or fixtures named for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*`. | Pipeline selector tests plus category option fixture record |
> | DEL-08-03-REQ-003 | UI/unit tests verifying disabled unsupported variants remain visible, communicate disabled or coming-soon semantics, and cannot initiate execution. | Disabled option handling tests |
> | DEL-08-03-REQ-004, DEL-08-03-REQ-005, DEL-08-03-REQ-006 | UI/state tests for split TASK selectors and required target deliverable behavior. | TASK selector state tests |
> | DEL-08-03-REQ-007 | State transition tests using named fixtures for root change, removed deliverable, disabled marker, and stale knowledge target. | Stale selection reset tests plus fixture inventory |
> | DEL-08-03-REQ-008, DEL-08-03-REQ-009 | Scope scan and UI tests for document-kit buckets (`Datasheet`, `Specification`, `Guidance`, `Procedure`) and any exposed metadata buckets using canonical `KnowledgeTypeOption` labels. | Knowledge-type discovery tests |
> | DEL-08-03-REQ-010 | API integration or mocked API contract tests for `/api/project/deliverables`, including evidence that returned deliverables and knowledge buckets come from the active working root. | Scope scan integration tests |
> | DEL-08-03-REQ-011 | Governance regression tests or review checks proving dispatch does not enable unauthorized Type 2 execution or bypass sealed context, approval metadata, no-ghost-input limits, write-scope limits, or fail-closed delegation. | Governance guard tests or review evidence |
> | DEL-08-03-REQ-012 | Test inventory review with named category, TASK scope, discovery, disabled-option, and reset fixtures. | Named tests or fixtures covering anticipated artifacts |
> | DEL-08-03-REQ-013 | Cross-surface regression proves existing Pipeline and contextual Run consumers resolve identical categories, options, task scope, dynamic validation, and disabled state. | Dispatch contract and contextual-consumer tests |
> | DEL-08-03-REQ-014, DEL-08-03-REQ-015, DEL-08-03-REQ-016 | Projection/boundary tests show only admitted work sources are rendered, prose is not synthesized into tasks, runtime/project statuses remain separate, and presentation/parentage/lifecycle controls stay outside DEL-08-03. | Work projection and semantic non-ownership evidence |
>

### CLM-016 — Documentation

> ##### Documentation
>
> Required or expected artifacts:
>
> - Pipeline selector tests.
> - Knowledge-type discovery tests.
> - Disabled option handling tests.
> - TASK scope selector fixtures for `DELIVERABLES` and `KNOWLEDGE_TYPES`.
> - Category-specific option-list source or fixture record for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*`.
> - Evidence that invalid selections reset after root and scan changes, including root-change, removed-deliverable, disabled-marker, and stale-target fixtures.
> - Scope-scan evidence showing `/api/working-root/scope` integration or a mocked equivalent for active-root scanning.
> - Governance guard evidence showing selector state does not bypass Type 2 sealed context, approval metadata, no-ghost-input limits, write-scope limits, or fail-closed delegation.
> - Cross-surface dispatch evidence proving contextual Run/Workbench/Work-panel consumers preserve Pipeline taxonomy, scope validation, and disabled states.
> - Projection evidence proving only explicitly recorded task/dispatch sources appear, conversational prose is not synthesized into structured work, and runtime status is not presented as project acceptance.
> - ASSUMPTION: implementation notes may be needed once actual frontend component/module paths are selected.
>

### CLM-017 — Source State

> ##### Source State
>
> | State ID | Statement | Impact |
> |---|---|---|
> | STATE-001 | `docs/PRD.md` is current under the D-APP-38 authority corpus; `_REFERENCES.md` records REF-006 as `MATCH`. | Former PRD source-state warning is resolved for this tranche. Implementation proof remains separate from source-state proof. |
>

### CLM-018 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | F-001 | Incorporated by adding a minimum governance proof threshold to DEL-08-03-REQ-011 and its verification evidence. |
> | X-001 | Incorporated by requiring named option-list sources or fixtures for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*`. |
> | X-002 | Incorporated by naming required document-kit discovery evidence and canonical `KnowledgeTypeOption` treatment for any exposed metadata buckets. |
> | X-003 | Incorporated by requiring visible, disabled or coming-soon semantics, and inability to initiate execution as one disabled-option evidence set. |
>

### CLM-019 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-134 supersedes run-scoped dependency deferral wording: the extracted derivative register exists and is live.

- **AC-001** — Presentation-neutral dispatch contract, Pipeline/contextual-consumer selector tests, knowledge-type discovery fixtures, dynamic-scope and disabled-option handling, governance guards, and Work-projection non-authority evidence.

## Production and Verification Method — Praxeology

### CLM-020 — Procedure: DEL-08-03 Pipeline Category and Task Scope Dispatch

> #### Procedure: DEL-08-03 Pipeline Category and Task Scope Dispatch
>

### CLM-021 — Purpose

> ##### Purpose
>
> Define an operational procedure for producing and verifying the DEL-08-03 implementation artifacts: pipeline selector tests, knowledge-type discovery behavior, and disabled option handling.
>

### CLM-022 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Source |
> |---|---|
> | Accepted decomposition entry for DEL-08-03 | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
> | Deliverable metadata files | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`, `_STATUS.md` present |
> | Authoritative vocabulary | `docs/TYPES.md` Section 4.4 |
> | Product requirements | `docs/PRD.md` Section 8.2; current under D-APP-38 with REF-006 `MATCH` |
> | Workspace scope API contract | `docs/SPEC.md` Section 17.2 |
> | Declared upstream dependencies | Extracted active rows exist in `_DEPENDENCIES.md` for accepted anchors, vocabulary, scope API, governance invariants, and PRD requirements; satisfaction remains TBD pending dependency closure. |
> | Declared downstream dependencies | `_DEPENDENCIES.md` records downstream handoff to pipeline selector, knowledge-type discovery, and disabled option tests; consumer target remains TBD. |
>

### CLM-023 — Steps

> ##### Steps
>
> 1. Confirm the implementation location for the PIPELINE category and TASK scope selector UI.
>    - If no existing location is confirmed, record the path as TBD rather than inventing it.
>
> 2. Map canonical vocabulary into UI/state constants.
>    - Use `PipelineCategory` values for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*` as the operative taxonomy.
>    - Use `TaskScopeMode` values `DELIVERABLES` and `KNOWLEDGE_TYPES`.
>    - Use `KnowledgeTypeOption` labels for supported bucket discovery where exposed.
>    - Use the disabled-option concept for visible unsupported variants.
>
> 3. Implement or verify PIPELINE category controls.
>    - Confirm `DECOMP`, `PREP`, `TASK`, and `AUDIT` are visible category controls.
>    - Confirm each category has documented options and record the option-list source or fixture for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*`.
>    - Confirm unsupported options are visible, carry disabled or coming-soon semantics, and cannot start execution.
>
> 4. Implement or verify TASK split selector behavior.
>    - Confirm task agent selection and scope selection are separate.
>    - Confirm scope mode supports deliverables and knowledge types.
>    - Confirm knowledge-type mode requires a selected target deliverable.
>
> 5. Implement or verify dynamic scope discovery.
>    - Use the working-root scope surface to scan deliverables and knowledge types.
>    - Record whether evidence comes from live `/api/working-root/scope` integration or a mock contract fixture.
>    - Confirm the evidence demonstrates active-root scanning rather than hard-coded project assumptions.
>    - Detect document-kit buckets: `Datasheet`, `Specification`, `Guidance`, and `Procedure`.
>    - If metadata buckets are exposed, align them with the `KnowledgeTypeOption` vocabulary.
>
> 6. Implement or verify invalid-selection reset behavior.
>    - Clear selected deliverable when the active root changes and the deliverable is absent.
>    - Clear selected knowledge target when its deliverable is absent.
>    - Clear selected knowledge target when the marker is disabled or stale.
>    - Name fixtures or tests for root change, removed deliverable, disabled marker, and stale knowledge target.
>
> 7. Verify governance boundary behavior.
>    - Confirm selector state does not bypass Type 2 task-agent governance.
>    - Confirm any actual Type 2 execution path still depends on the relevant sealed-context and approval checks.
>    - Record evidence that write-scope limits, no-ghost-input limits, approval reference checks, and fail-closed delegation remain enforced outside the selector.
>
> 8. Write or update tests.
>    - Cover pipeline category rendering and category option lists.
>    - Cover disabled option visibility and non-interactivity.
>    - Cover TASK selector split and required target deliverable behavior.
>    - Cover knowledge-type discovery for document-kit files.
>    - Cover stale-selection reset cases.
>
> 9. Verify contextual presentation consumers.
>    - Prove re-hosted Pipeline/Workbench and contextual Run controls consume
>      the same DECOMP/PREP/TASK/AUDIT semantics and dynamic task-scope rules.
>    - Prove Work-panel items cite an admitted dispatch/task source, status
>      basis, and currency.
>    - Prove conversational prose is not synthesized into structured work and
>      runtime completion is not mapped to project lifecycle or approval.
>    - Preserve DEL-02-02 presentation ownership and DEL-08-05 child-record
>      ownership.
>

### CLM-024 — Verification

> ##### Verification
>
> | Check | Expected Result |
> |---|---|
> | Category selector test | `DECOMP`, `PREP`, `TASK`, and `AUDIT` are available as PIPELINE category controls. |
> | Category option-list test | `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*` option lists have named source or fixture evidence. |
> | Disabled option test | Unsupported variants are visible, carry disabled or coming-soon semantics, and cannot be selected for execution. |
> | TASK scope selector test | Task agent and scope controls are independently represented. |
> | Knowledge-type target test | Knowledge-type mode requires a selected deliverable. |
> | Scope API evidence check | `/api/working-root/scope` integration or mock evidence demonstrates active-root deliverable and knowledge-type scanning. |
> | Knowledge bucket discovery test | Document kit files are detected as first-class knowledge buckets; any metadata buckets use canonical `KnowledgeTypeOption` labels. |
> | Stale selection reset test | Root change, removed deliverable, disabled marker, and stale knowledge target fixtures clear invalid UI state. |
> | Governance boundary review | UI dispatch does not grant runtime authority beyond governed execution checks, including sealed context, approval metadata, no ghost inputs, explicit write scope, and fail-closed delegation. |
>

### CLM-025 — Records

> ##### Records
>
> Maintain or produce these records during implementation:
>
> - Pipeline selector tests.
> - Category-specific option-list source or fixture inventory.
> - Knowledge-type discovery tests or fixtures.
> - Disabled option handling tests.
> - Scope API integration or mock-contract evidence for active-root scanning.
> - Reset fixtures for root change, removed deliverable, disabled marker, and stale knowledge target.
> - Governance boundary review evidence for selector-only intent versus runtime authority.
> - Any implementation note identifying confirmed UI component and test file paths.
> - Any implementation worker note naming the final component path and test file path owner; owner remains TBD until assigned.
> - Any future authority-corpus update if `docs/PRD.md` changes.
>

### CLM-026 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | F-002 | Incorporated by requiring live or mocked `/api/working-root/scope` evidence that demonstrates active-root scanning. |
> | F-003 | Incorporated by naming reset fixture cases for root change, removed deliverable, disabled marker, and stale knowledge target. |
> | D-002 | Converted to an implementation-worker record slot for final UI component and test file paths, with owner still TBD. |

- **VER-001** — Test inventory review with named category, TASK scope, discovery, disabled-option, and reset fixtures.

## Governing Values and Decisions — Axiology

### CLM-027 — Guidance: DEL-08-03 Pipeline Category and Task Scope Dispatch

> #### Guidance: DEL-08-03 Pipeline Category and Task Scope Dispatch
>

### CLM-028 — Purpose

> ##### Purpose
>
> This deliverable keeps the operative PIPELINE dispatch surface aligned with Chirality's agent architecture. It connects the operator-facing category controls to the governed execution model without turning UI selection into runtime authority.
>
> The practical outcome is a user experience where operators can see the available operative lanes, choose a valid TASK scope, discover deliverable-local knowledge buckets, and understand unsupported variants because they remain visible but disabled.
>

### CLM-029 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Use canonical vocabulary | Use the terms `PipelineCategory`, `TaskScopeMode`, `KnowledgeTypeOption`, and `DisabledOption` consistently in implementation-facing docs, tests, and state models where applicable. | `docs/TYPES.md` Section 4.4 |
> | Keep operative dispatch explicit | PIPELINE category controls should make `DECOMP`, `PREP`, `TASK`, and `AUDIT` visible as separate operative choices. | `docs/PRD.md` FR-011 |
> | Separate task selection from scope selection | TASK flow should not collapse task-agent choice and scope choice into one ambiguous selector. | `docs/PRD.md` FR-012 |
> | Treat knowledge-type mode as deliverable-bound | Knowledge-type targets depend on a selected deliverable and should clear when that deliverable is unavailable or stale. | `docs/PRD.md` FR-012, FR-013 |
> | Show unsupported variants without enabling them | Disabled options preserve roadmap awareness while preventing accidental execution. | `docs/PRD.md` FR-011; success metric 7 |
> | Do not expand authority | Selector state may request or describe a route, but Type 2 execution remains governed by agent instructions, sealed context, approval metadata, and fail-closed gates. | `docs/CONTRACT.md` Section 1.8 |
>

### CLM-030 — Considerations

> ##### Considerations
>
> - Prefer source-derived option lists and vocabulary over ad hoc labels. If implementation code already has local naming, reconcile it with `docs/TYPES.md` rather than silently creating a parallel taxonomy.
> - Scope scan behavior should be resilient to working-root changes. A selected deliverable or knowledge bucket that is no longer present should be cleared instead of retained as stale UI state.
> - Knowledge-type discovery should account for the four-document kit first. Metadata buckets should be exposed only when the UI can use canonical `KnowledgeTypeOption` labels or an explicit mapping to them, because partial local labels would create a parallel taxonomy.
> - The deliverable's anticipated artifacts are tests and discovery behavior, not new authority for runtime subagent execution.
> - REF-006 is current under D-APP-38 and `_REFERENCES.md` records `docs/PRD.md` as `MATCH`. Preserve implementation proof separately from source-state proof.
>

### CLM-031 — Boundary Rationale

> ##### Boundary Rationale
>
> PIPELINE dispatch expresses operator intent and selects a proposed route through the operative surface. It is not an authorization boundary. Runtime authority remains with TASK and Type 2 governance checks because `docs/CONTRACT.md` requires explicit write scope, sealed context and gate metadata, no ghost inputs, and fail-closed subagent delegation. Selector state can therefore prepare or display a route, but execution must still pass the governed runtime checks before any child agent or task path is enabled.
>

### CLM-032 — Human Ruling Path

> ##### Human Ruling Path
>
> | Topic | Required Ruling | Current Treatment |
> |---|---|---|
> | REF-006 source state | Resolved by D-APP-38. | Use PRD-derived selector requirements under the current authority corpus; keep implementation proof separate. |
> | PRD-derived control wording | Resolved by D-APP-38 and ADQ-12 evidence update. | State that PRD content is current for source-state purposes while selector behavior remains proven by code/tests. |
>

### CLM-033 — Trade-offs

> ##### Trade-offs
>
> | Decision Area | Preferred Direction | Trade-off |
> |---|---|---|
> | Disabled options | Keep unsupported variants visible and disabled. | Operators see future or unavailable paths, but the UI must avoid implying they are executable. |
> | Dynamic scope reset | Clear invalid selections aggressively. | Users may need to reselect after root changes, but stale execution targets are avoided. |
> | Knowledge bucket coverage | Start from canonical document-kit and metadata bucket terms. | Implementation may need mapping if existing file names or UI labels differ. |
> | Governance boundary | Let UI dispatch describe intent only; execution approval remains separate. | More state checks may be needed before invoking TASK or subagent pathways. |
>

### CLM-034 — Examples

> ##### Examples
>
> | Scenario | Expected Handling |
> |---|---|
> | Operator selects PIPELINE `TASK`, then switches scope mode to `KNOWLEDGE_TYPES` without selecting a deliverable. | The UI should require a target deliverable before knowledge-type targets become executable. |
> | Active working root changes and the previously selected deliverable is no longer in the scope scan. | The selected deliverable and dependent knowledge target should reset. |
> | A future AUDIT variant is known but not implemented. | It may be visible as a disabled option with no runtime execution path. |
> | A deliverable folder has `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`. | These files should be discoverable as first-class knowledge buckets when knowledge-type scope is used. |
>

### CLM-035 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | CONFLICT-001 | Former PRD source-state warning resolved by D-APP-38. | `_REFERENCES.md` REF-006 | D-APP-38 current authority corpus | All PRD-derived requirements | Use PRD content under the current authority corpus; keep implementation proof separate from source-state proof. | D-APP-38 accepted current authority corpus |
>

### CLM-036 — Assumptions

> ##### Assumptions
>
> - ASSUMPTION: OBJ-001 and OBJ-007 are relevant because the decomposition explicitly lists them for DEL-08-03.
> - ASSUMPTION: The final implementation surface is frontend/UI state and tests, but specific component and test file paths are TBD until the implementation worker selects or confirms existing modules.
>

### CLM-037 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | A-001 | Resolved by D-APP-38; the former PRD source-state warning is retained as historical context only. |
> | C-001 | Incorporated as rationale for exposing metadata buckets only with canonical `KnowledgeTypeOption` labels or explicit mapping. |
> | D-001 | Resolved by D-APP-38; no further source-state ruling is required for this tranche. |
> | E-001 | Incorporated as boundary rationale distinguishing UI intent from TASK and Type 2 runtime authority. |
> | E-002 | Resolved by D-APP-38 and ADQ-12 wording updates; PRD-derived controls are current while implementation proof stays separate. |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-007 SOW-026 OBJ-001 OBJ-007 | CLM-011 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
