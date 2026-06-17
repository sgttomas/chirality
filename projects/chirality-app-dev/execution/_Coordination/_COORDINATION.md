# Coordination Record - Chirality App Dev

**Recorded:** 2026-06-13
**Active persona:** `WORKING_ITEMS`
**Default work mode:** bounded app-integration tranches
**Current strategic focus:** Chirality-owned provider-adapter runtime. Claude Agent SDK / Anthropic is the first concrete adapter and opt-in `agentSdk` probe path. D-APP-12 Option B holds the default-provider cutover. Pi is a pattern corpus / reference only, not an adapter, fork, package import, sidecar, or spike target.
**Current active queue:** none selected. The R6 Extensibility & MCP Boundary Maturity program `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` is completed closed history after R6-05; R6-04 was explicitly deferred as optional organization work. The Runtime Stabilization program `plans/PLAN_2026-06-16_runtime_stabilization.md` (STAB-00..STAB-06) and the six-node SCC plan are also completed closed history.

## Active Surface

Use this coordination surface as the active entrypoint for app-integration work. Keep it lean: project truth remains in governed docs, decomposition and deliverable artifacts, source, tests, evidence records, and git history.

Path anchors for executable prompts:

- Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
- Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.

Primary authority and guidance:

- `{REPO_ROOT}/AGENTS.md`
- `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`
- `{WORKING_ROOT}/AGENTS.md` - project-local agent posture and closeout discipline
- `docs/PRD.md` - product requirements and current runtime scope
- `docs/PLAN.md` - strategic roadmap, not the active queue
- `docs/DIRECTIVE.md`
- `docs/CONTRACT.md`
- `docs/SPEC.md`
- `docs/TYPES.md`
- `docs/VALIDATION_STRATEGY.md`
- `docs/RELEASE_QUALITY_GATES.md`
- `docs/BUILD_AND_RELEASE.md`
- `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`
- `docs/README.md`
- `docs/MANIFEST.json`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `execution/_ScopeChange/_LATEST.md`
- `frontend/docs/harness/runtime_engine_contract.md`
- `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` - completed R6 Extensibility & MCP Boundary Maturity program (R6-01..R6-05; R6-04 deferred), accepted by D-APP-14 and closed by R6-05
- `plans/PLAN_2026-06-16_runtime_stabilization.md` - completed Runtime Stabilization program (STAB-00..STAB-06), accepted by D-APP-11 and closed by STAB-06
- `plans/PLAN_2026-06-16_six_node_scc_resolution.md` - completed non-governing SCC-resolution tranche-selection plan (closed history)
- `plans/PLAN_2026-06-13_runtime_completion.md` - retired runtime completion history
- `plans/PLAN_COMPLETION_LOG.md` - landed-tranche narrative history
- `plans/chirality-app-future-development-plan.md` - seed runtime roadmap/reference
- `plans/claude-agent-sdk-implementation-followups.md` - first-adapter implementation reference
- `plans/pi-agent-harness-assessment.md` - Pi pattern-corpus reference
- `plans/pi-assessment/*.md` - Pi pattern-corpus reference assessments
- `execution/_Coordination/_LATEST.md`
- `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
- `execution/_Coordination/_DECISIONS/_REGISTER.md`
- `execution/_Reconciliation/DepClosure/_LATEST.md`
- `execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/Dependency_Closure_Report.md`
- `execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/Closure_Acceptance_Audit.md`

## Authority And State Rules

Do not maintain a separate next-instance state file. Current state must be discovered from authoritative artifacts, dependency evidence, current implementation surfaces, selected plans, decision records, validation evidence, and git history. Do not let handoff prose, completion plans, dependency snapshots, or runtime logs become substitute authority.

Authoritative state:

1. `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/TYPES.md` define requirements, invariants, mechanics, and vocabulary.
2. `docs/PLAN.md` records strategic runtime direction and roadmap rationale. It is not the ordinary active work queue.
3. `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` route evidence, release-quality checks, and local build/package evidence. They do not create release readiness, lifecycle issuance, publication authorization, or professional acceptance.
4. `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json` are workflow/index surfaces. They help discovery and orientation, but they do not replace canonical agent instructions, coordination policy, project truth, or human rulings.
5. `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` records the package/deliverable decomposition and source-governed scope basis.
6. Accepted SCOPE_CHANGE snapshots under `execution/_ScopeChange/**` record governed decomposition/guidance amendments. `SCA-APP-001` approves provider-adapter generality, Pi pattern-corpus-only posture, and capability-forward permission governance with explicit hard-deny precedence.
7. Deliverable-local `_STATUS.md`, `MEMORY.md`, `_run_records/**`, four-document kits, dependency files, and review/evidence files carry lifecycle, working memory, and execution evidence inside their ownership boundary.
8. Current dependency and SCC evidence lives in immutable reconciliation snapshots under `execution/_Reconciliation/DepClosure/**`, with `execution/_Reconciliation/DepClosure/_LATEST.md` as a discovery pointer. The accepted latest snapshot `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z` reports strict `scc_count = 0`; the residual six-node SCC no longer blocks project-wide strict dependency-closure claims. This is dependency-closure evidence only and does not create product, runtime, release, lifecycle, professional, certification, sealing, authentication, or code-compliance approval. Future SCC work follows the shared cycle-driven resolution doctrine (the shared repo-root `docs/CYCLE_DRIVEN_RESOLUTION.md`): each strongly-connected component is resolved by a recorded move — decompose / invert / merge / cut (cut/merge human-gated) — and cycle-participating edges stay non-gating until resolved.
9. Current implementation truth lives in source, tests, build scripts, validation artifacts, and git history.

Guidance and history surfaces:

0a. `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` is completed closed history after R6-05. It matured the local/in-process tool extension boundary (catalog, naming, collision prevention, contributor docs) and exposed no new capability; remote MCP, plugins, broad tool search, and domain tools remain out of scope (§7). R6-04 was deferred as optional organization work.
0b. `plans/PLAN_2026-06-16_runtime_stabilization.md` is completed closed history (tranches STAB-00..STAB-06), accepted by `D-APP-11` and closed by STAB-06. It records the current runtime stabilization evidence, D-APP-12 Option B hold ruling, and D-APP-13 mutating MCP ruling, but it is no longer an active tranche-selection queue.
1. `plans/PLAN_2026-06-16_six_node_scc_resolution.md` is the completed non-governing SCC-resolution plan. It records closure of the residual six-node strict dependency SCC; it is closed history and is no longer the active queue.
2. `plans/PLAN_2026-06-13_runtime_completion.md` is retired as the active queue and retained only as historical completion evidence for landed runtime work.
3. `plans/PLAN_COMPLETION_LOG.md` preserves landed-tranche narrative after plan rows are compressed.
4. `execution/_Coordination/_DECISIONS/_REGISTER.md` tracks human-gated decision-packet status. Agents prepare `PROPOSAL` packets; humans rule.
5. `execution/_Coordination/_LATEST.md` is a discovery pointer for coordination surfaces only. It is not authority and must not accumulate state history.
6. There is no active `NEXT_INSTANCE_STATE.md`; do not recreate it or use any hand-maintained coordination file as the app state.

When guidance surfaces disagree with authoritative surfaces, surface the discrepancy and correct the guidance surface. Do not silently rewrite authority.

## Baseline Intake

At the start of a new loop:

1. Read `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`.
2. Read `{WORKING_ROOT}/AGENTS.md`.
3. Act in the `WORKING_ITEMS` persona for `{WORKING_ROOT}`.
4. Read this file and `NEXT_INSTANCE_PROMPT.md`.
5. Read `execution/_Coordination/_LATEST.md` for discovery pointers only.
6. Read `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` as completed R6 history; read `plans/PLAN_2026-06-16_runtime_stabilization.md` as completed stabilization history and evidence context.
7. Read `_DECISIONS/_REGISTER.md` for ruled and pending human decisions. `D-APP-14` accepted the now-completed R6 program; `D-APP-12` is ruled Option B and blocks default-provider cutover until later proof/ruling; `D-APP-13` is ruled.
8. Read `execution/_Reconciliation/DepClosure/_LATEST.md` and the latest dependency closure report when dependency/SCC state can affect tranche selection or blocker claims.
9. Read `execution/_ScopeChange/_LATEST.md` when provider, Pi, permission posture, decomposition amendment, or deliverable-local context alignment can affect the selected tranche.
10. Read `docs/PRD.md`, `docs/PLAN.md`, and `frontend/docs/harness/runtime_engine_contract.md` enough to confirm the selected tranche's runtime target.
11. Read selected deliverable-local `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`, `MEMORY.md`, `_run_records/**`, and review/evidence files only when the plan item or dependency evidence points to those surfaces.
12. Read `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` when selecting validation for governance, runtime, SDK/tool, network, packaging, build, or release-significant work.
13. Read `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md` and `docs/README.md` when changing the coordination loop or docs index.
14. Read the implementation reference surfaces needed for the selected tranche.
15. Run `git status --short` before coordination-sensitive planning or edits.

## Active Development Loop

Use bounded app-integration tranches. No active development queue is currently selected. If a human has already approved or requested a new tranche, continue it within its write bounds. Otherwise stop and report that the next active plan must be selected by the human. Do not select from the completed R6 program, completed Runtime Stabilization spine, closed SCC-resolution plan, or retired runtime completion plan.

A tranche is acceptable when it has:

- one clear objective tied to the human-selected active plan;
- a narrow write scope;
- a validation command or concrete manual verification target;
- all required human rulings recorded in `_DECISIONS/_REGISTER.md`;
- work contained within accepted professional-boundary, network, dependency, runtime, and release policy.

Default ordering:

1. Repair failing validation or incomplete evidence for already-landed runtime/control-plane work first if such a regression is found.
2. Stop when no active queue is selected; report that R6 is complete and the next active plan must be selected by the human.
3. If any work requires remote MCP, plugins, broad tool search, domain tools, default-provider cutover, live packaged provider evidence, provider/network expansion, release posture changes, or a new runtime roadmap, stop and require a fresh human ruling.
4. Do not revive a completed/closed/retired plan or invent a replacement queue.

If dependency evidence is needed, use the latest DepClosure snapshot and selected deliverable-local dependency files to discover blockers. Do not infer project-wide blocked/unblocked state from a stale summary or from a hand-maintained coordination state file.

## Subagent Use

Spawn `TASK` agents only for separable implementation subscopes with explicit briefs and disjoint write scopes. Use fan-out/fan-in when the work naturally separates by subsystem, for example:

- runtime contract and event schema;
- SDK options and message mapping;
- session storage and replay;
- permission overlay and tool descriptor design;
- documentation / evidence update.

Every subagent brief must state:

- source files to read;
- files it may write;
- validation expected;
- whether it may modify production code or only produce assessment/docs.

Keep parallel write scopes disjoint.

This TASK restriction does not apply to final Git closeout. After a validated tranche, `WORKING_ITEMS` must autonomously hand off to a `CHANGE` agent/subagent for final Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline.

## Git And Validation Closeout

At the end of a validated tranche:

1. Run the tranche-specific verification.
2. Run broader checks when the tranche touches shared runtime behavior:
   - from `frontend/`: `npm run test`;
   - from `frontend/`: `npm run typecheck`;
   - from `frontend/`: `npm run harness:validate:premerge`;
   - from `frontend/`: `npm run instruction-root:integrity`.
3. For governance/control-plane-only tranches, run static governance checks and explicitly record that frontend tests were skipped because no runtime/source files changed.
4. Route build, packaging, and release-significant changes through `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md`.
5. Completed plans are edited only for closeout corrections or explicit human-directed governance work. There is no active R6 plan after R6-05 closeout.
6. Move landed narrative detail to `plans/PLAN_COMPLETION_LOG.md` when closing a tranche.
7. Update `_DECISIONS/_REGISTER.md` only when a decision packet or ruling state changes.
8. Update `execution/_Coordination/_LATEST.md` only when coordination or planning discovery surfaces change.
9. Do not update or recreate `NEXT_INSTANCE_STATE.md`.
10. Record any skipped checks and why.
11. Autonomously hand off to a `CHANGE` agent/subagent for final Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline.

Git closeout is source-control hygiene. Lifecycle issuance, release readiness, professional approval, certification, sealing, authentication, and code-compliance acceptance remain human-governed states.

## Human-Ruling Stops

Stop and surface a human-ruling request when further progress requires a change to:

- product runtime policy in `docs/PRD.md` or strategic roadmap policy in `docs/PLAN.md`;
- outbound network policy or shipped provider scope;
- package/runtime requirements for Pi-backed execution, which remains unapproved after D-APP-01 and D-APP-02;
- concrete non-Anthropic provider implementation, provider-network expansion, or provider routing beyond the current shipped Anthropic path;
- write/edit/bash/tool-execution exposure beyond the current approved plan item;
- the project-truth model for sessions, transcripts, chats, runtime logs, or completion logs;
- professional-boundary claims or release-readiness posture.

Record human-gated questions in `_DECISIONS/_REGISTER.md`.
