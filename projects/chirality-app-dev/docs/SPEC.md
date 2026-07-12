# SPEC — Physical Structures, Runtime Mechanics, and File Contracts

**Status:** vNext governance rewrite aligned to the approved `docs/PRD.md` dated 2026-05-20
**Date:** 2026-05-20
**Product:** Chirality desktop harness and bundled agent operating system
**Applies to:** Chirality App vNext filesystem, APIs, runtime, packaged app, and validation

This document is the authoritative specification for Chirality App physical structures, file formats, schemas, runtime mechanics, session storage, validation surfaces, and layout conventions.

Normative keywords `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are used in their ordinary specification sense.

---

## 1. Root Model

### 1.1 Instruction Root

The instruction root is the release-managed resource set bundled with the desktop app or supplied through `CHIRALITY_INSTRUCTION_ROOT` during development.

Required entries for a complete source tree / packaged app include:

- `AGENTS.md`
- `README.md`
- `agents/`
- `docs/`
- `docs/DIRECTIVE.md`
- `docs/CONTRACT.md`
- `docs/SPEC.md`
- `docs/TYPES.md`
- `docs/PLAN.md`
- `docs/WHAT-IS-AN-AGENT.md` where required by packaging/integrity policy
- `PROFESSIONAL_ENGINEERING.md` where required by packaging/integrity policy

Rules:

- The instruction root is read-only during ordinary project execution.
- Writes to the instruction root MUST be blocked by runtime hooks and path policy.
- Packaged builds MUST verify instruction-root integrity.
- Missing required instruction-root assets are a P0 packaging and runtime-readiness blocker.

### 1.2 Working Root / `projectRoot`

The working root is the user-selected local project folder.

Rules:

- MUST be an absolute existing directory.
- MUST be readable and writable by the app.
- MUST NOT be inside the instruction root.
- Contains project execution state, deliverables, tool roots, sessions, and local artifacts.
- Is the ordinary location where agents and tools write project truth.

### 1.3 Runtime Configuration State

Runtime configuration state such as UI presets, API keys, provider/SDK linkage, adapter transcript cross-references, session metadata, and window layout is non-authoritative convenience state unless imported into a governed project file.

---

## 2. Execution Root Layout

An execution instance is rooted at `{EXECUTION_ROOT}/` and contains package folders plus tool roots.

```text
{EXECUTION_ROOT}/
├── INIT.md
├── PKG-XX_{PkgLabel}/
│   ├── 0_References/
│   │   └── _Archive/
│   ├── 1_Working/
│   │   ├── DEL-XX-YY_{DelLabel}/
│   │   └── _Archive/
│   ├── 2_Checking/
│   │   ├── From/
│   │   └── To/
│   └── 3_Issued/
│       └── _Archive/
├── _Aggregation/
├── _Change/
├── _Coordination/
│   └── _COORDINATION.md
├── _Decomposition/
├── _Estimates/
├── _Reconciliation/
├── _Archive/
├── _Scripts/
└── _Sources/
```

### 2.1 Package Folders

Naming:

```text
{PKG-ID}_{Sanitize(PackageName)}/
```

Required or expected subfolders:

| Subfolder | Requirement | Purpose |
|---|---|---|
| `0_References/` | SHOULD | Package-level references. |
| `0_References/_Archive/` | SHOULD | Archived references. |
| `1_Working/` | MUST | Active deliverables. |
| `1_Working/_Archive/` | SHOULD | Archived drafts. |
| `2_Checking/` | SHOULD | Review staging. |
| `2_Checking/From/` | SHOULD | Incoming review items. |
| `2_Checking/To/` | SHOULD | Outgoing review items. |
| `3_Issued/` | SHOULD | Released deliverables. |
| `3_Issued/_Archive/` | SHOULD | Archived issued versions. |

### 2.2 Tool Roots

| Tool Root | Purpose |
|---|---|
| `_Aggregation/` | Aggregation snapshots and templates. |
| `_Change/` | Change-management records. |
| `_Coordination/` | Coordination representation. |
| `_Decomposition/` | Project decomposition documents. |
| `_Estimates/` | Cost estimate snapshots. |
| `_Reconciliation/` | Reconciliation reports and closure analysis. |
| `_Archive/` | Baseline snapshots with checksums. |
| `_Scripts/` | Deployment and analysis scripts. |
| `_Sources/` | Shared sources and reference documents. |

Snapshot-producing workflows SHOULD write timestamped immutable folders and MAY update `_LATEST.md` pointer files.

---

## 3. Deliverable Folder Layout

Each deliverable occupies:

```text
{EXECUTION_ROOT}/{PKG-ID}_{PkgLabel}/1_Working/{DEL-ID}_{DelLabel}/
```

### 3.1 File Inventory

| File | Presence | Purpose |
|---|---|---|
| `_STATUS.md` | MUST | Lifecycle state and history. |
| `_CONTEXT.md` | MUST | Identity, package, decomposition reference, traceability. |
| `_DEPENDENCIES.md` | MUST | Dependency summary and run history. |
| `_REFERENCES.md` | MUST | Source references and hash notes. |
| `_SEMANTIC.md` | SHOULD for PREPARATION baseline | Semantic placeholder or lens. |
| `Datasheet.md` | SHOULD when initialized | Key parameters and structured metadata. |
| `Specification.md` | SHOULD when initialized | Requirements and scope definition. |
| `Guidance.md` | SHOULD when initialized | Rationale and design guidance. |
| `Procedure.md` | SHOULD when initialized | Step-by-step workflow. |
| `Dependencies.csv` | SHOULD when tracked | Structured dependency register v3.1. |
| `MEMORY.md` | SHOULD | Canonical deliverable-local working memory. |
| `_SEMANTIC_LENSING.md` | MAY | Semantic analysis narrative. |
| `HASH_VERIFICATION_BYPASS.jsonl` | MAY | Durable record of approved reference-hash bypasses. |
| `_MEMORY.md` | MUST NOT in this project profile | Disabled noncanonical memory file. |

Minimum PREPARATION fileset:

- `_STATUS.md`
- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- `_SEMANTIC.md` placeholder

Document kit:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`

