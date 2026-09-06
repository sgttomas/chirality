---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-01
package_id: PKG-03
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-037]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-03-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-03-01` in service of project scope [SOW-037] and package objectives [OBJ-002].

- **OUT-001** — A product-owned AgentEnginePort / RuntimeEngineContract, runtime contract documentation, and conformance tests for stub and provider/SDK-backed adapters.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-03-01 AgentEnginePort and Engine Conformance Suite

> #### Datasheet: DEL-03-01 AgentEnginePort and Engine Conformance Suite
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-03-01 |
> | DeliverableName | AgentEnginePort and Engine Conformance Suite |
> | PackageID | PKG-03 |
> | PackageName | Runtime Engine Contract and Turn Lifecycle |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ResponsibleParty | TBD |
> | Type | API_CONTRACT |
> | ContextEnvelope | M |
> | CoversScopeItems | SOW-037 |
> | SupportsObjectives | OBJ-002 |
> | AnticipatedArtifacts | `agent-engine-port.ts`; runtime contract docs; conformance tests |
>
> Source: `_CONTEXT.md` and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` section "PKG-03 Runtime Engine Contract and Turn Lifecycle".
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Contract identity | `AgentEnginePort` / `RuntimeEngineContract` | `docs/SPEC.md` section 10.1; `docs/TYPES.md` section 7.1 |
> | Contract ownership | Chirality owns the runtime contract; SDK APIs do not define public harness semantics. | `docs/DIRECTIVE.md` section 2.8; `docs/CONTRACT.md` K-ENGINE-1 |
> | Adapter role | `EngineAdapter` is provider/SDK-specific implementation behind `AgentEnginePort`. | `docs/TYPES.md` section 7.1; `docs/SPEC.md` section 10.3 |
> | Primary operation | `startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>` | `docs/SPEC.md` section 10.2; D-APP-40 |
> | Optional operation | `interrupt?(sessionId: string): Promise<void>` | `docs/SPEC.md` section 10.2 |
> | Browser stream contract | `UIEvent` stream using stable SSE names. | `docs/SPEC.md` section 11; `docs/TYPES.md` section 7.4 |
> | Canonical runtime record | `HarnessEvent` records in product-owned event JSONL. | `docs/SPEC.md` section 9; `docs/TYPES.md` section 7.3 |
> | Required conformance subject | Stub adapter and SDK-backed adapter. | `docs/SPEC.md` section 10.3; `docs/PRD.md` section 12.5 |
> | Production-default gate | SDK-backed adapter must pass engine conformance before default production use. | `docs/CONTRACT.md` K-ENGINE-2; `docs/PRD.md` FR-123 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Requirement / Constraint | Source |
> |---|---|---|
> | Provider-neutral core | Public APIs, canonical event schemas, session storage contracts, permission decision records, and governance rules must not become SDK-shaped. | `docs/DIRECTIVE.md` section 2.10; `docs/CONTRACT.md` K-ENGINE-4 |
> | Route compatibility | Existing `/api/harness/*` route shapes remain stable during SDK adoption and TurnEngine extraction. | `docs/PRD.md` section 9.1; `docs/SPEC.md` section 10.4 |
> | SSE compatibility | Browser-facing SSE event names remain compatible during SDK adoption. | `docs/SPEC.md` section 11; `docs/PRD.md` section 9.3 |
> | Terminal outcomes | Accepted turns must persist terminal success, failure, cancellation, or interruption outcomes. | `docs/CONTRACT.md` K-EVENT-3; `docs/PRD.md` FR-123 |
> | Accepted-turn persistence | Accepted user input must be persisted before SDK/model execution begins. | `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` section 12.6 |
> | SDK metadata boundary | SDK identifiers, message names, permission modes, tool names, transcript paths, and session IDs are adapter metadata. | `docs/DIRECTIVE.md` section 2.10; `docs/SPEC.md` section 10.3 |
> | Source-state status | `docs/PRD.md` is reconciled under the current D-APP-38 authority corpus; PRD-derived runtime details are accepted for this tranche. | `_REFERENCES.md` REF-006; D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Construct | Target / Shape | Source / Status |
> |---|---|---|
> | Runtime contract module | `agent-engine-port.ts` or equivalent product-owned runtime contract. | `execution/_Decomposition/...v3_2.md` DEL-03-01; `docs/PLAN.md` R1; `docs/PRD.md` R1 |
> | TypeScript interface | `AgentEnginePort` with `startTurn(input: AgentEngineRunInput)` and optional `interrupt`. | `docs/SPEC.md` section 10.2; D-APP-40 |
> | Turn input type | Must include active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable. | `docs/SPEC.md` section 10.2 |
> | Conformance suite | `engine-conformance.ts` or equivalent tests for stub and SDK-backed adapters. | `docs/PLAN.md` R1; `docs/PRD.md` section 12.5 |
> | Stub adapter | Deterministic adapter retained for tests. | `docs/SPEC.md` section 10.3 |
> | SDK-backed adapter | Provider implementation behind the product-owned contract. | `docs/SPEC.md` section 10.3 |
> | Exact final source path | ACCEPTED PLACEMENT (2026-07-03): D-APP-46 extraction accepted `frontend/packages/harness-contract/src/agent-engine-port.ts` as the package-owned source. The original app-dev path `frontend/src/lib/harness/agent-engine-port.ts` remains as a back-compat shim that re-exports `@chirality/harness-contract/agent-engine-port`. | D-APP-46 ruling; `frontend/packages/harness-contract/src/agent-engine-port.ts`; `frontend/src/lib/harness/agent-engine-port.ts` |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Status / Note |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | MATCH; sections 2.8-2.11 used. |
> | REF-002 | `docs/CONTRACT.md` | MATCH; sections 1.4-1.5 and enforcement map used. |
> | REF-003 | `docs/SPEC.md` | MATCH; sections 9-13 used. |
> | REF-004 | `docs/TYPES.md` | MATCH; sections 7 and 12 used. |
> | REF-005 | `docs/PLAN.md` | MATCH; sections 2-4, 6.2, and 8 used. |
> | REF-006 | `docs/PRD.md` | MATCH under the current D-APP-38 authority corpus; sections 8.16, 9, 12, and 13 used. |
> | REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | MATCH; not used for content requirements beyond decomposition provenance. |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-03-01 AgentEnginePort and Engine Conformance Suite

