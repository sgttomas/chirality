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
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Read `{REPO_ROOT}/<LOOP_DIR>/LOOP_INIT.md` and follow it: pursue the loop's
inherent goals — recorded in its standing plan — as far as live authority
permits.

Steer (this run): <none>
</init-prompt>

`<LOOP_DIR>` for the app-dev ↔ piping tier-0 bridge loop: `_DomainEngines/bridge`.
The launcher is deliberately generic: the loop's goal, protocol, and specifics
live in `<LOOP_DIR>`'s `LOOP_INIT.md` → standing plan → receipts, which change
at their own pace; a stale pasted copy of this launcher can only mispoint,
never override protocol. Replace the `Steer` placeholder with any per-run
direction (or leave `<none>`); the steer overrides the loop's default posture
but never the owner gate.
