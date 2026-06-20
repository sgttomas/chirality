# DIRECTIVE — Founding Intent, Scope, and Constraints

**Status:** vNext governance rewrite aligned to the approved `docs/PRD.md` dated 2026-05-20
**Date:** 2026-05-20
**Product:** Chirality desktop harness and bundled agent operating system
**Applies to:** Chirality App vNext, bundled governance/runtime documents, frontend implementation, packaged app, and governed workspaces
**Audience:** product owner, engineering, agent-instruction maintainers, reviewers, release operators, and future harness-runtime implementers

This document captures the founding intent, design philosophy, professional responsibility model, and structural constraints for Chirality App. It is the “why” document. `CONTRACT.md`, `SPEC.md`, `TYPES.md`, `PLAN.md`, agent instructions, implementation code, execution deliverables, and release runbooks must remain consistent with this directive. Where implementation conflicts with this directive, implementation is incomplete or nonconforming until a governed change updates the relevant record.

---

## 0. Authority and Reading Order

The governing document set is read as a coherent system:

1. `DIRECTIVE.md` defines intent, values, and structural commitments.
2. `CONTRACT.md` defines binding invariants.
3. `SPEC.md` defines physical structures, file formats, runtime mechanics, and validation surfaces.
4. `TYPES.md` defines vocabulary, identifiers, enums, and type targets.
5. `PLAN.md` defines the development roadmap and sequencing rationale.
6. `docs/PRD.md` states current product requirements and the accepted implementation direction.
7. `AGENTS.md`, `agents/AGENT_*.md`, accepted execution deliverables, scope-change records, and release runbooks constrain concrete operations.

If a lower-authority artifact conflicts with a higher-authority governance source, the higher-authority source controls until a governed change updates the record. The PRD establishes vNext product direction, but it does not erase the authority of the directive, contract, specification, vocabulary, accepted execution scope, or professional-boundary commitments.

---

## 1. Founding Intent

Chirality is a local-first desktop harness for running governed AI agents against a user-selected filesystem workspace. It bundles a release-managed instruction root inside the app, lets the user select a mutable working root, and uses plain files plus git history as the durable substrate for professional work.

The core insight is:

> If the filesystem is the database, architecture is a state-and-authority specification, not a service mesh.

Chirality exists to:

- accelerate deliverable-heavy professional work by organizing agent activity around packages, deliverables, dependencies, lifecycle files, and review gates;
- make AI-assisted work auditable, reviewable, and controllable in settings where provenance, human accountability, and traceability matter;
- keep humans in charge of every binding decision while agents perform drafting, extraction, reconciliation, scaffolding, summarization, and routine transformation;
- provide a desktop harness whose product identity is Chirality, not a vendor CLI, SDK, cloud workflow, or hidden database;
- preserve a path from interactive assistance to governed deliverable production without implying automated professional approval.

Chirality is not just a chat wrapper. It is a governed work harness. Its value is the combination of local filesystem truth, agent instructions, deterministic tools, runtime auditability, human gates, and a professional-responsibility posture.

---

## 2. Design Philosophy

### 2.1 Filesystem Is the Database

Project state is represented as human-readable files under the working root. The system does not require an external database, hidden server, or vendor-hosted project memory to know what the project is.

