# PREGATHER — DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

Read-only evidence map (TASK, Type 2) for RUN_D128_CONCORDANCE_2026-09-21_1614Z R2 / PKG-09, taken from the frozen tree at `00115c719`. It contains no dispositions or verdicts. The REACH tag is the module-level value from `R2/PKG-09/EVIDENCE_PACK/REACHABILITY.csv`, which is a hint only. `TOUCHED` means the path appears in `TOUCHED_PATHS.csv`.

Path legend (repo-relative): `fe/` = `projects/chirality-app-dev/frontend/`; `rt/` = `projects/chirality-runtime/`; `DEL/` = `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/`.

## Deliverable key files (bytes)

| File | Bytes |
|---|---|
| `DEL/ScopeOfWork.md` | 30258 |
| `DEL/_STATUS.md` (Remaining REM-1..4; History) | 19840 |
| `DEL/_SEMANTIC.md` | 62162 |
| `DEL/_SEMANTIC_LENSING.md` | 30434 |
| `DEL/Assessment_INSP-03_DEL-09-06.md` | 7263 |
| `DEL/Dependencies.csv` | 6870 |
| `DEL/MEMORY.md` | 6562 |
| `DEL/_DEPENDENCIES.md` | 6442 |
| `DEL/_REFERENCES.md` | 2753 |
| `DEL/_CONTEXT.md` | 2606 |
| `DEL/Evidence/**` | 216 files in 6 subfolders (listed below) |
| `DEL/_run_records/**` | 17 files |

The folder holds 243 files in total. Its SoW frontmatter pins decomposition `d6f6cadb2`, SOW-019/020/022/023 and OBJ-008.

## Decision IDs cited most (DECISION_HITS rows for DEL-09-06, excluding Evidence/ and _run_records/ paths)

| Decision | Hits | Register state |
|---|---|---|
| D-APP-38 | 13 | RULED |
| D-APP-56 | 9 | RULED |
| D-APP-97 | 6 | RULED |
| D-APP-127 | 4 | RULED |
| D-APP-36, D-APP-55, D-APP-99 | 3 each | RULED |
| D-APP-19, D-APP-71 | 2 each | RULED |
| D-GOV-43 | 2 | ROOT |
| D-APP-121, D-APP-54, D-APP-70, D-APP-72 | 1 each | RULED |

The Evidence/ and _run_records/ rows are dominated by D-APP-61 (132), D-APP-65 (88), D-APP-64 (56), D-APP-12 (20) and D-APP-94 (16).

## Main code areas

The following modules are LIVE unless another tag is shown:

- **ELECTRON renderer egress guard:** `fe/electron/main.ts`
- **Renderer window hardening, CSP and PDF classification:** `fe/electron/renderer-window-policy.ts`
- **IPC sender policy:** `fe/electron/ipc-sender-policy.ts`
- **Credential storage and IPC:** `fe/electron/api-key-storage.ts` and `fe/electron/api-key-ipc.ts`
- **Attachment picker:** `fe/electron/attachment-picker.ts`
- **Desktop log redaction:** `fe/electron/desktop-log.ts`
- **Runtime attachment staging:** `rt/packages/core/src/runtime-attachment-resolver.ts` and `rt/packages/core/src/attachment-copy.ts`
- **Runtime turn coordinator:** `rt/packages/core/src/turn-coordinator.ts`
- **Codex supervisor:** `rt/packages/daemon/src/codex-supervisor.ts` (LIVE, TOUCHED)
- **Frontend harness lib:** `fe/src/lib/harness/run-logger.ts`, `fe/src/lib/harness/api-key-store.ts`, `fe/src/lib/harness/ui-attachments.ts` and `fe/src/lib/harness/error-display.ts`
- **Legacy SDK path (LEGACY_ONLY):** `fe/src/lib/harness/anthropic-agent-sdk-manager.ts`, `fe/src/lib/harness/attachment-resolver.ts`, `fe/src/lib/harness/turn-engine.ts`, `fe/src/lib/harness/runtime.ts` and `fe/src/lib/harness/session-events.ts`
- **Build and proof scripts (not in REACHABILITY):**
  - `fe/scripts/run-packaged-security-proof.mjs` (1512 lines)
  - `fe/scripts/run-network-policy-proof.mjs` (826 lines)
  - `fe/scripts/scan-secret-evidence.mjs` (467 lines)

