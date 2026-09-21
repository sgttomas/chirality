# PREGATHER — DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

Read-only evidence map (TASK, Type 2) for run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-09 R2.
Basis: frozen tree at `00115c719` (HEAD `00115c71931bcae79909602d653740d3bb72dfa1`, 2026-09-21).
This map gives pointers only. It records no dispositions and no alignment verdicts. Paths are repo-relative.
Abbreviations: `FE` = `projects/chirality-app-dev/frontend`, `DEL` = `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`, `RT` = `projects/chirality-runtime`.

## 0. Orientation

### 0.1 Deliverable key files (frozen bytes)

| File | Size (B) | Note |
|---|---|---|
| `DEL/ScopeOfWork.md` | 27,560 | 1 SEC + CLM-001..025; decomposition basis `d6f6cadb2` |
| `DEL/_STATUS.md` | 43,325 | State `IN_PROGRESS`, Last Updated 2026-09-12; Remaining items REM-1 (L105) and REM-2 (L114); D-GOV-43 history entry 2026-09-12 |
| `DEL/_SEMANTIC.md` / `_SEMANTIC_LENSING.md` | 48,965 / 34,064 | derived matrices |
| `DEL/MEMORY.md` | 13,611 | |
| `DEL/Assessment_INSP-03_DEL-09-04.md` | 6,285 | |
| `DEL/Dependencies.csv` / `_DEPENDENCIES.md` | 5,724 / 4,684 | |
| `DEL/_CONTEXT.md` / `_REFERENCES.md` | 2,593 / 2,749 | |
| `DEL/Evidence/` | — | `Packaged_Security_Proof_2026-08-20/DEPENDENT_EVIDENCE.md` (points at DEL-09-06 Evidence), `R20_Owner_Login_Proof_PASS_2026-08-23/{evidence-package,prepared,summary}.json` (LaunchAgent login proof) |
| `DEL/_run_records/` | 38 files | most recent: `D_APP_124_*_2026-09-06.md`; R1..R21 LaunchAgent/daemon-era records 2026-07-20..08-23; none dated after 2026-09-06 |

### 0.2 Decisions cited most (from `EVIDENCE_PACK/DECISION_HITS.csv`, DEL-09-04 rows = 170)

D-APP-88 (25), D-APP-56 (15), D-APP-93 (15), D-APP-97 (14), D-APP-38 (12), D-APP-100 (11), D-APP-71 (8), D-APP-55 (7), D-APP-89 (7), D-APP-124 (6), D-GOV-43 (5, ROOT), D-APP-108 (4), D-APP-127 (4), D-APP-70 (4).
In `ScopeOfWork.md` only: D-APP-38 (8), D-APP-56 (4), D-APP-18 (2), D-APP-80 (1).
`D-APP-127_APPLICATION_MAP.csv`: `_STATUS.md` = YES (`_STATUS.md:92`). `ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md` and `Dependencies.csv` = NO/NONE_FOUND.

### 0.3 Main code areas and packaging chain

- **Packaging entry (`FE/package.json`):**
  - `desktop:dist` (L43) = `pack-electron.mjs --target dmg` → `desktop:verify-dependencies` → `desktop:verify-codex-pin -- --after-signing` → `instruction-root:integrity`.
  - `desktop:pack` (L42) runs the same chain with `--target dir` and without `--after-signing`.
  - `desktop:prepare` (L41) = `instruction-root:prepare` → `runtime:build` → `build` → `pack-electron.mjs` (dir).
  - **Remark:** `desktop:dist` and `desktop:pack` do not themselves run `instruction-root:prepare`, `runtime:build` or `build`. `pack-electron.mjs:26-34` `REQUIRED_BUILD_INPUTS` fails closed when those outputs are absent.
- **electron-builder config (`FE/package.json` `build`, L100-170):**
  - `asar: true` (L101) and `electronFuses` (L102), including `onlyLoadAppFromAsar` and `enableEmbeddedAsarIntegrityValidation`.
  - `afterPack` = `scripts/finalize-electron-resources.mjs` (L109).
  - `extraResources` (L122) stages:
    - `@openai/codex-darwin-arm64/vendor/aarch64-apple-darwin` → `codex`
    - `dist-runtime/runtime-service` → `runtime-service`
    - `dist-runtime/runtime-cli` → `runtime-cli`
    - `node_modules/.cache/chirality-instruction-root` → `instruction-root`
  - `mac` settings: `icon build/icon.icns` (L153), `sign ./scripts/sign-electron-runtime-v2.mjs` (L154), `hardenedRuntime true` (L157), `minimumSystemVersion "15.0.0"` (L158), `target dmg arm64` (L159).
  - No `win` or `linux` block, and no `nsis` or `AppImage`.
  - `@openai/codex` is pinned at `0.154.0` (L54). `engines.node` is `>=22.19.0` (L95-96).
