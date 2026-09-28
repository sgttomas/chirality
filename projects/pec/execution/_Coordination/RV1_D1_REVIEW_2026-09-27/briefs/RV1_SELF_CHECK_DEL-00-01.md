# RV1 REVIEW TASK — DEL-00-01 SELF_CHECK

Read `COMMON_REVIEW_TASK.md` beside this file first; it binds you.

- **Deliverable:** `DEL-00-01` — `{P}/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/`.
- **Review type:** `SELF_CHECK` — the owner's replacement ruling of 2026-08-01
  recorded in the deliverable's `_REVIEW.md` ("I agree with your
  recommendation for the replacement ruling. Proceed accordingly."), carried
  by `D-PEC-107`. In the old method `SELF_CHECK` is "producer reviews own
  work", focused on completeness, internal consistency and TBD reduction. The
  prior record performed it as a producer-side mechanical `AGENT_CHECK` with
  no human reviewer; do the same.
- **Reviewer identity:** `REVIEW-SELF-DEL-00-01-20260927-RV1` — a fresh Type 2
  TASK instance on the PEC loop's producer side. State plainly that SELF_CHECK
  is not independent review, that you authored none of the `D-PEC-105` bytes
  (true of your own context: confirm it), and that no human reviewer is
  inferred.
- **Bytes under review (verify first; stop on mismatch):**
  `artifacts/v2/ADRs.md` `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e`;
  `ScopeOfWork.md` `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647`.
- **Checklist:** 7 criteria, `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9`
  (prior `bb815439…3b84`; the `D-PEC-105` proposal says only the source hash
  changed — confirm by diffing against a derivation from the prior SOW
  `4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740`, which you
  can obtain with `git show` of the pre-act commit into `$TMPDIR`).
- **Prior review records:** `_REVIEW.md` (`c417418e…6968`),
  `Review_Findings.csv` (`3f1cec3b…25e0`, header only), snapshots
  `{P}/_Evaluation/Reviews/REV_DEL-00-01_2026-08-01_1935`, `…_2029`, `…_2109`
  (the 2026-08-01 SELF_CHECK and the AC-007 acceptance), and the ruling
  `ARTIFACT_ACCEPTANCE_AND_DEL10_REPAIR_RULING_2026-08-01.md` it cites.
- **Assess at least:**
  - every `AC-001`..`AC-006` against the amended ADR and SOW; `AC-007` is the
    owner-only criterion: record what the owner would confirm (the selected
    core-isolation style at the ADR; that nothing in the set makes a governed
    act depend on PEC-held state) and whether the amended bytes still support
    both confirmations;
  - whether the ADR's six `D-PEC-105` hunks (`D1_PREMISE_AMEND_2026-09-27/premise/DEL-00-01_ADR.json`)
    and add-on P's three SOW hunks (`…/premise/DEL-00-01_SOW.json`) left the ADR
    and its contract consistent (CLM-005, REQ-004 vs carried posture 3; OUT/AC/VER closure);
  - proposal "Other findings" 1, 7, 8, 10 (and 9, 11 where they bear on this
    deliverable) and intake CAND-01 item 8: decide for each whether it is a
    finding of this review, with a severity, or out of scope, and why;
  - OC-001 (`OBJ-005`), DS (`Dependencies.csv`: active upstream `EXECUTION`
    rows), TB (registered `TBD-*` and unregistered TBD text).
- **Snapshot label:** `REV_DEL-00-01_2026-09-27_HHMM` (the manager creates it).
