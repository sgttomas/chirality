---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-03
package_id: PKG-03
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-011, SOW-040]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-03-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-03-03` in service of project scope [SOW-011, SOW-040] and package objectives [OBJ-001, OBJ-002].

- **OUT-001** — A harness API and SSE compatibility adapter package for DEL-03-03 comprising the route adapter tests, SSE compatibility fixtures, and UI event contract documentation defined by the preserved legacy source kit.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-03-03 Harness API and SSE Compatibility Adapter

> #### Datasheet: DEL-03-03 Harness API and SSE Compatibility Adapter
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-03-03 |
> | DeliverableName | Harness API and SSE Compatibility Adapter |
> | PackageID | PKG-03 |
> | PackageName | Runtime Engine Contract and Turn Lifecycle |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ResponsibleParty | TBD |
> | Type | API_CONTRACT |
> | ContextEnvelope | S |
> | ScopeItems | SOW-011, SOW-040 |
> | SupportsObjectives | OBJ-001, OBJ-002 |
>
> Source: `_CONTEXT.md` Identity and Traceability; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-03 deliverable table.
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary subject | Compatibility adapter for harness API routes and browser-facing SSE event names while runtime policy moves behind services. | `_CONTEXT.md` Deliverable Scope; decomposition DEL-03-03 entry |
> | API surface in scope | `/api/harness/session/create`, `/api/harness/session/boot`, `/api/harness/session/list`, `/api/harness/session/[id]`, `/api/harness/turn`, `/api/harness/interrupt`, `/api/harness/scaffold`. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1 |
> | Turn route role | `/api/harness/turn` remains a transport adapter that validates request shape, obtains session lock, forwards input to `TurnEngine`, writes SSE, and handles cleanup. | `docs/SPEC.md` Section 10.4 |
> | Browser SSE event names | `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, `harness:event`. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4; `docs/PRD.md` Section 9.3; D-APP-40 |
> | Runtime/UI contract separation | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts; UI events remain stable and compact. | `docs/CONTRACT.md` Section 1.5 K-EVENT-1; `docs/PRD.md` Section 8.12 FR-074 |
> | Adapter boundary | SDK messages are not the browser contract or canonical persisted event contract; provider/SDK fields belong at adapter metadata boundaries. | `docs/SPEC.md` Section 10.3; `docs/DIRECTIVE.md` Sections 2.8 and 2.10 |
> | Anticipated artifacts | Route adapter tests; SSE compatibility fixtures; UI event contract docs. | `_CONTEXT.md` Anticipated Artifacts |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Compatibility condition | Existing route shapes and SSE event names remain stable during SDK adoption and `TurnEngine` extraction. | `docs/SPEC.md` Sections 11 and 17.1; `docs/PRD.md` Sections 9.1 and 9.3 |
> | Active-turn condition | Only one active turn may run per session; concurrent turn attempts return `TURN_IN_PROGRESS`. | `docs/PRD.md` Section 8.3 FR-018 |
> | Stream termination condition | The stream terminates with a process-level completion/error signal unless the client disconnects. | `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3 |
> | Disconnect condition | Client disconnect cleanup records cancellation once the event log exists. | `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3 |
> | Source-state status | `docs/PRD.md` is reconciled under the current D-APP-38 authority corpus; PRD-derived route/SSE details are accepted for this tranche. | `_REFERENCES.md` REF-006; D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Construction Notes | Source |
> |---|---|---|
> | Route adapter layer | Keep `/api/harness/turn` as SSE transport adapter; runtime policy belongs behind `TurnEngine` and engine contract services. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` Section 8.12 FR-071 |
> | SSE encoder/fixture layer | Preserve named SSE events listed in SPEC/TYPES/PRD; additional tool progress events require UI compatibility handling. | `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3 |
> | UI/runtime mapper boundary | Map SDK messages into browser `UIEvent`s and richer persisted `HarnessEvent`s without exposing SDK message names as public UI contract. | `docs/PRD.md` Sections 8.12 FR-116 and 9.3 |
> | Test artifacts | Build route adapter tests, SSE compatibility fixtures, and UI event contract docs. Exact fixture payloads are TBD pending current implementation capture. | `_CONTEXT.md` Anticipated Artifacts; `docs/PRD.md` Section 12.6 |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Source Slice Used | Status |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Sections 2.8, 2.10 | MATCH |
> | REF-002 | `docs/CONTRACT.md` | Section 1.5; Enforcement Map Summary | MATCH |
> | REF-003 | `docs/SPEC.md` | Sections 10, 11, 17.1 | MATCH |
> | REF-004 | `docs/TYPES.md` | Sections 7.1, 7.2, 7.3, 7.4 | MATCH |
> | REF-005 | `docs/PLAN.md` | R1 acceptance and route/SSE stability context | MATCH |
> | REF-006 | `docs/PRD.md` | Sections 8.3, 8.12, 9.1, 9.3, 12.5, 12.6, R1 roadmap | MATCH under the current D-APP-38 authority corpus |
> | REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method reference only; no deliverable-specific details used | MATCH |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-03-03 Harness API and SSE Compatibility Adapter

