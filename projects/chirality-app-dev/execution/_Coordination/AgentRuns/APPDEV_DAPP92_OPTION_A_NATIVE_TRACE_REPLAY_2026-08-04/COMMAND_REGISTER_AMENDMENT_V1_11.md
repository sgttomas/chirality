# Command-register amendment v1.11 — electron-builder cache namespace correction

Status: `FROZEN AFTER SECOND C198 FAILURE; BEFORE C204`

C201-C203 copied and reproduced the exact local Electron archive, but the
second C198 invocation still failed closed before package construction.
Read-only source inspection established that electron-builder passes
`~/Library/Caches/electron-builder` as `@electron/get`'s cache root, not
`~/Library/Caches/electron`. The exact release-directory URL
`https://github.com/electron/electron/releases/download/v43.2.0/` hashes to
`eee4c0a11146d71f2a23f97ebe56f88f3317ed947626839ecfe7a163d32c09b8`
under the package's `Cache.getCacheDirectory` algorithm.

The following commands copy the same already hash-bound public archive into
that exact isolated cache namespace. No network call, owner configuration,
credential, environment read, or product-source change is involved. Corrected
C198 is then retried byte-for-byte unchanged one final time.

| ID | Class | State | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C204 | temporary product reconstruction/runtime | AUTHORIZED_UNPRIVILEGED | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/home/Library/Caches/electron-builder/eee4c0a11146d71f2a23f97ebe56f88f3317ed947626839ecfe7a163d32c09b8` | Create the exact isolated electron-builder cache directory. |
| C205 | temporary product reconstruction/runtime | AUTHORIZED_UNPRIVILEGED | `/bin/cp -p /Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip /private/tmp/chirality-dapp92-option-a-20260804/home/Library/Caches/electron-builder/eee4c0a11146d71f2a23f97ebe56f88f3317ed947626839ecfe7a163d32c09b8/electron-v43.2.0-darwin-arm64.zip` | Copy only the exact public Electron archive. |
| C206 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/home/Library/Caches/electron-builder/eee4c0a11146d71f2a23f97ebe56f88f3317ed947626839ecfe7a163d32c09b8/electron-v43.2.0-darwin-arm64.zip` | Must reproduce `ad4a0ae3…fe28` before retry. |

If the next C198 invocation fails, the attempt stops and performs mandatory
rollback; no further packaging recovery is inferred.