> #### Specification: DEL-03-01 AgentEnginePort and Engine Conformance Suite
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable defines the product-owned runtime boundary for harness turn execution and the conformance suite any engine adapter must satisfy before use as the default production path.
>
> In scope:
>
> - `AgentEnginePort` / `RuntimeEngineContract` API contract.
> - Adapter boundary rules for stub and SDK-backed implementations.
> - Conformance expectations for accepted-turn persistence, terminal outcomes, SSE compatibility, SDK message mapping, permission/tool boundary behavior, interrupt/cancel behavior, session resume/linkage, and redaction.
> - Runtime contract documentation and tests associated with the contract.
>
> Out of scope:
>
> - SDK-specific message translation implementation details, except as conformance inputs and adapter-boundary expectations.
> - Full `TurnEngine` extraction and session locking implementation, owned by DEL-03-02.
> - Browser API/SSE route adapter fixtures, owned by DEL-03-03 except where conformance verifies compatibility.
> - Interrupt/cancel cleanup implementation, owned by DEL-03-04 except where conformance verifies required adapter behavior.
> - SDK probe/version decision details, owned by DEL-04-01.
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-03-01; `docs/SPEC.md` sections 10-12; `docs/PRD.md` sections 8.16, 9, and 12.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-03-01-REQ-001 | Chirality SHALL define `AgentEnginePort` / `RuntimeEngineContract` separate from SDK APIs. | `docs/SPEC.md` section 10.1; `docs/PRD.md` FR-122 |
> | DEL-03-01-REQ-002 | Public harness semantics SHALL remain Chirality-owned; SDK APIs, message names, transcript shape, and tool names SHALL NOT define public semantics. | `docs/DIRECTIVE.md` sections 2.8 and 2.10; `docs/CONTRACT.md` K-ENGINE-1 and K-ENGINE-4 |
> | DEL-03-01-REQ-003 | `AgentEnginePort` SHALL expose `startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>`. | `docs/SPEC.md` section 10.2; D-APP-40 |
> | DEL-03-01-REQ-004 | `AgentEnginePort` MAY expose `interrupt?(sessionId: string): Promise<void>` when the adapter can support interruption. | `docs/SPEC.md` section 10.2 |
> | DEL-03-01-REQ-005 | `AgentEngineRunInput` SHALL carry active session identity, resolved runtime options, and content blocks; normalized project root, persona, mode, and attachment summaries are carried through `SessionRecord`/resolved options, while interrupt and stream cancellation are out of band. | `docs/SPEC.md` section 10.2 |
> | DEL-03-01-REQ-006 | The contract SHALL cover accepted turn input, browser `UIEvent` yield, canonical `HarnessEvent` persistence, permission enforcement or invocation, permitted tool exposure, SDK session metadata linkage, interrupt/cancel behavior, and terminal outcomes. | `docs/SPEC.md` section 10.1; `docs/TYPES.md` section 7.1 |
> | DEL-03-01-REQ-007 | SDK-specific names, IDs, permission modes, transcript paths, tool names, and hook names SHALL appear only as explicit adapter metadata. | `docs/SPEC.md` section 10.3; `docs/DIRECTIVE.md` section 2.10 |
> | DEL-03-01-REQ-008 | The SDK-backed adapter SHALL pass the engine conformance suite before becoming the default production path. | `docs/CONTRACT.md` K-ENGINE-2; `docs/SPEC.md` section 10.3; `docs/PRD.md` FR-123 |
> | DEL-03-01-REQ-009 | A deterministic stub adapter SHALL remain available for tests. | `docs/SPEC.md` section 10.3 |
> | DEL-03-01-REQ-010 | Engine conformance tests SHALL cover accepted-turn persistence before SDK/model execution, terminal outcome persistence, SSE compatibility, SDK message mapping, permission denial, tool exposure, interrupt/cancel behavior, session resume, and redaction. | `docs/PRD.md` FR-123; `docs/PRD.md` section 12.5 |
> | DEL-03-01-REQ-011 | The contract and tests SHALL preserve the stable browser SSE names: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, and the additive redacted `harness:event` bridge. | `docs/SPEC.md` section 11; `docs/TYPES.md` section 7.4; D-APP-40 |
> | DEL-03-01-REQ-012 | `/api/harness/turn` SHALL remain a transport adapter; runtime policy belongs behind the contract and `TurnEngine`, not in the route. | `docs/SPEC.md` section 10.4; `docs/PRD.md` section 9.1 |
> | DEL-03-01-REQ-013 | The conformance suite SHALL reject provider-shaped leakage in public APIs and canonical `HarnessEvent` fields except as explicit adapter metadata. | `docs/PRD.md` section 12.5; `docs/CONTRACT.md` K-ENGINE-4 |
> | DEL-03-01-REQ-014 | The contract documentation SHALL record fallback criteria when SDK behavior cannot satisfy or verify a product-critical boundary. | `docs/CONTRACT.md` K-ENGINE-5; `docs/PLAN.md` R0 acceptance; `docs/PRD.md` FR-126 |
> | DEL-03-01-REQ-015 | Requirements derived from `docs/PRD.md` SHALL use the current D-APP-38 authority-corpus reference state. | `_REFERENCES.md` REF-006; D-APP-38 |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / Source | Applicability |
> |---|---|
> | `docs/DIRECTIVE.md` sections 2.8-2.11 | Runtime ownership, reliance boundaries, provider-neutral core, product identity. |
> | `docs/CONTRACT.md` sections 1.4-1.5 | Binding invariants for engine boundary and runtime events. |
> | `docs/SPEC.md` sections 9-13 | Event schema, runtime engine contract, SSE names, SDK settings posture, runtime options/persona composition. |
> | `docs/TYPES.md` section 7 | Canonical runtime vocabulary and type targets. |
> | `docs/PLAN.md` R0/R1 | Roadmap and sequencing constraints for engine contract and conformance. |
> | `docs/PRD.md` sections 8.16, 9, 12, and 13 | Product requirements and validation expectations; REF-006 is reconciled under D-APP-38. |
>

