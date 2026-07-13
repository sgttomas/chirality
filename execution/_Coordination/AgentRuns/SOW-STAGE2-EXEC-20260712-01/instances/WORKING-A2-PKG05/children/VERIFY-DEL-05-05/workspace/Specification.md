# Specification: DEL-05-05 ToolResultStore and Session Artifacts

## Scope

DEL-05-05 covers the backend feature slice that stores, previews, and references medium/large tool outputs as session artifacts so chat and model context are not flooded. The slice belongs to PKG-05, whose package scope is canonical session layout, `HarnessEvent`, JSONL append/replay, redaction, and tool result artifacts.

In scope:

- Product-owned `ToolResultStore` policy and implementation surface for tool output budgeting.
- Session-local artifact storage under `.chirality/sessions/<sessionId>/artifacts/`.
- Metadata records linking stored artifacts to tool name, optional turn ID where available, byte counts, truncation flag, SHA-256 checksum, session-lifetime retention policy, and relative artifact path.
- Preview behavior for medium results and inline behavior for small results.
- Output budget tests, replay/metadata fixtures, and redaction-sensitive artifact behavior.

Out of scope:

- Tool permission semantics and deny-first policy, except where stored tool output must respect redaction and audit constraints.
- SDK transcript canonicality decisions outside artifact linkage.
- Bash enablement policy, except that allowed bash output must eventually use the same result budgeting behavior.

