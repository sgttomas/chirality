# Specification: DEL-02-02 Workbench and Pipeline Selection UX

## Scope

This deliverable specifies the user-facing UX slice for Workbench active-agent context and Pipeline selection controls in PKG-02. It covers:

- WORKBENCH presentation of selected agent, row, and column context.
- WORKBENCH read-only deliverable contract summaries and disabled lifecycle controls where the selected agent cannot perform transitions.
- PIPELINE category controls for operative categories.
- PIPELINE `TASK` split selectors for task agent and scope.
- Stale selection reset behavior for root, deliverable, and knowledge-type changes.

Excluded:

- Runtime engine internals and SDK/provider behavior.
- Authoritative dependency extraction and `Dependencies.csv` creation.
- Agent-suite dispatch governance beyond the UI controls needed to select a category or task scope.

Sources: `_CONTEXT.md` Package Scope and Deliverable Scope; `docs/PRD.md` Section 8.2; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 7-9.

## Requirements

| ReqID | Requirement | Priority / Status | Source |
|---|---|---|---|
| DEL-02-02-REQ-001 | WORKBENCH shall show the selected agent, matrix row, and matrix column from query parameters, with sensible defaults when parameters are absent or incomplete. | P0 | `docs/PRD.md` Section 8.2 FR-009 |
| DEL-02-02-REQ-002 | Matrix routing inputs to this UX shall preserve the rule that NORMATIVE and EVALUATIVE cells open WORKBENCH, while OPERATIVE cells open PIPELINE. | P0 | `docs/PRD.md` Sections 7.2 and 8.2 FR-008; `docs/TYPES.md` Section 4 |
| DEL-02-02-REQ-003 | WORKBENCH shall consume deliverable contract APIs for read-only status/dependency checks when a deliverable is selected. | P1 | `docs/PRD.md` Section 8.2 FR-010; `docs/SPEC.md` Section 17.2 |
| DEL-02-02-REQ-004 | WORKBENCH lifecycle transition controls shall be disabled for unsupported agents. The source of truth for unsupported controls is TBD until the UI control registry, workspace API response, or authorized actor/transition policy surface is named. | P1 | `docs/PRD.md` Section 8.2 FR-010; `docs/SPEC.md` Section 17.2; `docs/CONTRACT.md` Section 1.7 |
| DEL-02-02-REQ-005 | PIPELINE shall expose category controls for `DECOMP`, `PREP`, `TASK`, and `AUDIT`. Unsupported options shall remain visible and disabled as coming soon. | P0 | `docs/PRD.md` Section 8.2 FR-011; `docs/PRD.md` Section 7.2; `docs/TYPES.md` Section 4.4 |
| DEL-02-02-REQ-006 | PIPELINE `TASK` shall use split selectors for task agent and scope. | P0 | `docs/PRD.md` Section 8.2 FR-012 |
| DEL-02-02-REQ-007 | `TASK` scope mode shall be `DELIVERABLES` or `KNOWLEDGE_TYPES`; a target deliverable is required for knowledge-type mode. | P0 | `docs/PRD.md` Section 8.2 FR-012; `docs/TYPES.md` Section 4.4 |
| DEL-02-02-REQ-008 | Dynamic scope scans shall reset invalid selections caused by root changes, removed deliverables, disabled knowledge markers, or stale knowledge targets. | P1 | `docs/PRD.md` Section 8.2 FR-013; `docs/PRD.md` Section 7.5 |
| DEL-02-02-REQ-009 | The UX shall preserve disabled or unsupported variants as visible non-selectable options rather than silently hiding roadmap scope. | P0/P1 context | `docs/PRD.md` Section 7.2; `docs/PRD.md` Section 14; `docs/TYPES.md` Section 4.4 |
| DEL-02-02-REQ-010 | UI state used by this slice shall remain non-authoritative and must not replace project truth in deliverable files, status files, dependency records, or accepted git history. | Governance constraint | `docs/DIRECTIVE.md` Sections 2.1, 2.2, and 2.6; `docs/CONTRACT.md` Section 1.7 |
| DEL-02-02-REQ-011 | Workbench status/dependency summaries shall not be populated from UI convenience state while dependency extraction remains deferred; empty or missing dependency records must remain visibly `TBD`, unavailable, or sourced from the deliverable contract API. | Governance constraint | `docs/PRD.md` Section 8.2 FR-010; `docs/SPEC.md` Section 17.2; `docs/DIRECTIVE.md` Section 2.6; `docs/CONTRACT.md` Section 1.7 |

## Standards

| Standard / contract | Application | Source |
|---|---|---|
| Chirality UI navigation vocabulary | Rows, columns, matrix cells, pipeline categories, scope modes, and disabled options. | `docs/TYPES.md` Section 4 |
| Chirality PRD functional requirements | Workbench and Pipeline requirements FR-007 through FR-013. | `docs/PRD.md` Section 8.2 |
| Chirality workspace API contract | Read deliverable status/dependency summaries through workspace APIs. | `docs/SPEC.md` Section 17.2 |
| Chirality lifecycle and dependency invariants | `_STATUS.md` and dependency records remain authoritative project files, not UI convenience state. | `docs/CONTRACT.md` Section 1.7 |

## Verification

| Requirement | Verification approach | Evidence target |
|---|---|---|
| DEL-02-02-REQ-001 | Route/query tests for missing, partial, and complete Workbench query params. | Workbench context UI tests |
| DEL-02-02-REQ-002 | Matrix navigation tests asserting destination by row class. | Matrix routing tests owned with DEL-02-01/DEL-08-02 as applicable |
| DEL-02-02-REQ-003 | UI/API integration tests or mocked API tests for status/dependency summary loading. | Workbench deliverable contract tests |
| DEL-02-02-REQ-004 | UI tests confirming unsupported lifecycle controls are disabled and do not submit transitions; source-of-truth fixture or control registry remains TBD. | Workbench lifecycle-control tests, exact registry/fixture TBD |
| DEL-02-02-REQ-005 | Pipeline selector tests for visible categories and disabled coming-soon variants. | Pipeline category selector tests |
| DEL-02-02-REQ-006 | Pipeline TASK selector tests confirming task-agent and scope controls are independently represented. | Pipeline TASK selector tests |
| DEL-02-02-REQ-007 | Scope-mode validation tests for deliverables, knowledge types, and required target deliverable. | Task-scope selector tests |
| DEL-02-02-REQ-008 | Stale selection tests for root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets. | Stale selection tests |
| DEL-02-02-REQ-010 | Review that no UI state is treated as authoritative project truth. | Governance review checklist or tests, exact artifact TBD |
| DEL-02-02-REQ-011 | Mocked API or integration tests proving status/dependency summaries come from deliverable contract APIs or remain explicitly unavailable/TBD when dependency extraction is deferred. | Workbench contract boundary fixture or tests, exact artifact TBD |

## Documentation

Required or anticipated artifacts:

- Workbench context UI implementation and tests.
- Pipeline selector behavior implementation and tests.
- Stale selection tests.
- Workbench contract boundary evidence showing that status/dependency summaries are not derived from local UI convenience state.
- Notes for disabled coming-soon variants if implementation uses a visible option registry.
- Any human ruling needed for cross-package ownership of SOW-007 and matrix-routing overlap with PKG-08.
