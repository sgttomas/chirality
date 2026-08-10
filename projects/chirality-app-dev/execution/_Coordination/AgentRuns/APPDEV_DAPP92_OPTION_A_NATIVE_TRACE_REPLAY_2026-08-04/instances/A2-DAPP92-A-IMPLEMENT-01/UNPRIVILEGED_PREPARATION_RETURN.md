# Unprivileged preparation return — A2-DAPP92-A-IMPLEMENT-01

- RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
- InstanceID: `A2-DAPP92-A-IMPLEMENT-01`
- Governing register: `COMMAND_REGISTER_AMENDMENT_V1_5.md`
- Executed tranche: C096–C146, subject to stop-on-failure and mandatory
  C136–C146 rollback
- Terminal status: `PREPARATION_FAILED — DEPENDENCY ENTRY UNRESOLVED — ROLLBACK PASS`
- GUI/helper/trace effect: none; C127–C135 and every GUI/helper launch,
  registration/contact, sample, attach, trace, signal, and C051–C059 command
  were not invoked.
- External effect: no credential, Git, network, provider, release, or
  foreign-loop action occurred.

## Exact command ledger

| IDs | Status | Exact result |
|---|---|---|
| C096 | PASS, exit 0 | Fixed runtime root was absent. |
| C097 | PASS, exit 0 | Created only the enumerated run-owned runtime, evidence, and baseline snapshot directories. |
| C098–C104 | PASS, exit 0 each | Copied the seven enumerated frontend baseline bytes into the fixed rollback snapshot. |
| C105 | PASS, exit 0 | All seven snapshot hashes reproduced the frozen baseline; exact hashes are below. |
| C106–C117 | PASS, exit 0 each | Reconstructed the exact 12-file uninstrumented candidate, using corrected immutable test paths from amendment v1.2. |
| C118 | PASS, exit 0 | All 12 candidate hashes and unchanged lockfile reproduced; exact hashes are below. |
| C119 | PASS, exit 0 | Materialized the accepted exact-lock dependency tree using the enumerated `ditto` command. |
| C120 | PASS, exit 0 | Removed only the three enumerated copied Root-owned entries. |
| C121–C123 | PASS, exit 0 each | Created exact contracts, policy, and daemon projections. |
| C124 | PASS, exit 0 | Contracts target: `/Users/ryan/dev/chirality/runtime/packages/contracts`. |
| C125 | PASS, exit 0 | Policy target: `/Users/ryan/dev/chirality/runtime/packages/policy`. |
| C126 | **FAIL, exit 1** | Focused Vitest preflight failed because Vite could not resolve the package entry for `@chirality/runtime-cli`; details below. |
| C127–C135 | NOT INVOKED | Held by C126 stop-on-failure. No typecheck, build, package, package hashes/plists/symlink census, or standalone/embedded diff exists from this tranche. |
| C136–C144 | PASS, exit 0 each | Mandatory byte restoration, five-addition removal, and named dependency/build derivative cleanup completed. |
| C145 | PASS, exit 0 | All eight baseline/lockfile hashes reproduced after rollback; exact hashes are below. |
| C146 | PASS, exit 0 | Produced no output: `projects/chirality-app-dev/frontend` is Git-clean after rollback. |

## Baseline snapshot — C105

| Snapshot path | SHA-256 |
|---|---|
| `baseline/electron/cli-launcher.ts` | `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b` |
| `baseline/electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` |
| `baseline/electron/runtime-control-ipc.ts` | `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a` |
| `baseline/package.json` | `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53` |
| `baseline/scripts/build-electron.mjs` | `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558` |
| `baseline/tests/cli-launcher.test.ts` | `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9` |
| `baseline/tests/runtime-control-ipc.test.ts` | `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6` |

## Reconstructed candidate — C118

