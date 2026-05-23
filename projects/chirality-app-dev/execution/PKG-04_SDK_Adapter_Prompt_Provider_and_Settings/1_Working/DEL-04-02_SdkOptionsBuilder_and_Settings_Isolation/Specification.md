# Specification: DEL-04-02 SdkOptionsBuilder and Settings Isolation

## Scope

This deliverable specifies the `SdkOptionsBuilder` backend feature slice for constructing deterministic Claude Agent SDK options from Chirality-owned runtime state and policy. It covers:

- runtime option fallback resolution for model, tools, max turns, mode, and persona;
- shipped SDK settings isolation;
- registered SDK built-in and Chirality MCP tool option mapping;
- safe visible metadata for tool/settings posture;
- max-turn option propagation;
- tests for settings isolation and options/tool mapping.

Exclusions:

- `PersonaComposer` content assembly is owned by DEL-04-04, though this builder consumes its output.
- SDK message to `UIEvent`/`HarnessEvent` mapping is owned by DEL-04-03.
- provider key/base URL handoff is owned by DEL-04-05.
- full permission overlay, hooks, write/bash enablement, and subagent execution gates deepen in PKG-06 and PKG-08; this deliverable must accept policy inputs without weakening those later boundaries.
- Chirality event-store internals beyond safe metadata handoff are outside PKG-04 scope.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-02; `docs/SPEC.md` Sections 12-15.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-04-02-REQ-001 | The builder MUST resolve runtime option fallback chains deterministically for model, tools, max turns, mode, and persona. | SOW-016; `docs/SPEC.md` Section 13.1; `docs/PRD.md` Section 8.4, HASH_MISMATCH |
| DEL-04-02-REQ-002 | Unknown option keys MUST be ignored with warnings rather than silently mutating behavior. | SOW-016; `docs/SPEC.md` Section 13.1; `docs/PRD.md` Section 8.4, HASH_MISMATCH |
| DEL-04-02-REQ-003 | Shipped SDK options MUST use `settingSources: []`. | SOW-045; `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| DEL-04-02-REQ-004 | Development-only project settings MAY use `['project']` only behind explicit environment configuration; `user` and `local` sources MUST NOT be used in shipped builds. | `docs/SPEC.md` Section 12.2; `docs/PRD.md` Section 8.12, HASH_MISMATCH |
| DEL-04-02-REQ-005 | `opts.tools` MUST map only to registered SDK built-ins or Chirality MCP tools; unknown names MUST produce structured validation errors. | SOW-047; `docs/SPEC.md` Section 14.3; `docs/PRD.md` Section 8.13, HASH_MISMATCH |
| DEL-04-02-REQ-006 | Tool ordering, naming, MCP server IDs, and allow/deny option lists MUST be stable for a given session, persona, mode, option set, SDK version, MCP server set, and permission policy. | `docs/CONTRACT.md` K-TOOL-1; `docs/PRD.md` Section 8.13, HASH_MISMATCH |
| DEL-04-02-REQ-007 | The builder MUST NOT treat `allowedTools` alone as a restriction boundary. Restriction posture MUST include deny rules, mode policy, hooks, `canUseTool`, and/or `dontAsk` where applicable. | `docs/CONTRACT.md` K-PERM-3; `docs/SPEC.md` Section 14.3 |
| DEL-04-02-REQ-008 | Resolved `maxTurns` MUST be included in SDK options so max-turn guards can stop runaway loops and terminal max-turn errors can be persisted by runtime/event layers. | SOW-052; `docs/PRD.md` Section 8.13, HASH_MISMATCH |
| DEL-04-02-REQ-009 | The builder MUST preserve Chirality-owned semantics by keeping SDK-specific names and option details at adapter boundaries and safe metadata surfaces, not public API contracts. | `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-4; `docs/TYPES.md` Section 9 |
| DEL-04-02-REQ-010 | Safe visible metadata SHOULD include SDK package version, SDK permission mode, visible tool list, MCP server names, settings-source posture, SDK session ID/resume mode, and transcript/store linkage where available. | `docs/SPEC.md` Section 12.4 |
| DEL-04-02-REQ-011 | API keys and secrets MUST NOT be written to project files or included in visible metadata produced by this builder. | `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` Section 10.3.1, HASH_MISMATCH |
| DEL-04-02-REQ-012 | Exact SDK option property names beyond cited source text are TBD until the SDK probe/version decision confirms current TypeScript APIs. | `docs/PLAN.md` R0; `docs/PRD.md` KG-021, HASH_MISMATCH |
| DEL-04-02-REQ-013 | The builder input contract MUST either define or explicitly import the owning adjacent contract for session state, persona output, hook policy, MCP server descriptors, subagent descriptors, resume linkage, and settings policy before the exact TypeScript shape is treated as closed. | `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` Section 4, HASH_MISMATCH; `execution/_Decomposition/...` DEL-04-01 through DEL-04-05 |
| DEL-04-02-REQ-014 | Before constructing SDK options, the builder MUST fail closed or return a structured integration error when required governed policy inputs for settings, tools, permission posture, hooks, MCP, or subagents are absent or explicitly unresolved. | `docs/CONTRACT.md` K-RELIANCE-2, K-PERM-1 through K-PERM-3, K-MCP-1, K-HOOK-1; `docs/PLAN.md` R2 |

