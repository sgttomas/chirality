# CANDIDATE — NOT ADOPTED — WP-09 authoring only; performs no release act

# Chirality App v3.0.0-rc.1 — Signing, Notarization, and Publication Runbook (candidate)

| Field | Value |
|---|---|
| Deliverable | DEL-09-05 (release-operations carrier); item DEL-09-05-V3-01 |
| Status | **CANDIDATE — NOT ADOPTED.** Authored and to be reviewed under WP-09. Adoption is the owner's act at G6a (plan §12.2 "Adopt the already reviewed release runbook at its accepted carrier path"). |
| Phase boundary | Every numbered step below is a **later owner or CHANGE act under WP-11**. **None is performed in preparation.** F-APP-2 and D-APP-97 remain active; DEP-09-05-015 (G6a exact-candidate owner ruling) gates WP-11 entry. REQ-002/REQ-003, AC-002, VER-002 (`ScopeOfWork.md`). |
| Authored | 2026-09-03, basis `0c683fb1657706316272951e4c3a0f7781b46009`, run record `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_B_2026-09-03/` |
| Completion reference | `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`) — cited by section number for what a gate or scenario *means*; **not authority, not status, not a queue** |
| App documents cited by path | `docs/BUILD_AND_RELEASE.md` (§4 command map, §5 evidence bundles, §8 packaging skeleton, §9 future CI/release mapping) · `docs/RELEASE_QUALITY_GATES.md` (§10 Packaging gate, §12 waivers, §13 Shared Runtime Gate) · `docs/RELEASE_QUALITY_RUNBOOK.md` (§2–§6) · `docs/ISSUE_READINESS_PROFILES.md` (§3 Validation/release profile) · `docs/CONTRACT.md` K-RELEASE-1, K-KEY-1, K-NET-1 |
| Companion | `Exact_Candidate_Identity_and_Custody_Checklist_CANDIDATE.md` (same folder) |

## 0. What this document is, and is not

This runbook states, as a reviewable procedure, exactly how the owner (and CHANGE for authorized Git/publication work) would take an **owner-named exact candidate** through signing, notarization, stapling, Gatekeeper verification, credential-transition review, exact-byte reruns, GitHub prerelease publication, and public download backcheck, and how recovery and rollback work. It exists so that no release procedure is authored ad hoc during signing (plan §12.2).

It is **not** a signing, notarization, publication, distribution, release-readiness, lifecycle, certification, or professional-approval act, and it does not make one more likely. Reading, reviewing, or seating this document changes no gate state. Nothing in it lifts F-APP-2, D-APP-97, APP-HOLD-1, or K-RELEASE-1.

Identity facts used below are taken only from the committed tree (`frontend/package.json` `build`): `productName` `Chirality`, `appId` `com.chirality.app`, macOS `minimumSystemVersion` `15.0.0`, target `dmg` × `arm64`, default electron-builder artifact name `Chirality-<version>-arm64.dmg`, Electron `43.2.0` (D-APP-98), `CSC_IDENTITY_AUTO_DISCOVERY=false` in `desktop:pack`/`desktop:dist`. **No Apple Team ID, Developer ID certificate name, Apple ID, App Store Connect key, or notarytool profile name is stated anywhere in this repository; each is supplied by the owner from local custody at G6a and is never committed.** Where a value is unknown it is written `<TBD-owner>`.

Gate meanings (plan §10.1): **G5** REVIEW of the preparation package (this runbook seated and reviewed is one of its inputs) · **G6a** owner's exact-candidate ruling (K-RELEASE-1 amendment / F-APP-2 lift for that candidate; identities frozen; runbook adopted) · **G6b** owner signs/notarizes/staples the exact frozen bytes in reviewed order without rebuild · **G-KEY** owner + security review of credential transitions on the real identities · **G7** owner reruns the full evidence set on the exact signed bytes · **G8** owner/CHANGE publish the prerelease and backcheck the public path; immutable snapshot recorded.

