---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-02
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-014, SOW-015, SOW-039, SOW-082]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-05-02` in service of project scope [SOW-014, SOW-015, SOW-039, SOW-082] and package objectives [OBJ-003].

- **OUT-001** — App consumption/replay conformance to the Runtime-owned extensible event stream and canonical append-only mirror, preserving accepted-turn and durable terminal evidence, safe payload handling, sequence, malformed-tail recovery and SOW-082 proposal audit meaning.

## SCA-APP-010 Gate-5 Current Contract (Controlling)

The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied
2026-09-04 at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged
as `7795b0972cac147869607d994173753e4a2fc232`; active pointer moved as
`311a2f0b811d55315d6eb623130cad0be1417565`) makes the centre dialogue the
invariant primary surface and seats the prompted specification ladder. Where any
earlier current-contract section or older clause in this document disagrees with
the applied row below, this section controls. Earlier sections, clauses, and
evidence remain dated compatibility history and are not deleted.

### Current responsibility

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

### Current acceptance obligations

Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

Implement and verify structural redaction and large-payload handling on live Runtime sinks; add malformed-tail/version/terminal fixtures and verify proposal-interaction replay with the actual SOW-082 producer. Preserve missing spike and native results.

### Seating and rulings

The D-APP-109 extraction and D-APP-110 retargeting are recorded in the existing dependency register; the former pending-extraction note is historical. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction. Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

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


Current deliverable responsibility: Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

### CLM-003 — Attributes

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Named verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

### CLM-004 — Conditions

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Named verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

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
> | REF-006 | `docs/PRD.md` Sections 8.12, 9.4, FR-072-FR-076 | REF-006 is HISTORICAL_MATCH under D-APP-38; the earlier warning is dated history. |
> | REF-007 | `workflows/software-decomp/WORKFLOW.md` | Decomposition method context only |
>


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-124 replaces provider-shaped kit wording with the corpus-current provider-neutral HarnessEvent names. UPD-125 records DEP-05-02-007 retired and the 11 ACTIVE / 1 RETIRED register state.


Current requirement and verification boundary: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

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

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-05-02-RQ-001 | The event record type shall be named `HarnessEvent` and include `schemaVersion`, `eventId`, `sessionId`, `timestamp`, `type`, and `data`. |
| DEL-05-02-RQ-002 | `HarnessEvent` may include `turnId` and `parentEventId` when applicable. |
| DEL-05-02-RQ-003 | Use the Runtime-owned versioned event envelope; retain readable historical schema versions without requiring closed schema v2 adoption. |
| DEL-05-02-RQ-004 | Event IDs shall be unique per event. |
| DEL-05-02-RQ-005 | Session event storage shall append newline-delimited JSON records in write sequence. |
| DEL-05-02-RQ-006 | `turn.accepted` shall be persisted before SDK/model execution starts. |
| DEL-05-02-RQ-007 | Every accepted turn shall persist a durable terminal success, failure, cancellation, or interruption outcome. |
| DEL-05-02-RQ-008 | Replay shall ignore malformed trailing JSONL lines, preserve valid prior records, and surface diagnostics. |
| DEL-05-02-RQ-009 | Event payloads shall not store secrets or API keys. |
| DEL-05-02-RQ-010 | Large event payloads shall be stored as artifacts and referenced by path. |
| DEL-05-02-RQ-011 | Browser `UIEvent`s and persisted `HarnessEvent`s shall remain separate contracts. |
| DEL-05-02-RQ-012 | Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. |
| DEL-05-02-RQ-013 | Event schema evolution shall be backward-compatible or explicitly versioned. |
| DEL-05-02-RQ-014 | Runtime owns the canonical central per-project/session events.jsonl mirror; project-local session paths are legacy sources. |
| DEL-05-02-RQ-015 | Event schema fixtures shall keep later tool, hook, compaction, subagent, and SDK mirror event categories representable without asserting payload-specific semantics before their owning deliverables mature. |

Verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

Evidence locations: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers. These are hooks and source locations, not newly executed results.

### CLM-011 — Standards

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Named verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

### CLM-012 — Verification

Required current checks: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay. With the actual SOW-082 producer, verify once-per-chat-per-trigger offer behavior and replay of a declined trigger through append-only storage and presentation; retain missing producer/results as open evidence.

Named evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Implement and verify structural redaction and large-payload handling on live Runtime sinks; add malformed-tail/version/terminal fixtures and verify proposal-interaction replay with the actual SOW-082 producer. Preserve missing spike and native results.

### CLM-013 — Documentation

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

Unfinished delivery: Implement and verify structural redaction and large-payload handling on live Runtime sinks; add malformed-tail/version/terminal fixtures and verify proposal-interaction replay with the actual SOW-082 producer. Preserve missing spike and native results.

- **AC-001** — The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

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

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

Current implementation/adoption evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-017 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.
4. Verify verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.
5. Retain inputs, source/candidate identity, commands, output and limitations; update governing scope and any selected work graph only for backchecked outcomes.

Locus and checks: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-018 — Verification

Required current checks: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

Named evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Implement and verify structural redaction and large-payload handling on live Runtime sinks; add malformed-tail/version/terminal fixtures and verify proposal-interaction replay with the actual SOW-082 producer. Preserve missing spike and native results.

### CLM-019 — Records

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

Unfinished delivery: Implement and verify structural redaction and large-payload handling on live Runtime sinks; add malformed-tail/version/terminal fixtures and verify proposal-interaction replay with the actual SOW-082 producer. Preserve missing spike and native results.

- **VER-001** — Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-021 — Purpose

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

### CLM-022 — Principles

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Named verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

### CLM-023 — Considerations

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Named verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

### CLM-024 — Trade-offs

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Named verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

### CLM-025 — Examples

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Named verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

### CLM-026 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Implement and verify structural redaction and large-payload handling on live Runtime sinks; add malformed-tail/version/terminal fixtures and verify proposal-interaction replay with the actual SOW-082 producer. Preserve missing spike and native results.

### CLM-027 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-124 replaces provider-shaped kit wording with the corpus-current provider-neutral HarnessEvent names. UPD-125 records DEP-05-02-007 retired and the 11 ACTIVE / 1 RETIRED register state.


Current requirement and verification boundary: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

### CLM-028 — D-APP-68 coordination-event ownership (2026-07-19)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

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


Current requirement and verification boundary: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

Verification: Verify malformed tails, append order, all four terminal outcomes, old/additive event versions, full notifications and server requests, structural redaction, oversized payload references and proposal offered/accepted/declined replay.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-014 SOW-015 SOW-039 SOW-082 OBJ-003 | CLM-010  | AC-001 | VER-001 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |

## Retired status detail (2026-09-23)

These clauses preserve operative meaning from the retired App status source. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R044:** With the actual SOW-082 producer, verify once-per-chat-per-trigger proposal offers and replay of accepted/declined triggers through append-only events and presentation. Closed-schema-v2 compatibility remains bounded to its recorded producer.
