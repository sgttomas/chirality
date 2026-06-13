# SCA-APP-001 Amendment Preview

**Package Role:** snapshot / handoff artifact
**Gate:** 3 - Amendment Approval
**Status:** PREVIEW_PENDING_HUMAN_APPROVAL

This file previews exact amendment intent. It does not apply changes to decomposition truth or governed docs.

## Decomposition Amendments

### Section 2.2 - v3.2 Revision Posture

Current invariant:

```text
no implementation work that exposes write, bash, subagent execution, remote MCP, plugins, or domain operations ahead of PLAN sequencing;
```

Proposed replacement:

```text
no implementation work that exposes write, bash, subagent execution, remote MCP, plugins, unvalidated provider/network expansion, or domain operations ahead of the approved provider-adapter and capability-policy sequencing;
```

### Section 3 - Intake Summary

Current strategic paragraph:

```text
The approved runtime direction is SDK-privileged, contract-owned, and Chirality-governed. The Claude Agent SDK is the preferred engine for generic agent-loop mechanics, but Chirality owns the runtime contract, permission semantics, audit mirror, filesystem boundaries, persona composition, professional boundaries, and fallback criteria.
```

Proposed replacement:

```text
The approved runtime direction is provider-adapter-general, contract-owned, and Chirality-governed. Chirality owns the runtime contract, permission semantics, audit mirror, filesystem boundaries, persona composition, professional boundaries, and fallback criteria. External provider SDKs may supply agent-loop mechanics only behind Chirality adapters. The Claude Agent SDK / Anthropic path remains the first concrete adapter and current shipped path; concrete non-Anthropic adapters require bounded future implementation tranches and validation.
```

Current implementation objective paragraph:

```text
The next implementation objective is to mature the existing desktop shell into a governed runtime by establishing `AgentEnginePort` / `RuntimeEngineContract`, SDK conformance, SDK-backed `TurnEngine`, append-only `HarnessEvent` JSONL, prompt/persona composition, settings isolation, run logging, and a reliance-boundary register before expanding read tools, writes, bash, subagents, or domain-engine profiles.
```

Proposed replacement:

```text
The next implementation objective is to mature the existing desktop shell into a governed provider-adapter runtime by establishing `AgentEnginePort` / `RuntimeEngineContract`, adapter conformance, the first Claude Agent SDK / Anthropic-backed `TurnEngine`, append-only `HarnessEvent` JSONL, prompt/persona composition, settings isolation, run logging, and a reliance-boundary register before expanding read tools, writes, bash, subagents, concrete non-Anthropic providers, or domain-engine profiles.
```

### Section 3 - Hard Constraints Captured

Proposed row-level edits:

| Current | Proposed |
|---|---|
| R0/R1 runtime contract and SDK adoption remain the immediate implementation slice. | R0/R1 runtime contract, provider-adapter architecture, and the first Claude Agent SDK / Anthropic adapter remain the immediate implementation slice. |
| `allowedTools` alone is not a restriction boundary. | Tool availability alone is not a restriction boundary; exposure requires capability policy, explicit deny precedence, hooks where needed, and evidence records. |
| Write, bash, subagent, remote MCP, plugin, and domain-operation capabilities remain gated until governance deliverables pass validation. | Write, bash, subagent, remote MCP, plugin, concrete non-Anthropic provider, and domain-operation capabilities remain gated until their governance and validation deliverables pass. |
| P0 reliance boundaries must be enforced by Chirality code, verified SDK callbacks/hooks, deterministic tools, release checks, or human gates; prompt text alone is insufficient. | P0 reliance boundaries must be enforced by Chirality code, verified adapter callbacks/hooks, deterministic tools, release checks, or human gates; prompt text alone is insufficient. |

Add hard constraint:

```text
Pi is a pattern corpus / reference source only. This amendment authorizes no Pi adapter, fork, direct package import, Node 22 sidecar, runtime-floor change, or immediate Pi spike.
```

Add hard constraint:

```text
Permission governance is capability-forward and policy-mediated. Useful agent tool use is enabled when allowed by mode, boundary policy, evidence capture, and human gates. Explicit hard denies override allows at reliance boundaries, secrets, protected paths, release/professional claims, destructive actions, and unvalidated provider/network expansion.
```

### Section 4 - Vocabulary Map

Proposed additions / modifications:

