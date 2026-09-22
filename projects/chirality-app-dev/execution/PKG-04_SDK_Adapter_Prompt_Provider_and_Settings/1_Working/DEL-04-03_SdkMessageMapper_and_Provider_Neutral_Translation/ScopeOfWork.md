---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-03
package_id: PKG-04
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-040, SOW-044, SOW-051]
package_objective_refs: [OBJ-002, OBJ-004]
---

# Scope of Work — DEL-04-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-04-03` in service of project scope [SOW-040, SOW-044, SOW-051] and package objectives [OBJ-002, OBJ-004].

- **OUT-001** — App event presentation and conformance to Runtime-owned extensible events: complete upstream preservation after redaction, normalized known views, inspectable unfamiliar notifications, resolved server requests, deterministic presentation and truthful terminal outcomes.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

> #### Datasheet: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-04-03 |
> | Deliverable Name | SdkMessageMapper and Provider-Neutral Translation |
> | Package ID | PKG-04 |
> | Package Name | SDK Adapter, Prompt, Provider, and Settings |
> | Decomposition Variant | SOFTWARE_DECOMP |
> | Decomposition Revision | v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | Responsible Party | TBD |
> | Context Envelope | M |
> | Current Source State | Historical assertions are snapshot-bound; current hash verdict comes from `_REFERENCES.md`. |
>


Current deliverable responsibility: The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

### CLM-003 — Attributes

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

Named verification: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence. Evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

### CLM-004 — Conditions

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

Named verification: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence. Evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

### CLM-005 — Construction

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Record the current implementation/consumer and named verification locations: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence.

Unfinished delivery: Add or recover the repeated-sequence golden, error/permission redaction, unfamiliar-event/request and current adapter-conformance witnesses; retain all missing live-path outcomes as unverified.

### CLM-006 — References

> ##### References
>
> | RefID | Source Slice Used |
> |---|---|
> | REF-001 | `docs/DIRECTIVE.md` Sections 2.8, 2.9, 2.10 and the decision record table covering product-owned contracts, provider-neutral core, SDK metadata posture, and audit mirror canonicality. |
> | REF-003 | `docs/SPEC.md` Sections 10, 11, 12, 14, 15, and 19.3 covering runtime engine boundary, SSE events, SDK settings, tool surface, permission mapping, and validation IDs. |
> | REF-004 | `docs/TYPES.md` Sections 7.1, 7.2, 7.3, 7.4, and 9 covering `SdkMessageMapper`, `HarnessEvent`, `UIEvent`, SDK transcript, and adapter vocabulary. |
> | REF-005 | `docs/PLAN.md` R1 targets and Section 6.3 covering `sdk-message-mapper.ts`, event mapping, and redaction. |
> | REF-006 | `docs/PRD.md` Sections 8.12 and 8.13, used with HASH_MISMATCH warning per task brief. |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-03, SOW-040, SOW-044, SOW-051, OBJ-002, OBJ-004, and OI-001. |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

> #### Specification: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation
>

### CLM-008 — Scope

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

Verification: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence.

### CLM-009 — Requirements

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-04-03-REQ001 | Browser presentation remains an App contract while preserving complete upstream native event information under D-GOV-43. |
| DEL-04-03-REQ002 | Runtime owns canonical event wrapping/persistence; App mapping must not create a competing event authority. |
| DEL-04-03-REQ003 | Preserve upstream names/IDs/payloads after redaction with truthful operational attribution; the legacy adapter-metadata-only restriction does not drop native data. |
| DEL-04-03-REQ004 | Present known event types through normalized views and unfamiliar notifications inspectably; the old closed SSE name list is compatibility history. |
| DEL-04-03-REQ005 | Conform persisted output to the current Runtime-owned versioned event envelope. |
| DEL-04-03-REQ006 | Preserve actual session/turn/model/tool/request/terminal facts when emitted, with exact upstream identity and safe envelope metadata. |
| DEL-04-03-REQ007 | Keep later or unfamiliar event categories representable without claiming unobserved payload semantics. |
| DEL-04-03-REQ008 | Deterministically present a repeated source sequence; verify with IDs and timestamps normalized where nondeterministic by design. |
| DEL-04-03-REQ009 | Retain native model/tool-loop activity in the canonical event stream and corresponding App views. |
| DEL-04-03-REQ010 | Provider transcripts are secondary operational linkage and never authoritative project evidence. |
| DEL-04-03-REQ011 | Maintain supported App route/stream compatibility while applying the extensible native notification/request representation. |
| DEL-04-03-REQ012 | Redact secrets from event/UI outputs, including result-error and permission-message strings, before every sink. |
| DEL-04-03-REQ013 | Preserve success/failure/interruption/cancellation translation; Runtime owns turn-lock cleanup, accepted-turn durability and cancellation classification. |
| DEL-04-03-REQ014 | The historical Claude probe basis is recorded in DEL-04-01; use current native fixtures for live mapping and record every missing fixture explicitly. |

Verification: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence.

Evidence locations: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests. These are hooks and source locations, not newly executed results.

### CLM-010 — Standards

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

Named verification: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence. Evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

### CLM-011 — Verification

Required current checks: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence.

