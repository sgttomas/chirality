# DEL-09-02 reverse notes (worker A, pass 2)

## Inputs and results

- **Capability files, in this order:** BUILD (41), ELECTRON (35), HARNESS (60), ROUTES (44), RTCONTRACT (53),
  RTCORE (50) and WORKSPACE (39), 322 rows in all.
- **Responses:** 1 CLAIMED_BY, 2 PARTIAL, 319 NOT_MINE.
  - CAP-BUILD-027 (the Section 9 runner and manifest) is CLAIMED_BY CLM-010.1.
  - CAP-BUILD-025 (the premerge orchestrator) is PARTIAL to CLM-010.12. DEL-09-02 owns only the Section 9 report-only step and the ordering that runs Section 8 first; the Section 8 work belongs to DEL-09-01.
  - CAP-BUILD-024 (the release-quality wrapper) is PARTIAL to CLM-010.13. DEL-09-02 owns only its Section 9 summary and manifest check and `section9Policy`.
  - The HARNESS modules exercised by the Section 9 fixtures are NOT_MINE. They are implementation surfaces owned by feature deliverables, and CLM-009 excludes feature implementation.
- **Validators:** the reverse check passes for each of the 7 files and the errata check passes, all with 0 errors and 0 warnings.
- **Seal:** the claims SHA-256 is unchanged, `3fa55fc71056ae01311b84316dc61015a065f6c4efec17251441c2ed8ba65cc7`.

## Errata (6 rows; no verdict field changed)

- **CLM-010.2 and CLM-010.10 (ImplementationEvidence).** The Runtime `engine-conformance.ts` suite is reached only through the
  contracts barrel and has no product consumer. Its tag changes from REACH=LIVE to REACH=TEST_ONLY
  (CAP-RTCONTRACT-039). This makes the "no Codex conformance" verdicts stronger.
- **CLM-010.11 and REM-1 (ImplementationEvidence and VerificationEvidence).** `core/src/descendant-tracker.ts` is TEST_ONLY and
  DISABLED (CAP-RTCORE-047). The live native child-thread tracking is in `daemon/src/codex-supervisor.ts` (`childThreads`,
  CAP-RTCORE-029), so the errata re-point the citation and its test.
- **Census.** The sealed and errata-applied figures are identical, because no Disposition changed: STALE_SPECIFICATION 23, ALIGNED 9,
  NOT_AUDITABLE 5, DOCUMENTED_UNIMPLEMENTED 4, IMPLEMENTED_DIFFERENTLY 4, PARTIALLY_IMPLEMENTED 4, AUTHORITY_CONFLICT 2,
  REMAINING_STATE_MISMATCH 2.

## Disagreements recorded, not corrected

- **REACH for the Section 9 scripts.** BUILD-024, 025 and 027 tag the Section 9, premerge and release-quality scripts REACH=TEST_ONLY.
  The forward ledger tags them REACH=LIVE, following the PKG-09 brief's rule that a script is live when the in-root workflow invokes
  it in the default path: `harness-premerge.yml:51-53` runs `harness:validate:premerge`, which runs Section 9. I left this unchanged
  for the manager or verifier to settle. Either tag leaves every verdict as it is, because the validated modules are LEGACY_ONLY either way.
- **EntryPoints in the capability file.** CAP-BUILD-023 and CAP-BUILD-024 list `.github/workflows/harness-premerge.yml` as an EntryPoint,
  including a "Release-quality wrapper" step. The in-root workflow at the frozen basis (71 lines) has no such step and no
  controlled-CI-runtime step. Those EntryPoints probably come from the repository-root workflow, which is outside the PKG-09 evidence roots
  and was not read.

## Coverage gaps (for the manager)

- No capability row corresponds to a Section 9 ID for the live Codex/Runtime path, which agrees with the forward coverage gap.
  The live replay (RTCORE-017, RTCONTRACT-020), notification pass-through and child threads (RTCORE-029), and Codex policy
  mapping (RTCONTRACT-019) each have Runtime tests, but none is registered in the Section 9 manifest. It remains open whether
  DEL-09-02 (a new Remaining item) or R4-Q1 and R4-Q2 should own this.
