# PR761 daemon project-reference repair — author return

Status: `AUTHOR_STATIC_CHECKS_PASS__FROZEN_FOR_REVIEW`

The isolated publication closure now adds exactly one TypeScript project reference in `projects/chirality-runtime/packages/daemon/tsconfig.json`: `{ "path": "../native-admission" }` appears after `../core` and before `../engine-pi-omlx`. The file changed from 345 bytes / `3b14197e0ee6cc749515c27953f5f20138404f98323be386655a7c3a58122833` to 394 bytes / `0bc20ec8bdb3348def4739751609e173745e12d8b4e6e346e78d692c173c2c9b`.

Static checks pass. The daemon package already depends on `@chirality/native-admission` with specifier `*`. Native admission references only `../core` and does not reference daemon. Focused directed reachability over the permitted project-reference arrays finds no return path from native admission to daemon, so the added edge does not introduce a cycle. The Runtime root solution already lists both daemon and native admission.

All 29 accepted Runtime R V3 source-selection members still match their accepted SHA-256 values and byte counts. The handed-off closure was Git-clean before this edit; afterward Git reports only `projects/chirality-runtime/packages/daemon/tsconfig.json` changed, and its diff is exactly `PATCH.diff`. No second source edit or broader semantic change is required.

No npm, TypeScript compiler, node-gyp, native compilation, test, dependency-setup, network, supplier, account, product-process, delegation, or Git mutation action was performed. No build PASS is claimed. Clean build validation remains for the required PR CI, including PEC and Harness runs after CHANGE commits the reviewed repair.

Closure verdict: author work complete and frozen for independent review; governed publication/CI closure remains pending.
