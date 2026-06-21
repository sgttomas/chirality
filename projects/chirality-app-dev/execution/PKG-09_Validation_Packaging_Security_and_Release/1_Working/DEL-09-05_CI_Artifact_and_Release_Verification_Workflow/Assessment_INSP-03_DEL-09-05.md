# Assessment INSP-03: DEL-09-05 CI Artifact and Release Verification Workflow

Deliverable: DEL-09-05
Package: PKG-09 Validation, Packaging, Security, and Release
Date: 2026-06-21
Inspector: WORKING_ITEMS
Lifecycle: CHECKING
Reviewed SHA: `d0766e0f24b923f7925c711fe05e0cf5d28fd1fb`
Spec source: `Specification.md`

## Scope

This assessment inspected the CI premerge workflow, stable upload behavior, local validation command sequence, release verification checklist expectations, secret/network evidence expectations, and macOS arm64 unsigned DMG target. It did not create a release, run `desktop:dist`, or inspect CI logs from a live workflow run.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ001 - Local sequence includes test, typecheck, premerge, and instruction-root integrity. | PARTIAL | `frontend/package.json` exposes those scripts at lines 14, 15, 18, and 24; `docs/VALIDATION_STRATEGY.md` and `docs/BUILD_AND_RELEASE.md` document the validation command surface. | The sequence is documented and runnable, but not enforced as one local wrapper. |
| REQ002 - Packaging check includes `desktop:dist`. | PASS | `frontend/package.json` exposes `desktop:dist` at line 27; `docs/BUILD_AND_RELEASE.md` names desktop distribution in release command policy. | Script exists; current artifact production was not performed. |
| REQ003 - Expected outputs include DMG, app bundle, and instruction-root summary. | FAIL | Direct artifact check found no current DMG, no current app bundle, and no current instruction-root summary artifact in the expected output locations. | This is an evidence failure for release verification, not necessarily a packaging-code failure. |
| REQ004 - CI checks out repo, uses Node 20, runs npm ci, verifies assets/preflight, starts/polls server, runs premerge, verifies summary, uploads summary. | PARTIAL | `.github/workflows/harness-premerge.yml` checks out repo and uses Node 20/npm ci at lines 19-28, preflights scripts at lines 30-31, starts/polls the Next server at lines 33-49, runs premerge at lines 51-53, and verifies/uploads summary at lines 55-64. | It does not run `npm run test`, `npm run typecheck`, or `instruction-root:integrity`, and it does not verify instruction-root assets before premerge. |
| REQ005 - Stable summary path for validation review is instruction-root integrity summary unless governed update. | FAIL | The CI workflow verifies/uploads `frontend/artifacts/harness/section8/latest/summary.json` at lines 55-64, while the spec names `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. | Spec/workflow conflict needs governance or implementation correction. |
| REQ006 - Manual DMG release verification checks architecture, OS, signing, instruction-root assets, working-root selector, network guardrails, SDK startup, unpacked SDK, transcript storage/mirroring. | PARTIAL | `docs/RELEASE_QUALITY_GATES.md` and `docs/BUILD_AND_RELEASE.md` describe release-quality checks; packaging/security scripts cover subsets. | No single manual DMG checklist artifact or completed run record was found. |
| REQ007 - Current release target constraints are explicit. | PASS | `frontend/package.json` lines 90-99 and docs define macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG as current target. | Target is bounded. |
| REQ008 - Release-significant changes pass local checks before acceptance. | PARTIAL | Validation docs name required local checks; no automated gate enforces the whole set for this assessment-only wave. | Needs a wrapper or checklist artifact for acceptance. |
| REQ009 - No API keys/secrets in evidence. | PARTIAL | Live packaged proof tests assert key material is absent from stdout/stderr/summary at `frontend/src/__tests__/scripts/run-live-packaged-agent-sdk-read-tool-proof.test.ts` lines 142-204. | No current CI log or release-record secret scan was available. |
| REQ010 - Outbound network loopback + Anthropic only. | PARTIAL | `frontend/scripts/run-network-policy-proof.mjs` classifies loopback/Anthropic and fails non-allowlisted traffic at lines 148-167 and 670-885. | No current CI/release network-proof artifact was present. |
| REQ011 - No automated professional approval, code compliance, external validation, or solver ownership claims. | PASS | Release/validation docs frame these checks as product/runtime validation, not professional or external approval. | No overclaim was found in inspected release docs. |
| REQ012 - GitHub Actions workflow exists because PRD says GitHub workflow; exact path TBD. | PASS | `.github/workflows/harness-premerge.yml` exists and is the active CI workflow path. | Path is concrete now. |
| REQ013 - Evidence maps each requirement to artifact/checklist/TBD. | PARTIAL | This assessment maps current evidence and TBDs; no product-owned release verification manifest exists yet. | The assessment is not a substitute for release workflow evidence. |
| REQ014 - CI review evidence shows ten PRD steps present/absent/TBD. | PARTIAL | Workflow source review identified present and absent steps. | No standalone CI review artifact with ten-step checklist was found. |
| REQ015 - Secret/network inspection covers CI logs, release records, and packaged verification. | PARTIAL | Redaction and network proof scripts exist, but no CI log/release-record packaged verification scan was present. | Needs run evidence before issuance. |

## Gap Inventory

| Gap | Severity | Finding | Recommended owner |
|---|---:|---|---|
| CI workflow omits full release-significant command sequence | G6 / High | GitHub workflow runs premerge only; it omits `test`, `typecheck`, and instruction-root integrity. | CI/release tranche |
| Stable summary path conflict | G6 / High | The spec names instruction-root integrity summary, while CI uploads Section 8 summary. | Governance plus CI implementation |
| No DMG/app/integrity artifacts current | High | Expected release-verification outputs are absent. | Packaging validation tranche |
| No manual DMG release checklist artifact | Medium | Required manual checks are scattered across docs/scripts but not captured as a checklist/run record. | Release docs tranche |
| No current CI/release secret and network evidence | Medium | Proof scripts exist, but current CI logs/release records were not inspected. | Security validation tranche |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

No dependency rows were marked satisfied or mutated by this assessment. DEL-09-05 still has 14 active dependency rows with `SatisfactionStatus: TBD`; closure remains open.

## Forward Development Recommendation

1. Update CI or add a release-validation wrapper so test, typecheck, premerge, instruction-root integrity, and artifact upload are run or explicitly skipped with reasons. Type: CI. Size: M. Strategic fit: ON-STRATEGY.
2. Resolve the summary-path conflict between Section 8 premerge summary and instruction-root integrity summary. Type: governance/CI reconciliation. Size: S. Strategic fit: ON-STRATEGY.
3. Add a manual DMG release verification checklist artifact tied to produced DMG/app paths and security proof summaries. Type: release docs. Size: M. Strategic fit: ON-STRATEGY.
4. Add secret/network scan steps for CI logs, release records, and packaged validation summaries. Type: security validation. Size: M. Strategic fit: ON-STRATEGY.

## Issuance-Gate-Process Observations

This deliverable is not issuance-ready. The gap is not mostly source availability; it is missing current release-run evidence and a conflict between required and uploaded summary artifacts.