## Standards

| Standard or Contract | Application | Source |
|---|---|---|
| Chirality `AgentEnginePort` / `RuntimeEngineContract` | SDK options are constructed behind a product-owned engine boundary. | `docs/CONTRACT.md` K-ENGINE-1; `docs/SPEC.md` Section 11; `docs/PRD.md` Section 8.12, HASH_MISMATCH |
| SDK settings isolation | Shipped runtime must not load ambient user/global Claude Code settings or local `.claude/settings.local.json`. | `docs/CONTRACT.md` K-SDK-1; `docs/SPEC.md` Section 12.2 |
| Deny-first permission policy | Builder must carry policy posture without confusing auto-approval with restriction. | `docs/CONTRACT.md` K-PERM-1 through K-PERM-6 |
| Chirality MCP naming | Chirality tools use `mcp__chirality__*` names. | `docs/SPEC.md` Section 14.2; `docs/TYPES.md` Section 8.4 |
| Epistemic controls | Unknown implementation details remain `TBD` rather than invented. | `docs/CONTRACT.md` K-INVENT-1; `docs/DIRECTIVE.md` Section 2.5 |

## Verification

| Verification ID | Requirement Links | Verification Approach | Expected Evidence |
|---|---|---|---|
| DEL-04-02-VER-001 | REQ-001, REQ-002 | Unit tests for model/tool/maxTurns/mode/persona fallback order and unknown-key warnings. | Options-builder test fixtures assert warning emission and identical resolved SDK behavior when unknown option keys are added to otherwise identical inputs. |
| DEL-04-02-VER-002 | REQ-003, REQ-004 | Settings isolation tests for shipped default, explicit development project opt-in, and forbidden setting-source cases. | Fixtures cover shipped `settingSources: []`, development-only `['project']` behind explicit environment configuration, and rejection/exclusion of `user` and `local` sources in shipped posture. |
| DEL-04-02-VER-003 | REQ-005, REQ-006, REQ-007, REQ-014 | Composite tool/policy mapping tests for registered built-ins, registered Chirality MCP names, deterministic ordering, unknown-name errors, MCP server IDs, allow/deny lists, and permission policy inputs. | One deterministic-order fixture includes requested tools, visible tools, MCP server IDs, `allowedTools`, `disallowedTools`, permission mode, hook/callback posture, and structured validation errors. |
| DEL-04-02-VER-004 | REQ-007, REQ-014 | Tests or static checks proving `allowedTools` is not the sole restriction mechanism for restricted modes. | Fixture showing deny/disallowed/hook/callback posture included or required before option construction proceeds. |
| DEL-04-02-VER-005 | REQ-008 | Max-turn option propagation test and terminal max-turn handoff fixture. | SDK options fixture plus runtime event handoff fixture location TBD; likely adjacent owner is DEL-04-03 or DEL-03-02 pending accepted integration contract. |
| DEL-04-02-VER-006 | REQ-009, REQ-010, REQ-011 | Metadata-shape and redaction review confirming SDK details are adapter metadata and safe runtime metadata only. | Single metadata fixture proves safe fields are present and API keys, raw secrets, hidden user settings content, and public product-version claims are absent. |
| DEL-04-02-VER-007 | REQ-011 | Redaction/secret exclusion test for builder output and visible metadata. | Fixture with API-key-like input verifies no secret output in project files, visible metadata, or runtime records owned by this slice. |
| DEL-04-02-VER-008 | REQ-012, REQ-013 | SDK probe/typecheck after package pin and adjacent-contract import review. | Probe notes, TypeScript compile evidence from DEL-04-01 or R1 implementation, and source-backed references for any imported persona/session/hook/MCP/settings policy types. |

## Documentation

Required artifacts:

- `sdk-options-builder.ts` or equivalent module path selected by implementation owner.
- Unit tests for fallback chains, unknown keys, settings isolation, tool mapping, deterministic ordering, max-turn propagation, and visible metadata.
- Safe visible tool/settings metadata fixture.
- Notes in implementation comments or local docs for any SDK option whose exact TypeScript shape depends on the accepted SDK probe.

Open documentation items:

- TBD: exact module path and exported TypeScript API.
- TBD: target test command or validation suite for this module after implementation path is selected.
- TBD: exact structured error type for unknown tools.
- TBD: exact integration point with `PersonaComposer`, `TurnEngine`, and PKG-06 permission overlay.
- TBD: exact SDK package version and option names confirmed by DEL-04-01 probe.
