---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-02
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-014, SOW-015, SOW-039]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-05-02` in service of project scope [SOW-014, SOW-015, SOW-039] and package objectives [OBJ-003].

- **OUT-001** — A provider-neutral HarnessEvent schema and append-only JSONL persistence surface that records accepted turns, ordered runtime events, and durable terminal outcomes for the declared project scope and package objective.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

> #### Datasheet: DEL-05-02 HarnessEvent Schema and Append-Only JSONL
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-05-02 |
> | DeliverableName | HarnessEvent Schema and Append-Only JSONL |
> | PackageID | PKG-05 |
> | PackageName | Session Audit, Replay, and Tool Result Records |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ResponsibleParty | TBD |
> | Type | DATA_MODEL_CHANGE |
> | ContextEnvelope | M |
> | ScopeItems | SOW-014, SOW-015, SOW-039 |
> | SupportsObjectives | OBJ-003 |
> | AnticipatedArtifacts | Event schema; JSONL writer; accepted-turn and terminal-event tests |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Runtime audit mirror path | `.chirality/sessions/<sessionId>/events.jsonl` under the canonical vNext session layout | `docs/SPEC.md` Section 8.2, 8.4; `docs/CONTRACT.md` K-EVENT-4 |
> | Event record type | `HarnessEvent` | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | Schema version | `schemaVersion: 1` | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | Required fields | `schemaVersion`, `eventId`, `sessionId`, `timestamp`, `type`, `data` | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | Optional fields | `turnId`, `parentEventId` | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | Data payload | `Record<string, unknown>`; payload contents are event-type specific and must avoid secrets | `docs/SPEC.md` Section 9.1, 9.2; `docs/CONTRACT.md` K-EVENT-6 |
> | Initial event categories | `session.created`, `session.resumed`, `turn.accepted`, `turn.started`, `sdk.system.init`, `model.request.started`, `model.delta`, `model.completed`, `turn.completed`, `turn.failed`, `turn.cancelled` | `docs/SPEC.md` Section 9.3; `docs/TYPES.md` Section 7.3 |
> | Later event categories | Tool, hook, compaction, subagent, and SDK mirror events listed by SPEC/TYPES | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3 |
> | Storage format | Append-only newline-delimited JSON | `docs/SPEC.md` Section 9.2 |
> | Ordering rule | JSONL writes append in write sequence | `docs/SPEC.md` Section 9.2 |
> | Replay tolerance | Replay ignores malformed trailing lines and surfaces diagnostics | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
> | Browser-event separation | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts | `docs/CONTRACT.md` K-EVENT-1; `docs/PRD.md` FR-074 (MATCH source status) — reconciled under D-APP-38 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Accepted-turn durability | Persist `turn.accepted` before SDK/model execution starts | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2 |
> | Terminal durability | Every accepted turn ends with durable success, failure, cancellation, or interruption state | `docs/CONTRACT.md` K-EVENT-3; decomposition SOW-015 |
> | Canonicality | Chirality `events.jsonl` is the product-owned runtime audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3 |
> | Secret handling | Secrets and API keys must not be stored in runtime event payloads, logs, provider errors, or tool artifacts | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6, K-KEY-1 |
> | Large payload handling | Large payloads are stored as artifacts and referenced by path | `docs/SPEC.md` Section 9.2 |
> | Event evolution | Backward-compatible or explicitly versioned schema evolution | `docs/SPEC.md` Section 9.2 |
> | PRD source state | `docs/PRD.md` is accessible but marked `MATCH` in `_REFERENCES.md`; PRD-derived items are used only where aligned with matching SPEC/TYPES/CONTRACT evidence | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Artifact | Construction Target | Source |
> |---|---|---|
> | Event schema | Define `HarnessEvent` type target with stable versioned fields and event categories | `docs/SPEC.md` Section 9.1-9.4; `docs/TYPES.md` Section 7.3 |
> | JSONL writer | Append newline-delimited event records in write sequence; ensure unique event IDs and no secret payloads | `docs/SPEC.md` Section 9.2 |
> | Replay reader support | Ignore malformed trailing lines while preserving valid prior events and surfacing diagnostics | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
> | Accepted-turn test | Verify `turn.accepted` exists before model/SDK execution begins | `docs/CONTRACT.md` K-EVENT-2; decomposition SOW-014 |
> | Terminal-event test | Verify accepted turns persist terminal success/failure/cancellation/interruption outcome | `docs/CONTRACT.md` K-EVENT-3; decomposition SOW-015 |
> | UI/runtime separation test | Verify browser `UIEvent` contracts remain separate from persisted `HarnessEvent`s | `docs/CONTRACT.md` K-EVENT-1 |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` Sections 2.3, governance principles | Runtime event authority and professional-boundary context |
> | REF-002 | `docs/CONTRACT.md` K-EVENT, K-ENGINE, K-KEY invariants | Binding event/storage/redaction constraints |
> | REF-003 | `docs/SPEC.md` Sections 8.2-8.4, 9, 10.1 | Canonical layout, event schema, JSONL rules, runtime contract responsibilities |
> | REF-004 | `docs/TYPES.md` Section 7.3 | `HarnessEvent` type target and event categories |
> | REF-005 | `docs/PLAN.md` R1 | Sequencing context for SDK adoption and session events |
> | REF-006 | `docs/PRD.md` Sections 8.12, 9.4, FR-072-FR-076 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method context only |
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-124 replaces provider-shaped kit wording with the corpus-current provider-neutral HarnessEvent names. UPD-125 records DEP-05-02-007 retired and the 11 ACTIVE / 1 RETIRED register state.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

