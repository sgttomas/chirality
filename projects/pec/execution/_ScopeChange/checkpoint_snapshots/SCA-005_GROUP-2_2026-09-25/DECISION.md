# SCA-005 checkpoint group 2 — accepted exact amendment and propagation plan

Recorded 2026-09-25 by HELP_HUMAN (run `HELP-HUMAN-PEC-20260923-SCA005`,
node G16). This is a faithful record of the owner's act in the session chat,
transcribed under K-AUTH-1. It claims no inspection the owner did not
perform.

## What the owner had in front of them

HELP_HUMAN's preceding chat message reported that the checkpoint-2 package
was published in PR #908 (merge `b08066aa273cb94bcc056c780d0fed1875091c0d`),
summarized the change, and put the package's question set
(`Propagation_Plan.md` §"Checkpoint-2 owner question set") with a
recommendation for each: Q-CP2-A accept, including the PRD §7.1
`WorkGraph / WorkNode` row that no Annex B row carries; Q-CP2-1 (a);
Q-CP2-2 (a); Q-CP2-3 (a); Q-CP2-4 (a) "with A4 deferred", explaining that the
final PR review had found Lane A4 (preparation of the DEL-02-08 and DEL-02-09
folders) not exact enough to be a D-PEC packet: its folder names are not
fixed, its `Dependencies.csv` ANCHOR rows overlap Lane B3, and
`projects/pec/AGENTS.md` has PROJECT_SETUP scaffold under its own packet. It
ended: "To take every recommendation, you could say: "CP2: accept; Q1 a; Q2
a; Q3 a; Q4 a with A4 deferred.""

## The owner's act (verbatim)

> CP2: accept; Q1 a; Q2 a; Q3 a; Q4 a with A4 deferred.

## HELP_HUMAN's interpretation (interpretation, not owner text)

| Item | Effect |
|---|---|
| Q-CP2-A | Accepted as one checkpoint-group-2 decision: the exact amendment and propagation plan at the hashes in `ACCEPTED_MANIFEST.csv`, including the PRD §7.1 `WorkGraph / WorkNode` row. The PRD v2.3 successor candidate bytes are adopted for application with the decomposition during checkpoint-3 preparation; this snapshot is its adopting record (the candidate's Status row cites this folder). The act falls on 2026-09-25, the value every acceptance-bound slot already carries, so no slot substitution changes any hash. |
| Q-CP2-1 (a) | The four retired deliverables (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) record `RETIRED` in `_STATUS.md` through the hand-authored exact edits of Lane A3, with an informational notice to Root that its scope-change method, `tools/scaffolding/write_status.sh`, `docs/SPEC.md` §3.2 and the practitioner-harness adapter disagree about RETIRED. The notice is sent during checkpoint-3 preparation. |
| Q-CP2-2 (a) | The INV-116 ContextBudgetQA correction rides A-12 as in the candidate. |
| Q-CP2-3 (a) | Residual stale text (`Amendment_Preview.md` §12) stays, with the supersession bindings the package records (D-026, D-029, D-033), and is carried into the next PEC scope change (the D-PEC-90 amendment, run-record node H6). |
| Q-CP2-4 (a), A4 deferred | This snapshot, with register row `D-PEC-92`, is the owner-ruled D-PEC packet that opens PEC's write fence for Lane A **except A4**: A1 (live `_Decomposition/SOFTWARE_DECOMP.md`, the four registers, `docs/PRD.md`), A2 (the 22 `_CONTEXT.md` mirrors), A3 (the four `_STATUS.md` retirements), A5 (this SCA's snapshot folder), A6 (the two `_LATEST.md` pointers, only after checkpoint-3 acceptance), and C4's new `_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_*` audit folder, with the plan's verification (Lane C) and rollback (§Failure and rollback). **A4 is not opened**: the DEL-02-08 and DEL-02-09 folders, their metadata files and their `Dependencies.csv` ANCHOR rows are created later by PROJECT_SETUP under its own packet, together with the Lane B3 dependency work. |

Consequences of deferring A4, recorded so checkpoint-3 preparation does not
treat them as defects: the Lane C1 allowlist excludes the two A4 folders;
Lane C2's expected result is 0 errors with the two DRB-008 warnings for
DEL-02-08 and DEL-02-09 (the plan's "after A4 and B3, 0/0" is not reached in
this stage); any `audit-decomp` finding in C4 that stems only from the absent
DEL-02-08/09 folders is reported as a consequence of this decision, not
repaired. The registers still carry the DEL-02-08 and DEL-02-09 rows, so the
Lane C3 counts are unchanged.

## What this acceptance authorizes and does not authorize

It authorizes checkpoint-3 preparation: execute Lane A as bounded above,
run Lane C, complete the SCA snapshot (A5), and prepare the audited
poststate package for the owner's checkpoint-3 acceptance.

It does not authorize: A4 or any Lane B rerun (PROJECT_SETUP re-pin,
dependency extraction, SOW currency, derivative artifacts, the registry
source packet, fixtures); any `v2/**`, `software-workflow.json`, SOW,
`_REFERENCES.md`, `_DEPENDENCIES.md` or foreign write; any pointer move
before checkpoint-3 acceptance; any lifecycle transition other than the four
A3 retirements; any CHECKING, ISSUED or artifact acceptance; or the D-PEC-90
reliance amendment. Revision 1.4, PRD v2.2, SCA-004 as `_LATEST.md`, and
fences F-PEC-1..4 remain current until the Lane A writes land and checkpoint 3
is accepted.
