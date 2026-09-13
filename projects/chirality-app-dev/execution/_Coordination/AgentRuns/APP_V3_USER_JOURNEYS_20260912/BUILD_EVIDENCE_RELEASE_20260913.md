# Replacement v3.0.0 release build evidence

Recorded 2026-09-13T03:50:50Z. TASK / Type 2, gpt-6-astra medium, delegated-harness-native packaging child; no delegation. This is the authorized replacement after the first artifact's dependency triage, not a overwrite or destruction of the preserved first artifact. Parent released preparation after reviewed PR 779 and required CI, then released signing only after the separate production HTTP check passed.

## Exact artifact basis

- Merged source `56c9f538da7f8ab355975efb0821b2b17f4a6814`, PR 779. Direct Git check shows source and reviewed/tested `ca4920ef062492114f3569405687e47cfb2bb771` both have tree `6c8a2ed38e6e4dca426a5fa1937ee8653e100a74`.
- New detached checkout `/Users/ryan/.claude/chirality-build-3-release-20260913`.
- New output `/Users/ryan/.claude/chirality-build-3-release-20260913-out`.
- DMG `/Users/ryan/.claude/chirality-build-3-release-20260913-out/Chirality-3.0.0-arm64.dmg`, **338040805 bytes**, pre-notarization SHA-256 **`4078225b7cdf8520b0b7beba80aa3d96b33c68ae1657844e7caac48f0239d920`**.
- Signed App `/Users/ryan/.claude/chirality-build-3-release-20260913-out/mac-arm64/Chirality.app`; CDHash `32245fdafd8aa84a3620574623461ccdd0057d95`.
- Product `3.0.0`, `Chirality`, `com.chirality.app`, arm64; Electron 43.2.0, Codex 0.154.0. Developer ID team `8A7JL35U4S` selected with configured non-secret fingerprint `C7F111429F7AC5085484A9DF6F5AE7CFF552DEEF`.

Both new destinations were absent before creation; worktree creation started 03:40:16Z and exited 0. All earlier artifacts/build worktrees remain untouched. Package/lock metadata remained clean after installation. Parent reports CI Root 34735868873 and App 34735868929 PASS, plus separate full-source review PASS. Local packaging is derivative evidence; it is not publication or owner acceptance.

## Sequence and results

Runtime npm ci, frontend npm ci, installed/lock identity and production audit, instruction preparation, Runtime build and production App build ran in that order. Production build completed 03:42:04Z; executor stopped before signing as instructed. No equivalent full test suites rerun.

Parent then executed the separately reviewed benign HTTP probe, hash `9c6ec80733070019c0305328c265e4522df36d1fb2161695874727dfd6aa6132`, on this exact production build at 03:45:13Z. Read-back evidence confirms production page 200, referenced static JavaScript 200, image optimizer without parameters 404, optimizer with an existing source 404, exit 0. Parent reports cleanup completed. Evidence: output `build-evidence/parent-production-image-http.log` and `.json`. This check uses the production Next build without an App launch or profile/auth access; it is not native install-over acceptance.

After parent's explicit release, **one** replacement `desktop:dist` ran 03:45:31Z to 03:48:52Z, exit 0. Existing verified Electron cache was used; the custom signing hook ran; notarization was skipped; publishing remained `never`.

Exact commands/cwd/UTC/exit JSON and filtered output logs reside under `/Users/ryan/.claude/chirality-build-3-release-20260913-out/build-evidence`. At-sign-containing command-output lines were removed before recording; all resulting log files checked free of such lines.