> #### Specification: DEL-05-02 HarnessEvent Schema and Append-Only JSONL
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable specifies the product-owned `HarnessEvent` schema and append-only JSONL persistence surface for Chirality runtime audit records.
>
> In scope:
>
> - Persist accepted user input as `turn.accepted` before SDK/model execution begins.
> - Persist runtime events and terminal turn outcomes as ordered append-only JSONL.
> - Define event schema fields, event category baseline, writer rules, replay tolerance, and tests for accepted-turn and terminal-event durability.
> - Preserve the separation between compact browser `UIEvent`s and richer persisted `HarnessEvent`s.
>
> Out of scope:
>
> - Tool permission semantics, except where event records must support future permission/tool event categories.
> - Redaction implementation details owned by DEL-05-03, except this deliverable must not permit secrets in event payloads.
> - Runtime replay/transcript view implementation owned by DEL-05-04, except this deliverable must provide replay-safe JSONL semantics.
> - Tool-result artifact budget/storage implementation owned by DEL-05-05, except this deliverable must reference artifacts for large payloads.
> - SDK transcript placement and migration details owned by adjacent session-layout/linkage deliverables, except Chirality `events.jsonl` remains canonical.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ReqID | Requirement | Source |
> |---|---|---|
> | DEL-05-02-RQ-001 | The event record type shall be named `HarnessEvent` and include `schemaVersion`, `eventId`, `sessionId`, `timestamp`, `type`, and `data`. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | DEL-05-02-RQ-002 | `HarnessEvent` may include `turnId` and `parentEventId` when applicable. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | DEL-05-02-RQ-003 | The initial schema version shall be `1`. | `docs/SPEC.md` Section 9.1 |
> | DEL-05-02-RQ-004 | Event IDs shall be unique per event. | `docs/SPEC.md` Section 9.2 |
> | DEL-05-02-RQ-005 | Session event storage shall append newline-delimited JSON records in write sequence. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` FR-073 (MATCH source status) — reconciled under D-APP-38 |
> | DEL-05-02-RQ-006 | `turn.accepted` shall be persisted before SDK/model execution starts. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2 |
> | DEL-05-02-RQ-007 | Every accepted turn shall persist a durable terminal success, failure, cancellation, or interruption outcome. | `docs/CONTRACT.md` K-EVENT-3; decomposition SOW-015 |
> | DEL-05-02-RQ-008 | Replay shall ignore malformed trailing JSONL lines, preserve valid prior records, and surface diagnostics. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
> | DEL-05-02-RQ-009 | Event payloads shall not store secrets or API keys. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6, K-KEY-1 |
> | DEL-05-02-RQ-010 | Large event payloads shall be stored as artifacts and referenced by path. | `docs/SPEC.md` Section 9.2 |
> | DEL-05-02-RQ-011 | Browser `UIEvent`s and persisted `HarnessEvent`s shall remain separate contracts. | `docs/CONTRACT.md` K-EVENT-1 |
> | DEL-05-02-RQ-012 | Core runtime APIs, events, tests, and records shall use Chirality terms; provider/SDK-specific terms may appear only as adapter metadata. | `docs/CONTRACT.md` K-CORE-1, K-ENGINE-4 |
> | DEL-05-02-RQ-013 | Event schema evolution shall be backward-compatible or explicitly versioned. | `docs/SPEC.md` Section 9.2 |
> | DEL-05-02-RQ-014 | The canonical runtime audit mirror shall be `.chirality/sessions/<sessionId>/events.jsonl` or an explicitly configured Chirality-controlled session path. | `docs/DIRECTIVE.md` Section 2.3; `docs/SPEC.md` Section 8.2, 8.4 |
> | DEL-05-02-RQ-015 | Event schema fixtures shall keep later tool, hook, compaction, subagent, and SDK mirror event categories representable without asserting payload-specific semantics before their owning deliverables mature. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3 |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Source |
> |---|---|---|
> | Chirality `HarnessEvent` type target | Governs the event record shape and event category vocabulary | `docs/TYPES.md` Section 7.3 |
> | SPEC Runtime Event Schema | Governs JSONL append rules, event IDs, replay tolerance, secret exclusion, large payload references, and versioning | `docs/SPEC.md` Section 9 |
> | CONTRACT K-EVENT invariants | Binding constraints for UI/runtime separation, accepted-turn persistence, terminal durability, canonical audit mirror, malformed-tail replay, redaction, and tool-result payload handling | `docs/CONTRACT.md` K-EVENT-1 through K-EVENT-7 |
> | Runtime Engine Contract | Requires runtime boundary to persist accepted turns and terminal outcomes while yielding UI events | `docs/SPEC.md` Section 10.1 |
> | PRD runtime requirements | Product requirements FR-072 through FR-076 and related SDK mapping requirements; use with hash warning | `docs/PRD.md` Section 9 / FR table; `_REFERENCES.md` REF-006 MATCH — reconciled under D-APP-38 |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement | Verification Approach |
> |---|---|
> | DEL-05-02-RQ-001 through RQ-004 | Event schema unit tests and serialization fixtures verify required/optional fields, `schemaVersion: 1`, and unique `eventId` behavior. |
> | DEL-05-02-RQ-005 | JSONL writer tests verify append-only newline-delimited writes and write-sequence ordering. |
> | DEL-05-02-RQ-006 | Accepted-turn lifecycle test verifies `turn.accepted` is written before the SDK/model request begins. |
> | DEL-05-02-RQ-007 | Terminal-event tests cover success, failure, cancellation, and interruption outcomes. |
> | DEL-05-02-RQ-008 | Replay tests include a malformed trailing line fixture and confirm valid prior records survive with diagnostics. |
> | DEL-05-02-RQ-009 | Redaction/secret-safety tests or fixtures verify API keys and configured secrets are absent from event payloads. ASSUMPTION: detailed redaction helper tests are owned by DEL-05-03; exact helper or fixture contract remains TBD until that deliverable is accepted. |
> | DEL-05-02-RQ-010 | Large-payload tests verify artifact references instead of inline oversized payloads. ASSUMPTION: storage thresholds are finalized by DEL-05-05; numeric threshold source remains TBD until that deliverable is accepted. |
> | DEL-05-02-RQ-011 through RQ-012 | Mapper/API contract tests verify browser `UIEvent`s remain compact and SDK/provider terms do not leak into canonical event fields except adapter metadata. |
> | DEL-05-02-RQ-013 | Compatibility tests verify older event fixtures replay after additive schema evolution, or require explicit version handling for breaking changes. |
> | DEL-05-02-RQ-014 | Session layout tests verify `.chirality/sessions/<sessionId>/events.jsonl` placement or configured Chirality-controlled override. |
> | DEL-05-02-RQ-015 | Fixture coverage plan verifies later event category names can serialize and replay as versioned `HarnessEvent`s while category-specific payload schemas remain TBD until source or implementation acceptance. |
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required deliverable artifacts:
>
> - `event-schema.ts` or equivalent `HarnessEvent` type definition.
> - `session-events.ts` or equivalent append/replay JSONL API.
> - Serialization fixtures covering initial event categories.
> - Accepted-turn persistence test.
> - Terminal-event persistence test.
> - Malformed-tail replay test.
> - UI/runtime separation test.
> - Later-category fixture coverage plan for tool, hook, compaction, subagent, and SDK mirror event names, with payload-specific fixtures marked TBD until owning deliverables mature.
> - Redaction helper or fixture contract reference from DEL-05-03, currently TBD.
> - Source notes documenting the `docs/PRD.md` MATCH status if PRD text is used to justify implementation behavior not also present in matching sources. (reconciled under D-APP-38).

- **AC-001** — The migrated contract preserves every line of the four legacy production documents and defines the accepted-turn, terminal-outcome, append-only JSONL, malformed-tail replay, UIEvent separation, and secret-exclusion expectations without changing lifecycle authority.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

> #### Procedure: DEL-05-02 HarnessEvent Schema and Append-Only JSONL
>

### CLM-015 — Purpose

> ##### Purpose
>
> Define and verify the deliverable implementation for `HarnessEvent` schema and append-only JSONL runtime event storage. The procedure covers producing the event schema, writer/replay API, and tests required for accepted-turn and terminal-event durability.
>

### CLM-016 — Prerequisites

> ##### Prerequisites
>
> - Deliverable context: `_CONTEXT.md` for DEL-05-02.
> - Decomposition entry: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, DEL-05-02 row.
> - Authoritative sources:
>   - `docs/SPEC.md` Sections 8.2-8.4, 9, 10.1.
>   - `docs/TYPES.md` Section 7.3.
>   - `docs/CONTRACT.md` K-EVENT, K-CORE, K-ENGINE, K-KEY invariants.
>   - `docs/DIRECTIVE.md` Section 2.3.
>   - `docs/PRD.md` Sections 8.12, 9.4, FR-072-FR-076, with HASH_MISMATCH warning from `_REFERENCES.md`.
> - Declared upstream dependencies: TBD - no accepted dependency edges have been extracted yet.
> - Declared downstream dependencies: TBD - no accepted dependency edges have been extracted yet.
> - Extracted active dependency edges are recorded in `Dependencies.csv` and summarized in `_DEPENDENCIES.md`: upstream/interface or constraint edges to DEL-05-01, DEL-03-04, DEL-05-03, DEL-05-05, DEL-03-03, and DEL-04-03, plus downstream enablement of DEL-05-04. Treat these as accepted only to the maturity and satisfaction state recorded in the dependency register.
>

### CLM-017 — Steps

> ##### Steps
>
> 1. Confirm the event storage location.
>    - Use `.chirality/sessions/<sessionId>/events.jsonl` under the canonical vNext session layout, unless a governed Chirality-controlled session root override applies.
>    - Source: `docs/SPEC.md` Sections 8.2 and 8.4.
>
> 2. Define the `HarnessEvent` schema.
>    - Include `schemaVersion: 1`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`.
>    - Keep provider/SDK-specific names out of canonical fields except as adapter metadata.
>    - Source: `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3; `docs/CONTRACT.md` K-CORE-1 and K-ENGINE-4.
>
> 3. Define the supported initial event categories.
>    - Include the initial categories listed in SPEC/TYPES: session, accepted turn, turn started, SDK system init, model request/delta/completion, and terminal turn categories.
>    - Leave later tool/hook/compaction/subagent categories representable without implementing unrelated deliverable behavior.
>    - Source: `docs/SPEC.md` Sections 9.3 and 9.4; `docs/TYPES.md` Section 7.3.
>
> 4. Implement or specify the append API.
>    - Append one newline-delimited JSON event per write.
>    - Preserve write-sequence ordering.
>    - Ensure event IDs are unique.
>    - Prevent secrets from being written into payloads.
>    - Store large payloads as artifacts and reference them by path.
>    - Source: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1.
>
> 5. Implement or specify the replay/read API.
>    - Parse valid prior JSONL records.
>    - Ignore malformed trailing lines.
>    - Surface diagnostics for malformed tail records.
>    - Source: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5.
>
> 6. Connect accepted-turn persistence to the runtime lifecycle.
>    - Persist `turn.accepted` before SDK/model execution starts.
>    - Treat this as a P0 audit boundary, not a UI-only event.
>    - Source: `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2.
>
> 7. Connect terminal-outcome persistence to the runtime lifecycle.
>    - Persist a durable terminal event for success, failure, cancellation, or interruption after an accepted turn.
>    - Source: `docs/CONTRACT.md` K-EVENT-3; decomposition SOW-015.
>
> 8. Preserve UI/runtime separation.
>    - Keep browser SSE event names and compact `UIEvent` payloads separate from persisted `HarnessEvent` payloads.
>    - Ensure SDK messages are mapped through an adapter rather than treated as the browser or persisted event contract.
>    - Source: `docs/CONTRACT.md` K-EVENT-1; `docs/PRD.md` Section 9.4 (HASH_MISMATCH source state).
>
> 9. Document unresolved implementation choices.
>    - Mark event payload schemas by type as TBD unless already supported by source or accepted implementation, including payload-specific schemas for later tool, hook, compaction, subagent, and SDK mirror categories.
>    - Mark artifact threshold values as TBD unless owned and accepted by DEL-05-05.
>    - Mark redaction mechanism details as TBD unless owned and accepted by DEL-05-03.
>

