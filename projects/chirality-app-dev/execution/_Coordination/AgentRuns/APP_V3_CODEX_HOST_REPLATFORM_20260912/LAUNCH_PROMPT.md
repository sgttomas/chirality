# Launch prompt for the implementing session (ready to paste)

Continue the Chirality v3 Codex-only MVP as the implementing agent for the
Codex host re-platform (D-GOV-43, topology A2). Work in a checkout of
`main` at or after `d2878462be59a43b4afc175a8cce85abca9cf696` (the merge
of PR #767). Read Root `AGENTS.md`, then
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PERSPECTIVE.md`
and `HANDOFF.md` in the same directory, then the records the handoff names:
`docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`, its
supplement `D-GOV-43_supplement_topology_A2.md`, and the proposal packet.
Verify the preconditions in the handoff's section 0 before any work.

Priority: retire the obsolete constraints (the application tranche), then
prove the production-path plan → execute → save → reuse → iterate
experience against the eight functional checks. Documentation supports that
work; it does not delay it. Codex is the only engine. Use a separate
independent source reviewer for your code before one consolidated signed
build. Bring back material scope or behaviour changes and consequential
findings; routine implementation choices are yours. Never enter credentials;
the owner performs OAuth and native verification. Preserve the R17
installation and all trial evidence. No publishing.
