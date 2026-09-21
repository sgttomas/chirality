## §4 Patterns (hand-written by the PKG-10 manager from the shard CSVs and notes)

1. **No verdict-field refutation in the package.** 0 of 98 checks is REFUTED on `Disposition` or a reverse
   `Response`. All 9 REFUTED items are field-level and are in `CORRECTIONS.csv`: ImplementationEvidence 4
   (a wrong line anchor, DEL-10-01#CLM-004.5; a mistyped PRD hash prefix `17ca3f4c…` for `17ca3f3c…`,
   DEL-10-02#CLM-001 and #CLM-004, and the same typo on the unsampled DEL-10-02#REGISTER-1; a facade reach
   tagged LIVE that is TEST_ONLY, DEL-10-02#REGISTER-4), AuthorityTier 2 (TYPES §11 restatements tiered `PRD`,
   DEL-10-04#CLM-010.4 and #CLM-030), Notes 3 (DEL-10-05#CLM-001 and #CLM-007 name the wrong commits for the
   REF-006 PRD change, and the same text sits on unsampled #CLM-012.2, #CLM-013 and #CLM-021; #CLM-015 restates
   "REF-006 is MATCH" without the `SEE:` to REGISTER-1 that tie-break rule 3 requires).
2. **CONTESTED items (18) are all on Disposition** and cluster in three places the rulebook leaves open:
   - *Future-boundary requirements read on the live path.* DEL-10-03#CLM-003.2, DEL-10-05#CLM-009.1 and #CLM-009.3,
     DEL-10-01#CLM-022.2: PARTIALLY_IMPLEMENTED (the present-tense GOVERNING clause, e.g. K-DOMAIN-2, is not
     enforced on the live path) against ALIGNED (the SoW and PRD §8.17 keep the enforcement surface future, and
     the documentary requirement is met).
   - *STALE_SPECIFICATION under tie-break rule 1 against the recorded verdict.* DEL-10-01#CLM-002, #CLM-004.1 and
     #REM-2; DEL-10-02#CLM-006; DEL-10-03#CLM-010.10; DEL-10-04#CLM-004.1, #CLM-004.4 and #CLM-006;
     DEL-10-05#STATE-2 and #STATE-3. Text that states a present fact ("tools live", "staged read-only boundary",
     "not current implementation", "TBD") admits both a STALE_SPECIFICATION reading and the worker's
     PARTIALLY_IMPLEMENTED / ALIGNED / NOT_AUDITABLE reading. All five workers received the Addendum 5 tie-break
     before sealing, so this is residual ambiguity in the rule, not non-application.
   - *AUTHORITY_CONFLICT (R4-Q1) against ACCEPTED_DIVERGENCE / ALIGNED.* DEL-10-02#CLM-010.9 and #CLM-024 (K-DOMAIN-2
     names path hooks; D-GOV-43 names approval and sandbox policy, not path hooks); DEL-10-04#CLM-016.1 (PEC fixture
     ownership against D-APP-58 / SPEC §18, or "owns" read as accountability under D-APP-70 §9); DEL-10-04#CLM-004.6
     (an OpenPipeStress descriptor in LIVE-mapped `runtime-contracts`, authorized by D-APP-50).
3. **Module map versus symbol-level reach.** Four reverse notes (DEL-10-02, 03, 04, 05) report that
   `RTCONTRACT_capabilities.csv` tags `packages/contracts/src/harness/domain-profile.ts` and `operation-proposal.ts`
   TEST_ONLY (no non-test consumer), while the pack's `REACHABILITY.csv` maps them LIVE (exported through
   `@chirality/runtime-*`). Workers followed the pack as the rulebook requires; verifiers confirmed no Disposition
   turns on it (grading key 3), except the contested DEL-10-04#CLM-004.6.
4. **Evidence-root boundary.** The DEL-10-01 worker self-reported reading parity evidence in the Root repository's
   top-level `execution/` tree for DEL-10-01#CLM-022.2 (VER-001), outside RUN_BASIS §3. The verifier graded the row
   on in-root evidence only: CONTESTED between ALIGNED and PARTIALLY_IMPLEMENTED (only the matrix half of VER-001 is
   evidenced in the roots; no parity report exists), and the out-of-root citation should be dropped by R3. Later
   dispatch prompts named the Root `execution/` tree explicitly as out of bounds; no other worker or shard reports
   crossing it.
5. **Coverage gap reported in reverse notes (not an erratum).** DEL-10-03's D-APP-52 live LLM demo (CAP-BUILD-040,
   recorded only in its `_STATUS` history and `Evidence_DAPP52_LIVE_LLM_DEMO_2026-07-18.md`) has no forward row;
   DEL-10-04 answers CAP-BUILD-040 PARTIAL under D-APP-70 §9.
6. **Rules applied correctly.** Addendum 6 (R4-Q1 subject test) is applied correctly on DEL-10-05#CLM-004.1 and
   #CLM-009.7 (`R4-Q1`, `ALSO_MODULE:ALIGNED`). DEL-10-04's one erratum (REACH tag LEGACY_ONLY → TEST_ONLY for
   `pec-scratch-server.mjs`) is CONFIRMED. All 7 class `c` capability responses checked are CONFIRMED.

## §5 Rerun decisions

- Structural: every ledger, reverse and errata file passes with 0 errors and 0 warnings (§1).
- Verdict-field threshold (RUN_BASIS Addendum 3): 0.0% for every ledger. **No rerun was dispatched**; every first
  attempt is the ledger of record.