TOUCHED check: no `projects/chirality-app-dev/**` product path appears in `TOUCHED_PATHS.csv`. The TOUCHED Runtime paths relevant here are `rt/packages/daemon/src/codex-supervisor.ts`, `rt/packages/client/src/client.ts` and `rt/packages/core/src/session-store.ts`.

### Script invokers (package.json / in-root workflow)

| File | Invoker | Notes |
|---|---|---|
| `fe/scripts/run-packaged-security-proof.mjs` | `proof:packaged-security` (fe/package.json:34) | No in-root workflow step invokes it. Its packaged-host run needs a built app. |
| `fe/scripts/run-network-policy-proof.mjs` | `proof:network-policy` (package.json:33) | No workflow step. |
| `fe/scripts/scan-secret-evidence.mjs` | `proof:secret-scan` (package.json:32) | No workflow step. |
| `fe/scripts/validate-harness-premerge.mjs` | `harness:validate:premerge` (package.json:21) | Also run by `projects/chirality-app-dev/.github/workflows/harness-premerge.yml:52`. That workflow injects `ANTHROPIC_API_KEY` from secrets (yml:13). |
| `fe/scripts/verify-instruction-root-integrity.mjs` | `instruction-root:integrity` (package.json:30) | Also chained by `desktop:pack` and `desktop:dist`. |
| `fe/scripts/pack-electron.mjs` | `desktop:pack` (package.json:42) and `desktop:dist` (`--target dmg`, package.json:43) | Signing is off by default: pack-electron.mjs:81-87 is unsigned unless an identity SHA-1 env is set. |
| `fe/scripts/validate-release-quality-evidence.mjs` | `validate:release-quality` (package.json:29) | — |
| `test` / `typecheck` | package.json:17-18 | — |

## Section: Current Codex MVP conformity (SEC-1)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| SEC-1 | Codex sole MVP engine; K-NET-1 endpoint/command-network safeguards; S0 default-app PDF fallback | **Codex sandbox policy:** `rt/packages/daemon/src/codex-supervisor.ts:106-107` (LIVE, TOUCHED). **Approval answer path:** `codex-supervisor.ts:476`. **Consent postures:** `fe/src/lib/consent/hosted-engine-consent-port.ts:45-56` (LIVE). **PDF classification:** `fe/electron/renderer-window-policy.ts:228-323` (LIVE). **PDF emitter:** `fe/src/app/api/working-root/file/route.ts:71` (LIVE). | `rt/tests/codex-supervisor.test.ts:90`; `fe/src/__tests__/components/account-consent-settings.test.ts:70`; `fe/src/__tests__/lib/consent/fake-hosted-engine-consent-port.test.ts:372-388`; `fe/src/__tests__/api/working-root/file-route.test.ts:58-90` | Sandbox policy objects set `networkAccess: false` (codex-supervisor.ts:106-107). The `fake-hosted-engine-consent-port.ts` port is TEST_ONLY. _STATUS History 2026-09-12 records that the per-root consent postures were retired under D-APP-127. |

