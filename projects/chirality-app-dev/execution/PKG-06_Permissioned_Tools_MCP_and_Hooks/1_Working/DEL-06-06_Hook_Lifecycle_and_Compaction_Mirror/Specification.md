# Specification: DEL-06-06 Hook Lifecycle and Compaction Mirror

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Scope

DEL-06-06 specifies the backend feature slice that mirrors SDK or adapter hook lifecycle, terminal finalization, and context-compaction boundaries into Chirality-owned runtime events. It covers hook start, completion, and failure event mapping; `PreCompact` boundary mirroring; Stop/finalization evidence; JSONL append semantics; replay-safe event payload discipline; and tests for `context.compacted` and terminal hook fixtures.

In scope:

- Produce or specify a hook lifecycle mapper that translates hook callbacks into Chirality `HarnessEvent` records.
- Emit safe `hook.started` and `hook.completed` event evidence, including failure outcome handling where supported.
- Mirror SDK/model compaction boundaries into `context.compacted` events when the boundary is available.
- Preserve the product-owned audit mirror in `.chirality/sessions/<id>/events.jsonl`; SDK transcripts remain secondary unless imported into `HarnessEvent` form.
- Connect Stop/finalization callbacks to durable terminal outcome evidence without making SDK hook names the public contract.
- Provide `context.compacted` tests and terminal hook fixtures.

Out of scope:

- Permission-mode decision semantics and `canUseTool` approval mediation, owned by DEL-06-01.
- Write/edit path containment, instruction-root protection, symlink rejection, and edit preconditions, owned primarily by DEL-06-04.
- Bash timeout/capture policy, owned by DEL-06-05.
- Subagent governance bridge behavior beyond preserving hook event compatibility, owned by PKG-08 deliverables.
- Custom context-compaction implementation unless a later governed source update requires fallback behavior.

