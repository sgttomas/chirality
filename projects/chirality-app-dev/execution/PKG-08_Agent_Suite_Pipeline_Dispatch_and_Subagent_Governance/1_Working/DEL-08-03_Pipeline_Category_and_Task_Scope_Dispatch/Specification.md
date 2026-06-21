# Specification: DEL-08-03 Pipeline Category and Task Scope Dispatch

## Scope

This deliverable specifies the PIPELINE category and TASK scope dispatch behavior for the Chirality App vNext operative surface.

In scope:

- PIPELINE category selection for `DECOMP`, `PREP`, `TASK`, and `AUDIT`.
- Category-specific option presentation, including disabled unsupported options.
- TASK split selectors for task agent and scope.
- Dynamic TASK scope from deliverables and knowledge-type buckets.
- Invalid-selection reset behavior when the active working root or scanned scope changes.
- Tests for pipeline selector behavior, knowledge-type discovery, and disabled option handling.

Out of scope:

- General SDK adapter mechanics.
- Type 2 subagent runtime governance bridge implementation, except where selector behavior must not expand authority.
- Dependency extraction for this deliverable run; `Dependencies.csv` remains deferred.
- Retired unified pipeline run-record or broader PKG-08 hardening scope unless a governed amendment reactivates it.

## Requirements

| ID | Requirement | Priority / Status | Source |
|---|---|---|---|
| DEL-08-03-REQ-001 | The PIPELINE UI shall expose operative category controls for `DECOMP`, `PREP`, `TASK`, and `AUDIT`. | P0 | `docs/PRD.md` FR-011 |
| DEL-08-03-REQ-002 | Category controls shall present documented category-specific options for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*`; the implementation record shall name the option-list source or fixture used for each category. | P0 | `docs/PRD.md` FR-011; `docs/TYPES.md` Section 4.4 |
| DEL-08-03-REQ-003 | Unsupported PIPELINE variants shall remain visible, shall carry disabled or coming-soon semantics, and shall be unable to initiate execution. | P0 | `docs/PRD.md` FR-011; `docs/TYPES.md` Section 4.4; `docs/PRD.md` success metric 7 |
| DEL-08-03-REQ-004 | PIPELINE `TASK` shall use split selectors for task agent and scope. | P0 | `docs/PRD.md` FR-012 |
| DEL-08-03-REQ-005 | TASK scope mode shall support `DELIVERABLES` and `KNOWLEDGE_TYPES`. | P0 | `docs/PRD.md` FR-012; `docs/TYPES.md` Section 4.4 |
| DEL-08-03-REQ-006 | Knowledge-type mode shall require a target deliverable. | P0 | `docs/PRD.md` FR-012 |
| DEL-08-03-REQ-007 | Dynamic scope scan shall reset invalid selection state when roots change, deliverables disappear, knowledge markers are disabled, or knowledge targets become stale. | P1 | `docs/PRD.md` FR-013 |
| DEL-08-03-REQ-008 | Knowledge-type discovery shall support document-kit files as first-class knowledge buckets: Datasheet, Specification, Guidance, and Procedure. | P1 | `docs/PRD.md` FR-049 |
| DEL-08-03-REQ-009 | Knowledge-type discovery shall align with the canonical `KnowledgeTypeOption` vocabulary when metadata buckets are exposed. | P1 | `docs/TYPES.md` Section 4.4 |
| DEL-08-03-REQ-010 | Scope scanning shall use the active working-root scope surface rather than hard-coded project assumptions, with evidence showing a call, mock contract, or fixture for `/api/working-root/scope`. | P0 | `docs/SPEC.md` Section 17.2; `docs/PRD.md` FR-013 |
| DEL-08-03-REQ-011 | Dispatch behavior shall not expand agent authority or bypass Type 2 governance constraints; pass evidence shall show selector state cannot bypass write-scope, sealed-context, no-ghost-input, approval-reference, or fail-closed delegation gates. | P0 | `docs/CONTRACT.md` K-WRITE-1, K-SEAL-1, K-GHOST-1, K-SUBAGENT-1 |
| DEL-08-03-REQ-012 | Selector tests shall cover pipeline selector behavior, knowledge-type discovery, disabled option handling, and invalid-selection reset fixtures for root change, removed deliverable, disabled marker, and stale knowledge target. | P1 | Decomposition anticipated artifacts; `docs/PRD.md` FR-013 |

## Standards

| Standard / Contract | Applicability | Evidence |
|---|---|---|
| Chirality `PipelineCategory` vocabulary | Defines operative category terms for dispatch. | `docs/TYPES.md` Section 4.4 |
| Chirality `TaskScopeMode` vocabulary | Defines valid TASK scope modes. | `docs/TYPES.md` Section 4.4 |
| Chirality `KnowledgeTypeOption` vocabulary | Defines knowledge bucket labels available for discovery. | `docs/TYPES.md` Section 4.4 |
| Chirality disabled-option vocabulary | Defines visible but non-selectable options. | `docs/TYPES.md` Section 4.4 |
| PRD Matrix, Workbench, and Pipeline requirements | Defines product behavior for PIPELINE and TASK selectors. | `docs/PRD.md` Section 8.2 |
| SPEC workspace API contract | Defines scope scan endpoint purpose. | `docs/SPEC.md` Section 17.2 |
| Agent/subagent governance invariants | Constrain dispatch behavior from expanding authority. | `docs/CONTRACT.md` Section 1.8 |

## Verification

| Requirement IDs | Verification Approach | Expected Evidence |
|---|---|---|
| DEL-08-03-REQ-001, DEL-08-03-REQ-002 | UI/unit tests for category selector rendering and option lists, with the option-list source or fixtures named for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*`. | Pipeline selector tests plus category option fixture record |
| DEL-08-03-REQ-003 | UI/unit tests verifying disabled unsupported variants remain visible, communicate disabled or coming-soon semantics, and cannot initiate execution. | Disabled option handling tests |
| DEL-08-03-REQ-004, DEL-08-03-REQ-005, DEL-08-03-REQ-006 | UI/state tests for split TASK selectors and required target deliverable behavior. | TASK selector state tests |
| DEL-08-03-REQ-007 | State transition tests using named fixtures for root change, removed deliverable, disabled marker, and stale knowledge target. | Stale selection reset tests plus fixture inventory |
| DEL-08-03-REQ-008, DEL-08-03-REQ-009 | Scope scan and UI tests for document-kit buckets (`Datasheet`, `Specification`, `Guidance`, `Procedure`) and any exposed metadata buckets using canonical `KnowledgeTypeOption` labels. | Knowledge-type discovery tests |
| DEL-08-03-REQ-010 | API integration or mocked API contract tests for `/api/working-root/scope`, including evidence that returned deliverables and knowledge buckets come from the active working root. | Scope scan integration tests |
| DEL-08-03-REQ-011 | Governance regression tests or review checks proving dispatch does not enable unauthorized Type 2 execution or bypass sealed context, approval metadata, no-ghost-input limits, write-scope limits, or fail-closed delegation. | Governance guard tests or review evidence |
| DEL-08-03-REQ-012 | Test inventory review with named category, TASK scope, discovery, disabled-option, and reset fixtures. | Named tests or fixtures covering anticipated artifacts |

