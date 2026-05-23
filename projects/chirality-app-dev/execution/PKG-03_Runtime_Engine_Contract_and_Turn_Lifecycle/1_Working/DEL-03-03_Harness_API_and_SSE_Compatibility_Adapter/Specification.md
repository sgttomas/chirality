# Specification: DEL-03-03 Harness API and SSE Compatibility Adapter

## Scope

This deliverable specifies the compatibility adapter contract for harness API routes and browser-facing SSE events during the runtime-engine pivot. It covers:

- preserving `/api/harness/*` route shapes during SDK adoption and `TurnEngine` extraction;
- keeping `/api/harness/turn` as the SSE transport adapter rather than the owner of runtime policy;
- preserving browser SSE event names and compact `UIEvent` semantics;
- separating browser `UIEvent`s from persisted `HarnessEvent`s;
- defining route adapter tests, SSE compatibility fixtures, and UI event contract documentation.

Source: `_CONTEXT.md` Deliverable Scope; `docs/SPEC.md` Sections 10.4, 11, 17.1; `docs/PRD.md` Sections 8.12, 9.1, 9.3.

Out of scope:

- SDK-specific message translation internals except where they must not leak into the browser contract.
- `TurnEngine` lifecycle ownership and session locking internals, owned primarily by DEL-03-02.
- interrupt/cancel terminal outcome handling, owned primarily by DEL-03-04.
- persisted event schema implementation, owned primarily by PKG-05, except for compatibility assertions that UI and runtime event contracts remain separate.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| DEL-03-03-REQ-001 | The adapter shall preserve the existing `/api/harness/*` route shapes during SDK adoption and `TurnEngine` extraction. Exact existing request/response schemas are TBD pending implementation fixture capture. | Route adapter regression tests compare current and post-extraction route shape fixtures. |
| DEL-03-03-REQ-002 | `/api/harness/turn` shall remain a transport adapter responsible for request validation, session locking, attachment option forwarding where applicable, SSE encoding, cancellation cleanup, and error response handling. | Route tests and code review verify policy behavior is delegated to `TurnEngine`/services. |
| DEL-03-03-REQ-003 | Browser-facing turn streams shall emit compatible named SSE events: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, and `process:exit`. | SSE compatibility fixtures assert event names and order constraints where source-backed. |
| DEL-03-03-REQ-004 | The SSE stream shall terminate with a process-level completion/error signal unless the client disconnects and cancel cleanup runs. | Stream integration test covers normal completion, error, and disconnect cases. |
| DEL-03-03-REQ-005 | Browser `UIEvent`s and persisted `HarnessEvent`s shall remain separate contracts; persisted events may be richer and versioned, but UI events remain compact and compatible. | Mapper/contract tests reject SDK-shaped leakage into public UI event payloads except explicit adapter metadata where relevant. |
| DEL-03-03-REQ-006 | SDK messages shall not be treated as the browser contract or canonical persisted event contract. | Mapper tests verify SDK message categories map through `sdk-message-mapper.ts` or equivalent boundary. |
| DEL-03-03-REQ-007 | Additional tool progress events may be introduced only with UI compatibility handling. | Compatibility review confirms existing UI consumers handle or ignore added events safely. |
| DEL-03-03-REQ-008 | The compatibility kit shall include route adapter tests, SSE compatibility fixtures, and UI event contract docs. | Artifact review confirms files exist and reference the source-backed route/event contract. |
| DEL-03-03-REQ-009 | PRD-derived requirements shall carry a source-state warning until the REF-006 hash mismatch is resolved. | Documentation and test traceability mark PRD sections as HASH_MISMATCH source-state-warning input. |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Product-owned runtime contract | Adapter behavior must serve Chirality-owned `AgentEnginePort`/`RuntimeEngineContract`, not SDK public semantics. | `docs/DIRECTIVE.md` Sections 2.8 and 2.10; `docs/SPEC.md` Section 10 |
| Browser SSE event contract | Required event names and stream termination behavior. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4; `docs/PRD.md` Section 9.3 |
| Harness API route contract | `/api/harness/*` route catalog and stability expectation. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1 |
| Runtime/audit event separation | Browser `UIEvent` and persisted `HarnessEvent` are distinct contracts. | `docs/CONTRACT.md` Section 1.5; `docs/PRD.md` Section 8.12 |
| Test/validation expectations | Route stream unchanged after SDK-backed `TurnEngine` extraction; SDK message mapper coverage. | `docs/PRD.md` Sections 12.5 and 12.6 |

## Verification

| Verification Item | Method | Source Basis |
|---|---|---|
| Route shape compatibility | Capture current route request/response/SSE fixtures, then replay against the adapter after extraction. Exact schema capture remains TBD. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1 |
| SSE event-name compatibility | Assert emitted event names include the documented stable set and preserve existing browser handling. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |
| Turn route delegation | Unit or route test proves `/api/harness/turn` delegates lifecycle execution behind `TurnEngine` and does not own runtime policy. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` Section 8.12 FR-071 |
| UI/runtime separation | Mapper and public API tests reject SDK message names as public UI contracts and keep persisted event richness behind `HarnessEvent`. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-EVENT-1 |
| Disconnect/terminal behavior hook | Integration tests include normal completion, error, and disconnect paths; detailed terminal persistence belongs to DEL-03-04/PKG-05. | `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3 |
| Source-state warning handling | Review confirms `docs/PRD.md` HASH_MISMATCH is carried in traceability and unsupported details stay `TBD`. | `_REFERENCES.md` REF-006 |

## Documentation

Required documentation artifacts:

- UI event contract docs listing stable SSE event names, payload ownership, and compatibility rules.
- Route adapter test index mapping each `/api/harness/*` route to preserved shape fixtures.
- SSE compatibility fixture README describing fixture capture source, replay method, and expected event sequence.
- Traceability note that PRD-derived requirements use `docs/PRD.md` as a HASH_MISMATCH source-state-warning input until the accepted reference hash is updated or the source is restored.

