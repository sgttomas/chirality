# Source Pack: SRC-DEL-DEL-08-05-SUBAGENT-CHILD-RUN-RECORDS-AND-ARTIFACTS

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/Datasheet.md

### Datasheet: DEL-08-05 Subagent Child Run Records and Artifacts

#### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-08-05 |
| DeliverableName | Subagent Child Run Records and Artifacts |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | DATA_MODEL_CHANGE |
| ContextEnvelope | M |
| ResponsibleParty | TBD |
| CoversScopeItems | SOW-063 |
| SupportsObjectives | OBJ-003, OBJ-007 |

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Scope | Persist parent-child runtime records, status, timestamps, SDK agent metadata, and output artifact paths. | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-08-05 |
| Primary record target | `HarnessSubagentRun` | `docs/TYPES.md` Section 10 |
| Parent audit event target | `HarnessEvent` | `docs/TYPES.md` Section 7.3; `docs/SPEC.md` Section 9 |
| Canonical event store | `.chirality/sessions/<id>/events.jsonl` | `docs/CONTRACT.md` K-EVENT-4; `docs/TYPES.md` Section 7.2 |
| Artifact folder | `.chirality/sessions/<sessionId>/artifacts/` | `docs/TYPES.md` Section 7.2; `docs/PRD.md` Section 10.5 |
| Relevant event categories | `subagent.started`, `subagent.completed` | `docs/PRD.md` Section 8.12; `docs/SPEC.md` Section 9.4 |
| Output artifact policy | Large payloads are stored as artifacts and referenced by metadata; child-run outputs use output artifact references. | `docs/SPEC.md` Sections 9.2 and 10.5; `docs/PLAN.md` R5 |
| Execution gate relationship | Child records are created for governed subagent execution; governance admission itself belongs to DEL-08-04. | `_CONTEXT.md`; `docs/PRD.md` FR-101 and FR-102 |

#### Conditions

| Condition | Value | Source |
|---|---|---|
| Subagent delegation must fail closed unless governance conditions pass. | Required. | `docs/CONTRACT.md` K-SUBAGENT-1 |
| SDK subagents may not expand parent capabilities. | Required. | `docs/CONTRACT.md` K-SUBAGENT-2 |
| Subagent runs must produce parent-child runtime records and output artifact references when execution is enabled. | Required. | `docs/CONTRACT.md` K-SUBAGENT-3 |
| Runtime events must redact secrets. | Required. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-075 |
| JSONL replay must tolerate malformed trailing records. | Required for the event store. | `docs/CONTRACT.md` K-EVENT-5; `docs/SPEC.md` Section 9.2 |
| SDK transcripts are secondary unless imported into `HarnessEvent` form. | Required. | `docs/CONTRACT.md` K-SDK-3; `docs/SPEC.md` Section 8 |
| Unified pipeline run records remain retired scope. | Required boundary. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
| PRD source hash | Source warning: expected hash differs from observed hash; content used only as accessible source with mismatch noted. | `_REFERENCES.md`; runtime assignment |

#### Construction

##### Target `HarnessSubagentRun` Fields

| Field | Type / Allowed Value | Requirement Status | Source |
|---|---|---|---|
| `runId` | string | Required by type target. | `docs/TYPES.md` Section 10 |
| `parentSessionId` | string | Required by type target. | `docs/TYPES.md` Section 10 |
| `parentTurnId` | string | Optional by type target. | `docs/TYPES.md` Section 10 |
| `persona` | string | Required by type target. | `docs/TYPES.md` Section 10 |
| `agentName` | string | Required by type target. | `docs/TYPES.md` Section 10 |
| `sdkAgentId` | string | Optional by type target; available when SDK exposes it. | `docs/TYPES.md` Section 10; `docs/PRD.md` FR-101 |
| `model` | string | Optional by type target. | `docs/TYPES.md` Section 10 |
| `projectRoot` | string | Required by type target. | `docs/TYPES.md` Section 10 |
| `status` | `queued`, `running`, `completed`, `failed`, `cancelled`, `denied` | Required by type target. | `docs/TYPES.md` Section 10 |
| `startedAt` | string | Optional by type target. | `docs/TYPES.md` Section 10 |
| `completedAt` | string | Optional by type target. | `docs/TYPES.md` Section 10 |
| `outputArtifactPath` | string | Optional by type target; required when child output is stored externally. | `docs/TYPES.md` Section 10; `docs/PRD.md` FR-101 |

##### Related `HarnessEvent` Fields

