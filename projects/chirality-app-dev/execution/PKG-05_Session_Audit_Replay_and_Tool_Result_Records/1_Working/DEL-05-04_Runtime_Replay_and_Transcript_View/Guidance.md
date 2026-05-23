# Guidance: DEL-05-04 Runtime Replay and Transcript View

## Purpose

This deliverable makes Chirality runtime work replayable from product-owned records. The replay surface should let operators and tests reconstruct accepted user turns, assistant output, tool activity summaries, terminal outcomes, diagnostics, artifact references, and SDK transcript linkage without treating SDK transcripts or UI state as canonical truth.

Sources: `_CONTEXT.md`; `docs/DIRECTIVE.md` Sections 2.2-2.3; `docs/SPEC.md` Sections 8-10; `docs/CONTRACT.md` K-EVENT and K-SDK invariants.

## Principles

1. **Replay from Chirality events first.** Use `.chirality/sessions/<sessionId>/events.jsonl` as the canonical replay input. SDK transcripts can help resume/debugging, but they do not replace the Chirality audit mirror. Sources: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4 and K-SDK-3.
2. **Separate UI compactness from audit richness.** Browser `UIEvent`s remain compact while persisted `HarnessEvent`s may carry richer runtime metadata. Replay should not blur those contracts. Sources: `docs/SPEC.md` Sections 10.3 and 11; `docs/CONTRACT.md` K-EVENT-1.
3. **Keep provider-specific details at adapter boundaries.** SDK session IDs, transcript paths, tool names, and message names are useful metadata but must not become public Chirality contract identity. Sources: `docs/SPEC.md` Section 10.3; `docs/DIRECTIVE.md` Section 2.10.
4. **Prefer recoverability over all-or-nothing parsing.** A malformed trailing JSONL record should not destroy access to earlier valid events. Sources: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5.
5. **Do not leak secrets through replay.** Replay output, diagnostics, and artifact summaries should follow redaction and artifact-reference rules. Sources: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6 and K-EVENT-7.

## Considerations

- The replay model should preserve stable identity fields: `sessionId`, `turnId`, and event identity. Stable identifiers persist across path and label changes. Source: `docs/TYPES.md` Sections 1.7-2.
- Terminal outcomes matter as much as streamed text. Accepted turns must end with a durable success, failure, cancellation, or interruption event for reliable replay. Source: `docs/CONTRACT.md` K-EVENT-2 and K-EVENT-3.
- Session metadata can provide SDK linkage (`sdkSessionId`, `sdkTranscriptPath`, `sdkSessionStoreKey`, `sdkResumeMode`) but replay should present it as linkage metadata, not as the transcript authority. Source: `docs/SPEC.md` Sections 8.3-8.4.
- Legacy session records remain a compatibility concern until migration is accepted. Source: `docs/SPEC.md` Section 8.1.
- The exact view model and API shape are not specified in the source corpus. Use `TBD` for module names, route paths, and component names until implementation ownership is assigned.

## Trade-offs

| Topic | Guidance | Rationale |
|---|---|---|
| Strict JSONL parsing vs. tolerant replay | Favor tolerant replay for a malformed final line, while surfacing diagnostics. | Protects audit recoverability after interruption or partial writes. |
| Raw tool output vs. artifact links | Favor compact summaries plus artifact links for large or sensitive results. | Prevents replay views from flooding UI/model context and supports redaction policy. |
| SDK transcript detail vs. Chirality canonicality | Show SDK transcript/store linkage as secondary metadata. | Maintains provider-neutral core and avoids SDK-shaped public contracts. |
| Legacy compatibility vs. clean vNext layout | Keep legacy reads until migration is explicitly complete. | Preserves existing session usability during layout transition. |

## Examples

| Scenario | Expected replay behavior | Source |
|---|---|---|
| Valid event log with accepted turn, model deltas, and completion | Transcript view shows the accepted user input, assistant output, and terminal completion. | `docs/SPEC.md` Sections 9.3-9.4 |
| Event log with malformed final line | Replay ignores the malformed tail, returns prior valid events, and surfaces a diagnostic. | `docs/SPEC.md` Section 9.2 |
| Session metadata includes `sdkTranscriptPath` | Transcript view may link or display the SDK transcript location as secondary metadata; it must keep `events.jsonl` canonical. | `docs/SPEC.md` Section 8.4 |
| Tool result event references an artifact | Transcript view should summarize the tool outcome and link the artifact path rather than inlining raw large content. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-7 |

## Source-State Notes

`docs/PRD.md` is listed in `_REFERENCES.md` with `HASH_MISMATCH`. Per the task brief, this is treated as a source-state warning. PRD-derived replay requirements were used only when consistent with matched sources or clearly labeled with the warning.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None | No content conflict identified in accessible source slices during P1/P2. | N/A | N/A | N/A | N/A | N/A |
