# Datasheet: DEL-09-01 Section 8 Harness Validation Preservation

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-09-01 |
| DeliverableName | Section 8 Harness Validation Preservation |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | TEST_SUITE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| CoversScopeItems | SOW-035, SOW-036 |
| SupportsObjectives | OBJ-008 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary purpose | Preserve baseline harness validation, current local checks, and stable premerge summary behavior. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 8, DEL-09-01 |
| Required local checks in scope | `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `npm run instruction-root:integrity`; packaging check `npm run desktop:dist` is release-scope context. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2; `docs/CONTRACT.md` K-VALIDATE-1 |
| Premerge command | `npm run harness:validate:premerge` from `frontend/`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` FR-066; `frontend/package.json` scripts |
| Stable Section 8 summary artifact | `frontend/artifacts/harness/section8/latest/summary.json`. | `docs/PRD.md` FR-066; `frontend/scripts/validate-harness-premerge.mjs` stableArtifactPath; `.github/workflows/harness-premerge.yml` Verify stable summary artifact |
| Current Section 8 required test IDs | `setup.server_reachable`; `regression.session_crud`; `section8.boot_error_taxonomy`; `section8.smoke_stream`; `section8.session_persistence_resume`; `section8.permissions_dontask`; `section8.interrupt_sigint`; `section8.sdk_native_stream`. | `frontend/scripts/validate-harness-premerge.mjs` REQUIRED_TEST_IDS; `frontend/scripts/validate-harness-section8.mjs` REQUIRED_CHECK_ORDER |
| Legacy removed test ID | `regression.api_chat_reachability` must not appear in the premerge summary. | `frontend/scripts/validate-harness-premerge.mjs` LEGACY_REMOVED_TEST_ID |
| CI workflow surface | Pull request and manual workflow run harness premerge validation, verify the stable summary JSON, and upload it as `harness-section8-summary`. | `.github/workflows/harness-premerge.yml` |

## Conditions

- The harness premerge wrapper depends on `frontend/scripts/validate-harness-section8.mjs` being readable; if absent, the wrapper reports `RUNTIME_SURFACE_MISSING` and fails. Source: `frontend/scripts/validate-harness-premerge.mjs`.
- Section 8 validation defaults to `HARNESS_BASE_URL=http://127.0.0.1:3000` and uses `HARNESS_PROJECT_ROOT` when provided; otherwise it resolves to `../examples/example-project` from `frontend/`. Source: `frontend/scripts/validate-harness-section8.mjs`.
- If the requested project root is inside the instruction root, the Section 8 script stages it under the temporary validation root before running tests. Source: `frontend/scripts/validate-harness-section8.mjs`.
- The current provenance summary records a passing Section 8 run with `testCount: 8`. Source: `provenance/build-artifacts/frontend__artifacts__harness__section8__latest__summary.json`.
- Source warning: `docs/PRD.md` is locally accessible but has a known hash mismatch for this run; the invoker instructed that mismatch to be treated as a source warning only.

## Construction

This deliverable should be implemented as a preservation-oriented test suite and validation wrapper guard, not as new harness feature implementation. The relevant construction surfaces are:

- `frontend/package.json` script entries for `harness:validate:section8` and `harness:validate:premerge`.
- `frontend/scripts/validate-harness-section8.mjs` for Section 8 scenario execution and summary generation.
- `frontend/scripts/validate-harness-premerge.mjs` for required test ID enforcement, legacy ID exclusion, and stable summary artifact copying.
- `.github/workflows/harness-premerge.yml` for CI readiness polling, wrapper execution, artifact verification, and upload.
- `frontend/artifacts/harness/section8/latest/summary.json` as the stable local artifact produced by the premerge wrapper.

## References

- `docs/SPEC.md` Sections 19.1 and 19.2.
- `docs/PRD.md` Sections 12.2 and 12.3; FR-066 and FR-068.
- `docs/CONTRACT.md` K-VALIDATE-1.
- `docs/TYPES.md` Section 12.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 7, 8, 10A.
- `frontend/package.json`.
- `frontend/scripts/validate-harness-premerge.mjs`.
- `frontend/scripts/validate-harness-section8.mjs`.
- `.github/workflows/harness-premerge.yml`.
- `provenance/build-artifacts/frontend__artifacts__harness__section8__latest__summary.json`.