## Section: Deliverable Definition — Ontology (CLM-001..007)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-001 | Datasheet (D-APP-56 R5 P40 note) | DOC_ONLY | — | Header note only. |
| CLM-002 | Identification | DOC_ONLY | — | — |
| CLM-003 | Attributes: key order, storage path, base URL, allowlist, extensions, 10/18 MB | **Key order:** `fe/electron/api-key-storage.ts:226-251` (LIVE module) and `fe/src/lib/harness/api-key-store.ts:33-43` (LIVE). **Storage path:** `api-key-storage.ts:30,50` (`userData/credentials/api-key.enc`). **Base URL:** `fe/src/lib/harness/anthropic-agent-sdk-manager.ts:41,47,181,261` (LEGACY_ONLY). **Renderer allowlist:** `fe/electron/main.ts:129-135,248-289` (LIVE). **Extensions and budgets:** `rt/packages/core/src/attachment-copy.ts:8-12` (LIVE), `fe/src/lib/harness/ui-attachments.ts:1` (LIVE) and `fe/electron/attachment-picker.ts:47` (LIVE). | `fe/src/__tests__/electron/api-key-storage.test.ts:99,221`; `fe/src/__tests__/lib/api-key-store.test.ts`; `fe/src/__tests__/lib/harness-ui-attachments.test.ts:17`; `fe/src/__tests__/electron/attachment-picker.test.ts:74` | `SafeStorageCredentialStore` (api-key-storage.ts:226) is not instantiated by any non-test fe code, and `loadStoredKeyIntoGlobal` has no non-test caller. The App-owned daemon composition wires a credential port whose `get` returns undefined and whose `set`/`remove` throw `ENGINE_UNAVAILABLE` (`rt/packages/daemon/src/app-owned-composition.ts:180,225`). |
| CLM-004 | Conditions: K-KEY-1, attachment trust boundary, failure handling | See CLM-003, REQ-002 and REQ-011/012. | See REQ rows | — |
| CLM-005 | Construction: guard / endpoint / key / resolver / retry check coverage | See REQ-001..013 rows. | See REQ rows | — |
| CLM-006 | References table | DOC_ONLY | — | — |
| CLM-007 | Pass 3 notes (B-001) | DOC_ONLY | — | — |

