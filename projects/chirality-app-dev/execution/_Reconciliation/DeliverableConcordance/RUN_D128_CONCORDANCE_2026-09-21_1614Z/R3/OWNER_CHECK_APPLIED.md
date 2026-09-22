# Owner check applied — RUN_D128 (R4 step 1)

The owner's answers to `OWNER_CHECK.md` (owner direction `r3_owner_check_answers`, read in RUN_BASIS Addendum 13) applied to `CLAIM_CONCORDANCE.csv` and `EXTENSION_CONCORDANCE.csv` through `_work/DEC_OWNERCHECK.csv` (Source `OWNER_CHECK`, last in `r3_build.py` DECISION_ORDER). Answers are owner testimony about events, not rulings on direction of change. A yes confirms an event; whether the deliverable text is accurate is judged against the claim. Helper scripts: `_work/T1R4_scripts/`.

Totals: 75 decision lines; 75 REMAP_LOG lines appended; 63 listed rows, all changed (every listed row takes at least one note). Disposition moves: 2 (both `UNKNOWN` → `PARTIALLY_IMPLEMENTED`). HumanDecisionNeeded: unchanged on every row.

## Per question

### OC-01 — answer: yes

- `DEL-09-05#CLM-016.3` (rows noted; final AUTHORITY_CONFLICT, HDN R4)
  - `Notes+`: "OWNER_TESTIMONY: OC-01 yes (RUN_BASIS Addendum 13)"

### OC-02 — answer: yes

- `DEL-09-04#CLM-005` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-02 yes (RUN_BASIS Addendum 13)"
- `DEL-09-04#CLM-011.1` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-02 yes (RUN_BASIS Addendum 13)"
- `DEL-09-04#CLM-011.2` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-02 yes (RUN_BASIS Addendum 13)"
- `DEL-09-04#CLM-011.3` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-02 yes (RUN_BASIS Addendum 13)"
- `DEL-09-04#CLM-011.7` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-02 yes (RUN_BASIS Addendum 13)"
- `DEL-09-04#CLM-018` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-02 yes (RUN_BASIS Addendum 13)"

### OC-03 — answer: yes

- `DOC:BUILDREL#9.3` (rows noted; final ALIGNED, HDN NO)
  - `Notes` correction: "RELEASE_PROCESS_NOT_RUN:notarization of v3.0.1 - package.json" → "v3.0.1 notarization: owner testimony that it was notarized and stapled (OC-03); no record in the evidence roots - package.json" (text asserted the event did not happen)
  - `Notes+`: "OWNER_TESTIMONY: OC-03 yes (RUN_BASIS Addendum 13)"

### OC-04 — answer: yes

- `DEL-09-05#CLM-016.6` (rows noted; final PARTIALLY_IMPLEMENTED, HDN R4)
  - `Notes+`: "OWNER_TESTIMONY: OC-04 yes (RUN_BASIS Addendum 13)"

### OC-05 — answer: yes

- `DEL-09-05#CLM-010.8` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes` correction: "desktop:dist ran only in the recorded 2026-09-12 build (agent record)" → "desktop:dist runs are recorded for the 3.0.0-rc.1 and 3.0.0 builds (agent records, 2026-09-12 and 2026-09-13), none for 3.0.1; owner testimony (OC-05) that the full set incl. desktop:dist passed before v3.0.0 and v3.0.1 were accepted" (text asserted the event did not happen)
  - `Notes+`: "OWNER_TESTIMONY: OC-05 yes (RUN_BASIS Addendum 13)"

### OC-06 — answer: yes

- `DEL-09-01#CLM-009.8` (rows noted; final PARTIALLY_IMPLEMENTED, HDN R4-Q1)
  - `Notes` correction: "the last passing run (revision 3, stub adapter, daemon) predates the A2 re-platform" → "the last recorded passing run (revision 3, stub adapter, daemon) predates the A2 re-platform; owner testimony (OC-06) that a Section 8 pass against the Codex-hosted Runtime was run since" (text asserted the event did not happen)
  - `VerificationEvidence` correction: "NONE_FOUND (no Section 8 run at or after 39c0bb6ab)" → "NONE_FOUND (no Section 8 run recorded at or after 39c0bb6ab)" (text asserted the event did not happen)
  - `Notes+`: "OWNER_TESTIMONY: OC-06 yes (RUN_BASIS Addendum 13)"
