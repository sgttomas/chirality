# Return D1 — Task Management notice triage (TASK, general-purpose/opus, high effort requested)

Result: no register rows added. Triage record written at
`projects/pec/execution/_Coordination/_TaskManagement/NOTICE_TRIAGE_2026-09-23.md`.
Next free ID would be TM-PEC-026 (highest existing TM-PEC-025 across both registers).

Dispositions (each notice states it takes no PEC action; every possible PEC consequence already has a home):
- APP_PIPING_RECEIPTS: feed-model consequence is SCA-005 input (D-PEC-86 I-1); loop adoption is the I-7 owner deferral.
- EVERGREEN_LOOP_INSTRUCTIONS: manifest places PEC's loop outside the change; PEC pins none of the changed Root files; SCA-005 input and I-7.
- SCOPED_PR_CI: `docs/CI_SELECTION.md` still routes PEC source changes to PEC tests; no PEC file pins the old routing; nothing unowned.
Optional DEFERRED row TM-PEC-026 (trigger "SCA-005 closed") described but left unminted as duplicative of I-7.

Method note returned by the TASK: the task-management workflow says a TASK never writes register rows (recording dispositions belongs to the human and WORKING_ITEMS); the brief's additive-row allowance conflicted but was not exercised. HELP_HUMAN accepts this reading; any future row is a manager act on a recorded human decision.

Checks: `taskmgmt validate` PASS on both registers before/after (10 and 15 rows, exit 0), registers byte-identical (`REGISTER.csv` d350d007…799d; `REGISTER_CLOSED.csv` ea730ae0…fd94); `federation` COMPLETE, 27 findings, none involving a PEC row, no writes; `scan` 481 candidates, only the three notices in scope; reliance-hold ALLOW ×2; `git diff --check` clean.