> #### Specification: DEL-03-03 Harness API and SSE Compatibility Adapter
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable specifies the compatibility adapter contract for harness API routes and browser-facing SSE events during the runtime-engine pivot. It covers:
>
> - preserving `/api/harness/*` route shapes during SDK adoption and `TurnEngine` extraction;
> - keeping `/api/harness/turn` as the SSE transport adapter rather than the owner of runtime policy;
> - preserving browser SSE event names and compact `UIEvent` semantics;
> - separating browser `UIEvent`s from persisted `HarnessEvent`s;
> - defining route adapter tests, SSE compatibility fixtures, and UI event contract documentation.
>
> Source: `_CONTEXT.md` Deliverable Scope; `docs/SPEC.md` Sections 10.4, 11, 17.1; `docs/PRD.md` Sections 8.12, 9.1, 9.3.
>
> Out of scope:
>
> - SDK-specific message translation internals except where they must not leak into the browser contract.
> - `TurnEngine` lifecycle ownership and session locking internals, owned primarily by DEL-03-02.
> - interrupt/cancel terminal outcome handling, owned primarily by DEL-03-04.
> - persisted event schema implementation, owned primarily by PKG-05, except for compatibility assertions that UI and runtime event contracts remain separate.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Verification |
> |---|---|---|
> | DEL-03-03-REQ-001 | The adapter shall preserve the existing `/api/harness/*` route shapes during SDK adoption and `TurnEngine` extraction. Exact existing request/response schemas are TBD pending implementation fixture capture. | Route adapter regression tests compare current and post-extraction route shape fixtures. |
> | DEL-03-03-REQ-002 | `/api/harness/turn` shall remain a transport adapter responsible for request validation, session locking, attachment option forwarding where applicable, SSE encoding, cancellation cleanup, and error response handling. | Route tests and code review verify policy behavior is delegated to `TurnEngine`/services. |
> | DEL-03-03-REQ-003 | Browser-facing turn streams shall emit compatible named SSE events: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, and the additive redacted `harness:event` bridge. Event ordering is unconstrained in this deliverable except where current implementation fixtures or explicit source text later establish an order. | SSE compatibility fixtures assert event names and only source-backed order constraints; unconstrained event paths are recorded as `TBD` or "order unconstrained." |
> | DEL-03-03-REQ-004 | The SSE stream shall terminate with a process-level completion/error signal unless the client disconnects and cancel cleanup runs. | Stream integration test covers normal completion, error, and disconnect cases. |
> | DEL-03-03-REQ-005 | Browser `UIEvent`s and persisted `HarnessEvent`s shall remain separate contracts; persisted events may be richer and versioned, but UI events remain compact and compatible. | Mapper/contract tests reject SDK-shaped leakage into public UI event payloads except explicit adapter metadata where relevant. |
> | DEL-03-03-REQ-006 | SDK messages shall not be treated as the browser contract or canonical persisted event contract. The concrete mapper boundary is expected to be `frontend/src/lib/harness/sdk-message-mapper.ts` during R1, or an explicitly documented equivalent if implementation naming changes. | Mapper tests verify known SDK message categories map through the selected boundary and do not expose SDK-shaped names in public UI events or canonical `HarnessEvent` fields except as adapter metadata. |
> | DEL-03-03-REQ-007 | Additional tool progress events may be introduced only with UI compatibility handling: older clients must either ignore them safely, handle them behind opt-in UI behavior, or receive them only through a documented backward-compatible consumption path. | Compatibility review confirms existing UI consumers handle or ignore added events safely and records the selected handling mode. |
> | DEL-03-03-REQ-008 | The compatibility kit shall include route adapter tests, SSE compatibility fixtures, and UI event contract docs. | Artifact review confirms files exist and reference the source-backed route/event contract. |
> | DEL-03-03-REQ-009 | PRD-derived requirements shall use the current D-APP-38 authority-corpus reference state. | Documentation and test traceability cite the reconciled REF-006 state and rerun D-APP-38 bump/apply when authority documents change. |
> | DEL-03-03-REQ-010 | The route adapter test index shall map each in-scope `/api/harness/*` route to a fixture path or `TBD` capture status before exact compatibility assertions are closed. | Artifact review confirms every route listed in SPEC Section 17.1 and PRD Section 9.1 appears in the route-to-fixture index. |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Source |
> |---|---|---|
> | Product-owned runtime contract | Adapter behavior must serve Chirality-owned `AgentEnginePort`/`RuntimeEngineContract`, not SDK public semantics. | `docs/DIRECTIVE.md` Sections 2.8 and 2.10; `docs/SPEC.md` Section 10 |
> | Browser SSE event contract | Required event names and stream termination behavior. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4; `docs/PRD.md` Section 9.3 |
> | Harness API route contract | `/api/harness/*` route catalog and stability expectation. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1 |
> | Runtime/audit event separation | Browser `UIEvent` and persisted `HarnessEvent` are distinct contracts. | `docs/CONTRACT.md` Section 1.5; `docs/PRD.md` Section 8.12 |
> | Test/validation expectations | Route stream unchanged after SDK-backed `TurnEngine` extraction; SDK message mapper coverage. | `docs/PRD.md` Sections 12.5 and 12.6 |
>

### CLM-011 — Verification

> ##### Verification
>
> | Verification Item | Method | Source Basis |
> |---|---|---|
> | Route shape compatibility | Capture current route request/response/SSE fixtures, then replay against the adapter after extraction. Exact schema capture remains TBD. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1 |
> | SSE event-name compatibility | Assert emitted event names include the documented stable set and preserve existing browser handling. Event order assertions are limited to source-backed or captured-fixture-backed paths; otherwise record order as unconstrained/TBD. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4; `docs/PRD.md` Section 9.3 |
> | Turn route delegation | Unit or route test proves `/api/harness/turn` delegates lifecycle execution behind `TurnEngine` and does not own runtime policy. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` Section 8.12 FR-071 |
> | UI/runtime separation | Mapper and public API tests reject SDK message names as public UI contracts and keep persisted event richness behind `HarnessEvent`; the selected mapper boundary is `sdk-message-mapper.ts` or an explicitly documented equivalent. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-EVENT-1; `docs/PRD.md` Sections 9.3 and 12.5 |
> | Disconnect/terminal behavior hook | Integration tests include normal completion, error, and disconnect paths; detailed terminal persistence belongs to DEL-03-04/PKG-05. | `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3 |
> | Authority-corpus handling | Review confirms REF-006 is reconciled under D-APP-38 and unsupported details stay `TBD`. | `_REFERENCES.md` REF-006; D-APP-38 |
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required documentation artifacts:
>
> - UI event contract docs listing stable SSE event names, payload ownership, and compatibility rules.
> - Route adapter test index mapping each `/api/harness/*` route to preserved shape fixtures.
> - SSE compatibility fixture README describing fixture capture source, replay method, and expected event sequence.
> - Fixture coverage notes identifying the implementation baseline commit/SHA, route fixture path, SSE fixture path, order constraint status, and any payload/schema field marked compatibility-only.
> - Traceability note that PRD-derived requirements use the current D-APP-38 authority-corpus state and require corpus bump/apply after future authority-document edits.
>

### CLM-013 — D-APP-56 route ownership map (2026-07-12)

> ##### D-APP-56 route ownership map (2026-07-12)
>
> R4-P30 assigns the three live uncataloged `/api/harness/*` routes by backing capability: `session/[id]/events` to DEL-05-02 replay ownership, permission routes to the PKG-06 permission owner, and agents routes to the PKG-08 agent-roster owner. The corresponding SPEC 17.1 catalog amendment executes only through the separately governed R4-P06 corpus tranche; this kit note does not pre-apply that corpus edit.

- **AC-001** — DEL-03-03 is acceptable when the preserved legacy requirements for the harness API and SSE compatibility adapter are satisfied and the route adapter tests, SSE compatibility fixtures, and UI event contract documentation provide the specified verification evidence.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-03-03 Harness API and SSE Compatibility Adapter

> #### Procedure: DEL-03-03 Harness API and SSE Compatibility Adapter
>

