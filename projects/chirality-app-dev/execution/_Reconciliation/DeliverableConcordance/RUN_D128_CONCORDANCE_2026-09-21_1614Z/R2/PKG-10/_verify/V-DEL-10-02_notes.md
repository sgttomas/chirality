# V-DEL-10-02: verifier shard notes (PKG-10, DEL-10-02)

Frozen basis `00115c719`. Graded against `CONVENTIONS.md`, RUN_BASIS Addenda 1–5 and the shared grading key in `BRIEFS/VERIFIER_BRIEF.md`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 5 | 2 | 0 | 3 |
| a30 | 11 | 8 | 3 | 0 |
| b | 2 | 2 | 0 | 0 |
| c | 1 | 1 | 0 | 0 |
| e | 0 | 0 | 0 | 0 |
| **Total** | **19** | **13** | **3** | **3** |

- **Verdict-field refutations (Addendum 3):** none.
- **Field refutations:** all 3 are on `ImplementationEvidence`, so each is a CORRECTIONS.csv candidate.
- **CONTESTED items:** all 3 are on `Disposition`. None counts as REFUTED.

## (ii) Patterns

1. **Mistyped recomputed PRD hash.**
   - Affected rows: CLM-001 and CLM-004.
   - The rows cite the frozen `docs/PRD.md` as `17ca3f4c...`. The actual value is `17ca3f3c...`, as in `REFERENCE_HASHES.csv` and a recompute.
   - The same typo appears in REGISTER-1, which was not selected. The manager may want to correct all three together.
   - Dispositions are unaffected.
2. **AUTHORITY_CONFLICT on future-scope K-DOMAIN-2 is contestable.**
   - Affected rows: CLM-010.9 and its SEE row CLM-024.
   - The conflict depends on whether D-GOV-43 (no pinning of approval or sandbox policy) undercuts the "path hooks" enforcement column of a clause in CONTRACT §1.10 "Future Scope".
   - The D-GOV-43 tranche `23b3879b3` edited App CONTRACT at K-UNTYPED-1 but left K-DOMAIN-2 unchanged. D-GOV-43's text names approval and sandbox policy, not path hooks.
   - So ACCEPTED_DIVERGENCE (future, gated) is also defensible.
   - The worker disclosed this alternative. If AUTHORITY_CONFLICT stands, R4-Q1 is the right named question, because RB-HOOKS and K-HOOK are unamended for D-GOV-43.
   - DEL-10-01/03/04 likely share the question.
3. **CLM-006 (LOW):** the CONTEXT_CLAIM rule admits both STALE_SPECIFICATION and NOT_AUDITABLE, because the SoW's own P40 note makes the older warning wording dated history.
4. **REACH inherited from a re-export target.**
   - Affected row: REGISTER-4.
   - The facade `frontend/packages/harness-contract/src/domain-profile.ts` is imported only by `frontend/src/__tests__/lib/harness-contract-rollback.test.ts`, so it should be `REACH=TEST_ONLY`, not `LIVE`.
   - For the runtime `contracts/src/harness/domain-profile.ts`, the rows' `REACH=LIVE` matches `REACHABILITY.csv`. The capability file says TEST_ONLY. That difference changes no disposition, because the rows already treat the contract as inert (grading key 3).
5. **Anchors checked with no problems:**
   - line anchors in App PRD, CONTRACT, SPEC, TYPES and PLAN, the decomposition row, both profiles, the registry, the coordinator and the proposal tools;
   - INSP-03 old-REQ mappings;
   - PostReleaseBasis `NO`, since no cited path is in `TOUCHED_PATHS.csv`;
   - SEE targets and their matching Dispositions.

## (iii) Effort

- **Files read:**
  - the unit's claims, notes and reverse files; the rulebook and RUN_BASIS;
  - evidence-pack rows (REFERENCE_HASHES, REACHABILITY, TOUCHED_PATHS, DECISION_HITS, the application map) and the RTCONTRACT capability row;
  - the SoW and the deliverable metadata files;
  - line ranges of 6 governing docs, 2 profiles and 5 code modules; Root AGENTS.md and the SoW standard.
- **Git:** blame on TYPES:668 and CONTRACT:128/150; log/show on 6 commits.
- **Budget:** adequate.
