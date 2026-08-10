# Deterministic offline-source analysis after Attempt 4

Status: `EVIDENCE-BOUND — NO EXECUTION AUTHORITY`

## Observed Attempt-4 boundary

The sole C198 invocation reached electron-builder's Electron `43.2.0`
Darwin-arm64 packaging stage and then failed `getaddrinfo ENOTFOUND github.com`.
The exact raw bytes remain losslessly preserved in
`C198_STDOUT_STDERR_RAW.txt.gz`; no deeper cause is inferred from those bytes
alone.

## Exact installed-source basis

The dependency projection used by C166-C173 is bound to the current governed
package-lock SHA-256
`5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`.
Its installed `app-builder-lib` package is version `26.15.3` and has package
metadata SHA-256
`3abe63010a62a67512f1dedaae48747081dfe22e22e4f197767bf2f4c51b60f9`.

Bound installed files under
`/Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules/`:

| File | SHA-256 | Relevant lines |
|---|---|---|
| `app-builder-lib/out/electron/ElectronFramework.js` | `4c3c4657a77736c3c81f074d70ead251d2e99d4fab1f81ad23c3d96bb1daefa0` | 164-173, 200-226 |
| `app-builder-lib/node_modules/@electron/get/dist/esm/index.js` | `b4fd1cc41680a5892f6125b08c604a2be0064c286ce81f330f524075e28af4d1` | 19-52, 90-140 |
| `app-builder-lib/node_modules/@electron/get/dist/esm/Cache.js` | `f8f8f15d54662bf621a3f6bd603767b68bc65ea0720e21fff5acba74238f14bb` | 19-44 |
| `app-builder-lib/scheme.json` | `5d0f9887f93a5ec9994c0c0ee86fbeb59fe63042e30051a94f4b0ce2a0835f9f` | 9254-9267 |

## Deterministic findings

1. Under an isolated HOME, the nested `@electron/get` default cache root is
   `HOME/Library/Caches/electron`, not `HOME/Library/Caches/electron-builder`.
   Direct evaluation of the exact bound `Cache` class with
   `HOME=/private/tmp/chirality-dapp92-source-proof-home` printed
   `/private/tmp/chirality-dapp92-source-proof-home/Library/Caches/electron`.
   Its exact artifact-URL key is the already proved `9c4e224...e621`.
   Therefore Attempt 4 seeded the right URL-key directory under the wrong
   default cache root.
2. A default-cache correction is still not an offline remedy. Attempt 3's C201
   already seeded the exact zip under `Library/Caches/electron/9c4e224...e621`.
   On a cache hit, the exact nested `@electron/get` source calls
   `validateArtifact`; absent embedded `checksums`, it downloads
   `SHASUMS256.txt` with `ElectronDownloadCacheMode.Bypass` and explicitly says
   to load checksums fresh every time. This deterministically identifies the
   remaining network request class and proves that another cached-file or
   namespace guess is not a supported next step.
3. The exact installed `app-builder-lib` source provides a direct offline
   route: when `electronDist` is a non-empty string ending in `.zip`, it
   validates path existence and calls `extractArchive` directly. The default
   `downloadElectronArtifactZip` path is not entered. The installed schema
   accepts `electronDist` as a string.

## Evidence-supported next option

Use the exact local archive, independently hash-verified as
`ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`,
through a temporary `electronDist` overlay in both reconstructed packager
configs. This is not a cache guess and does not disable checksum validation;
the run itself binds the archive hash before any package command. The overlay
must be temporary, exact-hash checked, and rolled back on every path.

No retry or other authority follows from this analysis.
