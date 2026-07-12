# Datasheet: DEL-02-02 Workbench and Pipeline Selection UX

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-02-02 |
| DeliverableName | Workbench and Pipeline Selection UX |
| PackageID | PKG-02 |
| PackageName | Desktop Shell, Navigation, and Operator State |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | UX_UI_SLICE |
| ContextEnvelope | M |
| ResponsibleParty | TBD |
| LifecycleState at authoring | OPEN |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary UI surfaces | WORKBENCH contract/context review and PIPELINE selection controls as right-sidebar/deep-link tertiary forms in the loop-first shell. | `docs/PRD.md` Section 7.2; `docs/PRD.md` Section 8.2; `docs/TYPES.md` Section 4; D-APP-28/D-APP-31 |
| Workbench context display | Selected agent, row, and column are shown from query params with sensible defaults. | `docs/PRD.md` Section 8.2 FR-009 |
| Workbench deliverable contract behavior | Status/dependency summaries load for selected deliverables; transition controls are disabled for unsupported agents; human-gated targets require approval SHA. | `docs/PRD.md` Section 8.2 FR-010; ADQ-13 implementation evidence |
| Pipeline categories | `DECOMP`, `PREP`, `TASK`, and `AUDIT` category controls. | `docs/PRD.md` Section 8.2 FR-011 |
| Pipeline task scope selectors | `TASK` uses split selectors for task agent and scope. Scope mode is `DELIVERABLES` or `KNOWLEDGE_TYPES`; target deliverable is required for knowledge-type mode. | `docs/PRD.md` Section 8.2 FR-012; `docs/TYPES.md` Section 4.4 |
| Unsupported variants | Unsupported options remain visible and disabled as coming soon. | `docs/PRD.md` Section 7.2; `docs/PRD.md` Section 8.2 FR-011; `docs/TYPES.md` Section 4.4 |
| Stale selection behavior | Root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets clear invalid selection state. | `docs/PRD.md` Section 8.2 FR-013; `docs/PRD.md` Section 7.5 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Current release priority | Workbench agent context, pipeline category controls, and TASK split selectors are P0. Workbench contract APIs and stale selection reset are P1. | `docs/PRD.md` Section 8.2 |
| Scope boundary | Includes UI and operator workflow behavior; excludes runtime engine internals. | `_CONTEXT.md` Package Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 7 |
| Source warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` Authoritative Source Corpus — reconciled under D-APP-38 |
| Dispatch path warning | The dispatched path used stale package label `PKG-02_Desktop_UI_and_Local_Experience`; the unique live DEL-02-02 folder is under `PKG-02_Desktop_Shell_Navigation_and_Operator_State`. | `execution/_Coordination/WORKSPACE_MANIFEST.csv`; `_CONTEXT.md` Identity |

## Construction

| Component / artifact | Required content | Source |
|---|---|---|
| Workbench context UI | Display selected agent context from row/column/agent query parameters with defaults in the Workbench sidebar/deep-link form. | `docs/PRD.md` Section 8.2 FR-009; D-APP-28 |
| Workbench deliverable checks | Read-only status/dependency summaries, disabled lifecycle controls for unsupported agents, and approval-SHA enforcement for human-gated targets. | `docs/PRD.md` Section 8.2 FR-010; `docs/SPEC.md` Section 17.2; ADQ-13 implementation evidence |
| Pipeline category selector | Visible controls for operative categories. | `docs/PRD.md` Section 8.2 FR-011 |
| Pipeline TASK selector | Separate task-agent and scope selection; scope modes for deliverables and knowledge types. | `docs/PRD.md` Section 8.2 FR-012; `docs/TYPES.md` Section 4.4 |
| Stale-selection tests | Tests covering root change, removed deliverables, disabled knowledge markers, and stale knowledge targets. | `docs/PRD.md` Section 8.2 FR-013; `_CONTEXT.md` Anticipated Artifacts |

## References

- `_CONTEXT.md` for deliverable identity, scope, and anticipated artifacts.
- `_REFERENCES.md` for source corpus and hash status.
- `_DEPENDENCIES.md` for declared dependency state; dependency extraction is deferred.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 7-9 for package, deliverable, and scope-ledger entries.
- `docs/PRD.md` Sections 7.2, 7.5, 8.2, 14, and 16 for source requirements and traceability.
- `docs/TYPES.md` Section 4 for navigation vocabulary.
- `docs/SPEC.md` Section 17.2 for deliverable status/dependency workspace APIs.
- `docs/CONTRACT.md` Section 1.7 for lifecycle/dependency/provenance invariants.
