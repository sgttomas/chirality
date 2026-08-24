# Carrier Map — SCA-APP-008

**Status:** `PROPOSED_NOT_APPLIED`
**Topology:** retain the live 10-package / 51-deliverable topology and stable IDs.
**Dispatch posture:** every row remains held until SCA-APP-008 is owner-accepted and the row's later gate/activation is satisfied.

“New carrier” below means a newly explicit v3 carrier assignment on an existing live deliverable. No new folder, ID, lifecycle state, or implementation authority is created by this assessment.

## Exact App carriers

| Carrier | Live folder | WP | Proposed v3 amendment / output seat | Entry and exit fences |
| --- | --- | --- | --- | --- |
| DEL-01-01 | `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/` | WP-01 | Record App authority/reliance alignment, accepted Root notice consumption, and AT-053 App evidence without treating plans/notices as authority. | Enters only after SCA-APP-008 acceptance; no implementation. |
| DEL-02-02 | `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/` | WP-07 | Add Codex Agent 0/1/2 role-entry UX, descendant/status presentation, and the required `role not mechanically enforced` label when G-ROLE cannot prove non-delegation. Preserve Woven Dialogue non-authority and compatibility. | Static UX only after carrier acceptance; live-account success waits for G3/G-WIRE. |
| DEL-02-05 | `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/` | WP-04, WP-07 | **New explicit account/consent UX carrier assignment.** Add `HostedEngineConsentPort` UI consumption; root-private login/logout/account state; per-root login explanation; the three command-network postures; consent/revocation; typed keyring/safeStorage states; rate-limit/approval status; `Opt-in Preview` copy; no secret persistence in project truth. | Root account/consent contract must be accepted. No ambient `~/.codex`; G3/G-CSP/G4 required for live claims. |
| DEL-03-01 | `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/` | WP-05, WP-10 | Extend App conformance consumption for Root API v2, exact adapter identity, explicit four-terminal outcomes, no automatic fallback, and RQG §13 evidence. Root retains generic runtime ownership. | Root protocol/event schemas accepted; G2/G-WIRE before exact-pin claim. |
| DEL-03-03 | `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-03_Harness_API_and_SSE_Compatibility_Adapter/` | WP-05, WP-08 | Consume the closed Root API/event schema v2 while preserving browser `UIEvent` compatibility; add resume-continuity behavior: after restart, `thread/resume` only when canonical root, account identity, and policy digest match, else fresh thread; never claim in-flight turn re-attach. | Root schema accepted and migration path frozen; G-WIRE before live claim. |
| DEL-04-01 | `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/` | WP-02 | **Stays a probe.** Observe exact App Server supply/protocol/config/role behavior and produce adoption evidence; do not own supply freeze, generic adapter semantics, or implementation. Electron 43.2.0 is an observed drift and G1 blocker only. | Root exact carrier and download authority required; probe evidence does not activate implementation. |
| DEL-04-05 | `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/` | WP-04, WP-07 | Extend provider-neutral App credential bridge conformance to OAuth/device-code/keyring/safeStorage/typed decrypt failure and root-account transitions without becoming a second credential owner. Carry the three per-root command-network postures through the App boundary. | No provider expansion. Root account/consent and K-NET-1 accepted first. |
| DEL-05-01 | `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/` | WP-08 | Add lazy, non-destructive v2→v3 session/consent/root-home migration, backup/rollback, account-change invalidation, and fresh-thread/resume compatibility. | Accepted storage/consent schema first; no destructive bulk rewrite. |
| DEL-05-02 | `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL/` | WP-05, WP-10 | Consume closed `HarnessEvent` schema v2, map completed/failed/interrupted/cancelled explicitly, migrate App replay/status consumers, preserve redaction and malformed-tail tolerance. | Root event schema v2 accepted; G-WIRE required. |
| DEL-05-03 | `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-03_Redacted_RunLogger_and_Secret_Hygiene/` | WP-05, WP-10 | Extend App-side sink/redaction verification for account/device/approval/helper/App Server fields and support bundles; no raw unknown payload reaches App sinks. | Closed schema and scanner scope accepted; G-WIRE required. |
| DEL-05-04 | `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-04_Runtime_Replay_and_Transcript_View/` | WP-08 | Present restart/resume continuity truthfully: stored thread may resume only on exact identity/policy match; otherwise fresh thread. Selected replay remains read-only and cannot imply in-flight re-attach. | Schema/migration acceptance before product claim. |
| DEL-08-04 | `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/` | WP-06 | **Stays the managed-delegation bridge.** Prospectively authorize multi-child managed execution and Root `AGENTS.md` Agent 0/1/2 graph as v3 App capabilities; consume the distinct delegated-harness-native class; seat origin/lineage, approvals, hard containment, role profiles, cancellation/cleanup, and the `subagent-governance.ts:205-213` class-aware change. The current `managed-delegation.ts:480-496` sibling-overlap fail-close remains a required managed invariant. | Root D-GOV-35 condition is satisfied, but App carrier acceptance and WP-03/05 fixtures are required. Native descendants are not automatically Agent 2. |
| DEL-08-05 | `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/` | WP-06 | Record both descendant classes with truthful origin/lineage, parentage, actual adapter/provider/model, role-entry state, policy/config digest, and `instruction-asserted` calibration where applicable. Preserve managed sealed-brief evidence and native-class distinction. | Evidence schema follows accepted class semantics; no role inferred from native descent. |
| DEL-09-01 | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-01_Section_8_Harness_Validation_Preservation/` | WP-10 | Carry App conformance for the widened v3 program, including Shared Runtime Gate mapping, role/account/consent/session and native-engine regression. | Activates incrementally per accepted carrier; no release claim. |
| DEL-09-02 | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-02_Section_9_Runtime_Validation_Additions/` | WP-06, WP-10 | Carry managed/native descendant fixtures, role/native-class attribution, closed event/schema, cancellation/cleanup, Root notice evidence, and AT-053/54/55 integration. | Root/App contracts and exact carriers accepted; review only. |
| DEL-09-03 | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/` | WP-10 | Expand fake/exact/live test fan-in for migration, account/null/change, consent, role, delegation, recovery, accessibility, and exact candidate regression. | Test activation follows each carrier; G6a exact candidate required before release-byte fan-in. |
| DEL-09-04 | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/` | WP-00, WP-03, WP-09 | Preserve R20 proof identity and A1 re-stage rule; add App-side two-job installer/migration/rollback through runtime-control IPC; package supervisor/runtime bytes; keep macOS arm64 only; produce unsigned/ad-hoc preparation evidence. | R20 proof does not authorize future mutated frontend proof. No signing/notary/distribution. |
| DEL-09-05 | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-05_CI_Artifact_and_Release_Verification_Workflow/` | WP-09, WP-11 | **New explicit release-operations carrier assignment.** Author and review the exact signing/notarization/recovery/rollback/custody runbook in WP-09; execute it only in WP-11 after the owner names the exact candidate at G6a. Carry version identity, nested signing order, fuses/entitlements, notarization/stapling/Gatekeeper, GitHub prerelease, and download backcheck as later owner/CHANGE acts. | D-APP-97/F-APP-2 remain active through preparation. WP-11 requires G6a and exact owner artifact ruling; owner performs release acts. |
| DEL-09-06 | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/` | WP-04, WP-07, WP-09, WP-10 | Require all six credential IPC handlers in `api-key-ipc.ts:110-176` to adopt `runtime-control-ipc.ts:85-95` sender authorization; verify typed storage/account states, command-network consent postures, CSP/window/navigation, privacy, evidence scanning, and preparation credential-transition drills. | No production signing or provider expansion. G-CSP/G-KEY/G-WIRE at assigned gates. |

