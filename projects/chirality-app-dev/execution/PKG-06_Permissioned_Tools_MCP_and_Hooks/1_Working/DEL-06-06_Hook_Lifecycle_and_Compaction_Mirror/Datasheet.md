# Datasheet: DEL-06-06 Hook Lifecycle and Compaction Mirror

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-06-06 |
| Deliverable name | Hook Lifecycle and Compaction Mirror |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Type | BACKEND_FEATURE_SLICE |
| Responsible party | TBD |
| Decomposition variant | SOFTWARE_DECOMP v3.2 |
| Context envelope | M |
| Scope items | SOW-057, SOW-061 |
| Objective context | OBJ-003, OBJ-005 |
| Anticipated artifacts | Hook lifecycle mapper; `context.compacted` tests; terminal hook fixtures |

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger rows SOW-057 and SOW-061.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary concern | Record hook start/stop/failure, stop/finalization, and SDK compaction boundaries into Chirality events. | `_CONTEXT.md`; decomposition DEL-06-06 row |
| Canonical runtime audit mirror | `.chirality/sessions/<id>/events.jsonl` is the product-owned Chirality runtime audit mirror. | `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `docs/SPEC.md` Section 8.4 |
| Event record shape | `HarnessEvent` with `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| Event write behavior | Runtime events are appended as newline-delimited JSONL in write sequence; event IDs are unique. | `docs/SPEC.md` Section 9.2 |
| Hook event categories | `hook.started`, `hook.completed`, and `context.compacted` are listed as later event categories. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3 |
| Hook lifecycle terms | `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PreCompact`, `Stop`, `SubagentStart`, and `SubagentStop`. | `docs/TYPES.md` Section 8.5 |
| Required hook behaviors in scope | PreCompact mirror persists compaction boundary when available; Stop/finalization persists terminal outcome. | `docs/SPEC.md` Section 15.2 |
| Fail-closed rule | Hook failures fail closed for write, shell, domain, and subagent actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| Compaction mirror obligation | Full Chirality event log stays on disk; SDK transcript linkage is preserved; compaction boundaries are mirrored when emitted. | `docs/PRD.md` Section 8.15, HASH_MISMATCH warning; `docs/PLAN.md` R4 |

## Conditions

| Condition | Constraint | Source |
|---|---|---|
| PRD source state | `docs/PRD.md` is accessible but has HASH_MISMATCH in `_REFERENCES.md`; PRD-derived details are treated as source-state-warning evidence, not as unqualified accepted truth. | `_REFERENCES.md` REF-006 |
| Product-owned contract | SDK messages, external hook names, and SDK-specific IDs must be translated into Chirality-owned contracts; SDK values may appear only as explicit adapter metadata. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` Section 1.4 K-ENGINE-4 |
| Audit authority | SDK transcripts are secondary runtime artifacts unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` Section 1.4 K-SDK-3; `docs/SPEC.md` Section 8.4 |
| Secret handling | Runtime events and logs must not store secrets; large payloads must be stored as artifacts and referenced by path. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |
| Terminal outcome linkage | Every accepted turn must end with a durable success, failure, cancellation, or interruption event. | `docs/CONTRACT.md` Section 1.5 K-EVENT-3 |
| Hook separation | Path containment and write/edit preconditions are owned primarily by DEL-06-04; DEL-06-06 mirrors lifecycle, failure, terminal, and compaction boundaries into events. | `_CONTEXT.md`; decomposition PKG-06 rows |
| Dependency state | `_DEPENDENCIES.md` lists no accepted upstream or downstream edges yet. | `_DEPENDENCIES.md` |

## Construction

| Component | Construction note | Source |
|---|---|---|
| Hook lifecycle mapper | Maps SDK or adapter hook callbacks into Chirality `HarnessEvent` records while preserving product-owned event type names. Exact module path: TBD. | `docs/SPEC.md` Sections 9 and 10.3; `docs/TYPES.md` Section 8.5 |
| Hook started event | Records safe start evidence for hook execution. Exact payload fields: TBD, but must conform to `HarnessEvent` and avoid secrets. | `docs/SPEC.md` Section 9.1 and 9.2; `docs/TYPES.md` Section 7.3 |
| Hook completed/failure event | Records hook completion or failure outcome; failure handling must preserve fail-closed behavior for write, shell, domain, and subagent actions. Exact failure taxonomy: TBD. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| PreCompact mirror | Emits `context.compacted` when the SDK/model compaction boundary is available. Boundary metadata, preserved recent turns, and replay implications are PRD-specified but source-state-warning qualified. | `docs/SPEC.md` Sections 9.4 and 15.2; `docs/PRD.md` Section 8.15, HASH_MISMATCH warning |
| Stop/finalization mapper | Connects Stop/finalization callbacks to terminal outcome persistence without replacing TurnEngine terminal records. Exact parent/child event relation: TBD. | `docs/SPEC.md` Section 15.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-3 |
| Event append integration | Uses append-only session event storage and replay-compatible JSONL behavior. Exact writer API: TBD. | `docs/SPEC.md` Sections 8.4 and 9.2 |
| Validation | Include `context.compacted` tests and terminal hook fixtures; Section 9 validation includes `section9.context_compaction_boundary`. Exact test paths: TBD. | `_CONTEXT.md`; `docs/SPEC.md` Section 19 |

## References

| RefID | Source | Use | Source state |
|---|---|---|---|
| REF-002 | `docs/CONTRACT.md` Sections 1.4 through 1.6 | Binding engine, event, SDK, permission, hook, and audit invariants | MATCH |
| REF-003 | `docs/SPEC.md` Sections 8 through 10, 15, and 19 | Session layout, `HarnessEvent` schema, adapter translation rules, required hooks, validation IDs | MATCH |
| REF-004 | `docs/TYPES.md` Sections 7.1 through 7.3 and 8.5 | Runtime vocabulary, event categories, hook terms | MATCH |
| REF-005 | `docs/PLAN.md` R4 and risk table | Sequencing and compaction acceptance context | MATCH |
| REF-006 | `docs/PRD.md` Sections 8.15 and runtime event requirements | Product requirements for compaction and hook event recording | HASH_MISMATCH warning |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |
