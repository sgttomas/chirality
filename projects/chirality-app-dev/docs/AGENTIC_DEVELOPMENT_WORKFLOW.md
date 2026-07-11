# AGENTIC DEVELOPMENT WORKFLOW - Chirality App Dev

**Status:** Draft governance support surface
**Date:** 2026-06-13
**Product:** Chirality desktop harness and bundled agent operating system
**Applies to:** app-dev agentic coordination, tranche selection, validation routing, and closeout discipline

## 1. Purpose

This document maps how agentic development moves through the app-dev governance surfaces. It explains the current workflow; it does not replace `AGENTS.md`, `agents/AGENT_*.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PRD.md`, `docs/PLAN.md`, `execution/_Coordination/_COORDINATION.md`, accepted execution artifacts, source, tests, decision records, planning records, or human project-authority instructions.

If this map conflicts with a governing document, active coordination record, selected tranche brief, human ruling, or source/test evidence, stop and surface the conflict.

This workflow is project guidance only. It is not lifecycle approval, release publication authorization, professional approval, certification, sealing, authentication, code-compliance acceptance, or external validation for reliance.

## 2. Authority Map

| Surface | What it owns | Boundary |
|---|---|---|
| `/Users/ryan/ai-env/projects/chirality/AGENTS.md` and `agents/AGENT_*.md` | Canonical agent roles, persona semantics, and task-agent discipline. | This file does not redefine canonical agent behavior. |
| `docs/DIRECTIVE.md` | Founding intent, design philosophy, filesystem truth posture, and professional-responsibility model. | Does not provide implementation sequencing by itself. |
| `docs/CONTRACT.md` | Binding invariant catalog for runtime, permissions, events, packaging, network, release, and professional boundaries. | Invariants require enforcement through code, tests, review, or human gates. |
| `docs/SPEC.md` | Physical structures, file formats, runtime mechanics, validation surfaces, and future domain-engine mechanics. | Does not authorize out-of-plan implementation. |
| `docs/TYPES.md` | Vocabulary, identifiers, states, runtime terms, and artifact names. | Does not settle active queue priority. |
| `docs/PRD.md` | Product requirements and accepted app-dev runtime direction. | Does not replace directive, contract, spec, types, or human gates. |
| `docs/PLAN.md` | Strategic roadmap and sequencing rationale. | It is not the active queue. |
| `docs/VALIDATION_STRATEGY.md` | Evidence classification and validation command routing. | Evidence does not create release readiness or approval. |
| `docs/RELEASE_QUALITY_GATES.md` | Release-quality gate selection by change family. | Gate evidence is not release publication authorization. |
| `docs/BUILD_AND_RELEASE.md` | Local build, packaging, artifact, and release-evidence command map. | It is not a live CI workflow or release approval. |
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Package and deliverable decomposition basis. | Does not substitute for current source/test state. |
| The newest `loop/WORKPLAN_*.md` (entry via `loop/LOOP_INIT.md`) | Current entry protocol, work selection from deliverable `_STATUS.md` `## Remaining` sections, validation closeout, and hard fences. | Handoff prose is not substitute authority. |
| `execution/_Coordination/_COORDINATION.md` | Ruled coordination records: work-discovery convention, authority-and-state rules, guidance-correction rule. | A record surface, not the operative protocol. |
| `execution/_Reconciliation/DepClosure/_LATEST.md` and latest DepClosure snapshot | Dependency/SCC discovery evidence. | Snapshot evidence informs blocker analysis; it does not replace decomposition truth or plan selection. |
| `plans/PLAN_2026-06-19_loop_first_pivot.md` | Active D-APP-28 full loop-first pivot queue. | Tranche spine 28a -> 28b -> 28c -> 28d -> 28e; routing/layout change only; does not touch the public UIEvent contract or permission plane, and does not approve default-provider cutover. |
| `plans/DESIGN_2026-06-18_agent_orchestration_ui.md` | Active Agent-Orchestration UI & Information Architecture redesign arc; Phases 1-5 complete. | Design basis for the harness-ability reorganization; does not by itself authorize tranches beyond the active loop-first pivot queue. |
| `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md` | Completed Live Packaged `agentSdk` Read-Tool Proof queue. | Records the bounded proof run (D-APP-17 passed with `sonnet`) and its `plans/artifacts/*` evidence; no longer selects active tranches; does not approve default-provider cutover before D-APP-18, release readiness, or professional reliance. |
| `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` | Completed R6 Extensibility & MCP Boundary Maturity program. | Records local/in-process tool catalog, naming, collision prevention, and contributor-doc work; no longer selects active tranches. |
| `plans/PLAN_2026-06-16_runtime_stabilization.md` | Completed Runtime Stabilization program. | Records STAB-00..STAB-06 runtime stabilization work, evidence, and rulings; no longer selects active tranches. |
| `plans/PLAN_2026-06-16_six_node_scc_resolution.md` | Completed non-governing SCC-resolution tranche-selection surface. | Records SCC-resolution work; does not change product requirements, decomposition truth, or release posture. |
| `plans/PLAN_2026-06-13_runtime_completion.md` | Retired runtime completion history. | Records landed runtime-spine work; it is not the active queue. |
| `plans/PLAN_COMPLETION_LOG.md` | Landed-tranche narrative history. | History only; not project truth or approval. |
| `execution/_Coordination/_DECISIONS/_REGISTER.md` | Human-gated decision-packet status and rulings. | Agents prepare packets; humans rule. |
| `frontend/docs/harness/runtime_engine_contract.md` | Current runtime adapter, event, session, and tool-descriptor contract posture. | Does not override higher governance or active plan staging. |
| Source, tests, build scripts, validation artifacts, and git history | Current implementation truth and evidence. | Implementation does not silently amend governed requirements. |

