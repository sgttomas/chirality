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
> | AnticipatedArtifacts | Canonical @chirality/runtime-contracts consumption; App-client conformance tests; current API/event compatibility evidence (D-APP-118 facade retirement). |
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
> | Optional operation | Interruption is required by current SPEC §10.2; the engine boundary exposes descriptor, preflight, turn execution and interrupt capability. | `docs/SPEC.md` section 10.2 |
> | Browser stream contract | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` section 11; `docs/TYPES.md` section 7.4 |
> | Canonical runtime record | `HarnessEvent` records in product-owned event JSONL. | `docs/SPEC.md` section 9; `docs/TYPES.md` section 7.3 |
> | Required conformance subject | The live Codex delegated adapter and App client are the qualification subjects; deterministic stubs and retained SDK cases remain bounded evidence. | `docs/SPEC.md` section 10.3; `docs/PRD.md` section 12.5 |
> | Production-default gate | Map accepted-input ordering, terminal durability, request/session correctness, current capabilities, permission decisions, applicable tool exposure, interruption, native resume and redaction to current Codex checks and S-1–S-8. Reuse source-valid evidence and run each missing distinct check; neither a blanket legacy-suite gate nor unproved equivalence qualifies the live Codex path. Stub and retained SDK results prove only their own subjects. | `docs/CONTRACT.md` K-ENGINE-2; `docs/PRD.md` FR-123 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Requirement / Constraint | Source |
> |---|---|---|
> | Provider-neutral core | Chirality owns its application contracts and authority boundaries while the full stock Codex protocol remains available; upstream event identity is preserved under D-GOV-43. | `docs/DIRECTIVE.md` section 2.10; `docs/CONTRACT.md` K-ENGINE-4 |
> | Route compatibility | Existing `/api/harness/*` route shapes remain stable during SDK adoption and TurnEngine extraction. | `docs/PRD.md` section 9.1; `docs/SPEC.md` section 10.4 |
> | SSE compatibility | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` section 11; `docs/PRD.md` section 9.3 |
> | Terminal outcomes | Accepted turns must persist terminal success, failure, cancellation, or interruption outcomes. | `docs/CONTRACT.md` K-EVENT-3; `docs/PRD.md` FR-123 |
> | Accepted-turn persistence | Accepted user input must be persisted before SDK/model execution begins. | `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` section 12.6 |
> | SDK metadata boundary | Preserve upstream Codex IDs, methods, tools and payloads as inspectable source data. Chirality normalized views do not replace or suppress that evidence. | `docs/DIRECTIVE.md` section 2.10; `docs/SPEC.md` section 10.3 |
> | Source-state status | `docs/PRD.md` was reconciled in an earlier D-APP-38 snapshot; consult current `_REFERENCES.md` observations and the accepted corpus separately. | `_REFERENCES.md` REF-006; D-APP-38 |
>

### CLM-005 — Engine boundary and conformance

The App must consume the Runtime-owned engine boundary for the sole MVP engine and qualification target, Codex. Turn inputs preserve the active session, registered project root, selected role, permission policy, resolved runtime options, content and attachment references, and cancellation semantics required by the accepted contract. Contract-module filenames, interface signatures and former shim paths are implementation evidence, rather than an additional App implementation mandate.

The surviving request/session correctness obligations must be mapped to current verification, including D-GOV-43 S-1–S-8 where applicable. D-GOV-43 retires vanished-purpose gates and avoids duplicate checks for the same condition; the legacy suite as a whole is not a new blanket admission gate. Deterministic stub and retained SDK tests establish only their own subjects. P-08 remains a bounded coverage-mapping residual: identify genuinely uncovered live-Codex obligations for accepted turns, terminal outcomes, capabilities, applicable tool handling and secret protection; do not declare equivalence without that mapping.

Verification hooks: `projects/chirality-runtime/packages/contracts/src/harness/engine-conformance.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/lib/engine-conformance.test.ts`. The last is retained compatibility/test evidence and is not a live-Codex qualification witness.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

D-APP-118 (2026-09-22) retires the former `@chirality/harness-contract` facade and its dedicated rollback support. The supported contract source is the Runtime package above; no facade retention or export-identity test remains a completion requirement. Historical source pins and the other live conformance obligations retain their separate evidence boundaries.

### CLM-006 — References

> ##### References
>
> | RefID | Source | Status / Note |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Observation: see _REFERENCES.md; sections 2.8-2.11 used. |
> | REF-002 | `docs/CONTRACT.md` | Observation: see _REFERENCES.md; sections 1.4-1.5 and enforcement map used. |
> | REF-003 | `docs/SPEC.md` | Observation: see _REFERENCES.md; sections 9-13 used. |
> | REF-004 | `docs/TYPES.md` | Observation: see _REFERENCES.md; sections 7 and 12 used. |
> | REF-005 | `docs/PLAN.md` | Observation: see _REFERENCES.md; sections 2-4, 6.2, and 8 used. |
> | REF-006 | `docs/PRD.md` | Current observation: see _REFERENCES.md; sections 8.16, 9, 12, and 13 used. |
> | REF-007 | `workflows/software-decomp/WORKFLOW.md` | Observation: see _REFERENCES.md; not used for content requirements beyond decomposition provenance. |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-03-01 AgentEnginePort and Engine Conformance Suite

> #### Specification: DEL-03-01 AgentEnginePort and Engine Conformance Suite
>

### CLM-008 — Scope

This deliverable verifies the App client against the Runtime-owned contracts for the sole MVP engine, Codex. It owns contract-consumption and conformance evidence, not a second engine implementation. Preserve session/input binding, accepted-turn ordering, terminal outcomes, current permission and tool boundaries, native resume, interrupt behavior and redaction. Map accepted-input ordering, terminal durability, request/session correctness, current capabilities, permission decisions, applicable tool exposure, interruption, native resume and redaction to current Codex checks and S-1–S-8. Reuse source-valid evidence and run each missing distinct check; neither a blanket legacy-suite gate nor unproved equivalence qualifies the live Codex path. Stub and retained SDK results prove only their own subjects.

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-03-01-REQ-001 | Chirality SHALL define `AgentEnginePort` / `RuntimeEngineContract` separate from SDK APIs. | `docs/SPEC.md` section 10.1; `docs/PRD.md` FR-122 |
> | DEL-03-01-REQ-002 | Chirality SHALL own application contracts and governance while hosting the full stock Codex protocol; upstream names and payloads SHALL remain inspectable under D-GOV-43. | `docs/DIRECTIVE.md` sections 2.8 and 2.10; `docs/CONTRACT.md` K-ENGINE-1 and K-ENGINE-4 |
> | DEL-03-01-REQ-003 | `AgentEnginePort` SHALL expose `startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>`. | `docs/SPEC.md` section 10.2; D-APP-40 |
> | DEL-03-01-REQ-004 | The engine boundary SHALL support descriptor, preflight and interruption as specified by current SPEC §10.2; explicit Stop reaches the active turn. | `docs/SPEC.md` section 10.2 |
> | DEL-03-01-REQ-005 | `AgentEngineRunInput` SHALL carry active session identity, resolved runtime options, and content blocks; normalized project root, persona, mode, and attachment summaries are carried through `SessionRecord`/resolved options, while interrupt and stream cancellation are out of band. | `docs/SPEC.md` section 10.2 |
> | DEL-03-01-REQ-006 | The contract SHALL cover accepted turn input, browser `UIEvent` yield, canonical `HarnessEvent` persistence, permission enforcement or invocation, permitted tool exposure, Codex thread/session linkage, interrupt/cancel behavior, and terminal outcomes. | `docs/SPEC.md` section 10.1; `docs/TYPES.md` section 7.1 |
> | DEL-03-01-REQ-007 | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` section 10.3; `docs/DIRECTIVE.md` section 2.10 |
> | DEL-03-01-REQ-008 | Map accepted-input ordering, terminal durability, request/session correctness, current capabilities, permission decisions, applicable tool exposure, interruption, native resume and redaction to current Codex checks and S-1–S-8. Reuse source-valid evidence and run each missing distinct check; neither a blanket legacy-suite gate nor unproved equivalence qualifies the live Codex path. Stub and retained SDK results prove only their own subjects. | `docs/CONTRACT.md` K-ENGINE-2; `docs/SPEC.md` section 10.3; `docs/PRD.md` FR-123 |
> | DEL-03-01-REQ-009 | A deterministic stub adapter SHALL remain available for tests. | `docs/SPEC.md` section 10.3 |
> | DEL-03-01-REQ-010 | Engine conformance tests SHALL cover accepted-turn persistence before Codex execution, terminal outcome persistence, browser event compatibility, complete upstream event preservation and normalization, permission outcomes, tool exposure, interrupt/cancel behavior, native session resume and sink-specific redaction. Retained SDK message-mapper fixtures prove compatibility only. | `docs/PRD.md` FR-123; `docs/PRD.md` section 12.5 |
> | DEL-03-01-REQ-011 | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` section 11; `docs/TYPES.md` section 7.4; D-APP-40 |
> | DEL-03-01-REQ-012 | The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn. | `docs/SPEC.md` section 10.4; `docs/PRD.md` section 9.1 |
> | DEL-03-01-REQ-013 | Conformance SHALL verify complete upstream event preservation, correct normalized views, and structural secret redaction on the live path; retired provider-name rejection is not an oracle. | `docs/PRD.md` section 12.5; `docs/CONTRACT.md` K-ENGINE-4 |
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
> | `docs/PRD.md` sections 8.16, 9, 12, and 13 | Product requirements and validation expectations; current observed reference status is read from _REFERENCES.md separately from accepted pins. |
>

### CLM-011 — Verification

Map accepted-input ordering, terminal durability, request/session correctness, current capabilities, permission decisions, applicable tool exposure, interruption, native resume and redaction to current Codex checks and S-1–S-8. Reuse source-valid evidence and run each missing distinct check; neither a blanket legacy-suite gate nor unproved equivalence qualifies the live Codex path. Stub and retained SDK results prove only their own subjects.

Verify the current SPEC §10.2 boundary, thin route transport, extensible events, accepted-input/terminal persistence, user-selected policy enforcement, tools, interrupt and resume. Source-map each case and result to the actual adapter and candidate. Use `projects/chirality-runtime/packages/contracts/src/harness/engine-conformance.ts`, `projects/chirality-runtime/tests/codex-supervisor.test.ts`, and the S-1–S-8 native checklist; `frontend/src/__tests__/lib/engine-conformance.test.ts` remains compatibility evidence only. Missing redaction or live cases remain open.

### CLM-012 — Documentation

Required artifacts are the App-client contract-consumption record, runtime boundary documentation and a live-Codex conformance matrix. The canonical source is `@chirality/runtime-contracts`; the former facade and rollback test are retired by D-APP-118. For each case record the actual adapter, source/candidate identity, requirement, named check, PASS/FAIL/BLOCKED result, output location, and any uncovered obligation. Include accepted input, terminal outcomes, stream preservation, policy/tool handling, interrupt, native resume and redaction. Missing results remain unknown; the historical SDK probe is not an admission prerequisite. Keep the applicable Section 9 validation linkage explicit.

### CLM-013 — Source-State Warning

> ##### Source-State Warning
>
> D-APP-38 established the authority-corpus reference model. That historical result does not establish the current observed hash. Consult `_REFERENCES.md`; genuine normative amendments retain D-APP-38 controls without an automatic re-pin merely for carrier lag.

- **AC-001** — The App consumes the Runtime-owned Codex boundary correctly; each surviving conformance obligation has source-bound current evidence or an explicit open result. Complete upstream events and structural secret protection are both required.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-03-01 AgentEnginePort and Engine Conformance Suite

> #### Procedure: DEL-03-01 AgentEnginePort and Engine Conformance Suite
>

### CLM-015 — Purpose

Verify App-client conformance against the Runtime-owned Codex contract, preserving request/session correctness, inspectable events and independent evidence. Map accepted-input ordering, terminal durability, request/session correctness, current capabilities, permission decisions, applicable tool exposure, interruption, native resume and redaction to current Codex checks and S-1–S-8. Reuse source-valid evidence and run each missing distinct check; neither a blanket legacy-suite gate nor unproved equivalence qualifies the live Codex path. Stub and retained SDK results prove only their own subjects.

### CLM-016 — Prerequisites

Read the current adopted SPEC §§10–11 and D-GOV-43/D-APP-127, record the source identity, and consult `_REFERENCES.md` plus the extracted `Dependencies.csv` without changing pins or satisfaction states. The canonical contract is in Runtime; use the current production Codex adapter and S-1–S-8 evidence. A missing distinct check blocks that claim, not every unrelated check. Lifecycle approval and current-source conformance evidence remain separate.

### CLM-017 — Steps

1. Bind the App client and Runtime contract to the actual candidate and Codex version.
2. Inventory each surviving request/session, capability, policy/tool, persistence, terminal, interrupt, resume and redaction obligation.
3. Map it to current contract checks and S-1–S-8; retain valid evidence and identify gaps without assuming suite equivalence.
4. Verify thin route transport and full upstream event preservation, including unfamiliar notifications and requests.
5. Execute missing checks on their actual live or deterministic subjects and record failures or blocked cases honestly.
6. Record the per-case result matrix, source identities, unresolved risk/fallback judgment and applicable validation linkage. No automatic second-engine fallback or facade rollback is introduced.

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-018 — Verification

Map accepted-input ordering, terminal durability, request/session correctness, current capabilities, permission decisions, applicable tool exposure, interruption, native resume and redaction to current Codex checks and S-1–S-8. Reuse source-valid evidence and run each missing distinct check; neither a blanket legacy-suite gate nor unproved equivalence qualifies the live Codex path. Stub and retained SDK results prove only their own subjects.

Required evidence includes descriptor/preflight/interrupt checks, accepted-input ordering, terminal durability, policy/tool behavior, native resume, complete event forwarding and sink-by-sink structural redaction. Compare each result to the exact current source. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-019 — Records

Preserve the canonical Runtime contract locator, App client source identity, requirement-to-check matrix, commands/results, and S-1–S-8 witness links. Record stub and legacy SDK evidence with their own subject, never as live-Codex qualification. Name every blocked or uncovered case, its owner and follow-up gate. Keep reference-currentness, Section 9 linkage and lifecycle authority separate.

- **VER-001** — Run the source-defined type/API, adapter-conformance, route/SSE compatibility, persistence, permission, tool-exposure, interrupt/cancel, resume/linkage, redaction, and provider-neutrality checks.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-03-01 AgentEnginePort and Engine Conformance Suite

> #### Guidance: DEL-03-01 AgentEnginePort and Engine Conformance Suite
>

### CLM-021 — Purpose

DEL-03-01 establishes evidence that the App consumes Runtime contracts correctly on the sole MVP engine and qualification target, Codex. Request/session correctness, observable permission and tool behavior, durable records and reliable continuation remain the purpose. A replaceable multi-engine implementation and the retired facade are not current completion subjects. Source: D-GOV-43, D-APP-127, D-APP-131 P-08 and D-APP-118.

### CLM-022 — Principles

Keep Chirality application authority explicit, preserve all Codex protocol events, and verify substantive boundaries on the actual execution path. Normalized presentation and durable runtime records serve different purposes but must preserve upstream identity. Map accepted-input ordering, terminal durability, request/session correctness, current capabilities, permission decisions, applicable tool exposure, interruption, native resume and redaction to current Codex checks and S-1–S-8. Reuse source-valid evidence and run each missing distinct check; neither a blanket legacy-suite gate nor unproved equivalence qualifies the live Codex path. Stub and retained SDK results prove only their own subjects. The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn.

### CLM-023 — Considerations

Use current Codex source and execution evidence; do not infer native resume or secret protection from a legacy SDK fixture. Preserve the deterministic stub for bounded contract checks, source-valid native witnesses for their conditions and explicit unknowns for missing results. Re-run only checks invalidated by changed source, configuration or packaging. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-024 — Trade-offs

Use the full stock Codex protocol while keeping application responsibilities and authority boundaries explicit. Type/unit checks and production/native evidence cover distinct conditions. Missing evidence stays open rather than becoming an SDK-probe prerequisite. If a product-critical boundary cannot be satisfied, record its risk and route the actual acceptance/scope decision; do not automatically switch engines.

### CLM-025 — Examples

A current engine descriptor and preflight establish supported capability before turn execution. Accepted input is durable before execution; an explicit Stop yields a truthful terminal interruption. Unknown upstream notifications remain inspectable, while a secret-bearing payload is structurally redacted before each sink. A relaunch resumes the existing Codex thread without resending the original prompt. Verify these examples with the current conformance matrix and S-1–S-8; they are requirements, not reported results.

### CLM-026 — Conflict Table (for human ruling)

D-GOV-43/D-APP-131 settle the former provider-name versus event-preservation question: preserve upstream Codex events and keep secret protection. D-APP-118 settles facade retirement. P-08 remains the current coverage-mapping task, with missing distinct live checks open. D-APP-38 reference observations and accepted corpus identity remain separate; no automatic corpus bump, re-pin or lifecycle promotion follows from this repair.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-037 OBJ-002 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
