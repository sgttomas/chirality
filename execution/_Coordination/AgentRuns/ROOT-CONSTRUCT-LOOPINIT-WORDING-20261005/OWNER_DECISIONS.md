# Owner decisions: construct-local-work-graph's LOOP_INIT wording (2026-10-05)

Run `ROOT-CONSTRUCT-LOOPINIT-WORDING-20261005`. HELP_HUMAN (Claude Code session, ROOT for piping T3) transcribed the owner's words exactly from the chat session.

## Context

HELP_HUMAN reported that `construct-local-work-graph`'s introduction says LOOP_INIT "supplies the evergreen procedure". That is no longer true for loops whose LOOP_INIT is in the binding form: App v4 (2026-10-04), and piping, in PR #1092. HELP_HUMAN also reported that revising a registered workflow needs `create-workflow`'s review, so it was left out of the consistency edits. App v4's LOOP_INIT mapping had proposed the same revision as A4 (`projects/chirality-app-v4/execution/_Coordination/AgentRuns/APP-V4-GRAPH-CLOSURE-20261004/LOOP_INIT_MAPPING.md`, "Additions needed elsewhere").

## The direction (owner, exact, 2026-10-05)

> also attend to the required changes to the `construct-local-work-graph` workflow and I will review and approve accordingly.

**Effect.** HELP_HUMAN prepares the revision under `create-workflow`. It is a Root bundled-library edit, so the candidate is a pull-request diff with a G4 tranche manifest and notices to the consuming loops. The owner reviews and approves the exact diff. **The PR is not merged before that approval.**

## The revision (A4, unchanged in substance)

1. **The introduction:** "`LOOP_INIT.md` supplies the evergreen procedure…" becomes "`LOOP_INIT.md` supplies, or points to, the evergreen procedure…". This is true both for loops whose LOOP_INIT still carries the procedure (App, PEC) and for binding-form loops (App v4, Piping).
2. **§3:** "(currently App, Piping and PEC)" becomes "(currently App, App v4, Piping and PEC)". App v4's LOOP_INIT adopts the method's graph, closeout, receipt and MEMORY conventions.

**Not changed:**
- the rest of the workflow;
- its template `resources/work-graph-template.md`, whose two LOOP_INIT statements stay true;
- its description, so `workflows/index.json` is unchanged.

The prior revision is preserved in Git history, which is the Root bundled library's revision mechanism.
