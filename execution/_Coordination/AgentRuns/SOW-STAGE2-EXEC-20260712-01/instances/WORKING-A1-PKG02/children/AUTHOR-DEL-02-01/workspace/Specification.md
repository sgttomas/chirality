# Specification: DEL-02-01 Desktop Shell and Matrix Navigation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Scope

This deliverable covers the user-facing desktop shell navigation and canonical matrix routing for `DEL-02-01 Desktop Shell and Matrix Navigation`.

In scope:

- Loop-first access to PORTAL, WORKBENCH, and PIPELINE shell surfaces.
- Primary header navigation to PORTAL (`/`), plus preserved deep-link route entries for `/workbench` and `/pipeline`.
- Right-sidebar tertiary tabs for PORTAL, WORKBENCH, and PIPELINE while the live loop remains mounted as the primary pane.
- PORTAL rendering of the canonical 3x4 agent matrix.
- Matrix row-semantics routing into live-loop persona context or PIPELINE.
- Navigation components, matrix UI tests, and route query handling to the extent supported by source evidence.

Out of scope:

- Runtime engine internals.
- Workbench agent-context detail owned by adjacent deliverables except where routing handoff requires it.
- Pipeline selector behavior beyond receiving OPERATIVE matrix routes.
- Dependency extraction and `Dependencies.csv` creation for this run.

## Requirements

| ID | Requirement | Priority | Source | Verification |
|---|---|---:|---|---|
| DEL-02-01-REQ-001 | The app shall provide a loop-first desktop shell where PORTAL, PIPELINE, and WORKBENCH are reachable while the live loop stays primary. | P0 | REF-006 Section 8.1 FR-001; SOW-001; D-APP-28/D-APP-31/D-APP-32 | Component render tests confirm all three tertiary surfaces are present in the right sidebar. |
| DEL-02-01-REQ-002 | Primary header navigation shall expose PORTAL at `/`; `/workbench` and `/pipeline` shall remain deep-link route entries that open their matching right-sidebar tertiary tab. | P0 | REF-006 Section 8.1 FR-001; D-APP-28/D-APP-31/D-APP-32 | Route-wrapper render tests confirm `/workbench` defaults to the Workbench tab and `/pipeline` defaults to the Pipeline tab. |
| DEL-02-01-REQ-003 | Header navigation shall visually indicate the active primary section for rendered header links. | P0 | REF-006 Section 8.1 FR-001; D-APP-28 | UI assertion confirms active state for the rendered primary header item; Workbench/Pipeline active context is represented by sidebar tab state. |
| DEL-02-01-REQ-004 | PORTAL shall render the canonical 3x4 agent matrix. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.3 | Matrix UI test confirms 3 rows and 4 columns. |
| DEL-02-01-REQ-005 | Matrix rows shall be `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE`. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.1 | Matrix UI test checks row labels and row order if order is encoded in implementation. |
| DEL-02-01-REQ-006 | Matrix columns shall be `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING`. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.2 | Matrix UI test checks column labels and column order if order is encoded in implementation. |
| DEL-02-01-REQ-007 | NORMATIVE matrix cells shall focus the mounted live loop with the selected Type-0/Type-1 persona context. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-30 | Matrix routing/render tests confirm loop-persona launch kind and mid-turn disabled state. |
| DEL-02-01-REQ-008 | EVALUATIVE matrix cells shall focus the mounted live loop with the selected Type-0/Type-1 persona context. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-30 | Matrix routing/render tests confirm loop-persona launch kind and mid-turn disabled state. |
| DEL-02-01-REQ-009 | OPERATIVE matrix cells shall open PIPELINE intent in the right sidebar or preserved `/pipeline` deep-link entry. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-31 | Matrix routing/render tests confirm Pipeline launch kind and sidebar destination. |
| DEL-02-01-REQ-010 | Disabled or unsupported variants shall remain visible as coming soon rather than disappearing when encountered in matrix-adjacent navigation flows. | P0 | REF-006 Section 7.2 acceptance | UI test confirms unsupported variants are visible and non-selectable where this deliverable exposes them. |
| DEL-02-01-REQ-011 | Stable identifiers shall remain distinct from path or label changes. Current implementation evidence uses `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` keys. | P1 | REF-002 `docs/CONTRACT.md` K-ID-1 and K-PATH-1; REF-006 Section 8.2 FR-009; ADQ-13 implementation evidence | Matrix identity and deliverable-key render tests confirm selected implementation keys while preserving source warnings for future authority reconciliation. |

## Standards

| Standard or Source | Applicability | Status |
|---|---|---|
| `docs/PRD.md` | Product requirements for shell navigation and matrix routing | Accessible; hash is MATCH under D-APP-38 — reconciled under D-APP-38 |
| `docs/TYPES.md` Section 4 | Canonical UI navigation vocabulary and matrix semantics | Accessible |
| `docs/CONTRACT.md` K-ID-1, K-PATH-1, K-INVENT-1, K-CONFLICT-1 | Stable identity and epistemic controls relevant to routing and document production | Accessible |
| `docs/DIRECTIVE.md` Section 4.1 | In-scope statement for local desktop operation and matrix navigation | Accessible |
| SOFTWARE_DECOMP v3.2 | Deliverable scope, SOW mapping, objective context, and execution note to preserve ResponsibleParty | Accessible |

## Verification

| Requirement IDs | Verification Approach | Evidence Record |
|---|---|---|
| REQ-001 through REQ-003 | Route/navigation component render tests | `frontend/src/__tests__/components/workspace-sidebar.test.ts`; `frontend/src/__tests__/components/loop-tertiary-routes.test.ts` |
| REQ-004 through REQ-006 | Matrix rendering tests | Matrix UI test output |
| REQ-007 through REQ-009 | Matrix launch-kind and route-query tests | `frontend/src/__tests__/lib/agent-matrix-cells.test.ts`; `frontend/src/__tests__/lib/agent-matrix-launch.test.ts`; `frontend/src/__tests__/components/agent-matrix-panel.test.ts` |
| REQ-010 | Disabled-state visibility render tests where unsupported variants are surfaced | `frontend/src/__tests__/components/agent-matrix-panel.test.ts`; `frontend/src/__tests__/components/pipeline-surface.test.ts` |
| REQ-011 | Identity/route-state review | `frontend/src/__tests__/lib/agent-matrix-cells.test.ts`; `frontend/src/__tests__/components/agent-matrix-panel.test.ts`; `frontend/src/__tests__/lib/task-scope-selection.test.ts` |

## Documentation

Required or anticipated artifacts:

- Navigation components.
- Matrix UI tests.
- Route query handling.
- Evidence notes identifying any route-state parameters chosen by implementation.
- ADQ-13 evidence: `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/Evidence_ADQ-13_UI_Specs_Render_Tests.md`.
- Human ruling if the dispatch path/package rename is material to scope identity.
- P3 disposition: selected implementation keys are documented above; source-pointer and package-path warnings remain surfaced for future governed reconciliation.

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-105 supersedes run-scoped dependency-extraction deferral wording: the extracted register exists and is live. UPD-106 is implemented by the `ShellFrame` render test asserting the rendered PORTAL link carries `shell-nav-link--active`.

## D-APP-56 shell ownership amendment (2026-07-12)

R4-P29 assigns the `/chat` direct-chat shell surface and portal persona-picker bar to DEL-02-01 shell scope. The deliverable-rows launcher remains covered by DEL-02-03 REQ-009. DEL-08-02 retains persona-alias ownership and owns the `isMatrixLaunchBlockedByStreaming` persona/matrix launch guard as consumer-side behavior.
