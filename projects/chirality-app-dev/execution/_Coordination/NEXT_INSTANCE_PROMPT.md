# NEXT INSTANCE PROMPT - Chirality App Dev

## Entry Protocol

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
2. Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.
3. Read `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`.
4. Read `{WORKING_ROOT}/AGENTS.md`.
5. Act in the `WORKING_ITEMS` persona for `{WORKING_ROOT}`.
6. Read `{WORKING_ROOT}/execution/_Coordination/_COORDINATION.md`.
7. Read `{WORKING_ROOT}/execution/_Coordination/_LATEST.md` for discovery pointers only.
8. Read `{WORKING_ROOT}/plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` (the active governing development queue); read `PLAN_2026-06-16_runtime_stabilization.md` as completed history/evidence context.
9. Read `{WORKING_ROOT}/execution/_Coordination/_DECISIONS/_REGISTER.md`.
10. Discover current state from the authoritative surfaces named by `_COORDINATION.md`: governed docs, decomposition and deliverable artifacts, dependency/SCC snapshots, decision records, source, tests, validation evidence, and git history.
11. Read `{WORKING_ROOT}/execution/_Reconciliation/DepClosure/_LATEST.md` and the latest dependency closure report when dependency or SCC posture can affect blocker claims or selected-tranche scope.
12. Read the relevant authority and implementation-reference files named by `_COORDINATION.md`.
13. For validation, release-quality, build, packaging, network, or governance-control-plane work, read `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md`.
14. For workflow or docs-index work, read `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json`.
15. Record `git status --short` before coordination-sensitive planning or edits.

## Active Direction

The active development queue is the **R6 Extensibility & MCP Boundary Maturity program** (`plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, tranches R6-01..R6-05), accepted by `execution/_Coordination/_DECISIONS/D-APP-14_RULING_2026-06-17.md`. It matures the local/in-process tool extension boundary (collision-prevention invariant, regenerable tool catalog, contributor docs) on top of the stabilized runtime and exposes no new capability. The Runtime Stabilization program (STAB-00..STAB-06) is completed closed history. Current stabilized runtime posture:

- a local desktop harness for governed agents;
- a Chirality-owned runtime contract and audit/event model;
- provider-adapter-general runtime architecture;
- Claude Agent SDK / Anthropic as the first concrete adapter, currently shipped as the **opt-in `agentSdk` probe** (D-APP-12 Option B holds default-provider cutover);
- Pi retained as a pattern corpus / reference only, not an adapter, fork, package import, sidecar, or spike target.

## Selection Rules

If a human has already approved or requested a tranche, continue it within its write bounds.

Otherwise, select the earliest unblocked tranche from the active R6 program (`plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, §4 spine, §6 sequencing). Do not select from the completed Runtime Stabilization spine, the closed SCC-resolution plan, or the retired runtime completion plan.

Default priority:

1. Repair failing validation for already-landed runtime/control-plane work first if such a regression is found.
2. Select the earliest unblocked R6 tranche (R6-01 collision invariant first; R6-04 optional; R6-05 closeout last).
3. R6 exposes no new capability. If any work requires crossing an R6 §7 fence (remote MCP, plugins, broad tool search, domain tools), default-provider cutover, live packaged provider evidence, provider/network expansion, or release posture changes, stop and require a fresh human ruling.
4. Stop when no R6 tranche remains unblocked; report that the R6 program is complete and the next active plan must be selected by the human.

## Execution Rules

- R6 tranches selected from the active plan are pre-approved for execution within their declared write scope. R6 is mostly documentation + one code tranche (R6-01 collision invariant); it exposes no new tools. The completed Runtime Stabilization plan no longer grants pre-approval for new work. D-APP-12 Option B holds default-provider cutover (`agentSdk` remains opt-in); `D-APP-13` is ruled. If no R6 tranche remains unblocked, stop and report that the next active plan is unselected.
- Do not read, update, or recreate `NEXT_INSTANCE_STATE.md`; current state is discovered from the dependency and authority surfaces named above.
- Spawn `TASK` agents only for separable subscopes with explicit briefs and disjoint write scopes.
- At validated closeout, autonomously hand off to a `CHANGE` agent/subagent for Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline. This closeout handoff is required and is not a substitute implementation tranche.
- Keep writes scoped to the selected tranche.
- Use `{REPO_ROOT}/../pi` and `plans/pi-agent-harness-assessment.md` only as read-only pattern-corpus references where they refine the active plan item.
- Do not perform coding-language, application-wrapper, package-runtime, provider-network, write/edit/bash/tool-execution, concrete non-Anthropic provider, Pi migrations, or new runtime roadmap work unless the active plan item and human rulings explicitly allow them.
- D-APP-01 and D-APP-02 rule out Pi adapter, fork, import, Node 22 sidecar, runtime-floor migration, and immediate spike work. D-APP-03 approves provider-adapter generality only; concrete new providers require bounded future implementation tranches.
- Stop when any further progress requires a human ruling.

## Closeout

At completion of a validated tranche:

1. Run appropriate verification.
2. Route checks through `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` for build, packaging, or release-significant work.
3. Update the active R6 plan `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` (compress the landed tranche row) and `plans/PLAN_COMPLETION_LOG.md` when a tranche lands.
4. Update `execution/_Coordination/_DECISIONS/_REGISTER.md` only when decision-packet state changes.
5. Update `execution/_Coordination/_LATEST.md` only when discovery pointers change.
6. Report skipped checks explicitly.
7. Hand off to a `CHANGE` agent/subagent for final Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline.

End the session summary with:

- completed tranche;
- validation performed;
- files changed;
- human rulings pending or blocking from `_DECISIONS/_REGISTER.md`;
- next R6 tranche, or state that the R6 program is complete and no active queue remains.
