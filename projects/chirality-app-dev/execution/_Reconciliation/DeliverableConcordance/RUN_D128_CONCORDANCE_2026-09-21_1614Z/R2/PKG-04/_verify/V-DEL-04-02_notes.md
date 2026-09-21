# V-DEL-04-02 verifier notes (R2, PKG-04)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 1 | 0 | 1 | 0 |
| n | 10 | 7 | 0 | 3 |
| b | 3 | 3 | 0 | 0 |
| c | 3 | 3 | 0 | 0 |
| e | 6 | 6 | 0 | 0 |
| **Total** | **23** | **19** | **1** | **3** |

Disposition-level refutation: `DEL-04-02#CLM-028` (sealed `IMPLEMENTED_DIFFERENTLY`, correct
`PARTIALLY_IMPLEMENTED`). The unit's own errata already propose this, and the errata rows are
CONFIRMED, so the errata-applied ledger is correct on this point.

## (ii) Systematic patterns

1. **Barrel re-export read as LIVE reach (GRADING_KEY 1).** `REACHABILITY.csv` marks
   `core/src/compatibility-session-policy.ts` LIVE only through the `core/src/index.ts:3` barrel.
   No code in packages, tests, the App or scripts imports or instantiates `CompatibilitySessionPolicy`.
   The sealed rows `CLM-010.1` and `CLM-028` carried LIVE, and for `CLM-028` that wrong reach drove the
   Disposition. The errata correct both rows. Likewise, `runtime-fingerprint.ts` is imported only by a
   test fake, so it is TEST_ONLY and not the pack's LEGACY_ONLY (`CLM-010.10` erratum). The wider
   legacy chain is a different case: `runtime.ts`, `sdk-options-builder.ts`, `turn-engine.ts`,
   `options.ts` and `persona-manager.ts` have no non-test static importer (`runtime.ts` is imported
   only from `__tests__`), and they keep LEGACY_ONLY only because the pack is seeded from
   LEGACY-IN-PROCESS entries. I did not refute that (A0: unreached code takes LEGACY_ONLY). A future
   key revision should say whether a legacy-seeded module that only tests reach is LEGACY_ONLY or
   TEST_ONLY.
2. **Tangential CTX citation for the dropped fallback tiers.** `CLM-003`, `CLM-010.1` and `CLM-028`
   cite `CORPUS_V21_CANDIDATE.md:10` as DirectionEvidence. That line is about corpus role-file
   membership and the role instruction that Runtime supplies. It does not name the removed
   model/tools/maxTurns frontmatter tiers. The explicit record is the `options.ts:23-26` comment from
   commit 9b005c23a, which is not a CONTEXT source. `CLM-021` writes `NONE_FOUND` for the same
   truncation while carrying `CAUSE2:RUNTIME_EXTRACTION`, so the ledger is internally inconsistent.
   Graded CONTESTED: `CLM-003` and `CLM-021`.
3. **The same snapshot fact gets two Dispositions.** REF-006 "MATCH" gives `REMAINING_STATE_MISMATCH`
   in `CLM-001` (MR-8 iv) but `STALE_SPECIFICATION` in `CLM-006` (the CONTEXT_CLAIM rule). The
   rulebook supports both, so `CLM-006` is CONTESTED (§2.3 versus MR-8 iv / GRADING_KEY 11).
4. **Minor findings, not graded (the rows were class c):** `CLM-010.12` has DirectionEvidence
   `GOV:D-APP-60`, but D-APP-60 is the delegation-instrument ruling and does not itself explain why
   REQ-012 still reads TBD. The closure was an agent pass recorded at `_DEPENDENCIES.md:60`, and the
   same row lists `D-APP-60 (context)` as LatestDecision. Its CauseTag `CARRIER_PROPAGATION` is weak
   because REQ-012 is original SoW text, not a propagated note, and the divergence dates from
   2026-07-18 (PRE_V3_DRIFT or DOC_HYGIENE). The `CLM-010.13` VerificationEvidence cites a typecheck
   with no named test case.
5. **CauseTag on CLM-028 after the errata.** The errata establish that the env tier was dropped, not
   relocated. The retained CauseTag `RUNTIME_EXTRACTION` is therefore contestable against
   `CODEX_SOLE_ENGINE`. This is listed in the CorrectReading of CLM-028's class-a row.

## (iii) Capability-file accuracy

- `CAP-HARNESS-019` REACH=LIVE STATE=ENABLED holds (`app/layout.tsx:105` ToolkitProvider;
  `chat-panel.tsx:320` optsPayload).
- `CAP-HARNESS-060` REACH=TEST_ONLY holds. `CAP-RTCORE-048` LEGACY_ONLY UNREACHED holds.
  `CAP-RTCONTRACT-045` LEGACY_ONLY holds.
- No inaccuracy found. `REACHABILITY.csv` is the file with inaccurate module-level LIVE and
  LEGACY_ONLY entries noted in pattern 1.

## (iv) Effort

About 25 file reads or greps against the frozen tree (the SoW, _REFERENCES, _DEPENDENCIES,
INSP-03, harness modules and tests, the Runtime compatibility policy, DIRECTIVE §0 and §2.8, the
SPEC 13.1 preamble, the CTX candidate) and one `blame -L` (codex-supervisor.ts:219 → da95ec194).
The context budget was not tight.
