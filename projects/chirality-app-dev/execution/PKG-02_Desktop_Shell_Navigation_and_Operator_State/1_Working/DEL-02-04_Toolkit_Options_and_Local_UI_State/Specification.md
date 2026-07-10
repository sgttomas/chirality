# Specification: DEL-02-04 Toolkit Options and Local UI State

## Scope

This deliverable covers the UX/UI slice that exposes runtime options and preserves pane layout, chat drafts, attachment selections, and local presets as non-authoritative convenience state for the Chirality desktop shell.

Included:

- Toolkit controls for per-turn runtime options.
- Local pane resize/collapse state for File Tree, Toolkit, and Chat panes.
- Local draft, attachment-selection, and preset persistence guards.
- UI behavior that respects deterministic runtime option fallback and warnings.

Excluded:

- Runtime engine internals.
- SDK-specific option builder implementation, except where the UI must not contradict accepted runtime option behavior.
- API key entry/status UI, secure-storage feedback, and typed runtime error display assigned to DEL-02-05.
- Dependency extraction; this run intentionally does not create `Dependencies.csv`.

Sources: `_CONTEXT.md`; `docs/PRD.md` Sections 8.1, 8.4, 8.7; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-04.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-02-04-REQ-001 | The shell shall support resizable and collapsible File Tree, Toolkit, and Chat panes. | `docs/PRD.md` Section 8.1 FR-005 |
| DEL-02-04-REQ-002 | Pane resize/collapse behavior shall support drag and keyboard operation; Home collapses, End expands, and widths are persisted locally. | `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019 |
| DEL-02-04-REQ-003 | The Toolkit panel shall expose per-turn options for model, tools, max turns, mode, persona, and governance metadata as supported by runtime. | `docs/PRD.md` Section 8.7 FR-041 |
| DEL-02-04-REQ-004 | Toolkit settings and presets shall persist locally and remain non-authoritative. | `docs/PRD.md` Section 8.7 FR-042; `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |
| DEL-02-04-REQ-005 | Local presets shall not override governance enforcement or project truth. | `docs/PRD.md` Section 8.7 FR-042; `docs/CONTRACT.md` K-NOMEM-1 |
| DEL-02-04-REQ-006 | Chat drafts and attachment selections shall persist locally per root/persona/mode. | `docs/PRD.md` Section 8.7 FR-043 |
| DEL-02-04-REQ-007 | Malformed local draft or attachment-selection records shall be dropped. | `docs/PRD.md` Section 8.7 FR-043 |
| DEL-02-04-REQ-008 | Local storage failures shall warn without breaking chat. | `docs/PRD.md` Section 8.7 FR-043 |
| DEL-02-04-REQ-009 | Toolkit mode controls shall map to permission policy modes once the policy engine exists. | `docs/PRD.md` Section 8.7 FR-044 |
| DEL-02-04-REQ-010 | Toolkit mode controls shall not be treated as mere prompt hints when permission policy enforcement exists. | `docs/PRD.md` Section 8.7 FR-044 |
| DEL-02-04-REQ-011 | Runtime option fallback chains represented or initiated by the UI shall remain deterministic. | `docs/PRD.md` Section 8.4 FR-023; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-016 |
| DEL-02-04-REQ-012 | Unknown option keys shall be ignored with warnings and shall not silently mutate behavior. | `docs/PRD.md` Section 8.4 FR-024; `docs/SPEC.md` Section 13.1 |
| DEL-02-04-REQ-013 | UI visibility of an option shall be non-authoritative; governance and permission policy remain authoritative. | `docs/SPEC.md` Section 7.4 |
| DEL-02-04-REQ-014 | The UI shall preserve a professional, dense-but-readable interface for the shell surfaces. | `docs/PRD.md` Section 8.1 FR-006 |

## Standards

| Standard or Source | Applicability | Status |
|---|---|---|
| Chirality Directive | Human authority, evidence posture, and non-authoritative convenience state. | Accessible: `docs/DIRECTIVE.md` |
| Chirality Contract | Binding invariants for hidden memory, SDK/settings posture, permissions, and tool exposure. | Accessible: `docs/CONTRACT.md` |
| Chirality Spec | Runtime configuration state, working-root truth, option visibility, and unknown-option behavior. | Accessible: `docs/SPEC.md` |
| Chirality PRD | Product requirements for desktop shell, runtime options, Toolkit, and local UI state. | Accessible: `_REFERENCES.md` REF-006 is reconciled and records `MATCH`. |
| Active SOFTWARE_DECOMP v3.2 | DEL-02-04 scope, SOW coverage, objective mapping, and package boundary. | Accessible: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |

## Verification

| Requirement IDs | Verification Approach |
|---|---|
| DEL-02-04-REQ-001, DEL-02-04-REQ-002 | UI tests or interaction checks for drag resizing, keyboard arrow resize if implemented, Home collapse, End expand, persistence after reload, and focusable separator semantics. |
| DEL-02-04-REQ-003 | Component or integration tests confirming the Toolkit can set only supported runtime options and labels unsupported/unavailable options without inventing behavior. |
| DEL-02-04-REQ-004, DEL-02-04-REQ-005, DEL-02-04-REQ-013 | Tests or review checks proving local presets do not write project truth files, do not override governance enforcement, and cannot be treated as authoritative runtime policy. |
| DEL-02-04-REQ-006, DEL-02-04-REQ-007, DEL-02-04-REQ-008 | Local-storage tests for root/persona/mode keying, malformed-record discard, and storage-failure warning behavior. |
| DEL-02-04-REQ-009, DEL-02-04-REQ-010 | Policy-mode integration tests once the permission policy engine exists; until then, mark enforcement wiring as TBD and avoid false claims. |
| DEL-02-04-REQ-011, DEL-02-04-REQ-012 | Option-handoff tests confirming deterministic fallback display/submit behavior and warnings for unknown keys; test records must show that unknown keys are warned, ignored, and do not silently mutate runtime behavior. |
| DEL-02-04-REQ-014 | Review against `docs/ui/UI_POLISH_EXECUTION_PLAN.md`, including D-APP-36 component/render evidence and browser or screenshot evidence where layout risk warrants it. The checklist makes verification repeatable; REQ-014 remains unproven until current evidence is recorded. |

## Documentation

Required artifacts for this deliverable:

- Toolkit controls.
- Pane resize/collapse state behavior.
- Draft and preset storage guards.
- Tests or verification notes for local-state non-authority and option fallback behavior.
- Any unresolved policy-mode wiring notes marked `TBD` until the permission policy engine exists.
- Policy-mode acceptance evidence after the permission policy engine exists, including the accepted enum/contract source, Toolkit mode-to-policy mapping, and evidence that controls are enforced by runtime policy rather than prompt text alone.
- Option-handoff evidence for deterministic fallback and unknown-key handling, including the submitted option payload, warning behavior, and unchanged runtime behavior for ignored keys.

## Assumptions and TBDs

- ASSUMPTION: UI implementation will key local draft and attachment-selection persistence by normalized root/persona/mode, matching PRD FR-043. Exact local storage namespace, key format, value schema, migration behavior, and retention policy are TBD.
- ASSUMPTION: Toolkit controls will present only runtime-supported option fields or clearly disabled/unavailable fields. Exact runtime-supported control inventory is TBD; current source support names model, tools, max turns, mode, persona, and governance metadata as candidate option categories.
- TBD: Exact file/component names for Toolkit controls and pane state implementation.
- TBD: Exact permission policy mode enum and enforcement integration until the policy engine is accepted.
