---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-05
package_id: PKG-08
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
project_scope_refs: [SOW-063]
package_objective_refs: [OBJ-003, OBJ-007]
---

# Scope of Work — DEL-08-05

## Purpose and Objective Traceability

This migration candidate defines `DEL-08-05` in service of project scope [SOW-063] and package objectives [OBJ-003, OBJ-007].

- **OUT-001** — The DEL-08-05 parent-child runtime record and artifact-reference contract, including ChildRunRecord status and metadata, HarnessEvent lifecycle linkage, child output artifact paths, and replay fixtures, for SOW-063 and OBJ-003, OBJ-007.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-08-05 Subagent Child Run Records and Artifacts

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":2,"line_start":1,"source_sha256":"7cd96f1df3e7498364a7921f05bf74c6b3353580f577e7aa701424b3ff12055b","target_id":"CLM-001"} -->
#### Datasheet: DEL-08-05 Subagent Child Run Records and Artifacts

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":18,"line_start":3,"source_sha256":"7cd96f1df3e7498364a7921f05bf74c6b3353580f577e7aa701424b3ff12055b","target_id":"CLM-002"} -->
##### Identification

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

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":31,"line_start":19,"source_sha256":"7cd96f1df3e7498364a7921f05bf74c6b3353580f577e7aa701424b3ff12055b","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Scope | Persist parent-child runtime records, status, timestamps, SDK agent metadata, and output artifact paths. | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-08-05 |
| Primary record target | `ChildRunRecord` | `docs/TYPES.md` Section 10; D-APP-40 |
| Parent audit event target | `HarnessEvent` | `docs/TYPES.md` Section 7.3; `docs/SPEC.md` Section 9 |
| Canonical event store | `.chirality/sessions/<id>/events.jsonl` | `docs/CONTRACT.md` K-EVENT-4; `docs/TYPES.md` Section 7.2 |
| Artifact folder | `.chirality/sessions/<sessionId>/artifacts/` | `docs/TYPES.md` Section 7.2; `docs/PRD.md` Section 10.5 |
| Relevant event categories | `subagent.started`, `subagent.completed` | `docs/PRD.md` Section 8.12; `docs/SPEC.md` Section 9.4 |
| Output artifact policy | Large payloads are stored as artifacts and referenced by metadata; child-run outputs use output artifact references. | `docs/SPEC.md` Sections 9.2 and 10.5; `docs/PLAN.md` R5 |
| Execution gate relationship | Child records are created for governed subagent execution; governance admission itself belongs to DEL-08-04. | `_CONTEXT.md`; `docs/PRD.md` FR-101 and FR-102 |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":44,"line_start":32,"source_sha256":"7cd96f1df3e7498364a7921f05bf74c6b3353580f577e7aa701424b3ff12055b","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Subagent delegation must fail closed unless governance conditions pass. | Required. | `docs/CONTRACT.md` K-SUBAGENT-1 |
| SDK subagents may not expand parent capabilities. | Required. | `docs/CONTRACT.md` K-SUBAGENT-2 |
| Subagent runs must produce parent-child runtime records and output artifact references when execution is enabled. | Required. | `docs/CONTRACT.md` K-SUBAGENT-3 |
| Runtime events must redact secrets. | Required. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-075 |
| JSONL replay must tolerate malformed trailing records. | Required for the event store. | `docs/CONTRACT.md` K-EVENT-5; `docs/SPEC.md` Section 9.2 |
| SDK transcripts are secondary unless imported into `HarnessEvent` form. | Required. | `docs/CONTRACT.md` K-SDK-3; `docs/SPEC.md` Section 8 |
| Unified pipeline run records remain retired scope. | Required boundary. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
| PRD source status | `docs/PRD.md` is reconciled under the current D-APP-38 authority corpus; PRD-derived subagent and artifact details are accepted for this tranche. | `_REFERENCES.md`; D-APP-38 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":46,"line_start":45,"source_sha256":"7cd96f1df3e7498364a7921f05bf74c6b3353580f577e7aa701424b3ff12055b","target_id":"CLM-005"} -->
##### Construction

<!-- sow-source-end -->

### CLM-006 — Target `ChildRunRecord` Fields

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":61,"line_start":47,"source_sha256":"7cd96f1df3e7498364a7921f05bf74c6b3353580f577e7aa701424b3ff12055b","target_id":"CLM-006"} -->
###### Target `ChildRunRecord` Fields

