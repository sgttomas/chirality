# Packaged build evidence: UI refinement

Recorded 2026-09-12T20:35:43Z by HELP_HUMAN / Codex. Task 4 of `HANDOFF_20260912.md`.
One build and one `desktop:dist` invocation completed; no source repair or build
retry was needed. The source worktree remained clean after the build.

## Basis and inputs

- Source: `85f19f019589b798331c804c4b206e34849eeab5`, the merge of PR #775.
- Independent source review: `returns/REVIEW_RETURN_3.md`, PASS for
  `51faa0a12fe3ce496eaa0c3549162072335e8f76`. The diff from that revision to
  the merged source contains only manifest, handoff, review and run records.
- PR #775 checks on merged head `cca1c652b793d0aed47516946f942a47f877d734`:
  `harness` (required), `Harness pre-merge` and `pec` all passed. The optional
  unsigned artifact job was skipped as designed; it is not required.
- Build checkout: `/Users/ryan/.claude/chirality-build-ui-85f19f019`, detached
  at the exact merged source. Earlier checkouts and output were preserved.
- Dependencies: `npm ci --no-audit --no-fund` in Runtime, then frontend.
  Node `24.18.0`, npm `11.16.0`; no lockfile changed.
- Electron `43.2.0`, using the distribution verified by the packaging entry.
- Stock Codex `0.154.0`, confirmed against package.json, lockfile and packaged
  executable by the maintained pin check. Platform `aarch64-apple-darwin`.
- Signing: Developer ID Application: Ryan Tufts (`8A7JL35U4S`), selected by
  `CHIRALITY_SIGNING_IDENTITY_SHA1=C7F111429F7AC5085484A9DF6F5AE7CFF552DEEF`
  from the previously recorded signer metadata in
  `../CODEX_MVP_PACKAGING_20260910/WORKING_RECORD.md`.
- Output selected by `CHIRALITY_ELECTRON_OUTPUT_DIRECTORY`:
  `/Users/ryan/.claude/chirality-build-ui-85f19f019-out`.
- Packaging used the repository's sign hook and `--publish never`.
  Notarization variables were omitted from the build environment. The builder
  recorded notarization skipped; no agent notarization or stapling was attempted.

## Build commands

The existing A2 packaging sequence was used. Each command's exit was checked
before the next began; detailed logs are in `/Users/ryan/.claude/chirality-build-ui-85f19f019-evidence`.
Lines containing `@` were omitted before logs were saved. No live App, daemon,
authentication or session log was read.

| Step | Command | Start UTC | End UTC | Exit |
|---|---|---|---|---|
| 01-runtime-npm-ci | `npm ci --no-audit --no-fund` | 2026-09-12T20:28:51Z | 2026-09-12T20:28:55Z | 0 |
| 02-frontend-npm-ci | `npm ci --no-audit --no-fund` | 2026-09-12T20:28:55Z | 2026-09-12T20:29:04Z | 0 |
| 03-instruction-root-prepare | `npm run instruction-root:prepare` | 2026-09-12T20:29:04Z | 2026-09-12T20:29:05Z | 0 |
| 04-runtime-build | `npm run runtime:build` | 2026-09-12T20:29:05Z | 2026-09-12T20:29:08Z | 0 |
| 05-app-build | `npm run build` | 2026-09-12T20:29:08Z | 2026-09-12T20:29:25Z | 0 |
| 06-desktop-dist | `npm run desktop:dist` | 2026-09-12T20:29:25Z | 2026-09-12T20:32:39Z | 0 |
| 07-version-identity | `npm run verify:version-identity -- --expect 3.0.0-rc.1` | 2026-09-12T20:32:39Z | 2026-09-12T20:32:39Z | 0 |

The final version check above inspected source/derived identity. A subsequent
`verify:version-identity -- --expect 3.0.0-rc.1 --app-path <built App>
--dmg-path <built DMG>` also exited 0 against the actual artifacts, with all
12 inspected identity surfaces matching. The rendered About value remains a
native observation, and no release-manifest version surface exists.

