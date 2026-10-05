# Owner decisions: App v4's reading sentence, consistency edits, and the Agent User Manual (2026-10-05)

Run `ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`. HELP_HUMAN (Claude Code session, ROOT for piping T3) transcribed the owner's words exactly from the chat session.

## Context

In PR #1092, run `projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING-LOOP-INIT-20261005/`, piping's LOOP_INIT took App v4's binding form, with one deliberate change. HELP_HUMAN reported it as follows:

> One deliberate change from App v4's wording: "if you are unsure whether something matters, ask the human" became "…whether a section matters, read it". The original contradicts Root AGENTS.md ("uncertainty alone does not require an extra prompt").

## The direction (owner, exact, 2026-10-05)

> Please also make the corresponding change to the App v4's wording:  "One deliberate change from App v4's wording: "if you are unsure whether something matters, ask the human" became "…whether a section matters, read it". The original contradicts Root AGENTS.md ("uncertainty alone does not require an extra prompt")."  And any other minimal consistency edits along the lines of what you did here.  Plus any corresponding updates to the Agent User Manual to make it consistent with these changes.  You can do this in a new PR distinct from your work here.

**Effect.** Authorized, in a PR separate from #1092:
- the same sentence change in `projects/chirality-app-v4/loop/LOOP_INIT.md`;
- other minimal consistency edits of the kind made in #1092;
- updates to the Agent User Manual that make it consistent with piping's binding-form LOOP_INIT and with App v4's changed sentence.