---

## 4. Lifecycle File Contract: `_STATUS.md`

### 4.1 Format

```markdown
# Status: {DEL-ID} {DeliverableName}

**Current State:** {STATE}
**Last Updated:** {YYYY-MM-DD}

## History
- {YYYY-MM-DD} — State set to {STATE} ({AGENT_OR_ACTOR})
```

`_STATUS.md` MAY host a `## Remaining` section: the deliverable-local record of warranted open scope. Where adopted, `## Remaining` is the sole deliverable-local executable work surface. This project has adopted it (owner-adopted 2026-07-10, loop Receipt 5).

### 4.2 Valid States

```text
OPEN → INITIALIZED → SEMANTIC_READY → IN_PROGRESS → CHECKING → ISSUED
```

| State | Meaning |
|---|---|
| `OPEN` | Folder exists with minimum viable fileset. |
| `INITIALIZED` | Draft documents or document kit initialized. |
| `SEMANTIC_READY` | Semantic lens or placeholder generated. |
| `IN_PROGRESS` | Human/agent work underway. |
| `CHECKING` | Frozen candidate under review against a declared basis. Entered when a human declares the checking basis and freezes the candidate; entry conditions in §4.4. |
| `ISSUED` | Accepted baseline, approved and issued by a human. Subsequent changes only via the governed scope-change process (`execution/_ScopeChange/**` SCA records). |

### 4.3 Transition Rules

| Transition | Authorized Actor |
|---|---|
| `→ OPEN` | PREPARATION / scaffold |
| `OPEN → INITIALIZED` | 4_DOCUMENTS / human |
| `INITIALIZED → SEMANTIC_READY` | CHIRALITY_FRAMEWORK / human |
| `INITIALIZED → IN_PROGRESS` | Human, WORKING_ITEMS |
| `SEMANTIC_READY → IN_PROGRESS` | Human, WORKING_ITEMS |
| `IN_PROGRESS → CHECKING` | Human |
| `CHECKING → ISSUED` | Human |
| `CHECKING → IN_PROGRESS` | Human (reversal — the sole exit from an unsuccessful or withdrawn check) |
| `ISSUED → IN_PROGRESS` | Human, via the governed scope-change process only (opens a new revision cycle) |

Rules:

- `_STATUS.md` is the canonical lifecycle file.
- Transitions are forward-only except the two human-authorized reversal transitions above; any other reversal requires a human explicitly amending the record.
- Transitions to `CHECKING` or `ISSUED` require approval SHA evidence.
- SDK/MCP status-transition tools MUST enforce these rules.

### 4.4 Lifecycle Regimes and CHECKING Entry Conditions

Lifecycle states are governed production and change-control regimes with maturity/readiness entry conditions; they are not percentage-complete scores. Advancing `IN_PROGRESS → CHECKING → ISSUED` carries maturity meaning — each transition asserts readiness against declared entry conditions — while the states themselves define which changes are lawful and under what control:

- `IN_PROGRESS` — ordinary authorized edits are permitted. This is the honest holding state whenever warranted open scope exists, however advanced the implementation.
- `CHECKING` — the candidate is frozen. Review evidence appends to run/review records, never to the frozen claim surfaces. Reversal to `IN_PROGRESS` is the only edit path.
- `ISSUED` — accepted baseline; changes only through the governed scope-change process (`execution/_ScopeChange/**` SCA records).

Entry to `CHECKING` is layered, not a single trigger:

1. **Universal minimums (candidacy).** The deliverable's `_STATUS.md` `## Remaining` section is warranted-empty — empty, with a current evidence basis bound to the candidate source state certifying that the emptiness is warranted.
2. **Candidate-specific checking basis.** Satisfaction of the declared review basis appropriate to the deliverable's claims and risk. These criteria are emergent: maturity feedback from real checks hardens into reusable ruled profiles. `docs/ISSUE_READINESS_PROFILES.md` is this project's profile surface.
3. **Human declaration.** A human declares the checking basis and freezes the candidate; entry is a human act.

Rules:

- There are no disclosed-deferral carve-outs: any warranted Remaining item — owner-gated included — keeps the deliverable `IN_PROGRESS`. Boundary adjustments happen through the decision register while `IN_PROGRESS` (rescope before freeze, never carve out during review).
- A failed check exits by reversal (`CHECKING → IN_PROGRESS`); its findings become Remaining items.
- Rebaseline asymmetry: demotion to `IN_PROGRESS` requires no criteria beyond the absence of a current, accepted basis for the asserted state; promotion requires a contemporary declared basis. Lifecycle corrections are human-authorized administrative acts recorded through the decision register; they do not invalidate prior work or evidence, which is preserved as history.
- Entry conditions are gate preconditions, not state determinants: `_STATUS.md` remains the sole lifecycle authority, and reversals are recorded there.
- No machine-enforced BLOCK applies to the `CHECKING → ISSUED` judgment; it remains a human gate.

Reference formulation: repo-root `docs/DELIVERABLE_CONCORDANCE_METHOD.md` §4 (ratified 2026-07-11). This amendment is authorized by owner direction of record (2026-07-11): "attend to both now and resolve the issues you find as you recommended in the sequence 1, 2, 3, 4 just stated.  I give you approval to edit the SPEC/TYPES and just report back what you did."

---

## 5. Context, Dependency Summary, References, and Memory

### 5.1 `_CONTEXT.md`

Required structure:

```markdown
# Context: {DEL-ID}

**Name:** {DeliverableName}
**Package:** {PKG-ID} {PackageName}
**Discipline:** {Discipline}
**Type:** {ArtifactType}
**Responsible:** {Role}

## Description
{Exact description from decomposition document}

## Acceptance Criteria
{Pass/fail conditions from decomposition}

## Anticipated Artifacts
- {List from decomposition; may be empty}

## Scope Traceability
- Scope items: {SOW-IDs}
- Objectives: {OBJ-IDs}

## Decomposition Reference
- **Decomposition file:** {path}
- **Deliverable ID:** {DEL-ID}
```

Rules:

- Header fields SHOULD match the accepted decomposition.
- `_CONTEXT.md` is created by PREPARATION/scaffold and is human-maintained thereafter.

### 5.2 `_DEPENDENCIES.md`

Hybrid container with human-owned and agent/tool-owned sections:

- Dependency Tracking Mode
- Declared Upstream
- Declared Downstream
- Extracted Dependency Register
- Lifecycle Summary
- Run Notes
- Run History

Tracking modes:

| Mode | Meaning |
|---|---|
| `NOT_TRACKED` | Dependencies coordinated externally by humans. |
| `DECLARED` | Human-declared upstream/downstream only. |
| `TRACKED` | Full extraction via dependency workflow and `Dependencies.csv`. |

### 5.3 `_REFERENCES.md`

Required structure:

```markdown
# References: {DEL-ID} {DeliverableName}

## Applicable References
- {RefName/ID} — {Location} — {Relevance}
  - ContentHash: {64-char lowercase SHA-256 | TBD | ERROR: <reason>}

## Notes
- {Notes or placeholder}
```

Rules:

- Reference paths SHOULD be relative where practical.
- Out-of-folder references SHOULD include `ContentHash` when tooling is available.
- Hash bypasses require human approval and durable bypass records.

### 5.4 `MEMORY.md`

Canonical deliverable-local working memory file:

```markdown
# Memory — {DEL-ID}

> Organize by semantic topic, then chronologically within each topic.

## Key Decisions & Human Rulings

## Domain Context

## Open Items

## Proposal History

## Interface & Dependency Notes
```

`_MEMORY.md` MUST NOT be created in this project profile.

---

## 6. `Dependencies.csv` v3.1 Schema

Every row MUST include `RegisterSchemaVersion` set to `v3.1`.

### 6.1 Core Columns

| # | Column | Type | Required | Description |
|---:|---|---|---|---|
| 1 | `RegisterSchemaVersion` | string | MUST | `v3.1`. |
| 2 | `DependencyID` | string | MUST | Unique within deliverable register. |
| 3 | `FromPackageID` | string | MUST | Host package ID. |
| 4 | `FromDeliverableID` | string | MUST | Host deliverable ID. |
| 5 | `FromDeliverableName` | string | MUST | Host deliverable name. |
| 6 | `DependencyClass` | enum | MUST | `ANCHOR` or `EXECUTION`. |
| 7 | `AnchorType` | enum | MUST | See TYPES. |
| 8 | `Direction` | enum | MUST | `UPSTREAM` or `DOWNSTREAM`. |
| 9 | `DependencyType` | enum | MUST | See TYPES. |
| 10 | `TargetType` | enum | MUST | See TYPES. |
| 11 | `TargetPackageID` | string | optional | Target package ID. |
| 12 | `TargetDeliverableID` | string | optional | Target deliverable ID. |
| 13 | `TargetRefID` | string | optional | Non-deliverable target ref. |
| 14 | `TargetName` | string | SHOULD | Human-readable target. |
| 15 | `TargetLocation` | string | optional | Path, URL, or identifier. |
| 16 | `Statement` | string | SHOULD | Dependency statement. |
| 17 | `EvidenceFile` | string | MUST* | Source filename or `location TBD`. |
| 18 | `SourceRef` | string | MUST* | Path + heading/section or `location TBD`. |
| 19 | `EvidenceQuote` | string | SHOULD | Short quote, <= 30 words. |
| 20 | `Explicitness` | enum | SHOULD | `EXPLICIT` or `IMPLICIT`. |
| 21 | `RequiredMaturity` | string | optional | Required maturity. |
| 22 | `ProposedMaturity` | string | optional | Proposed maturity. |
| 23 | `SatisfactionStatus` | enum | SHOULD | Closure status. |
| 24 | `Confidence` | enum | SHOULD | `HIGH`, `MEDIUM`, `LOW`. |
| 25 | `Origin` | enum | MUST | `DECLARED` or `EXTRACTED`. |
| 26 | `FirstSeen` | date | MUST | ISO date. |
| 27 | `LastSeen` | date | MUST | ISO date. |
| 28 | `Status` | enum | MUST | `ACTIVE` or `RETIRED`. |
| 29 | `Notes` | string | optional | Notes and epistemic labels. |

Extension columns MAY be present and are non-breaking, including `EstimateImpactClass` and `ConsumerHint`.

### 6.2 Row Rules

- `DependencyID` MUST be unique within a deliverable register.
- `FromDeliverableID` MUST match the host deliverable ID.
- `ANCHOR` rows use `IMPLEMENTS_NODE` or `TRACES_TO_REQUIREMENT` and `DependencyType=OTHER`.
- `EXECUTION` rows use `AnchorType=NOT_APPLICABLE`.
- Rows are retired, not deleted.
- Legacy missing `RegisterSchemaVersion` is normalized on write to `v3.1`.

---

## 7. Agent Instruction File Contract

Agent instruction files use `AGENT_*.md` names.

### 7.1 Required Header

```markdown
[[DOC:AGENT_INSTRUCTIONS]]
# AGENT INSTRUCTIONS — {AGENT_NAME} ({Brief Descriptor})
AGENT_TYPE: {0|1|2}
```

### 7.2 Required Agent Type Table

```markdown
## Agent Type

| Property | Value |
|---|---|
| **AGENT_TYPE** | TYPE {0|1|2} |
| **AGENT_CLASS** | {PERSONA|TASK} |
| **INTERACTION_SURFACE** | {chat|INIT-TASK|spawned|both} |
| **WRITE_SCOPE** | {scope description} |
| **BLOCKING** | {never|allowed} |
| **PRIMARY_OUTPUTS** | {description} |
```

### 7.3 Required Section Markers

