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

- **OUT-001** — A hook lifecycle and compaction mirror that records hook start, progress, completion or failure outcomes, Stop/finalization, and available compaction boundaries as Chirality-owned HarnessEvent records while preserving append-only replay.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-06 Hook Lifecycle and Compaction Mirror

> #### Datasheet: DEL-06-06 Hook Lifecycle and Compaction Mirror
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

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

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary concern | Record hook start/stop/failure, stop/finalization, and SDK compaction boundaries into Chirality events. | `_CONTEXT.md`; decomposition DEL-06-06 row |
> | Canonical runtime audit mirror | `.chirality/sessions/<id>/events.jsonl` is the product-owned Chirality runtime audit mirror. | `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `docs/SPEC.md` Section 8.4 |
> | Event record shape | `HarnessEvent` with `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | Event write behavior | Runtime events are appended as newline-delimited JSONL in write sequence; event IDs are unique. | `docs/SPEC.md` Section 9.2 |
> | Hook event categories | `hook.started`, `hook.completed`, and `context.compacted` are listed as later event categories. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3 |
> | Hook lifecycle terms | `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PreCompact`, `Stop`, `SubagentStart`, and `SubagentStop`. | `docs/TYPES.md` Section 8.5 |
> | Required hook behaviors in scope | PreCompact mirror persists compaction boundary when available; Stop/finalization persists terminal outcome. | `docs/SPEC.md` Section 15.2 |
> | Fail-closed rule | Hook failures fail closed for write, shell, domain, and subagent actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
> | Compaction mirror obligation | Full Chirality event log stays on disk; SDK transcript linkage is preserved; compaction boundaries are mirrored when emitted. | `docs/PRD.md` Section 8.15, MATCH status; `docs/PLAN.md` R4 — reconciled under D-APP-38 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Constraint | Source |
> |---|---|---|
> | PRD source state | `docs/PRD.md` is accessible but has MATCH in `_REFERENCES.md`; PRD-derived details are treated as source-state evidence, not as unqualified accepted truth. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
> | Product-owned contract | SDK messages, external hook names, and SDK-specific IDs must be translated into Chirality-owned contracts; SDK values may appear only as explicit adapter metadata. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` Section 1.4 K-ENGINE-4 |
> | Audit authority | SDK transcripts are secondary runtime artifacts unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` Section 1.4 K-SDK-3; `docs/SPEC.md` Section 8.4 |
> | Secret handling | Runtime events and logs must not store secrets; large payloads must be stored as artifacts and referenced by path. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |
> | Terminal outcome linkage | Every accepted turn must end with a durable success, failure, cancellation, or interruption event. | `docs/CONTRACT.md` Section 1.5 K-EVENT-3 |
> | Hook separation | Path containment and write/edit preconditions are owned primarily by DEL-06-04; DEL-06-06 mirrors lifecycle, failure, terminal, and compaction boundaries into events. | `_CONTEXT.md`; decomposition PKG-06 rows |
> | Dependency state | `_DEPENDENCIES.md` lists no accepted upstream or downstream edges yet. | `_DEPENDENCIES.md` |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Construction note | Source |
> |---|---|---|
> | Hook lifecycle mapper | `frontend/src/lib/harness/chirality-hooks.ts` and `sdk-message-mapper.ts` map SDK/adapter hook callbacks into product-owned `HarnessEvent` records. | `docs/SPEC.md` Sections 9 and 10.3; cited implementation paths |
> | Hook started event | Records safe start evidence for hook execution. Exact payload fields: TBD, but must conform to `HarnessEvent` and avoid secrets. | `docs/SPEC.md` Section 9.1 and 9.2; `docs/TYPES.md` Section 7.3 |
> | Hook completed/failure event | Records hook completion or failure outcome; failure handling must preserve fail-closed behavior for write, shell, domain, and subagent actions. Exact failure taxonomy: TBD. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
> | PreCompact mirror | Emits `context.compacted` when the SDK/model compaction boundary is available. Boundary metadata, preserved recent turns, and replay implications are PRD-specified but source-state qualified. | `docs/SPEC.md` Sections 9.4 and 15.2; `docs/PRD.md` Section 8.15, MATCH status — reconciled under D-APP-38 |
> | Stop/finalization mapper | Connects Stop/finalization callbacks to terminal outcome persistence without replacing TurnEngine terminal records. Exact parent/child event relation: TBD. | `docs/SPEC.md` Section 15.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-3 |
> | Event append integration | Uses `frontend/src/lib/harness/session-events.ts` `appendHarnessEvent` for append-only replay-compatible JSONL and `tool-result-artifacts.ts` for session artifact records. | `docs/SPEC.md` Sections 8.4 and 9.2; cited implementation paths |
> | Validation | Mapper/terminal/compaction fixtures live in `chirality-hooks.test.ts` and `sdk-message-mapper.test.ts`; replay and artifact checks live in `session-events.test.ts` and `tool-result-artifacts.test.ts`; Section 9 runs through `scripts/validate-harness-section9.mjs`. | `_CONTEXT.md`; `docs/SPEC.md` Section 19; cited test/runner paths |
>

