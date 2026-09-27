# D-PEC-108: owner decision on the RV1-reviewed D1 bytes (all findings accepted as-is; exact-byte re-acceptance of DEL-00-01 and DEL-00-03; CU-001 retired)

Owner: Ryan Tufts. Date: 2026-09-27. Recorded by HELP_HUMAN as a faithful transcription under K-AUTH-1. The record belongs to work-graph node ACC of undertaking `HELP-HUMAN-PEC-20260927-RV1-INTAKE`.

## Exact owner decision (verbatim)

> ACC: option 1; accept all findings as is; re-accept DEL-00-01 and DEL-00-03 exact bytes; retire CU-001

HELP_HUMAN's preceding presentation offered exactly this string as the reply that takes the recommendation. It reported:
- that the RV1 REVIEW merged as PR #1023 (`31a90f3e6`), after two independent reviews with nothing blocking and green CI (`AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/REVIEW_PR1023_0{1,2}.md`);
- that `D-PEC-105` corrected premises in four files, which let the owner's earlier exact-byte acceptances of them lapse, and that neither deliverable changes status (both stay `CHECKING`);
- DEL-00-03 (peer review): AC-001 to AC-010 pass, with no CRITICAL or MAJOR finding. There are two MINOR findings proposed for revision (RF-004, "Not a Git actor" missing from the SPEC's non-goals; RF-005, an unresolvable commit citation) and five observations. CU-001 still asserts revision-1.4 totals;
- DEL-00-01 (self-check): RF-001, MAJOR. AC-002 is only partly met, because the ADR's Context omits the "§16 open decisions are adapter-level" element and the functional-core element appears only later in the ADR. The decision itself is unaffected, and the independent reviewer read the severity as MINOR under the method's definitions, while MAJOR is the conservative reading. "The severity call is yours." There are also three MINOR findings proposed for revision and one observation;
- three options:
  - **1**, accept every finding as-is and re-accept both deliverables' exact bytes (recommended);
  - **2**, revise the flagged findings, with the corrections recorded, not prepared, under the freeze;
  - **3**, a mixed route, re-accepting DEL-00-03 only;
- what option 1 records, which the next section transcribes.

Status: **OPTION 1 RULED / ALL RV1 FINDINGS ACCEPT_AS_IS / ACCEPT_EXACT_BYTES / CU-001 RETIRED / EFFECTIVE ON SHARED-MAIN PUBLICATION**.

## What the decision records

### Finding dispositions

Every RV1 finding is `ACCEPT_AS_IS` and recorded as a known limitation:
- DEL-00-01: RF-001 to RF-005;
- DEL-00-03: RF-004 to RF-010.

For DEL-00-01 RF-001, this means AC-002 is accepted as partly met. The owner made no separate severity call, so RF-001's severity stays MAJOR as recorded. `ACCEPT_AS_IS` is not a deferral.

The reviewers' REVISE proposals stay on the record as considerations for the owner's ground-up reassessment under the `D-PEC-107` freeze point. No correction packet is prepared.

### ACCEPT_EXACT_BYTES

| Deliverable | File | SHA-256 |
|---|---|---|
| DEL-00-01 | `artifacts/v2/ADRs.md` | `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e` |
| DEL-00-01 | `ScopeOfWork.md` | `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647` (its first owner acceptance) |
| DEL-00-03 | `ScopeOfWork.md` | `0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843` |
| DEL-00-03 | `artifacts/v2/SPEC.md` | `f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617` |

These are the bytes that RV1 reviewed against the checklists in `../RV1_D1_REVIEW_2026-09-27/checklists/`.

### Acceptance-criterion confirmations

- **DEL-00-01 AC-007.** The owner accepts the ADRs at `ad6bab7e…c49e` as fit for DEL-00-01. The owner confirms ports-and-adapters (hexagonal) isolation as PEC v2's selected core-isolation style, and confirms that no governed act depends on PEC-held state.
- **DEL-00-03 AC-011.** The owner confirms the SPEC at `f84c067b…f617`, with its contract at `0fed4ecb…e843`, as PEC's v2 SPEC of record.
  - The SPEC was born from PRD v2.2 and decomposition revision 1.3 at `11a494e9a`. Its premises are now brought current to PRD v2.4 and revision 1.6 at `189f205ff`, under `D-PEC-105` reading 4(a).
  - The owner confirms that the single-objective attribution to OBJ-001 remains acceptable, given the recorded LOW-confidence qualification.
  - The alternatives, the full objective set and OBJ-006, stay unadopted.

### CU-001

DEL-00-03's custom checklist item CU-001 is retired as history and not carried forward. No successor custom item is added.

## Scope and limits

This decision:
- accepts these exact bytes only. There is no ISSUED, Gate 5, lifecycle, P1 or production act. *HELP_HUMAN interpretation:* following the RV1 return's owner-decision draft (`returns/RV1A_D1_REVIEW.md`), it also imposes this architecture on no other loop. That narrows the act and adds nothing to it;
- makes no C-05 act. The C-05 closure recorded under `D-PEC-72` relied on the earlier acceptances and stays as recorded. The optional C-05 line was not taken;
- leaves both deliverables `CHECKING`. Nothing here prompts about CHECKING;
- writes no `ScopeOfWork.md`, artifact, `_STATUS.md`, `v2/**`, PRD, decomposition, register, dependency, context or reference file;
- makes no readiness, release or reliance claim.

## Grant and records (HELP_HUMAN interpretation)

The owner's words name no write targets. The writes below are the review method's ordinary Gate 4 recording of an exact-byte acceptance, and they are no wider than the owner's act.

With this record and its register row, one WORKING_ITEMS instance may record the decision:
- in each deliverable's `_REVIEW.md` and `Review_Findings.csv`, setting the RV1 rows' `HumanDisposition` to `ACCEPT_AS_IS` and, because the pinned method (`2f825f180`, Gate 4 step 2) sets it for a final disposition, `Status` to `RESOLVED`, keeping prior bytes;
- in one acceptance snapshot per deliverable, following the 2026-08-09 precedent (`REV_DEL-00-03_2026-08-09_2156/`), with the reviews `_LATEST.md` pointer moved to the newer one.

The records are `_Evaluation/Reviews/REV_DEL-00-01_2026-09-27_1655/` and `REV_DEL-00-03_2026-09-27_1658/`, with evidence in `../RV1_ACCEPTANCE_RECORD_2026-09-27/`, all in PR #1028. With RF-001 resolved, the method's precondition that MAJOR findings are resolved before ISSUED is formally met. No Gate 5 or ISSUED act follows from that.

The same closeout PR also writes:
- the two `MEMORY.md` rows granted in `D-PEC-107_MEMORY_GRANT_2026-09-27.md`;
- the central receipt, the work-graph completion, and `docs/STATUS.md` under `D-PEC-88`.

Everything publishes through the undertaking's final PR under the standing Git authorization of 2026-09-12.

- **Verification:**
  - the four hashes reproduce at the PR head;
  - only the RV1 rows' `HumanDisposition` and `Status` change in the CSVs;
  - the strict-register, harness and loop-receipt outputs match `origin/main`;
  - an independent review covers the actual head.
- **Rollback:** before merge, drop the recording commits. After merge, revert the final PR's merge commit, which restores the RV1 rows to `TBD / OPEN`, the prior `_LATEST.md` and the `MEMORY.md` bytes. This record would then stand as the owner's decision, not yet recorded.
