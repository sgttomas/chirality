# PR764 Section 8 CI repair — manager return

Status: candidate repair validated; no commit, push, release, packaging, native launch, or supplier qualification performed.

## Diagnosis and repair

The shared Runtime selected the registered stub adapter, but `RuntimeService.bootSession` supplied an empty message. The production App compatibility adapter admits a frozen v3 boot only with the reserved `bootstrap` marker, so the boot failed with typed `ENGINE_UNAVAILABLE`/HTTP 503 before `session:init`. Runtime now supplies `bootstrap` and records that exact marker on the accepted boot event. Provider attribution and all existing boot validation remain required.

The Section 8 validator now includes the exact HTTP status and JSON payload in a boot failure result. The premerge wrapper remains fail-closed, but copies the validator's exact nonzero summary to the stable artifact path and reports its result count. A malformed summary is still copied for diagnosis, reports count zero, and cannot pass.

## Exact source subjects

- `projects/chirality-runtime/packages/core/src/runtime-service.ts` — `d0b0debf6e47b844483e6f29cef27e323a2bb662c9d1c0ef2d77b77a4ec0bbbb`
- `projects/chirality-runtime/tests/runtime-v3-api.test.ts` — `005725ec2d50f4fb99f5043514cf45c05a3b9e5eabefa07d016bcca9e9180e6e`
- `projects/chirality-app-dev/frontend/scripts/validate-harness-section8.mjs` — `9ce64529359fe3134fbead391a22162561ffa248111349fc2182664bb24c00b4`
- `projects/chirality-app-dev/frontend/scripts/validate-harness-premerge.mjs` — `2d23414e7cdc90cf20943ea22fde4f9c9a38f58f7aacae8d572ab79fb6eba535`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/validate-harness-premerge.test.ts` — `7e2b8f99fc10fd7efee23c19adf39721c8ab31037b2b2fe7e3a33af22626bbc8`
- `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-successor-adapters.integration.test.ts` — `3f3807f043948a3e6799e61b9ba323ced2b3af02623bc3cf751418b330870e45`

## Validation

- Runtime v3 API integration: 26/26 PASS.
- App focused production-adapter and premerge-wrapper tests: 8/8 PASS.
- Runtime typecheck/build: PASS.
- App typecheck: PASS.
- Selected diff check: PASS.

Raw patch, subject hash list, and logs are preserved at `/private/tmp/chirality-pr764-section8-repair-v2`. The controlled stub proves the contract and transport seam only; it is not native-provider qualification. The amended GitHub Actions run remains the required integrated CI check.