- `DEL-09-01#CLM-011` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-06 yes (RUN_BASIS Addendum 13)"
- `DEL-09-01#CLM-023` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes` correction: "(no summary; last run 2026-09-04)" → "(no summary; last recorded run 2026-09-04; owner testimony OC-06 of a later run)" (text asserted the event did not happen)
  - `Notes+`: "OWNER_TESTIMONY: OC-06 yes (RUN_BASIS Addendum 13)"
- `DEL-09-01#REM-1` (rows noted; final REMAINING_STATE_MISMATCH, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-06 yes (RUN_BASIS Addendum 13)"

### OC-07 — answer: yes

- `DEL-09-02#CLM-020.2` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-07 yes (RUN_BASIS Addendum 13)"

### OC-08 — answer: don't know

- `DOC:BUILDREL#11` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_CHECK OC-08: don't know (owner does not recognise the terms; RUN_BASIS Addendum 13)"
- `DOC:BUILDREL#12` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_CHECK OC-08: don't know (owner does not recognise the terms; RUN_BASIS Addendum 13)"
- `DOC:RQGATES#12` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_CHECK OC-08: don't know (owner does not recognise the terms; RUN_BASIS Addendum 13)"
- `DOC:VALSTRAT#7` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_CHECK OC-08: don't know (owner does not recognise the terms; RUN_BASIS Addendum 13)"

### OC-09 — answer: no

- `DOC:BUILDREL#11` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-09 no (RUN_BASIS Addendum 13)"
- `DOC:BUILDREL#12` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-09 no (RUN_BASIS Addendum 13)"
- `DOC:RQGATES#12` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-09 no (RUN_BASIS Addendum 13)"
- `DOC:VALSTRAT#7` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-09 no (RUN_BASIS Addendum 13)"

### OC-10 — answer: yes

- `DEL-09-04#CLM-011.5` (rows decided; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Disposition`: `UNKNOWN` → `PARTIALLY_IMPLEMENTED` (OC-10 yes: the arm64 inspection happened (owner testimony). The claim requires the verification package to include the inspected architecture; the build record states arm64 identity (BUILD_EVIDENCE_RELEASE_20260913.md:12) but no inspection output is kept in the deliverable evidence or the AgentRuns records at the frozen basis.)
  - `Notes+`: "OWNER_TESTIMONY: OC-10 yes (RUN_BASIS Addendum 13). Disposition set from the answer and the claim: event confirmed, inspected record not kept in the verification package; ALSO:UNKNOWN on the record part if a record is kept outside the evidence roots."

### OC-11 — answer: yes

- `DEL-09-04#CLM-011.4` (rows decided; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Disposition`: `UNKNOWN` → `PARTIALLY_IMPLEMENTED` (OC-11 yes: the LSMinimumSystemVersion inspection happened (owner testimony). The claim requires the verification package to include the inspected value; configuration pins 15.0.0 (frontend/package.json:158) but no inspected value is kept in the deliverable evidence or the AgentRuns records at the frozen basis.)
  - `RemainingWork`: `Inspect and record LSMinimumSystemVersion on the candidate bundle` → `Record the LSMinimumSystemVersion inspection (owner testimony OC-11) in the verification package for the candidate bundle` (OC-11 yes: the inspection happened; the residual is the kept record, not the inspection.)
  - `Notes+`: "OWNER_TESTIMONY: OC-11 yes (RUN_BASIS Addendum 13). Disposition set from the answer and the claim: event confirmed, inspected value not kept in the verification package; ALSO:UNKNOWN on the record part if a record is kept outside the evidence roots."

### OC-12 — answer: yes

- `DEL-09-04#CLM-009.8` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-12 yes (RUN_BASIS Addendum 13)"
- `DEL-09-04#CLM-011.8` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_TESTIMONY: OC-12 yes (RUN_BASIS Addendum 13)"

### OC-13 — answer: don't know

- `DEL-09-04#CLM-012.1` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-13, RUN_BASIS Addendum 13)"
- `DEL-09-04#CLM-017` (rows noted; final PARTIALLY_IMPLEMENTED, HDN R4)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-13, RUN_BASIS Addendum 13)"
- `DEL-09-06#CLM-016` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-13, RUN_BASIS Addendum 13)"
- `DEL-09-06#CLM-021` (rows noted; final PARTIALLY_IMPLEMENTED, HDN D-APP-121)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-13, RUN_BASIS Addendum 13)"
- `DOC:RELIANCE#8` (rows noted; final STALE_SPECIFICATION, HDN R4-Q1)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-13, RUN_BASIS Addendum 13)"
- `DOC:VALSTRAT#4.11` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-13, RUN_BASIS Addendum 13)"

### OC-14 — answer: don't know