- **Build/packaging scripts (not covered by REACHABILITY; invoker recorded instead):**
  - `pack-electron.mjs` (219 LOC). Invoked by `desktop:pack`, `desktop:dist` and `desktop:prepare`.
  - `finalize-electron-resources.mjs` (149). Invoked by `build.afterPack`.
  - `sign-electron-runtime-v2.mjs` (98). Invoked by `build.mac.sign`.
  - `prepare-packaged-instruction-root.mjs` (482). Invoked by `instruction-root:prepare`; `verify-instruction-root-integrity.mjs` also imports it.
  - `verify-instruction-root-integrity.mjs` (825). Invoked by `instruction-root:integrity`.
  - `verify-codex-pin.mjs` (202). Invoked by `desktop:verify-codex-pin`.
  - `verify-packaged-dependency-boundary.mjs` (341). Invoked by `desktop:verify-dependencies`.
  - `verify-electron-dist.mjs` (144). Invoked by `electron:supply-chain`; `pack-electron.mjs:6` also imports it.
  - `build-electron.mjs` (141). Invoked by `build:electron`, which `build` runs.
  - `verify-version-identity.mjs` (647). Invoked by `verify:version-identity`.
  - `generate-macos-icon.mjs` (106). `NO_INVOKER_FOUND`; its own header (L3-9) states it is one-time and not part of the build graph.
- **Legacy (Claude SDK) packaged proof scripts:**
  - `verify-packaged-agent-sdk-runtime.mjs` (`harness:validate:agentsdk-packaged-proof`) and `run-live-packaged-agent-sdk-read-tool-proof.mjs` (`harness:validate:agentsdk-packaged-live-read-tool`). Both reference `@anthropic-ai/claude-agent-sdk`, 7 hits each.
  - `run-network-policy-proof.mjs` (`proof:network-policy`; allowlist `api.anthropic.com`, L20) and `run-packaged-security-proof.mjs` (`proof:packaged-security`; markers `api.anthropic.com`, L22-30).
  - `run-network-policy-proof.mjs:14-17` writes into the DEL-09-06 deliverable root.
- **Electron main (REACH=LIVE):**
  - `FE/electron/main.ts`. Relevant functions:
    - `resolveInstructionRootForProcess` L408-438
    - `resolveServiceInstructionRoot` L441-445
    - `resolveRuntimeServiceEntry` L457-470
    - REQ-NET-001 renderer egress policy L129-135, L197-330
    - codex resolution L816-820, directory selection L551/L800
    - service config L826-833
  - Also `FE/electron/codex-executable.ts`, `FE/electron/product-instructions.ts` and `FE/electron/runtime-service-host.ts`.
- **Runtime (REACH=LIVE via `RT/packages/daemon/src/standalone-bin.ts`):**
  - `RT/packages/daemon/src/codex-supervisor.ts` (TOUCHED).
  - `sandboxPolicy()` L104-108 sets `networkAccess:false`. It is used at L261; `thread/start` and `thread/resume` pass `envelope.policy.sandbox` at L191/L219.
- **In-root CI:**
  - `projects/chirality-app-dev/.github/workflows/harness-premerge.yml` (71 lines). It runs `npm ci`, `harness:validate:premerge` and a section8 summary check. It has no desktop, DMG or instruction-root step.
  - The DMG workflow that `FE/src/__tests__/scripts/desktop-release-workflow.test.ts:6-11` reads is `OUT_OF_ROOT:.github/workflows/desktop-release-template.yml`.
  - `contract-pins.manifest.ts:71` pins `OUT_OF_ROOT:.github/workflows/harness-premerge.yml` (repository root). That pin includes the `prepare-packaged-instruction-root` and `instruction-root:integrity` steps (L95-105).
- **TOUCHED_PATHS:**
  - No `FE/**` path is touched. `FE/package.json`, `FE/scripts/**` and `FE/electron/**` are all untouched.
  - Touched Runtime files that appear here: `RT/packages/daemon/src/codex-supervisor.ts`, `RT/packages/daemon/src/runtime-daemon.ts`, `RT/packages/daemon/src/app-owned-composition.ts`.
- **Frontend artefact dir:** `FE/artifacts/` is absent from the frozen tree. It is a build output, so `summary.json` is not committed.

### 0.4 Recorded proof artefacts (code-independent)

| ID | Artefact | Content pointer |
|---|---|---|
| PA-1 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md` | A2 build of 3.0.0-rc.1 from source `388de6973` (details below) |
| PA-2 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_RELEASE_20260913.md` | `Chirality-3.0.0-arm64.dmg` (details below) |
| PA-3 | `.../APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_FINAL_UPDATES_20260913.md` | Second 3.0.0 DMG (338,043,892 B); stage `04-instruction-root` exit 0; Developer ID signed; Gatekeeper `Unnotarized Developer ID` |
| PA-4 | `.../APP_V3_USER_JOURNEYS_20260912/{BUILD_EVIDENCE_20260913.md, PUBLIC_RELEASE_20260913.md, returns/*PACKAGING*.md}` | Further 3.0.0 packaging/release records (not read in detail) |
| PA-5 | `.../APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md` (81 lines), `NATIVE_CHECKLIST.md` | Packaging procedure cited by REM-1 |
| PA-6 | `DEL/Evidence/Packaged_Security_Proof_2026-08-20/DEPENDENT_EVIDENCE.md` | Pointer to DEL-09-06 Evidence (details below) |
| PA-7 | `DEL/Evidence/R20_Owner_Login_Proof_PASS_2026-08-23/*.json`; `DEL/_run_records/R10..R21_*` | LaunchAgent packaged-login proofs (daemon model); `_STATUS.md` history 2026-09-12 retires the LaunchAgent under D-GOV-43 |
| PA-8 | `DEL/_run_records/DAPP100_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19.md`, `R18_ELECTRON_SUPPLY_FREEZE_AND_OFFLINE_BUILD_2026-08-22.md` | D-APP-100 node, which `_STATUS` says is superseded; Electron 43.2.0 supply freeze |

