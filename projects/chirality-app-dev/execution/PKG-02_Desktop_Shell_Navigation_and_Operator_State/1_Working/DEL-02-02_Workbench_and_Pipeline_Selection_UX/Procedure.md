# Procedure: DEL-02-02 Workbench and Pipeline Selection UX

## Purpose

Define the operational steps to produce and verify the Workbench and Pipeline Selection UX slice without expanding scope into runtime internals, dependency extraction, or PKG-08 dispatch governance.

## Prerequisites

- Accepted working root with DEL-02-02 scaffolded under PKG-02.
- Accessible source corpus from `_REFERENCES.md`, especially `docs/PRD.md`, `docs/TYPES.md`, `docs/SPEC.md`, and the active SOFTWARE_DECOMP file.
- Current deliverable status and dependencies available through deliverable-local files or workspace APIs.
- Declared upstream dependencies: TBD; `_DEPENDENCIES.md` says no accepted dependency edges have been extracted yet.
- Declared downstream dependencies: TBD; `_DEPENDENCIES.md` says no accepted dependency edges have been extracted yet.

## Steps

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

## Verification

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

## Records

- Workbench context UI implementation or inspection notes: TBD.
- Workbench context UI test evidence for query defaults: TBD.
- Workbench lifecycle-control source-of-truth fixture or registry evidence: TBD.
- Workbench contract boundary evidence for status/dependency summaries: TBD.
- Pipeline selector behavior implementation or inspection notes: TBD.
- Pipeline category and TASK split-selector test evidence: TBD.
- Stale selection test evidence for root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets: TBD.
- Human rulings for conflict table entries in `Guidance.md`: TBD.
- Dependency extraction remains deferred; `Dependencies.csv` is intentionally not produced by this run.
