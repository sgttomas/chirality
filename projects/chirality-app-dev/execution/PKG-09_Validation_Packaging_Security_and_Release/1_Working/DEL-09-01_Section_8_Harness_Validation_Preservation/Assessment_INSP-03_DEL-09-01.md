# Assessment INSP-03: DEL-09-01 Section 8 Harness Validation Preservation

Deliverable: DEL-09-01
Package: PKG-09 Validation, Packaging, Security, and Release
Date: 2026-06-21
Inspector: WORKING_ITEMS
Lifecycle: CHECKING
Reviewed SHA: `d0766e0f24b923f7925c711fe05e0cf5d28fd1fb`
Spec source: `Specification.md`

## Scope

This assessment inspected the Section 8 harness validation preservation scope only: package-script entrypoints, premerge wrapper behavior, stable Section 8 summary handling, CI preservation, and Section 8 runtime coverage. It did not issue the deliverable and did not run release packaging.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ001 - Expose `harness:validate:section8` and `harness:validate:premerge`. | PASS | `frontend/package.json` scripts expose `harness:validate:section8` and `harness:validate:premerge` at lines 16 and 18. | Runnable script surface exists. |
| REQ002 - Local release-significant checks include test, typecheck, premerge, and instruction-root integrity. | PASS | `frontend/package.json` exposes `test`, `typecheck`, `harness:validate:premerge`, and `instruction-root:integrity` at lines 14, 15, 18, and 24; `docs/VALIDATION_STRATEGY.md` records the same command family. | This assesses command availability and documented command policy, not a fresh full-suite release run. |
| REQ003 - Premerge fails if the Section 8 validator is missing or unreadable. | PASS | `frontend/scripts/validate-harness-premerge.mjs` resolves the Section 8 script and exits on inaccessible/missing script at lines 80-114. | The wrapper fail-fast is implemented. |
| REQ004 - Premerge requires the eight named Section 8 IDs. | PASS | Required IDs are listed in `frontend/scripts/validate-harness-premerge.mjs` lines 8-17 and enforced at lines 148-152; the Section 8 validator declares the same ordered IDs at `frontend/scripts/validate-harness-section8.mjs` lines 21-30. | ID contract is explicit and enforced. |
| REQ005 - Premerge rejects removed legacy ID `regression.api_chat_reachability`. | PASS | Legacy ID constant and rejection check are in `frontend/scripts/validate-harness-premerge.mjs` lines 19 and 154-156. | Removed-ID guard is present. |
| REQ006 - Premerge creates or updates stable Section 8 summary. | PASS | Stable summary path and copy are implemented in `frontend/scripts/validate-harness-premerge.mjs` lines 87-94 and 158-160, and emitted in the wrapper result at lines 190-193. | Current checkout has no fresh `frontend/artifacts/harness/section8/latest/summary.json`; that is an evidence freshness gap, not missing wrapper code. |
| REQ007 - CI runs the wrapper after server readiness and uploads the stable summary. | PARTIAL | `.github/workflows/harness-premerge.yml` installs Node/npm at lines 19-28, preflights scripts at lines 30-31, starts/polls the server at lines 33-49, runs premerge at lines 51-53, and verifies/uploads the Section 8 summary at lines 55-64. | CI preserves the Section 8 wrapper path, but it does not run the full local release-significant command sequence. |
| REQ008 - Section 8 covers server reachability, session CRUD, boot taxonomy, smoke stream, persistence/resume, permissions, interrupt, SDK-native stream, and no legacy parser regression. | PASS | `frontend/scripts/validate-harness-section8.mjs` covers those checks at lines 395-711 and writes normalized summary/status fields at lines 722-772. | Coverage exists in the Section 8 validator. |
| REQ009 - Validation docs do not invent implementation beyond checked sources. | PARTIAL | `frontend/docs/harness/TRACEABILITY.md` maps Section 8 requirements to validators at lines 5-29; source evidence was read directly from scripts and tests. | No separate doc-invention audit artifact exists for this wave. |
| REQ010 - PRD hash mismatch is warning-only. | PASS | This deliverable's `_REFERENCES.md` records REF-006 as warning-limited hash drift; no requirement was failed solely on that basis. | See source-state caveat below. |

## Gap Inventory

| Gap | Severity | Finding | Recommended owner |
|---|---:|---|---|
| Current Section 8 premerge artifact absent | G6 / Medium | The wrapper can write the stable summary, but no current `frontend/artifacts/harness/section8/latest/summary.json` was present in the checkout during this inspection. | Validation tranche |
| CI preserves Section 8 but does not prove the whole local release sequence | G6 / Medium | The workflow runs premerge and uploads the Section 8 summary, but it does not run `npm run test`, `npm run typecheck`, or instruction-root integrity. | Release/CI tranche |
| No independent validation-doc invention audit | Low | Requirement conformance was checked by source review, but no separate generated audit artifact records that docs did not overclaim. | Documentation/validation tranche |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

No dependency rows were marked satisfied or mutated by this assessment. DEL-09-01 still has 10 active dependency rows with `SatisfactionStatus: TBD`; closure remains open until those rows are reviewed under the dependency workflow.

## Forward Development Recommendation

1. Add a CI/release evidence step that runs the full local release-significant validation family or explicitly records why a command is skipped. Type: CI/test. Size: M. Strategic fit: ON-STRATEGY.
2. Preserve the Section 8 stable summary as a review artifact for each premerge/release-quality run. Type: validation evidence. Size: S. Strategic fit: ON-STRATEGY.
3. Add a small validation-doc consistency check that compares the traceability table to the live validator ID set. Type: test/docs. Size: S. Strategic fit: ON-STRATEGY.

## Issuance-Gate-Process Observations

This deliverable is close to issuance-ready on implementation mechanics, but it should not issue from source review alone. The gate needs a current premerge run artifact plus explicit skipped-check notes for any release-significant commands not executed.