- `DOC:BUILDREL#9.5` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-14, RUN_BASIS Addendum 13)"
- `DOC:RELIANCE#11.1` (rows noted; final ALIGNED, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-14, RUN_BASIS Addendum 13)"
- `DOC:VALSTRAT#8` (rows noted; final ALIGNED, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-14, RUN_BASIS Addendum 13)"

### OC-15 — answer: don't know

- `DEL-09-04#REM-1` (rows noted; final REMAINING_STATE_MISMATCH, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-15, RUN_BASIS Addendum 13)"

### OC-16 — answer: don't know

- `DEL-09-05#CLM-010.6` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-16, RUN_BASIS Addendum 13)"

### OC-17 — answer: don't know

- `DEL-09-05#CLM-010.9` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-17, RUN_BASIS Addendum 13)"
- `DEL-09-05#CLM-010.15` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-17, RUN_BASIS Addendum 13)"

### OC-18 — answer: don't know

- `DEL-09-05#CLM-010.13` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-18, RUN_BASIS Addendum 13)"
- `DEL-09-05#CLM-010.14` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-18, RUN_BASIS Addendum 13)"
- `DEL-09-05#CLM-016.5` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-18, RUN_BASIS Addendum 13)"
- `DEL-09-05#CLM-023.1` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-18, RUN_BASIS Addendum 13)"
- `DEL-09-05#CLM-021` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-18, RUN_BASIS Addendum 13)"
- `DEL-09-05#CLM-022` (rows noted; final PARTIALLY_IMPLEMENTED, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-18, RUN_BASIS Addendum 13)"

### OC-19 — answer: don't know

- `DEL-01-03#CLM-017` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-19, RUN_BASIS Addendum 13)"
- `DEL-01-03#CLM-011` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-19, RUN_BASIS Addendum 13)"

### OC-20 — answer: don't know

- `DEL-00-01#CLM-018.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-00-02#CLM-021.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-01-01#CLM-018` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-01-02#CLM-038.4` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-01-03#CLM-022` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-01-04#CLM-020.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-02-01#CLM-023.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-02-02#CLM-021.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-02-03#CLM-023.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-02-04#CLM-021.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-02-05#CLM-020.1` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-05-03#CLM-020.1` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-05-04#CLM-019.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-10-01#CLM-022.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-10-04#CLM-023.2` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-10-05#CLM-020.1` (rows decided; final UNKNOWN, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-03-02#CLM-018` (rows noted; final STALE_SPECIFICATION, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-05-05#CLM-020.2` (rows noted; final STALE_VERIFICATION, HDN R4-Q1)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"
- `DEL-10-02#CLM-019.2` (rows noted; final STALE_VERIFICATION, HDN NO)
  - `Notes+`: "OWNER_BELIEF: likely performed if the instructions called for it (OC-20, RUN_BASIS Addendum 13)"

## Decided rows left `UNKNOWN`