| Field | Type / Allowed Value | Requirement Status | Source |
|---|---|---|---|
| `childRunId` | string | Required by type target. | `docs/TYPES.md` Section 10; D-APP-40 |
| `parentSessionId` | string | Required by type target. | `docs/TYPES.md` Section 10 |
| `parentTurnId` | string | Optional by type target. | `docs/TYPES.md` Section 10 |
| `parentPersona` | string | Required by type target. | `docs/TYPES.md` Section 10 |
| `agentName` | string | Required by type target. | `docs/TYPES.md` Section 10 |
| `adapter.adapterAgentId` | string | Optional adapter metadata when available. | `docs/TYPES.md` Section 10; `docs/PRD.md` FR-101 |
| `projectRoot` | string | Required by type target. | `docs/TYPES.md` Section 10 |
| `status` | `queued`, `running`, `completed`, `failed`, `cancelled`, `denied` | Required by type target. | `docs/TYPES.md` Section 10 |
| `completedAt` | string | Optional by type target. | `docs/TYPES.md` Section 10 |
| `outputArtifactPath` | string | Optional by type target; required when child output is stored externally. | `docs/TYPES.md` Section 10; `docs/PRD.md` FR-101 |

<!-- sow-source-end -->

### CLM-007 — Related `HarnessEvent` Fields

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":74,"line_start":62,"source_sha256":"7cd96f1df3e7498364a7921f05bf74c6b3353580f577e7aa701424b3ff12055b","target_id":"CLM-007"} -->
###### Related `HarnessEvent` Fields

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

<!-- sow-source-end -->

### CLM-008 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":84,"line_start":75,"source_sha256":"7cd96f1df3e7498364a7921f05bf74c6b3353580f577e7aa701424b3ff12055b","target_id":"CLM-008"} -->
##### References

- `docs/DIRECTIVE.md` - runtime audit mirror and subagent governance direction.
- `docs/CONTRACT.md` - event, hook, and subagent invariants.
- `docs/SPEC.md` - event schema, artifact policy, and runtime engine contract.
- `docs/TYPES.md` - `HarnessEvent`, session artifact, and `ChildRunRecord` type targets.
- `docs/PLAN.md` - R5 governed subagent runtime sequencing and retired-scope boundary.
- `docs/PRD.md` - runtime event, artifact, and subagent requirements. Current under the D-APP-38 authority corpus.
- `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` - decomposition method reference.

<!-- sow-source-end -->

### CLM-009 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":87,"line_start":85,"source_sha256":"7cd96f1df3e7498364a7921f05bf74c6b3353580f577e7aa701424b3ff12055b","target_id":"CLM-009"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-138 records the implemented ChildRunRecord fields: remove `completedAt`; include `mode`, `capabilityPolicy`, `governance`, and `contractVersion`; examples must not invent persona/sdkAgentId/model timestamps. UPD-139 marks only artifact-policy row DEP-08-05-006 satisfied.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-010 — Specification: DEL-08-05 Subagent Child Run Records and Artifacts

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"f142d6e4abee57ac2d9326f34b191f31391de94c91c641ce006cbe6441d8fdd7","target_id":"CLM-010"} -->
#### Specification: DEL-08-05 Subagent Child Run Records and Artifacts

<!-- sow-source-end -->

### CLM-011 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":8,"line_start":3,"source_sha256":"f142d6e4abee57ac2d9326f34b191f31391de94c91c641ce006cbe6441d8fdd7","target_id":"CLM-011"} -->
##### Scope

This deliverable specifies the data-record and artifact-reference behavior for governed Type 2 subagent child runs. It covers parent-child runtime records, child status, timestamps, SDK agent metadata when available, and output artifact paths.

This deliverable excludes the admission decision and permission gate implementation for subagent execution. That bridge is assigned to DEL-08-04. It also excludes retired PKG-08 hardening scope such as unified pipeline run records, dependency graph generation, deliverable locks, and staleness propagation.

<!-- sow-source-end -->

### CLM-012 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":25,"line_start":9,"source_sha256":"f142d6e4abee57ac2d9326f34b191f31391de94c91c641ce006cbe6441d8fdd7","target_id":"CLM-012"} -->
##### Requirements

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

<!-- sow-source-end -->

### CLM-013 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":35,"line_start":26,"source_sha256":"f142d6e4abee57ac2d9326f34b191f31391de94c91c641ce006cbe6441d8fdd7","target_id":"CLM-013"} -->
##### Standards