## Artifact

| Item | Value |
|---|---|
| DMG | `/Users/ryan/.claude/chirality-build-ui-85f19f019-out/Chirality-3.0.0-rc.1-arm64.dmg` |
| DMG bytes | 337335358 (about 337 MB) |
| DMG SHA-256 | `29ab257087bee96bb5f4dda1909264e5a35e2f43079ac024fb268735222c23ca` |
| App | `/Users/ryan/.claude/chirality-build-ui-85f19f019-out/mac-arm64/Chirality.app` |
| App regular-file bytes, symlinks excluded | 1044619869 (about 1.04 GB) |
| Bundle identifier | `com.chirality.app` |
| Version / bundle version | `3.0.0-rc.1` / `3.0.0-rc.1` |
| Minimum macOS | `15.0.0` |
| App CDHash | `7371ba01705a141187309b766d74624b17909c32` |

The DMG digest identifies the artifact before owner notarization/stapling.
If that process changes the distributed artifact, record its resulting digest.
The earlier build has the same version string, so source and artifact identity
must accompany any before/after observation.

## Verification and limits

- `desktop:verify-dependencies`: PASS. The `app-owned-codex` profile has the
  expected Codex tree and Runtime service/CLI source proofs, with no forbidden
  development or legacy runtime packages in the application payload.
- `desktop:verify-codex-pin -- --after-signing`: PASS. Installed and packaged
  versions agree at `0.154.0`. The recorded installed and packaged binary hashes
  differ because signing rewrites binaries; the check explicitly uses its
  after-signing mode and does not claim byte parity.
- `instruction-root:integrity`: PASS, all 366 files match, bundle manifest
  matches, no missing/unexpected/mismatched files. The separate legacy PRD
  source-completeness rows for KG-001 tools registry and examples still report
  `remediation_required`, as in the previous build. This does not constitute
  their remediation or acceptance; no instruction-bundle defect was reported.
- `codesign --verify --deep --strict --verbose=2 <App>`: exit 0, valid on disk
  and satisfies its Designated Requirement.
- Signature inspection: Developer ID chain through Apple Root CA, team
  `8A7JL35U4S`, hardened runtime. Secure signing timestamp shown as September
  12 at 14:32:01 local time (20:32:01 UTC).
- Both bundled Codex executables carry the same team and hardened runtime.
  `codex-code-mode-host` has the JIT entitlement; `codex` has an empty entitlement
  dictionary. Their strict verification was performed by the sign hook before
  packaging returned successfully.
- `spctl --assess --type execute --verbose=4 <App>`: exit 3,
  **rejected: Unnotarized Developer ID**, expected before the owner's
  notarization. Gatekeeper acceptance is not claimed. Recheck after stapling.
- Actual packaged version inspection: PASS as described above, with no product
  byte mutation.

Logs `01` through `13`, `build-results.json`, `signature-results.json`,
`artifact.json` and the small sequential build recorder are preserved in the
local evidence directory. The detailed instruction comparison is also under
`<build checkout>/projects/chirality-app-dev/frontend/artifacts/harness/instruction-root-integrity/latest/`.

No broad source tests were repeated: PR #775's reviewed source and CI were
unchanged. No App/account/model turn was launched by this packaging run. The
owner's update-preservation and native checks, notarization/stapling, final
system-prompt discussion and publishing approval remain outstanding. See
`OWNER_HANDOFF_20260912.md` for the manual steps and carried review notes.

## Cleanup state

The earlier dev process was already absent: no matching concurrently process
and no port-3000 listener were observed. No kill command was needed. The old
`/Users/ryan/.claude/chirality-build-a2` checkout and its output are preserved
pending owner verification. No trial state, identity, auth, token, binding,
keychain, Codex-home or session/event files were inspected or modified.
