# Source Pack: SRC-DEL-DEL-02-05-API-KEY-UI-AND-RUNTIME-FEEDBACK

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Datasheet.md

### Datasheet: DEL-02-05 API Key UI and Runtime Feedback

#### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-02-05 |
| DeliverableName | API Key UI and Runtime Feedback |
| PackageID | PKG-02 |
| PackageName | Desktop Shell, Navigation, and Operator State |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ContextEnvelope | S |

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary UI surfaces | API key settings panel; typed error display; secure-storage error UI | `_CONTEXT.md` Deliverable Scope and Anticipated Artifacts; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-05 row |
| Scope items covered | SOW-013 typed runtime errors; SOW-019 API key storage and resolution | `_CONTEXT.md` Traceability; decomposition SOW ledger |
| Objective support | OBJ-001 and OBJ-008 | `_CONTEXT.md` Traceability; decomposition objectives table |
| Key status values | `ui`, `env`, `none` | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
| API key precedence | UI safeStorage key, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY` | `docs/PRD.md` FR-030; `docs/SPEC.md` Section 12.3 |
| Browser-facing turn error event | `turn:error` | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |
| Terminal stream event | `process:exit` | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |

#### Conditions

| Condition | Value | Source |
|---|---|---|
| API key material must remain outside project truth | Required | `docs/CONTRACT.md` K-KEY-1; `docs/SPEC.md` Section 16.2; `docs/PRD.md` NFR-002 |
| Secure key storage location | `app.getPath('userData')/credentials/api-key.enc` | `docs/SPEC.md` Section 16.2 |
| Secure-storage mechanism | Electron `safeStorage` | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
| Runtime errors preserve retry context | Required for drafts and attachments | `docs/PRD.md` Section 7.3 and FR-020; decomposition SOW-013 |
| Runtime event/log redaction | API keys and configured secrets must be redacted | `docs/PRD.md` FR-075 and NFR-002; `docs/CONTRACT.md` K-EVENT-6 |
| PRD source integrity | PRD hash mismatch observed; use as source warning, not blocker per dispatch instruction | `_REFERENCES.md` REF-006; dispatch override |

#### Construction

| Component | Construction Notes | Source |
|---|---|---|
| API key settings panel | Must allow user key storage through Electron IPC and expose key source/status without exposing key material. Specific component path is TBD. | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
| Secure-storage feedback | Must report secure-storage unavailability as a user-visible error. Exact copy and visual treatment are TBD. | `docs/PRD.md` Section 7.7 |
| Typed runtime error display | Must map harness errors to title, message, and next-step text. Exact error taxonomy and component path are TBD for this UI slice. | `docs/PRD.md` FR-020; decomposition SOW-013 |
| Retry-preserving failure state | Must preserve drafts and attachments after runtime errors so the user can retry. Exact local state owner and final evidence path are TBD. | `docs/PRD.md` FR-020; decomposition SOW-013 and SOW-023 |
| SSE compatibility | UI behavior must preserve existing browser-facing SSE event names during runtime changes. | `docs/SPEC.md` Section 11; decomposition acceptance checklist |

#### References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `docs/CONTRACT.md`
- `docs/DIRECTIVE.md`
- `docs/PLAN.md`
- `docs/PRD.md` (**source warning:** hash mismatch recorded in `_REFERENCES.md`)
- `docs/SPEC.md`
- `docs/TYPES.md`

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Guidance.md

### Guidance: DEL-02-05 API Key UI and Runtime Feedback

#### Purpose

This deliverable gives operators a clear UI for API key status and runtime failure recovery while preserving Chirality's governance boundary: key material and runtime convenience state are useful for operation, but they are not project truth.

Sources: `_CONTEXT.md`; decomposition DEL-02-05 row; `docs/DIRECTIVE.md` Project Truth sections; `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` Sections 7.3 and 7.7.

#### Principles

- Keep key material invisible. The UI may show whether a key comes from `ui`, `env`, or `none`, but must not display, log, or persist the key value. Sources: `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2.
- Separate user-facing feedback from runtime authority. UI messages can help the operator recover, but runtime policy remains in the engine/provider/session layers. Sources: `_CONTEXT.md` Exclusions; `docs/SPEC.md` Section 10 and Section 11.
- Preserve retry context. Runtime errors should not destroy draft prompt text or attachment state needed for retry. Sources: `docs/PRD.md` Section 7.3 and FR-020.
- Use stable browser-facing events. UI handling should consume the established SSE names, including `turn:error` and `process:exit`, instead of exposing SDK-specific message semantics. Sources: `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4.
- Treat the PRD hash mismatch as a source warning. Use PRD content conservatively and prefer corroborated SPEC/CONTRACT/TYPES statements for binding implementation detail. Source: `_REFERENCES.md` REF-006 and dispatch instruction.

#### Considerations

- The API key UI is a presentation/control surface. Actual key storage, provider handoff, redaction, and network policy belong to adjacent runtime/security deliverables.
- Secure-storage unavailability needs a clear visible error because the PRD acceptance criteria explicitly require it, but the exact wording is not specified in the accessible source corpus.
- Typed runtime error copy should be actionable without leaking secret-bearing provider detail.
- The UI can show status and next steps, but should avoid language that suggests the app has approved, certified, or externally validated work.
- Retry preservation should account for both draft text and attachments; attachment server validation remains outside this deliverable.

#### Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Detail vs. secrecy in key/error feedback | Prefer source/status and next-step text over raw provider details or key fragments. | `docs/CONTRACT.md` K-KEY-1 and K-EVENT-6 |
| UI convenience vs. project truth | Store only non-authoritative UI convenience state; never write API key material into project files. | `docs/DIRECTIVE.md`; `docs/TYPES.md` Section 1.7 |
| Error specificity vs. taxonomy ownership | Show typed actionable UI states, but do not invent canonical runtime error enums in this deliverable. | `_CONTEXT.md` Exclusions; decomposition package boundaries |
| Backward compatibility vs. runtime refactor | Preserve browser-facing SSE names while runtime internals move behind `TurnEngine`. | `docs/SPEC.md` Section 11; `docs/PRD.md` FR-071 |

#### Examples

TBD: The accessible source corpus defines required status values and behavior, but does not provide approved UI copy examples, component names, screenshots, or visual states.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT001 | PRD source hash differs from expected scaffold hash, but dispatch says to treat mismatch as warning, not blocker. | `_REFERENCES.md` REF-006 | Dispatch instruction for this TASK run | All PRD-cited requirements | Use PRD only with warning; prefer corroborated SPEC/CONTRACT/TYPES for implementation detail. | TBD |
| CT002 | Deliverable covers API key UI/status, but SOW-019 primary package is PKG-09 with related implementation deliverables DEL-04-05 and DEL-09-06. | Decomposition DEL-02-05 row | Decomposition SOW ledger for SOW-019 | Specification scope and verification ownership | Treat DEL-02-05 as UI feedback surface only; leave storage/resolution/security enforcement to adjacent deliverables. | TBD |

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Procedure.md

### Procedure: DEL-02-05 API Key UI and Runtime Feedback

#### Purpose

Define the working procedure to produce and verify the API key UI and runtime feedback slice for DEL-02-05 without expanding into runtime engine internals or dependency extraction.

#### Prerequisites

- Accepted deliverable context in `_CONTEXT.md`.
- Source corpus listed in `_REFERENCES.md`.
- Current `_STATUS.md` state permits work.
- Runtime/API contracts for key status, typed errors, and SSE events are available or mocked for UI work.
- Declared upstream dependencies: TBD - no accepted dependency edges have been extracted yet (`_DEPENDENCIES.md`).

#### Steps

1. Confirm the UI scope.
   - Verify that work remains limited to API key settings/status UI, secure-storage feedback, typed runtime error presentation, and retry-preserving failure states.
   - Source: `_CONTEXT.md`; decomposition DEL-02-05 row.

2. Define the key status UI contract.
   - Display key status/source as `ui`, `env`, or `none`.
   - Do not display key material.
   - Reflect precedence: UI safeStorage, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`.
   - Sources: `docs/PRD.md` Section 7.7 and FR-030; `docs/SPEC.md` Sections 12.3 and 16.2.

