---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-05
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-053, SOW-059]
package_objective_refs: [OBJ-003, OBJ-005]
---

# Scope of Work — DEL-05-05

## Purpose and Objective Traceability

This Scope of Work defines `DEL-05-05` in service of project scope [SOW-053, SOW-059] and package objectives [OBJ-003, OBJ-005].

- **OUT-001** — App consumption, summaries/artifact links and conformance for Runtime tool results under current small-inline and artifact-backed overflow thresholds, preserving exact-byte metadata, redaction and deterministic replay. Distinct medium-band preview remains deferred under D-APP-56 R4-P08; optional full inventory/cleanup remains separately unadopted under D-APP-132.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-05-05 ToolResultStore and Session Artifacts

> #### Datasheet: DEL-05-05 ToolResultStore and Session Artifacts
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-05-05 |
> | DeliverableName | ToolResultStore and Session Artifacts |
> | PackageID | PKG-05 |
> | PackageName | Session Audit, Replay, and Tool Result Records |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | ContextEnvelope | M |
> | ResponsibleParty | TBD |
>

### CLM-003 — Attributes

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Named verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

### CLM-004 — Conditions

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Named verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

### CLM-005 — Construction

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

Unfinished delivery: Implement live Runtime budgeting/artifact production/redaction and App summary/artifact-link conformance at current thresholds; verify D-APP-42 metadata, thresholds, hashes, ordering and session-lifetime behavior. Optional D-APP-116 full inventory/cleanup remains deferred with future adoption gate.

### CLM-006 — Current Discovery State

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

Unfinished delivery: Implement live Runtime budgeting/artifact production/redaction and App summary/artifact-link conformance at current thresholds; verify D-APP-42 metadata, thresholds, hashes, ordering and session-lifetime behavior. Optional D-APP-116 full inventory/cleanup remains deferred with future adoption gate.

### CLM-007 — References

> ##### References
>
> | RefID | Source | Notes |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | HISTORICAL_MATCH. Runtime events explain work and the Chirality audit mirror is canonical. |
> | REF-002 | `docs/CONTRACT.md` | HISTORICAL_MATCH. K-EVENT and K-KEY invariants bind redaction, artifacts, and replay. |
> | REF-003 | `docs/SPEC.md` | HISTORICAL_MATCH. Defines session layout, `HarnessEvent`, append/replay rules, and artifact path references. |
> | REF-004 | `docs/TYPES.md` | HISTORICAL_MATCH. Defines `ToolResultStore`, session terms, `events.jsonl`, and `artifacts/`. |
> | REF-005 | `docs/PLAN.md` | HISTORICAL_MATCH. Places tool-result budgeting in R4 and preserves Chirality ownership of artifact/preview policy. |
> | REF-006 | `docs/PRD.md` | HISTORICAL_MATCH. D-APP-38 authority corpus v2 reconciled the accepted PRD snapshot. |
> | REF-007 | `workflows/software-decomp/WORKFLOW.md` | HISTORICAL_MATCH. Used for decomposition method context only. |


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-05-05 ToolResultStore and Session Artifacts

> #### Specification: DEL-05-05 ToolResultStore and Session Artifacts
>

### CLM-009 — Scope

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

### CLM-010 — Requirements