Further details:

- **PA-1:**
  - Output: `Chirality-3.0.0-rc.1-arm64.dmg`, 337,038,438 B, sha256 `efaac5d7…58fb9`, plus `mac-arm64/Chirality.app`.
  - Checks: `desktop:verify-dependencies` PASS; `desktop:verify-codex-pin --after-signing` PASS (codex 0.154.0); `instruction-root:integrity` pass (366 files); KG-001 source-completeness rows `remediation_required`.
  - Signing: Developer ID signed (not unsigned/adhoc); `spctl` rejected as `Unnotarized Developer ID`; `verify:version-identity` PASS.
  - Not performed: packaged S-6/S-8 checks.
- **PA-2:**
  - Output: `Chirality-3.0.0-arm64.dmg`, 338,040,805 B.
  - Stage table L26-42: `07-desktop-dist` exit 0; `04-instruction-root` exit 0.
  - Checks: instruction integrity PASS (367 files); dependency boundary PASS; Codex pin PASS; version identity PASS.
  - Signing: Developer ID signed; Gatekeeper exit 3.
- **PA-6:** records a fresh unsigned `desktop:dist` plus integrity and network proofs at source `357a58b5`, and says it is "not closure-authorizing". That build predates A2 (2026-08-20).
- **No build evidence found for the current `package.json` version `3.0.1`** (bumped by `cf4653526`, 2026-09-19). Grep for `Chirality-3.0.1-arm64.dmg` over in-root `execution/` returned no hits.

---

## P1 — SEC-1 and CLM-001..CLM-012

### SEC-1 — Codex MVP packaging basis (SoW L12-16)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| SEC-1 | Codex-only engine; subprocess executability; version identity | Codex staging: `FE/package.json:122-128` (extraResources `codex`), `:54` pin; `FE/scripts/pack-electron.mjs:103-145` `assertPackagingInputs` (Codex exec bit, code-mode host, exact pin); `FE/scripts/verify-codex-pin.mjs:99-178` (runs packaged `codex --version` L106/L122; lockfile vs package.json L113-116); `FE/electron/codex-executable.ts:15,66-94` (REACH=LIVE); `FE/electron/main.ts:816-833` (REACH=LIVE); version identity: `FE/scripts/verify-version-identity.mjs:44-47,87,124-278` (DMG name derived from productName/version/arch; Info.plist `CFBundleShortVersionString` L209) | `FE/src/__tests__/scripts/verify-codex-pin.test.ts` (4 cases), `FE/src/__tests__/electron/codex-executable.test.ts:17-57`, `FE/src/__tests__/scripts/verify-version-identity.test.ts:77,142,216` (DMG filename; staged bundle; package.json + both lock version lines) | Script invoker: `desktop:verify-codex-pin` and `verify:version-identity` (the latter is not chained into `desktop:dist`). `package.json` version `3.0.1` = `package-lock.json:3,9`. Proof: PA-1 (rc.1), PA-2/PA-3 (3.0.0); no 3.0.1 artefact. "network, credential, account-identity… containment safeguards": see CLM-004/CLM-009 REQ-009 rows. |