### CLM-006 — Pass 3 Disposition

> ##### Pass 3 Disposition
>
> | ItemID | Disposition | Evidence reread |
> |---|---|---|
> | C-001 | Converted to an explicit implementation blocker: the hook lifecycle mapper is required, but the exact module path remains `TBD` until implementation ownership assigns the adapter surface. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-06-06 row; `docs/SPEC.md` Sections 9, 10.3, and 15.2; `docs/TYPES.md` Sections 7.3 and 8.5 |
>

### CLM-007 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-002 | `docs/CONTRACT.md` Sections 1.4 through 1.6 | Binding engine, event, SDK, permission, hook, and audit invariants | MATCH |
> | REF-003 | `docs/SPEC.md` Sections 8 through 10, 15, and 19 | Session layout, `HarnessEvent` schema, adapter translation rules, required hooks, validation IDs | MATCH |
> | REF-004 | `docs/TYPES.md` Sections 7.1 through 7.3 and 8.5 | Runtime vocabulary, event categories, hook terms | MATCH |
> | REF-005 | `docs/PLAN.md` R4 and risk table | Sequencing and compaction acceptance context | MATCH |
> | REF-006 | `docs/PRD.md` Sections 8.15 and runtime event requirements | Product requirements for compaction and hook event recording | MATCH status — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-06-06 Hook Lifecycle and Compaction Mirror

> #### Specification: DEL-06-06 Hook Lifecycle and Compaction Mirror
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-009 — Scope

