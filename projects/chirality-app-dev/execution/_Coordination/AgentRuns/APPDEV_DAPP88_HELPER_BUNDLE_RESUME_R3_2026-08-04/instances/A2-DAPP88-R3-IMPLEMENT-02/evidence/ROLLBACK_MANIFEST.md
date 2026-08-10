# R3 product rollback manifest

Status: `PASS`

All 7 pre-existing product/test files were restored to their pre-R3 SHA-256 values:

- `electron/cli-launcher.ts`: `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`
- `electron/main.ts`: `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f`
- `electron/runtime-control-ipc.ts`: `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a`
- `package.json`: `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53`
- `scripts/build-electron.mjs`: `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558`
- `src/__tests__/electron/cli-launcher.test.ts`: `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9`
- `src/__tests__/electron/runtime-control-ipc.test.ts`: `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6`

All 5 R3 additions are absent:

- `electron-builder.runtime-helper.json`
- `electron/runtime-helper-entry.ts`
- `electron/runtime-helper-path.ts`
- `scripts/embed-runtime-helper.mjs`
- `src/__tests__/electron/runtime-helper-packaging.test.ts`

Scoped Git status over all 12 surfaces plus `package-lock.json` is empty. Reconstructable candidate bytes remain at the immutable R2 source snapshot cited in `SOURCE_MANIFEST.md`.
