# PREGATHER — DEL-01-02 Reliance Boundary Register (PKG-01, R2)

Read-only evidence map for run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, frozen basis `00115c719`.
It contains no dispositions and no judgments of alignment. Remarks are factual pointers only.

**Path legend** (all repo-relative): `FE/` = `projects/chirality-app-dev/frontend/`;
`APPDOC/` = `projects/chirality-app-dev/docs/`; `RT/` = `projects/chirality-runtime/`;
`DEL/` = `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/`.
`REG` = `APPDOC/harness/reliance_boundary_register.md` (the deliverable's primary artifact, 193 lines).
`MAN` = `FE/scripts/harness-section9-manifest.json`; `VAL` = `FE/scripts/validate-harness-section9.mjs`.
REACH comes from `EVIDENCE_PACK/REACHABILITY.csv` (module-level, import-based; a hint only).
`n/a` = a test, a document or a script, with no REACH row. `TOUCHED` = listed in `TOUCHED_PATHS.csv`.

## 1. Header

### Key deliverable files (bytes)

| File | Bytes |
|---|---:|
| `DEL/ScopeOfWork.md` (775 lines; 60 CLM, AC-001, VER-001) | 49772 |
| `DEL/_SEMANTIC.md` | 58864 |
| `DEL/_SEMANTIC_LENSING.md` | 38019 |
| `DEL/Dependencies.csv` | 25047 |
| `DEL/Assessment_INSP-03_DEL-01-02.md` | 9828 |
| `DEL/_DEPENDENCIES.md` | 8126 |
| `DEL/Evidence_D53A_Dependency_Reconciliation_2026-07-10.md` | 7144 |
| `DEL/_STATUS.md` (IN_PROGRESS; Checking Approval SHA 8c6d55d3e…) | 4269 |
| `DEL/MEMORY.md` | 2979 |
| `DEL/_REFERENCES.md` | 2725 |
| `DEL/_CONTEXT.md` | 2604 |
| `DEL/_run_records/` | 15 entries |

### Decision IDs cited most (DECISION_HITS.csv, DEL-01-02: 148 rows)

D-APP-56 (34), D-APP-53 (31), D-APP-38 (29), D-APP-68 (23), D-GOV-16 (19), D-APP-55 (4), D-APP-77 (3),
D-APP-19 (2), D-GOV-20 / D-APP-72 / D-APP-54 (1 each). Register states: DELIVERABLE RULED 125,
DELIVERABLE ROOT 20, RULING RULED 2, REGISTER RULED 1.
REG itself cites D-GOV-43 (A2 amendment, REG:12, :142, :171), D-APP-72 (REG:42), D-APP-74 (REG:182), D-APP-98 (REG:42).
The D-APP-127 application map lists every DEL-01-02 carrier as `NO`/`NONE_FOUND`.
REFERENCE_HASHES: CONTRACT, PRD and SPEC recorded as `MATCH` in `_REFERENCES.md`, but all three recompute `Match=NO` at `00115c719`.

### Main code areas involved

1. **Legacy in-process SDK harness** `FE/src/lib/harness/*`. Every module that REG rows RB-ENGINE…RB-FALLBACK name is
   `LEGACY_ONLY`, except `session-manager.ts`, `run-logger.ts` and `sanitize.ts`, which are `LIVE`.
2. **Deprecated re-export shims** `FE/packages/harness-contract/src/{agent-engine-port,event-schema,tool-catalog,tool-descriptor}.ts`.
   Each file has 2 lines, `export * from '@chirality/runtime-contracts/…'`, and has no REACH row. The targets are
   `RT/packages/contracts/src/harness/*.ts` (LIVE).
3. **Live Codex/Runtime path** (not cited by the SoW; cited only by REG's SCA-APP-003 addendum rows):
   `RT/packages/daemon/src/codex-supervisor.ts`, `RT/packages/core/src/{session-store,delegated-runtime,runtime-service}.ts`,
   and `FE/electron/runtime-service-{host,launcher}.ts` (all LIVE).
4. **Lifecycle API**: `FE/src/app/api/working-root/deliverable/status/{route,transition/route}.ts`, `FE/src/lib/lifecycle/transition.ts` (LIVE).
5. **Section 9 validator**: MAN plus VAL (16 IDs; the ID list is at VAL:30-45).

TOUCHED check: `TOUCHED_PATHS.csv` lists no `projects/chirality-app-dev/**` path. None of the paths below is `TOUCHED`.
The TOUCHED Runtime files (`RT/packages/core/src/session-store.ts`, `RT/packages/daemon/src/codex-supervisor.ts`,
`RT/packages/daemon/src/runtime-daemon.ts`, `RT/packages/daemon/src/app-owned-composition.ts`) appear below and are flagged where they do.

### Path-existence check for surfaces named in the SoW and REG

Every backticked concrete path in CLM-051 and REG exists at the frozen tree, with 2 exceptions.
`LIVE_OMLX_PROOF_2026-07-22.json` (REG:42) is a bare filename not found at the App, frontend, Root or Runtime root.
`_STATUS.md` is generic. `.chirality/sessions/<sessionId>/events.jsonl` is a runtime pattern. The retained guard test
`FE/src/__tests__/docs/reliance-boundary-register.test.ts:20-31` checks only backticked `frontend/(src|packages|scripts|docs)/…` paths.

## 2. Deliverable Definition — Ontology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-001 | Datasheet heading | DOC_ONLY | — | Heading only. |
| CLM-002 | Identification | `REG` exists (n/a) | `FE/src/__tests__/docs/reliance-boundary-register.test.ts`; `FE/src/__tests__/contract-pins.test.ts` (pin manifest `FE/src/__tests__/contract-pins.manifest.ts:411`) | DOC_ONLY fields. Primary artifact path resolves to `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md`. `MAN:41` lists it as the evidenceFile for `section9.reliance_boundary_register`. HINTS hits for DeliverableID/PackageID tokens are generic fixtures. |
| CLM-003 | Attributes | DOC_ONLY | — | Heading only. |
| CLM-004 | Source State | `APPDOC/{DIRECTIVE,CONTRACT,SPEC,TYPES,PLAN,PRD}.md` all exist | `FE/src/__tests__/scripts/verify-instruction-root-integrity.test.ts` (hint hits at :18, :22) | DOC_ONLY. Every REF row reads `MATCH`, but REFERENCE_HASHES recomputes CONTRACT/SPEC/PRD as `Match=NO` at `00115c719`. `AGENT_SOFTWARE_DECOMP.md` (REF-007) was not located by this gather. |
| CLM-005 | Decomposition Traceability | DOC_ONLY | — | SOW/OBJ trace only. |
| CLM-006 | Boundary Taxonomy (13 RB rows) | See §2a | See §2a | REG has 14 core rows (it adds `RB-LOCAL-PROVIDER`, REG:42) plus SCA-APP-003 rows (REG:142-149) and SCA-APP-004 rows (REG:188-193) not present in the SoW taxonomy. |
| CLM-007 | Conditions | `FE/src/lib/harness/sdk-options-builder.ts:27,248` `settingSources` (LEGACY_ONLY); `FE/src/lib/harness/permission-overlay.ts:14` `'allow'\|'deny'\|'ask'` (LEGACY_ONLY) | `FE/src/__tests__/lib/sdk-options-builder.test.ts`; `FE/src/__tests__/lib/permission-overlay.test.ts` | `sdk-options-builder.ts:248` parses `CHIRALITY_SDK_SETTING_SOURCES`. No `settingSources` occurrence exists in `RT/packages/**`. The live engine is Codex App Server (`RT/packages/daemon/src/codex-supervisor.ts`, LIVE, TOUCHED). The events.jsonl condition corresponds to `RT/packages/core/src/session-store.ts:969-974` (LIVE, TOUCHED). |
| CLM-008 | Construction | DOC_ONLY | — | Heading only. |
| CLM-009 | Minimum Register Fields | `REG:19-35` schema; `REG:39` header row | `FE/src/__tests__/docs/reliance-boundary-register.test.ts` | DOC_ONLY. The field list at REG:23-35 matches the SoW field names. |
| CLM-010 | Deferred Completion Fields | DOC_ONLY | — | ResponsibleParty is still `TBD` (SoW:38). |
| CLM-011 | Candidate Validation Index | `MAN:10-115` (16 IDs); `VAL:30-45` | See §2b | SoW:164 and :166 say `section9.reliance_boundary_register` and `section9.sdk_session_link_resume` are not implemented. Both are present at `MAN:38` and `MAN:52`, and in REG:87 and :89. `section9.domain_profile_validation` (MAN:115) is not in the SoW index. |
| CLM-012 | References | `APPDOC/*.md` exist | — | DOC_ONLY. |
| CLM-013 | D-APP-56 R5 P45 reconciliation | `MAN:52`, `MAN:115`; `FE/src/lib/harness/tool-shell-policy.ts:157` `evaluateShellCommandPolicy` (LEGACY_ONLY) | `FE/src/__tests__/lib/session-manager.test.ts`; `FE/src/__tests__/lib/domain-profile-registry.test.ts` | REG:131-136 carries the same annotation. REG:52 and :114 still read "Bash … denied by default". |

### 2a. Boundary rows (CLM-006 taxonomy × REG core rows)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-006/RB-ENGINE | Runtime engine contract | `FE/packages/harness-contract/src/agent-engine-port.ts` (no REACH row; re-export shim) → `RT/packages/contracts/src/harness/agent-engine-port.ts:77` `AgentEnginePort`, `:90` `RuntimeEngineContract` (LIVE); `FE/src/lib/harness/agent-runtime-contract.ts` (LEGACY_ONLY); `FE/src/lib/harness/runtime.ts` (LEGACY_ONLY); `FE/src/lib/harness/turn-engine.ts` (LEGACY_ONLY); `FE/docs/harness/runtime_engine_contract.md` exists | `FE/src/__tests__/lib/engine-conformance.test.ts`; `FE/src/__tests__/lib/sdk-message-mapper.test.ts` | The `RuntimeEngineContract` symbol is defined in RT contracts, not in `FE/src/lib/harness/agent-runtime-contract.ts`, which exports child-run contract types (:10-242). The REACH entry for the RT port is `FE/src/app/api/harness/interrupt/route.ts`. |
| CLM-006/RB-AUDIT | Runtime audit mirror | `FE/packages/harness-contract/src/event-schema.ts` (shim) → `RT/packages/contracts/src/harness/event-schema.ts` (LIVE); `FE/src/lib/harness/session-events.ts` (LEGACY_ONLY); `FE/src/lib/harness/sdk-message-mapper.ts` (LEGACY_ONLY); live writer `RT/packages/core/src/session-store.ts:969-974` (LIVE, TOUCHED); `FE/src/app/api/harness/session/[id]/events/route.ts` (LIVE) | `FE/src/__tests__/lib/turn-engine.test.ts`; `FE/src/__tests__/lib/session-events.test.ts`; `FE/src/__tests__/lib/transcript-replay.test.ts`; `FE/src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts`; `RT/tests/native-message-replay.test.ts`; `RT/tests/agent1-run.test.ts` | REG:43 cites only FE legacy modules plus the shim. The RT session-store is not cited in the SoW. |
| CLM-006/RB-PERMISSION | Permission decisions | `FE/src/lib/harness/permission-overlay.ts:112` `resolveHarnessPermissionDecision`, `:364` `createHarnessCanUseTool` (LEGACY_ONLY); `permission-broker.ts`, `permission-event-channel.ts` (LEGACY_ONLY); live: `RT/packages/daemon/src/codex-supervisor.ts:40` `APPROVAL_REQUEST_METHODS`, `:219` `approvalPolicy`/`sandbox` on `thread/start` (LIVE, TOUCHED); `FE/src/components/shell/request-card.tsx`, `FE/src/lib/shell/harness-event-views.ts` (LIVE) | `FE/src/__tests__/lib/permission-overlay.test.ts`; `RT/tests/codex-supervisor.test.ts`; `FE/src/__tests__/components/request-card.test.tsx`; `FE/src/__tests__/lib/harness-event-views-codex.test.ts` | Codex approval handling is not cited in REG:44 or the SoW. |
| CLM-006/RB-FILESYSTEM | Filesystem writes and roots | `FE/src/lib/harness/tool-path-policy.ts:164` `evaluateToolPathPolicy` (LEGACY_ONLY); `FE/src/lib/harness/chirality-hooks.ts:426` `createChiralityToolHooks` (LEGACY_ONLY); `FE/src/lib/harness/mcp/read-tools.ts` (LEGACY_ONLY); live: `RT/packages/core/src/runtime-service.ts:592-598` `isContained(roots.instructionRoot, …)` (LIVE); `RT/packages/core/src/fs.ts` (LIVE) | `FE/src/__tests__/lib/chirality-hooks.test.ts`; `FE/src/__tests__/lib/harness-instruction-root.test.ts`; `FE/src/__tests__/scripts/verify-instruction-root-integrity.test.ts`; `FE/src/__tests__/lib/chirality-read-mcp.test.ts`; `FE/src/__tests__/api/working-root/file-route.test.ts`; `RT/tests/physical-filesystem.test.ts` | Under the live path, write sandboxing is set through Codex `sandbox`/`sandboxPolicy` (`codex-supervisor.ts:219,261`). REG:45 says "working-root API tests" without naming a file. |
| CLM-006/RB-LIFECYCLE | Lifecycle and gates | `FE/src/app/api/working-root/deliverable/status/route.ts` (LIVE); `…/status/transition/route.ts` (LIVE); `FE/src/lib/lifecycle/transition.ts:26-29` (`IN_PROGRESS→CHECKING` and `CHECKING→ISSUED` actors `['HUMAN']`), `:55` `approvalSha` (LIVE); `FE/src/lib/lifecycle/status-writer.ts` (LIVE); `FE/src/lib/workspace/deliverable-contracts.ts` (LIVE); `FE/src/lib/harness/mcp/read-tools.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/lifecycle-status.test.ts`; `FE/src/__tests__/api/working-root/deliverable-contracts.test.ts`; `FE/src/__tests__/lib/workspace-deliverable-api.test.ts`; `FE/src/__tests__/lib/chirality-mutating-mcp.test.ts` | REG:46 cites `…/deliverable/status/**`, which exists. |
| CLM-006/RB-TRANSCRIPT | SDK transcript separation | `FE/src/lib/harness/session-manager.ts:632` `FileSessionManager` (LIVE; REACH entry `FE/src/app/api/working-root/file/route.ts`); `session-events.ts`, `sdk-options-builder.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/session-manager.test.ts`; `FE/src/__tests__/lib/session-manager-v2-legacy-access.test.ts`; `FE/src/__tests__/lib/transcript-replay.test.ts` | `session-manager.ts:22` distinguishes `'legacy' \| 'canonical'` record shapes. |
| CLM-006/RB-SETTINGS | SDK settings isolation | `FE/src/lib/harness/sdk-options-builder.ts:248` (LEGACY_ONLY) | `FE/src/__tests__/lib/sdk-options-builder.test.ts`; `FE/src/__tests__/lib/claude-agent-sdk-manager.test.ts`; `FE/src/__tests__/lib/engine-conformance.test.ts` | NO_CANDIDATE on the live path. Terms tried: `settingSources` across `RT/packages`, `RT/tests`, `FE/src`, `FE/electron`. Only FE legacy/test hits. The live Codex path uses the user's shared Codex configuration (AGENTS.md D-GOV-43). |
| CLM-006/RB-SUBAGENT | Subagent delegation | `FE/src/lib/harness/subagent-governance.ts:196` `evaluateSubagentGovernance` (LEGACY_ONLY); `managed-delegation.ts`, `subagent-bridge.ts`, `mcp/coordination-tools.ts` (LEGACY_ONLY); live: `RT/packages/core/src/delegated-runtime.ts:83,103` `developerInstructions` envelope (LIVE); `RT/packages/core/src/delegated-engine-adapter.ts` (LIVE); `delegate_agent` name in `RT/packages/contracts/src/harness/{tool-descriptor,mcp/tool-names}.ts` (LIVE) | `FE/src/__tests__/lib/harness-subagent-governance.test.ts`; `FE/src/__tests__/lib/agent-runtime-contract.test.ts`; `FE/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`; `RT/tests/delegated-runtime.test.ts`; `RT/tests/descendant-tracker.test.ts`; `RT/tests/stagec-native-child-history.test.ts` | REG:49 cites FE legacy modules only. |
| CLM-006/RB-HUMAN-GATE | Human authority | `FE/src/lib/lifecycle/transition.ts:26-29` (LIVE) | `FE/src/__tests__/lib/lifecycle-status.test.ts` | Mostly process/human surfaces. REG:50 ValidationID is `TBD`. `MAN:115` domain_profile_validation is mapped to RB-HUMAN-GATE at REG:98. |
| CLM-006/RB-TOOL-SURFACE | Tool exposure | `FE/packages/harness-contract/src/{tool-descriptor,tool-catalog}.ts` (shims) → `RT/packages/contracts/src/harness/{tool-descriptor,tool-catalog}.ts` (LIVE); `FE/src/lib/harness/sdk-options-builder.ts` (LEGACY_ONLY); `FE/docs/harness/tool_catalog.md` exists; live dynamic tools `RT/packages/daemon/src/application-tools.ts` (LIVE, TOUCHED) | `FE/src/__tests__/lib/tool-descriptor.test.ts`; `FE/src/__tests__/lib/permission-overlay.test.ts`; `FE/src/__tests__/lib/chirality-read-mcp.test.ts`; `RT/tests/application-tools.test.ts`; `RT/tests/codex-application-tools.test.ts` | Live Codex `dynamicTools` are passed at `codex-supervisor.ts:219`. |
| CLM-006/RB-HOOKS | Hook lifecycle / fail-closed | `FE/src/lib/harness/chirality-hooks.ts:426` (LEGACY_ONLY); `tool-shell-policy.ts:157` (LEGACY_ONLY); `tool-path-policy.ts:164` (LEGACY_ONLY) | `FE/src/__tests__/lib/chirality-hooks.test.ts`; `FE/src/__tests__/lib/harness-subagent-governance.test.ts` | No live-path hook runner located. Terms tried: `PreToolUse`, `failClosed`, `createChiralityToolHooks` in `RT/packages`, `RT/tests`; the only hit is descriptive text at `RT/packages/contracts/src/harness/tool-catalog.ts:62-69` (LIVE). |
| CLM-006/RB-REDACTION | Secrets / redaction | `FE/src/lib/harness/run-logger.ts:81` `redactConfiguredApiKeys`, `:95` `redactJsonLike` (LIVE; REACH entry `FE/src/app/chat/page.tsx`); `FE/src/lib/harness/sanitize.ts` (LIVE); `tool-evidence.ts`, `tool-result-artifacts.ts` (LEGACY_ONLY); `FE/scripts/scan-secret-evidence.mjs` exists; `RT/packages/daemon/src/codex-app-server-client.ts:44` `redactAccountText` | `FE/src/__tests__/lib/tool-evidence.test.ts`; `FE/src/__tests__/lib/tool-result-artifacts.test.ts`; `RT/tests/codex-app-server-client.test.ts` | `sanitize.ts` exports only `sanitizeLabel`/`sanitizeNonEmptyLabel` (:12, :16). It contains no `redact`/secret handling. |
| CLM-006/RB-FALLBACK | SDK fallback | `RT/packages/contracts/src/harness/engine-conformance.ts` (LIVE) | `FE/src/__tests__/lib/engine-conformance.test.ts` | Governance-only row; REG:54 says `TBD` for fallback trigger review. |
| (REG only) RB-LOCAL-PROVIDER | Pi/oMLX path | `FE/src/lib/harness/pi-agent-engine-adapter.ts`, `omlx-provider-config.ts` (LEGACY_ONLY); `FE/electron/api-key-ipc.ts`, `api-key-storage.ts` (LIVE); `RT/packages/engine-pi-omlx/src/*` (TEST_ONLY) | `FE/src/__tests__/lib/pi-agent-engine-adapter.test.ts`; `RT/tests/omlx-client.test.ts`; `RT/tests/pi-turn-runtime.test.ts`; `RT/tests/pi-packaging.test.ts` | Not in the SoW taxonomy. `LIVE_OMLX_PROOF_2026-07-22.json` is MISSING at the checked roots. |
| (REG only) SCA-APP-003 rows | RB-DAEMON, RB-CONTROL-SOCKET, RB-ROLE-MODEL, etc. | `FE/electron/runtime-service-host.ts`, `runtime-service-launcher.ts`, `runtime-socket-watch.ts`, `runtime-control-ipc.ts` (LIVE); `RT/packages/daemon/src/runtime-daemon.ts:293` `chmod(socketPath, 0o600)` (LIVE, TOUCHED); `RT/packages/core/src/project-registry.ts`, `native-role-config.ts` (LIVE) | `FE/src/__tests__/electron/runtime-service-host.test.ts`; `…/runtime-socket-watch.test.ts`; `…/runtime-control-ipc.test.ts`; `RT/tests/daemon.test.ts`; `RT/tests/runtime-daemon-signal.test.ts`; `RT/tests/native-role-config.test.ts`; `RT/tests/contracts-and-project.test.ts` | Not in the SoW. REG:146 RB-RESIDENCY and REG:148 RB-PEC-ADAPTER are marked RETIRED. |

### 2b. Validation IDs (CLM-011, CLM-032) — MAN line, test files (all exist), evidence file REACH

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-011/runtime_engine_contract | MAN:10 | `FE/src/lib/harness/agent-runtime-contract.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/engine-conformance.test.ts` | — |
| CLM-011/adapter_turn_engine_event_log | MAN:17 | `FE/src/lib/harness/turn-engine.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/turn-engine.test.ts` | — |
| CLM-011/adapter_message_mapper | MAN:24 | `FE/src/lib/harness/sdk-message-mapper.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/sdk-message-mapper.test.ts` | — |
| CLM-011/session_event_replay | MAN:31 | `FE/src/lib/harness/session-events.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/session-events.test.ts`; `FE/src/__tests__/lib/transcript-replay.test.ts` | — |
| CLM-011/reliance_boundary_register | MAN:38 | `REG` (n/a) | `FE/src/__tests__/docs/reliance-boundary-register.test.ts`; `FE/src/__tests__/contract-pins.test.ts` | SoW:164 says it is not in the script. MAN and VAL include it. |
| CLM-011/settingsources_isolation | MAN:45 | `FE/src/lib/harness/sdk-options-builder.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/sdk-options-builder.test.ts` | — |
| CLM-011/sdk_session_link_resume | MAN:52 | `FE/src/lib/harness/session-manager.ts` (LIVE) | `sdk-options-builder.test.ts`; `session-manager.test.ts`; `transcript-replay.test.ts` (all under `FE/src/__tests__/lib/`) | SoW:166 says it is not implemented. CLM-013/023/060 say it is implemented. |
| CLM-011/permission_overlay_hard_deny_precedence | MAN:59 | `FE/src/lib/harness/permission-overlay.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/permission-overlay.test.ts` | — |
| CLM-011/tool_runtime_read_file | MAN:66 | `FE/src/lib/harness/mcp/read-tools.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/chirality-read-mcp.test.ts` | — |
| CLM-011/chirality_mcp_status_dependencies | MAN:73 | `FE/src/lib/harness/mcp/read-tools.ts` (LEGACY_ONLY) | `chirality-read-mcp.test.ts`; `dependencies-register-contract.test.ts` | — |
| CLM-011/path_containment_hook | MAN:80 | `FE/src/lib/harness/tool-path-policy.ts` (LEGACY_ONLY) | `chirality-hooks.test.ts`; `permission-overlay.test.ts` | — |
| CLM-011/instruction_root_protection_hook | MAN:87 | `FE/src/lib/harness/tool-path-policy.ts` (LEGACY_ONLY) | `FE/src/__tests__/lib/harness-instruction-root.test.ts`; `FE/src/__tests__/scripts/verify-instruction-root-integrity.test.ts` | — |
| CLM-011/tool_result_budget | MAN:94 | `FE/src/lib/harness/tool-result-artifacts.ts` (LEGACY_ONLY) | `tool-evidence.test.ts`; `tool-result-artifacts.test.ts`; `sdk-message-mapper.test.ts`; `chirality-hooks.test.ts` | — |
| CLM-011/context_compaction_boundary | MAN:101 | `FE/src/lib/harness/sdk-message-mapper.ts` (LEGACY_ONLY) | `sdk-message-mapper.test.ts`; `session-events.test.ts` | — |
| CLM-011/subagent_governance_hook | MAN:108 | `FE/src/lib/harness/subagent-governance.ts` (LEGACY_ONLY) | `harness-subagent-governance.test.ts`; `agent-runtime-contract.test.ts` | — |
| (MAN only) domain_profile_validation | MAN:115 | `FE/src/lib/harness/mcp/domain-profile-registry.ts` (LEGACY_ONLY) | `domain-profile-registry.test.ts`; `contract-pins.test.ts` | Named by SoW CLM-013 only. |

Fifteen of the 16 Section 9 evidence files are `LEGACY_ONLY`. The exception is `session-manager.ts`, which is `LIVE`.

## 3. Completion and Reliance Basis — Epistemology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-014 | Specification heading | DOC_ONLY | — | — |
| CLM-015 | Scope | `REG` | `FE/src/__tests__/docs/reliance-boundary-register.test.ts` | DOC_ONLY; this unit names no runtime module. |
| CLM-016 | In Scope | `REG:37-54`, `:56-73`, `:75-105`, `:107-117` | same | DOC_ONLY; maps to REG sections. |
| CLM-017 | Out of Scope | DOC_ONLY | — | — |
| CLM-018 | Requirements RBR-001…025 | See §3a | See §3a | — |
| CLM-019 | Standards | `APPDOC/*.md` exist | — | DOC_ONLY. |
| CLM-020 | Verification | `REG:119-129` Cross-Check Record | `FE/src/__tests__/docs/reliance-boundary-register.test.ts` | REG:123 lists 13 categories. The REG test checks path existence (:20-31) and the PEC retirement wording (:33+). A schema-completeness assertion was not located in that test beyond those two `it` blocks (grep `it(` found 2). |
| CLM-021 | Documentation | `REG` exists; embedded matrix REG:56-73; test index REG:75-105; residual risks REG:107-117 | — | DOC_ONLY. |
| CLM-022 | Open Items | `REG:75-99` | — | OI-RBR-004 "PARTIAL" versus MAN:38/52 (both IDs present). |
| CLM-023 | D-APP-56 R5 P45 reconciliation | `MAN:52`, `:115` | — | Same text as CLM-013. |
| CLM-023/AC-001 | Conversion trace | DOC_ONLY | — | Front-matter SOW/OBJ refs at `DEL/ScopeOfWork.md:6-7`. |

### 3a. Requirements (CLM-018)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-018/RBR-001 | Register row fields | `REG:39` header | `FE/src/__tests__/docs/reliance-boundary-register.test.ts` | DOC_ONLY artifact check. The SCA-APP-003/004 addendum tables (REG:140, :186) use a different column set. |
| CLM-018/RBR-002 | No prompt-only P0 | `REG:41-54` column `PromptOnlyAllowed=NO` | — | DOC_ONLY. |
| CLM-018/RBR-003 | No SDK-default-only P0 | `REG:41-54` `SDKDefaultOnlyAllowed=NO` | — | DOC_ONLY. |
| CLM-018/RBR-004 | Engine port product-owned | `RT/packages/contracts/src/harness/agent-engine-port.ts:77,90` (LIVE) | `FE/src/__tests__/lib/engine-conformance.test.ts` | See RB-ENGINE. |
| CLM-018/RBR-005 | UIEvent vs HarnessEvent separation | `RT/packages/contracts/src/harness/event-schema.ts` (LIVE); `FE/src/lib/harness/harness-ui-bridge.ts` (LEGACY_ONLY; :17 mentions `providerMetadataAllowed`); `FE/src/lib/shell/harness-event-views.ts` (LIVE) | `FE/src/__tests__/lib/sdk-message-mapper.test.ts`; `FE/src/__tests__/lib/harness-ui-bridge.test.ts`; `FE/src/__tests__/lib/harness-event-views-codex.test.ts` | Codex payload translation is the subject of named question R4-Q5 (run addendum 7); this gather has not examined it. |
| CLM-018/RBR-006 | Append-only audit mirror | `RT/packages/core/src/session-store.ts` (LIVE, TOUCHED) | `RT/tests/native-message-replay.test.ts`; `FE/src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts` | See RB-AUDIT. |
| CLM-018/RBR-007 | Transcripts secondary | `FE/src/lib/harness/session-manager.ts` (LIVE) | `FE/src/__tests__/lib/transcript-replay.test.ts` | SoW says the tests "remain TBD"; `MAN:52` names 3 test files. |
| CLM-018/RBR-008 | `settingSources: []` | `FE/src/lib/harness/sdk-options-builder.ts:248` (LEGACY_ONLY) | `FE/src/__tests__/lib/sdk-options-builder.test.ts` | NO_CANDIDATE on the live path (see RB-SETTINGS). |
| CLM-018/RBR-009 | allow/deny/ask decisions | `permission-overlay.ts:14,327` `appendHarnessPermissionDecisionEvent` (LEGACY_ONLY); `RT/packages/daemon/src/codex-supervisor.ts:40` (LIVE, TOUCHED) | `permission-overlay.test.ts`; `RT/tests/codex-supervisor.test.ts` | — |
| CLM-018/RBR-010 | Deny overrides allows | `permission-overlay.ts:112` (LEGACY_ONLY) | `FE/src/__tests__/lib/permission-overlay.test.ts` | — |
| CLM-018/RBR-011 | allowedTools not a boundary | `FE/src/lib/harness/sdk-options-builder.ts` (LEGACY_ONLY) | `sdk-options-builder.test.ts` | — |
| CLM-018/RBR-012 | Containment / instruction-root / symlink | `tool-path-policy.ts:164` (LEGACY_ONLY); `RT/packages/core/src/runtime-service.ts:592-598` (LIVE) | `chirality-hooks.test.ts`; `harness-instruction-root.test.ts`; `verify-instruction-root-integrity.test.ts` | — |
| CLM-018/RBR-013 | Hooks fail closed | `chirality-hooks.ts:426` (LEGACY_ONLY) | `chirality-hooks.test.ts` | Live-path hook runner: NO_CANDIDATE (terms `PreToolUse`, `failClosed`, `createChiralityToolHooks` in `RT/packages`, `RT/tests`; only descriptive strings at `RT/packages/contracts/src/harness/tool-catalog.ts:62-69`). |
| CLM-018/RBR-014 | Bash denied by default | `tool-shell-policy.ts:7-9,157` (LEGACY_ONLY) | `FE/src/__tests__/lib/chirality-hooks.test.ts` | Superseded in text by CLM-013/023/060 (UPD-101). |
| CLM-018/RBR-015 | MCP tools through same policy | `FE/src/lib/harness/chirality-tool-bridge.ts`, `mcp/read-tools.ts` (LEGACY_ONLY); `RT/packages/daemon/src/application-tools.ts` (LIVE, TOUCHED) | `FE/src/__tests__/lib/chirality-tool-bridge.test.ts`; `chirality-read-mcp.test.ts`; `RT/tests/application-tools.test.ts` | — |
| CLM-018/RBR-016 | Subagent fail-closed | `subagent-governance.ts:196` (LEGACY_ONLY); `RT/packages/core/src/delegated-runtime.ts` (LIVE) | `harness-subagent-governance.test.ts`; `RT/tests/delegated-runtime.test.ts` | — |
| CLM-018/RBR-017 | `_STATUS.md` canonical, human gates | `FE/src/lib/lifecycle/transition.ts:26-29,55` (LIVE); `…/deliverable/status/transition/route.ts` (LIVE) | `FE/src/__tests__/lib/lifecycle-status.test.ts`; `FE/src/__tests__/lib/chirality-mutating-mcp.test.ts` | — |
| CLM-018/RBR-018 | No automated approval claims | DOC_ONLY (copy review) | — | REG:14-17 disclaimer. |
| CLM-018/RBR-019 | Redaction | `FE/src/lib/harness/run-logger.ts:81,95` (LIVE); `RT/packages/daemon/src/codex-app-server-client.ts:44` | `RT/tests/codex-app-server-client.test.ts`; `FE/src/__tests__/lib/tool-evidence.test.ts` | See RB-REDACTION regarding `sanitize.ts`. |
| CLM-018/RBR-020 | Fallback criteria row | `REG:54`, `:73` | — | DOC_ONLY. |
| CLM-018/RBR-021 | Corpus version recorded | `REG:9` | — | DOC_ONLY. REFERENCE_HASHES: CONTRACT/SPEC/PRD `Match=NO`. |
| CLM-018/RBR-022 | Drift distinction | `REG:116`, `:126` | — | DOC_ONLY. |
| CLM-018/RBR-023 | Acceptance evidence of no prompt/SDK-only | `REG:124-125` | — | DOC_ONLY. |
| CLM-018/RBR-024 | Paths kept current | `FE/src/__tests__/docs/reliance-boundary-register.test.ts:20-31` | same | The test regex covers backticked `frontend/…` paths only. REG cites `docs/…`, `projects/pec/docs/PRD.md` and a bare JSON filename outside that pattern. `_STATUS.md` history (2026-07-12) records UPD-097/RBR-025 path-existence coverage. |
| CLM-018/RBR-025 | Post-generation cross-check | `REG:119-129` | same | DOC_ONLY. |

## 4. Production and Verification Method — Praxeology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-024 | Procedure heading | DOC_ONLY | — | — |
| CLM-025 | Purpose | DOC_ONLY | — | Artifact-production procedure. |
| CLM-026 | Prerequisites | `DEL/_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv` exist | — | DOC_ONLY. `_STATUS.md` state is IN_PROGRESS, matching SoW:354. |
| CLM-027 | Steps heading | DOC_ONLY | — | — |
| CLM-028 | 1. Confirm Scope and Status | DOC_ONLY | — | — |
| CLM-029 | 2. Load Authoritative Sources | DOC_ONLY | — | Hash status: REFERENCE_HASHES `Match=NO` ×3. |
| CLM-030 | 3. Build Boundary Inventory | `REG:41-54` | — | DOC_ONLY. |
| CLM-031 | 4. Assign Enforcement Surfaces | `REG:56-73` | — | DOC_ONLY. |
| CLM-032 | 5. Attach Validation Evidence | `MAN`, `VAL:30-45` | See §2b | The step lists 13 IDs as existing and 2 as TBD. MAN has all 16. |
| CLM-033 | 6. Cross-Check Against Spec | `REG:119-129` | `FE/src/__tests__/docs/reliance-boundary-register.test.ts` | DOC_ONLY. |
| CLM-034 | 7. Produce Artifacts | `REG` | — | DOC_ONLY. |
| CLM-035 | 8. Review and Close | DOC_ONLY | — | No lifecycle transition is recorded beyond `_STATUS.md` history. |
| CLM-036 | Verification | `REG:119-129` | same | DOC_ONLY. |
| CLM-037 | Records | `REG`; `DEL/_run_records/` (15 entries) | — | DOC_ONLY. |
| CLM-038 | Remaining Blockers | DOC_ONLY | — | BLK-RBR-003 concerns SDK settings/transcripts; see RB-SETTINGS NO_CANDIDATE. |
| CLM-038/VER-001 | Deterministic validation | `VAL`; `MAN` | `FE/src/__tests__/docs/reliance-boundary-register.test.ts` | Tests were not run (no-test discipline). |

## 5. Governing Values and Decisions — Axiology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-039 | Guidance heading | DOC_ONLY | — | — |
| CLM-040 | Purpose | DOC_ONLY | — | SoW:564 says the product "privileges the Claude Agent SDK". The live engine per AGENTS.md is Codex App Server (`RT/packages/daemon/src/codex-supervisor.ts`, LIVE). |
| CLM-041 | Principles heading | DOC_ONLY | — | — |
| CLM-042 | 1. Product semantics not vendor mechanics | DOC_ONLY | — | — |
| CLM-043 | 2. P0 need enforceable surfaces | See §2a | — | — |
| CLM-044 | 3. Deny-first | `permission-overlay.ts:112` (LEGACY_ONLY) | `permission-overlay.test.ts` | — |
| CLM-045 | 4. Canonical audit Chirality-owned | `RT/packages/core/src/session-store.ts` (LIVE, TOUCHED) | `RT/tests/native-message-replay.test.ts` | — |
| CLM-046 | 5. Human authority not automatable | `FE/src/lib/lifecycle/transition.ts:26-29` (LIVE) | `lifecycle-status.test.ts` | — |
| CLM-047 | 6. Unknowns stay visible | DOC_ONLY | — | — |
| CLM-048 | Considerations heading | DOC_ONLY | — | — |
| CLM-049 | Source-State Handling | DOC_ONLY | — | REFERENCE_HASHES PRD `Match=NO`. |
| CLM-050 | Boundary Granularity | DOC_ONLY | — | — |
| CLM-051 | Current Implementation Surfaces | `FE/packages/harness-contract/src/agent-engine-port.ts` exists (2-line deprecated re-export; no REACH row); `FE/src/lib/harness/agent-runtime-contract.ts` exists (LEGACY_ONLY); `turn-engine.ts` exists (LEGACY_ONLY); `sdk-options-builder.ts` exists (LEGACY_ONLY); `permission-overlay.ts` exists (LEGACY_ONLY); `chirality-hooks.ts` exists (LEGACY_ONLY); `subagent-governance.ts` exists (LEGACY_ONLY) | `engine-conformance.test.ts`; `turn-engine.test.ts`; `sdk-options-builder.test.ts`; `permission-overlay.test.ts`; `chirality-hooks.test.ts`; `harness-subagent-governance.test.ts` | All 7 paths exist; none is MISSING. `RuntimeEngineContract` is defined at `RT/packages/contracts/src/harness/agent-engine-port.ts:90`, not at the cited `agent-runtime-contract.ts`. |
| CLM-052 | Residual Risk Topics | `REG:107-117` | — | DOC_ONLY. |
| CLM-053 | Trade-offs | DOC_ONLY | — | — |
| CLM-054 | Examples heading | DOC_ONLY | — | — |
| CLM-055 | Example row (RB-SETTINGS) | `sdk-options-builder.ts:248` (LEGACY_ONLY) | `sdk-options-builder.test.ts` | Illustrative. |
| CLM-056 | Example incomplete row | `subagent-governance.ts:196` (LEGACY_ONLY) | `harness-subagent-governance.test.ts` | Illustrative. |
| CLM-057 | Closed Source-State Note | DOC_ONLY | — | — |
| CLM-058 | Generated Artifact Note | `REG` (git: last touched `23b3879b3` 2026-09-12, D-GOV-43 A2 tranche) | — | DOC_ONLY. |
| CLM-059 | Assumptions and TBDs | DOC_ONLY | — | TBD-RBR-003 has the same MAN:38/52 note as CLM-011. |
| CLM-060 | D-APP-56 R5 P45 reconciliation | `MAN:52`, `:115`; `tool-shell-policy.ts` (LEGACY_ONLY) | — | Same text as CLM-013. |

## 6. Status Remaining

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| REM-1 | PEC v2 shared-runtime client seam (DEL-07-05) | `FE/src/lib/harness/mcp/pec-bridge-client.ts` (LEGACY_ONLY); `REG:148-178` RB-PEC-ADAPTER RETIRED | `FE/src/__tests__/docs/reliance-boundary-register.test.ts:33+` (retired-PEC wording) | The gating evidence belongs to the PEC project and was not read (out of bounds). `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md` exists. REG:171 records D-GOV-43 superseding D-GOV-20 items 2–4 on the App path. |
