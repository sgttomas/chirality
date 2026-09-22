# BUILD capability inventory — notes (R2, area BUILD)

Area: the `Area=BUILD` rows of `R1_INVENTORY/IMPLEMENTATION_SURFACES.csv` (38 files: `frontend/scripts/**`,
`frontend/package.json`, `next.config.mjs`, `tsconfig.json`, `tsconfig.electron.json`), read at frozen basis
`00115c719`. Output: `BUILD_capabilities.csv`, 41 rows (`CAP-BUILD-001`…`041`).
Validator: `RESULT PASS errors=0 warnings=0`. No deliverable folders were read.

## 1. Census

`CENSUS rows=41 LIVE=20 LEGACY_ONLY=10 TEST_ONLY=11 UNREACHED=4 ENABLED=35 DISABLED=6`

- `PostReleaseBasis` is `NO` on every row. `TOUCHED_PATHS.csv` has no row under
  `projects/chirality-app-dev/frontend/**`; outside the Runtime its only paths are `exports/chirality-app/*` and a
  tranche manifest (all `ccb95e06a`).
- The six `DISABLED` rows:
  - signing policy (`CAP-BUILD-016`) and post-sign verification (`017`): no identity by default, `pack-electron.mjs:86-95`;
  - packaged Agent SDK proof (`031`), live packaged SDK read-tool proof (`032`) and packaged Pi proof (`033`):
    they cannot pass on an A2 package, and the release workflow is blocked;
  - the pec scratch server (`038`): opt-in gate `PEC_BRIDGE_IT=1`.

## 2. Granularity rationale

- One row per build, packaging, signing or proof behaviour a release/installer package could own.
  `package.json` is split by contract surface rather than treated as one file:
  - Next build (`001`);
  - dev chain (`004`);
  - typecheck/test (`005`);
  - desktop chains (`008`);
  - electron-builder app config (`009`);
  - fuses (`010`);
  - Codex staging (`011`);
  - dependency pins/overrides (`021`).
- `build-electron.mjs` has two rows: Electron main/preload bundling (`002`) and the Runtime service/CLI bundles for
  `extraResources` (`003`). Different deliverables plausibly own them.
- Signing has two rows: the policy/identity gate (`016`) and post-sign `codesign` verification (`017`). The identity
  gate in `pack-electron.mjs` is folded into `016`.
- Packaging verifiers each get a row (Codex pin, Electron dist pin, afterPack inventory, dependency boundary,
  instruction-root integrity). Each is a distinct gate in the `desktop:pack`/`desktop:dist` chains.
- Release-evidence generators (SBOM, notices, version identity) and release proofs (network policy, packaged
  security, secret scan) each get a row, per the brief.
- Two things were folded:
  - the vitest-based `harness:validate:agentsdk-*` npm scripts, into the packaged Agent SDK proof row (`031`);
  - `harness-section9-manifest.json`, into the section 9 row (`027`).
- Reach rule for scripts, applied consistently:
  - `LIVE`: in the build/pack/dist chain or an electron-builder hook/config key, plus standalone release-evidence npm
    scripts (`sbom:generate`, `notices:generate`, `verify:version-identity`). These are flagged "not chained" in Notes.
  - `TEST_ONLY`: validation and proof harnesses (CI or manual).
  - `LEGACY_ONLY`: scripts that serve only the Claude SDK / Pi path, or that nothing invokes (`UNREACHED`).
  - The dev chain (`004`) is tagged `LIVE` as a developer run path, not packaging.

## 3. Files covered versus total

`COVERAGE covered=38 total=38`

- No uncovered files.
- Some rows also name the `frontend/build/` plists and icons (`entitlements.mac*.plist`, `icon.icns`,
  `icon-macos.svg`) in `Paths`. These are not in the area list, so they do not count toward coverage.

## 4. Dead, unreached, disabled or retired code observed

- **No notarization anywhere.** There is no `afterSign`/notarize hook, no `notarize` key and no notarization script.
  The only mentions are "evidence only, no notarization" disclaimers (`generate-sbom.mjs:23`,
  `generate-third-party-notices.mjs:26`, `validate-release-quality-evidence.mjs:95`). The release CI workflow fails
  closed if Apple notarization credentials are present.
- **Signing is off by default.**
  - `signingEnvironment` sets `CSC_IDENTITY_AUTO_DISCOVERY=false` unless `CHIRALITY_SIGNING_IDENTITY_SHA1` is set
    (`pack-electron.mjs:86-95`).
  - `.github/workflows/desktop-release-template.yml` forces the unsigned posture.
  - The `mac.sign` hook and `verifySignedBundle` are therefore dormant in every configured path.
