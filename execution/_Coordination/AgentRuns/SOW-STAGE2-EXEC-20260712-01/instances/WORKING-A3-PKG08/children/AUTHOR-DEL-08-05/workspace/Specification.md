# Specification: DEL-08-05 Subagent Child Run Records and Artifacts

## Scope

This deliverable specifies the data-record and artifact-reference behavior for governed Type 2 subagent child runs. It covers parent-child runtime records, child status, timestamps, SDK agent metadata when available, and output artifact paths.

This deliverable excludes the admission decision and permission gate implementation for subagent execution. That bridge is assigned to DEL-08-04. It also excludes retired PKG-08 hardening scope such as unified pipeline run records, dependency graph generation, deliverable locks, and staleness propagation.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-08-05-REQ-001 | The implementation shall represent governed child execution with a `ChildRunRecord` containing `childRunId`, `parentSessionId`, `parentPersona`, `agentName`, `projectRoot`, `mode`, `status`, `capabilityPolicy`, and `governance`. | `docs/TYPES.md` Section 10; D-APP-40 |
| DEL-08-05-REQ-002 | The child run status shall use only `queued`, `running`, `completed`, `failed`, `cancelled`, or `denied`. | `docs/TYPES.md` Section 10 |
| DEL-08-05-REQ-003 | The child run record shall support optional `parentTurnId`, `outputArtifactPath`, and adapter metadata fields such as adapter session, agent, task, tool-use, or transcript identifiers. | `docs/TYPES.md` Section 10; D-APP-40 |
| DEL-08-05-REQ-004 | Parent session runtime events shall record subagent lifecycle using `subagent.started`, `subagent.progress`, `subagent.completed`, and `subagent.failed` event categories when subagent lifecycle support is active. Terminal child state is carried through `ChildRunRecord.status` and event data. | `docs/PRD.md` Section 8.12; `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Sections 7.3 and 10; D-APP-40 |
| DEL-08-05-REQ-005 | Persisted runtime events shall conform to the `HarnessEvent` shape: `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`. For subagent lifecycle events, `data` shall preserve child-run linkage through `childRunId` and the current or terminal `status`; exact additional payload keys remain bounded by the `ChildRunRecord` contract unless a later governed source specifies them. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Sections 7.3 and 10; D-APP-40 |
| DEL-08-05-REQ-006 | Runtime events shall append to newline-delimited JSONL in write sequence, with unique event IDs. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` FR-073 |
| DEL-08-05-REQ-007 | Child output payloads that are too large for inline event storage shall be stored under session artifacts and referenced by metadata/path. | `docs/SPEC.md` Sections 9.2 and 10.5; `docs/PRD.md` FR-096 |
| DEL-08-05-REQ-008 | Artifact metadata shall include tool name, turn ID, byte count, truncation flag, and relative artifact path where the artifact policy applies. | `docs/PRD.md` Section 10.5 |
| DEL-08-05-REQ-009 | Event and artifact records shall avoid storing secrets and shall pass through redaction where policy requires. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-075 |
| DEL-08-05-REQ-010 | SDK transcript paths or SDK session identifiers shall remain secondary runtime metadata unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` K-SDK-3; `docs/TYPES.md` Section 7.2 |
| DEL-08-05-REQ-011 | The data model shall not reactivate retired unified pipeline run records or broader PKG-08 hardening scope. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
| DEL-08-05-REQ-012 | A denied subagent attempt shall produce a `ChildRunRecord` with `status: denied` only when the attempt reaches the child-run record layer. Denials before allocation may remain permission or hook evidence only. | `docs/TYPES.md` Section 10; `docs/CONTRACT.md` K-SUBAGENT-1; D-APP-40 |

## Standards

| Standard / Contract | Applicability |
|---|---|
| `HarnessEvent` persisted event schema | Governs parent session event records and subagent lifecycle mirror events. |
| `ChildRunRecord` type target | Governs child run record fields and status vocabulary. |
| Runtime Audit Mirror | `.chirality/sessions/<id>/events.jsonl` remains the product-owned event store. |
| Tool Result Artifact policy | Governs child output artifact storage and metadata. |
| Subagent governance invariants | Child records must align with fail-closed governance, restricted capability inheritance, and output references. |

## Verification

| Requirement IDs | Verification Approach |
|---|---|
| DEL-08-05-REQ-001 through DEL-08-05-REQ-003 | Type-level tests or schema tests validate required fields, optional fields, and status enum values. |
| DEL-08-05-REQ-004 through DEL-08-05-REQ-006 | Event writer/replay tests validate lifecycle event categories, `HarnessEvent` shape, append ordering, unique event IDs, child `childRunId` linkage, and status propagation through the child run record or lifecycle event data. |
| DEL-08-05-REQ-007 through DEL-08-05-REQ-008 | Artifact-store tests validate child output storage, relative path references, byte counts, and truncation metadata. |
| DEL-08-05-REQ-009 | Redaction tests validate that secrets do not enter event data or stored artifacts. |
| DEL-08-05-REQ-010 | Replay/session tests validate that SDK transcript metadata does not replace canonical Chirality events. |
| DEL-08-05-REQ-011 | Scope-boundary review verifies no retired unified pipeline run record behavior is introduced. |
| DEL-08-05-REQ-012 | D-APP-40 fixes the denied-allocation test boundary: keep denied-before-allocation and denied-after-allocation fixtures separate, and require `ChildRunRecord.status = denied` only after the child-run record layer is reached. |

## Pass 3 Disposition Evidence

| ItemID | Disposition | Evidence |
|---|---|---|
| C-001 | Resolved by D-APP-38. | Conflict Table now treats PRD-derived requirements and guidance as current under the D-APP-38 authority corpus. Source reread: `_REFERENCES.md` REF-006 and current Conflict Table. |
| F-001 | Resolved by D-APP-40. | DENIED child-run allocation is required only after the runtime reaches the child-run record layer; earlier denials may remain permission or hook evidence. Source reread: D-APP-40, `docs/TYPES.md` Section 10, and `docs/CONTRACT.md` K-SUBAGENT-1. |
| F-002 | Resolved by D-APP-40. | Verification separates denied-before-allocation and denied-after-allocation fixtures according to the D-APP-40 allocation boundary. Source reread: DEL-08-05-REQ-012 and `docs/CONTRACT.md` K-SUBAGENT-1. |
| X-001 | Incorporated with bounded payload language. | DEL-08-05-REQ-005 now requires only sourced `HarnessEvent` envelope plus `childRunId` and `status` linkage; additional `data` keys remain bounded by the child-run contract. Source reread: `docs/SPEC.md` Section 9.1 and `docs/TYPES.md` Sections 7.3 and 10. |
| E-001 | Cross-disposed to Procedure verification. | Artifact metadata assertions are enumerated in `Procedure.md` Verification. Source reread: `docs/PRD.md` Section 10.5. |
| E-002 | Converted to explicit category boundary. | DEL-08-05-REQ-004 states that no sourced separate failed/cancelled/denied subagent event category names exist; terminal state is carried by status until governed source text changes. Source reread: `docs/PRD.md` Section 8.12, `docs/SPEC.md` Section 9.4, and `docs/TYPES.md` Sections 7.3 and 10. |

## Documentation

Required or anticipated artifacts for this deliverable:

- Parent-child event records.
- Child output artifact paths.
- Subagent replay fixtures.
- Schema or type definitions for `ChildRunRecord` if not already present.
- Tests or fixtures proving replay across `subagent.started` and `subagent.completed`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | Former PRD source-state warning resolved by D-APP-38. | `_REFERENCES.md` REF-006 | D-APP-38 current authority corpus | All PRD-derived requirements | Use PRD content under the current authority corpus; keep implementation proof separate from source-state proof. | D-APP-38 accepted current authority corpus |
| Denied allocation ruling | Resolved by D-APP-40. | `docs/TYPES.md` Section 10 includes `denied` status | `docs/CONTRACT.md` K-SUBAGENT-1 describes fail-closed delegation gate | DEL-08-05-REQ-012; replay fixtures | Record permission denial always; create child-run `denied` record only after the runtime reaches the child-run record layer. | Ruled 2026-06-21 |

## D-APP-56 child-output amendment (2026-07-12)

R4-P32 assigns `artifacts/subagents/` child-output storage to DEL-08-05 and makes the live thresholds normative for its child-run records: inline output is limited to 16 KiB and artifact-backed output to 512 KiB. These are distinct from DEL-05-05 `descriptor.resultBudget`.
