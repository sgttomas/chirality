# Attempt 4 cleanup proof

Status: `PASS — GOVERNED BASELINE RESTORED`

## Mandatory cleanup outcomes

C185-C193 returned exit `0` for every exact restoration/removal command.
C194 returned exit `0` and reproduced every frozen governed hash. C195
returned exit `0` with exactly empty stdout. C199 returned exit `0`; C200
returned exit `0` and proved the fixed temporary root absent.

## Eight final governed hashes — C194

| Frontend path | SHA-256 |
|---|---|
| `electron/cli-launcher.ts` | `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b` |
| `electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` |
| `electron/runtime-control-ipc.ts` | `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a` |
| `package.json` | `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53` |
| `package-lock.json` | `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56` |
| `scripts/build-electron.mjs` | `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558` |
| `src/__tests__/electron/cli-launcher.test.ts` | `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9` |
| `src/__tests__/electron/runtime-control-ipc.test.ts` | `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6` |

## Removed candidate additions — C192

The exact removal command returned `0` for all five paths:

- `frontend/electron-builder.runtime-helper.json`
- `frontend/electron/runtime-helper-entry.ts`
- `frontend/electron/runtime-helper-path.ts`
- `frontend/scripts/embed-runtime-helper.mjs`
- `frontend/src/__tests__/electron/runtime-helper-packaging.test.ts`

## Removed dependency/build paths — C193

The exact recursive removal command returned `0` for every named path:

- `frontend/node_modules`
- `frontend/dist`
- `frontend/dist-runtime-helper`
- `frontend/dist-electron`
- `frontend/dist-runtime`
- `frontend/.next`

## Fixed temporary root — C199/C200

`/private/tmp/chirality-dapp92-option-a-20260804` was removed by C199 and C200
proved it absent; both commands returned `0`.

## Exact frontend Git-status bytes — C195

Command: `/usr/bin/git status --short -- projects/chirality-app-dev/frontend`

Exit: `0`

Stdout byte count: `0`

Exact stdout: empty.