### CLM-011 — Verification

> ##### Verification
>
> | Requirement IDs | Verification Approach |
> |---|---|
> | REQ-001, REQ-002, REQ-007, REQ-013 | Type/API review and tests proving public contract types do not expose SDK-shaped names except adapter metadata. |
> | REQ-003, REQ-004, REQ-005, REQ-006 | Unit tests around `AgentEnginePort`/`RuntimeEngineContract` type fixtures and adapter test harness inputs. |
> | REQ-008, REQ-009, REQ-010 | Engine conformance suite runs against stub and SDK-backed adapters before production-default enablement. |
> | REQ-011, REQ-012 | Integration or compatibility tests proving `/api/harness/turn` shape and browser SSE event names are unchanged. |
> | REQ-014 | Runtime contract documentation includes fallback criteria and cross-reference to reliance-boundary register. |
> | REQ-015 | D-APP-38 confirms the current `docs/PRD.md` authority-corpus state before closing the deliverable. |
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required deliverable artifacts:
>
> - `agent-engine-port.ts` or equivalent product-owned runtime contract.
> - Runtime contract documentation describing ownership, adapter boundary, input/output shape, and fallback criteria.
> - Engine conformance suite covering stub and SDK-backed adapters.
> - Test index or validation reference for `section9.runtime_engine_contract` once Section 9 runtime validation is implemented.
>
> Conformance evidence schema:
>
> - Adapter subject: `stub`, `SDK-backed`, or `blocked SDK-backed case`.
> - Case coverage: accepted-turn persistence, terminal outcome persistence, SSE compatibility, SDK message mapping, permission denial, tool exposure, interrupt/cancel behavior, session resume/linkage, redaction, and SDK-shaped leakage checks.
> - Result status: `PASS`, `FAIL`, or `BLOCKED_TBD`; blocked cases must name the missing DEL-04-01 probe detail or other upstream blocker.
> - Closure evidence: test output path or `TBD`, runtime contract documentation link, fallback/risk note when a product-critical boundary cannot be verified, REF-006 human ruling status, and `section9.runtime_engine_contract` linkage status once available.
>
> TBD:
>
> - Final implementation path if not `frontend/src/lib/harness/agent-engine-port.ts`.
> - Exact SDK-backed adapter fixture shape until DEL-04-01 confirms SDK probe details.
> - Exact session-link metadata fields accepted by the conformance suite until DEL-04-01/DEL-05 work confirms transcript/store placement.
> - Accepting party for staged SDK-dependent conformance cases beyond the current scripted adapter coverage.
> - Section 9 runtime validation linkage remains through the current `section9.adapter_*` validation IDs until a later governed rename.
>