| Standard / Contract | Applicability |
|---|---|
| `HarnessEvent` persisted event schema | Governs parent session event records and subagent lifecycle mirror events. |
| `ChildRunRecord` type target | Governs child run record fields and status vocabulary. |
| Runtime Audit Mirror | `.chirality/sessions/<id>/events.jsonl` remains the product-owned event store. |
| Tool Result Artifact policy | Governs child output artifact storage and metadata. |
| Subagent governance invariants | Child records must align with fail-closed governance, restricted capability inheritance, and output references. |

<!-- sow-source-end -->

### CLM-014 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":47,"line_start":36,"source_sha256":"f142d6e4abee57ac2d9326f34b191f31391de94c91c641ce006cbe6441d8fdd7","target_id":"CLM-014"} -->
##### Verification

| Requirement IDs | Verification Approach |
|---|---|
| DEL-08-05-REQ-001 through DEL-08-05-REQ-003 | Type-level tests or schema tests validate required fields, optional fields, and status enum values. |
| DEL-08-05-REQ-004 through DEL-08-05-REQ-006 | Event writer/replay tests validate lifecycle event categories, `HarnessEvent` shape, append ordering, unique event IDs, child `childRunId` linkage, and status propagation through the child run record or lifecycle event data. |
| DEL-08-05-REQ-007 through DEL-08-05-REQ-008 | Artifact-store tests validate child output storage, relative path references, byte counts, and truncation metadata. |
| DEL-08-05-REQ-009 | Redaction tests validate that secrets do not enter event data or stored artifacts. |
| DEL-08-05-REQ-010 | Replay/session tests validate that SDK transcript metadata does not replace canonical Chirality events. |
| DEL-08-05-REQ-011 | Scope-boundary review verifies no retired unified pipeline run record behavior is introduced. |
| DEL-08-05-REQ-012 | D-APP-40 fixes the denied-allocation test boundary: keep denied-before-allocation and denied-after-allocation fixtures separate, and require `ChildRunRecord.status = denied` only after the child-run record layer is reached. |

<!-- sow-source-end -->

### CLM-015 — Pass 3 Disposition Evidence

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":58,"line_start":48,"source_sha256":"f142d6e4abee57ac2d9326f34b191f31391de94c91c641ce006cbe6441d8fdd7","target_id":"CLM-015"} -->
##### Pass 3 Disposition Evidence

| ItemID | Disposition | Evidence |
|---|---|---|
| C-001 | Resolved by D-APP-38. | Conflict Table now treats PRD-derived requirements and guidance as current under the D-APP-38 authority corpus. Source reread: `_REFERENCES.md` REF-006 and current Conflict Table. |
| F-001 | Resolved by D-APP-40. | DENIED child-run allocation is required only after the runtime reaches the child-run record layer; earlier denials may remain permission or hook evidence. Source reread: D-APP-40, `docs/TYPES.md` Section 10, and `docs/CONTRACT.md` K-SUBAGENT-1. |
| F-002 | Resolved by D-APP-40. | Verification separates denied-before-allocation and denied-after-allocation fixtures according to the D-APP-40 allocation boundary. Source reread: DEL-08-05-REQ-012 and `docs/CONTRACT.md` K-SUBAGENT-1. |
| X-001 | Incorporated with bounded payload language. | DEL-08-05-REQ-005 now requires only sourced `HarnessEvent` envelope plus `childRunId` and `status` linkage; additional `data` keys remain bounded by the child-run contract. Source reread: `docs/SPEC.md` Section 9.1 and `docs/TYPES.md` Sections 7.3 and 10. |
| E-001 | Cross-disposed to Procedure verification. | Artifact metadata assertions are enumerated in `Procedure.md` Verification. Source reread: `docs/PRD.md` Section 10.5. |
| E-002 | Converted to explicit category boundary. | DEL-08-05-REQ-004 states that no sourced separate failed/cancelled/denied subagent event category names exist; terminal state is carried by status until governed source text changes. Source reread: `docs/PRD.md` Section 8.12, `docs/SPEC.md` Section 9.4, and `docs/TYPES.md` Sections 7.3 and 10. |

<!-- sow-source-end -->

### CLM-016 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":68,"line_start":59,"source_sha256":"f142d6e4abee57ac2d9326f34b191f31391de94c91c641ce006cbe6441d8fdd7","target_id":"CLM-016"} -->
##### Documentation

Required or anticipated artifacts for this deliverable:

