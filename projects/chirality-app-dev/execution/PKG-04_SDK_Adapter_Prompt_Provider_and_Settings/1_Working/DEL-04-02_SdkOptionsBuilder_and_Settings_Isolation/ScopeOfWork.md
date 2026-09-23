---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-02
package_id: PKG-04
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-016, SOW-045, SOW-047, SOW-052, SOW-076]
package_objective_refs: [OBJ-004, OBJ-005]
---

# Scope of Work — DEL-04-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-04-02` in service of project scope [SOW-016, SOW-045, SOW-047, SOW-052, SOW-076] and package objectives [OBJ-004, OBJ-005].

- **OUT-001** — App configuration-composition and conformance evidence for supported Codex thread/turn options, shared-configuration/private-authentication separation, deterministic tool metadata, unknown-key behavior and max-turn guard/terminal handoff, with retained Claude-builder evidence labelled by its actual reach.

**D-APP-80 concordance note (2026-07-28):** SOW-076 is recorded as an OUT
boundary-only trace. It does not activate non-App provider scope or expand
this deliverable beyond App-side SDK option construction and settings
isolation.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-02 SdkOptionsBuilder and Settings Isolation

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-04-02 |
> | DeliverableName | SdkOptionsBuilder and Settings Isolation |
> | PackageID | PKG-04 |
> | PackageName | SDK Adapter, Prompt, Provider, and Settings |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | CoversScopeItems | SOW-016, SOW-045, SOW-047, SOW-052, SOW-076 |
> | SupportsObjectives | OBJ-004, OBJ-005 |
> | AnticipatedArtifacts | `sdk-options-builder.ts`; settings isolation tests; visible tool metadata |
>

### CLM-003 — Attributes

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

Named verification: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`.

### CLM-004 — Conditions

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

Named verification: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`.

### CLM-005 — Construction

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path.

Unfinished delivery: Verify live configuration/unknown-input and safe-metadata behavior; supply a live max-turn guard and terminal-handoff witness or route an actual requirement change through its owner. Retain absent fallback/metadata fixtures as historical limitations.

### CLM-006 — References

> ##### References
>
> | RefID | SourcePath | SectionRef | Use |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Sections 0, 2.8 | Authority order and SDK-governed posture |
> | REF-002 | `docs/CONTRACT.md` | Sections 1.4, 1.6 | SDK governance, settings isolation, permission/tool invariants |
> | REF-003 | `docs/SPEC.md` | Sections 12-15 | Runtime configuration, fallback chains, tool surface, modes/hooks |
> | REF-004 | `docs/TYPES.md` | Sections 7.2, 8.2, 8.3, 9 | Vocabulary for SdkOptionsBuilder, settings, permission, tools, session linkage |
> | REF-005 | `docs/PLAN.md` | Sections 2-4, 6-8 | Roadmap sequencing, tests, known SDK risks |
> | REF-006 | `docs/PRD.md` | Sections 8.4, 8.12, 8.13, 10.3.1, KG-021 through KG-032 | Product requirements; source hash status: HISTORICAL_MATCH noted — reconciled under D-APP-38 |
> | REF-DEC | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | DEL-04-02; SOW-016, SOW-045, SOW-047, SOW-052, SOW-076 | Deliverable scope and traceability |
>


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-119/120/121 record the realized split: `TurnEngine.assertKnownAgentSdkTools` owns runtime validation, the options builder owns deterministic mapping, concrete compiling SDK property names are probe-backed, and the module/test paths are landed.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-04-02 SdkOptionsBuilder and Settings Isolation

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-009 — Scope

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

Verification: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path.