> ##### Scope
>
> DEL-06-06 specifies the backend feature slice that mirrors SDK or adapter hook lifecycle, terminal finalization, and context-compaction boundaries into Chirality-owned runtime events. It covers hook start, completion, and failure event mapping; `PreCompact` boundary mirroring; Stop/finalization evidence; JSONL append semantics; replay-safe event payload discipline; and tests for `context.compacted` and terminal hook fixtures.
>
> In scope:
>
> - Produce or specify a hook lifecycle mapper that translates hook callbacks into Chirality `HarnessEvent` records.
> - Emit safe `hook.started` and `hook.completed` event evidence, including failure outcome handling where supported.
> - Mirror SDK/model compaction boundaries into `context.compacted` events when the boundary is available.
> - Preserve the product-owned audit mirror in `.chirality/sessions/<id>/events.jsonl`; SDK transcripts remain secondary unless imported into `HarnessEvent` form.
> - Connect Stop/finalization callbacks to durable terminal outcome evidence without making SDK hook names the public contract.
> - Provide `context.compacted` tests and terminal hook fixtures.
>
> Out of scope:
>
> - Permission-mode decision semantics and `canUseTool` approval mediation, owned by DEL-06-01.
> - Write/edit path containment, instruction-root protection, symlink rejection, and edit preconditions, owned primarily by DEL-06-04.
> - Bash timeout/capture policy, owned by DEL-06-05.
> - Subagent governance bridge behavior beyond preserving hook event compatibility, owned by PKG-08 deliverables.
> - Custom context-compaction implementation unless a later governed source update requires fallback behavior.
>
> Sources: `_CONTEXT.md`; decomposition PKG-06 rows; `docs/SPEC.md` Sections 8 through 10 and 15; `docs/CONTRACT.md` Sections 1.4 through 1.6; `docs/TYPES.md` Sections 7 and 8.5; `docs/PRD.md` Section 8.15 with MATCH status. (reconciled under D-APP-38).
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-06-06-REQ-001 | The hook lifecycle mapper MUST emit Chirality-owned `HarnessEvent` records rather than exposing SDK hook names as the persisted event contract. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` Section 1.4 K-ENGINE-4 |
> | DEL-06-06-REQ-002 | Each emitted runtime event MUST conform to the `HarnessEvent` shape: `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | DEL-06-06-REQ-003 | Runtime event writes MUST append newline-delimited JSONL in write sequence and use unique event IDs. | `docs/SPEC.md` Section 9.2 |
> | DEL-06-06-REQ-004 | Hook lifecycle event mapping MUST include `hook.started`, `hook.progress`, and `hook.completed` categories where hook execution evidence is available. Progress mapping MUST preserve available stdout, stderr, and output fields in provider-neutral `HarnessEvent` data. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3; D-APP-56 R4-P04 |
> | DEL-06-06-REQ-005 | Hook failure outcomes MUST preserve fail-closed behavior for write, shell, domain, and subagent actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
> | DEL-06-06-REQ-006 | The mapper MUST support `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PreCompact`, `Stop`, and subagent hook terms without making exact SDK callback names authoritative in public APIs. | `docs/TYPES.md` Section 8.5; `docs/SPEC.md` Section 10.3 |
> | DEL-06-06-REQ-007 | `PreCompact` mirroring MUST persist a compaction boundary when available. | `docs/SPEC.md` Section 15.2; decomposition SOW-061 |
> | DEL-06-06-REQ-008 | `context.compacted` events MUST be persisted for compaction boundaries and record replay implications where knowable. | `docs/SPEC.md` Section 9.4; `docs/PRD.md` Section 8.15, MATCH status — reconciled under D-APP-38 |
> | DEL-06-06-REQ-009 | Full Chirality event log replay MUST remain possible after compaction; SDK transcript linkage may be preserved but cannot displace `events.jsonl`. | `docs/CONTRACT.md` Section 1.4 K-SDK-3 and Section 1.5 K-EVENT-4; `docs/PLAN.md` R4 |
> | DEL-06-06-REQ-010 | Stop/finalization mapping MUST preserve durable terminal outcome evidence for success, failure, cancellation, or interruption. | `docs/CONTRACT.md` Section 1.5 K-EVENT-3; `docs/SPEC.md` Section 15.2 |
> | DEL-06-06-REQ-011 | Runtime event payloads MUST NOT store secrets, and large or sensitive payloads MUST be stored as artifacts or redacted according to policy. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |
> | DEL-06-06-REQ-012 | SDK-specific values MAY be retained only as explicit adapter metadata fields, not as Chirality public contract identifiers. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` Section 1.4 K-CORE-1 |
> | DEL-06-06-REQ-013 | Tests MUST cover `context.compacted` event production and terminal hook fixtures. | `_CONTEXT.md`; `docs/SPEC.md` Section 19 `section9.context_compaction_boundary` |
> | DEL-06-06-REQ-014 | Implementation MUST record the `docs/PRD.md` MATCH status for any behavior that depends only on PRD Section 8.15 details. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
> | DEL-06-06-REQ-015 | Implementation evidence identifies mapper components (`chirality-hooks.ts`, `sdk-message-mapper.ts`), mapper/terminal/compaction tests (`chirality-hooks.test.ts`, `sdk-message-mapper.test.ts`), replay validation (`session-events.ts` / `session-events.test.ts`), artifact/redaction checks (`tool-result-artifacts.ts` / tests), and the Section 9 runner (`scripts/validate-harness-section9.mjs`). | `_CONTEXT.md`; `docs/SPEC.md` Sections 9.2 and 19; cited live paths |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard or governing source | Applicability |
> |---|---|
> | `docs/CONTRACT.md` Sections 1.4 through 1.6 | Binding invariants for engine contract ownership, runtime audit mirror, SDK transcript secondary status, event durability, redaction, and hook fail-closed behavior. |
> | `docs/SPEC.md` Sections 8 through 10 | Session storage, `events.jsonl`, `HarnessEvent` shape, event append rules, event categories, and adapter translation rules. |
> | `docs/SPEC.md` Section 15.2 | Required hooks, including PreCompact mirror and Stop/finalization behavior. |
> | `docs/TYPES.md` Sections 7 and 8.5 | Runtime vocabulary, event categories, hook terms, and adapter boundary vocabulary. |
> | `docs/PLAN.md` R4 | Sequencing and acceptance for compaction mirror and replay preservation. |
> | `docs/PRD.md` Section 8.15 | Product requirements for compaction event persistence; use with MATCH status from `_REFERENCES.md`. — reconciled under D-APP-38 |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement | Verification approach |
> |---|---|
> | DEL-06-06-REQ-001, REQ-012 | Type or mapper tests assert persisted event types use Chirality-owned names and SDK details appear only under explicit adapter metadata. |
> | DEL-06-06-REQ-002 | Schema tests validate every emitted hook/compaction/terminal event against `HarnessEvent`. |
> | DEL-06-06-REQ-003 | Session event writer tests assert newline-delimited append order and unique event IDs. |
> | DEL-06-06-REQ-004 | Mapper and persistence tests assert `hook.progress` is emitted and replayed with available stdout, stderr, and output fields, alongside start and completion evidence. |
> | DEL-06-06-REQ-005 | Failure fixtures assert failed hook outcomes do not silently allow write, shell, domain, or subagent execution. |
> | DEL-06-06-REQ-006 | Mapper tests cover `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PreCompact`, `Stop`, and subagent hook term handling where runtime support exists. |
> | DEL-06-06-REQ-007, REQ-008 | `context.compacted` tests assert a compaction boundary event is persisted when the SDK/model emits the boundary. |
> | DEL-06-06-REQ-009 | Replay tests assert event log replay remains possible after a compaction event and does not require SDK transcript data as canonical truth. |
> | DEL-06-06-REQ-010 | Terminal hook fixtures assert Stop/finalization evidence aligns with durable terminal turn outcomes. |
> | DEL-06-06-REQ-011 | Redaction and payload-budget tests assert secrets are excluded and large payloads are artifact-referenced. |
> | DEL-06-06-REQ-013 | Section 9 validation includes or points to `section9.context_compaction_boundary`; exact runner path: TBD. |
> | DEL-06-06-REQ-014 | Review evidence records the PRD hash warning when PRD-only behavior is cited. |
> | DEL-06-06-REQ-015 | Closure review verifies the cited mapper, fixture, replay, artifact/redaction, and Section 9 runner paths exist and remain testable. |
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required implementation evidence:
>
> - Hook lifecycle mapper: `frontend/src/lib/harness/chirality-hooks.ts`; adapter mapping: `frontend/src/lib/harness/sdk-message-mapper.ts`.
> - Schema/mapper and terminal/compaction fixtures: `frontend/src/__tests__/lib/chirality-hooks.test.ts` and `sdk-message-mapper.test.ts`.
> - Replay validation: `frontend/src/lib/harness/session-events.ts` and `frontend/src/__tests__/lib/session-events.test.ts`.
> - Artifact/redaction and payload-budget checks: `frontend/src/lib/harness/tool-result-artifacts.ts`, its tests, and `chirality-hooks.test.ts`.
> - Section 9 runner: `frontend/scripts/validate-harness-section9.mjs` with `harness-section9-manifest.json`.
> - Residual-risk note for `docs/PRD.md` MATCH under the reconciled D-APP-38 source state. (reconciled under D-APP-38).
>

### CLM-014 — Pass 3 Disposition

> ##### Pass 3 Disposition
>
> | ItemID | Disposition | Evidence reread |
> |---|---|---|
> | F-001 | Converted to a concrete verification obligation without inventing paths: `context.compacted` and terminal hook evidence must point to exact runner or fixture paths before closure; current path remains `TBD`. | `docs/SPEC.md` Section 19 `section9.context_compaction_boundary`; `_CONTEXT.md` anticipated artifacts |
> | F-002 | Incorporated as DEL-06-06-REQ-015 and documentation evidence blockers for mapper, schema tests, terminal fixtures, replay, and redaction or payload-budget checks. | `docs/SPEC.md` Sections 9.2 and 19; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |
> | X-002 | Already covered in validation intent but not in path evidence; retained as `TBD` runner/fixture evidence tied to `section9.context_compaction_boundary`. | `docs/SPEC.md` Section 19; `docs/PRD.md` Section 8.14/8.15 validation list, MATCH status — reconciled under D-APP-38 |
>

### CLM-015 — Traceability

> ##### Traceability
>
> | Source item | Covered by |
> |---|---|
> | SOW-057 Hooks and fail-closed behavior | DEL-06-06-REQ-001 through REQ-006, REQ-010 through REQ-013 |
> | SOW-061 Compaction mirror | DEL-06-06-REQ-007 through REQ-009, REQ-013 |
> | OBJ-003 Audit and session objective | DEL-06-06-REQ-002, REQ-003, REQ-008 through REQ-010 |
> | OBJ-005 Tool governance objective | DEL-06-06-REQ-004 through REQ-006, REQ-011 |

- **AC-001** — The mirror satisfies the preserved DEL-06-06 requirements when hook lifecycle, failure, terminal, and compaction events validate against HarnessEvent, append safely to events.jsonl, preserve fail-closed and replay semantics, avoid secrets, and the cited tests and Section 9 evidence pass.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-06-06 Hook Lifecycle and Compaction Mirror

> #### Procedure: DEL-06-06 Hook Lifecycle and Compaction Mirror
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-017 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and verify the DEL-06-06 hook lifecycle and compaction mirror implementation. It is written for the deliverable artifact, not as an end-user operation runbook.
>

### CLM-018 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Accepted DEL-06-06 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
> | Runtime event schema and event categories | Available in `docs/SPEC.md` Section 9 and `docs/TYPES.md` Section 7.3 |
> | Session audit mirror rules | Available in `docs/SPEC.md` Section 8.4 and `docs/CONTRACT.md` Section 1.5 |
> | Hook vocabulary and required hook behavior | Available in `docs/TYPES.md` Section 8.5 and `docs/SPEC.md` Section 15.2 |
> | Engine adapter translation rules | Available in `docs/SPEC.md` Section 10.3 |
> | Compaction mirror product direction | Available in `docs/PLAN.md` R4; `docs/PRD.md` Section 8.15 is current and MATCH — reconciled under D-APP-38 |
> | Declared upstream dependencies | Human-declared upstream dependencies remain `TBD`; extracted ACTIVE upstream edges exist in `_DEPENDENCIES.md` and must be closure-checked before final acceptance. |
> | Exact implementation file paths | `frontend/src/lib/harness/chirality-hooks.ts`; `sdk-message-mapper.ts`; `session-events.ts`; `tool-result-artifacts.ts` |
> | Exact test fixture paths | `frontend/src/__tests__/lib/chirality-hooks.test.ts`; `sdk-message-mapper.test.ts`; `session-events.test.ts`; `tool-result-artifacts.test.ts`; `frontend/scripts/validate-harness-section9.mjs` |
>

### CLM-019 — Steps

> ##### Steps
>
> 1. Confirm the event contract boundary.
>    - Use `HarnessEvent` as the persisted runtime event shape.
>    - Keep SDK callback names, SDK transcript IDs, and SDK compaction metadata as adapter metadata rather than public Chirality contract fields.
>    - Preserve `events.jsonl` as the canonical audit mirror.
>
> 2. Define or locate the hook lifecycle mapper.
>    - Map supported hook terms from `docs/TYPES.md` Section 8.5: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PreCompact`, `Stop`, `SubagentStart`, and `SubagentStop`.
>    - Keep detailed policy enforcement ownership aligned with adjacent deliverables; this mapper records lifecycle and boundary evidence.
>    - Exact module path: TBD.
>
> 3. Implement hook start evidence.
>    - Emit or stage `hook.started` evidence when a supported hook begins.
>    - Include session and turn linkage where available.
>    - Include safe hook term and target context where available.
>    - Do not include secrets or large raw payloads.
>
> 4. Implement hook completion and failure evidence.
>    - Emit `hook.completed` evidence for successful completion.
>    - For failure outcomes, record safe diagnostics and outcome status without inventing an unregistered public event type unless the event registry is updated.
>    - Ensure failed hooks preserve fail-closed behavior for write, shell, domain, and subagent actions.
>
> 5. Implement `PreCompact` mirroring.
>    - When the SDK/model exposes a compaction boundary, persist `context.compacted`.
>    - Record boundary metadata and replay implications when safe and available.
>    - Mark unavailable SDK-specific fields as `TBD`; do not infer hidden transcript state.
>
> 6. Implement Stop/finalization mapping.
>    - Record finalization evidence associated with the relevant session and turn.
>    - Preserve the existing terminal event contract: accepted turns end with success, failure, cancellation, or interruption evidence.
>    - Avoid duplicate or contradictory terminal outcomes.
>
> 7. Integrate with append-only session event storage.
>    - Append JSONL events in write sequence with unique event IDs.
>    - Keep replay tolerant of malformed trailing lines as required by the session event contract.
>    - Store large or sensitive payloads as session artifacts or redact them according to policy.
>    - Event writer/session-artifact call paths are resolved: `session-events.ts` `appendHarnessEvent` and `tool-result-artifacts.ts`.
>
> 8. Add tests and fixtures.
>    - Add hook lifecycle mapper tests for start, completion, and failure outcomes.
>    - Add `context.compacted` tests for boundary persistence and replay implications.
>    - Add terminal hook fixtures for Stop/finalization behavior.
>    - Add redaction or payload-budget checks for hook/compaction payloads.
>    - Include Section 9 validation linkage for `section9.context_compaction_boundary` where the validation runner expects it.
>
> 9. Record residual gaps and source warnings.
>    - Keep only genuinely unsupported payload fields or linkage policy as `TBD`; the mapper, fixture, replay, artifact, and runner paths above are assigned.
>    - Record the `docs/PRD.md` MATCH status anywhere PRD-only compaction payload details are used. (reconciled under D-APP-38).
>

