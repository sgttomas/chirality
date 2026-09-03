---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-01
package_id: PKG-04
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-018, SOW-044, SOW-046]
package_objective_refs: [OBJ-004]
---

# Scope of Work — DEL-04-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-04-01` in service of project scope [SOW-018, SOW-044, SOW-046] and package objectives [OBJ-004].

- **OUT-001** — First-adapter probe notes, a version-pinned adoption decision, fallback criteria, future-provider criteria, and residual-risk notes for DEL-04-01 covering SOW-018, SOW-044, SOW-046 and supporting OBJ-004.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision

> #### Datasheet: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-04-01 |
> | Deliverable Name | First-Adapter Probe and Version-Pinned Adoption Decision |
> | Package | PKG-04 SDK Adapter, Prompt, Provider, and Settings |
> | Decomposition Variant | SOFTWARE_DECOMP v3.2 |
> | Type | REQ_SLICE |
> | Context Envelope | M |
> | Responsible Party | TBD |
> | Scope Items | SOW-018, SOW-044, SOW-046 |
> | Objective | OBJ-004 |
> | Anticipated Artifacts | first-adapter probe notes; version decision; fallback criteria; residual-risk notes |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Runtime direction | Claude Agent SDK is the preferred runtime spine only if empirical verification and conformance tests preserve Chirality-owned governance. | `docs/SPEC.md` Section 12.1; `docs/DIRECTIVE.md` Section 2.8 |
> | Product boundary | Chirality owns `AgentEnginePort` / `RuntimeEngineContract`, browser `UIEvent`s, persisted `HarnessEvent`s, session canonicality, permission semantics, working-root/instruction-root policy, prompt/persona composition, redaction, provenance, and fallback criteria. | `docs/DIRECTIVE.md` Section 2.8; `docs/SPEC.md` Section 10 |
> | Probe purpose | Validate SDK assumptions before R1 implementation details harden and make adoption a replaceable engine choice, not product identity. | `docs/PLAN.md` R0; `docs/PRD.md` R0 |
> | Required probe topics | Package version, `query()` message sequence, `settingSources`, permission mapping, `canUseTool`, hooks, in-process MCP, agents, resume, `SessionStore`, `CLAUDE_CONFIG_DIR`, interrupt behavior, Electron packaging, API key environment handling, branding constraints, and fallback triggers. | `docs/PLAN.md` R0; `docs/PRD.md` R0 |
> | Required metadata to capture | SDK package version; Claude Code subprocess version when knowable; SDK permission mode; visible tool list; MCP server names; settings-source posture; SDK session ID and resume mode; transcript/store linkage. | `docs/SPEC.md` Section 12.4 |
> | Adoption decision state | `ADOPT_WITH_RESIDUAL_RISK` for the repository demonstrator, pinned to `@anthropic-ai/claude-agent-sdk@0.3.150` and observed Claude Code `2.1.150`; see `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`. | D-APP-68 recommendation 8; D-APP-52 live evidence |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Current Value | Source |
> |---|---|---|
> | Shipped settings isolation | `settingSources: []` is required for shipped SDK builds. | `docs/SPEC.md` Section 12.2; `docs/PLAN.md` R1; `docs/PRD.md` R1 |
> | Development settings posture | Development-only project settings may use `['project']` behind explicit environment configuration; `user` and `local` setting sources must not be used in shipped builds. | `docs/SPEC.md` Section 12.2 |
> | Transcript canonicality | SDK transcripts are secondary runtime state unless imported into `HarnessEvent` form; Chirality JSONL remains canonical. | `docs/SPEC.md` Sections 8.4 and 10.3; `docs/CONTRACT.md` K-SDK-3 |
> | Tool restriction boundary | `allowedTools` is not a restriction boundary by itself; restrictions require deny policy, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture. | `docs/SPEC.md` Section 14.3; `docs/CONTRACT.md` K-PERM-3 |
> | Permission overlay | Deny overrides allow, including policy, hooks, SDK deny rule, or human gate denials. | `docs/CONTRACT.md` K-PERM-1 |
> | Probe exposure | R0 acceptance requires no local tools exposed to the model during the probe outside controlled validation. | `docs/PLAN.md` R0; `docs/PRD.md` R0 |
> | Source-state warning | `docs/PRD.md` is accessible but `_REFERENCES.md` records `MATCH`; claims citing PRD require snapshot confirmation before closure. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> This deliverable is a requirements/probe decision package, not runtime code. It should be constructed as:
>
> 1. first-adapter probe notes that record empirical behavior for every required probe topic.
> 2. A version-pinned adoption decision identifying the exact `@anthropic-ai/claude-agent-sdk` version and any Claude Code subprocess version when knowable.
> 3. Fallback criteria that preserve the custom-runtime roadmap if a product-critical boundary cannot be satisfied or verified.
> 4. Residual-risk notes for SDK API drift, settings leakage, transcript location, packaging, permissions, subagents, and product-identity drift.
>
> The final adoption record is the deliverable-local `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`. The earlier assumption that the location might be under `docs/harness/` is superseded by D-APP-68 and retained in repository history as pre-ruling drafting context.
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Status | Used For |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | MATCH | Product boundary, reliance boundaries, provider-neutrality, product identity |
> | REF-002 | `docs/CONTRACT.md` | MATCH | Binding invariants for SDK governance, permissions, events, settings, transcripts |
> | REF-003 | `docs/SPEC.md` | MATCH | Runtime contract, session/event schema, SDK configuration, tool surface, hooks |
> | REF-004 | `docs/TYPES.md` | MATCH | Vocabulary for engine, SDK metadata, tools, hooks, MCP, events |
> | REF-005 | `docs/PLAN.md` | MATCH | R0/R1 sequencing, probe deliverables, acceptance criteria |
> | REF-006 | `docs/PRD.md` | MATCH | Product requirements and runtime direction; use requires source-state confirmation — reconciled under D-APP-38 |
> | REF-007 | `AGENT_SOFTWARE_DECOMP.md` | MATCH | Decomposition method context only |
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-118 supersedes setup-era probe TBDs: the probe record, version/package pins, dependency register, and governed environment are landed.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision

