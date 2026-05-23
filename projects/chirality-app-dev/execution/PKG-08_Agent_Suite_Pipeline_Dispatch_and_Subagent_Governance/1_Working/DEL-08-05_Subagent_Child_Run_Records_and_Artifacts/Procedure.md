# Procedure: DEL-08-05 Subagent Child Run Records and Artifacts

## Purpose

Define the operational steps for producing and validating the subagent child run record and artifact-reference slice for governed Type 2 subagent execution.

## Prerequisites

| Prerequisite | Status / Note |
|---|---|
| Accepted source corpus listed in `_REFERENCES.md` | Available, with REF-006 PRD hash mismatch treated as a warning. |
| DEL-08-04 Type 2 Subagent Governance Bridge | Upstream relationship is implied by scope, but `_DEPENDENCIES.md` has no accepted dependency edge yet. Keep as ASSUMPTION until dependency extraction runs. |
| Runtime event schema / `HarnessEvent` | Required source target exists in `docs/SPEC.md` and `docs/TYPES.md`. |
| Artifact storage policy | Required source target exists in `docs/SPEC.md` and `docs/PRD.md`. |
| Human ruling for denied child-run allocation | TBD. |

## Steps

1. Confirm the deliverable remains scoped to child run records and artifact references, not the governance admission bridge.
2. Define or update the `HarnessSubagentRun` data shape with the sourced fields from `docs/TYPES.md` Section 10.
3. Ensure `status` accepts only `queued`, `running`, `completed`, `failed`, `cancelled`, and `denied`.
4. Link each child run to its parent session using `parentSessionId`; include `parentTurnId` when the child run is associated with a turn.
5. Capture runtime metadata that is available without invention: `persona`, `agentName`, optional `sdkAgentId`, optional `model`, and `projectRoot`.
6. Capture lifecycle timestamps when known: `startedAt` and `completedAt`.
7. Emit or map parent session events for subagent lifecycle using `subagent.started` and `subagent.completed` when lifecycle support is active.
8. Store large child outputs under the session artifact folder instead of embedding bulky payloads in events or child records.
9. Record `outputArtifactPath` when a child output artifact is created.
10. Apply redaction policy before persisting event data, run logs, or artifacts.
11. Keep SDK transcript identifiers and paths as secondary metadata; do not replace canonical Chirality events with SDK transcripts.
12. Add replay fixtures for parent-child linkage and child output artifact paths.
13. Add or update tests for completed, failed, cancelled, and TBD denied-run behavior.
14. Verify the implementation does not introduce retired unified pipeline run records, dependency graph generation, deliverable locks, or staleness propagation tooling.

## Verification

| Check | Expected Result |
|---|---|
| `HarnessSubagentRun` required fields | `runId`, `parentSessionId`, `persona`, `agentName`, `projectRoot`, and `status` are required. |
| Status enum | Only `queued`, `running`, `completed`, `failed`, `cancelled`, and `denied` are accepted. |
| Event envelope | Subagent lifecycle events use the `HarnessEvent` envelope with schema version, unique event ID, session ID, timestamp, type, and data payload. |
| Append-only storage | Runtime events are appended as newline-delimited JSONL in write sequence. |
| Artifact references | Child output artifacts are referenced by path and metadata rather than embedded when large. |
| Redaction | Secrets are absent from event data and artifact metadata. |
| Replay | Replay can reconstruct parent session, child lifecycle, terminal child status, and child output artifact path. |
| Scope boundary | No retired PKG-08 pipeline run-record behavior is introduced. |

## Records

- `HarnessSubagentRun` schema/type and tests.
- `HarnessEvent` subagent lifecycle event fixtures.
- Child output artifact path fixtures.
- Replay fixtures covering parent-child linkage.
- Human ruling record for denied child-run allocation semantics.
- Source warning record for PRD hash mismatch until resolved.

