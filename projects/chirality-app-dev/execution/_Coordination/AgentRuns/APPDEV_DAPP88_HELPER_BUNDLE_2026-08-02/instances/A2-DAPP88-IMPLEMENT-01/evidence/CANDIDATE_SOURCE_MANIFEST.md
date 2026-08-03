# Reconstructable candidate source manifest

The `candidate-source/` subtree freezes the final D-APP-88 product candidate before rollback. It includes complete files, not excerpts; package metadata also contains the concurrent accepted D-APP-89 state and must be reconciled by hunk if reconstructed.

| Snapshot path | SHA-256 |
|---|---|
| `electron/cli-launcher.ts` | `8ed60f9606d4fb4bb03738ee061393b21c00175996aae78725f4ee1e4a0e34ff` |
| `electron/main.ts` | `6116044082b404fbe634cb5ad0282ca16ef4fde224ac1237933ce8054346adf0` |
| `electron/runtime-control-ipc.ts` | `970583be61674d8818046108d5129df90d06484d64c94ee904bbfedb2d0f2fc4` |
| `electron/runtime-helper-bundle.ts` | `f60f6486051c311d8a81026c5b7236490bced983338e3827efc915bb2870086e` |
| `package.json` | `c51da05e5221f2e858c484c7c2760b2154b53639f3074b254abf5792cca32ad0` |
| `scripts/afterpack-runtime-helper.mjs` | `1b38ae363b76c55f31e50dbbd79f733479d292724b672e2303e6b54ee20b8e5f` |
| `tests/cli-launcher.test.ts` | `d01c48462e7a91b2a5aa971f6a4115c7bf9a33065b6bf425975376a30320df0c` |
| `tests/runtime-control-ipc.test.ts` | `7caab58dbb02ef8547ffc857ba9a786c48ae18d53d0617267b4d96a29b6370e3` |
| `tests/runtime-helper-bundle.test.ts` | `44fa5a529d8f19a0c28d6da46c286589c157ff6a5e5d08b9f35ea9d2e3330531` |

The diagnostic SIGUSR2 handler is absent from this snapshot.