| Stage | Start UTC | End UTC | Exit |
|---|---|---|---|
| 01-runtime-ci | 2026-09-13T03:40:34Z | 2026-09-13T03:40:40Z | 0 |
| 02-frontend-ci | 2026-09-13T03:40:49Z | 2026-09-13T03:41:00Z | 0 |
| 03-installed-production-audit | 2026-09-13T03:41:20Z | 2026-09-13T03:41:21Z | 0 |
| 04-instruction-root | 2026-09-13T03:41:33Z | 2026-09-13T03:41:34Z | 0 |
| 05-runtime-build | 2026-09-13T03:41:34Z | 2026-09-13T03:41:37Z | 0 |
| 06-app-build | 2026-09-13T03:41:46Z | 2026-09-13T03:42:04Z | 0 |
| 07-desktop-dist | 2026-09-13T03:45:31Z | 2026-09-13T03:48:52Z | 0 |
| 08-asar-repair-assertions | 2026-09-13T03:49:04Z | 2026-09-13T03:49:04Z | 0 |
| 09-version-identity | 2026-09-13T03:49:04Z | 2026-09-13T03:49:04Z | 0 |
| 10-signature-verify | 2026-09-13T03:49:17Z | 2026-09-13T03:49:17Z | 0 |
| 11-signature-details | 2026-09-13T03:49:17Z | 2026-09-13T03:49:17Z | 0 |
| 12-gatekeeper | 2026-09-13T03:49:17Z | 2026-09-13T03:49:18Z | 3 |
| 13-artifact-hash | 2026-09-13T03:49:29Z | 2026-09-13T03:49:30Z | 0 |
| 14-codex-entitlements | 2026-09-13T03:49:30Z | 2026-09-13T03:49:30Z | 0 |
| 15-code-mode-entitlements | 2026-09-13T03:49:30Z | 2026-09-13T03:49:30Z | 0 |

- Actual ASAR assertions PASS: Next **15.5.25**, sharp **0.35.4**, nanoid **3.3.18**. Both packaged `next.config.mjs` and `.next/required-server-files.json` establish **images.unoptimized=true**. This combines source-build HTTP behavior with actual packaged configuration, without invoking a packaged App.
- Dependency boundary PASS: no forbidden development/legacy package presence; Codex tree PASS; source proofs 118 desktop / 121 service / 16 CLI.
- Post-sign Codex pin PASS, package/lock/actual version 0.154.0. Signing changes binary digests, handled by the existing after-signing check.
- Instruction integrity PASS, 367 files, manifest match, no missing/mismatching/unexpected files. Historical KG-001 tools-registry/examples source-completeness rows still require remediation; this independent status is not hidden or newly accepted here.
- Actual bundle/DMG version check PASS, twelve matching surfaces, zero mismatches. Rendered native About version remains uninspected, and no release manifest exists.
- Deep strict signature PASS, valid on disk and Designated Requirement satisfied, correct Developer ID authority and hardened runtime. Both Codex executables have correct team/hardened runtime; ordinary Codex entitlements empty, Code Mode host JIT only.
- Gatekeeper **exit 3, Unnotarized Developer ID**, expected pending owner notarization/stapling. No Gatekeeper PASS claim.

## Remaining warnings and handoff

Installed and lockfile versions of the three repaired packages matched before packaging. Current frontend **production audit has zero critical/high and two moderate package rows**: PostCSS and its propagated Next effect, [GHSA-fxqj-rqcc-2cmp](https://github.com/advisories/GHSA-fxqj-rqcc-2cmp). Raw npm audit exited 1 for those findings; the input assertion wrapper exited 0 because versions matched and critical/high counts were zero. This is not an audit-clean claim.

Full frontend installation audit reports 19 rows (1 low, 9 moderate, 9 high), including excluded development/legacy dependencies. Runtime installation reports unchanged 7 rows (4 moderate, 3 high), including excluded legacy Pi support and development tooling discussed in the earlier triage. Both installations emitted six uncovered install-script warnings. No audit fix, dependency changes or script approvals were run in this executor. Next build retains nonblocking named JSON version-import warnings in About/account components. Existing source-completeness tracking remains as above.

Packaging contribution is complete, with no unresolved packaging failure. This replacement supersedes the earlier source9eaddb596 artifact for owner review while preserving it. Owner notarization/stapling, post-staple Gatekeeper assessment, native installation/preservation checks and explicit public-release direction remain separate. No protected identity/auth/binding/token/Codex-home/session/event access, security command, App launch, install/profile/R17 changes, notarization, stapling, publication, old-artifact cleanup or commit/push occurred. Only this evidence and the focused release return were written in the parent workspace. No further build is needed absent a new concrete reason.
