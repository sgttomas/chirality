# Source Pack: SRC-DEL-DEL-02-02-WORKBENCH-AND-PIPELINE-SELECTION-UX

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/Datasheet.md

### Datasheet: DEL-02-02 Workbench and Pipeline Selection UX

#### Identification

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

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary UI surfaces | WORKBENCH and PIPELINE selection controls, reached from matrix routing. | `docs/PRD.md` Section 7.2; `docs/PRD.md` Section 8.2; `docs/TYPES.md` Section 4 |
| Workbench context display | Selected agent, row, and column are shown from query params with sensible defaults. | `docs/PRD.md` Section 8.2 FR-009 |
| Workbench deliverable contract behavior | Status/dependency summaries load for selected deliverables; transition controls are disabled for unsupported agents. | `docs/PRD.md` Section 8.2 FR-010 |
| Pipeline categories | `DECOMP`, `PREP`, `TASK`, and `AUDIT` category controls. | `docs/PRD.md` Section 8.2 FR-011 |
| Pipeline task scope selectors | `TASK` uses split selectors for task agent and scope. Scope mode is `DELIVERABLES` or `KNOWLEDGE_TYPES`; target deliverable is required for knowledge-type mode. | `docs/PRD.md` Section 8.2 FR-012; `docs/TYPES.md` Section 4.4 |
| Unsupported variants | Unsupported options remain visible and disabled as coming soon. | `docs/PRD.md` Section 7.2; `docs/PRD.md` Section 8.2 FR-011; `docs/TYPES.md` Section 4.4 |
| Stale selection behavior | Root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets clear invalid selection state. | `docs/PRD.md` Section 8.2 FR-013; `docs/PRD.md` Section 7.5 |

#### Conditions

| Condition | Value | Source |
|---|---|---|
| Current release priority | Workbench agent context, pipeline category controls, and TASK split selectors are P0. Workbench contract APIs and stale selection reset are P1. | `docs/PRD.md` Section 8.2 |
| Scope boundary | Includes UI and operator workflow behavior; excludes runtime engine internals. | `_CONTEXT.md` Package Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 7 |
| Source warning | `docs/PRD.md` is accessible but has the expected PRD hash mismatch recorded in `_REFERENCES.md`; per dispatch, this is treated as a source warning, not a blocker. | `_REFERENCES.md` Authoritative Source Corpus |
| Dispatch path warning | The dispatched path used stale package label `PKG-02_Desktop_UI_and_Local_Experience`; the unique live DEL-02-02 folder is under `PKG-02_Desktop_Shell_Navigation_and_Operator_State`. | `execution/_Coordination/WORKSPACE_MANIFEST.csv`; `_CONTEXT.md` Identity |

#### Construction

| Component / artifact | Required content | Source |
|---|---|---|
| Workbench context UI | Display selected agent context from row/column/agent query parameters with defaults. | `docs/PRD.md` Section 8.2 FR-009 |
| Workbench deliverable checks | Read-only status/dependency summaries and disabled lifecycle controls for unsupported agents. | `docs/PRD.md` Section 8.2 FR-010; `docs/SPEC.md` Section 17.2 |
| Pipeline category selector | Visible controls for operative categories. | `docs/PRD.md` Section 8.2 FR-011 |
| Pipeline TASK selector | Separate task-agent and scope selection; scope modes for deliverables and knowledge types. | `docs/PRD.md` Section 8.2 FR-012; `docs/TYPES.md` Section 4.4 |
| Stale-selection tests | Tests covering root change, removed deliverables, disabled knowledge markers, and stale knowledge targets. | `docs/PRD.md` Section 8.2 FR-013; `_CONTEXT.md` Anticipated Artifacts |

#### References

- `_CONTEXT.md` for deliverable identity, scope, and anticipated artifacts.
- `_REFERENCES.md` for source corpus and hash status.
- `_DEPENDENCIES.md` for declared dependency state; dependency extraction is deferred.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 7-9 for package, deliverable, and scope-ledger entries.
- `docs/PRD.md` Sections 7.2, 7.5, 8.2, 14, and 16 for source requirements and traceability.
- `docs/TYPES.md` Section 4 for navigation vocabulary.
- `docs/SPEC.md` Section 17.2 for deliverable status/dependency workspace APIs.
- `docs/CONTRACT.md` Section 1.7 for lifecycle/dependency/provenance invariants.

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/Guidance.md

