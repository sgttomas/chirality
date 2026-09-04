# WP-09 artifact evidence bundle — run record (DEL-09-05-V3-02)

**Boundary:** evidence only. No signing, notarization, publication, distribution, or release act; no release-readiness claim. F-APP-2 and D-APP-97 active.

## Identity of inputs

| Input | Identity |
|---|---|
| Basis commit | `0c683fb1657706316272951e4c3a0f7781b46009` (frontend tooling added on branch `codex/app-v3-nodeB-wp09-prep-2026-09-03`; product bytes unchanged) |
| `frontend/package.json` (basis) | SHA-256 `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc`; on-branch version adds three `scripts` entries only (`sbom:generate`, `notices:generate`, `verify:version-identity`); `version` remains `2.0.0` |
| `frontend/package-lock.json` | SHA-256 `717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458` (unchanged) |
| `frontend/THIRD_PARTY_NOTICES_PI.md` | SHA-256 `0195b5ce8b7be8b6bff6de3e50f6a38b3d9d4919c075e7c93ca8118b7e866328` (the four Pi packages it names are asserted present in the closure by the tool) |
| Installed `node_modules` | produced by `npm ci` from the lockfile above (warm `~/.npm` cache; exit 0) |
| Tool: `frontend/scripts/generate-third-party-notices.mjs` | see `MANIFEST.sha256` in the run record for the committed tool bytes |
| Tool: `frontend/scripts/generate-sbom.mjs` | Syft pin `v1.18.1` (`SYFT_PIN`) |

## Host and runtime

macOS 26.6.2 (Apple Silicon); Node `v24.18.0`; npm `11.16.0`; git `2.55.0`; `syft`: **not installed** (`which syft` → not found; see `sbom/which-syft.txt`). No network act, no download, no tool installation was performed.

## Commands (cwd `projects/chirality-app-dev/frontend`; env: inherited PATH/HOME/TMPDIR only; no secrets)

| # | Command | Exit | Output |
|---|---|---|---|
| 1 | `npm run -s notices:generate -- --output <bundle>/run1/THIRD_PARTY_NOTICES.md --summary <bundle>/run1/notices-summary.json` | 0 | `run1/` |
| 2 | `npm run -s notices:generate -- --output <bundle>/run2/THIRD_PARTY_NOTICES.md --summary <bundle>/run2/notices-summary.json` | 0 | `run2/` |
| 3 | `cmp run1/THIRD_PARTY_NOTICES.md run2/THIRD_PARTY_NOTICES.md` | 0 | byte-identical (determinism). Per D-APP-99 the second copy is not committed; `run2/THIRD_PARTY_NOTICES.md.sha256` records its digest (equal to run1's) and both `notices-summary.json` files carry the same `output.sha256` |
| 4 | `npm run -s sbom:generate -- --closure --dry-run --output <bundle>/sbom/sbom.closure.cdx.json` | 0 | `sbom/dry-run.closure.json` — the exact command, arguments, and environment that would produce the SBOM |
| 5 | `npm run -s sbom:generate -- --closure --output <bundle>/sbom/sbom.closure.cdx.json` | **2 (refused)** | `sbom/attempt.closure.stderr.txt`: `Syft binary not found ("syft"); install Syft v1.18.1 locally — this script does not download it` |

Absolute scratch-worktree paths inside the recorded outputs were replaced with the literal `{REPO_ROOT}` for portability after the runs; every other byte is as emitted. Rerun method: check out the branch head, `cd projects/chirality-app-dev/frontend && npm ci`, run commands 1–5, apply the same substitution, and compare with `MANIFEST.sha256`.

## Results

### Third-party notices (always possible offline) — PASS

- Output SHA-256 (both runs): `384127cc4fc7f807f089c629160beeac4557ae71260bd1e51318bee032d70f52`; 6907 lines.
- Closure: 504 lock entries (excluding root); 420 distinct third-party `name@version`; 14 first-party entries (7 `@chirality/*` `file:` links + their 7 link targets under `../../../runtime/packages/*`, whose transitive closure was walked — they declare only intra-`@chirality` dependencies).
- Required packages present: `@earendil-works/pi-agent-core@0.82.0`, `@earendil-works/pi-ai@0.82.0`, `@earendil-works/pi-coding-agent@0.82.0`, `@earendil-works/pi-tui@0.82.0`, and the seven `@chirality/*` links (`notices-summary.json` → `requiredPackages`).
- 28 installed packages carry no license file in their published tarball (`missingLicenseFile`; declared license retained from the lockfile); 39 optional platform-conditional packages are in the lockfile closure but not installed on this darwin/arm64 host (`optionalNotInstalled`; declared license from the lockfile). Both lists are in `run1/notices-summary.json` and must be reviewed by the owner before any distribution — this bundle makes no license-compliance claim.
- D-APP-99 note: `THIRD_PARTY_NOTICES.md` exceeds the ~2,000-line guideline (6,907 lines). Reason: it is the notices artifact itself (420 packages × declared license + bounded 8-line excerpt + full-text SHA-256), not a capture; excerpts are bounded and the full license text is identified by hash and byte length rather than reproduced.

### CycloneDX SBOM — `UNAVAILABLE_UNDER_BOUNDS`

- Status: **UNAVAILABLE_UNDER_BOUNDS**. `syft` at the pinned release `v1.18.1` is not installed on this host, and the brief grants no network or host-mutation act (no download, no `brew install`, no Go build).
- Exact command that would produce the closure SBOM once Syft `v1.18.1` is installed locally (from `sbom/dry-run.closure.json`): `syft scan file:{REPO_ROOT}/projects/chirality-app-dev/frontend/package-lock.json --output cyclonedx-json={REPO_ROOT}/…/Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/sbom/sbom.closure.cdx.json --quiet --source-name chirality-frontend --source-version 2.0.0` with env `SYFT_CHECK_FOR_APP_UPDATE=false SYFT_JAVASCRIPT_INCLUDE_DEV_DEPENDENCIES=false` (plus inherited `PATH`/`HOME`/`TMPDIR`), preceded by the pin check `syft version` → `Version: 1.18.1`.
- Exact command for one identified artifact (the D-APP-97 C1 unsigned staged app after `npm run desktop:pack`, or the mounted app of the CI DMG): `npm run sbom:generate -- --artifact dist/mac-arm64/Chirality.app --output <bundle>/sbom/sbom.artifact.cdx.json`. Not run: no packaged artifact was built in this tranche (packaging is not required by V3-02/V3-03 and would not change the Syft-absent outcome).
- The tool's refusal path (missing binary, exit 2) is the recorded behaviour; the mismatched-version refusal is covered by unit tests (`src/__tests__/scripts/generate-sbom.test.ts`).

## Cleanup

No disposable state was created outside this bundle; scratch trial outputs under the session scratchpad are not part of the record and were not committed.
