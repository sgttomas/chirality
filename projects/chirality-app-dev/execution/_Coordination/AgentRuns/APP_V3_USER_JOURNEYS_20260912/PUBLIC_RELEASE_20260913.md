# v3.0.0 publication record

The owner authorized the automatic-update fix and subsequent release, then
explicitly directed this agent to perform notarization with the existing Apple
setup. That later direction supersedes the earlier owner-performed Apple step.
No additional publishing approval is needed. Credential, trial-state and
preservation restrictions remain applicable.

## Source and artifact

- Product source: `6f41f93e74b31796302fd45a228ebeabdcd5dd0e`, merged
  [PR #781](https://github.com/sgttomas/chirality/pull/781). Required CI and
  independent source review passed. The merge tree matches the reviewed and
  tested candidate.
- Final build completed at `2026-09-13T04:29:16Z` under
  `briefs/FINAL_UPDATE_PACKAGING.md`. The unchanged historical
  `BUILD_EVIDENCE_FINAL_UPDATES_20260913.md` records the original signing,
  package, supplier, instruction and actual ASAR checks.
- Installer:
  `/Users/ryan/.claude/chirality-build-3-publish-20260913-out/Chirality-3.0.0-arm64.dmg`.
  Final post-staple size: **338046035 bytes**.
- Final post-staple SHA-256:
  `8841144cbb3d90237295d0e2317f30e0bba58423d1e71a0bbf6f3b31f5821c85`.
  The adjacent `Chirality-3.0.0-arm64.dmg.sha256` contains this digest and the
  exact installer basename. The pre-notarization digest is historical and is
  not the published download checksum.

## Apple verification

One notarization submission, `e8a2a95a-9851-4050-a187-175b98ed7a30`, returned
**Accepted**. Apple's log reports status code 0, Ready for distribution,
`issues: null` and 37 ticket entries; its archive hash matches the exact
original final package.

Stapling and stapler validation passed. The final DMG was mounted read-only,
without launching the App. Deep strict signature verification passed on the
actual mounted App, and Gatekeeper accepted it as **Notarized Developer ID**.
The temporary volume was detached. No installed App or profile was changed.
The final artifact identity was recorded at `2026-09-13T04:56:47.494397Z`.
Command results and Apple evidence are preserved in stages 16 through 24 of
the final output's `build-evidence/` folder. No password was revealed, copied,
entered or exported; no raw credential store or `security` command was used.

## GitHub publication

Published [Chirality v3.0.0](https://github.com/sgttomas/chirality-app/releases/tag/v3.0.0)
as the latest stable release at **2026-09-13T05:08:54Z**, release ID
`387790842`. Its target is `343e6eed9d1a1b51ff4b087c0f73fcda305b0c7c`, the release
repository's existing framework snapshot. Notes explicitly link the exact
public canonical desktop source and distinguish GitHub's automatic source
archives from the desktop installer.

The broad library exporter still unconditionally writes a D-GOV-41 adoption
hold. It was not run or bypassed. This release distributes the installer and
checksum and does not synchronize that separate framework projection.

The one upload completed at `2026-09-13T05:08:01.294471Z`. Before publication,
GitHub's uploaded sizes and SHA-256 digests matched both verified final files.
No existing asset was overwritten.

| Public asset | Size | GitHub asset ID |
|---|---:|---|
| [Chirality-3.0.0-arm64.dmg](https://github.com/sgttomas/chirality-app/releases/download/v3.0.0/Chirality-3.0.0-arm64.dmg) | 338046035 bytes | 560596977 |
| [Chirality-3.0.0-arm64.dmg.sha256](https://github.com/sgttomas/chirality-app/releases/download/v3.0.0/Chirality-3.0.0-arm64.dmg.sha256) | 92 bytes | 560596981 |

At `2026-09-13T05:10:01.616Z`, anonymous requests verified the public release
page and latest-release endpoint both returned 200, the release was stable and
published, both asset names, URLs, sizes and digests matched, and the downloaded
public checksum matched the final DMG digest. The checksum file itself has
SHA-256 `fbba4f643ab6bb87ac66a01cb9105ef17f0a1805052110217bd9c3469ecf0bcd`.

The production update checker from the exact build source parsed that fetched
public response successfully for macOS arm64. Using explicit version controls,
2.0.0 returned update-available with the correct 3.0.0 DMG URL, and 3.0.0 returned
up-to-date. This is source-checker verification against the real public feed,
not an installed 2.0.0 UI observation. No App launch or rebuild was needed.
Command and verification records are stages 25 through 28 in the final output's
`build-evidence/` folder.

Earlier installers, worktrees, profiles and evidence remain preserved.
`OWNER_TRIAL_NOTES.md` retains the campaign results, limits and optional
installation-preservation checklist. Agent review and technical verification
do not assert the owner's unperformed installation checks.
