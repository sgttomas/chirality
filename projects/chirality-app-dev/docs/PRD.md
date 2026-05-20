# PRD - Chirality Desktop Harness

**Status:** Revised product requirements after repository, execution-plan, frontend, and harness-runtime assessment  
**Date:** 2026-05-20  
**Product:** Chirality desktop harness and bundled agent operating system  
**Primary repository/workspace:** `chirality-app-dev`  
**Development source path:** `chirality/projects/chirality-app-dev/frontend` in the complete source tree; `frontend/` in the reviewed archive snapshot  
**Public release snapshot path:** `chirality-app/frontend`, maintained as a release operation rather than the active vNext development source  
**Primary audience:** product owner, engineering, agent-instruction maintainers, reviewers, release operators, and future harness-runtime implementers

---

## 1. Source Basis

This PRD is derived from the attached `chirality-app-dev` archive and two supplied assessment/planning inputs. It is intended to capture the product direction after reviewing the repository-local documents, the package/deliverable execution plan, and the current frontend implementation.

Primary archive-local inputs reviewed:

- `docs/DIRECTIVE.md`
- `docs/CONTRACT.md`
- `docs/SPEC.md`
- `docs/TYPES.md`
- `docs/PLAN.md`
- `docs/DBM_Agent_Instruction_Architecture.md`
- `docs/SE_Design_Analysis.md`
- `docs/START_HERE_AGENT_PATHS.md`
- `docs/CHANGE_PUBLICATION_GUIDANCE_CONSTRAINTS.md`
- `docs/harness/*`
- `docs/ui/UI_POLISH_EXECUTION_PLAN.md`
- `docs/thesis/*`
- `docs/thesis/bigger-picture/*`
- `execution/_Decomposition/ChiralityApp_SoftwareDecomposition_2026-02-21_G7-APPROVED.md`
- `execution/_ScopeChange/*`
- `execution/PKG-*/1_Working/DEL-*/*`
- `frontend/`

Additional assessment/planning inputs reviewed:

- `agent-harness-patterns-from-claw-code-assessment.md`
- `chirality-app-future-development-plan.md`

Important archive-local observation:

- The reviewed archive contains `docs/`, `execution/`, and `frontend/` roots.
- The reviewed archive does **not** include root-level `AGENTS.md`, `README.md`, `agents/`, `WHAT-IS-AN-AGENT.md`, `PROFESSIONAL_ENGINEERING.md`, `tools/REGISTRY.md`, or `examples/` assets, although the frontend instruction-root and packaging code expects several of those resources.
- Therefore this PRD distinguishes between (a) product requirements for the full Chirality source tree and (b) implementation gaps visible in the reviewed archive snapshot.

Authority rule:

