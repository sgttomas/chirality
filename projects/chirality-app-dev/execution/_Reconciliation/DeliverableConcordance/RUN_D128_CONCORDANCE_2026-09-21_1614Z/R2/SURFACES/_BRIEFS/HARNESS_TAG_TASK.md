# Brief — R1b HARNESS-TAG (TASK, Type 2)

**Role:** TASK (Type 2). One bounded assignment; no delegation, no commits. Parent: the R1b
WORKING_ITEMS manager of run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-129 ruling C).
Placeholders `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>` are supplied in your prompt.

## Purpose

`<RUN>/R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` (60 rows, area
`frontend/src/lib/harness/**`) predates the adopted reach and enabled-state tags and fails
validator v2. Produce `<RUN>/R2/SURFACES/HARNESS_capabilities.csv`: **the same rows and the same
CapabilityIDs, in the same order**, with the tags added and each tag verified from code.
**Do not edit the R0 file.**

## Read first

- `<RUN>/R2/SURFACES/_BRIEFS/AREA_CAPABILITY_TASK.md`: the common rules for capability files
  (Notes tags `REACH=…`, `UNREACHED`, `TYPE-ONLY`, `STATE=…`; PostReleaseBasis; reading, git and
  path discipline; validation). Everything there applies, except that you do not re-derive the
  row set.
- `<RUN>/R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` and `HARNESS_notes.md`.
- `<RUN>/R2/_shared/EVIDENCE_PACK/REACHABILITY.csv` (its LEGACY_ONLY class was seeded from the R0
  rows' `LEGACY-IN-PROCESS:` notes and re-verified from imports) and `TOUCHED_PATHS.csv`.

## Output (write only these two files)

- `<RUN>/R2/SURFACES/HARNESS_capabilities.csv`: same header, same 60 rows and IDs. For each row:
  - Keep the R0 Notes text and append the tags, e.g.
    `LEGACY-IN-PROCESS: … | REACH=LEGACY_ONLY; STATE=ENABLED`.
  - Verify reach per row from the code and REACHABILITY.csv (a row whose R0 note says
    LEGACY-IN-PROCESS but whose code is reached from LIVE code is `REACH=LIVE`, and vice versa).
  - Verify STATE from gates in code (flags, env, unmounted UI, retired stubs).
  - Correct any other cell only if code at the frozen basis shows the R0 value is wrong
    (e.g. a wrong path, a missing covering test, a wrong PostReleaseBasis). Keep such changes minimal.
- `<RUN>/R2/SURFACES/HARNESS_notes.md`: sections
  1. Census line exactly `CENSUS rows=N LIVE=a LEGACY_ONLY=b TEST_ONLY=c UNREACHED=d ENABLED=e DISABLED=f`;
  2. Coverage line `COVERAGE covered=X total=Y` against IMPLEMENTATION_SURFACES.csv rows with Area=HARNESS;
  3. **Substance changes:** a table `CapabilityID | Column | R0 value | R2 value | Evidence` for every
     row whose content changed beyond the appended tags (write "none" if none);
  4. Rows where the tag contradicts the R0 `LEGACY-IN-PROCESS:` note or the R0 notes' §3 reading;
  5. Method friction; 6. Effort.

Validate from `<APP_WORK>`:
`python3 <RUN>/_scripts/validate_ledger.py capabilities <RUN>/R2/SURFACES/HARNESS_capabilities.csv`
(errors must be zero). Return ≤ 8 lines: paths (repo-relative), CENSUS and COVERAGE lines, the
count of substance changes, validator RESULT line, `shasum -a 256` of the CSV.
