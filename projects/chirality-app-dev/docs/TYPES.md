# TYPES — Domain Vocabulary and Runtime Type Targets

**Status:** vNext governance rewrite aligned to the approved `docs/PRD.md` dated 2026-05-20
**Product:** Chirality desktop harness and bundled agent operating system

This document is the authoritative vocabulary reference for Chirality App. It defines canonical entities, stable identifier formats, enumerated values, agent roles, runtime vocabulary, and type targets used by governance documents, agent instructions, implementation code, validation scripts, and release runbooks.

Where a term is used differently elsewhere, this document governs unless a higher-authority source has been explicitly amended.

---

## 1. Project Hierarchy

The project hierarchy is flat:

```text
{EXECUTION_ROOT}/
└── PKG-XX_{PkgLabel}/
    └── 1_Working/
        └── DEL-XX-YY_{DelLabel}/
```

### 1.1 Package

A **Package** is a flat partition of project scope. Packages do not nest. Each package contains references, active working deliverables, checking staging, and issued artifacts.

### 1.2 Deliverable

A **Deliverable** is a unit of production within a package. Each deliverable has a stable ID, lifecycle state, context file, dependency record, reference record, and optional document kit or specialized artifacts.

### 1.3 Artifact

An **Artifact** is a tangible output such as a markdown document, CSV register, tool-root snapshot, domain proposal, runtime event file, or validation summary. Artifacts are authoritative only when placed in the proper project location and accepted by the relevant process.

### 1.4 Tool Root

A **Tool Root** is a project-level directory for derived outputs such as `_Aggregation/`, `_Change/`, `_Coordination/`, `_Decomposition/`, `_Estimates/`, `_Reconciliation/`, `_Archive/`, `_Scripts/`, and `_Sources/`.

### 1.5 Instruction Root

The **Instruction Root** is the release-managed app resource tree containing governance documents, agent instructions, and framework materials. Ordinary project execution must not mutate it.

### 1.6 Working Root / `projectRoot`

The **Working Root** is the user-selected local filesystem location where project execution state, sessions, artifacts, and git history live.

### 1.7 Project Truth

**Project Truth** is gate-relevant project state represented in versioned project files. Runtime transcripts, chat drafts, UI state, API keys, SDK transcripts, and caches are not project truth unless a governed process imports relevant content into project files.

### 1.8 Runtime Audit Mirror

The **Runtime Audit Mirror** is the product-owned runtime event log, normally `.chirality/sessions/<sessionId>/events.jsonl`, used to reconstruct and review accepted turns, model output, permissions, tool activity, hooks, compaction boundaries, and subagent lifecycle.

---

## 2. Stable Identifiers

Identifiers are assigned once and persist across renames and path changes.

| Entity | Format | Example | Assigned by |
|---|---|---|---|
| Package | `PKG-XX` or `PKG-XXX` | `PKG-01` | Decomposition / human approval |
| Deliverable | `DEL-XX-YY` or `DEL-XXX-YY` | `DEL-01-01` | Decomposition / human approval |
| Dependency | `DEP-XX-YY-NNN` | `DEP-01-01-001` | DEPENDENCIES workflow/tool |
| Scope Item | `SOW-NNN` | `SOW-003` | Decomposition |
| Objective | `OBJ-NNN` | `OBJ-001` | Decomposition |
| Session | implementation-generated stable ID | `sess_...` | Harness session manager |
| Turn | implementation-generated stable ID | `turn_...` | `TurnEngine` |
| Runtime Event | implementation-generated stable ID | `evt_...` | `SessionEvents` |
| Subagent Run | implementation-generated stable ID | `subrun_...` | `SubagentGovernanceBridge` |
| Domain Profile | `domain-profile-id` string | `openpipestress` | Future domain profile author |
| Operation Proposal | implementation-generated stable ID | `op_...` | Future domain operation workflow |

### 2.1 Folder Labels

Folder names combine stable ID and sanitized label:

- Package: `{PKG-ID}_{Sanitize(PackageName)}`
- Deliverable: `{DEL-ID}_{Sanitize(DeliverableName)}`

The unsanitized canonical name belongs in `_CONTEXT.md` or the governing decomposition document.

### 2.2 ID Rules