### CLM-013 — Source-State Warning

> ##### Source-State Warning
>
> D-APP-38 established the authority-corpus reference model. Current `_REFERENCES.md` records REF-006 as `MATCH`; future authority-document edits require a corpus bump/apply before acceptance.

- **AC-001** — The product-owned runtime boundary keeps SDK-shaped semantics behind explicit adapter metadata, and the stub and SDK-backed adapters satisfy the source-defined conformance suite before production-default use.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-03-01 AgentEnginePort and Engine Conformance Suite

> #### Procedure: DEL-03-01 AgentEnginePort and Engine Conformance Suite
>

### CLM-015 — Purpose

> ##### Purpose
>
> Define and verify the product-owned engine boundary and conformance suite for stub and SDK-backed runtime adapters while preserving Chirality-owned semantics, stable route/SSE behavior, and adapter replaceability.
>
> Sources: `docs/SPEC.md` sections 10-12; `docs/PRD.md` sections 8.16, 9, 12, and 13; `docs/CONTRACT.md` sections 1.4-1.5.
>

### CLM-016 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Note |
> |---|---|
> | Deliverable state allows drafting | Current `_STATUS.md` state was `OPEN` before this P1/P2 run. |
> | Authoritative sources available | REF-001 through REF-007 are locally accessible. |
> | PRD source state acknowledged | REF-006 is MATCH under the current D-APP-38 authority corpus. |
> | Declared upstream dependencies | `_DEPENDENCIES.md` lists declared upstream as TBD; no accepted dependency edges have been extracted yet. |
> | SDK probe details | TBD; exact SDK message categories, session store behavior, and interrupt behavior depend on DEL-04-01. |
> | Acceptance authority for staged SDK cases | TBD; human acceptance is required for any `BLOCKED_TBD` SDK-backed conformance case until DEL-04-01 supplies the missing probe detail. |
>

