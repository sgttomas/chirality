# NEXT INSTANCE PROMPT - Chirality App Dev

## Entry Protocol

1. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_WORKING_ITEMS.md`.
2. Act in the `WORKING_ITEMS` persona for `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev`.
3. Read `execution/_Coordination/_COORDINATION.md`.
4. Read `execution/_Coordination/_LATEST.md` for discovery pointers only.
5. Read `plans/PLAN_2026-06-13_runtime_completion.md`.
6. Read `execution/_Coordination/_DECISIONS/_REGISTER.md`.
7. Discover current state from the authoritative surfaces named by `_COORDINATION.md`: governed docs, decomposition and deliverable artifacts, dependency/SCC snapshots, decision records, source, tests, validation evidence, and git history.
8. Read `execution/_Reconciliation/DepClosure/_LATEST.md` and the latest dependency closure report when dependency or SCC posture can affect blocker claims or selected-tranche scope.
9. Read the relevant authority and implementation-reference files named by `_COORDINATION.md`.
10. For validation, release-quality, build, packaging, network, or governance-control-plane work, read `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md`.
11. For workflow or docs-index work, read `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json`.
12. Record `git status --short` before coordination-sensitive planning or edits.

## Active Direction

Continue bounded app-integration tranches toward the Chirality App's inherent goals:

- a local desktop harness for governed agents;
- a Chirality-owned runtime contract and audit/event model;
- Claude Agent SDK as the current privileged adapter path;
- Pi retained as a reference and possible later constrained backend-adapter spike.

## Selection Rules

If a human has already approved or requested a tranche, continue it within its write bounds.

Otherwise, select exactly one next bounded tranche from the earliest unblocked item in `plans/PLAN_2026-06-13_runtime_completion.md`.

Default priority:

1. Fix failing validation or incomplete evidence for already-landed runtime work.
2. Select the earliest unblocked item on the active runtime completion plan's dependency spine.
3. If that item is blocked by a human decision, prepare a decision packet if none exists.
4. If a packet already awaits ruling, take the next unblocked implementation item.
5. Stop when no current plan item remains unblocked; do not substitute unrelated hardening or out-of-stage scope.

## Execution Rules

- Tranches selected from unblocked completion-plan items are pre-approved for execution.
- Do not read, update, or recreate `NEXT_INSTANCE_STATE.md`; current state is discovered from the dependency and authority surfaces named above.
- Spawn `TASK` agents only for separable subscopes with explicit briefs and disjoint write scopes.
- Keep writes scoped to the selected tranche.
- Use `/Users/ryan/ai-env/projects/pi` and `plans/pi-agent-harness-assessment.md` as reference sources for runtime design only where they refine the active plan item.
- Do not perform coding-language, application-wrapper, package-runtime, provider-network, write/edit/bash/tool-execution, or Pi-adapter migrations unless the active plan item and human rulings explicitly allow them.
- Stop when any further progress requires a human ruling.

## Closeout

At completion of a validated tranche:

1. Run appropriate verification.
2. Route checks through `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` for build, packaging, or release-significant work.
3. Update `plans/PLAN_2026-06-13_runtime_completion.md` and `plans/PLAN_COMPLETION_LOG.md` when a plan item lands.
4. Update `execution/_Coordination/_DECISIONS/_REGISTER.md` only when decision-packet state changes.
5. Update `execution/_Coordination/_LATEST.md` only when discovery pointers change.
6. Report skipped checks explicitly.
7. Git commit and push when validation and git state allow closeout.

End the session summary with:

- completed tranche;
- validation performed;
- files changed;
- human rulings pending from `_DECISIONS/_REGISTER.md`;
- next unblocked plan item.
