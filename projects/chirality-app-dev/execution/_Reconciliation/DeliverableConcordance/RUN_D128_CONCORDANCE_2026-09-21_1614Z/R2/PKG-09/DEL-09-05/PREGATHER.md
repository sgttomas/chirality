# PREGATHER — DEL-09-05 CI Artifact and Release Verification Workflow

Read-only evidence map (TASK, Type 2) under `R2/PKG-09/BRIEFS/PREGATHER_BRIEF.md`. Basis: frozen tree
`00115c719`. No dispositions, no alignment judgments. Remarks are factual pointers only.

**Path legend (repo-relative):** `fe/` = `projects/chirality-app-dev/frontend/`;
`del/` = `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-05_CI_Artifact_and_Release_Verification_Workflow/`;
`runs/` = `projects/chirality-app-dev/execution/_Coordination/AgentRuns/`;
`wf/` = `projects/chirality-app-dev/.github/workflows/` (in-root; allowed).
Repository-root `.github/workflows/**` is **not read** and appears only as `OUT_OF_ROOT:`.

**TOUCHED:** `TOUCHED_PATHS.csv` lists no path under `projects/chirality-app-dev/**`; none of the candidate
App paths below is TOUCHED. (Its Runtime rows are `packages/{client,contracts,core,daemon}/src/**` and
`tests/**`, none of which is a candidate for this deliverable.)

## Overview

### Deliverable key files (bytes)

| File | Bytes |
|---|---:|
| `del/ScopeOfWork.md` | 44174 |
| `del/_SEMANTIC.md` | 47454 |
| `del/Release_Runbook_CANDIDATE_2026-09-03.md` | 37377 |
| `del/_SEMANTIC_LENSING.md` | 32633 |
| `del/_STATUS.md` | 16434 |
| `del/Dependencies.csv` | 10036 |
| `del/_DEPENDENCIES.md` | 9689 |
| `del/Exact_Candidate_Identity_and_Custody_Checklist_CANDIDATE.md` | 8897 |
| `del/Assessment_INSP-03_DEL-09-05.md` | 7916 |
| `del/MEMORY.md` | 5741 |
| `del/_REFERENCES.md` | 2744 |
| `del/_CONTEXT.md` | 2464 |
| `del/Evidence/VERSION_IDENTITY_3.0.0-rc.1/` (11 files) | — |
| `del/Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/` (sbom/, run1/, run2/, RUN_RECORD, MANIFEST) | — |
| `del/_run_records/` (15 files; incl. `R6_DAPP97_UNSIGNED_ARTIFACT_WORKFLOW_2026-08-19.md`, `R5_DAPP56_P05_WORKFLOW_NEUTRALIZATION_2026-07-12.md`, `TASK_RUN_2026-09-03_NODE_B.md`, `TASK_RUN_2026-07-12_DAPP56_R5_P45.md`) | — |

### Decision IDs cited most (grep over `del/*.md`, `del/*.csv`)

D-APP-56 (22), D-APP-97 (13), D-APP-38 (12), D-APP-55 (3), D-APP-127 (3), D-GOV-43 (2), D-APP-98 (2),
D-APP-19 (2), D-APP-54 (1), D-APP-36 (1). `D-APP-127_APPLICATION_MAP.csv`: this deliverable's `_STATUS.md`
is a `YES` carrier; its `ScopeOfWork.md` is `NO`/`ABSENT` (SoW still carries pre-D-GOV-43 wording).

### Main code areas

- Build/packaging scripts (not in REACHABILITY; invoker recorded instead): `fe/package.json` scripts
  (lines 17–46) and `build` config (fuses 102, afterPack 109, `mac.sign` 154, hardenedRuntime 157,
  minimumSystemVersion 158, arm64 dmg target 162); `fe/scripts/*.mjs`.
- In-root CI: `wf/harness-premerge.yml` (70 lines; only commit touching it in frozen history: `7bee9ae41`
  "Initial migrated Chirality repository").
- Electron main (LIVE): `fe/electron/main.ts`, `fe/electron/codex-executable.ts`, `fe/electron/app-update*.ts`.
- Script tests: `fe/src/__tests__/scripts/*.test.ts`, `fe/src/__tests__/contract-pins.manifest.ts` + `contract-pins.test.ts`.

### Script invoker map (build/packaging scripts; REACH not applicable)