## Required owner-amendment seating

| Owner record | Exact App seating |
| --- | --- |
| G0 D1 | D-APP-74 lines 101–104 are tranche-scoped to SCA-APP-004. SCA-APP-008 prospectively supersedes that exclusion for DEL-08-04/05 v3 work by allowing multi-child managed execution and the Root Agent 0/1/2 graph as App capabilities; D-APP-74 history is not rewritten. |
| G0 A3 | DEL-02-02/05 and DEL-08-04/05 always offer Agent 0/1/2 role entry for Codex sessions. On failed G-ROLE proof, Agent 2/TASK is labelled `role not mechanically enforced`, with governed evidence marked `instruction-asserted`. |
| G0 A4 | DEL-03-03, DEL-05-01, and DEL-05-04 implement stored-thread resume only when root/account/policy identity matches; otherwise fresh thread; no in-flight turn re-attach. |
| G0 A5 | DEL-09-04/06 record no App Sandbox. Hardened runtime and later Developer ID/notarization remain gated. |
| G0 A7 | DEL-02-05/04-05/09-06 carry three per-root postures: default no command network; ask per destination via managed-network prompts showing host/protocol and caveat, with `acceptForSession` only as an explicit user act; command network on with `network_access=true`, labelled. |
| G0 A8 | DEL-02-02/05 product posture label is `Opt-in Preview`. |
| G0 A9 | DEL-02-05/04-05/05-01 use root-private app-owned `CODEX_HOME`; login per root unless G3 proves safe keyring reuse; ambient `~/.codex` is not read. |
| G0 B1 | DEL-09-04/05 target macOS arm64 only. A second target is deferred to a post-rc.1 scope change. |
| G0 B2 | TM-APP-030 remains for G-HELPER. No carrier makes the bundle-identity decision. |
| G0 B4 | TM-ROOT-122 / Electron 43.2.0 is a G1 blocker only. No pin amendment occurs; R18 frozen `electronDist` is the current package-supply posture. |
| G0 D2 | D-APP-97 and F-APP-2 remain active through preparation and lift only at G6a with the exact candidate. |
| A1 | WP-00 is closed by the R20 owner proof. Any future frontend mutation invalidates the staged procedure for any future claim and requires a newly staged revision and fresh owner-executed proof. |

