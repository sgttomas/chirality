# Attempt-3 terminal fresh adversarial verifier return R2

## Verdict

`PASS_FOR_APPROVAL_STOP`

This verdict supports only presentation of the exact Attempt-4 command token.
It does not authorize or credit reconstruction, packaging, launch, LLDB,
signal, replay, network, credentials, release, or Git effects.

## Independently reproduced findings

1. The current Attempt-3 evidence records C175 as four files / 30 tests PASS,
   C176 PASS, C177 PASS, and three byte-identical C198 invocations failing at
   `getaddrinfo ENOTFOUND github.com` before package construction. C179-C184
   are explicitly `NOT RUN`; no package identity or topology is claimed.
2. Current records contain no numeric helper or GUI PID, launch result,
   C196/C197 invocation, LLDB output, first SIGTERM, polls, or replay result.
   The separately approved C196/C197 authority remains unused and is not
   implied by the proposed Attempt-4 commands.
3. The fixed run root `/private/tmp/chirality-dapp92-option-a-20260804` is
   absent. Frontend Git status is empty. All five candidate additions,
   `node_modules`, `dist`, `dist-runtime-helper`, `dist-electron`,
   `dist-runtime`, and `.next` are absent. The eight current baseline/lockfile
   SHA-256 values exactly reproduce the recorded C194 values:
   `850f7b00...335b`, `16ad6688...d1f`, `5006bef6...026a`,
   `1f14df17...fa53`, `5c8fce2a...1a56`, `a6759be0...5558`,
   `1918ae7d...91e9`, and `f8b6d8c2...36be6`.
4. The local Electron archive exists at the exact cited operator-cache path.
   Its independently recomputed SHA-256 is
   `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
5. Read-only extraction of installed-version `@electron/get` 3.1.0 from the
   npm content cache reproduced `Cache.getCacheDirectory`: it removes search,
   hash, and filename, formats the containing URL, then SHA-256 hashes it.
   For the exact Electron 43.2.0 artifact URL, the resulting containing URL is
   `https://github.com/electron/electron/releases/download/v43.2.0`, whose
   independently recomputed SHA-256 is
   `9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621`.
   By contrast, v1.11 hashed the trailing-slash release URL and obtained
   `eee4c0a11146d71f2a23f97ebe56f88f3317ed947626839ecfe7a163d32c09b8`;
   that is not the package algorithm's cache key for the artifact.
6. Proposed C207 creates only the exact isolated `electron-builder/9c4e...`
   directory; C208 copies only the already-local hash-bound public archive;
   C209 requires the exact `ad4a0ae3...fe28` hash; and the proposed C198 is
   byte-identical to the frozen corrected `npm run desktop:pack` command. One
   retry is explicit, failure or any network attempt stops, and mandatory
   C185-C195 plus C199-C200 cleanup remains required. This is an exact,
   bounded, offline correction sufficient to put the archive where the
   installed cache algorithm looks; it adds no C196/C197 authority.
7. The requested owner token names exactly C207-C209 and one byte-identical
   C198 retry, binds the local hash-bound Electron 43.2.0 archive to the proven
   `9C4E224` namespace, and excludes network, helper, GUI, LLDB, signal, replay,
   credential, release, Git, and other authority. It is neither broader nor
   narrower than the proposed amendment.

## Evidence hashes recomputed

- amendment v1.9: `6e2069c1bb0f741b7e0d76ec5187a4ef374e0ab16c751fc6e9607b7558867915`
- amendment v1.10: `897440169654c336ce8ac84a6683b8a1304c67ac7ac0588abc1eba0ad72b7985`
- amendment v1.11: `d06d1106fb5b776e7a8a4886c6882371111cea31c387b0384a78b294cc63adf9`
- proposed amendment v1.12: `3a5ad0869e1d10ec550a3b1fd63f0bd649398f414b6746bce06906980c8a73bc`
- Attempt-4 approval request: `8a79b2b7a5eae60d83e1968c3def28dc7f1a93848f5f6e932b01e5da45de056d`
- offline-cache proof: `470f315043a19aaa0d93115750d6fd8944d10bcdfdde28f7be2207d6c16ff1f9`
- captured C198 failure bytes: `9b1ff70e90cfa20f18733cc002e716ebc9cd7cba872554cce250e6e3a3a39cbb`

No excluded operation was performed and no repair was made.