- `XX`, `YY`, and `NNN` are zero-padded numeric sequences.
- Deliverable IDs use hyphen separators, not dots.
- Stable IDs must not change unless a human explicitly approves renumbering.
- Runtime event IDs are unique per event and never reused.

---

## 3. Agent Roles and Authority

### 3.1 Agent Types

| Type | Name | Role | Scope |
|---|---|---|---|
| **Type 0** | Supervising Architect | Aligns the human and workflow, supervises Agent 1 managers, brokers cross-package coordination, and returns consequential decisions. HELP_HUMAN is the sole canonical instance role. | Cross-manager and cross-package. |
| **Type 1** | Manager | Owns one management scope, derives work graphs, routes specialists, coordinates evidence, and validates fan-in. | Package, project workflow, source campaign, or bounded management domain. |
| **Type 2** | Specialist | Executes one sealed brief and returns outputs plus evidence without delegating. | Deliverable-local, page/sheet-local, or narrow task. |

### 3.2 Agent Classification Properties

| Property | Values | Meaning |
|---|---|---|
| `AGENT_CLASS` | `PERSONA`, `TASK` | Persona agents run interactive sessions; task agents run straight-through or delegated work. |
| `INTERACTION_SURFACE` | `chat`, `INIT-TASK`, `spawned`, `both` | How the agent is invoked. |
| `WRITE_SCOPE` | `repo-wide`, `project-level`, `deliverable-local`, `tool-root-only`, `workspace-scaffold-only`, `repo-metadata-only`, `none` | Permitted write area. |
| `BLOCKING` | `never`, `allowed` | Whether the agent may pause for human input. |

### 3.3 Authority Model

Delegation flows downward; evidence, coordination notices, and escalation flow
upward. Standards constrain every layer but do not occupy Agent 0.

- Type 0 aligns the human, scope, stakes, managers, and decision points.
- Type 1 prepares, routes, and reconciles work.
- Type 2 executes bounded work.
- Humans approve, issue, sign, seal, and accept reliance.

Agent 0 delegates only to named Agent 1 roles. Agent 1 delegates only to TASK,
allowed ephemeral generalists, or approved dedicated Agent 2 roles. Agent 2
does not delegate. A Type 1 agent cannot issue work for reliance. No agent can
approve professional work.

### 3.4 Persona Alias Terms

| UI Alias | Canonical Agent |
|---|---|
| `HELP` | `HELP_HUMAN` |
| `ORCHESTRATE` | `PROJECT_SETUP` |
| `AGENTS` | `HELPS_HUMANS` |
| `DEPENDENCIES` | `EVALUATION` |

---

## 4. UI Navigation Vocabulary

### 4.1 Matrix Rows

| Value | Meaning | Destination |
|---|---|---|
| `NORMATIVE` | Guidance, orchestration, standards, and review support. | Mounted loop-persona intent; tertiary forms stay sidebar-reachable. |
| `OPERATIVE` | Pipeline execution categories. | PIPELINE |
| `EVALUATIVE` | Review, evaluation, change, and research support. | Mounted loop-persona intent; tertiary forms stay sidebar-reachable. |

### 4.2 Matrix Columns

| Value | Meaning |
|---|---|
| `GUIDING` | Helps orient or define the work. |
| `APPLYING` | Helps execute or apply the work. |
| `JUDGING` | Helps inspect, assess, or manage work items. |
| `REVIEWING` | Helps aggregate, reconcile, or review work. |

### 4.3 Matrix Cells

| Row | Guiding | Applying | Judging | Reviewing |
|---|---|---|---|---|
| `NORMATIVE` | `HELP` | `ORCHESTRATE` | `WORKING_ITEMS` | `REVIEW` |
| `OPERATIVE` | `DECOMP*` | `PREP*` | `TASK*` | `AUDIT*` |
| `EVALUATIVE` | `AGENTS` | `DEPENDENCIES` | `CHANGE` | `RESEARCH` |

### 4.4 Pipeline Terms

| Term | Values | Meaning |
|---|---|---|
| `PipelineCategory` | `DECOMP*`, `PREP*`, `TASK*`, `AUDIT*` | Top-level operative category. |
| `TaskScopeMode` | `DELIVERABLES`, `KNOWLEDGE_TYPES` | Dynamic scope mode for `TASK*`. |
| `KnowledgeTypeOption` | `Datasheet`, `Specification`, `Guidance`, `Procedure`, `Dependencies`, `References`, `Context`, `Status`, `Semantic`, `Memory` | File-type buckets discovered from deliverable content. |
| `DisabledOption` | any visible but non-selectable option | A coming-soon or unsupported variant intentionally shown without enabling runtime selection. |

