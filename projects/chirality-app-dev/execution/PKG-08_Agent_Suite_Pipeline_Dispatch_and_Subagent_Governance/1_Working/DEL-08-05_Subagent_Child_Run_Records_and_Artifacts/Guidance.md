# Guidance: DEL-08-05 Subagent Child Run Records and Artifacts

## Purpose

This deliverable makes governed subagent execution replayable and auditable without expanding subagent authority. Its product value is the durable record of what child agent was requested, how it was linked to the parent session or turn, what status it reached, and where any child output artifact was stored.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Keep Chirality events canonical. | Treat `.chirality/sessions/<id>/events.jsonl` and `HarnessEvent` replay as the product-owned audit mirror. SDK transcript paths may be linked but should not become canonical unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` K-EVENT-4 and K-SDK-3 |
| Separate governance gate from child record persistence. | DEL-08-04 owns the subagent governance bridge. DEL-08-05 should persist the resulting child lifecycle and artifact references without weakening or duplicating admission rules. | `_CONTEXT.md`; `docs/PRD.md` FR-101 and FR-102 |
| Fail closed is still visible. | Denied or failed subagent actions should leave reviewable runtime evidence. The exact boundary for a `HarnessSubagentRun` with `status: denied` needs a human or architecture ruling. | `docs/CONTRACT.md` K-SUBAGENT-1; `docs/TYPES.md` Section 10 |
| Store references, not bulky payloads. | Child outputs that exceed inline budgets should be represented by artifact metadata and relative paths. | `docs/SPEC.md` Sections 9.2 and 10.5 |
| Do not reintroduce retired scope. | Runtime event logging and child-run records are not the retired unified pipeline run record system. Avoid names, APIs, or storage layouts that imply pipeline-wide run-record reactivation. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
| Preserve professional and security boundaries. | Event data and artifacts should avoid secrets and should not represent child output as professional approval, certification, or external validation. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-115 |

## Considerations

- `HarnessSubagentRun` should be small and stable. Put bulky child output in artifacts, not in the record itself.
- `runId` should be distinct from `eventId`; lifecycle events can reference the child run, while the child run remains the durable summary of the child execution.
- `parentSessionId` is required and `parentTurnId` is optional. The implementation should handle session-level child delegation if a future flow lacks a turn ID.
- `sdkAgentId`, `model`, and SDK transcript metadata may be unavailable for some runtime paths. These fields should remain optional rather than synthesized.
- `status` should reflect the child run lifecycle, not the parent turn outcome. A parent turn can fail after a child completed, and a child can fail while the parent records that failure successfully.
- Artifact paths should be relative to session-controlled storage when possible to support migration and replay.
- Replay fixtures should cover at least completed, failed, cancelled, and denied status behavior. The exact denied-record expectation is pending ruling.

## Trade-offs

| Topic | Option | Trade-off |
|---|---|---|
| Denied attempts | Record only `tool.permission` / hook denial events | Avoids allocating child runs before execution but may make subagent-specific denial replay less direct. |
| Denied attempts | Also create `HarnessSubagentRun` with `status: denied` | Makes subagent denial visible in one record family but requires a clear allocation boundary before execution. |
| SDK metadata | Store only stable Chirality fields | More portable and less coupled, but loses SDK-specific debugging detail. |
| SDK metadata | Store optional SDK identifiers and transcript paths | Better debugging and resume correlation, but must remain secondary to Chirality events. |
| Output storage | Inline small child summaries | Easier replay and inspection for small data. |
| Output storage | Store child outputs as artifacts | Better for large data and context hygiene, but requires artifact lifecycle and path validation. |

## Examples

### Example `HarnessSubagentRun`

```json
{
  "runId": "subrun_123",
  "parentSessionId": "session_abc",
  "parentTurnId": "turn_001",
  "persona": "TASK",
  "agentName": "TASK",
  "sdkAgentId": "sdk-agent-id-if-available",
  "model": "TBD",
  "projectRoot": "/absolute/project/root",
  "status": "completed",
  "startedAt": "2026-05-20T00:00:00.000Z",
  "completedAt": "2026-05-20T00:01:00.000Z",
  "outputArtifactPath": ".chirality/sessions/session_abc/artifacts/subrun_123/output.json"
}
```

`model` is shown as `TBD` because the accessible sources identify the field as optional but do not require a specific model value.

### Example Lifecycle Event Payload

```json
{
  "schemaVersion": 1,
  "eventId": "event_456",
  "sessionId": "session_abc",
  "turnId": "turn_001",
  "timestamp": "2026-05-20T00:00:00.000Z",
  "type": "subagent.started",
  "data": {
    "runId": "subrun_123",
    "agentName": "TASK",
    "status": "running"
  }
}
```

The exact event payload keys inside `data` are TBD beyond the sourced `HarnessEvent` envelope and the minimum child-run linkage needed for replay (`runId` plus current or terminal `status`).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | PRD hash mismatch: referenced PRD expected SHA does not match observed SHA. | `_REFERENCES.md` REF-006 expected hash | `_REFERENCES.md` REF-006 actual hash; runtime assignment says treat as warning | PRD-derived guidance and requirements | Use PRD content as accessible source with source warning; do not treat mismatch as closure blocker. | TBD |
| Denied allocation ruling | Denied subagent attempts may be represented as permission events, child-run records with `status: denied`, or both. | `docs/TYPES.md` Section 10 includes `denied` status | `docs/CONTRACT.md` K-SUBAGENT-1 describes fail-closed delegation gate | Denial replay, schema tests, procedure verification | Record permission denial always; create child-run `denied` record only after the run allocation boundary is defined. | TBD |