### CLM-020 — Verification

> ##### Verification
>
> | Check | Expected result |
> |---|---|
> | Event schema | Hook, compaction, and terminal mirror events conform to `HarnessEvent`. |
> | Event append behavior | Events append as newline-delimited JSONL in order with unique event IDs. |
> | Product-owned names | Persisted event types use Chirality names, with SDK details only in adapter metadata. |
> | Hook start | Supported hook execution emits or stages `hook.started` evidence. |
> | Hook completion/failure | Supported hook completion records outcome; failures preserve fail-closed semantics for write, shell, domain, and subagent actions. |
> | Compaction boundary | SDK/model compaction boundary emits `context.compacted` when available. |
> | Replay preservation | Full Chirality event replay remains possible after compaction without relying on SDK transcript as canonical truth. |
> | Stop/finalization | Finalization evidence aligns with exactly one durable terminal outcome for the accepted turn. |
> | Redaction and payload budget | Secrets are absent and large payloads are artifact-referenced or redacted. |
> | PRD warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
>

### CLM-021 — Records

> ##### Records
>
> - Hook lifecycle mapper implementation: `frontend/src/lib/harness/chirality-hooks.ts` and `sdk-message-mapper.ts`.
> - Event schema/mapper and `context.compacted` tests: `frontend/src/__tests__/lib/chirality-hooks.test.ts` and `sdk-message-mapper.test.ts`.
> - Terminal hook fixtures: `frontend/src/__tests__/lib/sdk-message-mapper.test.ts`.
> - Session event replay validation: `frontend/src/lib/harness/session-events.ts` and `frontend/src/__tests__/lib/session-events.test.ts`.
> - Redaction/payload-budget validation: `frontend/src/lib/harness/tool-result-artifacts.ts`, its test, and `chirality-hooks.test.ts`.
> - Section 9 validation: `frontend/scripts/validate-harness-section9.mjs` and `harness-section9-manifest.json`.
> - Review note for PRD MATCH: required under the reconciled D-APP-38 source state. (reconciled under D-APP-38).
> - Dependency-closure note: human-declared upstream dependency status is TBD; extracted ACTIVE edges in `_DEPENDENCIES.md` must be reconciled before closure.
>

