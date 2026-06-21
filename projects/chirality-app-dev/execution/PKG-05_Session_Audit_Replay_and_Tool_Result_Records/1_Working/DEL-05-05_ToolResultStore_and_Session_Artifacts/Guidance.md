# Guidance: DEL-05-05 ToolResultStore and Session Artifacts

## Purpose

This deliverable exists to keep tool-heavy runtime work auditable and readable. Tool results must be available for replay and diagnosis, but large payloads must not be pushed unbounded into chat, browser events, or model context. Chirality owns the artifact/preview policy even when the SDK supplies the tool loop.

Sources: `_CONTEXT.md`; decomposition `DEL-05-05`; `docs/DIRECTIVE.md` Sections 2.3 and 2.8; `docs/PLAN.md` R4; `docs/PRD.md` Sections 9.4 and 10.5; D-APP-42.

## Principles

- Keep `events.jsonl` canonical. Runtime artifact metadata should point from Chirality events to stored outputs; artifact storage must not make SDK transcripts or chat history the authority. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4.
- Budget output by representation. Small text can be inline, medium output needs preview plus metadata, and large output needs artifact storage plus a compact reference. Source: `docs/PRD.md` Section 10.5.
- Preserve replay before convenience. A user reviewing a session later should be able to reconstruct tool summaries, terminal outcomes, and artifact links from Chirality JSONL plus session metadata. Source: `docs/PRD.md` FR-076 and NFR-017; `docs/SPEC.md` Section 9.2.
- Redact before storing sensitive content. Secrets must not land in runtime events, run logs, provider errors, or tool artifacts. Source: `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1.
- Keep provider details out of product contracts. `ToolResultStore` should operate on Chirality event/session concepts, not SDK-native transcript shapes. Source: `docs/PRD.md` Section 9.4; `docs/CONTRACT.md` K-ENGINE-4.
- Make policy boundaries explicit. D-APP-42 accepts SHA-256 checksums and session-lifetime retention, leaves thresholds, preview length, and naming unchanged, and authorizes no TTL, quota, daemon, or release-retention claim.

## Considerations

### Source-state posture

D-APP-38 authority corpus v2 reconciles `docs/PRD.md`; `_REFERENCES.md` records REF-006 as `MATCH`. Historical B-001 source-state warnings are retired for the ADQ-10 scope.

### Budget thresholds

The runtime already defines tool-specific byte thresholds in `frontend/src/lib/harness/tool-descriptor.ts`. D-APP-42 deliberately leaves those values and the artifact naming scheme unchanged, so ADQ-10 validation should verify current behavior rather than introduce new policy.

F-001 and X-001 remain linked for future threshold changes: if thresholds or preview limits are changed later, that change needs a governed policy decision plus boundary tests. ADQ-10 does not alter those values.

### Event and artifact separation

Avoid embedding raw large payloads in `HarnessEvent.data`. Store the payload under session artifacts and persist metadata sufficient for replay. This keeps UI events compact and prevents model-context flooding while preserving audit evidence.

### Redaction posture

The safest implementation shape is a redaction decision before artifact persistence. If source uncertainty remains about whether a payload contains secrets, prefer redacted preview and blocked raw storage over saving unreviewed sensitive output.

### Concurrent tool activity

The decomposition explicitly includes deterministic replay under tool concurrency. Store enough sequence or parent-event linkage to preserve replay order under interleaved completions. ADQ-10 accepts JSONL append order as the deterministic ordering signal for the interleaved artifact replay fixture.

D-001 is best handled as an assertion-design requirement: replay tests should prove ordering from JSONL write sequence or accepted event-ordering metadata, not from incidental SDK completion order.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Inline content vs artifact link | Inline improves immediate readability for small text. Artifact links preserve performance and context for large output. Use the budget class, not ad hoc UI convenience, to decide. |
| Preview richness vs leakage risk | Rich previews help review, but sensitive data must be redacted. Prefer safe summaries when redaction status is uncertain. |
| SDK transcript detail vs Chirality canonicality | SDK transcripts may contain useful details, but Chirality event metadata and artifact references are the replay authority unless transcript content is imported into `HarnessEvent` form. |
| Early hardcoded thresholds vs configurable policy | ADQ-10 does not introduce new threshold values. It preserves the current descriptor-defined thresholds and records that future threshold changes need a governed policy update. |
| Retention/checksum certainty vs premature policy | D-APP-42 chooses SHA-256 for exact stored bytes after redaction/truncation and session-lifetime retention. This gives replay/audit verification without claiming TTL, quota, daemon cleanup, release retention, or broader custody guarantees. |

## Examples

| Scenario | Expected behavior |
|---|---|
| Small text result | Store result inline in the tool completion event data when it is within the current descriptor-defined small-output threshold and contains no unredacted secrets. |
| Medium text result | Store a bounded preview and required metadata; avoid placing the full raw result in chat/model context. |
| Large result | Store payload under `.chirality/sessions/<sessionId>/artifacts/`; persist relative artifact path, tool name where known, optional turn ID where available, byte counts, truncation flag, SHA-256, and session-lifetime retention in event metadata. |
| Sensitive tool output | Apply redaction before event/artifact persistence; if redaction cannot approve the payload, do not store raw sensitive values. |
| Malformed trailing JSONL line | Replay should ignore the malformed tail and preserve valid prior events and artifact links. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| NONE | No direct source-content conflict remains open for ADQ-10. REF-006 is `MATCH` under D-APP-38 authority corpus v2, and D-APP-42 resolves checksum/retention policy. | `_REFERENCES.md` REF-006; D-APP-42 | `docs/PRD.md` Sections 10.4-10.5 and NFR-017 | All sections citing PRD; artifact metadata policy | Use matched PRD source plus D-APP-42 for checksum/retention; preserve thresholds, preview length, and naming unchanged. | ACCEPTED |
| B-001 | RETIRED: PRD-derived tool-result budgeting and metadata claims are no longer warning-qualified for this scope because REF-006 now matches the accepted authority corpus. | `_REFERENCES.md` REF-006 | D-APP-38 authority corpus v2 | Datasheet Attributes; Specification Requirements; Procedure Steps | Retire B-001 source-state caveat. | ACCEPTED |
