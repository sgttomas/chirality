# Brief — T1: apply the owner-check answers (RUN_D128, R4 step 1)

You are a TASK (Type 2) worker dispatched by the R4 WORKING_ITEMS packet manager. You do not
delegate. Placeholders `<FROZEN_TREE>`, `<RUN>` and `<APP_WORK>` are resolved in your dispatch
prompt; never write their values into any output. Follow `<RUN>/R3/BRIEFS/_COMMON.md` for evidence
roots, git limits, CSV handling and path style, **except for the write scope below**, which
replaces its write scope for this task.

## Read first

- `<RUN>/RUN_BASIS.md` Addenda 10 and 13 (13 is the reading of the answers).
- `<APP_WORK>/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`,
  section `r3_owner_check_answers` (the owner's verbatim answers).
- `<RUN>/R3/OWNER_CHECK.md` (the 20 questions, with "Rows decided" and "Rows noted" per question).
- `<RUN>/CONVENTIONS.md` §2.6 (Disposition vocabulary, "Absence is not evidence of absence").
- `<RUN>/R3/_scripts/r3_build.py`, `r3_qa.py`, `r3_summary.py`, `r3lib.py`.

## Answers (Addendum 13)

OC-01..OC-07 yes; OC-08 don't know (the owner does not recognise "attestation" or "SBOM");
OC-09 no; OC-10..OC-12 yes; OC-13..OC-20 don't know, with the owner's belief that steps the
instructions called for were likely done.

## What to do

For every row listed under an OC question in `R3/OWNER_CHECK.md`, look up its current final row
(concordance) and decide field changes. Work script-first; judge each row individually against
its claim text in the frozen deliverable (read the claim at `<FROZEN_TREE>`).

1. **Rows decided, answer yes or no** (OC-10 `DEL-09-04#CLM-011.5`, OC-11 `DEL-09-04#CLM-011.4`,
   and any other decided row under OC-01..OC-12): set the Disposition from the answer **and** the
   claim text, on the frozen evidence. A yes confirms that the event happened; whether the
   deliverable text is then accurate is judged against the claim (for example, a claim that also
   requires a kept record or a specific procedure may still diverge). Update `Notes+` to record
   `OWNER_TESTIMONY: OC-nn <answer> (RUN_BASIS Addendum 13)`, and update `Confidence`,
   `RemainingWork`, `CauseTag` and `DirectionEvidence` only where the new Disposition requires it
   under CONVENTIONS (for example `CauseTag = NONE` and `DirectionEvidence = NOT_APPLICABLE` on
   ALIGNED). Leave HumanDecisionNeeded alone unless the row's only reason for a non-NO value was
   the owner check.
2. **Rows decided, answer don't know** (OC-14, OC-18, OC-19, OC-20 decided rows): Disposition stays
   `UNKNOWN`. For OC-13..OC-20 add to Notes (`Notes+`):
   `OWNER_BELIEF: likely performed if the instructions called for it (OC-nn, RUN_BASIS Addendum 13)`.
3. **Rows noted** (every question): the Disposition stands on other evidence. Correct any note text
   that asserts the event did not happen ("never ran", "not performed", "no v3.0.1 notarization",
   and so on) — use `Find`/`Replace` on the exact substring where the assertion is wrong in light
   of a yes/no answer, and add `Notes+` `OWNER_TESTIMONY: OC-nn <answer> (RUN_BASIS Addendum 13)`.
   For noted rows under OC-13..OC-20 add the `OWNER_BELIEF` note (step 2 wording). For OC-08 noted
   rows add `OWNER_CHECK OC-08: don't know (owner does not recognise the terms; RUN_BASIS Addendum 13)`.
   If a noted row's Disposition rested partly on absence of the event that the owner now confirms
   (or denies), **do not change it**; list it in `OWNER_CHECK_APPLIED.md` under "Noted rows for R4
   attention" with one line of reasoning.
4. Do not change any row not listed in `R3/OWNER_CHECK.md`.

## Mechanism

- Write the decisions to `<RUN>/R3/_work/DEC_OWNERCHECK.csv` in the existing decision-file format
  used by `r3_build.py` (`ClaimKey,Field,NewValue,Source,RuleOrEvidence,Find,Replace`, Source `OWNER_CHECK`, as the other
  `_work/DEC_*.csv` files; check one). Use `Notes+` for appended notes, `Find`/`Replace` for
  corrections of existing note text.
- Edit `r3_build.py` minimally:
  - add `("DEC_OWNERCHECK.csv", "OWNER_CHECK")` as the **last** entry of `DECISION_ORDER`;
  - write REMAP_LOG so that all `OWNER_CHECK` lines come **after** all earlier lines (a stable
    partition), so the existing REMAP_LOG is kept byte-for-byte as a prefix and the new lines are
    appended. Add a one-line comment saying why.
- Edit `r3_summary.py` minimally so the §3 Source table and moves list include `OWNER_CHECK`.
  Keep `_work/SUMMARY_HANDWRITTEN.md` unchanged except for **appending** one short paragraph
  "Owner check applied (R4 step 1)" that points to `OWNER_CHECK_APPLIED.md`.
- Rebuild with the existing scripts: `r3_build.py`, then `r3_qa.py`, then `r3_summary.py`.
  **Do not rerun** `r3_owner_check.py` (the questionnaire is the record put to the owner),
  `r3_clusters.py` (cluster membership is frozen for R4), or the spot-check scripts.
- **Checks, all must hold (report each):**
  - the pre-change `REMAP_LOG.csv` (copy at `<RUN>/R4/_work/pre_owner_check/REMAP_LOG.csv`,
    excluding its final `#END` record) is a byte-identical prefix of the new one;
  - every appended line has Source `OWNER_CHECK`;
  - `CLAIM_CONCORDANCE.csv` and `EXTENSION_CONCORDANCE.csv` differ from the pre-change copies
    only in rows listed in `OWNER_CHECK.md`, and in those rows only in the fields you decided and
    in `RemapSources`;
  - `REVERSE_CONCORDANCE.csv` is byte-identical to the pre-change copy;
  - `r3_qa.py` Q1–Q6 all PASS (Q6 is the REMAP_LOG replay).
  If a check fails, fix the cause and rebuild; never hand-edit a built file.
- Write `<RUN>/R3/OWNER_CHECK_APPLIED.md`: per OC question, the answer, each row changed with
  field, old → new, and one line of reason; the unchanged decided rows; "Noted rows for R4
  attention"; the check results; SHA-256 of the rebuilt files.

## Write scope

Only: `<RUN>/R3/_work/DEC_OWNERCHECK.csv`, `<RUN>/R3/_work/T1R4_scripts/**` (helpers),
`<RUN>/R3/_scripts/r3_build.py` and `r3_summary.py` (the minimal edits above),
`<RUN>/R3/_work/SUMMARY_HANDWRITTEN.md` (append only), and the files the rebuild scripts write
(`R3/CLAIM_CONCORDANCE.csv`, `EXTENSION_CONCORDANCE.csv`, `REVERSE_CONCORDANCE.csv`,
`REMAP_LOG.csv`, `INPUT_MANIFEST.md`, `_work/SEALED_ROWS.csv`, `COVERAGE_AND_QA.md`,
`R3_SUMMARY.md`), plus `<RUN>/R3/OWNER_CHECK_APPLIED.md`. Nothing else.

## Return (≤ 12 lines)

Rows changed by answer (Disposition moves and note-only changes), the noted rows for R4
attention, the check results, and SHA-256 of `CLAIM_CONCORDANCE.csv`, `EXTENSION_CONCORDANCE.csv`,
`REMAP_LOG.csv`, `R3_SUMMARY.md`, `OWNER_CHECK_APPLIED.md`.
