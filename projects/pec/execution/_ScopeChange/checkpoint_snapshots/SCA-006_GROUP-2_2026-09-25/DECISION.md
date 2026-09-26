# SCA-006 checkpoint group 2 — accepted exact amendment and propagation plan

Recorded 2026-09-25 by HELP_HUMAN (undertaking
`HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node R2). This is a
faithful record of the owner's act in the session chat, transcribed under
K-AUTH-1. It claims no inspection the owner did not perform.

## What the owner had in front of them

HELP_HUMAN's preceding chat message reported that the checkpoint-2 package
merged as PR #934 (`a558f5a405390633085bb2c323d52ab445fe5bc0`), after the
manager's fresh verifier passed it on round 03 with no blocking finding in any
round. The message summarized:

- the PRD v2.4 candidate, including the PEC-K-03 operational-reliance text, the
  §8 `agent` class, PEC-ORI-007, PEC-API-006, PEC-API-007 and the standing §12
  gate, with 46 requirements becoming 49;
- decomposition revision 1.6: 100 scope items, 68 deliverables, DEL-08-06 and
  DEL-10-13;
- the `AGENTS.md` candidate, with an instruction tranche and Root, App and
  Runtime notices at checkpoint 3;
- the plan: 54 actions, 16 bindings and the S4 set;
- the later packets.

It put the package's question set, with a recommendation for each:
Q-CP2-A accept; Q-CP2-1 (a); Q-CP2-2 (a). It ended: "To take every
recommendation: "SCA-006 CP2: accept; Q1 a; Q2 a"".

## The owner's act (verbatim)

> SCA-006 CP2: accept; Q1 a; Q2 a

## HELP_HUMAN's interpretation (interpretation, not owner text)

| Item | Effect |
|---|---|
| Q-CP2-A | Accepted as one checkpoint-group-2 decision. The exact amendment and propagation plan are accepted at the hashes in `ACCEPTED_MANIFEST.csv`. The PRD v2.4 successor candidate is adopted for application with the decomposition at Lane A1 during checkpoint-3 preparation, and this snapshot is its adopting record: the candidate's Status row cites this folder. The act falls on 2026-09-25, which is the default of every acceptance-bound slot and of the folder token `SCA-006_GROUP-2_2026-09-25`, so the adopted PRD and `AGENTS.md` hashes stand as listed. The decomposition's acceptance-date slots take their actual dates at application and at checkpoint-3 acceptance, under the `Amendment_Preview.md` hash rule. The S4 membership is fixed as `Propagation_Plan.md` §B4 states. |
| Q-CP2-1 (a) | The I1 residual corrections ride the SCA-006 instruction tranche. `CP2_CANDIDATE/AGENTS.candidate.md` is applied at Lane A4, and work-graph node I1 completes with R3. |
| Q-CP2-2 (a) | This snapshot, with `_DECISIONS/_REGISTER.md` row `D-PEC-97`, is the owner-ruled D-PEC packet that opens PEC's write fence for Lane A. It opens:<ul><li>A1: the live `_Decomposition/SOFTWARE_DECOMP.md`, the four registers and `docs/PRD.md`;</li><li>A2: the `_CONTEXT.md` mirrors for Seq 30, 31 and 32;</li><li>A4: `projects/pec/AGENTS.md`, the tranche manifest `docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-<date>.yaml`, and the three non-binding notice files in Root, App and Runtime `execution/_Coordination/`;</li><li>A5: this SCA's snapshot folder;</li><li>A6: the two `_LATEST.md` pointers, only after checkpoint-3 acceptance;</li><li>C4's `_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_*` audit folder.</li></ul>Verification is the plan's Lane C, and rollback is its §"Failure and rollback". It does **not** open Lane B: B1 PROJECT_SETUP for DEL-08-06 and DEL-10-13, B2 dependency extraction, B3 the EvidenceQuote refresh, B4 SOW currency, B5 the DEL-00-03 SPEC premise, B6 the tier-0 profile act, and B7 the revision-1.6 re-pin. The owner did not direct adding the register-row number to the candidates' lineage lines, so the folder citation stands and the candidate bytes are applied unchanged (plan §A4 lineage note). |

**Notices.** The three A4 notices are the only foreign-path writes this
acceptance covers, and they grant nothing in the receiving loops. D-PEC-90
grant item 2 covers Root and App. The Runtime basis is the Root `AGENTS.md`
instruction-change notice rule, applied to Runtime DEL-02-06 `SOURCE_PINS.json`
S4–S6.

## What this acceptance authorizes and does not authorize

It authorizes checkpoint-3 preparation:
- verify the checkpoint-3 preconditions against the live bytes;
- execute Lane A as bounded above;
- run Lane C, including the post-change audit, which attributes COV-068/069/072/073 to `D-PEC-95` and not to SCA-006;
- complete the SCA snapshot (A5);
- present the audited poststate for the owner's checkpoint-3 acceptance.

It does not authorize any of the following:
- any Lane B item;
- any `v2/**`, `software-workflow.json`, SOW, SPEC, `_REFERENCES.md` or `_DEPENDENCIES.md` write;
- a tier-0 profile write;
- any pointer move before checkpoint-3 acceptance;
- any foreign-path write other than the three notices;
- any lifecycle change (plan §A3: none);
- any access-class change in running code;
- any consumer adoption or release;
- any CHECKING, ISSUED or artifact acceptance.

Nothing here prompts about CHECKING. Revision 1.5, PRD v2.3, SCA-005 as
`_LATEST.md`, and fences F-PEC-1..4 remain current until the Lane A writes land
and checkpoint 3 is accepted.

**Method edition (open).** SCA-006 was prepared on the scope-change edition
whose `contract.md` and `method.md` hash `4453a719…` and `34187e83…`. Root's
tranche `ROOT-WORKFLOW-WAVE2A-CHANGE-CONCERNS-20260926` revised both, to
`74793f04…` and `fd3fe525…`. Whether checkpoint 3 continues on the pinned
edition is recorded as an open choice for the owner in the work graph. This
acceptance does not decide it.