| Script | Invoked by | Off-by-default / notes |
|---|---|---|
| `fe/scripts/validate-harness-premerge.mjs` (282 l.) | `harness:validate:premerge` (pkg.json:21); `wf/harness-premerge.yml:51-53`; imported by `validate-release-quality-evidence.mjs:8` | writes `artifacts/harness/section8/latest` (lines 134-149) |
| `fe/scripts/validate-release-quality-evidence.mjs` (529 l.) | `validate:release-quality` (pkg.json:29) | `--skip-premerge <reason>` / `RELEASE_QUALITY_SKIP_PREMERGE_REASON` (lines 90, 120-135); summary `artifacts/harness/release-quality/latest/summary.json` (25-30, 87); reads section8/section9 summaries (31-46) |
| `fe/scripts/verify-instruction-root-integrity.mjs` (825 l.) | `instruction-root:integrity` (pkg.json:30); tail of `desktop:pack` (42) and `desktop:dist` (43) | default output `artifacts/harness/instruction-root-integrity/latest` (97, 683); `--runtime-profile` default `codex-only` (76, 672); SDK-unpacked (`app.asar.unpacked/.../claude-agent-sdk`) check only under `legacy-claude` (475-500, 693-705) |
| `fe/scripts/prepare-packaged-instruction-root.mjs` | `instruction-root:prepare` (pkg.json:31) → `desktop:prepare` | — |
| `fe/scripts/pack-electron.mjs` (219 l.) | `desktop:prepare`, `desktop:pack` (42), `desktop:dist` (43, `--target dmg`) | unsigned unless `CHIRALITY_SIGNING_IDENTITY_SHA1` set (23, 81-94: `CSC_IDENTITY_AUTO_DISCOVERY=false`); output `dist/mac-arm64/Chirality.app` (61); `--arm64` (72) |
| `fe/scripts/sign-electron-runtime-v2.mjs` (98 l.) | `package.json` `build.mac.sign` (154) via electron-builder | Developer ID signing + `codesign --verify --deep --strict` (65-86); only effective when an identity is supplied (pack-electron.mjs:16-18) |
| `fe/scripts/finalize-electron-resources.mjs` | `build.afterPack` (109) | resources inventory (90-149) |
| `fe/scripts/verify-packaged-dependency-boundary.mjs` (341 l.) | `desktop:verify-dependencies` (39) in `desktop:pack`/`desktop:dist` | Codex tree regular/executable/non-symlink check `verifyPackagedCodexTree` (94-119); runtimeProfile `app-owned-codex` (318) |
| `fe/scripts/verify-codex-pin.mjs` (202 l.) | `desktop:verify-codex-pin` (40); `desktop:dist` passes `--after-signing` unconditionally (43) | `verifyCodexPin` (99-); `--after-signing` (185) |
| `fe/scripts/scan-secret-evidence.mjs` (467 l.) | `proof:secret-scan` (32) only | not chained from `desktop:dist`, `validate:release-quality`, or `wf/harness-premerge.yml`; patterns are Anthropic-key-specific (50, 183-184, 345-356) |
| `fe/scripts/run-network-policy-proof.mjs` (826 l.) | `proof:network-policy` (33) only | allowlist DNS host `api.anthropic.com` only (20, 158-178, 233-245); not chained from packaging/CI |
| `fe/scripts/run-packaged-security-proof.mjs` (1512 l.) | `proof:packaged-security` (34) only | not chained from packaging/in-root CI |
| `fe/scripts/generate-sbom.mjs` (411 l.) | `sbom:generate` (44) | `SYFT_PIN` (41); refuses absent/mismatched Syft (54-101) |
| `fe/scripts/generate-third-party-notices.mjs` (657 l.) | `notices:generate` (45) | — |
| `fe/scripts/verify-version-identity.mjs` (647 l.) | `verify:version-identity` (46) | staged patch builder 320-406; `verifyVersionIdentity` 528 |
| `fe/scripts/verify-packaged-agent-sdk-runtime.mjs`, `run-live-packaged-agent-sdk-read-tool-proof.mjs`, `run-packaged-pi-runtime-proof.mjs` | `harness:validate:agentsdk-packaged-proof`, `...-live-read-tool`, `harness:validate:pi-packaged-proof` | reference `@anthropic-ai/claude-agent-sdk-*` (read-tool-proof:13-17); not chained from `desktop:dist` |

### Recorded proof artefacts (separate from code)

