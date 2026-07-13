---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-05
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-053, SOW-059]
package_objective_refs: [OBJ-003, OBJ-005]
---

# Scope of Work — DEL-05-05

## Purpose and Objective Traceability

This migration candidate defines `DEL-05-05` in service of project scope [SOW-053, SOW-059] and package objectives [OBJ-003, OBJ-005].

- **OUT-001** — Artifact store, output budget tests, and metadata fixtures that preserve deterministic replay under tool concurrency and keep medium/large tool outputs out of unbounded chat or model context.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-05-05 ToolResultStore and Session Artifacts

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":2,"line_start":1,"source_sha256":"de3c285578887f23499a6c9c5f89e211f3e4308d8359ec7d4df70baf19a05307","target_id":"CLM-001"} -->
#### Datasheet: DEL-05-05 ToolResultStore and Session Artifacts

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":16,"line_start":3,"source_sha256":"de3c285578887f23499a6c9c5f89e211f3e4308d8359ec7d4df70baf19a05307","target_id":"CLM-002"} -->
##### Identification

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

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":29,"line_start":17,"source_sha256":"de3c285578887f23499a6c9c5f89e211f3e4308d8359ec7d4df70baf19a05307","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary purpose | Store and preview medium/large tool outputs under session artifacts without flooding chat or model context. | `_CONTEXT.md` Deliverable Scope; decomposition `DEL-05-05` row |
| Session artifact location | `.chirality/sessions/<sessionId>/artifacts/` for large tool results after redaction/truncation policy has been applied. | `docs/SPEC.md` Sections 8.2, 9.2; `docs/PRD.md` Sections 10.3, 10.5 |
| Canonical audit mirror | `.chirality/sessions/<sessionId>/events.jsonl`; SDK transcripts remain secondary unless imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3 |
| Event linkage | Tool result artifacts must be referenced by path from persisted runtime event metadata. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 |
| Artifact metadata fields | Tool name where known, optional turn ID where available, original and stored byte counts, truncation flag, SHA-256, session-lifetime retention policy, redaction status, and relative artifact path. | `docs/PRD.md` Section 10.5; D-APP-42 |
| Redaction boundary | Runtime events, run logs, tool artifacts, and provider errors must redact secrets and avoid API keys. | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PRD.md` NFR-002 |
| Output budget classes | Small results inline, medium results preview plus metadata, large results artifact plus metadata. | `docs/PRD.md` Section 10.5 |
| Output budget thresholds | Existing descriptor-defined thresholds remain unchanged by D-APP-42. | `frontend/packages/harness-contract/src/tool-descriptor.ts`; D-APP-42 |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":40,"line_start":30,"source_sha256":"de3c285578887f23499a6c9c5f89e211f3e4308d8359ec7d4df70baf19a05307","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Working-root locality | Project execution state, sessions, and tool artifacts live under the selected working root or configured Chirality-controlled session path. | `docs/DIRECTIVE.md` Sections 2.3, 2.8; `docs/SPEC.md` Section 10.2 |
| Replay requirement | JSONL replay must tolerate malformed trailing lines while preserving valid prior events. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| Ordering requirement | JSONL writes must append newline-delimited events in write sequence. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 |
| Concurrent tool activity | Deterministic replay must survive SDK tool concurrency. | Decomposition SOW-053; `docs/SPEC.md` Section 9.2 |
| Model/chat budget | Large outputs must not flood chat or model context. | `docs/PRD.md` NFR-017 and R4 acceptance |
| Sensitive payload storage | Sensitive values must not be stored unless a redaction pass has approved the payload. | `docs/PRD.md` Section 10.5; `docs/CONTRACT.md` K-EVENT-6 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":51,"line_start":41,"source_sha256":"de3c285578887f23499a6c9c5f89e211f3e4308d8359ec7d4df70baf19a05307","target_id":"CLM-005"} -->
##### Construction

| Component | Expected construction | Status |
|---|---|---|
| `ToolResultStore` | Product-owned artifact and preview policy for tool outputs. | Implemented in `frontend/src/lib/harness/tool-result-artifacts.ts` and `frontend/src/lib/harness/tool-evidence.ts` |
| Session artifact writer | Writes artifact results beneath `.chirality/sessions/<sessionId>/artifacts/tools/` and returns relative artifact references, byte counts, SHA-256, and retention metadata. | Implemented in `frontend/src/lib/harness/tool-result-artifacts.ts` |
| Preview builder | Produces inline small results and artifact-backed overflow without unbounded chat/model expansion. | Implemented with current descriptor-defined thresholds |
| Metadata fixture set | Covers tool name, optional turn ID where available, byte counts, SHA-256, session-lifetime retention, truncation flag, relative artifact path, and redaction status. | Covered by focused tests |
| Output budget tests | Verify inline/artifact behavior and no chat/context flooding. | Covered by focused tests |
| Replay fixtures | Verify artifact links remain reconstructible through `events.jsonl` replay, including malformed-tail tolerance and interleaved append order. | Covered by focused tests |

<!-- sow-source-end -->

### CLM-006 — Current Discovery State

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":59,"line_start":52,"source_sha256":"de3c285578887f23499a6c9c5f89e211f3e4308d8359ec7d4df70baf19a05307","target_id":"CLM-006"} -->
##### Current Discovery State

| Topic | Current state | Disposition |
|---|---|---|
| B-001 source-state warning | `_REFERENCES.md` now marks REF-006 `docs/PRD.md` as `MATCH` under D-APP-38 authority corpus v2. | Retired for ADQ-10 scope. |
| C-001 implementation and fixture paths | Accepted implementation and fixture paths are now recorded in `Specification.md`, `Procedure.md`, and ADQ-10 evidence. | Closed for ADQ-10 scope. |
| F-001 unresolved policy fields | D-APP-42 accepts SHA-256 and session-lifetime retention while leaving byte thresholds, preview length, and artifact naming unchanged. | Closed for checksum/retention; no TTL, quota, daemon, or release-retention claim authorized. |

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":70,"line_start":60,"source_sha256":"de3c285578887f23499a6c9c5f89e211f3e4308d8359ec7d4df70baf19a05307","target_id":"CLM-007"} -->
##### References

| RefID | Source | Notes |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | MATCH. Runtime events explain work and the Chirality audit mirror is canonical. |
| REF-002 | `docs/CONTRACT.md` | MATCH. K-EVENT and K-KEY invariants bind redaction, artifacts, and replay. |
| REF-003 | `docs/SPEC.md` | MATCH. Defines session layout, `HarnessEvent`, append/replay rules, and artifact path references. |
| REF-004 | `docs/TYPES.md` | MATCH. Defines `ToolResultStore`, session terms, `events.jsonl`, and `artifacts/`. |
| REF-005 | `docs/PLAN.md` | MATCH. Places tool-result budgeting in R4 and preserves Chirality ownership of artifact/preview policy. |
| REF-006 | `docs/PRD.md` | MATCH. D-APP-38 authority corpus v2 reconciled the accepted PRD snapshot. |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | MATCH. Used for decomposition method context only. |
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-05-05 ToolResultStore and Session Artifacts

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"5e03e9d2edf5560e4c19bcf0733a32d8998ebe346a34af18f5262bb7e0d64f77","target_id":"CLM-008"} -->
#### Specification: DEL-05-05 ToolResultStore and Session Artifacts

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":22,"line_start":3,"source_sha256":"5e03e9d2edf5560e4c19bcf0733a32d8998ebe346a34af18f5262bb7e0d64f77","target_id":"CLM-009"} -->
##### Scope

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

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":41,"line_start":23,"source_sha256":"5e03e9d2edf5560e4c19bcf0733a32d8998ebe346a34af18f5262bb7e0d64f77","target_id":"CLM-010"} -->
##### Requirements

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

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":56,"line_start":42,"source_sha256":"5e03e9d2edf5560e4c19bcf0733a32d8998ebe346a34af18f5262bb7e0d64f77","target_id":"CLM-011"} -->
##### Standards

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

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":70,"line_start":57,"source_sha256":"5e03e9d2edf5560e4c19bcf0733a32d8998ebe346a34af18f5262bb7e0d64f77","target_id":"CLM-012"} -->
##### Verification

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

<!-- sow-source-end -->

### CLM-013 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":82,"line_start":71,"source_sha256":"5e03e9d2edf5560e4c19bcf0733a32d8998ebe346a34af18f5262bb7e0d64f77","target_id":"CLM-013"} -->
##### Documentation

Required implementation artifacts for this deliverable:

- Artifact store implementation path: `frontend/src/lib/harness/tool-result-artifacts.ts`.
- Output budget tests for inline/artifact overflow behavior: `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` and `frontend/src/__tests__/lib/tool-evidence.test.ts`.
- Metadata fixtures covering required artifact metadata fields: `frontend/src/__tests__/lib/tool-result-artifacts.test.ts`, `frontend/src/__tests__/lib/sdk-message-mapper.test.ts`, and `frontend/src/__tests__/lib/transcript-replay.test.ts`.
- Replay fixtures with artifact references and malformed-tail JSONL tolerance: `frontend/src/__tests__/lib/session-events.test.ts`.
- Redaction fixtures for sensitive tool output handling: `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` and `frontend/src/__tests__/lib/session-events.test.ts`.
- Developer notes identifying that D-APP-42 chose SHA-256 plus session-lifetime retention while leaving thresholds, preview length, and naming unchanged.
- P3 disposition record for B-001, C-001, F-001, D-001, X-001, and E-001 showing which items were retired, incorporated, or explicitly left outside ADQ-10.

<!-- sow-source-end -->

### CLM-014 — D-APP-56 child-output partition note (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":85,"line_start":83,"source_sha256":"5e03e9d2edf5560e4c19bcf0733a32d8998ebe346a34af18f5262bb7e0d64f77","target_id":"CLM-014"} -->
##### D-APP-56 child-output partition note (2026-07-12)

R4-P32 assigns `artifacts/subagents/` child-output storage and its 16 KiB/512 KiB thresholds to DEL-08-05. DEL-05-05 continues to own `descriptor.resultBudget`; it does not duplicate child-output artifact ownership.
<!-- sow-source-end -->

- **AC-001** — The artifact store, output-budget behavior, metadata fixtures, redaction boundary, and replay ordering satisfy the preserved source requirements for SOW-053 and SOW-059 without changing the accepted threshold, preview-length, naming, or lifecycle policies.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-05-05 ToolResultStore and Session Artifacts

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"8728b8dfdcb9257426265b4c59e797e8515847d721c41a6edb9467be90c64da0","target_id":"CLM-015"} -->
#### Procedure: DEL-05-05 ToolResultStore and Session Artifacts

<!-- sow-source-end -->

### CLM-016 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"8728b8dfdcb9257426265b4c59e797e8515847d721c41a6edb9467be90c64da0","target_id":"CLM-016"} -->
##### Purpose

Define the production and verification procedure for implementing `ToolResultStore` and session artifact behavior for DEL-05-05. The procedure focuses on producing the deliverable artifacts named in `_CONTEXT.md`: artifact store, output budget tests, and metadata fixtures.

<!-- sow-source-end -->

### CLM-017 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":16,"line_start":7,"source_sha256":"8728b8dfdcb9257426265b4c59e797e8515847d721c41a6edb9467be90c64da0","target_id":"CLM-017"} -->
##### Prerequisites

- Confirm the active source corpus listed in `_REFERENCES.md` is available.
- Review `docs/SPEC.md` Sections 8-9 for session layout and `HarnessEvent` append/replay rules.
- Review `docs/CONTRACT.md` K-EVENT-4 through K-EVENT-7 and K-KEY-1 for canonical audit, replay, redaction, and artifact constraints.
- Review `docs/PRD.md` Sections 10.4-10.5 and NFR-017 from the D-APP-38 authority corpus v2; `_REFERENCES.md` records REF-006 as `MATCH`.
- Confirm upstream dependencies in `Dependencies.csv`; ADQ-10 closes the REF-006 source-state warning, implementation path, checksum, retention, and interleaved replay residuals.
- Use `frontend/src/lib/harness/tool-result-artifacts.ts` as the artifact persistence implementation path.
- Treat B-001 as retired by the D-APP-38 authority corpus v2 reconciliation.

<!-- sow-source-end -->

### CLM-018 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":65,"line_start":17,"source_sha256":"8728b8dfdcb9257426265b4c59e797e8515847d721c41a6edb9467be90c64da0","target_id":"CLM-018"} -->
##### Steps

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

<!-- sow-source-end -->

### CLM-019 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":77,"line_start":66,"source_sha256":"8728b8dfdcb9257426265b4c59e797e8515847d721c41a6edb9467be90c64da0","target_id":"CLM-019"} -->
##### Verification

| Check | Expected result |
|---|---|
| Session path check | Large artifact payloads are written beneath `.chirality/sessions/<sessionId>/artifacts/` or an approved Chirality-controlled session artifact root. |
| Metadata check | Tool name where known, optional turn ID where available, byte counts, truncation flag, SHA-256, session-lifetime retention policy, and relative artifact path are persisted with the result reference. |
| Budget check | Small and artifact-overflow outputs follow the current descriptor-defined policy without changing thresholds. |
| Redaction check | API keys and configured secrets do not appear in event data, logs, provider errors, or stored artifacts. |
| Replay check | Valid prior artifact links survive malformed trailing JSONL during replay. |
| Concurrency check | Interleaved tool completions replay deterministically by write sequence or accepted event ordering metadata. |
| Provider-neutral check | Public contracts and canonical events are Chirality-owned and do not expose SDK-shaped internals except as adapter metadata. |

<!-- sow-source-end -->

### CLM-020 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":90,"line_start":78,"source_sha256":"8728b8dfdcb9257426265b4c59e797e8515847d721c41a6edb9467be90c64da0","target_id":"CLM-020"} -->
##### Records

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
<!-- sow-source-end -->

- **VER-001** — Validate the candidate, prove complete source-range parity, derive the exact acceptance checklist, render the offline derivative deterministically, and execute the source-defined artifact, budget, metadata, redaction, malformed-tail replay, and concurrency-ordering checks.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-05-05 ToolResultStore and Session Artifacts

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-021"} -->
#### Guidance: DEL-05-05 ToolResultStore and Session Artifacts

<!-- sow-source-end -->

### CLM-022 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":8,"line_start":3,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-022"} -->
##### Purpose

This deliverable exists to keep tool-heavy runtime work auditable and readable. Tool results must be available for replay and diagnosis, but large payloads must not be pushed unbounded into chat, browser events, or model context. Chirality owns the artifact/preview policy even when the SDK supplies the tool loop.

Sources: `_CONTEXT.md`; decomposition `DEL-05-05`; `docs/DIRECTIVE.md` Sections 2.3 and 2.8; `docs/PLAN.md` R4; `docs/PRD.md` Sections 9.4 and 10.5; D-APP-42.

<!-- sow-source-end -->

### CLM-023 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":17,"line_start":9,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-023"} -->
##### Principles

- Keep `events.jsonl` canonical. Runtime artifact metadata should point from Chirality events to stored outputs; artifact storage must not make SDK transcripts or chat history the authority. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4.
- Budget output by representation. Small text can be inline, medium output needs preview plus metadata, and large output needs artifact storage plus a compact reference. Source: `docs/PRD.md` Section 10.5.
- Preserve replay before convenience. A user reviewing a session later should be able to reconstruct tool summaries, terminal outcomes, and artifact links from Chirality JSONL plus session metadata. Source: `docs/PRD.md` FR-076 and NFR-017; `docs/SPEC.md` Section 9.2.
- Redact before storing sensitive content. Secrets must not land in runtime events, run logs, provider errors, or tool artifacts. Source: `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1.
- Keep provider details out of product contracts. `ToolResultStore` should operate on Chirality event/session concepts, not SDK-native transcript shapes. Source: `docs/PRD.md` Section 9.4; `docs/CONTRACT.md` K-ENGINE-4.
- Make policy boundaries explicit. D-APP-42 accepts SHA-256 checksums and session-lifetime retention, leaves thresholds, preview length, and naming unchanged, and authorizes no TTL, quota, daemon, or release-retention claim.

