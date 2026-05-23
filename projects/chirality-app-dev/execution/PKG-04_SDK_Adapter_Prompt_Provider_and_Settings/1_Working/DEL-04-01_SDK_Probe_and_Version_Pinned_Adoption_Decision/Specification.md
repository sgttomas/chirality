# Specification: DEL-04-01 SDK Probe and Version-Pinned Adoption Decision

## Scope

This deliverable specifies the evidence required to decide whether Chirality should adopt a version-pinned Claude Agent SDK runtime path for R1.

Included:

- Confirm the SDK package version and Claude Code subprocess version when knowable.
- Probe `query()` message sequence, permissions, hooks, in-process MCP, sessions, storage, interrupts, packaging, settings isolation, API key handoff, and fallback triggers.
- Preserve Chirality-owned runtime semantics for `AgentEnginePort` / `RuntimeEngineContract`, `UIEvent`, `HarnessEvent`, session metadata, permission decisions, redaction, prompt composition, and product identity.
- Produce SDK probe notes, version decision, fallback criteria, and residual-risk notes.

Excluded:

- Implementing `SdkOptionsBuilder`, `SdkMessageMapper`, `TurnEngine`, provider key bridge, or prompt composer code.
- Exposing new user-visible write, bash, remote MCP, plugin, domain-operation, or subagent execution capability.
- Treating SDK transcripts or SDK message names as canonical Chirality contracts.

Sources: `_CONTEXT.md`; decomposition row for `DEL-04-01`; `docs/PLAN.md` R0/R1; `docs/PRD.md` R0/R1 with REF-006 hash warning.

## Requirements

