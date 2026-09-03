# CANDIDATE — NOT ADOPTED — WP-09 authoring only; performs no release act

# Exact-Candidate Identity and Custody Checklist (candidate)

| Field | Value |
|---|---|
| Deliverable | DEL-09-05 (release-operations carrier); item DEL-09-05-V3-01; companion to `Release_Runbook_CANDIDATE_2026-09-03.md` |
| Status | **CANDIDATE — NOT ADOPTED.** Every row is a later owner or CHANGE act under WP-11. Preparation status of every row is `NOT PERFORMED`. F-APP-2 and D-APP-97 remain active; DEP-09-05-015 (G6a) gates WP-11. |
| Purpose | The single sheet the owner fills at G6a to bind the **exact** candidate (AT-039) and to attest custody (plan §12.2 bullet 9), and that G6b/G-KEY/G7/G8 reread on the **same bytes** |
| Authored | 2026-09-03, basis `0c683fb1657706316272951e4c3a0f7781b46009` |
| Non-authority | Plan sections cited for meaning only (`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`) |

Values known from the committed tree are pre-filled; everything else is `<TBD-owner>` (supplied at G6a from local custody, **never committed**) or `<TBD-Root-G2>` (supplied by the accepted Root G2 snapshot through a routed notice). An agent never fills a `<TBD-owner>` cell.

## A. Exact candidate identity (AT-039 freeze — G6a; owner)

| # | Identity | Value | Source of truth | Filled at | Status |
|---|---|---|---|---|---|
| A1 | Release identity | `3.0.0-rc.1` | Owner G6a ruling; DEL-09-05-V3-06 applied on `main` | G6a | NOT PERFORMED |
| A2 | Product name / bundle id | `Chirality` / `com.chirality.app` | `frontend/package.json` `build.productName`, `build.appId` | pre-filled (tree) | present |
| A3 | Target | macOS 15+ (`LSMinimumSystemVersion` `15.0.0`), `arm64`, DMG | `frontend/package.json` `build.mac`; REQ-004 | pre-filled (tree) | present |
| A4 | Expected DMG filename | `Chirality-3.0.0-rc.1-arm64.dmg` | electron-builder default artifact name (`scripts/verify-version-identity.mjs` derived surface) | pre-filled (derived) | present |
| A5 | Frozen source SHA | `<TBD-owner>` (40 hex) | `git rev-parse HEAD` on the frozen checkout | G6a | NOT PERFORMED |
| A6 | `package-lock.json` SHA-256 at A5 | `<TBD-owner>` | `shasum -a 256 frontend/package-lock.json` | G6a | NOT PERFORMED |
| A7 | Electron supply identity | `43.2.0`; `electron-v43.2.0-darwin-arm64.zip` SHA-256 `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28` | `scripts/verify-electron-dist.mjs` `ELECTRON_SUPPLY_PIN`; D-APP-98 | pre-filled (tree); re-verified at G6a (`npm run electron:supply-chain`) | present |
| A8 | Pi supply identity | `@earendil-works/*` `0.82.0` | `scripts/verify-pi-supply-chain.mjs`; `THIRD_PARTY_NOTICES_PI.md` | pre-filled (tree); re-verified at G6a (`npm run pi:supply-chain`) | present |
| A9 | App Server binary digest and generated protocol schema/config digest (AT-001) | `<TBD-Root-G2>` | Accepted Root G2 snapshot via routed notice | G6a (must exist, else stop) | NOT PERFORMED |
| A10 | Third-party notices SHA-256 | `<TBD-owner>` at freeze; preparation sample recorded in `Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/` | `npm run notices:generate` | G6a | NOT PERFORMED |
| A11 | CycloneDX SBOM SHA-256 (pinned Syft `v1.18.1`) | `<TBD-owner>` | `npm run sbom:generate -- --closure …` and `-- --artifact <app>` | G6a (closure) / G7 (artifact) | NOT PERFORMED |
| A12 | Runbook SHA-256 (adopted bytes) | `<TBD-owner>` = SHA-256 of `Release_Runbook_CANDIDATE_2026-09-03.md` as reviewed at G5 | `shasum -a 256` | G6a | NOT PERFORMED |
| A13 | Unsigned candidate DMG SHA-256 (pre-signing) | `<TBD-owner>` | `shasum -a 256 frontend/dist/Chirality-3.0.0-rc.1-arm64.dmg` | G6a | NOT PERFORMED |
| A14 | Unsigned candidate executable SHA-256 | `<TBD-owner>` | `shasum -a 256 …/Chirality.app/Contents/MacOS/Chirality` | G6a | NOT PERFORMED |
| A15 | Nested-byte inventory SHA-256 (AT-047) | `<TBD-owner>` | Inventory file from runbook step 3.B | G6a | NOT PERFORMED |
| A16 | Fuse/entitlement inventory SHA-256 (AT-058) | `<TBD-owner>` | Runbook step 3.C | G6a | NOT PERFORMED |
| A17 | Signed DMG SHA-256 (post-staple) | `<TBD-owner>` | Runbook step 3.G | G6b | NOT PERFORMED |
| A18 | Signed executable SHA-256 | `<TBD-owner>` | Runbook step 3.G | G6b | NOT PERFORMED |
| A19 | Notarization submission ids (app, DMG) | `<TBD-owner>` | `xcrun notarytool submit … --wait` | G6b | NOT PERFORMED |
| A20 | Git tag and tag object SHA | `v3.0.0-rc.1` / `<TBD-owner>` | `git rev-parse v3.0.0-rc.1^{}` = A5 | G8 | NOT PERFORMED |
| A21 | Release URL and asset digests | `<TBD-owner>` | `gh release view v3.0.0-rc.1 --json …` | G8 | NOT PERFORMED |
| A22 | Public download DMG SHA-256 (AT-042) | `<TBD-owner>` = A17 | Runbook step 3.K | G8 | NOT PERFORMED |