<!-- sow-source-end -->

### CLM-024 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":19,"line_start":18,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-024"} -->
##### Considerations

<!-- sow-source-end -->

### CLM-025 — Source-state posture

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":23,"line_start":20,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-025"} -->
###### Source-state posture

D-APP-38 authority corpus v2 reconciles `docs/PRD.md`; `_REFERENCES.md` records REF-006 as `MATCH`. Historical B-001 source-state warnings are retired for the ADQ-10 scope.

<!-- sow-source-end -->

### CLM-026 — Budget thresholds

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":29,"line_start":24,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-026"} -->
###### Budget thresholds

The runtime already defines tool-specific byte thresholds in `frontend/packages/harness-contract/src/tool-descriptor.ts`. D-APP-42 deliberately leaves those values and the artifact naming scheme unchanged, so ADQ-10 validation should verify current behavior rather than introduce new policy.

F-001 and X-001 remain linked for future threshold changes: if thresholds or preview limits are changed later, that change needs a governed policy decision plus boundary tests. ADQ-10 does not alter those values.

<!-- sow-source-end -->

### CLM-027 — Event and artifact separation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":33,"line_start":30,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-027"} -->
###### Event and artifact separation

Avoid embedding raw large payloads in `HarnessEvent.data`. Store the payload under session artifacts and persist metadata sufficient for replay. This keeps UI events compact and prevents model-context flooding while preserving audit evidence.