- This PRD states product direction and implementation sequence.
- It does not supersede `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `AGENTS.md` when present, accepted execution deliverables, or approved scope-change records.
- If this PRD conflicts with a higher-authority governance source, the higher-authority source controls until a governed product change updates the record.
- The vNext development source should remain the app-development workspace. The public application snapshot is synchronized only through an explicit release operation.

Where documents, execution records, and implementation disagree, this PRD states the product requirement and records the implementation note under **Known Gaps and Risks**. Advisory assessment material is adopted only where it aligns with Chirality's local-first, professional-work, filesystem-native governance model.

---

## 2. Product Summary

Chirality is a desktop harness for running governed AI agents against a user-selected local filesystem workspace. It packages a release-managed instruction root inside the desktop app and keeps all mutable project execution state in a user-selected working root (`projectRoot`).

The product exists to accelerate deliverable-heavy professional work while preserving human authority, provenance, auditability, and filesystem-native state. Agents and deterministic tools may decompose scope, scaffold execution roots, draft document kits, extract dependencies, perform semantic analysis, reconcile across deliverables, support estimates/schedules, and manage change. Outputs remain drafts or decision support until accepted by an accountable human.

Core product thesis:

> Project truth lives in git-tracked plain files. If a decision is not in a versioned file, it does not exist for purposes of reliance.

Runtime thesis:

> Agents propose and organize. The runtime records what happened. Deterministic tools validate and transform. Humans decide what can be relied upon. Git-tracked files remember.

Current implementation assessment:

- The desktop and harness shell are useful and substantially scaffolded: typed API routes, JSON session records, attachment validation, provider selection, subagent governance, network guardrails, API-key handling, UI surfaces, and Section 8 validation exist.
- The harness is not yet a full agent runtime. It is still mostly a provider streaming adapter: `opts.tools` is not backed by executable local tool contracts, permission behavior is partly simulated for validation, there is no append-only per-turn transcript, and the Next.js turn route owns too much runtime lifecycle.

Revised product direction:

- The next development objective is to evolve the shell into a Chirality-native agent runtime.
- The runtime must be local-first, auditable, permissioned, resumable, deterministic where practical, and aligned with professional-work governance.
- The first implementation slice must establish a `TurnEngine`, append-only session event log, durable runtime event schema, and redacted run logging without changing the browser-facing SSE contract.

---

## 3. Goals

### 3.1 Product Goals

1. Provide a local desktop application that runs agent workflows against a selected working root without requiring an external database.
2. Preserve strict separation between bundled instruction root and mutable working root.
3. Make agent work auditable through plain files, git diffs, lifecycle files, dependency registers, immutable snapshots, and runtime session events.
4. Provide matrix-based navigation into two execution surfaces: WORKBENCH for interactive persona agents and PIPELINE for operative task categories.
5. Support streaming chat turns with session persistence, runtime options, interrupts, multimodal attachments, and Anthropic provider integration.
6. Enforce safety and governance boundaries: human authority at gates, no automated issuance, no hidden project memory, fail-closed subagent delegation, and Anthropic-only outbound network policy.
7. Provide deterministic tools and validation workflows for scaffolding, schema checks, dependency closure, harness runtime validation, and release packaging.
8. Ship a macOS 15+ Apple Silicon unsigned DMG build path with instruction-root integrity verification.
9. Establish a `TurnEngine` that owns the harness turn lifecycle outside the HTTP route.
10. Persist accepted user input before provider/model execution.
11. Persist success, failure, interruption, tool, hook, compaction, and subagent lifecycle records in an append-only runtime event log.
12. Define a first-class local tool contract, deterministic tool registry, and tool-pool resolver before exposing tools to the model.
13. Add a deny-first permission policy engine before any workspace-write, shell, or network-capable tools.
14. Implement a model/tool loop that validates tool input, resolves permission, executes local tools, stores or summarizes results, and continues until completion or guardrail termination.
15. Keep the full transcript and runtime evidence available on disk even when model context is compacted.
16. Treat subagents as governed runtime entities with identity, parent-child linkage, restricted capabilities, and stored output artifacts.
17. Preserve a future path for generic Domain Engine Profiles only after the core harness runtime is stable.
18. Use OpenPipeStress, if adopted, as the first concrete Domain Engine Profile fixture rather than as Chirality core behavior.

### 3.2 Non-Goals

The product must not:

- Replace professional judgment or produce binding approval records autonomously.
- Sign, seal, certify, approve, issue, transmit, or otherwise release professional work for reliance.
- Make safety-critical decisions without human review.
- Conduct financial transactions or binding commitments.
- Depend on an external project database.
- Persist project truth in hidden app state, chats, caches, or vendor systems.
- Treat local UI preferences, API keys, runtime logs, or chat drafts as authoritative project state.
- Allow outbound network access beyond the Anthropic API path required for provider execution unless a governed future amendment explicitly permits it.
- Treat prompt instructions as the only safety boundary for filesystem writes or tool execution.
- Add `bash` as the first real local tool.
- Add MCP, plugins, remote execution, or a plugin marketplace before local tool registry, permission policy, hooks, event logging, and result storage are stable.
- Reproduce, port, or chase feature parity with any external codebase. Architectural lessons may be adopted only as Chirality-native components.
- Reopen retired execution-scope items such as unified **pipeline** run records, dependency graph generation, deliverable locks, or staleness tooling without a governed scope amendment. Harness session event logs are a runtime audit facility and do not by themselves reactivate retired pipeline deliverables.
- Become OpenPipeStress, a pipe-stress solver, or any other domain-specific engineering solver.
- Allow agents to write directly into protected domain-engine model paths.

---

## 4. Users and Personas

### 4.1 Professional Operator

The primary user is a licensed professional, project lead, or accountable reviewer who needs AI-assisted production while retaining decision rights. They select the working root, approve gates, review evidence, and decide what can be relied upon.

### 4.2 Project Orchestrator

A user who converts a scope of work into packages, deliverables, lifecycle records, document kits, dependency registers, and coordination artifacts. They use ORCHESTRATOR, WORKING_ITEMS, RECONCILIATION, CHANGE, and PIPELINE lanes.

### 4.3 Specialist Contributor

A user or workflow that executes bounded deliverable-local work through TASK, DEPENDENCIES, CHIRALITY_FRAMEWORK, CHIRALITY_LENS, ESTIMATING, or audit agents.

### 4.4 Governance Maintainer

A maintainer responsible for agent instruction conformance, invariant consistency, deterministic tooling, permission modes, runtime policies, and release-managed instruction root changes.

### 4.5 Release Operator

A maintainer who builds, validates, packages, verifies instruction-root inclusion, and distributes local unsigned desktop builds.

### 4.6 Harness Runtime Maintainer

A maintainer responsible for `TurnEngine`, event schema, tool contracts, permission policy, provider adapters, result storage, context compaction, and validation evolution.

### 4.7 Future Domain Engine Integrator

A future role responsible for defining Domain Engine Profiles, deterministic adapters, protected path rules, manifest requirements, and operation-proposal workflows. This role appears only after the harness runtime spine, permissions, tools, hooks, and result storage are stable.

### 4.8 Future Domain Reviewer

A future accountable reviewer who examines domain-engine proposals, deterministic results, provenance, and professional-boundary notices before any accepted domain state changes.

---

## 5. Product Principles

1. **Filesystem is the database.** Project state is represented as human-readable files under the working root.
2. **Git is the event store for project truth.** Review, audit, rollback, and approvals bind to git-tracked content.
3. **Runtime events are an audit trail, not project truth.** Session logs explain what happened in the harness, but gate-relevant project decisions must still land in versioned project files.
4. **Human authority at every gate.** Agents propose; humans approve, issue, sign, seal, and decide.
5. **Evidence over plausibility.** Claims require provenance. Unknowns become `TBD`, not guesses.
6. **No hidden memory for project truth.** Runtime convenience state is allowed only when explicitly non-authoritative.
7. **Instruction root and working root are separate.** Release-managed agent OS files must not be modified by project execution.
8. **Routes stay thin.** HTTP routes parse requests, handle transport, acquire/release locks, and forward events; runtime services own behavior.
9. **Persist accepted user input early.** A killed or interrupted process must leave a recoverable accepted-turn record.
10. **Separate UI events from runtime events.** Browser `UIEvent`s remain stable and compact; persisted runtime events may be richer and versioned.
11. **Expose only permitted tools to the model.** Tool-pool resolution happens before provider request construction.
12. **Deny overrides allow.** Deny rules, hook denials, and containment failures override any prompt, persona, session, or operator allow decision.
13. **Safety lives in runtime code.** Prompts reinforce safety but do not replace path containment, permission policy, hooks, result budgets, and timeouts.
14. **Immutable snapshots.** Snapshot-producing runs create timestamped folders that are not overwritten. `_LATEST.md` pointers may move.
15. **Least structure that works.** Rigor scales with stakes; structure is added when it reduces error, rework, or ambiguity.
16. **Extensibility follows maturity.** Bash, MCP, plugins, remote execution, and deferred tool discovery are later-phase capabilities gated by stable local runtime primitives.
17. **Domain engines own domain truth.** When a domain engine is integrated, Chirality governs interaction, proposals, records, and human gates; it does not become the solver.
18. **Fixtures are not core.** OpenPipeStress may be the first useful Domain Engine Profile fixture, but its assumptions belong in profile and adapter layers rather than Chirality core runtime.

---

## 6. Scope

### 6.1 In Scope

Current product scope:

- Desktop shell built with Next.js and Electron.
- Working-root selection, validation, file tree browsing, and deliverable scanning.
- Matrix navigation across PORTAL, WORKBENCH, and PIPELINE.
- Session lifecycle APIs and turn execution via SSE.
- Anthropic SDK provider path with local UI key storage and environment fallback.
- Stub provider mode for deterministic local tests.
- Server-side attachment resolution for supported file types.
- Operator Toolkit for per-turn runtime options and local presets.
- Execution-root scaffolding from decomposition markdown.
- Deliverable status and dependency contract APIs.
- Lifecycle transition enforcement for `_STATUS.md`.
- Dependency register read/write support for `Dependencies.csv` v3.1.
- Subagent governance evaluation and fail-closed delegation behavior.
- Harness validation scripts and CI premerge workflow.
- Instruction-root integrity verification in packaged builds.
- macOS Apple Silicon unsigned DMG packaging workflow.

New harness-runtime scope:

- `TurnEngine` extraction from `/api/harness/turn`.
- Versioned `HarnessEvent` schema.
- Append-only session event log and replay helpers.
- Redacted run logger shared by provider, tool, and runtime phases.
- Real prompt/system-context builder from instruction root and active persona.
- Tool contract, registry, and tool-pool resolver.
- Permission policy engine with deny/ask/allow decisions.
- Read-only local tools, then controlled write/edit tools.
- Model/tool loop and provider adapter capable of tool-use events.
- Tool result storage with inline/preview/artifact policies.
- Hook runner for path containment, instruction-root protection, provenance, and failure triage.
- Context window and deterministic compaction records.
- Bash only after permission, hooks, result storage, timeouts, and event logging exist.
- Governed subagent runtime records only after parent turn records and tool permissions are stable.

Future platform compatibility scope, not current-release scope:

- Generic `DomainEngineProfile` contracts.
- Protected-path and proposal-path policy.
- Deterministic adapter manifests.
- Operation proposals with explicit human gates.
- OpenPipeStress as a fixture profile only after generic profile boundaries are accepted.

### 6.2 Current Release Target

The current concrete release target remains:

- macOS 15+
- Apple Silicon (`arm64`)
- Unsigned, unnotarized local-builder DMG
- Node.js `>=20` for development/build

README references to Windows packaging, if present in a complete source tree, are not current release commitments unless separately scoped.

### 6.3 Current Implementation Baseline

The reviewed frontend implementation already includes:

- Session create/boot/list/get/delete APIs.
- Turn SSE route with session-level active-turn locking.
- Stub and Anthropic provider mode selection.
- Anthropic SDK request streaming for text responses.
- Interrupt support through abort controllers.
- API key resolution with UI safeStorage precedence and environment fallback.
- Anthropic API base URL allowlist validation.
- Electron renderer network guardrails.
- Attachment resolver with extension, symlink, file-type, per-file, and per-turn budget validation.
- Runtime option resolution from request options, persona frontmatter, global model, and defaults.
- Explicit subagent governance gates.
- Section 8 validation scripts and stable premerge summary artifact path.

### 6.4 Out of Scope for Current Release

- Automated staleness propagation and dirty-state SHA comparison.
- Deliverable-level lock mechanism.
- Unified pipeline run record persistence across all task agents.
- Project-level dependency graph visualization output.
- Automated merge gates beyond documented/human CHANGE constraints.
- Windows release packaging unless separately scoped.
- Runtime enforcement monitor that intercepts every non-harness file write.
- MCP, plugins, remote execution, and shell access before local runtime spine is reliable.
- Domain-engine integration as a shipping feature unless a separate amendment activates it.

---

## 7. User Journeys

### 7.1 Select and Validate a Working Root

1. User opens Chirality.
2. User enters an absolute path or chooses a folder via native Electron directory picker.
3. App validates that the path exists, is a directory, is readable/writable, and is not inside the instruction root.
4. App stores the selected root as local UI state and uses it for file tree, scan, chat session, scaffold, and contract APIs.

Acceptance:

- Relative paths are rejected.
- Missing or inaccessible directories show actionable errors.
- Instruction-root conflicts are blocked.
- Clearing the root disables runtime actions that require `projectRoot`.

### 7.2 Navigate the Agent Matrix

1. User enters PORTAL.
2. User selects a NORMATIVE or EVALUATIVE cell and routes to WORKBENCH with agent context.
3. User selects an OPERATIVE cell and routes to PIPELINE with category context.
4. If deliverables are present, user can click a deliverable row to route to PIPELINE `TASK*` with that deliverable preselected.

Acceptance:

- NORMATIVE and EVALUATIVE route to WORKBENCH.
- OPERATIVE routes to PIPELINE.
- Disabled or unsupported variants remain visible as coming soon rather than silently disappearing.

### 7.3 Scaffold an Execution Root

1. User selects a working root.
2. User opens PIPELINE.
3. User enters a decomposition markdown path and coordination mode.
4. App calls `POST /api/harness/scaffold`.
5. Runtime parses package/deliverable tables, creates tool roots, copies decomposition, writes `INIT.md`, writes `_Coordination/_COORDINATION.md`, creates packages and deliverable folders, and returns validation summaries.

Acceptance:

- Scaffolding is idempotent for existing directories/files.
- Failures are fail-fast and include stage, target path, and created paths for recovery.
- PREPARATION compatibility is reported before the user proceeds.

### 7.4 Run a Workbench Persona Session

1. User routes to WORKBENCH with an agent persona.
2. Chat panel resolves persona aliases to instruction-file names.
3. User sends a prompt with optional runtime options and attachments.
4. App creates/boots a harness session if needed.
5. Runtime persists `turn.accepted` before calling the model.
6. Runtime streams turn events to the UI.
7. User may interrupt the turn.

Acceptance:

- Session identity is preserved across turns for the same root/persona/mode.
- Runtime errors preserve the draft and attachments for retry.
- Interrupt returns a terminal `process:exit` event and updates UI state.
- Persisted runtime events can reconstruct accepted turns, assistant deltas, terminal outcome, and interruption status.

### 7.5 Run an Operative Pipeline Intent

1. User opens PIPELINE.
2. User selects one of `DECOMP`, `PREP`, `TASK`, or `AUDIT`.
3. User selects a category-specific agent or lane.
4. For `TASK`, user selects scope mode and dynamic scope from the working root.
5. User inspects deliverable status/dependency contract snapshots and may apply allowed lifecycle transitions.

Acceptance:

- Deliverable selections reset when the project root or scan results become stale.
- `KNOWLEDGE_TYPES` mode is shown only when a knowledge decomposition marker is detected.
- Lifecycle transitions enforce authorized actors and approval SHA requirements for human gate states.

### 7.6 Attach Files to a Turn

1. User opens file picker from Chat Panel.
2. User selects supported files by absolute path.
3. UI previews attachments as non-authoritative client metadata.
4. Server validates, classifies, and reads attachments.
5. Turn proceeds if user text exists or at least one valid attachment resolves.

Acceptance:

- Allowed extensions: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, `.csv`.
- Symlinks, directories, special files, unsupported extensions, unreadable files, files over 10 MB, and total raw bytes over 18 MB are rejected.
- Partial attachment failure is non-fatal when executable content remains.
- If all attachments fail and text is empty, request fails with `ATTACHMENT_FAILURE`.

### 7.7 Store and Use an Anthropic API Key

1. User opens API key settings.
2. User stores a key through Electron IPC.
3. Electron encrypts key material with `safeStorage` outside the working root.
4. Server runtime reads UI key from process global; if absent, uses `ANTHROPIC_API_KEY` or `CHIRALITY_ANTHROPIC_API_KEY`.

Acceptance:

- Key material is never written to working-root files.
- UI key takes precedence over env keys.
- API key status can report source as `ui`, `env`, or `none`.
- If secure storage is unavailable, UI reports an error.

### 7.8 Execute a Permissioned Read Tool

1. User asks an active persona to inspect a local file.
2. Runtime resolves the tool pool and exposes only permitted read tools to the model.
3. Model requests `read_file` or `list_files`.
4. Runtime validates input, checks path containment and symlink policy, records permission decision, executes the tool, stores/summarizes result, and feeds the result back to the model.
5. UI displays compact tool progress/result events.

Acceptance:

- Read tool execution is represented in both SSE and persisted runtime events.
- Denied or malformed tool calls do not execute.
- Large outputs are previewed and stored under session artifacts rather than flooding chat.

### 7.9 Execute a Controlled Write or Edit

1. User requests a workspace edit.
2. Runtime exposes write tools only if mode and permission rules allow or can ask.
3. Runtime validates target path under working root, rejects instruction-root writes, rejects symlink writes initially, and requires exact edit preconditions.
4. User approval is requested when policy requires `ask`.
5. Runtime performs atomic write/edit where practical and emits a diff/summary.

Acceptance:

- `readOnly` mode cannot write.
- `dontAsk` denies unapproved writes and bash actions.
- Explicit deny rules override session/operator allows.
- Write/edit operations are auditable through runtime events and project git diffs.

### 7.10 Resume After Failure or Interruption

1. User sends a turn.
2. Process is interrupted or fails after input is accepted.
3. User later opens session history.
4. Runtime event replay shows the accepted turn and terminal failure/cancellation status.

Acceptance:

- Accepted user input is recoverable even if no model token was produced.
- Malformed trailing JSONL writes do not break session listing or replay of valid prior events.
- Session metadata remains usable for listing and resume.

### 7.11 Governed Subagent Delegation

1. User or persona requests delegation.
2. Runtime evaluates `evaluateSubagentGovernance` as the authoritative gate.
3. Delegation requires environment enablement, persona allowlist, context sealing, pipeline approval, approval reference, and Type 2 task-agent eligibility.
4. If allowed in a later implementation phase, runtime creates a child run record with restricted tools/cwd and streams lifecycle to the parent session.

Acceptance:

- Delegation without governance metadata is denied.
- Delegation to a non-allowlisted or non-Type-2 candidate is denied.
- Parent session records child lifecycle and output artifact path when execution support exists.

### 7.12 Validate and Package a Release

1. Release operator installs dependencies in `frontend/`.
2. Operator runs tests/typecheck/harness validation.
3. Operator runs desktop distribution build.
4. Build packages app resources and verifies instruction-root integrity.

Acceptance:

- `frontend/dist/Chirality-0.1.0-arm64.dmg` is produced for macOS arm64.
- App bundle includes expected instruction-root resources.
- App minimum macOS target is `15.0.0` or later.
- Build is unsigned/adhoc by design.

---

## 8. Functional Requirements

Priority:

- `P0`: required for current release usefulness, safety, or next-runtime foundation.
- `P1`: important for current release quality, governed operation, or runtime maturity.
- `P2`: desirable, later hardening, or future extension.

### 8.1 Desktop Shell and Navigation

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-001 | P0 | The app shall provide a desktop shell with PORTAL, PIPELINE, and WORKBENCH navigation. | Header nav routes to `/`, `/pipeline`, and `/workbench`; active route is visually indicated. |
| FR-002 | P0 | The app shall expose working-root selection globally. | User can type a path, choose folder in Electron, apply, and clear root. |
| FR-003 | P0 | The app shall validate working roots before use. | Non-absolute, missing, inaccessible, non-directory, or instruction-root-contained paths fail with typed errors. |
| FR-004 | P0 | The app shall show a file tree for the selected working root. | Tree API skips `.git`, `.next`, `node_modules`, `dist`, `dist-electron`, and `out`; depth is bounded; inaccessible directories mark truncation. |
| FR-005 | P1 | The shell shall support resizable/collapsible File Tree, Toolkit, and Chat panes. | Drag and keyboard resize work; Home collapses; End expands; widths are persisted locally. |
| FR-006 | P1 | The UI shall preserve a calm, professional, dense-but-readable interface. | UI polish acceptance from `docs/ui/UI_POLISH_EXECUTION_PLAN.md` remains applicable; no regression in harness behavior. |

### 8.2 Matrix, Workbench, and Pipeline

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-007 | P0 | PORTAL shall render the 3x4 agent matrix using canonical rows and columns. | Rows: `NORMATIVE`, `OPERATIVE`, `EVALUATIVE`; columns: `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING`. |
| FR-008 | P0 | Matrix routing shall follow the docs/SPEC contract. | NORMATIVE/EVALUATIVE cells open WORKBENCH; OPERATIVE cells open PIPELINE categories. |
| FR-009 | P0 | WORKBENCH shall present active agent context. | Selected agent, row, and column are shown from query params with sensible defaults. |
| FR-010 | P1 | WORKBENCH shall consume deliverable contract APIs for read-only checks and permitted lifecycle transitions. | Status/dependency summaries load for selected deliverables; transition controls are disabled for unsupported agents. |
| FR-011 | P0 | PIPELINE shall expose `DECOMP`, `PREP`, `TASK`, and `AUDIT` category controls. | Each category has documented options; unsupported options are visible and disabled as coming soon. |
| FR-012 | P0 | PIPELINE `TASK` shall use split selectors for task agent and scope. | Scope mode is `DELIVERABLES` or `KNOWLEDGE_TYPES`; target deliverable is required for knowledge-type mode. |
| FR-013 | P1 | Dynamic scope scan shall reset invalid selections. | Root changes, removed deliverables, disabled knowledge markers, and stale knowledge targets clear invalid selection state. |

### 8.3 Harness Sessions and Turns

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-014 | P0 | The app shall create, list, resume, save, and delete harness sessions. | Session records are stored under `.chirality/sessions` or `CHIRALITY_SESSION_ROOT`; sessions are filtered by normalized project root. |
| FR-015 | P0 | Session creation shall bind `projectRoot`, `persona`, and `mode`. | Missing persona/mode use defaults; invalid project root is rejected. |
| FR-016 | P0 | Session boot shall accept runtime options. | `POST /api/harness/session/boot` accepts `opts` and records boot metadata. |
| FR-017 | P0 | Turn execution shall stream Server-Sent Events. | `POST /api/harness/turn` returns `text/event-stream`; browser-facing events remain backward-compatible. |
| FR-018 | P0 | Only one active turn may run per session. | Concurrent turn attempts return `TURN_IN_PROGRESS`. |
| FR-019 | P0 | Users shall be able to interrupt active turns. | `POST /api/harness/interrupt` aborts the active provider request and yields interrupted `process:exit`. |
| FR-020 | P1 | Runtime errors shall be typed and actionable in UI. | UI maps harness errors to title/message/next-step text and preserves drafts for retry. |
| FR-021 | P0 | The runtime shall persist accepted user input before model/provider execution. | A killed or interrupted turn leaves a recoverable `turn.accepted` event. |
| FR-022 | P0 | The runtime shall persist terminal turn outcomes. | Success, failure, and cancellation each produce a terminal runtime event. |

### 8.4 Runtime Options and Personas

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-023 | P0 | Runtime option fallback chains shall be deterministic. | Model: `opts.model` -> `CHIRALITY_GLOBAL_MODEL` or instruction-root frontmatter -> default; tools: `opts.tools` -> persona defaults -> runtime default; max turns: `opts.maxTurns` -> persona defaults -> default. |
| FR-024 | P0 | Unknown option keys shall be ignored with warnings. | Unknown fields do not break turns or silently mutate behavior. |
| FR-025 | P0 | Persona names shall resolve to `agents/AGENT_*.md`. | Missing personas return `PERSONA_NOT_FOUND`. |
| FR-026 | P0 | Persona aliases shall map UI labels to canonical agents. | `HELP -> HELP_HUMAN`, `ORCHESTRATE -> ORCHESTRATOR`, `AGGREGATE -> AGGREGATION`, `RECONCILING -> RECONCILIATION`, `AGENTS -> HELPS_HUMANS`. |
| FR-027 | P0 | Production provider mode shall support Anthropic SDK. | `CHIRALITY_HARNESS_PROVIDER=anthropic` uses the Anthropic SDK path; default/stub mode remains testable. |
| FR-028 | P0 | The runtime shall compose real agent instruction context into turns. | Provider requests include selected agent instruction content, global instruction context, working-root boundaries, mode, and available permitted tools. |
| FR-029 | P1 | Boot fingerprints shall reflect actual prompt inputs. | Fingerprint includes persona content hash, global instruction hash, mode, tool names/versions, project-root policy version, and subagent policy version. |

### 8.5 Anthropic Provider and Network Policy

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-030 | P0 | Anthropic API key resolution shall follow `ENV+UI`. | UI safeStorage key first; then `ANTHROPIC_API_KEY`; then `CHIRALITY_ANTHROPIC_API_KEY`. |
| FR-031 | P0 | Key material shall remain non-project-truth convenience state. | No key is written to working root, docs, logs, runtime event payloads, or git-tracked execution files. |
| FR-032 | P0 | Anthropic base URL shall be allowlisted. | Only `https://api.anthropic.com` with no credentials and port empty/443 is accepted. |
| FR-033 | P0 | Electron renderer outbound traffic shall be blocked except loopback and Anthropic API. | `webRequest.onBeforeRequest` cancels non-allowlisted outbound requests and logs policy metadata without secrets. |
| FR-034 | P1 | Provider errors shall be classified. | Auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation produce typed `SDK_FAILURE` details with key redaction. |
| FR-035 | P1 | Provider integration shall be wrapped by a model adapter. | Anthropic request/stream mapping is isolated from turn lifecycle, permission, and tool execution logic. |

