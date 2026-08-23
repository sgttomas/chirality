# Sealed Fresh Review Brief — N3 TM-ROOT-107 / TM-ROOT-126

InstanceID: `N3_TM107_TM126_REVIEW_CYCLE_1`
Parent: `TASK_MANAGEMENT / N3_TM107_TM126`
Agent type: bounded ephemeral generalist (Agent 2; non-delegating)
Basis: `b143444bd497eae1b1b638670a33e6df756d9084`

## Objective

Independently review the completed N3 owner-ruled dispositions and mechanical
archive. Return `PASS — ZERO ACTIONABLE FINDINGS` only if every sealed check
passes; otherwise return exact actionable findings without changing N3 output.

## Required reads

- `AGENTS.md`
- `agents/AGENT_TASK.md`
- `agents/AGENT_TASK_MANAGEMENT.md`
- `plans/steers/chirality_app_v3_phase0b_steer_root_2026-08-22.md`, N3
- `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`, R1-D
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0B_2026-08-22/instances/N3_TM107_TM126/LAUNCH_BRIEF.md`
- the N3 manager `RETURN.md`, child return/status, ruling record, live/archive
  registers, Root handoff, SCA-004 Brief, and D-GOV-35 decision record

## Checks

1. Reproduce the mandatory federation survey and both Root register validators.
2. Compare the basis live+archive row corpus with the candidate corpus keyed by
   `ActionItemID`; exactly `TM-ROOT-107` and `TM-ROOT-126` may differ.
3. Verify the exact R1-D dispositions, evidence refs/SHAs/quotes, `ScaRef`,
   dates, Notes provenance, and mechanical archival order.
4. Verify `TM-ROOT-035/042/108/106/122` are byte-identical at row level.
5. Reconcile 19 live (`OPEN=11`, `DEFERRED=8`) and 108 archived to the Root
   handoff count update.
6. Verify R1-D is quoted verbatim with R1 SHA in the new ruling record.
7. Check exact N3 content containment, candidate whitespace, `git diff --check`,
   evidence hashes, and no prohibited authority effects.

## Permissions and return

- You MUST NOT delegate or create another orchestration layer.
- You MUST NOT modify any N3 content output, register, evidence, handoff,
  source, or another instance.
- Write only `REVIEW.md` and `STATUS.json` in this review folder.
- Set terminal status to `COMPLETE` with verdict `PASS` or `FAIL`.
