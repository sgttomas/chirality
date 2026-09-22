---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-06
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-057, SOW-061]
package_objective_refs: [OBJ-003, OBJ-005]
---

# Scope of Work — DEL-06-06

## Purpose and Objective Traceability

This Scope of Work defines `DEL-06-06` in service of project scope [SOW-057, SOW-061] and package objectives [OBJ-003, OBJ-005].

- **OUT-001** — Actual hook/compaction/terminal observation and replay conformance through the complete Runtime/Codex stream, preserving available hook facts, append order, redaction, compaction implications and exactly one noncontradictory durable terminal outcome per accepted turn.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-06 Hook Lifecycle and Compaction Mirror

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-06-06 |
> | Deliverable name | Hook Lifecycle and Compaction Mirror |
> | Package | PKG-06 Permissioned Tools, MCP, and Hooks |
> | Type | BACKEND_FEATURE_SLICE |
> | Responsible party | TBD |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 |
> | Context envelope | M |
> | Scope items | SOW-057, SOW-061 |
> | Objective context | OBJ-003, OBJ-005 |
> | Anticipated artifacts | Hook lifecycle mapper; `context.compacted` tests; terminal hook fixtures |
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger rows SOW-057 and SOW-061.
>


Current deliverable responsibility: Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

### CLM-003 — Attributes

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Named verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

### CLM-004 — Conditions

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Named verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

### CLM-005 — Construction

For each accepted turn, persist exactly one durable terminal outcome. Completion, Stop/finalization and interruption races must not append duplicate or contradictory terminal records. Verify a named completion-versus-Stop race fixture against the live Runtime event store, asserting exactly one terminal event and a truthful final result.

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

Unfinished delivery: Deliver live named compaction/replay and terminal witnesses, identify which hook facts Codex actually emits, and close structural-redaction/artifact gaps with PKG-05. Record any absent native hook or enforcement subject without recreating retired SDK callbacks.

### CLM-006 — Pass 3 Disposition

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Disposition
>
> | ItemID | Disposition | Evidence reread |
> |---|---|---|
> | C-001 | Converted to an explicit implementation blocker: the hook lifecycle mapper is required, but the exact module path remains `TBD` until implementation ownership assigns the adapter surface. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-06-06 row; `docs/SPEC.md` Sections 9, 10.3, and 15.2; `docs/TYPES.md` Sections 7.3 and 8.5 |
>


Current requirement and verification boundary: Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

### CLM-007 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-002 | `docs/CONTRACT.md` Sections 1.4 through 1.6 | Binding engine, event, SDK, permission, hook, and audit invariants | HISTORICAL_MATCH |
> | REF-003 | `docs/SPEC.md` Sections 8 through 10, 15, and 19 | Session layout, `HarnessEvent` schema, adapter translation rules, required hooks, validation IDs | HISTORICAL_MATCH |
> | REF-004 | `docs/TYPES.md` Sections 7.1 through 7.3 and 8.5 | Runtime vocabulary, event categories, hook terms | HISTORICAL_MATCH |
> | REF-005 | `docs/PLAN.md` R4 and risk table | Sequencing and compaction acceptance context | HISTORICAL_MATCH |
> | REF-006 | `docs/PRD.md` Sections 8.15 and runtime event requirements | Product requirements for compaction and hook event recording | HISTORICAL_MATCH status — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-06-06 Hook Lifecycle and Compaction Mirror

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-009 — Scope

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

### CLM-010 — Requirements

