# Init prompt for the next session (ephemeral, 2026-10-09)

The owner pastes the block below as the first message of the new session, started in the T3 integration worktree `WT/numerics` (see [the handoff](HANDOFF_2026-10-09_TO_NEXT_ROOT.md)). It is `projects/chirality-piping/init/dev-loop-init-prompt.md` with the steer filled in.

```
<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to
`{REPO_ROOT}/projects/chirality-piping`.

Read `{REPO_ROOT}/AGENTS.md`.
Read `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.

Act as `HELP_HUMAN` for `{WORKING_ROOT}`.

Read `{WORKING_ROOT}/loop/LOOP_INIT.md` and follow it within the owner's
steering and live authority.

Steer (this run): Continue as ROOT (Agent 0) for T3, and as coordinator of T4, in `HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION`, under the owner's standing delegation. Production code comes first; keep records short.

- Work in the T3 integration checkout: `chirality-t3/numerics`, in the folder beside the main checkout, on branch `codex/piping-numerical-integrity-20260926` (NUM). The handoff and T3's records exist only there. If `{REPO_ROOT}` is not that checkout, tell the owner before doing anything else.
- Orient from `{WORKING_ROOT}/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/HANDOFF_2026-10-09_TO_NEXT_ROOT.md`, which points to the rest. Read further only as the work needs.
- The previous session's agents are gone. Commission fresh T3 and T4 WORKING_ITEMS from their briefs; each resumes from its log's "Resume here". You coordinate and rule, and they implement.
- Not obvious:
  - A manager that ends its turn while its agents run loses their reports to you; the host forces its report-back on turn end. Tested 2026-10-09: managers must dispatch with blocking calls (`run_in_background: false`), several in one message for parallelism, so reports reach them. **This is the most important rule for keeping Agent 0/1/2 intact.** Each manager's brief carries it in its "Dispatching agents" section, and a blocking call returns only a pointer, because the report arrives as a separate message. A manager reports to you once, after its agents are in. Returns also travel by record (`RETURN.md`). If one still reaches you, send its manager a one-line pointer.
  - Give managers standing assignments, and do not resume them for single steps.
  - Agents here cannot run `gh pr merge`, because the permission classifier blocks it. When a PR is ready, ask the owner to merge it.
  - In the full-SHA dispatch, `target_base` must be the PR's integrated base, not current main.
  - DEC-025 holds the exclusive host lock for about two hours, which stalls every other heavy job, T4's included.
  - Compare path sets without rename detection.
  - Never commit `IMPLEMENTATION/U3_MERGE/dec025/surfaces.txt`: it contains a machine path.
</init-prompt>
```