## Section: Completion and Reliance Basis — Epistemology (CLM-008..014, AC-001)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-008 | Specification header | DOC_ONLY | — | — |
| CLM-009 | Scope (in/out) | DOC_ONLY | — | — |
| CLM-010 | Requirements table REQ-001..015 | See the per-REQ rows below. | — | — |
| REQ-001 | Key precedence: UI safeStorage > `ANTHROPIC_API_KEY` > `CHIRALITY_ANTHROPIC_API_KEY` | `fe/electron/api-key-storage.ts:235-251` (LIVE module); `fe/src/lib/harness/api-key-store.ts:33-43` (LIVE); `fe/electron/api-key-ipc.ts:185-298` (LIVE; delegates to `runtimeClient`) | `fe/src/__tests__/electron/api-key-storage.test.ts:221,428,508`; `fe/src/__tests__/electron/api-key-ipc.test.ts:125`; `fe/src/__tests__/lib/api-key-store.test.ts` | In main.ts:990 the IPC handlers delegate to the daemon client. For the live daemon credential port, see the CLM-003 remark. |
| REQ-002 | No key material in working root, logs, events or artifacts | **Configured-key redaction:** `fe/src/lib/harness/run-logger.ts:81-106` (LIVE). **Log e-mail redaction:** `fe/electron/desktop-log.ts:63` (LIVE) and `rt/packages/daemon/src/codex-app-server-client.ts:44` (LIVE). **Session-events redaction:** `fe/src/lib/harness/session-events.ts:17,74` (LEGACY_ONLY). **Secret scan:** `fe/scripts/scan-secret-evidence.mjs` (`proof:secret-scan`). | `fe/src/__tests__/lib/run-logger.test.ts:22-82`; `fe/src/__tests__/lib/redaction-path-matrix.test.ts:23,65`; `fe/src/__tests__/electron/desktop-log.test.ts`; `fe/src/__tests__/scripts/run-packaged-security-proof.test.ts:865` | `scan-secret-evidence.mjs` has no dedicated test file; it is referenced only in `fe/src/__tests__/contract-pins.manifest.ts`. |
| REQ-003 | safeStorage at `userData/credentials/api-key.enc` | `fe/electron/api-key-storage.ts:30,50,75-90,112-140` (LIVE) | `api-key-storage.test.ts:99,186,194,205,403,486` | — |
| REQ-004 | Base URL accepts only `https://api.anthropic.com`, no creds, port empty/443 | `fe/src/lib/harness/anthropic-agent-sdk-manager.ts:181-262` (LEGACY_ONLY) | `fe/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` | Only `fe/src/lib/harness/runtime.ts:1` (LEGACY_ONLY) imports the manager. No Codex-path provider-endpoint validator was found in `rt/packages/**` (grep: `api.anthropic.com`, `baseUrl`, `ANTHROPIC_BASE_URL`). |
| REQ-005 | Renderer outbound blocked except loopback + Anthropic | `fe/electron/main.ts:248-315` (`evaluateRendererEgressPolicy`, `registerRendererEgressPolicy`), registered at main.ts:666 (LIVE). **Renderer CSP:** `connect-src 'self'` at `fe/electron/renderer-window-policy.ts:187-224` (LIVE). **Navigation and window-open:** renderer-window-policy.ts:105,134,476. | `fe/src/__tests__/electron/renderer-window-policy.test.ts:60,485,731-750`; `fe/src/__tests__/scripts/run-packaged-security-proof.test.ts:638-737`; `fe/src/__tests__/scripts/run-network-policy-proof.test.ts:10,24`; `fe/src/__tests__/contract-pins.manifest.ts:215-252` | `evaluateRendererEgressPolicy` is not exported and has no direct unit test. It is covered by contract pins (string `contains`) and by the packaged-proof log parser (`run-packaged-security-proof.mjs:1061-1105`). |
| REQ-006 | Policy logs have metadata and no secrets | main.ts:301-310 logs `summarizeRendererRequestDestination` (main.ts:201) plus the category/reason. Also `summarizeDestination` at renderer-window-policy.ts:437. | `renderer-window-policy.test.ts:530,671` | — |
| REQ-007 | Node/SDK provider calls do not broaden network policy | **Codex sandbox:** `rt/packages/daemon/src/codex-supervisor.ts:106-107` (`networkAccess:false`; LIVE, TOUCHED). **Legacy path:** `anthropic-agent-sdk-manager.ts:181` (LEGACY_ONLY). **Descendant scrub:** `fe/scripts/run-network-policy-proof.mjs`. | `rt/tests/codex-supervisor.test.ts:90`; `run-network-policy-proof.test.ts:57` | — |
| REQ-008 | Server revalidates path, ext, type, readability, symlink, regular file, size | `rt/packages/core/src/attachment-copy.ts:19,42-66` and `rt/packages/core/src/runtime-attachment-resolver.ts:9-50` (LIVE; wired at `rt/packages/daemon/src/app-owned-composition.ts:226`). **Picker side:** `fe/electron/attachment-picker.ts:70,102` (LIVE). | `rt/tests/attachment-copy.test.ts:26-53`; `rt/tests/codex-attachment-adapter.test.ts:64,84`; `fe/src/__tests__/electron/attachment-picker.test.ts:60-86` | The legacy fe resolver `fe/src/lib/harness/attachment-resolver.ts:47-123` is LEGACY_ONLY and is tested at `fe/src/__tests__/lib/harness-attachment-resolver.test.ts`. |
| REQ-009 | Reject symlinks, dirs, special, unsupported, unreadable, >10 MB, >18 MB turn | `attachment-copy.ts:46-58` (LIVE) | `rt/tests/attachment-copy.test.ts:32,53`; `rt/tests/codex-attachment-adapter.test.ts:64`; `attachment-picker.test.ts:74` | No rt test hit was found for the per-turn 18 MB message (grep: `per-turn size`, `MAX_TOTAL`). |
| REQ-010 | Extension allowlist (9 extensions) | `attachment-copy.ts:10-12` (LIVE); `fe/src/lib/harness/ui-attachments.ts:1,91` (LIVE); `attachment-picker.ts:47` | `harness-ui-attachments.test.ts:17`; `codex-attachment-adapter.test.ts:64` | — |
| REQ-011 | Partial attachment failure non-fatal when content remains | **Legacy only:** `fe/src/lib/harness/attachment-resolver.ts:84-123` (LEGACY_ONLY) and `fe/src/lib/harness/turn-engine.ts:218` (LEGACY_ONLY). | `fe/src/__tests__/lib/harness-attachment-resolver.test.ts` | The live `RuntimeAttachmentResolver` throws on the first failing attachment and always returns `errors: []` (runtime-attachment-resolver.ts:49). No partial-continuation branch exists on the live path. |
| REQ-012 | Total failure with empty text → `ATTACHMENT_FAILURE` | **Contract:** `rt/packages/contracts/src/harness/types.ts:19` and `rt/packages/contracts/src/harness/errors.ts:33` (LIVE). **Mapping:** `rt/packages/core/src/turn-coordinator.ts:58` maps `ATTACHMENT_FAILURE` to `INVALID_REQUEST`. **Emitters:** `anthropic-agent-sdk-manager.ts:371-409` (LEGACY_ONLY) and `turn-engine.ts:218` (LEGACY_ONLY). **Display:** `fe/src/lib/harness/error-display.ts:47,225` (LIVE). | `harness-anthropic-agent-sdk-manager.test.ts:1548,1582`; `fe/src/__tests__/api/harness/routes.test.ts:982`; `fe/src/__tests__/lib/harness-error-display.test.ts:51,82` | No live emitter of `ATTACHMENT_FAILURE` was found in `rt/packages/**` (grep `ATTACHMENT_FAILURE`). The live resolver raises `INVALID_REQUEST`. |
| REQ-013 | UI retry preserves draft + attachments on failed send | `fe/src/components/shell/chat-panel.tsx:1379-1380,1535,1610-1627` (LIVE); `fe/src/lib/harness/chat-draft.ts` (LIVE) | `fe/src/__tests__/components/chat-panel-native-attachments.test.tsx:99`; `fe/src/__tests__/components/chat-panel-folder-binding.test.tsx:106,729,942`; `fe/src/__tests__/components/chat-panel-turn-attach.test.tsx:328` | Restoration is conditioned on `definitelyNotStarted` (chat-panel.tsx:1387,1535). |
| REQ-014 | Explicit repeatable local checks | See the script invokers table above. | — | — |
| REQ-015 | Command family `npm run test`/`typecheck`/`harness:validate:premerge`/`instruction-root:integrity`/`desktop:dist` | package.json:17,18,21,30,43; `harness-premerge.yml:52` | `fe/src/__tests__/scripts/verify-instruction-root-integrity.test.ts`; `fe/src/__tests__/scripts/desktop-release-workflow.test.ts` | — |
| CLM-011 | Standards table | DOC_ONLY | — | — |
| CLM-012 | Verification (sub-items REQ-001/004/005/008/011/014) | See the REQ rows above. | See REQ rows | Sub-items map as follows: REQ-001 to REQ-001..003; REQ-004 to REQ-004/007; REQ-005 to REQ-005/006; REQ-008 to REQ-008..010; REQ-011 to REQ-011..013; REQ-014 to REQ-014/015. |
| CLM-013 | Documentation (C-001, D-001 TBD slots) | DOC_ONLY | — | The proof artefacts are listed below. |
| CLM-014 / AC-001 | Acceptance incl. D121 central policy, trusted-server eligibility, packaged multi-page PDF | **Central finalizer:** `fe/electron/renderer-window-policy.ts:282-323,372,418` (`isEligiblePdfResponse`, `finalizeRendererResponseHeaders`, `createEligiblePdfResponseHeaders`, `applyPackagedRendererRequestPolicy`), applied at `fe/electron/main.ts:599` (LIVE). **PDF emitter:** `fe/src/app/api/working-root/file/route.ts:71` (LIVE). **D121 matrix:** `fe/scripts/run-packaged-security-proof.mjs:50-140,248-400`. | `renderer-window-policy.test.ts:214,225,297,441,737,773`; `run-packaged-security-proof.test.ts:91,130,317,532`; `file-route.test.ts:58-90` | `D121_S1_MATRIX_STATUS = 'INAPPLICABLE_OWNER_DEFERRED'` is set at run-packaged-security-proof.mjs:92. No D121/PDF packaged-evidence folder exists under `DEL/Evidence/`. |

