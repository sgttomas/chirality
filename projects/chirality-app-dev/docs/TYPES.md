# TYPES - Domain Vocabulary, Runtime Types, and Enumerations

Status: Active vocabulary derived from `docs/PRD.md`
Date: 2026-05-20
Applies to: Chirality App vNext docs, runtime, frontend, tests, and governed workspaces

This document defines canonical terms and type vocabularies. When another document uses a term differently, this document governs unless the approved PRD says otherwise.

---

## 1. Product Entities

### 1.1 Chirality App

The local-first desktop application that hosts governed AI-agent work over a selected filesystem working root.

### 1.2 Instruction Root

Release-managed app-bundled governance and instruction content. Expected entries include `AGENTS.md`, `agents/`, `docs/`, `README.md`, and other package resources required by integrity policy.

### 1.3 Working Root

User-selected filesystem directory containing mutable project execution state. The working root must be absolute, existing, readable/writable, and outside the instruction root.

### 1.4 Project Truth

Gate-relevant project state stored in versioned files. Runtime transcripts, chat drafts, UI state, API keys, and SDK transcripts are not project truth.

### 1.5 Runtime Audit Mirror

The product-owned runtime event log, normally `.chirality/sessions/<sessionId>/events.jsonl`.

---

## 2. Execution Hierarchy

The project execution hierarchy is flat:

```text
{EXECUTION_ROOT}/
  PKG-XX_Label/
    1_Working/
      DEL-XX-YY_Label/
```

| Entity | Meaning |
|---|---|
| Package | Flat partition of scope; packages do not nest. |
| Deliverable | Unit of production inside a package. |
| Artifact | File output produced by a deliverable, tool, runtime, or release workflow. |
| Tool root | Project-level folder for derived or operational outputs. |

---

## 3. Stable Identifiers

| Entity | Format | Example |
|---|---|---|
| Package | `PKG-XX` or `PKG-XXX` | `PKG-01` |
| Deliverable | `DEL-XX-YY` or `DEL-XXX-YY` | `DEL-01-03` |
| Dependency | `DEP-XX-YY-NNN` | `DEP-01-03-001` |
| Scope item | `SOW-NNN` | `SOW-003` |
| Objective | `OBJ-NNN` | `OBJ-001` |
| Harness session | opaque string | `session_...` |
| Turn | opaque string scoped to session | `turn_...` |
| Harness event | opaque string scoped to event store | `evt_...` |

IDs are identity. Folder paths are physical projections and may change.

---

## 4. Agent Vocabulary

### 4.1 Agent Types

| Type | Name | Role |
|---|---|---|
| Type 0 | Standard-setting | Defines governance, rules, and role boundaries. |
| Type 1 | Orchestrating | Interprets intent, routes work, prepares context, reconciles outputs. |
| Type 2 | Bounded execution | Executes narrow tasks under sealed context and explicit scope. |

### 4.2 Agent Classification Properties

| Property | Values |
|---|---|
| `AGENT_CLASS` | `PERSONA`, `TASK` |
| `INTERACTION_SURFACE` | `chat`, `INIT-TASK`, `spawned`, `both` |
| `WRITE_SCOPE` | `repo-wide`, `project-level`, `deliverable-local`, `tool-root-only`, `workspace-scaffold-only`, `repo-metadata-only`, `none` |
| `BLOCKING` | `never`, `allowed` |

### 4.3 Personas And Aliases

Canonical persona names resolve to `agents/AGENT_*.md`.

| UI Alias | Canonical Agent |
|---|---|
| `HELP` | `HELP_HUMAN` |
| `ORCHESTRATE` | `ORCHESTRATOR` |
| `AGGREGATE` | `AGGREGATION` |
| `RECONCILING` | `RECONCILIATION` |
| `AGENTS` | `HELPS_HUMANS` |

---

## 5. Runtime Engine Vocabulary

| Term | Definition |
|---|---|
| Claude Agent SDK | Preferred hosted engine for generic agent-loop mechanics. |
| AgentEnginePort / RuntimeEngineContract | Product-owned boundary an engine adapter must satisfy. |
| EngineAdapter | Provider-specific translator from external runtime concepts to Chirality contracts. |
| TurnEngine | Runtime service that owns accepted-turn lifecycle and delegates engine execution behind the contract. |
| EngineConformanceSuite | Tests that prove an engine satisfies the Chirality runtime contract. |
| SdkOptionsBuilder | Adapter module that constructs SDK options from Chirality policy. |
| SdkMessageMapper | Adapter module that maps SDK messages into `UIEvent` and `HarnessEvent`. |
| PersonaComposer | Builds system or appended prompt from instruction root, persona, mode, and project policy. |
| RelianceBoundaryRegister | Record of product-critical boundaries and their enforcement surfaces. |
| ChiralityPermissionOverlay | Deny-first permission layer over SDK modes, tools, hooks, and approval UI. |
| ChiralityHooks | Hook callbacks for path, provenance, redaction, compaction, and subagent policy. |
| ChiralityMcpTools | In-process MCP tools for deterministic Chirality operations. |
| SdkSessionLink | Metadata connecting Chirality sessions to SDK session IDs/transcripts. |

---

## 6. Session And Event Types

### 6.1 Session Record

Canonical session metadata includes:

- `sessionId`
- `projectRoot`
- `persona`
- `mode`
- `createdAt`
- `updatedAt`
- `claudeSessionId` (legacy)
- `bootFingerprint`
- `bootedAt`
- `model`

Future SDK metadata includes:

- `sdkSessionId`
- `sdkProjectKey`
- `sdkTranscriptPath` or `sdkSessionStoreKey`
- `sdkConfigDir`
- `sdkSettingSources`
- `sdkPackageVersion`
- `sdkClaudeCodeVersion`
- `sdkResumeMode`

