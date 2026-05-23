# Procedure: DEL-05-05 ToolResultStore and Session Artifacts

## Purpose

Define the production and verification procedure for implementing `ToolResultStore` and session artifact behavior for DEL-05-05. The procedure focuses on producing the deliverable artifacts named in `_CONTEXT.md`: artifact store, output budget tests, and metadata fixtures.

## Prerequisites

- Confirm the active source corpus listed in `_REFERENCES.md` is available.
- Review `docs/SPEC.md` Sections 8-9 for session layout and `HarnessEvent` append/replay rules.
- Review `docs/CONTRACT.md` K-EVENT-4 through K-EVENT-7 and K-KEY-1 for canonical audit, replay, redaction, and artifact constraints.
- Review `docs/PRD.md` Sections 10.4-10.5 and NFR-017 as source-state-warning input because `_REFERENCES.md` marks PRD as `HASH_MISMATCH`.
- Confirm upstream dependencies once dependency extraction exists. Current `_DEPENDENCIES.md` lists upstream and downstream as TBD.
- Confirm implementation location for `ToolResultStore`. Current source corpus names the concept but does not specify a module path.
- Treat B-001 as unresolved until REF-006 source reconciliation is accepted; PRD-derived artifact-budget details remain warning-qualified.

## Steps

1. Identify the session artifact root.
   - Use canonical `.chirality/sessions/<sessionId>/artifacts/` from `docs/SPEC.md` Section 8.2 unless the runtime is explicitly configured with a Chirality-controlled session root.
   - Keep artifact paths relative in event metadata where required by `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning).

2. Define the tool-result budget policy.
   - Represent small, medium, and large result classes.
   - Keep concrete byte thresholds and preview length as `TBD` until accepted design work supplies values.
   - Ensure the policy can produce inline small data, medium preview plus metadata, and large artifact references.

3. Define the artifact metadata shape.
   - Include tool name, turn ID, byte count, truncation flag, and relative artifact path.
   - ASSUMPTION: Include redaction status or redaction decision reference if the implementation needs audit evidence for sensitive payload handling. Source support exists for redaction before storage, but the exact metadata field is TBD.

4. Implement artifact persistence.
   - Store raw large results under the session artifact folder.
   - Persist compact metadata in Chirality runtime events rather than embedding raw large payloads in `HarnessEvent.data`.
   - Preserve ordered append/write sequence semantics for replay.

5. Implement preview handling.
   - Inline small text results only when within the accepted threshold and after redaction policy permits storage.
   - Generate medium previews that are sufficient for UI scan/replay without full raw output in chat/model context.
   - For large results, show artifact metadata/link plus a bounded preview if permitted by redaction policy.

6. Apply redaction before persistence.
   - Redact API keys and configured secret variants from event data, logs, provider errors, and tool artifacts.
   - Do not store sensitive values unless a redaction pass has approved the payload.

7. Add output budget tests.
   - Cover small inline, medium preview plus metadata, and large raw artifact storage.
   - Include threshold-boundary fixtures once threshold values are accepted.
   - Verify large outputs do not flood chat or model context.
   - For X-001, record exact threshold-boundary tests as pending until byte thresholds and preview limits are accepted.

8. Add metadata and replay fixtures.
   - Assert required metadata fields.
   - Verify relative artifact paths resolve under the session artifact root.
   - Verify valid artifact links remain available when replay ignores a malformed trailing JSONL line.
   - Include interleaved tool-result fixtures for deterministic replay under concurrency.
   - For D-001, assert replay order from JSONL write sequence or accepted event-ordering metadata; do not rely on incidental SDK completion order.

9. Run relevant validation.
   - Run unit and integration tests for the artifact store, event append/replay, redaction, and session metadata.
   - Add or update Section 9 validation coverage when the runtime validation IDs land.

10. Record residual TBDs.
    - If thresholds, naming, checksum, retention, or redaction metadata remain unspecified, leave explicit `TBD` notes in implementation documentation and test TODOs rather than encoding hidden policy.
    - For E-001, explain any accepted retention/deletion, checksum, and redaction-status metadata policy as a balance between audit reconstructability and leakage minimization.

## Verification

| Check | Expected result |
|---|---|
| Session path check | Large artifact payloads are written beneath `.chirality/sessions/<sessionId>/artifacts/` or an approved Chirality-controlled session artifact root. |
| Metadata check | Tool name, turn ID, byte count, truncation flag, and relative artifact path are persisted with the result reference. |
| Budget check | Small, medium, and large outputs take distinct inline/preview/artifact paths. Threshold values remain TBD until accepted. |
| Redaction check | API keys and configured secrets do not appear in event data, logs, provider errors, or stored artifacts. |
| Replay check | Valid prior artifact links survive malformed trailing JSONL during replay. |
| Concurrency check | Interleaved tool completions replay deterministically by write sequence or accepted event ordering metadata. |
| Provider-neutral check | Public contracts and canonical events are Chirality-owned and do not expose SDK-shaped internals except as adapter metadata. |

## Records

- Artifact store implementation path: TBD.
- Output budget test files: TBD.
- Metadata fixture files: TBD.
- Replay fixture files: TBD.
- Redaction fixture files: TBD.
- Residual design decisions: thresholds, preview length, artifact naming, checksum policy, retention/deletion behavior, and optional redaction-status metadata.
- C-001 path disposition: current code discovery found no accepted implementation or fixture paths for this deliverable; all listed paths remain `TBD`.
- F-001 policy disposition: output thresholds, preview length, artifact naming, checksum policy, and retention/deletion behavior remain governed deferrals.
- D-001 verification disposition: concurrent replay checks must bind to write sequence or accepted event-ordering metadata.
- X-001 verification disposition: threshold-boundary checks remain pending until threshold and preview-limit values are accepted.
- E-001 rationale disposition: retention/deletion, checksum, and redaction-status rationale remains pending until the corresponding policies are chosen.
