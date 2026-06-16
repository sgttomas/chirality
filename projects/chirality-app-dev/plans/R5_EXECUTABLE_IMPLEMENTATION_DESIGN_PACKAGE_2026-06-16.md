# R5 Executable Implementation Design Package

**Status:** DESIGN PACKAGE
**Date:** 2026-06-16
**Prepared by:** WORKING_ITEMS
**Tranche:** `R5-DESIGN-001`
**Authorizing ruling:** `execution/_Coordination/_DECISIONS/D-APP-08_RULING_2026-06-16.md`

This package decomposes executable R5 governed subagent runtime into smaller future
implementation slices and validation gates. It is not executable implementation approval.

No source code, package manifest, dependency, lockfile, desktop wrapper, provider routing,
network policy, Pi runtime path, release-readiness posture, or professional-boundary posture
changes in this package.

## Authority Inputs

- `execution/_Coordination/_DECISIONS/D-APP-05_RULING_2026-06-15.md` approved a
  provider-adapter-neutral contract prerequisite before executable subagents.
- `execution/_Coordination/_DECISIONS/D-APP-06_RULING_2026-06-15.md` held executable R5
  pending the residual SCC ruling package.
- `execution/_Reconciliation/RECON_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1825/SCC_Ruling_Package.md`
  identified the residual six-node strict SCC and its blocker implications.
- `execution/_Coordination/_DECISIONS/D-APP-07_RULING_2026-06-16.md` ruled that the
  residual SCC blocks project-wide strict dependency-closure claims only, not bounded R5
  dispatch selection.
- `execution/_Coordination/_DECISIONS/D-APP-08_RULING_2026-06-16.md` approved Option C:
  prepare this design/evidence package before executable implementation.
- `/Users/ryan/ai-env/projects/chirality/docs/CYCLE_DRIVEN_RESOLUTION.md` and
  `{REPO_ROOT}/docs/CYCLE_DRIVEN_RESOLUTION.md` define objective-relative graph doctrine
  and named SCC-resolution moves.

## Current Runtime Baseline

Existing implementation surfaces already establish the non-executable prerequisite posture:

- `frontend/src/lib/harness/agent-runtime-contract.ts` records
  `AGENT_SUBAGENT_PREREQUISITE_POSTURE` with executable delegation blocked, child
  definitions contract-only, pattern-corpus runtime reference-only, concrete provider
  routing blocked, and child capability inheritance blocked.
- `frontend/src/lib/harness/subagent-governance.ts` evaluates subagent governance through
  fail-closed gates: environment enablement, persona allowlist, metadata presence, sealed
  context, pipeline approval, approval reference, internal error, and allow.
- `frontend/src/lib/harness/turn-engine.ts` runs the governance evaluator and passes only
  delegated subagent names into effective turn options when governance allows them.
- `frontend/src/lib/harness/tool-descriptor.ts` contains descriptor metadata for the SDK
  `Agent` tool, but the descriptor remains human-gated/future-policy and descriptor-only.
- `frontend/docs/harness/runtime_engine_contract.md` records the provider-neutral
  child-run contract and blocked executable delegation posture.

## SCC Doctrine Handling

The residual six-node SCC contains:

- `DEL-03-01`
- `DEL-03-02`
- `DEL-03-03`
- `DEL-03-04`
- `DEL-04-03`
- `DEL-05-02`

Under the cycle-driven resolution doctrine, dependency graphs are objective-relative. The
strict dependency-closure graph and a bounded R5 implementation dispatch graph are not the
same objective. `D-APP-07` therefore permits bounded R5 dispatch selection while preserving
the residual SCC as unresolved for project-wide strict dependency closure.

Rules for future R5 work:

- Do not use cycle-participating dependency rows as blocker, readiness, priority, or
  project-wide closure evidence.
- Do not claim project-wide strict dependency closure until a later SCC-resolution package
  resolves the SCC and a fresh dependency-closure audit accepts the result.
