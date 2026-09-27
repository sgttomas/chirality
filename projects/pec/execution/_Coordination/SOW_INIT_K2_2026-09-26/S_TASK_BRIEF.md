# S TASK brief — D-PEC-103 add-on S (`OPEN → INITIALIZED`), generic-shell TASK

- **Dispatcher:** WORKING_ITEMS (Type 1) for the D-PEC-103 act, under HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, node K2. Brief `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K2A_D103_SOW_ACT.md` (SHA-256 `bb0d6e3105cd9a221f9adc1572e446c096bb2af04a472a8df267356c6ba48d6b`), step 6.
- **Role:** TASK (Type 2), `pec-task`, model opus (`claude-opus-5-5`, high). **No workflow is selected** (`D-PEC-63` §3.2 generic-shell pattern; history label `TASK+status-advance`). This runs outside the scope-of-work run, whose `NO_STATUS_TOUCH` covered everything it did.
- **Authority:** ruling `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-103_RULING_2026-09-26.md` (owner: "D-PEC-103: A; S; M; C8; defaults"; question 2 resolution and Grant item 4) and the proposal's "Add-on S" section (`_DECISIONS/D-PEC-103_first_sows_del_08_06_10_13_proposal_2026-09-26.md`, SHA-256 `cfc2e65d5ae91f0d62d4ef993bc22a91d2bb4716969d083ae98f0fc948eb5417`).
- **Repository root (worktree):** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d103-act`, branch `claude/pec-d103-first-sows-act`.

## Conditions (already established by the dispatcher; re-check before writing)

1. The act's independent verifier has passed: `projects/pec/execution/_Coordination/SOW_INIT_K2_2026-09-26/VERIFIER_VERDICT_01.md` — PASS WITH NOTES, 0 blocking.
2. For each deliverable, `python3 tools/scope_of_work/validate_scope_of_work.py <DEL folder>` prints `PASS format=SOW_V1`. Re-run it yourself (with `PYTHONDONTWRITEBYTECODE=1`) immediately before that deliverable's command, and do not run the command if it does not pass.
3. Preimages: DEL-08-06 `_STATUS.md` `73e21846186b3ab46d4d11042ecb2bb00d0c69a0d7b4fa70734c75e65a892511`; DEL-10-13 `_STATUS.md` `c7a5705d7203a26f525317e85fa068d29cfeb49b8686eab1b5cd3e782e22543b`. Both read `**Current State:** OPEN`. Stop and report on any mismatch.
4. `tools/scaffolding/write_status.sh` SHA-256 `0bf835f54f4bb9a78a51d0b56392a8686d1f255f06d3c2bcaf7e8665f77bece3`. Record the hash you observe; stop and report on mismatch.
5. Reliance-hold preflight, from `projects/pec`: `python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <each _STATUS.md, project-relative> --operation dispatch-for-production` must print `ALLOW` (exit 0) for both. Stop on anything else.

## The act (from the repository root, in this order, one run each)

```text
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface" INITIALIZED "TASK+status-advance"
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate" INITIALIZED "TASK+status-advance"
```

Run each exactly once. Do not retry on failure; stop and report.

## Write boundary

Your **only** repository write targets are these two files, and only through the two commands above:
- `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/_STATUS.md`
- `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_STATUS.md`

Do not edit, create, stage, commit or delete anything else in the worktree (the dispatcher commits). No git checkout/switch/commit/stash/reset/fetch/pull/push. Create and delete scratch files only inside your own `mktemp -d` directory under `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/`, and never delete other files there. Use `PYTHONDONTWRITEBYTECODE=1` for Python.

## Postimage check

Compare each postimage with the prepared postimage in the run root (`addons/S/DEL-08-06_STATUS.postimage_D2026-09-26.md` `75366b6b8a0050c520ab583be927da3960d21df0b8cd3011668b2047db89a127`; `addons/S/DEL-10-13_STATUS.postimage_D2026-09-26.md` `3771d5262b8f9044a3dbed81af0032a155ec12e876ec90c1f8253a8e5237e567`). These are tabled for act date `{D}` = 2026-09-26. If `date +%Y-%m-%d` gave another date, the only permitted differences (slot rule) are the date in `**Last Updated:** {D}` and in the appended line `- {D} — State set to INITIALIZED (TASK+status-advance)`; `**Current State:**` must read `INITIALIZED` and every other byte must be unchanged. Show `git diff` of both files and `git status --short`, which must list no other change made by you.

## Limits

No lifecycle change other than this single `OPEN → INITIALIZED` per deliverable. No `CHECKING`, `ISSUED`, acceptance, readiness, release or reliance claim, and no prompt about `CHECKING`.

## Return

Your full report, which the dispatcher saves verbatim as `S_TASK_RETURN.md`: conditions checked (with outputs), the two commands with their exit codes and stdout/stderr, pre- and post-hashes of both files, the observed `write_status.sh` hash, the date used, the postimage comparison, `git diff` and `git status --short`, and your temp dir.
