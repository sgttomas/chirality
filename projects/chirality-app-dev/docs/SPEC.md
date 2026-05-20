# SPEC - Physical Structures, Runtime Contracts, and Mechanics

Status: Active specification derived from `docs/PRD.md`
Date: 2026-05-20
Applies to: Chirality App vNext filesystem, APIs, runtime, packaged app, and validation

This document specifies the concrete structures and mechanics required by Chirality App. It is the "how it is shaped" document. `DIRECTIVE.md` states intent. `CONTRACT.md` states invariants. `TYPES.md` defines vocabulary. `PLAN.md` sequences work.

Normative keywords `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are used with their usual standards-track meanings.

---

## 1. Root Model

### 1.1 Instruction Root

The instruction root is release-managed app content. A complete source tree or packaged app SHOULD include:

- `AGENTS.md`
- `README.md`
- `agents/`
- `docs/`
- `docs/DIRECTIVE.md`
- `docs/CONTRACT.md`
- `docs/SPEC.md`
- `docs/TYPES.md`
- `docs/PLAN.md`
- `WHAT-IS-AN-AGENT.md` where required by packaging/integrity policy
- `PROFESSIONAL_ENGINEERING.md` where required by packaging/integrity policy

`CHIRALITY_INSTRUCTION_ROOT` MAY override the instruction root in development. Packaged builds use the packaged resource root.

### 1.2 Working Root

The working root MUST be:

- absolute;
- existing;
- a directory;
- readable and writable;
- not inside the instruction root.

The working root contains mutable project execution state. Agents and runtime tools MUST NOT treat the instruction root as a working root.

---

## 2. Session Store

### 2.1 Current Layout

Current legacy session records may exist as:

```text
.chirality/sessions/<sessionId>.json
```

or under `CHIRALITY_SESSION_ROOT`.

Legacy records MUST remain readable until migration is explicitly completed.

### 2.2 Canonical Future Layout

```text
.chirality/
  sessions/
    <sessionId>/
      session.json
      events.jsonl
      turns/
        <turnId>.json
      artifacts/
      sdk/