## Documentation

Required or expected artifacts:

- Pipeline selector tests.
- Knowledge-type discovery tests.
- Disabled option handling tests.
- TASK scope selector fixtures for `DELIVERABLES` and `KNOWLEDGE_TYPES`.
- Category-specific option-list source or fixture record for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*`.
- Evidence that invalid selections reset after root and scan changes, including root-change, removed-deliverable, disabled-marker, and stale-target fixtures.
- Scope-scan evidence showing `/api/working-root/scope` integration or a mocked equivalent for active-root scanning.
- Governance guard evidence showing selector state does not bypass Type 2 sealed context, approval metadata, no-ghost-input limits, write-scope limits, or fail-closed delegation.
- ASSUMPTION: implementation notes may be needed once actual frontend component/module paths are selected.

## Source State

| State ID | Statement | Impact |
|---|---|---|
| STATE-001 | `docs/PRD.md` is current under the D-APP-38 authority corpus; `_REFERENCES.md` records REF-006 as `MATCH`. | Former PRD source-state warning is resolved for this tranche. Implementation proof remains separate from source-state proof. |

## Pass 3 Disposition Notes

| ItemID | Disposition |
|---|---|
| F-001 | Incorporated by adding a minimum governance proof threshold to DEL-08-03-REQ-011 and its verification evidence. |
| X-001 | Incorporated by requiring named option-list sources or fixtures for `DECOMP*`, `PREP*`, `TASK*`, and `AUDIT*`. |
| X-002 | Incorporated by naming required document-kit discovery evidence and canonical `KnowledgeTypeOption` treatment for any exposed metadata buckets. |
| X-003 | Incorporated by requiring visible, disabled or coming-soon semantics, and inability to initiate execution as one disabled-option evidence set. |
