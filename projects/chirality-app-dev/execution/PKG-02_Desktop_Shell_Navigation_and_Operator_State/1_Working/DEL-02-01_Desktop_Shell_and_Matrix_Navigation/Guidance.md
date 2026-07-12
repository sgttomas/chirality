# Guidance: DEL-02-01 Desktop Shell and Matrix Navigation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

This deliverable preserves the operator's primary movement through Chirality's loop-first desktop shell: PORTAL for the matrix entry point, WORKBENCH as a contract/context review form, and PIPELINE for operative task categories. It supports OBJ-001 by keeping the local desktop harness clear, governed, and navigable while the live loop remains mounted.

## Principles

- Keep shell navigation explicit: PORTAL, PIPELINE, and WORKBENCH are first-class surfaces, with PORTAL as the primary header entry and Workbench/Pipeline preserved as right-sidebar tertiary forms and deep-link entries.
- Treat the agent matrix as canonical product vocabulary. Use `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE` for rows, and `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING` for columns.
- Route by row semantics: `NORMATIVE` and `EVALUATIVE` focus the mounted live loop with Type-0/Type-1 persona context; `OPERATIVE` opens PIPELINE intent.
- Preserve stable IDs and route meaning across label or path changes. Current implementation evidence uses `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` keys; future authority work may still reconcile source wording.
- Keep unsupported variants visible as coming soon when this slice exposes them, instead of hiding roadmap-aware choices.
- Do not make runtime engine behavior part of this deliverable; this slice owns navigation and routing presentation.

## Considerations

- `docs/PRD.md` is the main product requirement source for this slice; its observed hash matches the expected REF-006 hash under D-APP-38 and is not a blocker.
- The PRD says matrix routing follows the `docs/SPEC` contract, while the accessible route semantics for rows and cells are in `docs/TYPES.md` Section 4 and PRD Section 7.2/8.2. Until a human reconciles that wording, use TYPES plus PRD as the concrete source for matrix routing behavior.
- DEL-08-02 also covers matrix routing contract concerns. DEL-02-01 should focus on the visible shell and matrix navigation behavior, while leaving persona alias and deeper routing-contract ownership to DEL-08-02 unless a human ruling expands this slice.
- DEL-02-02 and DEL-08-03 own adjacent workbench/pipeline selector details. This deliverable should test that row routing lands on the correct surface without over-specifying downstream controls.
- Query-state naming for selected agent, row, column, category, task scope, and deliverable key is source-supported as anticipated "route query handling"; ADQ-13 records the selected implementation keys while leaving older source-pointer wording MATCH-verified. (reconciled under D-APP-38).

## Trade-offs

| Topic | Direction | Rationale |
|---|---|---|
| Canonical matrix vocabulary vs. UI copy flexibility | Prefer canonical row/column values in tests and route state | TYPES Section 4 gives stable terms that reduce routing ambiguity. |
| Shell scope vs. runtime scope | Keep runtime internals out of this deliverable | PKG-02 excludes runtime engine internals. |
| Visible disabled options vs. minimal UI | Keep unsupported variants visible when this slice exposes them | PRD Section 7.2 acceptance requires unsupported variants to remain visible as coming soon. |
| Query parameter specificity | Treat selected implementation keys as evidence-backed, not new source authority | Source slices require active context/query handling but do not independently define this deliverable's full parameter schema. |

## Examples

| Example | Expected Result | Source |
|---|---|---|
| Operator selects a NORMATIVE matrix cell from PORTAL | The mounted live loop receives the selected persona context without replacing the primary pane | REF-006 Section 7.2; REF-004 Section 4.1; D-APP-28/D-APP-30 |
| Operator selects an OPERATIVE matrix cell from PORTAL | PIPELINE opens with category context in the right sidebar or preserved deep-link entry | REF-006 Section 7.2; REF-004 Section 4.1; D-APP-28/D-APP-31 |
| Operator opens `/pipeline` directly | The route opens the loop-first shell with the Pipeline sidebar tab selected | REF-006 Section 8.1 FR-001; D-APP-31 |

## Conflict Table (for human ruling)

| Conflict ID | Source A | Source B | Issue | Current Handling | Human Ruling Needed |
|---|---|---|---|---|---|
| CONFLICT-001 | Dispatch deliverable path uses `PKG-02_Desktop_UI_and_Local_Experience` | Existing in-repo deliverable folder uses `PKG-02_Desktop_Shell_Navigation_and_Operator_State` and `_CONTEXT.md` package name matches decomposition | Package path segment differs from dispatch, while deliverable ID and name match | Wrote only inside the existing DEL-02-01 folder and recorded this as a scope/path warning. P3 disposition: E-001 already covered as conflict. | Confirm whether the package path rename is accepted and whether future dispatches should use the existing path |
| CONFLICT-002 | REF-006 expected SHA in `_REFERENCES.md` | REF-006 actual SHA in `_REFERENCES.md` | PRD hash status: MATCH | Treated as source warning, not blocker, per dispatch. P3 disposition: B-001 already covered as conflict. | Confirm whether observed PRD hash should replace expected hash in a later governed reference update — reconciled under D-APP-38 |
| CONFLICT-003 | PRD FR-008 says matrix routing shall follow the `docs/SPEC` contract | Accessible concrete matrix vocabulary and row destination semantics are in `docs/TYPES.md` Section 4, not in located `docs/SPEC.md` slices | Source pointer appears imprecise or stale | Used PRD Section 7.2/8.2 plus TYPES Section 4 for concrete routing requirements. P3 disposition: F-001 already covered as conflict. | Confirm whether SPEC should be amended or whether TYPES is the intended route-semantics authority |
