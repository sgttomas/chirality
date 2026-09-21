# V-DEL-03-03 verifier notes (DEL-03-03, PKG-03 R2)

Graded against CONVENTIONS.md, including RUN_BASIS Addendum 4 (R4-Q4) and Addendum 5 (the §2.6 tie-break).
Evidence was read at the frozen tree `00115c719`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 6 | 3 | 1 | 2 |
| a30 | 14 | 13 | 0 | 1 |
| b | 4 | 3 | 0 | 1 |
| c | 7 | 7 | 0 | 0 |
| **Total** | **31** | **26** | **1** | **4** |

- **Verdict-field refutations (Addendum 3):** 0 of 31.
- **Field-only refutation:** CLM-005.3 AuthorityTier. The row has `GOVERNANCE_INVARIANT`; the correct value is `PRD`, because the SoW row cites only PRD FR-116 and PRD 9.3.
- **CONTESTED items:**
  - **STATE-2 (Disposition):** STALE_SPECIFICATION, or a snapshot with no defect.
  - **CLM-003.3 (Disposition):** IMPLEMENTED_DIFFERENTLY, or AUTHORITY_CONFLICT.
  - **CLM-003.1 (Disposition):** ALIGNED, or STALE_SPECIFICATION with SEE:CLM-003.4.
  - **CLM-009.6 (HumanDecisionNeeded):** `R4`, or `R4; R4-Q1`.

## (ii) Patterns

1. **The unamended-SPEC-clause structure is handled two ways.** Both cases turn on a SPEC clause that D-GOV-43 did not amend. Neither SPEC 10.3 nor SPEC 10.4 is named in D-GOV-43.
   - At CLM-003.6, and its SEE rows CLM-005.3, CLM-009.6 and CLM-023.3, the worker compared SPEC 10.3 with the amended SPEC 11. It graded AUTHORITY_CONFLICT.
   - At CLM-003.3 it compared SPEC 10.4 with the amended SPEC 17.1. It graded IMPLEMENTED_DIFFERENTLY with R4-Q1, and named AUTHORITY_CONFLICT only as the alternative.
   - Both readings are defensible, so CLM-003.3 is CONTESTED. R3 should treat the pair consistently.
2. **Split rows that defer half of a clause to another row are handled two ways.**
   - CLM-003.1 is the subject row: a compatibility adapter for routes and SSE event names. The worker graded it ALIGNED and pointed to CLM-003.4 in prose.
   - CLM-004.1 has the same routes-plus-SSE-names shape. The worker graded it STALE_SPECIFICATION with `SEE:`.
   - Under MR-4, a prose deferral is not a SEE row, so CLM-003.1 is CONTESTED.
3. **Minor, no verdict effect:**
   - CLM-003.6 cites a verification test file without naming the test case.
   - CLM-003.7 tags only one of its two test paths with REACH; both paths are TEST_ONLY.
   - STATE-1: `_CONTEXT.md` copies the decomposition PKG-03 row (L281) word for word, and that row is also unamended. DIRECTIVE §0 still resolves this in favour of the PRD, so this is not an AUTHORITY_CONFLICT.
4. **Everything else checked out:**
   - All code line anchors were exact at the frozen tree.
   - REACH tags agree with REACHABILITY.csv.
   - PostReleaseBasis NO is correct: no relied-on lines fall in TOUCHED_PATHS ranges.
   - The REFERENCE_HASHES recomputes reproduce, and SEE targets carry the same Disposition.
   - REM-1 MechanicallyUnblocked NO is correct: DEP-03-03-010 is an ACTIVE PREREQUISITE with status TBD.
   - REM-1 REMAINING_STATE_MISMATCH follows tie-break 2(a).

## (iii) Effort

- **Files read:** about 25, including CONVENTIONS, RUN_BASIS, the unit ledger rows (by script), and the deliverable's SoW, _STATUS, _CONTEXT, _REFERENCES, Dependencies, INSP-03 assessment and the two artifacts.
- **Governing sources checked:** SPEC §10.3, §10.4, §11 and §17.1; CONTRACT K-ENGINE-4 and K-EVENT; PRD FR-116 and the PRD PKG-03 row; DIRECTIVE §0; the D-APP-127 record; a grep of the D-GOV-43 records.
- **Code and tests:** about 12 code files, spot-checked by line, and 4 test files, checked by case name.
- **Git and budget:** git use was limited to `log`. The context budget was comfortable.
