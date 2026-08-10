# R3 reconstructable source manifest

The retained source candidate was byte-identical to the immutable R2 candidate at:

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/`

The current `package.json` dependency, devDependency, override, engine, and version state was preserved. Only the frozen R2 scripts and `build.afterPack` hunks were applied. After evidence freeze, the product source was restored to the pre-R3 hashes below.

| Product path | Pre-R3 SHA-256 | Candidate SHA-256 |
|---|---|---|
| `electron-builder.runtime-helper.json` | absent | `bd1925a50ac18258bd03db0e475f9ac04d4fcbc46ab7a79b62a4090d92580982` |
| `electron/cli-launcher.ts` | `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b` | `2a0724f11d71a0682d2a9674c24fefd2d2f0137ed70e2190a84944d060a1126d` |
| `electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` | `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491` |
| `electron/runtime-control-ipc.ts` | `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a` | `970583be61674d8818046108d5129df90d06484d64c94ee904bbfedb2d0f2fc4` |
| `electron/runtime-helper-entry.ts` | absent | `7e0ab20f14d634f9ce4e77fcfa55826cf4b0c022828acaee0709b8927123e2bc` |
| `electron/runtime-helper-path.ts` | absent | `7df8dc3f66d0fc070d3728854f6c5421bd2bff3ba1864bafbacec04485ebbf02` |
| `package.json` | `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53` | `7996a9066e14188d859c499c243bf6ca2f864f7c2c8616a364c897d6ba658e15` |
| `scripts/build-electron.mjs` | `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558` | `cee808c108826e9987d5197bdc63c86d32ac1a428e54537fe4c3a3d79138a505` |
| `scripts/embed-runtime-helper.mjs` | absent | `a710b7790ad92c4a64526478baa6e8f49c00a9070c7b84fb22529104f2a79199` |
| `src/__tests__/electron/cli-launcher.test.ts` | `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9` | `27b3a0e36c4b5592a776057b71fa40ba391cb05170dacc91594e8736caafcc7f` |
| `src/__tests__/electron/runtime-control-ipc.test.ts` | `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6` | `8402b8b703f44bad6a4f8a74a8614a53ca5294f16c96b6c5b05f47a19ac2964e` |
| `src/__tests__/electron/runtime-helper-packaging.test.ts` | absent | `0915e0b4645bfd194512ed2677ca72d4863884346726aa81265a638ce6826465` |

All candidate hashes matched the R2 manifest exactly before rollback.
