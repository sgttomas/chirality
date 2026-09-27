# Receipt — HELP-HUMAN-PEC-20260925-POST-SCA005

This is a derivative account. The [work graph](../../WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md) carries the execution, and the sources below keep their authority. The graph's owner-direction section quotes every owner direction and ruling verbatim.

## Owner direction

Ryan Tufts, 2026-09-25 (`D-PEC-94`), verbatim: "You can continue with all the open work you identified.  Start with the loop migration, then use the loops for organizing the remaining work into a work graph to help plan and orchestrate the implementation." Each fenced act below was separately owner-ruled.

## Result

- **Currency and registry.**
  - `D-PEC-95` P + R (PR #924, `abfd0897b`): revision-1.5 re-pin, 19 quote refreshes, TM-PEC-023 closed.
  - `D-PEC-96` revision 4 (PR #950, `73ed349ed`): registry schema v2, with PEC's row migrated to `shared-dev-loop`.
- **Scope change SCA-006.** Checkpoints 1–3 were accepted and revision 1.6 and PRD v2.4 applied (PR #943, `db9328789`; ruling PR #954, `189f205ff`).
- **Setup and re-pin.** `D-PEC-101` K4 + C, K1 and V (PR #976, `ce934ac33`). DEL-08-06 and DEL-10-13 were scaffolded at `OPEN`, 22 dependency rows were added, 129 contexts and references were re-pinned to revision 1.6, and audit `COV_D101_POSTSETUP_2026-09-26_1651` found 0 blockers.
- **Scope of Work contracts (36 exist):**
  - first contracts for DEL-02-08 and DEL-02-09 (`D-PEC-98`, PR #958) and for DEL-08-06 and DEL-10-13 (`D-PEC-103`, PR #992, with add-on S and the owner's C-08 classification of DEL-10-13, C8);
  - currency replacements:
    - S2, seven contracts (`D-PEC-100`, PR #979);
    - S4, eight contracts (`D-PEC-102`, PR #998);
    - S1, twelve contracts (`D-PEC-104`, PR #1010).
- **Derivative premises.** D1: premise-only amendments of the DEL-00-01 ADRs and contract and the DEL-00-03 SPEC and contract (`D-PEC-105`, PR #1007). Both deliverables stay `CHECKING`.
- **P1 fixtures.** X1: 34 files under `v2/tests/parsers/` and the `v2-parsers` check (`D-PEC-106`, PR #1008). Add-on L moved DEL-02-03, DEL-02-08 and DEL-02-09 to `IN_PROGRESS`.
- **Retirement.** PEC's 57 `## Remaining` sections were retired in the separate undertaking `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT` ([receipt](../HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT/RECEIPT.md)). S2, S4 and S1 absorbed its Part B carry-forwards.
- **Lifecycle census at close** (68 deliverables): 28 `OPEN` / 27 `INITIALIZED` / 4 `CHECKING` / 5 `IN_PROGRESS` / 4 `RETIRED`.
- **Owner acceptances that lapsed or became history under the ruled acts:**
  - DEL-02-07 and DEL-01-06 (`D-PEC-100`; recorded after the fact, with no contrary owner direction);
  - DEL-04-01 (`D-PEC-102`);
  - DEL-03-01 (lapsed) and DEL-01-05 (`D-PEC-77`, history), with the separate 2026-08-03 exact-artifact acceptance also history (`D-PEC-104`);
  - DEL-00-03 SOW and SPEC and DEL-00-01 ADR (`D-PEC-105`). With P, DEL-00-01's SELF_CHECK SOW basis describes superseded bytes.

  No review was opened for any of these.

## Checks

- Every fenced act had:
  - its proposal's finite verification;
  - an in-run independent verifier;
  - one or more fresh HELP_HUMAN PR reviews, transcribed under [`returns/`](returns/) as `REVIEW_PR*.md`;
  - required CI.
- Strict registers stayed at 0 errors throughout. Each act recorded its own before-and-after comparison. `D-PEC-95` ended at 0 warnings. `D-PEC-101` moved the result from 26 `XRG-013` plus 2 `DRB-008` to 26 `XRG-013` (68 registers, 285 rows). Every later act kept the 26 `XRG-013` identical (D-GOV-48 deferred). `D-PEC-100` (S2) recorded its comparison on a base from before `D-PEC-101`, so it still showed the 2 `DRB-008`. The harness self-check and the receipts validator passed.
- **Closeout C1** ([account](../../CLOSEOUT_POST_SCA005_2026-09-27/C1_ACCOUNT.md)):
  - a supported no-change result for every deliverable-local record of the 33 touched deliverables;
  - 127/127 active execution dependency quotes verbatim;
  - no missing implementation or evidence;
  - two newly found families of fenced contract text, carried to intake (below).
- **M1:** 31 `MEMORY.md` files were created and rows appended in DEL-01-03, DEL-01-06 and DEL-02-03/08/09, each linking this receipt. The verifier returned PASS WITH NOTES (`../../CLOSEOUT_POST_SCA005_2026-09-27/M1_VERIFIER_VERDICT_01.md`).
  - DEL-01-06 gained the `D-PEC-96` run row that ruling row 5 assigns to closeout, ahead of the `D-PEC-100` row. Its text is composed from the `D-PEC-96` proposal's named parts, because no exact row was tabled.
- **STATUS and README** changes made under `D-PEC-88` are listed in the graph's D-PEC-88 trace.

## Task Management transfer

Intake `../../_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md` holds three candidates awaiting the owner's disposition. The federation preflight was COMPLETE, and no register row was written.
- **CAND-PEC-2026-09-27-01:** contract-currency residuals with no owning packet. These include:
  - S2-1, the "(provisional `D-PEC-100`)" references;
  - F-C2, S4 CON items still routed to the K2 first Scopes of Work;
  - the S1 and S4 wording items;
  - DEL-10-11 `CLM-014`; DEL-03-04's quotation of DEL-03-01 `CON-005`; the partly overtaken DEL-02-07 and DEL-10-13 `CON-003` premises;
  - the DEL-02-08/09 wording items and others in the graph's carry list.
- **CAND-02:** decomposition, PRD and instruction wording awaiting a scope change or instruction tranche.
- **CAND-03:** hosted CI does not run PEC v2's registered checks (Root/CI scope).

## Carried beyond this undertaking

- **RV1:** the `D-PEC-105` RR1 re-review of the D1 bytes and the owner's re-acceptance (DEL-00-01 AC-007, DEL-00-03 AC-011). It needs its own owner authorization. It waits, BLOCKED, in the next undertaking's graph. RV1 is a CARRIED state, which extends the graph template's state vocabulary.
- **K3:** the tier-0 profile act (SCA-006 plan §B6). It follows a DEL-08-06 production packet that fixes the tool's exact shape (DEL-08-06 TBD-003/004/006). TBD-007 and CON-002 come with it.
- **From the `D-PEC-103` act:** two possible register amends (DEL-08-06 → DEL-04-03; DEL-10-13 → DEL-02-07), the missing PEC v2 release process (DEL-10-13 CON-004), and DEL-08-06 REQ-016 and AC-005/VER-005 (verifier notes 2 and 4).
- **For the first parser packet (X1 residuals):**
  - field attribution by review;
  - AST write-guard gaps;
  - partial-clone detection;
  - `.DS_Store`;
  - widening the `v2-parsers` path rule;
  - FX-PEC-0's run-index presupposition;
  - golden tests and value representations.
- **Carry sources held in hash-bound run-root files:**
  - `SOW_CURRENCY_S1_2026-09-27/HANDOFF_STATE.md` (register and record wording);
  - `D1_PREMISE_AMEND_2026-09-27/HANDOFF_STATE.md` items 6–7;
  - `SOW_INIT_K2_2026-09-26/HANDOFF_STATE.md`;
  - `X1_FIXTURES_2026-09-27/HANDOFF_STATE.md`;
  - the `D-PEC-100` proposal's register list.
- **Lapsed acceptances:** each deliverable's exact-byte `_REVIEW.md` binding records the prior bytes. A REVIEW against the new bytes precedes any re-acceptance, and any CHECKING or ISSUED step. RV1 covers the D1 pair; for the others the graph records that any new review waits for those deliverables' production.

## Final PR

[sgttomas/chirality#1014](https://github.com/sgttomas/chirality/pull/1014), from branch `claude/pec-post-sca005-closeout`. Its description is this receipt's result, checks and limits.

## Limits

- The only lifecycle changes were ruled ones. `D-PEC-101` K1 created DEL-08-06 and DEL-10-13 at `OPEN`. `D-PEC-98` S moved DEL-02-08 and DEL-02-09 `OPEN → INITIALIZED`, and `D-PEC-103` S moved DEL-08-06 and DEL-10-13 the same way. `D-PEC-106` L then moved DEL-02-03, DEL-02-08 and DEL-02-09 `INITIALIZED → IN_PROGRESS`.
- No CHECKING, ISSUED, artifact acceptance or REVIEW act, and nothing prompted about CHECKING.
- No readiness, release or reliance claim. Operational reliance still begins only at a release that passes the PRD §12 gate.
- No Task Management promotion or disposition. The three intake candidates are the owner's to dispose.
