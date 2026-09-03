# PLAN — Development Roadmap

**Status:** vNext governance rewrite aligned to the approved `docs/PRD.md` dated 2026-05-20
**Date:** 2026-05-20
**Product:** Chirality desktop harness and bundled agent operating system
**Applies to:** Chirality App vNext development and release planning

This document captures the strategic development roadmap for Chirality App. It summarizes the accepted baseline, records the controlling runtime direction, identifies sequencing rationale, and defines the near-term implementation path.

---

## Control-Plane Boundary

- `docs/PLAN.md` is strategic. It explains priorities, rationale, and roadmap direction.
- Operational sequencing and blocker policy belong in execution coordination artifacts such as `execution/_Coordination/_COORDINATION.md`, `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`, the active tranche-selection plan, decision records, and dependency/SCC evidence. `NEXT_INSTANCE_STATE.md` is retired and must not be used as current app state.
- `docs/PRD.md` defines current product requirements; this plan translates those requirements into roadmap structure.
- `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/TYPES.md` govern intent, invariants, mechanics, and vocabulary.
- Accepted execution deliverables and scope-change records remain authoritative for the work they cover.

---

## Local Source Policy

Development guidance and execution evidence should come from repository-local files, accepted execution records, and governed source material. External references may inform implementation, but they do not override Chirality’s local governance.

The active vNext development source is the app-development workspace (`chirality/projects/chirality-app-dev/frontend` in the complete tree; `frontend/` in the reviewed archive snapshot). The public `chirality-app/frontend` path is a release snapshot synchronized by release operation, not the live vNext source.

---

## 1. Current Baseline

The issued baseline already provides substantial product scaffolding:

- Electron/Next.js desktop shell.
- Live loop-first PORTAL, WORKBENCH, PIPELINE, matrix, toolkit, file-tree, and replay surfaces; these remain the compatibility baseline while the owner-selected Woven Dialogue target is implemented and validated.
- Working-root selection and validation.
- Harness session create/boot/list/get/delete APIs.
- Turn SSE route with session-level active-turn locking.
- Stub and Anthropic provider modes.
- Interrupt support.
- Attachment resolver with file type, symlink, per-file, and total-byte controls.
- API key storage/resolution and Anthropic network policy.
- Execution-root scaffolding.
- Deliverable status and dependency APIs.
- Subagent governance evaluation and fail-closed delegation behavior.
- Harness validation scripts and CI premerge summary artifacts.
- Instruction-root integrity verification.
- macOS 15+ Apple Silicon unsigned DMG build path.

The baseline is useful and must be preserved while the runtime and
owner-selected information architecture evolve. SCA-APP-004 selects Woven
Dialogue with a right Work/Agents Coordination Panel as the target: actual
human–agent dialogue remains mounted and primary; artifacts are
provenance-bearing inline/focused views; Work and Agents are rebuildable,
evidence-conditional projections; and selected-session replay is read-only
and distinct from the primary live dialogue.

---

## 2. Controlling Runtime Direction

The approved vNext direction is:

> **Provider-adapter-general, contract-owned, and Chirality-governed.**