| Req ID | Requirement | Verification | Source |
|---|---|---|---|
| DEL-04-01-REQ-001 | The probe notes MUST record the exact `@anthropic-ai/claude-agent-sdk` package version selected for evaluation and the Claude Code subprocess version when knowable. | Inspect probe record and package/version evidence. | `docs/SPEC.md` Section 12.4; `docs/PLAN.md` R0 |
| DEL-04-01-REQ-002 | The adoption decision MUST remain version-pinned and regression-tested on upgrade. | Confirm version decision identifies pin and upgrade test expectation. | `docs/CONTRACT.md` K-SDK-2; `docs/PRD.md` KG-021 |
| DEL-04-01-REQ-003 | The probe MUST capture SDK `query()` message sequence and determine whether known SDK messages can map to stable `UIEvent`s and provider-neutral `HarnessEvent`s. | Compare probe notes to event mapping acceptance criteria. | `docs/PLAN.md` R0/R1; `docs/SPEC.md` Sections 9 and 10.3 |
| DEL-04-01-REQ-004 | The decision MUST not accept SDK-specific message names, permission modes, transcript paths, tool names, or session IDs as public API or canonical event fields except as adapter metadata. | Review adoption decision and residual risks for provider-neutral boundary. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-ENGINE-4 |
| DEL-04-01-REQ-005 | The probe MUST verify shipped settings isolation using `settingSources: []`; any development `['project']` use must be explicit and non-shipped. | Inspect probe result and planned settings tests. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| DEL-04-01-REQ-006 | The probe MUST test permission behavior, including `allowedTools`, `disallowedTools`, `permissionMode`, `canUseTool`, hooks, and deny-first overlay implications. | Inspect probe notes for each permission surface and a restriction-boundary conclusion. | `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` K-PERM-1 through K-PERM-3 |
| DEL-04-01-REQ-007 | The probe MUST test in-process Chirality MCP feasibility without treating MCP as a bypass around permission, hooks, path policy, redaction, or event logging. | Confirm probe notes cover MCP transport and wrapper policy expectations. | `docs/SPEC.md` Section 14.2; `docs/CONTRACT.md` K-MCP-1 |
| DEL-04-01-REQ-008 | The probe MUST capture SDK session ID, resume behavior, transcript/store linkage, `SessionStore`, and `CLAUDE_CONFIG_DIR` behavior. | Inspect session/storage section of probe notes and residual-risk register. | `docs/SPEC.md` Sections 8.4 and 12.4; `docs/PRD.md` KG-024 and KG-028 |
| DEL-04-01-REQ-009 | The decision MUST keep `.chirality/sessions/<id>/events.jsonl` or a configured Chirality-controlled session path as the canonical audit mirror. | Review adoption decision for transcript canonicality statement. | `docs/DIRECTIVE.md` Section 2.4; `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4 |
| DEL-04-01-REQ-010 | The probe MUST test interrupt/cancel terminal behavior and require success, failure, interruption, and cancellation events to persist before production default use. | Inspect probe notes and R1 acceptance mapping. | `docs/PLAN.md` R1; `docs/SPEC.md` Section 10.1 |
| DEL-04-01-REQ-011 | The probe MUST test Electron packaging of the SDK subprocess and record any `asarUnpack`, signing, environment, or path residual risks. | Inspect packaging probe result and residual-risk notes. | `docs/PLAN.md` R0; `docs/PRD.md` KG-025 |
| DEL-04-01-REQ-012 | The probe MUST verify API key environment handling: key material is supplied only as needed for active turns and redacted from logs/events. | Inspect probe notes for env handoff and redaction evidence. | `docs/SPEC.md` Section 12.3; `docs/PLAN.md` R1 |
| DEL-04-01-REQ-013 | The adoption decision MUST define fallback triggers if SDK behavior cannot satisfy or verify product-critical boundaries. | Confirm fallback criteria exist and reference custom-runtime path. | `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` K-ENGINE-5; `docs/PLAN.md` R0 |
| DEL-04-01-REQ-014 | The probe MUST not expose local tools to the model outside controlled validation. | Review probe setup and notes. | `docs/PLAN.md` R0; `docs/PRD.md` R0 |
| DEL-04-01-REQ-015 | The decision MUST record residual risks for SDK API drift, settings leakage, allowed-tools misconception, transcript location, Electron packaging, SDK security boundary, subagent inherited permissions, session mirror reliability, product-identity drift, platform dependency, reliance-boundary ambiguity, and engine adapter lock-in. | Inspect residual-risk notes. | `docs/PRD.md` KG-021 through KG-032 |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Chirality runtime engine contract | Defines product-owned boundary before SDK adapter can become production default. | `docs/SPEC.md` Section 10 |
| Chirality runtime event schema | Defines canonical persisted event shape and required terminal categories. | `docs/SPEC.md` Section 9 |
| SDK runtime configuration | Governs settings isolation, API key handoff, and metadata capture. | `docs/SPEC.md` Section 12 |
| SDK tool surface and Chirality MCP rules | Governs tool names, MCP wrappers, and restriction boundary. | `docs/SPEC.md` Section 14 |
| Permission modes and hooks | Governs provisional SDK posture, deny overlay, and required hooks. | `docs/SPEC.md` Section 15 |
| Binding invariants | Governs SDK, engine, event, permission, filesystem, and release constraints. | `docs/CONTRACT.md` Sections 1.4 through 1.7 |

## Verification

| Verification ID | Check | Required Result |
|---|---|---|
| DEL-04-01-V-001 | Version evidence check | Exact SDK package version is recorded, with lockfile/package evidence when implementation begins. |
| DEL-04-01-V-002 | Message sequence probe | SDK message categories used by Chirality are observed and mapped or flagged as fallback blockers. |
| DEL-04-01-V-003 | Settings isolation probe | Shipped posture proves `settingSources: []`; no user/local settings load. |
| DEL-04-01-V-004 | Permission probe | `allowedTools` is not mistaken for restriction; deny-first overlay, hooks, and callbacks are evaluated. |
| DEL-04-01-V-005 | MCP probe | In-process MCP tooling can be exposed only through Chirality policy and event logging. |
| DEL-04-01-V-006 | Session/storage probe | SDK session ID, resume, transcript path/store key, `SessionStore`, and `CLAUDE_CONFIG_DIR` behavior are documented. |
| DEL-04-01-V-007 | Interrupt probe | Cancel/interrupt behavior preserves terminal outcomes and releases route/session control. |
| DEL-04-01-V-008 | Packaging probe | Packaged Electron runtime can start SDK-backed harness turn or records a fallback-blocking issue. |
| DEL-04-01-V-009 | Fallback decision review | Any failed P0 reliance boundary produces fallback or residual-risk action before R1 production default. |
| DEL-04-01-V-010 | Source-state check | REF-006 `docs/PRD.md` hash mismatch is resolved or explicitly accepted before closure. |

## Documentation

Required records:

- SDK probe notes.
- Version-pinned adoption decision.
- Fallback criteria.
- Residual-risk notes.
- Source-state note for REF-006 `docs/PRD.md` hash mismatch.
- Traceability to SOW-018, SOW-044, SOW-046, OBJ-004, OI-001, and OI-002.

TBD:

- Final document file path for the SDK probe decision.
- Exact SDK version and subprocess version.
- Exact transcript storage decision: `SessionStore`, `CLAUDE_CONFIG_DIR`, both, or cross-reference default path as residual risk.
- Exact packaging requirements discovered by the probe.