---

## 5. Deliverable Lifecycle Vocabulary

Lifecycle states are tracked in `_STATUS.md`.

```text
OPEN → INITIALIZED → SEMANTIC_READY → IN_PROGRESS → CHECKING → ISSUED
```

| State | Meaning |
|---|---|
| `OPEN` | Folder exists with minimum viable fileset; content is not yet initialized. |
| `INITIALIZED` | Document kit has been drafted or initialized. |
| `SEMANTIC_READY` | Semantic lens or semantic placeholder has been generated. |
| `IN_PROGRESS` | Active human and/or agent work is underway. |
| `CHECKING` | A frozen candidate is under review against a declared basis; a human declares the checking basis and freezes the candidate. |
| `ISSUED` | Accepted baseline, approved and issued by a human; subsequent changes only via the governed scope-change process. |

Lifecycle states are governed production and change-control regimes with maturity/readiness entry conditions, not percentage-complete scores. Advancing `IN_PROGRESS → CHECKING → ISSUED` carries maturity meaning while the states define which changes are lawful and under what control; entry conditions and the human-authorized reversal transitions (`CHECKING → IN_PROGRESS`; `ISSUED → IN_PROGRESS` via the governed scope-change process only) are specified in `SPEC.md`.

Stage gates such as 30%, 60%, 90%, or IFC are project milestones, not lifecycle states.

The `INITIALIZED → SEMANTIC_READY` transition is optional. If semantic lensing is skipped, deliverables may transition directly from `INITIALIZED → IN_PROGRESS` under the authorized actor rules in `SPEC.md`.

---

## 6. Dependency Vocabulary

### 6.1 Dependency Classes

| Class | Meaning | Graph Role |
|---|---|---|
| `ANCHOR` | Connects a deliverable to a definition or traceability node. | Tree edge. |
| `EXECUTION` | Captures information flow, prerequisite, handoff, interface, or constraint. | DAG edge. |

### 6.2 Anchor Types

| Value | Meaning |
|---|---|
| `IMPLEMENTS_NODE` | Parent definition node; normally one per deliverable. |
| `TRACES_TO_REQUIREMENT` | Requirement trace link; zero or more per deliverable. |
| `NOT_APPLICABLE` | Used for execution rows. |

### 6.3 Direction

| Value | Meaning |
|---|---|
| `UPSTREAM` | The host deliverable requires information from the target. |
| `DOWNSTREAM` | The host deliverable produces information for the target. |

Legacy `INBOUND` normalizes to `UPSTREAM`; legacy `OUTBOUND` normalizes to `DOWNSTREAM`.

### 6.4 Dependency Types

| Value | Meaning |
|---|---|
| `PREREQUISITE` | Required input or approval before work can proceed. |
| `INTERFACE` | Explicit data or artifact exchange. |
| `HANDOVER` | Output consumed as input by another work item. |
| `CONSTRAINT` | Explicit constraint or condition. |
| `ENABLES` | Host deliverable enables downstream work. |
| `OTHER` | Catch-all; required for anchor rows. |

Legacy `COORDINATION` and `INFORMATION` are not emitted in new extractions.

### 6.5 Target Types

| Value | Meaning |
|---|---|
| `DELIVERABLE` | Another deliverable in the project. |
| `PACKAGE` | A package. |
| `WBS_NODE` | Work breakdown or scope node. |
| `REQUIREMENT` | Requirement, SOW item, objective, or acceptance item. |
| `DOCUMENT` | External or reference document. |
| `EQUIPMENT` | Physical equipment or asset. |
| `EXTERNAL` | External entity, organization, code, standard, or interface. |
| `UNKNOWN` | Target cannot be confidently resolved. |

### 6.6 Provenance and Status Terms

| Dimension | Values | Meaning |
|---|---|---|
| `Explicitness` | `EXPLICIT`, `IMPLICIT` | Whether the dependency is directly stated. |
| `Confidence` | `HIGH`, `MEDIUM`, `LOW` | Strength of evidence. |
| `Origin` | `DECLARED`, `EXTRACTED` | Human-declared versus agent/tool-extracted. |
| `SatisfactionStatus` | `TBD`, `PENDING`, `IN_PROGRESS`, `SATISFIED`, `WAIVED`, `NOT_APPLICABLE` | Closure lifecycle. |
| `Status` | `ACTIVE`, `RETIRED` | Extraction lifecycle. |

