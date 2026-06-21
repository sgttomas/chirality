# Procedure: DEL-02-01 Desktop Shell and Matrix Navigation

## Purpose

Produce and verify the loop-first desktop shell and matrix navigation slice for DEL-02-01, preserving PORTAL, WORKBENCH, and PIPELINE access while the live loop remains the primary pane.

## Prerequisites

- Accessible source references listed in `_REFERENCES.md`.
- Current deliverable context in `_CONTEXT.md`.
- Existing implementation workspace for navigation components and tests.
- Implementation evidence slots are required for later closure: navigation component path, matrix UI test path, and route query handling test path. ADQ-13 records selected paths in the implementation evidence table below.
- Human acceptance that `ResponsibleParty` remains `TBD` until assigned.
- Dependency extraction remains deferred; do not create `Dependencies.csv` as part of this procedure.

Declared upstream dependencies:

- TBD - no accepted dependency edges have been extracted yet.

Declared downstream dependencies:

- TBD - no accepted dependency edges have been extracted yet.

## Steps

1. Confirm the deliverable identity from `_CONTEXT.md`: `DEL-02-01 Desktop Shell and Matrix Navigation`, `ResponsibleParty: TBD`, `Type: UX_UI_SLICE`, `ContextEnvelope: M`.
2. Confirm authoritative source availability from `_REFERENCES.md`; treat the PRD hash mismatch as a source warning unless a human ruling changes that instruction.
3. Preserve the shell's three surfaces: PORTAL at `/`, PIPELINE through the right-sidebar tertiary tab and `/pipeline` deep link, and WORKBENCH through the right-sidebar tertiary tab and `/workbench` deep link.
4. Ensure primary header navigation exposes PORTAL and visually indicates the active rendered section; route wrappers for `/workbench` and `/pipeline` must default to their matching sidebar tabs.
5. Render the PORTAL matrix with rows `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE`.
6. Render the PORTAL matrix with columns `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING`.
7. Route `NORMATIVE` cells to the mounted live loop by updating persona/query context without replacing the primary pane.
8. Route `EVALUATIVE` cells to the mounted live loop by updating persona/query context without replacing the primary pane.
9. Route `OPERATIVE` cells to PIPELINE intent in the right sidebar or preserved `/pipeline` deep link.
10. Preserve unsupported or disabled variants as visible coming-soon options where this deliverable exposes them.
11. Add or update matrix UI tests for row/column rendering and row-semantics routing.
12. Add or update route query handling tests for selected implementation keys. Current evidence covers `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` keys while preserving older source warnings.
13. Keep runtime engine internals out of this slice; hand off engine or selector-specific behavior to adjacent deliverables.
14. Record selected implementation paths for navigation components, matrix UI tests, and route query handling tests in this kit and in the ADQ-13 evidence note.

## Verification

| Check | Expected Result |
|---|---|
| Surface reachability | `/`, `/pipeline`, and `/workbench` remain reachable; `/workbench` and `/pipeline` open matching right-sidebar tertiary forms. |
| Active surface state | Primary header state covers rendered header links; Workbench/Pipeline active context is represented by sidebar tab state. |
| Matrix shape | PORTAL shows 3 rows and 4 columns. |
| Row labels | `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE` are present. |
| Column labels | `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING` are present. |
| Loop-persona routing | NORMATIVE and EVALUATIVE cells focus the mounted loop with selected persona context. |
| PIPELINE routing | OPERATIVE cells route to PIPELINE intent. |
| Unsupported variants | Unsupported variants visible in this slice are disabled or coming soon, not silently removed. |
| Scope discipline | No runtime engine internals are changed under this deliverable's authority. |

## Implementation Evidence Slots

| Evidence Slot | Current Value | Source |
|---|---|---|
| Navigation component path | `frontend/src/components/shell/shell-frame.tsx`; `frontend/src/components/shell/sidebar-right-loop-layout.tsx`; `frontend/src/components/shell/loop-tertiary-shell.tsx`; `frontend/src/app/workbench/workbench-client.tsx`; `frontend/src/app/pipeline/pipeline-client.tsx` | ADQ-13 inspection and render tests |
| Matrix UI test path | `frontend/src/__tests__/components/agent-matrix-panel.test.ts`; `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` | ADQ-13 AMD-01 render evidence |
| Route query handling test path | `frontend/src/__tests__/components/loop-tertiary-routes.test.ts`; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts`; `frontend/src/__tests__/lib/loop-first.test.ts` | ADQ-13 AMD-01 render evidence |

P3 disposition: D-001 is now implementation-evidence-backed for the selected paths above. Package path, PRD hash, and source-pointer conflicts remain warning-limited and are not resolved by this procedure update.

## Records

- Navigation component change notes or diff references.
- Matrix UI test results.
- Route query handling test results, with selected query key names documented.
- Any human rulings resolving the package path mismatch, PRD hash mismatch, or PRD/SPEC/TYPES source-pointer issue.
- This four-document kit and the TASK run record.