For each accepted turn, persist exactly one durable terminal outcome. Completion, Stop/finalization and interruption races must not append duplicate or contradictory terminal records. Verify a named completion-versus-Stop race fixture against the live Runtime event store, asserting exactly one terminal event and a truthful final result.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-06-06-REQ-001 | Preserve all actual Codex hook/notification/request evidence and present known lifecycle facts without dropping unfamiliar data; exact SDK hook names are compatibility evidence. |
| DEL-06-06-REQ-002 | Preserve the Runtime event envelope, version, event/session/turn/parent identity, timestamp, type and safe data. |
| DEL-06-06-REQ-003 | Append unique event records in canonical Runtime write sequence. |
| DEL-06-06-REQ-004 | Represent actual hook start/progress/completion/failure and supplied output where observed; no missing native hook is fabricated or counted as passed. |
| DEL-06-06-REQ-005 | Application-controlled mutating/domain/delegation validation remains fail-closed; native requests obey selected Codex policy, with enforcement evidence recorded separately. |
| DEL-06-06-REQ-006 | Retain legacy PreToolUse/PostToolUse/PostToolUseFailure/PreCompact/Stop/subagent mappings as compatibility evidence; preserve their surviving outcomes from current native facts when emitted. |
| DEL-06-06-REQ-007 | Observe and persist available native compaction boundaries; a callback with a retired SDK name is not required. |
| DEL-06-06-REQ-008 | Preserve the context.compacted semantic requirement and known replay implications; where only generic native notifications exist, record the missing named mapping/verification as delivery work. |
| DEL-06-06-REQ-009 | Full canonical event replay must remain possible after compaction; provider transcript linkage never displaces Runtime events. |
| DEL-06-06-REQ-010 | Preserve exactly one durable actual terminal success/failure/cancellation/interruption outcome per accepted turn; completion/Stop/finalization races must not create duplicate or contradictory records. |
| DEL-06-06-REQ-011 | Apply structural redaction and accepted payload budgets/artifact references before Runtime persistence, SSE and replay sinks. |
| DEL-06-06-REQ-012 | Preserve upstream method names/identifiers/payloads after redaction as directed by D-GOV-43, with clear operational attribution; do not reintroduce a closed neutral vocabulary. |
| DEL-06-06-REQ-013 | Verify live compaction observation, replay implications and terminal outcomes, explicitly identifying absent native hook facts. |
| DEL-06-06-REQ-014 | Bind source-dependent behavior to its evaluated current reference state; historical MATCH is not current qualification. |
| DEL-06-06-REQ-015 | Name the current Runtime supervisor/store/replay and live fixture paths. Legacy hooks, SDK mapper and Section 9 fixtures are evidence only for the paths they exercise. |

Verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

Evidence locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach. These are hooks and source locations, not newly executed results.

### CLM-011 — Standards

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Named verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

### CLM-012 — Verification

Required current checks: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

Named evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Deliver live named compaction/replay and terminal witnesses, identify which hook facts Codex actually emits, and close structural-redaction/artifact gaps with PKG-05. Record any absent native hook or enforcement subject without recreating retired SDK callbacks.

### CLM-013 — Documentation

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

Unfinished delivery: Deliver live named compaction/replay and terminal witnesses, identify which hook facts Codex actually emits, and close structural-redaction/artifact gaps with PKG-05. Record any absent native hook or enforcement subject without recreating retired SDK callbacks.

### CLM-014 — Pass 3 Disposition

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Disposition
>
> | ItemID | Disposition | Evidence reread |
> |---|---|---|
> | F-001 | Converted to a concrete verification obligation without inventing paths: `context.compacted` and terminal hook evidence must point to exact runner or fixture paths before closure; current path remains `TBD`. | `docs/SPEC.md` Section 19 `section9.context_compaction_boundary`; `_CONTEXT.md` anticipated artifacts |
> | F-002 | Incorporated as DEL-06-06-REQ-015 and documentation evidence blockers for mapper, schema tests, terminal fixtures, replay, and redaction or payload-budget checks. | `docs/SPEC.md` Sections 9.2 and 19; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |
> | X-002 | Already covered in validation intent but not in path evidence; retained as `TBD` runner/fixture evidence tied to `section9.context_compaction_boundary`. | `docs/SPEC.md` Section 19; `docs/PRD.md` Section 8.14/8.15 validation list, MATCH status — reconciled under D-APP-38 |
>


Current requirement and verification boundary: Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

### CLM-015 — Traceability

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Named verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

- **AC-001** — Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-06-06 Hook Lifecycle and Compaction Mirror

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-017 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and verify the DEL-06-06 hook lifecycle and compaction mirror implementation. It is written for the deliverable artifact, not as an end-user operation runbook.
>

### CLM-018 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Current implementation/adoption evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-019 — Steps

For each accepted turn, persist exactly one durable terminal outcome. Completion, Stop/finalization and interruption races must not append duplicate or contradictory terminal records. Verify a named completion-versus-Stop race fixture against the live Runtime event store, asserting exactly one terminal event and a truthful final result.

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.
4. Verify verify actual emitted hook coverage, named compaction observation/replay implications, preserved terminal outcomes, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.
5. Retain inputs, source/candidate identity, commands, output and limitations; update Remaining only for backchecked outcomes.

Locus and checks: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-020 — Verification

Required current checks: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

Named evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Deliver live named compaction/replay and terminal witnesses, identify which hook facts Codex actually emits, and close structural-redaction/artifact gaps with PKG-05. Record any absent native hook or enforcement subject without recreating retired SDK callbacks.

### CLM-021 — Records

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

Unfinished delivery: Deliver live named compaction/replay and terminal witnesses, identify which hook facts Codex actually emits, and close structural-redaction/artifact gaps with PKG-05. Record any absent native hook or enforcement subject without recreating retired SDK callbacks.