### Deliverable Definition — Ontology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-001 | Datasheet header (D-APP-56 R5 P40 note; REF-006 MATCH) | DOC_ONLY | — | Hints only for token `MATCH`/`docs/PRD.md` in `FE/scripts/verify-version-identity.mjs`, `FE/scripts/harness-section9-manifest.json` (incidental). |
| CLM-002 | Identification table | DOC_ONLY | — | Hint hits (`DeliverableID`, `PackageName`, `ResponsibleParty`) are incidental: `FE/src/lib/harness/scaffold.ts` (REACH=LIVE), several `FE/src/__tests__/lib/*` and `FE/src/__tests__/api/*` tests; none concern DEL-09-04. |
| CLM-003 | Attributes (release target, packaging command, outputs, integrity command, resource requirement, SDK subprocess posture, source-completeness, PRD status) | Target: `FE/package.json:158-165` (min 15.0.0, dmg arm64); `FE/scripts/pack-electron.mjs:65-78` (`--mac`, `--arm64`, `--publish never`). Command: `FE/package.json:43`. Outputs: `pack-electron.mjs:61-63` `expectedPackagedAppPath` → `<out>/mac-arm64/Chirality.app`; `verify-instruction-root-integrity.mjs:20-30` default bundle root under `dist/mac-arm64/Chirality.app/Contents/Resources/instruction-root`, output `artifacts/harness/instruction-root-integrity/latest` (L97, L683), `summary.json` write L771. Resource requirement: `FE/scripts/prepare-packaged-instruction-root.mjs:10-66,235-372`; `FE/scripts/finalize-electron-resources.mjs:20-49`. Subprocess posture: `verify-codex-pin.mjs:106,122`; `verify-packaged-dependency-boundary.mjs:94-120` `verifyPackagedCodexTree`. Source-completeness: `verify-instruction-root-integrity.mjs:54-65,579-633`. | `FE/src/__tests__/scripts/dmg-packaging-policy.test.ts:60,83,113,136`; `pack-electron.test.ts:65-140`; `verify-instruction-root-integrity.test.ts:130,142,290`; `finalize-electron-resources.test.ts:36-69`; `verify-packaged-dependency-boundary.test.ts:101` | "SDK subprocess" attribute cites NFR-030; the code now stages Codex (not the Claude SDK). `verify-instruction-root-integrity.mjs:48-52,67-74` retains `REQUIRED_UNPACKED_SDK_FILES` for `@anthropic-ai/claude-agent-sdk`, active only under `--runtime-profile legacy-claude` (default `codex-only`, L672, L697-707). |
| CLM-004 | Conditions (Node >=20, npm ci; Win/Linux excluded; unsigned/adhoc; Codex network guardrails) | Node: `FE/package.json:95-96` (`>=22.19.0`). Win/Linux: `FE/package.json` build has only `mac`. Signing: `FE/scripts/pack-electron.mjs:81-96` `signingEnvironment` (unsigned default sets `CSC_IDENTITY_AUTO_DISCOVERY=false`; Developer ID only when `CHIRALITY_SIGNING_IDENTITY_SHA1` set, off by default); `FE/package.json:154` mac.sign → `FE/scripts/sign-electron-runtime-v2.mjs:84-95`. Network: `RT/packages/daemon/src/codex-supervisor.ts:104-108,261` (REACH=LIVE, TOUCHED); `FE/electron/main.ts:129-135,197-330` REQ-NET-001 renderer egress (REACH=LIVE). | `pack-electron.test.ts:65,86`; `sign-electron-runtime-v2.test.ts:23-77`; `dmg-packaging-policy.test.ts:46` (Node floor/toolchain); `RT/tests/codex-supervisor.test.ts:90` (`sandboxPolicy` readOnly `networkAccess:false`); `FE/src/__tests__/electron/renderer-window-policy.test.ts:863-1014` (REQ-NET-001); `desktop-release-workflow.test.ts:66-80` (reads OUT_OF_ROOT workflow) | Node floor in code (`>=22.19.0`) differs textually from SoW `>=20`. The renderer allowlist names `api.anthropic.com` (`main.ts:133`) and has no Codex/OpenAI host; Codex egress is governed in the Codex child by the sandbox policy (`networkAccess:false` for read-only/workspace-write). Whether electron-builder invokes the `mac.sign` hook without an identity was not established from code. PA-1/PA-2 builds were Developer ID signed. |
| CLM-005 | Construction (run checks; build DMG; prove assets; emit summary; verify subprocess; record blockers) | `FE/package.json:17,18,21,30,43`; `pack-electron.mjs:168-189` `runElectronPack`; `finalize-electron-resources.mjs:90-149` (inventory `packaged-resources-inventory.json`, required files, executables, forbidden supply-model entries); `verify-instruction-root-integrity.mjs:645-782`; `verify-codex-pin.mjs:99-178` | As CLM-003 | Blocker recording is by script exit/`summary.status` (`verify-instruction-root-integrity.mjs:709-717`; `verify-codex-pin.mjs:169`). Deliverable-side blocker records: `DEL/_STATUS.md` Remaining. |
| CLM-006 | References | DOC_ONLY | — | `docs/*` cited are App docs at `projects/chirality-app-dev/docs/{CONTRACT,SPEC,TYPES,PLAN,PRD}.md` (present). Hints: `verify-instruction-root-integrity.mjs:589-590` cites `SOW-073; OI-004`. |