> #### Specification: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable specifies the evidence required to decide whether Chirality should adopt a version-pinned Claude Agent SDK runtime path for R1.
>
> Included:
>
> - Confirm the SDK package version and Claude Code subprocess version when knowable.
> - Probe `query()` message sequence, permissions, hooks, in-process MCP, sessions, storage, interrupts, packaging, settings isolation, API key handoff, and fallback triggers.
> - Preserve Chirality-owned runtime semantics for `AgentEnginePort` / `RuntimeEngineContract`, `UIEvent`, `HarnessEvent`, session metadata, permission decisions, redaction, prompt composition, and product identity.
> - Produce first-adapter probe notes, version decision, fallback criteria, and residual-risk notes.
>
> Excluded:
>
> - Implementing `SdkOptionsBuilder`, `SdkMessageMapper`, `TurnEngine`, provider key bridge, or prompt composer code.
> - Exposing new user-visible write, bash, remote MCP, plugin, domain-operation, or subagent execution capability.
> - Treating SDK transcripts or SDK message names as canonical Chirality contracts.
>
> Sources: `_CONTEXT.md`; decomposition row for `DEL-04-01`; `docs/PLAN.md` R0/R1; `docs/PRD.md` R0/R1 with REF-006 hash warning.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | Req ID | Requirement | Verification | Source |
> |---|---|---|---|
> | DEL-04-01-REQ-001 | The probe notes MUST record the exact `@anthropic-ai/claude-agent-sdk` package version selected for evaluation and the Claude Code subprocess version when knowable. | Inspect probe record and package/version evidence. | `docs/SPEC.md` Section 12.4; `docs/PLAN.md` R0 |
> | DEL-04-01-REQ-002 | The adoption decision MUST remain version-pinned and regression-tested on upgrade. | Confirm version decision identifies pin and upgrade test expectation. | `docs/CONTRACT.md` K-SDK-2; `docs/PRD.md` KG-021 |
> | DEL-04-01-REQ-003 | The probe MUST capture SDK `query()` message sequence and determine whether known SDK messages can map to stable `UIEvent`s and provider-neutral `HarnessEvent`s. | Compare probe notes to event mapping acceptance criteria. | `docs/PLAN.md` R0/R1; `docs/SPEC.md` Sections 9 and 10.3 |
> | DEL-04-01-REQ-004 | The decision MUST not accept SDK-specific message names, permission modes, transcript paths, tool names, or session IDs as public API or canonical event fields except as adapter metadata. | Review adoption decision and residual risks for provider-neutral boundary. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-ENGINE-4 |
> | DEL-04-01-REQ-005 | The probe MUST verify shipped settings isolation using `settingSources: []`; any development `['project']` use must be explicit and non-shipped. | Inspect probe result and planned settings tests. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
> | DEL-04-01-REQ-006 | The probe MUST test permission behavior, including `allowedTools`, `disallowedTools`, `permissionMode`, `canUseTool`, hooks, and capability policy, explicit hard-deny precedence, and overlay implications. | Inspect probe notes for each permission surface and a restriction-boundary conclusion. | `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` K-PERM-1 through K-PERM-3 |
> | DEL-04-01-REQ-007 | The probe MUST test in-process Chirality MCP feasibility without treating MCP as a bypass around permission, hooks, path policy, redaction, or event logging. | Confirm probe notes cover MCP transport and wrapper policy expectations. | `docs/SPEC.md` Section 14.2; `docs/CONTRACT.md` K-MCP-1 |
> | DEL-04-01-REQ-008 | The probe MUST capture SDK session ID, resume behavior, transcript/store linkage, `SessionStore`, and `CLAUDE_CONFIG_DIR` behavior. | Inspect session/storage section of probe notes and residual-risk register. | `docs/SPEC.md` Sections 8.4 and 12.4; `docs/PRD.md` KG-024 and KG-028 |
> | DEL-04-01-REQ-009 | The decision MUST keep `.chirality/sessions/<id>/events.jsonl` or a configured Chirality-controlled session path as the canonical audit mirror. | Review adoption decision for transcript canonicality statement. | `docs/DIRECTIVE.md` Section 2.4; `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4 |
> | DEL-04-01-REQ-010 | The probe MUST test interrupt/cancel terminal behavior and require success, failure, interruption, and cancellation events to persist before production default use. | Inspect probe notes and R1 acceptance mapping. | `docs/PLAN.md` R1; `docs/SPEC.md` Section 10.1 |
> | DEL-04-01-REQ-011 | The probe MUST test Electron packaging of the SDK subprocess and record any `asarUnpack`, signing, environment, or path residual risks. | Inspect packaging probe result and residual-risk notes. | `docs/PLAN.md` R0; `docs/PRD.md` KG-025 |
> | DEL-04-01-REQ-012 | The probe MUST verify API key environment handling: key material is supplied only as needed for active turns and redacted from logs/events. | Inspect probe notes for env handoff and redaction evidence. | `docs/SPEC.md` Section 12.3; `docs/PLAN.md` R1 |
> | DEL-04-01-REQ-013 | The adoption decision MUST define fallback triggers if SDK behavior cannot satisfy or verify product-critical boundaries. | Confirm fallback criteria exist and reference custom-runtime path. | `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` K-ENGINE-5; `docs/PLAN.md` R0 |
> | DEL-04-01-REQ-014 | The probe MUST not expose local tools to the model outside controlled validation. | Review probe setup and notes. | `docs/PLAN.md` R0; `docs/PRD.md` R0 |
> | DEL-04-01-REQ-015 | The decision MUST record residual risks for SDK API drift, settings leakage, allowed-tools misconception, transcript location, Electron packaging, SDK security boundary, subagent inherited permissions, session mirror reliability, product-identity drift, platform dependency, reliance-boundary ambiguity, and engine adapter lock-in. | Inspect residual-risk notes. | `docs/PRD.md` KG-021 through KG-032 |
>

### CLM-011 — Probe Evidence Thresholds

> ##### Probe Evidence Thresholds
>
> The first-adapter probe may remain `TBD` until implementation begins, but the final probe notes and adoption decision must contain the following evidence rows before the first-adapter path is accepted as a production default.
>
> | Evidence Area | Required Evidence Row(s) | Accept / TBD / Fallback Rule | Source |
> |---|---|---|---|
> | Version pin | Exact `@anthropic-ai/claude-agent-sdk` version, package manifest evidence, lockfile evidence, and Claude Code subprocess version where knowable. | `TBD` until the package and lockfile evidence exist; do not infer a version from roadmap text. | `docs/SPEC.md` Section 12.4; `docs/PLAN.md` R1 implementation targets |
> | Settings isolation | Shipped-like SDK options showing `settingSources: []`; negative evidence that `user` and `local` settings were not loaded; separate notation for any development-only `['project']` posture. | Failure to prove shipped `settingSources: []` is a fallback blocker or explicit residual-risk decision. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
> | Permission behavior | Rows for `allowedTools`, `disallowedTools`, `permissionMode`, `canUseTool`, hooks, and capability-policy and hard-deny precedence outcome. | Passing evidence must show `allowedTools` is not treated as a restriction boundary by itself and explicit denials fail closed. | `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` K-PERM-1 through K-PERM-3 |
> | Message mapping | Observed SDK `query()` message categories and sequence; mapping of each product-relevant message into stable `UIEvent` and `HarnessEvent` categories; unmapped categories with fallback or residual-risk treatment. | Adequate proof requires provider-neutral mapping without SDK names becoming public API or canonical persisted event fields. | `docs/SPEC.md` Sections 9 and 10.3; `docs/CONTRACT.md` K-ENGINE-4 |
> | Terminal outcomes | Success, failure, interruption, and cancellation evidence, including persisted terminal events and route/session cleanup behavior. | Production default use remains blocked until all required terminal outcomes persist or are explicitly carried as residual risk. | `docs/SPEC.md` Sections 10.1 and 11; `docs/PLAN.md` R1 acceptance |
> | API key handoff and redaction | Active-turn SDK environment handoff; redaction checks for logs, events, SDK transcripts if avoidable, provider errors, and tool artifacts. | Any persisted key material in project files, runtime events, logs, or artifacts is a blocker. | `docs/SPEC.md` Section 12.3; `docs/CONTRACT.md` K-KEY-1 |
> | Packaging | Packaged Electron app SDK turn result; subprocess/binary path behavior; `asarUnpack` or equivalent need; signing posture; environment handling; transcript/storage effect. | Packaging failure is fallback-blocking unless a human accepts a bounded residual-risk posture. | `docs/PLAN.md` Section 6.4; `docs/SPEC.md` Section 19.4 |
> | Decision authority | Human approver for `ADOPT`, `ADOPT_WITH_RESIDUAL_RISK`, or `FALLBACK`. | Ryan Tufts (K-AUTH-1) rendered `ADOPT_WITH_RESIDUAL_RISK` on 2026-07-19 through D-APP-68, demonstrator scope; `ResponsibleParty` remains TBD. | D-APP-65; D-APP-68 recommendation 8; `_CONTEXT.md` Identity |
>

### CLM-012 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Source |
> |---|---|---|
> | Chirality runtime engine contract | Defines product-owned boundary before SDK adapter can become production default. | `docs/SPEC.md` Section 10 |
> | Chirality runtime event schema | Defines canonical persisted event shape and required terminal categories. | `docs/SPEC.md` Section 9 |
> | SDK runtime configuration | Governs settings isolation, API key handoff, and metadata capture. | `docs/SPEC.md` Section 12 |
> | SDK tool surface and Chirality MCP rules | Governs tool names, MCP wrappers, and restriction boundary. | `docs/SPEC.md` Section 14 |
> | Permission modes and hooks | Governs provisional SDK posture, deny overlay, and required hooks. | `docs/SPEC.md` Section 15 |
> | Binding invariants | Governs SDK, engine, event, permission, filesystem, and release constraints. | `docs/CONTRACT.md` Sections 1.4 through 1.7 |
>

### CLM-013 — Verification

> ##### Verification
>
> | Verification ID | Check | Required Result |
> |---|---|---|
> | DEL-04-01-VER-001 | Version evidence check | Exact SDK package version is recorded, with lockfile/package evidence when implementation begins. |
> | DEL-04-01-VER-002 | Message sequence probe | SDK message categories used by Chirality are observed and mapped or flagged as fallback blockers. |
> | DEL-04-01-VER-003 | Settings isolation probe | Shipped posture proves `settingSources: []`; no user/local settings load. |
> | DEL-04-01-VER-004 | Permission probe | `allowedTools` is not mistaken for restriction; capability policy with explicit hard-deny precedence, hooks, and callbacks are evaluated. |
> | DEL-04-01-VER-005 | MCP probe | In-process MCP tooling can be exposed only through Chirality policy and event logging. |
> | DEL-04-01-VER-006 | Session/storage probe | SDK session ID, resume, transcript path/store key, `SessionStore`, and `CLAUDE_CONFIG_DIR` behavior are documented. |
> | DEL-04-01-VER-007 | Interrupt probe | Cancel/interrupt behavior preserves terminal outcomes and releases route/session control. |
> | DEL-04-01-VER-008 | Packaging probe | Packaged Electron runtime can start SDK-backed harness turn or records a fallback-blocking issue. |
> | DEL-04-01-VER-009 | Fallback decision review | Any failed P0 reliance boundary produces fallback or residual-risk action before R1 production default. |
> | DEL-04-01-VER-010 | Source-state check | REF-006 `docs/PRD.md` hash status: MATCH is resolved or explicitly accepted before closure. — reconciled under D-APP-38 |
> | DEL-04-01-VER-011 | Probe evidence completeness | Evidence rows listed in Probe Evidence Thresholds are present, or each missing row is marked `TBD` with fallback/residual-risk impact. |
>

### CLM-014 — Documentation

> ##### Documentation
>
> Required records:
>
> - first-adapter probe notes.
> - Version-pinned adoption decision.
> - Fallback criteria.
> - Residual-risk notes.
> - Source-state note for REF-006 `docs/PRD.md` hash status: MATCH. (reconciled under D-APP-38).
> - Traceability to SOW-018, SOW-044, SOW-046, OBJ-004, OI-001, and OI-002.
>
> Current records (D-APP-68 recommendation 8):
>
> - Decision: `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md` records `ADOPT_WITH_RESIDUAL_RISK`.
> - Versions: `@anthropic-ai/claude-agent-sdk@0.3.150`; observed Claude Code `2.1.150`.
> - Package evidence: `frontend/package.json` and `frontend/package-lock.json`.
> - Transcript treatment: SDK data under controlled `CLAUDE_CONFIG_DIR/projects/` is secondary adapter metadata; Chirality JSONL remains canonical.
> - Packaging treatment: unsigned local `darwin:arm64` proof under `app.asar.unpacked`; signing, notarization, distribution, release, and other platforms remain outside the evidence.
> - Approver/verdict: Ryan Tufts (K-AUTH-1), `ADOPT_WITH_RESIDUAL_RISK`, demonstrator scope, rendered through D-APP-68 on 2026-07-19. The D-APP-65 pre-ruling state—role assigned while the verdict remained a future owner act—is retained as dated history in `_CONTEXT.md` and `_STATUS.md`.

- **AC-001** — The DEL-04-01 evidence package records the first-adapter probe results and a version-pinned adoption decision, including provider/SDK message mapping, SDK session link and transcript placement, fallback triggers, future-provider criteria, and residual-risk notes, for SOW-018, SOW-044, SOW-046 and OBJ-004.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision

> #### Procedure: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-016 — Purpose

> ##### Purpose
>
> Define the operational steps to produce and verify the first-adapter probe notes, version-pinned adoption decision, fallback criteria, and residual-risk notes for DEL-04-01.
>
> This procedure is for producing the deliverable artifact. It does not authorize implementation of SDK-backed runtime code or exposure of new user-visible tools.
>

### CLM-017 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Note | Source |
> |---|---|---|
> | Accepted decomposition row for DEL-04-01 | Present in SOFTWARE_DECOMP v3.2. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
> | Source corpus | Accessible; `docs/PRD.md` has REF-006 `MATCH`. | `_REFERENCES.md` — reconciled under D-APP-38 |
> | Upstream dependencies | TBD: no accepted dependency edges have been extracted yet. | `_DEPENDENCIES.md` |
> | first-adapter probe environment | SDK `0.3.150`, Claude Code `2.1.150`, live development probe, and unsigned local `darwin:arm64` packaged Read proof are recorded; signing, notarization, distribution, release, and other platforms remain outside the evidence. | `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`; D-APP-68 recommendation 8 |
> | Runtime contract expectations | Required before SDK adapter production default. | `docs/SPEC.md` Section 10; `docs/PLAN.md` R1 |
> | Reliance-boundary expectations | Required for P0 boundaries and fallback decisions. | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-1 |
>

### CLM-018 — Steps

> ##### Steps
>
> 1. Confirm source-state before final closure.
>    - Re-check `_REFERENCES.md` and resolve or explicitly accept the REF-006 `docs/PRD.md` hash status: MATCH. (reconciled under D-APP-38).
>    - If unresolved, keep PRD-derived conclusions marked as draft/source-warning material.
>
> 2. Prepare the probe matrix.
>    - Include package version, `query()` message sequence, `settingSources`, permission mapping, `canUseTool`, hooks, in-process MCP, agents, resume, `SessionStore`, `CLAUDE_CONFIG_DIR`, interrupt behavior, Electron packaging, API key environment handling, branding/product identity, fallback triggers, and residual risks.
>    - Source: `docs/PLAN.md` R0 and `docs/PRD.md` R0.
>
> 3. Record version evidence.
>    - Capture exact `@anthropic-ai/claude-agent-sdk` version under evaluation.
>    - Capture package manifest and lockfile evidence location once implementation begins.
>    - Capture Claude Code subprocess version where knowable.
>    - Mark unknowns as `TBD`; do not infer a version from roadmap text.
>    - Source: `docs/SPEC.md` Section 12.4; `docs/CONTRACT.md` K-SDK-2.
>
> 4. Probe SDK message behavior.
>    - Run a controlled `query()` sequence in the intended adapter environment.
>    - Record observed message categories, ordering, terminal states, and error/interrupt behavior.
>    - Determine whether each required message can map to stable `UIEvent` and `HarnessEvent` contracts.
>    - Source: `docs/SPEC.md` Sections 9 and 10.3.
>
> 5. Probe settings isolation.
>    - Verify shipped-like options use `settingSources: []`.
>    - Verify `user` and `local` setting sources are not used in shipped builds.
>    - If development-only project settings are used, require explicit environment configuration.
>    - Record the evidence row location for shipped settings posture, negative user/local settings evidence, and any development-only project-setting posture.
>    - Source: `docs/SPEC.md` Section 12.2.
>
> 6. Probe permissions and tool exposure.
>    - Test `permissionMode`, `allowedTools`, `disallowedTools`, `canUseTool`, and hooks.
>    - Confirm that `allowedTools` is not treated as a restriction boundary.
>    - Confirm denied tools are blocked by policy, hooks, SDK deny rule, or human gate and are recorded before allowing/denying when applicable.
>    - Record one minimal evidence row per permission surface and one capability-policy and hard-deny precedence outcome row.
>    - Source: `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` K-PERM-1 through K-PERM-3.
>
> 7. Probe MCP and hook behavior.
>    - Test in-process Chirality MCP exposure only under controlled validation.
>    - Confirm MCP tools are not bypasses and remain subject to permission, hook, path, redaction, and event logging policy.
>    - Confirm required hooks for path containment, instruction-root protection, symlink write rejection, and write budget are feasible where applicable.
>    - Source: `docs/SPEC.md` Sections 14.2 and 15.2; `docs/CONTRACT.md` K-MCP-1.
>
> 8. Probe sessions, storage, transcripts, and resume.
>    - Record SDK session ID, resume mode, transcript path or store key, SDK config dir, `SessionStore`, and `CLAUDE_CONFIG_DIR` behavior.
>    - Prefer project-controlled transcript placement or mirroring when reliable.
>    - If SDK writes outside project-controlled storage, cross-reference the path or store key and record residual risk while keeping Chirality JSONL canonical.
>    - Source: `docs/SPEC.md` Sections 8.4 and 12.4.
>
> 9. Probe API key environment handling and redaction.
>    - Confirm key precedence and active-turn handoff behavior.
>    - Confirm key material is redacted from logs, events, SDK transcripts if avoidable, and tool artifacts.
>    - Source: `docs/SPEC.md` Section 12.3; `docs/CONTRACT.md` K-KEY-1.
>
> 10. Probe Electron packaging.
>     - Validate that a packaged build can start an SDK-backed harness turn.
>     - Record subprocess/binary execution path, `asarUnpack`, signing, environment, and transcript/storage effects.
>     - Record the residual-risk verdict if packaging works only with special path, signing, environment, or storage assumptions.
>     - Source: `docs/PRD.md` KG-025; `docs/PLAN.md` R0.
>
> 11. Draft the version-pinned adoption decision.
>     - State `ADOPT`, `ADOPT_WITH_RESIDUAL_RISK`, or `FALLBACK`.
>     - Current result: Ryan Tufts (K-AUTH-1) rendered `ADOPT_WITH_RESIDUAL_RISK` for the demonstrator through D-APP-68 on 2026-07-19; see `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`.
>     - Cite probe evidence for each P0 reliance boundary.
>     - Keep the SDK privileged as implementation substrate, not product identity or governance authority.
>     - Source: `docs/DIRECTIVE.md` Sections 2.8 through 2.11.
>
> 12. Draft fallback criteria and residual-risk notes.
>     - Include SDK API drift, settings leakage, allowed-tools misconception, transcript location, Electron packaging, SDK security boundary, subagent inherited permissions, session mirror reliability, product-identity drift, platform dependency, reliance-boundary ambiguity, and engine adapter lock-in.
>     - Source: `docs/PRD.md` KG-021 through KG-032.
>
> 13. Route downstream work.
>     - Send implementation requirements to DEL-04-02 through DEL-04-05 as appropriate.
>     - Keep this deliverable as the documentation/probe decision slice.
>     - Source: decomposition rows for PKG-04.
>

### CLM-019 — Verification

> ##### Verification
>
> | Check | Pass Criteria |
> |---|---|
> | Source-state check | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | Probe coverage | Every required probe topic from R0 has an evidence row or `TBD` blocker. |
> | Version pin | Exact SDK package version is recorded before adoption. |
> | Version evidence location | Package manifest and lockfile evidence location is recorded once implementation begins. |
> | Contract boundary | Decision states that SDK-specific identifiers remain adapter metadata and Chirality contracts stay product-owned. |
> | Settings isolation | Shipped posture uses `settingSources: []`. |
> | Permissions | Rows exist for `allowedTools`, `disallowedTools`, `permissionMode`, `canUseTool`, hooks, and explicit hard-deny precedence; `allowedTools` is not treated as restriction. |
> | Sessions/transcripts | SDK transcript/store linkage is recorded without replacing Chirality audit JSONL. |
> | Interrupts | Success, failure, interruption, and cancellation terminal behavior is evidenced or flagged. |
> | Packaging | Packaged app SDK turn is proven or recorded as fallback/residual risk. |
> | Fallback criteria | Any unverifiable P0 reliance boundary has an explicit fallback trigger. |
> | Adoption authority | PASS for the documentary decision: Ryan Tufts (K-AUTH-1) rendered `ADOPT_WITH_RESIDUAL_RISK` through D-APP-68 on 2026-07-19, demonstrator scope. This is not release, issuance, certification, professional acceptance, signing, notarization, publication, or external distribution. |
>

### CLM-020 — Records

> ##### Records
>
> Required records:
>
> - first-adapter probe matrix and notes.
> - Version-pinned adoption decision.
> - Fallback criteria.
> - Residual-risk notes.
> - Source-state warning or resolution for REF-006.
> - Traceability to SOW-018, SOW-044, SOW-046, OBJ-004, OI-001, and OI-002.
>
> Current decision records:
>
> - SDK version: `@anthropic-ai/claude-agent-sdk@0.3.150`.
> - Observed Claude Code version: `2.1.150`.
> - Package/lock evidence: `frontend/package.json`; `frontend/package-lock.json`.
> - Transcript/store treatment: controlled SDK transcript linkage is secondary adapter metadata; Chirality JSONL is canonical.
> - Electron result: live unsigned local `darwin:arm64` packaged Read proof with the binary under `app.asar.unpacked`; no release/distribution claim.
> - Verdict: `ADOPT_WITH_RESIDUAL_RISK` in `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`.
> - Approver: Ryan Tufts (K-AUTH-1), demonstrator scope, D-APP-68 recommendation 8.
>

### CLM-021 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-118 supersedes setup-era probe TBDs: the probe record, version/package pins, dependency register, and governed environment are landed.

- **VER-001** — Inspect the DEL-04-01 evidence package against SOW-018, SOW-044, SOW-046, OBJ-004, and the preserved legacy requirements to confirm the probe notes, pinned-version decision, mappings, transcript treatment, fallback and future-provider criteria, and residual-risk notes are present.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision

> #### Guidance: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-023 — Purpose

> ##### Purpose
>
> This deliverable creates the evidence package for deciding whether Chirality can adopt the Claude Agent SDK as a version-pinned, replaceable runtime substrate for R1. The decision must preserve Chirality-owned runtime contracts, audit records, settings isolation, permission semantics, transcript canonicality, product identity, and fallback control.
>
> Source grounding: `docs/DIRECTIVE.md` Section 2.8 through 2.11; `docs/PLAN.md` R0/R1; decomposition row for `DEL-04-01`.
>

### CLM-024 — Principles

> ##### Principles
>
> 1. Chirality contracts come first.
>    SDK APIs, message names, tool names, session IDs, and transcript paths are adapter metadata. `AgentEnginePort`, `UIEvent`, `HarnessEvent`, session storage, permission decisions, and governance records remain Chirality-owned. Sources: `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-5.
>
> 2. Probe before adoption.
>    R0 exists to validate SDK assumptions before R1 implementation details harden. The probe should produce a positive adoption decision only where behavior is observed, recorded, and compatible with conformance expectations. Sources: `docs/PLAN.md` R0; `docs/PRD.md` R0.
>
> 3. Product-critical reliance boundaries need enforceable surfaces.
>    Prompt text and opaque SDK defaults are insufficient for P0 audit, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundaries. Sources: `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-1 and K-RELIANCE-2.
>
> 4. Settings isolation is a release boundary.
>    Shipped SDK builds must use `settingSources: []`; user and local setting sources are not allowed in shipped builds. Source: `docs/SPEC.md` Section 12.2.
>
> 5. Permission restrictions require more than `allowedTools`.
>    `allowedTools` can auto-approve but is not by itself a restriction boundary. The probe should explicitly test deny rules, mode policy, hooks, and `canUseTool` behavior. Sources: `docs/SPEC.md` Section 14.3; `docs/CONTRACT.md` K-PERM-3.
>
> 6. SDK transcripts assist but do not govern.
>    SDK transcript placement and mirroring may support resume/debugging, but the Chirality audit JSONL remains canonical unless SDK content is imported into `HarnessEvent` form. Sources: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3.
>

### CLM-025 — Considerations

> ##### Considerations
>
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - The decomposition marks this as a documentation/probe slice with no new user tool exposure. Keep implementation changes out of this deliverable and route code work to downstream DEL-04-02 through DEL-04-05.
> - OI-001's empirical questions now have bounded D-APP-52 live and deterministic evidence; remaining limitations are carried explicitly in the twelve-area D-APP-68 residual-risk appraisal rather than treated as unknown results.
> - OI-002 is resolved for the demonstrator as cross-referenced SDK transcript placement under controlled `CLAUDE_CONFIG_DIR/projects/`, carried as secondary adapter metadata while Chirality JSONL remains canonical.
> - Packaging risk is not limited to the SDK package dependency. The probe must consider SDK subprocess/binary execution in Electron and any built-app path constraints.
> - D-APP-68 selected `ADOPT_WITH_RESIDUAL_RISK` for the demonstrator. If a product-critical reliance boundary cannot be observed, enforced, and recorded in Chirality terms, the fallback triggers in `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md` apply.
>

### CLM-026 — Trade-offs

> ##### Trade-offs
>
> | Decision Area | Prefer | Watch For | Source |
> |---|---|---|---|
> | Runtime mechanics | SDK handles generic model/tool loop when verified. | SDK defaults redefining product semantics. | `docs/DIRECTIVE.md` Section 2.8; `docs/PLAN.md` R0/R1 |
> | Event model | Chirality maps SDK messages into stable UI/runtime events. | Browser or persisted event contracts becoming SDK-shaped. | `docs/SPEC.md` Sections 9 and 10.3 |
> | Tool permissions | Capability-forward policy with explicit hard-deny precedence overlay with hooks and callbacks. | Mistaking `allowedTools` for restriction. | `docs/SPEC.md` Sections 14.3 and 15.1 |
> | Session storage | Project-controlled transcript/store linkage where reliable. | SDK default transcript path becoming de facto canonical. | `docs/SPEC.md` Section 8.4; `docs/PRD.md` KG-024 |
> | Settings | `settingSources: []` in shipped builds. | Ambient `.claude` or user/local settings entering product behavior. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
> | Adoption | Version-pinned SDK path with conformance tests. | SDK API drift, packaging failures, or unverifiable reliance boundaries. | `docs/CONTRACT.md` K-SDK-2; `docs/PRD.md` KG-021 through KG-032 |
>

### CLM-027 — Residual-Risk Appraisal Method

> ##### Residual-Risk Appraisal Method
>
> Residual-risk notes should evaluate each unresolved SDK adoption issue against three questions:
>
> 1. Can Chirality observe the behavior in project-owned records or adapter metadata?
> 2. Can Chirality enforce or fail closed at a product-owned boundary rather than relying on prompt text or opaque SDK defaults?
> 3. Can a human reviewer distinguish `ADOPT_WITH_RESIDUAL_RISK` from `FALLBACK` using version-pinned probe evidence?
>
> Apply the method to SDK API drift, settings leakage, allowed-tools misconception, transcript location, Electron packaging, SDK security boundary, subagent inherited permissions, session mirror reliability, product-identity drift, platform dependency, reliance-boundary ambiguity, and engine adapter lock-in. Sources: `docs/DIRECTIVE.md` Sections 2.8 through 2.11; `docs/CONTRACT.md` K-ENGINE-5, K-RELIANCE-1, K-RELIANCE-2, and K-SDK-2; `docs/PLAN.md` R0/R1 and Section 8.
>

### CLM-028 — Examples

> ##### Examples
>
> Completed live probe observations are recorded in `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`; the adopted assessment is recorded in `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`. The table below remains the evidence-row pattern used to evaluate the result.
>
> Example evidence rows the final probe notes should contain:
>
> | Probe Topic | Evidence to Capture | Accept / Fallback Question |
> |---|---|---|
> | SDK version | Package name, exact version, lockfile evidence, subprocess version when knowable. | Can this version be pinned and regression-tested? |
> | Messages | Observed message categories and sequence from `query()`. | Can all required categories map to stable `UIEvent` and `HarnessEvent` records? |
> | Settings | Effective `settingSources` behavior in shipped-like and dev-only modes. | Can shipped builds avoid ambient user/local settings? |
> | Permissions | Behavior of `permissionMode`, `allowedTools`, `disallowedTools`, `canUseTool`, and hooks. | Can capability policy with explicit hard-deny precedence be verified in Chirality terms? |
> | Session storage | SDK session ID, resume behavior, transcript path/store key, `SessionStore`, `CLAUDE_CONFIG_DIR`. | Can SDK transcripts remain secondary and traceable? |
> | Packaging | Built Electron app starts SDK-backed turn and can execute required subprocess/binary. | Does packaging require fallback or release blocker? |
>

### CLM-029 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | SRC-001 | `docs/PRD.md` is authoritative in role but `_REFERENCES.md` reports `MATCH`; content based on PRD should not be closed without source-state confirmation. | `_REFERENCES.md` REF-006 | `docs/PRD.md` R0/R1 and KG-021 through KG-032 | Datasheet References; Specification Requirements and Verification; Guidance Considerations | Use corroborated PRD claims as draft context where they match MATCH sources; require human/source refresh before closure. | TBD — reconciled under D-APP-38 |
>

### CLM-030 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-118 supersedes setup-era probe TBDs: the probe record, version/package pins, dependency register, and governed environment are landed.

### CLM-031 — D-APP-68 version-pinned adoption verdict (2026-07-19)

> ##### D-APP-68 version-pinned adoption verdict (2026-07-19)
>
> Ryan Tufts (K-AUTH-1) rendered `ADOPT_WITH_RESIDUAL_RISK` for this
> repository's demonstrator, pinned to `@anthropic-ai/claude-agent-sdk@0.3.150`
> and observed Claude Code `2.1.150`. The decision and its twelve residual-risk
> assessments are in `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`.
> The D-APP-65 state in which the approving role was assigned but the verdict
> remained a future owner act is dated pre-ruling history. The verdict grants
> no release approval, issuance, certification, professional acceptance,
> signing, notarization, publication, or external distribution.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-018 SOW-044 SOW-046 OBJ-004 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