| Field | Type / Allowed Value | Requirement Status | Source |
|---|---|---|---|
| `schemaVersion` | `1` | Required by type target. | `docs/TYPES.md` Section 7.3; `docs/SPEC.md` Section 9.1 |
| `eventId` | string | Required; unique per event. | `docs/SPEC.md` Section 9.2 |
| `sessionId` | string | Required. | `docs/SPEC.md` Section 9.1 |
| `turnId` | string | Optional. | `docs/SPEC.md` Section 9.1 |
| `parentEventId` | string | Optional. | `docs/SPEC.md` Section 9.1 |
| `timestamp` | string | Required. | `docs/SPEC.md` Section 9.1 |
| `type` | string; includes later categories `subagent.started` and `subagent.completed` | Required. | `docs/SPEC.md` Sections 9.1 and 9.4 |
| `data` | `Record<string, unknown>` | Required; must avoid secrets. | `docs/SPEC.md` Sections 9.1 and 9.2 |

#### References

- `docs/DIRECTIVE.md` - runtime audit mirror and subagent governance direction.
- `docs/CONTRACT.md` - event, hook, and subagent invariants.
- `docs/SPEC.md` - event schema, artifact policy, and runtime engine contract.
- `docs/TYPES.md` - `HarnessEvent`, session artifact, and `HarnessSubagentRun` type targets.
- `docs/PLAN.md` - R5 governed subagent runtime sequencing and retired-scope boundary.
- `docs/PRD.md` - runtime event, artifact, and subagent requirements. Source warning: hash mismatch recorded in `_REFERENCES.md`.
- `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` - decomposition method reference.

## Component: execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/Guidance.md

### Guidance: DEL-08-05 Subagent Child Run Records and Artifacts

#### Purpose

This deliverable makes governed subagent execution replayable and auditable without expanding subagent authority. Its product value is the durable record of what child agent was requested, how it was linked to the parent session or turn, what status it reached, and where any child output artifact was stored.

#### Principles