### 8.6 Attachments

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-036 | P0 | UI shall allow file attachments from the selected working root. | File picker supports navigation, multi-select, preview chips, remove, and clear. |
| FR-037 | P0 | Server shall treat client attachment metadata as non-authoritative. | Server revalidates path, extension, file type, readability, symlink status, and size. |
| FR-038 | P0 | Attachment resolver shall enforce supported file types and budgets. | Extension, regular-file, per-file 10 MB, and total 18 MB raw-byte rules are enforced. |
| FR-039 | P0 | Anthropic provider shall map supported files to content blocks. | Images use base64 image blocks; PDFs use document blocks; text/markdown/csv use text document blocks. |
| FR-040 | P1 | Attachment failure handling shall be resilient. | Partial failures prepend a warning; total failure without text rejects the turn; UI preserves draft/attachments on failed send. |

### 8.7 Operator Toolkit and Local UI State

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-041 | P1 | Toolkit panel shall expose per-turn options. | UI can set model/tools/max turns/mode/persona/governance metadata as supported by runtime. |
| FR-042 | P1 | Toolkit settings shall persist locally and remain non-authoritative. | Local presets do not override governance enforcement or project truth. |
| FR-043 | P1 | Chat drafts and attachment selections shall persist locally per root/persona/mode. | Malformed records are dropped; storage failures warn without breaking chat. |
| FR-044 | P1 | Toolkit mode controls shall map to permission policy modes once the policy engine exists. | Modes are not mere prompt hints; runtime enforces read/write/ask/dontAsk behavior. |

