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

The owner then asked about K3. HELP_HUMAN's last recommendation before this direction was:
- K3 stays PEC's single publication record in its tier-0 profile, prepared when a DEL-08-06 production packet fixes the tool's exact shape;
- a per-project consumer contract with PEC is a design addition for the next PEC scope change.

## Resolution (HELP_HUMAN interpretation)

| Item | Resolution |
|---|---|
| CAND-PEC-2026-09-27-01 | **Disposition (b).** Each residual contract item is absorbed by its own deliverable's first production or currency packet. The PKG-02 items go with the first parser packet. The DEL-00-01 and DEL-00-03 items go with RV1: as inputs to that REVIEW, and corrected only by an owner-ruled packet. No SOW-currency packet is allocated for them. |
| CAND-PEC-2026-09-27-02 | **Promoted** as one Task Management row. It resolves in the next PEC scope change, which bundles the listed decomposition and PRD wording, plus an instruction-tranche item for the `AGENTS.md` sentence. |
| CAND-PEC-2026-09-27-03 | **Promoted** as one Task Management row and **routed to Root**. A coordination notice in Root's coordination folder asks Root to allocate hosted CI for PEC v2's registered checks, with a full-history checkout. Root decides its own intake. |
| DEL-01-06 `MEMORY.md` `D-PEC-96` row | **Kept** as merged in PR #1014. No change. |
| RV1 | **Authorized.** This is the separate REVIEW authorization that `D-PEC-105` RR1 requires. See "RV1 authorization" below. |
| K3 | **HELP_HUMAN's recommended approach.** K3 remains PEC's single publication record: one tool entry in `_DomainEngines/profiles/pec.yaml`, a tier-0 act the owner rules. A PEC Task Management row tracks it, replacing the carried graph node. The row is triggered by a DEL-08-06 production packet that fixes the tool's exact shape (DEL-08-06 TBD-003/004/006). DEL-08-06 TBD-007 and CON-002 go with it. PEC decides what it publishes. The per-project consumer contract (what each project takes from PEC and on what terms, the counterpart of each loop's feed-profile row) is added to the promoted CAND-02 row as a design item for the next PEC scope change. |
| Production | **Not in this undertaking.** Production happens in a different session, and its packets are decided there. This undertaking prepares a production packet only if one becomes a dependency of something necessary here. |

## RV1 authorization

This section names what `D-PEC-105` RR1 says "the later authorization names": the review type and the method basis.
- **Scope.** A REVIEW of the `D-PEC-105` postimages for each deliverable:
  - DEL-00-03 SPEC `f84c067b…f617` and SOW `0fed4ecb…e843`;
  - DEL-00-01 ADRs `ad6bab7e…c49e` and SOW `3757632b…a647`.

  Each review uses a fresh checklist derivation. The `D-PEC-105` proposal tables the expected checklists: DEL-00-03 `a3bc80a0…21b1` and DEL-00-01 `6e99f93c…8cf9`. The review writes each deliverable's `_REVIEW.md`, its `Review_Findings.csv` and one new `_Evaluation/Reviews/REV_DEL-00-0x_<date>_<time>/` snapshot, plus the reviews `_LATEST.md` pointer where the method requires it. The CAND-01 (b) DEL-00-01/00-03 items are review inputs.
- **Review type.** The same as each deliverable's prior acceptance: `SELF_CHECK` for DEL-00-01 (the owner's replacement ruling recorded in its `_REVIEW.md`) and `PEER_REVIEW` for DEL-00-03.
- **Method basis (HELP_HUMAN's choice, disclosed).** The bundled `review` workflow as of commit `2f825f180`. That is the last edition before Root's SPEC §3.4 alignment tranche (`77dbfcb72` onward, `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md`), which PEC has not adopted: the owner deferred Root notices for PEC, and `D-PEC-105` excludes adopting the revised edition. The revised edition's CHECKING-entry, frozen-SHA and reversal rules are not applied. If they would surface anything for these CHECKING deliverables, it is recorded as a consequence for the owner's reserved decision, and **nothing prompts about CHECKING**.
- **Limits.**
  - No lifecycle change and no CHECKING, ISSUED or Gate 5 act.
  - No write to a `ScopeOfWork.md` or artifact. A correction the REVIEW finds needs its own owner-ruled packet before re-acceptance.
  - No acceptance: the owner's `ACCEPT_EXACT_BYTES` of the reviewed hashes follows as a separate owner act. It carries the confirmations the prior acts carried (DEL-00-01 AC-007; DEL-00-03 AC-011), and HELP_HUMAN presents it once the REVIEW has merged.
- **Models:** Opus 5.5 (`claude-opus-5-5`) at high reasoning, per the owner's standing steer.