| Principle | Guidance | Source |
|---|---|---|
| Keep Chirality events canonical. | Treat `.chirality/sessions/<id>/events.jsonl` and `HarnessEvent` replay as the product-owned audit mirror. SDK transcript paths may be linked but should not become canonical unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` K-EVENT-4 and K-SDK-3 |
| Separate governance gate from child record persistence. | DEL-08-04 owns the subagent governance bridge. DEL-08-05 should persist the resulting child lifecycle and artifact references without weakening or duplicating admission rules. | `_CONTEXT.md`; `docs/PRD.md` FR-101 and FR-102 |
| Fail closed is still visible. | Denied or failed subagent actions should leave reviewable runtime evidence. The exact boundary for a `HarnessSubagentRun` with `status: denied` needs a human or architecture ruling. | `docs/CONTRACT.md` K-SUBAGENT-1; `docs/TYPES.md` Section 10 |
| Store references, not bulky payloads. | Child outputs that exceed inline budgets should be represented by artifact metadata and relative paths. | `docs/SPEC.md` Sections 9.2 and 10.5 |
| Do not reintroduce retired scope. | Runtime event logging and child-run records are not the retired unified pipeline run record system. Avoid names, APIs, or storage layouts that imply pipeline-wide run-record reactivation. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
| Preserve professional and security boundaries. | Event data and artifacts should avoid secrets and should not represent child output as professional approval, certification, or external validation. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-115 |

#### Considerations

- `HarnessSubagentRun` should be small and stable. Put bulky child output in artifacts, not in the record itself.
- `runId` should be distinct from `eventId`; lifecycle events can reference the child run, while the child run remains the durable summary of the child execution.
- `parentSessionId` is required and `parentTurnId` is optional. The implementation should handle session-level child delegation if a future flow lacks a turn ID.
- `sdkAgentId`, `model`, and SDK transcript metadata may be unavailable for some runtime paths. These fields should remain optional rather than synthesized.
- `status` should reflect the child run lifecycle, not the parent turn outcome. A parent turn can fail after a child completed, and a child can fail while the parent records that failure successfully.
- Artifact paths should be relative to session-controlled storage when possible to support migration and replay.
- Replay fixtures should cover at least completed, failed, cancelled, and denied status behavior. The exact denied-record expectation is pending ruling.

#### Trade-offs

| Topic | Option | Trade-off |
|---|---|---|
| Denied attempts | Record only `tool.permission` / hook denial events | Avoids allocating child runs before execution but may make subagent-specific denial replay less direct. |
| Denied attempts | Also create `HarnessSubagentRun` with `status: denied` | Makes subagent denial visible in one record family but requires a clear allocation boundary before execution. |
| SDK metadata | Store only stable Chirality fields | More portable and less coupled, but loses SDK-specific debugging detail. |
| SDK metadata | Store optional SDK identifiers and transcript paths | Better debugging and resume correlation, but must remain secondary to Chirality events. |
| Output storage | Inline small child summaries | Easier replay and inspection for small data. |
| Output storage | Store child outputs as artifacts | Better for large data and context hygiene, but requires artifact lifecycle and path validation. |

#### Examples

##### Example `HarnessSubagentRun`

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

##### Example Lifecycle Event Payload

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

#### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | PRD hash mismatch: referenced PRD expected SHA does not match observed SHA. | `_REFERENCES.md` REF-006 expected hash | `_REFERENCES.md` REF-006 actual hash; runtime assignment says treat as warning | PRD-derived guidance and requirements | Use PRD content as accessible source with source warning; do not treat mismatch as closure blocker. | TBD |
| Denied allocation ruling | Denied subagent attempts may be represented as permission events, child-run records with `status: denied`, or both. | `docs/TYPES.md` Section 10 includes `denied` status | `docs/CONTRACT.md` K-SUBAGENT-1 describes fail-closed delegation gate | Denial replay, schema tests, procedure verification | Record permission denial always; create child-run `denied` record only after the run allocation boundary is defined. | TBD |

## Component: execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/Procedure.md

### Procedure: DEL-08-05 Subagent Child Run Records and Artifacts

#### Purpose

Define the operational steps for producing and validating the subagent child run record and artifact-reference slice for governed Type 2 subagent execution.

#### Prerequisites

| Prerequisite | Status / Note |
|---|---|
| Accepted source corpus listed in `_REFERENCES.md` | Available, with REF-006 PRD hash mismatch treated as a warning. |
| DEL-08-04 Type 2 Subagent Governance Bridge | Upstream relationship is implied by scope, but `_DEPENDENCIES.md` has no accepted dependency edge yet. Keep as ASSUMPTION until dependency extraction runs. |
| Runtime event schema / `HarnessEvent` | Required source target exists in `docs/SPEC.md` and `docs/TYPES.md`. |
| Artifact storage policy | Required source target exists in `docs/SPEC.md` and `docs/PRD.md`. |
| Human ruling for denied child-run allocation | TBD. |

#### Steps

1. Confirm the deliverable remains scoped to child run records and artifact references, not the governance admission bridge.
2. Define or update the `HarnessSubagentRun` data shape with the sourced fields from `docs/TYPES.md` Section 10.
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
13. Add or update tests for completed, failed, cancelled, denied-before-allocation, and denied-after-allocation behavior. Keep the denied allocation expectation marked TBD until the human ruling is recorded.
14. Verify the implementation does not introduce retired unified pipeline run records, dependency graph generation, deliverable locks, or staleness propagation tooling.

#### Verification

| Check | Expected Result |
|---|---|
| `HarnessSubagentRun` required fields | `runId`, `parentSessionId`, `persona`, `agentName`, `projectRoot`, and `status` are required. |
| Status enum | Only `queued`, `running`, `completed`, `failed`, `cancelled`, and `denied` are accepted. |
| Event envelope | Subagent lifecycle events use the `HarnessEvent` envelope with schema version, unique event ID, session ID, timestamp, type, and data payload. |
| Append-only storage | Runtime events are appended as newline-delimited JSONL in write sequence. |
| Artifact references | Child output artifacts are referenced by path and metadata rather than embedded when large. |
| Artifact metadata fields | Where the artifact policy applies, fixture assertions cover tool name, turn ID, byte count, truncation flag, and relative artifact path. |
| Redaction | Secrets are absent from event data and artifact metadata. |
| Replay | Replay can reconstruct parent session, child lifecycle, terminal child status, and child output artifact path. |
| Terminal subagent state | Failed, cancelled, and denied terminal states are asserted through `HarnessSubagentRun.status` and `subagent.completed` event data unless a governed source later adds separate event category names. |
| Scope boundary | No retired PKG-08 pipeline run-record behavior is introduced. |

#### Pass 3 Disposition Evidence

| ItemID | Disposition | Evidence |
|---|---|---|
| F-001 | Converted to TBD/human-ruling prerequisite. | Prerequisites and Step 13 keep denied child-run allocation semantics unresolved. Source reread: `docs/TYPES.md` Section 10 and `docs/CONTRACT.md` K-SUBAGENT-1. |
| F-002 | Incorporated as fixture split. | Step 13 now separates denied-before-allocation and denied-after-allocation behavior, with final expectation pending ruling. Source reread: Specification DEL-08-05-REQ-012. |
| E-001 | Incorporated. | Verification now enumerates tool name, turn ID, byte count, truncation flag, and relative artifact path for artifact metadata fixture assertions. Source reread: `docs/PRD.md` Section 10.5. |
| E-002 | Incorporated as a terminal-state category boundary. | Step 7 and Verification avoid invented event categories and assert terminal state through `HarnessSubagentRun.status` and `subagent.completed` event data unless governed sources change. Source reread: `docs/PRD.md` Section 8.12, `docs/SPEC.md` Section 9.4, and `docs/TYPES.md` Sections 7.3 and 10. |

#### Records

- `HarnessSubagentRun` schema/type and tests.
- `HarnessEvent` subagent lifecycle event fixtures.
- Child output artifact path fixtures.
- Replay fixtures covering parent-child linkage.
- Human ruling record for denied child-run allocation semantics.
- Source warning record for PRD hash mismatch until resolved.

## Component: execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/Specification.md

### Specification: DEL-08-05 Subagent Child Run Records and Artifacts

#### Scope

This deliverable specifies the data-record and artifact-reference behavior for governed Type 2 subagent child runs. It covers parent-child runtime records, child status, timestamps, SDK agent metadata when available, and output artifact paths.

This deliverable excludes the admission decision and permission gate implementation for subagent execution. That bridge is assigned to DEL-08-04. It also excludes retired PKG-08 hardening scope such as unified pipeline run records, dependency graph generation, deliverable locks, and staleness propagation.

#### Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-08-05-REQ-001 | The implementation shall represent governed child execution with a `HarnessSubagentRun` record containing `runId`, `parentSessionId`, `persona`, `agentName`, `projectRoot`, and `status`. | `docs/TYPES.md` Section 10 |
| DEL-08-05-REQ-002 | The child run status shall use only `queued`, `running`, `completed`, `failed`, `cancelled`, or `denied`. | `docs/TYPES.md` Section 10 |
| DEL-08-05-REQ-003 | The child run record shall support optional `parentTurnId`, `sdkAgentId`, `model`, `startedAt`, `completedAt`, and `outputArtifactPath` fields. | `docs/TYPES.md` Section 10 |
| DEL-08-05-REQ-004 | Parent session runtime events shall record subagent lifecycle using `subagent.started` and `subagent.completed` event categories when subagent lifecycle support is active. No separate sourced event category names exist for failed, cancelled, or denied child terminals; until governed source text adds them, terminal child state should be carried through `HarnessSubagentRun.status` and the `subagent.completed` event data. | `docs/PRD.md` Section 8.12; `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Sections 7.3 and 10 |
| DEL-08-05-REQ-005 | Persisted runtime events shall conform to the `HarnessEvent` shape: `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`. For subagent lifecycle events, `data` shall preserve child-run linkage through `runId` and the current or terminal `status`; exact additional payload keys remain TBD unless a later governed source specifies them. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Sections 7.3 and 10 |
| DEL-08-05-REQ-006 | Runtime events shall append to newline-delimited JSONL in write sequence, with unique event IDs. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` FR-073 |
| DEL-08-05-REQ-007 | Child output payloads that are too large for inline event storage shall be stored under session artifacts and referenced by metadata/path. | `docs/SPEC.md` Sections 9.2 and 10.5; `docs/PRD.md` FR-096 |
| DEL-08-05-REQ-008 | Artifact metadata shall include tool name, turn ID, byte count, truncation flag, and relative artifact path where the artifact policy applies. | `docs/PRD.md` Section 10.5 |
| DEL-08-05-REQ-009 | Event and artifact records shall avoid storing secrets and shall pass through redaction where policy requires. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-075 |
| DEL-08-05-REQ-010 | SDK transcript paths or SDK session identifiers shall remain secondary runtime metadata unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` K-SDK-3; `docs/TYPES.md` Section 7.2 |
| DEL-08-05-REQ-011 | The data model shall not reactivate retired unified pipeline run records or broader PKG-08 hardening scope. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
| DEL-08-05-REQ-012 | ASSUMPTION: a denied subagent attempt should produce a child-run record with `status: denied` when the attempt reaches the child-run record layer. Human ruling is needed on whether denials before child-run allocation are represented only as permission events or also as `HarnessSubagentRun` records. | `docs/TYPES.md` Section 10; `docs/CONTRACT.md` K-SUBAGENT-1 |

