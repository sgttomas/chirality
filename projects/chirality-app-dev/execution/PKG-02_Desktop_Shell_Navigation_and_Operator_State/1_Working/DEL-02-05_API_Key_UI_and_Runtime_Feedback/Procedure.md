# Procedure: DEL-02-05 API Key UI and Runtime Feedback

## Purpose

Define the working procedure to produce and verify the API key UI and runtime feedback slice for DEL-02-05 without expanding into runtime engine internals or dependency extraction.

## Prerequisites

- Accepted deliverable context in `_CONTEXT.md`.
- Source corpus listed in `_REFERENCES.md`.
- Current `_STATUS.md` state permits work.
- Runtime/API contracts for key status, typed errors, and SSE events are available or mocked for UI work.
- Declared upstream dependencies: TBD - no accepted dependency edges have been extracted yet (`_DEPENDENCIES.md`).

## Steps

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

## Verification

| Check | Expected Result |
|---|---|
| Four-document traceability | Datasheet, Specification, Guidance, and Procedure cite the same source-backed status values, precedence order, and retry requirements. |
| Key status UI | Tests or review cover `ui`, `env`, and `none`; key value never appears. |
| SafeStorage unavailable | Mocked unavailable secure storage produces visible error feedback. |
| Runtime error UI | Representative typed errors map to title/message/next-step text and preserve retry context. |
| Retry state | Draft and attachment state remain available after a runtime error. |
| SSE compatibility | `turn:error` and `process:exit` remain accepted browser-facing event names. |
| Secret hygiene | Redaction checks confirm no API keys in project files, logs, runtime events, or UI error details. |

## Records

- API key settings panel implementation and tests.
- Typed error display implementation and tests.
- Secure-storage error UI implementation and tests.
- Evidence that key material is not written to working root, logs, runtime events, or tool artifacts.
- Human rulings for `Guidance.md` Conflict Table entries CT001 and CT002.

### Evidence Binding Table

| Evidence Need | Required Record | Current Binding |
|---|---|---|
| API key settings surface | Component/module path and test path for the settings panel that routes key storage through Electron IPC. | TBD - implementation path not yet accepted. |
| Key source/status and precedence | Test or review evidence covering `ui`, `env`, `none`, and precedence order. | TBD - final fixture or command not yet accepted. |
| Secure-storage unavailable feedback | Test or review evidence proving unavailable safeStorage produces visible error feedback. | TBD - final fixture or command not yet accepted. |
| Typed runtime error mapping | Test or review evidence mapping representative typed errors to title, message, and next-step fields. | TBD - runtime/provider taxonomy owner not yet accepted. |
| Retry preservation | Test or review evidence proving draft prompt text and attachment metadata remain available after runtime error. | TBD - exact retry state owner not yet accepted. |
| SSE compatibility | Test or review evidence proving `turn:error` and `process:exit` remain browser-facing event names. | TBD - final compatibility fixture not yet accepted. |
| Secret hygiene and project-truth boundary | Static, unit, integration, or review evidence proving key material, logs, drafts, transcripts, and UI state do not become project truth. | TBD - final evidence paths or commands not yet accepted. |
