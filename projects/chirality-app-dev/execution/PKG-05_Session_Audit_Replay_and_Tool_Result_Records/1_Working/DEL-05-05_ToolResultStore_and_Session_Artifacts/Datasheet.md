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
| Session artifact location | `.chirality/sessions/<sessionId>/artifacts/` for large tool results after redaction/truncation policy has been applied. | `docs/SPEC.md` Sections 8.2, 9.2; `docs/PRD.md` Sections 10.3, 10.5 |
| Canonical audit mirror | `.chirality/sessions/<sessionId>/events.jsonl`; SDK transcripts remain secondary unless imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3 |
| Event linkage | Tool result artifacts must be referenced by path from persisted runtime event metadata. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 |
| Artifact metadata fields | Tool name where known, optional turn ID where available, original and stored byte counts, truncation flag, SHA-256, session-lifetime retention policy, redaction status, and relative artifact path. | `docs/PRD.md` Section 10.5; D-APP-42 |
| Redaction boundary | Runtime events, run logs, tool artifacts, and provider errors must redact secrets and avoid API keys. | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PRD.md` NFR-002 |
| Output budget classes | Small results inline, medium results preview plus metadata, large results artifact plus metadata. | `docs/PRD.md` Section 10.5 |
| Output budget thresholds | Existing descriptor-defined thresholds remain unchanged by D-APP-42. | `frontend/src/lib/harness/tool-descriptor.ts`; D-APP-42 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Working-root locality | Project execution state, sessions, and tool artifacts live under the selected working root or configured Chirality-controlled session path. | `docs/DIRECTIVE.md` Sections 2.3, 2.8; `docs/SPEC.md` Section 10.2 |
| Replay requirement | JSONL replay must tolerate malformed trailing lines while preserving valid prior events. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| Ordering requirement | JSONL writes must append newline-delimited events in write sequence. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 |
| Concurrent tool activity | Deterministic replay must survive SDK tool concurrency. | Decomposition SOW-053; `docs/SPEC.md` Section 9.2 |
| Model/chat budget | Large outputs must not flood chat or model context. | `docs/PRD.md` NFR-017 and R4 acceptance |
| Sensitive payload storage | Sensitive values must not be stored unless a redaction pass has approved the payload. | `docs/PRD.md` Section 10.5; `docs/CONTRACT.md` K-EVENT-6 |

## Construction

| Component | Expected construction | Status |
|---|---|---|
| `ToolResultStore` | Product-owned artifact and preview policy for tool outputs. | Implemented in `frontend/src/lib/harness/tool-result-artifacts.ts` and `frontend/src/lib/harness/tool-evidence.ts` |
| Session artifact writer | Writes artifact results beneath `.chirality/sessions/<sessionId>/artifacts/tools/` and returns relative artifact references, byte counts, SHA-256, and retention metadata. | Implemented in `frontend/src/lib/harness/tool-result-artifacts.ts` |
| Preview builder | Produces inline small results and artifact-backed overflow without unbounded chat/model expansion. | Implemented with current descriptor-defined thresholds |
| Metadata fixture set | Covers tool name, optional turn ID where available, byte counts, SHA-256, session-lifetime retention, truncation flag, relative artifact path, and redaction status. | Covered by focused tests |
| Output budget tests | Verify inline/artifact behavior and no chat/context flooding. | Covered by focused tests |
| Replay fixtures | Verify artifact links remain reconstructible through `events.jsonl` replay, including malformed-tail tolerance and interleaved append order. | Covered by focused tests |

## Current Discovery State

| Topic | Current state | Disposition |
|---|---|---|
| B-001 source-state warning | `_REFERENCES.md` now marks REF-006 `docs/PRD.md` as `MATCH` under D-APP-38 authority corpus v2. | Retired for ADQ-10 scope. |
| C-001 implementation and fixture paths | Accepted implementation and fixture paths are now recorded in `Specification.md`, `Procedure.md`, and ADQ-10 evidence. | Closed for ADQ-10 scope. |
| F-001 unresolved policy fields | D-APP-42 accepts SHA-256 and session-lifetime retention while leaving byte thresholds, preview length, and artifact naming unchanged. | Closed for checksum/retention; no TTL, quota, daemon, or release-retention claim authorized. |

## References

| RefID | Source | Notes |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | MATCH. Runtime events explain work and the Chirality audit mirror is canonical. |
| REF-002 | `docs/CONTRACT.md` | MATCH. K-EVENT and K-KEY invariants bind redaction, artifacts, and replay. |
| REF-003 | `docs/SPEC.md` | MATCH. Defines session layout, `HarnessEvent`, append/replay rules, and artifact path references. |
| REF-004 | `docs/TYPES.md` | MATCH. Defines `ToolResultStore`, session terms, `events.jsonl`, and `artifacts/`. |
| REF-005 | `docs/PLAN.md` | MATCH. Places tool-result budgeting in R4 and preserves Chirality ownership of artifact/preview policy. |
| REF-006 | `docs/PRD.md` | MATCH. D-APP-38 authority corpus v2 reconciled the accepted PRD snapshot. |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | MATCH. Used for decomposition method context only. |