#### Standards

| Standard / Contract | Applicability |
|---|---|
| `HarnessEvent` persisted event schema | Governs parent session event records and subagent lifecycle mirror events. |
| `HarnessSubagentRun` type target | Governs child run record fields and status vocabulary. |
| Runtime Audit Mirror | `.chirality/sessions/<id>/events.jsonl` remains the product-owned event store. |
| Tool Result Artifact policy | Governs child output artifact storage and metadata. |
| Subagent governance invariants | Child records must align with fail-closed governance, restricted capability inheritance, and output references. |

#### Verification

| Requirement IDs | Verification Approach |
|---|---|
| DEL-08-05-REQ-001 through DEL-08-05-REQ-003 | Type-level tests or schema tests validate required fields, optional fields, and status enum values. |
| DEL-08-05-REQ-004 through DEL-08-05-REQ-006 | Event writer/replay tests validate lifecycle event categories, `HarnessEvent` shape, append ordering, unique event IDs, child `runId` linkage, and status propagation through the child run record or lifecycle event data. |
| DEL-08-05-REQ-007 through DEL-08-05-REQ-008 | Artifact-store tests validate child output storage, relative path references, byte counts, and truncation metadata. |
| DEL-08-05-REQ-009 | Redaction tests validate that secrets do not enter event data or stored artifacts. |
| DEL-08-05-REQ-010 | Replay/session tests validate that SDK transcript metadata does not replace canonical Chirality events. |
| DEL-08-05-REQ-011 | Scope-boundary review verifies no retired unified pipeline run record behavior is introduced. |
| DEL-08-05-REQ-012 | Human ruling required before final denied-allocation test expectation is fixed; interim tests should keep denied-before-allocation and denied-after-allocation fixtures separate. |

