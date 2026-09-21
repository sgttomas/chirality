# DEL-07-01 reverse-pass notes (R2, PKG-07)

The sealed forward ledger is `DEL-07-01_claims.csv`, SHA-256
`e3fedfed073b66946e372aaedaa354a190bf34744455ad46879c47478185e93b`. The seal holds: I recomputed the
hash after the reverse pass and it has not changed.

## Responses

The reverse pass covered seven capability files, 322 rows in total, in the order the manager gave:
BUILD 41, ELECTRON 35, HARNESS 60, ROUTES 44, RTCONTRACT 53, RTCORE 50, WORKSPACE 39.

| Response | Rows |
|---|---:|
| CLAIMED_BY | 5 |
| PARTIAL | 17 |
| NOT_MINE | 300 |

**CLAIMED_BY (5 rows)**

| Capability | Owning claim |
|---|---|
| CAP-ELECTRON-006 | CLM-005 |
| CAP-HARNESS-025 | CLM-005 |
| CAP-HARNESS-026 | CLM-004 |
| CAP-HARNESS-045 | CLM-011.5 |
| CAP-ROUTES-026 | CLM-011.11 |

**PARTIAL (17 rows)**

- **The CLM-011.11 reuse gap (7 rows):** ROUTES-001, 027 and 029; RTCORE-009; WORKSPACE-001 and 009.
- **CLM-025, where App routes use several containment models (5 rows):** ELECTRON-023 and 024;
  ROUTES-034 and 035; WORKSPACE-019.
- **The legacy or live mechanisms behind CLM-011.4, .5, .6 and .8:** HARNESS-043, 046 and 047;
  RTCONTRACT-019; RTCORE-028.
- **Runtime registry disjointness (CLM-011.3):** RTCORE-010.

**Excluded as NOT_MINE**

- BUILD-006 and BUILD-007 (packaged instruction-root staging and integrity). CLM-009 puts packaging
  and release integrity out of scope, and `_STATUS.md` Depends gives the packaging checks to
  DEL-08-01.
- The organisation-layer part of SEC-1, SEC-2 and REM-1 has no capability in any file. This matches
  the forward NONE_FOUND.

## Errata

There is no errata file. Nothing found in the reverse pass contradicts a sealed field value.

- **D-APP-98 versus D-APP-100.** The deliverable's `_STATUS.md` REM-1 write locus cites
  "(additive; D-APP-98)". D-APP-98 is the Electron-version authority. D-APP-100 is the
  packaged-daemon instruction-root decision, which D-APP-127 supersedes. The sealed REM-1 row
  already records this in Notes as a probable mis-citation in the deliverable text. No sealed field
  value (LatestDecision `D-APP-127`, HumanDecisionNeeded `D-APP-119`) depends on it, so no erratum
  is needed. Repairing it belongs to the deliverable-text repair of REM-1 (STALE_SPECIFICATION).
- **CLM-025 Notes: an understated count, not an error.** The Notes say App routes use "at least
  three root normalizers". CAP-WORKSPACE-019 shows a fourth: `deliverable-contracts.ts` realpath
  containment. The sealed text says "at least", so it stays true, and I made no erratum.

## REACH and STATE agreement

None of the files disagrees with my ledger. At module level, the pack's `REACHABILITY.csv` also
agrees except in the two places below, and in each the capability file matches the ledger.

- **`session-manager.ts`.** The pack tags the whole module LIVE. CAP-HARNESS-026 tags only
  `assertProjectRootAccessible` LIVE. CAP-HARNESS-037 tags the file-backed session store in the
  same module LEGACY_ONLY and DISABLED. My per-symbol reading agrees with the capability files.
- **`instruction-root.ts`.** The pack tags it LIVE. CAP-HARNESS-025 adds that
  `assertInstructionRootReadable` is LEGACY_ONLY. My ledger cites only
  `resolveInstructionRootPath` and `instructionRootContainsPath` (lines 18-54), so this is
  consistent.
- **Consistent with the ledger's LEGACY_ONLY tags.** HARNESS-043, 045, 046 and 047 are LEGACY_ONLY
  and DISABLED.
- **Consistent with the ledger's LIVE tags.** The following are LIVE and ENABLED, matching my LIVE
  tags and the reading that the live path uses the user-chosen Codex sandbox rather than Chirality
  hooks:
  - ROUTES-026, 027 and 029;
  - WORKSPACE-001, 009 and 019;
  - RTCONTRACT-019;
  - RTCORE-010 and 028;
  - ELECTRON-006.
- **`codex-supervisor.ts` blame.** CAP-RTCORE-028 notes the lines in this file that blame to
  `da95ec194`. My sealed citations (104-110 and 719-728) avoid them, so PostReleaseBasis `NO`
  stands.

## Coverage gaps

The reverse pass found no new forward coverage gap. The notes file already records two SoW sections
that no indexed unit covers: Purpose/OUT-001 and the Output and Evaluation Matrix.
