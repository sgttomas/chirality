# D-APP-88 product rollback manifest

Manager direction required all blocked D-APP-88 product/config/test changes to leave integration state while preserving D-APP-89 and durable diagnostics.

## Removed additions

- `frontend/electron/runtime-helper-bundle.ts`
- `frontend/scripts/afterpack-runtime-helper.mjs`
- `frontend/src/__tests__/electron/runtime-helper-bundle.test.ts`

Their exact candidate bytes remain in `candidate-source/` and are hash-bound by `CANDIDATE_SOURCE_MANIFEST.md`.

## Reverted D-APP-88 hunks

- `electron/main.ts`: helper import/mode detection, helper LaunchAgent path, and helper activation guard.
- `electron/cli-launcher.ts`: helper path import, daemon executable parameter/rendering, and helper-pinned install.
- `electron/runtime-control-ipc.ts`: `daemonExecutable` dependency rename and install target.
- Electron CLI/runtime-control tests: helper executable fixtures/expectations.
- `package.json`: removed D-APP-88 `build.afterPack` only.

## Post-rollback hashes

These five restored files exactly equal Git `HEAD` byte-for-byte:

| Path | Worktree SHA-256 = HEAD SHA-256 |
|---|---|
| `electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` |
| `electron/cli-launcher.ts` | `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b` |
| `electron/runtime-control-ipc.ts` | `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a` |
| `src/__tests__/electron/cli-launcher.test.ts` | `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9` |
| `src/__tests__/electron/runtime-control-ipc.test.ts` | `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6` |

`package.json` post-rollback SHA-256 is `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53`. Its only remaining Git diff is the D-APP-89 removal of `@chirality/harness-contract`; no D-APP-88 `afterPack` key remains. HEAD SHA-256 is `1e62d22ec4a07fb225352c90ddfa5ce41d736d3d169e04cf7bd3684e54557c9c`.

`rg` confirms no `SIGUSR2`, `single-process`, `NetworkServiceInProcess`, or `browser-subprocess-path` diagnostic remains in the product helper surfaces. Root runtime tracked state is clean and the temporary dependency projection is restored.