Chirality should build a provider-adapter runtime where external SDKs and provider APIs remain implementation substrates behind Chirality-owned contracts. The Claude Agent SDK / Anthropic path remains the first concrete adapter, key-aware default provider per D-APP-18, and supervisor. D-APP-72 / SCA-APP-002 authorizes Pi `0.80.10` as an opt-in in-process second adapter over authenticated `127.0.0.1` oMLX, initially for one governed read-only Agent 2 child after Electron `43.2.0` validation (D-APP-98 successor authority; D-APP-72's `43.1.1` is historical). Chirality builds the governance, UI, audit, lifecycle, and adapter layer **over** provider harness mechanics — not a standalone general agent harness, and not Claude Code / Pi / Codex feature parity (CONTRACT K-ENGINE-6). Chirality must not let provider defaults, SDK transcript shape, SDK tool names, Claude Code/Pi product assumptions, ambient user settings, provider-specific APIs, or broad provider registries define product semantics.

2026-06-17 stabilization note: R0-R5 roadmap text below is retained as strategic history.
Runtime Stabilization landed the runtime spine, validation surface, persona composer,
mutating Chirality MCP exposure, and no-live packaged SDK resolver/HOME evidence. Active
implementation no longer proceeds from these roadmap rows unless a new governed plan
selects that work.

Chirality owns:

- `AgentEnginePort` / `RuntimeEngineContract`;
- engine conformance tests;
- reliance-boundary register;
- prompt/persona composition;
- working-root/instruction-root separation;
- capability policy, permission overlay, and explicit hard-deny precedence;
- Chirality hooks and in-process MCP tools;
- `HarnessEvent` schema and `events.jsonl` audit mirror;
- adapter session linkage policy;
- runtime redaction and product identity;
- fallback criteria if an adapter cannot preserve governance.

External provider SDKs may own generic mechanics only when verified behind adapters:

- model/tool loop;
- built-in file tools;
- bash surface;
- permission-mode machinery;
- hook dispatch;
- MCP transport;
- SDK transcripts;
- subagent invocation;
- compaction messages.

This plan does not chase feature parity with Claude Code, Pi, or any external agent harness. It adapts useful runtime mechanics only where they accelerate Chirality's product-owned runtime contract.

---

## 3. Immediate Development Objective

The current product-identity/UX objective is the governed SCA-APP-004
implementation tranche:

> implement Woven Dialogue, provenance-bearing inline/focused artifacts, and
> the informational Work/Agents Coordination Panel without changing runtime
> capability or breaking compatibility.

The implementation must preserve the mounted primary live dialogue, explicit
next-turn context, source/provenance/currency labels, exact recorded
parentage, isolated read-only replay, current browser-facing SSE behavior,
public route/API/query shapes, provider composition, security boundaries, and
the loop-first UI through the compatibility period.

The historical R0/R1 sequence below remains strategic history. The accepted
D-APP-73 shared-runtime execution order in §13.1 remains controlling and is
not reordered by this frontend information-architecture tranche.

---

## 4. Runtime Roadmap

### R0 — Runtime Scope Confirmation, First-Adapter Probe, and Reliance Boundary Register

Purpose:

- Record what Chirality owns versus what provider/SDK adapters own.
- Validate first-adapter assumptions before implementation details harden.
- Make Claude Agent SDK / Anthropic adoption a first-adapter choice, not a product-identity or permanent strategy ceiling.

Deliverables:

- `docs/harness/runtime_scope.md`.
- `docs/harness/runtime_engine_contract.md` defining `AgentEnginePort` / `RuntimeEngineContract`.
- `docs/harness/reliance_boundary_register.md` mapping audit, permission, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundaries to enforcement surfaces.
- Updated `docs/harness/chirality_harness_graphs_and_sequence.md`.
- First-adapter probe notes covering SDK package version, `query()` message sequence, `settingSources`, permission mapping, `canUseTool`, hooks, in-process MCP, `agents`, `resume`, `SessionStore`, `CLAUDE_CONFIG_DIR`, interrupt behavior, Electron packaging, API key environment handling, branding constraints, and fallback triggers.

Acceptance:

- Claude Agent SDK / Anthropic is confirmed viable for R1 or a governed fallback decision reactivates the custom-runtime roadmap.
- Engine conformance tests are specified before SDK adapter becomes production path.
- Every P0 reliance boundary has a non-prompt-only enforcement plan.
- No local tools are exposed to the model during the probe outside controlled validation.

### R1 — First-Adapter Adoption, Engine Contract, Thin TurnEngine, Prompt Composer, and Chirality Audit JSONL

Purpose:

- Replace the current direct Anthropic streaming adapter with the first provider-adapter runtime while preserving visible app behavior.

Implementation targets:

- Add and pin `@anthropic-ai/claude-agent-sdk` for the first concrete adapter.
- Add `agent-engine-port.ts` or equivalent.
- Add `engine-conformance.ts` or equivalent test harness.
- Add `reliance-boundaries.ts` or equivalent register loader/checker.
- Add `turn-engine.ts` invoking SDK `query()` through the engine contract.
- Add `sdk-options-builder.ts`.
- Add `sdk-message-mapper.ts`.
- Add `session-events.ts`.
- Add `event-schema.ts`.
- Add `run-logger.ts`.
- Add `PersonaComposer` or equivalent governed prompt composer.
- Add `sdk-session-link.ts` for `sdkSessionId`, transcript/store linkage, and resume.
- Wire `CHIRALITY_HARNESS_PROVIDER=agentSdk` to the opt-in SDK-backed path while preserving stub tests and leaving default cutover gated by D-APP-12.
- Ensure shipped SDK options use `settingSources: []`.
- Supply API key to SDK only for active turn and redact logs/events.

Acceptance:

- Existing tests pass.
- Section 8 validation passes.
- `turn.accepted` persists before SDK `query()` begins.
- Initial engine conformance suite passes.
- Reliance-boundary register covers P0 audit, permission, path, transcript, settings, and human-gate semantics.
- SDK messages map to stable UI/runtime events.
- Terminal success, failure, interruption, and cancellation persist.
- Route shapes and SSE event names are unchanged.
- Settings isolation test passes.
- SDK session ID and transcript/store linkage persist.
- No new user-visible local tool capability is enabled beyond current surface.

### R2 — Capability-Policy-Gated Read Surface and First Chirality MCP Tools

Purpose:

- Make `opts.tools` meaningful through first-adapter SDK built-ins and in-process Chirality MCP tools without opening write or shell capability.

Implementation targets:

- Define `ChiralityPermissionOverlay` as capability-forward policy with explicit hard-deny precedence.
- Map `readOnly`, `dontAsk`, and `ask` modes to SDK plus overlay behavior.
- Validate that `allowedTools` does not restrict by itself.
- Enable SDK read tools such as `Read`, `Glob`, `Grep`, and `LS` where available.
- Register in-process read MCP tools: status read, dependency read, scope scan, and scaffold dry-run/preview where appropriate.
- Persist tool permission/start/completion/failure events.

Acceptance:

- Unknown tools fail with structured validation errors.
- Read-only tool calls execute and produce Chirality events.
- Denied tools do not execute.
- Tool results appear in SSE and persisted runtime events.
- Large outputs are budgeted or stored as artifacts.

### R3 — Write Surface and Chirality Hooks

Purpose:

- Enable controlled writes through SDK `Write`/`Edit` and Chirality MCP write tools after path, permission, and hook policy are stable.

Implementation targets:

- `PreToolUse` hook for project-root containment.
- Instruction-root write block.
- Symlink write rejection.
- `_STATUS.md` transition tool with approval SHA gate.
- `Dependencies.csv` writer preserving v3.1 schema.
- `PostToolUse` provenance/diff/summary capture.
- `workspaceWrite` mode mapped through SDK posture plus Chirality overlay.

Acceptance:

- Writes outside project root denied.
- Instruction-root writes denied.
- Symlink writes rejected.
- Human-gate lifecycle transitions require approval SHA.
- Every write attempt produces permission/runtime events.

### R4 — Bash, Tool Result Budgeting, and Context Mirror

Purpose:

- Unlock bash only when explicit governed-mode posture, timeout, result storage, hooks, audit logging, and packaging behavior are ready.

Implementation targets:

- Add `Bash` to allowed tools only for explicitly permitted modes.
- Enforce timeout and capture stdout/stderr separately.
- Store large command output under session artifacts.
- Mirror SDK compaction boundaries into Chirality events.
- Preserve full audit replay even when model context is compacted.

Acceptance:

- Bash is denied by default and in `readOnly` / `dontAsk`.
- Denied bash never spawns.
- Allowed bash can time out, interrupt, and persist output metadata.
- `context.compacted` events record replay implications.

### R5 — Governed Subagent Runtime

Purpose:

- Connect existing `evaluateSubagentGovernance` to SDK subagent execution without weakening governance.

Implementation targets:

- Generate SDK `agents` definitions from allowed Type 2 task-agent instructions.
- Restrict child tools and working directory.
- Add `Agent` tool hook that calls `evaluateSubagentGovernance` and fails closed.
- Persist parent-child lifecycle records and output artifact paths.

Acceptance:

- Delegation without governance metadata is denied.
- Delegation to non-allowlisted or non-Type-2 candidate is denied.
- Parent session records child lifecycle and output reference.

### R6 — Extensibility and MCP Boundaries

Purpose:

- Document and mature extension boundaries after local/in-process SDK governance is reliable.

Implementation targets:

- Tool catalog with descriptions, modes, write scopes, and hook requirements.
- Naming convention for `mcp__chirality__*` tools.
- Tool collision prevention.
- Documentation for adding in-process tools without bypassing permissions or hooks.

Acceptance:

- New MCP tools pass through the same permission and hook overlay as SDK built-ins.
- Tool collisions are prevented.
- Remote MCP and plugin marketplace remain out of scope until governed future amendment.

### R7 — Domain Engine Profiles and Operation Proposals — Staged / Future Amendment

Purpose:

- Preserve the D-APP-49 through D-APP-52 staged-live source-type, closed-registry, read-tool, and pec-scoped loopback proposal surface while governing broader domain-engine activation separately.

Implementation targets:

- `DomainEngineProfile` contract and type guards (staged live).
- Protected path and proposal path policy.
- Deterministic adapter manifests.
- `OperationProposal` records and pec-scoped propose/refresh/validate transport (staged live).
- Human-gated operation application.
- Boundary notices.
- OpenPipeStress as first fixture profile if adopted.

Acceptance:

- Domain engines own domain truth.
- Agents write proposals and summaries, not protected model truth.
- Applying domain operations remains excluded from the tool surface and requires a future proposal plus explicit human acceptance.
- Chirality does not claim professional approval, code compliance, external validation, or solver ownership.

---

## 5. Consolidated Prior Custom-Runtime Phases

The prior custom-runtime roadmap is not deleted; it becomes the fallback path if the current provider/SDK adapter cannot satisfy critical boundaries. Under the approved vNext direction:

| Prior custom-runtime area | vNext disposition |
|---|---|
| Custom model/tool loop | Provided by a provider/SDK adapter when conformance passes. |
| Custom built-in read/write/bash tools | Prefer first-adapter SDK built-ins plus Chirality overlays where they satisfy Chirality policy. |
| Custom MCP transport | Prefer adapter-supported MCP where it satisfies Chirality policy. |
| Custom hook runner | Prefer adapter hooks plus Chirality callbacks where they satisfy Chirality policy. |
| Custom subagent runtime | Prefer adapter subagent support plus Chirality governance bridge where it satisfies Chirality policy. |
| Custom context compaction | Mirror adapter compaction; add custom fallback only if needed. |
| Custom tool result store | Chirality still owns artifact/preview policy. |
| Custom session events | Chirality still owns `events.jsonl`. |
| Custom permission semantics | Chirality still owns capability policy, decisions, and explicit hard-deny precedence. |

---

## 6. Cross-Cutting Workstreams

### 6.1 Governance Documents

- Keep `DIRECTIVE`, `CONTRACT`, `SPEC`, `TYPES`, `PLAN`, and `PRD` mutually aligned.
- Update agent instructions only after runtime policy and tool surfaces are accepted.
- Keep retired scope visibly out of current commitments.

### 6.2 Tests and Validation

Required categories:

- engine conformance;
- accepted-turn persistence;
- provider/SDK message mapping;
- event append/replay;
- settings isolation;
- adapter session link/resume;
- explicit hard-deny precedence;
- path containment;
- instruction-root protection;
- MCP tool contracts;
- tool result budget;
- compaction boundary mirror;
- subagent governance;
- domain profile validation after amendment.

### 6.3 Security and Privacy

- API keys never enter project files or runtime event payloads.
- Redaction applies across provider, SDK, tool, and run logs.
- Current shipped renderer network guardrails default to loopback + Anthropic API. Per D-T0-04 / D-APP-44 (OPEN RESIDENCY), the owner may configure additional providers/residency (local / Anthropic / other); the renderer must not egress beyond loopback + the configured provider(s), and absent an explicit owner provider/residency configuration the loopback + Anthropic default stands. The app does not itself enforce privacy/residency, but it also does not auto-egress (default-closed).
- Provider/SDK stderr/debug logs pass through redaction.
- Provider/SDK settings load is explicit and isolated.

### 6.4 Packaging

R1 packaging checks must prove:

- SDK package and subprocess/binary are accessible from built app.
- `asarUnpack` or equivalent packaging is correct if needed.
- Environment variables and API key handoff work without leaking secrets.
- SDK transcript placement/mirroring follows accepted decision.
- Instruction-root integrity passes.

### 6.5 Product Identity and UX

- UI copy describes Chirality’s governed-work posture.
- Actual human–agent dialogue is the primary workspace; shared intent is not a stored or authoritative UI object.
- Provenance-bearing artifacts may appear inline and open into focused views that retain a return-to-dialogue anchor.
- Work/Agents displays only admitted project/runtime records with visible source class/reference, status basis, currency, and exact recorded relationships.
- Conversational prose is not silently converted into work; runtime completion is not deliverable acceptance.
- Selected-session replay is clearly labelled, read-only, and isolated from primary dialogue draft, context, permissions, interruption, and interaction authority.
- Existing routes, queries, aliases/matrix behavior, APIs, SSE, provider composition, and old UI remain compatible until a separate owner retirement decision.
- Tool-heavy turns remain readable.
- Permission decisions are visible without overwhelming users.
- No UI or packaging implies Chirality is Claude Code or an Anthropic product.

---

## 7. Required Local Checks

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

Expected package artifacts:

- `frontend/dist/Chirality-0.1.0-arm64.dmg`
- `frontend/dist/mac-arm64/Chirality.app`
- `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`

---

## 8. Known Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Provider/SDK API drift | Pin versions; run adapter probes and conformance tests on upgrade. |
| Settings leakage | Shipped `settingSources: []`; test isolation. |
| Misunderstanding `allowedTools` | Document and test that restriction requires explicit hard-deny precedence, mode policy, hooks, and overlay. |
| SDK transcript path under user home | Prefer project-controlled `CLAUDE_CONFIG_DIR` / `SessionStore`; keep Chirality JSONL canonical. |
| Electron packaging of SDK subprocess | R1 packaging probe and `desktop:dist` validation. |
| Provider/SDK permissions insufficient for professional safety | Maintain Chirality path containment, human gates, redaction, and hooks. |
| Subagent inherited permissions | Restrict child tools/cwd; fail closed through governance hook. |
| Thin-wrapper drift | Enforce product identity, engine contract, and reliance-boundary register. |
| Engine adapter lock-in | Keep public APIs and canonical events provider-neutral. |
| Domain-engine scope creep | Keep domain profiles future-scope until core harness stability. |

---


## 9. Optional and Retired Scope Status

PKG-08 status remains explicit so runtime event logging does not accidentally reactivate retired hardening work:

- **Issued / in scope where already accepted:** reference hashes and dependency linter behavior.
- **Retired / out of scope without amendment:** execution-root validator, dependency graph generator, deliverable lock, unified pipeline run records, and staleness propagation tooling.

Harness runtime event logging is separate runtime infrastructure. It does not reactivate retired unified pipeline run records or broader PKG-08 hardening scope.

---

## 10. First Concrete Action

Create the R0/R1 implementation plan before code changes:

1. Draft `docs/harness/runtime_scope.md`.
2. Draft `docs/harness/runtime_engine_contract.md`.
3. Draft `docs/harness/reliance_boundary_register.md`.
4. Run a minimal first-adapter SDK probe for options, messages, hooks, permissions, MCP, agents, resume, storage, interrupts, and Electron packaging.
5. Define initial `EngineConformanceSuite` cases.
6. Specify session file migration from legacy `.json` records to folder layout.
7. Specify `HarnessEvent` mapper coverage.
8. Specify R1 tests and Section 9 validation IDs.
9. Only then implement the R1 code modules.

---

## 11. Out-of-Scope Until Amendment

- Remote MCP servers.
- Plugin marketplace.
- Remote execution.
- Broad tool search before local tool governance is mature.
- Windows/Linux release packaging.
- Retired PKG-08 deliverables.
- Domain-engine operation execution.
- Direct protected-domain-path writes by agents.
- Shipped `bypassPermissions` ordinary workflow.
- Ambient user/global Claude Code settings.
- Pi fork, Node sidecar, Pi-native tools/subagents/extensions/skills/ambient discovery, direct Pi supervisor, automatic fallback, or Pi write/shell/network capabilities. The sole current exception is the D-APP-72 / SCA-APP-002 pinned in-process Pi `0.80.10` read-only child tranche after Electron `43.2.0` (D-APP-98 successor authority; D-APP-72's `43.1.1` is historical).
- Concrete non-Anthropic provider *implementation* without an explicit owner provider/residency configuration and its own governed implementation tranche (per D-T0-04 / D-APP-44, OPEN RESIDENCY: provider/residency is owner-configurable, but actually building non-Anthropic routing or private-data egress remains net-new work that must still pass the engine-conformance gate (K-ENGINE-2) and respect the release fence; absent owner configuration the Anthropic default stands and the app does not auto-egress).

---

## 12. Roadmap Acceptance Principles

This plan remains acceptable only if:

- the first slice remains R0/R1 runtime contract + first-adapter probe + TurnEngine + event log + prompt composer + settings isolation;
- Claude Agent SDK / Anthropic remains the first adapter and, per D-APP-18, the key-aware default provider while provider-adapter generality remains the strategic architecture; Chirality is a governance/UI/audit/lifecycle/adapter layer over provider harness mechanics, not a standalone harness and not a Claude Code / Pi / Codex feature-parity effort (CONTRACT K-ENGINE-6);
- no write/bash/subagent/domain capability is exposed before permission, hooks, result storage, and event logging pass validation;
- roadmap order stays clear: provider-adapter runtime spine before tool expansion, read before writes/bash, domain after core harness stability;
- runtime event logging does not reactivate retired pipeline run-record scope;
- product identity and professional-boundary language remain Chirality-owned.

---

## 13. Accepted Scope Changes

| Scope Change | Date | Effect |
|---|---|---|
| `SCA-APP-001` | 2026-06-13 | Approved provider-adapter generality, retained Claude Agent SDK / Anthropic as first concrete adapter, ruled Pi pattern-corpus-only, and reframed permission governance as capability-forward with explicit hard-deny precedence. D-APP-12 later clarified that `agentSdk` remains opt-in pending further proof/ruling. |
| `SCA-APP-002` | 2026-07-21 | Authorizes the bounded Pi `0.80.10` / authenticated loopback oMLX second-engine tranche, subject to Electron `43.1.1` prerequisite proof (Electron authority since superseded by D-APP-98: `43.2.0`), provider-neutral contracts, fail-closed conformance/security validation, and a governed read-only Agent 2 child milestone. |
| `SCA-APP-003` | 2026-07-22 | Promotes the executable harness to root `runtime/`, then adds one shared daemon, authenticated Unix-socket client/CLI, explicit local-model residency, the app-dev Agent 1 → local Agent 2 pilot, PEC client migration, and public generic-runtime export. |
| `SCA-APP-004` | 2026-07-23 | Selects Woven Dialogue with a Work/Agents Coordination Panel; preserves runtime/API/SSE/security/history and compatibility while adding provenance-labelled informational projection, explicit context/artifact anchors, and strict primary-dialogue/read-only-replay separation. |

### 13.1 D-APP-73 execution order

1. Close and commit D-APP-72/SCA-APP-002 after validation.
2. Reconcile root, app-dev, tier-0 domain, and PEC governance.
3. Promote provider-neutral packages without behavior change.
4. Introduce the daemon and convert Desktop into a client.
5. Add the bundled CLI and explicit one-primary-model residency control.
6. Prove the app-dev Agent 1 → read-only local Agent 2 vertical slice.
7. Migrate PEC’s agent path without a dual execution loop.
8. Export the generic runtime after both pilots pass.

Piping, automatic scheduling, local Agent 1, multiple simultaneous primary
local models, and production PEC use remain later governed milestones.

### 13.2 SCA-APP-004 implementation and cutover order

1. Freeze a compatibility matrix for `/`, `/chat`, `/pipeline`, `/workbench`,
   known and unknown query parameters, browser APIs, SSE names/order, provider
   singletons, drafts/toolkit/layout state, and packaged Desktop startup.
2. Add the Woven Dialogue shell behind a reversible compatibility selection
   while keeping the provider composition and primary dialogue controller
   singular.
3. Add provenance-bearing inline/focused artifact presentation and explicit
   next-turn context references without treating visible material as model
   context.
4. Add the Work projection over explicitly recorded project work with source
   class/reference, status basis, currency, responsibility/relationship
   references, and explicit stale/empty/conflict/unknown states.
5. Add the Agents projection over recorded sessions, exact canonical
   parentage, attribution, and selected-session read-only replay without
   global AgentRun discovery or runtime expansion.
6. Re-host Workbench, Pipeline, toolkit, working-root, credential, runtime,
   and settings surfaces while preserving their existing semantic and
   security owners.
7. Apply versioned, non-destructive, rollback-safe local-state migration and
   complete accessibility, focus, keyboard, responsive, bounded-data, and
   performance work.
8. Run component/render, route/query, API/SSE/replay/interruption, runtime,
   security, build, premerge, instruction-root, and packaged Desktop
   validation, followed by independent semantic-boundary review.

The existing loop-first UI remains the compatibility implementation after
this sequence until parity evidence is accepted and the owner separately
authorizes retirement. SCA-APP-004 does not authorize runtime/API expansion,
arbitrary graphs, multiple-child execution, scheduling, direct child
messaging, global AgentRun discovery, automatic intent summarization, or model
routing/residency control.
