# G2 CHANGE Launch Brief — PR #602 repair and ruling closeout

- **RunID:** `ROOT_CROSS_LOOP_CARRIERS_2026-08-21`
- **Parent:** `HELP_HUMAN`
- **Role:** `CHANGE` (Agent 1)
- **Branch:** `codex/root-cross-loop-carriers-20260821`
- **Existing PR:** `#602`, base `main`

## Objective

Create two ordinary commits in dependency order on the existing branch, push
normally, update the existing PR description for the repair/rulings, and
return it for owner review. No new PR, rebase, force push, label, branch
deletion, or merge.

## Commit 1 — basis repair

Message: `fix(governance): repair PR 602 run basis`

Stage only:

- the four exact owner-named basis-repair targets;
- `OWNER_DIRECTION_TRANSCRIPT_PR602_REPAIR_AND_RULINGS_2026-08-21.md`;
- `instances/H2-HELPS-BASIS-SHA-REPAIR/`;
- this `LAUNCH_BRIEF.md`.

Before commit, confirm each repaired target has one mechanical line
replacement, the bad SHA has zero occurrences in those targets and does not
resolve, and the corrected SHA has four occurrences and resolves as a commit.

## Commit 2 — owner rulings and governed closeout

Message: `chore(governance): apply root carrier rulings`

Stage all remaining scoped continuation paths:

- Root and run `HANDOFF_STATE.md`;
- run `VALIDATION.md`;
- `DEL02_PREPARATION_AUTHORIZATION_HANDOFF.md`;
- `WORK_GRAPH_AMENDMENT_PR602_REPAIR_AND_RULINGS_2026-08-21.json`;
- `instances/T2-TASKMGMT-TMROOT117-RULING/`;
- this G2 instance's `RETURN.md` and `STATUS.json`;
- Root `LOOP_RECEIPTS.md`;
- Root live/archive registers and
  `_TaskManagement/CLOSEOUT_2026-08-21_TM-ROOT-117.md`;
- App reciprocal notice
  `NOTICE_2026-08-21_ROOT_TM117_TRIGGER_RESCOPE_AND_DEL0206_PREPARATION_AUTHORIZATION.md`.

Before this commit, set G2 status to `COMPLETE` in the work-graph amendment
and write the G2 return/status. Self-referential final commit/PR identifiers
may be returned out of band.

## Post-commit checks

- `python3 -m pytest tools/validation -q`;
- Root G0–G4;
- instruction entrypoints and live agent validation;
- Root live/archive validators at 21/104;
- candidate-range G4 from common ancestor
  `e3e18d27740018efd12e73193c02395a9eca93c2` to final `HEAD`, using
  `--added-manifests-only`;
- `git diff --check`;
- three-way merge simulation against current `origin/main` without changing
  branch history.

## Push and PR

Push the existing branch normally. Update PR #602's body to state:

- the four basis citations are repaired to the existing commit;
- TM-ROOT-117 is closed `RESOLVED_BY_DECISION` and the exact App trigger
  re-scope is routed with no successor identity accepted;
- epoch `1` / `root-runtime-1` and one separate preparation-only activation
  are owner-authorized, but no preparation output is attached to PR #602;
- exact future bytes return to a separate owner acceptance gate;
- validation results and residual gates;
- review and merge remain owner acts.

Do not add any label. Do not merge.

## Stop conditions

Stop and return the exact blocker on any failed required check, unexpected
dirty path, rejected non-fast-forward push, merge conflict, or scope drift.
Do not repair by rebase, force push, or history rewrite.
