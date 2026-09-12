# Replacement packaged build evidence

Recorded 2026-09-12T23:19:13.480177+00:00 by delegated TASK,
gpt-6-astra, medium; native descendant of the supervising task. Packaging only,
without further delegation. One sequential build and one `desktop:dist` invocation
succeeded without source modification or retry.

## Basis

Source `26657ff9080efbba7ec1e71e6f1d08731462de0f`, merged PR #776. Parent dispatched this exact commit
following three green CI checks and `returns/REVIEW_PRODUCT_GUIDANCE_FINAL.md`
PASS across 104 paths. Parent records reviewed source `3ad6fac0d` and tested PR
head `5c3765952`; intervening differences are record-only. This artifact is a
derivative of that merged source, not independent acceptance or release authority.
Direct owner refinement continuation has no new App deliverable target, per the
parent's APP-HOLD applicability determination and existing RUN_LOG17:45Z record.

Detached checkout: `/Users/ryan/.claude/chirality-build-ui-recovery-20260912`. Fresh output: `/Users/ryan/.claude/chirality-build-ui-recovery-20260912-out`.
Earlier A2/UI builds, outputs, evidence and trial state remain preserved.
Node `v24.18.0`, npm `11.16.0`, Electron `43.2.0` from the verified distribution.
Both workspace lockfiles remained unchanged; source Git status is clean.

## Sequential execution

| Step | Command | Started UTC | Finished UTC | Exit |
|---|---|---|---|---|
| 01-runtime-npm-ci | `npm ci --no-audit --no-fund` | 2026-09-12T23:14:08Z | 2026-09-12T23:14:13Z | 0 |
| 02-frontend-npm-ci | `npm ci --no-audit --no-fund` | 2026-09-12T23:14:13Z | 2026-09-12T23:14:21Z | 0 |
| 03-instruction-root-prepare | `npm run instruction-root:prepare` | 2026-09-12T23:14:21Z | 2026-09-12T23:14:22Z | 0 |
| 04-runtime-build | `npm run runtime:build` | 2026-09-12T23:14:22Z | 2026-09-12T23:14:24Z | 0 |
| 05-app-build | `npm run build` | 2026-09-12T23:14:24Z | 2026-09-12T23:14:41Z | 0 |
| 06-desktop-dist | `npm run desktop:dist` | 2026-09-12T23:14:41Z | 2026-09-12T23:17:45Z | 0 |

Step 07 ran `npm run verify:version-identity -- --expect 3.0.0-rc.1
--app-path /Users/ryan/.claude/chirality-build-ui-recovery-20260912-out/mac-arm64/Chirality.app --dmg-path /Users/ryan/.claude/chirality-build-ui-recovery-20260912-out/Chirality-3.0.0-rc.1-arm64.dmg` from
2026-09-12T23:17:45Z to 2026-09-12T23:17:46Z, exit 0. It inspected the actual
App Info.plist and DMG filename: 12 identity surfaces match; the rendered About
value is still a native observation and no release manifest exists.

Signing selected only the recorded owner-supplied SHA1
`C7F111429F7AC5085484A9DF6F5AE7CFF552DEEF` through
`CHIRALITY_SIGNING_IDENTITY_SHA1`. All inherited APPLE_ variables and CSC import
link/password variables were removed from the build child environment without
printing values. The repository pack entry uses `--publish never`; the builder
recorded notarization skipped.

## Artifacts

| Item | Value |
|---|---|
| DMG | `/Users/ryan/.claude/chirality-build-ui-recovery-20260912-out/Chirality-3.0.0-rc.1-arm64.dmg` |
| DMG bytes | 337427404 |
| DMG SHA-256 | `d3d32be65e515d48035fd923b08870a30f3cde2f42d5c04558e2153746408caf` |
| App | `/Users/ryan/.claude/chirality-build-ui-recovery-20260912-out/mac-arm64/Chirality.app` |
| App regular-file bytes, symlinks excluded | 1046498822 |
| App regular-file count | 656 |
| App file SHA-256 manifest digest | `602743c4df652c977ffd007e5a61e96fe851f0efdf5541e9f8ea8ab9c2b33e3d` |
| App CDHash | `f111cedc07f357c20409dcf23722ab34841f3720` |
| Bundle identity | `com.chirality.app`; version/build `3.0.0-rc.1` |
| Minimum macOS | `15.0.0` |

`app-files.sha256` defines the App digest as an ordered manifest of regular-file
SHA-256 values and relative paths, excluding symlinks. DMG digest is before any
owner notarization/stapling. Same-version earlier packages remain distinct.

## Verification

- Dependency boundary PASS within `desktop:dist`, runtime profile
  `app-owned-codex`; required Runtime service/CLI proofs present and no failures.
- Stock Codex pin PASS after signing: package, lockfile and packaged executable
  all `0.154.0`, `aarch64-apple-darwin`. Signed binary hashes differ from installed
  binaries as expected; no pre-signing byte-parity claim.
- Instruction integrity PASS: all 366 files match, manifest matches, no missing,
  unexpected or mismatched files. Existing KG-001 tools/examples source
  completeness tracking remains `needs_remediation`, not an artifact mismatch.
- Explicit byte equality confirms source
  `projects/chirality-app-dev/instructions/AGENTS.md` maps to packaged
  `Contents/Resources/instruction-root/AGENTS.md`; both SHA-256 values are
  `80ccc8eaf4919815332acf9e1ac3a88bc982571392931eb6ea0bbfc72705d008`.
- Packaged `agents/registry.json` contains exactly HELP_HUMAN, HELPS_HUMANS,
  WORKING_ITEMS and TASK. Each declared path is `agents/AGENT_<role>.md` and
  every role file matches the merged source bytes.
- `codesign --verify --deep --strict --verbose=2 <App>` exit 0, valid on disk
  and satisfies its Designated Requirement. App and both bundled Codex binaries
  show Developer ID Application: Ryan Tufts, team `8A7JL35U4S`, Apple authority
  chain and hardened runtime. App secure timestamp is 2026-09-12 23:17:19 UTC.
  App and code-mode-host carry JIT entitlement; codex entitlement dictionary is
  empty. Both Codex binaries were strictly verified by the successful sign hook.
- Signature display checks exit 0. `spctl --assess --type execute --verbose=4
  <App>` exit 3, `Unnotarized Developer ID`. This is pending owner notarization,
  not Gatekeeper success.

Detailed filtered command logs 01-12, `build-results.json`,
`signature-results.json`, `artifact.json`, `app-files.sha256`, context hashes,
and reproducible recorder scripts are preserved at `/Users/ryan/.claude/chirality-build-ui-recovery-20260912-evidence`.
Every recorded command-output line containing an at-sign was omitted. The
instruction comparison is under the build checkout's
`projects/chirality-app-dev/frontend/artifacts/harness/instruction-root-integrity/latest/`.

## Handoff state

Packaging objective PASS. No unaffected source suites repeated. No App launch,
model turn, security command, live identity/auth/token/binding/keychain/Codex-home/
session/event read, notarization, stapling, deletion or publishing occurred.
Native update preservation, authentication separation, recovery/history and
rendered About observations remain with the parent/owner's guarded verification
workflow. After notarization/stapling, recheck Gatekeeper and record changed
artifact digests. Parent owns OWNER_HANDOFF, UPDATE_PRESERVATION and RUN_LOG
integration. No source/package blocker remains in this bounded packaging return.