Named evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Add or recover the repeated-sequence golden, error/permission redaction, unfamiliar-event/request and current adapter-conformance witnesses; retain all missing live-path outcomes as unverified.

### CLM-012 — Documentation

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Record the current implementation/consumer and named verification locations: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence.

Unfinished delivery: Add or recover the repeated-sequence golden, error/permission redaction, unfamiliar-event/request and current adapter-conformance witnesses; retain all missing live-path outcomes as unverified.

### CLM-013 — D-APP-56 event-lane amendment (2026-07-12)

> ##### D-APP-56 event-lane amendment (2026-07-12)
>
> R4-P34 adds the `message.delta`, `message.completed`, and `queue.enqueued` lane emitted by `sdk-message-mapper.ts` to the REQ-006 event-category mapping, parallel to the existing `model.*` lane.

- **AC-001** — The App event interface preserves the complete Runtime/Codex stream after structural redaction, presents known and unfamiliar events truthfully, resolves server requests and preserves deterministic presentation/terminal mapping within the Runtime ownership boundary. Historical migration evidence retains its original source basis; current acceptance uses the named live checks.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

> #### Procedure: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation
>

### CLM-015 — Purpose

> ##### Purpose
>
> Define the working procedure to implement and verify the `SdkMessageMapper` deliverable so SDK stream messages are translated into stable browser `UIEvent`s and provider-neutral `HarnessEvent`s without leaking SDK shape into Chirality core contracts.
>

### CLM-016 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Current implementation/adoption evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-017 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.
4. Verify repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence.
5. Retain inputs, source/candidate identity, commands, output and limitations; update Remaining only for backchecked outcomes.

Locus and checks: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-018 — Verification

Required current checks: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence.

Named evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Add or recover the repeated-sequence golden, error/permission redaction, unfamiliar-event/request and current adapter-conformance witnesses; retain all missing live-path outcomes as unverified.

### CLM-019 — Records

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Record the current implementation/consumer and named verification locations: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence.

Unfinished delivery: Add or recover the repeated-sequence golden, error/permission redaction, unfamiliar-event/request and current adapter-conformance witnesses; retain all missing live-path outcomes as unverified.

- **VER-001** — Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

> #### Guidance: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation
>

### CLM-021 — Purpose

> ##### Purpose
>
> This deliverable exists to create a narrow SDK adapter mapping surface: SDK stream messages can power the runtime, but Chirality's browser stream and persisted runtime events remain product-owned, stable, and provider-neutral. The mapper is one of the control points that prevents SDK defaults, transcript shape, message names, or tool names from silently redefining Chirality behavior.
>

### CLM-022 — Principles

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

Named verification: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence. Evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

### CLM-023 — Considerations

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

Named verification: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence. Evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

### CLM-024 — Trade-offs

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

Named verification: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence. Evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

### CLM-025 — Adapter Metadata Rationale

The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve deterministic repeated-sequence presentation, distinct browser and persistence contracts, explicit success/failure/interruption/cancellation, redaction of error and permission strings, replay linkage and safe diagnostics.

Named verification: Repeat a source sequence with IDs/timestamps normalized; verify known and unfamiliar notifications, server-request resolution, terminal translation and synthetic secrets at mapping/SSE/persistence boundaries. Map current K-ENGINE-2 and S-1/S-7 coverage without asserting legacy equivalence. Evidence: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests.

### CLM-026 — Examples

> ##### Examples
>
> Illustrative mappings, subject to DEL-04-01 probe confirmation:
>
> | SDK-side input category | Browser `UIEvent` direction | `HarnessEvent` direction | Notes |
> |---|---|---|---|
> | SDK system/session initialization | `session:init` if the UI needs session start metadata | `sdk.system.init` with adapter metadata | Exact payload fields TBD pending first-adapter probe. |
> | Partial assistant text | `chat:delta` | `model.delta` | Preserve text ordering; avoid embedding raw SDK message object. |
> | Assistant completion/result | `chat:complete` or `session:complete` as appropriate | `model.completed` and/or `turn.completed` | Terminal split depends on TurnEngine contract. |
> | Tool result/progress | `tool:result` for compact UI feedback | `tool.progress`, `tool.completed`, or `tool.failed` | Later category support should be fixture-backed. |
> | Permission denial | `turn:error` only if it is turn-terminal or UI-actionable | `tool.permission` or `turn.failed` depending on contract | Capability-forward policy with explicit hard-deny precedence semantics are owned by policy, not the SDK name. |
> | Compact boundary | Usually no direct UI event unless UI compatibility accepts it | `context.compacted` | Probe exact SDK compact message shape. |
> | Subagent lifecycle | TBD for UI | `subagent.started` / `subagent.completed` | Governed subagent support is later-phase and must remain restricted. |
>

### CLM-027 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. The App maps Runtime events for display and conforms to Root-owned event semantics under SCA-APP-005. It does not create a second canonical writer or own lock cleanup, cancellation classification or turn persistence.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Add or recover the repeated-sequence golden, error/permission redaction, unfamiliar-event/request and current adapter-conformance witnesses; retain all missing live-path outcomes as unverified.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-040 SOW-044 SOW-051 OBJ-002 OBJ-004 | CLM-009  | AC-001 | VER-001 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
