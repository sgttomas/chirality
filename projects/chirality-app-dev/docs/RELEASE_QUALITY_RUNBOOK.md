# RELEASE QUALITY RUNBOOK - Chirality App Dev

**Status:** Draft validation runbook
**Date:** 2026-06-21
**Applies to:** PKG-09 runtime-premerge evidence collection and local release-quality review

## 1. Purpose

This runbook gives a repeatable way to collect runtime-premerge software validation evidence. It complements `docs/VALIDATION_STRATEGY.md`, `docs/BUILD_AND_RELEASE.md`, and `docs/RELEASE_QUALITY_GATES.md`.

The runbook does not publish a release, issue a deliverable, authorize distribution, approve professional work, certify, seal, authenticate, notarize, or accept code compliance.

## 2. Runtime-Premerge Wrapper

Run from `frontend/`:

```bash
npm run validate:release-quality
```

The wrapper runs:

- full Vitest suite: `npm run test -- --testTimeout=15000`;
- TypeScript checks: `npm run typecheck`;
- standalone Section 9 runtime-ID validation: `npm run harness:validate:section9`;
- harness premerge validation: `npm run harness:validate:premerge`, unless explicitly skipped with reason.

It writes `frontend/artifacts/harness/release-quality/latest/summary.json`. That summary records command outcomes, summary-consistency checks, Section 9 policy, generated artifact paths, skipped checks, and no-release-claim boundaries.

## 3. Premerge Prerequisite

`npm run harness:validate:premerge` requires a reachable local harness API. Before running the wrapper without a skip:

1. Stop any unrelated local dev server before build/package/premerge work.
2. Start the harness API on `HARNESS_BASE_URL` (default `http://127.0.0.1:3000`).
3. Set `HARNESS_PROJECT_ROOT` when the default example project is not the intended workroot.
4. Confirm local provider/key prerequisites if the selected harness path needs them.

If premerge cannot be run in the current environment, the wrapper may be run with an explicit skip reason:

```bash
npm run validate:release-quality -- --skip-premerge "No local harness API is running in this evidence-only docs tranche."
```

The command exits successfully only if all non-skipped commands and summary checks pass. The generated summary status becomes `pass_with_skips`, not `pass`.

## 4. Section 9 Policy

The wrapper treats standalone Section 9 as blocking for the wrapper result. If `npm run harness:validate:section9` fails or its stable summary is malformed, the wrapper fails.

Inside `npm run harness:validate:premerge`, Section 9 remains report-only. Section 8 remains the premerge blocking surface until a governed policy change promotes Section 9.

## 5. Summary Consistency

The wrapper checks:

- `frontend/artifacts/harness/section9/latest/summary.json` exists after Section 9 runs;
- Section 9 `testCount` equals `results.length`;
- each Section 9 result has an ID, status, and test file list;
- when premerge is not skipped, `frontend/artifacts/harness/section8/latest/summary.json` exists, is `pass`, contains all required Section 8 IDs, and omits the removed legacy ID `regression.api_chat_reachability`.

The release-quality summary itself is ignored by git like other generated harness summaries. Commit the evidence note and runbook updates, not generated logs.

## 6. Packaging Boundary

Packaging and DMG evidence remain separate. Use `docs/BUILD_AND_RELEASE.md` and `docs/RELEASE_QUALITY_GATES.md` for `npm run build`, `npm run desktop:pack`, `npm run desktop:dist`, `npm run instruction-root:integrity`, and packaged SDK proof selection.

Do not use this runtime-premerge wrapper to imply signing, notarization, publication, distribution, release-readiness, professional approval, certification, sealing, authentication, or code-compliance acceptance.
