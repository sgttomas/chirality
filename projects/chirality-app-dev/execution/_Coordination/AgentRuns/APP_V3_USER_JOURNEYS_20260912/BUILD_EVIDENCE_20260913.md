# Consolidated v3.0.0 build evidence

Recorded 2026-09-13T03:12:32Z by TASK / Type 2, gpt-6-astra medium, delegated-harness-native child of the campaign parent. No delegation. Parent released this single local package after PR 778 merged, required CI and independent review passed. Those preconditions are parent-reported; source-tree equivalence was also checked directly here.

## Source and artifacts

- Source: `9eaddb5965642a783ad700743eecdf876e9e0104` (PR 778). Its tree and reviewed candidate `897d54e32ee4a97aeaa292adf1dbe046d5d88b35` both resolve to `5ae726cc8209ed2c3d4345f428fd27aefa4c8655`.
- New detached build checkout: `/Users/ryan/.claude/chirality-build-user-journeys-20260912`.
- New output: `/Users/ryan/.claude/chirality-build-user-journeys-20260912-out`.
- DMG: `/Users/ryan/.claude/chirality-build-user-journeys-20260912-out/Chirality-3.0.0-arm64.dmg`, 337955318 bytes, pre-notarization SHA-256 `321a4de9c8155be1fcd0a24f3aebfae55693df181a3151c5ad16952ef8171cb1`.
- App: `/Users/ryan/.claude/chirality-build-user-journeys-20260912-out/mac-arm64/Chirality.app`, CDHash `4f77d1a84bf9e3eedbb816d0564897b058cd9a8b`.
- Identity: `3.0.0`, `Chirality`, `com.chirality.app`, arm64. Electron `43.2.0`; Codex `0.154.0`.
- Configured Developer ID Application Ryan Tufts, team `8A7JL35U4S`, selected through non-secret fingerprint `C7F111429F7AC5085484A9DF6F5AE7CFF552DEEF` from the parent-authorized historical record.

Both destinations were absent before creation. Detached worktree creation started 2026-09-13T03:06:06Z and exited 0. Every earlier App, output and worktree remains preserved. Package/lock files remained unchanged after dependency installation (read-only scoped diff exit 0). This is a derivative local artifact of the source revision, not governed acceptance or publication.

## Execution

Commands followed `returns/PACKAGING_PREPARATION.md` with final source and actual v3.0.0 identity. Runtime `npm ci`, frontend `npm ci`, instruction preparation, Runtime build, App build and one `desktop:dist` ran sequentially. The packager used the existing verified Electron distribution `/Users/ryan/Library/Caches/chirality/electron-dist`, configured signing hook and `--publish never`.

Per-stage exact command, cwd, UTC start/end and exit are in JSON records beside filtered logs under `/Users/ryan/.claude/chirality-build-user-journeys-20260912-out/build-evidence`. Every command-output line containing an at-sign was removed before output or log recording. No raw unfiltered harness log was saved.

| Stage | Start UTC | End UTC | Exit |
|---|---|---|---|
| 01-runtime-ci | 2026-09-13T03:06:32Z | 2026-09-13T03:06:38Z | 0 |
| 02-frontend-ci | 2026-09-13T03:06:45Z | 2026-09-13T03:06:56Z | 0 |
| 03-instruction-root | 2026-09-13T03:07:03Z | 2026-09-13T03:07:04Z | 0 |
| 04-runtime-build | 2026-09-13T03:07:09Z | 2026-09-13T03:07:12Z | 0 |
| 05-app-build | 2026-09-13T03:07:18Z | 2026-09-13T03:07:39Z | 0 |
| 06-desktop-dist | 2026-09-13T03:07:46Z | 2026-09-13T03:10:36Z | 0 |
| 07-version-identity | 2026-09-13T03:10:43Z | 2026-09-13T03:10:43Z | 0 |
| 08-signature-verify | 2026-09-13T03:10:52Z | 2026-09-13T03:10:52Z | 0 |
| 09-signature-details | 2026-09-13T03:10:59Z | 2026-09-13T03:10:59Z | 0 |
| 10-gatekeeper | 2026-09-13T03:10:59Z | 2026-09-13T03:10:59Z | 3 |
| 11-artifact-hash | 2026-09-13T03:11:11Z | 2026-09-13T03:11:12Z | 0 |
| 12-codex-entitlements | 2026-09-13T03:11:12Z | 2026-09-13T03:11:12Z | 0 |
| 13-code-mode-entitlements | 2026-09-13T03:11:13Z | 2026-09-13T03:11:13Z | 0 |

## Verification

- Dependency boundary PASS: forbidden development/legacy packages absent, Codex tree PASS, packaged Runtime source proofs PASS (118 desktop, 121 service, 16 CLI sources).
- Post-sign Codex pin PASS: package, lockfile and packaged executable all `0.154.0`. Signed executable digests differ from installed supplier bytes as expected after signing.
- Instruction-root integrity PASS: 367 files match; no missing, mismatching or unexpected files; bundle manifest match. Source completeness separately remains `needs_remediation` for historical KG-001 tools-registry/examples tracking rows, the same distinction recorded by the earlier A2 package. This is not reported as complete source-completeness acceptance.
- Actual App Info.plist and DMG identity PASS: twelve matching surfaces, zero mismatches. Rendered UI version remains uninspected because no App launch occurred; no release manifest exists.
- `codesign --verify --deep --strict --verbose=2` PASS: valid on disk and satisfies Designated Requirement. Bundle hardened-runtime flag and Developer ID authority chain verified.
- Both packaged Codex binaries carry team `8A7JL35U4S` and hardened runtime. Ordinary Codex has empty entitlements; Code Mode host has only `com.apple.security.cs.allow-jit`.
- `spctl --assess --type execute --verbose=2` exited 3, `Unnotarized Developer ID`, expected before owner notarization/stapling. No Gatekeeper PASS claim.

## Warnings and remaining boundary

Dependency installation reported existing audit counts: Runtime 7 vulnerabilities (4 moderate, 3 high), frontend 21 (1 low, 8 moderate, 11 high, 1 critical). Both reported six install-script coverage warnings. No upgrades, audit fixes or script approvals were performed. Production Next build warned about named JSON version imports in About/account components, then compiled successfully. These warnings did not fail the authorized build; no repair or second package was attempted.

Packaging contribution is complete and signed local artifact is ready for owner handling. No equivalent test suites rerun, native App launch, installed App/profile/R17 access, protected identity/auth/binding/token/Codex session/event reads, security command, notarization, stapling, publication, old-artifact cleanup or commit/push occurred. Parent owns direct native tests and owner notes. Owner notarization/stapling, post-staple Gatekeeper check, install-over preservation acceptance and explicit release direction remain distinct. Same-build journey/restart evidence is not install-over preservation evidence. No packaging blocker remains; do not rerun the consolidated package absent a new concrete reason.
