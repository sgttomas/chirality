# D-PEC-107 — owner direction after the POST-SCA005 closeout: intake dispositions, RV1, K3, production

- **Owner:** Ryan Tufts. **Date:** 2026-09-27.
- **Recorded by:** HELP_HUMAN, as a faithful transcription under K-AUTH-1.
- **Undertaking:** this direction opens `HELP-HUMAN-PEC-20260927-RV1-INTAKE`, whose graph is `../WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md`.

## Exact owner direction (verbatim)

> Intake: CAND-01 b (each deliverable's production packet will absorb its own); CAND-02 promote; CAND-03 promote to Root; keep D-PEC-96 row.
> Proceed with RV-1.
> Take the approach you recommend for K3.
> Production itself will be done in a different session and production packets will be determined at that time, unless they become a dependency of something necessary.

## Context

HELP_HUMAN presented the closeout of `HELP-HUMAN-PEC-20260925-POST-SCA005` (final PR #1014, `974bf7da4`). That presentation covered:
- the three intake candidates in `../_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md`, with their options;
- the DEL-01-06 `D-PEC-96` MEMORY row;
- RV1 (`D-PEC-105` RR1);
- K3.

The owner then asked about K3, and HELP_HUMAN answered in two messages.

The earlier message recommended two things:
- (i) replacing the carried K3 node with a PEC Task Management row for the declaration;
- (ii) coordination notices suggesting that each project take in a consumer-enablement item.

The owner then reframed the question ("There should be a contract with PEC from each project.  PEC determines what it publishes.  The design of PEC is my responsibility."). HELP_HUMAN's last message recommended:
- (iii) keeping K3 as PEC's single publication record in its tier-0 profile, prepared when a DEL-08-06 production packet fixes the tool's exact shape;
- (iv) treating a per-project consumer contract with PEC as a design addition for the next PEC scope change.

The last message did not restate (i).

## Resolution (HELP_HUMAN interpretation)

| Item | Resolution |
|---|---|
| CAND-PEC-2026-09-27-01 | **Disposition (b).** Each residual contract item is absorbed by its own deliverable's first production or currency packet. The PKG-02 items go with the first parser packet. The DEL-00-01 and DEL-00-03 items go with RV1: as inputs to that REVIEW, and corrected only by an owner-ruled packet. No SOW-currency packet is allocated for them. |
| CAND-PEC-2026-09-27-02 | **Promoted** as one Task Management row. It resolves in the next PEC scope change, which bundles the listed decomposition and PRD wording, plus an instruction-tranche item for the `AGENTS.md` sentence. |
| CAND-PEC-2026-09-27-03 | **Promoted** as one Task Management row and **routed to Root**. A coordination notice in Root's coordination folder asks Root to allocate hosted CI for PEC v2's registered checks, with a full-history checkout. Root decides its own intake. |
| DEL-01-06 `MEMORY.md` `D-PEC-96` row | **Kept** as merged in PR #1014. No change. |
| RV1 | **Authorized.** This is the separate REVIEW authorization that `D-PEC-105` RR1 requires. See "RV1 authorization" below. |
| K3 | **HELP_HUMAN's recommended approach, as HELP_HUMAN interprets it (disclosed).** The substance is (iii): K3 remains PEC's single publication record, one tool entry in `_DomainEngines/profiles/pec.yaml`, which is a tier-0 act the owner rules. The tracking vehicle is (i), taken from the earlier message: a PEC Task Management row replaces the carried graph node. The earlier message's (ii), the per-project enablement notices, is dropped, because the owner's reframing replaced it with the consumer-contract design item (iv). This departs from the closeout intake's judgment that K3 was already homed and needed no intake row (INTAKE, "Supplied concerns judged already homed"). The owner's "the approach you recommend" is read as taking the row. The row also carries the PR #994 review 02 wording notes: TBD-004's owners include the access-class decision-logic owners, and CON-002 is the owner's question. The row is triggered by a DEL-08-06 production packet that fixes the tool's exact shape (DEL-08-06 TBD-003/004/006). DEL-08-06 TBD-007 and CON-002 go with it. PEC decides what it publishes. Under (iv), the per-project consumer contract (what each project takes from PEC and on what terms, the counterpart of each loop's feed-profile row) is a design item for the next PEC scope change. Attaching it to the promoted CAND-02 row, rather than a row of its own, is HELP_HUMAN's choice. |
| Production | **Not in this undertaking.** Production happens in a different session, and its packets are decided there. This undertaking prepares a production packet only if one becomes a dependency of something necessary here. |

## RV1 authorization

This section names what `D-PEC-105` RR1 says "the later authorization names": the review type and the method basis.
- **Scope.** A REVIEW of the `D-PEC-105` postimages for each deliverable:
  - DEL-00-03 SPEC `f84c067b…f617` and SOW `0fed4ecb…e843`;
  - DEL-00-01 ADRs `ad6bab7e…c49e` and SOW `3757632b…a647`.

  Each review uses a fresh checklist derivation. The `D-PEC-105` proposal tables the expected checklists: DEL-00-03 `a3bc80a0…21b1` and DEL-00-01 `6e99f93c…8cf9`. The review writes each deliverable's `_REVIEW.md`, its `Review_Findings.csv` and one new `_Evaluation/Reviews/REV_DEL-00-0x_<date>_<time>/` snapshot, plus the reviews `_LATEST.md` pointer where the method requires it. The CAND-01 (b) DEL-00-01/00-03 items are review inputs. The DEL-00-03 prior review's owner custom item CU-001 asserts revision-1.4 totals, now stale after the rebind to revision 1.6. The review states whether CU-001 carries forward, and how.
- **Review type.** The same as each deliverable's prior acceptance: `SELF_CHECK` for DEL-00-01 (the owner's replacement ruling recorded in its `_REVIEW.md`) and `PEER_REVIEW` for DEL-00-03.
- **Method basis (HELP_HUMAN's choice, disclosed).** The bundled `review` workflow as of commit `2f825f180` (`WORKFLOW.md` `f8a8f240…06bc`, `execution.json` `d1c668ae…74df`, `resources/contract.md` `d3d7eb27…b328`, `resources/method.md` `63c8a395…0daa`). The review follows the 2026-08-09 precedent: no transition is attempted and Gate 5 is not entered. No CRITICAL or MAJOR finding is recorded as DEFERRED, which keeps SPEC §3.4's rule even though the old edition would permit a deferral. The DEL-00-03 `PEER_REVIEW` is performed by a fresh agent instance independent of the `D-PEC-105` authors, as the prior review was (findings labelled as agent checks), and the record names that identity. The `2f825f180` edition is the last before Root's SPEC §3.4 alignment tranche (`77dbfcb72` onward, `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md`), which PEC has not adopted: the owner deferred Root notices for PEC, and `D-PEC-105` excludes adopting the revised edition. The revised edition's CHECKING-entry, frozen-SHA and reversal rules are not applied. If they would surface anything for these CHECKING deliverables, it is recorded as a consequence for the owner's reserved decision, and **nothing prompts about CHECKING**.
- **Limits.**
  - No lifecycle change and no CHECKING, ISSUED or Gate 5 act.
  - No write to a `ScopeOfWork.md` or artifact. A correction the REVIEW finds needs its own owner-ruled packet before re-acceptance.
  - No acceptance: the owner's `ACCEPT_EXACT_BYTES` of the reviewed hashes follows as a separate owner act. It carries the confirmations the prior acts carried (DEL-00-01 AC-007; DEL-00-03 AC-011), and HELP_HUMAN presents it once the REVIEW has merged.
- **Models:** Opus 5.5 (`claude-opus-5-5`) at high reasoning, per the owner's standing steer.

## Freeze point (owner direction, same day, verbatim)

HELP_HUMAN had listed further work that could run in parallel. That list covered three things:
- a consumer-contract options note, which HELP_HUMAN would start;
- preparing the next PEC scope change (SCA-007), if the owner opened it;
- what HELP_HUMAN would not start: production packets, re-reviews of DEL-04-01 and DEL-03-01 (unless folded into RV1), and the deferred Root notices.

The DEL-02-07/DEL-01-06 pair was not on the list; its re-review waits for their production. The owner replied:

> I don't want to proceed with the scope change right now.  I'm re-writing the App PRD and along with it the entire governance framework of Chirality.  I want to have this as a freeze point where important decision have been made and a large undertaking is complete.  This work you're proposing now is meant just to be put in the record so that it can be considered when everything undergoes a reassessment from the ground up.

**Resolution (HELP_HUMAN interpretation).**
- **The freeze point.** PEC's state at the merge of `HELP-HUMAN-PEC-20260925-POST-SCA005` (final PR #1014, `974bf7da4`), together with this record's decisions, is a freeze point: important decisions are made and a large undertaking is complete. The only additions after it are the TM1 and RV1 records and this undertaking's own graph, receipt and final PR. It is the basis for a later ground-up reassessment, alongside the owner's rewrite of the App PRD and of Chirality's governance framework.
- **No scope change now.** SCA-007 is not opened. The promoted CAND-02 row records it, together with the per-project consumer-contract design item, as a consideration for that reassessment. It is not scheduled work.
- **Recorded as considerations only.** The consumer-contract options note, the next scope change and the re-reviews HELP_HUMAN offered not to start are recorded here as considerations only. They are not prepared:
  - a per-project contract with PEC: what each project takes from PEC and on what terms, as the counterpart of each loop's feed-profile row, with who writes each side and how it relates to the PRD §12 reliance gate;
  - the next PEC scope change, bundling CAND-02;
  - re-review of DEL-04-01 and DEL-03-01, whose acceptances lapsed with no re-review scheduled.
- **Already-directed items still proceed.** TM1 records the owner's intake dispositions and the K3 row, which puts the decisions on the record. RV1 is the owner's explicit "Proceed with RV-1". Neither changes a frozen product byte.
  - During the freeze, any correction a RV1 finding calls for is recorded only and not prepared.
  - The owner's re-acceptance (graph node ACC) is part of RV1 as the carried records define it. HELP_HUMAN presents it once the REVIEW merges, and the decision stays the owner's.

  Asked whether RV1 should be held as part of the freeze, the owner replied, verbatim: "Yes I still want you to complete the task management work and the RV1."
- **MEMORY.** This record grants no `MEMORY.md` path. At closeout, HELP_HUMAN asks the owner for the grant (`projects/pec/AGENTS.md`, "Deliverable records and loop ownership"). The graph completes after the rows are written, or after the owner's recorded decision to complete without them.

## MEMORY grant (owner direction, same day, verbatim)

The MEMORY bullet above said that at closeout HELP_HUMAN would ask the owner for the grant. The owner gave it in advance:

> grant the MEMORY rows for DEL-00-01 and DEL-00-03

**Resolution (HELP_HUMAN interpretation).** At closeout (graph node M1), WORKING_ITEMS appends one `## Runs` row for this undertaking to each of these existing files. Both files were created under `D-PEC-105` add-on M. Each row records the RV1 REVIEW and its outcome and links the central receipt.
- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/MEMORY.md`
- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/MEMORY.md`

Prior bytes are preserved. No other `MEMORY.md` is opened. The grant is recorded here, in the governing `D-PEC` record, as `projects/pec/AGENTS.md` ("Deliverable records and loop ownership") requires.
