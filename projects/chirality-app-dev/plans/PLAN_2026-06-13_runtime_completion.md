# Chirality App Runtime Completion Plan

**Date:** 2026-06-13
**Epistemic status:** PROPOSAL (non-governing)
**Product:** Chirality desktop harness and bundled agent operating system

This plan is the active app-dev tranche-selection surface for governed harness-runtime work. It proposes a route from the current runtime integration state to the runtime direction defined by `docs/PRD.md` and the strategic roadmap in `docs/PLAN.md`.

This plan does not change product requirements, lifecycle state, release readiness, professional approval, certification, sealing, authentication, or code-compliance posture. Project truth remains in governed docs, decomposition and deliverable artifacts, source, tests, evidence records, and git history. Humans decide all gates.

## Plan Maintenance

This plan is a selection instrument, not a history. When an item lands, compress its row to one line with:

- `LANDED <date>`;
- tranche id, or commit when no tranche id exists;
- residual handoffs;
- validation pointer;
- a link to `plans/PLAN_COMPLETION_LOG.md`.

Move narrative detail to `plans/PLAN_COMPLETION_LOG.md`. Partially landed rows keep remaining scope in this plan and move landed detail to the log. Decision rows carry only state, packet pointer, and ruling pointer.

## Completion Yardstick

Completion is defined against:

1. `docs/PRD.md` product goals for a local desktop harness, Chirality-owned runtime contract, append-only audit/event model, permission semantics, SDK isolation, and human-gated professional boundaries.
2. `docs/PLAN.md` strategic runtime phases R0-R7, with `docs/PLAN.md` retained as strategic roadmap rather than active work queue.
3. `frontend/docs/harness/runtime_engine_contract.md` for current runtime adapter, event, session, and tool-descriptor contract posture.

## Current Runtime Posture

| Area | Status | Residual handoff | Validation pointer |
|---|---|---|---|
| Provider-neutral contract cleanup | LANDED 2026-06-13 (`6b23eb96c`) | Continue avoiding SDK-shaped public/core contract leakage. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Commit/test history. |
| Turn lifecycle extraction | LANDED 2026-06-13 (`c8d735e2e`) | Continue extracting policy from route-owned surfaces where planned. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Commit/test history. |
| HarnessEvent expansion | LANDED 2026-06-13 (`e39d07827`) | Continue conformance and replay coverage as runtime surfaces grow. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Commit/test history. |
| Engine conformance fixtures | LANDED 2026-06-13 (`02f92417b`) | Extend fixtures for tool and permission phases. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Commit/test history. |
| Tool descriptor design | LANDED 2026-06-13 (`3bf6f9fb1`) | Permission overlay skeleton remains next. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Prior tranche closeout evidence recorded in `plans/PLAN_COMPLETION_LOG.md`. |

## Dependency Spine

Select the earliest unblocked item in this table unless regression repair is needed for already-landed runtime work or the human explicitly approves a different tranche.

| # | Tranche | Scope | Acceptance / validation |
|---|---|---|---|
| 1 | **Permission overlay skeleton** | Define `HarnessPermissionDecision` and deny-first, mode-aware permission resolution against descriptor metadata. Keep tool execution disabled. | Unit tests for allow/deny/ask precedence; `npm run test -- permission tool-descriptor sdk-options-builder`; `npm run typecheck`. |
| 2 | **SDK read-tool exposure behind deny-first policy** | Enable only read-class SDK built-ins after the overlay exists. Preserve `disallowedTools` for write, shell, network, and subagent surfaces. | Unknown tools fail structurally; denied tools are not exposed; SDK options tests cover read-only and dontAsk modes. |
| 3 | **Read MCP / descriptor integration** | Add Chirality-owned read MCP descriptors for status/dependency/scope/scaffold-preview surfaces without write capability. | Descriptor tests, MCP input/output tests, and no write/bash exposure. |
| 4 | **Tool result and event evidence expansion** | Persist tool permission/start/completion/failure evidence and budgeted result metadata for read tools. | `HarnessEvent` replay tests and conformance fixture coverage. |
| 5 | **Write/edit hooks and path containment** | Add write/edit policy only after read surface is proven. Enforce project-root containment, instruction-root block, symlink rejection, provenance, and diff/result evidence. | Path/hook tests, denied-write tests, and no bash exposure. |
| 6 | **Bash, governed subagents, Pi adapter packet** | Prepare or execute only after required human gates and prior conformance evidence. Pi work remains packet/spike only until approved. | Decision packets or human rulings in `_DECISIONS/_REGISTER.md`; no implementation before approval. |

## Governance Support Lane

This lane records human-requested control-plane support work that improves validation, release-quality, and workflow governance without reordering the runtime dependency spine above.

| ID | Tranche | Status | Residual handoff | Validation pointer |
|---|---|---|---|---|
| GOV-QUALITY-001 | **Quality and validation skeleton** | LANDED 2026-06-13 | Build/release skeleton landed in `GOV-BUILD-001`. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| GOV-BUILD-001 | **Build/release skeleton** | LANDED 2026-06-13 | Workflow and docs index cleanup remains next if the governance migration lane continues. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| GOV-WORKFLOW-001 | **Workflow and docs index cleanup** | LANDED 2026-06-13 | Governance-support lane has no current next item; return to runtime spine unless the human selects another governance tranche. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |

## Human-Gated Decisions

Decision authority lives in `execution/_Coordination/_DECISIONS/_REGISTER.md`. This table is a planning mirror only.

| ID | Decision | Blocks | State | Packet | Ruling |
|---|---|---|---|---|---|
| D-APP-01 | Whether to approve a constrained Pi-backed backend-adapter spike after runtime contract hardening and conformance fixtures exist | Any `pi-ai` / `pi-agent-core` adapter implementation | NOT_PREPARED | - | - |
| D-APP-02 | If Pi packages are imported, choose runtime strategy: raise runtime floor to Node `>=22.19.0` or isolate Pi behind a Node 22 sidecar | Any direct Pi package dependency | NOT_PREPARED | - | - |
| D-APP-03 | Whether to broaden network/provider policy beyond the current Anthropic-centered runtime scope | Any non-Anthropic shipped backend adapter or provider routing | NOT_PREPARED | - | - |

## Guardrails

- Do not treat `docs/PLAN.md` as the active queue; it remains the strategic roadmap.
- Do not expose write/edit/bash/network/subagent/Pi capabilities before their prerequisites and human gates.
- Do not make package, dependency, runtime-language, or desktop-wrapper migrations in this control-plane plan.
- Do not turn runtime events, SDK transcripts, completion logs, or coordination state into project-truth substitutes.
- Do not advance release-readiness, lifecycle, professional, certification, sealing, authentication, or code-compliance claims.