| Section | Marker | Purpose |
|---|---|---|
| PROTOCOL | `[[BEGIN:PROTOCOL]]` … `[[END:PROTOCOL]]` | Procedure and sequencing. |
| SPEC | `[[BEGIN:SPEC]]` … `[[END:SPEC]]` | Validity requirements. |
| STRUCTURE | `[[BEGIN:STRUCTURE]]` … `[[END:STRUCTURE]]` | Schemas and templates. |
| RATIONALE | `[[BEGIN:RATIONALE]]` … `[[END:RATIONALE]]` | Non-normative interpretation. |

Precedence:

```text
PROTOCOL > SPEC > STRUCTURE > RATIONALE
```

### 7.4 Runtime Metadata Frontmatter

Machine-consumed YAML frontmatter MAY include:

- `description`
- `subagents`
- `tools`
- `model`
- `max_turns`
- `disallowed_tools`
- `auto_approve_tools`

Runtime MUST treat UI visibility of an option as non-authoritative. Governance and permission policy remain authoritative.

---

## 8. Harness Session Store

### 8.1 Current / Legacy Session Record

Legacy sessions may exist as:

```text
{sessionRoot}/{sessionId}.json
```

Current fields:

- `sessionId`
- `projectRoot`
- `persona`
- `mode`
- `createdAt`
- `updatedAt`
- `engineSessionId`
- `claudeSessionId`
- `bootFingerprint`
- `bootedAt`
- `model`

Legacy records MUST remain readable during migration.

### 8.2 Canonical vNext Layout

```text
.chirality/sessions/<sessionId>/
├── session.json
├── events.jsonl
├── turns/
│   └── <turnId>.json
├── artifacts/
└── sdk/
```

Optional override:

```text
CHIRALITY_SESSION_ROOT
```

### 8.3 Future Session Metadata

`session.json` SHOULD include:

- `sessionId`
- `projectRoot`
- `persona`
- `mode`
- `createdAt`
- `updatedAt`
- `model`
- `bootFingerprint`
- `engineSessionId`
- `sdkSessionId`
- `sdkProjectKey`
- `sdkTranscriptPath` or `sdkSessionStoreKey`
- `sdkConfigDir`
- `sdkSettingSources`
- `sdkPackageVersion`
- `sdkClaudeCodeVersion`
- `sdkResumeMode`

### 8.4 Canonicalization Rules

- `events.jsonl` is the product-owned Chirality audit mirror.
- SDK transcripts are secondary runtime state unless imported into `HarnessEvent` form.
- The product SHOULD prefer SDK transcript placement or mirroring under the working root or parent project-controlled folder using `SessionStore`, `CLAUDE_CONFIG_DIR`, or both when reliable.
- If SDK writes under `~/.claude/projects/...`, Chirality MUST cross-reference the path or store key, keep `events.jsonl` canonical, and record residual risk in the reliance-boundary register.

---

## 9. Runtime Event Schema

### 9.1 Shape

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

### 9.2 Rules

- JSONL writes MUST append newline-delimited events in write sequence.
- Event IDs MUST be unique.
- Secrets MUST NOT be stored.
- Large payloads MUST be stored as artifacts and referenced by path.
- Replay MUST ignore malformed trailing lines and surface diagnostics.
- Event schema evolution MUST be backward-compatible or explicitly versioned.

### 9.3 Initial Event Categories

- `session.created`
- `session.resumed`
- `turn.accepted`
- `turn.started`
- `adapter.initialized`
- `model.request.started`
- `model.delta`
- `model.completed`
- `turn.completed`
- `turn.failed`
- `turn.cancelled`
- `turn.interrupted`

### 9.4 Later Event Categories

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
- `runtime.mirror.error`

---

## 10. Runtime Engine Contract

### 10.1 Product-Owned Boundary

Chirality MUST define an `AgentEnginePort` / `RuntimeEngineContract` separate from provider/SDK APIs.

Target responsibilities:

- accept validated turn input;
- persist `turn.accepted` before adapter/model execution;
- yield browser `UIEvent`s;
- persist canonical `HarnessEvent`s;
- enforce or invoke permission decisions;
- expose only permitted tools;
- link adapter session metadata;
- handle interrupt/cancel behavior;
- persist terminal outcomes.

### 10.2 Target Type

```ts
interface AgentEnginePort {
  startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>;
  interrupt?(sessionId: string): Promise<void>;
}
```

`AgentEngineRunInput` carries the implemented adapter-port inputs: active session identity and resolved options plus content blocks. The session record and resolved options carry normalized `projectRoot`, persona, mode, and attachment summaries; interrupt and stream cancellation carry cancellation out of band. `TurnEngine.runTurn(request)` remains the route-independent product lifecycle method above this adapter port.