## 3. Current Development Posture

The current default work mode is bounded app-integration tranches. The active development
queue is `plans/PLAN_2026-06-19_loop_first_pivot.md` — the D-APP-28 full loop-first pivot,
with tranche spine 28a -> 28b -> 28c -> 28d -> 28e. No tranche has started; no source code
is written yet. This is a routing/layout change only: the public UIEvent contract and the
permission plane are untouched, in-flight turns survive every relayout, and nothing is
deleted. It builds on the active Agent-Orchestration UI & Information Architecture redesign
arc (`plans/DESIGN_2026-06-18_agent_orchestration_ui.md`), whose Phases 1-5 are complete
(typecheck clean, 491 vitest tests, `next build` green). The Live Packaged `agentSdk`
Read-Tool Proof is completed closed history (D-APP-17 passed with `sonnet`). The R6
Extensibility & MCP Boundary Maturity program is completed closed history after R6-05;
R6-04 was deferred as optional organization work. The Runtime Stabilization program is
completed closed history after STAB-06. The residual six-node strict dependency SCC is
closed by accepted DepClosure snapshot `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z`. The
completed SCC-resolution plan has:

- a safe-move tranche for source-grounded decompose/invert dependency-row moves;
- a required fresh dependency-closure audit after the safe-move tranche;
- a human-gated move packet if cut, merge, or objective-dependent rulings are needed; and
- a closeout tranche that recorded strict acyclicity and updated control-plane handoff state.

Select exactly one tranche unless the human explicitly approves batching. Tranches
selected from unblocked rows in a human-selected active plan are pre-approved for
execution within their stated write scope. Stop when further progress requires a human
ruling. In the active loop-first pivot plan, advance the 28a -> 28b -> 28c -> 28d -> 28e
spine in order, keeping each tranche independently `npm run typecheck` + vitest-green
(491 baseline) with `next build` prerendering affected routes. Do not return to the
completed live-proof plan, completed R6 program, completed Runtime Stabilization plan, the
closed SCC-resolution plan, or the retired runtime completion plan for new implementation
work.

## 4. Phase-Aware Loop