- Parent-child event records.
- Child output artifact paths.
- Subagent replay fixtures.
- Schema or type definitions for `ChildRunRecord` if not already present.
- Tests or fixtures proving replay across `subagent.started` and `subagent.completed`.

<!-- sow-source-end -->

### CLM-017 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":75,"line_start":69,"source_sha256":"f142d6e4abee57ac2d9326f34b191f31391de94c91c641ce006cbe6441d8fdd7","target_id":"CLM-017"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | Former PRD source-state warning resolved by D-APP-38. | `_REFERENCES.md` REF-006 | D-APP-38 current authority corpus | All PRD-derived requirements | Use PRD content under the current authority corpus; keep implementation proof separate from source-state proof. | D-APP-38 accepted current authority corpus |
| Denied allocation ruling | Resolved by D-APP-40. | `docs/TYPES.md` Section 10 includes `denied` status | `docs/CONTRACT.md` K-SUBAGENT-1 describes fail-closed delegation gate | DEL-08-05-REQ-012; replay fixtures | Record permission denial always; create child-run `denied` record only after the runtime reaches the child-run record layer. | Ruled 2026-06-21 |

<!-- sow-source-end -->

### CLM-018 — D-APP-56 child-output amendment (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":78,"line_start":76,"source_sha256":"f142d6e4abee57ac2d9326f34b191f31391de94c91c641ce006cbe6441d8fdd7","target_id":"CLM-018"} -->
##### D-APP-56 child-output amendment (2026-07-12)

R4-P32 assigns `artifacts/subagents/` child-output storage to DEL-08-05 and makes the live thresholds normative for its child-run records: inline output is limited to 16 KiB and artifact-backed output to 512 KiB. These are distinct from DEL-05-05 `descriptor.resultBudget`.
<!-- sow-source-end -->

- **AC-001** — DEL-08-05 is accepted when the complete preserved legacy source's schema/type, lifecycle-event, append/replay, artifact-reference, redaction, SDK-metadata-boundary, denied-allocation, and retired-scope checks demonstrate auditable governed child-run records for SOW-063 and OBJ-003, OBJ-007.

## Production and Verification Method — Praxeology

### CLM-019 — Procedure: DEL-08-05 Subagent Child Run Records and Artifacts

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"ba4bdbb0c9c414ee85d61c45c360c40cff6a00cd59f1fb0db5dfcb606885e417","target_id":"CLM-019"} -->
#### Procedure: DEL-08-05 Subagent Child Run Records and Artifacts

<!-- sow-source-end -->

### CLM-020 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"ba4bdbb0c9c414ee85d61c45c360c40cff6a00cd59f1fb0db5dfcb606885e417","target_id":"CLM-020"} -->
##### Purpose

Define the operational steps for producing and validating the subagent child run record and artifact-reference slice for governed Type 2 subagent execution.

<!-- sow-source-end -->

### CLM-021 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":16,"line_start":7,"source_sha256":"ba4bdbb0c9c414ee85d61c45c360c40cff6a00cd59f1fb0db5dfcb606885e417","target_id":"CLM-021"} -->
##### Prerequisites

| Prerequisite | Status / Note |
|---|---|
| Accepted source corpus listed in `_REFERENCES.md` | Available under the current D-APP-38 authority corpus. |
| DEL-08-04 Type 2 Subagent Governance Bridge | Upstream relationship is implied by scope, but `_DEPENDENCIES.md` has no accepted dependency edge yet. Keep as ASSUMPTION until dependency extraction runs. |
| Runtime event schema / `HarnessEvent` | Required source target exists in `docs/SPEC.md` and `docs/TYPES.md`. |
| Artifact storage policy | Required source target exists in `docs/SPEC.md` and `docs/PRD.md`. |
| Human ruling for denied child-run allocation | D-APP-40 ruled: denied records are required only after the runtime reaches the child-run record layer. |

<!-- sow-source-end -->

### CLM-022 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":33,"line_start":17,"source_sha256":"ba4bdbb0c9c414ee85d61c45c360c40cff6a00cd59f1fb0db5dfcb606885e417","target_id":"CLM-022"} -->
##### Steps

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

<!-- sow-source-end -->

### CLM-023 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":48,"line_start":34,"source_sha256":"ba4bdbb0c9c414ee85d61c45c360c40cff6a00cd59f1fb0db5dfcb606885e417","target_id":"CLM-023"} -->
##### Verification

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

<!-- sow-source-end -->

