---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-03
package_id: PKG-03
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
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

The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn.

Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it.

Required artifacts remain route-adapter tests, current SSE fixtures and UI-event contract documentation. Fixtures must bind actual route/source identity; none is invented by this repair. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-004 — Conditions

The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn.

Retain route-shape compatibility, one-active-turn rejection and truthful terminal/error presentation. Streams need keepalives and no idle timeout that terminates the turn; detach/reattach must recover missed activity and outstanding decisions. Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. Current reference observations are recorded in `_REFERENCES.md`.

### CLM-005 — Route and stream compatibility

Harness routes must remain thin, validated clients of the App-owned Runtime service. Their compatibility obligation concerns the supported App operations and inspectable outcomes, with live Codex notifications preserved through the full protocol. Compatibility does not require manufacturing every legacy SDK event name or translating away an unknown Codex notification.

The stream must preserve ordering and replay identity, expose failures, and permit detach/reattach without turning a renderer disconnect into a turn interrupt. Runtime owns turn coordination. Route presence alone does not establish operation completeness: the live scaffold route's missing composition remains a P-15 residual, and fake-port tests do not establish a live fixture capture.

Verification hooks: `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`, `frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts`, and `projects/chirality-runtime/tests/daemon.test.ts`. `RouteAdapterTestIndex.md` and the R3 rows preserve missing-fixture evidence separately.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

### CLM-006 — References

> ##### References
>
> | RefID | Source | Source Slice Used | Status |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Sections 2.8, 2.10 | Current observation: see _REFERENCES.md |
> | REF-002 | `docs/CONTRACT.md` | Section 1.5; Enforcement Map Summary | Current observation: see _REFERENCES.md |
> | REF-003 | `docs/SPEC.md` | Sections 10, 11, 17.1 | Current observation: see _REFERENCES.md |
> | REF-004 | `docs/TYPES.md` | Sections 7.1, 7.2, 7.3, 7.4 | Current observation: see _REFERENCES.md |
> | REF-005 | `docs/PLAN.md` | R1 acceptance and route/SSE stability context | Current observation: see _REFERENCES.md |
> | REF-006 | `docs/PRD.md` | Sections 8.3, 8.12, 9.1, 9.3, 12.5, 12.6, R1 roadmap | Current observation: see _REFERENCES.md |
> | REF-007 | `workflows/software-decomp/WORKFLOW.md` | Decomposition method reference only; no deliverable-specific details used | Current observation: see _REFERENCES.md |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-03-03 Harness API and SSE Compatibility Adapter

> #### Specification: DEL-03-03 Harness API and SSE Compatibility Adapter
>

### CLM-008 — Scope

Own the App route/stream boundary and its conformance evidence against the application-owned Runtime service. Preserve supported `/api/harness/*` request/response behavior, current SSE transport, full upstream events, keepalive and detach/reattach continuity. Runtime owns the turn and lock. Exact fixture capture and the scaffold composition gap remain open delivery tasks. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Verification |
> |---|---|---|
> | DEL-03-03-REQ-001 | The adapter shall preserve the existing `/api/harness/*` route shapes during SDK adoption and `TurnEngine` extraction. Exact existing request/response schemas are TBD pending implementation fixture capture. | Route adapter regression tests compare current and post-extraction route shape fixtures. |
> | DEL-03-03-REQ-002 | The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn. | Route tests and code review verify policy behavior is delegated to `TurnEngine`/services. |
> | DEL-03-03-REQ-003 | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | SSE compatibility fixtures assert event names and only source-backed order constraints; unconstrained event paths are recorded as `TBD` or "order unconstrained." |
> | DEL-03-03-REQ-004 | The subscribed stream exposes truthful completion/error state; a disconnected client only unsubscribes and may reattach by sequence. Keepalives and idle behavior MUST NOT interrupt the turn. | Stream integration test covers normal completion, error, and disconnect cases. |
> | DEL-03-03-REQ-005 | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | Mapper/contract tests reject SDK-shaped leakage into public UI event payloads except explicit adapter metadata where relevant. |
> | DEL-03-03-REQ-006 | Normalize known upstream Codex events for display while preserving original method, identity and payload; unfamiliar notifications remain inspectable. Verify live mapping rather than the retired SDK mapper alone. | Mapper tests verify known SDK message categories map through the selected boundary and do not expose SDK-shaped names in public UI events or canonical `HarnessEvent` fields except as adapter metadata. |
> | DEL-03-03-REQ-007 | Additional upstream notifications remain inspectable through generic presentation even when no specialized view exists; no notification is silently ignored or dropped. | Compatibility review confirms existing UI consumers handle or ignore added events safely and records the selected handling mode. |
> | DEL-03-03-REQ-008 | The compatibility kit shall include route adapter tests, SSE compatibility fixtures, and UI event contract docs. | Artifact review confirms files exist and reference the source-backed route/event contract. |
> | DEL-03-03-REQ-009 | PRD-derived requirements shall use the current D-APP-38 authority-corpus reference state. | Documentation and test traceability cite the reconciled REF-006 state and rerun D-APP-38 bump/apply when authority documents change. |
> | DEL-03-03-REQ-010 | The route adapter test index shall map each in-scope `/api/harness/*` route to a fixture path or `TBD` capture status before exact compatibility assertions are closed. | Artifact review confirms every route listed in SPEC Section 17.1 and PRD Section 9.1 appears in the route-to-fixture index. |
>

