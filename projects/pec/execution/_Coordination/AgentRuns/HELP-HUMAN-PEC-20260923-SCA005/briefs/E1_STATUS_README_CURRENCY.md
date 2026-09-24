# Brief E1 — docs/STATUS.md and README.md present-current refresh (TASK)

Authority basis: D-PEC-86 §3 I-5 (packet clause for the one-time STATUS/README currency the SCA-004 Handoff_State already lists as `STALE_POINTER_OR_MAP_NOTE` owned by HELP_HUMAN loop maintenance). Role: TASK. No delegation. Runs only after the SCA-005 checkpoint-1 package exists.

Write boundary (only): `projects/pec/docs/STATUS.md` and `projects/pec/README.md`. Prose about present-current basis, gates and pointers only. Do not touch any other file.

What to reflect (verify each against its source before writing; cite in the text as the existing style does): D-PEC-80 loop consolidation (loop home `projects/pec/loop/`, workplans retired, run-based PR boundary); D-PEC-81..84 Remaining concordance, application and scanner repair; D-PEC-85 first store/guard slice with DEL-01-03 `IN_PROGRESS` and DEL-01-05 `IN_PROGRESS` after the D-PEC-84 L reversal; current lifecycle census (32 OPEN / 26 INITIALIZED / 4 CHECKING / 2 IN_PROGRESS — recount from `_STATUS.md` files); Task Management register state after D1 (recount); D-PEC-86 owner direction, SCA-005 opened at Gate 1 with its checkpoint-1 package path and Impact Assessment SHA-256 (from the SCA-005 snapshot folder), owner checkpoints remaining; D-PEC-79 PRD v2.3 postimage still adopted-not-applied; TM-PEC-023 folded into SCA-005 intake; DEL-01-03 inquiry reports produced with obligations awaiting owner disposition (from C1's return in `AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/`); the frozen corpus and fences unchanged; PEC loop method migration deferred (D-PEC-86 I-7). Keep the "Orient yourself" read-order and governance sections, updating only stale sentences. Remove or rewrite the 2026-08 "Superseding owner ruling" paragraphs only by marking them historical where they are no longer the current state; do not delete decision lineage.

Do not assert: any checkpoint acceptance, any lifecycle promotion, any release, any reliance, any adoption of the shared development-loop method by PEC, any PRD version other than v2.2 live.

Checks: `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` after the edit (record exit code and any new PEC finding); `git diff --stat` limited to the two files.

Return: a bullet list of every sentence-level change with its source citation, the two files' SHA-256 after edit, and check results.
