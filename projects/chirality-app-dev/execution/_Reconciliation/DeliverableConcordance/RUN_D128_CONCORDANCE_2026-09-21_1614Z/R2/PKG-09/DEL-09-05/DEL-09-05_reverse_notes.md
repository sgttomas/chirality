# DEL-09-05 reverse-pass notes (pass 2, merged deliverable)

Written by the P1 worker, which answers for the merged ledger `DEL-09-05_claims.csv` (70 rows, sealed, SHA-256 `3038765c…c2d`).

Capability files, in order:
1. BUILD (41)
2. ELECTRON (35)
3. HARNESS (60)
4. SETTINGS (42)
5. WORKSPACE (39)

That is 217 rows in total.

## Responses

- CLAIMED_BY 4:
  - BUILD-018 → REM-3
  - BUILD-019 → REM-1
  - BUILD-024 → CLM-010.1
  - BUILD-025 → CLM-010.5
- PARTIAL 15, all BUILD or ELECTRON:
  - release-verification checks whose implementation is owned by DEL-09-04 (packaging and instruction root) or DEL-09-06 (security proofs);
  - the signing policy (CLM-010.7);
  - the post-signing verification (REM-2);
  - the Codex executable and pin (SEC-1);
  - the folder picker (the manual-checklist item on CLM-010.6).
- NOT_MINE 198: every HARNESS, SETTINGS and WORKSPACE capability and the rest of BUILD and ELECTRON. DEL-09-05 owns CI and release verification, not product behaviour. The HINTS matches in those areas are generic tokens.

## Errata and census

Three Notes errata add `SEE:DEL-09-05#REGISTER-51` to CLM-001, CLM-006 and CLM-014. All three restate the `_REFERENCES.md` MATCH hash as current. CLM-008 already has `SEE:` pointing to CLM-001.

| Figure | Sealed | Errata-applied |
|---|---|---|
| Rows | 70 | 70 |
| STALE_SPECIFICATION | 25 | 25 |
| ALIGNED | 17 | 17 |
| PARTIALLY_IMPLEMENTED | 10 | 10 |
| NOT_AUDITABLE | 7 | 7 |
| REMAINING_STATE_MISMATCH | 6 | 6 |
| DOCUMENTED_UNIMPLEMENTED | 3 | 3 |
| AUTHORITY_CONFLICT | 2 | 2 |
| SEE rows | 7 | 10 |

No Disposition changes.

## REACH differences between the capability file and the ledger (build scripts)

- **Release-quality wrapper and premerge orchestrator** (`validate-release-quality-evidence.mjs`, `validate-harness-premerge.mjs`).
  - BUILD-024 and BUILD-025 tag them TEST_ONLY. The ledger (CLM-007, CLM-010.1) tags them LIVE.
  - I keep LIVE. Under the brief, a build or packaging script is LIVE when a package.json release script invokes it in the default path. `validate:release-quality` (package.json:29) is that release script, and it imports the premerge orchestrator.
  - TEST_ONLY is reserved for a script invoked only by a test. These scripts are invoked by npm and CI, not by tests.
  - No erratum.
- **Manual proof scripts** (`scan-secret-evidence.mjs`, `run-network-policy-proof.mjs`).
  - BUILD-028 and BUILD-029 tag them TEST_ONLY. The ledger (CLM-010.9, .10, .15) tags them LIVE, with the text "manual; not chained from desktop:dist or CI".
  - Neither label fits the brief exactly. They are package.json `proof:*` entries, not release or packaging defaults, so under the brief they are "not live". The A0 vocabulary would then give LEGACY_ONLY with UNREACHED, not TEST_ONLY.
  - LEGACY_ONLY would wrongly trigger the R3 R4-Q1 script. I therefore file no erratum.
  - Proposal: R3 reads these as `LIVE (manual entry)`. The capability-file tag is not right under the brief either.
- **Everything else** (signing hook DISABLED_BY_DEFAULT, verify-codex-pin, version identity, SBOM) matches the capability file.

## Cross-check findings (no erratum)

1. **Possible secret-scan step in repo-root CI.**
   - BUILD-028 says the premerge workflow has a `Secret scan` step. That can only be the repository-root file: the in-root `projects/chirality-app-dev/.github/workflows/harness-premerge.yml` has no such step.
   - CLM-010.9's gloss "not chained from … CI" may therefore be wrong for the executing workflow. I cannot verify it: the file is OUT_OF_ROOT (`.github/workflows/harness-premerge.yml`), and the in-root contract pins do not pin a secret-scan step.
   - The row's Disposition (PARTIALLY_IMPLEMENTED) holds either way, because the scanner patterns are Anthropic-only.
   - Flagged for the verifier.
2. **The K-RELEASE-1 target question gets different Dispositions in the two parts.**
   - P1 CLM-010.7 and STATE-1 are STALE_SPECIFICATION at LOW confidence, with AUTHORITY_CONFLICT recorded as the alternative.
   - P2 CLM-026 is AUTHORITY_CONFLICT.
   - Same question, in both directions, for G6a:
     - P1 CLM-016.3 is AUTHORITY_CONFLICT (R4): the decomposition row keeps G6a, and D-APP-127 does not name it.
     - P2 REGISTER-52 is STALE_SPECIFICATION: it treats G6a as retired on the strength of `_STATUS.md`.
   - Both pairs turn on done-declaration Q-02. I propose that R3 cluster them under a single owner question instead of reconciling by errata. The sealed P1 verdicts stand.
3. **BUILD-016 says no notarization step exists anywhere in the area.** This agrees with CLM-010.7 and with REM-2: notarization is an owner act in PACKAGING_PROCEDURE.

## Coverage gaps (missing forward rows; not errata)

- **App update checker (ELECTRON-029).** Update-metadata GETs are an enumerated K-NET-1 transport. No DEL-09-05 row owns verifying them in the network-scope inspection. CLM-010.10 mentions this only in its RemainingWork; I answered NOT_MINE.
- **Electron fuses (BUILD-010) and entitlements.** CLM-016.2 cites them as runbook topics only. No row owns verifying fuses or entitlements on the packaged candidate. This is probably DEL-09-04 scope.

## Seal check

- P1 claims `b69fe238…99da`: unchanged.
- Merged claims `3038765c…c2d`: unchanged.