### 10.3 Engine Adapter Rules

- Provider/SDK messages are not the browser contract.
- Provider/SDK messages are not the canonical persisted event contract.
- Provider/SDK-specific names and IDs appear only as adapter metadata.
- `EngineAdapter` MUST translate external message names, external session IDs, external tool names, external permission modes, external transcript paths, and external hook names into Chirality-owned contracts.
- Provider-specific values MAY be retained under explicit adapter metadata fields.
- Any provider/SDK-backed adapter MUST pass engine conformance tests before production default use.
- The Claude Agent SDK / Anthropic adapter is the first concrete adapter and the key-aware
  default provider per D-APP-18: `agentSdk` is selected when an Anthropic API key is
  configured and no explicit provider override is set; `stub` remains available as an
  explicit/keyless fallback.
- Stub adapter remains available for deterministic tests.

### 10.4 Thin Route Rule

`/api/harness/turn` remains a transport adapter. It validates request shape, obtains session lock, forwards input to `TurnEngine`, writes SSE, and handles cleanup. It does not own runtime policy.

---

## 11. Browser SSE Event Contract

Turn streams emit named SSE events with JSON payloads:

- `session:init`
- `chat:delta`
- `chat:complete`
- `tool:result`
- `session:complete`
- `turn:error`
- `process:exit`
- `harness:event`

Rules:

- Existing event names MUST remain compatible during SDK adoption.
- Additional tool progress events MAY be introduced only with UI compatibility handling.
- The stream MUST terminate with a process-level completion/error signal unless the client disconnects.
- Client disconnect cleanup MUST record cancellation once the event log exists.

---

## 12. Provider/SDK Runtime Configuration

### 12.1 Adapter Position

Chirality uses a provider-adapter runtime architecture. Claude Agent SDK / Anthropic is the first concrete adapter and the key-aware default provider (per the D-APP-18 ruling), subject to ongoing conformance tests; further provider expansion remains human-gated. Concrete non-Anthropic providers require bounded future implementation scope. Chirality builds a governance / UI / audit / lifecycle / adapter layer **over** provider harness mechanics — not a standalone general agent harness, and not Claude Code / Pi / Codex feature parity (CONTRACT K-ENGINE-6); Pi is reference-only.

### 12.2 Shipped First-Adapter Settings Isolation

Shipped builds MUST use:

```ts
settingSources: []
```

Development-only project settings MAY use `['project']` behind explicit environment configuration. `user` and `local` setting sources MUST NOT be used in shipped builds.

### 12.3 API Key Handling

- UI safeStorage key takes precedence.
- Then `ANTHROPIC_API_KEY`.
- Then `CHIRALITY_ANTHROPIC_API_KEY`.
- Key material is supplied to the provider/SDK environment only as needed for active turns and redacted from logs/events.

### 12.4 Adapter Metadata to Record

Safe runtime metadata SHOULD include:

- provider/SDK package version;
- Claude Code subprocess version where knowable;
- provider/SDK permission mode;
- visible tool list;
- MCP server names;
- settings-source posture;
- provider/SDK session ID and resume mode;
- transcript/store linkage.

---

## 13. Runtime Options and Persona Composition

### 13.1 Runtime Option Fallbacks

| Option | Fallback Chain |
|---|---|
| Model | `opts.model` → `CHIRALITY_GLOBAL_MODEL` or instruction-root frontmatter → runtime default |
| Tools | `opts.tools` → persona frontmatter → runtime default |
| Max turns | `opts.maxTurns` → persona frontmatter → runtime default |
| Mode | request/session mode → runtime default |
| Persona | request/session persona → hardcoded `WORKING_ITEMS` default when empty or missing |

Unknown option keys MUST be ignored with warnings rather than silently mutating behavior.

### 13.2 Persona Composer

The persona composer builds system prompt or appended system prompt from:

- Chirality governance preface;
- selected `agents/AGENT_<persona>.md` content;
- working-root summary;
- mode policy;
- permitted tool surface;
- professional-boundary reminders.

Boot fingerprints SHOULD include hashes for persona content, governance preface, mode, adapter tool names/versions, permission-policy version, settings-source posture, MCP server versions, and subagent policy version.

---

## 14. Adapter Tool Surface and Chirality MCP Tools

### 14.1 Tool Naming

First-adapter SDK built-ins map to SDK names where available:

| Chirality concept | SDK built-in candidate |
|---|---|
| Read file | `Read` |
| List files | `LS`, `Glob` |
| Search files | `Grep` |
| Write file | `Write` |
| Edit file | `Edit` |
| Shell command | `Bash` |

