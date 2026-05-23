# Guidance: DEL-02-01 Desktop Shell and Matrix Navigation

## Purpose

This deliverable preserves the operator's primary movement through Chirality's desktop shell: PORTAL for the matrix entry point, WORKBENCH for interactive persona agents, and PIPELINE for operative task categories. It supports OBJ-001 by keeping the local desktop harness clear, governed, and navigable.

## Principles

- Keep shell navigation explicit: PORTAL, PIPELINE, and WORKBENCH are first-class surfaces, not incidental views.
- Treat the agent matrix as canonical product vocabulary. Use `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE` for rows, and `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING` for columns.
- Route by row semantics: `NORMATIVE` and `EVALUATIVE` go to WORKBENCH; `OPERATIVE` goes to PIPELINE.
- Preserve stable IDs and route meaning across label or path changes. ASSUMPTION: this applies to matrix cell identifiers and query state, although exact route parameter names are TBD in the available source slices.
- Keep unsupported variants visible as coming soon when this slice exposes them, instead of hiding roadmap-aware choices.
- Do not make runtime engine behavior part of this deliverable; this slice owns navigation and routing presentation.

## Considerations

- `docs/PRD.md` is the main product requirement source for this slice, but its observed hash differs from the expected hash in `_REFERENCES.md`. The dispatch instruction says to treat that mismatch as a source warning, not a blocker.
- The PRD says matrix routing follows the `docs/SPEC` contract, while the accessible route semantics for rows and cells are in `docs/TYPES.md` Section 4 and PRD Section 7.2/8.2. Until a human reconciles that wording, use TYPES plus PRD as the concrete source for matrix routing behavior.
- DEL-08-02 also covers matrix routing contract concerns. DEL-02-01 should focus on the visible shell and matrix navigation behavior, while leaving persona alias and deeper routing-contract ownership to DEL-08-02 unless a human ruling expands this slice.
- DEL-02-02 and DEL-08-03 own adjacent workbench/pipeline selector details. This deliverable should test that row routing lands on the correct surface without over-specifying downstream controls.
- Query-state naming for selected agent, row, column, or category is source-supported only as anticipated "route query handling"; exact key names are TBD.

## Trade-offs

| Topic | Direction | Rationale |
|---|---|---|
| Canonical matrix vocabulary vs. UI copy flexibility | Prefer canonical row/column values in tests and route state | TYPES Section 4 gives stable terms that reduce routing ambiguity. |
| Shell scope vs. runtime scope | Keep runtime internals out of this deliverable | PKG-02 excludes runtime engine internals. |
| Visible disabled options vs. minimal UI | Keep unsupported variants visible when this slice exposes them | PRD Section 7.2 acceptance requires unsupported variants to remain visible as coming soon. |
| Query parameter specificity | Mark exact parameter names TBD | Source slices require active context/query handling elsewhere but do not define this deliverable's parameter schema. |

## Examples

| Example | Expected Result | Source |
|---|---|---|
| Operator selects a NORMATIVE matrix cell from PORTAL | WORKBENCH opens with row/cell context as supported by route state | REF-006 Section 7.2; REF-004 Section 4.1 |
| Operator selects an OPERATIVE matrix cell from PORTAL | PIPELINE opens with category context as supported by route state | REF-006 Section 7.2; REF-004 Section 4.1 |
| Operator uses header navigation to open PIPELINE | `/pipeline` route is reached and active route is visually indicated | REF-006 Section 8.1 FR-001 |

## Conflict Table (for human ruling)

| Conflict ID | Source A | Source B | Issue | Current Handling | Human Ruling Needed |
|---|---|---|---|---|---|
| CONFLICT-001 | Dispatch deliverable path uses `PKG-02_Desktop_UI_and_Local_Experience` | Existing in-repo deliverable folder uses `PKG-02_Desktop_Shell_Navigation_and_Operator_State` and `_CONTEXT.md` package name matches decomposition | Package path segment differs from dispatch, while deliverable ID and name match | Wrote only inside the existing DEL-02-01 folder and recorded this as a scope/path warning. P3 disposition: E-001 already covered as conflict. | Confirm whether the package path rename is accepted and whether future dispatches should use the existing path |
| CONFLICT-002 | REF-006 expected SHA in `_REFERENCES.md` | REF-006 actual SHA in `_REFERENCES.md` | PRD hash mismatch | Treated as source warning, not blocker, per dispatch. P3 disposition: B-001 already covered as conflict. | Confirm whether observed PRD hash should replace expected hash in a later governed reference update |
| CONFLICT-003 | PRD FR-008 says matrix routing shall follow the `docs/SPEC` contract | Accessible concrete matrix vocabulary and row destination semantics are in `docs/TYPES.md` Section 4, not in located `docs/SPEC.md` slices | Source pointer appears imprecise or stale | Used PRD Section 7.2/8.2 plus TYPES Section 4 for concrete routing requirements. P3 disposition: F-001 already covered as conflict. | Confirm whether SPEC should be amended or whether TYPES is the intended route-semantics authority |