## Section: Production and Verification Method — Praxeology (CLM-015..021, VER-001)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-015 | Procedure header | DOC_ONLY | — | — |
| CLM-016 | Purpose | DOC_ONLY | — | — |
| CLM-017 | Prerequisites (TBD slots F-001, D-001) | DOC_ONLY | — | The implementation targets now located are in the REQ rows. |
| CLM-018 | Steps 1-8 | **Steps 3-7:** see REQ-001..013. **Step 8:** see the script invokers table. | See REQ rows | Step 3 asks for key status `ui`/`env`/`none`, which is at `api-key-storage.ts:16`. The UI is `fe/src/components/settings/api-key-settings.tsx` (LIVE), tested at `fe/src/__tests__/components/api-key-settings-storage-states.test.ts`. |
| CLM-019 | Verification checks table | See REQ-001, 002, 004, 005, 008, 009 and 011-013. | See REQ rows | — |
| CLM-020 | Records (X-001 TBD) | DOC_ONLY | — | The proof artefacts are listed below. |
| CLM-021 / VER-001 | Run or inspect the key/provider/renderer/attachment/retry/secret-scan checks, plus the D121 matrix | `fe/scripts/run-packaged-security-proof.mjs`; `fe/scripts/run-network-policy-proof.mjs`; `fe/scripts/scan-secret-evidence.mjs` | `run-packaged-security-proof.test.ts` (24 cases); `run-network-policy-proof.test.ts` (3 cases) | — |

