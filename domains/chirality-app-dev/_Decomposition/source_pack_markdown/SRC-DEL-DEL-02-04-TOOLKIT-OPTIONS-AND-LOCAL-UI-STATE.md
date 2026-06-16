# Source Pack: SRC-DEL-DEL-02-04-TOOLKIT-OPTIONS-AND-LOCAL-UI-STATE

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Datasheet.md

### Datasheet: DEL-02-04 Toolkit Options and Local UI State

#### Identification

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

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary UI surfaces | File Tree, Toolkit, and Chat panes for layout behavior; Toolkit panel for runtime options. | `docs/PRD.md` Section 8.1 FR-005; Section 8.7 FR-041 |
| Runtime option categories exposed by Toolkit | model, tools, max turns, mode, persona, governance metadata as supported by runtime. | `docs/PRD.md` Section 8.7 FR-041 |
| Runtime option fallback behavior | Model, tools, and max-turn options follow deterministic fallback chains. | `docs/PRD.md` Section 8.4 FR-023; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-016 |
| Unknown option behavior | Unknown option keys are ignored with warnings. | `docs/PRD.md` Section 8.4 FR-024; `docs/SPEC.md` runtime option rules, line 681 |
| Local persistence scope | Toolkit settings, pane widths, chat drafts, attachment selections, and local presets are local convenience state. | `docs/PRD.md` Section 8.1 FR-005; Section 8.7 FR-042 and FR-043; `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |
| Accessibility expectation | Keyboard users can resize/collapse panes; resize handles are focusable separators with arrow/Home/End behavior. | `docs/PRD.md` Section 11.4 NFR-019 |

#### Conditions

| Condition | Value | Source |
|---|---|---|
| Authority boundary | Local UI state is non-authoritative and must not override governance enforcement or project truth. | `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3; `docs/PRD.md` Section 8.7 FR-042 |
| Professional reliance boundary | Agent outputs and UI/runtime state remain draft or decision-support material until accepted by an accountable human. | `docs/DIRECTIVE.md` Sections 2.3 and 2.4; `docs/PRD.md` Section 15 KG-015 |
| Storage failure behavior | Storage failures for chat drafts and attachment selections warn without breaking chat. | `docs/PRD.md` Section 8.7 FR-043 |
| Malformed local records | Malformed draft/attachment records are dropped. | `docs/PRD.md` Section 8.7 FR-043 |
| Runtime governance | Toolkit mode controls must map to permission policy modes once the policy engine exists. | `docs/PRD.md` Section 8.7 FR-044 |
| PRD source status | Source usable with warning: `_REFERENCES.md` reports expected PRD SHA `86cb6f...` and observed SHA `fb1c73...`. | `_REFERENCES.md` REF-006 |

#### Construction

| Component or Artifact | Required Content | Source |
|---|---|---|
| Toolkit controls | UI controls for per-turn runtime options supported by the runtime. Exact component names and implementation files are TBD. | `docs/PRD.md` Section 8.7 FR-041 |
| Pane state controls | Drag and keyboard resize/collapse support for File Tree, Toolkit, and Chat panes, with locally persisted widths. | `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019 |
| Draft and preset guards | Local persistence keyed per root/persona/mode for drafts and attachment selections; malformed records dropped; storage failures warn. | `docs/PRD.md` Section 8.7 FR-043 |
| Governance guard | Local presets and visibility of options cannot become authoritative or override runtime governance. | `docs/PRD.md` Section 8.7 FR-042; `docs/SPEC.md` runtime UI option rule, line 431 |
| Deterministic option handoff | Runtime option keys follow accepted fallback behavior; unknown keys warn and do not silently mutate behavior. | `docs/PRD.md` Section 8.4 FR-023 and FR-024 |

#### References

- `docs/DIRECTIVE.md` Sections 2.3, 2.4, 2.5, 2.6, 4.2.
- `docs/CONTRACT.md` invariants K-NOMEM-1, K-SDK-1, K-PERM-3, K-TOOL-1.
- `docs/SPEC.md` Sections 1.2, 1.3 and runtime option rules around UI option authority and unknown keys.
- `docs/TYPES.md` lifecycle state definitions.
- `docs/PRD.md` Sections 8.1, 8.4, 8.7, 11.4, 15, 16.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-04, SOW-004, SOW-008, SOW-016, OBJ-001, OBJ-004.

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Guidance.md

### Guidance: DEL-02-04 Toolkit Options and Local UI State

#### Purpose

DEL-02-04 exists to make runtime options and local operator conveniences visible and usable without turning those conveniences into project truth. The slice supports OBJ-001 by preserving clear desktop-shell operator behavior and supports OBJ-004 where Toolkit options touch deterministic runtime option handling.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-04, OBJ-001, OBJ-004; `docs/PRD.md` Sections 8.1, 8.4, 8.7.

#### Principles

1. Treat local state as convenience, not authority.
   UI drafts, local presets, pane widths, SDK transcripts, API keys, runtime logs, and caches are non-authoritative unless governed project files import relevant content. Sources: `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3.

