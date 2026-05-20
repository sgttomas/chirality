# PLAN - Development Roadmap

Status: Active roadmap derived from `docs/PRD.md`
Date: 2026-05-20
Applies to: Chirality App vNext development and release planning

This document summarizes the sequencing plan. The PRD defines product scope. The CONTRACT defines invariants. The SPEC defines mechanics. This PLAN defines the order of work and why that order matters.

---

## 1. Control-Plane Boundary

- `docs/PLAN.md` is strategic and sequencing-oriented.
- `docs/PRD.md` is the product source of truth.
- `docs/CONTRACT.md` is the invariant catalog.
- `docs/SPEC.md` is the physical/API/runtime specification.
- Execution-package coordination, if present, belongs in execution coordination artifacts, not in this document.

---

## 2. Current Baseline

The current baseline includes:

- Electron/Next desktop shell.
- PORTAL, WORKBENCH, PIPELINE, file tree, toolkit, and chat surfaces.
- Working-root validation and selection.
- Harness session APIs and turn streaming.
- Anthropic provider path and stub provider path.
- Attachment resolver.
- API key UI and local secure storage.
- Execution-root scaffolding.
- Deliverable status and dependency APIs.
- Subagent governance evaluator.
- Harness validation scripts.
- macOS Apple Silicon unsigned DMG runbook.

The baseline is useful but not yet a governed agent runtime.

Primary gap:

- Current turn execution is still mostly a provider streaming adapter, with no complete SDK-hosted governed runtime, no canonical per-turn Chirality event log, no real prompt composer, no permission overlay, and no conformance-tested engine boundary.

---

## 3. Architectural Direction

The runtime direction is:

> SDK-privileged, contract-owned, and Chirality-governed.

The Claude Agent SDK is the preferred engine for generic runtime mechanics. Chirality owns the product contract:

- `AgentEnginePort` / `RuntimeEngineContract`;
- browser `UIEvent` mapping;
- canonical `HarnessEvent` schema;
- `.chirality/sessions/<id>/events.jsonl` audit mirror;
- permission semantics;
- hook policy;
- path containment;
- human gates;
- product identity;
- fallback criteria.

The first implementation work must prevent SDK-shaped leakage into product-owned state.

---

## 4. Runtime Roadmap

### R0 - Runtime Scope Confirmation, SDK Probe, And Reliance Boundary Register

Purpose:

- confirm what Chirality owns versus what the SDK owns;
- empirically validate SDK behavior before deep integration;
- define reliance boundaries and enforcement surfaces.

Deliverables:

- `docs/harness/runtime_scope.md`
- `docs/harness/runtime_engine_contract.md`
- `docs/harness/reliance_boundary_register.md`
- updated `docs/harness/chirality_harness_graphs_and_sequence.md`
- SDK probe notes for package version, message sequence, settings, permissions, hooks, MCP, agents, resume, session store, config dir, interrupt, packaging, API key handling, branding, and fallback triggers.

Acceptance:

- SDK confirmed viable for R1 or governed fallback decision made.
- Engine conformance tests specified.
- Every P0 reliance boundary has a non-prompt-only enforcement plan.
- No local tools exposed outside controlled validation.

### R1 - SDK Adoption, Engine Contract, Thin TurnEngine, Prompt Composer, And Audit JSONL

Purpose:

- replace the current direct provider streaming adapter with SDK-hosted runtime behavior while preserving UI/API behavior.

Implementation targets:

- add and pin `@anthropic-ai/claude-agent-sdk`;
- define `agent-engine-port.ts`;
- add conformance tests;
- add reliance-boundary register support;
- add `turn-engine.ts`;
- add `sdk-options-builder.ts`;
- add `sdk-message-mapper.ts`;
- add `session-events.ts`;
- add `event-schema.ts`;
- add `run-logger.ts`;
- add `persona-composer.ts`;
- add `sdk-session-link.ts`;
- wire `CHIRALITY_HARNESS_PROVIDER=anthropic` to the SDK-backed path when ready.

Acceptance:

- existing tests pass;
- Section 8 validation passes;
- `turn.accepted` persists before SDK `query()`;
- engine conformance suite passes;
- route shape and SSE names unchanged;
- `settingSources: []` isolation test passes;
- SDK session linkage persists;
- no new user-visible local tool capability is enabled.

