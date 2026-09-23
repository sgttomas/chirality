---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-02
package_id: PKG-03
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-009, SOW-010, SOW-011, SOW-038, SOW-083]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-03-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-03-02` in service of project scope [SOW-009, SOW-010, SOW-011, SOW-038, SOW-083] and package objectives [OBJ-002].

- **OUT-001** — App-client request binding and Runtime lifecycle/locking conformance for DEL-03-02 that fulfills SOW-009, SOW-010, SOW-011, SOW-038, and SOW-083 in support of OBJ-002.

## SCA-APP-010 Gate-5 Current Contract (Controlling)

The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied
2026-09-04 at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged
as `7795b0972cac147869607d994173753e4a2fc232`; active pointer moved as
`311a2f0b811d55315d6eb623130cad0be1417565`) makes the centre dialogue the
invariant primary surface and seats the prompted specification ladder. Where any
earlier current-contract section or older clause in this document disagrees with
the applied row below, this section controls. Earlier sections, clauses, and
evidence remain dated compatibility history and are not deleted.

### Current responsibility

App HTTP and Desktop surfaces are clients of the application-owned Runtime service. They bind registered project identity/root, role, permission and delegation policy, and runtime options; Runtime owns the session lifecycle and the one-active-turn invariant. The App must not construct a second runtime.

The delegation-policy purpose survives, while the retired Root DEL-02-11 storage owner does not. D-APP-127 retires the former Root owner; it does not settle the replacement storage or interface allocation for the surviving policy. Binding/default behavior and that ownership follow-through remain open rather than being inferred from the existence of an App thread index or upstream agent configuration.

Verification hooks: `frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts` and `projects/chirality-runtime/tests/turn-hardening.test.ts`.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

### Current acceptance obligations

1. App HTTP and Desktop surfaces remain clients of the application-owned Runtime service; Runtime owns session execution state and the active-turn invariant.
2. Boot and session-creation requests bind registered project identity/root, role, mode, delegation policy and options; the boot fingerprint reflects the real inputs.
3. The accepted delegation policy defaults to `none`, narrows managed delegation only, and adds no delegation class. The retired Root DEL-02-11 is no longer an acceptance dependency. Replacement storage/interface ownership and verification of the surviving policy obligation remain explicit residuals; this clause assigns no new storage field.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

### Seating and rulings

Remaining items seated under D-APP-108 (2026-09-04): DEL-03-02-V3-01. Ruled
questions applied here: none beyond SR-24. Alignment writes WI-021, WI-022,
WI-023, WI-024, WI-025 performed in run `APP_SCA_APP_010_SEATING_2026-09-04`;
dependency writes DEP-009, DEP-010 were performed under D-APP-109/D-APP-110 on 2026-09-05; consult Dependencies.csv. No lifecycle, Checking Approval SHA,
dependency-acceptance, product, or release act is implied.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-03-02 Thin TurnEngine and Session Locking

> #### Datasheet: DEL-03-02 Thin TurnEngine and Session Locking
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-03-02 |
> | Deliverable Name | Thin TurnEngine and Session Locking |
> | Package | PKG-03 Runtime Engine Contract and Turn Lifecycle |
> | Decomposition Variant | SOFTWARE_DECOMP v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | Context Envelope | M |
> | Responsible Party | TBD |
> | Primary Objective | OBJ-002 - establish product-owned runtime contracts and thin route boundaries before SDK behavior becomes production default |
> | Scope Items | SOW-009, SOW-010, SOW-011, SOW-038, SOW-083 |
>
> Source: `_CONTEXT.md` Identity and Traceability; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-03-02 row and OBJ-002 row.
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Runtime owner | The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn. | `docs/TYPES.md` Section 7.1; `docs/PRD.md` FR-070 |
> | Engine boundary | `AgentEnginePort` / `RuntimeEngineContract` is separate from SDK APIs. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-ENGINE-1 |
> | Target adapter type | The current SPEC §10.2 AgentEnginePort includes descriptor, preflight, turn execution and required interrupt; lifecycle remains Runtime-owned. | `docs/SPEC.md` Section 10.2; D-APP-40 |
> | Turn input content | Active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable. | `docs/SPEC.md` Section 10.2 |
> | HTTP route role | The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn. | `docs/SPEC.md` Section 10.4 |
> | Session locking | Only one active turn may run per session; concurrent turn attempts return `TURN_IN_PROGRESS`. | `docs/PRD.md` FR-018 |
> | Browser stream contract | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` Section 11; `docs/PRD.md` FR-017, FR-071 |
> | Accepted-turn persistence | Accepted user input persists before current Codex turn execution; retained provider/SDK ordering fixtures are compatibility evidence. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` FR-021 |
> | Terminal outcomes | Success, failure, cancellation, and explicit user interruption persist as terminal runtime events; explicit user interruption uses `turn.interrupted`. | `docs/CONTRACT.md` K-EVENT-3; `docs/PRD.md` FR-022; D-APP-40 |
> | SDK isolation | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-CORE-1, K-ENGINE-4 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Source state status | `docs/PRD.md` was reconciled in an earlier D-APP-38 snapshot; consult current `_REFERENCES.md` observations and the accepted corpus separately. | `_REFERENCES.md` REF-006; D-APP-38 |
> | Route compatibility constraint | Existing `/api/harness/*` route shapes remain stable during SDK adoption and TurnEngine extraction. | `docs/SPEC.md` Section 17.1 |
> | Event separation constraint | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts. | `docs/SPEC.md` Sections 9 and 11; `docs/CONTRACT.md` K-EVENT-1 |
> | Session storage context | Runtime owns the canonical session record and native Codex thread linkage. Historical records remain readable; automatic v2 import or continuation is not a release prerequisite (D-GOV-43 item 5). | `docs/SPEC.md` Sections 8.1 and 8.2 |
> | Settings isolation context | Codex shares the user configuration/resources by reference while keeping Chirality authentication private. The user selects approval/sandbox policy; retired SDK settingSources isolation is compatibility history. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
> | Implementation sequencing | Current App-client binding and Runtime conformance follow D-GOV-43/D-APP-127 and the surviving per-chat delegation task, not the retired R1 SDK extraction sequence. | `docs/PLAN.md` R1; `docs/PRD.md` R1 |
>

### CLM-005 — Runtime lifecycle and App transport boundary

The App delegates execution to its application-owned Runtime service. Runtime owns turn admission and the one-active-turn-per-session invariant, releases active-turn ownership after a terminal outcome, and preserves accepted input and terminal evidence. HTTP and Desktop surfaces validate and transport requests and stream results; they do not create an independent runtime or acquire an App-local substitute lock.

Requests bind registered project identity/root, role, permission and delegation policy, runtime options, content and attachment references. Interrupt and cancellation handling remains coordinated with DEL-03-04. A renderer disconnect unsubscribes from the stream and must not interrupt the running turn. Public event handling preserves Codex notifications under the accepted protocol rather than promising the former closed SDK event vocabulary.

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. Binding and delegation-policy findings retain their gates in this Scope of Work and TM-APP-045; the wording does not certify them complete.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

### CLM-006 — References

> ##### References
>
> | RefID | Source | Sections Used | Status |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | 2.8-2.10 | Current observation: see _REFERENCES.md |
> | REF-002 | `docs/CONTRACT.md` | 1.4-1.5 | Current observation: see _REFERENCES.md |
> | REF-003 | `docs/SPEC.md` | 8-12, 17.1, 19.2-19.3 | Current observation: see _REFERENCES.md |
> | REF-004 | `docs/TYPES.md` | 7.1-7.4 | Current observation: see _REFERENCES.md |
> | REF-005 | `docs/PLAN.md` | R1 | Current observation: see _REFERENCES.md |
> | REF-006 | `docs/PRD.md` | FR-014-FR-022, FR-070-FR-077, FR-116, FR-122-FR-128, R1, validation additions | Current observation: see _REFERENCES.md |
> | REF-007 | `workflows/software-decomp/WORKFLOW.md` | Not directly used for implementation requirements in this draft. | Current observation: see _REFERENCES.md |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-03-02 Thin TurnEngine and Session Locking

> #### Specification: DEL-03-02 Thin TurnEngine and Session Locking
>

### CLM-008 — Scope

The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn.

Bind project/session identity, selected role and policy, resolved options, content and attachment references at the App client boundary. Per-chat delegation policy binding remains DEL-03-02-V3-01 with DEL-08-04; replacement storage/interface ownership must be established before that implementation. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | DEL-03-02-REQ-001 | Implement a `TurnEngine` or equivalent runtime service that owns harness turn lifecycle and can be unit-tested without HTTP. | `docs/PRD.md` FR-070; `docs/TYPES.md` Section 7.1 | Unit test `TurnEngine.runTurn()` without route invocation. |
> | DEL-03-02-REQ-002 | Invoke execution through the current Runtime-owned AgentEnginePort. Preserve full stock Codex protocol and map surviving correctness obligations to current conformance checks. | `docs/SPEC.md` Sections 10.1-10.3; `docs/CONTRACT.md` K-ENGINE-1, K-ENGINE-4; D-APP-56 R4-P24 | Engine boundary/conformance tests reject SDK-shaped public event/session/API leakage. |
> | DEL-03-02-REQ-003 | The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` FR-071 | Route integration test proves stable route behavior while lifecycle executes through `TurnEngine`. |
> | DEL-03-02-REQ-004 | Enforce one active turn per session; concurrent turn attempts for the same session return `TURN_IN_PROGRESS`. | `docs/PRD.md` FR-018; decomposition SOW-011 | Lock concurrency test covers duplicate active-turn request. |
> | DEL-03-02-REQ-005 | Release active-turn ownership after the turn terminates on completion, failure, cancellation or interrupt. Route abort only unsubscribes and MUST NOT release the running turn or interrupt it. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` FR-019, FR-022; `docs/CONTRACT.md` K-EVENT-3 | Current Runtime terminal tests cover completion, failure, cancellation and interrupt; disconnect tests prove retained turn ownership and reattachment. |
> | DEL-03-02-REQ-006 | Bind turn input to active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable. | `docs/SPEC.md` Section 10.2; `docs/PRD.md` FR-015-FR-016 | Session lifecycle tests assert `TurnInput` construction and option forwarding. |
> | DEL-03-02-REQ-007 | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` Section 11 and 17.1; `docs/PRD.md` FR-017, FR-071 | Route/SSE compatibility fixtures verify event names and stream media type. |
> | DEL-03-02-REQ-008 | Runtime SHALL persist accepted input before model execution and coordinate durable terminal outcomes; upstream terminals are mapped before coordinator persistence. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` FR-021; D-APP-56 R4-P24 | Unit/integration test asserts event write precedes engine adapter invocation and the Runtime coordinator persists terminal outcomes. |
> | DEL-03-02-REQ-009 | Persist durable terminal outcome events for success, failure, cancellation, and explicit user interruption; explicit user interruption uses `turn.interrupted` per D-APP-40. | `docs/CONTRACT.md` K-EVENT-3; `docs/PRD.md` FR-022; D-APP-40 | Tests assert one terminal outcome for each accepted turn path. |
> | DEL-03-02-REQ-010 | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` Sections 9, 10.3, 11; `docs/CONTRACT.md` K-EVENT-1 | Event schema and mapper tests verify separation. |
> | DEL-03-02-REQ-011 | Preserve legacy session readability while this slice interacts with active sessions. | `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077 | Session lifecycle tests include legacy-readable session metadata where current code supports it. |
> | DEL-03-02-REQ-012 | Do not enable new user-visible local tool capability as part of this slice. | `docs/PLAN.md` R1 Acceptance; `docs/PRD.md` R1 Acceptance | Regression check confirms no new write/bash/subagent/domain capability is exposed by route refactor. |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / Contract Surface | Applicability |
> |---|---|
> | `docs/SPEC.md` Section 8 | Session metadata and canonicalization context for active session binding. |
> | `docs/SPEC.md` Section 9 | `HarnessEvent` shape and append-only event semantics relevant to accepted-turn and terminal event persistence. |
> | `docs/SPEC.md` Section 10 | Runtime engine contract, target type, adapter rules, and thin route rule. |
> | `docs/SPEC.md` Section 11 | Browser SSE event names and compatibility rule. |
> | `docs/SPEC.md` Section 17.1 | Harness API route shape stability. |
> | `docs/CONTRACT.md` K-CORE, K-ENGINE, K-EVENT | Product-owned runtime semantics, SDK isolation, accepted-turn persistence, terminal outcomes, and UI/runtime event separation. |
> | `docs/TYPES.md` Section 7 | Canonical vocabulary for `TurnEngine`, `AgentEnginePort`, `UIEvent`, `HarnessEvent`, session IDs, and SDK metadata. |
> | `docs/PRD.md` | Product requirements accepted under the current D-APP-38 authority corpus. |
>

### CLM-011 — Verification

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

Required checks cover one-active-turn rejection, release at each terminal, accepted-input ordering, terminal persistence, request/session binding and extensible events. Disconnect/reconnect must preserve the running turn. Delegation-policy default, supported values and request/fingerprint binding remain distinct missing checks under V3-01; current source and policy ownership must be bound first.

### CLM-012 — Documentation

Required artifacts are App-client binding evidence, Runtime lifecycle/lock and session tests, and a source-bound request/terminal verification matrix. `projects/chirality-runtime/packages/core/src/turn-coordinator.ts` and `packages/daemon/src/turn-registry.ts` are evidence loci for the Runtime owner; App `frontend/src/app/api/harness/turn/route.ts` is transport. Record residual delegation-policy binding and missing results. Consult reference observations separately from authority acceptance.

- **AC-001** — The DEL-03-02 output satisfies the exact legacy source requirements bound to SOW-009, SOW-010, SOW-011, SOW-038, SOW-083, and OBJ-002 without adding scope or lifecycle meaning.

## Production and Verification Method — Praxeology

### CLM-013 — Procedure: DEL-03-02 Thin TurnEngine and Session Locking

> #### Procedure: DEL-03-02 Thin TurnEngine and Session Locking
>

### CLM-014 — Purpose

Verify current App-client request binding and Runtime-owned lifecycle/locking, including session identity, policy/options, accepted input, durable terminals and disconnect continuity. The per-chat delegation interface/fingerprint obligation remains separately gated with DEL-08-04. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-015 — Prerequisites

Use current SPEC §§10–11, D-GOV-43 and D-APP-127; consult each extracted `Dependencies.csv` edge for its actual status. App routes forward to the Runtime service; they do not use an App-local session manager or lock. Current verification hooks are listed in CLM-011. Per-chat delegation storage/interface ownership remains unresolved and is required before V3-01 implementation, alongside DEL-08-04-V3-02.

### CLM-016 — Steps

1. Bind the App request and Runtime service source identities.
2. Trace session/project, role, selected policy, options, content and attachment references through the client to Runtime.
3. Verify admission rejects a second concurrent turn and persists accepted input before engine execution.
4. Verify each terminal outcome is durable and releases ownership, while a route disconnect only unsubscribes.
5. Verify complete upstream event preservation and native resume without replaying the prompt.
6. Resolve the owning current delegation interface with DEL-08-04; bind the selected per-chat policy and its fingerprint, then test default and supported values.
7. Record source-bound results, incomplete cases and actual remaining gates.

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-017 — Verification

The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn.

Verify session identity/options/policy forwarding, accepted-input-before-execution, concurrent rejection, durable terminal outcomes, subsequent-turn admission, detach/reattach continuity and event preservation. Keep delegation-policy binding tests open until their current interface is established. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-018 — Records

Preserve App/Runtime source identities, each request/locking/persistence check and result, the actual `Dependencies.csv` state, reference-currentness observations, and unresolved delegation binding. No old blanket PENDING claim is made. Preserve source conversion/claim-map evidence separately; locate it before relying on VER-001.

- **VER-001** — Validate the candidate schema, complete source-marker disposition, claim mapping, parity, and the legacy verification methods preserved in this candidate.

## Governing Values and Decisions — Axiology

### CLM-019 — Guidance: DEL-03-02 Thin TurnEngine and Session Locking

> #### Guidance: DEL-03-02 Thin TurnEngine and Session Locking
>

### CLM-020 — Purpose

The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn. App scope is client binding and conformance evidence. Runtime lifecycle ownership and the per-chat request policy remain explicit. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-021 — Principles

The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn.

Persist accepted input before execution; bind session identity and user-selected policy; preserve complete upstream events. No runtime logs or policy label grant normative authority. Keep this record repair within existing scope and route delegation-binding implementation through its owning task. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-022 — Considerations

The active-turn guard is Runtime-owned and observable through current turn state; `TurnRegistry` and the Runtime coordinator replace the old App-local Set as evidence loci. Boot/session identity and the per-chat delegation request must remain consistent; V3-01 still requires the current storage/interface owner and fingerprint test. Historical sessions remain readable, while native thread resume is the current continuation path. Source-state observations do not refresh accepted corpus pins.

### CLM-023 — Trade-offs

Prefer the Runtime-owned lifecycle behind thin App transport. Release at the turn terminal and unsubscribe on route abort, preserving active work. Preserve complete Codex events and secret protection together. Coordinate terminal taxonomy with DEL-03-04 and delegation-binding ownership with DEL-08-04; this slice does not authorize new capability.

### CLM-024 — Examples

The App validates and forwards a session-bound turn to Runtime. Runtime admits one turn, persists accepted input, executes through the Codex boundary, and persists the terminal result before releasing ownership. The App streams/replays inspectable events. Closing its stream only unsubscribes; explicit Stop interrupts. Verify the sequence and subsequent-turn admission in CLM-017 checks.

### CLM-025 — Conflict Table (for human ruling)

D-GOV-43 resolves the closed-event and SDK-settings mechanisms in favor of full Codex protocol and user-selected policy. The surviving unresolved task is current per-chat delegation request/storage/fingerprint binding with DEL-08-04, not retired Root DEL-02-11 acceptance. Reference observations and accepted corpus identity retain their separate D-APP-38 controls.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-009 SOW-010 SOW-011 SOW-038 SOW-083 OBJ-002 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

## Retired status detail (2026-09-23)

These clauses preserve operative meaning from the retired App status source. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R032:** Per-chat delegation policy request/default and fingerprint remain required. TM-APP-045 holds the missing App/Runtime durable storage and interface owner assignment after Root DEL-02-11 retirement; V3-01 remains gated.

- **APP-R033:** Bind per-chat managed/native delegation selection to durable policy fields and verify the current-path boundary. TM-APP-045 holds the shared storage/interface assignment; no dispatch or acceptance follows from deferral.
