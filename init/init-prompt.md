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

Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
Set `WORKING_ROOT` to `{REPO_ROOT}`.
Read `{REPO_ROOT}/agents/AGENT_DOMAIN_ENGINE.md`.
Act in the `DOMAIN_ENGINE` persona for `{WORKING_ROOT}`.
Then read `{WORKING_ROOT}/execution/_Coordination/NEXT_INSTANCE_PROMPT-piping.md` for the `chirality-piping` perspective of the bridge, 
and `{WORKING_ROOT}/execution/_Coordination/NEXT_INSTANCE_PROMPT-app-dev.md` for the `chirality-app-dev` perspective of the bridge, and then act in accordance with your goals.