<!-- sow-source-end -->

### CLM-028 — Redaction posture

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":37,"line_start":34,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-028"} -->
###### Redaction posture

The safest implementation shape is a redaction decision before artifact persistence. If source uncertainty remains about whether a payload contains secrets, prefer redacted preview and blocked raw storage over saving unreviewed sensitive output.

<!-- sow-source-end -->

### CLM-029 — Concurrent tool activity

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":43,"line_start":38,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-029"} -->
###### Concurrent tool activity

The decomposition explicitly includes deterministic replay under tool concurrency. Store enough sequence or parent-event linkage to preserve replay order under interleaved completions. ADQ-10 accepts JSONL append order as the deterministic ordering signal for the interleaved artifact replay fixture.

D-001 is best handled as an assertion-design requirement: replay tests should prove ordering from JSONL write sequence or accepted event-ordering metadata, not from incidental SDK completion order.

<!-- sow-source-end -->

### CLM-030 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":53,"line_start":44,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-030"} -->
##### Trade-offs

| Trade-off | Guidance |
|---|---|
| Inline content vs artifact link | Inline improves immediate readability for small text. Artifact links preserve performance and context for large output. Use the budget class, not ad hoc UI convenience, to decide. |
| Preview richness vs leakage risk | Rich previews help review, but sensitive data must be redacted. Prefer safe summaries when redaction status is uncertain. |
| SDK transcript detail vs Chirality canonicality | SDK transcripts may contain useful details, but Chirality event metadata and artifact references are the replay authority unless transcript content is imported into `HarnessEvent` form. |
| Early hardcoded thresholds vs configurable policy | ADQ-10 does not introduce new threshold values. It preserves the current descriptor-defined thresholds and records that future threshold changes need a governed policy update. |
| Retention/checksum certainty vs premature policy | D-APP-42 chooses SHA-256 for exact stored bytes after redaction/truncation and session-lifetime retention. This gives replay/audit verification without claiming TTL, quota, daemon cleanup, release retention, or broader custody guarantees. |

