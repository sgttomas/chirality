# DEL-09-06 — reverse-pass notes (R2, PKG-09 wave 5)

The sealed forward ledger `DEL-09-06_claims.csv` is unchanged. Its SHA-256 is `99e96ff222fe7bbc072be476226d66fb9ffde8979efb6fc6103e21e20c01ea40`.

## Capability files and responses

I answered eight capability files, in the manager's order: BUILD (41), ELECTRON (35), HARNESS (60), ROUTES (44), RTCORE (50), SETTINGS (42), SHELL (45) and WOVEN (43). That is 360 rows.

| Response | Rows |
|---|---:|
| CLAIMED_BY | 7 |
| PARTIAL | 46 |
| NOT_MINE | 307 |

The 7 CLAIMED_BY rows are:

| Capability | Ledger row | Why |
|---|---|---|
| BUILD-028 (secret-evidence scan) | CLM-010.2 | REQ-002's fixture scan |
| BUILD-029 (network egress proof) | CLM-021 | VER-001 |
| BUILD-030 (packaged security proof) | CLM-021 | VER-001, including the D121 matrix |
| ELECTRON-018 (renderer egress allowlist) | CLM-010.5 | REQ-005 |
| ELECTRON-034 (safeStorage store) | CLM-010.3 | REQ-003 |
| HARNESS-027 (configured-key redaction) | CLM-010.2 | REQ-002 |
| RTCORE-026 (turn attachments) | CLM-010.8 | REQ-008, 009 and 010 |

The PARTIAL rows fall into seven groups:

- **Shared checks owned elsewhere.** This deliverable verifies a control whose implementation belongs to the shell, Electron, packaging or Runtime deliverables. Examples are the attachment picker, the draft and attachment preservation helpers, and the sandbox policy.
- **Command family.** These are REQ-014/015 command-family members: `test`, `typecheck`, `instruction-root:integrity`, `desktop:dist`, `validate:release-quality` and `harness:validate:premerge`.
- **SEC-1 controls.** SEC-1 retains the nonce, window, IPC and egress controls and the S0 default-app PDF observation. That covers ELECTRON-012, 014, 015, 016, 020, 024 and 029, ROUTES-035 and SHELL-043.
- **D121.** CLM-014 (AC-001) covers ELECTRON-017 and ROUTES-034.
- **REM-2 boundary.** REM-2 covers ROUTES-012, RTCORE-005, 006 and 030, SETTINGS-002, and SETTINGS-016 (a retired posture).
- **Legacy-only surfaces.** These are cited in R4-Q1 rows: HARNESS-030, 033, 036, 038 and 042.
- **Disabled credential surfaces.** ELECTRON-032 and 033, RTCORE-022, and SETTINGS-009, 010 and 011.

## Reach tags where the capability files and my ledger disagreed

Three tags differed. The brief's rule is: "A script invoked only by a test is REACH=TEST_ONLY". CONVENTIONS §9 defines TEST_ONLY as reached only from tests.

- **BUILD-029 and BUILD-030** (network egress proof, packaged security proof).
  - **Capability file:** TEST_ONLY. **Sealed ledger:** LEGACY_ONLY, noted as UNREACHED.
  - **I believe the capability file.** No release or packaging script chains either script, and they do not serve the legacy harness at run time. Both are imported by their own tests: `run-packaged-security-proof.test.ts` and `run-network-policy-proof.test.ts`.
  - **Errata:** the proof-script tags are corrected in ImplementationEvidence on CLM-016, CLM-020, CLM-021, REM-3 and REM-4, and in Notes on CLM-016, CLM-021 and REM-4. Across all three corrections, 14 rows carry ImplementationEvidence errata: CLM-003, 005, 010.1, 010.3, 012.1, 014, 016, 018, 019, 020, 021, REM-3, REM-4 and STATE-2.