### CLM-022 — Pass 3 Disposition

> ##### Pass 3 Disposition
>
> | ItemID | Disposition | Evidence reread |
> |---|---|---|
> | D-001 | Converted to a dependency-closure blocker: the deliverable is not asserted dependency-free; human-declared edges remain `TBD`, while extracted ACTIVE upstream edges require closure review. | `_DEPENDENCIES.md` Declared Upstream and Extracted Dependency Register |
> | D-002 | Rejected as an implementation assumption and replaced with a blocker: event writer/session artifact APIs must be cited from PKG-05/PKG-03 ownership before closure. | `docs/SPEC.md` Sections 8.4 and 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-4 through K-EVENT-7 |
> | E-002 | Incorporated as an explicit records and verification obligation for redaction or payload-budget validation evidence on hook and compaction payloads; evidence path remains `TBD`. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |

- **VER-001** — Run the cited mapper, schema, replay, redaction/payload-budget, terminal-fixture, context.compacted, and Section 9 validation checks against the preserved source requirements.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-06-06 Hook Lifecycle and Compaction Mirror

> #### Guidance: DEL-06-06 Hook Lifecycle and Compaction Mirror
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-024 — Purpose

> ##### Purpose
>
> DEL-06-06 exists to make hook execution, failure, terminal finalization, and SDK/model compaction boundaries auditable in Chirality-owned runtime events. It is an event-mirroring slice, not the owner of every hook policy: path/write hook enforcement is primarily DEL-06-04, permission mediation is DEL-06-01, and this deliverable ensures those hook and compaction boundaries become replayable evidence in `events.jsonl`.
>
> Sources: `_CONTEXT.md`; decomposition PKG-06; `docs/SPEC.md` Sections 8 through 10 and 15.2; `docs/CONTRACT.md` Sections 1.4 through 1.6.
>

