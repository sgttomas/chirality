# Procedure: DEL-08-05 Subagent Child Run Records and Artifacts

## Purpose

Define the operational steps for producing and validating the subagent child run record and artifact-reference slice for governed Type 2 subagent execution.

## Prerequisites

| Prerequisite | Status / Note |
|---|---|
| Accepted source corpus listed in `_REFERENCES.md` | Available under the current D-APP-38 authority corpus. |
| DEL-08-04 Type 2 Subagent Governance Bridge | Upstream relationship is implied by scope, but `_DEPENDENCIES.md` has no accepted dependency edge yet. Keep as ASSUMPTION until dependency extraction runs. |
| Runtime event schema / `HarnessEvent` | Required source target exists in `docs/SPEC.md` and `docs/TYPES.md`. |
| Artifact storage policy | Required source target exists in `docs/SPEC.md` and `docs/PRD.md`. |
| Human ruling for denied child-run allocation | D-APP-40 ruled: denied records are required only after the runtime reaches the child-run record layer. |

## Steps

1. Confirm the deliverable remains scoped to child run records and artifact references, not the governance admission bridge.
2. Define or update the `ChildRunRecord` data shape with the sourced fields from `docs/TYPES.md` Section 10.
3. Ensure `status` accepts only `queued`, `running`, `completed`, `failed`, `cancelled`, and `denied`.
4. Link each child run to its parent session using `parentSessionId`; include `parentTurnId` when the child run is associated with a turn.
5. Capture runtime metadata that is available without invention: `persona`, `agentName`, optional `sdkAgentId`, optional `model`, and `projectRoot`.
6. Capture lifecycle timestamps when known: `startedAt` and `completedAt`.
7. Emit or map parent session events for subagent lifecycle using `subagent.started` and `subagent.completed` when lifecycle support is active; do not invent additional failed, cancelled, or denied event category names without governed source text.
8. Store large child outputs under the session artifact folder instead of embedding bulky payloads in events or child records.
9. Record `outputArtifactPath` when a child output artifact is created.
10. Apply redaction policy before persisting event data, run logs, or artifacts.
11. Keep SDK transcript identifiers and paths as secondary metadata; do not replace canonical Chirality events with SDK transcripts.
12. Add replay fixtures for parent-child linkage and child output artifact paths.
13. Add or update tests for completed, failed, cancelled, denied-before-allocation, and denied-after-allocation behavior. D-APP-40 requires `status: denied` only after the child-run record layer is reached; earlier denials may remain permission/hook evidence.
14. Verify the implementation does not introduce retired unified pipeline run records, dependency graph generation, deliverable locks, or staleness propagation tooling.

## Verification

| Check | Expected Result |
|---|---|
| `ChildRunRecord` required fields | `childRunId`, `parentSessionId`, `parentPersona`, `agentName`, `projectRoot`, `mode`, `status`, `capabilityPolicy`, and `governance` are required. |
| Status enum | Only `queued`, `running`, `completed`, `failed`, `cancelled`, and `denied` are accepted. |
| Event envelope | Subagent lifecycle events use the `HarnessEvent` envelope with schema version, unique event ID, session ID, timestamp, type, and data payload. |
| Append-only storage | Runtime events are appended as newline-delimited JSONL in write sequence. |
| Artifact references | Child output artifacts are referenced by path and metadata rather than embedded when large. |
| Artifact metadata fields | Where the artifact policy applies, fixture assertions cover tool name, turn ID, byte count, truncation flag, and relative artifact path. |
| Redaction | Secrets are absent from event data and artifact metadata. |
| Replay | Replay can reconstruct parent session, child lifecycle, terminal child status, and child output artifact path. |
| Terminal subagent state | Failed, cancelled, and denied terminal states are asserted through `ChildRunRecord.status` and provider-neutral subagent lifecycle event data. |
| Scope boundary | No retired PKG-08 pipeline run-record behavior is introduced. |

## Pass 3 Disposition Evidence

| ItemID | Disposition | Evidence |
|---|---|---|
| F-001 | Resolved by D-APP-40. | Prerequisites and Step 13 apply the denied child-run allocation boundary. Source reread: `docs/TYPES.md` Section 10 and `docs/CONTRACT.md` K-SUBAGENT-1. |
| F-002 | Resolved by D-APP-40. | Step 13 separates denied-before-allocation and denied-after-allocation behavior according to the ruled boundary. Source reread: Specification DEL-08-05-REQ-012. |
| E-001 | Incorporated. | Verification now enumerates tool name, turn ID, byte count, truncation flag, and relative artifact path for artifact metadata fixture assertions. Source reread: `docs/PRD.md` Section 10.5. |
| E-002 | Incorporated as a terminal-state category boundary. | Step 7 and Verification assert terminal state through `ChildRunRecord.status` and provider-neutral subagent lifecycle event data. Source reread: `docs/PRD.md` Section 8.12, `docs/SPEC.md` Section 9.4, and `docs/TYPES.md` Sections 7.3 and 10. |

## Records

- `ChildRunRecord` schema/type and tests.
- `HarnessEvent` subagent lifecycle event fixtures.
- Child output artifact path fixtures.
- Replay fixtures covering parent-child linkage.
- D-APP-40 ruling record for denied child-run allocation semantics.