#### Pass 3 Disposition Evidence

| ItemID | Disposition | Evidence |
|---|---|---|
| C-001 | Already covered; retained as a source-authority conflict. | Conflict Table keeps REF-006 hash mismatch warning for PRD-derived requirements and guidance. Source reread: `_REFERENCES.md` REF-006 and current Conflict Table. |
| F-001 | Converted to explicit TBD/human-ruling language. | DEL-08-05-REQ-012 continues to require a human ruling for denied child-run allocation; verification keeps final denied expectation unfixed. Source reread: `docs/TYPES.md` Section 10 and `docs/CONTRACT.md` K-SUBAGENT-1. |
| F-002 | Incorporated as interim verification guidance. | Verification now separates denied-before-allocation and denied-after-allocation fixtures pending the human ruling. Source reread: DEL-08-05-REQ-012 and `docs/CONTRACT.md` K-SUBAGENT-1. |
| X-001 | Incorporated with bounded payload language. | DEL-08-05-REQ-005 now requires only sourced `HarnessEvent` envelope plus `runId` and `status` linkage; additional `data` keys remain TBD. Source reread: `docs/SPEC.md` Section 9.1 and `docs/TYPES.md` Sections 7.3 and 10. |
| E-001 | Cross-disposed to Procedure verification. | Artifact metadata assertions are enumerated in `Procedure.md` Verification. Source reread: `docs/PRD.md` Section 10.5. |
| E-002 | Converted to explicit category boundary. | DEL-08-05-REQ-004 states that no sourced separate failed/cancelled/denied subagent event category names exist; terminal state is carried by status until governed source text changes. Source reread: `docs/PRD.md` Section 8.12, `docs/SPEC.md` Section 9.4, and `docs/TYPES.md` Sections 7.3 and 10. |

#### Documentation

Required or anticipated artifacts for this deliverable:

- Parent-child event records.
- Child output artifact paths.
- Subagent replay fixtures.
- Schema or type definitions for `HarnessSubagentRun` if not already present.
- Tests or fixtures proving replay across `subagent.started` and `subagent.completed`.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | PRD hash mismatch: referenced PRD expected SHA does not match observed SHA. | `_REFERENCES.md` REF-006 expected hash | `_REFERENCES.md` REF-006 actual hash; runtime assignment says treat as warning | All PRD-derived requirements | Use PRD content as accessible source with source warning; do not block P1/P2. | TBD |
| Denied allocation ruling | Denied subagent attempts may be represented as permission events, child-run records with `status: denied`, or both. | `docs/TYPES.md` Section 10 includes `denied` status | `docs/CONTRACT.md` K-SUBAGENT-1 describes fail-closed delegation gate | DEL-08-05-REQ-012; replay fixtures | Record permission denial always; create child-run `denied` record only after run allocation boundary is defined. | TBD |
