# Coordination Notice — PEC SCA-005: RETIRED `_STATUS.md` method/tool mismatch

**Status:** NON-BINDING NOTICE
**Receiving loop:** Chirality Root
**Sending loop:** PEC (`projects/pec`), HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`

PEC scope change SCA-005 retires four deliverables non-destructively
(DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05). The owner accepted checkpoint
group 2 on 2026-09-25 with Q-CP2-1 (a)
(`projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/DECISION.md`;
register row `D-PEC-92`). Each retired `_STATUS.md` therefore records
`**Current State:** RETIRED` through a hand-authored exact edit, applied during
checkpoint-3 preparation, with the folder and every file retained.

PEC found four Root surfaces that disagree about RETIRED:

- the bundled `scope-change` method (`workflows/scope-change/resources/method.md`,
  checkpoint group 3 step 2) says a PROJECT/SOFTWARE `REMOVE` updates
  `_STATUS.md`, and the scope-change contract requires `_STATUS.md` RETIRED;
- `tools/scaffolding/write_status.sh` admits only `OPEN INITIALIZED
  SEMANTIC_READY IN_PROGRESS CHECKING ISSUED` (L86) and exits 2 on any other
  state (L99–103), so it cannot perform that step;
- `docs/SPEC.md` §3.2 has no RETIRED lifecycle value, and its Root
  historical-product extension (L985) says RETIRED is "never an active project
  lifecycle value";
- `tools/practitioner_harness/adapter_project.py` L124–125 raises
  `HarnessOperationalError` when a non-Root project's `_STATUS.md` shows
  RETIRED. PEC has no `_harness/adapter.yaml` today, so nothing breaks now; it
  would if PEC adopted the practitioner harness while these files exist.

PEC does not depend on Root's answer: its edits are already hand-authored
under its own accepted instrument. For this loop: Root may reconcile its
method, tool, SPEC and adapter in whichever direction it chooses, or decline.

This notice grants no authority in the receiving loop, creates no
requirement there, and asks for no write. The receiving loop may adopt,
amend, defer or decline any implication under its own instruments.