## 1. Preflight checklist (G6a inputs — owner verifies before any Apple service call; plan §12.2 bullet 3)

Every row must be `YES` with evidence before step 3 begins. Preparation status for every row today is **NOT PERFORMED**.

| # | Preflight item | How verified (later act) | Evidence obligation |
|---|---|---|---|
| P1 | Owner G6a ruling exists naming the exact candidate: source SHA, unsigned candidate DMG SHA-256, release identity `3.0.0-rc.1`, publication route (GitHub prerelease) — plan §12.2 bullet 1 | Ruling record in `execution/_Coordination/_DECISIONS/` and the A-series steer record | Ruling path + SHA-256 in the WP-11 execution record (DEL-09-05-V3-05) |
| P2 | D-APP-97 / F-APP-2 lifted **for that candidate only** by the same ruling | Same ruling text | Same |
| P3 | Version identity applied to product (DEL-09-05-V3-06 landed on `main`); `npm run verify:version-identity -- --expect 3.0.0-rc.1` reports no `MISMATCH` on the frozen source | Command output on the frozen checkout | `Evidence/VERSION_IDENTITY_3.0.0-rc.1/` successor report bound to the frozen SHA |
| P4 | Identity freeze recorded (AT-039): source SHA, `package-lock.json` SHA-256, Electron `43.2.0` supply pin (`npm run electron:supply-chain` PASS), Pi supply pin (`npm run pi:supply-chain` PASS), accepted App Server digest and generated schema/config digest from the Root G2 snapshot (or explicit `UNAVAILABLE` if Root has not accepted G2 — then **stop**, P4 fails), notices SHA-256, SBOM SHA-256, this runbook's SHA-256 | Freeze table in the execution record | Freeze table with every hash recomputable |
| P5 | This runbook adopted **as reviewed** at this carrier path; G5 REVIEW verdict recorded; no edit since review | G5 record + `git log` on this file | Review record path + file SHA-256 |
| P6 | Self-signed A→B transition drill (DEL-09-05-V3-04) evidence current for the frozen packaging configuration | Drill record cited | Drill record path |
| P7 | Developer ID Application identity present in the owner's **local** keychain; Team ID known to the owner; `security find-identity -v -p codesigning` lists exactly one intended identity | Local command, output redacted to identity hash + name in the record | Redacted output |
| P8 | notarytool credentials stored **locally** (`xcrun notarytool store-credentials <profile>` with an App Store Connect API key or app-specific password); nothing in `.env`, repository, CI secrets, or shell history | Owner attestation + `env | grep -E '^(CSC_LINK|CSC_KEY_PASSWORD|APPLE_ID|APPLE_APP_SPECIFIC_PASSWORD|APPLE_TEAM_ID)='` empty in every CI job (the active workflow already asserts this) | Attestation line + CI assertion reference |
| P9 | Fuse and entitlement inventory for the frozen unsigned candidate recorded (step 3.C) and the RunAsNode posture is `usable` | Inventory file | Inventory SHA-256 |
| P10 | Clean signing host: macOS 15+ Apple Silicon, Xcode command-line tools present (`codesign`, `spctl`, `xcrun notarytool`, `xcrun stapler`, `hdiutil`), no local dev server running, `git status` clean at the frozen SHA | Host record | Tool versions in the execution record |
| P11 | Rollback plan (section 4) read and the "do not proceed if" list (section 2) is clear | Owner initials in the execution record | — |

## 2. Do not proceed if (any one stops the lane; return to the owner)

