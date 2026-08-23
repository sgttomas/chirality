# Sealed Agent-2 Brief — Federation and Two-Row Disposition Analysis

InstanceID: `A2_FEDERATION_ROW_ANALYSIS`
Parent: `TASK_MANAGEMENT / N3_TM107_TM126`
Agent type: bounded ephemeral generalist (Agent 2; non-delegating)
Basis: `b143444bd497eae1b1b638670a33e6df756d9084`

## Objective

Perform the mandatory read-only Task Management federation preflight for the
Root invocation and independently analyze the owner-ruled dispositions of
`TM-ROOT-107` and `TM-ROOT-126`. Determine whether the two closed rows must be
mechanically relocated with `tools/taskmgmt/taskmgmt.py archive`; propose exact
field values and reconciled live/archive counts. Do not apply any disposition.

## Required reads

- `AGENTS.md`
- `agents/AGENT_TASK.md` (Agent-2 base contract)
- `agents/AGENT_TASK_MANAGEMENT.md`
- `plans/chirality-task-management/PRD_CANDIDATE_2026-07-31.md`
- `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`
- `execution/_Coordination/_TaskManagement/REGISTER.csv`
- `execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv`
- `execution/_Coordination/_TaskManagement/RULING_2026-08-21_ROOT_DEL0206_TRIGGER_PROMOTIONS.md`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Brief.md`
- `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md` if present; if concurrently pending, report that fact and the required evidence fields.
- `tools/taskmgmt/taskmgmt.py` help for `federation`, `validate`, and `archive`.

## Tools and permissions

- Read-only shell and Git inspection are allowed.
- You MUST NOT delegate or create another orchestration layer.
- You MUST NOT modify registers, rulings, handoff files, source evidence, or
  any path outside this child folder.
- Your only write targets are `RETURN.md` and `STATUS.json` in this folder.

## Required checks and output

1. Run the deterministic federation helper read-only and report inventory,
   exclusions, validation errors, relationships, and `COMPLETE`/`PARTIAL`.
2. Validate both live and closed Root registers.
3. Extract the exact current rows for `TM-ROOT-107` and `TM-ROOT-126` and the
   untouched comparison rows `TM-ROOT-035/042/108/106/122`.
4. Bind each proposed disposition to its exact evidence path and SHA-256.
5. State the exact fields that should change, whether `Status=CLOSED` is
   required, whether archive is required, and expected live/archive counts.
6. Return `RETURN.md` with a PASS/FAIL verdict and terminal `STATUS.json` with
   `status` equal to `COMPLETE` or `BLOCKED`.
