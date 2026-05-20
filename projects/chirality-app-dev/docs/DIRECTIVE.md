# DIRECTIVE - Founding Intent, Product Boundary, and Operating Constraints

Status: Active directive derived from `docs/PRD.md`
Date: 2026-05-20
Applies to: Chirality App vNext and its bundled governance/runtime documents

This document is the "why" document for Chirality App. It states the product intent, authority boundaries, professional responsibility posture, and structural constraints that govern the rest of the documentation set.

Where this document conflicts with the approved `docs/PRD.md`, the PRD controls until a governed product change updates both documents. Where implementation conflicts with this document, implementation is incomplete or nonconforming.

---

## 1. Founding Intent

Chirality App is a local-first desktop harness for governed AI-agent work over a user-selected filesystem workspace.

The app packages a release-managed instruction root and binds it to a mutable working root selected by the user. The working root holds project execution state as inspectable files. The instruction root holds the agent operating system, governance documents, and release-managed behavior.

The app exists to:

- accelerate deliverable-heavy professional work;
- keep project truth in plain files under user control;
- preserve human authority at all reliance gates;
- make runtime actions auditable and replayable;
- let agents propose, organize, draft, reconcile, and execute bounded tool work without becoming the authority for professional judgment.

The runtime direction is:

> SDK-privileged, contract-owned, and Chirality-governed.

The Claude Agent SDK is the preferred engine for generic agent-loop mechanics. Chirality owns the runtime contract, audit mirror, permission semantics, filesystem boundaries, lifecycle authority, product identity, and professional reliance boundaries.

---

## 2. Product Thesis

### 2.1 Filesystem Is The Database

Project execution truth lives in user-controlled files.

- Deliverables, dependencies, status records, context, references, and handoff states are file-backed.
- Runtime convenience state is permitted only when it is explicitly non-authoritative.
- Hidden vendor state, chat state, SDK transcripts, caches, or UI settings are not project truth.

### 2.2 Git Is The Event Store For Accepted Project State

Git-tracked files provide reviewable history, rollback, auditability, and release evidence.

If a gate-relevant decision is not in a versioned project file, it does not exist for reliance.

Runtime event logs explain what happened during agent sessions. Git records accepted project state.

### 2.3 Runtime Events Are Audit Evidence

Chirality runtime events record accepted turns, provider/SDK messages, permission decisions, tool calls, hook outcomes, terminal status, compaction boundaries, and subagent lifecycle events.

The canonical Chirality runtime audit mirror is `.chirality/sessions/<sessionId>/events.jsonl` or an explicitly configured Chirality-controlled session path.

External SDK transcripts are secondary runtime artifacts unless imported into Chirality's event schema.

### 2.4 Humans Decide What Can Be Relied Upon

Agents propose. Runtime records. Deterministic tools validate and transform. Humans decide what can be relied upon.

No agent, SDK, provider, endpoint, tool, or generated artifact may sign, seal, approve, certify, issue, or otherwise release professional work for reliance.

---

## 3. SDK Boundary Directive

### 3.1 Privileged Engine, Not Product Authority

The Claude Agent SDK is the preferred substrate for:

- model/tool loop execution;
- built-in read/write/edit/bash tool surfaces when enabled;
- hook dispatch;
- MCP transport;
- SDK session mechanics;
- subagent invocation;
- compaction messages.

The SDK does not own:

- Chirality's public APIs;
- browser `UIEvent` contract;
- canonical `HarnessEvent` schema;
- permission semantics;
- tool exposure rules;
- lifecycle transitions;
- human-gate requirements;
- product identity;
- canonical audit storage.

### 3.2 Provider-Neutral Core

Core runtime records, APIs, and tests use Chirality terms.

Claude/SDK-specific identifiers, message names, transcript paths, permission modes, and tool names must be translated at the adapter boundary. They may appear only as adapter metadata, not as required public API fields or canonical event identities.

### 3.3 Engine Replaceability