- No G6a ruling names **this exact** candidate by digest, or the ruling names a different digest than the bytes on disk.
- Any P-row in section 1 is not `YES`.
- The candidate was **rebuilt** after G6a (plan §12.2 bullet 4: "Do not rebuild after final acceptance without restarting the gate").
- `codesign --display` on the unsigned candidate shows an `Authority=` line or a `TeamIdentifier` (opportunistic signing; G5 fail condition).
- The signed Electron binary does **not** honor `ELECTRON_RUN_AS_NODE=1` for the supervisor/daemon entry (step 3.E; AT-058): stop, and route the separately governed helper alternative as new scope — never work around it with an Electron-spawned shim.
- A nested vendor signature is invalid before signing, or nested bytes differ from the freeze inventory (AT-047).
- Any Apple credential would need to be placed in GitHub Actions, a repository file, or an agent context.
- `stapler validate`, `spctl --assess`, or `codesign --verify --deep --strict` fails on the signed bytes.
- Public download bytes differ from the published digest (G8).
- Any step would replace bytes under an existing tag or asset name (section 4).
- The owner is not the person performing steps 3.A–3.K; an agent never performs them.

## 3. Procedure (each step: gate · decision owner · evidence obligation · **NOT PERFORMED in preparation**)

Conventions: `$CANDIDATE` = frozen unsigned candidate checkout at the G6a source SHA; `$APP` = `frontend/dist/mac-arm64/Chirality.app`; `$DMG` = `frontend/dist/Chirality-3.0.0-rc.1-arm64.dmg`; `$ID` = Developer ID Application identity name as listed by `security find-identity` (`<TBD-owner>`); `$TEAM` = Team ID (`<TBD-owner>`); `$PROFILE` = notarytool keychain profile name (`<TBD-owner>`); `$EVID` = the WP-11 execution record directory (DEL-09-05-V3-05). All commands run from `projects/chirality-app-dev/frontend/` unless stated.

### 3.A Freeze the release identity (AT-039)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G6a | Human owner (Ryan Tufts) | Freeze table: every identity in P4 with SHA-256, plus `git rev-parse HEAD`, `shasum -a 256 package-lock.json`, the `electron:supply-chain` and `pi:supply-chain` outputs, `npm run notices:generate -- --output $EVID/THIRD_PARTY_NOTICES.md --summary $EVID/notices-summary.json`, `npm run sbom:generate -- --closure --output $EVID/sbom.closure.cdx.json` (pinned Syft `v1.18.1`, see `scripts/generate-sbom.mjs`), `npm run verify:version-identity -- --expect 3.0.0-rc.1 --json $EVID/version-identity.json` | NOT PERFORMED |

The freeze binds source, lock, Electron, App Server, schema/config, notices, SBOM, procedure, and version **before** signing (plan §12.2 bullet 1; AT-039). After G6a the identity may not change without restarting G6a.

### 3.B Build once from the frozen identity, or promote the frozen candidate (AT-038, AT-047)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G6a → G6b | Human owner | Build log; `shasum -a 256 $DMG $APP/Contents/MacOS/Chirality`; nested-byte inventory before and after (below); `codesign --display --verbose=4 $APP` showing **no** `Authority=` line and `TeamIdentifier=not set` before signing | NOT PERFORMED |

Command (unchanged from `docs/BUILD_AND_RELEASE.md` §4): `CSC_IDENTITY_AUTO_DISCOVERY=false npm run desktop:dist`. If the G6a ruling names an already-built unsigned candidate, **promote those bytes** instead of rebuilding; verify their SHA-256 equals the ruling's digest first.

Nested-byte inventory (AT-047) — record path, size, SHA-256, and `codesign -dvvv` result (or `code object is not signed at all`) for every Mach-O and native module in the candidate, at minimum:

- `Contents/MacOS/Chirality` (Electron host; also the Electron-as-Node supervisor/daemon host — `--runtime-daemon` relaunch and the `chirality` CLI launcher which sets `ELECTRON_RUN_AS_NODE=1`, `electron/cli-launcher.ts`);
- `Contents/Frameworks/Electron Framework.framework` and every `Contents/Frameworks/Chirality Helper*.app`;
- `Contents/Resources/app.asar.unpacked/**/*.node` (`@earendil-works/pi-tui/native/darwin/prebuilds/darwin-arm64/darwin-modifiers.node`, `@mariozechner/clipboard-darwin-arm64/**/*.node` and siblings unpacked by `build.asarUnpack`) and `**/*.wasm`;
- `Contents/Resources/runtime-cli/chirality-cli.mjs` (JavaScript, not Mach-O — inventoried by hash, not signed separately);
- the App Server binary and CLI host as shipped by the accepted Root G2 snapshot under `Contents/Resources/` (`<TBD-Root-G2>` path; if absent, record `ABSENT` and P4 fails).

