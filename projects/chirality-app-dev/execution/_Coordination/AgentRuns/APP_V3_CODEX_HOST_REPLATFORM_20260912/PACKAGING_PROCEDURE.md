# Packaging procedure (D-GOV-43, topology A2)

Recorded 2026-09-12 under D-GOV-43 item 11 and the A2 supplement; App
application record `../../_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md`.
This short procedure supersedes the applicability of the Stage 9 to 13
twenty-five-step spine (`../APP_V3_DIRECT_TRIAL_20260910/REBUILD_PLAN.md`)
and the Stage 16 to 26 records under `../APP_V3_TRIAL_COMPLETION_20260910/`,
which are preserved unchanged as history. It is not trimmed from them.

## Precondition

One consolidated build follows the eight functional checks (S-1 to S-8) on
the production path from source and a separate independent source review
with no unresolved blocking finding. The build packages the Runtime service
and the lockfile-pinned stock `@openai/codex`; no patched supplier, no
admission addon, no LaunchAgent.

## Steps

1. **Build.** From `frontend/`: `npm run instruction-root:prepare`,
   `npm run runtime:build` (the Runtime workspace, so the service and CLI
   sources bundle from built packages), `npm run build` (Next and Electron;
   `build:electron` also writes `dist-runtime/runtime-service/standalone-bin.mjs`
   and `dist-runtime/runtime-cli/chirality-cli.mjs`), then the packaging
   entry. The entry is `npm run desktop:dist`, which runs the plain
   `scripts/pack-electron.mjs --target dmg` (electron-builder with the
   verified Electron distribution, no supply phases, no runtime manifest,
   no payload bind) followed by `desktop:verify-dependencies`,
   `desktop:verify-codex-pin -- --after-signing` and
   `instruction-root:integrity`. `npm run desktop:pack` is the unsigned
   directory build with the same checks and the pre-signing digest
   comparison. `npm run electron:supply-chain` remains the Electron
   distribution check. Revised by W3 on 2026-09-12: the supply-model
   phases and `pack-electron-with-supply.mjs` are retired with the
   supplier, the admission addon and the LaunchAgent.
2. **Sign.** Developer ID signing with hardened runtime over the whole
   bundle, including the two bundled Codex binaries (`codex` and
   `codex-code-mode-host`, the latter with the JIT entitlement) and the
   Runtime service bundle inside `app.asar`'s sibling resources. The
   identity is selected only through `CHIRALITY_SIGNING_IDENTITY_SHA1`;
   without it the pack script disables keychain discovery and produces an
   unsigned candidate. Owner act or owner-supplied identity. The Runtime
   service child is started through Electron's `utilityProcess`, so the
   `runAsNode: false` fuse stays set and no Node CLI surface is enabled in
   the packaged App.
3. **Notarize** and staple. Owner act.
4. **Verify the bundle signature and the Codex pin.** `codesign --verify
   --deep --strict` and `spctl --assess` on the stapled bundle;
   `npm run desktop:verify-codex-pin -- --after-signing` runs the packaged
   `codex --version` and compares it to the lockfile-resolved version and
   to the staged `codex-package.json` (the pre-signing sha256 comparison
   against the installed platform package is recorded by `desktop:pack`,
   since signing rewrites the binaries). Record both results.
   `npm run verify:version-identity` checks the App's own version identity.
5. **Packaged checks.** Only the checks that exercise a distinct packaged
   or native condition, on the packaged App with a fresh `userData` and its
   own effective Codex home: S-6 (quit, relaunch, continuation of the same
   chat) and S-8 (sign-in and sign-out scoped to Chirality with another
   Codex client's state unchanged), plus step 4. `NATIVE_CHECKLIST.md` is
   the native script.

## Post-build rule (minimum, not ceiling)

S-6, S-8 and the signature and pin verification are the expected minimum
after the build, not a ceiling. Repeat any affected check when a source,
configuration or packaging change invalidates its earlier evidence; for
example, packaged instruction roots resolving differently from development
files (`npm run instruction-root:integrity` is the relevant script), or a
renderer policy change (`npm run proof:packaged-security`,
`npm run proof:network-policy`, `npm run proof:secret-scan`). Do not repeat
unaffected tests merely because another stage has begun; a test runs once
per distinct condition.

## Record

Record the build inputs (source SHA, lockfile pin, Electron version), the
signing and notarization results, the step 4 outputs and the packaged-check
results in this run directory (`RUN_LOG.md` and a dated evidence file). No
observer, payload-bind, governance, seal or supplier-signing step exists.
Native verification of the packaged App is by the owner's designated direct
tester; publishing is the owner's separate explicit approval.