The SDK adapter may be difficult to replace in practice, but it must sit behind an `AgentEnginePort` / `RuntimeEngineContract` and an `EngineConformanceSuite`.

A future provider, local model, or self-hosted runtime may be adopted only if it satisfies the same Chirality-owned contract and reliance-boundary requirements.

### 3.4 Fallback Principle

A custom or alternate runtime remains a governed fallback if the SDK cannot satisfy, expose, or be wrapped to satisfy a product-critical Chirality boundary without weakening governance.

---

## 4. Professional Responsibility Model

### 4.1 AI Outputs Are Drafts

All agent outputs are drafts, proposals, structured assistance, or decision support until accepted by an accountable human.

### 4.2 Non-Delegable Human Authority

Only an accountable human may:

- approve a governed state change;
- issue or transmit work for reliance;
- sign, seal, certify, or stamp work;
- accept residual risk;
- adjudicate conflicts requiring professional judgment;
- decide code or regulatory compliance.

### 4.3 Tool Competence

Users must not rely on an agent or deterministic tool for work they are not competent to verify at the appropriate level of risk.

### 4.4 Professional Boundary

Chirality may support professional reliance by improving traceability, auditability, evidence handling, and workflow discipline. It does not itself create professional reliability or code compliance.

Domain-engine outputs, including future OpenPipeStress outputs, are not professional approval and are not solver truth owned by Chirality.

---

## 5. Structural Constraints

| Constraint | Directive |
|---|---|
| Local-first desktop | The app must not require an external project database or central service. |
| Instruction root separation | Bundled instructions and governance are release-managed and distinct from the working root. |
| Working root authority | Mutable project execution state belongs under the selected working root or explicitly configured Chirality-controlled project/session paths. |
| Canonical audit mirror | Chirality `events.jsonl` is the product-owned runtime audit record. |
| SDK settings isolation | Shipped builds must not load ambient user/global Claude Code settings. |
| Deny-first runtime | Deny rules, hook denials, path failures, and human gates override prompt text and convenience settings. |
| Tool availability is not exposure | Built-in, SDK-backed, MCP-backed, or local tools are exposed only through Chirality policy. |
| Human gates | Gate-relevant decisions must be explicit, reviewable, and human-owned. |
| Provider neutrality | External engine details must be translated behind adapters. |
| Product identity | Chirality must not present itself as Claude Code or an Anthropic product. |

---

## 6. Scope Boundary

### 6.1 In Scope

- Desktop shell and working-root selection.
- PORTAL, WORKBENCH, PIPELINE, file tree, toolkit, and chat surfaces.
- Harness session APIs and SSE turn execution.
- SDK-backed runtime through a Chirality-owned engine contract.
- Canonical runtime event logging and replay.
- Prompt/persona composition from the instruction root.
- Permission overlay, hooks, path containment, redaction, and result budgeting.
- In-process Chirality MCP tools for deterministic project operations.
- Execution-root scaffolding and lifecycle/dependency contracts.
- macOS 15+ Apple Silicon unsigned DMG release path.
- Future generic Domain Engine Profile support after harness stability.

### 6.2 Out Of Scope Without Governed Amendment

- Automated professional approval, certification, code compliance, signing, sealing, or issuance.
- Direct protected domain-engine writes by agents.
- Treating SDK transcripts, chat drafts, or user settings as project truth.
- Loading ambient `~/.claude` user/local settings in shipped builds.
- Shipped `bypassPermissions`.
- Remote MCP, plugin marketplaces, remote execution, or network expansion beyond scoped policy.
- Windows/Linux packaging.
- Reactivation of retired PKG-08 hardening deliverables.

---

## 7. Responsible Use

Use Chirality as a governed harness for producing traceable, inspectable work.

Do not use Chirality to bypass professional judgment, human review, or explicit project governance.

Do not rely on prompt text as the safety boundary for filesystem writes, tool execution, lifecycle transitions, or professional decisions.

Do not treat external runtime behavior as authoritative unless Chirality has mapped it into product-owned events, records, and gates.