Any drift between the pre-signing inventory and the freeze table fails G5/G6a.

### 3.C Fuses, hardened runtime, and entitlements for the `--runtime-daemon` / supervisor entry (AT-058, G-SBX)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G6a (accept posture) · G6b (prove on signed bytes) | Human owner (+ security review for G-SBX) | Fuse inventory output; entitlements plist SHA-256; `codesign -d --entitlements :- $APP` output | NOT PERFORMED |

Requirements the owner accepts at G6a (plan §6.3, §12.1 bullet 6, §12.2 bullet 3):

1. **Electron fuses** — inventory with `npx @electron/fuses read --app $APP` (package present transitively through electron-builder; no dependency is added by this runbook). Required posture: `RunAsNode` **enabled** (the daemon relaunch and the bundled CLI depend on `ELECTRON_RUN_AS_NODE=1`), `EnableNodeCliInspectArguments` disabled, `EnableNodeOptionsEnvironmentVariable` disabled, `OnlyLoadAppFromAsar` enabled, `EnableEmbeddedAsarIntegrityValidation` enabled where the packaged layout permits it (the `app.asar.unpacked` native modules are loaded from outside the archive; verify the integrity fuse does not break them before accepting), `EnableCookieEncryption` per product decision. **A fuse posture that disables `RunAsNode` is not acceptable for rc.1; it triggers the separately governed helper fallback, not a workaround.** Record the inventory verbatim.
2. **Hardened runtime** — sign with `--options runtime` (electron-builder default `hardenedRuntime: true`); RC does **not** adopt Apple App Sandbox (plan §12.1 bullet 3).
3. **Entitlements** — candidate set to be confirmed against the fuse inventory and the packaged proofs, not assumed: `com.apple.security.cs.allow-jit` (V8), `com.apple.security.cs.allow-unsigned-executable-memory` (Electron requirement), `com.apple.security.cs.disable-library-validation` **only if** any unpacked `.node` module remains signed by a different Team ID after step 3.D (prefer re-signing every nested module with `$ID` so this entitlement is unnecessary). No network-client restriction applies outside App Sandbox; K-NET-1 remains enforced by the app, not by entitlements. The entitlements file is committed only if the owner rules so at G6a; until then it is local custody.
4. **Environment** — hardened runtime strips `DYLD_*` variables; `ELECTRON_RUN_AS_NODE` is not stripped, but it is honored **only while the `RunAsNode` fuse is on**. This is the coupling AT-058 proves on the signed bytes (step 3.E).

### 3.D Sign in the exact nested order (G6b)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G6b | Human owner (performs); security review (order accepted at G6a) | Per-object `codesign -dvvv` after each layer; final `codesign --verify --deep --strict --verbose=2 $APP` and `$DMG` outputs; signing log with timestamps | NOT PERFORMED |

Order (innermost first; each layer signed with `codesign --force --timestamp --options runtime --sign "$ID"` and, for executables that need them, `--entitlements <file>`):

1. **App Server / CLI host binaries** shipped as extra resources (`Contents/Resources/<Root-G2 path>`), and every unpacked native module `Contents/Resources/app.asar.unpacked/**/*.node`.
2. **Electron helpers and framework**: each `Contents/Frameworks/Chirality Helper*.app`, then `Contents/Frameworks/Electron Framework.framework` (its nested `Libraries/*.dylib` and helper executables first, then the framework bundle).
3. **The app bundle** `$APP` (with the accepted entitlements), so its seal covers every nested code object.
4. **The DMG** (after step 3.F stapled the app and the DMG was rebuilt around the stapled app): `codesign --force --timestamp --sign "$ID" $DMG`.

