# NEXT INSTANCE PROMPT - Chirality App Dev

## Entry Protocol

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
2. Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.
3. Read `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`.
4. Read `{WORKING_ROOT}/AGENTS.md`.
5. Act in the `WORKING_ITEMS` persona for `{WORKING_ROOT}`.
6. Read `{WORKING_ROOT}/execution/_Coordination/_COORDINATION.md`.
7. Read `{WORKING_ROOT}/execution/_Coordination/_LATEST.md` for discovery pointers only.
8. Read `{WORKING_ROOT}/plans/PLAN_2026-06-16_runtime_stabilization.md` (the active governing development queue).
9. Read `{WORKING_ROOT}/execution/_Coordination/_DECISIONS/_REGISTER.md`.
10. Discover current state from the authoritative surfaces named by `_COORDINATION.md`: governed docs, decomposition and deliverable artifacts, dependency/SCC snapshots, decision records, source, tests, validation evidence, and git history.
11. Read `{WORKING_ROOT}/execution/_Reconciliation/DepClosure/_LATEST.md` and the latest dependency closure report when dependency or SCC posture can affect blocker claims or selected-tranche scope.
12. Read the relevant authority and implementation-reference files named by `_COORDINATION.md`.
13. For validation, release-quality, build, packaging, network, or governance-control-plane work, read `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md`.
14. For workflow or docs-index work, read `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json`.
15. Record `git status --short` before coordination-sensitive planning or edits.

## Active Direction

Continue bounded app-integration tranches toward the Chirality App's inherent goals. The active development queue is the **Runtime Stabilization program** (`plans/PLAN_2026-06-16_runtime_stabilization.md`, tranches STAB-00..STAB-06), accepted by `execution/_Coordination/_DECISIONS/D-APP-11_RULING_2026-06-16.md`. The residual six-node strict dependency SCC was previously closed by accepted snapshot `execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/`. The program stabilizes the landed runtime before any further expansion:

- a local desktop harness for governed agents;
- a Chirality-owned runtime contract and audit/event model;
- provider-adapter-general runtime architecture;
- Claude Agent SDK / Anthropic as the first concrete adapter, currently shipped as the **opt-in `agentSdk` probe** (default provider unchanged pending `D-APP-12`);
- Pi retained as a pattern corpus / reference only, not an adapter, fork, package import, sidecar, or spike target.

## Selection Rules

If a human has already approved or requested a tranche, continue it within its write bounds.

Otherwise, select the earliest unblocked tranche from the Runtime Stabilization spine in `plans/PLAN_2026-06-16_runtime_stabilization.md` (§6 spine, §10 sequencing DAG).

Default priority:

1. Fix failing validation or incomplete evidence for already-landed runtime/control-plane work.
2. Select the earliest unblocked tranche on the stabilization spine, honoring the sequencing DAG (STAB-00 first; STAB-00 gates STAB-01 and STAB-06; STAB-04 depends on STAB-01 + an SDK-behavior probe; STAB-02 cutover ruling follows its readiness steps).
3. For governance tranches (STAB-00, STAB-06), produce the required reconciliation/disposition artifacts within their write bounds.
4. If the next tranche requires a pending human ruling (`D-APP-12` default-provider cutover), prepare a decision packet if none exists.
5. If a packet already awaits ruling, stop; do not substitute unrelated runtime hardening or out-of-stage scope.
6. Stop when no stabilization tranche remains unblocked; do not select from the retired runtime completion plan or invent a replacement active queue.

## Execution Rules

- Tranches selected from unblocked stabilization-plan items are pre-approved for execution within their declared write scope. STAB-02 step (d) packaging and the `D-APP-12` ruling remain human-gated. `D-APP-13` is ruled. If the stabilization plan has no remaining unblocked tranche, stop and report that the program is complete and the next active plan is unselected.
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
3. Update `plans/PLAN_2026-06-16_runtime_stabilization.md` (compress the landed tranche row per its §8 rule) and `plans/PLAN_COMPLETION_LOG.md` when a tranche lands.
4. Update `execution/_Coordination/_DECISIONS/_REGISTER.md` only when decision-packet state changes.
5. Update `execution/_Coordination/_LATEST.md` only when discovery pointers change.
6. Report skipped checks explicitly.
7. Hand off to a `CHANGE` agent/subagent for final Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline.

End the session summary with:

- completed tranche;
- validation performed;
- files changed;
- human rulings pending from `_DECISIONS/_REGISTER.md` (`D-APP-12`);
- next stabilization tranche, or state that no stabilization tranche remains unblocked.