### 6.2 Harness Event

`HarnessEvent` is the canonical persisted runtime event type:

```ts
type HarnessEvent = {
  schemaVersion: 1;
  eventId: string;
  sessionId: string;
  turnId?: string;
  parentEventId?: string;
  timestamp: string;
  type: string;
  data: Record<string, unknown>;
};
```

### 6.3 Initial Event Categories

- `session.created`
- `session.resumed`
- `turn.accepted`
- `turn.started`
- `sdk.system.init`
- `model.request.started`
- `model.delta`
- `model.completed`
- `turn.completed`
- `turn.failed`
- `turn.cancelled`

### 6.4 Later Event Categories

- `tool.queued`
- `tool.permission`
- `tool.started`
- `tool.progress`
- `tool.completed`
- `tool.failed`
- `hook.started`
- `hook.completed`
- `context.compacted`
- `subagent.started`
- `subagent.completed`
- `sdk.mirror.error`

### 6.5 UI Event

Browser-facing stream event. Valid names:

- `session:init`
- `chat:delta`
- `chat:complete`
- `tool:result`
- `session:complete`
- `turn:error`
- `process:exit`

SDK messages are not UI events. They must be translated.

---

## 7. Permission Vocabulary

### 7.1 Chirality Modes

| Mode | Meaning |
|---|---|
| `readOnly` | Read-only tool behavior only. |
| `workspaceWrite` | Controlled workspace writes after hooks and policy. |
| `dontAsk` | Deny unapproved actions without prompting. |
| `ask` | Use UI-mediated approval for governed actions. |
| `bypass` | Developer-only local mode; never shipped as ordinary mode. |

### 7.2 Permission Decision

| Decision | Meaning |
|---|---|
| `allow` | Tool/action may proceed under current policy. |
| `deny` | Tool/action must not execute. |
| `ask` | User or explicit policy approval is required before allow/deny is returned. |

### 7.3 SDK Permission Terms

SDK permission modes, SDK tool names, and SDK session IDs are adapter vocabulary. They may be recorded as metadata but must not define Chirality's public or canonical runtime types.

---

## 8. Tool Vocabulary

| Term | Meaning |
|---|---|
| SDK built-in tool | Tool supplied by Claude Agent SDK, such as read/write/edit/bash surfaces where available. |
| Chirality MCP tool | In-process deterministic tool exposed through SDK MCP mechanics. |
| Tool surface | Set of tools visible or available to the model for a turn. |
| Tool exposure | Policy act of making a tool available; existence does not imply exposure. |
| Tool result artifact | Stored large or sensitive tool output referenced from events. |

Initial Chirality MCP tool families:

- status read/transition;
- dependency CSV read/write;
- scope scan;
- scaffold.

---

## 9. Dependency Vocabulary

| Dimension | Values |
|---|---|
| `DependencyClass` | `ANCHOR`, `EXECUTION` |
| `AnchorType` | `IMPLEMENTS_NODE`, `TRACES_TO_REQUIREMENT`, `NOT_APPLICABLE` |
| `Direction` | `UPSTREAM`, `DOWNSTREAM` |
| `DependencyType` | `PREREQUISITE`, `INTERFACE`, `HANDOVER`, `CONSTRAINT`, `ENABLES`, `OTHER` |
| `TargetType` | `DELIVERABLE`, `PACKAGE`, `WBS_NODE`, `REQUIREMENT`, `DOCUMENT`, `EQUIPMENT`, `EXTERNAL`, `UNKNOWN` |
| `Explicitness` | `EXPLICIT`, `IMPLICIT` |
| `Confidence` | `HIGH`, `MEDIUM`, `LOW` |
| `Origin` | `DECLARED`, `EXTRACTED` |
| `SatisfactionStatus` | `TBD`, `PENDING`, `IN_PROGRESS`, `SATISFIED`, `WAIVED`, `NOT_APPLICABLE` |
| `Status` | `ACTIVE`, `RETIRED` |

---

## 10. Lifecycle States

```text
OPEN -> INITIALIZED -> SEMANTIC_READY -> IN_PROGRESS -> CHECKING -> ISSUED
```

| State | Meaning |
|---|---|
| `OPEN` | Folder exists with minimum metadata. |
| `INITIALIZED` | Document kit exists. |
| `SEMANTIC_READY` | Semantic lens exists, where used. |
| `IN_PROGRESS` | Active work is underway. |
| `CHECKING` | Under human review. |
| `ISSUED` | Released by accountable human process. |

Human gate states require approval SHA evidence where specified by `SPEC.md`.

---

## 11. UI Navigation Vocabulary

| Type | Values |
|---|---|
| `MatrixRow` | `NORMATIVE`, `OPERATIVE`, `EVALUATIVE` |
| `MatrixColumn` | `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING` |
| `PipelineCategory` | `DECOMP*`, `PREP*`, `TASK*`, `AUDIT*` |
| `TaskScopeMode` | `DELIVERABLES`, `KNOWLEDGE_TYPES` |

NORMATIVE and EVALUATIVE rows route to WORKBENCH. OPERATIVE row routes to PIPELINE.

---

## 12. Domain Engine Vocabulary

| Term | Meaning |
|---|---|
| DomainEngineProfile | Future contract describing deterministic domain engine boundaries and operations. |
| OperationProposal | Future record for proposed domain operation requiring checks and human gate. |
| Protected path | Domain-engine path not directly writable by agents. |
| Proposal path | Agent-writable path for draft proposals and summaries. |
| OpenPipeStress | First intended fixture profile if domain-engine scope is later activated. |

Domain engines own domain truth. Chirality governs interaction, proposals, records, and human gates.
