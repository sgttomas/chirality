# Datasheet: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-05-02 |
| DeliverableName | HarnessEvent Schema and Append-Only JSONL |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ResponsibleParty | TBD |
| Type | DATA_MODEL_CHANGE |
| ContextEnvelope | M |
| ScopeItems | SOW-014, SOW-015, SOW-039 |
| SupportsObjectives | OBJ-003 |
| AnticipatedArtifacts | Event schema; JSONL writer; accepted-turn and terminal-event tests |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Runtime audit mirror path | `.chirality/sessions/<sessionId>/events.jsonl` under the canonical vNext session layout | `docs/SPEC.md` Section 8.2, 8.4; `docs/CONTRACT.md` K-EVENT-4 |
| Event record type | `HarnessEvent` | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| Schema version | `schemaVersion: 1` | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| Required fields | `schemaVersion`, `eventId`, `sessionId`, `timestamp`, `type`, `data` | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| Optional fields | `turnId`, `parentEventId` | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| Data payload | `Record<string, unknown>`; payload contents are event-type specific and must avoid secrets | `docs/SPEC.md` Section 9.1, 9.2; `docs/CONTRACT.md` K-EVENT-6 |
| Initial event categories | `session.created`, `session.resumed`, `turn.accepted`, `turn.started`, `sdk.system.init`, `model.request.started`, `model.delta`, `model.completed`, `turn.completed`, `turn.failed`, `turn.cancelled` | `docs/SPEC.md` Section 9.3; `docs/TYPES.md` Section 7.3 |
| Later event categories | Tool, hook, compaction, subagent, and SDK mirror events listed by SPEC/TYPES | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3 |
| Storage format | Append-only newline-delimited JSON | `docs/SPEC.md` Section 9.2 |
| Ordering rule | JSONL writes append in write sequence | `docs/SPEC.md` Section 9.2 |
| Replay tolerance | Replay ignores malformed trailing lines and surfaces diagnostics | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| Browser-event separation | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts | `docs/CONTRACT.md` K-EVENT-1; `docs/PRD.md` FR-074 (MATCH source status) — reconciled under D-APP-38 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Accepted-turn durability | Persist `turn.accepted` before SDK/model execution starts | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2 |
| Terminal durability | Every accepted turn ends with durable success, failure, cancellation, or interruption state | `docs/CONTRACT.md` K-EVENT-3; decomposition SOW-015 |
| Canonicality | Chirality `events.jsonl` is the product-owned runtime audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3 |
| Secret handling | Secrets and API keys must not be stored in runtime event payloads, logs, provider errors, or tool artifacts | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6, K-KEY-1 |
| Large payload handling | Large payloads are stored as artifacts and referenced by path | `docs/SPEC.md` Section 9.2 |
| Event evolution | Backward-compatible or explicitly versioned schema evolution | `docs/SPEC.md` Section 9.2 |
| PRD source state | `docs/PRD.md` is accessible but marked `MATCH` in `_REFERENCES.md`; PRD-derived items are used only where aligned with matching SPEC/TYPES/CONTRACT evidence | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |

## Construction

| Artifact | Construction Target | Source |
|---|---|---|
| Event schema | Define `HarnessEvent` type target with stable versioned fields and event categories | `docs/SPEC.md` Section 9.1-9.4; `docs/TYPES.md` Section 7.3 |
| JSONL writer | Append newline-delimited event records in write sequence; ensure unique event IDs and no secret payloads | `docs/SPEC.md` Section 9.2 |
| Replay reader support | Ignore malformed trailing lines while preserving valid prior events and surfacing diagnostics | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| Accepted-turn test | Verify `turn.accepted` exists before model/SDK execution begins | `docs/CONTRACT.md` K-EVENT-2; decomposition SOW-014 |
| Terminal-event test | Verify accepted turns persist terminal success/failure/cancellation/interruption outcome | `docs/CONTRACT.md` K-EVENT-3; decomposition SOW-015 |
| UI/runtime separation test | Verify browser `UIEvent` contracts remain separate from persisted `HarnessEvent`s | `docs/CONTRACT.md` K-EVENT-1 |

## References

| RefID | Source | Use |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` Sections 2.3, governance principles | Runtime event authority and professional-boundary context |
| REF-002 | `docs/CONTRACT.md` K-EVENT, K-ENGINE, K-KEY invariants | Binding event/storage/redaction constraints |
| REF-003 | `docs/SPEC.md` Sections 8.2-8.4, 9, 10.1 | Canonical layout, event schema, JSONL rules, runtime contract responsibilities |
| REF-004 | `docs/TYPES.md` Section 7.3 | `HarnessEvent` type target and event categories |
| REF-005 | `docs/PLAN.md` R1 | Sequencing context for SDK adoption and session events |
| REF-006 | `docs/PRD.md` Sections 8.12, 9.4, FR-072-FR-076 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method context only |
