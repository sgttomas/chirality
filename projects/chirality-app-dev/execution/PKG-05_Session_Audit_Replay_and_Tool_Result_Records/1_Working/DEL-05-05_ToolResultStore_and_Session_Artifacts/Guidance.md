# Guidance: DEL-05-05 ToolResultStore and Session Artifacts

## Purpose

This deliverable exists to keep tool-heavy runtime work auditable and readable. Tool results must be available for replay and diagnosis, but large payloads must not be pushed unbounded into chat, browser events, or model context. Chirality owns the artifact/preview policy even when the SDK supplies the tool loop.

Sources: `_CONTEXT.md`; decomposition `DEL-05-05`; `docs/DIRECTIVE.md` Sections 2.3 and 2.8; `docs/PLAN.md` R4; `docs/PRD.md` Sections 9.4 and 10.5 (HASH_MISMATCH warning).

## Principles

- Keep `events.jsonl` canonical. Runtime artifact metadata should point from Chirality events to stored outputs; artifact storage must not make SDK transcripts or chat history the authority. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4.
- Budget output by representation. Small text can be inline, medium output needs preview plus metadata, and large output needs artifact storage plus a compact reference. Source: `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning).
- Preserve replay before convenience. A user reviewing a session later should be able to reconstruct tool summaries, terminal outcomes, and artifact links from Chirality JSONL plus session metadata. Source: `docs/PRD.md` FR-076 and NFR-017 (HASH_MISMATCH warning); `docs/SPEC.md` Section 9.2.
- Redact before storing sensitive content. Secrets must not land in runtime events, run logs, provider errors, or tool artifacts. Source: `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1.
- Keep provider details out of product contracts. `ToolResultStore` should operate on Chirality event/session concepts, not SDK-native transcript shapes. Source: `docs/PRD.md` Section 9.4 (HASH_MISMATCH warning); `docs/CONTRACT.md` K-ENGINE-4.
- Make missing policy explicit. Thresholds, preview lengths, naming, checksum, and retention are currently source gaps and should remain `TBD` until accepted design work fills them.

## Considerations

### Source-state warning

`docs/PRD.md` is listed with `HASH_MISMATCH` in `_REFERENCES.md`. The task instruction says to treat this as a source-state warning. This draft uses PRD content as accessible vNext direction but does not invent unsupported values from it.

### Budget thresholds

The corpus defines small, medium, and large output classes but does not define byte thresholds. Use `TBD` in implementation tickets and tests until thresholds are selected and accepted. A test can still assert class behavior once thresholds are parameterized.

### Event and artifact separation

Avoid embedding raw large payloads in `HarnessEvent.data`. Store the payload under session artifacts and persist metadata sufficient for replay. This keeps UI events compact and prevents model-context flooding while preserving audit evidence.

### Redaction posture

The safest implementation shape is a redaction decision before artifact persistence. If source uncertainty remains about whether a payload contains secrets, prefer redacted preview and blocked raw storage over saving unreviewed sensitive output.

### Concurrent tool activity

The decomposition explicitly includes deterministic replay under tool concurrency. Store enough sequence or parent-event linkage to preserve replay order under interleaved completions. The source corpus does not specify exact fields beyond the `HarnessEvent` shape, so sequence metadata details are TBD.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Inline content vs artifact link | Inline improves immediate readability for small text. Artifact links preserve performance and context for large output. Use the budget class, not ad hoc UI convenience, to decide. |
| Preview richness vs leakage risk | Rich previews help review, but sensitive data must be redacted. Prefer safe summaries when redaction status is uncertain. |
| SDK transcript detail vs Chirality canonicality | SDK transcripts may contain useful details, but Chirality event metadata and artifact references are the replay authority unless transcript content is imported into `HarnessEvent` form. |
| Early hardcoded thresholds vs configurable policy | Hardcoded thresholds would unblock tests but risk becoming undocumented product policy. Keep threshold values TBD until design acceptance. |

## Examples

| Scenario | Expected behavior |
|---|---|
| Small text result | Store result inline in the tool completion event data when it is within the accepted small-output threshold and contains no unredacted secrets. Threshold TBD. |
| Medium text result | Store a preview and required metadata; avoid placing the full raw result in chat/model context. Preview length TBD. |
| Large result | Store raw payload under `.chirality/sessions/<sessionId>/artifacts/`; persist relative artifact path, tool name, turn ID, byte count, and truncation flag in event metadata. |
| Sensitive tool output | Apply redaction before event/artifact persistence; if redaction cannot approve the payload, do not store raw sensitive values. |
| Malformed trailing JSONL line | Replay should ignore the malformed tail and preserve valid prior events and artifact links. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| TBD | No direct source-content conflict identified. `docs/PRD.md` has a hash mismatch warning, but the task instructed use as a source-state warning. | `_REFERENCES.md` REF-006 | User task instruction | All sections citing PRD | Treat PRD as accessible direction while preserving unsupported details as `TBD`. | TBD |