Expected result after (3): `codesign --verify --deep --strict --verbose=2 $APP` prints `$APP: valid on disk` and `$APP: satisfies its Designated Requirement`; `codesign -dvvv $APP` shows `Authority=Developer ID Application: <name> ($TEAM)`, `Authority=Developer ID Certification Authority`, `Authority=Apple Root CA`, `TeamIdentifier=$TEAM`, `Runtime Version=` set, and flags containing `runtime`. Any `code object is not signed at all` or `a sealed resource is missing or invalid` means the order was wrong — stop, do not re-sign over a bad seal without recording it.

electron-builder can perform layers 1–3 itself when `CSC_NAME`/`CSC_LINK` is supplied; if the owner elects that path at G6a, `CSC_IDENTITY_AUTO_DISCOVERY` must be set explicitly for that one local invocation and the post-signing verification is identical. Either path is an owner act; neither runs in CI.

### 3.E Prove the signed Electron binary still hosts the supervisor/daemon entry (AT-058)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G6b → G7 (G-HELPER/G-SBX applicability) | Human owner | Command transcript; socket path and permissions; `launchctl print` excerpt; process-group termination proof; exit codes | NOT PERFORMED |

On the **signed** `$APP`: run the packaged daemon entry (`$APP/Contents/MacOS/Chirality --runtime-daemon` through the governed LaunchAgent install, per `docs/BUILD_AND_RELEASE.md` §11) and the bundled CLI (`~/.local/bin/chirality`, which sets `ELECTRON_RUN_AS_NODE=1`) and rerun the packaged proofs that exist today: `node ./scripts/run-packaged-launchagent-runatload-proof.mjs --app-path $APP …`, `run-packaged-launchagent-login-proof.mjs`, `run-packaged-daemon-instruction-root-proof.mjs`, `npm run proof:packaged-security -- --app-path $APP …`, `npm run harness:validate:agentsdk-packaged-proof -- --bundle-root $APP/Contents/Resources`. Expected: every summary `status: pass`; daemon socket created with private permissions; launchd signals honored; worker process groups terminated on shutdown. **Failure stops the lane** (section 2).

### 3.F Notarize and staple (G6b)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G6b | Human owner | `notarytool submit` output with submission id and `status: Accepted`; `notarytool log <id>` JSON saved; `stapler staple` and `stapler validate` outputs for app and DMG | NOT PERFORMED |

1. Zip the signed app for submission: `ditto -c -k --keepParent "$APP" "$EVID/Chirality-3.0.0-rc.1-arm64.app.zip"`.
2. Submit: `xcrun notarytool submit "$EVID/Chirality-3.0.0-rc.1-arm64.app.zip" --keychain-profile "$PROFILE" --wait`. Expected final line: `status: Accepted`. Save `xcrun notarytool log <submission-id> "$EVID/notarytool-log-app.json"`; it must contain `"status": "Accepted"` and no `issues` of severity `error`.
3. Staple the app: `xcrun stapler staple "$APP"` → `The staple and validate action worked!`.
4. Build the DMG around the stapled app (the same electron-builder DMG target, from the same frozen configuration, with the stapled `$APP` as input — no source rebuild), then sign it (step 3.D layer 4).
5. Submit the DMG: `xcrun notarytool submit "$DMG" --keychain-profile "$PROFILE" --wait` → `status: Accepted`; save the log as `notarytool-log-dmg.json`.
6. Staple the DMG: `xcrun stapler staple "$DMG"` → `The staple and validate action worked!`.

Notarization is the only Apple service call in this runbook; it occurs exactly here and only under G6b. No preparation build is ever submitted.

### 3.G Gatekeeper and identity verification on the exact signed bytes (G6b, rerun at G7 and G8)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G6b (first), G7, G8 (repeat on public bytes) | Human owner | Verbatim command outputs saved under `$EVID/verify/`; SHA-256 of `$DMG`, `$APP/Contents/MacOS/Chirality`, and the mounted copy | NOT PERFORMED |

