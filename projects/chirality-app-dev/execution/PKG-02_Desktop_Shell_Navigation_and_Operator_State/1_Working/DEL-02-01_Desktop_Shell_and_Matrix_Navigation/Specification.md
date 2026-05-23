# Specification: DEL-02-01 Desktop Shell and Matrix Navigation

## Scope

This deliverable covers the user-facing desktop shell navigation and canonical matrix routing for `DEL-02-01 Desktop Shell and Matrix Navigation`.

In scope:

- PORTAL, WORKBENCH, and PIPELINE shell navigation.
- Header navigation between `/`, `/pipeline`, and `/workbench`.
- PORTAL rendering of the canonical 3x4 agent matrix.
- Matrix row-semantics routing into WORKBENCH or PIPELINE.
- Navigation components, matrix UI tests, and route query handling to the extent supported by source evidence.

Out of scope:

- Runtime engine internals.
- Workbench agent-context detail owned by adjacent deliverables except where routing handoff requires it.
- Pipeline selector behavior beyond receiving OPERATIVE matrix routes.
- Dependency extraction and `Dependencies.csv` creation for this run.

## Requirements

| ID | Requirement | Priority | Source | Verification |
|---|---|---:|---|---|
| DEL-02-01-REQ-001 | The app shall provide a desktop shell with PORTAL, PIPELINE, and WORKBENCH navigation. | P0 | REF-006 Section 8.1 FR-001; SOW-001 | Navigation UI test or route-level integration test confirms all three surfaces are reachable. |
| DEL-02-01-REQ-002 | Header navigation shall route to `/`, `/pipeline`, and `/workbench`. | P0 | REF-006 Section 8.1 FR-001 | Route assertion confirms the header target paths. |
| DEL-02-01-REQ-003 | Header navigation shall visually indicate the active route. | P0 | REF-006 Section 8.1 FR-001 | UI assertion confirms active state on each route. |
| DEL-02-01-REQ-004 | PORTAL shall render the canonical 3x4 agent matrix. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.3 | Matrix UI test confirms 3 rows and 4 columns. |
| DEL-02-01-REQ-005 | Matrix rows shall be `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE`. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.1 | Matrix UI test checks row labels and row order if order is encoded in implementation. |
| DEL-02-01-REQ-006 | Matrix columns shall be `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING`. | P0 | REF-006 Section 8.2 FR-007; REF-004 Section 4.2 | Matrix UI test checks column labels and column order if order is encoded in implementation. |
| DEL-02-01-REQ-007 | NORMATIVE matrix cells shall route to WORKBENCH. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1 | Matrix routing test confirms destination surface. |
| DEL-02-01-REQ-008 | EVALUATIVE matrix cells shall route to WORKBENCH. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1 | Matrix routing test confirms destination surface. |
| DEL-02-01-REQ-009 | OPERATIVE matrix cells shall route to PIPELINE. | P0 | REF-006 Sections 7.2 and 8.2 FR-008; REF-004 Section 4.1 | Matrix routing test confirms destination surface. |
| DEL-02-01-REQ-010 | Disabled or unsupported variants shall remain visible as coming soon rather than disappearing when encountered in matrix-adjacent navigation flows. | P0 | REF-006 Section 7.2 acceptance | UI test confirms unsupported variants are visible and non-selectable where this deliverable exposes them. |
| DEL-02-01-REQ-011 | Stable identifiers shall remain distinct from path or label changes. | TBD | REF-002 `docs/CONTRACT.md` K-ID-1 and K-PATH-1; REF-006 Section 8.2 FR-009 | ASSUMPTION: applies to route state and matrix identity; exact implementation assertion TBD until route-state key names are selected. P3 disposition: C-001 converted to TBD for key names; X-001 converted to TBD for acceptance assertion names. |

## Standards

| Standard or Source | Applicability | Status |
|---|---|---|
| `docs/PRD.md` | Product requirements for shell navigation and matrix routing | Accessible; hash mismatch recorded as warning per dispatch |
| `docs/TYPES.md` Section 4 | Canonical UI navigation vocabulary and matrix semantics | Accessible |
| `docs/CONTRACT.md` K-ID-1, K-PATH-1, K-INVENT-1, K-CONFLICT-1 | Stable identity and epistemic controls relevant to routing and document production | Accessible |
| `docs/DIRECTIVE.md` Section 4.1 | In-scope statement for local desktop operation and matrix navigation | Accessible |
| SOFTWARE_DECOMP v3.2 | Deliverable scope, SOW mapping, objective context, and execution note to preserve ResponsibleParty | Accessible |

## Verification

| Requirement IDs | Verification Approach | Evidence Record |
|---|---|---|
| REQ-001 through REQ-003 | Route/navigation component tests | Navigation component test output; route assertions |
| REQ-004 through REQ-006 | Matrix rendering tests | Matrix UI test output |
| REQ-007 through REQ-009 | Matrix click/routing tests | Route query handling test output |
| REQ-010 | Disabled-state visibility test if unsupported variants are surfaced in this slice | UI test output or human ruling if owned by another deliverable |
| REQ-011 | Identity/route-state review | TBD; once route-state keys are selected, evidence should assert that selected agent, row, column, or category identity remains stable across label/path changes. Exact query key names and assertion names remain TBD from source slices. P3 disposition: C-001 and X-001 converted to TBD. |

## Documentation

Required or anticipated artifacts:

- Navigation components.
- Matrix UI tests.
- Route query handling.
- Evidence notes identifying any route-state parameters chosen by implementation.
- Human ruling if the dispatch path/package rename is material to scope identity.
- P3 disposition: C-001 and X-001 require implementation-time evidence notes once route-state keys and acceptance assertions are selected.