### CLM-025 — Principles

> ##### Principles
>
> 1. Chirality event names are the durable contract. SDK hook names and SDK transcript details may be adapter metadata, but persisted runtime semantics should remain `HarnessEvent` records in Chirality terms. Sources: `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` Section 1.4 K-ENGINE-4.
> 2. The audit mirror stays canonical. `.chirality/sessions/<id>/events.jsonl` remains the product-owned audit record even when SDK transcripts assist resume or debugging. Sources: `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `docs/SPEC.md` Section 8.4.
> 3. Hook failure is safety-relevant. Failed hooks cannot be reduced to diagnostics when the attempted action is write, shell, domain, or subagent execution; fail-closed behavior must be preserved. Sources: `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2.
> 4. Compaction must not erase replay. Context compaction can reduce model context, but the full Chirality event log must remain on disk and replayable. Sources: `docs/PLAN.md` R4; `docs/PRD.md` Section 8.15, MATCH status. (reconciled under D-APP-38).
> 5. Terminal outcomes remain durable. Stop/finalization evidence should support, not replace, the TurnEngine/session event obligation that every accepted turn ends in a durable terminal event. Source: `docs/CONTRACT.md` Section 1.5 K-EVENT-3.
>

### CLM-026 — Considerations

> ##### Considerations
>