---

## 7. Runtime and Session Vocabulary

### 7.1 Runtime Engine Terms

| Term | Meaning |
|---|---|
| `AgentEnginePort` | Product-owned boundary for running a turn, yielding UI events, recording canonical events, enforcing permissions, managing session linkage, and terminal outcomes. |
| `RuntimeEngineContract` | The formal expectations an engine adapter must satisfy before use. |
| `EngineAdapter` | Provider/SDK-specific implementation behind `AgentEnginePort`; translates provider-specific events, sessions, permissions, and tool names into Chirality-owned contracts. |
| `ProviderAdapter` | Concrete integration layer for an external agent provider or provider SDK. |
| `FirstAdapter` | The current concrete Claude Agent SDK / Anthropic adapter path. It is the first shipped path, not the strategic ceiling. |
| `EngineSelection` | Per-session or governed-child selection of `adapterId`, `providerId`, and exact `model`; it is persisted and never silently replaced after turn acceptance. |
| `EngineDescriptor` | Adapter identity, provider identity, package attribution, and declared capabilities used by preflight and conformance. |
| `PiAdapter` | D-APP-72-bounded in-process Pi `0.80.10` adapter. Initially valid only with authenticated `127.0.0.1` oMLX and a governed read-only Agent 2 child. |
| `oMLXProvider` | Local OpenAI-compatible provider endpoint authorized only at authenticated `http://127.0.0.1:8000/v1` by default; exact model IDs come from `/v1/models`. |
| `EngineConformanceSuite` | Tests proving an adapter satisfies Chirality contracts. |
| `TurnEngine` | Runtime service that owns a single turn lifecycle and invokes the engine through the product-owned boundary. |
| `SdkOptionsBuilder` | Deterministic constructor for first-adapter SDK options from Chirality state and policy. |
| `SdkMessageMapper` | First-adapter mapper from SDK stream messages into browser `UIEvent`s and persisted `HarnessEvent`s. |
| `PersonaComposer` | Builder for system prompt / appended prompt from instruction root, active persona, mode, and working-root policy. |
| `RelianceBoundaryRegister` | Record of product-critical semantics and their enforcement surfaces. |
| `PiPatternCorpus` | Historical/reference use of Pi patterns under SCA-APP-001. D-APP-72 / SCA-APP-002 adds one prospective bounded runtime exception and does not convert the corpus into general Pi adoption or feature-parity authority. |

### 7.2 Session Terms

| Term | Meaning |
|---|---|
| `SessionRecord` | Metadata record for a harness session. |
| `sessionId` | Chirality session identifier. |
| `engineSessionId` | Provider-neutral adapter session identifier exposed by the runtime boundary when available. |
| `sdkSessionId` | SDK session identifier used for resume; adapter metadata, not Chirality identity. |
| `sdkProjectKey` | SDK project key or encoded cwd, if exposed. |
| `sdkTranscriptPath` | Path to SDK transcript when applicable. Secondary to Chirality audit events. |
| `sdkSessionStoreKey` | Key used by a configured SDK session store or mirror. |
| `sdkConfigDir` | Explicit SDK config directory when redirected to project-controlled storage. |
| `events.jsonl` | Append-only Chirality runtime audit mirror. |
| `session.json` | Session metadata/index file. |
| `artifacts/` | Session-local artifact folder for large tool outputs and child-run outputs. |

### 7.3 `HarnessEvent` Type Target

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

Initial event categories:

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

Later event categories:

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
- `coordination.notice`
- `coordination.update`
- `coordination.acknowledged`
- `runtime.mirror.error`

### 7.4 Browser `UIEvent` Terms

Browser-facing turn streams use compact UI events. Provider/SDK messages are not the UI contract.

SSE event names:

- `session:init`
- `chat:delta`
- `chat:complete`
- `tool:result`
- `session:complete`
- `turn:error`
- `process:exit`
- `harness:event`

---

## 8. Permission and Tool Vocabulary

### 8.1 Chirality Permission Modes