2. Keep governance stronger than UI choice.
   Toolkit settings and visible options may help the operator express intent, but they cannot override governance enforcement, permission policy, or project truth. Sources: `docs/PRD.md` Section 8.7 FR-042; `docs/SPEC.md` Section 7.4.

3. Prefer explicit warnings over silent behavior changes.
   Unknown option keys should warn and be ignored instead of mutating behavior. Storage failures should warn without breaking chat. Sources: `docs/PRD.md` Section 8.4 FR-024; Section 8.7 FR-043.

4. Preserve drafts for operator continuity, not approval.
   Draft and attachment-selection persistence improves recovery and retry behavior, but it does not approve work or create project truth. Sources: `docs/DIRECTIVE.md` Sections 2.3, 2.4, 2.6; `docs/PRD.md` Section 8.7 FR-043.

5. Make pane controls accessible.
   Resize/collapse affordances should be usable by keyboard users through focusable separators and keyboard behavior. Sources: `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019.

#### Considerations

- Runtime option controls should distinguish "operator selected," "runtime defaulted," and "governance enforced" states where the source model supports that distinction. Exact UI copy and state model are TBD.
- Local storage should degrade gracefully. A blocked quota, private-window limitation, or parse error should not make chat unusable; malformed records should be dropped and failures should warn. Source: `docs/PRD.md` Section 8.7 FR-043.
- The Toolkit should not imply that SDK or permission modes are prompt hints only. PRD FR-044 requires runtime enforcement once the permission policy engine exists.
- The PRD source is accessible but hash-mismatched against `_REFERENCES.md`; use it as directed by this task with warning, and avoid over-claiming details not present in the accessible text.
- PRD FR-006 points to `docs/ui/UI_POLISH_EXECUTION_PLAN.md` for polish acceptance, but that file was not accessible in the source tree during this P3 run. Treat dense, professional interface review as required with checklist location TBD rather than substituting an invented rubric.

#### Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Convenience persistence vs. project truth | Persist pane widths, drafts, and presets locally, but never write them as authoritative deliverable state unless a governed import occurs. | `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |
| Rich Toolkit controls vs. runtime authority | Surface options that improve operator control, but let runtime fallback, validation, and permission policy remain authoritative. | `docs/PRD.md` Section 8.4 FR-023 and FR-024; Section 8.7 FR-042 and FR-044 |
| Strict local parsing vs. operator continuity | Drop malformed local records and warn on storage failures, but avoid breaking chat when local persistence fails. | `docs/PRD.md` Section 8.7 FR-043 |
| Keyboard support vs. compact shell layout | Keep resize/collapse controls accessible even in a dense desktop shell. | `docs/PRD.md` Section 11.4 NFR-019 |

#### Examples