### CLM-010 — Requirements

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-04-02-REQ-001 | Resolve supported model/tool/turn-limit/policy/role options deterministically at the current Runtime boundary; historical Claude fallback tiers do not define native Codex configuration. |
| DEL-04-02-REQ-002 | Unknown optional option keys must be ignored with warnings and must not silently mutate effective behavior. If the live interface rejects them instead, retain that conformance difference as a delivery/scope-resolution gap rather than claim equivalence. |
| DEL-04-02-REQ-003 | Current Codex uses the shared-configuration effective home with separate private credentials. The shipped settingSources:[] rule is retained Claude compatibility history. |
| DEL-04-02-REQ-004 | User configuration/resources remain available through Codex native discovery; the historical project-only development settings exception does not veto native configuration. |
| DEL-04-02-REQ-005 | Validate registered Chirality application tools through the Runtime catalog and structured errors, separately from native Codex tools. |
| DEL-04-02-REQ-006 | Keep application-tool exposure and safe effective configuration deterministic for identical supported inputs; prove any canonical ordering claim with permutations. |
| DEL-04-02-REQ-007 | An allow-name list is not restriction; pass actual native policy and verify separate application-operation authorization. |
| DEL-04-02-REQ-008 | Preserve the max-turn runaway-loop and terminal-outcome requirement. The legacy SDK option is not a live guard; implement/verify the native equivalent or route an actual scope change. |
| DEL-04-02-REQ-009 | Preserve Chirality-owned configuration interface semantics while carrying actual upstream native parameters and safe metadata under the supported contract. |
| DEL-04-02-REQ-010 | Record safe effective version/model/policy/tool/session/resume/linkage metadata where available, with unsupported or absent fields explicit. |
| DEL-04-02-REQ-011 | Do not place credentials or secrets in project files, visible configuration metadata or runtime records. |
| DEL-04-02-REQ-012 | Record exact evaluated options and version from the actual supplier/probe. The historical SDK pin is @anthropic-ai/claude-agent-sdk@0.3.150; it does not qualify current native parameters. |
| DEL-04-02-REQ-013 | Use the owning Runtime session, instruction, tool, delegation and policy interfaces rather than inventing parallel App contracts. |
| DEL-04-02-REQ-014 | Reject missing or inconsistent required current interface inputs with a structured outcome; do not invent permissive defaults or an App policy veto. |

Verification: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path.