| Mode | Meaning |
|---|---|
| `readOnly` | Read-only tools only; write/edit/bash/network-capable tools denied. |
| `workspaceWrite` | Governed writes inside project root may be allowed after hooks and policy pass. |
| `dontAsk` | Deny unapproved actions rather than prompting. |
| `ask` | Application may request interactive approval for governed actions. |
| `bypass` | Developer-local escape hatch only; never shipped ordinary mode; still subject to explicit Chirality hard denies. |

Capability policy is the Chirality-owned policy that decides which tools and capabilities
are exposed and executable for a session, persona, mode, provider adapter, and validation
state. Explicit hard-deny precedence overrides allows at reliance boundaries, secrets,
protected paths, release/professional claims, destructive actions, and unvalidated
provider/network expansion.

### 8.2 Permission Decision

```ts
type HarnessPermissionDecision = {
  decisionId: string;
  sessionId: string;
  turnId?: string;
  toolName: string;
  decision: 'allow' | 'deny' | 'ask';
  reason: string;
  source: 'sdk-option' | 'sdk-callback' | 'chirality-policy' | 'hook' | 'human' | 'prompt-support';
  decidedAt: string;
  safeMetadata?: Record<string, unknown>;
};
```

`ask` is an application-level state. SDK callbacks ultimately return an allow or deny decision.

### 8.3 Tool Surface Terms

| Term | Meaning |
|---|---|
| `SDK built-in tool` | Tool supplied by the current first-adapter SDK, such as `Read`, `Glob`, `Grep`, `LS`, `Write`, `Edit`, or `Bash` where available. |
| `Chirality MCP tool` | In-process deterministic Chirality operation exposed through SDK MCP tooling with `mcp__chirality__*` naming. |
| `allowedTools` | SDK option that may auto-approve tools; not by itself a restriction boundary. |
| `disallowedTools` | SDK option or Chirality wrapper policy used to prevent tool use or remove tools from context; participates in explicit hard-deny precedence. |
| `canUseTool` | SDK callback or equivalent hook path used by Chirality to mediate permission decisions. |
| `ToolResultStore` | Chirality artifact and preview policy for tool outputs. |

### 8.4 Chirality MCP Tool Names

Initial in-process MCP tool names should use this namespace:

- `mcp__chirality__status_read`
- `mcp__chirality__status_transition`
- `mcp__chirality__deps_read`
- `mcp__chirality__deps_write`
- `mcp__chirality__scope_scan`
- `mcp__chirality__scaffold`
- `mcp__chirality__delegate_agent`
- `mcp__chirality__report_coordination_notice`
- `mcp__chirality__send_agent_update`
- `mcp__chirality__ack_agent_update`

Future domain tools use `mcp__chirality__domain_*` only after a governed domain-profile amendment.

### 8.5 Hook Terms

| Hook Term | Meaning |
|---|---|
| `PreToolUse` | Runs before tool execution; can deny write/shell/domain/subagent actions. |
| `PostToolUse` | Runs after successful tool execution; may record provenance, budgets, and summaries. |
| `PostToolUseFailure` | Runs after tool failure; records triage and safe diagnostics. |
| `PreCompact` | Records compaction boundary before SDK/model context compaction where available. |
| `Stop` | Finalizes terminal turn event. |
| `SubagentStart` / `SubagentStop` | Records governed child-run lifecycle where supported. |

---

## 9. Provider/SDK Adapter Vocabulary

| Term | Meaning |
|---|---|
| Claude Agent SDK | Current first concrete hosted runtime substrate for generic agent-loop mechanics; implementation substrate, not product identity or strategic ceiling. |
| SDK transcript | SDK-managed session transcript, secondary to Chirality audit mirror. |
| `settingSources` | SDK option controlling filesystem settings load. Shipped builds use `[]`. |
| `SessionStore` | SDK session mirror/storage mechanism when used. Mirror reliability is not assumed to be canonical. |
| `CLAUDE_CONFIG_DIR` | Environment mechanism that may redirect SDK local config/transcript behavior if empirically reliable. |
| `permissionMode` | SDK permission posture translated from Chirality mode plus capability policy and explicit hard-deny precedence. |
| `bypassPermissions` | SDK mode not permitted in shipped ordinary workflows. |
| Pi pattern corpus / bounded adapter | D-APP-01 and D-APP-02 remain historical and govern all unamended Pi scope. D-APP-72 / SCA-APP-002 prospectively permits only Pi `0.80.10` in-process after Electron `43.1.1`, authenticated loopback oMLX, and a governed read-only Agent 2 child. |