The distinct medium-band preview representation remains deferred under D-APP-42 and D-APP-56 R4-P08. Current small-inline and artifact-backed overflow behavior under unchanged descriptor thresholds is required; it must not be claimed as implementing the deferred distinct medium band. Adopting that band or changing thresholds/preview limits needs its own governed policy decision and boundary tests. D-APP-132's D-APP-116 inventory/cleanup disposition does not adopt it.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-05-05-REQ-001 | Preserve Runtime-owned central events.jsonl as canonical runtime mirror; provider transcripts remain secondary. |
| DEL-05-05-REQ-002 | Large tool result payloads MUST be stored as artifacts and referenced by path from runtime event metadata. |
| DEL-05-05-REQ-003 | Store applicable tool-result artifacts within the Runtime-owned session artifact contract with safe relative links; App does not create a second generic store. |
| DEL-05-05-REQ-004 | Small text tool results MAY remain inline; overflow uses the current descriptor-defined artifact-backed behavior and metadata. The distinct medium-band preview representation is deferred under D-APP-56 R4-P08, not a present implementation requirement. |
| DEL-05-05-REQ-005 | Artifact metadata MUST include tool name where known, optional turn ID where available, original and stored byte counts, truncation flag, SHA-256 for exact stored bytes, session-lifetime retention policy, and relative artifact path. |
| DEL-05-05-REQ-006 | Runtime events, run logs, tool artifacts, and provider errors MUST redact secrets and avoid storing API keys. |
| DEL-05-05-REQ-007 | Sensitive values MUST NOT be stored in tool artifacts unless a redaction pass has approved the payload. |
| DEL-05-05-REQ-008 | Artifact links and summaries MUST remain replayable from Chirality JSONL plus session metadata even when a malformed trailing JSONL line exists. |
| DEL-05-05-REQ-009 | Tool result storage MUST preserve deterministic replay under concurrent SDK tool activity by relying on ordered append/write sequence metadata rather than arrival ambiguity. |
| DEL-05-05-REQ-010 | Output budget tests MUST verify current small-inline and artifact-backed overflow boundaries, no flooding of chat/model context, and usable summaries/links. Distinct medium-band representation stays deferred under D-APP-56 R4-P08. |
| DEL-05-05-REQ-011 | App consumes/previews Runtime-owned tool-result policy and storage through its published interface; generic custody remains Runtime-owned. |
| DEL-05-05-REQ-012 | Output class byte thresholds, preview length, and artifact naming scheme remain the existing descriptor/artifact-writer policy; persisted artifacts MUST carry SHA-256 checksums and session-lifetime retention metadata, with no TTL, quota, daemon, or release-retention claim authorized. |
| DEL-05-05-REQ-013 | The deterministic replay test for concurrent or interleaved tool-result completions MUST assert the accepted ordering signal: JSONL append/write sequence, `parentEventId` linkage where applicable, or another explicitly accepted event-ordering metadata field. |
| DEL-05-05-REQ-014 | Threshold-boundary verification MUST cover the current descriptor-defined byte thresholds and preview behavior; D-APP-42 does not change those thresholds. |

Verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

Evidence locations: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures. These are hooks and source locations, not newly executed results.

### CLM-011 — Standards

The distinct medium-band preview representation remains deferred under D-APP-42 and D-APP-56 R4-P08. Current small-inline and artifact-backed overflow behavior under unchanged descriptor thresholds is required; it must not be claimed as implementing the deferred distinct medium band. Adopting that band or changing thresholds/preview limits needs its own governed policy decision and boundary tests. D-APP-132's D-APP-116 inventory/cleanup disposition does not adopt it.

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Named verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

### CLM-012 — Verification

The distinct medium-band preview representation remains deferred under D-APP-42 and D-APP-56 R4-P08. Current small-inline and artifact-backed overflow behavior under unchanged descriptor thresholds is required; it must not be claimed as implementing the deferred distinct medium band. Adopting that band or changing thresholds/preview limits needs its own governed policy decision and boundary tests. D-APP-132's D-APP-116 inventory/cleanup disposition does not adopt it.

Required current checks: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

Named evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Implement live Runtime budgeting/artifact production/redaction and App summary/artifact-link conformance at current thresholds; verify D-APP-42 metadata, thresholds, hashes, ordering and session-lifetime behavior. Optional D-APP-116 full inventory/cleanup remains deferred with future adoption gate.

### CLM-013 — Documentation

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

Unfinished delivery: Implement live Runtime budgeting/artifact production/redaction and App summary/artifact-link conformance at current thresholds; verify D-APP-42 metadata, thresholds, hashes, ordering and session-lifetime behavior. Optional D-APP-116 full inventory/cleanup remains deferred with future adoption gate.

### CLM-014 — D-APP-56 child-output partition note (2026-07-12)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-56 child-output partition note (2026-07-12)
>
> R4-P32 assigns `artifacts/subagents/` child-output storage and its 16 KiB/512 KiB thresholds to DEL-08-05. DEL-05-05 continues to own `descriptor.resultBudget`; it does not duplicate child-output artifact ownership.

- **AC-001** — The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-05-05 ToolResultStore and Session Artifacts

> #### Procedure: DEL-05-05 ToolResultStore and Session Artifacts
>

### CLM-016 — Purpose

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

### CLM-017 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

