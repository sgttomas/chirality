---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-04
package_id: PKG-02
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-004, SOW-008, SOW-016]
package_objective_refs: [OBJ-001, OBJ-004]
---

# Scope of Work — DEL-02-04

## Purpose and Objective Traceability

This Scope of Work defines `DEL-02-04` in service of project scope [SOW-004, SOW-008, SOW-016] and package objectives [OBJ-001, OBJ-004].

- **OUT-001** — Dialogue toolkit, explicit-context, and versioned local-workspace-state contract for DEL-02-04, traceable to SOW-004, SOW-008, SOW-016, OBJ-001, and OBJ-004.

## SCA-APP-004 Gate-5 Current Contract (Controlling until SCA-APP-010)

The owner-approved SCA-APP-004 amendment expands this deliverable's
non-authoritative convenience-state responsibilities for the Woven Dialogue
shell. Where older clauses below prescribe the former fixed pane arrangement,
this section controls. Prior resize, draft, option, and accessibility evidence
remains accepted compatibility evidence.

### Current responsibility

`DEL-02-04 Dialogue Toolkit, Context, and Local UI State` owns presentation and
local persistence for:

- versioned Navigator, dialogue, Coordination Panel, artifact-focus, and
  Activity Shelf layout state;
- primary-dialogue drafts, attachments, and local presets;
- explicit next-turn context references;
- provenance-bearing artifact anchors and return targets;
- selected replay references and Work/Agents panel selection; and
- rollback-safe, non-destructive local-state migration.

The primary live dialogue remains mounted and retains its draft, attachments,
context, permissions, interruption state, and interaction authority while a
focus view or replay is visible. Selected replay state is observational only.
Visible artifacts are not automatically next-turn context.

All state in this deliverable is convenience state. It cannot store or create
authoritative workflow, hierarchy, parentage, permission, approval,
assignment, lifecycle, acceptance, transcript, artifact, or runtime
conclusions. Runtime option validation and permission enforcement remain with
their existing owners.

### Current acceptance obligations

1. Introduce a versioned workspace-state schema and a one-time,
   rollback-safe migration that retains the prior state needed for rollback.
2. Preserve primary-dialogue draft, attachment, explicit-context, permission,
   interruption, and focus state across panel, artifact-focus, and replay
   selection.
3. Keep explicit next-turn context references separate from visible artifacts;
   no artifact becomes model context merely by being visible.
4. Persist only references and presentation state for artifacts, recorded
   sessions, and panel selections; missing targets degrade to explicit
   unavailable/unknown states.
5. Preserve accessible resize, collapse, keyboard region traversal, focus
   restoration, focusable separators, Home/End/Arrow behavior, and
   reduced-motion handling.
6. Verify malformed-state discard, storage-failure recovery, per-dialogue
   draft/context isolation, replay/primary isolation, and rollback behavior.

## SCA-APP-010 Gate-5 Current Contract (Controlling)

The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied
2026-09-04 at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged
as `7795b0972cac147869607d994173753e4a2fc232`; active pointer moved as
`311a2f0b811d55315d6eb623130cad0be1417565`) makes the centre dialogue the
invariant primary surface and seats the prompted specification ladder. Where any
earlier current-contract section or older clause in this document disagrees with
the applied row below, this section controls. Earlier sections, clauses, and
evidence remain dated compatibility history and are not deleted.

### Current responsibility

`DEL-02-04 Dialogue Toolkit, Context, and Local UI State` (UX_UI_SLICE, applied decomposition row L310):

Expose runtime options and preserve versioned layout (per-view right-panel
widths, expand state), drafts, explicit next-turn context references, artifact
anchors, selected replay references, panel state, chat annotations, known
folders, chat rung and declined proposal triggers, and local presets as
non-authoritative convenience state with rollback-safe migration; present the
one-line activity strip in place of the resizable shelf.

Applied row notes: Convenience state stores references and presentation only; it
never stores authoritative workflow, hierarchy, permission, or acceptance
conclusions; the workflow file and the session record own rung-related truth.

Applied row outputs: Toolkit controls; workspace-state schema (additive v1
fields); resize/expand/anchor behavior; activity strip; context-reference,
draft/preset, annotation, and migration guards.