Evidence locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`. These are hooks and source locations, not newly executed results.

### CLM-011 — Standards

> ##### Standards
>
> | Standard or Contract | Application | Source |
> |---|---|---|
> | Chirality `AgentEnginePort` / `RuntimeEngineContract` | SDK options are constructed behind a product-owned engine boundary. | `docs/CONTRACT.md` K-ENGINE-1; `docs/SPEC.md` Section 11; `docs/PRD.md` Section 8.12, MATCH — reconciled under D-APP-38 |
> | SDK settings isolation | Shipped runtime must not load ambient user/global Claude Code settings or local `.claude/settings.local.json`. | `docs/CONTRACT.md` K-SDK-1; `docs/SPEC.md` Section 12.2 |
> | Capability-forward policy with explicit hard-deny precedence permission policy | Builder must carry policy posture without confusing auto-approval with restriction. | `docs/CONTRACT.md` K-PERM-1 through K-PERM-6 |
> | Chirality MCP naming | Chirality tools use `mcp__chirality__*` names. | `docs/SPEC.md` Section 14.2; `docs/TYPES.md` Section 8.4 |
> | Epistemic controls | Unknown implementation details remain `TBD` rather than invented. | `docs/CONTRACT.md` K-INVENT-1; `docs/DIRECTIVE.md` Section 2.5 |
>

### CLM-012 — Verification

Required current checks: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path.

Named evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Verify live configuration/unknown-input and safe-metadata behavior; supply a live max-turn guard and terminal-handoff witness or route an actual requirement change through its owner. Retain absent fallback/metadata fixtures as historical limitations.

### CLM-013 — Documentation

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path.

Unfinished delivery: Verify live configuration/unknown-input and safe-metadata behavior; supply a live max-turn guard and terminal-handoff witness or route an actual requirement change through its owner. Retain absent fallback/metadata fixtures as historical limitations.

### CLM-014 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-119/120/121 record the realized split: `TurnEngine.assertKnownAgentSdkTools` owns runtime validation, the options builder owns deterministic mapping, concrete compiling SDK property names are probe-backed, and the module/test paths are landed.

- **AC-001** — Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-04-02 SdkOptionsBuilder and Settings Isolation

> #### Procedure: DEL-04-02 SdkOptionsBuilder and Settings Isolation
>

### CLM-016 — Purpose

> ##### Purpose
>
> Define the operational steps to produce and verify the `SdkOptionsBuilder` feature slice without exceeding the deliverable boundary. The procedure supports creation of `sdk-options-builder.ts`, settings isolation tests, and visible tool metadata.
>

### CLM-017 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Current implementation/adoption evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-018 — Steps

> ##### Steps
>
> 1. Confirm source and package scope.
>    - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the DEL-04-02 decomposition row.
>    - Confirm SOW coverage: SOW-016, SOW-045, SOW-047, SOW-052, SOW-076.
>    - Record the `docs/PRD.md` `HASH_MISMATCH` warning if using PRD-backed details.
>
> 2. Define the builder input shape.
>    - Include session/runtime state needed for model, tools, max turns, mode, persona, hooks, MCP servers, subagents, resume/session linkage, and settings policy.
>    - Reference or import adjacent owner contracts for persona output, session linkage, hooks, MCP server descriptors, subagent descriptors, permission policy, and settings policy when those contracts exist.
>    - Mark exact TypeScript API names as TBD until first-adapter probe/version evidence is accepted.
>
> 3. Implement deterministic fallback resolution.
>    - Resolve model, tools, and max turns using `docs/SPEC.md` Section 13.1.
>    - Resolve mode and persona from request/session values before runtime defaults.
>    - Emit warnings for unknown option keys and ensure unknown keys do not mutate behavior.
>
> 4. Implement settings isolation posture.
>    - For shipped posture, set SDK settings source behavior to `settingSources: []`.
>    - Permit `['project']` only under explicit development configuration.
>    - Reject invalid shipped policy inputs before option construction or omit ambient settings by construction; do not pass `user` or `local` settings sources in shipped builds.
>    - Add safe visible metadata for selected settings-source posture.
>
> 5. Implement tool-surface resolution.
>    - Resolve requested tools against registered SDK built-ins and registered Chirality MCP tool names.
>    - Preserve deterministic ordering.
>    - Return structured validation errors for unknown names before SDK request construction.
>    - Include visible tool metadata that is safe for runtime display/logging.
>
> 6. Carry permission, hook, MCP, and subagent policy posture.
>    - Include `disallowedTools`, permission mode, hooks, `canUseTool`, MCP server descriptors, and subagent descriptors only as supplied by governed policy inputs.
>    - Do not treat `allowedTools` alone as sufficient restriction.
>    - Fail closed or return TBD/integration errors for subagent descriptors until governance bridge requirements are available.
>
> 7. Include max-turn guard option.
>    - Pass resolved `maxTurns` into SDK options.
>    - Ensure runtime/event layers can observe terminal max-turn errors; exact event mapping is TBD in adjacent deliverables.
>
> 8. Produce safe metadata.
>    - Include SDK package version where known, permission mode, visible tool list, MCP server names, settings-source posture, SDK session ID/resume mode, and transcript/store linkage where available.
>    - Exclude API keys, raw secrets, hidden user settings content, and project-truth claims.
>
> 9. Add tests.
>    - Add fallback-chain tests.
>    - Add unknown-option warning tests that prove resolved SDK behavior is unchanged when unknown keys are present.
>    - Add shipped settings isolation tests.
>    - Add development-only project-setting opt-in tests.
>    - Add forbidden `user` and `local` settings-source tests for shipped posture.
>    - Add tool mapping, ordering, and unknown-tool tests.
>    - Add one composite deterministic-order fixture covering requested tools, visible tools, MCP server IDs, allow/deny lists, permission mode, hook/callback posture, and permission policy inputs together.
>    - Add `allowedTools` misconception guard test.
>    - Add max-turn propagation test.
>    - Add safe metadata redaction/exclusion test proving safe fields are present and API keys/secrets are absent.
>
> 10. Run validation.
>     - Run targeted unit tests for `sdk-options-builder.ts` or the selected equivalent module.
>     - Run typecheck after SDK version/API is pinned.
>     - Run broader harness validation when the feature is wired into `TurnEngine`.
>     - Record the exact test command or validation suite once the implementation path exists; until then, keep the command as TBD.
>     - Record any remaining TBD fields, terminal max-turn fixture owner, or SDK-probe dependencies.
>

### CLM-019 — Verification

Required current checks: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path.

Named evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Verify live configuration/unknown-input and safe-metadata behavior; supply a live max-turn guard and terminal-handoff witness or route an actual requirement change through its owner. Retain absent fallback/metadata fixtures as historical limitations.

### CLM-020 — Records

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path.

Unfinished delivery: Verify live configuration/unknown-input and safe-metadata behavior; supply a live max-turn guard and terminal-handoff witness or route an actual requirement change through its owner. Retain absent fallback/metadata fixtures as historical limitations.

### CLM-021 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-119/120/121 record the realized split: `TurnEngine.assertKnownAgentSdkTools` owns runtime validation, the options builder owns deterministic mapping, concrete compiling SDK property names are probe-backed, and the module/test paths are landed.

- **VER-001** — Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-04-02 SdkOptionsBuilder and Settings Isolation

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-023 — Purpose

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

Verification: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path.

### CLM-024 — Principles

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

Named verification: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`.