### CLM-015 — Purpose

> ##### Purpose
>
> Define the working procedure for producing and validating the harness API and SSE compatibility adapter artifacts for DEL-03-03. The procedure is oriented to artifact production and compatibility verification, not to implementing the full `TurnEngine` or SDK adapter internals.
>
> Sources: `_CONTEXT.md` Anticipated Artifacts; `docs/SPEC.md` Sections 10.4, 11, 17.1; `docs/PRD.md` Sections 12.5 and 12.6.
>

### CLM-016 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Notes | Source |
> |---|---|---|
> | Accepted deliverable scope | Available in `_CONTEXT.md`; ResponsibleParty remains TBD. | `_CONTEXT.md` |
> | Authoritative route/event source slices | Available from SPEC, TYPES, CONTRACT, DIRECTIVE, PLAN, and PRD with PRD hash warning. | `_REFERENCES.md` |
> | Current implementation fixture capture | BLOCKING for exact route payload, SSE payload, event-order, and compatibility-only field assertions. Baseline source SHA and fixture paths remain TBD. | `docs/PRD.md` Sections 12.5 and 12.6; `docs/PLAN.md` R1 acceptance |
> | Upstream dependencies | TBD; no accepted dependency edges extracted yet. | `_DEPENDENCIES.md` |
> | Sibling deliverable boundaries | DEL-03-02 owns thin `TurnEngine` and session locking; DEL-03-04 owns interrupt/cancel terminal handling. | Decomposition PKG-03 table |
>

### CLM-017 — Steps

> ##### Steps
>
> 1. Confirm source state.
>    - Read `_REFERENCES.md` and record that `docs/PRD.md` is current under the D-APP-38 authority corpus.
>    - Use PRD-derived details with traceability and keep unsupported details as `TBD`.
>
> 2. Build the compatibility inventory.
>    - List `/api/harness/*` routes from `docs/SPEC.md` Section 17.1 and `docs/PRD.md` Section 9.1.
>    - List stable SSE event names from `docs/SPEC.md` Section 11, `docs/TYPES.md` Section 7.4, and `docs/PRD.md` Section 9.3.
>
> 3. Capture current behavior fixtures.
>    - Record the implementation baseline commit/SHA before capture; if unavailable, record `TBD` and do not close exact compatibility assertions.
>    - Capture route request/response schemas for the in-scope `/api/harness/*` routes.
>    - Capture representative SSE streams for successful turn, error, and disconnect/cancel paths where current implementation permits.
>    - Record which implementation paths can emit successful turn, error, and disconnect/cancel streams; unresolved path availability remains `TBD`.
>    - Mark any unavailable payload details as `TBD` rather than filling from assumption.
>
> 4. Implement or review the route adapter boundary.
>    - Keep `/api/harness/turn` responsible for request validation, session locking, attachment option forwarding where applicable, SSE encoding, cancellation cleanup, and error response handling.
>    - Delegate runtime lifecycle behavior to `TurnEngine` or the agreed service boundary.
>    - Reject SDK message names as browser event names.
>
> 5. Implement or review UI event mapping.
>    - Ensure SDK or engine messages map to compact browser `UIEvent`s and richer persisted `HarnessEvent`s through an adapter/mapper boundary.
>    - Confirm public browser events remain compatible with the stable names.
>
> 6. Add compatibility tests and docs.
>    - Add route adapter tests for preserved route shapes.
>    - Create a route adapter test index that maps each in-scope route to fixture path, capture status, and replay test status.
>    - Add SSE compatibility fixtures for stable event names and terminal/error behavior.
>    - Add UI event contract documentation that distinguishes browser `UIEvent`s from persisted `HarnessEvent`s.
>
> 7. Run verification.
>    - Run the relevant route/SSE tests.
>    - Run mapper/conformance tests that prove SDK-specific names do not leak into the public browser contract.
>    - Run broader validation only when this deliverable is integrated into the package-level or release-level check sequence.
>

### CLM-018 — Verification

> ##### Verification
>
> | Check | Expected Result | Source |
> |---|---|---|
> | Route inventory complete | In-scope `/api/harness/*` routes from SPEC/PRD are represented in docs or fixtures. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1 |
> | SSE event names stable | Fixtures include the stable event-name set or document why a path cannot emit a given event. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |
> | Turn route is an adapter | `/api/harness/turn` delegates runtime lifecycle policy behind `TurnEngine`; route remains transport/SSE boundary. | `docs/SPEC.md` Section 10.4 |
> | UI/runtime separation preserved | Browser `UIEvent` payloads remain compact and distinct from persisted `HarnessEvent` records. | `docs/CONTRACT.md` K-EVENT-1; `docs/PRD.md` FR-074 |
> | Authority-corpus state preserved | Traceability records REF-006 under the current D-APP-38 corpus and unsupported payload/schema details remain `TBD`. | `_REFERENCES.md`; D-APP-38 |
>