### Completion and Reliance Basis — Epistemology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-007 | Specification header | DOC_ONLY | — | |
| CLM-008 | Scope (desktop:dist, desktop:pack, DMG verification, asset inclusion/integrity, SDK subprocess probe, summary; out: Win/Linux, signing/notarization) | `FE/package.json:42,43`; `pack-electron.mjs:21,65-78` (targets `dir`/`dmg` only; `--mac --arm64`); `verify-codex-pin.mjs`; `verify-instruction-root-integrity.mjs` | `pack-electron.test.ts:127` (rejects other targets); `dmg-packaging-policy.test.ts:60`; `desktop-release-workflow.test.ts:66-80` (OUT_OF_ROOT workflow; asserts no windows/nsis) | "SDK subprocess/binary package-layout probe" is implemented for Codex by `verify-codex-pin.mjs` (packaged `--version`) and `verify-packaged-dependency-boundary.mjs:94-120`; the Claude-SDK probe scripts remain as legacy (`verify-packaged-agent-sdk-runtime.mjs`, `run-live-packaged-agent-sdk-read-tool-proof.mjs`). Signing code path exists but is off by default (see CLM-004). |
| CLM-009 | Requirements REQ-001..REQ-011 | see per-REQ rows below | see below | |
| CLM-009 / REQ-001 | macOS 15+ arm64 unsigned/unnotarized | `FE/package.json:158-165`; `pack-electron.mjs:71-72,88-96` | `dmg-packaging-policy.test.ts:60`; `pack-electron.test.ts:65,86`; `desktop-release-workflow.test.ts:66,80` (OUT_OF_ROOT workflow: `lipo -archs`, `LSMinimumSystemVersion`) | No in-root script inspects `lipo`/`LSMinimumSystemVersion`/codesign on an output; `verify-version-identity.mjs:92,209` reads Info.plist version keys only. Proof PA-1/PA-2: arm64, Developer ID signed (not unsigned). |
| CLM-009 / REQ-002 | `npm run desktop:dist` | `FE/package.json:43` | `contract-pins.manifest.ts:171` (desktop:dist contains `desktop:verify-dependencies`); `desktop-release-workflow.test.ts:66` | PA-1 L25, PA-2 L22 (`07-desktop-dist` exit 0). |
| CLM-009 / REQ-003 | `dist/Chirality-<v>-arm64.dmg` | electron-builder default artifact name (no `artifactName` in `FE/package.json` build); `verify-version-identity.mjs:44,87,177-202` | `verify-version-identity.test.ts:77,166` | Output dir overridable via `CHIRALITY_ELECTRON_OUTPUT_DIRECTORY` (`pack-electron.mjs:23,43-58`); PA-1/PA-2 used out-of-tree output dirs. |
| CLM-009 / REQ-004 | `dist/mac-arm64/Chirality.app` | `pack-electron.mjs:61-63`; `FE/package.json` `productName: Chirality` | `pack-electron.test.ts` | |
| CLM-009 / REQ-005 | integrity `summary.json` with pass or blockers | `verify-instruction-root-integrity.mjs:97,683,709-771` (`status` pass/fail; `sourceCompleteness`) | `verify-instruction-root-integrity.test.ts:181,251,290` | `sourceCompleteness.status` is independent of `status` (L579-633); PA-1/PA-2 report integrity pass with KG-001 rows `remediation_required`. |
| CLM-009 / REQ-006 | packaged resources contain instruction-root and verify before distribution | `FE/package.json:31,146-150` (prepare + extraResources `instruction-root`); `finalize-electron-resources.mjs:29` requires `instruction-root/instruction-bundle-manifest.json`; `pack-electron.mjs:32` requires cache manifest; `verify-instruction-root-integrity.mjs:337-356,387-470` (compares against `buildExpectedInstructionManifest`) | `prepare-packaged-instruction-root.test.ts:27,123,135`; `verify-instruction-root-integrity.test.ts:142` | Integrity runs after packaging, in the same `desktop:dist` chain (`FE/package.json:43`). |
| CLM-009 / REQ-007 | missing assets = P0 blocker | `verify-instruction-root-integrity.mjs:709-717` (fail on missing/mismatch/unexpected); `pack-electron.mjs:103-145`; `finalize-electron-resources.mjs:90-122` | `finalize-electron-resources.test.ts:50`; `verify-instruction-root-integrity.test.ts:142,251` | |
| CLM-009 / REQ-008 | SDK subprocess executable from package layout, no secret leakage / broader network | `verify-codex-pin.mjs:106,119-130` (packaged `codex --version`); `verify-packaged-dependency-boundary.mjs:94-120` (regular executable binaries); `finalize-electron-resources.mjs:32-35` REQUIRED_EXECUTABLES; `FE/package.json:106` `onlyLoadAppFromAsar` + Codex outside asar (`files` excludes `node_modules/@openai/**`, L117); runtime use: `FE/electron/runtime-service-host.ts:92-114` (REACH=LIVE) | `verify-codex-pin.test.ts:74,85,110`; `verify-packaged-dependency-boundary.test.ts:101`; `FE/src/__tests__/electron/runtime-service-host.test.ts:131,175`; `finalize-electron-resources.test.ts:50` | No in-root secret-leakage check tied to the Codex probe located; `FE/scripts/scan-secret-evidence.mjs` (`proof:secret-scan`) exists (not inspected). Legacy Claude probes: `FE/scripts/verify-packaged-agent-sdk-runtime.mjs` + test `FE/src/__tests__/scripts/verify-packaged-agent-sdk-runtime.test.ts`; `run-live-packaged-agent-sdk-read-tool-proof.mjs` + test. |
| CLM-009 / REQ-009 | Codex supplier network guardrails preserved | `RT/packages/daemon/src/codex-supervisor.ts:104-108,191,219,261` (REACH=LIVE, TOUCHED); `FE/electron/main.ts:129-330` (renderer REQ-NET-001, REACH=LIVE); `FE/scripts/run-network-policy-proof.mjs`, `run-packaged-security-proof.mjs` (Anthropic-host oriented) | `RT/tests/codex-supervisor.test.ts:90`; `FE/src/__tests__/electron/renderer-window-policy.test.ts`; `FE/src/__tests__/scripts/run-network-policy-proof.test.ts`, `run-packaged-security-proof.test.ts` | PA-6: `_STATUS`/Evidence note says REQ-009 / R4-P49 remained open as of 2026-08-20 (pre-A2). No A2-era packaged network proof located in PA-1/PA-2 (PA-1 L59-63 lists packaged checks as owner acts). |
| CLM-009 / REQ-010 | no Windows/Linux | `FE/package.json` build `mac` only; `pack-electron.mjs:65-78` hard-codes `--mac` | `desktop-release-workflow.test.ts:66` (OUT_OF_ROOT workflow) | `verify-instruction-root-integrity.mjs:67-74` and `codex-executable.ts:25-35` keep multi-platform maps (resolution tables, not packaging targets). |
| CLM-009 / REQ-011 | `npm run desktop:pack` | `FE/package.json:42` | `contract-pins.manifest.ts:166` | `projects/chirality-app-dev/docs/BUILD_AND_RELEASE.md:63-64,173` describe `desktop:pack`/`desktop:dist` as unsigned. |
| CLM-010 | Standards (K-ROOT/K-PACKAGE/K-RELEASE/K-VALIDATE; SPEC 1.1/19.x; PRD; TYPES) | DOC_ONLY | `contract-pins.manifest.ts:148-175` pins package.json scripts | K-VALIDATE-1 `desktop:dist` inclusion: `FE/scripts/validate-release-quality-evidence.mjs` (not verified whether it runs desktop:dist). |
| CLM-011 | Verification table (build transcript, DMG check, app check, min OS, arch, signing, summary, SDK probe, network) | As CLM-009 rows | As CLM-009 rows | Arch / min-OS / signing inspections of an output exist only in the OUT_OF_ROOT workflow and in manual records PA-1/PA-2 (`codesign` verification, arm64, `spctl`). |
| CLM-012 | Documentation (+AC-001) | DOC_ONLY for artefact list | — | Artefact-side: PA-1..PA-3 (transcript/stage tables, DMG size+sha256, app CDHash, integrity pass, Codex pin, codesign). `DEL/Evidence/` holds no A2-era packaging bundle; pointers only in `_STATUS` REM-1. "first-adapter probe output": grep `first-adapter` in `FE/scripts` → NO_CANDIDATE. |
| CLM-012 / AC-001 | DMG + app identity, arm64, min 15.0.0, unsigned/adhoc, assets + passing summary, executable Codex subprocess, network guardrails, blockers explicit | Union of REQ-001..011 rows | Union | Proof status as of frozen basis: PA-1/PA-2 cover identity, arm64, integrity pass, Codex pin (execution via `--version`); signing posture recorded = Developer ID, not unsigned/adhoc; packaged network/S-6/S-8 checks = owner acts (PA-1 L55-63). |