3. Implement secure-storage feedback.
   - Route key storage through Electron IPC and safeStorage-capable runtime surfaces.
   - Show a user-visible error when secure storage is unavailable.
   - Keep exact copy as TBD until product copy is approved.
   - Sources: `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2.

4. Implement typed runtime error display.
   - Map typed runtime/provider errors to title, message, and next-step text.
   - Redact or avoid raw provider detail that may contain secrets.
   - ASSUMPTION: consume taxonomy from runtime/provider layers rather than defining it here.
   - Sources: `docs/PRD.md` FR-020 and FR-075; `docs/CONTRACT.md` K-EVENT-6.

5. Preserve retry state after failure.
   - Keep draft prompt text and attachment metadata available after runtime errors.
   - Do not make draft or attachment UI state authoritative project truth.
   - Sources: `docs/PRD.md` Section 7.3 and FR-020; `docs/DIRECTIVE.md` Project Truth sections.

6. Preserve event compatibility.
   - Handle existing browser-facing SSE events, including `turn:error` and `process:exit`.
   - Do not expose SDK-specific message names as the browser UI contract.
   - Sources: `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4.

7. Check project-truth and secret boundaries.
   - Verify no key material is written to working-root files, runtime event payloads, logs, or tool artifacts.
   - Verify UI state remains non-authoritative convenience state.
   - Sources: `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` NFR-002; `docs/TYPES.md` Section 1.7.