### 8.8 Filesystem Execution Model

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-045 | P0 | Execution roots shall follow the `docs/SPEC.md` layout. | Root contains `INIT.md`, package folders, and tool roots such as `_Aggregation`, `_Change`, `_Coordination`, `_Decomposition`, `_Estimates`, `_Reconciliation`, `_Archive`, `_Scripts`, `_Sources`. |
| FR-046 | P0 | Package folders shall follow flat `PKG-XX_Label` or `PKG-XXX_Label` structure. | Required subfolders are created or validated. No nested packages are introduced. |
| FR-047 | P0 | Deliverable folders shall follow `DEL-XX-YY_Label` or `DEL-XXX-YY_Label` structure. | Deliverable scan detects folders with `_STATUS.md` and valid DEL prefix. |
| FR-048 | P0 | Deliverable metadata files shall be canonical. | `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md`, and `MEMORY.md` expectations follow SPEC. |
| FR-049 | P1 | Document kit files shall be supported as first-class knowledge buckets. | Datasheet, Specification, Guidance, and Procedure are detected for knowledge-type scope. |
| FR-050 | P0 | Tool path policy shall enforce working-root containment. | Local tools resolve project-relative/absolute paths and reject paths outside active project root. |
| FR-051 | P0 | Runtime tools shall protect the instruction root. | Writes to instruction root are blocked; reads follow an explicit policy and never mutate release-managed files. |

### 8.9 Lifecycle and Dependency Contracts

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-052 | P0 | `_STATUS.md` shall be the canonical lifecycle state file. | Status parser reads `Current State`, `Last Updated`, and history. |
| FR-053 | P0 | Lifecycle transitions shall be forward-only and actor-authorized. | Allowed transitions follow SPEC; unauthorized actors and backward transitions fail. |
| FR-054 | P0 | Human gate transitions shall require approval SHA evidence. | Transitions to `CHECKING` or `ISSUED` require a 7-64 char hex SHA-like token. |
| FR-055 | P0 | `Dependencies.csv` v3.1 shall be parsed and validated. | Required headers, enum values, identity rules, and warnings are exposed by contract APIs. |
| FR-056 | P0 | Dependency rows shall preserve provenance. | Active extracted rows require `EvidenceFile` and `SourceRef` or explicit `location TBD`. |
| FR-057 | P1 | Dependency writes shall preserve lifecycle behavior. | Rows are serialized with schema version, host deliverable consistency, and warnings for legacy/invalid data. |

### 8.10 Agents, Tools, and Governance

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-058 | P0 | The full instruction root shall include the indexed core agent suite and governance docs. | Packaged resources contain `agents/`, `docs/`, `AGENTS.md`, `README.md`, `WHAT-IS-AN-AGENT.md`, and `PROFESSIONAL_ENGINEERING.md` where required by integrity policy. |
| FR-059 | P0 | Agent instruction files shall declare type/class/surface/write-scope/blocking/output metadata. | Conformance is auditable against governing instruction architecture and SPEC. |
| FR-060 | P0 | Type 2 subagent injection shall fail closed. | Requires `CHIRALITY_ENABLE_SUBAGENTS=true`, persona allowlist, `contextSealed=true`, `pipelineRunApproved=true`, non-empty `approvalRef`, and Type 2 candidate files. |
| FR-061 | P1 | Deterministic project tools and scripts shall remain indexed and executable when present. | Tool registries and validation scripts identify inputs/outputs and remain locally runnable. |
| FR-062 | P1 | Snapshot-producing workflows shall write immutable snapshot folders and mutable `_LATEST.md` pointers. | Reruns create new timestamped folders; prior snapshots are not overwritten. |
| FR-063 | P1 | CHANGE/publication workflows shall require explicit approval tokens and SHA checks. | Approval records include candidate SHA/action list; CHANGE rechecks HEAD before approved actions. |

### 8.11 Validation and Release

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-064 | P0 | Unit and API tests shall cover runtime, workspace, lifecycle, dependency, scaffold, attachment, key storage, network policy, and packaging behavior. | `frontend/src/__tests__` remains comprehensive and `npm run test` passes when dependencies and required instruction-root assets are present. |
| FR-065 | P0 | TypeScript typecheck shall pass for Next.js and Electron code. | `npm run typecheck` exits zero. |
| FR-066 | P0 | Harness premerge validation shall be repeatable locally and in CI. | `npm run harness:validate:premerge` creates `frontend/artifacts/harness/section8/latest/summary.json` with required SDK test IDs. |
| FR-067 | P0 | Desktop distribution build shall include instruction-root integrity verification. | `npm run desktop:dist` runs build, packages DMG, and runs `instruction-root:integrity`. |
| FR-068 | P1 | CI shall upload stable harness summary artifact. | Harness premerge workflow validates server readiness and uploads summary JSON. |
| FR-069 | P1 | Section 9 runtime validation shall be added as runtime phases land. | New validation IDs cover event log, tool runtime, permission precedence, result budget, context compaction, and subagent lifecycle. |

