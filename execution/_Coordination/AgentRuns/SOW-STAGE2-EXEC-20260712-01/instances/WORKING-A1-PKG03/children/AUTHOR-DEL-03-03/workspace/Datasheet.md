# Datasheet: DEL-03-03 Harness API and SSE Compatibility Adapter

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-03-03 |
| DeliverableName | Harness API and SSE Compatibility Adapter |
| PackageID | PKG-03 |
| PackageName | Runtime Engine Contract and Turn Lifecycle |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ResponsibleParty | TBD |
| Type | API_CONTRACT |
| ContextEnvelope | S |
| ScopeItems | SOW-011, SOW-040 |
| SupportsObjectives | OBJ-001, OBJ-002 |

Source: `_CONTEXT.md` Identity and Traceability; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-03 deliverable table.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary subject | Compatibility adapter for harness API routes and browser-facing SSE event names while runtime policy moves behind services. | `_CONTEXT.md` Deliverable Scope; decomposition DEL-03-03 entry |
| API surface in scope | `/api/harness/session/create`, `/api/harness/session/boot`, `/api/harness/session/list`, `/api/harness/session/[id]`, `/api/harness/turn`, `/api/harness/interrupt`, `/api/harness/scaffold`. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1 |
| Turn route role | `/api/harness/turn` remains a transport adapter that validates request shape, obtains session lock, forwards input to `TurnEngine`, writes SSE, and handles cleanup. | `docs/SPEC.md` Section 10.4 |
| Browser SSE event names | `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, `harness:event`. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4; `docs/PRD.md` Section 9.3; D-APP-40 |
| Runtime/UI contract separation | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts; UI events remain stable and compact. | `docs/CONTRACT.md` Section 1.5 K-EVENT-1; `docs/PRD.md` Section 8.12 FR-074 |
| Adapter boundary | SDK messages are not the browser contract or canonical persisted event contract; provider/SDK fields belong at adapter metadata boundaries. | `docs/SPEC.md` Section 10.3; `docs/DIRECTIVE.md` Sections 2.8 and 2.10 |
| Anticipated artifacts | Route adapter tests; SSE compatibility fixtures; UI event contract docs. | `_CONTEXT.md` Anticipated Artifacts |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Compatibility condition | Existing route shapes and SSE event names remain stable during SDK adoption and `TurnEngine` extraction. | `docs/SPEC.md` Sections 11 and 17.1; `docs/PRD.md` Sections 9.1 and 9.3 |
| Active-turn condition | Only one active turn may run per session; concurrent turn attempts return `TURN_IN_PROGRESS`. | `docs/PRD.md` Section 8.3 FR-018 |
| Stream termination condition | The stream terminates with a process-level completion/error signal unless the client disconnects. | `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3 |
| Disconnect condition | Client disconnect cleanup records cancellation once the event log exists. | `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3 |
| Source-state status | `docs/PRD.md` is reconciled under the current D-APP-38 authority corpus; PRD-derived route/SSE details are accepted for this tranche. | `_REFERENCES.md` REF-006; D-APP-38 |

## Construction

| Component | Construction Notes | Source |
|---|---|---|
| Route adapter layer | Keep `/api/harness/turn` as SSE transport adapter; runtime policy belongs behind `TurnEngine` and engine contract services. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` Section 8.12 FR-071 |
| SSE encoder/fixture layer | Preserve named SSE events listed in SPEC/TYPES/PRD; additional tool progress events require UI compatibility handling. | `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3 |
| UI/runtime mapper boundary | Map SDK messages into browser `UIEvent`s and richer persisted `HarnessEvent`s without exposing SDK message names as public UI contract. | `docs/PRD.md` Sections 8.12 FR-116 and 9.3 |
| Test artifacts | Build route adapter tests, SSE compatibility fixtures, and UI event contract docs. Exact fixture payloads are TBD pending current implementation capture. | `_CONTEXT.md` Anticipated Artifacts; `docs/PRD.md` Section 12.6 |

## References

| RefID | Source | Source Slice Used | Status |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Sections 2.8, 2.10 | MATCH |
| REF-002 | `docs/CONTRACT.md` | Section 1.5; Enforcement Map Summary | MATCH |
| REF-003 | `docs/SPEC.md` | Sections 10, 11, 17.1 | MATCH |
| REF-004 | `docs/TYPES.md` | Sections 7.1, 7.2, 7.3, 7.4 | MATCH |
| REF-005 | `docs/PLAN.md` | R1 acceptance and route/SSE stability context | MATCH |
| REF-006 | `docs/PRD.md` | Sections 8.3, 8.12, 9.1, 9.3, 12.5, 12.6, R1 roadmap | MATCH under the current D-APP-38 authority corpus |
| REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method reference only; no deliverable-specific details used | MATCH |
