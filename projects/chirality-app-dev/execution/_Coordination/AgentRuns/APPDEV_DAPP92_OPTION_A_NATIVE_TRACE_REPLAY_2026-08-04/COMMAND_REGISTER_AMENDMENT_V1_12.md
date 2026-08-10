# Command-register amendment v1.12 — exact offline cache correction

Status: `OWNER APPROVED — FROZEN BEFORE ATTEMPT-4 C096`

This immutable adopted copy is byte-for-byte equivalent in operative command
scope to `COMMAND_REGISTER_AMENDMENT_V1_12_PROPOSED.md`. The exact owner token
is transcribed in `OWNER_ATTEMPT4_COMMAND_APPROVAL_ADOPTION.md`.

Amendment v1.11 made its third Attempt-3 C198 invocation terminal on failure.
The owner has approved one fourth and final retry. No fifth retry is inferred.

Attempt 4 executes only:

1. existing C096-C105;
2. existing C152-C177;
3. new C207-C209 below;
4. one byte-identical existing C198;
5. existing C179-C184 only if C198 passes; and
6. mandatory existing C185-C195 plus C199-C200 on every terminal path.

| ID | Class | Adopted state | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C207 | temporary product reconstruction/runtime | OWNER_APPROVED | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/home/Library/Caches/electron-builder/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621` | Create only the exact proven isolated cache directory. |
| C208 | temporary product reconstruction/runtime | OWNER_APPROVED | `/bin/cp -p /Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip /private/tmp/chirality-dapp92-option-a-20260804/home/Library/Caches/electron-builder/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip` | Copy only the already-local hash-bound public Electron archive. |
| C209 | read-only/unprivileged | OWNER_APPROVED | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/home/Library/Caches/electron-builder/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip` | Must reproduce `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`; otherwise stop and roll back. |
| C198 | temporary product reconstruction/runtime | OWNER_APPROVED FOR ONE FINAL RETRY | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run desktop:pack` | One byte-identical retry only; exact frontend cwd; no network authority. Stop and roll back on any failure or network attempt. |

This amendment adds no network, debugger, helper/GUI launch, signal, replay,
credential, environment-dump, release, Git, TM, or foreign-loop authority.
C196/C197 approval remains separate and unused.
