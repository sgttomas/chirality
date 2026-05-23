# Datasheet: DEL-04-01 SDK Probe and Version-Pinned Adoption Decision

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-04-01 |
| Deliverable Name | SDK Probe and Version-Pinned Adoption Decision |
| Package | PKG-04 SDK Adapter, Prompt, Provider, and Settings |
| Decomposition Variant | SOFTWARE_DECOMP v3.2 |
| Type | REQ_SLICE |
| Context Envelope | M |
| Responsible Party | TBD |
| Scope Items | SOW-018, SOW-044, SOW-046 |
| Objective | OBJ-004 |
| Anticipated Artifacts | SDK probe notes; version decision; fallback criteria; residual-risk notes |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Runtime direction | Claude Agent SDK is the preferred runtime spine only if empirical verification and conformance tests preserve Chirality-owned governance. | `docs/SPEC.md` Section 12.1; `docs/DIRECTIVE.md` Section 2.8 |
| Product boundary | Chirality owns `AgentEnginePort` / `RuntimeEngineContract`, browser `UIEvent`s, persisted `HarnessEvent`s, session canonicality, permission semantics, working-root/instruction-root policy, prompt/persona composition, redaction, provenance, and fallback criteria. | `docs/DIRECTIVE.md` Section 2.8; `docs/SPEC.md` Section 10 |
| Probe purpose | Validate SDK assumptions before R1 implementation details harden and make adoption a replaceable engine choice, not product identity. | `docs/PLAN.md` R0; `docs/PRD.md` R0 |
| Required probe topics | Package version, `query()` message sequence, `settingSources`, permission mapping, `canUseTool`, hooks, in-process MCP, agents, resume, `SessionStore`, `CLAUDE_CONFIG_DIR`, interrupt behavior, Electron packaging, API key environment handling, branding constraints, and fallback triggers. | `docs/PLAN.md` R0; `docs/PRD.md` R0 |
| Required metadata to capture | SDK package version; Claude Code subprocess version when knowable; SDK permission mode; visible tool list; MCP server names; settings-source posture; SDK session ID and resume mode; transcript/store linkage. | `docs/SPEC.md` Section 12.4 |
| Adoption decision state | TBD: no probe result or pinned SDK version is present in the accessible source corpus. | Source gap from `_REFERENCES.md` corpus |

## Conditions

| Condition | Current Value | Source |
|---|---|---|
| Shipped settings isolation | `settingSources: []` is required for shipped SDK builds. | `docs/SPEC.md` Section 12.2; `docs/PLAN.md` R1; `docs/PRD.md` R1 |
| Development settings posture | Development-only project settings may use `['project']` behind explicit environment configuration; `user` and `local` setting sources must not be used in shipped builds. | `docs/SPEC.md` Section 12.2 |
| Transcript canonicality | SDK transcripts are secondary runtime state unless imported into `HarnessEvent` form; Chirality JSONL remains canonical. | `docs/SPEC.md` Sections 8.4 and 10.3; `docs/CONTRACT.md` K-SDK-3 |
| Tool restriction boundary | `allowedTools` is not a restriction boundary by itself; restrictions require deny policy, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture. | `docs/SPEC.md` Section 14.3; `docs/CONTRACT.md` K-PERM-3 |
| Permission overlay | Deny overrides allow, including policy, hooks, SDK deny rule, or human gate denials. | `docs/CONTRACT.md` K-PERM-1 |
| Probe exposure | R0 acceptance requires no local tools exposed to the model during the probe outside controlled validation. | `docs/PLAN.md` R0; `docs/PRD.md` R0 |
| Source-state warning | `docs/PRD.md` is accessible but `_REFERENCES.md` records `HASH_MISMATCH`; claims citing PRD require snapshot confirmation before closure. | `_REFERENCES.md` REF-006 |

## Construction

This deliverable is a requirements/probe decision package, not runtime code. It should be constructed as:

1. SDK probe notes that record empirical behavior for every required probe topic.
2. A version-pinned adoption decision identifying the exact `@anthropic-ai/claude-agent-sdk` version and any Claude Code subprocess version when knowable.
3. Fallback criteria that preserve the custom-runtime roadmap if a product-critical boundary cannot be satisfied or verified.
4. Residual-risk notes for SDK API drift, settings leakage, transcript location, packaging, permissions, subagents, and product-identity drift.

ASSUMPTION: The final artifact format may be Markdown under `docs/harness/` because R0 deliverables named in `docs/PLAN.md` and `docs/PRD.md` are documentation artifacts, but the exact file name for this probe decision is TBD.

## References

| RefID | Source | Status | Used For |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | MATCH | Product boundary, reliance boundaries, provider-neutrality, product identity |
| REF-002 | `docs/CONTRACT.md` | MATCH | Binding invariants for SDK governance, permissions, events, settings, transcripts |
| REF-003 | `docs/SPEC.md` | MATCH | Runtime contract, session/event schema, SDK configuration, tool surface, hooks |
| REF-004 | `docs/TYPES.md` | MATCH | Vocabulary for engine, SDK metadata, tools, hooks, MCP, events |
| REF-005 | `docs/PLAN.md` | MATCH | R0/R1 sequencing, probe deliverables, acceptance criteria |
| REF-006 | `docs/PRD.md` | HASH_MISMATCH | Product requirements and runtime direction; use requires source-state confirmation |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | MATCH | Decomposition method context only |
