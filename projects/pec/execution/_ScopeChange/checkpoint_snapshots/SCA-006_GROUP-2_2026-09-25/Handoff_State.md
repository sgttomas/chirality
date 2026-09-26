# Group-2 handoff

**Decision.** Checkpoint group 2 is accepted, as recorded in `DECISION.md` and
`ACCEPTED_MANIFEST.csv` (owner act 2026-09-25): the exact amendment and the
propagation plan, with Q-CP2-1 (a) and Q-CP2-2 (a). This snapshot, together
with `_DECISIONS/_REGISTER.md` row `D-PEC-97`, is the D-PEC packet that opens
Lane A.

**Next owning stage.** WORKING_ITEMS runs checkpoint-3 preparation for the
scope change under a HELP_HUMAN brief:
- verify the checkpoint-3 preconditions in
  `../../SCA-006_2026-09-25_1912/Propagation_Plan.md` against the live bytes;
- execute Lane A1, A2, A4 and A5. A6 waits for the checkpoint-3 acceptance;
- write the A4 tranche manifest and the three notices;
- run Lane C, with the C4 audit written into a new `COV_SCA006_POSTCHANGE_*`
  folder;
- present the audited poststate for the owner's checkpoint-3 acceptance.

**Derivative and closure state.**
- Derivative status is `INCOMPLETE`.
- There is no closure yet; checkpoint 3 is open.
- Reruns are `FROZEN`, because Lane B is not authorized.

**Expected structural result before B1.** 0 errors, with two DRB-008 warnings
for DEL-08-06 and DEL-10-13, whose folders do not exist until B1.

**What stays current.** Revision 1.5, PRD v2.3, `projects/pec/AGENTS.md` as it
stands, and `_LATEST.md` naming SCA-005 all remain current until the Lane A
writes land and checkpoint 3 is accepted.