Current implementation/adoption evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-018 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.
4. Verify verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.
5. Retain inputs, source/candidate identity, commands, output and limitations; update Remaining only for backchecked outcomes.

Locus and checks: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-019 — Verification

Required current checks: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

Named evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Implement live Runtime budgeting/artifact production/redaction and App summary/artifact-link conformance at current thresholds; verify D-APP-42 metadata, thresholds, hashes, ordering and session-lifetime behavior. Optional D-APP-116 full inventory/cleanup remains deferred with future adoption gate.

### CLM-020 — Records

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

Unfinished delivery: Implement live Runtime budgeting/artifact production/redaction and App summary/artifact-link conformance at current thresholds; verify D-APP-42 metadata, thresholds, hashes, ordering and session-lifetime behavior. Optional D-APP-116 full inventory/cleanup remains deferred with future adoption gate.

- **VER-001** — Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-05-05 ToolResultStore and Session Artifacts

> #### Guidance: DEL-05-05 ToolResultStore and Session Artifacts
>

### CLM-022 — Purpose

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes.

### CLM-023 — Principles

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Named verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

### CLM-024 — Considerations

> ##### Considerations
>

### CLM-025 — Source-state posture

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Implement live Runtime budgeting/artifact production/redaction and App summary/artifact-link conformance at current thresholds; verify D-APP-42 metadata, thresholds, hashes, ordering and session-lifetime behavior. Optional D-APP-116 full inventory/cleanup remains deferred with future adoption gate.

### CLM-026 — Budget thresholds

The distinct medium-band preview representation remains deferred under D-APP-42 and D-APP-56 R4-P08. Current small-inline and artifact-backed overflow behavior under unchanged descriptor thresholds is required; it must not be claimed as implementing the deferred distinct medium band. Adopting that band or changing thresholds/preview limits needs its own governed policy decision and boundary tests. D-APP-132's D-APP-116 inventory/cleanup disposition does not adopt it.

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Named verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

### CLM-027 — Event and artifact separation

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Named verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

### CLM-028 — Redaction posture

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Named verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

### CLM-029 — Concurrent tool activity

> ###### Concurrent tool activity
>
> The decomposition explicitly includes deterministic replay under tool concurrency. Store enough sequence or parent-event linkage to preserve replay order under interleaved completions. ADQ-10 accepts JSONL append order as the deterministic ordering signal for the interleaved artifact replay fixture.
>
> D-001 is best handled as an assertion-design requirement: replay tests should prove ordering from JSONL write sequence or accepted event-ordering metadata, not from incidental SDK completion order.
>

### CLM-030 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Inline content vs artifact link | Inline improves immediate readability for small text. Artifact links preserve performance and context for large output. Use the budget class, not ad hoc UI convenience, to decide. |
> | Preview richness vs leakage risk | Rich previews help review, but sensitive data must be redacted. Prefer safe summaries when redaction status is uncertain. |
> | SDK transcript detail vs Chirality canonicality | SDK transcripts may contain useful details, but Chirality event metadata and artifact references are the replay authority unless transcript content is imported into `HarnessEvent` form. |
> | Early hardcoded thresholds vs configurable policy | ADQ-10 does not introduce new threshold values. It preserves the current descriptor-defined thresholds and records that future threshold changes need a governed policy update. |
> | Retention/checksum certainty vs premature policy | D-APP-42 chooses SHA-256 for exact stored bytes after redaction/truncation and session-lifetime retention. This gives replay/audit verification without claiming TTL, quota, daemon cleanup, release retention, or broader custody guarantees. |
>

### CLM-031 — Examples

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

Named verification: Verify real live producers, threshold boundaries, current small-inline and artifact-backed overflow behavior (distinct medium-band representation remains deferred), stored-byte hashes/metadata, stream separation, redaction, concurrent completion order, malformed-tail replay and session-lifetime behavior. Existing legacy artifact tests do not establish these live outcomes. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

### CLM-032 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Implement live Runtime budgeting/artifact production/redaction and App summary/artifact-link conformance at current thresholds; verify D-APP-42 metadata, thresholds, hashes, ordering and session-lifetime behavior. Optional D-APP-116 full inventory/cleanup remains deferred with future adoption gate.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-053 SOW-059 OBJ-003 OBJ-005 | CLM-010  | AC-001 | VER-001 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
