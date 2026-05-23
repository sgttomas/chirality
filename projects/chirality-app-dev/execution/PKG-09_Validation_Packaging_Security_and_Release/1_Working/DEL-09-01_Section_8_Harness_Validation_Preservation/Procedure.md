# Procedure: DEL-09-01 Section 8 Harness Validation Preservation

## Purpose

Define the operating procedure for preserving and verifying Section 8 harness validation behavior and stable premerge summary output for DEL-09-01.

## Prerequisites

- Work from the repository root with frontend dependencies installed under `frontend/`.
- The frontend server must be reachable at `HARNESS_BASE_URL`, defaulting to `http://127.0.0.1:3000`, before Section 8 validation runs.
- `frontend/scripts/validate-harness-section8.mjs` must exist and be readable.
- `frontend/package.json` must expose `harness:validate:section8` and `harness:validate:premerge`.
- Declared upstream dependencies are `TBD`; no accepted dependency edges have been extracted yet. Source: `_DEPENDENCIES.md`.
- Source warning: `docs/PRD.md` has a known hash mismatch for this run and remains usable only under the invoker's warning-only ruling.

## Steps

1. Confirm the validation script surface.
   - Inspect `frontend/package.json` for `harness:validate:section8` and `harness:validate:premerge`.
   - Inspect `frontend/scripts/validate-harness-premerge.mjs` for `REQUIRED_TEST_IDS`, `LEGACY_REMOVED_TEST_ID`, and stable artifact path.

2. Start or verify the harness server.
   - For local runs, start the Next.js server using the repository's frontend workflow.
   - For CI, preserve the readiness poll against `/api/harness/session/list?projectRoot=/tmp` before running the wrapper.

3. Run the premerge wrapper from `frontend/`.
   - Command: `npm run harness:validate:premerge`.
   - The wrapper should invoke `frontend/scripts/validate-harness-section8.mjs`.

4. Verify the Section 8 summary contents.
   - Confirm status is `pass`.
   - Confirm all required IDs are present:
     - `setup.server_reachable`
     - `regression.session_crud`
     - `section8.boot_error_taxonomy`
     - `section8.smoke_stream`
     - `section8.session_persistence_resume`
     - `section8.permissions_dontask`
     - `section8.interrupt_sigint`
     - `section8.sdk_native_stream`
   - Confirm `regression.api_chat_reachability` is absent.

5. Verify stable artifact placement.
   - Confirm `frontend/artifacts/harness/section8/latest/summary.json` exists and is readable after the wrapper completes.
   - In CI, confirm the workflow uploads the same path as `harness-section8-summary`.

6. Preserve required local checks for release-significant changes.
   - Run or require evidence for:
     - `npm run test`
     - `npm run typecheck`
     - `npm run harness:validate:premerge`
     - `npm run instruction-root:integrity`
   - Packaging release context additionally requires `npm run desktop:dist`.

7. Record outcomes.
   - Capture command status, summary path, test count, and any missing IDs.
   - Record `TBD`, `ASSUMPTION`, or source-warning items instead of filling unsupported facts.

## Verification

| Check | Expected result | Source |
|---|---|---|
| Wrapper script exists | `frontend/scripts/validate-harness-premerge.mjs` readable | `frontend/scripts/validate-harness-premerge.mjs` |
| Section 8 script exists | `frontend/scripts/validate-harness-section8.mjs` readable | `frontend/scripts/validate-harness-premerge.mjs` |
| Required IDs | All eight accepted Section 8 IDs present | `frontend/scripts/validate-harness-premerge.mjs`; `docs/SPEC.md` Section 19.2 |
| Legacy ID | `regression.api_chat_reachability` absent | `frontend/scripts/validate-harness-premerge.mjs` |
| Stable summary | `frontend/artifacts/harness/section8/latest/summary.json` exists | `docs/PRD.md` FR-066; `.github/workflows/harness-premerge.yml` |
| CI upload | `harness-section8-summary` artifact uploaded from stable summary path | `.github/workflows/harness-premerge.yml` |

## Records

- Local command transcript or CI job log for `npm run harness:validate:premerge`.
- Stable summary JSON at `frontend/artifacts/harness/section8/latest/summary.json`.
- CI artifact named `harness-section8-summary`.
- Any preservation test fixture outputs proving missing-ID rejection and legacy-ID rejection.
- Human ruling record for the PRD hash mismatch before closure, if closure requires source hash reconciliation.

