# Datasheet: DEL-08-05 Subagent Child Run Records and Artifacts

## Identification

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

## Attributes

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

## Conditions

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

## Construction

### Target `ChildRunRecord` Fields

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

### Related `HarnessEvent` Fields

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

## References

- `docs/DIRECTIVE.md` - runtime audit mirror and subagent governance direction.
- `docs/CONTRACT.md` - event, hook, and subagent invariants.
- `docs/SPEC.md` - event schema, artifact policy, and runtime engine contract.
- `docs/TYPES.md` - `HarnessEvent`, session artifact, and `ChildRunRecord` type targets.
- `docs/PLAN.md` - R5 governed subagent runtime sequencing and retired-scope boundary.
- `docs/PRD.md` - runtime event, artifact, and subagent requirements. Current under the D-APP-38 authority corpus.
- `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` - decomposition method reference.

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-138 records the implemented ChildRunRecord fields: remove `completedAt`; include `mode`, `capabilityPolicy`, `governance`, and `contractVersion`; examples must not invent persona/sdkAgentId/model timestamps. UPD-139 marks only artifact-policy row DEP-08-05-006 satisfied.