### CLM-010 — Standards

SPEC §§10–11/17.1 and D-GOV-43/D-APP-127 govern the thin route, Runtime-owned turn and extensible event representation. CONTRACT K-EVENT preserves durability and secret protection. Route tests, SSE fixture replay and live presentation checks establish behavior; a reference-currentness claim or fake-port test alone does not establish live compatibility.

### CLM-011 — Verification

Capture and replay request/response and SSE fixtures against the exact current candidate. Check keepalive, no idle-timeout interruption, disconnect without interrupt, reattachment by sequence, truthful terminal/error presentation, and generic display of unfamiliar notifications. Verify full upstream identity/payload preservation and structural redaction before every sink. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence. Missing live fixture captures and S-2/renderer-disconnect evidence remain open.

### CLM-012 — Documentation

Produce route-adapter tests, current SSE fixture captures, a route-to-fixture index and UI-event contract docs for D-GOV-43. Record source/candidate identity, capture/replay results and unavailable paths. The existing `RouteAdapterTestIndex.md` and `UiEventContract.md` are earlier evidence and require current-subject reissue before reliance; the record repair does not rewrite them.

### CLM-013 — D-APP-56 route ownership map (2026-07-12)

The acceptance subject is supported App operation and stream behavior on the Runtime service path: stable request/response meaning, keepalive, continuity, complete upstream event inspection and separate secret protection. Exact route/SSE fixtures and live results remain required before compatibility closure. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

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

Use the current source basis and extracted `Dependencies.csv`; no unextracted-edge placeholder applies. Bind the actual candidate/source SHA before fixture capture. DEL-03-02 covers Runtime/client binding, DEL-03-04 terminal/interrupt evidence and PKG-05 durability/presentation. Missing exact fixture or native results remain blockers to the corresponding assertions.

### CLM-017 — Steps

1. Record the source/candidate identity and current `/api/harness/*` operation inventory.
2. Capture current request/response and successful/error/detach/reattach streams with fixture hashes.
3. Verify thin forwarding to Runtime and one active turn; the App must not own an independent lock.
4. Check keepalive, absence of idle interruption, replay ordering and recovery of outstanding decisions.
5. Check known-event views and unfamiliar notification inspection with original identity/payload retained and secrets redacted.
6. Update the route-to-fixture index and UI-event docs; identify the still-uncomposed scaffold operation explicitly.
7. Record results, missing captures, source validity and the required current native witness.

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-018 — Verification

Verify every supported route against its source-bound fixture; keep uncaptured cases explicitly open. Check the live event representation, no idle termination, renderer detach/reattach, sequence/order, terminal/error presentation and every secret-protection sink. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

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

Required records are route and current SSE fixtures, baseline/candidate SHA, capture and replay outputs, route-to-fixture index, UI-event contract documentation, and S-2/renderer-disconnect evidence. Distinguish deterministic fake-port results from live results. Record unsupported scaffold composition separately. Existing legacy docs stay historical until reissued for D-GOV-43; exact payload or result gaps remain unknown.

- **VER-001** — Review the preserved legacy requirements and execute the specified route adapter, SSE compatibility, stream integration, mapper/contract, and artifact checks, retaining TBD where fixture capture or baseline evidence remains unresolved.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-03-03 Harness API and SSE Compatibility Adapter

> #### Guidance: DEL-03-03 Harness API and SSE Compatibility Adapter
>

### CLM-022 — Purpose

The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn. Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. Compatibility concerns supported operation meaning and inspectable outcomes, not the retired eight-event ceiling. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-023 — Principles

The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn. Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. Capture fixtures for source-backed assertions; incidental field shape does not silently become an accepted requirement. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-024 — Considerations

Inspect current routes from the browser boundary: request/response meaning, status, stream order, terminal/error behavior and reconnect. Preserve all upstream notifications; normalized views do not replace source data. Runtime turn ownership and terminal persistence stay with DEL-03-02/04 and PKG-05. Source-valid fixture capture and missing redaction verification remain explicit.

### CLM-025 — Trade-offs

Classify fixture fields as source-required, incidental compatibility evidence, upstream source data, or unresolved. Preserve the full Codex protocol, including unfamiliar notifications, while keeping structural redaction. An incidental field does not force new product scope; an adopted operation or continuity guarantee cannot be removed merely because its implementation is absent. Record exact capture identity and any real scope decision separately.

### CLM-026 — Examples

When a renderer disconnects, its subscription ends while Runtime continues the turn. On reattachment, replay by sequence supplies missed events and current state without resending the prompt. A previously unknown Codex notification is available in generic inspection with its upstream method/ID/payload and redacted secrets. Exact request/response fixtures remain an outstanding capture task. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-027 — Conflict Table (for human ruling)

D-GOV-43/D-APP-127 settle the old closed-event and disconnect-cancellation conflicts. Full event preservation and secret protection both survive. Current route/SSE fixture capture, redaction verification and scaffold composition remain delivery tasks; reference observations remain distinct from accepted corpus pins.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-011 SOW-040 OBJ-001 OBJ-002 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

## Retired status detail (2026-09-23)

These clauses preserve operative meaning from the retired App status source. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R034:** The App transport/SSE consumer must preserve complete events, reconnect and unsubscribe behavior and noninterrupting detach semantics on the current Runtime path; record a current-path witness and any gaps.