```

### 2.3 `session.json`

Required or expected fields:

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

Future SDK linkage fields:

- `sdkSessionId`
- `sdkProjectKey`
- `sdkTranscriptPath` or `sdkSessionStoreKey`
- `sdkConfigDir`
- `sdkSettingSources`
- `sdkPackageVersion`
- `sdkClaudeCodeVersion`
- `sdkResumeMode`

SDK linkage fields are metadata. They MUST NOT become the canonical Chirality session identity.

### 2.4 `events.jsonl`

`events.jsonl` is the canonical Chirality runtime audit mirror.

Rules:

- one JSON object per line;
- append-only during ordinary runtime operation;
- each event includes `schemaVersion`, `eventId`, `sessionId`, timestamp, `type`, and `data`;
- payloads avoid secrets;
- large payloads are stored as artifacts and referenced;
- replay ignores malformed trailing lines while preserving prior valid events.

### 2.5 SDK Transcript Placement

The product SHOULD prefer SDK transcript placement or mirroring under the working root or a parent project-controlled folder, using `SessionStore`, `CLAUDE_CONFIG_DIR`, or both where empirically reliable.

If SDK transcripts must live under `~/.claude/projects/...`, Chirality MUST:

- keep `events.jsonl` canonical;
- cross-reference the external path or store key in `session.json`;
- record residual risk in the reliance-boundary register.

---

## 3. Harness Event Schema

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

Initial event types:

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

Later event types:

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

SDK message names MUST be mapped into Chirality event names. SDK names MUST NOT be required public event types.

---

## 4. Browser SSE Contract

`POST /api/harness/turn` returns `text/event-stream`.

Valid browser event names:

- `session:init`
- `chat:delta`
- `chat:complete`
- `tool:result`
- `session:complete`
- `turn:error`
- `process:exit`

The stream MUST terminate with a completion/error signal unless the client disconnects. Client disconnect cleanup MUST record cancellation once session events exist.

SDK messages are not browser events. `SdkMessageMapper` maps SDK stream messages to this UI contract and to `HarnessEvent`.

---

## 5. Runtime Engine Contract

### 5.1 Purpose

`AgentEnginePort` / `RuntimeEngineContract` is the product-owned boundary between Chirality and an engine implementation.

The SDK-backed adapter is the preferred implementation, but the contract is not SDK-shaped.

### 5.2 Required Engine Behavior

An engine adapter MUST support:

- accepted-turn persistence before execution;
- async yield of browser-compatible `UIEvent`s;
- deterministic mapping to canonical `HarnessEvent`s;
- terminal success/failure/cancel/interruption outcomes;
- permission decision reporting;
- tool exposure reporting;
- session linkage/resume;
- interrupt/cancel behavior where the engine supports it;
- redaction and safe metadata capture.

### 5.3 Provider-Neutral Translation

`EngineAdapter` MUST translate:

- external message names;
- external session IDs;
- external tool names;
- external permission modes;
- external transcript paths;
- external hook names;

into Chirality-owned contracts.

Provider-specific values MAY be retained under adapter metadata fields.

### 5.4 Engine Conformance

`EngineConformanceSuite` MUST test at least:

- accepted-turn persistence;
- terminal event persistence;
- SSE compatibility;
- SDK/provider message mapping;
- permission denial;
- tool exposure;
- interrupt/cancel behavior;
- session resume;
- redaction;
- provider-neutral core leakage.

---

## 6. SDK Configuration Mechanics

### 6.1 SDK Options

`SdkOptionsBuilder` constructs SDK options from:

- session record;
- resolved runtime options;
- content blocks from text/attachments;
- persona/system prompt;
- `cwd` / project root;
- permission mode;
- allowed/disallowed tool posture;
- hooks;
- MCP servers;
- subagent definitions;
- session ID / resume;
- settings isolation policy.

### 6.2 Settings Isolation

Shipped builds MUST use:

```ts
settingSources: []
```

Development MAY enable `['project']` only through explicit environment configuration. Shipped builds MUST NOT use `user` or `local` setting sources.

### 6.3 API Key Handling

API key resolution order:

1. UI safeStorage key;
2. `ANTHROPIC_API_KEY`;
3. `CHIRALITY_ANTHROPIC_API_KEY`.

The active key MAY be supplied to the SDK process for the active turn and SHOULD be restored/cleared afterward where feasible. Keys MUST be redacted from logs, events, and artifacts.

---

## 7. Permission And Tool Mechanics

### 7.1 Chirality Modes

| Chirality mode | SDK posture | Required overlay |
|---|---|---|
| `readOnly` | Prefer SDK `plan` or `dontAsk` with read tools pre-approved. | Deny write/edit/bash/network-capable tools and unexpected tools. |
| `workspaceWrite` | SDK `acceptEdits` only after write hooks pass; otherwise `default`. | Enforce root containment, instruction-root block, symlink rejection, provenance. |
| `dontAsk` | SDK `dontAsk`. | Pre-approve only exact safe tools; deny everything else without prompting. |
| `ask` | SDK `default` with `canUseTool`. | Use UI approval for governed writes/shell; persist decision. |
| `bypass` | SDK `bypassPermissions` only in developer-local mode. | Still apply deny rules, path hooks, instruction-root protection, and subagent governance. |

`allowedTools` auto-approval MUST NOT be treated as a restriction boundary.

### 7.2 Tool Sequence

Tool rollout sequence:

1. SDK read tools and Chirality read MCP tools.
2. Chirality status/dependency/scope/scaffold MCP tools.
3. SDK `Write`/`Edit` plus Chirality write MCP tools after write hooks and policy pass.
4. SDK `Bash` only after timeout, result storage, hook, interrupt, and audit validation.
5. Remote MCP, tool search, and plugins only after local/in-process governance matures.

### 7.3 Chirality MCP Tools

Initial in-process MCP tools:

- status read;
- status transition;
- dependency CSV read;
- dependency CSV write;
- scope scan;
- scaffold or scaffold dry-run.

All Chirality MCP tools MUST:

- validate input schemas;
- enforce path containment;
- pass through permission overlay;
- pass through hooks where applicable;
- emit or mirror `HarnessEvent`s;
- redact sensitive output.

---

## 8. Hook Mechanics

Required hook phases:

- `PreToolUse`
- `PostToolUse`
- `PostToolUseFailure`
- `PreCompact`
- `Stop`
- `SubagentStart`
- `SubagentStop`

First hook policies:

- project-root containment;
- instruction-root write block;
- symlink write rejection;
- write budget;
- provenance append;
- compaction boundary mirror;
- stop/finalization;
- subagent governance.

Pre-tool denials for write, shell, domain, and subagent tools MUST fail closed.

---

## 9. Prompt And Persona Mechanics

Persona names resolve to `agents/AGENT_*.md`.

`PersonaComposer` MUST compose prompt/system context from:

- selected persona instruction content;
- relevant instruction-root governance context;
- working-root boundaries;
- mode policy;
- configured tool surface;
- professional-boundary reminders.

Boot fingerprints SHOULD include:

- persona content hash;
- governance preface hash;
- mode;
- SDK tool names/versions;
- permission-policy version;
- settings-source posture;
- MCP server versions;
- subagent policy version.

---

## 10. Attachments

Server-side attachment resolution is authoritative.

Supported extensions:

- `.png`
- `.jpg`
- `.jpeg`
- `.gif`
- `.webp`
- `.pdf`
- `.txt`
- `.md`
- `.csv`

Rules:

- client metadata is non-authoritative;
- directories, symlinks, special files, unsupported extensions, unreadable files, files over 10 MB, and total raw bytes over 18 MB are rejected;
- partial attachment failure is non-fatal when executable content remains;
- all attachment failure with empty text returns `ATTACHMENT_FAILURE`.

---

## 11. Execution Root Layout

```text
{EXECUTION_ROOT}/
  INIT.md
  PKG-XX_Label/
    0_References/
      _Archive/
    1_Working/
      DEL-XX-YY_Label/
      _Archive/
    2_Checking/
      From/
      To/
    3_Issued/
      _Archive/
  _Aggregation/
  _Change/
  _Coordination/
    _COORDINATION.md
  _Decomposition/
  _Estimates/
  _Reconciliation/
  _Archive/
  _Scripts/
  _Sources/
