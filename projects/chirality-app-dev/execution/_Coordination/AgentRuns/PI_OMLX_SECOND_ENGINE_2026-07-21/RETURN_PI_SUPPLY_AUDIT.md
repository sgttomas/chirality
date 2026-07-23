# Pi 0.80.10 Offline Supply-Chain and Packaging Audit

**Result: CONDITIONAL**

**Scope:** bounded offline review of `frontend/package.json`, `frontend/package-lock.json`, the installed `@earendil-works/pi-coding-agent@0.80.10` publication, its published `npm-shrinkwrap.json`, and its installed dependency closure. No network request, vulnerability audit, source/package/lock edit, reinstall, or package build was performed.

**Actual model:** `gpt-5.6-sol`

## Executive ruling

The requested Pi release is exactly pinned, its top-level tarball has a valid SHA-512 lock integrity, its published shrinkwrap resolves a complete 139-package nested closure, all resolved artifacts use the npm registry over HTTPS, the locally cached Pi-family tarballs match the registry metadata integrities available offline, the only two install lifecycles in the nested closure are bounded and non-networking, and the public SDK imports successfully under Node `24.18.0`.

It is not yet acceptable as an unconditional production packaging pass for two reasons:

1. The published shrinkwrap and Chirality lock omit `integrity` for the three Pi-owned nested packages `@earendil-works/pi-agent-core`, `@earendil-works/pi-ai`, and `@earendil-works/pi-tui`, even though cached registry metadata supplies SHA-512 integrities for all three. A clean install therefore lacks lock-enforced content integrity for those three tarballs.
2. Chirality's current explicit `asarUnpack` covers only the Claude SDK. Pi carries nested Mach-O `.node` binaries and a filesystem-loaded WASM module. A fresh packaged Pi import/turn and asset-location proof has not yet been run, and the current explicit packaging policy does not document how those files remain loadable from the packaged app.

The license inventory is permissive, but redistribution closeout also needs a third-party notice/license artifact because the four Pi publications declare `MIT` while shipping only a one-word `MIT` statement in README files, not the full MIT license notice.

## Pin and lock findings

- `frontend/package.json` pins `@earendil-works/pi-coding-agent` exactly to `0.80.10`; no range operator is used.
- The project lock is npm lockfile v3 and records the top-level artifact as:
  - resolved: `https://registry.npmjs.org/@earendil-works/pi-coding-agent/-/pi-coding-agent-0.80.10.tgz`
  - integrity: `sha512-aL4apbupCHiVLSXASXvRzH4Q2vmtfrDa+0s909CJuVu/GgGylbDzr7oyF1mPmip5E+VxYYxKWmph4hV04wUcQg==`
- Pi publishes an npm lockfile-v3 `npm-shrinkwrap.json`. Its 139 nested package entries are reproduced one-for-one beneath `node_modules/@earendil-works/pi-coding-agent/node_modules/` in Chirality's lock: no missing entries and no version, resolved-URL, or integrity mismatches were found.
- All 139 nested entries have npm registry HTTPS `resolved` URLs. No git, local-file, HTTP, or alternate-registry resolution was found.
- `npm ls --all --offline --json` reports no dependency problems and resolves the requested package as `0.80.10`.
- The Pi-owned runtime packages resolve together at `0.80.10`: coding-agent, agent-core, pi-ai, and pi-tui.
- All 95 dependency manifests that declare a Node engine accept Node `24.18.0`; Pi itself requires `>=22.19.0`.

### Missing lock integrity

The following exact tarballs have `resolved` URLs but no `integrity` field in both Pi's shrinkwrap and the corresponding nested entries copied into Chirality's lock:

| Package | Version | Offline registry/cacache SHA-512 |
|---|---:|---|
| `@earendil-works/pi-agent-core` | `0.80.10` | `sha512-nwnOR3SuLYGRFfyQm8ri4Nj5VGVAvAM9GuqQd3u7BUQj0d6hmD2F8w7OHAAjThE3CuySIdM+v8E22QJG6/RfCg==` |
| `@earendil-works/pi-ai` | `0.80.10` | `sha512-Moe/H8c87yacDGK9dPbWphZNjVsrb3nTrIHycOQJAkFEnY9PYxOOd74+ny44kATfPU9Dm7aTHefar3pZF+UKUA==` |
| `@earendil-works/pi-tui` | `0.80.10` | `sha512-c2JO29PbhKPEQ6fgHQKAl0WhwuFqzWfzspMmP+8B5tpDuP+0mvarRbKKg8gq4b+pQx/QX+6aVS4ko7deoyjQjg==` |