### CLM-027 — Event Boundary

> ###### Event Boundary
>
> | Topic | Guidance | Source |
> |---|---|---|
> | Event type names | Use `hook.started`, `hook.completed`, and `context.compacted` where they apply. If a distinct failure event type is proposed, treat it as PROPOSAL until the event category registry accepts it; meanwhile encode failure as outcome data under an accepted event type or a versioned extension. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3 |
> | Payload content | Keep payloads replay-useful but safe: IDs, timestamps, hook term, action/tool context, outcome, duration, adapter metadata, and artifact references are plausible; exact fields are TBD until implementation defines the event schema. | `docs/SPEC.md` Section 9.1 and 9.2 |
> | SDK metadata | Store SDK hook names, transcript keys, or compaction metadata only under explicit adapter metadata fields. | `docs/SPEC.md` Section 10.3 |
> | Parent linkage | Use `parentEventId` or turn/session IDs where useful to connect hook events to tool, turn, terminal, or subagent events. Exact linkage policy is TBD until the mapper owns the relationship between hook callbacks and event-writer records. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Sections 7.3 and 8.5 |
>

### CLM-028 — Compaction Mirror

> ###### Compaction Mirror
>
> REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-029 — Terminal Hook Handling

> ###### Terminal Hook Handling
>
> Stop/finalization hooks should be mapped carefully so they do not race or duplicate terminal `turn.completed`, `turn.failed`, `turn.cancelled`, or interruption records. A useful implementation pattern is to make the finalization mapper attach safe hook evidence to the same turn/session lineage while preserving the TurnEngine as terminal outcome owner. Exact implementation: TBD.
>

