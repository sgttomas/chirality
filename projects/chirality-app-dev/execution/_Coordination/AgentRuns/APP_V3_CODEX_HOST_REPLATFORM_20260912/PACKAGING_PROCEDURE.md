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
   `npm run build` (Next and Electron), then the packaging entry. The
   current entry is `npm run desktop:dist`; its supply-model phases
   (`pack-electron-with-supply.mjs --runtime-manifest v2`) are re-authored
   for the bundled stock dependency in the spike and the script name may
   change with it. `npm run desktop:verify-dependencies` and
   `npm run electron:supply-chain` remain the dependency-boundary checks.
2. **Sign.** Developer ID signing with hardened runtime over the whole
   bundle, including the bundled Codex binary and the Runtime service. Owner
   act or owner-supplied identity.
3. **Notarize** and staple. Owner act.
4. **Verify the bundle signature and the Codex pin.** `codesign --verify
   --deep --strict` and `spctl --assess` on the stapled bundle; confirm the
   bundled `@openai/codex` version equals the lockfile pin and the binary
   inside the bundle is the one the lockfile resolved. Record both results.
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