22 rows (OC-14, OC-18, OC-19, OC-20; answer don't know): `DOC:BUILDREL#9.5`, `DEL-09-05#CLM-010.13`, `DEL-09-05#CLM-010.14`, `DEL-09-05#CLM-016.5`, `DEL-09-05#CLM-023.1`, `DEL-01-03#CLM-017`, `DEL-00-01#CLM-018.2`, `DEL-00-02#CLM-021.2`, `DEL-01-01#CLM-018`, `DEL-01-02#CLM-038.4`, `DEL-01-03#CLM-022`, `DEL-01-04#CLM-020.2`, `DEL-02-01#CLM-023.2`, `DEL-02-02#CLM-021.2`, `DEL-02-03#CLM-023.2`, `DEL-02-04#CLM-021.2`, `DEL-02-05#CLM-020.1`, `DEL-05-03#CLM-020.1`, `DEL-05-04#CLM-019.2`, `DEL-10-01#CLM-022.2`, `DEL-10-04#CLM-023.2`, `DEL-10-05#CLM-020.1`. Each carries the `OWNER_BELIEF` note only; Disposition, Confidence, RemainingWork, CauseTag and DirectionEvidence unchanged.

## Noted rows for R4 attention

Dispositions not changed (step 3). Each rested partly on absence of an event the owner now confirms:

- `DEL-09-05#CLM-010.8` (OC-05 yes): PARTIALLY_IMPLEMENTED rests partly on 'no recorded gate' for the full K-VALIDATE-1 set before release; the owner confirms it passed for v3.0.0 and v3.0.1. The code part (desktop:dist in no PR gate) stands. R3 had this row UNDECIDED.
- `DEL-09-01#CLM-009.8` (OC-06 yes): PARTIALLY_IMPLEMENTED and RemainingWork ('then rerun') rest partly on no post-A2 Section 8 run; the owner confirms one. The LEGACY_ONLY marker finding (R4-Q1) stands.
- `DEL-09-01#CLM-023` (OC-06 yes): STALE_SPECIFICATION rests partly on 'current stable summary ... unsupported' (no summary; last recorded run 2026-09-04); a later run is confirmed, the summary is still not in the tree. The CI-chain part stands.
- `DEL-09-01#REM-1` (OC-06 yes): RemainingWork asks to 'rerun Section 8 at a post-A2 basis'; the owner confirms a post-re-platform run. REMAINING_STATE_MISMATCH (gate condition 1 met) stands on code.
- `DEL-09-02#CLM-020.2` (OC-07 yes): PARTIALLY_IMPLEMENTED rests partly on no recorded 16-ID Section 9 run; the owner confirms one with its summary kept (location not stated). The CI-retention finding stands.
- `DEL-09-04#CLM-009.8` (OC-12 yes): PARTIALLY_IMPLEMENTED rests partly on no packaged app-server run with secret and network checks; the owner confirms one. The code finding (verify-codex-pin proves only --version; no secret/network assertion in the chain) stands. CLM-011.8 follows by SEE.
- `DEL-09-05#CLM-016.3` (OC-01 yes): AUTHORITY_CONFLICT stands on the texts; the owner's testimony that the 3.0.0 and 3.0.1 candidates were named and authorized bears on the G6a exact-candidate clause and on RemainingWork's 'release act for the published build'.

Other noted rows under yes/no answers: the Disposition rests on code or on records missing from the deliverable, which the answer does not change (OC-02 rows: the build record's location stays open; OC-04 `DEL-09-05#CLM-016.6`: the WP-11 record; OC-09 rows: the owner's 'no' agrees with the notes that a wider matrix is still open). Notes that still read `RELEASE_PROCESS_NOT_RUN:` under OC-08 and OC-14 (don't know) were left as written, per the brief.

## Checks

- C1 REMAP_LOG prefix byte-identical: PASS 1002876 bytes
- C2 appended lines all Source OWNER_CHECK: PASS 75 lines
- C3 concordance diffs only in listed rows/decided fields: PASS {'CLAIM_CONCORDANCE.csv': 53, 'EXTENSION_CONCORDANCE.csv': 10} []
- C4 REVERSE_CONCORDANCE byte-identical: PASS
- listed rows 63 rows changed 63
- r3_qa Q1 CLAIM_INDEX units dispositioned: PASS
- r3_qa Q2 EXTENSION_INDEX units dispositioned: PASS
- r3_qa Q3 capabilities claimed or listed as unmapped (with reach and state): PASS
- r3_qa Q4 package summaries reproduce from the ledgers (sealed Disposition census): PASS
- r3_qa Q5 no duplicate keys: PASS
- r3_qa Q6 REMAP_LOG reconciles the sealed census to the final census: PASS

Not rerun: `r3_owner_check.py`, `r3_clusters.py`, spot-check scripts.

## SHA-256 of rebuilt files

- `CLAIM_CONCORDANCE.csv` `a6f6cdda685173cac3aa8ab75d8dd823143feadbde2c44a755571337936dd852`
- `EXTENSION_CONCORDANCE.csv` `eeaaf27fcba05f2b8a16c6429a95be220b071c2b8938c41a3d5ff959854dbb37`
- `REVERSE_CONCORDANCE.csv` `2f07bfd122d88375c138d5a4ee86ef0023ebc06c9ada164ab41962e1f6648022`
- `REMAP_LOG.csv` `e53c0122d6c70c4ec91dde72232f4660e8475799ba2bbf7b0bdffe66e9150cd9`
- `INPUT_MANIFEST.md` `9f7f1b2755d89c3315a0959bb8c85ea197a907228a722bcc3407ed5dbc0037b9`
- `COVERAGE_AND_QA.md` `ccc03c6317babc0ad7a25723de72c8cd1fdb95e73ea41d91029e3da17d8c1cfa`
- `R3_SUMMARY.md` `7b12ad67181ac7db47f54709631d2b51812f2cba7bbc5f32e7b6fe836799c6ae`
- `_work/SEALED_ROWS.csv` `c3808d2eaa7b9383a6cf3582e41d9c01ad4d7aa8ed01e0741f893548f484ee5b`
- `_work/DEC_OWNERCHECK.csv` `e8b45bb671beba9cf73a0f0252e606786fa20e65b04971ca1e7088e13c93f401`