#### Verification

| Check | Expected Result |
|---|---|
| Four-document traceability | Datasheet, Specification, Guidance, and Procedure cite the same source-backed status values, precedence order, and retry requirements. |
| Key status UI | Tests or review cover `ui`, `env`, and `none`; key value never appears. |
| SafeStorage unavailable | Mocked unavailable secure storage produces visible error feedback. |
| Runtime error UI | Representative typed errors map to title/message/next-step text and preserve retry context. |
| Retry state | Draft and attachment state remain available after a runtime error. |
| SSE compatibility | `turn:error` and `process:exit` remain accepted browser-facing event names. |
| Secret hygiene | Redaction checks confirm no API keys in project files, logs, runtime events, or UI error details. |

#### Records

- API key settings panel implementation and tests.
- Typed error display implementation and tests.
- Secure-storage error UI implementation and tests.
- Evidence that key material is not written to working root, logs, runtime events, or tool artifacts.
- Human rulings for `Guidance.md` Conflict Table entries CT001 and CT002.

##### Evidence Binding Table

| Evidence Need | Required Record | Current Binding |
|---|---|---|
| API key settings surface | Component/module path and test path for the settings panel that routes key storage through Electron IPC. | TBD - implementation path not yet accepted. |
| Key source/status and precedence | Test or review evidence covering `ui`, `env`, `none`, and precedence order. | TBD - final fixture or command not yet accepted. |
| Secure-storage unavailable feedback | Test or review evidence proving unavailable safeStorage produces visible error feedback. | TBD - final fixture or command not yet accepted. |
| Typed runtime error mapping | Test or review evidence mapping representative typed errors to title, message, and next-step fields. | TBD - runtime/provider taxonomy owner not yet accepted. |
| Retry preservation | Test or review evidence proving draft prompt text and attachment metadata remain available after runtime error. | TBD - exact retry state owner not yet accepted. |
| SSE compatibility | Test or review evidence proving `turn:error` and `process:exit` remain browser-facing event names. | TBD - final compatibility fixture not yet accepted. |
| Secret hygiene and project-truth boundary | Static, unit, integration, or review evidence proving key material, logs, drafts, transcripts, and UI state do not become project truth. | TBD - final evidence paths or commands not yet accepted. |

## Component: execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Specification.md

### Specification: DEL-02-05 API Key UI and Runtime Feedback

#### Scope

This deliverable covers the user-facing UI slice for API key entry/status, secure-storage feedback, typed runtime errors, and retry-preserving failure states in PKG-02.

In scope:

- API key settings/status UI for UI safeStorage and environment fallback state.
- User-visible secure-storage error feedback.
- Typed runtime error presentation with actionable title/message/next-step content.
- UI state preservation needed to retry after runtime failure.
- Browser-facing event compatibility where this UI consumes turn stream outcomes.

Out of scope:

- Runtime engine internals.
- Provider wrapper implementation.
- Redaction helper implementation.
- Network allowlist enforcement.
- Dependency extraction and `Dependencies.csv` creation.

Sources: `_CONTEXT.md` Deliverable Scope; decomposition DEL-02-05 row; `docs/PRD.md` Sections 7.3 and 7.7; `docs/SPEC.md` Sections 11, 12.3, and 16.2.

#### Requirements