Sources: `_CONTEXT.md`; decomposition `DEL-05-05`; `docs/SPEC.md` Sections 8-9; `docs/PRD.md` Sections 10.4-10.5; D-APP-42.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-05-05-REQ-001 | The implementation MUST preserve `.chirality/sessions/<sessionId>/events.jsonl` as the product-owned Chirality audit mirror; artifact storage MUST NOT make SDK transcripts canonical. | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-EVENT-4 |
| DEL-05-05-REQ-002 | Large tool result payloads MUST be stored as artifacts and referenced by path from runtime event metadata. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 |
| DEL-05-05-REQ-003 | Raw large tool results MUST be stored beneath `.chirality/sessions/<sessionId>/artifacts/` or an explicitly configured Chirality-controlled session artifact path. | `docs/SPEC.md` Section 8.2; `docs/PRD.md` Section 10.5 |
| DEL-05-05-REQ-004 | Small text tool results MAY be carried inline in `tool.completed` data; medium results MUST include preview and metadata; large results MUST include artifact metadata rather than unbounded inline content. | `docs/PRD.md` Section 10.5 |
| DEL-05-05-REQ-005 | Artifact metadata MUST include tool name where known, optional turn ID where available, original and stored byte counts, truncation flag, SHA-256 for exact stored bytes, session-lifetime retention policy, and relative artifact path. | `docs/PRD.md` Section 10.5; D-APP-42 |
| DEL-05-05-REQ-006 | Runtime events, run logs, tool artifacts, and provider errors MUST redact secrets and avoid storing API keys. | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PRD.md` NFR-002 |
| DEL-05-05-REQ-007 | Sensitive values MUST NOT be stored in tool artifacts unless a redaction pass has approved the payload. | `docs/PRD.md` Section 10.5; `docs/CONTRACT.md` K-EVENT-6 |
| DEL-05-05-REQ-008 | Artifact links and summaries MUST remain replayable from Chirality JSONL plus session metadata even when a malformed trailing JSONL line exists. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| DEL-05-05-REQ-009 | Tool result storage MUST preserve deterministic replay under concurrent SDK tool activity by relying on ordered append/write sequence metadata rather than arrival ambiguity. | Decomposition SOW-053; `docs/SPEC.md` Section 9.2 |
| DEL-05-05-REQ-010 | Output budget tests MUST verify that large outputs do not flood chat or model context and that medium/large outputs surface usable previews or artifact links. | `docs/PRD.md` NFR-017 and R4 acceptance; decomposition anticipated artifacts |
| DEL-05-05-REQ-011 | ASSUMPTION: The implementation should expose `ToolResultStore` through a product-owned interface/module that is not SDK-shaped, because TYPES and PRD identify it as Chirality-owned policy. | `docs/TYPES.md` Section 7/8 glossary; `docs/PRD.md` Section 9.4 |
| DEL-05-05-REQ-012 | Output class byte thresholds, preview length, and artifact naming scheme remain the existing descriptor/artifact-writer policy; persisted artifacts MUST carry SHA-256 checksums and session-lifetime retention metadata, with no TTL, quota, daemon, or release-retention claim authorized. | `frontend/packages/harness-contract/src/tool-descriptor.ts`; `frontend/src/lib/harness/tool-result-artifacts.ts`; D-APP-42 |
| DEL-05-05-REQ-013 | The deterministic replay test for concurrent or interleaved tool-result completions MUST assert the accepted ordering signal: JSONL append/write sequence, `parentEventId` linkage where applicable, or another explicitly accepted event-ordering metadata field. | D-001; `docs/SPEC.md` Section 9.1-9.2; decomposition SOW-053 |
| DEL-05-05-REQ-014 | Threshold-boundary verification MUST cover the current descriptor-defined byte thresholds and preview behavior; D-APP-42 does not change those thresholds. | X-001; `docs/PRD.md` NFR-017 and R4 acceptance; D-APP-42 |

## Standards

The distinct medium-band preview representation remains explicitly deferred
under D-APP-42 and D-APP-56 R4-P08 as a future output-budget policy question.
Current small-inline and artifact-backed overflow behavior remains governed and
must not be represented as implementing that deferred representation.

| Standard / Contract | Applicability | Source |
|---|---|---|
| Chirality `HarnessEvent` schema | Persisted runtime event metadata must use stable product-owned event shape. | `docs/SPEC.md` Section 9.1; `docs/PRD.md` Section 10.4 |
| Append-only JSONL event store | Artifact references must be compatible with ordered append/replay semantics. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| Session layout contract | Artifact storage must fit canonical session folder layout. | `docs/SPEC.md` Section 8.2 |
| K-EVENT invariants | Binding audit, replay, redaction, and artifact-budget constraints. | `docs/CONTRACT.md` Section 1.5 |
| Working-root/project-truth boundary | Tool artifacts are runtime audit state, not accepted project truth or human approval records. | `docs/DIRECTIVE.md` Sections 2.3, 2.8 |

## Verification

| Requirement IDs | Verification approach |
|---|---|
| REQ-001, REQ-002, REQ-003 | Unit tests for session path resolution, relative artifact references, and event metadata persistence under `.chirality/sessions/<sessionId>/`. |
| REQ-004, REQ-010 | Output budget tests covering small inline and artifact-backed overflow behavior under current descriptor-defined limits. |
| REQ-005 | Metadata fixture tests asserting tool name, optional turn ID where available, byte counts, truncation flag, SHA-256, session-lifetime retention, and relative artifact path. |
| REQ-006, REQ-007 | Redaction tests using provider errors, run logs, event data, and tool-result payload fixtures with secret-like values. |
| REQ-008 | Replay tests using valid JSONL followed by a malformed trailing line; valid prior artifact links must remain available. |
| REQ-009, REQ-013 | Deterministic ordering tests using concurrent or interleaved tool-result completion fixtures; assertions must bind replay order to write sequence or accepted event-ordering metadata rather than completion-arrival ambiguity. |
| REQ-011 | Conformance/type tests ensuring public event/API contracts remain provider-neutral and not SDK-shaped. |
| REQ-012 | Unit tests and review confirming existing thresholds/naming are unchanged while SHA-256 and session-lifetime retention metadata are present. |
| REQ-014 | Threshold and overflow tests for the current descriptor-defined limits. |

## Documentation

Required implementation artifacts for this deliverable:

- Artifact store implementation path: `frontend/src/lib/harness/tool-result-artifacts.ts`.
- Output budget tests for inline/artifact overflow behavior: `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` and `frontend/src/__tests__/lib/tool-evidence.test.ts`.
- Metadata fixtures covering required artifact metadata fields: `frontend/src/__tests__/lib/tool-result-artifacts.test.ts`, `frontend/src/__tests__/lib/sdk-message-mapper.test.ts`, and `frontend/src/__tests__/lib/transcript-replay.test.ts`.
- Replay fixtures with artifact references and malformed-tail JSONL tolerance: `frontend/src/__tests__/lib/session-events.test.ts`.
- Redaction fixtures for sensitive tool output handling: `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` and `frontend/src/__tests__/lib/session-events.test.ts`.
- Developer notes identifying that D-APP-42 chose SHA-256 plus session-lifetime retention while leaving thresholds, preview length, and naming unchanged.
- P3 disposition record for B-001, C-001, F-001, D-001, X-001, and E-001 showing which items were retired, incorporated, or explicitly left outside ADQ-10.

## D-APP-56 child-output partition note (2026-07-12)

R4-P32 assigns `artifacts/subagents/` child-output storage and its 16 KiB/512 KiB thresholds to DEL-08-05. DEL-05-05 continues to own `descriptor.resultBudget`; it does not duplicate child-output artifact ownership.
