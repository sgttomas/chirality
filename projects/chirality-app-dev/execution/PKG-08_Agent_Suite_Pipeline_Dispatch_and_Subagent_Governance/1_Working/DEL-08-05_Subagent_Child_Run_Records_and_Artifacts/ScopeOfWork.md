---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-05
package_id: PKG-08
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-063]
package_objective_refs: [OBJ-003, OBJ-007]
---

# Scope of Work — DEL-08-05

## Purpose and Objective Traceability

This Scope of Work defines `DEL-08-05` in service of project scope [SOW-063] and package objectives [OBJ-003, OBJ-007].

- **OUT-001** — The DEL-08-05 managed-child runtime record and artifact contract, including `ChildRunRecord` lifecycle, parent/declaration linkage, coordination-aware persistence, `artifacts/subagents/` child outputs, and replay fixtures, for SOW-063 and OBJ-003, OBJ-007.
- **OUT-002** — The v3.0.0-rc.1 carrier outputs assigned to `DEL-08-05` by the applied decomposition row (`execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` line 358 at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`): Checkout AgentRun and native-descendant evidence records; parentage/origin and daemon linkage metadata; role/config/model attribution; child output evidence paths; managed/native replay and reconstruction fixtures. Traceable to SOW-063 and OBJ-003, OBJ-007.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-08-05 Subagent Child Run Records and Artifacts

> #### Datasheet: DEL-08-05 Subagent Child Run Records and Artifacts
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-08-05 |
> | DeliverableName | Subagent Child Run Records and Artifacts |
> | PackageID | PKG-08 |
> | PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | DATA_MODEL_CHANGE |
> | ContextEnvelope | M |
> | ResponsibleParty | TBD |
> | CoversScopeItems | SOW-063 |
> | SupportsObjectives | OBJ-003, OBJ-007 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Scope | Persist managed-child lifecycle, direct-parent linkage, declared context/write-target linkage, provider-neutral status, optional adapter metadata, and child-output artifact paths. | D-APP-68 disposition 3; root `AGENTS.md` |
> | Primary record target | `ChildRunRecord` | `docs/TYPES.md` Section 10; D-APP-40 |
> | Parent audit event target | `HarnessEvent` | `docs/TYPES.md` Section 7.3; `docs/SPEC.md` Section 9 |
> | Canonical event store | `.chirality/sessions/<id>/events.jsonl` | `docs/CONTRACT.md` K-EVENT-4; `docs/TYPES.md` Section 7.2 |
> | Child-output artifact folder | `.chirality/sessions/<sessionId>/artifacts/subagents/` | D-APP-56 R4-P32; D-APP-68 dispositions 3 and 5 |
> | Relevant event categories | `subagent.started`, `subagent.progress`, `subagent.completed`, `subagent.failed` | D-APP-40; D-APP-68 disposition 3 |
> | Output artifact policy | Child output is inline through 16 KiB; over-inline output is artifact-backed under `artifacts/subagents/` through 512 KiB, with bounded truncation metadata beyond that ceiling. | D-APP-56 R4-P32; D-APP-68 disposition 5 |
> | Coordination-aware persistence | Managed child records preserve direct-parent identity, declared context/write-target linkage, lifecycle status, and replay linkage to persisted coordination notices, updates, and acknowledgments. | D-APP-68 disposition 3; root `AGENTS.md` |
> | Execution gate relationship | Child records are created for governed subagent execution; governance admission itself belongs to DEL-08-04. | `_CONTEXT.md`; `docs/PRD.md` FR-101 and FR-102 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Subagent delegation must fail closed unless governance conditions pass. | Required. | `docs/CONTRACT.md` K-SUBAGENT-1 |
> | Managed children may not expand parent capabilities or authority. | Required. | `docs/CONTRACT.md` K-SUBAGENT-2; root `AGENTS.md` |
> | Subagent runs must produce parent-child runtime records and output artifact references when execution is enabled. | Required. | `docs/CONTRACT.md` K-SUBAGENT-3 |
> | Runtime events must redact secrets. | Required. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-075 |
> | JSONL replay must tolerate malformed trailing records. | Required for the event store. | `docs/CONTRACT.md` K-EVENT-5; `docs/SPEC.md` Section 9.2 |
> | SDK transcripts are secondary unless imported into `HarnessEvent` form. | Required. | `docs/CONTRACT.md` K-SDK-3; `docs/SPEC.md` Section 8 |
> | Unified pipeline run records remain retired scope. | Required boundary. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
> | PRD source status | `docs/PRD.md` is reconciled under the current D-APP-38 authority corpus; PRD-derived subagent and artifact details are accepted for this tranche. | `_REFERENCES.md`; D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>

### CLM-006 — Target `ChildRunRecord` Fields

> ###### Target `ChildRunRecord` Fields
>
> | Field | Type / Allowed Value | Requirement Status | Source |
> |---|---|---|---|
> | `childRunId` | string | Required by type target. | `docs/TYPES.md` Section 10; D-APP-40 |
> | `parentSessionId` | string | Required by type target. | `docs/TYPES.md` Section 10 |
> | `parentTurnId` | string | Optional by type target. | `docs/TYPES.md` Section 10 |
> | `parentPersona` | string | Required by type target. | `docs/TYPES.md` Section 10 |
> | `agentName` | string | Required by type target. | `docs/TYPES.md` Section 10 |
> | `adapter.adapterAgentId` | string | Optional adapter metadata when available. | `docs/TYPES.md` Section 10; `docs/PRD.md` FR-101 |
> | `projectRoot` | string | Required by type target. | `docs/TYPES.md` Section 10 |
> | `status` | `queued`, `running`, `completed`, `failed`, `cancelled`, `denied` | Required by type target. | `docs/TYPES.md` Section 10 |
> | `mode` | string | Required by the implemented child-run contract. | D-APP-56 R5 P45 UPD-138 |
> | `capabilityPolicy` | object | Required by the implemented child-run contract. | D-APP-56 R5 P45 UPD-138 |
> | `governance` | object | Required by the implemented child-run contract. | D-APP-56 R5 P45 UPD-138 |
> | `contractVersion` | string | Required by the implemented child-run contract. | D-APP-56 R5 P45 UPD-138 |
> | `outputArtifactPath` | string | Optional by type target; required when child output is stored externally. | `docs/TYPES.md` Section 10; `docs/PRD.md` FR-101 |
>

### CLM-007 — Related `HarnessEvent` Fields

> ###### Related `HarnessEvent` Fields
>
> | Field | Type / Allowed Value | Requirement Status | Source |
> |---|---|---|---|
> | `schemaVersion` | `1` | Required by type target. | `docs/TYPES.md` Section 7.3; `docs/SPEC.md` Section 9.1 |
> | `eventId` | string | Required; unique per event. | `docs/SPEC.md` Section 9.2 |
> | `sessionId` | string | Required. | `docs/SPEC.md` Section 9.1 |
> | `turnId` | string | Optional. | `docs/SPEC.md` Section 9.1 |
> | `parentEventId` | string | Optional. | `docs/SPEC.md` Section 9.1 |
> | `timestamp` | string | Required. | `docs/SPEC.md` Section 9.1 |
> | `type` | string; includes later categories `subagent.started` and `subagent.completed` | Required. | `docs/SPEC.md` Sections 9.1 and 9.4 |
> | `data` | `Record<string, unknown>` | Required; must avoid secrets. | `docs/SPEC.md` Sections 9.1 and 9.2 |
>

### CLM-008 — References

> ##### References
>
> - `docs/DIRECTIVE.md` - runtime audit mirror and subagent governance direction.
> - `docs/CONTRACT.md` - event, hook, and subagent invariants.
> - `docs/SPEC.md` - event schema, artifact policy, and runtime engine contract.
> - `docs/TYPES.md` - `HarnessEvent`, session artifact, and `ChildRunRecord` type targets.
> - `docs/PLAN.md` - R5 governed subagent runtime sequencing and retired-scope boundary.
> - `docs/PRD.md` - runtime event, artifact, and subagent requirements. Current under the D-APP-38 authority corpus.
> - `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` - decomposition method reference.
>

### CLM-009 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-138 records the implemented ChildRunRecord fields: remove `completedAt`; include `mode`, `capabilityPolicy`, `governance`, and `contractVersion`; examples must not invent persona/sdkAgentId/model timestamps. UPD-139 marks only artifact-policy row DEP-08-05-006 satisfied.

### CLM-037 — Applied decomposition v3 carrier assignment (SCA-APP-008 Gate 5, 2026-09-03)

> ##### Applied decomposition row for DEL-08-05 at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`
>
> The accepted SCA-APP-008 Gate-5 application (PR #662) amended this deliverable's row. The row text below is transcribed verbatim from the applied decomposition and is the sole scope basis for the v3 outputs and requirements added on 2026-09-03; it adds no obligation beyond the row.
>
> | Column | Applied row text |
> |---|---|
> | Description | Preserve reconstructible checkout-contained records for Chirality-managed and delegated-harness-native descendants without conflating the classes: parentage, native origin/lineage, selected role-entry state, actual adapter/provider/model, instruction/brief and policy/configuration digests, approvals, status, return/output and accepted artifact paths, cancellation/cleanup, and truthful `instruction-asserted` calibration where G-ROLE cannot mechanically prove Agent 2/TASK non-delegation. |
> | Principal outputs | Checkout AgentRun and native-descendant evidence records; parentage/origin and daemon linkage metadata; role/config/model attribution; child output evidence paths; managed/native replay and reconstruction fixtures |
> | Notes | Project evidence slice; daemon operational state is non-authoritative, native descent assigns no Agent 0/1/2 role, and managed sealed-brief evidence remains distinct and required. Evidence schema follows accepted class semantics. |

## Completion and Reliance Basis — Epistemology

### CLM-010 — Specification: DEL-08-05 Subagent Child Run Records and Artifacts

> #### Specification: DEL-08-05 Subagent Child Run Records and Artifacts
>

### CLM-011 — Scope

> ##### Scope
>
> This deliverable specifies the data-record and artifact-reference behavior for governed managed child sessions. It covers child lifecycle, direct-parent identity, declared context/write-target linkage, provider-neutral status, optional adapter metadata, coordination-aware persistence, and `artifacts/subagents/` output paths.
>
> This deliverable excludes the admission decision and permission gate implementation for subagent execution. That bridge is assigned to DEL-08-04. It also excludes retired PKG-08 hardening scope such as unified pipeline run records, dependency graph generation, deliverable locks, and staleness propagation.
>

### CLM-012 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-08-05-REQ-001 | The implementation shall represent governed child execution with a `ChildRunRecord` containing `childRunId`, `parentSessionId`, `parentPersona`, `agentName`, `projectRoot`, `mode`, `status`, `capabilityPolicy`, and `governance`. | `docs/TYPES.md` Section 10; D-APP-40 |
> | DEL-08-05-REQ-002 | The child run status shall use only `queued`, `running`, `completed`, `failed`, `cancelled`, or `denied`. | `docs/TYPES.md` Section 10 |
> | DEL-08-05-REQ-003 | The child run record shall support optional `parentTurnId`, `outputArtifactPath`, and adapter metadata fields such as adapter session, agent, task, tool-use, or transcript identifiers. | `docs/TYPES.md` Section 10; D-APP-40 |
> | DEL-08-05-REQ-004 | Parent session runtime events shall record subagent lifecycle using `subagent.started`, `subagent.progress`, `subagent.completed`, and `subagent.failed` event categories when subagent lifecycle support is active. Terminal child state is carried through `ChildRunRecord.status` and event data. | `docs/PRD.md` Section 8.12; `docs/SPEC.md` Section 9.4; `docs/TYPES.md` Sections 7.3 and 10; D-APP-40 |
> | DEL-08-05-REQ-005 | Persisted runtime events shall conform to the `HarnessEvent` shape: `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`. For subagent lifecycle events, `data` shall preserve child-run linkage through `childRunId` and the current or terminal `status`; exact additional payload keys remain bounded by the `ChildRunRecord` contract unless a later governed source specifies them. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Sections 7.3 and 10; D-APP-40 |
> | DEL-08-05-REQ-006 | Runtime events shall append to newline-delimited JSONL in write sequence, with unique event IDs. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` FR-073 |
> | DEL-08-05-REQ-007 | Child output shall remain inline through 16 KiB; over-inline output shall be stored under `.chirality/sessions/<sessionId>/artifacts/subagents/` and referenced by metadata/path through the 512 KiB artifact ceiling, with bounded preview/truncation metadata for larger original output. | D-APP-56 R4-P32; D-APP-68 disposition 5 |
> | DEL-08-05-REQ-008 | Artifact metadata shall include tool name, turn ID, byte count, truncation flag, and relative artifact path where the artifact policy applies. | `docs/PRD.md` Section 10.5 |
> | DEL-08-05-REQ-009 | Event and artifact records shall avoid storing secrets and shall pass through redaction where policy requires. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-075 |
> | DEL-08-05-REQ-010 | SDK transcript paths or SDK session identifiers shall remain secondary runtime metadata unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` K-SDK-3; `docs/TYPES.md` Section 7.2 |
> | DEL-08-05-REQ-011 | The data model shall not reactivate retired unified pipeline run records or broader PKG-08 hardening scope. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
> | DEL-08-05-REQ-012 | A denied subagent attempt shall produce a `ChildRunRecord` with `status: denied` only when the attempt reaches the child-run record layer. Denials before allocation may remain permission or hook evidence only. | `docs/TYPES.md` Section 10; `docs/CONTRACT.md` K-SUBAGENT-1; D-APP-40 |
> | DEL-08-05-REQ-013 | Each managed child record shall preserve its direct-parent identity, lifecycle status, and linkage to the sealed declared context and write targets; persisted coordination notices, updates, and acknowledgments shall remain replayable with that parent/child lineage. | D-APP-68 disposition 3; root `AGENTS.md` |
>

### CLM-013 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability |
> |---|---|
> | `HarnessEvent` persisted event schema | Governs parent session event records and subagent lifecycle mirror events. |
> | `ChildRunRecord` type target | Governs child run record fields and status vocabulary. |
> | Runtime Audit Mirror | `.chirality/sessions/<id>/events.jsonl` remains the product-owned event store. |
> | DEL-08-05 child-output artifact policy | Governs `artifacts/subagents/` persistence and its 16 KiB inline / 512 KiB artifact ceilings; it is distinct from DEL-05-05 ordinary tool-result `descriptor.resultBudget`. |
> | Subagent governance invariants | Child records must align with fail-closed governance, restricted capability inheritance, and output references. |
>

### CLM-014 — Verification

> ##### Verification
>
> | Requirement IDs | Verification Approach |
> |---|---|
> | DEL-08-05-REQ-001 through DEL-08-05-REQ-003 | Type-level tests or schema tests validate required fields, optional fields, and status enum values. |
> | DEL-08-05-REQ-004 through DEL-08-05-REQ-006 | Event writer/replay tests validate lifecycle event categories, `HarnessEvent` shape, append ordering, unique event IDs, child `childRunId` linkage, and status propagation through the child run record or lifecycle event data. |
> | DEL-08-05-REQ-007 through DEL-08-05-REQ-008 | Artifact-store tests validate child output storage, relative path references, byte counts, and truncation metadata. |
> | DEL-08-05-REQ-009 | Redaction tests validate that secrets do not enter event data or stored artifacts. |
> | DEL-08-05-REQ-010 | Replay/session tests validate that SDK transcript metadata does not replace canonical Chirality events. |
> | DEL-08-05-REQ-011 | Scope-boundary review verifies no retired unified pipeline run record behavior is introduced. |
> | DEL-08-05-REQ-012 | D-APP-40 fixes the denied-allocation test boundary: keep denied-before-allocation and denied-after-allocation fixtures separate, and require `ChildRunRecord.status = denied` only after the child-run record layer is reached. |
> | DEL-08-05-REQ-013 | Managed-delegation replay tests validate direct-parent identity, declared-context/write-target linkage, lifecycle state, and coordination notice/update/acknowledgment linkage. |
>

### CLM-015 — Pass 3 Disposition Evidence

> ##### Pass 3 Disposition Evidence
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | C-001 | Resolved by D-APP-38. | Conflict Table now treats PRD-derived requirements and guidance as current under the D-APP-38 authority corpus. Source reread: `_REFERENCES.md` REF-006 and current Conflict Table. |
> | F-001 | Resolved by D-APP-40. | DENIED child-run allocation is required only after the runtime reaches the child-run record layer; earlier denials may remain permission or hook evidence. Source reread: D-APP-40, `docs/TYPES.md` Section 10, and `docs/CONTRACT.md` K-SUBAGENT-1. |
> | F-002 | Resolved by D-APP-40. | Verification separates denied-before-allocation and denied-after-allocation fixtures according to the D-APP-40 allocation boundary. Source reread: DEL-08-05-REQ-012 and `docs/CONTRACT.md` K-SUBAGENT-1. |
> | X-001 | Incorporated with bounded payload language. | DEL-08-05-REQ-005 now requires only sourced `HarnessEvent` envelope plus `childRunId` and `status` linkage; additional `data` keys remain bounded by the child-run contract. Source reread: `docs/SPEC.md` Section 9.1 and `docs/TYPES.md` Sections 7.3 and 10. |
> | E-001 | Cross-disposed to Procedure verification. | Artifact metadata assertions are enumerated in `Procedure.md` Verification. Source reread: `docs/PRD.md` Section 10.5. |
> | E-002 | Converted to explicit category boundary. | DEL-08-05-REQ-004 states that no sourced separate failed/cancelled/denied subagent event category names exist; terminal state is carried by status until governed source text changes. Source reread: `docs/PRD.md` Section 8.12, `docs/SPEC.md` Section 9.4, and `docs/TYPES.md` Sections 7.3 and 10. |
>

### CLM-016 — Documentation

> ##### Documentation
>
> Required or anticipated artifacts for this deliverable:
>
> - Parent-child event records.
> - Child output artifact paths.
> - Subagent replay fixtures.
> - Schema or type definitions for `ChildRunRecord` if not already present.
> - Tests or fixtures proving replay across `subagent.started` and `subagent.completed`.
> - Tests or fixtures proving direct-parent, declared-context/write-target, and coordination-message linkage.
>

### CLM-017 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | C-001 | Former PRD source-state warning resolved by D-APP-38. | `_REFERENCES.md` REF-006 | D-APP-38 current authority corpus | All PRD-derived requirements | Use PRD content under the current authority corpus; keep implementation proof separate from source-state proof. | D-APP-38 accepted current authority corpus |
> | Denied allocation ruling | Resolved by D-APP-40. | `docs/TYPES.md` Section 10 includes `denied` status | `docs/CONTRACT.md` K-SUBAGENT-1 describes fail-closed delegation gate | DEL-08-05-REQ-012; replay fixtures | Record permission denial always; create child-run `denied` record only after the runtime reaches the child-run record layer. | Ruled 2026-06-21 |
>

### CLM-018 — D-APP-56 child-output amendment (2026-07-12)

> ##### D-APP-56 child-output amendment (2026-07-12)
>
> R4-P32 assigns `artifacts/subagents/` child-output storage to DEL-08-05 and makes the live thresholds normative for its child-run records: inline output is limited to 16 KiB and artifact-backed output to 512 KiB. These are distinct from DEL-05-05 `descriptor.resultBudget`.

- **REQ-001** — The deliverable shall preserve reconstructible checkout-contained records for Chirality-managed and delegated-harness-native descendants without conflating the classes.
- **REQ-002** — Each record shall carry parentage, native origin/lineage, selected role-entry state, actual adapter/provider/model, instruction/brief and policy/configuration digests, approvals, status, return/output and accepted artifact paths, and cancellation/cleanup.
- **REQ-003** — Records shall carry truthful `instruction-asserted` calibration where G-ROLE cannot mechanically prove Agent 2/TASK non-delegation; native descent assigns no Agent 0/1/2 role.
- **REQ-004** — Daemon operational state is non-authoritative; managed sealed-brief evidence remains distinct and required; the evidence schema follows accepted class semantics.
- **AC-001** — DEL-08-05 is accepted when the complete preserved legacy source's schema/type, lifecycle-event, append/replay, artifact-reference, redaction, SDK-metadata-boundary, denied-allocation, and retired-scope checks demonstrate auditable governed child-run records for SOW-063 and OBJ-003, OBJ-007.
- **AC-002** — The v3 outputs assigned by the applied decomposition row (checkout AgentRun and native-descendant evidence records, parentage/origin and daemon linkage metadata, role/config/model attribution, child output evidence paths, and managed/native replay and reconstruction fixtures) exist and satisfy REQ-001 through REQ-004 with the two descendant classes kept distinct.

## Production and Verification Method — Praxeology

### CLM-019 — Procedure: DEL-08-05 Subagent Child Run Records and Artifacts

> #### Procedure: DEL-08-05 Subagent Child Run Records and Artifacts
>

### CLM-020 — Purpose

> ##### Purpose
>
> Define the operational steps for producing and validating the subagent child run record and artifact-reference slice for governed Type 2 subagent execution.
>

### CLM-021 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Note |
> |---|---|
> | Accepted source corpus listed in `_REFERENCES.md` | Available under the current D-APP-38 authority corpus. |
> | DEL-08-04 Type 2 Subagent Governance Bridge | Upstream relationship is implied by scope, but `_DEPENDENCIES.md` has no accepted dependency edge yet. Keep as ASSUMPTION until dependency extraction runs. |
> | Runtime event schema / `HarnessEvent` | Required source target exists in `docs/SPEC.md` and `docs/TYPES.md`. |
> | Artifact storage policy | Required source target exists in `docs/SPEC.md` and `docs/PRD.md`. |
> | Human ruling for denied child-run allocation | D-APP-40 ruled: denied records are required only after the runtime reaches the child-run record layer. |
>

### CLM-022 — Steps

> ##### Steps
>
> 1. Confirm the deliverable remains scoped to child run records and artifact references, not the governance admission bridge.
> 2. Define or update the `ChildRunRecord` data shape with the sourced fields from `docs/TYPES.md` Section 10.
> 3. Ensure `status` accepts only `queued`, `running`, `completed`, `failed`, `cancelled`, and `denied`.
> 4. Link each managed child to its direct parent session using `parentSessionId`; include `parentTurnId` when associated with a turn, and retain declared-context/write-target linkage from the sealed brief.
> 5. Capture runtime metadata without invention: `parentPersona`, `agentName`, `projectRoot`, `mode`, `capabilityPolicy`, `governance`, `contractVersion`, and optional adapter metadata.
> 6. Capture only lifecycle fields present in the implemented contract; do not reintroduce removed or provider-shaped timestamps.
> 7. Emit or map parent-session events for lifecycle using the provider-neutral `subagent.started`, `subagent.progress`, `subagent.completed`, and `subagent.failed` categories accepted by D-APP-40.
> 8. Keep child output inline through 16 KiB; store over-inline output under `artifacts/subagents/` through 512 KiB and preserve bounded preview/truncation metadata beyond the ceiling.
> 9. Record `outputArtifactPath` when a child output artifact is created.
> 10. Apply redaction policy before persisting event data, run logs, or artifacts.
> 11. Keep SDK transcript identifiers and paths as secondary metadata; do not replace canonical Chirality events with SDK transcripts.
> 12. Add replay fixtures for parent-child linkage and child output artifact paths.
> 13. Add or update tests for completed, failed, cancelled, denied-before-allocation, and denied-after-allocation behavior. D-APP-40 requires `status: denied` only after the child-run record layer is reached; earlier denials may remain permission/hook evidence.
> 14. Verify the implementation does not introduce retired unified pipeline run records, dependency graph generation, deliverable locks, or staleness propagation tooling.
> 15. Verify direct-parent identity, declared context/write targets, and coordination notice/update/acknowledgment records remain linked and replayable across the managed child lifecycle.
>

### CLM-023 — Verification

> ##### Verification
>
> | Check | Expected Result |
> |---|---|
> | `ChildRunRecord` required fields | `childRunId`, `parentSessionId`, `parentPersona`, `agentName`, `projectRoot`, `mode`, `status`, `capabilityPolicy`, and `governance` are required. |
> | Status enum | Only `queued`, `running`, `completed`, `failed`, `cancelled`, and `denied` are accepted. |
> | Event envelope | Subagent lifecycle events use the `HarnessEvent` envelope with schema version, unique event ID, session ID, timestamp, type, and data payload. |
> | Append-only storage | Runtime events are appended as newline-delimited JSONL in write sequence. |
> | Artifact references | Child output through 16 KiB remains inline; over-inline output is referenced under `artifacts/subagents/` through the 512 KiB artifact ceiling, with bounded truncation metadata beyond it. |
> | Artifact metadata fields | Where the artifact policy applies, fixture assertions cover tool name, turn ID, byte count, truncation flag, and relative artifact path. |
> | Redaction | Secrets are absent from event data and artifact metadata. |
> | Replay | Replay can reconstruct parent session, child lifecycle, terminal child status, and child output artifact path. |
> | Terminal subagent state | Failed, cancelled, and denied terminal states are asserted through `ChildRunRecord.status` and provider-neutral subagent lifecycle event data. |
> | Scope boundary | No retired PKG-08 pipeline run-record behavior is introduced. |
> | Managed lineage | Direct parent, declared context/write targets, lifecycle, and coordination message linkage are persisted and replayable. |
>

### CLM-024 — Pass 3 Disposition Evidence

> ##### Pass 3 Disposition Evidence
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | F-001 | Resolved by D-APP-40. | Prerequisites and Step 13 apply the denied child-run allocation boundary. Source reread: `docs/TYPES.md` Section 10 and `docs/CONTRACT.md` K-SUBAGENT-1. |
> | F-002 | Resolved by D-APP-40. | Step 13 separates denied-before-allocation and denied-after-allocation behavior according to the ruled boundary. Source reread: Specification DEL-08-05-REQ-012. |
> | E-001 | Incorporated. | Verification now enumerates tool name, turn ID, byte count, truncation flag, and relative artifact path for artifact metadata fixture assertions. Source reread: `docs/PRD.md` Section 10.5. |
> | E-002 | Incorporated as a terminal-state category boundary. | Step 7 and Verification assert terminal state through `ChildRunRecord.status` and provider-neutral subagent lifecycle event data. Source reread: `docs/PRD.md` Section 8.12, `docs/SPEC.md` Section 9.4, and `docs/TYPES.md` Sections 7.3 and 10. |
>

### CLM-025 — Records

> ##### Records
>
> - `ChildRunRecord` schema/type and tests.
> - `HarnessEvent` subagent lifecycle event fixtures.
> - Child output artifact path fixtures.
> - Replay fixtures covering parent-child linkage.
> - D-APP-40 ruling record for denied child-run allocation semantics.

- **VER-001** — Review the complete preserved legacy source and execute its specified type/schema, status-enum, lifecycle-event, append-order, unique-event-ID, parent-child-linkage, artifact-metadata/path, redaction, replay, denied-allocation, and scope-boundary checks; record concrete evidence.
- **VER-002** — Replay and reconstruct managed and native descendant records from checkout-contained evidence; confirm parentage, origin/lineage, role-entry state, adapter/provider/model, digests, approvals, status, artifact paths, cancellation/cleanup, and `instruction-asserted` calibration reproduce without class conflation.

## Governing Values and Decisions — Axiology

### CLM-026 — Guidance: DEL-08-05 Subagent Child Run Records and Artifacts

> #### Guidance: DEL-08-05 Subagent Child Run Records and Artifacts
>

### CLM-027 — Purpose

> ##### Purpose
>
> This deliverable makes governed subagent execution replayable and auditable without expanding subagent authority. Its product value is the durable record of what child agent was requested, how it was linked to the parent session or turn, what status it reached, and where any child output artifact was stored.
>

### CLM-028 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Keep Chirality events canonical. | Treat `.chirality/sessions/<id>/events.jsonl` and `HarnessEvent` replay as the product-owned audit mirror. SDK transcript paths may be linked but should not become canonical unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` K-EVENT-4 and K-SDK-3 |
> | Separate governance gate from child record persistence. | DEL-08-04 owns the subagent governance bridge. DEL-08-05 should persist the resulting child lifecycle and artifact references without weakening or duplicating admission rules. | `_CONTEXT.md`; `docs/PRD.md` FR-101 and FR-102 |
> | Fail closed is still visible. | Denied or failed subagent actions should leave reviewable runtime evidence. D-APP-40 fixes the boundary: create a denied `ChildRunRecord` only when the runtime reaches the child-run record layer; earlier denials may remain permission/hook evidence. | `docs/CONTRACT.md` K-SUBAGENT-1; `docs/TYPES.md` Section 10; D-APP-40 |
> | Store references, not bulky payloads. | Child output through 16 KiB remains inline; larger output is represented under `artifacts/subagents/` with relative artifact metadata through 512 KiB and bounded truncation beyond it. | D-APP-56 R4-P32; D-APP-68 disposition 5 |
> | Do not reintroduce retired scope. | Runtime event logging and child-run records are not the retired unified pipeline run record system. Avoid names, APIs, or storage layouts that imply pipeline-wide run-record reactivation. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 |
> | Preserve professional and security boundaries. | Event data and artifacts should avoid secrets and should not represent child output as professional approval, certification, or external validation. | `docs/CONTRACT.md` K-EVENT-6; `docs/PRD.md` FR-115 |
>

### CLM-029 — Considerations

> ##### Considerations
>
> - `ChildRunRecord` should be small and stable. Put bulky child output in artifacts, not in the record itself.
> - `childRunId` should be distinct from `eventId`; lifecycle events can reference the child run, while the child run remains the durable summary of the child execution.
> - `parentSessionId` is required and `parentTurnId` is optional. The implementation should handle session-level child delegation if a future flow lacks a turn ID.
> - `sdkAgentId`, `model`, and SDK transcript metadata may be unavailable for some runtime paths. These fields should remain optional rather than synthesized.
> - `status` should reflect the child run lifecycle, not the parent turn outcome. A parent turn can fail after a child completed, and a child can fail while the parent records that failure successfully.
> - Artifact paths should be relative to session-controlled storage when possible to support migration and replay.
> - The child-output 16 KiB/512 KiB policy is owned solely here. DEL-05-05 owns the distinct ordinary tool-result `descriptor.resultBudget` and does not duplicate these thresholds.
> - Managed replay should bind lifecycle and coordination traffic to direct-parent identity and the sealed declared context/write targets without turning artifacts into authority.
> - Replay fixtures should cover at least completed, failed, cancelled, and denied status behavior. D-APP-40 fixes the denied-record expectation: require `ChildRunRecord.status = denied` only after the child-run record layer is reached.
>

### CLM-030 — Trade-offs

> ##### Trade-offs
>
> | Topic | Option | Trade-off |
> |---|---|---|
> | Denied attempts | Record only `tool.permission` / hook denial events | Avoids allocating child runs before execution but may make subagent-specific denial replay less direct. |
> | Denied attempts | Create `ChildRunRecord` with `status: denied` after the child-run record layer is reached | Makes subagent denial visible in one record family while preserving D-APP-40's allocation boundary. |
> | SDK metadata | Store only stable Chirality fields | More portable and less coupled, but loses SDK-specific debugging detail. |
> | SDK metadata | Store optional SDK identifiers and transcript paths | Better debugging and resume correlation, but must remain secondary to Chirality events. |
> | Output storage | Inline small child summaries | Easier replay and inspection for small data. |
> | Output storage | Store child outputs as artifacts | Better for large data and context hygiene, but requires artifact lifecycle and path validation. |
>

### CLM-031 — Examples

> ##### Examples
>

### CLM-032 — Example `ChildRunRecord`

> ###### Example `ChildRunRecord`
>
> ```json
> {
>   "childRunId": "child_123",
>   "parentSessionId": "session_abc",
>   "parentTurnId": "turn_001",
>   "parentPersona": "WORKING_ITEMS",
>   "agentName": "TASK",
>   "projectRoot": "/absolute/project/root",
>   "mode": "workspaceWrite",
>   "status": "completed",
>   "capabilityPolicy": {},
>   "governance": {},
>   "contractVersion": "1",
>   "outputArtifactPath": ".chirality/sessions/session_abc/artifacts/subagents/child_123/output.json"
> }
> ```
>

### CLM-033 — Example Lifecycle Event Payload

> ###### Example Lifecycle Event Payload
>
> ```json
> {
>   "schemaVersion": 1,
>   "eventId": "event_456",
>   "sessionId": "session_abc",
>   "turnId": "turn_001",
>   "timestamp": "2026-05-20T00:00:00.000Z",
>   "type": "subagent.started",
>   "data": {
>     "childRunId": "child_123",
>     "agentName": "TASK",
>     "status": "running"
>   }
> }
> ```
>
> The exact event payload keys inside `data` are bounded by the sourced `HarnessEvent` envelope and the minimum child-run linkage needed for replay (`childRunId` plus current or terminal `status`).
>

### CLM-034 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | C-001 | Former PRD source-state warning resolved by D-APP-38. | `_REFERENCES.md` REF-006 | D-APP-38 current authority corpus | PRD-derived guidance and requirements | Use PRD content under the current authority corpus; keep implementation proof separate from source-state proof. | D-APP-38 accepted current authority corpus |
> | Denied allocation ruling | D-APP-40 resolves denied allocation: denials before child-run allocation may remain permission/hook evidence; after the child-run record layer is reached, create a `ChildRunRecord` with `status: denied`. | `docs/TYPES.md` Section 10 includes `denied` status | `docs/CONTRACT.md` K-SUBAGENT-1 describes fail-closed delegation gate | Denial replay, schema tests, procedure verification | Record permission denial always; create child-run `denied` record only after the child-run record layer is reached. | Ruled 2026-06-21 |
>

### CLM-035 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-138 records the implemented ChildRunRecord fields: remove `completedAt`; include `mode`, `capabilityPolicy`, `governance`, and `contractVersion`; examples must not invent persona/sdkAgentId/model timestamps. UPD-139 marks only artifact-policy row DEP-08-05-006 satisfied.

### CLM-036 — D-APP-68 managed-orchestration ownership mapping (2026-07-19)

> ##### D-APP-68 managed-orchestration ownership mapping (2026-07-19)
>
> DEL-08-05 is the sole owner of managed-child lifecycle, direct-parent linkage, declared-context/write-target linkage, replayable child-run records, coordination-aware persistence, and `artifacts/subagents/` child-output persistence. D-APP-56 R4-P32 already makes 16 KiB inline and 512 KiB artifact-backed limits normative here; D-APP-68 disposition 5 confirms that policy without changing either value or transferring ownership. DEL-05-05 remains limited to ordinary tool-result `descriptor.resultBudget` and ToolResultStore semantics. DEL-08-04 separately owns admission and `delegate_agent`; this deliverable does not duplicate the gate.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-063 OBJ-003 OBJ-007 | CLM-010 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
| OUT-002 | SOW-063 OBJ-003 OBJ-007 | CLM-037 REQ-001 REQ-002 REQ-003 REQ-004 | AC-002 | VER-002 | Managed/native replay and reconstruction fixtures; attribution and lineage records; sealed-brief evidence kept distinct from native-descent records |