### CLM-018 — Verification

> ##### Verification
>
> - Schema test confirms required fields, optional fields, `schemaVersion: 1`, and event ID uniqueness.
> - Writer test confirms ordered append-only newline-delimited JSON.
> - Lifecycle test confirms `turn.accepted` is persisted before SDK/model execution.
> - Terminal tests confirm success, failure, cancellation, and interruption outcomes are persisted.
> - Replay test confirms malformed trailing JSONL does not discard prior valid events and does surface diagnostics.
> - Separation test confirms browser `UIEvent`s and persisted `HarnessEvent`s remain separate contracts.
> - Secret-safety test confirms API keys and configured secrets are absent from event payload fixtures.
> - Later-category fixture plan confirms tool, hook, compaction, subagent, and SDK mirror event names remain serializable/replayable while category-specific payload schemas remain TBD.
> - Source-state check records that `docs/PRD.md` is HASH_MISMATCH if PRD text is used for verification expectations.
>

### CLM-019 — Records

> ##### Records
>
> - `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` for DEL-05-02.
> - Event schema file or equivalent implementation artifact.
> - JSONL writer/replay implementation artifact.
> - Accepted-turn test fixture/results.
> - Terminal-event test fixture/results.
> - Malformed-tail replay fixture/results.
> - UI/runtime separation test fixture/results.
> - Dependency-edge register snapshot used for implementation handoff.
> - Later-category fixture coverage plan with TBD payload-schema slots.
> - DEL-05-03 redaction helper or fixture contract reference, currently TBD.
> - DEL-05-05 artifact threshold source, currently TBD.
> - TASK run record under `_run_records/`.