Sources: `_CONTEXT.md`; decomposition PKG-06 rows; `docs/SPEC.md` Sections 8 through 10 and 15; `docs/CONTRACT.md` Sections 1.4 through 1.6; `docs/TYPES.md` Sections 7 and 8.5; `docs/PRD.md` Section 8.15 with MATCH status. (reconciled under D-APP-38).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-06-06-REQ-001 | The hook lifecycle mapper MUST emit Chirality-owned `HarnessEvent` records rather than exposing SDK hook names as the persisted event contract. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` Section 1.4 K-ENGINE-4 |
| DEL-06-06-REQ-002 | Each emitted runtime event MUST conform to the `HarnessEvent` shape: `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| DEL-06-06-REQ-003 | Runtime event writes MUST append newline-delimited JSONL in write sequence and use unique event IDs. | `docs/SPEC.md` Section 9.2 |
| DEL-06-06-REQ-004 | Hook lifecycle event mapping MUST include `hook.started` and `hook.completed` categories where hook execution evidence is available. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3 |
| DEL-06-06-REQ-005 | Hook failure outcomes MUST preserve fail-closed behavior for write, shell, domain, and subagent actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| DEL-06-06-REQ-006 | The mapper MUST support `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PreCompact`, `Stop`, and subagent hook terms without making exact SDK callback names authoritative in public APIs. | `docs/TYPES.md` Section 8.5; `docs/SPEC.md` Section 10.3 |
| DEL-06-06-REQ-007 | `PreCompact` mirroring MUST persist a compaction boundary when available. | `docs/SPEC.md` Section 15.2; decomposition SOW-061 |
| DEL-06-06-REQ-008 | `context.compacted` events MUST be persisted for compaction boundaries and record replay implications where knowable. | `docs/SPEC.md` Section 9.4; `docs/PRD.md` Section 8.15, MATCH status — reconciled under D-APP-38 |
| DEL-06-06-REQ-009 | Full Chirality event log replay MUST remain possible after compaction; SDK transcript linkage may be preserved but cannot displace `events.jsonl`. | `docs/CONTRACT.md` Section 1.4 K-SDK-3 and Section 1.5 K-EVENT-4; `docs/PLAN.md` R4 |
| DEL-06-06-REQ-010 | Stop/finalization mapping MUST preserve durable terminal outcome evidence for success, failure, cancellation, or interruption. | `docs/CONTRACT.md` Section 1.5 K-EVENT-3; `docs/SPEC.md` Section 15.2 |
| DEL-06-06-REQ-011 | Runtime event payloads MUST NOT store secrets, and large or sensitive payloads MUST be stored as artifacts or redacted according to policy. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |
| DEL-06-06-REQ-012 | SDK-specific values MAY be retained only as explicit adapter metadata fields, not as Chirality public contract identifiers. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` Section 1.4 K-CORE-1 |
| DEL-06-06-REQ-013 | Tests MUST cover `context.compacted` event production and terminal hook fixtures. | `_CONTEXT.md`; `docs/SPEC.md` Section 19 `section9.context_compaction_boundary` |
| DEL-06-06-REQ-014 | Implementation MUST record the `docs/PRD.md` MATCH status for any behavior that depends only on PRD Section 8.15 details. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
| DEL-06-06-REQ-015 | Implementation evidence identifies mapper components (`chirality-hooks.ts`, `sdk-message-mapper.ts`), mapper/terminal/compaction tests (`chirality-hooks.test.ts`, `sdk-message-mapper.test.ts`), replay validation (`session-events.ts` / `session-events.test.ts`), artifact/redaction checks (`tool-result-artifacts.ts` / tests), and the Section 9 runner (`scripts/validate-harness-section9.mjs`). | `_CONTEXT.md`; `docs/SPEC.md` Sections 9.2 and 19; cited live paths |

## Standards

| Standard or governing source | Applicability |
|---|---|
| `docs/CONTRACT.md` Sections 1.4 through 1.6 | Binding invariants for engine contract ownership, runtime audit mirror, SDK transcript secondary status, event durability, redaction, and hook fail-closed behavior. |
| `docs/SPEC.md` Sections 8 through 10 | Session storage, `events.jsonl`, `HarnessEvent` shape, event append rules, event categories, and adapter translation rules. |
| `docs/SPEC.md` Section 15.2 | Required hooks, including PreCompact mirror and Stop/finalization behavior. |
| `docs/TYPES.md` Sections 7 and 8.5 | Runtime vocabulary, event categories, hook terms, and adapter boundary vocabulary. |
| `docs/PLAN.md` R4 | Sequencing and acceptance for compaction mirror and replay preservation. |
| `docs/PRD.md` Section 8.15 | Product requirements for compaction event persistence; use with MATCH status from `_REFERENCES.md`. — reconciled under D-APP-38 |

## Verification

| Requirement | Verification approach |
|---|---|
| DEL-06-06-REQ-001, REQ-012 | Type or mapper tests assert persisted event types use Chirality-owned names and SDK details appear only under explicit adapter metadata. |
| DEL-06-06-REQ-002 | Schema tests validate every emitted hook/compaction/terminal event against `HarnessEvent`. |
| DEL-06-06-REQ-003 | Session event writer tests assert newline-delimited append order and unique event IDs. |
| DEL-06-06-REQ-004 | Hook lifecycle tests invoke start and completion paths and assert `hook.started` and `hook.completed` evidence. |
| DEL-06-06-REQ-005 | Failure fixtures assert failed hook outcomes do not silently allow write, shell, domain, or subagent execution. |
| DEL-06-06-REQ-006 | Mapper tests cover `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PreCompact`, `Stop`, and subagent hook term handling where runtime support exists. |
| DEL-06-06-REQ-007, REQ-008 | `context.compacted` tests assert a compaction boundary event is persisted when the SDK/model emits the boundary. |
| DEL-06-06-REQ-009 | Replay tests assert event log replay remains possible after a compaction event and does not require SDK transcript data as canonical truth. |
| DEL-06-06-REQ-010 | Terminal hook fixtures assert Stop/finalization evidence aligns with durable terminal turn outcomes. |
| DEL-06-06-REQ-011 | Redaction and payload-budget tests assert secrets are excluded and large payloads are artifact-referenced. |
| DEL-06-06-REQ-013 | Section 9 validation includes or points to `section9.context_compaction_boundary`; exact runner path: TBD. |
| DEL-06-06-REQ-014 | Review evidence records the PRD hash warning when PRD-only behavior is cited. |
| DEL-06-06-REQ-015 | Closure review verifies the cited mapper, fixture, replay, artifact/redaction, and Section 9 runner paths exist and remain testable. |

## Documentation

Required implementation evidence:

- Hook lifecycle mapper: `frontend/src/lib/harness/chirality-hooks.ts`; adapter mapping: `frontend/src/lib/harness/sdk-message-mapper.ts`.
- Schema/mapper and terminal/compaction fixtures: `frontend/src/__tests__/lib/chirality-hooks.test.ts` and `sdk-message-mapper.test.ts`.
- Replay validation: `frontend/src/lib/harness/session-events.ts` and `frontend/src/__tests__/lib/session-events.test.ts`.
- Artifact/redaction and payload-budget checks: `frontend/src/lib/harness/tool-result-artifacts.ts`, its tests, and `chirality-hooks.test.ts`.
- Section 9 runner: `frontend/scripts/validate-harness-section9.mjs` with `harness-section9-manifest.json`.
- Residual-risk note for `docs/PRD.md` MATCH under the reconciled D-APP-38 source state. (reconciled under D-APP-38).

## Pass 3 Disposition

| ItemID | Disposition | Evidence reread |
|---|---|---|
| F-001 | Converted to a concrete verification obligation without inventing paths: `context.compacted` and terminal hook evidence must point to exact runner or fixture paths before closure; current path remains `TBD`. | `docs/SPEC.md` Section 19 `section9.context_compaction_boundary`; `_CONTEXT.md` anticipated artifacts |
| F-002 | Incorporated as DEL-06-06-REQ-015 and documentation evidence blockers for mapper, schema tests, terminal fixtures, replay, and redaction or payload-budget checks. | `docs/SPEC.md` Sections 9.2 and 19; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |
| X-002 | Already covered in validation intent but not in path evidence; retained as `TBD` runner/fixture evidence tied to `section9.context_compaction_boundary`. | `docs/SPEC.md` Section 19; `docs/PRD.md` Section 8.14/8.15 validation list, MATCH status — reconciled under D-APP-38 |

## Traceability

| Source item | Covered by |
|---|---|
| SOW-057 Hooks and fail-closed behavior | DEL-06-06-REQ-001 through REQ-006, REQ-010 through REQ-013 |
| SOW-061 Compaction mirror | DEL-06-06-REQ-007 through REQ-009, REQ-013 |
| OBJ-003 Audit and session objective | DEL-06-06-REQ-002, REQ-003, REQ-008 through REQ-010 |
| OBJ-005 Tool governance objective | DEL-06-06-REQ-004 through REQ-006, REQ-011 |
