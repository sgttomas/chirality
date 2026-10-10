# Development session entry

Choose the working root and loop below. Read Root `AGENTS.md`, the selected role
(default `agents/AGENT_HELP_HUMAN.md`) and that loop entry. Supply the current
objective and limits in the session steer. Do not recover a standing backlog
from historical workplans or receipts.

| Scope | Working root | Loop entry, repository-relative |
|---|---|---|
| Root | repository root | `execution/_Coordination/LOOP_INIT.md` |
| App v4 | `projects/chirality-app-v4` | `projects/chirality-app-v4/loop/LOOP_INIT.md` |
| Piping | `projects/chirality-piping` | `projects/chirality-piping/loop/LOOP_INIT.md` |

App v3, Runtime and PEC are frozen references, not development entries.

Project-local `init/dev-loop-init-prompt.md` files are equivalent launchers where
present. These entries grant no new project activation, product acceptance or
release. The bridge's historical standing-plan launcher is not a current
development entry; explicitly scoped domain integration starts from its current
product contracts and owner steering.

<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
Set `WORKING_ROOT` to `{REPO_ROOT}/<working-root>`.
Read `{REPO_ROOT}/AGENTS.md` and `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.
Act as HELP_HUMAN for the selected scope.
Read `{REPO_ROOT}/<loop-entry>` from the table above.
Steer: <current objective, limits and reserved decisions>
</init-prompt>