### Guidance: DEL-02-02 Workbench and Pipeline Selection UX

#### Purpose

This deliverable keeps the Workbench and Pipeline selection experience coherent for operators moving from the matrix into interactive personas or operative task categories. The UX should preserve active agent context, make available pipeline choices visible, prevent stale or invalid selections, and keep UI convenience state subordinate to governed project files.

Sources: `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` Sections 7.2, 7.5, 8.2, and 14.

#### Principles

- Preserve context at route boundaries: when the matrix opens WORKBENCH, the selected agent, row, and column should remain visible and recoverable from query parameters. Source: `docs/PRD.md` Section 8.2 FR-009.
- Keep operative selection explicit: PIPELINE should expose `DECOMP`, `PREP`, `TASK`, and `AUDIT`, and `TASK` should separate agent choice from scope choice. Source: `docs/PRD.md` Section 8.2 FR-011 and FR-012.
- Prefer disabled visibility over disappearance for unsupported options, so operators can see roadmap shape without being able to invoke unavailable behavior. Source: `docs/PRD.md` Section 7.2; `docs/TYPES.md` Section 4.4.
- Reset stale selections rather than carrying invalid state across root or scan changes. Source: `docs/PRD.md` Section 8.2 FR-013 and Section 7.5.
- Treat UI local state as non-authoritative convenience state. Project truth remains in working-root files and accepted git history. Source: `docs/DIRECTIVE.md` Sections 2.1, 2.2, and 2.6.

#### Considerations

- SOW-007 is listed in `_CONTEXT.md` as covered by DEL-02-02, while the decomposition scope ledger assigns SOW-007 to PKG-08 / DEL-08-03 as the primary package for agent dispatch. For this deliverable, treat Pipeline selectors as a UI presentation and selection concern; dispatch semantics remain with PKG-08 unless a human rules otherwise.
- Workbench deliverable contract summaries depend on status and dependency APIs. This deliverable should verify UI behavior but not extract dependencies or create `Dependencies.csv`.
- `KNOWLEDGE_TYPES` mode should not become selectable unless the source scan indicates a knowledge decomposition marker. Source: `docs/PRD.md` Section 7.5.
- The PRD is usable for this run but has a recorded hash mismatch in `_REFERENCES.md`; source-backed content from the PRD should remain reviewable against the observed file.
- ASSUMPTION: Existing implementation already has some PORTAL, WORKBENCH, PIPELINE, matrix navigation, toolkit, and file-tree surfaces because `docs/PLAN.md` Section 1 lists them as part of the current baseline. This run did not inspect frontend code and does not claim implementation conformance.

#### Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Visible disabled options vs. hiding unsupported scope | Prefer visible disabled options when a variant is unsupported or coming soon. This preserves operator awareness without enabling execution. | `docs/PRD.md` Sections 7.2 and 14; `docs/TYPES.md` Section 4.4 |
| Local UI persistence vs. authoritative project state | Persist convenience state only when it cannot override `_STATUS.md`, dependency records, deliverable files, or accepted git history. | `docs/DIRECTIVE.md` Section 2.6; `docs/CONTRACT.md` Section 1.7 |
| UX slice ownership vs. agent-dispatch ownership | Keep selector display and stale-selection behavior in this UX slice; keep dispatch governance and subagent behavior in PKG-08. | `_CONTEXT.md`; decomposition scope ledger SOW-007 |
| Defaults vs. explicit context | Provide sensible defaults for incomplete Workbench query params, but visibly show the resolved agent/row/column so the operator knows active context. | `docs/PRD.md` Section 8.2 FR-009 |

#### Examples

