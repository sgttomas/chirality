# NEXT INSTANCE PROMPT - Chirality App Dev

## Entry Protocol

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
2. Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.
3. Read `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`.
4. Read `{WORKING_ROOT}/AGENTS.md`.
5. Act in the `WORKING_ITEMS` persona for `{WORKING_ROOT}`.
6. Read `{WORKING_ROOT}/execution/_Coordination/_COORDINATION.md`.
7. Read `{WORKING_ROOT}/execution/_Coordination/_LATEST.md` for discovery pointers only.
8. Read `{WORKING_ROOT}/plans/PLAN_2026-06-19_loop_first_pivot.md` as the active queue, and `{WORKING_ROOT}/plans/DESIGN_2026-06-18_agent_orchestration_ui.md` as the active design; read `PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`, `PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, and `PLAN_2026-06-16_runtime_stabilization.md` as completed history/evidence context.
9. Read `{WORKING_ROOT}/execution/_Coordination/_DECISIONS/_REGISTER.md`.
10. Discover current state from the authoritative surfaces named by `_COORDINATION.md`: governed docs, decomposition and deliverable artifacts, dependency/SCC snapshots, decision records, source, tests, validation evidence, and git history.
11. Read `{WORKING_ROOT}/execution/_Reconciliation/DepClosure/_LATEST.md` and the latest dependency closure report when dependency or SCC posture can affect blocker claims or selected-tranche scope.
12. Read the relevant authority and implementation-reference files named by `_COORDINATION.md`.
13. For validation, release-quality, build, packaging, network, or governance-control-plane work, read `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md`.
14. For workflow or docs-index work, read `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json`.
15. Record `git status --short` before coordination-sensitive planning or edits.

## Active Direction

The active development arc is the Agent-Orchestration UI & Information Architecture redesign — `plans/DESIGN_2026-06-18_agent_orchestration_ui.md` — which reorganizes the app around harness abilities (the live event-stream loop) instead of the filesystem. Phases 1-5 are COMPLETE and the D-APP-28 full loop-first pivot is COMPLETE: (1) keystone `harness:event` bridge; (2) shell refactor to a collapsible multi-view sidebar; (3) permission pause + live operator-mode switcher, plus (3.1) hardening; (4) read-only document content API + viewer, plus the D-APP-25 manager-lifecycle + Anthropic-parity bridge tranche; (5) typed agent roster + route-free persona resolution + direct-chat `/chat` surface + session list + hydrate-on-open; (6) loop-first pivot with live loop primary app-wide, right sidebar app-wide, and Portal/Workbench/Pipeline as sidebar-reachable tertiary forms. Typecheck is clean, 499 vitest tests pass, `next build` is green, and `desktop:pack` is green after 28d.

The active development queue `plans/PLAN_2026-06-19_loop_first_pivot.md` has no remaining unstarted tranche. Its tranche spine 28a -> 28b -> 28c -> 28d -> 28e has LANDED. 28a extracted a reusable sidebar-right loop primitive; 28b flipped AppShell to sidebar-right + geometry guard tests; 28c made portal `/` a loop-first home + in-place Type-0/Type-1 matrix launch; 28d demoted `/workbench` and `/pipeline` into sidebar-reachable tertiary forms; 28e recorded closeout in DESIGN, the decision register, prompts, and completion history. This was a routing/layout change only: the public UIEvent contract and the permission plane were untouched, in-flight turns survive every relayout, and nothing was deleted.

D-APP-20 through D-APP-32 are ALL RULED (`execution/_Coordination/_DECISIONS/_REGISTER.md`). Key rulings: D-APP-28 -> Option B (full loop-first pivot); D-APP-30 -> B (guard-mid-turn in-place launch); D-APP-31 -> B (in-place `/pipeline` tertiary form, staged with 28d); D-APP-32 -> A (new sidebar tabs). Chat history stays on the RIGHT as the existing Sessions tab — no left rail (owner directive 2026-06-19). The Phase rulings D-APP-20..25 are ruled AND implemented.

D-APP-18 (default-provider cutover) remains separately AWAITING_RULING: `agentSdk` stays the opt-in probe (the default provider is `stub`); do not change provider defaults or declare SDK default before D-APP-18 is ruled. D-APP-18 is now a SEPARATE open decision, NOT the active development gate — it only blocks default-provider cutover, not the loop-first pivot.

Completed closed history (retain as evidence, do not revive as a queue): the live packaged `agentSdk` read-tool proof (`plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`, where D-APP-17 passed with `sonnet`) and its `plans/artifacts/*` evidence; the R6 Extensibility & MCP Boundary Maturity program (`plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, R6-04 deferred); the Runtime Stabilization program (`plans/PLAN_2026-06-16_runtime_stabilization.md`, STAB-00..06); `plans/PLAN_2026-06-16_six_node_scc_resolution.md`; and `plans/PLAN_2026-06-13_runtime_completion.md`.

Current stabilized runtime posture:

- a local desktop harness for governed agents;
- a Chirality-owned runtime contract and audit/event model;
- provider-adapter-general runtime architecture;
- Claude Agent SDK / Anthropic as the first concrete adapter, currently shipped as the **opt-in `agentSdk` probe** (D-APP-12 Option B holds default-provider cutover);
- Pi retained as a pattern corpus / reference only, not an adapter, fork, package import, sidecar, or spike target.

## Selection Rules

The loop-first pivot plan (`plans/PLAN_2026-06-19_loop_first_pivot.md`) has no remaining unstarted tranche. Do not invent a replacement queue; select new work only from explicit human direction or a newly accepted plan/ruling. Do not select from the completed live packaged proof plan, the completed R6 program, the completed Runtime Stabilization spine, the closed SCC-resolution plan, or the retired runtime completion plan.

Default priority:

1. Repair failing validation for already-landed runtime/control-plane/UI work first if such a regression is found.
2. Treat the loop-first pivot tranche spine (28a -> 28b -> 28c -> 28d -> 28e) as complete; repair regressions if found, but do not select more pivot work unless directed.
3. Treat D-APP-18 as a SEPARATE still-open decision that only blocks default-provider cutover; it does not gate the pivot. Do not change provider defaults or governance wording declaring SDK default before D-APP-18 is ruled.
4. Keep the public UIEvent contract and the permission plane untouched during the pivot; in-flight turns must survive every relayout, and nothing is deleted.
5. If any work requires remote MCP, plugins, broad tool search, domain tools, default-provider cutover, provider/network expansion beyond the bounded Anthropic proof path, release posture changes, or a new runtime roadmap, stop and require a fresh human ruling.
6. Do not revive a completed/closed/retired plan or invent a replacement queue.

## Execution Rules

- The loop-first pivot (`plans/PLAN_2026-06-19_loop_first_pivot.md`) has no remaining unstarted tranche. The completed live-proof, R6, Runtime Stabilization, and loop-first pivot plans no longer grant pre-approval for new work. D-APP-12 Option B holds default-provider cutover (`agentSdk` remains opt-in); `D-APP-13`..`D-APP-17` and D-APP-20..D-APP-32 are ruled. D-APP-18 is awaiting ruling; do not implement default-provider cutover unless that ruling explicitly approves it.
- Do not read, update, or recreate `NEXT_INSTANCE_STATE.md`; current state is discovered from the dependency and authority surfaces named above.
- Spawn `TASK` agents only for separable subscopes with explicit briefs and disjoint write scopes.
- At validated closeout, autonomously hand off to a `CHANGE` agent/subagent for Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline. This closeout handoff is required and is not a substitute implementation tranche.
- Keep writes scoped to the selected tranche.
- For browser-verified tranches, stop the local Next dev server before running `npm run build`, `npm run desktop:pack`, or `npm run harness:validate:premerge` unless the command explicitly owns the server lifecycle; see `plans/PLAN_2026-06-19_validation_server_build_isolation.md`.
- Use `{REPO_ROOT}/../pi` and `plans/pi-agent-harness-assessment.md` only as read-only pattern-corpus references where they refine the active plan item.
- Do not perform provider-network, concrete non-Anthropic provider, Pi migrations, default-provider cutover, or new runtime roadmap work unless the active plan item and human rulings explicitly allow them. D-APP-18 blocks any default-provider cutover implementation.
- D-APP-01 and D-APP-02 rule out Pi adapter, fork, import, Node 22 sidecar, runtime-floor migration, and immediate spike work. D-APP-03 approves provider-adapter generality only; concrete new providers require bounded future implementation tranches.
- Stop when any further progress requires a human ruling.

## Closeout

At completion of a validated tranche:

1. Run appropriate verification.
2. Route checks through `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` for build, packaging, or release-significant work.
3. Update the active plan and `plans/PLAN_COMPLETION_LOG.md` only when a selected tranche lands; completed plans are edited only for closeout corrections or explicit human-directed governance work.
4. Update `execution/_Coordination/_DECISIONS/_REGISTER.md` only when decision-packet state changes.
5. Update `execution/_Coordination/_LATEST.md` only when discovery pointers change.
6. Report skipped checks explicitly.
7. Hand off to a `CHANGE` agent/subagent for final Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline.

End the session summary with:

- completed tranche;
- validation performed;
- files changed;
- human rulings pending or blocking from `_DECISIONS/_REGISTER.md`;
- next selected tranche, or state that the active loop-first pivot queue (`plans/PLAN_2026-06-19_loop_first_pivot.md`) has no remaining unstarted tranche and that D-APP-18 remains separately open for default-provider cutover.