### CLM-017 — Steps

> ##### Steps
>
> 1. Confirm the scope boundary.
>    - Use DEL-03-01 only for the engine contract and conformance suite.
>    - Keep `TurnEngine` implementation, route adapter fixtures, SDK probe decision, and event store implementation in their owning deliverables unless needed as conformance references.
>
> 2. Draft the runtime contract.
>    - Define `AgentEnginePort` / `RuntimeEngineContract` as product-owned.
>    - Include `startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>`.
>    - Include optional `interrupt?(sessionId: string): Promise<void>` when adapter support exists.
>    - Define `TurnInput` with active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable.
>
> 3. Define adapter boundary rules.
>    - Keep SDK/provider message names, tool names, permission modes, transcript paths, hook names, and session IDs outside public APIs and canonical event fields except under explicit adapter metadata.
>    - Preserve the stub adapter as deterministic conformance baseline.
>    - Mark exact SDK-backed fixture details as `TBD` until DEL-04-01 confirms SDK behavior.
>
> 4. Specify the conformance suite.
>    - Test accepted-turn persistence before SDK/model execution.
>    - Test terminal success, failure, cancellation, and interruption persistence.
>    - Test browser SSE compatibility and stable UI event names.
>    - Test SDK message mapping into product-owned UI/runtime events.
>    - Test permission denial and permitted tool exposure behavior at the contract boundary.
>    - Test session resume/linkage metadata without making SDK transcripts canonical.
>    - Test redaction and absence of SDK-shaped leakage in public contracts and canonical events.
>
> 5. Align with route and event contracts.
>    - Confirm `/api/harness/turn` remains a transport adapter.
>    - Confirm browser-facing event names remain `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, and the additive redacted `harness:event` bridge.
>    - Confirm canonical runtime records use `HarnessEvent` shape and product-owned event categories.
>
> 6. Record fallback and source-state caveats.
>    - Document fallback criteria if SDK behavior cannot satisfy a product-critical boundary.
>    - If future authority documents change, run the D-APP-38 corpus bump/apply before acceptance.
>
> 7. Prepare deliverable records.
>    - Produce or update runtime contract docs.
>    - Produce or update `agent-engine-port.ts` or equivalent.
>    - Produce or update engine conformance tests.
>    - Link the conformance suite to `section9.runtime_engine_contract` once Section 9 validation exists.
>

### CLM-018 — Verification

> ##### Verification
>
> | Check | Expected Result |
> |---|---|
> | Contract shape check | `AgentEnginePort` exposes `startTurn` and optional `interrupt` with inputs/outputs matching `docs/SPEC.md` section 10.2. |
> | Provider-neutrality check | Public APIs and canonical `HarnessEvent` fields do not contain SDK-shaped names except explicit adapter metadata. |
> | Stub conformance | Stub adapter passes the same conformance suite used for SDK-backed adapter where applicable. |
> | SDK-backed conformance | SDK-backed adapter passes before default production enablement; cases blocked by SDK probe details remain `TBD` until DEL-04-01 closes. |
> | SSE compatibility | Browser event names and `/api/harness/turn` route shape remain stable. |
> | Event persistence | Accepted turn and terminal outcomes are persisted in Chirality-owned event form. |
> | Redaction | Provider/SDK errors and runtime records do not store API keys or secrets. |
> | Authority-corpus check | REF-006 is reconciled under D-APP-38; future authority-doc edits trigger corpus bump/apply. |
>

### CLM-019 — Records

> ##### Records
>
> Required records for closure:
>
> - Runtime contract source file: `agent-engine-port.ts` or equivalent.
> - Runtime contract documentation.
> - Engine conformance test file or suite.
> - Test output showing stub adapter pass.
> - Test output showing SDK-backed adapter pass, or a `BLOCKED_TBD` record naming the DEL-04-01 blocker, affected conformance case, fallback/risk note, and accepting party status.
> - Conformance evidence matrix covering adapter subject, case coverage, result status, test output path or `TBD`, fallback/risk note, D-APP-38 authority-corpus status, and Section 9 linkage status.
> - Section 9 validation linkage when `section9.runtime_engine_contract` exists, or a `TBD` linkage record naming DEL-09-02 as the unavailable validation surface.

- **VER-001** — Run the source-defined type/API, adapter-conformance, route/SSE compatibility, persistence, permission, tool-exposure, interrupt/cancel, resume/linkage, redaction, and provider-neutrality checks.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-03-01 AgentEnginePort and Engine Conformance Suite

> #### Guidance: DEL-03-01 AgentEnginePort and Engine Conformance Suite
>

### CLM-021 — Purpose

> ##### Purpose
>
> DEL-03-01 exists to make the runtime engine replaceable by construction while allowing the Claude Agent SDK to serve as the preferred implementation substrate when it satisfies Chirality-owned governance, audit, permission, session, and route-compatibility requirements.
>
> The decomposition assigns this deliverable to SOW-037 and OBJ-002: define the product-owned `AgentEnginePort` / `RuntimeEngineContract` and conformance tests before SDK behavior becomes production default.
>
> Sources: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-03-01; `docs/DIRECTIVE.md` sections 2.8-2.10; `docs/PLAN.md` sections 2-4.
>

### CLM-022 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Chirality terms at the core | Contract names, public APIs, browser events, persisted events, permission decisions, and session records should use Chirality vocabulary. SDK details belong behind `EngineAdapter`. | `docs/CONTRACT.md` K-CORE-1 and K-ENGINE-4; `docs/TYPES.md` section 7 |
> | Conformance before default | Treat SDK adoption as conditional. The SDK-backed adapter is not default until it passes conformance tests. | `docs/CONTRACT.md` K-ENGINE-2; `docs/SPEC.md` section 10.3 |
> | Route stability | Keep `/api/harness/turn` as transport and compatibility surface. Runtime policy should be owned by `TurnEngine` and the engine boundary. | `docs/SPEC.md` section 10.4; `docs/PRD.md` section 9.1 |
> | Event separation | Keep compact browser `UIEvent`s distinct from richer persisted `HarnessEvent`s. | `docs/CONTRACT.md` K-EVENT-1; `docs/SPEC.md` sections 9 and 11 |
> | Adapter metadata quarantine | SDK session IDs, transcript paths, tool names, permission modes, message categories, and hook names may be retained only as explicit adapter metadata. | `docs/DIRECTIVE.md` section 2.10; `docs/SPEC.md` section 10.3 |
> | Reliance boundaries are test subjects | Product-critical boundaries must be testable in Chirality terms, not only described in prompts or assumed from SDK defaults. | `docs/DIRECTIVE.md` section 2.9; `docs/CONTRACT.md` K-RELIANCE-2 |
>

### CLM-023 — Considerations

> ##### Considerations
>
> - Keep the initial `AgentEnginePort` narrow. A small boundary makes stub and SDK-backed adapters easier to compare and keeps SDK-specific behavior from leaking into the product contract.
> - Make the conformance suite adapter-agnostic. Tests should assert Chirality outcomes: accepted-turn persistence, stable UI events, canonical event records, terminal outcomes, permission denial, redaction, and absence of SDK-shaped leakage.
> - Expect some tests to be staged. SDK message categories, resume behavior, `SessionStore`, `CLAUDE_CONFIG_DIR`, and interrupt behavior depend on DEL-04-01 probe findings, so mark unsupported cases as `TBD` rather than hard-coding assumptions.
> - Preserve the stub adapter. It is the deterministic baseline for contract tests and fallback analysis.
> - Keep PRD-derived details visible and source-bound. D-APP-38 confirms the current authority corpus for `docs/PRD.md`; implementation proof still needs deliverable-local evidence.
>

### CLM-024 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Preferred Direction | Rationale |
> |---|---|---|
> | Thin contract vs broad SDK wrapper | Prefer thin product-owned contract. | Reduces SDK lock-in and supports provider-neutral conformance. |
> | Full SDK parity vs governed subset | Prefer governed subset. | PLAN states Chirality does not chase Claude Code feature parity; it adopts SDK mechanics where they accelerate the product-owned contract. |
> | Unit-only tests vs mixed conformance | Use both type/unit tests and route/SSE compatibility checks. | Contract correctness must cover adapter behavior and user-visible stream compatibility. |
> | Early implementation specificity vs `TBD` | Use `TBD` until SDK probe results exist. | Prevents inaccessible or unstable SDK behavior from becoming accepted project truth. |
> | Fallback criteria in docs vs tests only | Keep fallback criteria in runtime contract documentation and verify them through conformance where possible. | `docs/CONTRACT.md` K-ENGINE-5 and `docs/PRD.md` FR-126 make fallback a governed acceptance judgment, not just a test failure outcome; documentation must state when an unverifiable SDK boundary triggers fallback or residual-risk review. |
>

### CLM-025 — Examples

> ##### Examples
>
> Illustrative interface shape from `docs/SPEC.md` section 10.2:
>
> ```ts
> interface AgentEnginePort {
>   startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>;
>   interrupt?(sessionId: string): Promise<void>;
> }
> ```
>
> Example conformance assertions:
>
> - A stub adapter yields only stable browser `UIEvent` names and does not expose provider-specific fields in public stream payloads.
> - An SDK-backed adapter persists `turn.accepted` before invoking SDK/model execution.
> - An SDK-backed adapter maps SDK result/failure/interruption outcomes into product-owned terminal `HarnessEvent` records; explicit user interruption terminates as `turn.interrupted` per D-APP-40.
> - A leakage test fails if public APIs or canonical `HarnessEvent` fields expose SDK message names, permission modes, transcript paths, tool names, or session IDs outside explicit adapter metadata.
>

### CLM-026 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | CT-001 | Resolved by D-APP-38: REF-006 now matches the authority corpus. | `_REFERENCES.md` REF-006 | `docs/PRD.md` sections 8.16, 9, 12, 13 | Datasheet Conditions/References; Specification Requirements/Verification; Procedure Prerequisites | Apply D-APP-38 corpus workflow for future authority edits. | Ruled 2026-06-20 |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-037 OBJ-002 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
