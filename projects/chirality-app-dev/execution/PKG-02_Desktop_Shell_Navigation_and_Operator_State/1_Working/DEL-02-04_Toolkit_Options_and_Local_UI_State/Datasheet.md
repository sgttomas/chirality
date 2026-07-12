# Datasheet: DEL-02-04 Toolkit Options and Local UI State

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-02-04 |
| DeliverableName | Toolkit Options and Local UI State |
| PackageID | PKG-02 |
| PackageName | Desktop Shell, Navigation, and Operator State |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | S |
| ScopeItems | SOW-004, SOW-008, SOW-016 |
| Objectives | OBJ-001, OBJ-004 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary UI surfaces | File Tree, Toolkit, and Chat panes for layout behavior; Toolkit panel for runtime options. | `docs/PRD.md` Section 8.1 FR-005; Section 8.7 FR-041 |
| Runtime option categories exposed by Toolkit | model, tools, max turns, mode, persona, governance metadata as supported by runtime. | `docs/PRD.md` Section 8.7 FR-041 |
| Runtime option fallback behavior | Model, tools, and max-turn options follow deterministic fallback chains. | `docs/PRD.md` Section 8.4 FR-023; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-016 |
| Unknown option behavior | Unknown option keys are ignored with warnings. | `docs/PRD.md` Section 8.4 FR-024; `docs/SPEC.md` runtime option rules, line 681 |
| Local persistence scope | Toolkit settings, pane widths, chat drafts, attachment selections, and local presets are local convenience state. | `docs/PRD.md` Section 8.1 FR-005; Section 8.7 FR-042 and FR-043; `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |
| Accessibility expectation | Keyboard users can resize/collapse panes; resize handles are focusable separators with arrow/Home/End behavior. | `docs/PRD.md` Section 11.4 NFR-019 |
| UI-quality evidence | Current component/render evidence plus risk-based browser or screenshot review; checklist presence alone is not acceptance. | `docs/ui/UI_POLISH_EXECUTION_PLAN.md`; `docs/ISSUE_READINESS_PROFILES.md` Section 4 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Authority boundary | Local UI state is non-authoritative and must not override governance enforcement or project truth. | `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3; `docs/PRD.md` Section 8.7 FR-042 |
| Professional reliance boundary | Agent outputs and UI/runtime state remain draft or decision-support material until accepted by an accountable human. | `docs/DIRECTIVE.md` Sections 2.3 and 2.4; `docs/PRD.md` Section 15 KG-015 |
| Storage failure behavior | Storage failures for chat drafts and attachment selections warn without breaking chat. | `docs/PRD.md` Section 8.7 FR-043 |
| Malformed local records | Malformed draft/attachment records are dropped. | `docs/PRD.md` Section 8.7 FR-043 |
| Runtime governance | Toolkit mode controls must map to permission policy modes once the policy engine exists. | `docs/PRD.md` Section 8.7 FR-044 |
| PRD source status | Reconciled: expected and actual SHA-256 values match. | `_REFERENCES.md` REF-006 |

## Construction

| Component or Artifact | Required Content | Source |
|---|---|---|
| Toolkit controls | UI controls for per-turn runtime options supported by the runtime. Exact component names and implementation files are TBD. | `docs/PRD.md` Section 8.7 FR-041 |
| Pane state controls | Drag and keyboard resize/collapse support for File Tree, Toolkit, and Chat panes, with locally persisted widths. | `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019 |
| Draft and preset guards | Local persistence keyed per root/persona/mode for drafts and attachment selections; malformed records dropped; storage failures warn. | `docs/PRD.md` Section 8.7 FR-043 |
| Governance guard | Local presets and visibility of options cannot become authoritative or override runtime governance. | `docs/PRD.md` Section 8.7 FR-042; `docs/SPEC.md` runtime UI option rule, line 431 |
| Deterministic option handoff | Runtime option keys follow accepted fallback behavior; unknown keys warn and do not silently mutate behavior. | `docs/PRD.md` Section 8.4 FR-023 and FR-024 |

## References

- `docs/DIRECTIVE.md` Sections 2.3, 2.4, 2.5, 2.6, 4.2.
- `docs/CONTRACT.md` invariants K-NOMEM-1, K-SDK-1, K-PERM-3, K-TOOL-1.
- `docs/SPEC.md` Sections 1.2, 1.3 and runtime option rules around UI option authority and unknown keys.
- `docs/TYPES.md` lifecycle state definitions.
- `docs/PRD.md` Sections 8.1, 8.4, 8.7, 11.4, 15, 16.
- `docs/ui/UI_POLISH_EXECUTION_PLAN.md` for UI-quality evidence routing.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-04, SOW-004, SOW-008, SOW-016, OBJ-001, OBJ-004.

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-109 records the ruled loop-first layout: File Tree and Chat are the resizable panes; Tool Kit is a right-sidebar tab. UPD-111 records that the 14-row derivative dependency register exists. UPD-110 is implemented by the governed `AppShell` keyboard-resize interaction test.
