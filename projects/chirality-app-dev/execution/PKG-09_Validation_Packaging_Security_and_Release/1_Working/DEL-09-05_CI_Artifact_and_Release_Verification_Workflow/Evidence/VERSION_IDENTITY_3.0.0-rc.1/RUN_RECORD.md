# Version identity check and staged 3.0.0-rc.1 patch — run record (DEL-09-05-V3-03)

**Boundary:** evidence only. The staged patch is **NOT applied**; `frontend/package.json` `version` remains `2.0.0` and `frontend/package-lock.json` is unchanged in the committed tree. Application is the parked item DEL-09-05-V3-06 (owner ruling). No signing, notarization, publication, distribution, or release act.

## Inputs

| Input | Identity |
|---|---|
| Basis commit | `0c683fb1657706316272951e4c3a0f7781b46009` |
| `frontend/package.json` (basis bytes) | SHA-256 `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc` — on-branch bytes add three `scripts` entries; the `version` line and the patch's context lines (file lines 1–6) are identical in both, so the patch applies to either |
| `frontend/package-lock.json` | SHA-256 `717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458` |
| Tool | `frontend/scripts/verify-version-identity.mjs` (npm script `verify:version-identity`) |

## Commands (cwd `projects/chirality-app-dev/frontend` unless stated; Node `v24.18.0`, npm `11.16.0`, git `2.55.0`)

| # | Command | Exit | Output |
|---|---|---|---|
| 1 | `npm run -s verify:version-identity -- --expect 2.0.0 --json <dir>/dry_run_report_expect_2.0.0.json` | 0 (`Result: PASS`) | `dry_run_report_expect_2.0.0.{txt,json,exit.txt}` |
| 2 | `npm run -s verify:version-identity -- --expect 3.0.0-rc.1 --stage-patch <dir>/staged_version_patch.diff --json <dir>/dry_run_report_expect_3.0.0-rc.1.json` | 1 (`Result: MISMATCH`, 4 mismatching surfaces) | `dry_run_report_expect_3.0.0-rc.1.{txt,json,exit.txt}`, `staged_version_patch.diff` |
| 3 | `shasum -a 256 staged_version_patch.diff` | 0 | `staged_version_patch.diff.sha256` → `311844f0a8b447085bf038ccbdda353a1240a5b44ae7a91df6754c9c154b1d82` |
| 4 | (cwd repo root) `git apply --check <dir>/staged_version_patch.diff`; `git apply --stat`; `git apply --numstat` | 0 | `git_apply_check.txt` — applies cleanly; 2 files, 3 insertions, 3 deletions; **not applied** |

Absolute scratch-worktree paths in the reports were replaced with `{REPO_ROOT}` after the runs.

## Surfaces enumerated (see the reports for observed/expected per surface)

1. `package.json` `version` — declared (`2.0.0`; MISMATCH vs `3.0.0-rc.1`)
2. `package-lock.json` top-level `version` — declared (MISMATCH)
3. `package-lock.json` `packages[""].version` — declared (MISMATCH)
4. electron-builder `build.productName` = `Chirality` — identity constant (MATCH)
5. electron-builder `build.appId` = `com.chirality.app` — identity constant (MATCH)
6. electron-builder artifact-name template — default `${productName}-${version}-${arch}.${ext}` (MATCH)
7. macOS arm64 DMG filename derived from package.json — `Chirality-2.0.0-arm64.dmg` vs `Chirality-3.0.0-rc.1-arm64.dmg` (MISMATCH)
8. staged app `Info.plist` `CFBundleShortVersionString`/`CFBundleVersion` — DERIVED from package.json by electron-builder (inspect with `--app-path` on a staged app)
9. named DMG file — NOT_INSPECTED (`--dmg-path` on a built DMG)
10. UI/about string or runtime report printing the product version — **ABSENT**: no `app.getVersion()`, `npm_package_version`, `NEXT_PUBLIC_APP_VERSION`, or product-version token exists in `electron/**` or `src/**`. Finding for AT-043 (UI and runtime must report `3.0.0-rc.1`); product source is outside this item's write locus, so it is recorded, not fixed.
11. release-manifest / proof-summary version field written by existing `scripts/**` — **ABSENT**: existing summaries carry digests, source revisions, and posture only.

## What applying the staged patch would change (and nothing else)

- `projects/chirality-app-dev/frontend/package.json` line 3: `"version": "2.0.0"` → `"version": "3.0.0-rc.1"`
- `projects/chirality-app-dev/frontend/package-lock.json` line 3 and line 9 (root `packages[""]`): `"version": "2.0.0"` → `"version": "3.0.0-rc.1"`

Consequences on other surfaces once applied and packaged: DMG filename becomes `Chirality-3.0.0-rc.1-arm64.dmg`; `CFBundleShortVersionString`/`CFBundleVersion` become `3.0.0-rc.1`; `app.getVersion()` (if ever used) returns `3.0.0-rc.1`. Surfaces 10–11 stay ABSENT until product work adds them.

## Rerun method

Check out the branch head; `cd projects/chirality-app-dev/frontend && npm ci`; run commands 1–4; apply the `{REPO_ROOT}` substitution; compare against `MANIFEST.sha256`.