### R2 - Permission-Gated Read Surface And First Chirality MCP Tools

Purpose:

- make `opts.tools` meaningful without enabling writes or shell.

Implementation targets:

- `ChiralityPermissionOverlay`;
- mapping for `readOnly`, `dontAsk`, and `ask`;
- SDK read tools where available;
- in-process Chirality MCP read tools for status, dependencies, scope scan, and scaffold preview/dry-run.

Acceptance:

- unknown tools produce structured validation errors;
- denied tools never execute;
- read tools emit UI and JSONL events;
- `dontAsk` denies non-approved actions.

### R3 - Write Surface And Chirality Hooks

Purpose:

- enable governed writes only after hooks and deny-first policy are active.

Implementation targets:

- project-root containment hook;
- instruction-root write block;
- symlink write rejection;
- `_STATUS.md` transition MCP tool;
- `Dependencies.csv` writer;
- provenance/diff summary;
- `workspaceWrite` and `ask` mappings.

Acceptance:

- outside-root writes denied;
- instruction-root writes denied;
- symlink writes rejected;
- human-gate transitions require approval SHA;
- every write attempt records permission events.

### R4 - Bash, Tool Result Budgeting, And Context Mirror

Purpose:

- unlock bash only as a governed capability and add output/compaction discipline.

Implementation targets:

- bash default-denied;
- bash timeout and command metadata;
- stdout/stderr capture where available;
- result size budget;
- artifact storage;
- compaction event mirror.

Acceptance:

- denied bash does not spawn;
- large output does not flood chat;
- full audit trail is reconstructible;
- compaction boundaries are visible in replay.

### R5 - Governed Subagent Runtime

Purpose:

- connect Type 2 task agents to SDK `agents` under Chirality governance.

Implementation targets:

- generate SDK agent definitions from `agents/AGENT_*.md`;
- restrict tools/model/max turns;
- fail-closed `Agent` tool gate through `evaluateSubagentGovernance`;
- parent-child session event linkage.

Acceptance:

- ungated delegation denied;
- non-allowlisted or non-Type-2 delegation denied;
- parent session records child lifecycle and output paths.

### R6 - Extensibility And MCP Boundaries

Purpose:

- define safe local extension rules without opening a marketplace or remote execution surface.

Implementation targets:

- tool catalog;
- `mcp__chirality__*` naming convention;
- collision prevention;
- documentation for new in-process Chirality MCP tools;
- deferred tool search only if justified.

Acceptance:

- new tools pass through the same permission overlay and hooks;
- remote MCP and plugins remain out of scope unless amended.

### R7 - Domain Engine Profiles And Operation Proposals

Purpose:

- add generic domain-engine awareness only after core runtime stability.

Acceptance:

- `DomainEngineProfile` validation deterministic;
- OpenPipeStress representable as fixture profile;
- protected paths not agent-writable;
- `OperationProposal` records precede application;
- human acceptance required for domain state changes.

---

## 5. Release And Validation Roadmap

Required checks from `frontend/`:

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

Post-R1 SDK checks:

- SDK version pinned;
- SDK TypeScript options compile;
- packaged app locates SDK subprocess/binary;
- SDK calls do not broaden network policy;
- SDK stderr/debug output redacted;
- `settingSources` default is `[]`;
- `resume` works from persisted SDK linkage.

---

## 6. Optional And Retired Scope

PKG-08 status remains:

- issued/in-scope: reference hashes and dependency linter where already accepted;
- retired/out-of-scope: execution-root validator, dependency graph generator, deliverable lock, unified pipeline run records, and staleness propagation tooling.

Harness runtime event logging is separate runtime infrastructure and does not reactivate retired pipeline run records.

---

## 7. Sequencing Rationale

Runtime order matters:

1. Define the engine contract before relying on the SDK.
2. Persist accepted turns before executing the model.
3. Establish canonical Chirality events before expanding tools.
4. Add read tools before writes.
5. Add writes before bash.
6. Add bash only after timeout, result storage, hooks, and audit logging.
7. Add subagents only after parent event and permission records are stable.
8. Add domain profiles only after protected-path policy and operation proposals are ready.

This order preserves the PRD's core bargain: use the SDK where it is strong, but keep Chirality's reliance boundaries product-owned and testable.
