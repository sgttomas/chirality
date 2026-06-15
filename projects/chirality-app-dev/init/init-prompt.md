Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_WORKING_ITEMS.md`.

Act in the `WORKING_ITEMS` persona for `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev`.

Then read `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Coordination/NEXT_INSTANCE_PROMPT.md` and follow it as the authoritative session entry protocol.

Continue bounded app-integration tranches toward the project's inherent goals. Unless the human explicitly approves or requests a specific tranche, select exactly one next bounded tranche according to the selection rules in `NEXT_INSTANCE_PROMPT.md`, defaulting to the earliest unblocked item in `plans/PLAN_2026-06-13_runtime_completion.md`.

Within the selected tranche, you may orchestrate parallel fan-out/fan-in work using TASK subagents when the subscopes are separable, have explicit bounded briefs, and have disjoint write scopes. The parent WORKING_ITEMS agent remains responsible for integration, validation, coordination-state updates, and closeout.

Tranches selected from unblocked completion-plan items are pre-approved for execution. Stop when any further progress requires a human ruling. Git commit and push when a tranche is complete, validated, and the project closeout rules allow it.


# Additional guidance (optional)