- Supported example: a user adjusts Toolkit max turns for one turn. The UI may submit that option, but runtime fallback and policy decide final behavior. Source: `docs/PRD.md` Section 8.4 FR-023; Section 8.7 FR-041.
- Supported example: a malformed local draft record is encountered. The UI drops the malformed record and continues with a warning if needed. Source: `docs/PRD.md` Section 8.7 FR-043.
- Supported example: pane widths persist locally after keyboard resize. Source: `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019.
- Unsupported as project truth: a local Toolkit preset that attempts to bypass governance or override permission policy. Source: `docs/PRD.md` Section 8.7 FR-042; `docs/SPEC.md` Section 7.4.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-001 | `_REFERENCES.md` records a PRD SHA mismatch while the task instructs that the mismatch is a warning, not a blocker. | `_REFERENCES.md` REF-006 | Dispatch instruction for this TASK run | All sections citing `docs/PRD.md` | Use accessible PRD text with warning for this run; require later source-hash reconciliation before closure. Closure artifact and accountable resolver are TBD. | TBD |

#### Rulings Needed

- Human ruling needed on PRD hash reconciliation before final package closure, because `_REFERENCES.md` expected and actual PRD hashes differ.
- Human ruling needed to name the accountable resolver and closure artifact for the PRD hash mismatch, such as an accepted reference refresh, source-snapshot ruling, or decomposition/package closure note.
- Human ruling needed if local presets should have a specific retention duration, storage namespace, or migration policy; no accessible source defines those details.
- Human ruling or downstream source needed for the missing UI polish checklist path referenced by PRD FR-006.

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Procedure.md

### Procedure: DEL-02-04 Toolkit Options and Local UI State

#### Purpose

Define the operational steps to produce and verify the Toolkit Options and Local UI State UX/UI slice while preserving the non-authoritative status of local UI convenience state.

#### Prerequisites

- Accepted source basis available locally:
  - `docs/DIRECTIVE.md`
  - `docs/CONTRACT.md`
  - `docs/SPEC.md`
  - `docs/TYPES.md`
  - `docs/PLAN.md`
  - `docs/PRD.md` with hash mismatch warning from `_REFERENCES.md`
  - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- Declared upstream dependencies: `_DEPENDENCIES.md` reports no accepted human-declared upstream dependency edges outside the extracted register. The extracted register is present and lists active source prerequisites plus `DEP-02-04-014` for TBD adjacent runtime option contracts and permission policy integration points.
- Runtime option contracts and permission policy integration points available from adjacent deliverables: TBD per `DEP-02-04-014`.
- ResponsibleParty: TBD.

#### Steps

1. Confirm scope boundaries.
   - Include Toolkit controls, pane resize/collapse state, local draft/preset guards, and UI handling of runtime option fallback.
   - Exclude runtime engine internals and DEL-02-05 API key/error-feedback UI.
   - Sources: `_CONTEXT.md`; `docs/PRD.md` Sections 8.1, 8.4, 8.7.

2. Implement or review pane resize/collapse behavior.
   - Provide File Tree, Toolkit, and Chat pane resize/collapse affordances.
   - Support drag behavior and keyboard behavior, including Home collapse and End expand.
   - Persist widths locally.
   - Sources: `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019.

3. Implement or review Toolkit per-turn option controls.
   - Expose model, tools, max turns, mode, persona, and governance metadata only as supported by runtime.
   - Treat exact component structure and labels as TBD until implementation files are selected.
   - Record the runtime-supported option inventory used by the UI, or explicitly mark unavailable controls as TBD/disabled.
   - Source: `docs/PRD.md` Section 8.7 FR-041.

4. Align Toolkit option handoff with deterministic runtime behavior.
   - Confirm model, tools, and max-turn fallback chains remain deterministic.
   - Confirm unknown option keys warn and are ignored.
   - Preserve test evidence that unknown keys do not silently mutate runtime behavior.
   - Sources: `docs/PRD.md` Section 8.4 FR-023 and FR-024; `docs/SPEC.md` Section 13.1.