- **Nodes:** package folders, deliverable folders, domain profile folders, proposal folders, tool-root snapshots.
- **Edges:** `Dependencies.csv` rows, lifecycle references, traceability references, operation proposals, review records.
- **Properties:** markdown and CSV files such as `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `Dependencies.csv`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, and session event logs.

Agents and tools may traverse this filesystem state, but they do not replace it. When a fact matters for reliance, it must land in the appropriate versioned project file or approved artifact.

### 2.2 Git Is the Event Store for Project Truth

Git history is the durable event store for accepted project state. It provides reviewable diffs, rollback, traceability, and auditability independent of chat history, vendor transcript formats, runtime caches, or UI convenience state.

If a decision is not in a versioned file, it does not exist for purposes of reliance.

Runtime session logs explain what happened during agent work. They are important audit records, but they are not a substitute for accepted project-state files and human approval records.

### 2.3 Runtime Events Explain Work; They Do Not Approve Work

Chirality runtime events record accepted turns, provider/SDK messages, model deltas, permission decisions, tool calls, hook outcomes, compaction boundaries, subagent lifecycle, failures, interruptions, and terminal outcomes. These records support replay, diagnosis, and review.

The canonical Chirality runtime audit mirror is `.chirality/sessions/<sessionId>/events.jsonl` or an explicitly configured Chirality-controlled session path. External SDK transcripts are secondary runtime artifacts unless imported into Chirality’s event schema.

Runtime events do not make a deliverable approved, issued, code-compliant, externally validated, or safe for reliance. Gate-relevant decisions must still be represented in versioned project files and accepted by an accountable human.

### 2.4 Human Authority at Every Gate

Agents propose; humans approve. Professional responsibility is personal, non-transferable, and not delegated to a model, tool, SDK, runtime, or deterministic validator.

Only humans may author binding approval records, approve issue/release actions, select governing standards, accept residual risk, adjudicate source conflicts requiring judgment, and decide whether work may be relied upon.

Approvals bind to specific content and must be traceable to a git SHA or equivalent immutable evidence. Content changes after approval void the approval until reviewed again.

### 2.5 Evidence Over Plausibility

Chirality values evidence over fluent output. The system must prefer source-backed statements, explicit assumptions, and visible uncertainty over plausible invention.

Required posture:

- cite or record source paths for extracted dependencies and important claims;
- label assumptions as `ASSUMPTION`, proposals as `PROPOSAL`, unknowns as `TBD`, and observed facts as `FACT` where practical;
- surface conflicts rather than silently resolving them;
- prefer `location TBD` over fabricated provenance;
- use deterministic tools for validation, parsing, scaffolding, linting, and repeatable transformations when available.

### 2.6 No Hidden Memory for Project Truth

No hidden memory may become authoritative project state. UI drafts, local presets, SDK transcripts, model context, runtime logs, app caches, API keys, and provider transcripts are non-authoritative unless a governed process imports their relevant content into the project filesystem.

Convenience state is permitted when it is explicitly non-authoritative and cannot override governance. Examples include UI pane widths, local runtime presets, API key storage, draft chat text, and SDK resume metadata.

### 2.7 Instruction Root and Working Root Are Separate

Chirality separates the release-managed instruction root from the mutable working root.

| Root | Meaning | Mutation policy |
|---|---|---|
| **Instruction root** | Bundled app resources such as `AGENTS.md`, `agents/`, `docs/`, framework guidance, and release-managed instructions. | Read-only during ordinary project execution. Updated only by release/governance changes. |
| **Working root** / `projectRoot` | User-selected local filesystem path where project execution state, deliverables, sessions, and tool artifacts live. | Mutable under runtime policy and human gates. |

The instruction root defines how agents should behave. The working root contains the project being worked on. These roots must not be conflated.

### 2.8 Provider-Adapter-General, Contract-Owned, Chirality-Governed

Chirality should use a provider-adapter runtime architecture for generic agent-loop mechanics where an external provider or SDK satisfies Chirality requirements behind product-owned contracts. The Claude Agent SDK / Anthropic path is the first concrete adapter and, per the human-gated D-APP-18 ruling (Option A), the key-aware default provider — the real `agentSdk` path when an Anthropic key is configured, else `stub`. Provider/SDK adapters may provide the model/tool loop, built-in file tools, bash surface, permission-mode machinery, hook dispatch, MCP transport, SDK transcripts, subagent invocation, and compaction messages.

Provider/SDK adapters do not own Chirality’s product contract. Chirality owns:

- `AgentEnginePort` / `RuntimeEngineContract`;
- browser `UIEvent` and persisted `HarnessEvent` schemas;
- session canonicality and the Chirality audit mirror;
- permission semantics, capability policy, and explicit hard-deny precedence;
- working-root and instruction-root policy;
- persona/system-prompt composition;
- `_STATUS.md` and `Dependencies.csv` lifecycle rules;
- subagent governance;
- path containment, redaction, and provenance;
- professional-boundary language;
- user-facing product identity;
- fallback criteria if SDK behavior cannot be governed.

The preferred architecture is **provider-adapter-general, contract-owned, and Chirality-governed**.

### 2.9 Reliance Boundaries Are First-Class

A reliance boundary is a product-critical semantic that determines whether a user can trust the harness to preserve safety, auditability, authority, or professional boundaries. Examples include path containment, instruction-root protection, accepted-turn persistence, human-gate enforcement, transcript canonicality, permission denial, subagent gating, and settings isolation.

Reliance boundaries must be documented, implemented, and tested in Chirality terms. They must not depend on prompt text or opaque SDK defaults alone. When SDK hooks or callbacks enforce a boundary, Chirality must be able to verify the enforcement path and record the result.

### 2.10 Provider-Neutral Core and Replaceable Engine

The runtime engine may be difficult to replace in practice, but it must be replaceable by construction. Public APIs, canonical event schemas, session storage contracts, permission decision records, and governance rules must not become SDK-shaped.

External identifiers, message names, permission modes, tool names, transcript paths, and SDK session IDs are adapter metadata. Chirality contracts remain provider-neutral and product-owned.

### 2.11 Product Identity Stays Chirality

Chirality may use external engines, libraries, and APIs, but it must not become a Claude Code wrapper in identity, copy, behavior, or governance. User-facing text should describe Chirality’s governed-work posture. SDK usage may be disclosed as implementation/provider detail where appropriate, but it must not imply that Chirality is Claude Code, an Anthropic product, or a feature-parity target.

---

## 3. Professional Responsibility Model

This section applies when Chirality is used for safety-significant, contractually binding, regulated, professional, or high-stakes deliverables.

### 3.1 AI Outputs Are Drafts

Agent outputs are drafts and structured assistance. They are not authoritative engineering judgment, professional approval, or certification. Human acceptance is what may turn an output into project work product.

### 3.2 Engineer-of-Record Principle

A licensed or accountable professional retains decision rights for:

- scope and boundary decisions;
- design basis and governing code/standard selection;
- assumptions and residual-risk acceptance;
- conflict adjudication where judgment is required;
- issuance, signature, seal, transmittal, or release for reliance.

No AI system, agent, tool, SDK, transcript, runtime event, or deterministic validator may claim to certify, approve, sign, seal, issue, or externally validate professional work.

### 3.3 Competence Includes Tool Competence

A professional must not use an agent for work they cannot adequately review. Using AI assistance that cannot be checked against professional knowledge, source documents, deterministic validation, or appropriate peer review is a competence failure.

### 3.4 Hierarchy of Authority

In technical and professional matters, agents and users follow:

1. laws and regulations;
2. codes and standards;
3. approved project specifications, design basis, and scope records;
4. verified analysis and published sources;
5. professional judgment.

Agent outputs carry no independent professional authority. They are decision support until accepted by an accountable human through a governed process.

---

## 4. Scope of the System

### 4.1 In Scope

Chirality supports:

- local desktop operation over a selected working root;
- matrix navigation across PORTAL, WORKBENCH, and PIPELINE;
- working-root validation, file-tree browsing, and deliverable scanning;
- harness sessions, streamed turns, interrupts, runtime options, and attachments;
- instruction-root packaging and integrity verification;
- API key handling as non-project convenience state;
- current Anthropic provider access under governed network policy;
- provider/SDK-hosted runtime integration behind Chirality contracts;
- append-only Chirality session event logs;
- persona/system-prompt composition from instruction-root resources;
- status and dependency contract APIs;
- execution-root scaffolding;
- read tools and Chirality MCP tools under capability policy with explicit hard-deny precedence;
- controlled write/edit/bash/subagent capability only after required gates land;
- validation and packaging runbooks;
- future Domain Engine Profiles after core harness stability.

### 4.2 Out of Scope

Chirality does not:

- approve, sign, seal, certify, issue, or transmit professional work autonomously;
- make safety-critical decisions without human review;
- conduct financial transactions or binding commitments;
- require a project database or remote project server;
- treat SDK transcripts, runtime logs, UI state, API keys, or chat drafts as project truth;
- load ambient user/global Claude Code settings in shipped builds;
- use `bypassPermissions` in shipped builds or ordinary operator workflows;
- expose bash, remote MCP, plugins, marketplace extensions, or remote execution before local SDK governance, hooks, event logging, result storage, and packaging checks are reliable;
- reactivate retired PKG-08 deliverables without governed amendment;
- become OpenPipeStress or any domain-specific solver;
- let agents write directly into protected domain-engine model paths.

---

## 5. Structural Constraints

| Constraint | Rationale |
|---|---|
| Local-first desktop harness | Users retain control of project files and working roots. |
| No external project database dependency | Project truth stays inspectable, git-trackable, and portable. |
| Plain-file project state | Humans and tools can inspect, diff, archive, and recover state without the app. |
| Git-backed reliance record | Accepted project decisions bind to versioned files, not transient chats. |
| Instruction root separate from working root | Release-managed agent instructions cannot be silently mutated by project execution. |
| Flat package → deliverable hierarchy | Simplifies decomposition, scanning, coverage checks, and lifecycle contracts. |
| Deliverable-local dependency registers | Dependencies remain near the work item; aggregation is on-demand. |
| Append-only runtime event log | Accepted turns and runtime outcomes are recoverable after interruption or failure. |
| Chirality audit mirror is canonical for runtime governance | SDK transcripts may assist resume/debugging but do not displace product-owned events. |
| SDK behind product-owned contract | Upstream behavior cannot silently redefine Chirality semantics. |
| Shipped SDK settings isolation | Ambient `.claude` or user-home settings cannot alter shipped harness behavior. |
| Deny-first permission semantics | A deny from policy, hook, path check, governance, or human gate overrides any allow. |
| Runtime code enforces safety | Prompt instructions reinforce policy but are not sufficient enforcement. |
| MCP is a transport, not a bypass | In-process MCP tools must pass through the same policy as SDK built-ins. |
| Product identity stays Chirality | The app must not present itself as a vendor CLI or external product. |
| Domain engines own domain truth | Chirality governs interaction and records; it does not become the solver. |

---

## 6. Responsible Use

Users and maintainers must:

- treat agent outputs as drafts until reviewed;
- preserve source paths, evidence, and explicit uncertainty;
- keep human review and sign-off at decision gates;
- inspect diffs before accepting project-file changes;
- understand the configured permission mode and tool surface before enabling writes or bash;
- keep API keys and secrets out of project files and runtime event payloads;
- verify packaging, instruction-root integrity, and SDK settings isolation before release;
- maintain professional-boundary copy in UI and documentation.

---

## 7. Change Discipline

Changes that alter scope, release target, data contracts, professional-boundary posture, runtime engine semantics, permission behavior, transcript canonicality, or retired/active execution scope must be handled as governed product changes.

A change is not complete until it is reflected in the appropriate combination of PRD, directive, contract, specification, type vocabulary, plan, tests, runbooks, and implementation artifacts.
