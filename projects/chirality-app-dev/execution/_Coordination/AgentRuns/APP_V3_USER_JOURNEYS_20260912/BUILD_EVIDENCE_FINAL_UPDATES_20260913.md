# Final automatic-update packaging evidence

Recorded 2026-09-13T04:30:56Z. TASK / Type 2, gpt-6-astra medium, delegated-harness-native child; no delegation. Parent authorization is `briefs/FINAL_UPDATE_PACKAGING.md`. Parent reports PR781 required Root34737560784/App34737560803 CI, independent source review and direct native startup observation PASS; Runtime364/frontend2238 tests passed, four skipped. Those existing checks were not repeated.

## Source and artifact

- Final merged source `6f41f93e74b31796302fd45a228ebeabdcd5dd0e` (PR781), verified tree `32a4a9b3472dd95528efe161833bb2375a97181d`, identical to tested `eac0dd6af6f5924c13731feaefa7dddd41d003e9`.
- Fresh detached checkout `/Users/ryan/.claude/chirality-build-3-publish-20260913`.
- Final output `/Users/ryan/.claude/chirality-build-3-publish-20260913-out`.
- DMG `/Users/ryan/.claude/chirality-build-3-publish-20260913-out/Chirality-3.0.0-arm64.dmg`, 338043892 bytes; **pre-notarization SHA-256 `e3171754f935dcf502641781586a5befa0c76714ea4f196ed3ca0ece0f846335`**.
- App `/Users/ryan/.claude/chirality-build-3-publish-20260913-out/mac-arm64/Chirality.app`; CDHash `fc7ac7f38828b66fdd298712b47fd8b98a8631ca`.
- Identity `3.0.0`, `Chirality`, `com.chirality.app`, arm64. Electron43.2.0, Codex0.154.0. Configured Developer ID team8A7JL35U4S, selected non-secret fingerprint C7F111429F7AC5085484A9DF6F5AE7CFF552DEEF.

Both new destinations were absent before creation. Detached worktree creation began 04:23:39Z and exited0. Previous build worktrees, profiles, Apps and artifacts remain preserved. This artifact supersedes the earlier installers for the final automatic-update source; historical evidence remains valid for its own revisions. No public projection/export ran.

## Execution and checks

Both locked installs, installed/lock identity and production audit, instruction preparation, Runtime build and production build passed. One final signed `desktop:dist` ran04:25:10Z to04:29:16Z, exit0, using the existing verified Electron cache and `--publish never`. No duplicate full suites or unchanged production HTTP probe ran. The prior HTTP result remains evidence for unchanged Next/config behavior; this run checks actual packaged config.

Exact commands/cwd/UTC/exit metadata and filtered command logs: `/Users/ryan/.claude/chirality-build-3-publish-20260913-out/build-evidence`, stages01..15. Established recorder/verification code was reused without adding product scripts. All15 log files contain no at-sign lines; command output was filtered before recording.

| Stage | Start UTC | End UTC | Exit |
|---|---|---|---|
| 01-runtime-ci | 2026-09-13T04:24:02Z | 2026-09-13T04:24:07Z | 0 |
| 02-frontend-ci | 2026-09-13T04:24:16Z | 2026-09-13T04:24:25Z | 0 |
| 03-installed-production-audit | 2026-09-13T04:24:30Z | 2026-09-13T04:24:31Z | 0 |
| 04-instruction-root | 2026-09-13T04:24:38Z | 2026-09-13T04:24:38Z | 0 |
| 05-runtime-build | 2026-09-13T04:24:38Z | 2026-09-13T04:24:41Z | 0 |
| 06-app-build | 2026-09-13T04:24:45Z | 2026-09-13T04:25:03Z | 0 |
| 07-desktop-dist | 2026-09-13T04:25:10Z | 2026-09-13T04:29:16Z | 0 |
| 08-asar-assertions | 2026-09-13T04:29:29Z | 2026-09-13T04:29:29Z | 0 |
| 09-version-identity | 2026-09-13T04:29:40Z | 2026-09-13T04:29:40Z | 0 |
| 10-signature-verify | 2026-09-13T04:29:41Z | 2026-09-13T04:29:41Z | 0 |
| 11-signature-details | 2026-09-13T04:29:41Z | 2026-09-13T04:29:41Z | 0 |
| 12-gatekeeper | 2026-09-13T04:29:41Z | 2026-09-13T04:29:41Z | 3 |
| 13-artifact-hash | 2026-09-13T04:29:52Z | 2026-09-13T04:29:52Z | 0 |
| 14-codex-entitlements | 2026-09-13T04:29:53Z | 2026-09-13T04:29:53Z | 0 |
| 15-code-mode-entitlements | 2026-09-13T04:29:53Z | 2026-09-13T04:29:53Z | 0 |

- Actual signed ASAR PASS: Next15.5.25, sharp0.35.4, nanoid3.3.18. Both source Next config and built required-server-files config set images.unoptimized=true.
- Actual packaged main PASS: automatic startup polling invocation, six-hour interval constant, immediate check and shutdown cleanup wiring present. This is static packaging correspondence, supported by parent's separate source-native startup observation; no packaged App was launched here.
- Dependency boundary PASS, no forbidden development/legacy packages, Codex tree PASS; Runtime source proof118desktop/121service/16CLI.
- Post-sign Codex pin PASS: installed/lock/actual executable version0.154.0. Signed binary digest changes are expected and handled by the after-signing verifier.
- Instruction integrity PASS367files, manifest match. Historical KG-001 tools-registry/examples source-completeness remediation rows remain distinct, as in preceding evidence; no acceptance inferred.
- Actual App/DMG version identity PASS, twelve matching surfaces, zero mismatches; rendered native About remains uninspected and no release-manifest surface exists.
- Deep strict codesign verification PASS: valid on disk, satisfies Designated Requirement. Correct Developer ID authority and hardened runtime. Codex executables both team8A7JL35U4S/hardened; ordinary Codex empty entitlements, Code Mode host JIT only.
- Gatekeeper exit3 **Unnotarized Developer ID**, expected before owner notarization/stapling. No notarization or Gatekeeper PASS claim.

## Residual warnings and handoff

Production audit has0critical/0high/2moderate rows: PostCSS [GHSA-fxqj-rqcc-2cmp](https://github.com/advisories/GHSA-fxqj-rqcc-2cmp) and propagated Next effect. Raw audit exit1 for remaining findings; identity/audit assertion wrapper exit0. Full frontend install audit19rows (1low/9moderate/9high) and Runtime7rows (4moderate/3high) include excluded tooling/legacy dependencies. Both install stages reported six uncovered install-script warnings. No audit fix, install-script approval or upgrade was run. Next build retained the nonblocking About/account named JSON version-import warnings. None of these observations is an audit-clean claim.

Packaging is complete, no unexpected failure. Parent owns Git, final release notes and publication. Owner notarization/stapling, final post-staple checksum and Gatekeeper checks remain; this checksum will change if stapling changes the DMG. No protected identity/auth/token/binding/keychain/Codex-home/session data access, security command, credential entry, App launch, native trial, notarization, stapling, publisher/exporter invocation or cleanup occurred. Only this evidence and `returns/FINAL_UPDATE_PACKAGING_RETURN.md` were written in the parent workspace. No further package is planned.
