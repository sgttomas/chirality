# DEL-09-01 — reverse-pass notes

The sealed ledger is unchanged: SHA-256 `f91122a47b0e5ef98e8b96be7c1467eecc9a39f7973abfd1664c89af897ef56d`. There is no errata file.

`DEL-09-01_reverse.csv` answers 320 capabilities, taken in the manager's order: BUILD 41, ELECTRON 35, HARNESS 60, RTCONTRACT 53, RTCORE 50, SETTINGS 42, WORKSPACE 39. Responses: CLAIMED_BY 2, PARTIAL 4, NOT_MINE 314. All seven validator runs passed with errors=0 and warnings=0.

## Claimed and partial

| Capability | Response | Claim |
|---|---|---|
| CAP-BUILD-025 premerge wrapper | CLAIMED_BY | CLM-009.4. Also covers CLM-009.3/.5/.6 and CLM-018.1-.5. |
| CAP-BUILD-026 Section 8 validator | CLAIMED_BY | CLM-009.8 |
| CAP-BUILD-005 test/typecheck scripts | PARTIAL | CLM-009.2. Required local checks only. |
| CAP-BUILD-007 instruction-root integrity | PARTIAL | CLM-009.2. Required local check only. |
| CAP-BUILD-024 release-quality wrapper | PARTIAL | CLM-013. The D-APP-56 P37 wrapper interest; DEL-09-05 owns the CI workflow. |
| CAP-HARNESS-029 legacy engine registry and stub engine | PARTIAL | CLM-009.8. Section 8's marker-driven checks rely on it. |

## Places where the capability files disagree with my ledger's REACH tags

- **BUILD-024, BUILD-025 and BUILD-026 are tagged `REACH=TEST_ONLY` in the capability file. The ledger tags these scripts `REACH=LIVE`.**
  - I keep LIVE.
  - Each script is invoked by a `frontend/package.json` script: `validate:release-quality`, `harness:validate:premerge` and `harness:validate:section8` (package.json:19, :21, :29).
  - The PKG-09 manager's dispatch note makes such scripts REACH=LIVE as build/CI entries.
  - The capability file applies the product-runtime reach reading instead.
  - Under the brief's rule the ledger is right, so I wrote no erratum.
  - BUILD-026's own note says the validator "exercises LIVE routes but ... carry legacy Agent SDK vocabulary". That matches the ledger's CLM-009.8 finding.
- **HARNESS-029 and BUILD-023 are tagged `REACH=LEGACY_ONLY`.**
  - This agrees with the ledger's position: Section 8's validation markers and stub stream are met only by legacy code, and CLM-009.8 cites R4-Q1.
  - BUILD-023 adds evidence I did not cite. The controlled CI Runtime fixture (`frontend/scripts/controlled-ci-runtime.ts:15-16`) imports the legacy `StubAgentSdkManager` and `LegacyAgentEngineAdapter`. The CI path that produced Section 8 passes therefore ran on legacy code.
  - This strengthens CLM-009.8 and changes no sealed field, so there is no erratum.
- **The capability files say "harness-premerge.yml runs the release-quality wrapper and instruction-root:integrity" (BUILD-007, BUILD-023, BUILD-024).**
  - That describes the repository-root workflow, not the in-root copy at `projects/chirality-app-dev/.github/workflows/harness-premerge.yml` that the ledger read.
  - The in-root copy has no such steps.
  - This supports the ledger's reading that the repo-root chain is the operative one. That chain is OUT_OF_ROOT for this worker.

## Coverage gaps (no forward row; for the manager)

- **CAP-BUILD-023, the controlled CI Runtime fixture.**
  - It is the Runtime that CI binds Section 8 to.
  - It is LEGACY_ONLY, and W3_RETURN §8 reports it broken against the A2 core.
  - No forward row owns its retirement or replacement. It sits between DEL-09-01 (Section 8 preservation) and DEL-09-05 (the CI workflow).
  - I answered NOT_MINE because the CI surface belongs to DEL-09-05. This matches the "Coverage gaps" note in `DEL-09-01_notes.md`.
