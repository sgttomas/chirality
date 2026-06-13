Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_WORKING_ITEMS.md`.

Act in the `WORKING_ITEMS` persona for `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev`.

Then read `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Coordination/NEXT_INSTANCE_PROMPT.md` and follow it as the authoritative session entry protocol.

This init prompt is a bootstrap convenience only. If it disagrees with `NEXT_INSTANCE_PROMPT.md` or `execution/_Coordination/_COORDINATION.md`, follow those files and surface the discrepancy.

Default to one bounded tranche. If no human-selected tranche is active, select the earliest unblocked item from `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/plans/PLAN_2026-06-13_runtime_completion.md`. Current governance-support lane is complete; return to the runtime spine unless the human explicitly selects another governance tranche.

TASK fan-out is allowed only for separable subscopes with explicit briefs and disjoint write scopes. The parent WORKING_ITEMS agent remains responsible for integration, validation, coordination-state updates, git closeout, and final summary.

Stop when further progress requires a human ruling. Commit and push completed validated work when validation and git state allow.