## Section: Governing Values — Axiology (CLM-022..029)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-022 | Guidance header | DOC_ONLY | — | — |
| CLM-023 | Purpose | DOC_ONLY | — | — |
| CLM-024 | Principles 1-6 | Covered by the REQ-002, 005, 007, 008 and 011-013 candidates. | See REQ rows | Principle 4 (separate provider vs renderer surfaces) corresponds to main.ts:248 (renderer) versus codex-supervisor.ts:106 and anthropic-agent-sdk-manager.ts:181 (provider). |
| CLM-025 | Considerations | DOC_ONLY | — | — |
| CLM-026 | Trade-offs | DOC_ONLY | — | — |
| CLM-027 | Examples (base URL, creds, renderer denial, symlink, partial/total failure) | See REQ-004, 005, 009, 011 and 012. | See REQ rows | — |
| CLM-028 | Conflict table | DOC_ONLY | — | — |
| CLM-029 | Pass 3 notes (E-001) | DOC_ONLY | — | — |

## Section: Remaining (`DEL/_STATUS.md`, REM-1..4)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| REM-1 | Prior D-APP-97 scope closed 2026-08-20 | DOC_ONLY | — | The proof is under `DEL/Evidence/Packaged_Security_Proof_2026-08-20*`. |
| REM-2 | V3-02: typed account states; App egress restricted to governed endpoint set; deny unexpected `networkApprovalContext` | `fe/electron/main.ts:248-315` (LIVE); `rt/packages/daemon/src/codex-supervisor.ts:106-107,476` (LIVE, TOUCHED); `fe/src/lib/harness/server-request-answer.ts` (LIVE) | `rt/tests/codex-supervisor.test.ts:90` | **NO_CANDIDATE** for `networkApprovalContext` handling (grep `networkApprovalContext`, `network_access`, `networkAccess` over fe/src, fe/electron, rt/packages, rt/tests). The status text alone names it. The item is marked NOT_SELECTABLE. |
| REM-3 | V3-03: scan new Codex field families with synthetic secrets absent from every sink | `fe/scripts/scan-secret-evidence.mjs`; `fe/src/lib/harness/run-logger.ts:81-106`; `fe/electron/desktop-log.ts:63`; `rt/packages/daemon/src/codex-app-server-client.ts:44` | `run-logger.test.ts`; `redaction-path-matrix.test.ts` | **NO_CANDIDATE** for Codex account/approval/thread/policy/tool-activity field-family scan fixtures (grep `synthetic`, `field famil`, `secret` in fe/src/__tests__ and rt/tests). The item is NOT_SELECTABLE until DEL-05-03-V3-01 lands. |
| REM-4 | V3-07: D121 bounded built-in PDF renderer policy exception | Write locus: `fe/scripts/run-packaged-security-proof.mjs:50-400` (D121 matrix), plus `fe/electron/renderer-window-policy.ts:228-323` and `fe/src/app/api/working-root/file/route.ts:71` (LIVE) | `fe/src/__tests__/scripts/run-packaged-security-proof.test.ts:91,130,317,532`; `renderer-window-policy.test.ts:214-312,737,773`; `file-route.test.ts:58-90` | The S1 status constant reads `INAPPLICABLE_OWNER_DEFERRED` (mjs:92). The item is NOT_SELECTABLE. The design reference `execution/_Coordination/AgentRuns/APP_V3_INTEGRATION_2026-09-06/pdf-scope/DESIGN.md` was not read. |