<!-- sow-source-end -->

### CLM-031 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":63,"line_start":54,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-031"} -->
##### Examples

| Scenario | Expected behavior |
|---|---|
| Small text result | Store result inline in the tool completion event data when it is within the current descriptor-defined small-output threshold and contains no unredacted secrets. |
| Medium text result | Store a bounded preview and required metadata; avoid placing the full raw result in chat/model context. |
| Large result | Store payload under `.chirality/sessions/<sessionId>/artifacts/`; persist relative artifact path, tool name where known, optional turn ID where available, byte counts, truncation flag, SHA-256, and session-lifetime retention in event metadata. |
| Sensitive tool output | Apply redaction before event/artifact persistence; if redaction cannot approve the payload, do not store raw sensitive values. |
| Malformed trailing JSONL line | Replay should ignore the malformed tail and preserve valid prior events and artifact links. |

<!-- sow-source-end -->

### CLM-032 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":69,"line_start":64,"source_sha256":"b4a5ac1a2f5e572770b23e36c28fd7e378d8f24f9eee990baf9ede10eb1761d4","target_id":"CLM-032"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| NONE | No direct source-content conflict remains open for ADQ-10. REF-006 is `MATCH` under D-APP-38 authority corpus v2, and D-APP-42 resolves checksum/retention policy. | `_REFERENCES.md` REF-006; D-APP-42 | `docs/PRD.md` Sections 10.4-10.5 and NFR-017 | All sections citing PRD; artifact metadata policy | Use matched PRD source plus D-APP-42 for checksum/retention; preserve thresholds, preview length, and naming unchanged. | ACCEPTED |
| B-001 | RETIRED: PRD-derived tool-result budgeting and metadata claims are no longer warning-qualified for this scope because REF-006 now matches the accepted authority corpus. | `_REFERENCES.md` REF-006 | D-APP-38 authority corpus v2 | Datasheet Attributes; Specification Requirements; Procedure Steps | Retire B-001 source-state caveat. | ACCEPTED |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-053 SOW-059 OBJ-003 OBJ-005 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
