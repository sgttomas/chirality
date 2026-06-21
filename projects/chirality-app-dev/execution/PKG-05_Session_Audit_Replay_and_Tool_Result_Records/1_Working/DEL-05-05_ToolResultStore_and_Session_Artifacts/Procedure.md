# Procedure: DEL-05-05 ToolResultStore and Session Artifacts

## Purpose

Define the production and verification procedure for implementing `ToolResultStore` and session artifact behavior for DEL-05-05. The procedure focuses on producing the deliverable artifacts named in `_CONTEXT.md`: artifact store, output budget tests, and metadata fixtures.

## Prerequisites

- Confirm the active source corpus listed in `_REFERENCES.md` is available.
- Review `docs/SPEC.md` Sections 8-9 for session layout and `HarnessEvent` append/replay rules.
- Review `docs/CONTRACT.md` K-EVENT-4 through K-EVENT-7 and K-KEY-1 for canonical audit, replay, redaction, and artifact constraints.
- Review `docs/PRD.md` Sections 10.4-10.5 and NFR-017 from the D-APP-38 authority corpus v2; `_REFERENCES.md` records REF-006 as `MATCH`.
- Confirm upstream dependencies in `Dependencies.csv`; ADQ-10 closes the REF-006 source-state warning, implementation path, checksum, retention, and interleaved replay residuals.
- Use `frontend/src/lib/harness/tool-result-artifacts.ts` as the artifact persistence implementation path.
- Treat B-001 as retired by the D-APP-38 authority corpus v2 reconciliation.

## Steps

1. Identify the session artifact root.
   - Use canonical `.chirality/sessions/<sessionId>/artifacts/` from `docs/SPEC.md` Section 8.2 unless the runtime is explicitly configured with a Chirality-controlled session root.
   - Keep artifact paths relative in event metadata where required by `docs/PRD.md` Section 10.5.

2. Define the tool-result budget policy.
   - Represent small, medium, and large result classes.
   - Use the existing descriptor-defined byte thresholds and preview behavior; D-APP-42 leaves thresholds, preview length, and naming unchanged.
   - Ensure the policy can produce inline small data, medium preview plus metadata, and large artifact references.

3. Define the artifact metadata shape.
   - Include tool name where known, optional turn ID where available, original and stored byte counts, truncation flag, SHA-256 checksum for the exact stored bytes after redaction/truncation, session-lifetime retention policy, redaction status, and relative artifact path.

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
   - For X-001, use the current descriptor-defined threshold and overflow tests; do not introduce new threshold values in ADQ-10.

8. Add metadata and replay fixtures.
   - Assert required metadata fields.
   - Verify relative artifact paths resolve under the session artifact root.
   - Verify valid artifact links remain available when replay ignores a malformed trailing JSONL line.
   - Include interleaved tool-result fixtures for deterministic replay under concurrency.
   - For D-001, assert replay order from JSONL write sequence or accepted event-ordering metadata; do not rely on incidental SDK completion order.

9. Run relevant validation.
   - Run unit and integration tests for the artifact store, event append/replay, redaction, and session metadata.
   - Add or update Section 9 validation coverage when the runtime validation IDs land.

10. Record residual policy boundaries.
    - If future work changes thresholds, preview length, naming, redaction-status policy, or retention beyond session lifetime, record a new governed decision before changing implementation behavior.
    - For E-001, record D-APP-42's balance: SHA-256 supports audit verification of exact stored bytes, while session-lifetime retention avoids TTL, quota, daemon, release-retention, or broader custody claims.

## Verification

| Check | Expected result |
|---|---|
| Session path check | Large artifact payloads are written beneath `.chirality/sessions/<sessionId>/artifacts/` or an approved Chirality-controlled session artifact root. |
| Metadata check | Tool name where known, optional turn ID where available, byte counts, truncation flag, SHA-256, session-lifetime retention policy, and relative artifact path are persisted with the result reference. |
| Budget check | Small and artifact-overflow outputs follow the current descriptor-defined policy without changing thresholds. |
| Redaction check | API keys and configured secrets do not appear in event data, logs, provider errors, or stored artifacts. |
| Replay check | Valid prior artifact links survive malformed trailing JSONL during replay. |
| Concurrency check | Interleaved tool completions replay deterministically by write sequence or accepted event ordering metadata. |
| Provider-neutral check | Public contracts and canonical events are Chirality-owned and do not expose SDK-shaped internals except as adapter metadata. |

## Records

- Artifact store implementation path: `frontend/src/lib/harness/tool-result-artifacts.ts`.
- Output budget test files: `frontend/src/__tests__/lib/tool-result-artifacts.test.ts`, `frontend/src/__tests__/lib/tool-evidence.test.ts`, and SDK mapping coverage in `frontend/src/__tests__/lib/sdk-message-mapper.test.ts`.
- Metadata fixture files: `frontend/src/__tests__/lib/tool-result-artifacts.test.ts`, `frontend/src/__tests__/lib/sdk-message-mapper.test.ts`, and `frontend/src/__tests__/lib/transcript-replay.test.ts`.
- Replay fixture files: `frontend/src/__tests__/lib/session-events.test.ts`.
- Redaction fixture files: `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` and `frontend/src/__tests__/lib/session-events.test.ts`.
- Residual design decisions: thresholds, preview length, and artifact naming remain the existing descriptor/artifact-writer policy and are unchanged by D-APP-42; no TTL, quota, daemon, or release-retention policy is claimed.
- C-001 path disposition: accepted implementation and fixture paths are recorded above.
- F-001 policy disposition: D-APP-42 accepts SHA-256 and session-lifetime retention; thresholds, preview length, and naming remain unchanged.
- D-001 verification disposition: `session-events.test.ts` includes an interleaved tool artifact replay fixture that asserts JSONL append order and checksum metadata.
- X-001 verification disposition: current descriptor threshold and overflow tests exist; ADQ-10 did not change threshold values.
- E-001 rationale disposition: SHA-256 verifies stored bytes after redaction/truncation; session-lifetime retention preserves session replay without expanding into release/distribution retention claims.
