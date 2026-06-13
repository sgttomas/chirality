# NEXT INSTANCE PROMPT - Chirality App Dev

## Entry Protocol

1. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_WORKING_ITEMS.md`.
2. Act in the `WORKING_ITEMS` persona for `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev`.
3. Read `execution/_Coordination/_COORDINATION.md`.
4. Read `execution/_Coordination/NEXT_INSTANCE_STATE.md`.
5. Read the relevant authority and plan files named by `_COORDINATION.md`.
6. Record `git status --short` before coordination-sensitive planning or edits.

## Active Direction

Continue bounded app-integration tranches toward the Chirality App's inherent goals:

- a local desktop harness for governed agents;
- a Chirality-owned runtime contract and audit/event model;
- Claude Agent SDK as the current privileged adapter path;
- Pi retained as a reference and possible later constrained backend-adapter spike.

## Selection Rules

If a human has already approved or requested a tranche, continue it within its write bounds.

Otherwise, select exactly one next bounded tranche from the unblocked items in:

1. `docs/PLAN.md` R0/R1 runtime objectives;
2. `plans/chirality-app-future-development-plan.md`;
3. `plans/claude-agent-sdk-implementation-followups.md`;
4. `plans/pi-agent-harness-assessment.md` only where it refines the runtime-adapter path.

Default priority:

1. Fix failing validation or incomplete evidence for already-landed runtime work.
2. Generalize provider-neutral contracts and metadata before adding new adapters.
3. Extract runtime lifecycle from route-owned code into product-owned services.
4. Expand session/event replay before tool expansion.
5. Define permission/tool descriptors before enabling read/write/bash tools.
6. Prepare Pi adapter work only after contract hardening and conformance tests exist.

## Execution Rules

- Tranches selected from unblocked completion-plan items are pre-approved for execution.
- Spawn `TASK` agents only for separable subscopes with explicit briefs and disjoint write scopes.
- Keep writes scoped to the selected tranche.
- Use `/Users/ryan/ai-env/projects/pi` and `plans/pi-agent-harness-assessment.md` as reference sources for runtime design.
- Stop when any further progress requires a human ruling.

## Closeout

At completion of a validated tranche:

1. Run appropriate verification.
2. Update `execution/_Coordination/NEXT_INSTANCE_STATE.md` if the queue or blockers changed.
3. Report skipped checks explicitly.
4. Git commit and push when validation and git state allow closeout.

End the session summary with:

- completed tranche;
- validation performed;
- files changed;
- human rulings pending from `_DECISIONS/_REGISTER.md`;
- next unblocked tranche.