---

## P2 — CLM-013..CLM-025, REM-1, REM-2

### Production and Verification Method — Praxeology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-013 | Procedure header (D-APP-56 R5 P40 note) | DOC_ONLY | — | |
| CLM-014 | Purpose | DOC_ONLY | — | |
| CLM-015 | Prerequisites (cwd frontend; Node >=20; npm ci; assets or blockers; Dependencies.csv 9 ACTIVE / 6 TBD; custody TBD) | `FE/package.json:95-96` (`>=22.19.0`) | `dmg-packaging-policy.test.ts:46` | Dependencies state: `DEL/Dependencies.csv` (5,724 B) — not recounted here. Hint hits on `ResponsibleParty`/`Dependencies.csv` in `FE/src/lib/harness/scaffold.ts` and `FE/src/__tests__/api/working-root/deliverable-contracts.test.ts` are incidental. |
| CLM-016 | Steps 1-10 | Step 2: `FE/package.json:17,18,21,30`. Step 4: `:43`. Step 5 outputs: `pack-electron.mjs:61-63`, `verify-instruction-root-integrity.mjs:683,771`. Step 6 (arm64/LSMinimumSystemVersion/signing): `FE/package.json:154-165`, `pack-electron.mjs:81-96`, `sign-electron-runtime-v2.mjs:59-95` (`verifySignedBundle` runs `codesign --verify` only when the sign hook runs). Step 7: `finalize-electron-resources.mjs:90-149`; `verify-instruction-root-integrity.mjs`. Step 8 (not trapped in app.asar): `FE/package.json:106,117,122-128`; `verify-packaged-dependency-boundary.mjs:9-23,94-120`; `verify-codex-pin.mjs:106`. Step 9 working-root selector / guardrails: `FE/electron/main.ts:551,800` `registerDirectorySelectionHandler` (REACH=LIVE); `codex-supervisor.ts:104-108`. | `validate-harness-section9.test.ts`, `validate-harness-premerge.test.ts`; `pack-electron.test.ts`; `sign-electron-runtime-v2.test.ts`; `finalize-electron-resources.test.ts`; `verify-packaged-dependency-boundary.test.ts:50-101`; `FE/src/__tests__/electron/directory-selection.test.ts` | `FE/electron/main.ts:414-416`: packaged `resolveInstructionRootForProcess` returns `process.resourcesPath` (not `.../instruction-root`) and `main.ts:808` assigns it to `CHIRALITY_INSTRUCTION_ROOT`; `resolveServiceInstructionRoot` (L441-445) passes `resourcesPath/instruction-root` to the Runtime service (L828). Step 9 "SDK-backed turn start" TBD: packaged turn start not probed in PA-1/PA-2 (owner native checklist PA-5). |
| CLM-017 | Verification table (local checks, DMG, app, summary, macOS target, signing, SDK subprocess, network) | As CLM-009 REQ rows | As CLM-009 REQ rows | Same pointers as P1 CLM-011. |
| CLM-018 | Records (pre-pack transcript, desktop:dist evidence, DMG identity, app identity, summary, SDK probe, manual notes, custody, blocker list) | DOC_ONLY (record set) | — | Records: PA-1 (stage/step list, DMG sha256, CDHash), PA-2 (stage table with UTC/exit L26-42, log dir outside repo `~/.claude/chirality-build-3-release-20260913-out/build-evidence`), PA-3. Deliverable-local `DEL/Evidence/` holds no A2-era record. |
| CLM-018 / VER-001 | Run/review pre-pack checks, desktop:dist and desktop:pack; inspect identities, arch, min OS, signing, resources, summary, SDK probe, network, blockers | Union of CLM-016 pointers | Union | desktop:pack evidence in A2 era: not located in PA-1/PA-2 (both `desktop:dist`). |