| Scenario | Expected behavior | Source |
|---|---|---|
| User clicks a NORMATIVE matrix cell | App opens WORKBENCH and shows the selected agent context. | `docs/PRD.md` Sections 7.2 and 8.2 |
| User clicks an OPERATIVE matrix cell | App opens PIPELINE with the relevant category context. | `docs/PRD.md` Section 7.2 |
| User opens PIPELINE TASK | UI shows split controls for task agent and scope; scope modes are deliverables or knowledge types. | `docs/PRD.md` Section 8.2 FR-012 |
| Working root changes | Invalid deliverable or knowledge-type selections reset. | `docs/PRD.md` Section 8.2 FR-013 |
| Unsupported pipeline option exists | Option remains visible but disabled as coming soon. | `docs/PRD.md` Section 7.2; `docs/TYPES.md` Section 4.4 |

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| DEL-02-02-CONFLICT-001 | Dispatch path used stale package label `PKG-02_Desktop_UI_and_Local_Experience`, but the live scaffolded deliverable is under `PKG-02_Desktop_Shell_Navigation_and_Operator_State`. | User dispatch brief | `_CONTEXT.md` Identity; `execution/_Coordination/WORKSPACE_MANIFEST.csv` row for DEL-02-02 | All run-record scope references | Use the unique live DEL-02-02 path and preserve the path mismatch as a source warning. | TBD |
| DEL-02-02-CONFLICT-002 | PRD expected hash differs from observed hash. Dispatch says to treat this as a source warning, not a blocker. | `_REFERENCES.md` REF-006 row | User dispatch brief | All PRD-backed requirements | Continue using accessible `docs/PRD.md`, cite sections, and surface hash mismatch for review. | TBD |
| DEL-02-02-CONFLICT-003 | `_CONTEXT.md` lists SOW-007 under DEL-02-02, while the decomposition scope ledger maps SOW-007 to PKG-08 / DEL-08-03 with PKG-08 as primary package. | `_CONTEXT.md` Traceability | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Scope Ledger SOW-007 | Specification scope, requirements, and ownership notes | Treat DEL-02-02 as UI selector owner and PKG-08 as dispatch semantics owner. | TBD |

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/Procedure.md

### Procedure: DEL-02-02 Workbench and Pipeline Selection UX

#### Purpose

Define the operational steps to produce and verify the Workbench and Pipeline Selection UX slice without expanding scope into runtime internals, dependency extraction, or PKG-08 dispatch governance.

#### Prerequisites

- Accepted working root with DEL-02-02 scaffolded under PKG-02.
- Accessible source corpus from `_REFERENCES.md`, especially `docs/PRD.md`, `docs/TYPES.md`, `docs/SPEC.md`, and the active SOFTWARE_DECOMP file.
- Current deliverable status and dependencies available through deliverable-local files or workspace APIs.
- Declared upstream dependencies: TBD; `_DEPENDENCIES.md` says no accepted dependency edges have been extracted yet.
- Declared downstream dependencies: TBD; `_DEPENDENCIES.md` says no accepted dependency edges have been extracted yet.

#### Steps