- Keep any dependency-register amendment, cut, merge, decompose, or invert work separate
  from executable R5 implementation unless separately ruled.
- Agent-proposable SCC moves are decompose or invert; human-gated moves are cut or merge.
- If a future R5 slice reveals a real implementation cycle inside the runtime objective,
  stop and record the cycle with a named move rather than silently choosing an order.

This package uses a bounded R5 runtime objective: prove governed SDK subagent execution can
be introduced without broadening provider/network policy, child capability inheritance, Pi
runtime, project-wide closure claims, release claims, or professional-boundary claims.

## Slice Plan

| Slice | Name | Purpose | Executable exposure | Primary touched surfaces | Entry condition |
|---|---|---|---|---|---|
| `R5-SLICE-001` | Child definition inventory and eligibility model | Define how Type 2 instruction files become candidate child definitions, including persona allowlist, sealed context metadata, stable names, and denial reasons. | None unless later ruled. | `agent-runtime-contract.ts`, `subagent-governance.ts`, focused tests, runtime contract docs. | Human approval of the slice or an active plan item explicitly authorizing it. |
| `R5-SLICE-002` | SDK `agents` option-construction bridge | Build and test SDK option shapes for `agents` definitions while keeping them non-model-visible or hard-denied. | Non-executable bridge only. | `sdk-options-builder.ts`, `types.ts`, focused tests. | Slice 001 accepted, or a ruling allowing bridge work without executable exposure. |
| `R5-SLICE-003` | Agent tool preflight and hook gate | Add a fail-closed preflight path for SDK `Agent` requests that checks governance, allowed child, cwd, tool list, and metadata before exposure. | Still denied until a later executable ruling. | `chirality-hooks.ts`, `permission-overlay.ts`, `tool-descriptor.ts`, focused tests. | Slice 002 accepted and human ruling confirms `Agent` remains non-model-visible during this slice. |
| `R5-SLICE-004` | Parent-child lifecycle event mapping | Map child-run records to parent runtime events and session evidence without claiming child output as project truth. | Event scaffolding only unless later ruled. | `agent-runtime-contract.ts`, `event-schema.ts`, `session-events.ts`, `sdk-message-mapper.ts`, tests. | Slice 003 accepted or explicit event-scaffold approval. |
| `R5-SLICE-005` | Bounded child output artifact references | Define storage references, size/redaction posture, and non-authoritative artifact semantics for completed child runs. | Artifact references only; no truth promotion. | session/event storage, artifact helpers if selected, docs/tests. | Slice 004 accepted and artifact scope approved. |
| `R5-SLICE-006` | Executable child turn integration | Expose model-visible SDK `Agent`, pass executable SDK `agents`, run child turns, persist lifecycle events, and attach bounded child output references. | Yes. | SDK manager/options, turn engine, hooks, events, tests. | Separate human ruling approving executable child turns and model-visible `Agent`. |

## Validation Gates