### CLM-025 — Considerations

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

Named verification: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`.

### CLM-026 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Preferred Direction | Rationale |
> |---|---|---|
> | SDK defaults vs explicit options | Prefer explicit Chirality options and recorded posture. | Prevents ambient settings and SDK defaults from becoming product semantics. |
> | Early tool exposure vs controlled sequence | Prefer read-only and registered tools first; defer write/bash/subagent execution until overlays and hooks are active. | Matches roadmap sequence and avoids permission boundary overclaiming. |
> | Rich SDK metadata vs provider-neutral core | Keep SDK metadata local to adapter/runtime metadata, with public APIs and canonical events in Chirality terms. | Preserves engine replaceability and conformance testing. |
> | Immediate exact SDK field design vs probe-backed API | Use `TBD` for exact fields until SDK version/probe confirms current TypeScript APIs. | Avoids encoding stale or guessed upstream SDK behavior. |
>

### CLM-027 — Examples

> ##### Examples
>

### CLM-028 — Example Fallback Trace

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

Named verification: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`.

### CLM-029 — Example Settings Posture

App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

Preserve deterministic resolution for identical supported inputs, explicit unknown-input handling, safe configuration/model/tool metadata and session/resume linkage. The effective Codex home shares user configuration/resources by reference while private authentication remains Codex-owned. Pass supported policy selections and model/effort changes through the current Runtime interface. Application-tool catalog validation and deterministic exposure retain DEL-06-02 ownership. The max-turn guard and terminal outcome requirement remain an explicit live delivery/evidence gap, not satisfied by a legacy options fixture.

Named verification: Check thread start/resume and turn overrides, unknown-key behavior, deterministic effective configuration, safe metadata, credential exclusion and live max-turn terminal handoff. Legacy fallback/settings tests qualify only their recorded path. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`.

### CLM-030 — Example Tool Resolution

> ###### Example Tool Resolution
>
> ```text
> Requested tools:
>   Read
>   mcp__chirality__status_read
>   unknown_tool
>
> Expected result:
>   Read maps to registered SDK built-in if available.
>   mcp__chirality__status_read maps to registered Chirality MCP tool.
>   unknown_tool returns structured validation error before SDK request construction.
>
> Source:
>   docs/SPEC.md Sections 14.1-14.3
> ```
>

### CLM-031 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. App option composition and conformance must expose the effective Codex thread/turn configuration and policy safely. The Claude options builder, its fallback tiers, `settingSources` and SDK-only option metadata are retained compatibility evidence.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Verify live configuration/unknown-input and safe-metadata behavior; supply a live max-turn guard and terminal-handoff witness or route an actual requirement change through its owner. Retain absent fallback/metadata fixtures as historical limitations.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-016 SOW-045 SOW-047 SOW-052 SOW-076 OBJ-004 OBJ-005 | CLM-010  | AC-001 | VER-001 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |

## Retired status detail (2026-09-23)

These clauses retain the operative meaning of the named App `Remaining` entries after their one-time retirement. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R038:** The max-turn guard and truthful terminal outcome remain current obligations. If the accepted contract cannot be met, use the owning requirement-change process before claiming a different behavior.
