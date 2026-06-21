# Evidence ADQ-14 - Release-Quality Validation Wrapper And Runbook

## Scope

ADQ-14 adds a runtime-premerge validation wrapper and runbook for PKG-09. This is software validation evidence only. It does not issue a deliverable, publish or distribute a release, authorize signing/notarization/publication, approve professional work, certify, seal, authenticate, accept code compliance, or make a release-readiness claim.

In scope:

- full frontend test and typecheck command aggregation;
- standalone Section 9 policy and summary validation;
- premerge execution or explicit skip reason;
- stable summary-artifact consistency checks;
- runbook instructions for local evidence collection and premerge prerequisites.

Out of scope:

- DMG/package artifact production;
- signing, notarization, publication, or distribution;
- packaged SDK subprocess proof refresh, which remains ADQ-15 scope;
- whole-product secret/network evidence, which remains ADQ-16 scope.

## Implementation

- Added `frontend/scripts/validate-release-quality-evidence.mjs`.
- Added `frontend/package.json` script `validate:release-quality`.
- Added `docs/RELEASE_QUALITY_RUNBOOK.md`.
- Updated `docs/VALIDATION_STRATEGY.md`, `docs/BUILD_AND_RELEASE.md`, `docs/RELEASE_QUALITY_GATES.md`, and `frontend/docs/harness/README.md` to reference the wrapper and generated summary.
- Updated DEL-09-02 and DEL-09-05 local kits to distinguish Section 8 premerge summary, Section 9 summary, release-quality wrapper summary, and instruction-root packaging summary.

## Wrapper Behavior

The wrapper runs from `frontend/`:

- `npm run test -- --testTimeout=15000`;
- `npm run typecheck`;
- `npm run harness:validate:section9`;
- `npm run harness:validate:premerge`, unless `--skip-premerge <reason>` is provided.

It writes `frontend/artifacts/harness/release-quality/latest/summary.json` and validates:

- Section 9 stable summary exists and has consistent `status`, `testCount`, and per-ID `results`;
- Section 8 stable summary exists and contains the required eight IDs when premerge is run;
- the removed legacy Section 8 ID `regression.api_chat_reachability` is absent when premerge is run;
- Section 9 is standalone-blocking for the wrapper while remaining report-only inside premerge.

Generated harness summaries and logs remain ignored derivative evidence artifacts.

## Validation

- `npm run validate:release-quality -- --skip-premerge "No local harness API is running in this evidence-only ADQ-14 wrapper validation."` passed with status `pass_with_skips`.
- The wrapper run executed full Vitest successfully (76 files / 520 tests), `npm run typecheck` successfully, and standalone Section 9 successfully (13 Section 9 IDs).
- Premerge was not run because no local harness API was running for this evidence-only wrapper validation; the skip is recorded in the generated summary and does not satisfy a gate item that explicitly requires a current premerge run.
- Generated wrapper summary check reported `releaseClaim: false`, `summaryConsistency: pass`, and Section 9 policy `{ standaloneSection9IsBlockingForThisWrapper: true, premergeSection9IsReportOnly: true }`.
