# TASK: read-only UI findings and parallel test path

Basis: main 6ac4055690e20ddffd6aa5fff58a8e7ddd3c072f; product source 26657ff90.
Role Type 2, gpt-6-astra medium, fresh context. Parent HELP_HUMAN.
Read Root/App AGENTS and agents/AGENT_TASK.md. Do not delegate.

Map these owner observations from source only, without claiming reproduced:
1. Plan Mode Refresh cycles repeatedly. 2. Skills Inspect does nothing.
3. Conversational workflow creation writes a package but the sidebar does not
refresh, while the plan-to-workflow action does. 4. Running banner above the
composer is remote from activity; assistant updates concatenate awkwardly.
Locate concrete likely paths, evidence vs uncertainty, and smallest useful
diagnostic or repair scope. Also inspect existing production browser/UI test
capabilities and whether distinct chats can have concurrent turns through the
same App-owned service. Recommend how one UI driver can start several actual
App turns and observe them without credential reads or bypassing UI paths.
Do not run tests, launch App, modify source, read live auth/session/event stores,
signal processes, build, use security, or mutate Git. No private-state access.
Return file/line anchors, hypotheses, and feasible bounded test architecture.
