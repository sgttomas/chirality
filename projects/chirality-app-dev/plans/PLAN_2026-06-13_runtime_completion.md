# Chirality App Runtime Completion Plan

**Date:** 2026-06-13
**Epistemic status:** PROPOSAL (non-governing)
**Product:** Chirality desktop harness and bundled agent operating system

This plan is the active app-dev tranche-selection surface for governed harness-runtime work. It proposes a route from the current runtime integration state to the runtime direction defined by `docs/PRD.md`, the strategic roadmap in `docs/PLAN.md`, and accepted scope-change records.

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

1. `docs/PRD.md` product goals for a local desktop harness, Chirality-owned provider-adapter runtime contract, append-only audit/event model, permission semantics, first-adapter SDK isolation, and human-gated professional boundaries.
2. `docs/PLAN.md` strategic runtime phases R0-R7, with `docs/PLAN.md` retained as strategic roadmap rather than active work queue.
3. `frontend/docs/harness/runtime_engine_contract.md` for current runtime adapter, event, session, and tool-descriptor contract posture.
4. `execution/_ScopeChange/SCA-APP-001_2026-06-13_1819_Provider-General_Runtime_Pi_Pattern-Corpus_v2/` for the accepted provider-general runtime, Pi pattern-corpus-only, and capability-forward permission-governance amendment.

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
| 1 | **Capability policy / permission overlay skeleton** | Define `HarnessPermissionDecision` and capability-forward, mode-aware permission resolution against descriptor metadata with explicit hard-deny precedence. Keep tool execution disabled. | Unit tests for allow/deny/ask precedence; `npm run test -- permission tool-descriptor sdk-options-builder`; `npm run typecheck`. |
| 2 | **SDK read-tool exposure behind capability policy** | Enable only read-class first-adapter SDK built-ins after the overlay exists. Preserve `disallowedTools` for write, shell, network, and subagent surfaces. | Unknown tools fail structurally; explicitly denied tools are not exposed/executed; SDK options tests cover read-only and dontAsk modes. |
| 3 | **Read MCP / descriptor integration** | Add Chirality-owned read MCP descriptors for status/dependency/scope/scaffold-preview surfaces without write capability. | Descriptor tests, MCP input/output tests, and no write/bash exposure. |
| 4 | **Tool result and event evidence expansion** | Persist tool permission/start/completion/failure evidence and budgeted result metadata for read tools. | `HarnessEvent` replay tests and conformance fixture coverage. |
| 5 | **Write/edit hooks and path containment** | Add write/edit policy only after read surface is proven. Enforce project-root containment, instruction-root block, symlink rejection, provenance, and diff/result evidence. | Path/hook tests, denied-write tests, and no bash exposure. |
| 6 | **Bash, governed subagents, provider-expansion packet** | Prepare or execute only after required human gates and prior conformance evidence. Pi remains pattern-corpus reference only; concrete non-Anthropic providers require future bounded implementation tranches. | Ruling records in `_DECISIONS/_REGISTER.md`; no implementation before approval. |

## Governance Support Lane

This lane records human-requested control-plane support work that improves validation, release-quality, and workflow governance without reordering the runtime dependency spine above.

| ID | Tranche | Status | Residual handoff | Validation pointer |
|---|---|---|---|---|
| GOV-QUALITY-001 | **Quality and validation skeleton** | LANDED 2026-06-13 | Build/release skeleton landed in `GOV-BUILD-001`. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| GOV-BUILD-001 | **Build/release skeleton** | LANDED 2026-06-13 | Workflow and docs index cleanup remains next if the governance migration lane continues. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| GOV-WORKFLOW-001 | **Workflow and docs index cleanup** | LANDED 2026-06-13 | State-file retirement landed in `GOV-STATE-001`. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| GOV-STATE-001 | **Retire next-instance state file** | LANDED 2026-06-13 | Governance-support lane has no current next item; return to runtime spine unless the human selects another governance tranche. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| SCA-APP-001-CLOSURE-001 | **Scope-change pointer, propagation, and supersession repair** | LANDED 2026-06-13 | Package-local context refresh remains if SCA closure continues. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance and supersession-map checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |

## Human-Gated Decisions

Decision authority lives in `execution/_Coordination/_DECISIONS/_REGISTER.md`. This table is a planning mirror only.

| ID | Decision | Blocks | State | Packet | Ruling |
|---|---|---|---|---|---|
| D-APP-01 | Pi posture: adapter/fork/import/spike scope versus pattern corpus only | Any Pi adapter, fork, package import, sidecar, or spike work | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-01_RULING_2026-06-13.md` |
| D-APP-02 | Pi package import/runtime strategy | Any direct Pi package dependency or Node 22 sidecar/runtime-floor change for Pi | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-02_RULING_2026-06-13.md` |
| D-APP-03 | Provider-adapter generality beyond the current shipped Anthropic path | Any concrete non-Anthropic shipped backend adapter or provider routing | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-03_RULING_2026-06-13.md` |

## Guardrails

- Do not treat `docs/PLAN.md` as the active queue; it remains the strategic roadmap.
- Do not expose write/edit/bash/network/subagent capabilities or concrete new providers before their prerequisites and human gates.
- Do not implement Pi adapter, fork, import, sidecar, runtime-floor migration, or spike work under this plan; Pi is a pattern corpus/reference only after D-APP-01 and D-APP-02.
- Treat provider-adapter generality as approved strategy after D-APP-03, but keep concrete new provider implementation behind future bounded tranches.
- Do not make package, dependency, runtime-language, or desktop-wrapper migrations in this control-plane plan.
- Do not turn runtime events, SDK transcripts, completion logs, handoff prose, or coordination state files into project-truth substitutes.
- Do not recreate `execution/_Coordination/NEXT_INSTANCE_STATE.md`; discover current state from authoritative surfaces, dependency/SCC evidence, source/tests, validation artifacts, and git history.
- Do not advance release-readiness, lifecycle, professional, certification, sealing, authentication, or code-compliance claims.
