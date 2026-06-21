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
   - Verify Workbench can operate as a loop-first right-sidebar/deep-link tertiary form rather than a replacement primary pane.
   - Source: `docs/PRD.md` Section 8.2 FR-009.

3. Implement or inspect Workbench deliverable contract summaries.
   - Load selected-deliverable status/dependency summaries through workspace contract APIs where the UI supports deliverable context.
   - Keep lifecycle controls disabled for unsupported agents.
   - Use `frontend/src/lib/workspace/deliverable-api.ts` `canAgentTransitionLifecycle` as the current implementation source of truth for lifecycle-control actor support.
   - Verify human-gated transitions require approval SHA before submission.
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
| Matrix routing boundary | NORMATIVE/EVALUATIVE select live-loop persona context; OPERATIVE routes to PIPELINE; WORKBENCH remains a tertiary review form. | `docs/PRD.md` Section 7.2; `docs/PRD.md` Section 8.2 FR-008; D-APP-28/D-APP-30/D-APP-31 |
| Workbench contract summaries | Status/dependency summaries load for selected deliverables; unsupported transition controls are disabled; approval SHA is required for human-gated target states. | `docs/PRD.md` Section 8.2 FR-010 |
| Workbench contract boundary | Status/dependency summaries come from deliverable contract APIs or remain explicitly unavailable/TBD; UI convenience state is not used as dependency truth. | `docs/SPEC.md` Section 17.2; `docs/DIRECTIVE.md` Section 2.6; `docs/CONTRACT.md` Section 1.7 |
| Pipeline categories | `DECOMP`, `PREP`, `TASK`, and `AUDIT` are represented; unsupported variants are disabled. | `docs/PRD.md` Section 8.2 FR-011 |
| TASK split selectors | Task agent and scope selectors are distinct; scope mode behavior matches `DELIVERABLES` / `KNOWLEDGE_TYPES`. | `docs/PRD.md` Section 8.2 FR-012 |
| Stale selection reset | Root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets clear invalid selections. | `docs/PRD.md` Section 8.2 FR-013 |
| Project truth boundary | No local UI state overrides `_STATUS.md`, dependency records, deliverable files, or accepted git history. | `docs/DIRECTIVE.md` Sections 2.1, 2.2, and 2.6 |

## Records

- Workbench context UI implementation or inspection notes: `frontend/src/components/workbench/workbench-surface.tsx`; ADQ-13 evidence note.
- Workbench context UI test evidence for query defaults: `frontend/src/__tests__/components/workbench-surface.test.ts`.
- Workbench lifecycle-control source-of-truth fixture or registry evidence: `frontend/src/lib/workspace/deliverable-api.ts`; `frontend/src/__tests__/components/workbench-surface.test.ts`; `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts`.
- Workbench contract boundary evidence for status/dependency summaries: `frontend/src/__tests__/lib/workspace-deliverable-api.test.ts`; ADQ-13 evidence note.
- Pipeline selector behavior implementation or inspection notes: `frontend/src/components/pipeline/pipeline-surface.tsx`; ADQ-13 evidence note.
- Pipeline category and TASK split-selector test evidence: `frontend/src/__tests__/components/pipeline-surface.test.ts`; `frontend/src/__tests__/lib/task-scope-selection.test.ts`.
- Stale selection test evidence for root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets: `frontend/src/__tests__/lib/task-scope-selection.test.ts`.
- Human rulings for conflict table entries in `Guidance.md`: TBD.
- Dependency extraction remains deferred; `Dependencies.csv` is intentionally not produced by this run.
