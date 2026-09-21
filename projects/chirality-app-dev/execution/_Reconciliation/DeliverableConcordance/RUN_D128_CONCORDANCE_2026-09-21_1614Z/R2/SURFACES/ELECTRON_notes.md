# ELECTRON capability inventory: notes (R2, R1b area TASK)

Area: `projects/chirality-app-dev/frontend/electron/**` at the frozen basis `00115c719`.
Output: `ELECTRON_capabilities.csv`, 35 rows (`CAP-ELECTRON-001`…`035`). Validator: `RESULT PASS errors=0 warnings=0`.
No deliverable folders were read. The inventory comes from the code, the evidence pack (`REACHABILITY.csv`, `TOUCHED_PATHS.csv`), import and test greps, and a symbol-level check of every IPC channel against its preload exposure and renderer callers.

## 1. Census

CENSUS rows=35 LIVE=34 LEGACY_ONLY=0 TEST_ONLY=1 UNREACHED=0 ENABLED=31 DISABLED=4

- `PostReleaseBasis` is `NO` on every row.
  - `TOUCHED_PATHS.csv` has no row under `frontend/electron/`.
  - Of the four post-release commits, only `ccb95e06a` touches the area. It changes `plan-export-ipc-contract.ts`, and the change is only the deletion of a trailing blank line. `git show ccb95e06a` confirms no line is blamed to it.
- The pack marks all 27 area modules `LIVE`: 26 from `main.ts` and `preload.ts` as its own entry. The one `TEST_ONLY` row is set at symbol level (§4).
- The four `DISABLED` rows:
  - 019: proof probes, off by default.
  - 032 and 033: credential IPC, stubbed behind the App-owned daemon and not mounted in the live shell.
  - 034: the safeStorage store, which is dead code.

## 2. Granularity rationale

- **One row per behaviour or contract surface.** Where a module is a pure contract (a `*-ipc-contract.ts` file), it is folded into the IPC behaviour it serves. It does not get its own row.
- **`main.ts` (1143 lines) is split by behaviour** rather than kept whole:
  - startup orchestration;
  - userData override;
  - instruction-root resolution;
  - packaged renderer server;
  - egress allowlist;
  - proof probes;
  - the folder picker;
  - folder conveniences (Open Recent and open-file intents);
  - document handoff;
  - quit and teardown.
- **The Runtime service child has two rows:** its lifecycle (host plus launcher), and its configuration and path contract. A deliverable could plausibly own either one alone.
- **`renderer-window-policy.ts` (774 lines) has five rows:**
  - web-preferences hardening;
  - navigation and window-open;
  - CSP;
  - eligible-PDF classification;
  - env-gated probes.
- **Credentials have three rows:**
  - the provider IPC;
  - the legacy Anthropic-only IPC trio, a duplicate surface with a different reach at symbol level;
  - the safeStorage store, which is dead code.
- **App update has three rows:**
  - the checker (feed, semver, policy fetch);
  - the controller state, polling and IPC;
  - the macOS menu and About signal.
- **Product instructions has two rows:** the store, and the IPC.

## 3. Files covered versus total

COVERAGE covered=27 total=27

Every file in the ELECTRON rows of `IMPLEMENTATION_SURFACES.csv` is named in at least one row's `Paths`. None is uncovered.

## 4. Dead, unreached, disabled or retired code observed

- **Credential IPC is registered but non-functional at the frozen basis** (rows 032 and 033).
  - `main.ts:990` registers all six `chirality:*api-key*` handlers, and the preload exposes all six.
  - The App-owned Runtime composition wires a stub credential port: `projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts:225`.
    - `status()` returns `{configured:false}` with no `source`. The fail-closed parser in `api-key-ipc.ts:120-125` therefore rejects it, and every status call returns "Runtime daemon returned an invalid credential status".
    - `set` and `remove` throw `ENGINE_UNAVAILABLE` through `offline` (line 180).
  - On the renderer side:
    - `settings-view.tsx:35` renders `ApiKeySettings` only when `!hosted`, and its sole caller (`shell-frame.tsx:404`) always passes `hosted`.
    - The only other mount is `shell-frame.tsx:302`, inside the legacy default-variant chrome. SHELL rows record that this chrome renders only on the 404 route.
  - The `omlx` provider has no engine in the App-owned composition.
- **Legacy `apiKey` trio never called by the renderer.** `api-key-settings.tsx:73-80` uses `chirality.apiKey` only when `providerApiKey` is absent, and `preload.ts:86` always exposes `providerApiKey`.
- **`api-key-storage.ts` is dead except for one guard.**
  - Its only production import is `isProviderCredentialId`, from `api-key-ipc.ts`. That is why the pack shows the module as `LIVE`.
  - These have no production or script importer, and no Runtime package imports them:
    - `SafeStorageCredentialStore`;
    - the encrypted-blob store, read, retrieve and remove functions;
    - `loadStoredKeyIntoGlobal`;
    - the `*ApiKey` compatibility aliases.
  - Row 034 is therefore tagged `REACH=TEST_ONLY` at symbol level.