SDK terms belong at the adapter boundary. Public Chirality APIs and canonical events use Chirality terms.

---

## 10. Multi-Agent Runtime Vocabulary

```ts
type ChildRunRecord = {
  schema: 'chirality-agent-runs/v2';
  orchestrationRunId: string;
  planVersion: string;
  childInstanceId: string;
  parentSessionId: string;
  parentTurnId?: string;
  parentRole: string;
  parentAgentType: 0 | 1;
  childRole: string;
  childAgentType: 1 | 2;
  childKind: 'named' | 'task' | 'generalist';
  projectRoot: string;
  mode: string;
  status: 'LAUNCHED' | 'RUNNING' | 'COMPLETED' | 'FAILED' | 'BLOCKED';
  approvalRef: string;
  instructionPath?: string;
  instructionHash?: string;
  briefHash: string;
  declaredContext: string[];
  declaredTools: string[];
  allowedWriteTargets: string[];
  requiredReturnMarkers: string[];
  outputArtifactPath?: string;
  adapter?: {
    adapterName: string;
    adapterSessionId?: string;
    adapterAgentId?: string;
    adapterTaskId?: string;
    adapterToolUseId?: string;
    adapterTranscriptKey?: string;
  };
};
```

| Term | Meaning |
|---|---|
| `ManagedDelegationService` | Authoritative hierarchy, seal, capability, path, write-overlap, and durable-record policy for managed delegation. |
| `evaluateSubagentGovernance` | Fail-closed gate retained for rejected legacy SDK Agent requests; it no longer launches children. |
| Named child | Agent 1 or Agent 2 instantiated from its actual `AGENT_*.md` and recorded instruction hash. |
| Generalist child | Ephemeral Agent 2 instantiated from the Agent 2 base contract and sealed brief without a persistent role file. |
| Parent session | Session requesting delegation. |
| Child run | Governed managed-session execution record. |
| Work graph | Versioned nodes, dependencies, concurrency, ownership, returns, and gates for one orchestration run. |
| Coordination notice | Typed child-to-parent information with claim status, evidence, affected scopes, and requested action. |
| Parent update | Immutable relay or versioned amendment delivered to one direct child at a safe turn boundary. |
| Update acknowledgment | Child response: `INCORPORATED`, `NO_EFFECT`, `BLOCKED`, `CONFLICT`, or `HUMAN_DECISION_REQUIRED`. |
| Return markers | Brief-declared structural markers that a completed return must contain before fan-in can accept it. |
| Context sealed | Required governance condition confirming bounded context. |
| Pipeline run approved | Required governance condition for Type 2 task invocation. |
| Approval reference | Citation to the applicable human approval record; runtime validates presence/structure, not the human act. |

Coordination claim statuses are distinct from epistemic and lifecycle status:
`PROVISIONAL` is unvalidated; `VALIDATED` requires `validationRef`; `ACCEPTED`
requires `humanAcceptanceRef` to a human act; `DISPUTED` preserves conflict.
Every `RELAY` cites its source notice and preserves that status. These values
do not mechanically accept a child return or advance lifecycle state.

Every work graph includes `nodes`, `edges`, `concurrencyEligibility`,
`expectedReturns`, `fanInGates`, and `humanDecisionPoints`. Every AMEND/REPLAN
records `amendmentCategories` and a stable amendment or plan version; scope,
risk, authority, shared-write, and acceptance categories require a human
ruling reference.

---

## 11. Domain Engine Vocabulary — Future Scope

This section is an app-dev vocabulary target that conforms to framework-root
`agents/AGENT_DOMAIN_ENGINE.md` at commit `77a327727605f05da5f304288f1ddd87dc09659d`.

> **Forward note (2026-07-12 — D-APP-49 through D-APP-52 ruled staged surface):**
> The prior documentation-only boundary is amended forward: the `DomainEngineProfile` /
> `OperationProposal` vocabulary below now has inert source-type mirrors (types + type guards
> only; no behavior, persistence, UI, I/O, or imports) in
> `frontend/packages/harness-contract/src/domain-profile.ts` and
> `frontend/packages/harness-contract/src/operation-proposal.ts`. D-APP-50 through D-APP-52
> also authorize the closed profile registry, ruled read tools, and pec-scoped loopback
> propose/refresh/validate tools. Operation apply, `/api/domain/*` endpoints, direct
> protected-path writes/hooks, and general domain-runtime activation remain future and gated.