Chirality-specific deterministic operations use `mcp__chirality__*` names.

### 14.2 Initial Chirality MCP Tools

| Tool | Purpose | Initial mode |
|---|---|---|
| `mcp__chirality__status_read` | Read `_STATUS.md`. | Read. |
| `mcp__chirality__status_transition` | Apply authorized lifecycle transition with approval SHA where required. | Write, gated. |
| `mcp__chirality__deps_read` | Read and validate `Dependencies.csv`. | Read. |
| `mcp__chirality__deps_write` | Append/update dependency rows preserving v3.1 schema. | Write, gated. |
| `mcp__chirality__scope_scan` | Run bounded workspace scope scan. | Read. |
| `mcp__chirality__scaffold` | Wrap scaffold service or dry-run preview. | Gated. |

### 14.3 Tool Surface Rules

- Unknown `opts.tools` names MUST produce structured validation errors.
- Tool ordering MUST be deterministic.
- Denied tools SHOULD be omitted from model context where possible.
- `allowedTools` MUST NOT be treated as a restriction boundary by itself.
- Explicit hard-deny precedence, `disallowedTools`, `permissionMode`, `canUseTool`, and hooks enforce restrictions.

---

## 15. Permission Modes and Hooks

### 15.1 Provisional Chirality-to-First-Adapter Mapping

| Chirality mode | First-adapter posture | Chirality overlay |
|---|---|---|
| `readOnly` | Prefer SDK `plan` or `dontAsk` with read tools pre-approved. | Deny write/edit/bash/network-capable tools and unexpected tools. |
| `workspaceWrite` | SDK `acceptEdits` only after write hooks pass; otherwise default with explicit approvals. | Enforce project-root containment, instruction-root block, symlink rejection, and provenance. |
| `dontAsk` | SDK `dontAsk` if available or equivalent deny-without-prompt overlay. | Pre-approve exact safe tools; everything else denies without prompting. |
| `ask` | SDK default with `canUseTool`. | Present UI approval for governed writes/shell; persist decision before returning SDK allow/deny. |
| `bypass` | SDK `bypassPermissions` only in developer-local mode. | Still apply explicit hard-deny rules, disallowed tools, path hooks, instruction-root protection, and subagent governance. |

### 15.2 Required Hooks

| Hook | Required Behavior |
|---|---|
| Path containment | Deny filesystem operations outside active project root. |
| Instruction-root protection | Deny writes under instruction root. |
| Symlink write rejection | Deny symlink writes in initial policy. |
| Write budget | Enforce output/result storage policy. |
| Provenance append | Record safe provenance/run evidence where policy requires. |
| PreCompact mirror | Persist compaction boundary when available. |
| Stop/finalization | Persist terminal outcome. |
| Subagent governance | Gate `Agent` tool through `evaluateSubagentGovernance`. |

Hook failures fail closed for write, shell, domain, and subagent actions.

---

## 16. Attachments, API Keys, and Network Policy

### 16.1 Attachments

Supported extensions:

- `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, `.csv`

Server-side resolver MUST enforce:

- path validation;
- regular-file check;
- symlink rejection;
- extension allowlist;
- readability;
- per-file 10 MB limit;
- total raw-byte 18 MB per-turn limit.

Partial attachment failure is non-fatal when executable content remains. If all attachments fail and user text is empty, the request fails with `ATTACHMENT_FAILURE`.

### 16.2 API Key Store

Electron storage:

```text
app.getPath('userData')/credentials/api-key.enc
```

Rules:

- Use Electron `safeStorage`.
- Do not write key material to working root.
- Do not log key material.
- Do not persist key material in runtime events.
- Status may report source: `ui`, `env`, or `none`.

### 16.3 Network Policy

- Renderer outbound traffic is allowlisted for loopback and the current shipped Anthropic API path.
- Node/provider/SDK calls must not silently broaden network policy.
- Provider-adapter generality is approved strategically, but concrete non-Anthropic providers, remote MCP, plugins, and network-capable tools require bounded governed future implementation scope.

---

## 17. API Requirements

### 17.1 Harness APIs

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/harness/session/create` | POST | Create session bound to `projectRoot`, persona, and mode. |
| `/api/harness/session/boot` | POST | Boot session and persist boot metadata. |
| `/api/harness/session/list` | GET | List sessions for normalized project root. |
| `/api/harness/session/[id]` | GET/DELETE | Retrieve or delete session. |
| `/api/harness/session/[id]/events` | GET | Replay the session's append-only HarnessEvent stream. |
| `/api/harness/turn` | POST | Execute turn and stream UI events over SSE. |
| `/api/harness/interrupt` | POST | Interrupt active turn. |
| `/api/harness/scaffold` | POST | Scaffold execution root from decomposition markdown. |
| `/api/harness/permission` | POST | Resolve the governed permission decision for a pending tool request. |
| `/api/harness/agents` | GET | Return the packaged agent roster used by the runtime shell. |

