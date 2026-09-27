# Return — ACCCLOSE (WORKING_ITEMS; nodes ACC and M1)

- **PR:** https://github.com/sgttomas/chirality/pull/1028. It is the undertaking's final PR (F1), opened against `main` and not merged. The last checked head is `a1a95aa01`; this return is committed after it.
- **Basis:** `origin/main` `31a90f3e6`. The brief is `briefs/ACCCLOSE_ACCEPTANCE_AND_MEMORY.md` (`facf2974…6ec461`). The run manifest, with source hashes, commands and outputs, is `../../RV1_ACCEPTANCE_RECORD_2026-09-27/MANIFEST.md`.

## Done

- **Review records:** both `_REVIEW.md` files record:
  - the owner's ruling, verbatim;
  - the option-1 content, labelled as HELP_HUMAN's presentation;
  - AC-007 (DEL-00-01) and AC-011 (DEL-00-03) satisfied for the `D-PEC-105` bytes;
  - the finding dispositions, with CU-001 retired as history;
  - the scope limits, and the closure state `ARTIFACT_ACCEPTANCE_COMPLETE / GATE_5_UNENTERED / CHECKING`.
- **Findings CSVs:** in both `Review_Findings.csv` files, the RV1 rows are now `HumanDisposition=ACCEPT_AS_IS` and `Status=RESOLVED`. This follows method Gate 4 step 2: a final disposition sets `RESOLVED`. The CSV has no basis column, so the basis (the owner's ruling) is recorded in `_REVIEW.md`. RF-001 stays MAJOR, and AC-002 is accepted as partly met. Nothing is deferred, and no successor custom item or C-05 line was added.
- **Snapshots:** new acceptance snapshots `REV_DEL-00-01_2026-09-27_1655` and `REV_DEL-00-03_2026-09-27_1658`, each in the five-file form. `_LATEST.md` now points to `_1658`.
- **M1:** one `## Runs` row is appended to each granted MEMORY.md, linking the receipt and `D-PEC-108`.
- **Prior bytes:** all preserved. The only deleted lines are the two review-stage lines (the prior text is quoted in the new sections), the RV1 CSV rows as changed, and the old `_LATEST.md` body.

## Checks

- Strict registers, harness self-check and loop receipts: output byte-identical to `origin/main`. Strict registers exit 1 with 0 errors and 26 warnings; the other two exit 0.
- `git diff --check`: clean.
- Reliance-hold preflight: 22 runs, all `ALLOW`. The register is header-only.
- Accepted hashes: all four reproduce.
- Order disclosure: the CSV edits and the DEL-00-01 `_REVIEW.md` insertion were made in the working tree shortly before the first preflight batch ran. The outcome could not change.

## Review

- **Review 01:** a fresh `pec-reviewer` (opus) returned PASS WITH NOTES, with no blocking findings.
- **Repairs in `a1a95aa01`:** notes 1–3.
  - `_LATEST.md` now names the serialized predecessor `_1655`.
  - The bridge paragraphs now name the acceptance section, and DEL-00-01's adds the AC-007 case.
  - The DEL-00-01 MEMORY row now says "first acceptance of the contract".
- **Notes 4–5:** no repair needed. Note 4 is the preflight order disclosed above. Note 5: RF-001 is now formally `RESOLVED`, so the method's MAJOR precondition for ISSUED is formally met, though no Gate 5 act follows.
- **Backcheck:** the same reviewer's backcheck of `a1a95aa01` had not arrived at hand-back.

## For the caller

- Add `D-PEC-108_D1_REACCEPTANCE_2026-09-27.md`, its register row, the central `RECEIPT.md`, the graph completion and STATUS. The MEMORY links to the receipt and the ruling record resolve once those files exist.
- Get the backcheck verdict and wait for CI on the final head before merging.