| ID | Requirement | Priority | Source |
|---|---|---:|---|
| DEL-02-05-R01 | The UI must provide an API key settings surface that allows key storage through Electron IPC without writing key material to the working root. | P0 | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
| DEL-02-05-R02 | The UI must display API key source/status as one of `ui`, `env`, or `none` without displaying key material. | P0 | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
| DEL-02-05-R03 | The UI must reflect API key precedence: UI safeStorage first, `ANTHROPIC_API_KEY` second, and `CHIRALITY_ANTHROPIC_API_KEY` third. | P0 | `docs/PRD.md` FR-030; `docs/SPEC.md` Section 12.3 |
| DEL-02-05-R04 | If secure storage is unavailable, the UI must report an error. | P0 | `docs/PRD.md` Section 7.7 |
| DEL-02-05-R05 | Runtime errors shown in the UI must be typed and actionable, mapped to title, message, and next-step text. | P1 | `docs/PRD.md` FR-020; decomposition SOW-013 |
| DEL-02-05-R06 | Runtime error states must preserve draft prompt content and attachments for retry. | P1 | `docs/PRD.md` Section 7.3 and FR-020 |
| DEL-02-05-R07 | UI error handling must preserve browser-facing SSE compatibility for `turn:error` and `process:exit` outcomes. | P0 | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |
| DEL-02-05-R08 | UI surfaces must not treat API keys, runtime logs, UI state, SDK transcripts, or chat drafts as authoritative project truth. | P0 | `docs/DIRECTIVE.md` Project Truth sections; `docs/TYPES.md` Section 1.7; `docs/CONTRACT.md` K-FS-1 and K-KEY-1 |
| DEL-02-05-R09 | Any user-facing provider/SDK error detail exposed by this UI must be redacted for secrets. | P0 | `docs/PRD.md` FR-075 and NFR-002; `docs/CONTRACT.md` K-EVENT-6 |
| DEL-02-05-R10 | ASSUMPTION: This UI slice consumes typed runtime/provider errors produced by PKG-03/PKG-04/PKG-05 implementations rather than defining the canonical taxonomy itself. | TBD | `_CONTEXT.md` Exclusions; decomposition package boundaries |

#### Standards

| Standard or Contract | Applicability | Source |
|---|---|---|
| Project truth boundary | API keys and runtime convenience state are not authoritative project state. | `docs/DIRECTIVE.md`; `docs/TYPES.md`; `docs/CONTRACT.md` K-FS-1 and K-KEY-1 |
| API key storage policy | UI safeStorage and environment fallback must keep key material out of working-root files, logs, and runtime events. | `docs/SPEC.md` Sections 12.3 and 16.2; `docs/PRD.md` FR-030, FR-031, NFR-002 |
| Browser SSE event contract | Existing browser-facing event names remain compatible. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |
| Runtime redaction policy | Secrets are redacted from provider errors, logs, event records, and relevant tool outputs. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-075 |

#### Verification

| Requirement | Verification Approach |
|---|---|
| DEL-02-05-R01 | UI/integration test confirms key save path uses Electron IPC and does not create working-root key material. |
| DEL-02-05-R02 | UI test covers status rendering for `ui`, `env`, and `none`; no key value appears in rendered text or captured events. Final fixture/module path is TBD until the API key settings surface is implemented. |
| DEL-02-05-R03 | Integration or mocked status test covers precedence order. Final fixture/command is TBD until the API key settings surface is implemented. |
| DEL-02-05-R04 | Mock unavailable safeStorage and verify visible error state. |
| DEL-02-05-R05 | Unit test maps representative typed errors to title/message/next-step fields. |
| DEL-02-05-R06 | UI state test confirms draft and attachment metadata remain available after a runtime error. |
| DEL-02-05-R07 | SSE/turn UI test confirms `turn:error` and terminal `process:exit` are handled without renaming browser events. |
| DEL-02-05-R08 | Static or integration check confirms API key UI state is local convenience state and not written to deliverable/project truth files. |
| DEL-02-05-R09 | Redaction fixture verifies visible/logged error strings do not expose API keys. |
| DEL-02-05-R10 | Human or architecture review confirms taxonomy ownership once PKG-03/PKG-04/PKG-05 runtime contracts are finalized. |

#### Documentation

Required artifacts for this deliverable:

- API key settings panel.
- Typed error display.
- Secure-storage error UI.

Documentation or implementation details still TBD:

- Exact component/module paths.
- Exact typed error enum consumed by the UI.
- Exact secure-storage unavailable copy.
- Exact retry state owner for drafts and attachments.
- Final evidence paths or commands for key status precedence, key storage secrecy, runtime redaction, and non-authoritative UI state checks.
