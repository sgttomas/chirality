# Specification: DEL-08-05 Subagent Child Run Records and Artifacts

## Scope

This deliverable specifies the data-record and artifact-reference behavior for governed Type 2 subagent child runs. It covers parent-child runtime records, child status, timestamps, SDK agent metadata when available, and output artifact paths.

This deliverable excludes the admission decision and permission gate implementation for subagent execution. That bridge is assigned to DEL-08-04. It also excludes retired PKG-08 hardening scope such as unified pipeline run records, dependency graph generation, deliverable locks, and staleness propagation.

## Requirements

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

## Standards

| Standard / Contract | Applicability |
|---|---|
| `HarnessEvent` persisted event schema | Governs parent session event records and subagent lifecycle mirror events. |
| `HarnessSubagentRun` type target | Governs child run record fields and status vocabulary. |
| Runtime Audit Mirror | `.chirality/sessions/<id>/events.jsonl` remains the product-owned event store. |
| Tool Result Artifact policy | Governs child output artifact storage and metadata. |
| Subagent governance invariants | Child records must align with fail-closed governance, restricted capability inheritance, and output references. |

## Verification

| Requirement IDs | Verification Approach |
|---|---|
| DEL-08-05-REQ-001 through DEL-08-05-REQ-003 | Type-level tests or schema tests validate required fields, optional fields, and status enum values. |
| DEL-08-05-REQ-004 through DEL-08-05-REQ-006 | Event writer/replay tests validate lifecycle event categories, `HarnessEvent` shape, append ordering, unique event IDs, child `runId` linkage, and status propagation through the child run record or lifecycle event data. |
| DEL-08-05-REQ-007 through DEL-08-05-REQ-008 | Artifact-store tests validate child output storage, relative path references, byte counts, and truncation metadata. |
| DEL-08-05-REQ-009 | Redaction tests validate that secrets do not enter event data or stored artifacts. |
| DEL-08-05-REQ-010 | Replay/session tests validate that SDK transcript metadata does not replace canonical Chirality events. |
| DEL-08-05-REQ-011 | Scope-boundary review verifies no retired unified pipeline run record behavior is introduced. |
| DEL-08-05-REQ-012 | Human ruling required before final denied-allocation test expectation is fixed; interim tests should keep denied-before-allocation and denied-after-allocation fixtures separate. |

## Pass 3 Disposition Evidence

| ItemID | Disposition | Evidence |
|---|---|---|
| C-001 | Already covered; retained as a source-authority conflict. | Conflict Table keeps REF-006 hash mismatch warning for PRD-derived requirements and guidance. Source reread: `_REFERENCES.md` REF-006 and current Conflict Table. |
| F-001 | Converted to explicit TBD/human-ruling language. | DEL-08-05-REQ-012 continues to require a human ruling for denied child-run allocation; verification keeps final denied expectation unfixed. Source reread: `docs/TYPES.md` Section 10 and `docs/CONTRACT.md` K-SUBAGENT-1. |
| F-002 | Incorporated as interim verification guidance. | Verification now separates denied-before-allocation and denied-after-allocation fixtures pending the human ruling. Source reread: DEL-08-05-REQ-012 and `docs/CONTRACT.md` K-SUBAGENT-1. |
| X-001 | Incorporated with bounded payload language. | DEL-08-05-REQ-005 now requires only sourced `HarnessEvent` envelope plus `runId` and `status` linkage; additional `data` keys remain TBD. Source reread: `docs/SPEC.md` Section 9.1 and `docs/TYPES.md` Sections 7.3 and 10. |
| E-001 | Cross-disposed to Procedure verification. | Artifact metadata assertions are enumerated in `Procedure.md` Verification. Source reread: `docs/PRD.md` Section 10.5. |
| E-002 | Converted to explicit category boundary. | DEL-08-05-REQ-004 states that no sourced separate failed/cancelled/denied subagent event category names exist; terminal state is carried by status until governed source text changes. Source reread: `docs/PRD.md` Section 8.12, `docs/SPEC.md` Section 9.4, and `docs/TYPES.md` Sections 7.3 and 10. |

## Documentation

Required or anticipated artifacts for this deliverable:

- Parent-child event records.
- Child output artifact paths.
- Subagent replay fixtures.
- Schema or type definitions for `HarnessSubagentRun` if not already present.
- Tests or fixtures proving replay across `subagent.started` and `subagent.completed`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | PRD hash mismatch: referenced PRD expected SHA does not match observed SHA. | `_REFERENCES.md` REF-006 expected hash | `_REFERENCES.md` REF-006 actual hash; runtime assignment says treat as warning | All PRD-derived requirements | Use PRD content as accessible source with source warning; do not block P1/P2. | TBD |
| Denied allocation ruling | Denied subagent attempts may be represented as permission events, child-run records with `status: denied`, or both. | `docs/TYPES.md` Section 10 includes `denied` status | `docs/CONTRACT.md` K-SUBAGENT-1 describes fail-closed delegation gate | DEL-08-05-REQ-012; replay fixtures | Record permission denial always; create child-run `denied` record only after run allocation boundary is defined. | TBD |