- **Sender-origin checks are missing on two preload-exposed channels.**
  - `chirality:select-directory` (`main.ts:553`) is registered before the renderer origin is known.
  - `chirality:runtime-connectivity-query` (`main.ts:747`).
  - Every other invoke channel applies `isAuthorizedSender`.
  - This is not dead code. It is recorded so the forward pass can compare it with the sender-authorization claim.
- **Preload exposure versus main registration.**
  - Every main-registered invoke channel is exposed by the preload. No handler is registered only in main.
  - `platform` and `versions` on `window.chirality` have no renderer consumer. This was checked by grep over `src/`, excluding tests.
- **Proof instrumentation, off by default** (row 019):
  - `CHIRALITY_NETWORK_POLICY_PROBE_URLS` (`main.ts:236-246, 317-321`);
  - `CHIRALITY_RENDERER_SECURITY_PROBE=1` (`renderer-window-policy.ts:589, 744`; `main.ts:1004`).
  - The probe route list still names the legacy `/chat`, `/pipeline` and `/workbench` routes.
- **The egress allowlist still names `api.anthropic.com`** (`main.ts:133`). Codex is the sole engine, and no live renderer code calls Anthropic. The name is also pinned by `contract-pins.manifest.ts`.
- **The update source is always configured.** `resolveAppUpdateSource` (`app-update-source.ts:17`) always returns the GitHub source, so the `no-release-source` and unconfigured-description branches cannot be reached at the frozen basis.
- **Inline desktop PDF preview is deliberately off** (`preload.ts:77`). The PDF classification in `renderer-window-policy.ts` stays live for the working-root file route.
- **Teardown asymmetry.** `teardown` (`main.ts:1047-1058`) does not remove these handlers:
  - `folder-register-recent`;
  - `folder-open-ready`;
  - `product-instructions`;
  - `plan-export-dialog`.
  - This is harmless because the process exits.
- **Duplicate constants.** `CODEX_SIGNED_BINARIES` and `CODEX_JIT_BINARY` in `codex-executable.ts` are redeclared with different path prefixes in `scripts/sign-electron-runtime-v2.mjs`.
- **Retired features, named in comments only, with no code left:**
  - the LaunchAgent install, start, stop and uninstall verbs;
  - the oMLX residency IPC.
  - Both are named in `runtime-control-ipc.ts`.
- **No direct test found:**
  - `runtime-shutdown-policy.ts`;
  - `runtime-service-launcher.ts` (only a source-boundary scan);
  - instruction-root resolution in `main.ts`;
  - `initializeGui` and the egress functions. These are module-private, and only source pins and the network-proof script test cover them.

## 5. Method friction with §5.2

- **REACH is module-level, but several findings here are symbol-level.**
  - `api-key-storage.ts` is `LIVE` only through one guard function.
  - The legacy `apiKey` channels are registered and exposed but never called.
  - I tagged the dead store `REACH=TEST_ONLY at symbol level` and explained why in `Notes`.
  - Proposal: allow an explicit `REACH=LIVE(module)/TEST_ONLY(symbol)` form, or a `SYMBOL-DEAD` marker, so forward workers do not read a `LIVE` module as live behaviour.
- **STATE is ambiguous for env-gated behaviour.** I used this rule:
  - proof or diagnostic instrumentation that does nothing without an explicit opt-in is `DISABLED`;
  - a configuration override that changes product paths when set (`CHIRALITY_USER_DATA`) is `ENABLED`, with the gate named.
  - Proposal: state that rule in §5.2.
- **Cross-area causes of DISABLED.** The credential IPC is disabled because of a Runtime stub and a renderer gate, both outside this area. §5.2 does not say whether STATE describes the area's code alone or the end-to-end behaviour. I used end-to-end and cited the external lines.
  - Proposal: state that STATE is end-to-end at the frozen basis, and that foreign gates are cited by path and line.
- **`EntryPoints` mixes three kinds of item:** exported symbols, `window.chirality.*` bridge members, and renderer consumer paths. For an IPC area, a separate `Channels` column, or a convention such as `ipc:<channel>`, would make channel-level concordance mechanical.

## 6. Effort

- **Files read:** about 20 electron files, in full or in ranges; `main.ts` and `preload.ts` in full.
- **Other files, by grep or short ranges:**
  - about 12 renderer consumer files;
  - `contract-pins.manifest.ts`;
  - two Runtime daemon files, to trace the credential endpoint.
- **Scripts and tools:** test-to-module mapping and path-existence checks were done with small greps and a scratchpad script. Git was used read-only: `show` on the four post-release commits.
- **Context:** comfortable, not tight.
