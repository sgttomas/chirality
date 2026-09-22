<!-- PACKET
id: P-02
cluster: CL-02
title: What is still unknown after your owner check
question: How should R5 treat rows your testimony confirmed, and the 22 rows still unknown?
recommended: a: look in Root records; b, c: repair text
depends_on: P-03, P-24
decision_type: owner (P-02.a widening of evidence roots, executed by HELP_HUMAN)
tier: mixed
-->
# P-02 — What is still unknown after your owner check

Cluster CL-02 · no named question · draft by TASK D1 for HELP_HUMAN review; not a ruling.

**Question.** Your answers to the 20 owner-check questions are now applied to the rows. What should R5 do with the rows your answers confirmed, and with the 22 rows you could not answer?

- **P-02.a** — 16 rows still unknown about the July 2026 ScopeOfWork conversion checks (OC-20).
- **P-02.b** — 6 rows still unknown about release-evidence records and packaged checks (OC-14, OC-18, OC-19).
- **P-02.c** — 41 rows whose verdict rests on code or on the text itself. Your answers corrected their notes and did not change the verdict.

**Two terms you asked about.** A *build attestation* is a signed, machine-checkable statement of how, and from what, a release file was built. An *SBOM* (software bill of materials) is a published list of every component, with its version, inside the release.

## What we found
- Your answers: OC-01 to OC-07 yes; OC-08 don't know (you did not recognise the terms); OC-09 no; OC-10 to OC-12 yes; OC-13 to OC-20 don't know. For OC-13 onwards you added that the steps were likely done if the instructions called for them; this is recorded as your belief, not a yes. Your testimony is evidence of events, not a ruling on the text (Addendum 13). [owner testimony]
- Applying the answers changed 63 rows. All 63 gained a note, and only 2 verdicts moved: `DEL-09-04#CLM-011.5` (arm64 inspected, OC-10) and `#CLM-011.4` (minimum macOS version inspected, OC-11) went from Unknown to **partly built**. The inspections happened, but the claims require the inspected values to be kept in the verification package, and they are not (`R3/OWNER_CHECK_APPLIED.md`). [run finding]
- **Still unknown, 22 rows**, each now carrying your belief note. 16 of them (OC-20) are VER-001 conversion-check rows. The records of that conversion run are in Root `execution/`, which is outside this run's evidence roots. Some rows show partial positive traces: a validator pass on 2026-07-19, and parity markers in git history (`R3/OWNER_CHECK.md` OC-20; RUNWIDE_CALLS call c). [run finding]
- The other 6: four `DEL-09-05` rows need a requirement-to-evidence matrix, a ten-step CI review or a manual-checklist status record (OC-18). The DEL-09-05 folder holds only the pre-v3 INSP-03 matrix. `DEL-01-03#CLM-017` needs a boundary-copy release review (OC-19). `DOC:BUILDREL#9.5` needs the packaged S-6/S-8 checks, which the 3.0.0-rc.1 build record left to your native verification (OC-14). [run finding]
- **Consequence for repair.** Where the text requires a *kept record* (a matrix, a checklist result, an inspection output), the record is still missing, even where you confirm the event. [run finding]
- The four OC-08 rows are text out of date on other grounds; your OC-09 "no" (macOS arm64 only) agrees with their notes. [owner testimony]
- The hosted release job stops at its first blocking step, before any build (repository-root `.github/workflows/desktop-release-template.yml:39-43`). An optional SBOM script exists (`frontend/package.json` `sbom:generate`) but is not wired into `desktop:dist` or CI (`DEL-09-05#REM-1`). [code]
- **Rows for R4 attention** (`OWNER_CHECK_APPLIED.md`; each verdict rested partly on the absence of an event you now confirm): [run finding]
  - `DEL-09-05#CLM-010.8` (OC-05): you confirm the full check set passed before release. The code finding stands: `desktop:dist` is in no PR gate. R3 had left this row undecided.
  - `DEL-09-01#CLM-009.8` (OC-06): its remaining work says to rerun Section 8, and you confirm a post-re-platform run. The legacy-only marker finding stands.
  - `DEL-09-01#CLM-023` (OC-06): a later run is confirmed, but its summary is not in the tree. The CI-chain part stands.
  - `DEL-09-01#REM-1` (OC-06): its remaining work asks for the run you confirm. The code-based verdict stands.
  - `DEL-09-02#CLM-020.2` (OC-07): you confirm the 16-ID run and its kept summary, but not where the summary is. The CI-retention finding stands.
  - `DEL-09-04#CLM-009.8` (OC-12): you confirm a packaged run with secret and network checks. The code finding stands: the probe proves only `codex --version`. `#CLM-011.8` follows.
  - `DEL-09-05#CLM-016.3` (OC-01): you confirm naming and authorizing both candidates. This bears on the exact-candidate gate G6a; see P-03.

