# Guidance: DEL-03-03 Harness API and SSE Compatibility Adapter

## Purpose

This deliverable protects the browser-facing harness contract while internal runtime ownership changes. The route adapter should let `/api/harness/*` and named SSE events remain stable for the UI while `TurnEngine`, `AgentEnginePort`, SDK message mapping, and persisted `HarnessEvent` records take over runtime responsibilities behind the boundary.

Sources: `_CONTEXT.md` Deliverable Scope; `docs/SPEC.md` Sections 10.4, 11, 17.1; `docs/PRD.md` Sections 8.12 and 9.3.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Preserve the browser contract | Treat existing `/api/harness/*` route shapes and named SSE events as compatibility surfaces. Do not rename stable SSE events during the runtime pivot. | `docs/SPEC.md` Sections 11 and 17.1 |
| Keep route and runtime ownership separate | `/api/harness/turn` should validate, lock, encode SSE, forward to `TurnEngine`, and handle cleanup; it should not own runtime policy. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` Section 8.12 FR-071 |
| Keep SDK details behind adapters | SDK message names, session IDs, transcript paths, permission modes, and tool names are adapter metadata, not public Chirality UI contracts. | `docs/SPEC.md` Section 10.3; `docs/DIRECTIVE.md` Section 2.10 |
| Treat UI and audit records differently | Browser `UIEvent`s should stay compact and compatible; persisted `HarnessEvent`s can be richer, versioned, and audit-oriented. | `docs/CONTRACT.md` Section 1.5 K-EVENT-1 |
| Verify compatibility with fixtures | Prefer captured route/SSE fixtures and replay tests over prose-only review. Exact existing payload fixtures are TBD. | `docs/PRD.md` Sections 12.5 and 12.6 |

## Considerations

- `docs/PRD.md` is a useful local source for the runtime pivot but is recorded as `HASH_MISMATCH`; keep PRD-derived details traceable and avoid treating unsupported details as immutable accepted truth.
- The stable event-name list is source-backed across SPEC, TYPES, and PRD: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`.
- Compatibility should be tested from the browser-facing side: route shapes, status codes, SSE names, payload fields, and terminal/error behavior observable by existing UI consumers.
- New internal `HarnessEvent` categories or SDK metadata should not force UI payload churn unless an explicit compatibility layer is documented and tested.
- Some behavior belongs to sibling deliverables: active-turn locking and `TurnEngine` internals primarily belong to DEL-03-02; interrupt/cancel cleanup and terminal outcome persistence primarily belong to DEL-03-04 and PKG-05.

## Trade-offs

| Choice | Benefit | Risk / Mitigation |
|---|---|---|
| Preserve route/SSE compatibility while refactoring internals | Reduces UI breakage during SDK adoption. | May constrain ideal internal API shape; mitigate by keeping compatibility adapters thin and source-backed. |
| Keep `UIEvent` compact and separate from `HarnessEvent` | Lets runtime audit expand without browser churn. | Requires mapper discipline; mitigate with tests that reject SDK-shaped public leakage. |
| Capture exact current route fixtures before implementation changes | Makes compatibility measurable. | Fixture capture can ossify accidental behavior; mitigate by documenting which fields are contractual and which are compatibility-only TBD. |
| Allow additional tool progress events only with compatibility handling | Enables future richer UI feedback. | Could surprise older clients; mitigate through opt-in handling or backward-compatible event consumption. |

Compatibility handling for additional tool progress events should name one accepted mode per event: ignored safely by existing clients, consumed only by opt-in UI behavior, or carried through a documented backward-compatible path. Source basis: `docs/PRD.md` Section 9.3 and `docs/PLAN.md` R2 acceptance context.

Classify captured fixture fields before treating them as contract:

| Field Class | Criteria | Evidence |
|---|---|---|
| Contractual | Named by SPEC, TYPES, CONTRACT, or PRD as part of the public route, SSE, `UIEvent`, or product-owned `HarnessEvent` contract. | Source section plus fixture assertion. |
| Compatibility-only | Present in captured current behavior but not source-backed as a required public contract. | Fixture path, implementation baseline SHA, and rationale for retaining or ignoring. |
| Adapter metadata | Provider/SDK identifiers, message names, transcript paths, session IDs, permission modes, or tool names that may appear only behind adapter boundaries. | DIRECTIVE Section 2.10; PRD Section 9.3; CONTRACT K-ENGINE-4. |
| TBD | Field cannot yet be classified because current implementation capture or source location is unavailable. | `TBD` with required source or fixture capture action. |

When a retained compatibility-only field constrains a cleaner internal API, add a decision note naming the field, source fixture, affected route/event, accepted risk, and why retaining it does not make the public contract SDK-shaped.

## Examples

Source-backed examples:

- A turn stream uses named SSE events from `docs/SPEC.md` Section 11 and `docs/TYPES.md` Section 7.4.
- `/api/harness/turn` remains the transport adapter while `TurnEngine.runTurn()` owns runtime lifecycle behind the route, per `docs/SPEC.md` Section 10.4 and `docs/PRD.md` Section 8.12.

TBD examples:

- Exact JSON payload examples for each SSE event are TBD pending current implementation fixture capture.
- Exact request/response schemas for each `/api/harness/*` route are TBD pending current implementation fixture capture.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-001 | `docs/PRD.md` content is accessible but REF-006 records `HASH_MISMATCH`. | `_REFERENCES.md` REF-006 | `docs/PRD.md` Sections 8.3, 8.12, 9.1, 9.3 | All PRD-derived requirements and verification notes | Treat PRD details as source-state-warning context until the reference hash is reconciled; do not invent missing details. | TBD |