### Current acceptance obligations

1. Workspace-state changes are additive v1 fields under the existing schema string with rollback-safe migration that preserves prior state.
2. Per-view right-panel widths, expand state, drafts, explicit next-turn context references, artifact anchors, selected replay references, panel state, chat annotations, known folders, chat rung, declined proposal triggers, and local presets are non-authoritative convenience state.
3. Convenience state never transfers session authority, never stands in for the governed workflow file, and visible artifacts are not automatically model context.
4. The one-line activity strip replaces the resizable shelf; the Activity view is a right-panel view.

### Seating and rulings

Remaining items seated under D-APP-108 (2026-09-04): DEL-02-04-V3-01. Ruled
questions applied here: none (Q3 and Q14 are applied by sibling carriers).
Alignment writes WI-011, WI-012, WI-013, WI-014, WI-015 performed in run
`APP_SCA_APP_010_SEATING_2026-09-04`; dependency writes DEP-005, DEP-006 were performed under D-APP-109/D-APP-110 on 2026-09-05; the extracted register now exists.
No lifecycle, Checking Approval SHA, dependency-acceptance, product, or release
act is implied.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-02-04 Dialogue Toolkit, Context, and Local UI State

> #### Datasheet: DEL-02-04 Dialogue Toolkit, Context, and Local UI State
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-02-04 |
> | DeliverableName | Dialogue Toolkit, Context, and Local UI State |
> | PackageID | PKG-02 |
> | PackageName | Woven Dialogue Shell, Navigation, and Operator State |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ResponsibleParty | TBD |
> | Type | UX_UI_SLICE |
> | ContextEnvelope | S |
> | ScopeItems | SOW-004, SOW-008, SOW-016 |
> | Objectives | OBJ-001, OBJ-004 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary UI surfaces | Navigator, primary dialogue, right-panel views and activity strip for layout behavior; composer and Settings for supported runtime options; the former Toolkit panel is historical presentation evidence. | `docs/PRD.md` Section 8.1 FR-005; Section 8.7 FR-041 |
> | Current runtime option categories | model, effort and user-selected permission policy in the composer/Settings; tools and max-turns remain concrete capability-alignment tasks against current PRD, without an invented Toolkit or persona control. | `docs/PRD.md` Section 8.7 FR-041 |
> | Runtime option fallback behavior | Use the current Codex model catalog and selected per-turn model/effort/policy with Runtime-admitted tools. The legacy max-turn fallback is compatibility evidence, not proof that Codex consumes maxTurns. | `docs/PRD.md` Section 8.4 FR-023; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-016 |
> | Unknown option behavior | Unknown option keys are ignored with warnings. | `docs/PRD.md` Section 8.4 FR-024; `docs/SPEC.md` runtime option rules, line 681 |
> | Local persistence scope | Toolkit settings, pane widths, chat drafts, attachment selections, and local presets are local convenience state. | `docs/PRD.md` Section 8.1 FR-005; Section 8.7 FR-042 and FR-043; `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |
> | Accessibility expectation | Keyboard users can resize/collapse panes; resize handles are focusable separators with arrow/Home/End behavior. | `docs/PRD.md` Section 11.4 NFR-019 |
> | UI-quality evidence | Current component/render evidence plus risk-based browser or screenshot review; checklist presence alone is not acceptance. | `docs/ui/UI_POLISH_EXECUTION_PLAN.md`; `docs/ISSUE_READINESS_PROFILES.md` Section 4 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Authority boundary | Local UI state is non-authoritative and must not override governance enforcement or project truth. | `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3; `docs/PRD.md` Section 8.7 FR-042 |
> | Professional reliance boundary | Agent outputs and UI/runtime state remain draft or decision-support material until accepted by an accountable human. | `docs/DIRECTIVE.md` Sections 2.3 and 2.4; `docs/PRD.md` Section 15 KG-015 |
> | Storage failure behavior | Storage failures for chat drafts and attachment selections warn without breaking chat. | `docs/PRD.md` Section 8.7 FR-043 |
> | Malformed local records | Malformed draft/attachment records are dropped. | `docs/PRD.md` Section 8.7 FR-043 |
> | Runtime governance | Composer-selected permission mode maps to the user-selected Codex approval/sandbox policy; no separate Toolkit mode control is required. Actual enforcement must be verified and Full access grants no normative authority. | `docs/PRD.md` Section 8.7 FR-044 |
> | PRD source status | D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment. | `_REFERENCES.md` REF-006 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component or Artifact | Required Content | Source |
> |---|---|---|
> | Toolkit controls | UI controls for per-turn runtime options supported by the runtime. Current loci are the composer and woven workspace-state/settings surfaces; unsupported legacy options remain keyed for alignment. | `docs/PRD.md` Section 8.7 FR-041 |
> | Pane state controls | Drag and keyboard resize/collapse support for Navigator, primary dialogue, right-panel views and activity strip, with locally persisted widths. | `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019 |
> | Draft and preset guards | Local persistence keyed per root/persona/mode for drafts and attachment selections; malformed records dropped; storage failures warn. | `docs/PRD.md` Section 8.7 FR-043 |
> | Governance guard | Local presets and visibility of options cannot become authoritative or override runtime governance. | `docs/PRD.md` Section 8.7 FR-042; `docs/SPEC.md` runtime UI option rule, line 431 |
> | Deterministic option handoff | Runtime option keys follow accepted fallback behavior; unknown keys warn and do not silently mutate behavior. | `docs/PRD.md` Section 8.4 FR-023 and FR-024 |
>

### CLM-006 — References

> ##### References
>
> - `docs/DIRECTIVE.md` Sections 2.3, 2.4, 2.5, 2.6, 4.2.
> - `docs/CONTRACT.md` invariants K-NOMEM-1, K-SDK-1, K-PERM-3, K-TOOL-1.
> - `docs/SPEC.md` Sections 1.2, 1.3 and runtime option rules around UI option authority and unknown keys.
> - `docs/TYPES.md` lifecycle state definitions.
> - `docs/PRD.md` Sections 8.1, 8.4, 8.7, 11.4, 15, 16.
> - `docs/ui/UI_POLISH_EXECUTION_PLAN.md` for UI-quality evidence routing.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-04, SOW-004, SOW-008, SOW-016, OBJ-001, OBJ-004.
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

The D-APP-56 2026-07-12 pane/policy observations are dated history. Current layout is Navigator, primary dialogue, right-panel views and activity strip. Composer policy selection must reach Codex enforcement. Current render/browser and option-handoff results remain required. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-02-04 Toolkit Options and Local UI State

> #### Specification: DEL-02-04 Toolkit Options and Local UI State
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable covers the UX/UI slice that exposes runtime options and preserves pane layout, chat drafts, attachment selections, and local presets as non-authoritative convenience state for the Chirality desktop shell.
>
> Included:
>
> - Toolkit controls for per-turn runtime options.
> - Local pane resize/collapse state for Navigator, primary dialogue, right-panel views and activity strip.
> - Local draft, attachment-selection, and preset persistence guards.
> - UI behavior that respects deterministic runtime option fallback and warnings.
>
> Excluded:
>
> - Runtime engine internals.
> - SDK-specific option builder implementation, except where the UI must not contradict accepted runtime option behavior.
> - API key entry/status UI, secure-storage feedback, and typed runtime error display assigned to DEL-02-05.
> - Dependency extraction; this run intentionally does not create `Dependencies.csv`.
>
> Sources: `_CONTEXT.md`; `docs/PRD.md` Sections 8.1, 8.4, 8.7; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-04.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-02-04-REQ-001 | The shell shall support resizable and collapsible Navigator, primary dialogue, right-panel views and activity strip. | `docs/PRD.md` Section 8.1 FR-005 |
> | DEL-02-04-REQ-002 | Pane resize/collapse behavior shall support drag and keyboard operation; Home collapses, End expands, and widths are persisted locally. | `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019 |
> | DEL-02-04-REQ-003 | Composer/Settings SHALL expose supported per-turn model and effort selections and faithfully show user-selected Codex policy. Tools/max-turns remain explicit capability-alignment and delivery work against the current PRD; an unsupported field must be labelled and must not silently change execution. The former Toolkit panel/persona picker is dated presentation history. | `docs/PRD.md` Section 8.7 FR-041; D-APP-56 R4-P07 |
> | DEL-02-04-REQ-004 | Toolkit settings and presets shall persist locally and remain non-authoritative. | `docs/PRD.md` Section 8.7 FR-042; `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |
> | DEL-02-04-REQ-005 | Local presets shall not override governance enforcement or project truth. | `docs/PRD.md` Section 8.7 FR-042; `docs/CONTRACT.md` K-NOMEM-1 |
> | DEL-02-04-REQ-006 | Chat drafts and attachment selections shall persist locally per root/persona/mode. | `docs/PRD.md` Section 8.7 FR-043 |
> | DEL-02-04-REQ-007 | Malformed local draft or attachment-selection records shall be dropped. | `docs/PRD.md` Section 8.7 FR-043 |
> | DEL-02-04-REQ-008 | Local storage failures shall warn without breaking chat. | `docs/PRD.md` Section 8.7 FR-043 |
> | DEL-02-04-REQ-009 | The composer shall present the user-selected Codex approval/sandbox policy for the project and turn and report actual enforcement truthfully; no separate Toolkit mode or persona-picker permission control is required. | `docs/PRD.md` Section 8.7 FR-044; D-APP-56 R4-P07 |
> | DEL-02-04-REQ-010 | A composer policy label shall not be treated as enforcement evidence or grant normative authority; verify the actual user-selected host policy and outcome. | `docs/PRD.md` Section 8.7 FR-044 |
> | DEL-02-04-REQ-011 | Per-turn options SHALL resolve deterministically against the current Codex catalog/policy and admitted application-tool contract. Unsupported legacy fields must not silently affect execution; the unknown-key warning obligation remains. | `docs/PRD.md` Section 8.4 FR-023; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-016 |
> | DEL-02-04-REQ-012 | Unknown option keys shall be ignored with warnings and shall not silently mutate behavior. | `docs/PRD.md` Section 8.4 FR-024; `docs/SPEC.md` Section 13.1 |
> | DEL-02-04-REQ-013 | UI visibility of an option shall be non-authoritative; governance and permission policy remain authoritative. | `docs/SPEC.md` Section 7.4 |
> | DEL-02-04-REQ-014 | The UI shall preserve a professional, dense-but-readable interface for the shell surfaces. | `docs/PRD.md` Section 8.1 FR-006 |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard or Source | Applicability | Status |
> |---|---|---|
> | Chirality Directive | Human authority, evidence posture, and non-authoritative convenience state. | Accessible: `docs/DIRECTIVE.md` |
> | Chirality Contract | Binding invariants for hidden memory, SDK/settings posture, permissions, and tool exposure. | Accessible: `docs/CONTRACT.md` |
> | Chirality Spec | Runtime configuration state, working-root truth, option visibility, and unknown-option behavior. | Accessible: `docs/SPEC.md` |
> | Chirality PRD | D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment. | Accessible: `_REFERENCES.md` REF-006 is reconciled and records `MATCH`. |
> | Active SOFTWARE_DECOMP v3.2 | DEL-02-04 scope, SOW coverage, objective mapping, and package boundary. | Accessible: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement IDs | Verification Approach |
> |---|---|
> | DEL-02-04-REQ-001, DEL-02-04-REQ-002 | UI tests or interaction checks for drag resizing, keyboard arrow resize if implemented, Home collapse, End expand, persistence after reload, and focusable separator semantics. |
> | DEL-02-04-REQ-003 | Current composer/Settings tests verify supported model/effort selection, truthful unavailable options and exact tools/max-turns capability alignment; historical Toolkit tests do not prove the live path. |
> | DEL-02-04-REQ-004, DEL-02-04-REQ-005, DEL-02-04-REQ-013 | Tests or review checks proving local presets do not write project truth files, do not override governance enforcement, and cannot be treated as authoritative runtime policy. |
> | DEL-02-04-REQ-006, DEL-02-04-REQ-007, DEL-02-04-REQ-008 | Local-storage tests for root/persona/mode keying, malformed-record discard, and storage-failure warning behavior. |
> | DEL-02-04-REQ-009, DEL-02-04-REQ-010 | Current composer/Runtime integration checks prove faithful display and handoff of user-selected Codex policy and actual host outcomes; labels alone do not prove enforcement. |
> | DEL-02-04-REQ-011, DEL-02-04-REQ-012 | Option-handoff tests confirming deterministic fallback display/submit behavior and warnings for unknown keys; test records must show that unknown keys are warned, ignored, and do not silently mutate runtime behavior. |
> | DEL-02-04-REQ-014 | Review against `docs/ui/UI_POLISH_EXECUTION_PLAN.md`, including D-APP-36 component/render evidence and browser or screenshot evidence where layout risk warrants it. The checklist makes verification repeatable; REQ-014 remains unproven until current evidence is recorded. |
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required artifacts for this deliverable:
>
> - Toolkit controls.
> - Pane resize/collapse state behavior.
> - Draft and preset storage guards.
> - Tests or verification notes for local-state non-authority and option fallback behavior.
> - Current policy-mode integration evidence for the user-selected Codex policy; missing verification stays explicit.
> - Policy-mode acceptance evidence for the current Codex policy, including its enum/contract source, composer mode-to-policy mapping, and evidence that controls are enforced by runtime policy rather than prompt text alone.
> - Option-handoff evidence for deterministic fallback and unknown-key handling, including the submitted option payload, warning behavior, and unchanged runtime behavior for ignored keys.
>

### CLM-014 — Assumptions and TBDs

Current UI option/state loci are the composer, woven workspace-state and settings surfaces. Model/effort/permission/interaction controls are present as source evidence; legacy tools/max-turns/governance metadata/presets and the unproduced artifact/rung fields remain exact alignment or delivery work. Preset retention duration is the unresolved policy choice; do not invent it. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-015 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

The D-APP-56 2026-07-12 pane/policy observations are dated history. Current layout is Navigator, primary dialogue, right-panel views and activity strip. Composer policy selection must reach Codex enforcement. Current render/browser and option-handoff results remain required. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

- **AC-001** — The Scope of Work preserves and traces all legacy source content to SOW-004, SOW-008, SOW-016, OBJ-001, and OBJ-004 without adding scope, reliance claims, lifecycle meaning, or obligations.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-02-04 Toolkit Options and Local UI State

> #### Procedure: DEL-02-04 Toolkit Options and Local UI State
>

### CLM-017 — Purpose

> ##### Purpose
>
> Define the operational steps to produce and verify the Toolkit Options and Local UI State UX/UI slice while preserving the non-authoritative status of local UI convenience state.
>

### CLM-018 — Prerequisites

Dependency extraction ran under D-APP-109/D-APP-110 on 2026-09-05. `Dependencies.csv` is the formal extracted register; consult each edge and gate directly. This record repair neither changes an edge nor infers satisfaction from implementation. Read current per-chat/local-state ownership and Codex option/policy boundary. Preserve stored-state validation and authority separation. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

### CLM-019 — Steps

1. Verify current pane resize/collapse, keyboard/focus behavior and local persistence.
2. Verify composer model/effort/permission/interaction selections reach current Runtime/Codex policy.
3. Verify malformed records drop and storage failures warn without breaking chat.
4. Prove local drafts, attachments, annotations and presets do not become project truth or override authority.
5. Check deterministic option handoff and unknown-key warn/ignore behavior on the live path; record missing controls/fields and producer dependencies explicitly.
6. Record D-APP-36 render/browser and source-bound integration results. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-020 — Verification

Verify current pane keyboard/drag and persistence behavior, malformed-record/drop and warning handling, policy enforcement and deterministic option handoff. The unknown-key warn/ignore check, supported legacy-option alignment, artifact/rung field producers and current polish review remain open where not evidenced. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-021 — Records

Existing evidence hooks include `frontend/src/__tests__/lib/woven-workspace-state.test.ts`, composer model/folder tests and woven controls tests. Preserve actual result/source identities. Missing live policy-mode and unknown-key results remain missing; no test-file presence supplies acceptance or VER-001 conversion evidence.

- **VER-001** — Run deterministic schema validation, source mapping, parity, checklist derivation, and render stability checks, followed by human review against the accepted legacy basis.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-02-04 Toolkit Options and Local UI State

> #### Guidance: DEL-02-04 Toolkit Options and Local UI State
>

### CLM-023 — Purpose

> ##### Purpose
>
> DEL-02-04 exists to make runtime options and local operator conveniences visible and usable without turning those conveniences into project truth. The slice supports OBJ-001 by preserving clear desktop-shell operator behavior and supports OBJ-004 where Toolkit options touch deterministic runtime option handling.
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-04, OBJ-001, OBJ-004; `docs/PRD.md` Sections 8.1, 8.4, 8.7.
>

### CLM-024 — Principles

> ##### Principles
>
> 1. Treat local state as convenience, not authority.
>    UI drafts, local presets, pane widths, SDK transcripts, API keys, runtime logs, and caches are non-authoritative unless governed project files import relevant content. Sources: `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3.
>
> 2. Keep governance stronger than UI choice.
>    Toolkit settings and visible options may help the operator express intent, but they cannot override governance enforcement, permission policy, or project truth. Sources: `docs/PRD.md` Section 8.7 FR-042; `docs/SPEC.md` Section 7.4.
>
> 3. Prefer explicit warnings over silent behavior changes.
>    Unknown option keys should warn and be ignored instead of mutating behavior. Storage failures should warn without breaking chat. Sources: `docs/PRD.md` Section 8.4 FR-024; Section 8.7 FR-043.
>
> 4. Preserve drafts for operator continuity, not approval.
>    Draft and attachment-selection persistence improves recovery and retry behavior, but it does not approve work or create project truth. Sources: `docs/DIRECTIVE.md` Sections 2.3, 2.4, 2.6; `docs/PRD.md` Section 8.7 FR-043.
>
> 5. Make pane controls accessible.
>    Resize/collapse affordances should be usable by keyboard users through focusable separators and keyboard behavior. Sources: `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019.
>

### CLM-025 — Considerations

D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment. Supported current Codex controls and local convenience state are the live subject. UI labels alone do not prove enforcement; retain missing integration/browser and option-warning results.

### CLM-026 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance | Source |
> |---|---|---|
> | Convenience persistence vs. project truth | Persist pane widths, drafts, and presets locally, but never write them as authoritative deliverable state unless a governed import occurs. | `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |
> | Rich Toolkit controls vs. runtime authority | Surface options that improve operator control, but let runtime fallback, validation, and permission policy remain authoritative. | `docs/PRD.md` Section 8.4 FR-023 and FR-024; Section 8.7 FR-042 and FR-044 |
> | Strict local parsing vs. operator continuity | Drop malformed local records and warn on storage failures, but avoid breaking chat when local persistence fails. | `docs/PRD.md` Section 8.7 FR-043 |
> | Keyboard support vs. compact shell layout | Keep resize/collapse controls accessible even in a dense desktop shell. | `docs/PRD.md` Section 11.4 NFR-019 |
>