### CLM-030 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Separate failure event type vs outcome field | The current listed categories include `hook.started` and `hook.completed` but not `hook.failed`. Prefer accepted event categories unless the event registry is explicitly extended. Preserve failure in outcome/status data when needed. |
> | Rich payloads vs redaction | Prefer minimal replay-relevant metadata plus artifact references. Do not store secrets or large raw tool outputs in hook events. Source: `docs/SPEC.md` Section 9.2. |
> | SDK transcript reliance vs Chirality mirror | Use SDK transcript linkage for resume/debug metadata, but never make it the only source needed to replay Chirality runtime history. |
> | Compaction mirror vs custom compaction | Mirror SDK compaction first. Custom compaction is not required by current sources and should remain TBD unless a governed update adds it. Source: `docs/PLAN.md` alternatives table. |
> | Hook enforcement vs hook evidence | DEL-06-06 should not absorb DEL-06-04's path enforcement scope. It records lifecycle/failure/finalization evidence and preserves fail-closed semantics at the mirror boundary. |
>

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

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | TBD | No direct source conflict identified during P1/P2. PRD has a MATCH source state. | `_REFERENCES.md` REF-006 | `docs/PRD.md` Section 8.15 and runtime event requirements | PRD-cited compaction payload details and acceptance wording | Treat PRD as a current MATCH source under the reconciled D-APP-38 source state; prefer CONTRACT/SPEC/TYPES for binding schema and invariants. | TBD — reconciled under D-APP-38 |
>

### CLM-033 — Pass 3 Disposition

> ##### Pass 3 Disposition
>
> | ItemID | Disposition | Evidence reread |
> |---|---|---|
> | C-002 | Already covered as a registry blocker: `hook.failed` is not in the current listed event categories, so failures remain outcome data under accepted event types unless a governed event-registry extension is accepted. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3; `docs/CONTRACT.md` Section 1.6 K-HOOK-1 |
> | X-001 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.15; `docs/SPEC.md` Sections 9.4 and 15.2 — reconciled under D-APP-38 |
> | E-001 | Converted to a tracked linkage-policy blocker: parent/child linkage may use `parentEventId`, `turnId`, or `sessionId`, but the exact policy remains `TBD` until mapper implementation assigns callback-to-event lineage. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Sections 7.3 and 8.5 |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-057 SOW-061 OBJ-003 OBJ-005 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
