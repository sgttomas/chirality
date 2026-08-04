# Orchestration plan amendment v2 — release N2 only

RunID: `ROOT_TM112_DECISION_PREP_2026-08-03`
Selection authority: `HUMAN`
Parent fan-in: N1 accepted `COMPLETE/PASS` by HELP_HUMAN

## Amendment

Release serial node N2 only. Repair
`execution/_Coordination/HANDOFF_STATE.md` §1 exactly under Receipt 90 M6 by
recomputing both Root Task Management register files and replacing the stale
count sentence with the current generation end state. Preserve every other
byte of semantic text and history.

N3 and all TM-ROOT-112 semantic-contract, implementation, test, Task
Management, lifecycle, foreign-loop, receipt, workplan, and Git work remain
held. N2 is executed directly by HELPS_HUMANS; no Agent 2 is dispatched.

## N2 acceptance

- counts are computed directly from `REGISTER.csv` and
  `REGISTER_CLOSED.csv`;
- live status vocabulary is exactly OPEN/DEFERRED and archive status exactly
  CLOSED;
- the only tracked diff is `execution/_Coordination/HANDOFF_STATE.md`;
- all other writes remain under this RunID;
- the exact before/after sentence and checks are returned to HELP_HUMAN.
