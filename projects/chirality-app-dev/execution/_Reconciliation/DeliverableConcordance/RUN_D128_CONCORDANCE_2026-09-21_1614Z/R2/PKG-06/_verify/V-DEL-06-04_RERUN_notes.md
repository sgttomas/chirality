# V-DEL-06-04_RERUN: verifier notes

Unit `DEL-06-04_RERUN` (DEL-06-04). Graded against `CONVENTIONS.md` and the PKG-06 shared grading key, using the frozen tree at `00115c719`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (AUTHORITY_CONFLICT) | 18 | 17 | 1 | 0 |
| a30 (30% sample) | 13 | 9 | 0 | 4 |
| b (ALIGNED sample) | 1 | 1 | 0 | 0 |
| c (reverse) | 3 | 3 | 0 | 0 |
| **Total** | **35** | **30** | **1** | **4** |

Every line anchor I opened matched its content at the frozen basis. The only drift was 1 line (`delegated.ts:321-331` against the function at 322-331), which is immaterial. Every REACH tag matched `REACHABILITY.csv`. Every cited test case name exists. `codex-supervisor.ts` is on `TOUCHED_PATHS.csv`, but `git blame -L` on 104-110, 700-704 and 719-728 shows none of the four post-release commits, so `PostReleaseBasis = NO` holds.

## (ii) Patterns

1. **The K-clause AUTHORITY_CONFLICT + R4-Q1 cluster is sound.** Examples: CLM-003, CLM-009.1-.7, CLM-009.13, CLM-018 and CLM-030.
   - K-PATH-2/3, K-ROOT-2, K-HOOK-1, K-PERM-1 and K-MCP-1 (CONTRACT.md:52, 90, 98-101) and SPEC 15.2 are engine-neutral and unamended.
   - D-GOV-43 does not name them.
   - On the live path, agent writes are bounded only by the user-chosen Codex sandbox and approval policy.
   - R4-Q1 is the named question for exactly these clauses.
   - Where the text is Claude-SDK-specific (SPEC 15.1 "First-Adapter Mapping"), the worker correctly used IMPLEMENTED_DIFFERENTLY instead (CLM-004.2).
2. **Register and hash lag was classed STALE_SPECIFICATION where grading key 5 admits both readings.** Graded CONTESTED:
   - CLM-001 and CLM-004.1: REF-006 "is MATCH". The CLM-001 note is dated 2026-07-12, so MR-8 iv / register-lag also fits.
   - CLM-004.7: the sentence is literally true of `_DEPENDENCIES.md`; the defect is lag behind the `Dependencies.csv` mirror.
3. **One wrong AUTHORITY_CONFLICT: STATE-2.** Graded REFUTED.
   - Why the Disposition is wrong: the "daemon conformance" wording comes from the decomposition, which ranks 7 in DIRECTIVE §0. CONTRACT and SPEC rank higher and were amended under D-GOV-43 to the App-owned Runtime service, so the authority order resolves the tension and AUTHORITY_CONFLICT does not apply.
   - AuthorityTier should be LOCAL_DESIGN, because the row restates the decomposition.
   - If an owner question is kept, SOW-057's fail-closed hook conformance points to R4-Q1 rather than plain R4.
4. **One CauseTag contest: CLM-004.5.** The now-false part, "scaffold must be classified", was resolved on 2026-06-14 (`54bd252c4`), which is PRE_V3_DRIFT. The row chose CODEX_SOLE_ENGINE as the primary tag and carries PRE_V3_DRIFT as CAUSE2.
5. **Minor, no verdict change: CLM-017.** The notes treat the HASH_MISMATCH-tracking step as closed by ADQ-11. At the frozen basis, however, REF-006 again fails to reproduce (`REFERENCE_HASHES.csv` Match=NO).

## (iii) Effort

- **Sources read:**
  - the ledger rows for the 35 items, by script;
  - the rulebook, RUN_BASIS and the evidence pack;
  - about 20 code files, as line ranges;
  - SoW, _CONTEXT, _REFERENCES, _DEPENDENCIES and Dependencies.csv;
  - CONTRACT, SPEC and DIRECTIVE headers;
  - the D-APP-43, D-APP-70 and D-APP-127 rulings;
  - three capability rows.
- **Git:** 3 blame ranges and 2 log queries, all read-only against the frozen tree.
- **Context budget:** moderate, not tight.
