# H2 launch brief — Receipt 90 M6 handoff count repair

Parent: `HELP_HUMAN`
Role/node: `HELPS_HUMANS` / `N2`
RunID: `ROOT_TM112_DECISION_PREP_2026-08-03`

## Objective

Recompute current Root live/archive register counts directly, then replace
only the stale count paragraph in `execution/_Coordination/HANDOFF_STATE.md`
§1 as required by Receipt 90 M6.

## Permissions and acceptance

Read the two Root register CSVs and Receipt 90. Write only the Root handoff
file and this RunID. Preserve all other handoff semantics/history. Do not edit
register rows, workplan, receipts, source/tests, foreign loops, lifecycle, or
Git. Return exact before/after text and deterministic checks. No Agent 2.
