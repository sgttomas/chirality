# Specification: DEL-02-05 API Key UI and Runtime Feedback

## Scope

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

## Requirements

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
| DEL-02-05-R10 | This UI slice MUST consume the product-owned `HarnessErrorType` from `@chirality/harness-contract` and MUST NOT redefine the canonical runtime taxonomy; provider-native errors remain adapter metadata. | P1 | `frontend/packages/harness-contract/src/types.ts`; `frontend/packages/harness-contract/src/errors.ts`; `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md` |

## Standards

| Standard or Contract | Applicability | Source |
|---|---|---|
| Project truth boundary | API keys and runtime convenience state are not authoritative project state. | `docs/DIRECTIVE.md`; `docs/TYPES.md`; `docs/CONTRACT.md` K-FS-1 and K-KEY-1 |
| API key storage policy | UI safeStorage and environment fallback must keep key material out of working-root files, logs, and runtime events. | `docs/SPEC.md` Sections 12.3 and 16.2; `docs/PRD.md` FR-030, FR-031, NFR-002 |
| Browser SSE event contract | Existing browser-facing event names remain compatible. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |
| Runtime redaction policy | Secrets are redacted from provider errors, logs, event records, and relevant tool outputs. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-075 |

## Verification

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
| DEL-02-05-R10 | Contract/import review confirms runtime, adapter, API, and UI layers use the canonical harness-contract error type; representative error-display, route, adapter, and mapper tests remain green. |

## Documentation

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