## Recorded proof artefacts (separate from code)

| Artefact | Relevant units |
|---|---|
| `DEL/Evidence/Packaged_Security_Proof_2026-08-20/` (61 files: SUMMARY.md, registered-product-checks*.json, secret-scan/, instruction-root/, packaged-host-attempt-1/2, Remediation_01) | REQ-001..007, REQ-014/015, REM-1 |
| `DEL/Evidence/Packaged_Security_Proof_2026-08-20_Precedence_Closure/` (SUMMARY.md, summary.json) | REQ-001 |
| `DEL/Evidence/Node_A_Credential_IPC_Sender_Authorization_2026-09-03/` (EVIDENCE.md and 3 proof bundles) | REQ-003/005, V3-01 (renderer hardening, IPC sender) |
| `DEL/Evidence/Node_G_Egress_Probe_Restriction_2026-09-03/` (EVIDENCE.md and 1 bundle) | REQ-005/006, V3-05 |
| `DEL/Evidence/Node_N_CSP_Nonce_2026-09-04/` (87 files: EVIDENCE.md, MANIFEST.sha256, secret-scan-summary.json, section8-local) | REQ-005, V3-04 |
| `DEL/Evidence/Historical_DEL-03-06/` (40 files; OI-002 proofs 2026-07-22/23; PROVENANCE.md) | Historical migration |
| `DEL/_run_records/TASK_RUN_2026-09-03_NODE_A.md`, `TASK_RUN_2026-09-03_NODE_G.md`, `TASK_RUN_2026-09-03_NODE_K.md`, `TASK_RUN_2026-09-04_NODE_N.md`, `TASK_RUN_2026-08-20_0047.md`, `TASK_RUN_2026-08-20_1630.md`, `D121_CARRIER_APPLICATION_2026-09-07.md`, `R5_DAPP56_DECISION_APPLICATION_2026-07-12.md` and 9 others | Per _STATUS History |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_{A,G,K,N}_2026-09-0x/` (in root, not read); `OUT_OF_ROOT:plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md` | Named by _STATUS History |