### CLM-027 — Examples

> ##### Examples
>
> - Supported example: a user selects a supported model and effort in the composer. The live Codex catalog and policy determine admitted behavior. Tools/max-turns require separate capability alignment before a current control or handoff is claimed. Source: `docs/PRD.md` Section 8.4 FR-023; Section 8.7 FR-041.
> - Supported example: a malformed local draft record is encountered. The UI drops the malformed record and continues with a warning if needed. Source: `docs/PRD.md` Section 8.7 FR-043.
> - Supported example: pane widths persist locally after keyboard resize. Source: `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019.
> - Unsupported as project truth: a local Toolkit preset that attempts to bypass governance or override permission policy. Source: `docs/PRD.md` Section 8.7 FR-042; `docs/SPEC.md` Section 7.4.
>

### CLM-028 — Resolved source-state note

D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

### CLM-029 — Rulings Needed

Preset retention duration remains an unresolved choice if presets are retained. Current policy ownership and four-role applicability are settled by D-GOV-43 and current App guidance; do not reopen those as old Toolkit choices. Exact missing controls and producer fields remain source-alignment/delivery tasks, not invented scope retirement.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-004 SOW-008 SOW-016 OBJ-001 OBJ-004 | SCA-APP-010 Gate-5 Current Contract; CLM-008 | AC-001 | VER-001 | Workspace-state migration, primary/replay isolation, explicit-context, focus/keyboard, rollback, and storage-guard evidence |
