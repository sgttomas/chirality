# Procedure: DEL-02-01 Desktop Shell and Matrix Navigation

## Purpose

Produce and verify the desktop shell and matrix navigation slice for DEL-02-01, preserving PORTAL, WORKBENCH, and PIPELINE navigation and canonical matrix routing.

## Prerequisites

- Accessible source references listed in `_REFERENCES.md`.
- Current deliverable context in `_CONTEXT.md`.
- Existing implementation workspace for navigation components and tests. Exact implementation paths are TBD because they are not listed in this deliverable's authoritative source slices.
- Implementation evidence slots are required for later closure: navigation component path, matrix UI test path, and route query handling test path. Exact paths remain TBD until selected by implementation. P3 disposition: D-001 converted to TBD.
- Human acceptance that `ResponsibleParty` remains `TBD` until assigned.
- Dependency extraction remains deferred; do not create `Dependencies.csv` as part of this procedure.

Declared upstream dependencies:

- TBD - no accepted dependency edges have been extracted yet.

Declared downstream dependencies:

- TBD - no accepted dependency edges have been extracted yet.

## Steps

1. Confirm the deliverable identity from `_CONTEXT.md`: `DEL-02-01 Desktop Shell and Matrix Navigation`, `ResponsibleParty: TBD`, `Type: UX_UI_SLICE`, `ContextEnvelope: M`.
2. Confirm authoritative source availability from `_REFERENCES.md`; treat the PRD hash mismatch as a source warning unless a human ruling changes that instruction.
3. Preserve the shell's three primary surfaces: PORTAL at `/`, PIPELINE at `/pipeline`, and WORKBENCH at `/workbench`.
4. Ensure header navigation exposes all three surfaces and visually indicates the active route.
5. Render the PORTAL matrix with rows `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE`.
6. Render the PORTAL matrix with columns `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING`.
7. Route `NORMATIVE` cells to WORKBENCH.
8. Route `EVALUATIVE` cells to WORKBENCH.
9. Route `OPERATIVE` cells to PIPELINE.
10. Preserve unsupported or disabled variants as visible coming-soon options where this deliverable exposes them.
11. Add or update matrix UI tests for row/column rendering and row-semantics routing.
12. Add or update route query handling tests only to the extent implementation chooses route-state keys; exact query key names are TBD from source.
13. Keep runtime engine internals out of this slice; hand off engine or selector-specific behavior to adjacent deliverables.
14. Record selected implementation paths for navigation components, matrix UI tests, and route query handling tests when they exist; until selected, keep those fields as TBD. P3 disposition: D-001 converted to TBD.

## Verification

| Check | Expected Result |
|---|---|
| Header navigation routes | `/`, `/pipeline`, and `/workbench` are reachable. |
| Active route state | Current surface is visually indicated. |
| Matrix shape | PORTAL shows 3 rows and 4 columns. |
| Row labels | `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE` are present. |
| Column labels | `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING` are present. |
| WORKBENCH routing | NORMATIVE and EVALUATIVE cells route to WORKBENCH. |
| PIPELINE routing | OPERATIVE cells route to PIPELINE. |
| Unsupported variants | Unsupported variants visible in this slice are disabled or coming soon, not silently removed. |
| Scope discipline | No runtime engine internals are changed under this deliverable's authority. |

## Implementation Evidence Slots

| Evidence Slot | Current Value | Source |
|---|---|---|
| Navigation component path | TBD until selected by implementation | `_CONTEXT.md` anticipated artifacts; decomp DEL-02-01 |
| Matrix UI test path | TBD until selected by implementation | `_CONTEXT.md` anticipated artifacts; decomp DEL-02-01 |
| Route query handling test path | TBD until selected by implementation | `_CONTEXT.md` anticipated artifacts; decomp DEL-02-01 |

P3 disposition: D-001 converted to TBD by adding explicit implementation evidence slots without inventing paths.

## Records

- Navigation component change notes or diff references.
- Matrix UI test results.
- Route query handling test results, with selected query key names documented.
- Any human rulings resolving the package path mismatch, PRD hash mismatch, or PRD/SPEC/TYPES source-pointer issue.
- This four-document kit and the TASK run record.
