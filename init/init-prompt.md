Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to `{REPO_ROOT}/<TARGET_WORKSPACE_REPO_SUBPATH>`; for root-governance work, set `WORKING_ROOT` to `{REPO_ROOT}`.

Read `{REPO_ROOT}/agents/<AGENT_INSTRUCTION_FILE>`.

Act in the `<AGENT_NAME>` persona for `{WORKING_ROOT}`.

Then read `{WORKING_ROOT}/<COORDINATION_PROMPT_SUBPATH>` and follow the instructions.

Stop when any further progress requires a human ruling. When the work is complete, validated, and the project closeout rules allow it, autonomously hand off to a `CHANGE` agent/subagent for final Git/file-state review. `CHANGE` should commit and push the validated tranche as the ordinary terminal action when git state allows closeout; do not require a per-run `APPROVE:` token for scoped closeout commit/push.

There may be other agents working in this monorepo with disjoint write scopes. Before staging, inspect root git status and stage only files in the selected tranche write scope, required evidence/coordination artifacts, and any explicitly created governance-issue plan. Do not stage unrelated dirty files.

Before pushing, verify the outgoing commits are scoped to this tranche or already accepted upstream. If the remote branch has advanced, use only a fast-forward update path; stop and surface the conflict if push would require merge, rebase, force push, or judgment about another agent’s work.

If concrete issues are discovered that would improve the agentic development loop, project governance, agents, or skills, record them in a new timestamped plan under `{WORKING_ROOT}/plans/`. Do not create a plan merely to satisfy this instruction when no actionable issue was found.

If a CHANGE agent/subagent is unavailable, perform the CHANGE closeout checklist inline: scoped status review, validation evidence check, scoped commit, and push when safe.