### 11.1 `DomainEngineProfile`

`DomainEngineProfile` is the profile record that defines a domain engine boundary before any governed
read-only or tool-integrated workflow is claimed. App-dev may expose camelCase documentation views, but
the canonical framework shape is the snake_case profile form below.

| Field | Meaning |
|---|---|
| `schema_version` | Profile schema version. |
| `id` | Stable domain engine profile ID. |
| `name` | Human-readable domain engine name. |
| `engine_type` | Domain classification, generic across engines. |
| `profile_version` | Version of this profile record; distinct from the engine executable version. |
| `profile_status` | One of `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`. Integrated workflows require `ADOPTED`; `MANUAL_BRIDGE` may explicitly record a missing profile. |
| `integration_level` | One of `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE`; do not skip levels. |
| `domain_root_patterns` | Domain-engine-owned roots or globs. |
| `authoritative_artifacts` | Engine-owned artifacts that define domain truth. |
| `chirality_readable_artifacts` | Manifests, summaries, warnings, assumptions, reports, or other artifacts safe for agents to read and cite. |
| `protected_write_paths` | Paths or globs agents must not directly write. |
| `agent_writable_paths` | Profile-approved proposal, review, checklist, TBD, or reconciliation paths where agents may write under explicit scope. |
| `deterministic_tools` | Declared tool contracts, each with `id`, `mode`, `requires_human_confirmation`, `validate_result_schema`, and `apply_result_schema`. Schema refs may be explicit `TBD`; they are not inferred from chat. |
| `operation_proposal_contract` | Contract for proposal lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements. |
| `professional_boundary` | Structured boundary language, including claims agents must not make without a cited human authoritative record. |
| `open_issues` | `TBD` items and blockers that prevent stronger closure. |

### 11.2 `OperationProposal`

`OperationProposal` is a structured proposed model/domain change. It remains non-binding project evidence
until deterministic checks, required human gates, and domain-engine-controlled apply or external terminal
acceptance records exist.

| Field | Requirement |
|---|---|
| `proposal_id` | Stable proposal ID. |
| `profile_id` | Stable ID of the active domain engine profile. |
| `base_state` | Base model state or domain state, if applicable; otherwise explicit `TBD`. |
| `operation_name` | Declared operation name from the active profile or deterministic tool contract. |
| `status` | Constant proposal-only classification; lifecycle carries review and application progression. |
| `lifecycle` | One of `draft | ready_for_review | accepted | rejected | applied`. `accepted` and `applied` require a human approval record bound to a git SHA per K-AUTH-2 and, where the engine has a terminal human-accepted lifecycle state, that external record. |
| `created_at` | Creation timestamp. |
| `created_by` | Actor that created the proposal. |
| `input_refs` | Evidence references such as manifests, warnings, run IDs, comparison IDs, schema refs, or file paths. |
| `intended_changes` | Proposed domain changes, each bounded to the profile and operation. |
| `deterministic_checks` | Declared checks to run before review or application, with result schema refs or explicit `TBD`. |
| `expected_output_refs` | Expected artifacts, IDs, summaries, validation records, or export refs. |
| `risks` | Known risks, including whether the operation can be fully checked by the engine. |
| `assumptions` | Unresolved assumptions, distinct from risks. |
| `blockers` | Unresolved blockers preventing acceptance or application. |
| `boundary_notice` | Professional-boundary language preventing claims of approval, certification, sealing, code compliance, ready-for-construction status, or external validation absent a cited human authoritative record. |
| `required_human_gate` | Gate token for the human-owned accept/reject decision; accepted/applied transitions bind to a git SHA per K-AUTH-2. |
| `operation_risk_class` | One of `engine_checkable | engine_silent`. Use `engine_silent` when correctness depends on judgment values or premises the engine cannot independently verify. |
| `provenance_on_judgment_values` | Required provenance for `engine_silent` values or explicit `TBD`. |
| `storage_path` | Path under a profile-approved `agent_writable_paths` entry. |

