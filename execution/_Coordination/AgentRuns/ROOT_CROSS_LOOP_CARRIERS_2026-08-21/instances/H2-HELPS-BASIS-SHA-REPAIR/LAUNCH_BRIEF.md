# H2 HELPS_HUMANS Launch Brief — PR #602 basis-SHA repair

- **RunID:** `ROOT_CROSS_LOOP_CARRIERS_2026-08-21`
- **Parent:** `HELP_HUMAN`
- **Role:** `HELPS_HUMANS` (Agent 1)
- **Objective:** Replace the one nonexistent run-basis SHA with the true
  existing basis in exactly four owner-named committed files.

## Exact replacement

- Incorrect/nonexistent:
  `e3e18d277a4b902e2a3347235239e90e946b91f4`
- Correct/existing:
  `e3e18d27740018efd12e73193c02395a9eca93c2`

## Allowed write targets

- `docs/governance_harness/tranche_manifests/ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821.yaml`
- `execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/ORCHESTRATION_PLAN.md`
- `execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/instances/H1-HELPS-TMROOT125/LAUNCH_BRIEF.md`
- `execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/instances/T1-TASKMGMT-CARRIERS/LAUNCH_BRIEF.md`
- this H2 instance's `RETURN.md` and `STATUS.json`

## Checks

- Prove the incorrect full SHA has zero remaining occurrences in the four
  named targets and the correct full SHA has the expected four occurrences.
- Prove the correct object exists and the incorrect object does not.
- Run the G4 manifest validator, instruction entrypoint validator, live agent
  validator, and `git diff --check`.
- Report exact before/after hashes for the four repaired files.

## Fences

- Mechanical replacement only; do not reinterpret or amend any other text.
- No commit, push, PR action, rebase, force push, branch deletion, label, or
  merge.
- Do not touch registers, receipts, notices, handoff state, or DEL-02-06.