| Term | Proposed definition |
|---|---|
| EngineAdapter | Provider or SDK adapter behind Chirality-owned contracts. Provider-specific terms, events, sessions, permission modes, and tool names are translated at this boundary. |
| Provider Adapter | Concrete integration layer for an external agent provider or SDK. The current shipped concrete adapter is Claude Agent SDK / Anthropic. |
| Pi Pattern Corpus | Reference corpus for stable agentic patterns observed in Pi packages and behavior. It is not a runtime dependency, adapter target, fork target, or package import path. |
| Capability Policy | Chirality policy that decides which tools/capabilities are exposed and executable for a session, persona, mode, provider adapter, and validation state. |
| Explicit Deny Precedence | A hard-deny rule that overrides allows at defined reliance, secret, protected-path, professional, destructive-action, or unvalidated expansion boundaries. This replaces blanket "deny-first" as the governing posture. |

### Section 7 - Packages

Proposed package description changes:

| Package | Proposed description adjustment |
|---|---|
| PKG-04 | Interpret the package as provider-adapter, prompt, first-adapter SDK, provider, and settings work. Keep the current package ID and folder path; no rename is required in this SCA. |
| PKG-06 | Replace "deny-first permission overlay" with "capability-forward permission policy with explicit deny precedence, tool exposure, MCP wrappers, hooks, writes, bash, and compaction hooks." |
| PKG-09 | Add validation responsibility for provider-adapter conformance and no unauthorized provider/network expansion. |

### Section 8 - Deliverables

Proposed deliverable description changes:

| Deliverable | Proposed adjustment |
|---|---|
| DEL-04-01 | Probe provider-adapter viability and Claude Agent SDK / Anthropic as first concrete adapter; record fallback and future-provider criteria. |
| DEL-04-02 | Build deterministic adapter options from session, persona, mode, tools, hooks, MCP, subagents, resume, and settings policy. |
| DEL-04-03 | Translate provider/SDK stream messages into stable `UIEvent`s and provider-neutral `HarnessEvent`s. |
| DEL-04-05 | Preserve API key precedence, current Anthropic network policy, provider error classification, and redacted adapter environment handoff for the current shipped path. |
| DEL-06-01 | Implement structured permission decisions, explicit deny precedence, capability-policy mode mapping, and `canUseTool` approval mediation. |
| DEL-06-02 | Resolve requested tools to provider/SDK built-ins or Chirality MCP names while preserving read-before-write rollout. |
| DEL-06-05 | Keep Bash unavailable unless explicitly enabled by a governed mode and validated timeout/capture/output/audit behavior. |
| DEL-09-02 | Add runtime validation IDs for provider-adapter conformance, first-adapter mapper, event log, settings isolation, permissions, MCP, hooks, compaction, and subagents. |
| DEL-09-06 | Verify renderer allowlist, API key redaction/storage, current provider endpoint policy, and no unauthorized provider/network expansion. |

### Section 9 - Scope Ledger

Proposed row text edits:

| SOW | Proposed change |
|---|---|
| SOW-018 | Change "SDK-backed Anthropic runtime path" to "Provider-adapter runtime path with Claude Agent SDK / Anthropic as first concrete adapter." |
| SOW-020 | Change "Base URL and network allowlist" to "Provider endpoint and network allowlist for current shipped adapter; concrete provider expansion requires bounded future tranche." |
| SOW-044 | Change "SDK message mapping" to "Provider/SDK message mapping into Chirality contracts." |
| SOW-045 | Change "SDK settings isolation" to "Provider/SDK settings isolation, with Claude Agent SDK settings isolation required for the current shipped adapter." |
| SOW-050 | Preserve "Read tools before writes/bash" as rollout sequencing, not a blanket denial of useful tool use. |
| SOW-055 | Change "Permission modes and deny-first overlay" to "Permission modes, capability policy, and explicit deny precedence." |
| SOW-062 | Preserve Bash as denied until explicitly governed and validated, without using Bash as a reason to suppress unrelated read/tool capability. |
| SOW-063 | Governed subagent runtime remains future-gated and provider-adapter-aware. |
| SOW-064 | MCP extension boundaries remain governed and cannot bypass adapter/permission/hook policy. |

### Section 10A - Non-PRD Control Coverage

Proposed coverage edits:

- Replace "SDK isolation, conformance, fallback" with "provider/SDK adapter isolation, first-adapter conformance, fallback."
- Replace "Deny-first policy" with "capability policy with explicit deny precedence."
- Add provider/network expansion checks under `K-NET`, `K-KEY`, `K-RELEASE`, and `K-VALIDATE` coverage.