### CLM-024 — Pass 3 Disposition Evidence

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":57,"line_start":49,"source_sha256":"ba4bdbb0c9c414ee85d61c45c360c40cff6a00cd59f1fb0db5dfcb606885e417","target_id":"CLM-024"} -->
##### Pass 3 Disposition Evidence

| ItemID | Disposition | Evidence |
|---|---|---|
| F-001 | Resolved by D-APP-40. | Prerequisites and Step 13 apply the denied child-run allocation boundary. Source reread: `docs/TYPES.md` Section 10 and `docs/CONTRACT.md` K-SUBAGENT-1. |
| F-002 | Resolved by D-APP-40. | Step 13 separates denied-before-allocation and denied-after-allocation behavior according to the ruled boundary. Source reread: Specification DEL-08-05-REQ-012. |
| E-001 | Incorporated. | Verification now enumerates tool name, turn ID, byte count, truncation flag, and relative artifact path for artifact metadata fixture assertions. Source reread: `docs/PRD.md` Section 10.5. |
| E-002 | Incorporated as a terminal-state category boundary. | Step 7 and Verification assert terminal state through `ChildRunRecord.status` and provider-neutral subagent lifecycle event data. Source reread: `docs/PRD.md` Section 8.12, `docs/SPEC.md` Section 9.4, and `docs/TYPES.md` Sections 7.3 and 10. |

<!-- sow-source-end -->

### CLM-025 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":64,"line_start":58,"source_sha256":"ba4bdbb0c9c414ee85d61c45c360c40cff6a00cd59f1fb0db5dfcb606885e417","target_id":"CLM-025"} -->
##### Records

- `ChildRunRecord` schema/type and tests.
- `HarnessEvent` subagent lifecycle event fixtures.
- Child output artifact path fixtures.
- Replay fixtures covering parent-child linkage.
- D-APP-40 ruling record for denied child-run allocation semantics.
<!-- sow-source-end -->

- **VER-001** — Review the complete preserved legacy source and execute its specified type/schema, status-enum, lifecycle-event, append-order, unique-event-ID, parent-child-linkage, artifact-metadata/path, redaction, replay, denied-allocation, and scope-boundary checks; record concrete evidence.

## Governing Values and Decisions — Axiology

### CLM-026 — Guidance: DEL-08-05 Subagent Child Run Records and Artifacts

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-026"} -->
#### Guidance: DEL-08-05 Subagent Child Run Records and Artifacts

<!-- sow-source-end -->

### CLM-027 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":6,"line_start":3,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-027"} -->
##### Purpose

This deliverable makes governed subagent execution replayable and auditable without expanding subagent authority. Its product value is the durable record of what child agent was requested, how it was linked to the parent session or turn, what status it reached, and where any child output artifact was stored.

<!-- sow-source-end -->

### CLM-028 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":17,"line_start":7,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-028"} -->
##### Principles

