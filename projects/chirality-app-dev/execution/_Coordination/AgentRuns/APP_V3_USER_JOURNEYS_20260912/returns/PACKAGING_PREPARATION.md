# Packaging preparation

Prepared 2026-09-13T02:48:13Z. TASK, delegated-harness-native child of the campaign parent; no delegation. Read-only preparation complete; dependency acquisition, build, signing and launch have not run. Await parent release after CI and its exact final source SHA.

Current candidate: `6e1e093006bea8ece5a624fdb4bba291a181262d`, branch `codex/user-journey-plan-20260912`. Historical build records establish procedure only, not this candidate's evidence. Parent confirmed campaign PLAN Delivery authorizes actual release identity `3.0.0`, `com.chirality.app`, arm64; Codex pin `0.154.0`, Electron `43.2.0`.

New detached source: `/Users/ryan/.claude/chirality-build-user-journeys-20260912`.
New output: `/Users/ryan/.claude/chirality-build-user-journeys-20260912-out`.
Expected DMG: output plus `/Chirality-3.0.0-arm64.dmg`.
Expected App: output plus `/mac-arm64/Chirality.app`.
Both new paths must be absent before creation; preserve every earlier worktree, App and output. Never reuse the historical A2 path. Build source is outside `/private/tmp` because electron-builder rejects that location.

## Commands after release

The parent supplies the final revision in place of FINAL_SOURCE_SHA. Commands execute sequentially, recording actual exit codes and UTC times; filter every line containing `@` before recording output. No equivalent test-suite reruns.

```sh
git -C /Users/ryan/.codex/worktrees/chirality-ui-refinement-packaged-20260912/chirality worktree add --detach /Users/ryan/.claude/chirality-build-user-journeys-20260912 FINAL_SOURCE_SHA
cd /Users/ryan/.claude/chirality-build-user-journeys-20260912/projects/chirality-runtime
npm ci
cd /Users/ryan/.claude/chirality-build-user-journeys-20260912/projects/chirality-app-dev/frontend
npm ci
npm run instruction-root:prepare
npm run runtime:build
npm run build
export CHIRALITY_ELECTRON_OUTPUT_DIRECTORY=/Users/ryan/.claude/chirality-build-user-journeys-20260912-out
export CHIRALITY_SIGNING_IDENTITY_SHA1=C7F111429F7AC5085484A9DF6F5AE7CFF552DEEF
npm run desktop:dist
npm run verify:version-identity -- --expect 3.0.0 --app-path /Users/ryan/.claude/chirality-build-user-journeys-20260912-out/mac-arm64/Chirality.app --dmg-path /Users/ryan/.claude/chirality-build-user-journeys-20260912-out/Chirality-3.0.0-arm64.dmg
codesign --verify --deep --strict --verbose=2 /Users/ryan/.claude/chirality-build-user-journeys-20260912-out/mac-arm64/Chirality.app
codesign -d --verbose=4 /Users/ryan/.claude/chirality-build-user-journeys-20260912-out/mac-arm64/Chirality.app
spctl --assess --type execute --verbose=2 /Users/ryan/.claude/chirality-build-user-journeys-20260912-out/mac-arm64/Chirality.app
shasum -a 256 /Users/ryan/.claude/chirality-build-user-journeys-20260912-out/Chirality-3.0.0-arm64.dmg
```

`desktop:dist` performs one DMG package/sign with `--publish never`, verifies the existing Electron distribution at `/Users/ryan/Library/Caches/chirality/electron-dist`, then runs dependency boundary, post-signing Codex pin, and instruction-root integrity checks against the explicit output directory. Its signing hook verifies both Codex binaries and the whole App, requiring hardened runtime. Read-only post-sign entitlement inspection will confirm Code Mode host JIT and ordinary Codex no JIT. Expected pre-notarization Gatekeeper outcome is `Unnotarized Developer ID`, recorded as pending rather than PASS. No separate preliminary package or duplicate packaging checks are needed. If dependency acquisition, Electron distribution verification, or configured signing fails, report the concrete failure; no protected-state diagnostics or retries.

Known non-secret configured signing fingerprint above comes only from `../CODEX_MVP_PACKAGING_20260910/WORKING_RECORD.md` line 307; no credential or identity store inspection. No `security` commands. Notarization, stapling, install-over preservation acceptance and publication remain owner acts. Parent owns direct native tests and guarded launcher; this executor does not launch. Same-build journey/restart passes do not establish install-over preservation. Version metadata aligned to `3.0.0` by parent direction; no old installation/profile use.

Context read from current checkout: Root AGENTS SHA256 `c3fb6dbe394c168f75f12e761fce47b80a81ab9ae1bd41cfb0d28dd1e4003352`; TASK `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`; App AGENTS `3b1c1ffdc5d99b035bb08164cc3b6e1425e57431c89d22902f6ba88cbb3adb79`. Also read the parent-named A2 BUILD_EVIDENCE, UI refinement HANDOFF and UPDATE_PRESERVATION_ACCEPTANCE, and current frontend package/scripts. Initial phase had no product writes. Parent subsequently authorized the metadata alignment below. No commit/push. Concrete blocker: none found in source flow; actual build inputs/environment are unverified until release.

## Authorized identity alignment, 2026-09-13T02:49:42Z

Parent recovered PLAN Delivery authorization for actual v3.0.0 identity at the consolidated packaging point. Changed only `frontend/package.json` version and `frontend/package-lock.json` top-level/root-package versions, three literal replacements total. No dependency change, release publication, historical evidence or test fixture rewrite. Electron Builder derives bundle/DMG metadata from this manifest; packaged About/update version comes from `app.getVersion()`.

Frozen changed source hashes: package.json `0582bf1dec2931dae2a897ba1040494b5d28af5565295b833b3c26e4c5a3514f`; package-lock.json `b6cfa3cf876d5c763862763393a4729034a797730d9cda077f95cd28e6b3f1cf`. Source identity check `npm run verify:version-identity -- --expect 3.0.0` PASS (zero mismatches; packaged surfaces remain uninspected). Existing `verify-version-identity.test.ts` and `pack-electron.test.ts`: 2 files, 19 tests PASS with local Vitest 4.1.10. Scoped diff whitespace check PASS. Frozen for fresh independent review; no build/signing begun.
