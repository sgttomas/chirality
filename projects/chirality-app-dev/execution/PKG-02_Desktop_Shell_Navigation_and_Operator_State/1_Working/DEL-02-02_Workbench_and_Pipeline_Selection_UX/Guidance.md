# Guidance: DEL-02-02 Workbench and Pipeline Selection UX

## Purpose

This deliverable keeps the Workbench and Pipeline selection experience coherent for operators moving from the matrix into interactive personas or operative task categories. The UX should preserve active agent context, make available pipeline choices visible, prevent stale or invalid selections, and keep UI convenience state subordinate to governed project files.

Sources: `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` Sections 7.2, 7.5, 8.2, and 14.

## Principles

- Preserve context at route boundaries: Workbench shall show selected agent, row, and column when opened as a sidebar/deep-link tertiary form; NORMATIVE/EVALUATIVE matrix cells now select live-loop persona context under the accepted loop-first pivot. Source: `docs/PRD.md` Section 8.2 FR-009; D-APP-28/D-APP-30.
- Keep operative selection explicit: PIPELINE should expose `DECOMP`, `PREP`, `TASK`, and `AUDIT`, and `TASK` should separate agent choice from scope choice. Source: `docs/PRD.md` Section 8.2 FR-011 and FR-012.
- Prefer disabled visibility over disappearance for unsupported options, so operators can see roadmap shape without being able to invoke unavailable behavior. Source: `docs/PRD.md` Section 7.2; `docs/TYPES.md` Section 4.4.
- Reset stale selections rather than carrying invalid state across root or scan changes. Source: `docs/PRD.md` Section 8.2 FR-013 and Section 7.5.
- Treat UI local state as non-authoritative convenience state. Project truth remains in working-root files and accepted git history. Source: `docs/DIRECTIVE.md` Sections 2.1, 2.2, and 2.6.

## Considerations

- SOW-007 is listed in `_CONTEXT.md` as covered by DEL-02-02, while the decomposition scope ledger assigns SOW-007 to PKG-08 / DEL-08-03 as the primary package for agent dispatch. For this deliverable, treat Pipeline selectors as a UI presentation and selection concern; dispatch semantics remain with PKG-08 unless a human rules otherwise.
- Workbench deliverable contract summaries depend on status and dependency APIs. This deliverable should verify UI behavior but not extract dependencies or create `Dependencies.csv`.
- `KNOWLEDGE_TYPES` mode should not become selectable unless the source scan indicates a knowledge decomposition marker. Source: `docs/PRD.md` Section 7.5.
- The PRD is usable for this run but has a recorded hash mismatch in `_REFERENCES.md`; source-backed content from the PRD should remain reviewable against the observed file.
- ADQ-13 inspected the current frontend surfaces for this deliverable and records implementation/test paths in `Evidence_ADQ-13_UI_Specs_Render_Tests.md`. Earlier source-warning and ownership conflicts remain visible; this does not assert dependency closure or lifecycle issuance.

## Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Visible disabled options vs. hiding unsupported scope | Prefer visible disabled options when a variant is unsupported or coming soon. This preserves operator awareness without enabling execution. | `docs/PRD.md` Sections 7.2 and 14; `docs/TYPES.md` Section 4.4 |
| Local UI persistence vs. authoritative project state | Persist convenience state only when it cannot override `_STATUS.md`, dependency records, deliverable files, or accepted git history. | `docs/DIRECTIVE.md` Section 2.6; `docs/CONTRACT.md` Section 1.7 |
| UX slice ownership vs. agent-dispatch ownership | Keep selector display and stale-selection behavior in this UX slice; keep dispatch governance and subagent behavior in PKG-08. | `_CONTEXT.md`; decomposition scope ledger SOW-007 |
| Defaults vs. explicit context | Provide sensible defaults for incomplete Workbench query params, but visibly show the resolved agent/row/column so the operator knows active context. | `docs/PRD.md` Section 8.2 FR-009 |

## Examples

| Scenario | Expected behavior | Source |
|---|---|---|
| User clicks a NORMATIVE matrix cell | The mounted live loop receives the selected persona context; Workbench remains available for context/contract review. | `docs/PRD.md` Sections 7.2 and 8.2; D-APP-28/D-APP-30 |
| User clicks an OPERATIVE matrix cell | App opens PIPELINE with the relevant category context. | `docs/PRD.md` Section 7.2 |
| User opens PIPELINE TASK | UI shows split controls for task agent and scope; scope modes are deliverables or knowledge types. | `docs/PRD.md` Section 8.2 FR-012 |
| Working root changes | Invalid deliverable or knowledge-type selections reset. | `docs/PRD.md` Section 8.2 FR-013 |
| Unsupported pipeline option exists | Option remains visible but disabled as coming soon. | `docs/PRD.md` Section 7.2; `docs/TYPES.md` Section 4.4 |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| DEL-02-02-CONFLICT-001 | Dispatch path used stale package label `PKG-02_Desktop_UI_and_Local_Experience`, but the live scaffolded deliverable is under `PKG-02_Desktop_Shell_Navigation_and_Operator_State`. | User dispatch brief | `_CONTEXT.md` Identity; `execution/_Coordination/WORKSPACE_MANIFEST.csv` row for DEL-02-02 | All run-record scope references | Use the unique live DEL-02-02 path and preserve the path mismatch as a source warning. | TBD |
| DEL-02-02-CONFLICT-002 | PRD expected hash differs from observed hash. Dispatch says to treat this as a source warning, not a blocker. | `_REFERENCES.md` REF-006 row | User dispatch brief | All PRD-backed requirements | Continue using accessible `docs/PRD.md`, cite sections, and surface hash mismatch for review. | TBD |
| DEL-02-02-CONFLICT-003 | `_CONTEXT.md` lists SOW-007 under DEL-02-02, while the decomposition scope ledger maps SOW-007 to PKG-08 / DEL-08-03 with PKG-08 as primary package. | `_CONTEXT.md` Traceability | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Scope Ledger SOW-007 | Specification scope, requirements, and ownership notes | Treat DEL-02-02 as UI selector owner and PKG-08 as dispatch semantics owner. | TBD |