1. Confirm source and scope.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`, and `_DEPENDENCIES.md`.
   - Confirm `ResponsibleParty` remains `TBD`.
   - Confirm this slice covers Workbench context UI, Pipeline selector behavior, and stale selection tests.

2. Implement or inspect Workbench context behavior.
   - Verify that selected agent, row, and column are read from query parameters.
   - Verify sensible defaults for incomplete or missing query parameters.
   - Verify the resolved active context is visible to the operator.
   - Source: `docs/PRD.md` Section 8.2 FR-009.

3. Implement or inspect Workbench deliverable contract summaries.
   - Load selected-deliverable status/dependency summaries through workspace contract APIs where the UI supports deliverable context.
   - Keep lifecycle controls disabled for unsupported agents.
   - Identify the source of truth for unsupported lifecycle controls, or record it as TBD if the registry/API response/policy surface is not yet named.
   - Verify status/dependency summaries are not populated from local UI convenience state while dependency extraction remains deferred.
   - Do not treat UI state as authoritative lifecycle or dependency truth.
   - Sources: `docs/PRD.md` Section 8.2 FR-010; `docs/SPEC.md` Section 17.2; `docs/DIRECTIVE.md` Section 2.6; `docs/CONTRACT.md` Section 1.7.

4. Implement or inspect Pipeline category controls.
   - Expose `DECOMP`, `PREP`, `TASK`, and `AUDIT` category controls.
   - Keep unsupported options visible and disabled as coming soon.
   - Sources: `docs/PRD.md` Section 8.2 FR-011; `docs/TYPES.md` Section 4.4.

5. Implement or inspect Pipeline TASK selectors.
   - Separate task-agent selection from scope selection.
   - Support scope modes `DELIVERABLES` and `KNOWLEDGE_TYPES`.
   - Require target deliverable selection for knowledge-type mode.
   - Source: `docs/PRD.md` Section 8.2 FR-012.

6. Implement or inspect stale selection reset behavior.
   - Reset invalid selection state when the working root changes.
   - Reset removed deliverables.
   - Reset disabled knowledge markers.
   - Reset stale knowledge targets.
   - Sources: `docs/PRD.md` Section 8.2 FR-013; `docs/PRD.md` Section 7.5.

7. Preserve governance boundaries.
   - Do not create or update `Dependencies.csv` as part of this UX deliverable.
   - Do not infer dependency edges from UI selector behavior.
   - Record unknowns as `TBD`, `ASSUMPTION`, or conflicts for human ruling.

#### Verification

| Check | Expected result | Source |
|---|---|---|
| Workbench query context | Selected agent, row, and column are shown with sensible defaults. | `docs/PRD.md` Section 8.2 FR-009 |
| Matrix routing boundary | NORMATIVE/EVALUATIVE route to WORKBENCH; OPERATIVE routes to PIPELINE. | `docs/PRD.md` Section 7.2; `docs/PRD.md` Section 8.2 FR-008 |
| Workbench contract summaries | Status/dependency summaries load for selected deliverables; unsupported transition controls are disabled. | `docs/PRD.md` Section 8.2 FR-010 |
| Workbench contract boundary | Status/dependency summaries come from deliverable contract APIs or remain explicitly unavailable/TBD; UI convenience state is not used as dependency truth. | `docs/SPEC.md` Section 17.2; `docs/DIRECTIVE.md` Section 2.6; `docs/CONTRACT.md` Section 1.7 |
| Pipeline categories | `DECOMP`, `PREP`, `TASK`, and `AUDIT` are represented; unsupported variants are disabled. | `docs/PRD.md` Section 8.2 FR-011 |
| TASK split selectors | Task agent and scope selectors are distinct; scope mode behavior matches `DELIVERABLES` / `KNOWLEDGE_TYPES`. | `docs/PRD.md` Section 8.2 FR-012 |
| Stale selection reset | Root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets clear invalid selections. | `docs/PRD.md` Section 8.2 FR-013 |
| Project truth boundary | No local UI state overrides `_STATUS.md`, dependency records, deliverable files, or accepted git history. | `docs/DIRECTIVE.md` Sections 2.1, 2.2, and 2.6 |

#### Records

- Workbench context UI implementation or inspection notes: TBD.
- Workbench context UI test evidence for query defaults: TBD.
- Workbench lifecycle-control source-of-truth fixture or registry evidence: TBD.
- Workbench contract boundary evidence for status/dependency summaries: TBD.
- Pipeline selector behavior implementation or inspection notes: TBD.
- Pipeline category and TASK split-selector test evidence: TBD.
- Stale selection test evidence for root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets: TBD.
- Human rulings for conflict table entries in `Guidance.md`: TBD.
- Dependency extraction remains deferred; `Dependencies.csv` is intentionally not produced by this run.

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/Specification.md

### Specification: DEL-02-02 Workbench and Pipeline Selection UX

#### Scope

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

#### Requirements

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

#### Standards

| Standard / contract | Application | Source |
|---|---|---|
| Chirality UI navigation vocabulary | Rows, columns, matrix cells, pipeline categories, scope modes, and disabled options. | `docs/TYPES.md` Section 4 |
| Chirality PRD functional requirements | Workbench and Pipeline requirements FR-007 through FR-013. | `docs/PRD.md` Section 8.2 |
| Chirality workspace API contract | Read deliverable status/dependency summaries through workspace APIs. | `docs/SPEC.md` Section 17.2 |
| Chirality lifecycle and dependency invariants | `_STATUS.md` and dependency records remain authoritative project files, not UI convenience state. | `docs/CONTRACT.md` Section 1.7 |

#### Verification

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

#### Documentation

Required or anticipated artifacts:

- Workbench context UI implementation and tests.
- Pipeline selector behavior implementation and tests.
- Stale selection tests.
- Workbench contract boundary evidence showing that status/dependency summaries are not derived from local UI convenience state.
- Notes for disabled coming-soon variants if implementation uses a visible option registry.
- Any human ruling needed for cross-package ownership of SOW-007 and matrix-routing overlap with PKG-08.
