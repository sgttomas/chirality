# Consolidated build evidence (D-GOV-43, topology A2)

Recorded 2026-09-12T16:40Z by the implementing session, per `PACKAGING_PROCEDURE.md`.
Precondition met: S-1..S-8 and the disconnect check pass from source
(`spike/EVIDENCE.md`); independent source review PASS with no unresolved blocking
finding on the built revision (`INDEPENDENT_REVIEW.md`, including the re-checks of
26fffb89a and 388de6973).

## Build inputs

| Input | Value |
|---|---|
| Source revision | `388de6973c32730d130b4084fd78996391899e06` (PR #774; later commits on the branch are review and evidence records only) |
| Build checkout | detached worktree at that revision under `~/.claude/chirality-build-a2` (electron-builder refuses sources under `/private/tmp`); dependencies from `npm ci` in both workspaces |
| Codex pin | `@openai/codex` 0.154.0 (package.json, lockfile umbrella and platform package, packaged `codex --version`) |
| Electron | 43.2.0 from the verified distribution cache (`electron:supply-chain` PASS) |
| Product identity | 3.0.0-rc.1, `com.chirality.app`, `Chirality` |
| Signing identity | Developer ID Application: Ryan Tufts (8A7JL35U4S), selected through `CHIRALITY_SIGNING_IDENTITY_SHA1` (the fingerprint recorded in `../CODEX_MVP_PACKAGING_20260910/WORKING_RECORD.md`); signed by electron-builder through the App's own `mac.sign` hook |

## Steps and results

1. Build: `instruction-root:prepare` (366 files), `runtime:build` (`tsc -b`), `build`
   (Next, Electron main and preload, `dist-runtime/runtime-service/standalone-bin.mjs`,
   `dist-runtime/runtime-cli/chirality-cli.mjs`): all exit 0. Started 16:24:55Z.
2. Package and sign: `desktop:dist` (`pack-electron.mjs --target dmg`) exit 0 at 16:28:28Z.
   Output `~/.claude/chirality-build-a2-out/`: `Chirality-3.0.0-rc.1-arm64.dmg`
   (337,038,438 bytes, sha256 `efaac5d78706f5647897cb25c756c4466f7b779cd976cf54aa1a56634c058fb9`),
   `mac-arm64/Chirality.app` (CDHash `0f87307884a71167df367c37d8d1e1d46225ecb6`).
   A first attempt at 26fffb89a failed inside the sign hook (electron-builder passes its
   packager as the hook's second argument, which the hook had used for dependency
   injection); fixed in 388de6973, re-reviewed, and the build repeated from that revision.
3. Notarize and staple: owner act, not performed here.
4. Verification on the signed bundle:
   - `desktop:verify-dependencies`: PASS (asar boundary, Codex tree, packaged runtime
     source proofs for desktop, service and CLI bundles; runtime profile `app-owned-codex`).
   - `desktop:verify-codex-pin -- --after-signing`: PASS (packaged 0.154.0 equals the pin;
     binary digests differ from the installed package only because signing rewrote them,
     as the script expects after signing).
   - `instruction-root:integrity`: status pass, 366 files, bundle manifest match. The
     summary's "source completeness" rows for PRD KG-001 (tools registry, examples) read
     `remediation_required` exactly as in the earlier trial records (pre-existing PRD
     tracking rows, not a candidate defect).
   - `codesign --verify --deep --strict --verbose=2`: valid on disk, satisfies its
     Designated Requirement. Bundle flags `runtime` (hardened), authority chain Developer
     ID Application: Ryan Tufts (8A7JL35U4S), Developer ID Certification Authority, Apple
     Root CA; secure timestamp 16:27:52Z.
   - Both bundled Codex binaries signed with TeamIdentifier 8A7JL35U4S and the hardened
     runtime; `codex-code-mode-host` carries the JIT entitlement, `codex` does not.
   - `spctl --assess --type execute`: rejected, `Unnotarized Developer ID` (expected
     before the owner's notarization; re-run after stapling).
   - `verify:version-identity --expect 3.0.0-rc.1`: PASS, 12 surfaces match, 2 absent
     (no UI version string or release manifest exists yet).
5. Packaged checks (S-6 quit and relaunch continuation; S-8 sign-in and sign-out scoped to
   Chirality with another Codex client unchanged; the renderer disconnect check) on the
   stapled App with a fresh `userData`: owner's native verification per
   `NATIVE_CHECKLIST.md`. Not performed by the agent (they need the owner's OAuth and a
   direct launch of the packaged App).

## Not done and why

- Notarization, stapling and the post-staple `spctl` re-check: owner acts.
- Packaged S-6, S-8 and disconnect: owner's native verification.
- Publishing: not authorized.
