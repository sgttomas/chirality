# Datasheet: DEL-08-03 Pipeline Category and Task Scope Dispatch

## Identification

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DeliverableID | DEL-08-03 |
| DeliverableName | Pipeline Category and Task Scope Dispatch |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | M |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Scope | Dispatch DECOMP/PREP/TASK/AUDIT lanes and dynamic task scope from deliverables and knowledge-type buckets. | `_CONTEXT.md`; decomposition entry |
| Package scope | Agent instruction conformance, matrix/pipeline dispatch, Type 2 subagent governance and child records. | `_CONTEXT.md`; decomposition PKG-08 row |
| Inclusion criteria | Agent OS behavior and delegation. | `_CONTEXT.md`; decomposition PKG-08 row |
| Exclusions | General SDK adapter mechanics. | `_CONTEXT.md`; decomposition PKG-08 row |
| Covered scope items | SOW-007, SOW-026 | `_CONTEXT.md`; decomposition entry |
| Supported objectives | OBJ-001, OBJ-007 | `_CONTEXT.md`; decomposition entry |
| Anticipated artifacts | Pipeline selector tests; knowledge-type discovery; disabled option handling | `_CONTEXT.md`; decomposition entry |
| Pipeline categories | `DECOMP*`, `PREP*`, `TASK*`, `AUDIT*` | `docs/TYPES.md` Section 4.4 |
| TASK scope modes | `DELIVERABLES`, `KNOWLEDGE_TYPES` | `docs/TYPES.md` Section 4.4 |
| Knowledge type options | `Datasheet`, `Specification`, `Guidance`, `Procedure`, `Dependencies`, `References`, `Context`, `Status`, `Semantic`, `Memory` | `docs/TYPES.md` Section 4.4 |
| Disabled option meaning | Visible but non-selectable coming-soon or unsupported variant. | `docs/TYPES.md` Section 4.4 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| PIPELINE category controls | The PIPELINE surface exposes `DECOMP`, `PREP`, `TASK`, and `AUDIT` category controls. | `docs/PRD.md` FR-011 |
| Unsupported options | Unsupported options remain visible and disabled as coming soon. | `docs/PRD.md` FR-011; success metric 7 |
| TASK selector split | PIPELINE `TASK` uses split selectors for task agent and scope. | `docs/PRD.md` FR-012 |
| TASK scope requirement | Scope mode is `DELIVERABLES` or `KNOWLEDGE_TYPES`; target deliverable is required for knowledge-type mode. | `docs/PRD.md` FR-012 |
| Dynamic reset | Root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets clear invalid selection state. | `docs/PRD.md` FR-013 |
| Knowledge bucket detection | Datasheet, Specification, Guidance, and Procedure are supported as first-class knowledge buckets. | `docs/PRD.md` FR-049 |
| Working-root scope API | `/api/working-root/scope` scans deliverables and knowledge types. | `docs/SPEC.md` Section 17.2 |

## Construction

| Component / Surface | Expected Role | Status |
|---|---|---|
| Pipeline category selector | Selects operative lane for `DECOMP`, `PREP`, `TASK`, or `AUDIT`. | TBD implementation location |
| Category option list | Shows documented options for selected lane; unsupported variants are disabled. | TBD implementation location |
| TASK agent selector | Selects the bounded task agent or skill route. | TBD implementation location |
| TASK scope mode selector | Switches between deliverable scope and knowledge-type scope. | TBD implementation location |
| Dynamic deliverable scan | Provides valid deliverable targets from the active working root. | Source identifies API contract; implementation location TBD |
| Knowledge-type discovery | Detects document-kit and metadata buckets from deliverable content. | Source identifies file types; implementation location TBD |
| Invalid-selection reset | Clears stale or disabled selections after root or scope changes. | Source requires behavior; implementation location TBD |
| Tests | Cover pipeline selector behavior, knowledge-type discovery, and disabled option handling. | Anticipated artifacts |

## Implementation Slots

| Slot | Required Record | Current Disposition |
|---|---|---|
| Category selector component path | Confirmed frontend component or module path for PIPELINE `DECOMP`, `PREP`, `TASK`, and `AUDIT` controls. | TBD - implementation worker must record before closure. |
| Category option source | Confirmed data source or fixture for category-specific option lists. | TBD - must distinguish documented executable options from visible disabled options. |
| TASK selector component path | Confirmed component or state module for task-agent selector and scope selector. | TBD - implementation worker must record before closure. |
| Scope scan integration path | Confirmed API client, hook, or mock boundary for `/api/working-root/scope`. | TBD - must prove active-root scanning, not hard-coded project assumptions. |
| Knowledge discovery fixture path | Confirmed fixture or test-data path covering document-kit buckets and any exposed metadata buckets. | TBD - must use `KnowledgeTypeOption` labels when metadata buckets are exposed. |
| Reset test fixture path | Confirmed fixture path for root-change, removed-deliverable, disabled-marker, and stale-target reset cases. | TBD - implementation worker must record before closure. |

## Dependency Edge Snapshot

| Edge Type | Current Evidence | Disposition |
|---|---|---|
| Accepted upstream anchors | `_DEPENDENCIES.md` lists active anchors for DEL-08-03, SOW-007, SOW-026, OBJ-001, and OBJ-007. | Use as context; satisfaction remains TBD until dependency closure accepts the register. |
| Accepted upstream interfaces and constraints | `_DEPENDENCIES.md` lists active execution rows for `docs/TYPES.md` Section 4.4, `docs/SPEC.md` Section 17.2, `docs/CONTRACT.md` Section 1.8, and `docs/PRD.md` Section 8.2. | Use as current extracted evidence with PRD hash warning preserved. |
| Downstream handoff | `_DEPENDENCIES.md` lists a downstream handoff to pipeline selector, knowledge-type discovery, and disabled option tests, with consumer target unresolved. | Consumer deliverable remains TBD. |

## References

| RefID | Path | Use |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Agent and working-root governance context |
| REF-002 | `docs/CONTRACT.md` | Agent/subagent governance invariants |
| REF-003 | `docs/SPEC.md` | Scope API and file contract surfaces |
| REF-004 | `docs/TYPES.md` | Pipeline category, task scope, knowledge-type, and disabled-option vocabulary |
| REF-005 | `docs/PLAN.md` | Runtime roadmap and retired-scope boundaries |
| REF-006 | `docs/PRD.md` | Product requirements for matrix, pipeline, scope, and knowledge buckets; hash mismatch recorded as warning |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | SOFTWARE_DECOMP method and deliverable sizing context |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Accepted deliverable entry and objective/scope mapping |

## Pass 3 Disposition Notes

| ItemID | Disposition |
|---|---|
| B-001 | Converted to explicit implementation slots for selector, option-list, scope-scan, knowledge-discovery, reset-fixture, and test-path records. |
| B-002 | Incorporated as a dependency edge snapshot that preserves accepted extracted rows as context while leaving closure status and downstream consumer target TBD. |