5. Guard local presets and Toolkit settings.
   - Persist settings locally only as non-authoritative convenience state.
   - Confirm local presets cannot override governance enforcement or project truth.
   - Sources: `docs/PRD.md` Section 8.7 FR-042; `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3.

6. Guard drafts and attachment selections.
   - Persist chat drafts and attachment selections locally per root/persona/mode.
   - Drop malformed records.
   - Warn on storage failures without breaking chat.
   - Source: `docs/PRD.md` Section 8.7 FR-043.

7. Prepare permission-mode integration without overclaiming.
   - Map Toolkit mode controls to permission policy modes once the policy engine exists.
   - Mark enforcement as TBD until the policy engine and accepted enums/contracts are available.
   - Source: `docs/PRD.md` Section 8.7 FR-044.

8. Check professional and project-truth boundaries.
   - Confirm UI copy, tests, and implementation do not imply local state, presets, drafts, or agent outputs are approved project truth.
   - Sources: `docs/DIRECTIVE.md` Sections 2.3, 2.4, 2.6; `docs/PRD.md` Section 15 KG-015.

#### Verification

| Check | Expected Result |
|---|---|
| Pane drag resize | File Tree, Toolkit, and Chat panes resize without layout breakage. |
| Pane keyboard resize/collapse | Resize handles are focusable; keyboard resize works where implemented; Home collapses; End expands. |
| Pane state persistence | Width/collapse state persists locally and remains non-authoritative. |
| Toolkit option controls | UI exposes only supported per-turn options or marks unsupported items as unavailable/TBD. |
| Deterministic option handoff | Runtime receives supported options; fallback behavior remains deterministic; unknown keys warn and are ignored. |
| Local preset authority | Presets do not write project truth and cannot override governance enforcement. |
| Draft/attachment local persistence | Records are keyed per root/persona/mode; malformed records are dropped; storage failures warn without breaking chat. |
| Permission-mode controls | If policy engine exists, controls map to enforced modes; if not, enforcement remains clearly TBD. |

#### Records

- Toolkit controls implementation or review notes: TBD.
- Pane resize/collapse implementation or review notes: TBD.
- Draft/preset storage guard tests: TBD.
- Runtime option handoff tests, including unknown-key warning/ignore evidence: TBD.
- Accessibility checks for keyboard resize/collapse: TBD.
- Local-state non-authority tests for presets, drafts, attachment selections, fallback behavior, accessibility, and storage guards: TBD.
- Policy-mode mapping evidence after the permission policy engine exists: TBD.
- Human ruling on PRD hash mismatch reconciliation: TBD.

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Specification.md

### Specification: DEL-02-04 Toolkit Options and Local UI State

#### Scope

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

#### Requirements

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

#### Standards

| Standard or Source | Applicability | Status |
|---|---|---|
| Chirality Directive | Human authority, evidence posture, and non-authoritative convenience state. | Accessible: `docs/DIRECTIVE.md` |
| Chirality Contract | Binding invariants for hidden memory, SDK/settings posture, permissions, and tool exposure. | Accessible: `docs/CONTRACT.md` |
| Chirality Spec | Runtime configuration state, working-root truth, option visibility, and unknown-option behavior. | Accessible: `docs/SPEC.md` |
| Chirality PRD | Product requirements for desktop shell, runtime options, Toolkit, and local UI state. | Accessible with source warning: hash mismatch recorded in `_REFERENCES.md` REF-006 |
| Active SOFTWARE_DECOMP v3.2 | DEL-02-04 scope, SOW coverage, objective mapping, and package boundary. | Accessible: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |

#### Verification

| Requirement IDs | Verification Approach |
|---|---|
| DEL-02-04-REQ-001, DEL-02-04-REQ-002 | UI tests or interaction checks for drag resizing, keyboard arrow resize if implemented, Home collapse, End expand, persistence after reload, and focusable separator semantics. |
| DEL-02-04-REQ-003 | Component or integration tests confirming the Toolkit can set only supported runtime options and labels unsupported/unavailable options without inventing behavior. |
| DEL-02-04-REQ-004, DEL-02-04-REQ-005, DEL-02-04-REQ-013 | Tests or review checks proving local presets do not write project truth files, do not override governance enforcement, and cannot be treated as authoritative runtime policy. |
| DEL-02-04-REQ-006, DEL-02-04-REQ-007, DEL-02-04-REQ-008 | Local-storage tests for root/persona/mode keying, malformed-record discard, and storage-failure warning behavior. |
| DEL-02-04-REQ-009, DEL-02-04-REQ-010 | Policy-mode integration tests once the permission policy engine exists; until then, mark enforcement wiring as TBD and avoid false claims. |
| DEL-02-04-REQ-011, DEL-02-04-REQ-012 | Option-handoff tests confirming deterministic fallback display/submit behavior and warnings for unknown keys; test records must show that unknown keys are warned, ignored, and do not silently mutate runtime behavior. |
| DEL-02-04-REQ-014 | UI review against the accepted polish plan referenced by PRD FR-006. The referenced path `docs/ui/UI_POLISH_EXECUTION_PLAN.md` is not present in the accessible source tree for this run, so the exact checklist location remains TBD. |

#### Documentation

Required artifacts for this deliverable:

- Toolkit controls.
- Pane resize/collapse state behavior.
- Draft and preset storage guards.
- Tests or verification notes for local-state non-authority and option fallback behavior.
- Any unresolved policy-mode wiring notes marked `TBD` until the permission policy engine exists.
- Policy-mode acceptance evidence after the permission policy engine exists, including the accepted enum/contract source, Toolkit mode-to-policy mapping, and evidence that controls are enforced by runtime policy rather than prompt text alone.
- Option-handoff evidence for deterministic fallback and unknown-key handling, including the submitted option payload, warning behavior, and unchanged runtime behavior for ignored keys.

#### Assumptions and TBDs

- ASSUMPTION: UI implementation will key local draft and attachment-selection persistence by normalized root/persona/mode, matching PRD FR-043. Exact local storage namespace, key format, value schema, migration behavior, and retention policy are TBD.
- ASSUMPTION: Toolkit controls will present only runtime-supported option fields or clearly disabled/unavailable fields. Exact runtime-supported control inventory is TBD; current source support names model, tools, max turns, mode, persona, and governance metadata as candidate option categories.
- TBD: Exact file/component names for Toolkit controls and pane state implementation.
- TBD: Exact permission policy mode enum and enforcement integration until the policy engine is accepted.
