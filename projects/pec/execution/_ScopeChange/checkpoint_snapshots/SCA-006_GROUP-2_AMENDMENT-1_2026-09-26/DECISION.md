# SCA-006 checkpoint group 2 — amendment 1: `AGENTS.md` Remaining-sections correction and the method edition

Recorded 2026-09-26 by HELP_HUMAN (undertaking
`HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node R3). This is a
faithful record of the owner's acts in the session chat, transcribed under
K-AUTH-1. It is additive to `../SCA-006_GROUP-2_2026-09-25/`, which stays
unchanged.

## The owner's acts (verbatim)

> Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them.

> revision 4: drop remaining-items and remaining-loop; yes, ride checkpoint 3.  SCA-006 pinned.

## HELP_HUMAN's interpretation (interpretation, not owner text)

| Item | Effect |
|---|---|
| Method edition ("SCA-006 pinned") | SCA-006 checkpoint 3 runs on the scope-change edition it was prepared under: `workflows/scope-change/resources/contract.md` `4453a719f1588c4eba08bdb4a979140ff3541ed5a29f04477ea58a844f344d02` and `method.md` `34187e83856853f655389625e3465e3c2cb9ff8ad38be1f4d138ee7470d167f5`, with `WORKFLOW.md` `58f5d1d53c655fdc5668d928f6087003590f40e321e25e3d9447805ee64a7a90`. These are read from the Git history, for example at `4d5f7b911`. The Root wave-2A revision applies to later PEC scope changes. The checkpoint-3 audit runs the current `audit-decomp`, a separate workflow, and may classify the D-PEC-95-resolved findings as `EXPECTED_CONSEQUENCE`. This mixing of editions was disclosed to the owner before the choice. |
| `AGENTS.md` Remaining correction ("yes, ride checkpoint 3") | The instruction candidate applied at Lane A4 gains exactly one correction. That candidate is `CP2_CANDIDATE/AGENTS.candidate.md`, accepted at `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d`. The correction replaces the paragraph at candidate L261–270 (live `projects/pec/AGENTS.md` L241–250), and no other line. The replacement states: PEC adds no new `## Remaining` sections or entries; PEC does not read them; new open scope goes to the work graph and its governing records. It keeps the status quo for the existing sections until any retirement ruling: they stay in place; each item's gate markers still bind that item; they are updated only under a packet that opens that `_STATUS.md`. It also keeps the statement that retiring them, as App and Piping did, is a separate owner-directed undertaking. WORKING_ITEMS drafts the exact hunk during checkpoint-3 preparation within these bounds, and the verifier checks it. **The owner's explicit approval of the exact hunk text is required before the checkpoint-3 application PR merges.** Display alone is not enough. |
| Existing 57 sections | Not deleted or retired by this amendment. Retiring them, as App and Piping did, is a separate owner-directed undertaking, and HELP_HUMAN puts that question to the owner. |

## Verification rule

This amends plan §A4 step 1 and Lane C1 item 2 for `AGENTS.md` only.
- The applied `projects/pec/AGENTS.md` must equal `49ce993a…070d` with its application-date slots filled per `AGENTS_MD_CANDIDATE_DIFF.md` §9, except for the one owner-approved hunk at candidate L261–270.
- The tranche manifest (draft `852b1d5b…`) and the three notices (drafts in §6.3) each gain only a named addition recording amendment 1: the owner's words, this snapshot's path, and the correction.
- Every other applied byte follows the accepted plan unchanged.

**Known consequence outside A4.** `docs/STATUS.md` ("the sections remain as records") goes stale once the correction applies. HELP_HUMAN corrects it under `D-PEC-88` in the same PR.

**Folder shape.** This amendment folder carries only `DECISION.md`, unlike SCA-005's group-1 amendments, which also carry `ACCEPTED_MANIFEST.csv` and `Handoff_State.md`. It accepts no new bytes now: the hunk's bytes are approved by the owner before merge. The package `Handoff_State.md` records the amendment instead.

## Bounds

- **Opens only** the correction above, inside the A4 write that `D-PEC-97` already opens.
- **Opens nothing new:** no new path, no `_STATUS.md` or lifecycle change, no SOW, and nothing under `v2/**`.
- **Instruction tranche:** the named additions to the manifest and notices (see the verification rule) record the correction as part of the SCA-006 instruction tranche.
- **No acceptance claims:** no CHECKING, ISSUED or acceptance claim.

Live `projects/pec/AGENTS.md` at the time of this record: `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a`.