### 8.12 Turn Engine, Event Log, and Runtime Event Schema

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-070 | P0 | A `TurnEngine` shall own the harness turn lifecycle. | `TurnEngine.runTurn()` can be unit-tested without HTTP and yields browser-facing `UIEvent`s. |
| FR-071 | P0 | `/api/harness/turn` shall become an SSE transport adapter. | Route responsibilities are request validation, session locking, attachment option forwarding, SSE encoding, cancellation cleanup, and error response handling. |
| FR-072 | P0 | Persisted runtime events shall use a stable versioned schema. | Each event includes `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, timestamp, type, and data payload. |
| FR-073 | P0 | Session event storage shall be append-only JSONL. | Event writer appends newline-delimited events and replay ignores malformed trailing writes while preserving valid prior events. |
| FR-074 | P0 | Browser `UIEvent`s and persisted `HarnessEvent`s shall be separate contracts. | UI contract remains small; runtime log can include richer diagnostic, permission, hook, and artifact metadata. |
| FR-075 | P0 | Runtime logging shall redact secrets. | API keys and configured secret variants are redacted from provider errors, tool outputs where policy requires, and event records. |
| FR-076 | P1 | Runtime event replay shall reconstruct a transcript view. | Replay produces accepted user messages, assistant deltas/completions, tool summaries, terminal outcomes, and artifact links. |
| FR-077 | P1 | Legacy session metadata layout shall remain readable during migration. | Existing `.chirality/sessions/*.json` records list/resume while canonical folder layout is introduced. |

Initial persisted event categories:

- `session.created`
- `session.resumed`
- `turn.accepted`
- `turn.started`
- `model.request.started`
- `model.delta`
- `model.completed`
- `turn.completed`
- `turn.failed`
- `turn.cancelled`

Later categories:

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

### 8.13 Tool Contract, Registry, Tool Pool, and Model/Tool Loop

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-078 | P0 | `opts.tools` shall map to real registered tool descriptors or structured validation errors. | Unknown tool names are not silently passed through or exposed to a provider. |
| FR-079 | P0 | Each local tool shall declare schema, permissions, read-only behavior, concurrency behavior, interruption behavior, execution, and summarization behavior. | Tool descriptors are unit-tested and deterministic. |
| FR-080 | P0 | Tool pool resolution shall be deterministic. | Tool ordering is stable; dynamic tools, if later added, sort deterministically after built-ins. |
| FR-081 | P0 | Denied tools shall not be exposed to the model. | Permission policy filters provider tool definitions before request construction. |
| FR-082 | P0 | Read-only tools shall ship before write/edit/shell tools. | `read_file` and `list_files` are first; write/edit follow permission engine; bash is deferred. |
| FR-083 | P0 | The model/tool loop shall validate and execute model tool requests. | Tool call flow: resolve descriptor, parse input, validate semantics, resolve permission, execute, store/summarize result, append result to next model request, continue or terminate. |
| FR-084 | P0 | Max-turn guards shall stop runaway loops. | Tool/model loop terminates at configured max turns with a persisted terminal event. |
| FR-085 | P1 | Tool results shall appear in SSE and persisted runtime events. | UI sees compact progress/results; JSONL stores rich result metadata and artifact paths. |
| FR-086 | P1 | Read-only concurrency may be added only after tool safety metadata exists. | First implementation may be serial; later concurrency preserves deterministic event ordering. |

Initial tool sequence:

1. `read_file`
2. `list_files`
3. `write_file`
4. `edit_file`
5. `bash` only after permission, hooks, result storage, and timeout semantics exist
6. `tool_search`, MCP-backed tools, and plugins only after local tool registry and permission policy mature

### 8.14 Permission Policy and Hooks

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-087 | P0 | Permission decisions shall be structured. | Decision is `allow`, `deny`, or `ask`, with reason and source. |
| FR-088 | P0 | Permission modes shall be enforced in runtime code. | `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, and optional local-only `bypass` behave as policy, not prompt text. |
| FR-089 | P0 | Deny rules shall override all allow decisions. | Explicit deny blocks persona/session/operator allow and hook/classifier allow. |
| FR-090 | P0 | `dontAsk` shall deny unapproved write or bash actions. | Denied action does not execute and emits permission/runtime events. |
| FR-091 | P0 | `readOnly` shall expose read-only tools only. | Write/edit/bash/network-capable tools are unavailable to the model. |
| FR-092 | P0 | Permission decisions shall be persisted. | `tool.permission` events record behavior, source, reason, and safe metadata. |
| FR-093 | P1 | Hooks shall run before and after tool use. | `beforeToolUse`, `afterToolUse`, and `onToolFailure` are recorded with duration and outcome. |
| FR-094 | P1 | Hook denials shall fail closed for write and shell tools. | Denied or failed pre-tool hook prevents execution. |
| FR-095 | P1 | First hooks shall enforce filesystem and provenance policy. | Hooks validate project-root containment, block instruction-root writes, reject symlink writes, append provenance/run evidence, and record failure triage. |

### 8.15 Tool Result Storage, Context Management, Bash, Subagents, and Extensibility

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-096 | P0 | Tool outputs shall be budgeted. | Small outputs inline; medium/large outputs preview; raw large outputs stored under session artifacts with metadata. |
| FR-097 | P0 | Write/edit tools shall use safe filesystem behavior. | Paths resolve inside project root, symlinks are rejected initially, instruction-root writes are blocked, edits require exact old content unless configured otherwise. |
| FR-098 | P1 | Context window management shall preserve auditability. | Full transcript stays on disk; model context can be compacted with deterministic boundaries. |
| FR-099 | P1 | Compaction events shall be persisted. | `context.compacted` records boundary, preserved recent turns, summary strategy, and replay metadata. |
| FR-100 | P1 | Bash shall be added only after permission, hooks, result storage, and timeout infrastructure exist. | Denied bash never spawns; allowed bash captures stdout/stderr separately, times out, stores large output, and can be interrupted when possible. |
| FR-101 | P1 | Subagent execution shall create governed child run records. | Child run includes parent session/turn, persona, agent name, model, project root, status, timestamps, and output artifact path. |
| FR-102 | P1 | Subagent tools and working directory shall be restricted. | Child runs inherit or reduce parent permissions; they cannot bypass `evaluateSubagentGovernance`. |
| FR-103 | P2 | Deferred tool search shall return only currently allowed tools. | `tool_search` is added only when catalog size justifies it and never reveals denied tools. |
| FR-104 | P2 | MCP tools shall pass through the same registry and permission engine as built-ins. | Server metadata is preserved, name collisions are prevented, and tools are filtered before model exposure. |
| FR-105 | P2 | Plugin-like extension points shall remain out of scope until mature guardrails exist. | Product does not ship a marketplace/plugin system before local runtime safety is stable. |

### 8.16 Domain Engine Future Compatibility

The thesis and bigger-picture documents describe domain-engine integration, including OpenPipeStress-style protected domain artifacts and operation-proposal workflows. This PRD does not make domain engines part of the current release. It preserves future compatibility through these requirements without moving domain work ahead of the harness runtime spine.

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| FR-106 | P2 | Domain engines shall own authoritative domain truth when adopted by amendment. | Agents propose; deterministic domain tools validate or apply domain operations; humans accept. |
| FR-107 | P2 | A generic `DomainEngineProfile` contract shall precede any engine-specific integration. | OpenPipeStress or any other engine can be described without hardcoding its assumptions into Chirality core. |
| FR-108 | P2 | Domain profiles shall declare engine identity, optional version, protected paths, proposal paths, artifact types, operations, manifest rules, and boundary notices. | Profile validation can determine what the harness may read, propose, validate, or request without guessing from prompt text. |
| FR-109 | P2 | Domain profile validation shall be deterministic. | Invalid or incomplete profiles fail before runtime exposure. |
| FR-110 | P2 | Protected domain paths shall be write-quarantined. | Chirality tools cannot directly overwrite authoritative domain artifacts except through approved domain adapters and human-gated operation workflows. |
| FR-111 | P2 | Agents shall write proposals, summaries, and review aids, not protected domain-engine model truth. | Agent-writable proposal paths are distinct from domain-tool-applied artifacts and accepted domain state. |
| FR-112 | P2 | Domain operations shall be represented as `OperationProposal` records before application. | Proposals identify inputs, intended changes, deterministic checks, expected outputs, risks, and required human gates. |
| FR-113 | P2 | Applying a domain operation shall require explicit human acceptance. | No domain endpoint or tool implies automated professional acceptance. |
| FR-114 | P2 | OpenPipeStress shall be treated as the first fixture profile when adopted. | OpenPipeStress-specific assumptions live in profile and adapter layers, not in the core harness runtime. |
| FR-115 | P2 | Domain-engine output shall not be represented as professional approval, code compliance, external validation, or solver truth owned by Chirality. | UI copy, documentation, and event records preserve professional-boundary language. |

---

## 9. API Requirements

### 9.1 Harness APIs

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/harness/session/create` | POST | Create a session bound to `projectRoot`, persona, and mode. |
| `/api/harness/session/boot` | POST | Boot a session and persist boot metadata. |
| `/api/harness/session/list` | GET | List sessions for a normalized project root. |
| `/api/harness/session/[id]` | GET/DELETE | Retrieve or delete a session. |
| `/api/harness/turn` | POST | Execute a turn and stream UI events over SSE. |
| `/api/harness/interrupt` | POST | Interrupt active turn for a session. |
| `/api/harness/scaffold` | POST | Scaffold execution root from decomposition markdown. |

Compatibility requirement:

- Existing `/api/harness/*` route shapes remain stable during TurnEngine extraction.
- Runtime implementation moves behind route boundaries; public SSE event names remain compatible while internal persisted events expand.

### 9.2 Workspace APIs

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/working-root/validate` | POST | Validate and normalize a working root. |
| `/api/working-root/tree` | GET | Return bounded file tree for the selected root. |
| `/api/working-root/scope` | GET | Scan deliverables and knowledge-type directories. |
| `/api/project/deliverables` | GET | Return deliverables plus knowledge decomposition metadata. |
| `/api/working-root/deliverable/status` | GET | Read `_STATUS.md` snapshot for a deliverable. |
| `/api/working-root/deliverable/status/transition` | POST | Apply an allowed lifecycle transition. |
| `/api/working-root/deliverable/dependencies` | GET/PUT | Read/write `Dependencies.csv` snapshot rows. |

### 9.3 SSE Event Contract

The browser-facing turn stream shall emit named SSE events with JSON payloads:

- `session:init`
- `chat:delta`
- `chat:complete`
- `tool:result`
- `session:complete`
- `turn:error`
- `process:exit`

Additional tool progress events may be introduced only with UI compatibility handling.

The stream must always terminate with a process-level completion/error signal unless the client disconnects and cancel cleanup runs. Client disconnect cleanup must record cancellation in the persisted runtime log once the event log exists.

### 9.4 Internal Runtime Interfaces

Target internal interfaces are not public API contracts, but they are product-significant implementation boundaries:

- `TurnEngine`: owns a single turn lifecycle.
- `HarnessEvent`: persisted runtime event.
- `SessionEvents`: append/replay JSONL event API.
- `RunLogger`: redacted structured runtime logger.
- `ModelAdapter`: provider-specific request/stream/tool-use mapping.
- `HarnessToolDescriptor`: executable local tool contract.
- `ToolRegistry`: built-in and later dynamic tool lookup.
- `ToolPoolResolver`: deterministic filtered tool exposure.
- `PermissionPolicy`: deny/ask/allow decisions.
- `HookRunner`: before/after/failure hook execution.
- `ToolResultStore`: output preview/artifact storage.
- `ContextWindowManager`: model context reconstruction and compaction.
- `SubagentRuntime`: later governed child run lifecycle.
- `DomainEngineProfile`: future-amendment contract for describing deterministic domain engine boundaries, protected paths, proposal paths, operations, manifests, and boundary notices.
- `OperationProposal`: future-amendment record for proposed domain operations that require deterministic checks and human gates before application.

### 9.5 Provisional Domain Interfaces

Domain-engine endpoints are provisional future platform interfaces. They should not be implemented as current-release scope and should not imply automated professional acceptance or direct protected-model writes by an agent.

Candidate endpoint families:

- `/api/domain/profiles/list`
- `/api/domain/profiles/validate`
- `/api/domain/artifacts/scan`
- `/api/domain/operations/propose`
- `/api/domain/operations/validate`
- `/api/domain/operations/apply`

---

## 10. Data and File Requirements

### 10.1 Instruction Root

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
- `WHAT-IS-AN-AGENT.md` where required by packaging/integrity policy
- `PROFESSIONAL_ENGINEERING.md` where required by packaging/integrity policy

Instruction root may be overridden by `CHIRALITY_INSTRUCTION_ROOT`; packaged builds set it to `process.resourcesPath` or equivalent resource root.

Implementation note:

- The reviewed archive does not contain several root-level instruction-root assets that `frontend/src/lib/harness/instruction-root.ts` and `frontend/package.json` expect. Source completeness is therefore a P0 packaging and runtime-readiness gate.

### 10.2 Working Root

Requirements:

- Must be an absolute existing readable/writable directory.
- Must not be inside instruction root.
- Contains project execution state, packages, deliverables, and tool roots.
- Is the only location where agents write project truth.

### 10.3 Session Store

Current implementation default:

- `{frontend cwd}/.chirality/sessions/*.json`

Override:

- `CHIRALITY_SESSION_ROOT`

Current session record fields:

- `sessionId`
- `projectRoot`
- `persona`
- `mode`
- `createdAt`
- `updatedAt`
- `claudeSessionId`
- `bootFingerprint`
- `bootedAt`
- `model`

Canonical future layout:

```text
.chirality/sessions/<sessionId>/session.json
.chirality/sessions/<sessionId>/events.jsonl
.chirality/sessions/<sessionId>/turns/<turnId>.json
.chirality/sessions/<sessionId>/artifacts/
```

Migration rule:

- Runtime must continue reading legacy `.chirality/sessions/<sessionId>.json` records until tests, validation scripts, and deletion/list behavior are explicitly migrated.

### 10.4 Runtime Event Schema

Target persisted event shape:

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

Rules:

- JSONL append must be ordered by write sequence.
- Event IDs must be unique per event.
- Payloads must avoid secrets.
- Large payloads must be stored as artifacts and referenced by metadata.
- Replay must ignore malformed trailing lines and surface diagnostics.

### 10.5 Tool Result Artifacts

Session artifact policy:

- Inline small text results in `tool.completed` data.
- Include preview and metadata for medium results.
- Store raw large results under `.chirality/sessions/<sessionId>/artifacts/`.
- Do not store sensitive values unless a redaction pass has approved the payload.
- Artifact metadata must include tool name, turn ID, byte count, truncation flag, and relative artifact path.

### 10.6 API Key Store

Electron storage:

- `app.getPath('userData')/credentials/api-key.enc`

Rules:

- Encrypted with Electron `safeStorage`.
- Process-global value is used by server runtime in packaged same-process builds.
- Not project truth.
- Not logged.
- Not persisted in runtime events except as source metadata such as `ui`, `env`, or `none`.

### 10.7 Execution Root Layout

Required or expected root entries include:

- `INIT.md`
- `PKG-XX_Label/`
- `_Aggregation/`
- `_Change/`
- `_Coordination/_COORDINATION.md`
- `_Decomposition/`
- `_Estimates/`
- `_Reconciliation/`
- `_Archive/`
- `_Scripts/`
- `_Sources/`

### 10.8 Deliverable Folder Layout

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

Additional expected/optional:

- `Dependencies.csv`
- `MEMORY.md`
- `_SEMANTIC_LENSING.md`
- `HASH_VERIFICATION_BYPASS.jsonl`

Disabled in this project profile:

- `_MEMORY.md`

### 10.9 Dependency Register

`Dependencies.csv` must follow schema version `v3.1` with required core columns plus optional extension columns. Rows are append/lifecycle aware:

- Rows are not deleted when retired.
- `FirstSeen`, `LastSeen`, `Status`, and `SatisfactionStatus` track extraction and closure state.
- `ANCHOR` rows connect deliverables to definition/traceability nodes.
- `EXECUTION` rows capture information flow, prerequisites, handoffs, and constraints.

### 10.10 Domain Engine Artifacts — Future Scope

Future Domain Engine Profiles may define:

- protected model paths;
- agent-writable proposal paths;
- deterministic adapter manifests;
- operation proposal records;
- generated summaries;
- tool result artifacts;
- reviewer acceptance records.

Protected domain-engine paths must not be directly mutated by agents. Any accepted mutation of domain state must flow through an approved adapter or operation workflow and an explicit human gate.

---

## 11. Non-Functional Requirements

### 11.1 Security and Privacy

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| NFR-001 | P0 | No project data shall require external storage. | All authoritative state is local files under working root. |
| NFR-002 | P0 | API keys shall not be written to project files, logs, runtime events, or tool artifacts. | Key redaction is applied to provider errors and logs; key storage stays under Electron userData. |
| NFR-003 | P0 | Renderer outbound traffic shall be allowlisted. | Non-loopback/non-Anthropic renderer requests are canceled. |
| NFR-004 | P0 | Attachment paths shall not follow symlinks. | Symlink attachments are rejected before provider execution. |
| NFR-005 | P0 | Working root shall not be inside instruction root. | Runtime rejects conflicting root selection. |
| NFR-006 | P0 | Runtime tools shall enforce path containment. | Tool execution cannot read/write outside allowed roots except through explicitly approved policies. |
| NFR-007 | P0 | Deny-first permission policy shall be enforced by runtime code. | Deny rules override all allow decisions. |

### 11.2 Reliability

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| NFR-008 | P0 | Harness turns shall be cancellable. | Interrupt/cancel aborts provider/tool request where supported and releases session lock. |
| NFR-009 | P0 | Runtime operations shall expose typed errors. | Harness and workspace errors include type, status, message, and details where applicable. |
| NFR-010 | P0 | Accepted turns shall survive failure after request acceptance. | `turn.accepted` exists before provider/model request starts. |
| NFR-011 | P1 | Scaffolding shall be idempotent and recoverable. | Existing paths are preserved; failures include stage and created path inventory. |
| NFR-012 | P1 | File scans shall avoid runaway traversal. | Tree and scope scan depth/count limits are enforced. |
| NFR-013 | P1 | JSONL replay shall tolerate malformed trailing writes. | Session listing and transcript replay ignore malformed final records without losing earlier valid events. |

### 11.3 Performance

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| NFR-014 | P1 | Working-root scans shall remain responsive on large repos. | Scope scan caps directories at 2500 and depth at 8; tree limits entries per directory to 60 and depth to 6. |
| NFR-015 | P1 | Provider streams shall time out. | Anthropic stream timeout defaults to 90 seconds and can be overridden by env. |
| NFR-016 | P1 | Attachment budgets shall protect request size. | Per-file and per-turn raw-byte limits are enforced before provider call. |
| NFR-017 | P1 | Tool output budgets shall protect chat and model context. | Large outputs are stored as artifacts and represented by previews. |
| NFR-018 | P1 | Context compaction shall keep recent interaction quality. | Recent turns are preserved verbatim while older context is summarized or bounded. |

### 11.4 Accessibility and UX Quality

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| NFR-019 | P1 | Keyboard users shall be able to resize/collapse panes. | Resize handles are focusable separators with arrow/Home/End behavior. |
| NFR-020 | P1 | Controls shall expose disabled/loading/error states. | Primary surfaces avoid silent failure and show typed feedback. |
| NFR-021 | P1 | UI shall avoid hydration mismatch from local browser state. | Browser-backed state initializes client-side and does not render conflicting server text. |
| NFR-022 | P1 | Tool-heavy turns shall remain readable. | UI groups model text, tool progress, permission decisions, and terminal status in a scan-friendly way. |

### 11.5 Auditability and Compliance

| ID | Priority | Requirement | Acceptance |
|---|---:|---|---|
| NFR-023 | P0 | Human approval remains non-delegable. | No automated endpoint can sign/seal/issue for reliance without human actor/approval evidence. |
| NFR-024 | P0 | Approval SHA evidence shall be captured for checking/issued transitions. | Status transition metadata includes SHA fields for human gate states. |
| NFR-025 | P0 | Runtime actions shall be auditable. | Turn, model, permission, tool, hook, and subagent lifecycle records are persisted when supported by phase. |
| NFR-026 | P1 | Validation artifacts shall be stable and reviewable. | Harness summary artifact path is deterministic and uploaded in CI. |
| NFR-027 | P1 | Runtime event schema shall evolve compatibly. | New event types do not break replay of existing sessions; schema versioning is explicit. |

---

## 12. Validation Plan

### 12.1 PRD Acceptance Checks

This PRD remains acceptable only if:

- it does not claim automated professional approval, code compliance, external validation, or solver ownership;
- the first implementation slice remains `R1 — Turn Engine, Session Event Log, and Run Logger`;
- roadmap order remains clear: runtime spine before tools, tools before writes/bash, and domain profiles only after core harness stability;
- retired PKG-08 deliverables remain out of current scope unless explicitly reactivated by governed amendment;
- domain-engine requirements remain future compatibility scope and preserve protected-path and human-gate boundaries;
- `git diff -- docs/PRD.md` shows the intended PRD change without unrelated file modifications.

### 12.2 Required Local Checks

From `frontend/`:

```bash
npm run test
npm run typecheck
npm run harness:validate:premerge
npm run instruction-root:integrity
```

Packaging check:

```bash
npm run desktop:dist
```

Expected packaging outputs:

- `frontend/dist/Chirality-0.1.0-arm64.dmg`
- `frontend/dist/mac-arm64/Chirality.app`
- `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`

### 12.3 Harness Section 8 Validation Acceptance

The Section 8 harness validation shall verify:

- Server reachable.
- Session CRUD.
- Boot error taxonomy.
- Smoke stream ordering.
- Session persistence and resume continuity.
- Permissions behavior under `dontAsk` for current validation markers.
- Interrupt behavior.
- SDK-native stream handling with no legacy parser regressions.

### 12.4 Harness Section 9 Runtime Validation Additions

As runtime phases land, add validation IDs:

- `section9.turn_engine_event_log`
- `section9.session_event_replay`
- `section9.tool_runtime_read_file`
- `section9.permission_rule_precedence`
- `section9.tool_result_budget`
- `section9.context_compaction_boundary`
- `section9.subagent_lifecycle`
- `section9.domain_profile_validation` after a governed domain-profile amendment enters scope

### 12.5 Unit Test Additions

Add tests for:

- `TurnEngine.runTurn()` lifecycle without HTTP.
- Session event append and replay.
- Event schema serialization and malformed trailing JSONL behavior.
- Redaction helper shared by provider, tool, and run logs.
- Prompt builder from instruction-root and persona content.
- Tool descriptor validation.
- Tool pool filtering and deterministic order.
- Permission rule precedence.
- Project-root path containment and symlink rejection.
- Tool result storage thresholds.
- Hook allow, deny, failure, and duration behavior.
- Context compaction boundaries.

### 12.6 Integration Test Additions

Add tests for:

- `/api/harness/turn` streaming unchanged after TurnEngine extraction.
- Accepted turn persisted before provider response.
- Interrupt during model stream records cancellation.
- Read-file tool call completes through model/tool loop.
- Denied write under `dontAsk`.
- Allowed write with explicit rule or prompt confirmation.
- Bash timeout after Phase R8.
- Subagent governance denial and allowed child run after Phase R9.

### 12.7 CI Acceptance

The GitHub workflow shall:

1. Checkout repository.
2. Setup Node.js 20.
3. Install dependencies with `npm ci`.
4. Verify required instruction-root assets are present.
5. Preflight validation script presence.
6. Start Next server.
7. Poll readiness.
8. Run `npm run harness:validate:premerge`.
9. Verify stable summary artifact.
10. Upload summary artifact.

### 12.8 Manual Release Verification

For macOS DMG:

- Binary is arm64.
- `LSMinimumSystemVersion` is `15.0.0` or later.
- Codesign reports no developer TeamIdentifier and adhoc signature.
- App resources contain required instruction-root assets.
- App launches and working-root selector is available.
- Anthropic-only network guardrails remain in force.

---

## 13. Runtime Development Sequence

The current execution decomposition is issued, but the harness runtime needs a forward implementation sequence. This sequence updates the product roadmap without reactivating retired PKG-08 project-level hardening deliverables.

### R0 — Runtime Scope Confirmation

Purpose:

- Record what the local harness owns versus what provider SDKs own.

Decisions:

- Chirality executes local tools itself.
- Provider adapter maps model/tool-use protocol but does not own local tool execution.
- First runtime supports single-agent turns; subagent execution records are later.
- Tool outputs and turn evidence are persisted under session runtime storage, not as authoritative project truth.

Deliverables:

- `docs/harness/runtime_scope.md`
- Updated `docs/harness/chirality_harness_graphs_and_sequence.md`

### R1 — Turn Engine, Session Event Log, and Run Logger

Purpose:

- Establish a stable runtime spine without changing visible app behavior.

Implementation targets:

- `frontend/src/lib/harness/turn-engine.ts`
- `frontend/src/lib/harness/session-events.ts`
- `frontend/src/lib/harness/run-logger.ts`
- `frontend/src/lib/harness/event-schema.ts`
- Refactor `frontend/src/app/api/harness/turn/route.ts` to call the engine.

Acceptance:

- Existing tests pass.
- Section 8 validation passes.
- `turn.accepted` persists before model request.
- Success, failure, and interruption terminal events persist.
- Route code is reduced to transport/locking/error handling.
- No local tool execution is introduced in this slice.

### R2 — Prompt Builder and Model Adapter Boundary

Purpose:

- Replace stub persona prompting and provider-owned lifecycle with a first-class prompt/model boundary.

Acceptance:

- Provider requests include selected persona instruction content and root governance context.
- Boot fingerprint reflects prompt inputs.
- Anthropic streaming remains compatible.
- Provider adapter can later map tool-use events.

### R3 — Tool Contract and Tool Pool

Purpose:

- Make `opts.tools` meaningful and safe.

Acceptance:

- Registered tools have descriptors.
- Unknown tools produce structured validation errors.
- Tool order is deterministic.
- Denied tools are not exposed to the model.
- Initial built-ins are `read_file` and `list_files`.

### R4 — Permission Policy Engine

Purpose:

- Enforce local action safety before adding write or shell tools.

Acceptance:

- `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, and optional local-only `bypass` are implemented.
- Deny overrides allow.
- Permission decisions emit runtime events.
- `dontAsk` denies unapproved write/bash.

### R5 — Model/Tool Loop and Read Tools

Purpose:

- Support actual agentic tool use with low write risk.

Acceptance:

- Model tool-use requests are parsed and validated.
- `read_file` and `list_files` execute through the local tool executor.
- Tool results are returned to the model.
- Tool events appear in SSE and JSONL.
- Max-turn guard stops runaway loops.

### R6 — Write/Edit Tools and Tool Result Store

Purpose:

- Enable controlled file modification.

Acceptance:

- `write_file` cannot write outside project root.
- Instruction root writes are blocked.
- Symlink writes are rejected initially.
- `edit_file` requires exact old content and fails on ambiguity.
- Diffs and artifact metadata are emitted.
- Large outputs do not flood chat.

### R7 — Hooks and Context Management

Purpose:

- Connect runtime actions to Chirality governance, provenance, and long-session stability.

Acceptance:

- Hook-denied tools do not execute.
- Hook events include duration and outcome.
- Full transcript remains on disk after compaction.
- Model context can be rebuilt from compacted state.
- Recent turns are preserved.

### R8 — Bash Tool

Purpose:

- Add shell execution only after permission, hooks, result storage, and timeouts exist.

Acceptance:

- Default deny in `readOnly` and `dontAsk`.
- Denied bash does not spawn.
- Timeout terminates process and records failure.
- stdout/stderr are captured separately.
- Large output is stored, previewed, and linked from events.
- Interrupt cancels running process when possible.

### R9 — Governed Subagent Runtime

Purpose:

- Extend existing subagent governance into executable runtime records.

Acceptance:

- `evaluateSubagentGovernance` remains authoritative.
- Delegation without metadata is denied.
- Delegation to non-allowlisted agents is denied.
- Parent session records child lifecycle and output path.
- Child tools and cwd are restricted.

### R10 — Deferred Tool Search, MCP, and Plugin Boundaries

Purpose:

- Add extensibility only after local runtime is stable.

Acceptance:

- Deferred tool search returns only currently allowed tools.
- MCP tools pass through registry and permission engine.
- Dynamic tool names avoid collisions.
- Plugins remain out of scope until permission, hooks, tool registry, and event logging are mature.

### R11 — Domain Engine Profiles and Operation Proposals — Future Amendment

Purpose:

- Add generic domain-engine awareness only after the core harness runtime, permissions, tool result storage, hooks, and protected-path policy are stable.

Acceptance:

- `DomainEngineProfile` validation is deterministic.
- OpenPipeStress can be represented as a fixture profile without core-runtime assumptions.
- Protected domain paths are not agent-writable.
- Domain operation requests become `OperationProposal` records before application.
- Applying a domain operation requires explicit human acceptance and professional-boundary notices.

---

## 14. Success Metrics

1. A first-time operator can select a working root, inspect the file tree, and start a WORKBENCH chat turn within one app session.
2. A decomposition markdown can be used to scaffold a SPEC-conformant execution root without manual folder creation.
3. A deliverable can be scanned, inspected, and transitioned according to lifecycle rules with approval SHA enforcement for human gate states.
4. Harness premerge validation passes in CI and produces a stable summary artifact.
5. Desktop DMG builds locally and passes instruction-root integrity checks.
6. No API key or project truth is written outside its approved storage zone.
7. Unsupported PIPELINE variants remain visible as disabled options, preserving operator awareness of roadmap scope.
8. A killed or interrupted turn leaves a replayable accepted-turn record.
9. A read-file model tool request completes through the local tool loop with permission and event records.
10. Denied write/bash actions do not execute and produce auditable permission events.
11. Large tool outputs are stored as artifacts rather than streamed unbounded into chat.
12. Long sessions retain full audit history while model context can be compacted deterministically.
13. A future Domain Engine Profile can describe OpenPipeStress without adding OpenPipeStress assumptions to Chirality core runtime.
14. No user-facing or documentation claim says Chirality approves professional work, proves code compliance, performs external validation, or owns solver truth.

---

## 15. Known Gaps and Risks

| ID | Area | Risk / Gap | Product Decision |
|---|---|---|---|
| KG-001 | Source completeness | The reviewed archive lacks required root instruction assets (`AGENTS.md`, `agents/`, root `README.md`, `WHAT-IS-AN-AGENT.md`, `PROFESSIONAL_ENGINEERING.md`, `tools/REGISTRY.md`, and `examples/`) expected by docs, packaging, validation, or frontend code. | P0 before packaging/reliance: complete the source tree or adjust integrity requirements and code paths explicitly. |
| KG-002 | Persona prompting | Current `StubPersonaManager.buildSystemPrompt()` validates persona existence but returns a short stub rather than composing full instruction-root context into provider requests. | P0 for runtime maturity: create a prompt builder and model adapter boundary. |
| KG-003 | Route lifecycle ownership | `turn/route.ts` owns locking, option resolution, attachment warnings, prompt validation, governance, provider streaming, session persistence, and error mapping. | P0 next slice: extract `TurnEngine` and keep route as SSE adapter. |
| KG-004 | Append-only transcript | Session metadata exists, but not a robust per-turn event log. | P0 next slice: add `HarnessEvent`, session JSONL, and replay. |
| KG-005 | Tool runtime | `opts.tools` exists but there is no local tool registry, executable tool contract, or model/tool loop. | P0/P1 runtime roadmap: tool contract and read tools follow event-log spine. |
| KG-006 | Permission model | Current validation uses `dontAsk` markers; no generic permission policy engine exists. | P0 before write/bash: implement deny-first permission policy and decisions. |
| KG-007 | Runtime enforcement | Several K-* invariants are enforced by instructions and human review, not runtime guards. | Accept for current governed-human use; add runtime path policy, hooks, and permission checks before powerful tools. |
| KG-008 | Context budgeting | `maxTurns` exists in options but not as full conversation context control. | P1: add context-window manager and deterministic compaction after event log and tool-result storage. |
| KG-009 | Tool output budget | Large future tool outputs could flood chat/model context. | P0 before tool expansion: add tool-result storage thresholds and artifacts. |
| KG-010 | Subagent execution | Governance gates exist, but no child runtime records or execution lifecycle exist. | Later: add governed subagent runtime after parent events and permissions stabilize. |
| KG-011 | Staleness/dirty state | K-STALE-1, K-VAL-1, K-MERGE-1, K-AUTH-2 automated enforcement is partial or future-scoped. | Keep human CHANGE constraints active; do not claim complete automated enforcement. |
| KG-012 | Retired PKG-08 scope | Execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record, and staleness propagation are retired in current decomposition. | Do not reintroduce as current commitments. Harness runtime event logging is separate and allowed as runtime infrastructure. |
| KG-013 | Registry ownership | Current membership belongs in source registries, not mutable count prose. | Treat root `AGENTS.md`, agent files, tools registry, and generated test discovery output as active registry surfaces when present. |
| KG-014 | Release target ambiguity | Some source references may mention Windows packaging, but current build config/runbook targets macOS 15+ Apple Silicon DMG. | Current release scope is macOS arm64 only; Windows requires explicit scope amendment. |
| KG-015 | Professional reliance | App supports auditability but does not make outputs professionally reliable by itself. | Product copy and UI must preserve draft/decision-support posture until human review. |
| KG-016 | Domain engine future scope | Bigger-picture docs describe domain-engine integration, but it is not current shipping scope. | Keep as future amendment; do not mix into first runtime-spine implementation. |
| KG-017 | Domain profile specification | No accepted generic `DomainEngineProfile` specification exists yet. | Draft and accept profile specification only after core harness stability. |
| KG-018 | Protected domain paths | Domain-engine protected paths need runtime enforcement, not prompt-only guidance. | Add profile-driven path policy before write tools can interact with domain artifacts. |
| KG-019 | Domain provenance | Domain summaries, manifests, and operation outputs need deterministic provenance. | Use adapter manifests, tool-result artifacts, and `OperationProposal` records. |
| KG-020 | Professional boundary | Domain-engine outputs may be mistaken for professional approval or solver truth. | Require boundary notices, human gates, and explicit copy restrictions. |

---

## 16. Execution Package Traceability Summary

Source-area traceability:

| Product Area | Primary Source Basis |
|---|---|
| Product constraints | `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md` |
| Agent governance | `AGENTS.md` when present, `docs/TYPES.md`, `docs/DBM_Agent_Instruction_Architecture.md` |
| Desktop and harness baseline | PKG-01 through PKG-04 execution deliverables and `frontend/` implementation |
| Filesystem governance | PKG-05 and PKG-06 execution deliverables |
| Validation and release | PKG-07, accepted PKG-08 hardening deliverables, validation runbooks |
| Runtime roadmap | `agent-harness-patterns-from-claw-code-assessment.md`, `chirality-app-future-development-plan.md` |
| Domain-engine future | `docs/thesis/` material, governed future amendment only |

The accepted decomposition partitions scope into eight flat packages and 37 deliverables:

| Package | Product Area | PRD Coverage |
|---|---|---|
| PKG-01 Build & Packaging | macOS build, unsigned DMG, frontend bootstrap | FR-064 through FR-068, NFR-014 through NFR-016, release validation |
| PKG-02 Desktop UI Workflow | FileTree, Portal/Pipeline, Toolkit, panes, API key UI | FR-001 through FR-013, FR-041 through FR-044 |
| PKG-03 Harness Runtime Core | Session/turn APIs, SSE, opts, subagent governance, Anthropic, network policy | FR-014 through FR-035, FR-070 through FR-095 |
| PKG-04 Attachments & Multimodal | Resolver, prompt mode, UI attachment pipeline | FR-036 through FR-040 |
| PKG-05 Filesystem Execution Model | Instruction/working root, scaffolding, lifecycle, dependencies | FR-045 through FR-057, data requirements |
| PKG-06 Agent Suite & Governance | Agent instruction conformance, local/cross-deliverable workflows, change hygiene | FR-058 through FR-063, governance principles |
| PKG-07 Validation & Example Assets | Harness validation, examples, runbooks | FR-064 through FR-069, validation plan |
| PKG-08 Optional Integrity Hardening | Hashes/linter active; several hardening items retired | Known gaps KG-011/KG-012; do not reintroduce retired scope without amendment |

Runtime roadmap traceability:

| Runtime Phase | Primary Requirement IDs |
|---|---|
| R0 Runtime scope confirmation | FR-070, FR-074, KG-004 through KG-006 |
| R1 TurnEngine/event log/run logger | FR-021, FR-022, FR-070 through FR-077, NFR-010, NFR-013 |
| R2 Prompt builder/model adapter | FR-028, FR-029, FR-035, KG-002 |
| R3 Tool contract/tool pool | FR-078 through FR-082 |
| R4 Permission policy | FR-087 through FR-092, NFR-006, NFR-007 |
| R5 Model/tool loop/read tools | FR-083 through FR-086 |
| R6 Write/edit/result storage | FR-096, FR-097 |
| R7 Hooks/context management | FR-093 through FR-095, FR-098, FR-099 |
| R8 Bash | FR-100 |
| R9 Subagent runtime | FR-101, FR-102 |
| R10 Extensibility | FR-103 through FR-105 |
| R11 Domain profiles and operation proposals | FR-106 through FR-115 |

---

## 17. Approval and Change Control

This PRD is a product requirements artifact. It does not supersede:

- `docs/DIRECTIVE.md`
- `docs/SPEC.md`
- `docs/TYPES.md`
- `docs/CONTRACT.md`
- Active decomposition and scope-change records under `execution/_Decomposition/` and `execution/_ScopeChange/`

This PRD **does** establish a revised product-development direction for the harness runtime. The immediate next implementation slice should be `R1 — Turn Engine, Session Event Log, and Run Logger`.

Changes to this PRD that alter scope, release targets, safety posture, data contracts, professional responsibility boundaries, or retired/active execution scope should be handled as governed product changes and traced back to stable SOW/OBJ/DEL identifiers or a new approved decomposition amendment.

---