Existing route shapes remain stable during adapter adoption and TurnEngine extraction.

### 17.2 Workspace APIs

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/working-root/validate` | POST | Validate and normalize working root. |
| `/api/working-root/tree` | GET | Return bounded file tree. |
| `/api/working-root/scope` | GET | Scan deliverables and knowledge types. |
| `/api/project/deliverables` | GET | Return deliverables plus knowledge decomposition metadata. |
| `/api/working-root/deliverable/status` | GET | Read `_STATUS.md` snapshot. |
| `/api/working-root/deliverable/status/transition` | POST | Apply allowed lifecycle transition. |
| `/api/working-root/deliverable/dependencies` | GET/PUT | Read/write `Dependencies.csv`. |

---

## 18. Domain Engine Future Specification Boundary

D-APP-49 through D-APP-52 authorize a bounded staged surface: source types and guards, a closed profile registry, ruled read tools, and pec-scoped loopback propose/refresh/validate tools. The endpoint families below, operation apply, direct protected-path writes/hooks, and general domain-runtime activation remain provisional future interfaces. No staged or future surface implies automated professional acceptance or direct protected-model writes.

Candidate endpoint families:

- `/api/domain/profiles/list`
- `/api/domain/profiles/validate`
- `/api/domain/artifacts/scan`
- `/api/domain/operations/propose`
- `/api/domain/operations/validate`
- `/api/domain/operations/apply`

Future profiles MUST define protected paths, proposal paths, operations, artifact types, deterministic adapter manifests, and boundary notices. Applying a domain operation requires explicit human acceptance.

---

## 19. Validation Checklist

### 19.1 Required Local Checks

From `frontend/`:

```bash
npm run test
npm run typecheck
npm run harness:validate:premerge
npm run instruction-root:integrity
```

Packaging:

```bash
npm run desktop:dist
```

Expected packaging outputs:

- `frontend/dist/Chirality-0.1.0-arm64.dmg`
- `frontend/dist/mac-arm64/Chirality.app`
- `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`

### 19.2 Section 8 Validation

Section 8 validation verifies baseline behavior:

- server reachable;
- session CRUD;
- boot error taxonomy;
- smoke stream ordering;
- session persistence and resume continuity;
- permissions behavior under current validation markers;
- interrupt behavior;
- SDK-native stream handling with no legacy parser regressions.

### 19.3 Section 9 Runtime Validation IDs

As runtime phases land, add:

- `section9.runtime_engine_contract`
- `section9.adapter_turn_engine_event_log`
- `section9.adapter_message_mapper`
- `section9.session_event_replay`
- `section9.reliance_boundary_register`
- `section9.settingsources_isolation`
- `section9.sdk_session_link_resume`
- `section9.permission_overlay_hard_deny_precedence`
- `section9.tool_runtime_read_file`
- `section9.chirality_mcp_status_dependencies`
- `section9.path_containment_hook`
- `section9.instruction_root_protection_hook`
- `section9.tool_result_budget`
- `section9.context_compaction_boundary`
- `section9.subagent_governance_hook`
- `section9.domain_profile_validation`

### 19.4 Manual Release Verification

For macOS DMG:

- binary is arm64;
- `LSMinimumSystemVersion` is `15.0.0` or later;
- signing posture is unsigned/adhoc as scoped;
- app resources contain required instruction-root assets;
- working-root selector is available;
- current loopback plus Anthropic network guardrails remain in force;
- no-live first-adapter SDK resolver/HOME proof passes from package layout and mounted DMG;
- SDK subprocess/binary is executable from package layout;
- live packaged provider turn and transcript creation remain unapproved until a later ruling.

---

## 20. Filesystem-Safe Labels

`Sanitize(name)`:

1. Replace `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|` with `-`.
2. Collapse consecutive whitespace to one space.
3. Trim leading/trailing whitespace.

Folder names:

- Package: `{PKG-ID}_{Sanitize(PackageName)}`
- Deliverable: `{DEL-ID}_{Sanitize(DeliverableName)}`

Canonical unsanitized names are stored in `_CONTEXT.md` and decomposition records.