### CLM-022 — Pass 3 Disposition

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Disposition
>
> | ItemID | Disposition | Evidence reread |
> |---|---|---|
> | D-001 | Converted to a dependency-closure blocker: the deliverable is not asserted dependency-free; human-declared edges remain `TBD`, while extracted ACTIVE upstream edges require closure review. | `_DEPENDENCIES.md` Declared Upstream and Extracted Dependency Register |
> | D-002 | Rejected as an implementation assumption and replaced with a blocker: event writer/session artifact APIs must be cited from PKG-05/PKG-03 ownership before closure. | `docs/SPEC.md` Sections 8.4 and 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-4 through K-EVENT-7 |
> | E-002 | Incorporated as an explicit records and verification obligation for redaction or payload-budget validation evidence on hook and compaction payloads; evidence path remains `TBD`. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |

- **VER-001** — Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-06-06 Hook Lifecycle and Compaction Mirror

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-024 — Purpose

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

### CLM-025 — Principles

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Named verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

### CLM-026 — Considerations

> ##### Considerations
>

### CLM-027 — Event Boundary

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Named verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

### CLM-028 — Compaction Mirror

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Named verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

### CLM-029 — Terminal Hook Handling

For each accepted turn, persist exactly one durable terminal outcome. Completion, Stop/finalization and interruption races must not append duplicate or contradictory terminal records. Verify a named completion-versus-Stop race fixture against the live Runtime event store, asserting exactly one terminal event and a truthful final result.

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Named verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

### CLM-030 — Trade-offs

Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Named verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach.

### CLM-031 — Examples

> ##### Examples
>
> | Scenario | Expected mirror behavior |
> |---|---|
> | `PreToolUse` starts for a governed write attempt | Emit or stage `hook.started` evidence tied to the session/turn/tool context. The path enforcement decision itself is owned by the hook policy implementation. |
> | `PreToolUse` denies or fails for a write action | Preserve fail-closed outcome and record safe diagnostics in hook completion/failure evidence; the write must not execute. |
> | `PostToolUse` completes after a read tool | Record hook completion evidence where runtime support exists; large tool output remains budgeted or artifact-referenced rather than copied into the hook event. |
> | SDK emits a compaction boundary | Persist `context.compacted` with boundary metadata that is safe and available; preserve replay implications and keep full `events.jsonl` on disk. |
> | Stop/finalization callback fires | Record finalization evidence associated with the turn/session while ensuring the durable terminal event remains success, failure, cancellation, or interruption. |
> | SDK transcript is available under a configured store | Cross-reference the transcript linkage as adapter metadata only; `events.jsonl` remains canonical. |
>

### CLM-032 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Deliver live named compaction/replay and terminal witnesses, identify which hook facts Codex actually emits, and close structural-redaction/artifact gaps with PKG-05. Record any absent native hook or enforcement subject without recreating retired SDK callbacks.

### CLM-033 — Pass 3 Disposition

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Disposition
>
> | ItemID | Disposition | Evidence reread |
> |---|---|---|
> | C-002 | Already covered as a registry blocker: `hook.failed` is not in the current listed event categories, so failures remain outcome data under accepted event types unless a governed event-registry extension is accepted. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3; `docs/CONTRACT.md` Section 1.6 K-HOOK-1 |
> | X-001 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.15; `docs/SPEC.md` Sections 9.4 and 15.2 — reconciled under D-APP-38 |
> | E-001 | Converted to a tracked linkage-policy blocker: parent/child linkage may use `parentEventId`, `turnId`, or `sessionId`, but the exact policy remains `TBD` until mapper implementation assigns callback-to-event lineage. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Sections 7.3 and 8.5 |


Current requirement and verification boundary: Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve unique event IDs and write sequence, available hook progress/output/failure data, safe provenance, durable terminal outcomes and replay after compaction. Record compaction boundaries and known replay implications; retain the context.compacted semantic requirement as unresolved where only a generic native notification is stored. Never fabricate a hook that Codex did not emit. Application-controlled mutating/domain/delegation operations retain fail-closed validation; native tools obey selected Codex policy. Redaction and payload budgets apply before sinks.

Verification: Verify actual emitted hook coverage, named compaction observation/replay implications, exactly one noncontradictory terminal outcome per accepted turn including a completion-versus-Stop race fixture, append order and structural redaction/budgets. Map section9.context_compaction_boundary to actual live fixtures; absence of hook evidence remains unknown, not success.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-057 SOW-061 OBJ-003 OBJ-005 | CLM-010  | AC-001 | VER-001 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