## Root relationship carriers

These are notice edges, not App write or ownership seats:

| Edge | Evidence | App consumers | Meaning |
| --- | --- | --- | --- |
| `ROOT_NOTICE_D_GOV_35` | `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md`, SHA-256 `9b8ebfe16e5241bc2c58b4bbc71032837632f5b07d776e82f11a273d2469cee7` | DEL-08-04, DEL-08-05, DEL-09-02 | Root delegated-harness-native class is ruled/applied; App must adopt/amend/decline under its own instruments. |
| `ROOT_NOTICE_SCA_004_APPLIED` | Root SCA-004 revision 1.3, Gate-5 merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2`, owner confirmation R6-A, seven carriers accepted at R7-A | DEL-03-01/03, DEL-04-01/05, DEL-05-01/02, DEL-09-* | Root implementation semantics/carriers exist; App consumes accepted contracts and remains an affected client. |

## Cross-cutting seats

### RQG §13 Shared Runtime Gate

`projects/chirality-app-dev/docs/RELEASE_QUALITY_GATES.md:161-178` maps to DEL-03-01, DEL-09-01, DEL-09-02, DEL-09-03, DEL-09-04, DEL-09-05, and DEL-09-06. Evidence must prove shared daemon/session/lock/credential/interruption ownership, socket security, model-switching rules, both pilot paths, and export exclusions. The gate remains validation evidence only.

### Frozen Electron supply posture

DEL-04-01 observes Electron drift; DEL-09-04/05 preserve the current frozen package posture from R18/Tranche A:

- `electron-v43.2.0-darwin-arm64.zip`
- exact size `122090802`
- SHA-256 `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`
- version/regular-file/non-symlink/size/hash checks in `frontend/scripts/verify-electron-dist.mjs`
- local directory passed to electron-builder by `frontend/scripts/pack-electron-with-supply.mjs`

This is evidence of current packaging posture, not a replacement for the G1 pin-drift decision.

### Credential and consent security

DEL-09-06 owns App proof that the six handlers registered at `frontend/electron/api-key-ipc.ts:110-176` apply the sender-origin policy embodied by `frontend/electron/runtime-control-ipc.ts:85-95`. DEL-02-05 owns comprehensible consent/login/storage-state UI. DEL-04-05 owns the provider-neutral bridge conformance. Root remains credential/account semantic owner.

## Dispatch matrix

| Carrier group | Earliest dispatch gate | Additional holds |
| --- | --- | --- |
| WP-01 assessment/application | Owner acceptance of exact SCA-APP-008 bytes | No implementation authority implied. |
| WP-02 probe | Exact Root carrier + supply authorization | Electron drift resolved separately at G1. |
| WP-03 / WP-05 implementation | Root/App carrier acceptance + explicit implementation act | G-HELPER/G2/schema gates as applicable. |
| WP-04 / WP-07 contract/static UX | Accepted Root contract + App carrier | No live-account claim before G3/G-WIRE. |
| WP-06 delegation | D-GOV-35 landed + App carrier acceptance + WP-03/05 fixtures | G-ROLE/G-APPR/G-SBX/G-SENT/G-PROT/G-ENV/G4. |
| WP-08 migration | Contract/schema freeze | Backup/rollback and no-destructive-rewrite proofs. |
| WP-09 preparation | Supply freeze + accepted App carrier | Unsigned/ad hoc; F-APP-2 active. |
| WP-10 fan-in | Per-carrier activation | No release-readiness claim until all named gates. |
| WP-11 release operation | Owner G6a exact-candidate ruling | Owner acts; no automatic transition from preparation. |

## Not seated / explicitly deferred

- No second deployment target in rc.1.
- No App Sandbox.
- No provider expansion.
- No TM-APP-030 disposition.
- No TM-ROOT-122 pin amendment.
- No release, signing, notarization, distribution, publication, issuance, acceptance, or lifecycle act.
- No decision-replay packet is produced inside this SCA assessment; the interaction disposition is recorded in `Brief.md` as directed.
