# Guidance: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

## Purpose

DEL-05-02 exists to make Chirality runtime work auditable through a product-owned event log. The core outcome is a stable, provider-neutral `HarnessEvent` schema and append-only JSONL writer that records accepted turns, runtime events, and terminal outcomes in `.chirality/sessions/<sessionId>/events.jsonl`.

This deliverable supports OBJ-003: making accepted turns, SDK messages, terminal outcomes, tool activity, and replay auditable through Chirality-owned session records.

## Principles

1. Chirality events are runtime audit records, not project approval records.
   Source: `docs/DIRECTIVE.md` Section 2.3.

2. `events.jsonl` is canonical for Chirality runtime governance; SDK transcripts are secondary unless imported into `HarnessEvent` form.
   Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4.

3. Persist `turn.accepted` before calling the model/SDK so killed or interrupted turns leave recoverable evidence.
   Source: `docs/CONTRACT.md` K-EVENT-2; `docs/SPEC.md` Section 10.1.

4. Every accepted turn should have a terminal persisted outcome so replay can distinguish success, failure, cancellation, and interruption.
   Source: `docs/CONTRACT.md` K-EVENT-3.

5. Browser `UIEvent`s and persisted `HarnessEvent`s must stay separate. The browser stream stays compact; the runtime audit log may be richer and versioned.
   Source: `docs/CONTRACT.md` K-EVENT-1.

6. Provider/SDK terms should be translated at adapter boundaries. Canonical event fields should remain Chirality-owned and provider-neutral.
   Source: `docs/CONTRACT.md` K-CORE-1 and K-ENGINE-4.

7. Secret hygiene applies at the schema boundary. The event API should make it difficult to persist API keys, configured secrets, or unredacted sensitive data.
   Source: `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1.

## Considerations

- `docs/PRD.md` is marked `HASH_MISMATCH` in `_REFERENCES.md`. PRD requirements such as FR-072 through FR-076 align with matching SPEC/CONTRACT/TYPES sources, but PRD-only interpretations should remain provisional until the hash state is resolved.
- `turn.accepted` is part of this deliverable's core slice; broader interrupt cleanup and lifecycle lock release are adjacent concerns owned by DEL-03-04.
- Redaction is adjacent but not optional. DEL-05-02 should define the event API so redaction can be enforced by DEL-05-03 without schema churn.
- Tool permission, hook, compaction, subagent, and SDK mirror categories are listed as later event categories in SPEC/TYPES. The initial implementation should not block those categories, but should avoid over-implementing behavior owned by later deliverables.
- Malformed-tail tolerance matters because append-only JSONL can be interrupted mid-write. Replay should preserve valid prior records and surface diagnostics rather than failing the whole session.
- Append-only JSONL is sufficient for interrupted-write recovery only when accepted-turn and terminal events are written in sequence and replay treats the final malformed line as diagnostic context rather than as authority over earlier valid records. This bounds recovery to reconstructing durable prior events; it does not approve project state or replace human gate evidence.
- Large payloads should be artifact references, not inline event blobs. Thresholds and storage policy are deferred to DEL-05-05 unless already established by adjacent implementation.

## Trade-offs

| Trade-off | Direction |
|---|---|
| Rich event payloads vs. stable replay | Prefer stable minimal required fields with event-type-specific `data`; keep schema evolution versioned or backward-compatible. |
| SDK transcript richness vs. Chirality canonicality | Keep SDK transcripts linked as secondary artifacts; import only selected data into `HarnessEvent` when needed. |
| Immediate category completeness vs. bounded slice | Implement the initial event categories required for accepted turns and terminal outcomes; leave later tool/hook/subagent semantics to their owning deliverables. |
| Inline data vs. artifact references | Inline small safe data only; reference large or sensitive data through governed artifact metadata. |
| PRD detail vs. hash mismatch | Use PRD only where corroborated by matching sources, or mark PRD-only details as TBD/ASSUMPTION. |

## Examples

Example `HarnessEvent` shape from `docs/SPEC.md` Section 9.1 and `docs/TYPES.md` Section 7.3:

```ts
type HarnessEvent = {
  schemaVersion: 1;
  eventId: string;
  sessionId: string;
  turnId?: string;
  parentEventId?: string;
  timestamp: string;
  type: string;
  data: Record<string, unknown>;
};
```

Example event categories from matching SPEC/TYPES sources:

- Initial: `session.created`, `session.resumed`, `turn.accepted`, `turn.started`, `sdk.system.init`, `model.request.started`, `model.delta`, `model.completed`, `turn.completed`, `turn.failed`, `turn.cancelled`.
- Later: `tool.queued`, `tool.permission`, `tool.started`, `tool.progress`, `tool.completed`, `tool.failed`, `hook.started`, `hook.completed`, `context.compacted`, `subagent.started`, `subagent.completed`, `sdk.mirror.error`.

## Conflict Table (for human ruling)

No source-content conflicts were identified during P1/P2 drafting.

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| SOURCE-WARN-001 | `docs/PRD.md` is listed as HASH_MISMATCH in `_REFERENCES.md`; PRD content aligns with matching SPEC/CONTRACT/TYPES slices used here but source state is not clean. | `_REFERENCES.md` REF-006 | `docs/PRD.md` Sections 8.12, 9.4, FR-072-FR-076 | Datasheet References; Specification Standards/Requirements; Guidance Considerations | Use PRD only as corroborating context until reference hash is reconciled. | TBD |