### CLM-019 — Route Adapter Test Index Template

> ##### Route Adapter Test Index Template
>
> Populate this table when implementation fixtures are captured. Until then, fixture paths, baseline SHA, and exact payload/schema assertions remain `TBD`.
>
> | Route | Method | Fixture Path | Baseline SHA | Capture Status | Replay Test Status |
> |---|---|---|---|---|---|
> | `/api/harness/session/create` | POST | TBD | TBD | TBD | TBD |
> | `/api/harness/session/boot` | POST | TBD | TBD | TBD | TBD |
> | `/api/harness/session/list` | GET | TBD | TBD | TBD | TBD |
> | `/api/harness/session/[id]` | GET/DELETE | TBD | TBD | TBD | TBD |
> | `/api/harness/turn` | POST | TBD | TBD | TBD | TBD |
> | `/api/harness/interrupt` | POST | TBD | TBD | TBD | TBD |
> | `/api/harness/scaffold` | POST | TBD | TBD | TBD | TBD |
>
> Source: `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1.
>

### CLM-020 — Records

> ##### Records
>
> Expected records and artifacts:
>
> - Route adapter tests.
> - SSE compatibility fixtures.
> - UI event contract docs.
> - Fixture capture notes identifying source commit or implementation baseline. Baseline source SHA is TBD and blocks exact compatibility closure until populated.
> - Route adapter test index mapping each in-scope route to preserved shape fixtures, capture status, replay test status, and unresolved `TBD` fields.
> - SSE stream fixture notes naming successful turn, error, and disconnect/cancel capture paths where current implementation permits; path availability is TBD until captured.
> - Compatibility decision notes for retained compatibility-only fields that constrain internal API shape.
> - Traceability notes mapping requirements to `_CONTEXT.md`, decomposition DEL-03-03, SPEC Sections 10/11/17.1, TYPES Section 7.4, CONTRACT K-EVENT-1, DIRECTIVE Sections 2.8/2.10, and PRD sections with hash warning.

- **VER-001** — Review the preserved legacy requirements and execute the specified route adapter, SSE compatibility, stream integration, mapper/contract, and artifact checks, retaining TBD where fixture capture or baseline evidence remains unresolved.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-03-03 Harness API and SSE Compatibility Adapter

> #### Guidance: DEL-03-03 Harness API and SSE Compatibility Adapter
>

### CLM-022 — Purpose

> ##### Purpose
>
> This deliverable protects the browser-facing harness contract while internal runtime ownership changes. The route adapter should let `/api/harness/*` and named SSE events remain stable for the UI while `TurnEngine`, `AgentEnginePort`, SDK message mapping, and persisted `HarnessEvent` records take over runtime responsibilities behind the boundary.
>
> Sources: `_CONTEXT.md` Deliverable Scope; `docs/SPEC.md` Sections 10.4, 11, 17.1; `docs/PRD.md` Sections 8.12 and 9.3.
>

### CLM-023 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Preserve the browser contract | Treat existing `/api/harness/*` route shapes and named SSE events as compatibility surfaces. Do not rename stable SSE events during the runtime pivot. | `docs/SPEC.md` Sections 11 and 17.1 |
> | Keep route and runtime ownership separate | `/api/harness/turn` should validate, lock, encode SSE, forward to `TurnEngine`, and handle cleanup; it should not own runtime policy. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` Section 8.12 FR-071 |
> | Keep SDK details behind adapters | SDK message names, session IDs, transcript paths, permission modes, and tool names are adapter metadata, not public Chirality UI contracts. | `docs/SPEC.md` Section 10.3; `docs/DIRECTIVE.md` Section 2.10 |
> | Treat UI and audit records differently | Browser `UIEvent`s should stay compact and compatible; persisted `HarnessEvent`s can be richer, versioned, and audit-oriented. | `docs/CONTRACT.md` Section 1.5 K-EVENT-1 |
> | Verify compatibility with fixtures | Prefer captured route/SSE fixtures and replay tests over prose-only review. Exact existing payload fixtures are TBD. | `docs/PRD.md` Sections 12.5 and 12.6 |
>

### CLM-024 — Considerations

> ##### Considerations
>
> - `docs/PRD.md` is a current D-APP-38 authority-corpus source for the runtime pivot; keep PRD-derived details traceable and avoid treating unsupported details as implementation proof.
> - The stable event-name list is source-backed across SPEC, TYPES, and PRD: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, and the additive redacted `harness:event` bridge.
> - Compatibility should be tested from the browser-facing side: route shapes, status codes, SSE names, payload fields, and terminal/error behavior observable by existing UI consumers.
> - New internal `HarnessEvent` categories or SDK metadata should not force UI payload churn unless an explicit compatibility layer is documented and tested.
> - Some behavior belongs to sibling deliverables: active-turn locking and `TurnEngine` internals primarily belong to DEL-03-02; interrupt/cancel cleanup and terminal outcome persistence primarily belong to DEL-03-04 and PKG-05.
>

### CLM-025 — Trade-offs

> ##### Trade-offs
>
> | Choice | Benefit | Risk / Mitigation |
> |---|---|---|
> | Preserve route/SSE compatibility while refactoring internals | Reduces UI breakage during SDK adoption. | May constrain ideal internal API shape; mitigate by keeping compatibility adapters thin and source-backed. |
> | Keep `UIEvent` compact and separate from `HarnessEvent` | Lets runtime audit expand without browser churn. | Requires mapper discipline; mitigate with tests that reject SDK-shaped public leakage. |
> | Capture exact current route fixtures before implementation changes | Makes compatibility measurable. | Fixture capture can ossify accidental behavior; mitigate by documenting which fields are contractual and which are compatibility-only TBD. |
> | Allow additional tool progress events only with compatibility handling | Enables future richer UI feedback. | Could surprise older clients; mitigate through opt-in handling or backward-compatible event consumption. |
>
> Compatibility handling for additional tool progress events should name one accepted mode per event: ignored safely by existing clients, consumed only by opt-in UI behavior, or carried through a documented backward-compatible path. Source basis: `docs/PRD.md` Section 9.3 and `docs/PLAN.md` R2 acceptance context.
>
> Classify captured fixture fields before treating them as contract:
>
> | Field Class | Criteria | Evidence |
> |---|---|---|
> | Contractual | Named by SPEC, TYPES, CONTRACT, or PRD as part of the public route, SSE, `UIEvent`, or product-owned `HarnessEvent` contract. | Source section plus fixture assertion. |
> | Compatibility-only | Present in captured current behavior but not source-backed as a required public contract. | Fixture path, implementation baseline SHA, and rationale for retaining or ignoring. |
> | Adapter metadata | Provider/SDK identifiers, message names, transcript paths, session IDs, permission modes, or tool names that may appear only behind adapter boundaries. | DIRECTIVE Section 2.10; PRD Section 9.3; CONTRACT K-ENGINE-4. |
> | TBD | Field cannot yet be classified because current implementation capture or source location is unavailable. | `TBD` with required source or fixture capture action. |
>
> When a retained compatibility-only field constrains a cleaner internal API, add a decision note naming the field, source fixture, affected route/event, accepted risk, and why retaining it does not make the public contract SDK-shaped.
>

### CLM-026 — Examples

> ##### Examples
>
> Source-backed examples:
>
> - A turn stream uses named SSE events from `docs/SPEC.md` Section 11 and `docs/TYPES.md` Section 7.4.
> - `/api/harness/turn` remains the transport adapter while `TurnEngine.runTurn()` owns runtime lifecycle behind the route, per `docs/SPEC.md` Section 10.4 and `docs/PRD.md` Section 8.12.
>
> TBD examples:
>
> - Exact JSON payload examples for each SSE event are TBD pending current implementation fixture capture.
> - Exact request/response schemas for each `/api/harness/*` route are TBD pending current implementation fixture capture.
>

### CLM-027 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | CONFLICT-001 | Resolved by D-APP-38: REF-006 now matches the authority corpus. | `_REFERENCES.md` REF-006 | `docs/PRD.md` Sections 8.3, 8.12, 9.1, 9.3 | All PRD-derived requirements and verification notes | Apply D-APP-38 corpus workflow for future authority edits; do not invent unsupported payload/schema details. | Ruled 2026-06-20 |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-011 SOW-040 OBJ-001 OBJ-002 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
