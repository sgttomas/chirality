# DEL-04-05 — reverse-pass notes (RUN_D128, R2, PKG-04)

- Sealed forward ledger SHA-256: `06247159ecc67149aa1295cb42d2263a68486ee1569d498dd06d2979abace20d`. It is unchanged after this pass.
- Areas reviewed (7): BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS.
- Capability rows answered: 325, taken from the concatenated input `_reverse_inputs/DEL-04-05_capabilities.csv`.

## 1. Response counts

| Response | Rows |
|---|---:|
| CLAIMED_BY | 5 |
| PARTIAL | 13 |
| NOT_MINE | 307 |

**CLAIMED_BY (5):**

| Capability | Forward row |
|---|---|
| ELECTRON-018 | CLM-009.8 |
| ELECTRON-032 | CLM-009.4 |
| ELECTRON-034 | CLM-009.3 |
| HARNESS-036 | CLM-009.1 |
| SETTINGS-011 | STATE-3 |

**PARTIAL (13):**

| Capability | Forward row |
|---|---|
| ELECTRON-019 | CLM-009.8 |
| BUILD-029 | CLM-009.8 |
| ELECTRON-033 | CLM-009.4 |
| HARNESS-027 | CLM-030 |
| HARNESS-031 | CLM-009.5 |
| HARNESS-033 | CLM-009.6 |
| HARNESS-035 | CLM-009.6 |
| BUILD-028 | CLM-009.2 |
| ROUTES-007 | CLM-009.13 |
| RTCONTRACT-019 | CLM-009.9 |
| RTCONTRACT-046 | STATE-3 |
| RTCORE-022 | STATE-3 |
| SETTINGS-016 | REM-1 |

## 2. Errata (8 rows, all in the ImplementationEvidence field)

**What was wrong.** The forward pass mis-tagged the reach of symbols in `frontend/electron/api-key-storage.ts`.

- The pack's `REACHABILITY.csv` marks the module LIVE. That is only because `api-key-ipc.ts` imports `isProviderCredentialId` (line 45).
- CAP-ELECTRON-034 and a grep of the frozen tree both show that every storage symbol is imported only by `src/__tests__` files. That covers the storage-path helpers, the store/read functions and `SafeStorageCredentialStore`.
- The correct symbol-level tag is therefore `REACH=TEST_ONLY`.
- The sealed ledger used two wrong tags:
  - `REACH=LEGACY_ONLY`, with UNREACHED in Notes, for `SafeStorageCredentialStore`. This is wrong because tests do reach the class.
  - `REACH=LIVE` for the storage-path lines. This is wrong because only line 45 is live.

**Rows corrected:** CLM-003, CLM-005, CLM-009.1, CLM-009.2, CLM-009.3, CLM-027, STATE-1 and STATE-3.

**Effect on dispositions: none.**

- Every affected row already judged the requirement on the live path.
- Those judgements rested on two facts that still hold: the live path has no credential store (a stub in the App-owned composition), and the settings UI is hidden.
- The words "UNREACHED" in the Notes of CLM-003, CLM-009.1, CLM-009.3, STATE-1 and STATE-3 should now read "test-only".
  - Notes is free text, so I did not raise a separate erratum for it.

**Census, sealed versus errata-applied.** The figures are identical for every column that census counts:

| Field | Sealed | Errata applied |
|---|---|---|
| Rows | 63 | 63 |
| Disposition | unchanged | unchanged |
| CauseTag | unchanged | unchanged |
| Confidence | unchanged | unchanged |
| HumanDecisionNeeded | unchanged | unchanged |

The only change is in REACH tags inside the ImplementationEvidence of those 8 rows.

## 3. Coverage gaps

These are items this deliverable delivered that no forward row covers.

- **Authenticated loopback oMLX provider bridge (D-APP-72, `_STATUS.md` History 2026-07-22).**
  - What it delivered:
    - literal-loopback `127.0.0.1` base-URL validation and model discovery (`frontend/src/lib/harness/omlx-provider-config.ts`);
    - isolated `CHIRALITY_OMLX_API_KEY` handoff;
    - typed, redacted oMLX failures.
  - Capabilities involved: CAP-HARNESS-035 (answered PARTIAL → CLM-009.6 for lack of a better key) and part of CAP-HARNESS-034.
  - It is LEGACY_ONLY and DISABLED at the frozen basis.
  - The SoW never gained a requirement for it. The only trace is the `_STATUS` history and the oMLX branch of the credential store (CLM-009.1 covers the Anthropic order only).
  - Suggestion: the manager could add a STATE or REQUIREMENT row in merge, disposition STALE_SPECIFICATION with CauseTag CODEX_SOLE_ENGINE. D-GOV-43 retired local-model residency; Codex model providers replace it.
- **Legacy `chirality:api-key-*` channels (CAP-ELECTRON-033) and the retained provider-network consent no-op surfaces.**
  - These are covered only indirectly. No separate row is needed.

## 4. Capabilities that look owned elsewhere

| Capability | Likely owner |
|---|---|
| API key settings UI and status rendering (CAP-SETTINGS-009/010) | DEL-02-05 |
| Account and consent ports and panels (CAP-SETTINGS-013..015); provider-network consent surfaces (CAP-ROUTES-025, RTCORE-008, RTCONTRACT-011, SETTINGS-039) | DEL-02-05 / Root. Consent is retired under D-GOV-43. |
| IPC sender authorization (CAP-ELECTRON-020); packaged security proof (CAP-BUILD-030) | DEL-09-06 |
| Packaged and live Agent SDK proofs and the error-shape probe (CAP-BUILD-031/032/041) | DEL-04-01 |
| Run-log redaction (CAP-HARNESS-038) and the secret scanner (CAP-BUILD-028, shared) | DEL-05-03 |
| Engine conformance suite (CAP-RTCONTRACT-039) | PKG-03 (see R4-Q2 in CLM-004) |

## 5. Capability-file accuracy observations

- **CAP-ELECTRON-032, CAP-RTCONTRACT-046, CAP-RTCORE-022.** These match the forward STATE-3 finding exactly: the stub at `app-owned-composition.ts:225` produces an "invalid credential status" result through `api-key-ipc.ts`. No disagreement.
- **CAP-ELECTRON-018.** Agrees with CLM-009.8: the allowlist is still Anthropic, and the policy function has no unit test.
  - Not in the capability file: embedded URL credentials to `api.anthropic.com` are not refused. The current K-NET-1 text requires such URLs to fail closed.
- **CAP-BUILD-029.** Its notes say the proof script's default output root resolves into a deliverable folder under `execution/`.
  - I did not verify which folder. If it is DEL-04-05's, that would be a write-locus concern for proof reruns.
- **CAP-HARNESS-036.** Tagged `STATE=DISABLED`. Consistent with the forward pass.
- I found no REACH or STATE tag contradicted by code.

## 6. Effort

- I read the 325 capability titles and the Notes of about 26 candidate rows.
- I ran one frozen-tree grep for the importers of `api-key-storage.ts` and read lines 28–52 of that file.
- No test runs and no builds. The context budget was comfortable.
