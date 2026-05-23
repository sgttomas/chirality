# Datasheet: DEL-05-03 Redacted RunLogger and Secret Hygiene

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-05-03 |
| Deliverable Name | Redacted RunLogger and Secret Hygiene |
| Package | PKG-05 Session Audit, Replay, and Tool Result Records |
| Decomposition Variant | SOFTWARE_DECOMP v3.2 |
| Responsible Party | TBD |
| Type | SECURITY_CONTROL |
| Context Envelope | S |
| Scope Items | SOW-021, SOW-041 |
| Supporting Objectives | OBJ-003, OBJ-008 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary control surface | Redaction of provider, SDK, tool, and run logs before key material or secrets enter runtime records. | `_CONTEXT.md`; `docs/PRD.md` Section 8.12; `docs/PLAN.md` Section 6.3 |
| Runtime logger target | `RunLogger` or equivalent redacted structured runtime logger. | `docs/PRD.md` R1 implementation targets |
| Secret classes explicitly named by sources | API keys and configured secret variants. | `docs/PRD.md` FR-075; `docs/PRD.md` NFR-002 |
| Records covered | Runtime events, run logs, tool artifacts, provider errors, SDK errors, SDK stderr/debug logs, and event records. | `docs/CONTRACT.md` K-EVENT-6; `docs/PLAN.md` Section 6.3; `docs/PRD.md` FR-075 |
| Canonical audit record relation | `.chirality/sessions/<sessionId>/events.jsonl` remains the product-owned Chirality audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` K-EVENT-4, K-SDK-3; `docs/SPEC.md` Sections 8.4 and 9 |
| Provider error relation | Provider errors must be classified and produce typed `SDK_FAILURE` details with key redaction. | `docs/PRD.md` Section 8.5, FR-034 |
| Tool result relation | Large or sensitive tool results must be budgeted, previewed, stored as artifacts, or redacted according to policy. | `docs/CONTRACT.md` K-EVENT-7; `docs/PRD.md` Section 10.5 |
| Existing code context | Current source tree contains Anthropic provider redaction helpers and tests for configured API-key redaction. | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts`; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` |

## Conditions

| Condition | Requirement-Relevant Fact | Source |
|---|---|---|
| API key storage | API keys are non-project convenience state and must not be written to project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` FR-031; `docs/SPEC.md` Section 12.3 |
| API key handoff | Key material is supplied to the SDK environment only as needed for active turns and redacted from logs/events. | `docs/SPEC.md` Section 12.3; `docs/PLAN.md` R1 |
| Event payloads | `HarnessEvent.data` payloads must avoid secrets. | `docs/SPEC.md` Section 9; `docs/PRD.md` Section 10.4 |
| SDK boundaries | SDK messages, IDs, tool names, transcript paths, and external names may appear only as adapter metadata under product-owned contracts. | `docs/SPEC.md` Section 10.3; `docs/DIRECTIVE.md` Section 4.2 |
| Source warning | `docs/PRD.md` is locally accessible but has a HASH_MISMATCH in `_REFERENCES.md`; this run treats it as a source-state warning, not an input failure. | `_REFERENCES.md`; human runtime instruction |

## Construction

| Component | Description | Status |
|---|---|---|
| Redaction helper | Shared helper that redacts configured API key material and configured secret variants before text or structured data is logged or persisted. | TBD: final module path and public API |
| Run logger | Structured runtime logger that applies the redaction helper before emitting logs, runtime events, error details, or debug/stderr captures. | TBD: final module path; anticipated as `frontend/src/lib/harness/run-logger.ts` by PRD R1 |
| Provider error fixtures | Fixtures covering auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation redaction. | TBD |
| Tool result redaction gate | Policy hook ensuring sensitive tool outputs are redacted or withheld before inline event payloads or artifacts are persisted. | TBD: exact policy integration point |
| Tests | Unit and integration tests proving configured key variants and provider/SDK/tool/run-log paths do not leak secrets. | TBD: final test names; current provider redaction tests exist |

## Pass 3 Implementation Slots

| Slot | Required Record | Current Disposition | Source |
|---|---|---|---|
| Shared redaction helper identity | Final module path, exported API name, accepted replacement token, and supported configured-secret schema. | TBD until implementation selects the shared helper contract. | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PRD.md` FR-075 |
| RunLogger identity | Final module path and public logging surface used by provider errors, SDK diagnostics, event emission, tool-result handling, and run logs. | TBD; PRD R1 names `run-logger.ts` as an implementation target but not an accepted final path. | `docs/PLAN.md` R1; `docs/PRD.md` R1 implementation targets |
| Boundary inventory | Discovered code paths for provider errors, SDK errors, SDK stderr/debug logs, `HarnessEvent.data`, run logs, and tool-result persistence/display. | TBD until code discovery records the implementation paths. | `docs/SPEC.md` Section 9; `docs/PRD.md` Sections 10.3.1, 10.4, 10.5 |

## References

| RefID | Source | Notes |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Runtime logs and API keys are non-authoritative unless governed import occurs; secrets stay out of project files and event payloads. |
| REF-002 | `docs/CONTRACT.md` | K-EVENT-6 and K-KEY-1 are the primary invariants for this deliverable. |
| REF-003 | `docs/SPEC.md` | Runtime event schema, SDK adapter rules, and API-key handling rules. |
| REF-004 | `docs/TYPES.md` | `HarnessEvent`, Runtime Audit Mirror, Project Truth, and SDK transcript vocabulary. |
| REF-005 | `docs/PLAN.md` | R1 sequencing and security/privacy acceptance notes. |
| REF-006 | `docs/PRD.md` | Product requirements for provider error classification, runtime redaction, session events, and R1 implementation targets. HASH_MISMATCH warning recorded in `_REFERENCES.md`. |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method; SECURITY_CONTROL type definition. |
