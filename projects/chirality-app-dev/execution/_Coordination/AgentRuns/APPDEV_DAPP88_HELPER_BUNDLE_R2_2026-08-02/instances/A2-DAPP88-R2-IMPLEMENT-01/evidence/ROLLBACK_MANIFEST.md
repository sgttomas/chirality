# R2 rollback manifest

## Removed R2 additions

- `frontend/electron/runtime-helper-entry.ts`
- `frontend/electron/runtime-helper-path.ts`
- `frontend/electron-builder.runtime-helper.json`
- `frontend/scripts/embed-runtime-helper.mjs`
- `frontend/src/__tests__/electron/runtime-helper-packaging.test.ts`

Their final candidate bytes remain under `candidate-source/` and are hash-bound by `CANDIDATE_SOURCE_MANIFEST.md`.

## Reverted R2 hunks

- `electron/main.ts`: helper-entry mode and helper executable routing.
- `electron/cli-launcher.ts`: helper-pinned daemon installation while preserving GUI-backed CLI execution.
- `electron/runtime-control-ipc.ts`: helper executable install target.
- `scripts/build-electron.mjs`: second entry build.
- focused CLI/runtime-control tests.
- `package.json`: helper build/package scripts and GUI `afterPack` embedding hook.

The six existing product/test files touched by R2 have zero diff against Git `HEAD`. `package.json` retains only the independent D-APP-89 change already present when R2 began. Root tracked state under `runtime/` is clean. The generated ignored `frontend/dist-runtime-helper/` derivative is not product truth and is not proposed for commit.

The reversible validation-only `runtime/node_modules` projection was restored to the original real directory (inode `22189023`, with `.vite` inode `22189024`); its backup is absent and tracked Root state is clean.
