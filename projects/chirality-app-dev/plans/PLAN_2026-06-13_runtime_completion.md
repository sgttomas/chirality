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
| Tool descriptor design | LANDED 2026-06-13 (`3bf6f9fb1`) | Permission overlay skeleton has landed; continue preserving descriptor metadata as read exposure begins. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Prior tranche closeout evidence recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| Capability policy / permission overlay skeleton | LANDED 2026-06-13 (`1532b32c7`) | SDK read-tool exposure has landed; pre-existing instruction-root integrity evidence debt remains recorded in `plans/PLAN_COMPLETION_LOG.md`. | Focused/full tests and typecheck passed; skipped/failed checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| SDK read-tool exposure behind capability policy | LANDED 2026-06-14 (`SDK-READ-TOOLS-001`) | Read MCP / descriptor integration has landed; write/edit/bash/network/subagent surfaces remain denied; pre-existing instruction-root split-root evidence debt remains. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Focused/full tests, typecheck, and temp-merged-root harness premerge passed; normal instruction-root integrity remains blocked by pre-existing split source-root posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |
| Read MCP / descriptor integration | LANDED 2026-06-14 (`READ-MCP-DESCRIPTORS-001`) | Tool result and event evidence expansion has landed; write/edit/bash/network/subagent surfaces remain denied; pre-existing instruction-root split-root evidence debt remains. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Focused/full tests, full test suite, typecheck, and temp-merged-root harness premerge passed; normal instruction-root integrity remains blocked by pre-existing split source-root posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |
| Tool result and event evidence expansion | LANDED 2026-06-15 (`TOOL-EVIDENCE-001`) | Write/edit hooks and path containment remains next; artifact spill files/storage contracts remain future scope; pre-existing instruction-root split-root evidence debt remains. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Focused/full tests, typecheck, and temp-merged-root harness premerge passed; normal instruction-root integrity remains blocked by pre-existing split source-root posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |
| Write/edit hooks and path containment | LANDED 2026-06-15 (`WRITE-HOOKS-001`) | Bash, governed subagents, and provider-expansion packet remain next; `MultiEdit`, mutating Chirality MCP tools, artifact spill files/full diff storage, and normal instruction-root split-root repair remain future scope. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Focused/full tests, typecheck, and temp-merged-root harness premerge passed; normal instruction-root integrity remains blocked by pre-existing split source-root posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |
| Post-write runtime capability ruling | RULED 2026-06-15 (`D-APP-04`) | Option A approved: bounded R4 Bash prerequisites and controlled Bash implementation may proceed next. Governed SDK subagents and concrete provider expansion remain deferred. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Ruling: `execution/_Coordination/_DECISIONS/D-APP-04_RULING_2026-06-15.md`; register state: `RULED`. |
| R4 Bash prerequisites and controlled Bash implementation | LANDED 2026-06-15 (`BASH-R4-001`) | Bash now lands only in `workspaceWrite`; governed SDK subagents, concrete provider expansion, remote MCP/plugins, Pi work, broader network scope, `MultiEdit`, mutating Chirality MCP tools, full read/write artifact storage, packaging proof, and split-root integrity repair remain future/human-gated. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Focused/full tests, typecheck, temp-merged-root harness premerge, and short network proof passed; normal instruction-root integrity remains blocked by pre-existing split source-root posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |

## Dependency Spine

Select the earliest unblocked item in this table unless regression repair is needed for already-landed runtime work or the human explicitly approves a different tranche.

| # | Tranche | Scope | Acceptance / validation |
|---|---|---|---|
| 1 | **Capability policy / permission overlay skeleton** | LANDED 2026-06-13; residual: SDK read-tool exposure remains next, and pre-existing instruction-root integrity evidence debt is recorded in `plans/PLAN_COMPLETION_LOG.md`. | Validation pointer: focused/full tests and typecheck passed; harness premerge skipped because no local API was reachable; instruction-root integrity attempted but blocked by pre-existing split source-root/stale package-resource posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |
| 2 | **SDK read-tool exposure behind capability policy** | LANDED 2026-06-14 (`SDK-READ-TOOLS-001`); residual: Read MCP / descriptor integration has landed, and normal instruction-root/harness validation still depends on split-root repair. | Validation pointer: focused/full tests and typecheck passed; harness premerge passed with a temporary merged instruction root; normal instruction-root integrity remains blocked by pre-existing split source-root/package-resource posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |
| 3 | **Read MCP / descriptor integration** | LANDED 2026-06-14 (`READ-MCP-DESCRIPTORS-001`); residual: Tool result and event evidence expansion has landed, and normal instruction-root/harness validation still depends on split-root repair. | Validation pointer: focused/full tests, full test suite, typecheck, and harness premerge with temporary merged instruction root passed; normal instruction-root integrity remains blocked by pre-existing split source-root/package-resource posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |
| 4 | **Tool result and event evidence expansion** | LANDED 2026-06-15 (`TOOL-EVIDENCE-001`); residual: write/edit hooks and path containment remains next; artifact spill files/storage contracts remain future scope; normal instruction-root/harness validation still depends on split-root repair. | Validation pointer: focused/full tests, full test suite, typecheck, and harness premerge with temporary merged instruction root passed; normal instruction-root integrity remains blocked by pre-existing split source-root/package-resource posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |
| 5 | **Write/edit hooks and path containment** | LANDED 2026-06-15 (`WRITE-HOOKS-001`); residual: Bash, governed subagents, and provider-expansion packet remain next; `MultiEdit`, mutating Chirality MCP tools, artifact spill files/full diff storage, and normal instruction-root split-root repair remain future scope. | Validation pointer: focused/full tests, typecheck, and harness premerge with temporary merged instruction root passed; normal instruction-root integrity remains blocked by pre-existing split source-root/package-resource posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |
| 6 | **R4 Bash prerequisites and controlled Bash implementation** | LANDED 2026-06-15 (`BASH-R4-001`); residual: Bash remains limited to `workspaceWrite` with conservative static command policy, hook enforcement, timeout injection, stdout/stderr metadata, redacted overflow artifacts, and no network/background/sandbox override. Governed SDK subagents, concrete provider expansion, provider/network broadening, Pi work, remote MCP/plugins, release-readiness claims, professional-boundary changes, `MultiEdit`, mutating Chirality MCP tools, packaging proof, and normal split-root integrity repair remain future/human-gated. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Validation pointer: focused descriptor/permission/options/hook/mapper tests, full test suite, typecheck, temp-merged-root harness premerge, and short network proof passed; normal instruction-root integrity remains blocked by pre-existing split source-root/package-resource posture. Detail: `plans/PLAN_COMPLETION_LOG.md`. |

