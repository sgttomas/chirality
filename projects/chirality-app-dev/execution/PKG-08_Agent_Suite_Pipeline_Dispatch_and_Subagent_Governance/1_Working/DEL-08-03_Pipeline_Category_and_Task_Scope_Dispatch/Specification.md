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
| DEL-08-03-REQ-002 | Category controls shall present documented category-specific options. | P0 | `docs/PRD.md` FR-011 |
| DEL-08-03-REQ-003 | Unsupported PIPELINE variants shall remain visible but disabled as coming-soon or unsupported options. | P0 | `docs/PRD.md` FR-011; `docs/TYPES.md` Section 4.4; `docs/PRD.md` success metric 7 |
| DEL-08-03-REQ-004 | PIPELINE `TASK` shall use split selectors for task agent and scope. | P0 | `docs/PRD.md` FR-012 |
| DEL-08-03-REQ-005 | TASK scope mode shall support `DELIVERABLES` and `KNOWLEDGE_TYPES`. | P0 | `docs/PRD.md` FR-012; `docs/TYPES.md` Section 4.4 |
| DEL-08-03-REQ-006 | Knowledge-type mode shall require a target deliverable. | P0 | `docs/PRD.md` FR-012 |
| DEL-08-03-REQ-007 | Dynamic scope scan shall reset invalid selection state when roots change, deliverables disappear, knowledge markers are disabled, or knowledge targets become stale. | P1 | `docs/PRD.md` FR-013 |
| DEL-08-03-REQ-008 | Knowledge-type discovery shall support document-kit files as first-class knowledge buckets: Datasheet, Specification, Guidance, and Procedure. | P1 | `docs/PRD.md` FR-049 |
| DEL-08-03-REQ-009 | Knowledge-type discovery shall align with the canonical `KnowledgeTypeOption` vocabulary when metadata buckets are exposed. | P1 | `docs/TYPES.md` Section 4.4 |
| DEL-08-03-REQ-010 | Scope scanning shall use the active working-root scope surface rather than hard-coded project assumptions. | P0 | `docs/SPEC.md` Section 17.2; `docs/PRD.md` FR-013 |
| DEL-08-03-REQ-011 | Dispatch behavior shall not expand agent authority or bypass Type 2 governance constraints. | P0 | `docs/CONTRACT.md` K-WRITE-1, K-SEAL-1, K-GHOST-1, K-SUBAGENT-1 |
| DEL-08-03-REQ-012 | Selector tests shall cover pipeline selector behavior, knowledge-type discovery, and disabled option handling. | P1 | Decomposition anticipated artifacts |

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
| DEL-08-03-REQ-001, DEL-08-03-REQ-002 | UI/unit tests for category selector rendering and option lists. | Pipeline selector tests |
| DEL-08-03-REQ-003 | UI/unit tests verifying disabled unsupported variants remain visible and non-interactive. | Disabled option handling tests |
| DEL-08-03-REQ-004, DEL-08-03-REQ-005, DEL-08-03-REQ-006 | UI/state tests for split TASK selectors and required target deliverable behavior. | TASK selector state tests |
| DEL-08-03-REQ-007 | State transition tests using root-change, removed-deliverable, disabled-marker, and stale-target fixtures. | Stale selection reset tests |
| DEL-08-03-REQ-008, DEL-08-03-REQ-009 | Scope scan and UI tests for document-kit and metadata bucket discovery. | Knowledge-type discovery tests |
| DEL-08-03-REQ-010 | API integration or mocked API contract tests for `/api/working-root/scope`. | Scope scan integration tests |
| DEL-08-03-REQ-011 | Governance regression tests or review checks proving dispatch does not enable unauthorized Type 2 execution. | Governance guard tests or review evidence |
| DEL-08-03-REQ-012 | Test inventory review. | Named tests or fixtures covering anticipated artifacts |

## Documentation

Required or expected artifacts:

- Pipeline selector tests.
- Knowledge-type discovery tests.
- Disabled option handling tests.
- TASK scope selector fixtures for `DELIVERABLES` and `KNOWLEDGE_TYPES`.
- Evidence that invalid selections reset after root and scan changes.
- ASSUMPTION: implementation notes may be needed once actual frontend component/module paths are selected.

## Source Warnings

| Warning ID | Statement | Impact |
|---|---|---|
| WARN-001 | `docs/PRD.md` has expected SHA `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34` but observed SHA `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. | Treated as a source warning per dispatch, not a blocker. Human may need to reconcile the reference hash before closure. |