- **VER-001** — Verify source-marker parity, schema and identifier closure, then apply the legacy kit’s schema, writer, accepted-turn, terminal-outcome, malformed-tail replay, UI/runtime separation, and secret-safety verification methods.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

> #### Guidance: DEL-05-02 HarnessEvent Schema and Append-Only JSONL
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-021 — Purpose

> ##### Purpose
>
> DEL-05-02 exists to make Chirality runtime work auditable through a product-owned event log. The core outcome is a stable, provider-neutral `HarnessEvent` schema and append-only JSONL writer that records accepted turns, runtime events, and terminal outcomes in `.chirality/sessions/<sessionId>/events.jsonl`.
>
> This deliverable supports OBJ-003: making accepted turns, SDK messages, terminal outcomes, tool activity, and replay auditable through Chirality-owned session records.
>

### CLM-022 — Principles

> ##### Principles
>
> 1. Chirality events are runtime audit records, not project approval records.
>    Source: `docs/DIRECTIVE.md` Section 2.3.
>
> 2. `events.jsonl` is canonical for Chirality runtime governance; SDK transcripts are secondary unless imported into `HarnessEvent` form.
>    Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4.
>
> 3. Persist `turn.accepted` before calling the model/SDK so killed or interrupted turns leave recoverable evidence.
>    Source: `docs/CONTRACT.md` K-EVENT-2; `docs/SPEC.md` Section 10.1.
>
> 4. Every accepted turn should have a terminal persisted outcome so replay can distinguish success, failure, cancellation, and interruption.
>    Source: `docs/CONTRACT.md` K-EVENT-3.
>
> 5. Browser `UIEvent`s and persisted `HarnessEvent`s must stay separate. The browser stream stays compact; the runtime audit log may be richer and versioned.
>    Source: `docs/CONTRACT.md` K-EVENT-1.
>
> 6. Provider/SDK terms should be translated at adapter boundaries. Canonical event fields should remain Chirality-owned and provider-neutral.
>    Source: `docs/CONTRACT.md` K-CORE-1 and K-ENGINE-4.
>
> 7. Secret hygiene applies at the schema boundary. The event API should make it difficult to persist API keys, configured secrets, or unredacted sensitive data.
>    Source: `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1.
>

### CLM-023 — Considerations

> ##### Considerations
>
> - `docs/PRD.md` is marked `MATCH` in `_REFERENCES.md`. PRD requirements such as FR-072 through FR-076 align with matching SPEC/CONTRACT/TYPES sources, but PRD-only interpretations should remain provisional until the hash state is resolved. (reconciled under D-APP-38).
> - `turn.accepted` is part of this deliverable's core slice; broader interrupt cleanup and lifecycle lock release are adjacent concerns owned by DEL-03-04.
> - Redaction is adjacent but not optional. DEL-05-02 should define the event API so redaction can be enforced by DEL-05-03 without schema churn.
> - Tool permission, hook, compaction, subagent, and SDK mirror categories are listed as later event categories in SPEC/TYPES. The initial implementation should not block those categories, but should avoid over-implementing behavior owned by later deliverables.
> - Malformed-tail tolerance matters because append-only JSONL can be interrupted mid-write. Replay should preserve valid prior records and surface diagnostics rather than failing the whole session.
> - Append-only JSONL is sufficient for interrupted-write recovery only when accepted-turn and terminal events are written in sequence and replay treats the final malformed line as diagnostic context rather than as authority over earlier valid records. This bounds recovery to reconstructing durable prior events; it does not approve project state or replace human gate evidence.
> - Large payloads should be artifact references, not inline event blobs. Thresholds and storage policy are deferred to DEL-05-05 unless already established by adjacent implementation.
>

### CLM-024 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Direction |
> |---|---|
> | Rich event payloads vs. stable replay | Prefer stable minimal required fields with event-type-specific `data`; keep schema evolution versioned or backward-compatible. |
> | SDK transcript richness vs. Chirality canonicality | Keep SDK transcripts linked as secondary artifacts; import only selected data into `HarnessEvent` when needed. |
> | Immediate category completeness vs. bounded slice | Implement the initial event categories required for accepted turns and terminal outcomes; leave later tool/hook/subagent semantics to their owning deliverables. |
> | Inline data vs. artifact references | Inline small safe data only; reference large or sensitive data through governed artifact metadata. |
> | PRD detail vs. hash status: MATCH | Use PRD only where corroborated by matching sources, or mark PRD-only details as TBD/ASSUMPTION. — reconciled under D-APP-38 |
>

### CLM-025 — Examples

> ##### Examples
>
> Example `HarnessEvent` shape from `docs/SPEC.md` Section 9.1 and `docs/TYPES.md` Section 7.3:
>
> ```ts
> type HarnessEvent = {
>   schemaVersion: 1;
>   eventId: string;
>   sessionId: string;
>   turnId?: string;
>   parentEventId?: string;
>   timestamp: string;
>   type: string;
>   data: Record<string, unknown>;
> };
> ```
>
> Example event categories from matching SPEC/TYPES sources:
>
> - Initial: `session.created`, `session.resumed`, `turn.accepted`, `turn.started`, `sdk.system.init`, `model.request.started`, `model.delta`, `model.completed`, `turn.completed`, `turn.failed`, `turn.cancelled`.
> - Later: `tool.queued`, `tool.permission`, `tool.started`, `tool.progress`, `tool.completed`, `tool.failed`, `hook.started`, `hook.completed`, `context.compacted`, `subagent.started`, `subagent.completed`, `sdk.mirror.error`.
>

### CLM-026 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> No source-content conflicts were identified during P1/P2 drafting.
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | SOURCE-WARN-001 | `docs/PRD.md` is listed as MATCH in `_REFERENCES.md`; PRD content aligns with matching SPEC/CONTRACT/TYPES slices used here but source state is not clean. | `_REFERENCES.md` REF-006 | `docs/PRD.md` Sections 8.12, 9.4, FR-072-FR-076 | Datasheet References; Specification Standards/Requirements; Guidance Considerations | Use PRD only as corroborating context until reference hash is reconciled. | TBD — reconciled under D-APP-38 |
>

### CLM-027 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-124 replaces provider-shaped kit wording with the corpus-current provider-neutral HarnessEvent names. UPD-125 records DEP-05-02-007 retired and the 11 ACTIVE / 1 RETIRED register state.

### CLM-028 — D-APP-68 coordination-event ownership (2026-07-19)

> ##### D-APP-68 coordination-event ownership (2026-07-19)
>
> D-APP-68 ruling 3 assigns the provider-neutral event vocabulary
> `coordination.notice`, `coordination.update`, and
> `coordination.acknowledged` to DEL-05-02. Each name is a versioned
> `HarnessEvent.type` value persisted through the same append-only
> `.chirality/sessions/<sessionId>/events.jsonl` contract, ordering rule,
> stable identifier requirements, malformed-tail tolerance, and secret-exclusion
> boundary as the other event categories.
>
> This ownership is limited to the canonical event vocabulary and append-only
> event schema. It does not assign coordination-tool descriptors or permissions,
> execute relays or acknowledgments, own managed-child lifecycle/records, or own
> child-output artifact persistence; those surfaces remain with DEL-06-01/02/03
> and DEL-08-05 under the consolidated D-APP-68 mapping.
>
> Source: D-APP-68 ruling 3; live contract evidence at
> `frontend/packages/harness-contract/src/event-schema.ts`.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-014 SOW-015 SOW-039 OBJ-003 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
