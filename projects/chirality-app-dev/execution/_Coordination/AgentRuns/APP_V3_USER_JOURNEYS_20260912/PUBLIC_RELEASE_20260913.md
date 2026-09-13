# v3.0.0 publication continuation

The owner authorized the automatic-update fix and subsequent release: “yes, make that fix. Then we are ready to publish.” Do not request another generic publishing approval. The retained credential restrictions and owner-performed notarization/stapling remain operational boundaries.

## Source and draft

- Product source: `6f41f93e74b31796302fd45a228ebeabdcd5dd0e`, merged PR781 with required CI and independent source review PASS.
- Final package completed at 04:29:16Z under `briefs/FINAL_UPDATE_PACKAGING.md`. The signed DMG is 338043892 bytes; pre-notarization SHA-256 `e3171754f935dcf502641781586a5befa0c76714ea4f196ed3ca0ece0f846335`. Parent validated the fifteen stage results, actual ASAR checks, signature result, digest record and size against `BUILD_EVIDENCE_FINAL_UPDATES_20260913.md`. Gatekeeper is still Unnotarized Developer ID, as expected before the Apple step.
- Public release draft: https://github.com/sgttomas/chirality-app/releases/tag/untagged-a6578619a34fa0775262, requested tag `v3.0.0`, title `Chirality v3.0.0`. Draft is private, has no assets and is not the latest release.
- Public repository target: `343e6eed9d1a1b51ff4b087c0f73fcda305b0c7c`. This is its existing framework snapshot, not the desktop application's source. Release notes make that distinction and link the exact public canonical product commit.
- Authored notes: `/Users/ryan/.claude/chirality-user-journeys-20260913/v3.0.0-release-notes.md`, already supplied to the draft.

The broad library exporter still unconditionally writes a D-GOV-41 adoption hold. It was not run or bypassed. The release task distributes the installer and checksum; it does not wholesale synchronize that separate framework projection.

## Finish after the owner's Apple step

The owner performs notarization and stapling of the final DMG using their own Apple signing setup. No usable notarization profile is documented; do not inspect credential stores or guess one. Source of that retained boundary: `../APP_V3_UI_REFINEMENT_20260912/HANDOFF_20260912.md` task4 and the original packaged build evidence. Normal agent signing uses the already configured non-secret Developer ID fingerprint; that does not authorize credential handling.

Owner commands, after the final build is complete. Replace `YOUR_EXISTING_PROFILE` with the profile name from your own Apple notarization setup. Enter no credentials in this chat. Stop if submission is not accepted.

```sh
xcrun notarytool submit '/Users/ryan/.claude/chirality-build-3-publish-20260913-out/Chirality-3.0.0-arm64.dmg' --keychain-profile 'YOUR_EXISTING_PROFILE' --wait &&
xcrun stapler staple '/Users/ryan/.claude/chirality-build-3-publish-20260913-out/Chirality-3.0.0-arm64.dmg' &&
xcrun stapler validate '/Users/ryan/.claude/chirality-build-3-publish-20260913-out/Chirality-3.0.0-arm64.dmg'
```

These switches were checked against the installed Xcode tools' help. No notarization or keychain operation was run by the agent. If the owner does not already have a profile, they should configure their Apple notarization credentials themselves; the agent must not inspect or obtain those credentials.

After the owner reports completion, verify the actual notarization/stapling result and applicable Gatekeeper/signature checks, calculate the final DMG SHA-256 after stapling, and write `Chirality-3.0.0-arm64.dmg.sha256` containing only the final hash and matching basename. Stapling changes bytes, so the pre-notarization digest must not become the published checksum.

Verify draft tag, target and empty asset state before uploading the exact final DMG and checksum. Reconcile any state change rather than replacing unexpected existing assets. Publish this reviewed draft as the latest stable release, then verify its public release page, both asset identities/sizes/checksum, and the public latest-release API. Existing approval authorizes this continuation; do not publish an unnotarized local build. Record actual publication time and URL. No auto-install, old profile reads, old build cleanup, account changes or unrelated repository edits are part of this step.
