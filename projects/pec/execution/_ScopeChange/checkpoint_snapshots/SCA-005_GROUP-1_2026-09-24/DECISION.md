# SCA-005 checkpoint group 1 — accepted impact assessment and change set

Recorded 2026-09-24 by HELP_HUMAN (run `HELP-HUMAN-PEC-20260923-SCA005`,
continuation G3). This is a faithful record of the owner's act in the
session chat, transcribed under K-AUTH-1. It is not a new request for the
same decision and it claims no inspection the owner did not perform.

## What the owner had in front of them

HELP_HUMAN's preceding chat message reported that PR #884 had merged and
asked the owner to "Accept checkpoint 1 at Impact Assessment hash
`0bcbe9bd…39bf` with the note's resolutions as the selected options". "The
note" is `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/CHECKPOINT1_RESOLUTION_NOTE.md`
(SHA-256 `af4e46d0dba2fb71c8f4aceca69098d81806b9add1ac960f074aa8fe949b0ad2`),
whose Section A resolves Q1–Q10 and CP1-R/D79/X/N/V/O each to one option
by citation to an accepted source, and whose Section B leaves CP1-A/CP1-B
and the TM-PEC-023 row selections to the owner.

## The owner's act (verbatim)

> I accept checkpoint 1 and the Impact Assessment.  Explain to me the other decisions I face with the context I need.

## HELP_HUMAN's interpretation (interpretation, not owner text)

| Item | Effect of this acceptance |
|---|---|
| CP1-A | The parsed change set in `Amendment_Actions.csv` (SHA-256 `5c4ae0532eb65ea83d0529a9f6395da392ae2bf5b254cfb6b2de49e4fbff2be2`, 76 PROPOSED actions: 8 ADD / 65 MODIFY / 3 REMOVE) is confirmed as the intake. Under the Q9 resolution, Seq 72 (SOW-058 MODIFY) is dropped when the checkpoint-2 exact amendment is prepared; under the Q10 (a) resolution, Seq 75 (PRD successor candidate) is narrowed: its "§12 P1 (Q10 c)" element is dropped and risk R-04's control becomes Q10 (a). The snapshot CSV is not rewritten. |
| CP1-B | `Impact_Assessment.md` is accepted at SHA-256 `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf`. |
| Q1–Q10, CP1-R, CP1-D79, CP1-X, CP1-N, CP1-V, CP1-O | Selected as the note's Section A resolutions: Q1 O-B2; Q2 (b); Q3 P-β; CP1-R R1; Q4 (a); Q5 (a); Q6 re-express with decisions open; Q7 (b); Q8 (a); Q9 no SOW-058 change and Seq 72 dropped (the Impact Assessment's §12.4 option (b)); Q10 (a) with no PRD exit-test change; CP1-D79 (b) one successor v2.3 candidate; CP1-X ADD DEL-02-08/09 with central receipts in SOW-013/DEL-02-03; CP1-N retain names and paths; CP1-V within D-PEC-78 O-A with no supersession; CP1-O OBJ-001;OBJ-002. Where a resolution differs from the design note or the manager (Q9, Q10), the note's cited source governs. |
| CP1-TM | Confirmed as carried: the nine TM-PEC-023 rows remain candidate MODIFYs with no option selected. Rows 4 and 7 (DEL-07-02, DEL-07-05) become moot under R1. The seven live rows are selected by the owner at checkpoint 2 through mechanic M1. |

## What this acceptance authorizes and does not authorize

It authorizes preparation of the checkpoint-2 package only: the exact
amendment (preview and postimage), the propagation plan, the PRD v2.3
successor candidate carrying the D-PEC-79 hunks, the `Supersession_Delta.csv`
bindings, and recommended (not selected) TM-PEC-023 row dispositions.

It applies no decomposition, decomposition-register, PRD, SOW, `_CONTEXT.md`,
`_STATUS.md`, `v2/**`, `software-workflow.json` or foreign change, and it
moves no active pointer: the amendment-qualified group-1 pointer
`../../SCA-005_GROUP-1_AUTHORIZED.md` is written per the scope-change method
("finalize the group-1 decision snapshot and pointer"), and `_LATEST.md` is
not touched. It does not
apply the D-PEC-79 postimage, select any TM-PEC-023 option, rule D-PEC-87,
or lift the D-PEC-86 I-7 deferral of PEC's own loop-method migration. The
exact candidate remains subject to checkpoint 2 and the audited poststate to
checkpoint 3; `_ScopeChange/_LATEST.md` continues to name SCA-004.

Upstream instruments that remain current during preparation: accepted
decomposition revision 1.4 (`SOFTWARE_DECOMP.md` SHA-256
`7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`), live
PRD v2.2 (SHA-256 `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`),
accepted SCA-004 snapshot, D-PEC-78 O-A, D-PEC-79 adopted-not-applied bytes,
fences F-PEC-1..4.
