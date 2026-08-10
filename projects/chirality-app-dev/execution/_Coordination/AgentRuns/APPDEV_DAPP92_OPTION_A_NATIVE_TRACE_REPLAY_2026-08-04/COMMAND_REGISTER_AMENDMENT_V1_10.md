# Command-register amendment v1.10 — offline exact Electron cache repair

Status: `FROZEN AFTER FIRST C198 FAILURE; BEFORE C201`

The first attempt-3 invocation of corrected C198 reached electron-builder but
failed before package construction because the isolated HOME had no Electron
archive. Electron-builder attempted `github.com` and received
`getaddrinfo ENOTFOUND`; no network result or package receives credit. Network
authority is absent and no network escalation is permitted.

Read-only discovery found the exact Electron `43.2.0` Darwin-arm64 archive in
the local operator cache. Its SHA-256 is
`ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
The following commands copy only that public runtime archive into the isolated
run HOME cache. They do not read or copy owner configuration, credentials,
environment, keychain state, or network content. Corrected C198 is then retried
byte-for-byte unchanged.

| ID | Class | State | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C201 | temporary product reconstruction/runtime | AUTHORIZED_UNPRIVILEGED | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/home/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621` | Create only the exact isolated cache directory. |
| C202 | temporary product reconstruction/runtime | AUTHORIZED_UNPRIVILEGED | `/bin/cp -p /Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip /private/tmp/chirality-dapp92-option-a-20260804/home/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip` | Copy only the exact public Electron archive. |
| C203 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/home/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip` | Must reproduce `ad4a0ae3…fe28` before retry. |

No helper, GUI, debugger, signal, credential, release, Git, or foreign-loop
authority is added.