| Phase | Dominant question | Normal work unit | Coordination emphasis |
|---|---|---|---|
| Governance baseline | What must remain true? | Governance doc or decomposition update. | Authority hierarchy, invariant clarity, project-truth boundaries, human gates. |
| Runtime integration | What runtime capability should become real next? | Narrow app/runtime slice. | Product-owned contract, SDK isolation, event evidence, tests, and premerge validation. |
| Permission/tool expansion | What can the model see or do? | Permission/tool tranche. | Deny-first posture, descriptor metadata, hooks, MCP wrappers, result evidence. |
| SCC resolution | Which cycle-participating dependency rows can be resolved by recorded moves? | Decompose/invert row tranche, closure audit, or human-gated move packet. | Objective-scoped graph semantics, no silent linearization, immutable closure snapshots. |
| Build and release evidence | What proves software-quality posture? | Docs, validation, packaging, or evidence tranche. | Evidence routing, package integrity, release-quality gates, no release claims. |
| Domain-engine future scope | How will Chirality govern domain truth without owning it? | Decision packet, profile, adapter, or proposal workflow. | Protected paths, operation proposals, deterministic checks, human acceptance. |

The current phase is the agent-orchestration UI loop-first pivot (`plans/PLAN_2026-06-19_loop_first_pivot.md`),
building on the redesign arc whose Phases 1-5 are complete. Runtime integration through the
retired completion plan, Runtime Stabilization program, R6 local/in-process
extension-boundary program, and the completed live packaged first-adapter proof is landed
through the accepted scope. The active plan reorganizes routing/layout around the live
event-stream loop without touching the public UIEvent contract or permission plane. D-APP-18
(default-provider cutover) remains a separate open decision before any default-provider
review. Formal lifecycle issuance, release readiness, professional approval, certification,
sealing, authentication, and code-compliance acceptance remain separate human-governed
states.

## 5. Standard Session Flow

1. Read `AGENT_WORKING_ITEMS.md` and act in the `WORKING_ITEMS` persona.
2. Read `execution/_Coordination/_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, the current selected plan, and the decision register.
3. Discover current state from governed docs, decomposition and deliverable artifacts, dependency/SCC snapshots, source, tests, validation evidence, and git history.
4. Read authority and implementation-reference files needed for the selected tranche.
5. Record `git status --short` before planning or edits.
6. Select the earliest unblocked active-plan item; for the current loop-first pivot queue, advance the 28a -> 28b -> 28c -> 28d -> 28e tranche spine in order.
7. Keep writes scoped to the tranche.
8. Route validation through `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` when applicable.
9. Update affected active-plan rows, completion log, discovery pointers, and decision-register rows only when their state changes.
10. Autonomously hand off to a `CHANGE` agent/subagent for final Git/file-state review.
11. `CHANGE` commits and pushes validated work as the ordinary terminal action when validation and git state allow closeout.

## 6. TASK Subagent Discipline

`TASK` fan-out is optional and bounded. Use it only when subscopes are separable, write scopes are disjoint, and the brief names:

- source files to read;
- allowed write targets;
- validation expected;
- whether production code may be changed or the output is assessment/docs only;
- excluded scope and human-ruling stops.

The parent `WORKING_ITEMS` agent remains responsible for integration, validation, coordination updates, invoking the `CHANGE` closeout handoff, and final summary. `TASK` outputs are draft evidence until integrated and validated.

## 7. Closeout Shape

A valid closeout identifies:

- completed tranche;
- validation performed, including skipped checks and reasons;
- files changed;
- decision packets or human rulings pending;
- next selected plan item, or state which loop-first pivot tranche (28a -> 28b -> 28c -> 28d -> 28e) is next in the active queue;
- `CHANGE` closeout result, including commit and push result when completed.

For governance-only tranches, frontend runtime tests are normally skipped and the skip must be explicit. For runtime, SDK, permission, network, packaging, or release-significant tranches, use the applicable gate family before closeout.

## 8. Non-Authority Boundaries

The following are evidence, history, or convenience surfaces, not substitute authority:

- runtime events and SDK transcripts;
- completion logs and handoff prose;
- generated build artifacts;
- validation summaries;
- chat history and model context;
- UI drafts or local presets.

`execution/_Coordination/NEXT_INSTANCE_STATE.md` is retired. Do not use it as the current app state, update it, or recreate it.

Accepted project truth must land in governed docs, accepted execution artifacts, source, tests, validation records, decision records, or git history as appropriate.