Each future implementation slice should run the union of applicable gates from
`docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and
`docs/BUILD_AND_RELEASE.md`.

| Gate | Applies to | Minimum evidence |
|---|---|---|
| Governance gate | Any decision, plan, runtime contract doc, or coordination update. | `git diff --check`; stale-reference searches; referenced-path existence checks; no-runtime-code-change check when docs-only. |
| Runtime contract gate | Child-run records, adapter metadata, lifecycle status, event schema, or session evidence. | Focused Vitest coverage for touched runtime modules; `npm run typecheck`; `npm run test` when shared event or route behavior changes. |
| Permission/tool gate | SDK `Agent` descriptor, `agents` option construction, permission overlay, hooks, and child tool restrictions. | Deny/allow/unknown-tool tests; explicit tests that `readOnly`, `dontAsk`, and developer-only `bypass` do not grant ungated subagent autonomy; `npm run typecheck`. |
| Harness workflow gate | Browser-facing session, SSE, interrupt, attachment, or turn behavior. | Relevant API/library tests; `npm run harness:validate:premerge` against a reachable local app; review generated summary artifact. |
| Security/network gate | Provider, API key, redaction, or outbound behavior. | Relevant tests plus `npm run proof:network-policy`; expected to be skipped for R5 slices unless a later ruling broadens provider/network behavior. |
| Packaging gate | Instruction-root resources, Electron package metadata, or distribution artifacts. | `npm run instruction-root:integrity`; build/package commands only when package behavior changes. |
| Claims gate | User-facing copy, release labels, or professional-boundary language. | Review that no release-readiness, lifecycle issuance, professional approval, certification, sealing, authentication, code-compliance, or reliance claim is made. |

## Required Denial Tests For Executable R5

Before `R5-SLICE-006` can be accepted, the executable tranche must prove denial for:

- `CHIRALITY_ENABLE_SUBAGENTS` absent or not strictly `true`;
- active persona with no Type 2 allowlist;
- allowlisted candidate whose instruction file is missing;
- candidate instruction that is not Type 2;
- missing, malformed, or unsealed `subagentGovernance` metadata;
- missing `pipelineRunApproved`;
- missing `approvalRef`;
- unknown child agent name;
- requested child cwd outside permitted scope;
- requested child tool list outside the child policy;
- attempted child capability inheritance;
- attempted nested child subagent autonomy;
- attempted provider routing or network broadening;
- evaluator internal error;
- adapter child-run metadata appearing in provider-neutral project truth.

## Follow-On Ruling Requirements

This package does not authorize implementation. At minimum, later human authority must
choose one of these paths before source changes land:

- approve `R5-SLICE-001` only as non-executable eligibility/inventory work;
- approve slices 001 through 003 as a non-executable SDK `agents`/`Agent` bridge with
  hard-denied model visibility;
- approve slices 001 through 005 as full scaffolding without executable child turns;
- approve `R5-SLICE-006` executable child turn integration after earlier slice evidence is
  accepted;
- hold R5 and select another unblocked plan item.

Any approval of executable child turns must explicitly state whether it permits:

- model-visible SDK `Agent`;
- executable SDK `agents` definitions;
- child turn execution;
- child output artifact references;
- child capability inheritance, which should remain denied by default;
- provider routing or network behavior changes, which are not required for R5;
- dependency-register edits or SCC-resolution moves, which are separate from R5 execution.

## Out Of Scope

The following remain denied by this package:

- model-visible SDK `Agent` tool execution;
- executable SDK `agents` definitions;
- child turn execution;
- child output artifacts from executable child runs;
- child capability inheritance or expansion;
- concrete provider implementation;
- provider routing;
- network expansion;
- Pi runtime paths, imports, forks, sidecars, or spikes;
- dependency-register edits;
- project-wide strict dependency-closure claims;
- release-readiness claims;
- lifecycle issuance;
- professional approval;
- certification, sealing, authentication, or code-compliance acceptance;
- professional-boundary claim changes.

## Closeout For This Package

This package is a docs/control-plane tranche. Required validation is:

- `git diff --check -- execution/_Coordination/_DECISIONS plans`;
- targeted `rg` checks for `D-APP-08`, `R5-DESIGN-001`, and cycle-doctrine references;
- referenced-path existence checks for the D-APP-08 packet/ruling, decision register,
  active plan, completion log, SCC ruling package, and cycle-driven resolution doctrine;
- decision-register ID uniqueness check;
- source/package exclusion check proving no runtime source, package manifest, dependency,
  lockfile, desktop wrapper, provider, network, tool-exposure, release, or
  professional-boundary surface changed.

Frontend runtime tests, typecheck, harness premerge, instruction-root integrity, build,
packaging, network proof, and DMG checks are skipped for this package because it changes
only docs/control-plane planning and decision evidence.