| Command | Expected output (must match) |
|---|---|
| `codesign --verify --deep --strict --verbose=2 "$APP"` | `…/Chirality.app: valid on disk` and `…/Chirality.app: satisfies its Designated Requirement` |
| `codesign -dvvv "$APP" 2>&1 \| grep -E '^(Identifier\|TeamIdentifier\|Authority\|Runtime Version\|CodeDirectory)'` | `Identifier=com.chirality.app`; `TeamIdentifier=$TEAM`; three `Authority=` lines ending in `Apple Root CA`; `Runtime Version=` present; `CodeDirectory … flags=0x10000(runtime)` |
| `codesign -d --entitlements :- "$APP"` | Exactly the accepted entitlement keys from step 3.C; nothing else |
| `spctl --assess --type execute --verbose=4 "$APP"` | `…/Chirality.app: accepted` and `source=Notarized Developer ID` |
| `xcrun stapler validate "$APP"` | `The validate action worked!` |
| `codesign --verify --verbose=2 "$DMG"` | `…dmg: valid on disk` / `satisfies its Designated Requirement` |
| `spctl --assess --type open --context context:primary-signature --verbose=4 "$DMG"` | `…dmg: accepted` and `source=Notarized Developer ID` |
| `xcrun stapler validate "$DMG"` | `The validate action worked!` |
| `hdiutil verify "$DMG"` | `…: verified   CRC32 …` (no error) |
| `hdiutil attach -nobrowse -readonly -mountpoint "$MNT" "$DMG"` then `shasum -a 256 "$MNT/Chirality.app/Contents/MacOS/Chirality" "$APP/Contents/MacOS/Chirality"` | The two digests are identical |
| `plutil -extract CFBundleShortVersionString raw "$APP/Contents/Info.plist"`, same for `CFBundleVersion`, `LSMinimumSystemVersion` | `3.0.0-rc.1`, `3.0.0-rc.1`, `15.0.0` |
| `lipo -archs "$APP/Contents/MacOS/Chirality"` | `arm64` |
| `npm run verify:version-identity -- --expect 3.0.0-rc.1 --app-path "$APP" --dmg-path "$DMG" --require-all` | `Result: PASS` (requires the AT-043 UI/runtime surfaces to exist by then; until they do, `--require-all` reports them `ABSENT` and G7 cannot pass AT-043) |

Any deviation is a G6b/G7 fail condition ("Signature/notary/staple failure or byte/source mismatch").

### 3.H Credential signature transition on the real identities (G-KEY, AT-051)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G-KEY | Human owner + security review | Transition record: App Server keyring state and Electron `safeStorage` state before/after unsigned/ad-hoc → Developer ID, and signed N → N+1 where applicable; typed state observed (`usable` / `reauthentication-required` / `decrypt-failed`); no plaintext, no silent loss | NOT PERFORMED |

The DEL-09-05-V3-04 self-signed A→B drill is preparation evidence only; it neither predicts Developer ID behavior nor satisfies G-KEY (plan §12.1 bullet 7). G-KEY runs on the signed bytes from step 3.D before G7.

### 3.I Exact-bytes reruns (G7; AT-041 clean-machine smoke, AT-043 identity, AT-001 supply)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G7 | Human owner | Full evidence set on the signed/notarized/stapled bytes: checksums, `THIRD_PARTY_NOTICES.md` and CycloneDX SBOM regenerated for the exact artifact (`npm run sbom:generate -- --artifact "$MNT/Chirality.app" --output $EVID/sbom.artifact.cdx.json`) and compared with the freeze, clean-machine install and launch on macOS 15+ arm64, migration, native-engine regression, login/turn/delegation/interrupt/quit, PB-08 release-notes review, rollback rehearsal; no open P0/high finding | NOT PERFORMED |

No unsigned or preparation evidence may be substituted at G7 (plan §10.1 G7 fail condition; §11.1).

