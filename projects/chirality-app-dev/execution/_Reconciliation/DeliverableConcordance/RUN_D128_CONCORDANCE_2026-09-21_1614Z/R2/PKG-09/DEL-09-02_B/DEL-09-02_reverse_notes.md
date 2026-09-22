# DEL-09-02 — reverse-pass notes (worker B)

## Summary

- **Capability files:** BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE and WORKSPACE, in that
  order. 322 capabilities in total.
- **Responses:** 1 CLAIMED_BY, 17 PARTIAL, 304 NOT_MINE. The reverse validator passes for each of the
  seven files.
- **Seal:** the claims SHA-256 is unchanged at
  `b93c270a66911f33a9a4ba5d74829e7d07d19816a4848f10df145bb4f6fd065c`.

## Response method

- **CLAIMED_BY:** CAP-BUILD-027 (the Section 9 runner and manifest) → `DEL-09-02#CLM-010.1`.
- **PARTIAL on shared validation tooling:**
  - CAP-BUILD-024, the release-quality wrapper: DEL-09-02 owns only its Section 9 leg and policy.
  - CAP-BUILD-025, the premerge orchestrator: DEL-09-02 owns the Section 9 report-only leg and
    Section 8 preservation. The Section 8 orchestration is DEL-09-01's.
- **PARTIAL on capabilities a Section 9 check validates.** The implementation of each belongs to its
  owning package, and DEL-09-02 owns only the validation. The key is the matching RQ row:
  - CAP-HARNESS-025, 030, 031, 032, 038, 043, 045, 047, 048, 050, 053 and 058;
  - CAP-RTCONTRACT-021, 039 and 044.
- **NOT_MINE on live Runtime capabilities.** Several of these match DEL-09-02 requirements in
  substance: CAP-RTCONTRACT-020, CAP-RTCORE-017 (event journal and replay), CAP-RTCORE-029 (native
  child tracking) and CAP-RTCORE-033 (application tools). No Section 9 ID covers any of them, so
  DEL-09-02 does not own them today. The forward ledger records this gap under CLM-010.3, .4, .7 and
  .11 and under R4-Q1.

## Errata (2 rows; no Disposition change)

- **What changes:** the ImplementationEvidence on `DEL-09-02#CLM-010.11` and `DEL-09-02#REM-1`.
- **Why:** the sealed rows cited `core/src/descendant-tracker.ts:35` as `REACH=LIVE`. That is correct
  at module level, but at symbol level `DescendantTracker` has no product consumer, so it is
  TEST_ONLY. This agrees with CAP-RTCORE-047.
- **Replacement:** the live native-child tracking is `CodexSupervisor.childThreads` at
  `daemon/src/codex-supervisor.ts:118`. That line blames to `95364569a`, which is not one of the
  post-release commits, so PostReleaseBasis stays `NO`.

**Census, sealed vs errata-applied:** identical. Both errata change evidence only: every Disposition,
ClaimType, CauseTag and HumanDecisionNeeded value is unchanged. The rows stay
STALE_SPECIFICATION 25, ALIGNED 6, IMPLEMENTED_DIFFERENTLY 6, DOCUMENTED_UNIMPLEMENTED 4,
NOT_AUDITABLE 4, PARTIALLY_IMPLEMENTED 3, STALE_VERIFICATION 1, REMAINING_STATE_MISMATCH 1.

## Disagreement kept without an erratum: reach of the validator scripts

- **What BUILD says:** CAP-BUILD-024, 025 and 027 tag the Section 9, premerge and release-quality
  scripts `REACH=TEST_ONLY`.
- **What the ledger says:** it tags them `REACH=LIVE`. The worker brief's build-script rule counts
  the in-root workflow as an invoking entry. That workflow runs `npm run harness:validate:premerge`,
  which spawns Section 9.
- **Why no erratum:** I left the ledger as it is and flag this for the manager.
  - Under the BUILD reading, CLM-010.1, 010.12 and 010.13 are met by TEST_ONLY code, so they would
    still be ALIGNED at module level.
  - CLM-010.14 and CLM-014.2 already cite R4-Q1.

## Coverage gaps (not expressible as errata)

- **Live Runtime surfaces with no Section 9 ID.** No Section 9 ID covers any of these:
  - the event journal and replay (CAP-RTCORE-017, CAP-RTCONTRACT-020);
  - application tools (CAP-RTCORE-033, CAP-RTCONTRACT-034);
  - Codex notification pass-through and native child tracking (CAP-RTCORE-029);
  - the effective Codex home (CAP-RTCORE-005), which is the live counterpart of settings isolation.

  Whether DEL-09-02 should own validation of these depends on R4-Q1 and R4-Q2.
- **CAP-BUILD-023, the controlled CI Runtime fixture.** It runs on the legacy stub engine, and no
  deliverable row here owns it.
