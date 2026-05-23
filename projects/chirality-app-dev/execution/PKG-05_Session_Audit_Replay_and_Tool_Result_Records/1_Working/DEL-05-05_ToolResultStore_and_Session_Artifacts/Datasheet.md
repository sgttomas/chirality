# Datasheet: DEL-05-05 ToolResultStore and Session Artifacts

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-05-05 |
| DeliverableName | ToolResultStore and Session Artifacts |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| ResponsibleParty | TBD |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary purpose | Store and preview medium/large tool outputs under session artifacts without flooding chat or model context. | `_CONTEXT.md` Deliverable Scope; decomposition `DEL-05-05` row |
| Session artifact location | `.chirality/sessions/<sessionId>/artifacts/` for raw large tool results. | `docs/SPEC.md` Sections 8.2, 9.2; `docs/PRD.md` Sections 10.3, 10.5 (HASH_MISMATCH warning) |
| Canonical audit mirror | `.chirality/sessions/<sessionId>/events.jsonl`; SDK transcripts remain secondary unless imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3 |
| Event linkage | Tool result artifacts must be referenced by path from persisted runtime event metadata. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 (HASH_MISMATCH warning) |
| Artifact metadata fields | Tool name, turn ID, byte count, truncation flag, and relative artifact path. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning) |
| Redaction boundary | Runtime events, run logs, tool artifacts, and provider errors must redact secrets and avoid API keys. | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PRD.md` NFR-002 (HASH_MISMATCH warning) |
| Output budget classes | Small results inline, medium results preview plus metadata, large results raw artifact plus metadata. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning) |
| Output budget thresholds | TBD. Source corpus defines classes but not byte thresholds. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Working-root locality | Project execution state, sessions, and tool artifacts live under the selected working root or configured Chirality-controlled session path. | `docs/DIRECTIVE.md` Sections 2.3, 2.8; `docs/SPEC.md` Section 10.2 |
| Replay requirement | JSONL replay must tolerate malformed trailing lines while preserving valid prior events. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| Ordering requirement | JSONL writes must append newline-delimited events in write sequence. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 (HASH_MISMATCH warning) |
| Concurrent tool activity | Deterministic replay must survive SDK tool concurrency. | Decomposition SOW-053; `docs/SPEC.md` Section 9.2 |
| Model/chat budget | Large outputs must not flood chat or model context. | `docs/PRD.md` NFR-017 and R4 acceptance (HASH_MISMATCH warning) |
| Sensitive payload storage | Sensitive values must not be stored unless a redaction pass has approved the payload. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning); `docs/CONTRACT.md` K-EVENT-6 |

## Construction

| Component | Expected construction | Status |
|---|---|---|
| `ToolResultStore` | Product-owned artifact and preview policy for tool outputs. | Required; interface/module location TBD |
| Session artifact writer | Writes large raw results beneath `.chirality/sessions/<sessionId>/artifacts/` and returns relative artifact references. | Required; implementation path TBD |
| Preview builder | Produces inline small results and medium previews without unbounded chat/model expansion. | Required; thresholds and preview format TBD |
| Metadata fixture set | Covers tool name, turn ID, byte count, truncation flag, relative artifact path, and redaction status where applicable. | Required |
| Output budget tests | Verify inline/preview/artifact behavior and no chat/context flooding. | Required |
| Replay fixtures | Verify artifact links remain reconstructible through `events.jsonl` replay, including malformed-tail tolerance. | Required |

## References

| RefID | Source | Notes |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | MATCH. Runtime events explain work and the Chirality audit mirror is canonical. |
| REF-002 | `docs/CONTRACT.md` | MATCH. K-EVENT and K-KEY invariants bind redaction, artifacts, and replay. |
| REF-003 | `docs/SPEC.md` | MATCH. Defines session layout, `HarnessEvent`, append/replay rules, and artifact path references. |
| REF-004 | `docs/TYPES.md` | MATCH. Defines `ToolResultStore`, session terms, `events.jsonl`, and `artifacts/`. |
| REF-005 | `docs/PLAN.md` | MATCH. Places tool-result budgeting in R4 and preserves Chirality ownership of artifact/preview policy. |
| REF-006 | `docs/PRD.md` | HASH_MISMATCH. Used as accessible vNext direction per task instruction; unsupported details remain `TBD`. |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | MATCH. Used for decomposition method context only. |
