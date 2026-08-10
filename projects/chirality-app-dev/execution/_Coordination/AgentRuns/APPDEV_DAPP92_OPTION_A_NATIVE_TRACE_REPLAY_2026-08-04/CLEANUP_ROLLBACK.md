# Cleanup and rollback — D-APP-92 Option A preparation

Status: `PASS`

Final baseline/lockfile hashes:

| Product path under `frontend/` | Restored SHA-256 |
|---|---|
| `electron/cli-launcher.ts` | `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b` |
| `electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` |
| `electron/runtime-control-ipc.ts` | `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a` |
| `package.json` | `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53` |
| `package-lock.json` | `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56` |
| `scripts/build-electron.mjs` | `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558` |
| `src/__tests__/electron/cli-launcher.test.ts` | `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9` |
| `src/__tests__/electron/runtime-control-ipc.test.ts` | `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6` |

All five candidate additions, `frontend/node_modules`, `dist`,
`dist-runtime-helper`, `dist-electron`, `dist-runtime`, `.next`, and the fixed
`/private/tmp/chirality-dapp92-option-a-20260804` tree are absent. Frontend Git
status is empty. No helper/GUI/tracer PID was ever created by this run.
