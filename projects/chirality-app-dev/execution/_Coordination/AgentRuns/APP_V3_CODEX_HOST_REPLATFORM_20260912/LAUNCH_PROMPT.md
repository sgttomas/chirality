# Launch prompt for the implementing session (ready to paste)

You are the implementing agent for the Chirality App's Codex host
re-platform: D-GOV-43 as ruled, topology A2 as recorded in its supplement.
Our purpose is to make directing and validating demanding knowledge work
feel natural, and to make what people learn through that work reusable. The
experience to deliver is plan → execute → save → reuse → iterate: a person
begins with an uncertain intention, develops an approach with an agent,
carries it out, inspects and corrects the results, and preserves a useful
workflow for another assignment. Judge the implementation by whether that
whole experience works.

Basis: `main` at or after `230be0ca9` (the merge of PR #768, which contains
PR #767's merge `d2878462b`). Verify with the command in HANDOFF.md
section 0 before anything else.

Read in this order, and no more than this to start: Root `AGENTS.md`;
`PERSPECTIVE.md` (the owner's note and the reviewer's statement of intent)
and `HANDOFF.md` in
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/`;
the ruling and the A2 supplement in `docs/governance_harness/_DECISIONS/`;
the purpose test by family in the proposal packet's `IMPACT.md`; sections
1, 3, 8 and 9 of `TOPOLOGY_COMPARISON.md`; the R17 findings named in the
handoff; and the PR #767 comment thread, which records a reproduced
interruption-versus-retirement defect (the logging-only green rerun was not
a repair). Everything else is history to open when a decision needs it.

The work in one line: keep the useful Runtime services, replace the
restrictive Codex integration with stock Codex, run the Runtime as a service
the App owns and manages, simplify governance by purpose, and prove the loop
on the production path. The measure of done is ruling item 12's eight
checks plus the disconnect-during-tool-work check in HANDOFF.md section 4,
then independent source review and one consolidated trial candidate.

Order: the application tranche first (section 2), then the spike (sections
3 and 4). Get the loop working end to end before refining presentation;
minimal presentation must still expose what the user needs to direct the
work. Codex is the only engine. Settled, and not to be reopened by accident:
the service composition, kept independent of Electron and Next, and the
rule that execution, observation, interruption and shutdown are distinct
(section 3). Account for the PR #767 defect in that composition and its
regression checks.

Boundaries are in sections 5 and 6: a separate independent source reviewer
before the one consolidated signed build; escalate only material scope or
behaviour changes, substantial product additions, or departures from the
established visual direction; routine choices are yours, recorded in a
`RUN_LOG.md` beside the handoff. Keep historical evidence intact and current
status clear. Never enter credentials; the owner performs OAuth and native
verification. Preserve the R17 installation and all trial evidence. No
publishing. No admission, certification or binding rebuilt under new names.

Open items you inherit: the interruption-versus-retirement defect; the
publication SHA still to be written into the register rows; PEC
compatibility unverified and not a prerequisite; Piping integration and
local models deferred.

The next milestone is a reliable App the owner can use for real work. The
system-prompt discussion and explicit publishing approval follow that trial.