## Governance Support Lane

This lane records human-requested control-plane support work that improves validation, release-quality, and workflow governance without reordering the runtime dependency spine above.

| ID | Tranche | Status | Residual handoff | Validation pointer |
|---|---|---|---|---|
| GOV-QUALITY-001 | **Quality and validation skeleton** | LANDED 2026-06-13 | Build/release skeleton landed in `GOV-BUILD-001`. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| GOV-BUILD-001 | **Build/release skeleton** | LANDED 2026-06-13 | Workflow and docs index cleanup remains next if the governance migration lane continues. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| GOV-WORKFLOW-001 | **Workflow and docs index cleanup** | LANDED 2026-06-13 | State-file retirement landed in `GOV-STATE-001`. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| GOV-STATE-001 | **Retire next-instance state file** | LANDED 2026-06-13 | Governance-support lane has no current next item; return to runtime spine unless the human selects another governance tranche. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| SCA-APP-001-CLOSURE-001 | **Scope-change pointer, propagation, and supersession repair** | LANDED 2026-06-13 | Package-local context refresh remains if SCA closure continues. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static governance and supersession-map checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |
| SCA-APP-001-CLOSURE-002 | **Package-local context and local-kit refresh** | LANDED 2026-06-13 | Fresh `AUDIT_SCOPE_CLOSURE` rerun remains required to accept SCC-003/SCC-004 closure; otherwise return to the runtime spine. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Static package-local refresh checks recorded in `plans/PLAN_COMPLETION_LOG.md`. |

## Human-Gated Decisions

Decision authority lives in `execution/_Coordination/_DECISIONS/_REGISTER.md`. This table is a planning mirror only.

| ID | Decision | Blocks | State | Packet | Ruling |
|---|---|---|---|---|---|
| D-APP-01 | Pi posture: adapter/fork/import/spike scope versus pattern corpus only | Any Pi adapter, fork, package import, sidecar, or spike work | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-01_RULING_2026-06-13.md` |
| D-APP-02 | Pi package import/runtime strategy | Any direct Pi package dependency or Node 22 sidecar/runtime-floor change for Pi | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-02_RULING_2026-06-13.md` |
| D-APP-03 | Provider-adapter generality beyond the current shipped Anthropic path | Any concrete non-Anthropic shipped backend adapter or provider routing | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-03_RULING_2026-06-13.md` |
| D-APP-04 | Post-write runtime capability lane: Bash, governed SDK subagents, or concrete provider expansion preparation | Bash exposure, governed SDK subagent execution, and concrete non-Anthropic provider implementation/routing after `WRITE-HOOKS-001` | RULED | `execution/_Coordination/_DECISIONS/D-APP-04_PACKET_2026-06-15.md` | `execution/_Coordination/_DECISIONS/D-APP-04_RULING_2026-06-15.md` |

## Guardrails

- Do not treat `docs/PLAN.md` as the active queue; it remains the strategic roadmap.
- Do not expose write/edit/bash/network/subagent capabilities or concrete new providers before their prerequisites and human gates.
- Do not implement Pi adapter, fork, import, sidecar, runtime-floor migration, or spike work under this plan; Pi is a pattern corpus/reference only after D-APP-01 and D-APP-02.
- Treat provider-adapter generality as approved strategy after D-APP-03, but keep concrete new provider implementation behind future bounded tranches.
- Do not make package, dependency, runtime-language, or desktop-wrapper migrations in this control-plane plan.
- Do not turn runtime events, SDK transcripts, completion logs, handoff prose, or coordination state files into project-truth substitutes.
- Do not recreate `execution/_Coordination/NEXT_INSTANCE_STATE.md`; discover current state from authoritative surfaces, dependency/SCC evidence, source/tests, validation artifacts, and git history.
- Do not advance release-readiness, lifecycle, professional, certification, sealing, authentication, or code-compliance claims.