The active profile identifies `validate_result_schema`, `apply_result_schema`, and
`operation_proposal_contract.deterministic_check_result_schema` for declared deterministic tools. Missing
schemas stay explicit `TBD`; they do not block the canonical field obligation, but they do block accepted
or applied proposal semantics.

### 11.3 Domain Terms

| Term | Meaning |
|---|---|
| Protected path | Authoritative domain-engine artifact path not directly writable by agents. |
| Agent-writable path | Profile-approved folder for proposed changes, summaries, review aids, checklists, TBD registers, or reconciliation notes. |
| Deterministic tool | Declared CLI/API adapter with bounded inputs, outputs, modes, side effects, failure behavior, and result schemas. |
| Boundary notice | Required copy explaining that Chirality does not approve, certify, seal, code-validate, externally validate, or own solver truth. |
| OpenPipeStress fixture | Potential first domain profile fixture, not Chirality core. |

---

## 12. Release and Validation Vocabulary

| Term | Meaning |
|---|---|
| Section 8 validation | Existing harness validation surface for baseline behavior. |
| Section 9 validation | New runtime validation IDs added as vNext phases land. |
| `instruction-root:integrity` | Packaging check verifying required instruction-root resources. |
| `desktop:dist` | Desktop build target producing macOS arm64 DMG. |
| `harness:validate:premerge` | Premerge harness validation script producing stable summary artifact. |
| `settingsources_isolation` | Validation that shipped SDK options do not load ambient user/local settings. |
| `runtime_engine_contract` | Validation that engine adapter satisfies product-owned contract. |
| `sdk_session_link_resume` | Validation that SDK session ID/linkage persists and resumes through Chirality metadata. |

### 12.1 Priorities

| Priority | Meaning |
|---|---|
| `P0` | Required for current release usefulness, safety, or runtime foundation. |
| `P1` | Important for quality, governed operation, or runtime maturity. |
| `P2` | Later hardening, future extension, or desirable capability. |

---


## 13. Coordination Representation Vocabulary

The framework separates **how teams coordinate** from **how the system tracks dependencies**. Deliverable-local registers remain the dependency tracking substrate; `_COORDINATION.md` records the project coordination representation.

| Representation | Meaning |
|---|---|
| `SCHEDULE_FIRST` | Gantt or schedule logic drives sequencing; dependency tracking remains active for blocker detection and audit. |
| `DEPENDENCY_TRACKED` | Dependency graph logic drives sequencing and handoff analysis. |
| `HYBRID` | Schedule-first and dependency-tracked representations are both used. |

## 14. Epistemic Labels

| Label | Meaning |
|---|---|
| `FACT` | Directly observed in source text or deterministic output. |
| `ASSUMPTION` | Reasonable inference that requires validation. |
| `PROPOSAL` | Agent or tool suggestion requiring human decision. |
| `TBD` | Unknown value requiring resolution. |

These labels help separate evidence from inference and prevent plausible invention from becoming project truth.

---

## 13. Shared Runtime Vocabulary

| Term | Meaning |
|---|---|
| **Runtime Daemon** | The one per-user headless Chirality process that exclusively owns engines, credentials, sessions, delegation, tools, turn locks, interruption, and model residency. |
| **Runtime Client** | Desktop, CLI, backend, or embedded UI using the authenticated Unix-socket API without constructing its own runtime. |
| **Project Manifest** | Tracked `chirality.project/v1` registration declaration containing stable project identity and relative authority references, never secrets or machine-specific absolute paths. |
| **Project Registration** | Machine-local binding of a manifest hash to its resolved checkout root, client credential, and approval metadata. It is operational state, not project authority. |
| **Residency Epoch** | Monotonic identifier for one verified primary-local-model residency state, referenced by every local session and AgentRun. |
| **Primary Local LLM** | The sole model the daemon currently manages for local Pi turns; helper, embedding, and reranking models are outside automatic unload authority. |
| **NO_MODEL** | Fail-closed residency state after no model is active or a prior unload succeeded and target load failed. |
| **Required Delegation** | A run contract requiring its Agent 1 to launch and review a specified bounded Agent 2 child; absence yields `REQUIRED_DELEGATION_MISSING`. |
| **Actual Model Attribution** | Recorded adapter/provider/model identity observed for a run. It does not prescribe a durable model-to-role mapping. |
