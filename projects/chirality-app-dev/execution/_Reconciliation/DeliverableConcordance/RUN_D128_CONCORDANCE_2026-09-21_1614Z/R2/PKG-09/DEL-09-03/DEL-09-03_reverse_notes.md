# DEL-09-03 reverse pass (pass 2) notes

The sealed claims SHA-256 is unchanged:
`1ee9158790384861073bd20d3ee3f6aaad7657db72833a9a22892ea8318ae529`.

The capability files were answered in this order: BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE,
SETTINGS, SHELL, WORKSPACE. That is 409 rows: 0 CLAIMED_BY, 34 PARTIAL and 375 NOT_MINE.

## Response policy

DEL-09-03 is a TEST_SUITE deliverable. It owns the tests for eight named behaviour groups, not the behaviour
itself. So a capability is never CLAIMED_BY: the implementing carriers own the behaviour. I answered PARTIAL
where one of my claims makes that capability a test target. Everything else is NOT_MINE, including all shell
UI, Electron, packaging, account and plan capabilities, and the test families that `_STATUS` V3-01 assigns to
their own carriers.

## REACH/STATE differences between the capability files and my ledger

- **CAP-BUILD-005 (`test` script), REACH=TEST_ONLY; my ledger had REACH=LIVE.** Two rows are affected,
  CLM-003 and CLM-009.12. I believe the capability file. The script runs only Vitest over test code. Under the
  brief's reach rule, only the build and packaging entries (build, pack, sign, verify) are live product
  entries, so a verification entry is not one. I have written two errata, on ImplementationEvidence only.
  The Dispositions are unchanged (both rows stay ALIGNED).
- **CAP-RTCONTRACT-022 (event-schema.ts), REACH=LIVE, TYPE-ONLY for live consumers.** The capability file notes
  that the `HARNESS_EVENT_TYPES` value is used only by tests and legacy code. My REACH=LIVE tag on
  `event-schema.ts:44-47` (CLM-009.10, CLM-023, REM-1) is consistent at module level. My substantive point
  rests on the separately cited `delegated-engine-adapter.ts:257-310` (REACH=LIVE), which emits the `codex.*`
  event types. No erratum.
- **HARNESS-030/038/042/043/045/046/047, LEGACY_ONLY and STATE=DISABLED.** This matches my LEGACY_ONLY tags.
- **ROUTES-006/007/011 and the RTCORE rows, LIVE.** These match my tags.

## Census, sealed vs errata-applied

The errata change only ImplementationEvidence REACH tags, so Disposition, ClaimType, HumanDecisionNeeded and
CauseTag counts are the same in both views: 54 rows; STALE_SPECIFICATION 21, ALIGNED 13, NOT_AUDITABLE 6,
PARTIALLY_IMPLEMENTED 5, IMPLEMENTED_DIFFERENTLY 4, AUTHORITY_CONFLICT 2, REMAINING_STATE_MISMATCH 2,
STALE_VERIFICATION 1.

## Coverage gaps (no forward row; for the manager)

- **Retained test of superseded disconnect behaviour.** `routes.test.ts:1270` still expects an SSE reader
  disconnect to cancel the turn. CAP-ROUTES-007 and CAP-HARNESS-024 say the opposite (closing the response
  only unsubscribes). No DEL-09-03 row owns retargeting or retiring this test. This repeats the pass-1 note.
- **Live-path malformed-tail replay test.** The code behind CAP-RTCONTRACT-020 and CAP-RTCORE-017 lacks a
  malformed-line test. The gap is recorded under CLM-005.3 (PARTIAL).
