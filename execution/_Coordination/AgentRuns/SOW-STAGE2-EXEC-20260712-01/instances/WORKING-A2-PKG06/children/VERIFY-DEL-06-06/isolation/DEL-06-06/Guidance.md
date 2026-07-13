# Guidance: DEL-06-06 Hook Lifecycle and Compaction Mirror

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

DEL-06-06 exists to make hook execution, failure, terminal finalization, and SDK/model compaction boundaries auditable in Chirality-owned runtime events. It is an event-mirroring slice, not the owner of every hook policy: path/write hook enforcement is primarily DEL-06-04, permission mediation is DEL-06-01, and this deliverable ensures those hook and compaction boundaries become replayable evidence in `events.jsonl`.

Sources: `_CONTEXT.md`; decomposition PKG-06; `docs/SPEC.md` Sections 8 through 10 and 15.2; `docs/CONTRACT.md` Sections 1.4 through 1.6.

## Principles

1. Chirality event names are the durable contract. SDK hook names and SDK transcript details may be adapter metadata, but persisted runtime semantics should remain `HarnessEvent` records in Chirality terms. Sources: `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` Section 1.4 K-ENGINE-4.
2. The audit mirror stays canonical. `.chirality/sessions/<id>/events.jsonl` remains the product-owned audit record even when SDK transcripts assist resume or debugging. Sources: `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `docs/SPEC.md` Section 8.4.
3. Hook failure is safety-relevant. Failed hooks cannot be reduced to diagnostics when the attempted action is write, shell, domain, or subagent execution; fail-closed behavior must be preserved. Sources: `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2.
4. Compaction must not erase replay. Context compaction can reduce model context, but the full Chirality event log must remain on disk and replayable. Sources: `docs/PLAN.md` R4; `docs/PRD.md` Section 8.15, MATCH status. (reconciled under D-APP-38).
5. Terminal outcomes remain durable. Stop/finalization evidence should support, not replace, the TurnEngine/session event obligation that every accepted turn ends in a durable terminal event. Source: `docs/CONTRACT.md` Section 1.5 K-EVENT-3.

## Considerations

### Event Boundary

| Topic | Guidance | Source |
|---|---|---|
| Event type names | Use `hook.started`, `hook.completed`, and `context.compacted` where they apply. If a distinct failure event type is proposed, treat it as PROPOSAL until the event category registry accepts it; meanwhile encode failure as outcome data under an accepted event type or a versioned extension. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3 |
| Payload content | Keep payloads replay-useful but safe: IDs, timestamps, hook term, action/tool context, outcome, duration, adapter metadata, and artifact references are plausible; exact fields are TBD until implementation defines the event schema. | `docs/SPEC.md` Section 9.1 and 9.2 |
| SDK metadata | Store SDK hook names, transcript keys, or compaction metadata only under explicit adapter metadata fields. | `docs/SPEC.md` Section 10.3 |
| Parent linkage | Use `parentEventId` or turn/session IDs where useful to connect hook events to tool, turn, terminal, or subagent events. Exact linkage policy is TBD until the mapper owns the relationship between hook callbacks and event-writer records. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Sections 7.3 and 8.5 |

### Compaction Mirror

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

### Terminal Hook Handling

Stop/finalization hooks should be mapped carefully so they do not race or duplicate terminal `turn.completed`, `turn.failed`, `turn.cancelled`, or interruption records. A useful implementation pattern is to make the finalization mapper attach safe hook evidence to the same turn/session lineage while preserving the TurnEngine as terminal outcome owner. Exact implementation: TBD.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Separate failure event type vs outcome field | The current listed categories include `hook.started` and `hook.completed` but not `hook.failed`. Prefer accepted event categories unless the event registry is explicitly extended. Preserve failure in outcome/status data when needed. |
| Rich payloads vs redaction | Prefer minimal replay-relevant metadata plus artifact references. Do not store secrets or large raw tool outputs in hook events. Source: `docs/SPEC.md` Section 9.2. |
| SDK transcript reliance vs Chirality mirror | Use SDK transcript linkage for resume/debug metadata, but never make it the only source needed to replay Chirality runtime history. |
| Compaction mirror vs custom compaction | Mirror SDK compaction first. Custom compaction is not required by current sources and should remain TBD unless a governed update adds it. Source: `docs/PLAN.md` alternatives table. |
| Hook enforcement vs hook evidence | DEL-06-06 should not absorb DEL-06-04's path enforcement scope. It records lifecycle/failure/finalization evidence and preserves fail-closed semantics at the mirror boundary. |

## Examples

| Scenario | Expected mirror behavior |
|---|---|
| `PreToolUse` starts for a governed write attempt | Emit or stage `hook.started` evidence tied to the session/turn/tool context. The path enforcement decision itself is owned by the hook policy implementation. |
| `PreToolUse` denies or fails for a write action | Preserve fail-closed outcome and record safe diagnostics in hook completion/failure evidence; the write must not execute. |
| `PostToolUse` completes after a read tool | Record hook completion evidence where runtime support exists; large tool output remains budgeted or artifact-referenced rather than copied into the hook event. |
| SDK emits a compaction boundary | Persist `context.compacted` with boundary metadata that is safe and available; preserve replay implications and keep full `events.jsonl` on disk. |
| Stop/finalization callback fires | Record finalization evidence associated with the turn/session while ensuring the durable terminal event remains success, failure, cancellation, or interruption. |
| SDK transcript is available under a configured store | Cross-reference the transcript linkage as adapter metadata only; `events.jsonl` remains canonical. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| TBD | No direct source conflict identified during P1/P2. PRD has a MATCH source state. | `_REFERENCES.md` REF-006 | `docs/PRD.md` Section 8.15 and runtime event requirements | PRD-cited compaction payload details and acceptance wording | Treat PRD as a current MATCH source under the reconciled D-APP-38 source state; prefer CONTRACT/SPEC/TYPES for binding schema and invariants. | TBD — reconciled under D-APP-38 |

## Pass 3 Disposition

| ItemID | Disposition | Evidence reread |
|---|---|---|
| C-002 | Already covered as a registry blocker: `hook.failed` is not in the current listed event categories, so failures remain outcome data under accepted event types unless a governed event-registry extension is accepted. | `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Section 7.3; `docs/CONTRACT.md` Section 1.6 K-HOOK-1 |
| X-001 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.15; `docs/SPEC.md` Sections 9.4 and 15.2 — reconciled under D-APP-38 |
| E-001 | Converted to a tracked linkage-policy blocker: parent/child linkage may use `parentEventId`, `turnId`, or `sessionId`, but the exact policy remains `TBD` until mapper implementation assigns callback-to-event lineage. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Sections 7.3 and 8.5 |
