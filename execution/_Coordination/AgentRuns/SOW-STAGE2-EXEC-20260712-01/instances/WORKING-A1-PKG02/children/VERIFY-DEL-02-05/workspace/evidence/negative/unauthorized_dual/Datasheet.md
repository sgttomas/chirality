# Datasheet: DEL-02-05 API Key UI and Runtime Feedback

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

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

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary UI surfaces | API key settings panel; typed error display; secure-storage error UI | `_CONTEXT.md` Deliverable Scope and Anticipated Artifacts; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-05 row |
| Scope items covered | SOW-013 typed runtime errors; SOW-019 API key storage and resolution | `_CONTEXT.md` Traceability; decomposition SOW ledger |
| Objective support | OBJ-001 and OBJ-008 | `_CONTEXT.md` Traceability; decomposition objectives table |
| Key status values | `ui`, `env`, `none` | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
| API key precedence | UI safeStorage key, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY` | `docs/PRD.md` FR-030; `docs/SPEC.md` Section 12.3 |
| Browser-facing turn error event | `turn:error` | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |
| Terminal stream event | `process:exit` | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| API key material must remain outside project truth | Required | `docs/CONTRACT.md` K-KEY-1; `docs/SPEC.md` Section 16.2; `docs/PRD.md` NFR-002 |
| Secure key storage location | `app.getPath('userData')/credentials/api-key.enc` | `docs/SPEC.md` Section 16.2 |
| Secure-storage mechanism | Electron `safeStorage` | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
| Runtime errors preserve retry context | Required for drafts and attachments | `docs/PRD.md` Section 7.3 and FR-020; decomposition SOW-013 |
| Runtime event/log redaction | API keys and configured secrets must be redacted | `docs/PRD.md` FR-075 and NFR-002; `docs/CONTRACT.md` K-EVENT-6 |
| PRD source integrity | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; dispatch override — reconciled under D-APP-38 |

## Construction

| Component | Construction Notes | Source |
|---|---|---|
| API key settings panel | Must allow user key storage through Electron IPC and expose key source/status without exposing key material. Specific component path is TBD. | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
| Secure-storage feedback | Must report secure-storage unavailability as a user-visible error. Exact copy and visual treatment are TBD. | `docs/PRD.md` Section 7.7 |
| Typed runtime error display | Must map harness errors to title, message, and next-step text. Exact error taxonomy and component path are TBD for this UI slice. | `docs/PRD.md` FR-020; decomposition SOW-013 |
| Retry-preserving failure state | Must preserve drafts and attachments after runtime errors so the user can retry. Exact local state owner and final evidence path are TBD. | `docs/PRD.md` FR-020; decomposition SOW-013 and SOW-023 |
| SSE compatibility | UI behavior must preserve existing browser-facing SSE event names during runtime changes. | `docs/SPEC.md` Section 11; decomposition acceptance checklist |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `docs/CONTRACT.md`
- `docs/DIRECTIVE.md`
- `docs/PLAN.md`
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
- `docs/SPEC.md`
- `docs/TYPES.md`

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-112 resolves the SOW-023 traceability delta in favor of inclusion because decomposition v3.2 explicitly maps SOW-023 to DEL-02-05; the new anchor is derivative traceability, not a lifecycle decision.