### Governing Values and Decisions — Axiology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-019 | Guidance header | DOC_ONLY | — | |
| CLM-020 | Purpose | DOC_ONLY | — | |
| CLM-021 | Principles (desktop:dist release-significant; narrow target; assets as blockers; preserve boundaries packaged) | `FE/package.json:43,158-165`; `verify-instruction-root-integrity.mjs:709-717`; `codex-supervisor.ts:104-108` | `contract-pins.manifest.ts:166-175`; `dmg-packaging-policy.test.ts` | `FE/scripts/validate-release-quality-evidence.mjs` (`validate:release-quality`) is the registered release-quality gate; whether it runs `desktop:dist` not established (hint token only). |
| CLM-022 | Considerations (required asset set incl. AGENTS.md, README.md, agents/, docs/; SDK packaging empirical; summary path; unsigned posture; reviewable evidence; OBJ-008 assumption) | Code-level manifest: `FE/scripts/prepare-packaged-instruction-root.mjs:10-66` (`ROOT_FILES` AGENTS.md/CLAUDE.md/README.md; `DOC_FILES` 12 entries incl. DIRECTIVE/CONTRACT/SPEC/TYPES/WORKFLOW_COMPONENT_STANDARD/AGENT_WORKFLOW_RUNTIME/…; `TOOL_FILES`; `BUNDLED_SKILL_NAMES`; `PRODUCT_AGENTS_SOURCE` L12), `:235-372` `buildExpectedInstructionManifest`; legacy list `verify-instruction-root-integrity.mjs:33-46` (`REQUIRED_DOC_FILES` includes `PLAN.md`, `WHAT-IS-AN-AGENT.md`; used only under legacy fixture path L357-371). App product instructions: `FE/electron/product-instructions.ts:11-17` (REACH=LIVE; packaged default `resourcesPath/instruction-root/AGENTS.md`). asarUnpack hint: `FE/scripts/verify-pi-supply-chain.mjs` (Pi engine; `FE/package.json` build has no `asarUnpack`). | `prepare-packaged-instruction-root.test.ts:27`; `verify-instruction-root-integrity.test.ts:142,391,458`; `FE/src/__tests__/electron/product-instructions.test.ts:52-96` | Two in-code lists differ: v3 path (`DOC_FILES`) vs legacy (`REQUIRED_DOC_FILES`). `instruction-root:prepare` sources Root (`--source-root ../../..`, `FE/package.json:31`); SoW names `agents/`, `docs/`. Relates to CONF-003. |
| CLM-023 | Trade-offs (strict assets; app.asar vs SDK exec access; unsigned vs notarized; CI upload in DEL-09-05) | `FE/package.json:101-107` (asar + fuses), `:117,122-128` (Codex outside asar as extraResources); `finalize-electron-resources.mjs:65` (treats `app.asar.unpacked`); `FE/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs` (legacy app.asar handling) | `dmg-packaging-policy.test.ts:113,136`; `finalize-electron-resources.test.ts:50` | |
| CLM-024 | Examples (TBD: no transcript) | DOC_ONLY | — | Since-drafting artefacts exist: PA-1..PA-3 (SoW text states none available). |
| CLM-025 | Conflict table CONF-001..004 | CONF-001: DOC_ONLY. CONF-002: `verify-instruction-root-integrity.mjs:54-65,579-633` (KG-001 `tools/REGISTRY.md`, `examples` rows). CONF-003: `prepare-packaged-instruction-root.mjs:10-66` vs `verify-instruction-root-integrity.mjs:33-46` (location of code-level manifest now identifiable). CONF-004: packaged turn start — `FE/electron/main.ts:826-833` + `runtime-service-host.ts`; no packaged turn-start probe script located. | `verify-instruction-root-integrity.test.ts:290` (source-completeness remediation) | PA-1 L39-42 and PA-2 L47 record KG-001 rows `remediation_required` alongside integrity pass. Hint hits (`_CONTEXT.md`, `_REFERENCES.md`, `TBD`) in `FE/src/__tests__/lib/harness-scaffold.test.ts`, `deliverables-route.test.ts` are incidental. |

