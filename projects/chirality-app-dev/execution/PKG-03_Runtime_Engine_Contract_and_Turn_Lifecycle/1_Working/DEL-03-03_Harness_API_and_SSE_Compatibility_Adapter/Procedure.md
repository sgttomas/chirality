# Procedure: DEL-03-03 Harness API and SSE Compatibility Adapter

## Purpose

Define the working procedure for producing and validating the harness API and SSE compatibility adapter artifacts for DEL-03-03. The procedure is oriented to artifact production and compatibility verification, not to implementing the full `TurnEngine` or SDK adapter internals.

Sources: `_CONTEXT.md` Anticipated Artifacts; `docs/SPEC.md` Sections 10.4, 11, 17.1; `docs/PRD.md` Sections 12.5 and 12.6.

## Prerequisites

| Prerequisite | Status / Notes | Source |
|---|---|---|
| Accepted deliverable scope | Available in `_CONTEXT.md`; ResponsibleParty remains TBD. | `_CONTEXT.md` |
| Authoritative route/event source slices | Available from SPEC, TYPES, CONTRACT, DIRECTIVE, PLAN, and PRD with PRD hash warning. | `_REFERENCES.md` |
| Current implementation fixture capture | BLOCKING for exact route payload, SSE payload, event-order, and compatibility-only field assertions. Baseline source SHA and fixture paths remain TBD. | `docs/PRD.md` Sections 12.5 and 12.6; `docs/PLAN.md` R1 acceptance |
| Upstream dependencies | TBD; no accepted dependency edges extracted yet. | `_DEPENDENCIES.md` |
| Sibling deliverable boundaries | DEL-03-02 owns thin `TurnEngine` and session locking; DEL-03-04 owns interrupt/cancel terminal handling. | Decomposition PKG-03 table |

## Steps

1. Confirm source state.
   - Read `_REFERENCES.md` and record that `docs/PRD.md` is current under the D-APP-38 authority corpus.
   - Use PRD-derived details with traceability and keep unsupported details as `TBD`.

2. Build the compatibility inventory.
   - List `/api/harness/*` routes from `docs/SPEC.md` Section 17.1 and `docs/PRD.md` Section 9.1.
   - List stable SSE event names from `docs/SPEC.md` Section 11, `docs/TYPES.md` Section 7.4, and `docs/PRD.md` Section 9.3.

3. Capture current behavior fixtures.
   - Record the implementation baseline commit/SHA before capture; if unavailable, record `TBD` and do not close exact compatibility assertions.
   - Capture route request/response schemas for the in-scope `/api/harness/*` routes.
   - Capture representative SSE streams for successful turn, error, and disconnect/cancel paths where current implementation permits.
   - Record which implementation paths can emit successful turn, error, and disconnect/cancel streams; unresolved path availability remains `TBD`.
   - Mark any unavailable payload details as `TBD` rather than filling from assumption.

4. Implement or review the route adapter boundary.
   - Keep `/api/harness/turn` responsible for request validation, session locking, attachment option forwarding where applicable, SSE encoding, cancellation cleanup, and error response handling.
   - Delegate runtime lifecycle behavior to `TurnEngine` or the agreed service boundary.
   - Reject SDK message names as browser event names.

5. Implement or review UI event mapping.
   - Ensure SDK or engine messages map to compact browser `UIEvent`s and richer persisted `HarnessEvent`s through an adapter/mapper boundary.
   - Confirm public browser events remain compatible with the stable names.

6. Add compatibility tests and docs.
   - Add route adapter tests for preserved route shapes.
   - Create a route adapter test index that maps each in-scope route to fixture path, capture status, and replay test status.
   - Add SSE compatibility fixtures for stable event names and terminal/error behavior.
   - Add UI event contract documentation that distinguishes browser `UIEvent`s from persisted `HarnessEvent`s.

7. Run verification.
   - Run the relevant route/SSE tests.
   - Run mapper/conformance tests that prove SDK-specific names do not leak into the public browser contract.
   - Run broader validation only when this deliverable is integrated into the package-level or release-level check sequence.

## Verification

| Check | Expected Result | Source |
|---|---|---|
| Route inventory complete | In-scope `/api/harness/*` routes from SPEC/PRD are represented in docs or fixtures. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1 |
| SSE event names stable | Fixtures include the stable event-name set or document why a path cannot emit a given event. | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |
| Turn route is an adapter | `/api/harness/turn` delegates runtime lifecycle policy behind `TurnEngine`; route remains transport/SSE boundary. | `docs/SPEC.md` Section 10.4 |
| UI/runtime separation preserved | Browser `UIEvent` payloads remain compact and distinct from persisted `HarnessEvent` records. | `docs/CONTRACT.md` K-EVENT-1; `docs/PRD.md` FR-074 |
| Authority-corpus state preserved | Traceability records REF-006 under the current D-APP-38 corpus and unsupported payload/schema details remain `TBD`. | `_REFERENCES.md`; D-APP-38 |

## Route Adapter Test Index Template

Populate this table when implementation fixtures are captured. Until then, fixture paths, baseline SHA, and exact payload/schema assertions remain `TBD`.

| Route | Method | Fixture Path | Baseline SHA | Capture Status | Replay Test Status |
|---|---|---|---|---|---|
| `/api/harness/session/create` | POST | TBD | TBD | TBD | TBD |
| `/api/harness/session/boot` | POST | TBD | TBD | TBD | TBD |
| `/api/harness/session/list` | GET | TBD | TBD | TBD | TBD |
| `/api/harness/session/[id]` | GET/DELETE | TBD | TBD | TBD | TBD |
| `/api/harness/turn` | POST | TBD | TBD | TBD | TBD |
| `/api/harness/interrupt` | POST | TBD | TBD | TBD | TBD |
| `/api/harness/scaffold` | POST | TBD | TBD | TBD | TBD |

Source: `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 9.1.

## Records

Expected records and artifacts:

- Route adapter tests.
- SSE compatibility fixtures.
- UI event contract docs.
- Fixture capture notes identifying source commit or implementation baseline. Baseline source SHA is TBD and blocks exact compatibility closure until populated.
- Route adapter test index mapping each in-scope route to preserved shape fixtures, capture status, replay test status, and unresolved `TBD` fields.
- SSE stream fixture notes naming successful turn, error, and disconnect/cancel capture paths where current implementation permits; path availability is TBD until captured.
- Compatibility decision notes for retained compatibility-only fields that constrain internal API shape.
- Traceability notes mapping requirements to `_CONTEXT.md`, decomposition DEL-03-03, SPEC Sections 10/11/17.1, TYPES Section 7.4, CONTRACT K-EVENT-1, DIRECTIVE Sections 2.8/2.10, and PRD sections with hash warning.