- **The release workflow is hard-blocked.** `desktop-release-template.yml` exits 1 at "Block release workload pending
  deferred S0 qualification", before `npm run desktop:dist`. The workflow is outside this area; it is cited as the
  gate for `031`.
- **Legacy proofs contradict the A2 package boundary.**
  - `verify-packaged-agent-sdk-runtime.mjs`, `run-live-packaged-agent-sdk-read-tool-proof.mjs` and
    `run-packaged-pi-runtime-proof.mjs` expect Claude Agent SDK or Pi packages inside the packaged app.
  - `verify-packaged-dependency-boundary.mjs` forbids exactly those packages in `app.asar`.
  - The release workflow still calls the Agent SDK proof after the boundary check. That sequence cannot pass.
- **Stale dependency assumptions.** Both of these conflict with the `package.json` state at the basis:
  - `verify-pi-supply-chain.mjs:23` requires the Pi packages in `dependencies`, but they are `devDependencies`.
  - `generate-third-party-notices.mjs:46-62` requires Pi and `@chirality/engine-*` in the production closure.
  - These are static readings; nothing was executed.
- **Anthropic-era network posture.**
  - `run-network-policy-proof.mjs:20` allowlists only `api.anthropic.com`.
  - `run-packaged-security-proof.mjs` markers include `api.anthropic.com` and an `@anthropic-ai/sdk` unpacked path
    (`:22`, `:145-146`).
  - The network proof's default output root points into an `execution/` deliverable folder (`:13-16`). Scripts
    writing into deliverable folders is a separation concern.
- **Section 8/9 validators carry legacy vocabulary.**
  - `harness-section9-manifest.json` evidence files are legacy engine modules (`agent-runtime-contract.ts`,
    `turn-engine.ts`, `sdk-message-mapper.ts`, which are LEGACY_ONLY in `REACHABILITY.csv`).
  - Section 8 check IDs include `sdk_native_stream` and `permissions_dontask`.
- **The CI Runtime fixture composes the legacy stub engine.** `controlled-ci-runtime.ts:15-16` uses
  `StubAgentSdkManager` and `LegacyAgentEngineAdapter`. CI route validation therefore runs against the legacy
  adapter, not Codex.
- **UNREACHED scripts** (no npm script, CI or test caller):
  - `generate-macos-icon.mjs` (self-declared one-time);
  - `run-pec-bridge-rehearsal.ts`, `run-dapp52-live-llm-demo.ts`, `run-dapp52-live-sdk-probe.mjs` (legacy
    D-APP-52 drivers).
- **Minor stale comment.** `generate-macos-icon.mjs` says `sharp` is pinned to 0.35.3; `overrides` pins 0.35.4.
- **Duplicate packing.** `desktop:prepare` ends with `pack-electron.mjs` (dir), and `desktop:pack` packs again. This
  is harmless but redundant.

## 5. Method friction with §5.2

- **The reach vocabulary is module-oriented.** For build scripts, "nothing invokes it" is ambiguous. A standalone
  npm script (for example `sbom:generate`) is invoked by a human, not by a chain.
  - I tagged release-evidence generators `LIVE` and validation proofs `TEST_ONLY`.
  - The generic rule "nothing invokes → LEGACY_ONLY UNREACHED" misfiles a non-legacy one-time tool such as the icon
    generator.
  - Proposal: for BUILD, allow a `MANUAL` qualifier in Notes (`REACH=LIVE; MANUAL`). Reserve `LEGACY_ONLY` for
    legacy-path scripts, and allow `UNREACHED` with a non-legacy reason.
- **STATE for scripts.** It is unclear whether a manual script that needs a live key is DISABLED. I used DISABLED
  only for default-off gates (env, opt-in flag) and for proofs that cannot pass at the basis.
  - Proposal: define `STATE=DISABLED` for BUILD as "not executed in any configured chain or CI path, or gated off by
    default".
- **Out-of-area config.** Out-of-area config such as the `frontend/build/` plists and `.github/workflows/*` gates
  determines BUILD state but is not in the area list. It is cited in Notes and Paths only.

## 6. Effort

- About 30 script headers and export lists were grepped. About 12 files were read in line ranges:
  - `pack-electron.mjs`, `sign-electron-runtime-v2.mjs` and `build-electron.mjs` in full;
  - `package.json` and the two workflows.
- A scratchpad reference scan mapped scripts to tests, CI and other scripts.
- Context was comfortable.