### Remaining items (`DEL/_STATUS.md`)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| REM-1 | DEL-09-04-V3-01 — package Runtime service + pinned stock `@openai/codex` into arm64 DMG under the short packaging procedure (`NOT_SELECTABLE_UNTIL` re-platformed Runtime service child + stock Codex build on production path) | `FE/package.json:41-43,54,109,122-150,154`; `FE/scripts/pack-electron.mjs` (header L8-19 "Plain Electron packaging for the App-owned Runtime (D-GOV-43, A2)"); `FE/scripts/build-electron.mjs:28-39,81-83` (bundles `dist-runtime/runtime-service/standalone-bin.mjs`, `dist-runtime/runtime-cli/chirality-cli.mjs`); `FE/scripts/finalize-electron-resources.mjs:20-49`; `FE/scripts/sign-electron-runtime-v2.mjs`; `FE/scripts/verify-codex-pin.mjs`; `FE/scripts/verify-packaged-dependency-boundary.mjs`; `FE/scripts/verify-electron-dist.mjs:9-15` (Electron 43.2.0, sha256 `ad4a0ae3…fe28`); runtime: `FE/electron/main.ts:457-470,826-833` (REACH=LIVE), `FE/electron/runtime-service-host.ts` (LIVE), `FE/electron/runtime-service-launcher.ts` (LIVE), `RT/packages/daemon/src/standalone-bin.ts` (LIVE), `codex-supervisor.ts` (LIVE, TOUCHED) | `pack-electron.test.ts`; `build-electron.test.ts:27`; `finalize-electron-resources.test.ts`; `sign-electron-runtime-v2.test.ts`; `verify-codex-pin.test.ts`; `verify-packaged-dependency-boundary.test.ts`; `verify-electron-dist.test.ts`; `dmg-packaging-policy.test.ts:113`; `FE/src/__tests__/electron/runtime-service-host.test.ts` | Hint hits for `LaunchAgent` in `FE/electron/{api-key-ipc,runtime-control-ipc,runtime-service-host}.ts` and `verify-packaged-dependency-boundary.mjs` — retired model per `_STATUS` 2026-09-12 history. Removal condition "package lands with the packaging procedure's verification evidence (bundle signature and Codex pin) recorded": PA-1 (rc.1) and PA-2/PA-3 (3.0.0) record signature + Codex pin; `_STATUS.md` (Last Updated 2026-09-12) still lists REM-1. Procedure: PA-5. Offline network-denied package evidence named in "Return": not located for A2 builds. |
| REM-2 | DEL-09-04-V3-02 — `build/icon.icns` replacement with integrity regeneration and raster reproducibility record (`NOT_SELECTABLE_UNTIL: DEL-02-01-V3-04 selected`) | `FE/build/icon.icns`, `FE/build/icon-macos.svg` (present); `FE/package.json:153` (`mac.icon`); `FE/scripts/generate-macos-icon.mjs` (106 LOC; NO_INVOKER_FOUND — header L3-9 states manual, not in build graph) | NO_CANDIDATE for icon generation (grep `icon.icns`, `generate-macos-icon`, `icon-macos` in `FE/src/__tests__`: only `dmg-packaging-policy.test.ts` reads package.json build) | `git -C <frozen> log` not run for icon files; gate is `DEL-02-01-V3-04` (outside PKG-09; not read). |

## Search notes

- Runtime searched only under `RT/packages` and `RT/tests`. `RT/execution/**` was excluded.
- Not read, recorded as out of root:
  - `OUT_OF_ROOT:.github/workflows/desktop-release-template.yml`, which `FE/src/__tests__/scripts/desktop-release-workflow.test.ts` reads.
  - `OUT_OF_ROOT:.github/workflows/harness-premerge.yml` (repository root), which `contract-pins.manifest.ts:71` pins.
- Not read (other deliverable folder): DEL-09-06 Evidence, referenced by PA-6.