```

Packages do not nest.

---

## 12. Deliverable Folder Layout

Required metadata:

- `_STATUS.md`
- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`

Minimum PREPARATION fileset also includes:

- `_SEMANTIC.md`

Document kit:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`

Expected/optional:

- `Dependencies.csv`
- `MEMORY.md`
- `_SEMANTIC_LENSING.md`
- `HASH_VERIFICATION_BYPASS.jsonl`

Disabled in this project profile:

- `_MEMORY.md`

---

## 13. `_STATUS.md`

Format:

```markdown
# Status: {DEL-ID} {DeliverableName}

**Current State:** {STATE}
**Last Updated:** {YYYY-MM-DD}

## History
- {YYYY-MM-DD} - State set to {STATE} ({AGENT_OR_ACTOR})
```

Valid lifecycle:

```text
OPEN -> INITIALIZED -> SEMANTIC_READY -> IN_PROGRESS -> CHECKING -> ISSUED
```

Human-gate transitions to `CHECKING` or `ISSUED` require approval SHA evidence.

---

## 14. Dependencies.csv v3.1

The `RegisterSchemaVersion` column MUST be present and set to `v3.1`.

Core columns:

1. `RegisterSchemaVersion`
2. `DependencyID`
3. `FromPackageID`
4. `FromDeliverableID`
5. `FromDeliverableName`
6. `DependencyClass`
7. `AnchorType`
8. `Direction`
9. `DependencyType`
10. `TargetType`
11. `TargetPackageID`
12. `TargetDeliverableID`
13. `TargetRefID`
14. `TargetName`
15. `TargetLocation`
16. `Statement`
17. `EvidenceFile`
18. `SourceRef`
19. `EvidenceQuote`
20. `Explicitness`
21. `RequiredMaturity`
22. `ProposedMaturity`
23. `SatisfactionStatus`
24. `Confidence`
25. `Origin`
26. `FirstSeen`
27. `LastSeen`
28. `Status`
29. `Notes`

Rows are not deleted. Rows no longer observed are marked `RETIRED`.

Active rows require `EvidenceFile` and `SourceRef`, or explicit `location TBD`.

---

## 15. Workspace APIs

Required API families:

- `/api/working-root/validate`
- `/api/working-root/tree`
- `/api/working-root/scope`
- `/api/project/deliverables`
- `/api/working-root/deliverable/status`
- `/api/working-root/deliverable/status/transition`
- `/api/working-root/deliverable/dependencies`

Harness APIs:

- `/api/harness/session/create`
- `/api/harness/session/boot`
- `/api/harness/session/list`
- `/api/harness/session/[id]`
- `/api/harness/turn`
- `/api/harness/interrupt`
- `/api/harness/scaffold`

Existing route shapes remain stable during SDK adoption.

---

## 16. Release And Packaging

Current target:

- macOS 15+
- Apple Silicon (`arm64`)
- unsigned, unnotarized local-builder DMG
- Node.js `>=20`

Release validation MUST include:

- tests;
- typecheck;
- harness validation;
- instruction-root integrity;
- desktop packaging;
- SDK subprocess/binary execution from packaged app after R1;
- settings isolation check;
- network policy check.

Expected output:

- `frontend/dist/Chirality-0.1.0-arm64.dmg`
- `frontend/dist/mac-arm64/Chirality.app`
- instruction-root integrity summary artifact.

---

## 17. Future Domain Interfaces

Domain endpoints are provisional and future-scoped:

- `/api/domain/profiles/list`
- `/api/domain/profiles/validate`
- `/api/domain/artifacts/scan`
- `/api/domain/operations/propose`
- `/api/domain/operations/validate`
- `/api/domain/operations/apply`

No domain endpoint may imply automated professional acceptance or direct protected-model writes by an agent.