## Affected rows
<!-- COUNTS -->
**63 rows are decided in this packet** (PRIMARY); 0 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-02`.

| Package | Matches (`ALIGNED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Unknown (`UNKNOWN`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT | 3 |  | 6 |  |  |  | 1 | 10 |
| PKG-00 |  |  |  |  |  |  | 2 | 2 |
| PKG-01 |  |  | 1 |  |  |  | 5 | 6 |
| PKG-02 |  |  |  |  |  |  | 5 | 5 |
| PKG-03 |  |  | 1 |  |  |  |  | 1 |
| PKG-05 |  |  |  | 1 |  |  | 2 | 3 |
| PKG-09 |  | 23 | 2 |  | 2 | 1 | 4 | 32 |
| PKG-10 |  |  |  | 1 |  |  | 3 | 4 |
| **Total** | **3** | **23** | **10** | **2** | **2** | **1** | **22** | **63** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-02.a: 16 rows — Unknown 16
- P-02.b: 6 rows — Unknown 6
- P-02.c: 41 rows — Partly built 23, Text out of date 10, Matches 3, Verification out of date 2, To-do list out of step 2, Governing texts disagree 1

<!-- /COUNTS -->
63 rows, split by the rule in `R4/_work/SUBQ/P-02_subq.csv`: (a) unknown with an OC-20 note; (b) unknown otherwise; (c) every other row.

## Options
**For P-02.a (conversion checks):**
**A1. Leave unknown.** *R5 would:* make no change. The rows stay open.
**A2. Look once in the Root records.** HELP_HUMAN widens the evidence roots for these 16 rows only, to read the conversion-wave records in Root `execution/`. Each row is then decided from what is found, and a row with nothing found stays unknown. *R5 would:* repair the rows the lookup decides.
**A3. Rule them historically met.** You rule that the July 2026 conversion checks were done, on your belief. *R5 would:* restate VER-001 in each deliverable as met historically, citing the ruling.

**For P-02.b (release records and packaged checks):**
**B1. Leave unknown and state the gap.** *R5 would:* reword the text so it says no kept record exists, without saying the step did not happen.
**B2. Make the records now.** This is a separate bounded task, run after the ruling, that writes the matrix, checklist status and S-6/S-8 results from today's evidence, or re-runs the checks. *R5 would:* repair the text once the records exist.
**B3. Drop the requirement.** Where D-GOV-43's shorter release procedure no longer asks for a record, restate the text to match. This ties to P-03 and to done-declaration Q-04 (P-24).

**For P-02.c (verdict stands):**
**C1. Confirm.** *R5 would:* repair each row as its verdict says, using your testimony: "rerun" becomes "record the run you confirmed", and "never ran" wording is removed.

## HELP_HUMAN recommendation (draft)
- **P-02.a: A2**, falling back to A1. The positive records probably exist; they are just outside this run's roots, so a bounded look is cheap and settles the rows on evidence rather than on belief.
- **P-02.b: B1 now.** Decide B2 or B3 when P-03 and Q-04 are ruled. Your belief is not a record, and the honest text is "no record kept".
- **P-02.c: C1.**
- This leaves open where the 3.0.1 build and publication records are kept (OC-02, OC-04).

## Who decides
Owner for all three sub-questions. For A2, HELP_HUMAN changes the run basis (the evidence roots) with your agreement. Reading Root records is within the run; changing them is not, and belongs to Root.

## On ruling
The consolidated R4 ruling record (the next free D-APP ID in the register, committed by HELP_HUMAN before any repair) gives one clause per sub-question and names the rows by `PACKET_INDEX.csv` P-02 and `R4/PACKET_SUBQUESTIONS.csv`.
- **A2:** HELP_HUMAN appends a RUN_BASIS addendum widening the roots for the 16 keys. A bounded TASK then records its verdicts through a REMAP_LOG line per row.
- **R5:** package-partitioned tranche managers (PKG-00, 01, 02, 05, 09, 10 and EXT) edit ScopeOfWork, `_STATUS` and document text for the listed rows.
- **B2:** a separate brief, after the ruling.
- **Checks:** R6 backchecks every listed row. No lifecycle transition.

## Risks, contested rows and dependencies
- `DEL-09-05#CLM-010.8` was undecided at R3 (both readings are in the R3 task files); its current value stands.
- Five P-02 rows are also members of P-03, and five are CONTEXT members of P-24. `DEL-09-05#CLM-016.3` and `#CLM-016.6` turn on G6a, so their repair follows P-03.
- B3 depends on P-03 (release posture) and on your handling of Q-04 in P-24.
- 14 rows still carry a `RELEASE_PROCESS_NOT_RUN:` note tag from R2, including OC-08, OC-13 (`DOC:RELIANCE#8`, `DOC:VALSTRAT#4.11`) and OC-14 rows. The tag is a sealed R2 label and does not assert that the event did not happen (Addendum 10). R5 should reword each to "no record".
