# Unprivileged preparation return R2 — A2-DAPP92-A-IMPLEMENT-01

- RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
- InstanceID: `A2-DAPP92-A-IMPLEMENT-01`
- Governing register: `COMMAND_REGISTER_AMENDMENT_V1_7.md`
- Executed tranche: C152–C195, subject to stop-on-failure and mandatory
  C185–C195 rollback
- Terminal status: `PACKAGE_PIPELINE_FAILED_AT_INSTRUCTION_ROOT_ARGUMENT — ROLLBACK PASS`
- Source posture: exact uninstrumented R3 candidate reconstructed and then
  byte-restored; no product change retained.
- Runtime posture: no GUI/helper launch, registration/contact, sample,
  attachment, trace, signal, or C051–C059 invocation.
- Authority posture: no credential, Git, provider, release, or foreign-loop
  operation. No deliberate standalone network command was invoked. C178's
  electron-builder output did emit `downloaded`/`downloaded electron zip
  extracted successfully`; whether that represented a cache copy or external
  transfer is not proven by the retained output and remains `UNKNOWN`.

## Command ledger

| IDs | Status | Exact result |
|---|---|---|
| C152 | PASS, exit 0 | Frontend dependency target was absent. |
| C153–C164 | PASS, exit 0 each | Reconstructed the exact 12-file uninstrumented candidate from the immutable R2 snapshot. |
| C165 | PASS, exit 0 | All 12 candidate hashes plus unchanged lockfile reproduced exactly. |
| C166 | PASS, exit 0 | Materialized the accepted dependency tree using the exact `ditto` command. |
| C167 | PASS, exit 0 | Removed only the six enumerated Root-owned copied entries. |
| C168–C173 | PASS, exit 0 each | Created the exact six accepted R3 projections. |
| C174 | PASS, exit 0 | Bound the six Root projections plus untouched harness-contract facade; exact output below. |
| C175 | PASS, exit 0 | Vitest `v4.1.10`: 4 test files passed, 30 tests passed. The command named five paths but Vitest reported four files/30 tests rather than the register purpose's “32-test” count; no count inflation is inferred. |
| C176 | PASS, exit 0 | Both TypeScript no-emit checks passed. |
| C177 | PASS, exit 0 | Next.js 15.5.21 production build and Electron/CLI bundle build passed. |
| C178 | **FAIL, exit 1** | Helper and GUI packages were generated with Electron 43.2.0; packaged dependency-boundary check passed; instruction-root integrity invocation failed because npm forwarded `never` as an unsupported positional argument. Exact outcome below. |
| C179–C184 | NOT INVOKED | Held by C178 stop-on-failure. Therefore package hashes, plist dumps, symlink census/targets, and standalone/embedded diff were not captured and no package-manifest conformance claim is made. |
| C185–C193 | PASS, exit 0 each | Mandatory byte restoration, five-addition removal, and named dependency/build derivative cleanup completed. |
| C194 | PASS, exit 0 | All eight baseline/lockfile hashes reproduced after rollback. |
| C195 | PASS, exit 0 | Empty output: frontend is Git-clean after rollback. |

## Candidate identity — C165

| Product surface | SHA-256 |
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

## Projection identity — C174

The exact output bound:

- `engine-pi-omlx -> /Users/ryan/dev/chirality/runtime/packages/engine-pi-omlx`
- `harness-contract -> ../../packages/harness-contract`
- `runtime-cli -> /Users/ryan/dev/chirality/runtime/packages/cli`
- `runtime-client -> /Users/ryan/dev/chirality/runtime/packages/client`
- `runtime-contracts -> /Users/ryan/dev/chirality/runtime/packages/contracts`
- `runtime-core -> /Users/ryan/dev/chirality/runtime/packages/core`
- `runtime-daemon -> /Users/ryan/dev/chirality/runtime/packages/daemon`

All seven entries were symlinks in C174 output. The six absolute links are the
enumerated Root projections; the relative harness-contract facade was left
untouched exactly as v1.7 required.

## Focused preflight — C175

- `runtime-helper-packaging.test.ts`: 2 passed
- `desktop-daemon-posture.test.ts`: 8 passed
- `runtime-control-ipc.test.ts`: 10 passed
- `cli-launcher.test.ts`: 10 passed
- total emitted by Vitest: 4 files, 30 tests, all passed
- elapsed summary: 409 ms

The exact command also named
`desktop-cli-single-daemon-integration.test.ts`, but Vitest emitted no file or
test count for it. The evidence therefore supports 30, not 32, focused tests.

## Build and package pipeline — C176–C178

C176 ran:

`tsc --noEmit --incremental false && tsc -p tsconfig.electron.json --noEmit --incremental false`

and exited 0.

C177 exited 0 after:

- Next.js `15.5.21` compiled and generated 24 static pages;
- `dist-electron/main.js`, `runtime-helper.js`, and `preload.js` built;
- `dist-runtime/chirality-cli.mjs` built.

C178 then:

1. rebuilt the production/Electron/CLI surfaces successfully;
2. packaged standalone runtime-helper and GUI applications using
   electron-builder `26.15.3`, Darwin `25.6.0`, arm64, Electron `43.2.0`;
3. skipped application signing because
   `CSC_IDENTITY_AUTO_DISCOVERY=false`;
4. passed `desktop:verify-dependencies` with:
   - `status: PASS`;
   - `localPackageEntries: 0`;
   - `forbiddenDevelopmentPackagesPresent: []`;
   - required packages `@anthropic-ai/claude-agent-sdk`,
     `@earendil-works/pi-coding-agent`, and `next` present;
   - `failures: []`;
5. emitted npm warnings that `never` was parsed as a normal argument and
   `--publish` as an unknown npm config;
6. invoked `node ./scripts/verify-instruction-root-integrity.mjs never`;
7. failed with `instruction-root integrity verification failed: Unknown
   argument: never` and exit 1.

Thus package construction and dependency-boundary evidence exist in C178's
transient output, but release-quality/instruction-root PASS does not. Because
C179–C184 were correctly not run and C193 removed generated packages, package
hash/metadata/topology identity is not retained and remains `UNKNOWN`.

## Rollback proof — C194/C195

| Restored path | SHA-256 |
|---|---|
| `electron/cli-launcher.ts` | `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b` |
| `electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` |
| `electron/runtime-control-ipc.ts` | `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a` |
| `package.json` | `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53` |
| `package-lock.json` | `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56` |
| `scripts/build-electron.mjs` | `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558` |
| `src/__tests__/electron/cli-launcher.test.ts` | `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9` |
| `src/__tests__/electron/runtime-control-ipc.test.ts` | `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6` |

C195 exited 0 with empty output. Candidate additions, dependency tree, and all
named generated package/build surfaces were removed. Frontend product/config/
test bytes are restored and Git-clean. The fixed `/private/tmp` run tree remains
under the manager's separately enumerated final evidence-synthesis cleanup.

## Exact next requirement

Any preparation retry must freeze a corrected `desktop:pack` invocation whose
argument forwarding preserves `--publish never` for electron-builder without
passing `never` into `verify-instruction-root-integrity.mjs`. It must rerun the
sole attempt from clean reconstructed state and preserve mandatory rollback.
No GUI/helper runtime or special-authority command may proceed until package
construction, instruction-root verification, and C179–C184 manifest binding
all pass in the same sealed attempt.