The cached tarballs for all four Pi-owned publications, including coding-agent, were independently SHA-512 hashed during this audit and match their offline registry metadata. This establishes the integrity of the artifacts installed on this machine; it does not repair clean-install enforcement in the committed lock.

**Required mitigation before production acceptance:** use a reproducible dependency mechanism that records and enforces the three missing SRIs. Prefer an upstream corrected Pi shrinkwrap or a documented, repeatable lock-generation/vendor step over an unexplained manual lock edit. Add a CI assertion that every non-local production `resolved` artifact in the Pi closure has `integrity`, then prove a clean offline `npm ci` from the approved cache/artifact mirror.

## Lifecycle-script findings

Pi itself and its Pi-owned direct dependencies have no dependency-install lifecycle. Exactly two packages in Pi's nested closure are marked with install scripts:

| Package | Lifecycle | Audited behavior |
|---|---|---|
| `@google/genai@1.52.0` | `preinstall` | Executes only `echo 'preinstall: no-op'`. Its source-tree `prepare` script is listed in the manifest but is not shipped and is not an npm registry dependency-install lifecycle. |
| `protobufjs@7.6.4` | `postinstall` | Reads its own and its dependent's `package.json` and may write a compatibility warning to stderr. It performs no network call, subprocess launch, or file mutation. |

No other Pi-closure entry is marked `hasInstallScript`. This finding is **PASS** for the audited version. Retain an install-script allowlist check in CI because the published shrinkwrap can change only when the pinned Pi version changes.

## License findings

All 139 nested lock entries declare a recognized license:

| SPDX declaration | Count |
|---|---:|
| MIT | 66 |
| Apache-2.0 | 46 |
| BSD-3-Clause | 13 |
| ISC | 8 |
| BlueOak-1.0.0 | 5 |
| 0BSD | 1 |

No copyleft, noncommercial, custom, or missing declaration was found in the lock inventory. Pi coding-agent, agent-core, pi-ai, and pi-tui each declare `MIT`; their published READMEs say only `MIT`, and the installed publications do not include the full MIT license notice.

**Required mitigation before redistribution:** generate and ship a third-party notices artifact containing the full applicable license texts and copyright notices for the exact packaged closure, including a verified upstream MIT notice for each Pi-owned package. A package manifest's `MIT` label alone is not a redistribution notice.

## Native, WASM, and payload findings

The installed Pi publication contains 18,577 files totaling approximately 122.2 MiB of file content (about 173 MiB allocated on this filesystem), of which its nested `node_modules` account for most of the payload. The closure includes provider SDKs for Anthropic, AWS Bedrock, Google, Mistral, and OpenAI even though the milestone authorizes only explicit oMLX `openai-completions` behavior. Their presence is an upstream dependency/payload fact and must not become runtime provider authority.

Relevant executable assets include:

- `@silvia-odwyer/photon-node/photon_rs_bg.wasm` — WebAssembly MVP binary, 1,881,634 bytes; its CommonJS loader reads the file synchronously by `__dirname`.
- `@mariozechner/clipboard-darwin-arm64/clipboard.darwin-arm64.node` — arm64 Mach-O, 1,447,440 bytes, linker ad-hoc signed.
- `@mariozechner/clipboard-darwin-universal/clipboard.darwin-universal.node` — universal clipboard native package, 2,954,768 bytes.
- `@earendil-works/pi-tui/native/darwin/prebuilds/darwin-arm64/darwin-modifiers.node` — arm64 Mach-O, 50,200 bytes, linker ad-hoc signed.
- Additional x64, Windows, and Linux optional native packages and an example Doom WASM file are present in the installed publication.

The public Pi module imports successfully in plain Node `24.18.0`, and the intended `createAgentSession` export is present. Photon is lazy-loaded; TUI native modifiers and clipboard native bindings are also feature-specific. Therefore a bounded text/tool child can avoid executing them, but packaging still must not rely on that assumption without a packaged proof.

## Electron packaging implications

Current Chirality configuration packages `node_modules/**/*` into ASAR and explicitly unpacks only Claude SDK paths. Consequences:

- Pi's nested dependency structure is material: asset patterns must address paths beneath `node_modules/@earendil-works/pi-coding-agent/node_modules/`, not assumed hoisted paths.
- Electron ASAR virtual filesystem reads may be sufficient for Photon WASM, but that must be proven in the packaged runtime. Native `.node` modules cannot be treated as ordinary archived JavaScript; electron-builder's smart unpack behavior is not a substitute for a recorded project guarantee.
- The broad `node_modules/**/*` rule is likely to include unused Pi docs/examples, remote-provider SDKs, non-arm64 optional binaries, and example WASM. This increases payload and review surface.
- The Pi package is ESM and Chirality's adapter uses dynamic `import()`. The package proof must exercise the Next/Electron server bundle, not only a source-tree Node import, so dependency tracing/externalization is covered.

**Required packaging mitigations and proofs:**

1. Add explicit, reviewed `asarUnpack` handling for the Pi nested native/WASM assets that remain in the application, or exclude unreachable optional native/image/TUI functionality and prove the bounded adapter still imports and runs. Do not unpack the entire 122 MiB closure without assessing payload and exposure.
2. Add package filters for demonstrably unused docs, examples, cross-platform binaries, and provider payload only where module resolution remains deterministic; otherwise record them as an accepted packaged residual.
3. Run `desktop:pack`, inspect `app.asar` plus `app.asar.unpacked`, and assert the exact Pi package/version, all required nested modules, and required loadable assets are present at the paths used at runtime.
4. Execute the planned offline scripted packaged Pi turn without a global Pi installation. The proof must import the adapter from the packaged Next/Electron process, keep built-ins and ambient resources disabled, call only the fake loopback oMLX provider and governed read-only tool, and terminate cleanly.
5. If any native module remains packaged/reachable, verify it loads under Electron 43's embedded Node 24 runtime and is included in final app signing/notarization. Source-tree Node loading is not an Electron ABI/signing proof.
6. Preserve behavioral isolation: construct only the explicit oMLX `openai-completions` model and custom Chirality resource/tool surfaces. Never expose the transitive remote-provider SDKs, Pi update/catalog/telemetry paths, native tools, or ambient configuration merely because they are present on disk.

## Acceptance disposition

| Area | Result |
|---|---|
| Exact direct pin | PASS |
| Nested resolution completeness | PASS |
| Registry/protocol provenance | PASS |
| Cached artifact hashes on this machine | PASS |
| Clean-install lock integrity | **CONDITIONAL — three missing SRIs** |
| Install lifecycle review | PASS |
| Node 24.18 compatibility declarations | PASS |
| License declarations | PASS |
| Redistribution notices | **CONDITIONAL — full notices not shipped by Pi publications** |
| Source-tree SDK import | PASS |
| Electron ASAR/native/WASM policy | **CONDITIONAL — explicit policy/proof required** |
| Offline packaged Pi turn | NOT RUN in this bounded no-write audit |

Do not promote this dependency tranche to unconditional production acceptance until the missing-integrity enforcement, redistribution notices, and packaged-runtime proofs above are closed. No finding here requires changing the approved behavioral boundary: Pi remains opt-in, oMLX-only, loopback-only, without built-ins or ambient resources.

## Integration-owner mitigation closeout

**Closeout result: PASS WITH RECORDED PAYLOAD AND ADVISORY RESIDUALS**

The integration owner closed the three conditional findings without changing the approved behavioral boundary:

- Added the three independently verified SHA-512 values to Chirality's lock and added `npm run pi:supply-chain`, which now proves that all 140 production artifacts in the Pi closure resolve from the HTTPS npm registry and carry SHA-512 integrity. The verifier also fixes the install-script allowlist to `@google/genai` and `protobufjs`.
- Added packaged `frontend/THIRD_PARTY_NOTICES_PI.md` with the full upstream Pi MIT notice and verified its presence in the packaging policy.
- Added explicit nested and flattened Pi native/WASM `asarUnpack` rules, externalized the Pi server package from the Next bundle so its optional browser/TUI closure is not evaluated during route loading, passed `desktop:pack`, inspected the packaged Photon WASM asset, and passed `npm run harness:validate:pi-packaged-proof`. That proof invokes the packaged production harness turn route, resolves Pi `0.80.10` from the packaged `app.asar`, authenticates to a temporary loopback fake provider, permits only `read_file`, persists canonical evidence, and reaches terminal success without a global Pi installation.

The packaged closure remains large because Pi brings optional provider and platform payloads; this is a size/review residual, not runtime provider authority. The adapter constructs only the explicit oMLX model and Chirality-owned tools/resources. The install reported dependency advisories, but a fresh remote `npm audit` was not performed because it would disclose the project dependency graph to the registry without separate owner authorization. Neither residual authorizes release, remote providers, Pi-native tools, or broader capability.
