# V-DEL-09-03 — verifier shard notes (DEL-09-03)

Graded against CONVENTIONS.md, RUN_BASIS §3/§5 and Addenda 1–9, and the PKG-09 shared grading key. Ledger
state per the dispatch STATE note: sealed after Addenda 5, 6 and 8, R4-Q4 and R4-Q5 were briefed, with the
Addendum 9 (R4-Q6) notice applied before sealing. R4-Q6 was therefore graded as in force.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 5 | 4 | 1 | 0 |
| a30 | 12 | 6 | 4 | 2 |
| b | 2 | 2 | 0 | 0 |
| c | 7 | 7 | 0 | 0 |
| e | 2 | 0 | 2 | 0 |
| **Total** | **28** | **19** | **7** | **2** |

- **Verdict fields.** No item is REFUTED on a verdict field (Disposition or reverse Response).
- **CONTESTED on Disposition** (2): CLM-004 and CLM-009.9.
- **REFUTED** (7): all field-level.
  - DirectionEvidence ×3: CLM-001, CLM-007, CLM-021.
  - HumanDecisionNeeded ×2: CLM-017, CLM-023.
  - Errata ImplementationEvidence ×2: CLM-003 and CLM-009.12 (erratum ProposedValue wrong).

## (ii) Patterns

1. **R4-Q6 applied to some K-PERM rows only.** The ledger cites R4-Q6 on CLM-005.8 and CLM-009.9, but
   omits it on two rows whose text also restates unamended K-PERM-1 hard-deny precedence:
   - CLM-017: the Permission check (HDN `NO`);
   - CLM-023: the "Deny paths" principle (HDN `R4-Q5` only).

   On CLM-009.9 the Disposition could equally be AUTHORITY_CONFLICT under §1: D-GOV-43 undercuts K-PERM-1..5
   and K-HOOK-1 without naming them, and that is exactly R4-Q6. Graded CONTESTED.
2. **Errata REACH downgrade conflicts with key 4b.** Both errata change `frontend/package.json:17` (`test`)
   from LIVE to TEST_ONLY, citing CAP-BUILD-005. Key 4b settles this statically:
   - the release script `validate:release-quality` runs `scripts/validate-release-quality-evidence.mjs`;
   - that script invokes `npm run test` unconditionally at lines 416–420.

   The sealed LIVE therefore stands. The CAP-BUILD-005 note (REACH=TEST_ONLY) is the source of the
   disagreement and may need the same correction in the BUILD capability file.
3. **REF-006 direction misattributed.**
   - CLM-001, CLM-007 and CLM-021 explain the stale PRD MATCH with `GOV:D-GOV-43`.
   - The recorded hash 8649ccba is PRD at 23b3879b3, the D-GOV-43 tranche that also refreshed
     `_REFERENCES.md`.
   - The mismatch comes from 9eaddb596 (PR #778), a later edit on the same day.
   - Disposition STALE_SPECIFICATION and CauseTag DOC_HYGIENE hold. The CAUSE2:A2_TOPOLOGY note on CLM-001
     does not.
   - The same pattern probably affects the CONTRACT and SPEC REFERENCE rows (REGISTER-1, not in this shard).
4. **Contested Disposition on CLM-004.** The Conditions table is dispatch-scoped history ("by this run",
   "Initial state was"), so tie-break rule 1 does not clearly apply. Both readings are recorded in the CSV.

Minor, not refuted:
- REM-2 AuthorityTier GOVERNANCE_INVARIANT is generous for an item that restates D-APP-127 and the packaging
  procedure.
- REM-1 UNKNOWN is correct in-bounds: its Depends lie in other packages' folders.

## (iii) Effort

- **Files read:** about 25 in the frozen tree, all read by line range:
  - the SoW, `_STATUS`, `_REFERENCES`, `Dependencies.csv` and MEMORY;
  - App CONTRACT and SPEC §10–11 and §16.1;
  - 12 code and test files.
- **Also read:** the evidence pack (REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES) and 5 capability rows.
- **Git:** read-only `git -C <frozen> log` and `show` for PRD.md history and for the deletion of the
  integration test.
- **Context budget:** not tight.