| Artefact | Content pointer |
|---|---|
| `runs/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md` | consolidated build 2026-09-12 at `388de6973`: `desktop:dist` exit 0, `Chirality-3.0.0-rc.1-arm64.dmg` sha256 `efaac5d7…`, Developer ID signed (TeamID 8A7JL35U4S), `desktop:verify-dependencies` PASS, `verify-codex-pin --after-signing` PASS, `instruction-root:integrity` pass (366 files), `codesign --verify` valid, `spctl` rejected `Unnotarized Developer ID`, `verify:version-identity --expect 3.0.0-rc.1` PASS; notarize/staple, S-6/S-8, publishing "not done" (lines 20-75) |
| `runs/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md` | build → sign → notarize → verify signature + Codex pin → S-6/S-8 packaged checks; record section (lines 1-80) |
| `runs/APP_V3_CODEX_HOST_REPLATFORM_20260912/{NATIVE_CHECKLIST,INDEPENDENT_REVIEW}.md` | owner native checklist; independent source review |
| `runs/APPDEV_UNSIGNED_RELEASE_WORKFLOW_2026-08-19/` (CI_ATTEMPT_01, MANAGER_VALIDATION, REVIEW_RETURN_0x …) | D-APP-97 C1 unsigned CI-artifact workflow; `_STATUS.md` History records PR #583, run `32327128935`, job `96300526868` |
| `runs/CODEX_MVP_PACKAGING_20260910/` | WORKING_RECORD (signing fingerprint), SUPERSESSION_NOTE_2026-09-12 |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/Evidence_ADQ-14_Release_Quality_Validation_Wrapper.md` | ADQ-14 wrapper evidence (named in CLM-014); siblings `Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`, `Evidence_ADQ-16_Secret_Network_Proof.md` |
| `del/Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/` | notices run1/run2 + sha; `sbom/dry-run.closure.json`, `which-syft.txt`, attempt exit/stdout/stderr (SBOM `UNAVAILABLE_UNDER_BOUNDS`) |
| `del/Evidence/VERSION_IDENTITY_3.0.0-rc.1/` | dry-run reports expect 2.0.0 / 3.0.0-rc.1, `staged_version_patch.diff` (+sha256), `git_apply_check.txt` |
| `del/Release_Runbook_CANDIDATE_2026-09-03.md`, `del/Exact_Candidate_Identity_and_Custody_Checklist_CANDIDATE.md` | "CANDIDATE — NOT ADOPTED" headers (line 1); runbook §3.A–3.K signing/notarization/Gatekeeper/prerelease/backcheck, §4 rollback, §5 custody; checklist §A–D |
| `del/Assessment_INSP-03_DEL-09-05.md` | REQ001–REQ015 conformance matrix (lines 15-34) against the pre-v3 tree |
| Git history of `fe/package.json` version line | `447f49cff` 2.0.0 → `2f825f180` 3.0.0-rc.1 → `9eaddb596` 3.0.0 → `cf4653526` 3.0.1 (frozen value `"version": "3.0.1"`, pkg.json:3) |

---

## Part P1 — SEC-1, CLM-001..CLM-016, CLM-034 (Ontology + Epistemology)

### SEC-1 — Current Codex MVP conformity (SoW:12-16)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| SEC-1 | Current Codex MVP conformity (version identity vs Info.plist/DMG name; staged+mounted Codex layout; K-NET-1; key custody) | `fe/scripts/verify-version-identity.mjs:79-124,528` (script); `fe/scripts/verify-codex-pin.mjs:99-` (script); `fe/scripts/verify-packaged-dependency-boundary.mjs:94-119` (script); `fe/electron/codex-executable.ts:66-80` `resolvePackagedCodexVendorRoot`/`resolveCodexExecutable` (LIVE; called `fe/electron/main.ts:34,816`); `fe/src/lib/consent/hosted-engine-consent-port.ts` (LIVE); `fe/src/components/settings/account-consent-settings.tsx` (LIVE); `fe/src/lib/consent/fake-hosted-engine-consent-port.ts` (TEST_ONLY) | `fe/src/__tests__/scripts/verify-version-identity.test.ts` (14), `verify-codex-pin.test.ts` (4), `verify-packaged-dependency-boundary.test.ts`, `dmg-packaging-policy.test.ts:113` (Codex tree + runtime bundles), `fe/src/__tests__/components/account-consent-settings.test.ts`, `fe/src/__tests__/lib/consent/fake-hosted-engine-consent-port.test.ts` | "Existing CI qualification stop" — `desktop-release-workflow.test.ts:152-200` pins an S0 hold step in `OUT_OF_ROOT:.github/workflows/desktop-release-template.yml`. Mounted-DMG inspection is performed only in that out-of-root workflow (test lines 185-198 reference `hdiutil attach`). Proof: BUILD_EVIDENCE_20260912.md step 4. HINTS K-NET-1 hits are consent UI/port, not packaging. |

### Ontology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-001 | Datasheet header (PRD MATCH note) | DOC_ONLY | — | REFERENCE_HASHES.csv: DEL-09-05 PRD/CONTRACT/SPEC recorded `MATCH`, `Match = NO` at frozen basis (pack manifest note). HINTS "MATCH" hits in `verify-version-identity.mjs` are unrelated tokens. |
| CLM-002 | Identification (ResponsibleParty TBD, Type CI_CD_CHANGE) | DOC_ONLY | — | HINTS hits (`scaffold.ts:615` ResponsibleParty, deliverable-contract tests) are generic scaffold fields, not this deliverable. |
| CLM-003 | Attributes (local command sequence; stable summary path; expected outputs; CI baseline; release target) | `fe/package.json:17,18,21,29,30,43` scripts; `build.mac` 154-162 (`minimumSystemVersion` 15.0.0, dmg arm64); `wf/harness-premerge.yml` (steps 16-70) | `dmg-packaging-policy.test.ts:60` (macOS min + arm64 dmg), `:83` (instruction-root resources); `contract-pins.manifest.ts:70-116` (pins `OUT_OF_ROOT:.github/workflows/harness-premerge.yml`) | `desktop:dist` output name from electron-builder; frozen version 3.0.1 → `Chirality-3.0.1-arm64.dmg` expected name (not observed in tree). `build.mac.sign` + `hardenedRuntime: true` (154,157) present vs "unsigned/unnotarized" target wording. |
| CLM-004 | Conditions (CI provider assumption; stable path; upload name TBD; K-KEY-1/K-NET-1; deps TBD) | `wf/harness-premerge.yml:58-64` upload name `harness-section8-summary`; `wf/harness-premerge.yml:13` `ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}` | `contract-pins.manifest.ts:113-114` pins `notContains 'secrets.ANTHROPIC_API_KEY'` for the out-of-root workflow | In-root workflow carries the provider secret env the out-of-root pin forbids; `_STATUS`/CLM-007 call the project-local workflow "non-executing". `Dependencies.csv` present in `del/`. |
| CLM-005 | Construction (CI workflow; local sequence; stable artifact; manual checklist; evidence capture) | `wf/harness-premerge.yml`; `fe/scripts/validate-release-quality-evidence.mjs`; `fe/scripts/verify-instruction-root-integrity.mjs:683`; `fe/scripts/verify-codex-pin.mjs`; `fe/scripts/sign-electron-runtime-v2.mjs:65-86` | `validate-harness-premerge.test.ts` (5), `verify-instruction-root-integrity.test.ts` (8), `sign-electron-runtime-v2.test.ts` (5) | "SDK-backed packaged turn startup / SDK transcript storage" items: SDK-unpacked check only under `--runtime-profile legacy-claude` (verify-instruction-root-integrity.mjs:698); transcript mirroring grep → NO_CANDIDATE in App (terms: `transcript.?(mirror|storage)`, `mirrorTranscript`, `persistSession`; only hit `projects/chirality-runtime/packages/engine-pi-omlx/src/pi-turn-runtime.ts`). Manual checklist artefact: `runs/APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md`. |
| CLM-006 | References table | DOC_ONLY | — | See REFERENCE_HASHES.csv for recompute. |
| CLM-007 | D-APP-56 R5 P45 reconciliation (repo-root workflow executed; project-local non-executing) | `wf/harness-premerge.yml` (project-local); executed workflow `OUT_OF_ROOT:.github/workflows/harness-premerge.yml` | `contract-pins.manifest.ts:70-116` pins `run: npm run validate:release-quality`, section8/release-quality/instruction-root summary paths, `prepare-packaged-instruction-root.mjs`, `instruction-root:integrity --` in the out-of-root file; `contract-pins.test.ts` | `harness-validation-summaries` name: no in-root hit (grep `harness-validation-summaries` over `fe/scripts`, `fe/src`, `fe/electron`, `wf/`) — only in out-of-root file per SoW text. |
| CLM-034 | Applied decomposition v3 row (WP-09 author/review; WP-11 after G6a; arm64 only) | DOC_ONLY for phase boundary; product surfaces: `fe/package.json:162` (arm64 only), `fe/scripts/pack-electron.mjs:81-94` (identity-gated signing) | `pack-electron.test.ts:65` (never discovers keychain identity), `:86` (Developer ID only via explicit SHA-1) | `_STATUS.md` records D-APP-127 retiring G6a/G6b/G-KEY/G7/G8 (V3-05 text). BUILD_EVIDENCE_20260912 records Developer ID signing performed 2026-09-12 by implementing session. Version history reached 3.0.0/3.0.1 (`9eaddb596`, `cf4653526`); no WP-11/V3-05 execution record in `del/`. |

### Epistemology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-008 | Specification header | DOC_ONLY | — | — |
| CLM-009 | Scope (in/out) | DOC_ONLY | — | Out-of-scope items owned by DEL-09-06 (security) and DEL-09-01/02 (Section 8/9). |
| CLM-010 | Requirements REQ-09-05-001..015 | see per-REQ rows below | see below | — |
| CLM-010 / REQ-001 | local sequence test/typecheck/premerge/instruction-root; release-quality wrapper w/ skip | `fe/package.json:17,18,21,30,29`; `validate-release-quality-evidence.mjs:90,120-135` (skip), `:8` imports premerge `run` | `contract-pins.manifest.ts:118-135` (wrapper runs `test -- --testTimeout=15000` and `typecheck`); `validate-harness-premerge.test.ts:50-150` | No dedicated test file for `validate-release-quality-evidence.mjs` (only contract pins). |
| CLM-010 / REQ-002 | packaging includes `desktop:dist` | `fe/package.json:43` → `pack-electron.mjs --target dmg` + verify-dependencies + verify-codex-pin `--after-signing` + instruction-root:integrity | `pack-electron.test.ts` (5), `dmg-packaging-policy.test.ts` (5) | `--after-signing` passed even for unsigned builds. |
| CLM-010 / REQ-003 | outputs DMG, `.app`, instruction-root summary | `pack-electron.mjs:61` (`mac-arm64/Chirality.app`); `verify-instruction-root-integrity.mjs:97,683` | `verify-instruction-root-integrity.test.ts:130` | No `fe/dist` or `fe/artifacts` in frozen tree (not listed at `fe/`). Proof: BUILD_EVIDENCE_20260912 (DMG outside repo `~/.claude/chirality-build-a2-out/`). |
| CLM-010 / REQ-004 | 10 PRD §12.7 CI steps | `wf/harness-premerge.yml`: checkout 16, Node 20 19-24, `npm ci` 26-28, preflight 30-31, start server 33-37, poll 39-49, premerge 51-53, verify summary 55-56, upload 58-64 | `contract-pins.manifest.ts:70-116` (out-of-root file) | No "verify instruction-root assets" step in `wf/harness-premerge.yml`; out-of-root pins include `prepare-packaged-instruction-root.mjs` + `instruction-root:integrity --`. |
| CLM-010 / REQ-005 | section8 summary uploaded; instruction-root summary separate; release-quality derivative | `validate-harness-premerge.mjs:134-149`; `validate-release-quality-evidence.mjs:25-46,313-360`; `wf/harness-premerge.yml:55-64` (section8 only) | `validate-harness-premerge.test.ts:95` (publishes exact Section 8 summary); `contract-pins.manifest.ts:108-112` | — |
| CLM-010 / REQ-006 | manual DMG checks (arm64, LSMinimumSystemVersion, signing posture, instruction-root assets, working-root selector, Codex network safeguards, SDK startup, SDK outside asar, transcript) | arm64/min: `fe/package.json:158-162`; signing: `sign-electron-runtime-v2.mjs`, `pack-electron.mjs:81-94`; working-root selector: `fe/electron/main.ts:491-520` `createDirectorySelectionHandler`, registered `:552-553` (LIVE); Codex executable outside asar: `fe/electron/codex-executable.ts:66-80` (LIVE) + `build.extraResources` codex → `Resources/codex`; `verify-packaged-dependency-boundary.mjs:94-119` | `dmg-packaging-policy.test.ts:60,83,113,136`; `sign-electron-runtime-v2.test.ts:23-77`; `verify-packaged-dependency-boundary.test.ts` | `verify-version-identity.mjs:92` `readPlistStrings` reads Info.plist keys. SDK transcript: NO_CANDIDATE (terms above). Owner native checklist: `runs/APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md`. |
| CLM-010 / REQ-007 | macOS 15+ arm64 unsigned/unnotarized target | `fe/package.json:154-162`; `pack-electron.mjs:81-94` | `dmg-packaging-policy.test.ts:60`; `pack-electron.test.ts:65,86`; `desktop-release-workflow.test.ts:66,80` (reads `OUT_OF_ROOT:.github/workflows/desktop-release-template.yml`) | Signing hook + hardened runtime + fuses configured (102-108, 154-157); Developer ID signing exercised in BUILD_EVIDENCE_20260912. |
| CLM-010 / REQ-008 | release-significant changes pass local checks | `validate:release-quality` (pkg.json:29) | — | No in-root gate enforcing the full set; enforcement is in `OUT_OF_ROOT:.github/workflows/harness-premerge.yml` per pins. |
| CLM-010 / REQ-009 | no secrets in records | `fe/scripts/scan-secret-evidence.mjs:50,180-209,300-383` (`proof:secret-scan`) | `run-live-packaged-agent-sdk-read-tool-proof.test.ts` (key-absence asserts, per Assessment REQ009) | Secret scan patterns are Anthropic-specific; not chained from CI/packaging. `wf/harness-premerge.yml:13` injects `ANTHROPIC_API_KEY`. |
| CLM-010 / REQ-010 | network scope = K-NET-1 | `fe/scripts/run-network-policy-proof.mjs:20,158-178,233-245` | `run-network-policy-proof.test.ts` | Proof allowlist is `api.anthropic.com` only; no Codex/OpenAI host in allowlist (grep `openai|chatgpt` → none). `fe/electron/app-update-source.ts:9-11` (LIVE) contacts `api.github.com`. |
| CLM-010 / REQ-011 | no professional-approval claims | DOC_ONLY | — | Runbook/checklist line 1 "CANDIDATE — NOT ADOPTED … performs no release act". |
| CLM-010 / REQ-012 | GitHub Actions assumption; path TBD | `wf/harness-premerge.yml` | — | Paths resolved in CLM-007/CLM-016 text (repo-root file, OUT_OF_ROOT). |
| CLM-010 / REQ-013 | requirement-to-evidence map | DOC_ONLY | — | `del/Assessment_INSP-03_DEL-09-05.md:15-34` matrix (pre-v3). |
| CLM-010 / REQ-014 | ten-step CI review table | DOC_ONLY | — | Assessment REQ014 row: "No standalone CI review artifact". |
| CLM-010 / REQ-015 | secret + network inspection of CI/release artefacts | `scan-secret-evidence.mjs`; `run-network-policy-proof.mjs` | as REQ-009/010 | Evidence: `Evidence_ADQ-16_Secret_Network_Proof.md` (PKG-09 1_Working). |
| CLM-011 | Standards | DOC_ONLY | — | — |
| CLM-012 | Verification approach per REQ | as CLM-010 rows | as CLM-010 rows | — |
| CLM-013 | Evidence matrix | DOC_ONLY; artefacts listed in Overview | — | REQ-010 row still says "loopback plus Anthropic API path". |
| CLM-014 | Documentation (outputs; ADQ-14 evidence) | `wf/harness-premerge.yml`; `validate-release-quality-evidence.mjs` | — | ADQ-14 file present at PKG-09 `1_Working/Evidence_ADQ-14_Release_Quality_Validation_Wrapper.md`. |
| CLM-015 | D-APP-56 R5 P45 reconciliation (dup of CLM-007) | as CLM-007 | as CLM-007 | — |
| CLM-016 | CI ownership amendment + REQ-001..004, AC-001..002 | owner file `OUT_OF_ROOT:.github/workflows/harness-premerge.yml` | `contract-pins.manifest.ts:70-116`; `contract-pins.test.ts` | Sub-items below. |
| CLM-016 / REQ-001 | CI premerge + stable artifacts; release-ops carrier | as CLM-007/REQ-005 | as CLM-007 | — |
| CLM-016 / REQ-002 | WP-09 runbook authoring (signing order, fuses/entitlements, notarization, rollback, version identity, custody, prerelease, backcheck) | product counterparts: `fe/package.json:102-108` fuses, `fe/build/entitlements.mac{,.inherit,.code-mode-host}.plist`, `sign-electron-runtime-v2.mjs:30-45` (entitlements, JIT only on code-mode host), `verify-version-identity.mjs`; `fe/electron/app-update-source.ts:9-18` GitHub releases feed (LIVE) | `sign-electron-runtime-v2.test.ts:23`; `verify-version-identity.test.ts`; `desktop-release-workflow.test.ts:203` (no `softprops/action-gh-release`) | Runbook: `del/Release_Runbook_CANDIDATE_2026-09-03.md` §3.C (fuses), 3.D (nested order), 3.F-3.G, 3.J-3.K, §4, §5. `_STATUS` History (node B): three review rounds `instances/B2_REVIEWER/REVIEW_0{1,2,3}_*.md` under `runs/APPDEV_V3_NODE_B_2026-09-03/`. |
| CLM-016 / REQ-003 | WP-11 only after G6a | DOC_ONLY | — | `_STATUS` V3-05: G6a retired under D-APP-127; signing recorded in BUILD_EVIDENCE_20260912 (implementing session, owner identity). |
| CLM-016 / REQ-004 | arm64 only for rc.1 | `fe/package.json:160-164` target dmg arch arm64 | `dmg-packaging-policy.test.ts:60` | — |
| CLM-016 / AC-001 | every REQ mapped; 10 CI steps; manual items; secret/network/target/boundary | DOC_ONLY | — | See REQ-013/014 rows. |
| CLM-016 / AC-002 | v3 outputs exist (CI evidence, runbook candidate, custody checklist, WP-11 record) | candidates: `del/Release_Runbook_CANDIDATE_2026-09-03.md`, `del/Exact_Candidate_Identity_and_Custody_Checklist_CANDIDATE.md`; WP-11 record: none in `del/` | — | `_STATUS` V3-05 Remaining (execution record not recorded). |

---

## Part P2 — CLM-017..CLM-033, REM-1..REM-3 (Praxeology, Axiology, Remaining)

### Praxeology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-017 | Procedure header | DOC_ONLY | — | HINTS row empty. |
| CLM-018 | Purpose | DOC_ONLY | — | — |
| CLM-019 | Prerequisites (ResponsibleParty, deps, CI path, upload name, runbook name, key/network) | `wf/harness-premerge.yml:58-64` (upload name `harness-section8-summary`, no `retention-days`) | — | Retention not set in in-root workflow (no `retention-days` key). |
| CLM-020 | Steps 1-8 (source/scope; local sequence; CI sequence; artifact handling; packaging; manual DMG; records; escalation) | Step 2: pkg.json:29,30,43; Step 3: `wf/harness-premerge.yml:16-64`; Step 4: `validate-harness-premerge.mjs:134-149`; Step 5: `pack-electron.mjs:61`, `verify-instruction-root-integrity.mjs:683`; Step 6: `fe/package.json:158-162`, `fe/electron/main.ts:491-553` (LIVE), `fe/electron/codex-executable.ts:66-80` (LIVE), `verify-packaged-dependency-boundary.mjs:94-119`; Step 7: `scan-secret-evidence.mjs`, `run-network-policy-proof.mjs` | `validate-harness-premerge.test.ts`, `pack-electron.test.ts`, `dmg-packaging-policy.test.ts`, `verify-instruction-root-integrity.test.ts`, `verify-packaged-dependency-boundary.test.ts` | Step 6 "SDK-backed harness turn after R1" / "SDK transcript storage": only `legacy-claude` profile path (verify-instruction-root-integrity.mjs:698) and agentsdk proof scripts (pkg.json `harness:validate:agentsdk-*`); transcript NO_CANDIDATE (terms in CLM-005). Current procedure: `runs/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md:18-60`. |
| CLM-021 | Verification table | as CLM-020 | as CLM-020 | — |
| CLM-022 | Records required | proof artefacts in Overview | — | No in-root CI log/upload records (CI artefacts live in GitHub). |
| CLM-023 | D-APP-56 R5 P45 reconciliation + VER-001/VER-002 | as CLM-007 | `contract-pins.manifest.ts:70-116` | — |
| CLM-023 / VER-001 | inspect local sequence, executed CI (10 steps), summaries, outputs, manual checklist, matrix, secret/network, target, boundary, blockers | as CLM-010 rows | as CLM-010 rows | Executed CI workflow is `OUT_OF_ROOT:.github/workflows/harness-premerge.yml`. |
| CLM-023 / VER-002 | inspect runbook candidate + custody checklist; independent review; no WP-11 act before G6a | DOC_ONLY; `del/Release_Runbook_CANDIDATE_2026-09-03.md`, `del/Exact_Candidate_Identity_and_Custody_Checklist_CANDIDATE.md` | — | Reviews: `runs/APPDEV_V3_NODE_B_2026-09-03/instances/B2_REVIEWER/REVIEW_0{1,2,3}_*.md` (per `_STATUS`). Signing act recorded 2026-09-12 in BUILD_EVIDENCE_20260912 (step 2, identity via `CHIRALITY_SIGNING_IDENTITY_SHA1`). |

### Axiology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-024 | Guidance header | DOC_ONLY | — | — |
| CLM-025 | Purpose | DOC_ONLY | — | — |
| CLM-026 | Principles (baseline commands; stable path = instruction-root summary; CI ≠ approval; unsigned target; security visible; prefer TBD) | pkg.json:17,18,21,30,43; `verify-instruction-root-integrity.mjs:683` | `verify-instruction-root-integrity.test.ts` | "Stable summary path" here names instruction-root summary; in-root CI uploads section8 summary (`wf/harness-premerge.yml:55-64`). |
| CLM-027 | Considerations (CI location; stable path; manual per-item; secrets; network loopback+Anthropic; boundary; target) | `run-network-policy-proof.mjs:20` (Anthropic allowlist); `scan-secret-evidence.mjs:50` | `run-network-policy-proof.test.ts` | Network row wording "loopback plus Anthropic API path" vs SEC-1 Codex supplier wording. |
| CLM-028 | Term normalization | DOC_ONLY | — | CI upload artifact name observed in-root: `harness-section8-summary` (`wf/harness-premerge.yml:62`); SoW CLM-007 names `harness-validation-summaries` (out-of-root). |
| CLM-029 | Trade-offs | DOC_ONLY | — | — |
| CLM-030 | Examples (5-command block; 6-row CI checklist) | pkg.json:17,18,21,30,43 | — | Example "Stable summary artifact" row names instruction-root path; in-root workflow verifies section8 path (line 56). |
| CLM-031 | Conflict table (PRD hash) | DOC_ONLY | — | REFERENCE_HASHES.csv: PRD recorded MATCH, recompute `Match = NO` (`HASH-RECOMPUTE@00115c719`). |
| CLM-032 | Open items (CI path, upload name/retention, runbook name, owner, immutable snapshots) | `wf/harness-premerge.yml:58-64` | — | See CLM-019/CLM-028 remarks. |
| CLM-033 | D-APP-56 R5 P45 reconciliation (dup) | as CLM-007 | as CLM-007 | — |

### Remaining (`del/_STATUS.md`)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| REM-1 | DEL-09-05-V3-02 SBOM (optional; NOT_SELECTABLE_UNTIL Syft v1.18.1 observable) | `fe/scripts/generate-sbom.mjs:41` `SYFT_PIN`, `:54-101` pin checks, `:273-348` plan/run; `fe/scripts/generate-third-party-notices.mjs`; invokers `sbom:generate`/`notices:generate` (pkg.json:44-45) | `fe/src/__tests__/scripts/generate-sbom.test.ts` (11), `generate-third-party-notices.test.ts` | Evidence: `del/Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/sbom/{dry-run.closure.json,which-syft.txt,attempt.closure.*}`; notices run1/run2. Not wired into in-root workflow. |
| REM-2 | DEL-09-05-V3-05 release operation record (short packaging procedure; D-APP-127) | `fe/package.json:43` `desktop:dist`; `pack-electron.mjs:81-94`; `sign-electron-runtime-v2.mjs:65-98`; `verify-codex-pin.mjs:99-,185` (`--after-signing`) | `pack-electron.test.ts`, `sign-electron-runtime-v2.test.ts`, `verify-codex-pin.test.ts` | Procedure: `runs/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md`; build record `BUILD_EVIDENCE_20260912.md` (signed, unnotarized, S-6/S-8 not performed, "Publishing: not authorized"). No deliverable-local execution record in `del/`. `fe/package.json` version later moved to 3.0.0 (`9eaddb596`) and 3.0.1 (`cf4653526` "Prepare Chirality v3.0.1 maintenance release"). |
| REM-3 | DEL-09-05-V3-06 apply 3.0.0-rc.1 version-identity patch (product stays 2.0.0 until consolidated build) | `fe/scripts/verify-version-identity.mjs:320-406` (staged patch), `:528` (verify); `fe/package.json:3` | `verify-version-identity.test.ts` (14) | Staged patch: `del/Evidence/VERSION_IDENTITY_3.0.0-rc.1/staged_version_patch.diff` (+`.sha256`, `git_apply_check.txt`). Frozen `fe/package.json:3` = `3.0.1`; history: `2f825f180` set `3.0.0-rc.1` ("Connect Codex MVP chat, account bootstrap and packaged Runtime"). BUILD_EVIDENCE_20260912: `verify:version-identity --expect 3.0.0-rc.1` PASS (12 surfaces, 2 absent). |

## NO_CANDIDATE summary

- SDK transcript storage/mirroring (CLM-005, CLM-010/REQ-006, CLM-020 step 6): terms `transcript.?(mirror|storage)`,
  `mirrorTranscript`, `persistSession` over `fe/src`, `fe/electron`, Runtime `packages`/`tests` — no App candidate.
- `harness-validation-summaries` artifact name (CLM-007/015/016/023/033): no in-root hit (only `OUT_OF_ROOT:.github/workflows/harness-premerge.yml`).
- Deliverable-local WP-11/V3-05 execution record (CLM-016/AC-002, REM-2): none under `del/`.