### 3.J Publish the GitHub prerelease (G8 — CHANGE performs only the authorized Git/publication work)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G8 | Human owner decides; CHANGE executes the tag and upload exactly as authorized | Tag name and object SHA; `gh release view` JSON; asset list with sizes and digests; release-notes SHA-256 | NOT PERFORMED |

1. Tag the frozen source: `git tag -a v3.0.0-rc.1 <frozen-SHA> -m "Chirality App v3.0.0-rc.1 (prerelease)"` and push the tag only after G7 passes. The tag object must point at the exact SHA in the freeze table.
2. Assemble the publication set (plan §12.3): `Chirality-3.0.0-rc.1-arm64.dmg` (signed, notarized, stapled); `SHA256SUMS` (`shasum -a 256 Chirality-3.0.0-rc.1-arm64.dmg > SHA256SUMS`); the release manifest binding source, lock, App Server, schema, config, notices, SBOM, signature/notary, and test-snapshot identities; `THIRD_PARTY_NOTICES.md`; the CycloneDX JSON SBOM; PB-08-reviewed release notes (Codex as Preview, ChatGPT login behavior, data transmission/consent, supported macOS/arch, known limitations, support route, rollback instructions).
3. Publish: `gh release create v3.0.0-rc.1 --prerelease --verify-tag --title "Chirality App v3.0.0-rc.1" --notes-file "$EVID/RELEASE_NOTES.md" "$DMG" SHA256SUMS release-manifest.json THIRD_PARTY_NOTICES.md sbom.cdx.json`. Expected: the release page URL; `gh release view v3.0.0-rc.1 --json isPrerelease,tagName,assets` shows `isPrerelease: true` and every asset with the expected size.
4. **Never** upload, replace, or delete an asset on an existing tag after publication (section 4).

The existing unsigned CI workflow (`.github/workflows/desktop-release-template.yml`) is **not** the publication path and is not changed by this runbook; it stays PR/manual, `contents: read`, unsigned, credential-free (plan §12.2 bullet 9). Wiring any SBOM/notice step into repo-root workflows is SCOPE_AMENDMENT S-6 and is not part of this procedure.

### 3.K Public download backcheck and immutable publication snapshot (G8, AT-042)

| Gate | Decision owner | Evidence obligation | Preparation status |
|---|---|---|---|
| G8 | Human owner | Download transcript; digest comparison; full step 3.G table rerun on the downloaded bytes; launch + version observation; immutable publication snapshot (`$EVID/PUBLICATION_SNAPSHOT.md` + `MANIFEST.sha256`) | NOT PERFORMED |

1. From a machine and account **not** used for signing, download through the user-visible release page (`curl -L -o ~/Downloads/Chirality-3.0.0-rc.1-arm64.dmg "<browser-download URL from the release page>"`).
2. `shasum -a 256 ~/Downloads/Chirality-3.0.0-rc.1-arm64.dmg` must equal the published `SHA256SUMS` entry and the G6b digest.
3. Rerun every row of the step 3.G table on the downloaded DMG and its mounted app (Gatekeeper assessment on the quarantined download is the real test: `xattr -p com.apple.quarantine` present; `spctl --assess … accepted`).
4. Install by drag to `/Applications`, launch, confirm the UI/about and runtime report `3.0.0-rc.1` (AT-043), complete the core + Codex smoke (AT-041 scope).
5. Record the immutable publication snapshot: release URL, tag SHA, every asset digest, verification outputs, host facts, and the statement that G8 passed. This snapshot closes DEL-09-05-V3-05.

## 4. Recovery and rollback (plan §12.4; never replace bytes under the same version/tag)

