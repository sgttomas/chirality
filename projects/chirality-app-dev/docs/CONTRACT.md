# CONTRACT - Invariant Catalog

Status: Active invariant catalog derived from `docs/PRD.md`
Date: 2026-05-20
Applies to: Chirality App vNext runtime, docs, frontend, packaged app, and governed project workspaces

This document defines binding invariants for Chirality App. Invariant IDs are stable. New invariants may be added. Existing invariant IDs must not be reused for different meanings.

Enforcement may occur in code, tests, release checks, instructions, human gates, or the reliance-boundary register. Prompt text alone is not sufficient enforcement for P0 safety, audit, filesystem, or human-gate boundaries.

---

## 1. Invariant Catalog

### 1.1 Product Authority And Identity

| ID | Invariant | Enforcement |
|---|---|---|
| K-PRD-1 | `docs/PRD.md` is the approved product source for vNext direction. | Governance review; traceability in docs |
| K-ID-1 | Chirality App remains a governed professional-work agent harness, not Claude Code branding or an Anthropic product wrapper. | UI copy review; release review; PRD acceptance checks |
| K-SDK-1 | The Claude Agent SDK is privileged as implementation substrate, not as product authority. | `AgentEnginePort`; `RuntimeEngineContract`; conformance tests |
| K-CORE-1 | Core runtime APIs, events, tests, and records use Chirality terms. Provider/SDK-specific terms are translated at adapter boundaries. | `EngineAdapter`; event schema tests; API review |

### 1.2 Filesystem Authority

| ID | Invariant | Enforcement |
|---|---|---|
| K-FS-1 | Authoritative project execution state lives in plain files under the working root or explicit Chirality-controlled project paths. | Working-root validation; file APIs; human review |
| K-FS-2 | The instruction root and working root are separate. The working root must not be inside the instruction root. | Working-root validation API |
| K-FS-3 | Runtime tools must enforce project-root containment before reads/writes. | Permission overlay; hooks; tool tests |
| K-FS-4 | Runtime tools must block instruction-root writes. | Pre-tool hooks; path policy tests |
| K-FS-5 | Symlink writes are rejected until a governed policy explicitly permits them. | Pre-tool hooks; filesystem tests |

### 1.3 Session And Audit

| ID | Invariant | Enforcement |
|---|---|---|
| K-AUDIT-1 | A user turn must be persisted as `turn.accepted` before SDK/model execution begins. | `TurnEngine`; session event tests |
| K-AUDIT-2 | Every accepted turn must end with a terminal event: completed, failed, cancelled, or interrupted. | `TurnEngine`; conformance tests |
| K-AUDIT-3 | `.chirality/sessions/<sessionId>/events.jsonl` or configured equivalent is the product-owned runtime audit mirror. | `SessionEvents`; replay tests |
| K-AUDIT-4 | SDK transcripts are secondary runtime artifacts unless imported into Chirality's event schema. | `SdkSessionLink`; reliance-boundary register |
| K-AUDIT-5 | Runtime event payloads must avoid secrets and store large payloads as referenced artifacts. | `RunLogger`; redaction tests; artifact policy |
| K-AUDIT-6 | Event replay must tolerate malformed trailing JSONL without losing valid prior events. | Replay parser tests |

### 1.4 Runtime Engine Boundary

| ID | Invariant | Enforcement |
|---|---|---|
| K-ENGINE-1 | All engine implementations must satisfy `AgentEnginePort` / `RuntimeEngineContract`. | `EngineConformanceSuite` |
| K-ENGINE-2 | Public harness APIs and browser `UIEvent`s must not depend on SDK message names or transcript shape. | API tests; mapper tests |
| K-ENGINE-3 | Provider-specific identifiers such as SDK session IDs may appear only as adapter metadata or explicit linkage fields. | Schema review; conformance tests |
| K-ENGINE-4 | SDK adapter version, settings posture, visible tools, and transcript linkage must be recorded in safe runtime metadata. | Runtime metadata tests |
| K-ENGINE-5 | If the SDK cannot satisfy a P0 reliance boundary, a governed fallback decision is required before production use. | R0/R1 gate; reliance-boundary register |

### 1.5 SDK Isolation And Network Policy

| ID | Invariant | Enforcement |
|---|---|---|
| K-SDK-SET-1 | Shipped builds use `settingSources: []` unless a governed exception is accepted. | SDK options builder tests |
| K-SDK-SET-2 | Shipped builds must not load `user` or `local` Claude Code settings. | SDK options builder tests; release checks |
| K-NET-1 | Renderer outbound traffic is limited to loopback and Anthropic API unless amended. | Electron network guardrail tests |
| K-NET-2 | Tool or MCP network expansion beyond Anthropic requires future scope approval. | Tool registry review; permission policy |
| K-KEY-1 | API keys are not written to project files, logs, runtime events, SDK transcripts intentionally, or tool artifacts. | Key store; redaction tests |

### 1.6 Permission And Tool Exposure

