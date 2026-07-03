<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to `{REPO_ROOT}/<TARGET_WORKSPACE_REPO_SUBPATH>`; for root-governance work, set `WORKING_ROOT` to `{REPO_ROOT}`.

Read `{REPO_ROOT}/agents/<AGENT_INSTRUCTION_FILE>`.

Act in the `<AGENT_NAME>` persona for `{WORKING_ROOT}`.

Then read `{WORKING_ROOT}/<COORDINATION_PROMPT_SUBPATH>` and follow the instructions.  
</init-prompt>


<init-prompt>
Your goal is to complete the inherent goals of this project that you will discover as you follow those instructions.

Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to `{REPO_ROOT}`.

Read `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`.

Read `{WORKING_ROOT}/AGENTS.md`.

Act in the `WORKING_ITEMS` persona for `{WORKING_ROOT}`.

Then read `{WORKING_ROOT}/execution/_Coordination/NEXT_INSTANCE_PROMPT.md` and follow the instructions.
</init-prompt>

<init-prompt>
Continuously pursue the inherent goals of the `chirality-app-dev` ↔
`chirality-piping` tier-0 bridge: keep the two project surfaces governably
aligned and move the standing bridge plan forward as far as live authority
permits.

Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`, read
`{REPO_ROOT}/_DomainEngines/bridge/LOOP_INIT.md`, then follow it. Continue
that pursuit until every lawful path of advancement is exhausted except for
human decision. Park gated decisions, stop at owner gates, and continue any
independent lawful work that keeps the development loop moving toward the
bridge's inherent goals.
</init-prompt>
