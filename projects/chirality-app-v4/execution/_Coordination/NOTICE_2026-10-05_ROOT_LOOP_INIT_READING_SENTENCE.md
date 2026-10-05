# Notice: one sentence of App v4's LOOP_INIT changed (Root tranche ROOT-LOOPINIT-AUM-ALIGNMENT-20261005, 2026-10-05)

**To:** the App v4 development loops. **From:** HELP_HUMAN (Claude Code session), by the owner's direction recorded in `execution/_Coordination/AgentRuns/ROOT-LOOPINIT-AUM-ALIGNMENT-20261005/OWNER_DECISIONS.md`. That path is relative to the repository root.

**What changed.** In `projects/chirality-app-v4/loop/LOOP_INIT.md`, the last sentence of "When to read further" now reads:

> If you are unsure whether a section matters, read it.

It used to read "If you are unsure whether something matters, ask the human." The old sentence conflicted with Root `AGENTS.md`: "uncertainty alone does not require an extra prompt". The new one keeps the reading decision with the agent, as the owner's guidance on LOOP_INIT intends. Nothing else in App v4's LOOP_INIT changed. Piping's LOOP_INIT took the same binding form, with this sentence, in PR #1092. The Agent User Manual is updated in the same tranche as this notice.

**What it affects in App v4.** Three product resources record the previous LOOP_INIT's sha256, `45c23cf477e23aff1d0152189caf7e8ebfb53eca42e3a1fae87a06af8c197f28`:
- `app/src-tauri/resources/instructions/SOURCE_MAP.json` (entry `loop`);
- `app/src-tauri/resources/policy_standing/basis.json`;
- `app/src-tauri/resources/policy_standing/a16/basis.json`.

No test or source compares these hashes with the live file, so nothing fails. The recorded basis is now one revision behind.

**For the receiving loop to decide.** Whether, when and how to re-pin. For example, `a16/basis.json` may be a fixed historical basis that should stay as it is. This notice changes no App v4 resource, and running sessions keep the instructions they loaded until their next entry.