Binding rule: A13/A14 must equal the digests named in the G6a ruling; A17/A18 must be the bytes verified at G6b, rerun at G7, and downloaded at G8; A22 must equal A17. Any inequality is a stop (runbook section 2).

## B. Version identity binding (AT-043 — G5/G7; owner)

| # | Surface | Expected | How checked | Gate | Status |
|---|---|---|---|---|---|
| B1 | `package.json` `version`, `package-lock.json` (top-level and `packages[""]`) | `3.0.0-rc.1` | `npm run verify:version-identity -- --expect 3.0.0-rc.1` declared surfaces `MATCH` | G5 (after V3-06 lands) | NOT PERFORMED (today: `2.0.0`, staged patch only in `Evidence/VERSION_IDENTITY_3.0.0-rc.1/`) |
| B2 | Bundle metadata `CFBundleShortVersionString` / `CFBundleVersion` | `3.0.0-rc.1` | same command with `--app-path` | G7 | NOT PERFORMED |
| B3 | DMG filename | `Chirality-3.0.0-rc.1-arm64.dmg` | same command with `--dmg-path` | G7 | NOT PERFORMED |
| B4 | UI/about string and runtime report | `3.0.0-rc.1` | same command `--require-all` once the surfaces exist; today the check reports them `ABSENT` (no `app.getVersion()`/about surface in `electron/**` or `src/**`) — a G7 blocker until product work adds them under its own item | G7 | NOT PERFORMED |
| B5 | Release manifest and updater/publication metadata | `3.0.0-rc.1` | Manifest field review at G8; today no script writes a product-version field (`ABSENT`) | G8 | NOT PERFORMED |

## C. Custody attestations (plan §12.2 bullet 9; K-KEY-1 — owner; security review at G-KEY)

| # | Attestation | Evidence (non-secret) | Gate | Status |
|---|---|---|---|---|
| C1 | Developer ID Application identity exists only in the owner's local keychain on the signing host | `security find-identity -v -p codesigning` output redacted to `<hash> "Developer ID Application: <name> (<TEAM>)"` | G6a | NOT PERFORMED |
| C2 | Team ID recorded in the execution record only (never in repository config) | Record line | G6a | NOT PERFORMED |
| C3 | notarytool keychain profile exists locally; no Apple ID password or API key in any file under version control or agent reach | `xcrun notarytool history --keychain-profile <profile>` succeeds; `npm run proof:secret-scan` PASS over the execution record | G6a | NOT PERFORMED |
| C4 | No Apple credential in GitHub Actions: no repository/organization secret named `CSC_LINK`, `CSC_KEY_PASSWORD`, `APPLE_ID`, `APPLE_APP_SPECIFIC_PASSWORD`, `APPLE_TEAM_ID`, or any API-key secret; the active workflow's "Verify unsigned build posture" step continues to assert absence | `gh secret list` (empty of the above) + workflow reference | G6a; rechecked G8 | NOT PERFORMED |
| C5 | `CSC_IDENTITY_AUTO_DISCOVERY=false` remains in `desktop:pack`/`desktop:dist`; any signing invocation is a separate, explicit, local owner command | `frontend/package.json` scripts (present today) | G5 | present (tree) |
| C6 | Signing host is clean: frozen checkout, no dev server, tool versions recorded | Host record | G6b | NOT PERFORMED |
| C7 | Agents never hold, read, or use signing/notary credentials; every G6b/G-KEY/G7/G8 act is performed by the owner (CHANGE only tags/uploads as authorized) | Execution record attribution | all | NOT PERFORMED |
| C8 | Credential rotation/revocation route known (Apple Developer portal; App Store Connect keys) and recorded without secret values | Custody record | — | NOT PERFORMED |
| C9 | Self-signed preparation identities A/B (DEL-09-05-V3-04) are disposable, created only under the owner's host act, and deleted with cleanup proof | Drill record | G5 | NOT PERFORMED |

## D. Do-not-proceed cross-reference

Any `NO`/blank in sections A–C at the gate that consumes it, or any condition in the runbook's section 2 list, stops the lane and returns to the owner. No agent advances a row from `NOT PERFORMED`.

*End of candidate. No release act was performed in authoring this checklist.*