- **BUILD-028** (`scan-secret-evidence.mjs`).
  - **Capability file:** TEST_ONLY, citing a `Secret scan` step in `.github/workflows/harness-premerge.yml`.
  - **I keep LEGACY_ONLY (UNREACHED)** and wrote no erratum.
    - The in-root workflow `projects/chirality-app-dev/.github/workflows/harness-premerge.yml` has no secret-scan step; its only run steps are `npm ci`, the server start/poll, `harness:validate:premerge` and the summary check.
    - The step the capability file cites must be in the repository-root workflow, which is outside the PKG-09 evidence roots.
    - No test imports the script. `contract-pins.manifest.ts` only pins its text.
    - If the owner accepts the repository-root workflow as evidence, the tag becomes LIVE (CI) or TEST_ONLY.
- **ELECTRON-034** (`SafeStorageCredentialStore`, `storeProviderApiKey` and the other storage functions).
  - **Capability file:** TEST_ONLY at symbol level. **Sealed ledger:** LEGACY_ONLY (UNREACHED).
  - **I believe the capability file.** The only importers are tests, and `api-key-ipc.ts` imports only `isProviderCredentialId`.
  - **Errata:** the reach tag is corrected across rows. This also changes CLM-010.3's HumanDecisionNeeded from R4-Q1 to NO:
    - under Addendum 8, TEST_ONLY code does not meet a product claim;
    - no LEGACY_ONLY code stores the key in `safeStorage`;
    - so the evidence trigger for R4-Q1 no longer holds.
  - CLM-010.3's Disposition stays IMPLEMENTED_DIFFERENTLY: the live path uses Codex credential custody.
  - CLM-010.1 keeps R4-Q1. The legacy `readAnthropicApiKey` (`anthropic-agent-sdk-manager.ts:265-272`, LEGACY_ONLY) is still the only product-path code that implements the precedence.

## Gloss correction (erratum)

- **The error.** The sealed ledger glossed `api-key-store.ts:33-45` `getProviderApiKey` as the UI > ANTHROPIC_API_KEY > CHIRALITY_ANTHROPIC_API_KEY precedence. Its only production caller is `getOmlxApiKey` (`api-key-store.ts:60-62`), which is legacy oMLX.
- **The fix.** The Anthropic precedence actually reached on a product path is `readAnthropicApiKey` in `anthropic-agent-sdk-manager.ts:265-272`, which is LEGACY_ONLY. The errata add that citation to CLM-003 and CLM-010.1 and correct the gloss.

## Errata summary and census (sealed vs errata-applied)

There are 20 errata rows:

| Field | Rows |
|---|---:|
| ImplementationEvidence | 14 |
| Notes | 5 |
| HumanDecisionNeeded | 1 |

No errata row changes a Disposition, so the Disposition census is identical before and after errata:

| Measure | Sealed | Errata-applied |
|---|---|---|
| STALE_SPECIFICATION | 21 | 21 |
| ALIGNED | 15 | 15 |
| PARTIALLY_IMPLEMENTED | 11 | 11 |
| IMPLEMENTED_DIFFERENTLY | 5 | 5 |
| NOT_AUDITABLE | 5 | 5 |
| REMAINING_STATE_MISMATCH | 2 | 2 |
| HumanDecisionNeeded R4-Q1 | 5 | 4 (CLM-010.3 changes to NO) |
| HumanDecisionNeeded NO | 51 | 52 |
| HumanDecisionNeeded D-APP-121 | 3 | 3 |

## Coverage gaps found in the reverse pass (not errata)

- **ELECTRON-014/015/016/020.** These cover renderer hardening, navigation containment, the CSP nonce and IPC sender authorization, delivered as V3-01 and V3-04. Only SEC-1's retained-controls sentence covers them. No SoW REQ or AC row exists, which confirms the forward notes' coverage gap. A SoW revision should add them as DEL-09-06 requirements.
- **ELECTRON-029** (update-metadata GET under amended K-NET-1). No DEL-09-06 requirement covers it, so ownership between DEL-02-01 and DEL-09-06 is unclear. The done-declaration's DONE-19 names both. I marked it PARTIAL SEC-1 only.
- **BUILD-012/015/017** (Codex pin, dependency boundary, post-signing verification). These are security-significant packaging checks. I answered NOT_MINE because they belong to the packaging deliverables (DEL-09-04/05). No DEL-09-06 row names them.