### Section 11 - Open Issues

Proposed changes:

| Issue | Proposed change |
|---|---|
| OI-001 | Reword as first-adapter probe: Claude Agent SDK / Anthropic viability, message categories, settings behavior, hooks, permissions, MCP, sessions, and packaging. |
| OI-003 | Keep packaging issue for the first adapter and avoid implying all future provider packaging is solved. |
| OI-006 | Add new provider-expansion issue: concrete non-Anthropic adapters require bounded implementation tranches, provider-network policy, conformance fixtures, error classification, and release/security checks. |
| OI-007 | Add Pi pattern-corpus issue if useful: Pi reference review may inform architecture, but no adapter/fork/import/spike is authorized. |

### Section 12 - Decision Log / Change Log

Add decision:

```text
| DEC-017 | 2026-06-13 | SCA-APP-001 reorients runtime strategy to provider-adapter generality, keeps Claude Agent SDK / Anthropic as first concrete adapter, treats Pi as a pattern corpus only, and reframes permission governance as capability-forward with explicit deny precedence. | Human ruled D-APP-01/02/03 and requested formal SCOPE_CHANGE before project-truth mutation. |
```

Add change-log line:

```text
- 2026-06-13: SCA-APP-001 preview prepared for provider-general runtime and Pi pattern-corpus reorientation; authoritative edits pending human approval.
```

## Governance Doc Amendments

These are proposed propagation amendments, not applied edits.

| File | Proposed amendment |
|---|---|
| `docs/PRD.md` | Replace Claude-SDK-only strategic framing with provider-adapter architecture. Keep Claude Agent SDK / Anthropic as first concrete shipped adapter. Replace "Anthropic-only" as strategic policy with "current shipped provider scope is loopback plus Anthropic; new providers require bounded tranches." Reframe deny-first language as explicit deny precedence within capability policy. |
| `docs/CONTRACT.md` | Amend K-ENGINE/K-SDK wording so external SDKs/providers are adapter substrates, not governance authorities. Amend K-PERM so explicit deny precedence remains hard while useful tool capability can be exposed through policy. Amend K-NET so provider-general strategy is approved but current shipped network remains bounded. |
| `docs/SPEC.md` | Generalize SDK runtime configuration, message mapping, tool surface, permission mapping, and network policy to provider/SDK adapters. Keep first concrete adapter details where implementation is current. |
| `docs/TYPES.md` | Add or adjust vocabulary for provider adapters, first adapter, Pi pattern corpus, capability policy, and explicit deny precedence. |
| `docs/PLAN.md` | Update strategic roadmap to describe provider-adapter runtime with Claude Agent SDK / Anthropic as first adapter. Keep read-before-write/bash sequencing and human gates. |

## Decision Records

Proposed decision register state after Gate 5:

| ID | State | Ruling record |
|---|---|---|
| D-APP-01 | RULED | `execution/_Coordination/_DECISIONS/D-APP-01_RULING_2026-06-13.md` |
| D-APP-02 | RULED | `execution/_Coordination/_DECISIONS/D-APP-02_RULING_2026-06-13.md` |
| D-APP-03 | RULED | `execution/_Coordination/_DECISIONS/D-APP-03_RULING_2026-06-13.md` |

## Control-Plane Amendments

| File | Proposed amendment |
|---|---|
| `execution/_Coordination/_COORDINATION.md` | Current strategic focus becomes provider-adapter-general Chirality runtime, Claude Agent SDK / Anthropic first concrete adapter, Pi pattern corpus only. |
| `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` | Next agents read active plan/coordination/decision register, select one earliest unblocked item, and treat provider-general work as governance-approved but implementation-bounded. |
| `plans/PLAN_2026-06-13_runtime_completion.md` | Replace "Pi adapter packet" with "provider expansion packet / future adapter packet" and update D-APP mirror rows to RULED after ruling records exist. |
| `frontend/docs/harness/runtime_engine_contract.md` | Generalize adapter contract wording while preserving current concrete adapter path. |
| `plans/pi-agent-harness-assessment.md` and `plans/pi-assessment/*.md` | Mark as pattern-corpus references or superseded by SCA-APP-001; remove active Pi spike/import/sidecar implications. |

## Gate 3 Approval Question

Do you approve these amendments to the decomposition document and the proposed governance/control-plane propagation surfaces for Gate 5 execution?
