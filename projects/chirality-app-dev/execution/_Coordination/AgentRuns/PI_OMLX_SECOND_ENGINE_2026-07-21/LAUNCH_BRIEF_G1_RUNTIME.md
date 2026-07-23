# Launch Brief — G1 Desktop Runtime Prerequisite

- **RunID:** `PI_OMLX_SECOND_ENGINE_2026-07-21`
- **Role:** WORKING_ITEMS desktop runtime prerequisite owner
- **Model:** `gpt-5.6-sol` (record any substitution)
- **Authority:** D-APP-72 and SCA-APP-002 after independent G0 authority audit PASS.
- **Required result:** upgrade only the desktop/runtime prerequisite while preserving Claude and stub behavior. Pi remains absent in G1.

## Write scope

- `frontend/package.json`
- `frontend/package-lock.json`
- `frontend/docs/harness/README.md`
- `frontend/src/__tests__/scripts/dmg-packaging-policy.test.ts`
- repository `.github/workflows/harness-premerge.yml`
- G1 evidence under this run directory
- Electron source/tests only if a concrete Electron 43 regression requires a compatibility repair

## Required versions and behavior

- Exact `electron: "43.1.1"`
- Exact `electron-builder: "26.15.3"`
- Exact `@types/node: "24.12.4"`
- `engines.node: ">=22.19.0"`
- Active CI Node 24
- Update developer runtime documentation and add exact package-policy assertions.
- Do not install Pi, change provider behavior, broaden network policy, alter credentials, or modify governance/decomposition/deliverable files.
- Preserve the current directory-picker behavior unless Electron 43 testing proves a blocking regression; do not add speculative UX changes.

## Validation

- Regenerate the lockfile using the exact versions.
- Confirm host Node/npm and Electron/embedded Node versions.
- Run focused Electron/package tests, full typecheck/tests/build, `desktop:pack`, instruction-root integrity, and packaged Claude SDK resolver proof where possible.
- Record skipped or environment-blocked checks exactly; no release/sign/notarize action.
- Write `RETURN_G1_RUNTIME.md` with exact changed paths, versions, checks, packaging observations, residuals, and actual model.