| Situation | Action (later owner/CHANGE act) | Gate | Evidence |
|---|---|---|---|
| Notarization `Invalid` or staple failure | Stop. Save `notarytool log`. Fix the cause in source or configuration → this is a **new candidate**: return to G6a with a new digest; the old candidate is retired in the execution record. | G6b | Log + retirement note |
| Signed binary fails the supervisor entry (3.E) | Stop. Do not ship a fuse workaround. Route the helper alternative as new governed scope. | G6b/G-HELPER | Transcript |
| G7 finding (P0/high) after signing | Do not publish. Fix → new version identity (`3.0.0-rc.2` or as ruled), repeat the full lane from 3.A. Never re-sign or patch bytes under `3.0.0-rc.1`. | G7 | Finding record |
| Defect discovered after publication | Withdraw the affected asset (`gh release delete-asset` or mark the prerelease as withdrawn in its notes), keep the tag, keep the evidence, record the incident reason; point users to the last accepted release if safe and document data compatibility; a fixed candidate receives a **new** version and repeats the full release lane. | G8 (rollback) | Incident record in the publication snapshot |
| Public download digest mismatch (3.K) | Treat as compromised publication: withdraw immediately, preserve evidence, investigate before any re-publication under a new version. | G8 | Incident record |
| Credential compromise (certificate, API key, app-specific password) | Revoke in the Apple Developer / App Store Connect portal (owner act), rotate local custody, record the revocation; already-notarized artifacts remain valid unless Apple revokes the ticket. | — | Custody record (no secret values) |

## 5. Credential custody (plan §12.2 bullet 9; K-KEY-1)

- **Local custody only.** The Developer ID Application certificate and private key live in the owner's login keychain on the signing host; notarytool credentials live in the owner's keychain profile (`xcrun notarytool store-credentials`). The App Store Connect API key file (`.p8`) is stored outside every repository and outside every agent-accessible working directory.
- **Nothing in GitHub Actions.** No `CSC_LINK`, `CSC_KEY_PASSWORD`, `APPLE_ID`, `APPLE_APP_SPECIFIC_PASSWORD`, `APPLE_TEAM_ID`, or API-key secret is created in the repository or organization; the active workflow fails if any is present. A future hosted-signing design requires its own explicit owner decision and threat/custody review.
- **Nothing in the repository or evidence.** Evidence records contain identity **names/hashes** and command outputs only; never a key, password, profile secret, or `.p8`. `npm run proof:secret-scan` runs over the execution record before it is committed.
- **Agents never hold or use these credentials.** An agent may generate evidence tooling and this runbook; it never signs, submits, staples, or publishes.

## 6. Evidence obligations by gate (summary)

| Gate | Obligation (durable, non-secret, recomputable per the workplan Evidence contract) |
|---|---|
| G5 | This runbook reviewed (G5 REVIEW record); notices + SBOM tooling and one evidence bundle (`Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/`); version-identity check and staged patch (`Evidence/VERSION_IDENTITY_3.0.0-rc.1/`); unsigned candidate posture (D-APP-97 C1 workflow run) |
| G6a | Owner ruling; freeze table (3.A); fuse/entitlement inventory (3.C); preflight P1–P11 |
| G6b | Signing log and per-layer verification (3.D); supervisor proof on signed bytes (3.E); notarization logs and staple results (3.F); verification table (3.G) |
| G-KEY | Credential transition record (3.H) |
| G7 | Exact-bytes rerun set (3.I) including regenerated SBOM/notices comparison and AT-043 identity on the signed bytes |
| G8 | Release JSON and asset digests (3.J); public download backcheck and immutable publication snapshot (3.K) |

## 7. Review and adoption route

1. G5: a fresh, read-only REVIEW instance examines this candidate against REQ-002 and plan §12; a finding-free PASS is recorded in this deliverable folder before the candidate is called "reviewed".
2. Any edit after the G5 review reopens review.
3. G6a: the owner adopts the reviewed bytes **at this path** (or rules an amendment). Adoption is recorded in the ruling; the file is not renamed or "activated" by an agent.
4. WP-11 execution is recorded in DEL-09-05-V3-05, which remains `NOT_SELECTABLE_UNTIL` the G6a ruling.

*End of candidate. No release act was performed in authoring this document.*
