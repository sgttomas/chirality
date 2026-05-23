# Specification: DEL-05-03 Redacted RunLogger and Secret Hygiene

## Scope

This deliverable specifies the security control for redacting provider, SDK, tool, and run-log data so key material and configured secrets do not enter Chirality runtime records.

In scope:

- Redaction helper behavior for configured API keys and configured secret variants.
- Redacted `RunLogger` or equivalent runtime logging surface.
- Secret hygiene for `HarnessEvent` payloads, provider errors, SDK errors, SDK stderr/debug logs, and tool result artifacts.
- Tests and fixtures proving provider error classification and redaction behavior.

Out of scope:

- Tool permission semantics and allow/deny policy, except where redaction must apply after permitted tool execution.
- Canonical session folder layout and append-only JSONL writer ownership, which belong to adjacent PKG-05 deliverables.
- API key storage implementation, except that this deliverable must not undermine the existing safeStorage/env precedence rules.

## Requirements

| ID | Requirement | Priority | Source |
|---|---|---:|---|
| DEL-05-03-R1 | Runtime events, run logs, tool artifacts, and provider errors MUST redact secrets and avoid storing API keys. | P0 | `docs/CONTRACT.md` K-EVENT-6 |
| DEL-05-03-R2 | API keys MUST remain non-project convenience state and MUST NOT be written to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. | P0 | `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` FR-031, NFR-002 |
| DEL-05-03-R3 | Runtime logging MUST redact API keys and configured secret variants from SDK errors, tool outputs where policy requires, and event records. | P0 | `docs/PRD.md` FR-075 |
| DEL-05-03-R4 | Provider error classification MUST produce typed `SDK_FAILURE` details for auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation, with key redaction. | P1 | `docs/PRD.md` FR-034 |
| DEL-05-03-R5 | SDK debug logs and stderr captures MUST pass through the run logger redaction layer before persistence or display. | P0 | `docs/PRD.md` Section 10.3 notes; `docs/PLAN.md` Section 6.3 |
| DEL-05-03-R6 | `HarnessEvent.data` payloads MUST avoid secrets; any persisted event data from provider, SDK, hook, permission, tool, or transcript metadata must be redacted first. | P0 | `docs/SPEC.md` Section 9; `docs/PRD.md` Section 10.4 |
| DEL-05-03-R7 | Large or sensitive tool results MUST be budgeted, previewed, stored as artifacts, or redacted according to policy; sensitive raw values MUST NOT be stored unless a redaction pass has approved the payload. | P0 | `docs/CONTRACT.md` K-EVENT-7; `docs/PRD.md` Section 10.5 |
| DEL-05-03-R8 | SDK transcripts remain secondary runtime state; this deliverable MUST NOT treat SDK transcripts as canonical project truth or allow unredacted transcript data to replace Chirality JSONL review surfaces. | P0 | `docs/CONTRACT.md` K-SDK-3; `docs/SPEC.md` Section 8.4 |
| DEL-05-03-R9 | ASSUMPTION: The redaction helper SHOULD handle raw, URL-encoded, lowercase URL-encoded, and double-encoded configured key variants, because current provider tests already exercise those cases. | P1 | Current code context: `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`; exact product-wide helper API TBD |
| DEL-05-03-R10 | Redaction MUST preserve enough non-secret metadata for audit and debugging, such as error class, policy category, status, source indicator, artifact metadata, and event type. | P1 | `docs/PRD.md` FR-034, FR-075; `docs/SPEC.md` Sections 9 and 12.3 |

## Standards

| Standard or Contract | Applicability |
|---|---|
| `docs/CONTRACT.md` K-EVENT-6 | Primary redaction invariant for runtime records. |
| `docs/CONTRACT.md` K-KEY-1 | Primary key-material hygiene invariant. |
| `docs/SPEC.md` Section 9 Runtime Event Schema | Defines `HarnessEvent` payload rules, including no secrets. |
| `docs/SPEC.md` Section 12.3 API Key Handling | Defines key precedence and active-turn-only SDK handoff. |
| `docs/PRD.md` Section 8.5 | Provider key, network, and typed provider error requirements. Source-state warning: HASH_MISMATCH. |
| `docs/PRD.md` Section 8.12 | Runtime event logging and redaction requirements. Source-state warning: HASH_MISMATCH. |

## Verification

| Requirement | Verification Approach |
|---|---|
| DEL-05-03-R1, R2, R3 | Unit tests for redaction helper and run logger using configured key material and representative provider/SDK/tool/run-log payloads. |
| DEL-05-03-R4 | Provider error fixtures for auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation; assert typed `SDK_FAILURE` details contain no key material. |
| DEL-05-03-R5 | Tests or harness fixtures for SDK stderr/debug capture through the redaction layer. |
| DEL-05-03-R6 | Event-schema tests that serialize representative `HarnessEvent` payloads and assert no configured secret variants are present. |
| DEL-05-03-R7 | Tool-result tests for inline, preview, artifact, and redacted/withheld payload paths. |
| DEL-05-03-R8 | Replay/session tests confirming Chirality JSONL remains canonical and SDK transcript metadata is treated as secondary adapter metadata. |
| DEL-05-03-R9 | Extend current provider redaction tests to the shared helper once the helper path is finalized. |
| DEL-05-03-R10 | Snapshot or structured assertions that non-secret diagnostic metadata survives redaction. |

## Documentation

Required artifacts:

- Redaction helper.
- Redacted run logger.
- Run logger tests.
- Provider error fixtures.
- Secret hygiene notes for event payloads and tool artifacts.

TBD:

- Final module path for the shared redaction helper.
- Final module path for `RunLogger` if it differs from the PRD R1 target.
- Config format for additional non-API-key secret variants.
- Exact redaction replacement token.
- Whether SDK transcript redaction can be guaranteed or only avoided/cross-referenced, because source text says SDK transcripts should avoid API keys "if avoidable".