| Product surface, register order | SHA-256 |
|---|---|
| `electron-builder.runtime-helper.json` | `bd1925a50ac18258bd03db0e475f9ac04d4fcbc46ab7a79b62a4090d92580982` |
| `electron/cli-launcher.ts` | `2a0724f11d71a0682d2a9674c24fefd2d2f0137ed70e2190a84944d060a1126d` |
| `electron/main.ts` | `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491` |
| `electron/runtime-control-ipc.ts` | `970583be61674d8818046108d5129df90d06484d64c94ee904bbfedb2d0f2fc4` |
| `electron/runtime-helper-entry.ts` | `7e0ab20f14d634f9ce4e77fcfa55826cf4b0c022828acaee0709b8927123e2bc` |
| `electron/runtime-helper-path.ts` | `7df8dc3f66d0fc070d3728854f6c5421bd2bff3ba1864bafbacec04485ebbf02` |
| `package.json` | `7996a9066e14188d859c499c243bf6ca2f864f7c2c8616a364c897d6ba658e15` |
| `scripts/build-electron.mjs` | `cee808c108826e9987d5197bdc63c86d32ac1a428e54537fe4c3a3d79138a505` |
| `scripts/embed-runtime-helper.mjs` | `a710b7790ad92c4a64526478baa6e8f49c00a9070c7b84fb22529104f2a79199` |
| `src/__tests__/electron/cli-launcher.test.ts` | `27b3a0e36c4b5592a776057b71fa40ba391cb05170dacc91594e8736caafcc7f` |
| `src/__tests__/electron/runtime-control-ipc.test.ts` | `8402b8b703f44bad6a4f8a74a8614a53ca5294f16c96b6c5b05f47a19ac2964e` |
| `src/__tests__/electron/runtime-helper-packaging.test.ts` | `0915e0b4645bfd194512ed2677ca72d4863884346726aa81265a638ce6826465` |
| `package-lock.json` | `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56` |

## C126 failure evidence

Exact command ran from the required cwd
`projects/chirality-app-dev/frontend` under the isolated HOME and enumerated
Node-24 PATH. npm expanded it to:

`vitest run src/__tests__/electron/desktop-daemon-posture.test.ts src/__tests__/electron/runtime-control-ipc.test.ts src/__tests__/electron/cli-launcher.test.ts src/__tests__/electron/runtime-helper-packaging.test.ts src/__tests__/electron/desktop-cli-single-daemon-integration.test.ts`

Vitest `v4.1.10` reported:

- `runtime-helper-packaging.test.ts`: 2 tests passed;
- `runtime-control-ipc.test.ts`: suite failed before test collection;
- `cli-launcher.test.ts`: suite failed before test collection;
- `desktop-daemon-posture.test.ts`: suite failed before test collection;
- summary: 3 failed test files, 1 passed test file; 2 passed tests;
- primary error: `Failed to resolve entry for package
  "@chirality/runtime-cli". The package may have incorrect
  main/module/exports specified in its package.json.`
- first reported import surface:
  `electron/desktop-daemon-posture.ts:27:7`, importing
  `@chirality/runtime-cli`;
- second reported import surface:
  `src/__tests__/electron/desktop-daemon-posture.test.ts:6:7`, importing
  `@chirality/runtime-cli`.

This is dependency-substrate insufficiency, not a candidate test assertion
failure and not signal/lifecycle evidence. No repair or inferred substitute was
authorized in v1.5.

## Rollback proof — C145/C146

| Restored product path | SHA-256 |
|---|---|
| `electron/cli-launcher.ts` | `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b` |
| `electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` |
| `electron/runtime-control-ipc.ts` | `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a` |
| `package.json` | `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53` |
| `package-lock.json` | `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56` |
| `scripts/build-electron.mjs` | `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558` |
| `src/__tests__/electron/cli-launcher.test.ts` | `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9` |
| `src/__tests__/electron/runtime-control-ipc.test.ts` | `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6` |

C146 was empty at exit 0. Therefore the exact frontend product/config/test
bytes are restored, candidate additions and named generated/dependency trees
are absent, and no frontend Git effect remains. The fixed `/private/tmp`
run-owned tree remains only because v1.5 reserves its later removal for the
manager's separately enumerated evidence-synthesis cleanup.

## Required next action

Manager must identify and freeze an exact accepted `@chirality/runtime-cli`
projection/build substrate before any rerun. This return grants no authority to
install, build Root packages, use network, change dependency versions, launch a
GUI/helper, or invoke C051–C059. Any continuation requires a new sealed command
amendment and must preserve mandatory rollback.