| ID | Invariant | Enforcement |
|---|---|---|
| K-PERM-1 | Deny rules override all allow decisions, including persona, operator, SDK mode, and developer-only bypass. | Permission overlay tests |
| K-PERM-2 | `allowedTools` alone is not a restriction boundary. Restrictions require deny rules, `disallowedTools`, hooks, `dontAsk`, or `canUseTool`. | SDK options tests; PRD acceptance |
| K-PERM-3 | Tool implementation availability does not imply model exposure. | Tool-surface resolver tests |
| K-PERM-4 | `readOnly` exposes or allows read-only tools only. | Permission tests |
| K-PERM-5 | `dontAsk` denies unapproved write, shell, network, or non-allowlisted actions without prompting. | Permission tests |
| K-PERM-6 | `bypassPermissions` is not shipped as ordinary operator behavior. | Build/runtime config checks |
| K-TOOL-1 | Chirality MCP tools pass through the same permission, hook, path, redaction, and event policy as SDK built-ins. | MCP tool tests; hook tests |
| K-TOOL-2 | Bash remains denied by default until timeout, result storage, interrupt, hook, and audit behavior pass validation. | Runtime phase gates |

### 1.7 Hooks And Reliance Boundaries

| ID | Invariant | Enforcement |
|---|---|---|
| K-HOOK-1 | Write, shell, domain, and subagent pre-tool hook denials fail closed. | Hook tests |
| K-HOOK-2 | Product-critical boundaries must be mapped in the reliance-boundary register. | R0/R1 deliverables; conformance tests |
| K-HOOK-3 | P0 reliance boundaries cannot be prompt-only or opaque SDK-default-only. | Reliance-boundary review |
| K-HOOK-4 | Compaction boundaries must be mirrored when the SDK exposes them. | SDK message mapper tests |

### 1.8 Agent And Subagent Governance

| ID | Invariant | Enforcement |
|---|---|---|
| K-AGENT-1 | Persona names resolve to `agents/AGENT_*.md` and aliases map to canonical agents. | Persona resolver tests |
| K-AGENT-2 | Real prompt composition must include agent instruction content and relevant governance context. | Persona composer tests |
| K-SUB-1 | Type 2 subagent delegation fails closed unless governance metadata is valid. | `evaluateSubagentGovernance`; hook tests |
| K-SUB-2 | Subagents inherit or reduce parent permissions; they cannot bypass governance. | SDK agents config tests |

### 1.9 Deliverable Governance

| ID | Invariant | Enforcement |
|---|---|---|
| K-HIER-1 | Execution roots use flat packages containing deliverables. No nested packages. | Scaffold validation; scope scan |
| K-STATUS-1 | `_STATUS.md` is the canonical lifecycle state file for each deliverable. | Status APIs; lifecycle tests |
| K-STATUS-2 | Lifecycle transitions are forward-only and actor-authorized. | Status transition API |
| K-AUTH-1 | Human gate transitions require approval SHA evidence. | Status transition API; human review |
| K-DEP-1 | `Dependencies.csv` v3.1 is the structured dependency register when dependencies are tracked. | Dependency API/linter |
| K-PROV-1 | Active dependency rows require `EvidenceFile` and `SourceRef`, or explicit `location TBD`. | Dependency validation |
| K-SNAP-1 | Snapshot-producing workflows write immutable snapshot folders; pointer files may move. | Tool conventions; review |

### 1.10 Professional Boundary And Domain Engines

| ID | Invariant | Enforcement |
|---|---|---|
| K-PRO-1 | No agent, SDK, endpoint, or tool may approve, certify, sign, seal, issue, or transmit work for reliance. | UI/docs review; human gates |
| K-PRO-2 | Chirality does not claim code compliance, external validation, or solver ownership. | PRD acceptance; copy review |
| K-DOM-1 | Generic `DomainEngineProfile` precedes engine-specific domain integration. | Future amendment gate |
| K-DOM-2 | OpenPipeStress is a fixture profile when adopted, not Chirality core. | Domain profile review |
| K-DOM-3 | Agents do not write directly into protected domain-engine model paths. | Domain path policy; hooks |

---

## 2. Enforcement Map

| Enforcement Surface | Invariants |
|---|---|
| `AgentEnginePort` / `RuntimeEngineContract` | K-SDK-1, K-CORE-1, K-ENGINE-1 through K-ENGINE-5 |
| `EngineConformanceSuite` | K-AUDIT-1 through K-AUDIT-6, K-ENGINE-1 through K-ENGINE-4 |
| SDK options builder | K-SDK-SET-1, K-SDK-SET-2, K-PERM-2, K-PERM-4 through K-PERM-6 |
| Permission overlay and hooks | K-FS-3 through K-FS-5, K-PERM-1 through K-PERM-6, K-HOOK-1 |
| Session event store | K-AUDIT-1 through K-AUDIT-6 |
| Persona composer | K-AGENT-1, K-AGENT-2 |
| Subagent governance bridge | K-SUB-1, K-SUB-2 |
| Workspace/status/dependency APIs | K-HIER-1, K-STATUS-1, K-STATUS-2, K-AUTH-1, K-DEP-1, K-PROV-1 |
| Release checks | K-ID-1, K-NET-1, K-KEY-1, K-SDK-SET-1, K-SDK-SET-2 |
| Human review | K-PRO-1, K-PRO-2, K-AUTH-1, K-DOM-1 through K-DOM-3 |

---

## 3. Retired Invariants

No vNext invariants have been retired.