| Principle | Guidance | Source |
|---|---|---|
| Keep Chirality events canonical. | Treat `.chirality/sessions/<id>/events.jsonl` and `HarnessEvent` replay as the product-owned audit mirror. SDK transcript paths may be linked but should not become canonical unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` K-EVENT-4 and K-SDK-3 |
| Separate governance gate from child record persistence. | DEL-08-04 owns the subagent governance bridge. DEL-08-05 should persist the resulting child lifecycle and artifact references without weakening or duplicating admission rules. | `_CONTEXT.md`; `docs/PRD.md` FR-101 and FR-102 |
| Fail closed is still visible. | Denied or failed subagent actions should leave reviewable runtime evidence. D-APP-40 fixes the boundary: create a denied `ChildRunRecord` only when the runtime reaches the child-run record layer; earlier denials may remain permission/hook evidence. | `docs/CONTRACT.md` K-SUBAGENT-1; `docs/TYPES.md` Section 10; D-APP-40 |
| Store references, not bulky payloads. | Child outputs that exceed inline budgets should be represented by artifact metadata and relative paths. | `docs/SPEC.md` Sections 9.2 and 10.5 |
| Do not reintroduce retired scope. | Runtime event logging and child-run records are not the retired unified pipeline run record system. Avoid names, APIs, or storage layouts that imply pipeline-wide run-record reactivation. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
| Preserve professional and security boundaries. | Event data and artifacts should avoid secrets and should not represent child output as professional approval, certification, or external validation. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-115 |

<!-- sow-source-end -->

### CLM-029 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":27,"line_start":18,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-029"} -->
##### Considerations

- `ChildRunRecord` should be small and stable. Put bulky child output in artifacts, not in the record itself.
- `childRunId` should be distinct from `eventId`; lifecycle events can reference the child run, while the child run remains the durable summary of the child execution.
- `parentSessionId` is required and `parentTurnId` is optional. The implementation should handle session-level child delegation if a future flow lacks a turn ID.
- `sdkAgentId`, `model`, and SDK transcript metadata may be unavailable for some runtime paths. These fields should remain optional rather than synthesized.
- `status` should reflect the child run lifecycle, not the parent turn outcome. A parent turn can fail after a child completed, and a child can fail while the parent records that failure successfully.
- Artifact paths should be relative to session-controlled storage when possible to support migration and replay.
- Replay fixtures should cover at least completed, failed, cancelled, and denied status behavior. D-APP-40 fixes the denied-record expectation: require `ChildRunRecord.status = denied` only after the child-run record layer is reached.

<!-- sow-source-end -->

### CLM-030 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":38,"line_start":28,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-030"} -->
##### Trade-offs

| Topic | Option | Trade-off |
|---|---|---|
| Denied attempts | Record only `tool.permission` / hook denial events | Avoids allocating child runs before execution but may make subagent-specific denial replay less direct. |
| Denied attempts | Create `ChildRunRecord` with `status: denied` after the child-run record layer is reached | Makes subagent denial visible in one record family while preserving D-APP-40's allocation boundary. |
| SDK metadata | Store only stable Chirality fields | More portable and less coupled, but loses SDK-specific debugging detail. |
| SDK metadata | Store optional SDK identifiers and transcript paths | Better debugging and resume correlation, but must remain secondary to Chirality events. |
| Output storage | Inline small child summaries | Easier replay and inspection for small data. |
| Output storage | Store child outputs as artifacts | Better for large data and context hygiene, but requires artifact lifecycle and path validation. |

<!-- sow-source-end -->

### CLM-031 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":40,"line_start":39,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-031"} -->
##### Examples

<!-- sow-source-end -->

### CLM-032 — Example `ChildRunRecord`

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":61,"line_start":41,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-032"} -->
###### Example `ChildRunRecord`

```json
{
  "childRunId": "child_123",
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

<!-- sow-source-end -->

### CLM-033 — Example Lifecycle Event Payload

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":81,"line_start":62,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-033"} -->
###### Example Lifecycle Event Payload

```json
{
  "schemaVersion": 1,
  "eventId": "event_456",
  "sessionId": "session_abc",
  "turnId": "turn_001",
  "timestamp": "2026-05-20T00:00:00.000Z",
  "type": "subagent.started",
  "data": {
    "childRunId": "child_123",
    "agentName": "TASK",
    "status": "running"
  }
}
```

The exact event payload keys inside `data` are bounded by the sourced `HarnessEvent` envelope and the minimum child-run linkage needed for replay (`childRunId` plus current or terminal `status`).

<!-- sow-source-end -->

### CLM-034 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":88,"line_start":82,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-034"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | Former PRD source-state warning resolved by D-APP-38. | `_REFERENCES.md` REF-006 | D-APP-38 current authority corpus | PRD-derived guidance and requirements | Use PRD content under the current authority corpus; keep implementation proof separate from source-state proof. | D-APP-38 accepted current authority corpus |
| Denied allocation ruling | D-APP-40 resolves denied allocation: denials before child-run allocation may remain permission/hook evidence; after the child-run record layer is reached, create a `ChildRunRecord` with `status: denied`. | `docs/TYPES.md` Section 10 includes `denied` status | `docs/CONTRACT.md` K-SUBAGENT-1 describes fail-closed delegation gate | Denial replay, schema tests, procedure verification | Record permission denial always; create child-run `denied` record only after the child-run record layer is reached. | Ruled 2026-06-21 |

<!-- sow-source-end -->

### CLM-035 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":91,"line_start":89,"source_sha256":"443ba89940a1ca587d96325dad769eb57023b5efc68df93eeb26927c0767f04d","target_id":"CLM-035"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-138 records the implemented ChildRunRecord fields: remove `completedAt`; include `mode`, `capabilityPolicy`, `governance`, and `contractVersion`; examples must not invent persona/sdkAgentId/model timestamps. UPD-139 marks only artifact-policy row DEP-08-05-006 satisfied.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-063 OBJ-003 OBJ-007 | CLM-010 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
