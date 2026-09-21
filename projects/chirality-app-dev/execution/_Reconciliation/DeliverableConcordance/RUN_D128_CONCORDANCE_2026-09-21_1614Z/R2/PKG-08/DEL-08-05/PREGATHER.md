# PREGATHER — DEL-08-05 Subagent Child Run Records and Artifacts

- **Run:** RUN_D128_CONCORDANCE_2026-09-21_1614Z (R2, PKG-08). Pre-gather TASK. Evidence locations only: no dispositions, alignment judgments or CauseTags.
- **Basis:** frozen tree at `00115c719`. All paths are repo-relative. Line numbers are taken at the frozen basis.
- **Deliverable folder:** `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/`. ScopeOfWork.md is 38,510 B and _STATUS.md is 5,080 B.
- **Units:** 38 indexed in CLAIM_INDEX: 37 CLM (CLM-001..036 plus CLM-037) and 1 REM (REM-1). A separate row, `DEL-02-02#REM-1`, names DEL-08-05-V3-01 as its gate. It belongs to DEL-02-02 and is not covered here.
- **Method:**
  1. Summarized HINTS/DEL-08-05.csv (851 rows) with python by ClaimKey, path and token. Most hint paths are unrelated token collisions: `api-key-ipc.ts`, `attachment-picker.ts`, `harness-section9-manifest.json` and `deliverables-route.test.ts` match on generic tokens such as `denied`, `docs/*.md` and `DeliverableID`.
  2. Grepped `frontend/src`, `frontend/electron`, `chirality-runtime/packages/*/src` and `chirality-runtime/tests` for the tokens listed below.
  3. Looked up REACH for every cited module in `EVIDENCE_PACK/REACHABILITY.csv`.
  4. Checked cited lines against the `EVIDENCE_PACK/TOUCHED_PATHS.csv` ranges.
  5. Mapped `EVIDENCE_PACK/DECISION_HITS.csv` rows for DEL-08-05 to SoW line ranges.
  - Search tokens: `ChildRunRecord`, `childRunId`, `subagent.(started|progress|completed|failed)`, `artifacts/subagents`, `16 * 1024|512 * 1024`, `parentPersona`, `outputArtifactPath`, `instruction-asserted`, `AgentRun`, `nativeDescendant|nativeChild`, `events.jsonl`, `redact`, `malformed`, `delegate_agent`, `adapterAgentId|adapterTranscriptKey`.
- **Counts:**
  - 22 code modules cited: 7 `REACH=LIVE` App, 12 `REACH=LIVE` runtime and 9 `REACH=LEGACY_ONLY` App.
  - 0 cited lines fall in a TOUCHED range, so no `TOUCHED(<commit>)` marks. `codex-supervisor.ts` and `session-store.ts` are touched files, but the cited lines lie outside their touched ranges (see cross-cutting).
  - 12 test files cited.
  - 14 decision IDs in DECISION_HITS for DEL-08-05.
  - 8 units are `NO_CANDIDATES`.
- **Recurrent anchors.** Units below cite these by their tag.
  - **[A-CONTRACT]** `projects/chirality-app-dev/frontend/src/lib/harness/agent-runtime-contract.ts` REACH=LEGACY_ONLY
    - :10 `AGENT_SUBAGENT_CONTRACT_VERSION`
    - :12-17 `CHILD_RUN_EVENT_TYPES`
    - :19-25 `AGENT_SUBAGENT_PREREQUISITE_POSTURE` (`executableDelegation: 'blocked'`)
    - :27-33 `ChildRunStatus`
    - :62-69 `ChildRunAdapterMetadata`
    - :71-85 `ChildRunRecord`
    - :138 `createDelegationChildRunRecord`
    - :185 `createAdapterObservedChildRunRecord`
    - :228 `providerNeutralChildRunRecord`
    - :235 `childRunRecordToEventData`
    - :242 `validateChildRunRecord`
  - **[A-MAPPER]** `projects/chirality-app-dev/frontend/src/lib/harness/sdk-message-mapper.ts` REACH=LEGACY_ONLY
    - :206 `createChildRunRecordForTaskMessage`
    - :231 and :342 `adapterSessionId`
    - :243 `childRunEventData`
    - :1065-1163 emission of `subagent.started`, `subagent.progress`, `subagent.completed` and `subagent.failed`
    - :1210-1230 child-output artifact linkage (`outputArtifactPath: artifactMetadata.artifactRelativePath`)
  - **[A-ARTIFACT]** `projects/chirality-app-dev/frontend/src/lib/harness/tool-result-artifacts.ts` REACH=LEGACY_ONLY
    - :21 `ChildOutputArtifactMetadata`
    - :38 `CHILD_OUTPUT_INLINE_BYTE_LIMIT = 16 * 1024`
    - :39 `CHILD_OUTPUT_ARTIFACT_BYTE_LIMIT = 512 * 1024`
    - :141 `persistChildOutputArtifact`
    - :177-199 inline/truncate/preview
    - :209 `'subagents'` path segment
  - **[A-MANAGED]** `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts` REACH=LEGACY_ONLY
    - :66-92 `declaredContext` and `writeTargets` fields
    - :366-384 brief render (`DeclaredContext`, `AllowedWriteTargets`)
    - :591-741 launch containment and persistence
    - :768 `coordinationRunRoot`
    - :806 `reportCoordinationNotice`
    - :835 `sendAgentUpdate`
    - :975 `acknowledgeAgentUpdate`
  - **[A-SESSEV]** `projects/chirality-app-dev/frontend/src/lib/harness/session-events.ts` REACH=LEGACY_ONLY
    - :11 `events.jsonl` path
    - :26-83 replay with `malformedLineCount`
  - **[R-EVSCHEMA]** `projects/chirality-runtime/packages/contracts/src/harness/event-schema.ts` REACH=LIVE
    - :1 `HARNESS_EVENT_TYPES`, with :40-43 the `subagent.*` entries
    - :56-61 `HarnessEvent` (`schemaVersion: 1`, `eventId`, `parentEventId?`)
  - **[R-STORE]** `projects/chirality-runtime/packages/core/src/session-store.ts` REACH=LIVE
    - :654 `appendEvent`, with :662 `eventId: randomUUID()`
    - :819-820 duplicate `eventId` guard
    - :825 `replay`
    - :829-844 `replayDetailed` (`malformedLineCount`)
    - :1126 `events.jsonl` path
  - **[R-AGENTRUN]** `projects/chirality-runtime/packages/core/src/agent1-run-coordinator.ts` REACH=LIVE
    - :62-104 `AgentRunRecord` (`schemaVersion: "chirality.agent-run/v1"`, `sealedBrief`, `briefHash`, `child.sealedBriefHash`, `returnHash`, `evidenceReference`, `status`, `completedAt?`)
    - :105 `GovernedAgent1RunCoordinator`
    - :294-317 child `parentSessionId` and sealed brief
    - :905 `persistAgentRun`
    - :914 `persistAgentProgress`
    - :918-926 write under `_Coordination/AgentRuns/runtime/<runId>/`
  - **[R-ROLEPOL]** `projects/chirality-runtime/packages/core/src/role-policy.ts` REACH=LIVE
    - :13-18 `RolePolicyInput.nativeDescendant`
    - :20 `createRolePolicyEvidence`
    - :34-35 `evidencePosture: "instruction-asserted"` and `nonDelegationEvidence`
    - :38 `policyDigest`
    - :39 `actual` (adapter, provider, model)
    - :43 `nativeDescendant`
  - **[R-NATIVE]** Native-child modules, each REACH=LIVE:
    - `projects/chirality-runtime/packages/contracts/src/engine.ts:22` `NativeChildSelectedRole`, and :31 `nativeChild` association
    - `projects/chirality-runtime/packages/contracts/src/delegated.ts:86-92` `DelegatedRoleEvidence` (`evidencePosture: "instruction-asserted"`), and :247 callback `nativeChild` (`associationId`, `parentThreadId`, `parentTurnId`, `selectedRole`, `inheritedToolsDigest`)
    - `projects/chirality-runtime/packages/core/src/runtime-method-service.ts:454-469` `native-child.method-loaded` history
    - `projects/chirality-runtime/packages/core/src/instruction-basis-store.ts:129` and :482 `native-child.method-loaded`
    - `projects/chirality-runtime/packages/core/src/delegated-runtime.ts:321` `createRolePolicyEvidence`, with delegationPolicy "native descent does not assign a role"
    - `projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts:277-287` `collabAgentToolCall` and `agentThreadIds` mapped to `tool.*` and `codex.notification`, not to `subagent.*`
    - `projects/chirality-runtime/packages/daemon/src/codex-supervisor.ts:280-309` loaded-descendant tree, :518-519 `childThreads` parent map, and :590-591 `chirality/nativeChildren/observationEnded`
  - **[F-VIEWS]** Live UI consumers of `subagent.*`:
    - `projects/chirality-app-dev/frontend/src/lib/shell/harness-event-views.ts` REACH=LIVE: :125-128 status map, :501 `deriveSubagentActivity`, :512 and :558 native `subagent.progress` and `agentThreadId` handling
    - `projects/chirality-app-dev/frontend/src/lib/shell/turn-activity.ts:73` REACH=LIVE
    - `projects/chirality-app-dev/frontend/src/components/shell/subagent-stream-view.tsx:26` `outputArtifactPath` REACH=LIVE
    - `projects/chirality-app-dev/frontend/src/components/woven-dialogue/activity-shelf.tsx:174-175` REACH=LIVE

## DEL-08-05#CLM-001 — Datasheet heading
- Gist: Heading only. Titles the datasheet for DEL-08-05.
- Code: NO_CANDIDATES. HINTS has an empty token row, and the claim has no content to search.
- Tests: NO_CANDIDATES.
- Decisions: none.

## DEL-08-05#CLM-002 — Identification
- Gist: Identification table: IDs, names, type DATA_MODEL_CHANGE, envelope M, ResponsibleParty TBD, SOW-063, OBJ-003 and OBJ-007.
- Code: NO_CANDIDATES. The HINTS hits on `DeliverableID`, `PackageID` and similar are generic column-name collisions in deliverable-contract tests and scripts. The claim is documentary.
- Tests: NO_CANDIDATES.
- Decisions: none in DECISION_HITS for SoW lines 26-43.

## DEL-08-05#CLM-003 — Attributes
- Gist: Scope includes managed-child lifecycle, parent and declared-context linkage, `ChildRunRecord` target, `HarnessEvent` store at `.chirality/sessions/<id>/events.jsonl`, and `artifacts/subagents/` with a 16/512 KiB policy.
- Code:
  - [A-CONTRACT] :71-85, REACH=LEGACY_ONLY
  - [A-ARTIFACT] :38-39 and :209, REACH=LEGACY_ONLY
  - [A-SESSEV] :11, REACH=LEGACY_ONLY
  - [A-MANAGED] :66-92 and :806-975, REACH=LEGACY_ONLY
  - [R-STORE] :654 and :1126, REACH=LIVE
  - [R-EVSCHEMA] :40-43, REACH=LIVE
  - No LIVE runtime module references `ChildRunRecord` or `artifacts/subagents`. The grep found no hits outside the modules above.
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` :: "creates provider-neutral child-run preflight records from governance decisions"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/tool-result-artifacts.test.ts` :: "persists over-inline child output summaries with redacted linkage metadata"
- Decisions: D-APP-40 (SoW:52 and :56), D-APP-56 (:55 and :57), D-APP-68 (:51 and :55-58). All are RULED.

## DEL-08-05#CLM-004 — Conditions
- Gist:
  - Delegation fails closed, children do not expand capabilities, and parent-child records are required when execution is enabled.
  - Events are redacted, JSONL replay tolerates malformed lines, and SDK transcripts are secondary.
  - Pipeline run records remain retired, and the PRD is current under D-APP-38.
- Code:
  - Fail-closed:
    - [A-CONTRACT] :19-25 posture and :138-180 (denied path), REACH=LEGACY_ONLY
    - [A-MANAGED] :237-283 and :591-638, REACH=LEGACY_ONLY
  - Malformed replay:
    - [A-SESSEV] :68-83, REACH=LEGACY_ONLY
    - [R-STORE] :829-844, REACH=LIVE
  - Redaction:
    - `projects/chirality-app-dev/frontend/src/lib/harness/run-logger.ts:81` `redactConfiguredApiKeys` and :95 `redactJsonLike`, REACH=LIVE
    - [A-ARTIFACT] redacted persistence, REACH=LEGACY_ONLY
  - SDK transcript as secondary: [A-CONTRACT] :62-69 `adapterTranscriptKey`, REACH=LEGACY_ONLY
  - Retired scope: no `PipelineRun` or unified run-record symbol found (grep `KG-012|pipeline run|PipelineRun`, no hits in lib or runtime src).
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` :: "records denied delegation without queueing execution"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/session-events.test.ts` :: "redacts raw imported JSONL records at replay time"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/managed-delegation.test.ts` :: "fails closed on missing governance metadata and capability inheritance"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts` :: "does not turn Pipeline presentation state into delegation authority"
- Decisions: D-APP-38 (SoW:75), RULED.

## DEL-08-05#CLM-005 — Construction heading
- Gist: Heading only.
- Code: NO_CANDIDATES. HINTS has an empty token row.
- Tests: NO_CANDIDATES.
- Decisions: none.

## DEL-08-05#CLM-006 — Target `ChildRunRecord` fields
- Gist: Field table: `childRunId`, parent session, turn and persona, `agentName`, `adapter.adapterAgentId`, `projectRoot`, a six-value `status`, `mode`, `capabilityPolicy`, `governance`, `contractVersion`, `outputArtifactPath`.
- Code:
  - [A-CONTRACT] :71-85 `ChildRunRecord`, REACH=LEGACY_ONLY
  - [A-CONTRACT] :27-33 status union, REACH=LEGACY_ONLY
  - [A-CONTRACT] :62-69 adapter metadata, REACH=LEGACY_ONLY
  - [A-CONTRACT] :10 contract version constant, REACH=LEGACY_ONLY
  - Compare [R-AGENTRUN] :62-104 `AgentRunRecord` (REACH=LIVE). It is a different record shape: `status` is `running|completed|failed|interrupted` and it has `completedAt?`.
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` :: "creates provider-neutral child-run preflight records from governance decisions"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` :: "keeps adapter-specific child-run identifiers under adapter metadata"
- Decisions: D-APP-40 (SoW:89), D-APP-56 (SoW:97-100). Both RULED.

## DEL-08-05#CLM-007 — Related `HarnessEvent` fields
- Gist: Envelope fields `schemaVersion` 1, `eventId`, `sessionId`, optional `turnId` and `parentEventId`, `timestamp`, `type` including `subagent.*`, and secret-free `data`.
- Code:
  - [R-EVSCHEMA] :56-61 and :40-43, REACH=LIVE
  - [R-STORE] :654-662, REACH=LIVE
  - `projects/chirality-app-dev/frontend/src/lib/harness/event-factory.ts` (HINTS), REACH=LEGACY_ONLY
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/session-events.test.ts` :: "keeps canonical HarnessEvent types provider-neutral"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/session-events.test.ts` :: "appends and replays HarnessEvent JSONL records"
- Decisions: none in DECISION_HITS for SoW lines 104-118.

## DEL-08-05#CLM-008 — References
- Gist: Lists the DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN and PRD documents plus a decomposition-method file given as an absolute user-home path.
- Code: NO_CANDIDATES. The unit is documentary; the hits are doc-name tokens in manifests and tests.
- Tests: NO_CANDIDATES.
- Decisions: D-APP-38 (SoW:129), RULED. Also see `EVIDENCE_PACK/REFERENCE_HASHES.csv` rows for DEL-08-05.

## DEL-08-05#CLM-009 — D-APP-56 R5 P45 reconciliation
- Gist: UPD-138: implemented fields drop `completedAt` and add `mode`, `capabilityPolicy`, `governance` and `contractVersion`, with no invented timestamps. UPD-139 marks DEP-08-05-006 satisfied.
- Code:
  - [A-CONTRACT] :71-85, REACH=LEGACY_ONLY. There is no `completedAt` in `ChildRunRecord`.
  - Compare [R-AGENTRUN] :102 `completedAt?` on `AgentRunRecord`, REACH=LIVE.
- Tests: `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` (whole file).
- Decisions: D-APP-56 (SoW:133 and :135), RULED.

## DEL-08-05#CLM-037 — Applied decomposition v3 carrier assignment
- Gist: Row text requires reconstructible checkout records for managed and native descendants, kept distinct. The records carry parentage, lineage, role state, adapter, provider and model, digests, approvals, status, artifacts, cleanup, and `instruction-asserted` calibration.
- Code:
  - Managed: [R-AGENTRUN] :62-104 and :905-926, REACH=LIVE. The records are written under `execution/_Coordination/AgentRuns/runtime/<runId>/` with `run.json` and `progress-*.json`.
  - Role, policy and attribution: [R-ROLEPOL] :20-43, REACH=LIVE.
  - Native descendants: [R-NATIVE], REACH=LIVE throughout:
    - `engine.ts:22` and :31
    - `delegated.ts:86-92` and :247
    - `runtime-method-service.ts:454-469`
    - `codex-supervisor.ts:280-309`, :518-519 and :590
  - Earlier managed-delegation graph: [A-MANAGED], REACH=LEGACY_ONLY.
  - No module named for "native-descendant evidence record" persistence or a reconstruction fixture was found. Grep for `native-descendant|nativeDescendant` returned only role-policy.
- Tests:
  - `projects/chirality-runtime/tests/role-policy.test.ts` :: "does not infer role from native descent or persist model assignment in digest"
  - `projects/chirality-runtime/tests/agent1-run.test.ts` :: "runs exactly one read-only Agent 2, records parentage/model epoch, and requires review"
  - `projects/chirality-runtime/tests/agent1-run.test.ts` :: "interrupts an active Agent 2 child and preserves canonical child interruption evidence"
  - `projects/chirality-runtime/tests/stagec-native-child-history.test.ts` :: "records configured-child activation under the child association without changing parent selection/history"
  - `projects/chirality-runtime/tests/native-event-adapter.test.ts` :: "retains message/summary/checklist updates and actual child identity independently of completed collaboration calls"
- Decisions: none in DECISION_HITS for SoW lines 139-150. Related: D-GOV-35 (ROOT, at `_STATUS.md:14`) and D-APP-117 (register row 133, AWAITING_RULING, names DEL-08-05 persistence).

## DEL-08-05#CLM-010 — Specification heading
- Gist: Heading only.
- Code: NO_CANDIDATES. HINTS has an empty token row.
- Tests: NO_CANDIDATES.
- Decisions: none.

## DEL-08-05#CLM-011 — Scope
- Gist: Covers child records and artifact references. Admission belongs to DEL-08-04. Retired pipeline records, dependency graphs, locks and staleness are excluded.
- Code: NO_CANDIDATES. The claim is boundary prose; searches for `ChildRunRecord` and `PipelineRun` are as in CLM-004. For boundary context: admission is in `projects/chirality-app-dev/frontend/src/lib/harness/subagent-governance.ts` and `subagent-bridge.ts`, both REACH=LEGACY_ONLY.
- Tests: `projects/chirality-app-dev/frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts` (boundary context only).
- Decisions: none in DECISION_HITS for SoW lines 158-165.

## DEL-08-05#CLM-012 — Requirements REQ-001..013
- Gist: Thirteen requirements:
  - record fields, status enum and optional adapter fields
  - `subagent.*` events, `HarnessEvent` shape, JSONL append with unique IDs
  - 16/512 KiB artifact policy and artifact metadata, redaction
  - SDK metadata kept secondary, no retired scope
  - denied-after-allocation record, managed lineage and coordination replay
- Code:
  - REQ-001..003, REQ-012: [A-CONTRACT] :27-85 and :138-242, REACH=LEGACY_ONLY
  - REQ-004: [A-MAPPER] :1065-1163, REACH=LEGACY_ONLY; [R-EVSCHEMA] :40-43 (type enum only), REACH=LIVE; [F-VIEWS] consumers, REACH=LIVE
  - REQ-005, REQ-006: [R-STORE] :654-662 and :819-820, REACH=LIVE; [A-SESSEV], REACH=LEGACY_ONLY
  - REQ-007, REQ-008: [A-ARTIFACT] :21-39 and :141-234, REACH=LEGACY_ONLY
  - REQ-009: `run-logger.ts:81-95`, REACH=LIVE; [A-ARTIFACT] redaction, REACH=LEGACY_ONLY
  - REQ-010: [A-CONTRACT] :62-69, and [A-MAPPER] :231 and :342, REACH=LEGACY_ONLY
  - REQ-013: [A-MANAGED] :591-741 and :806-975, REACH=LEGACY_ONLY; managed Agent-2 child parentage in [R-AGENTRUN] :294-317, REACH=LIVE
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` (all 5 cases)
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/tool-result-artifacts.test.ts` :: "skips persistence for inline-sized child output summaries"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/tool-result-artifacts.test.ts` :: "truncates child output summaries that exceed the artifact budget"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts` :: "embeds adapter-observed child-run records in SDK task lifecycle events"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts` :: "materializes over-inline child output summaries as redacted session artifacts"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/managed-delegation.test.ts` :: "persists child→parent notices and parent→child updates with acknowledgments"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/session-events.test.ts` :: "appends and replays HarnessEvent JSONL records"
- Decisions: D-APP-40 (SoW:173, :175, :176, :177, :184), D-APP-56 (:179), D-APP-68 (:179, :185). All RULED.

## DEL-08-05#CLM-013 — Standards
- Gist: Applicable standards: `HarnessEvent` schema, `ChildRunRecord` target, the `events.jsonl` audit mirror, the child-output policy (distinct from DEL-05-05 `descriptor.resultBudget`), and subagent governance invariants.
- Code:
  - [R-EVSCHEMA], REACH=LIVE
  - [A-CONTRACT], REACH=LEGACY_ONLY
  - [R-STORE] :1126, REACH=LIVE
  - [A-ARTIFACT] :38-39 versus :58-93 `persistToolResultArtifact` (the ordinary budget), REACH=LEGACY_ONLY
  - `projects/chirality-app-dev/frontend/src/lib/harness/chirality-tool-bridge.ts` (`resultBudget` hits), REACH=LEGACY_ONLY
- Tests: `projects/chirality-app-dev/frontend/src/__tests__/lib/tool-result-artifacts.test.ts` :: "truncates results that exceed the artifact budget" (ordinary), plus the child cases listed under CLM-012.
- Decisions: none in DECISION_HITS for SoW lines 188-199.

## DEL-08-05#CLM-014 — Verification (spec)
- Gist: Maps REQ groups to type, schema, event-writer, replay, artifact-store, redaction, replay-boundary, scope-review, denied-boundary and managed-replay test approaches.
- Code: see CLM-012.
- Tests:
  - REQ-012 denied-before versus denied-after allocation: `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` :: "records denied delegation without queueing execution". No separately named denied-after-allocation fixture was found (grep `denied` in agent-runtime-contract and managed-delegation tests).
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-event-views.test.ts` :: "collapses the subagent lifecycle into one row per childRunId"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/session-events.test.ts` :: "summarizes full replay coverage and preserves artifact references without raw secrets"
- Decisions: D-APP-40 (SoW:213), RULED.

## DEL-08-05#CLM-015 — Pass 3 disposition evidence (spec)
- Gist: Pass-3 items C-001 (D-APP-38), F-001 and F-002 (D-APP-40), X-001 (bounded payload), E-001 (cross-disposed to `Procedure.md`), E-002 (no separate terminal event names).
- Code: NO_CANDIDATES. The unit is documentary provenance. `Procedure.md` is not present in the deliverable folder listing at the frozen basis (files: Assessment_INSP-03, Dependencies.csv, MEMORY.md, ScopeOfWork.md, _CONTEXT, _DEPENDENCIES, _REFERENCES, _SEMANTIC, _SEMANTIC_LENSING, _STATUS, _run_records).
- Tests: NO_CANDIDATES.
- Decisions: D-APP-38 (SoW:223), D-APP-40 (:224, :225). Both RULED.

## DEL-08-05#CLM-016 — Documentation
- Gist: Anticipated artifacts: parent-child event records, artifact paths, replay fixtures, `ChildRunRecord` types, `subagent.started`/`subagent.completed` replay tests, and lineage-linkage tests.
- Code: [A-CONTRACT], [A-MAPPER] and [A-ARTIFACT], all REACH=LEGACY_ONLY.
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts` :: "maps SDK tool, hook, status, and subagent messages into expanded HarnessEvent categories"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-event-views.test.ts` :: "collapses the subagent lifecycle into one row per childRunId"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/managed-delegation.test.ts` :: "persists child→parent notices and parent→child updates with acknowledgments"
  - `projects/chirality-app-dev/frontend/src/__tests__/components/activity-view-presentation.test.tsx` (hits on `subagent.*`)
- Decisions: none in DECISION_HITS for SoW lines 231-243.

## DEL-08-05#CLM-017 — Conflict table (spec)
- Gist: C-001, the PRD source state, is resolved by D-APP-38. The denied-allocation conflict was resolved by D-APP-40, ruled 2026-06-21.
- Code: NO_CANDIDATES. The unit is documentary.
- Tests: NO_CANDIDATES.
- Decisions: D-APP-38 (SoW:251), D-APP-40 (:252). Both RULED.

## DEL-08-05#CLM-018 — D-APP-56 child-output amendment, with REQ-001..004 and AC-001..002 (v3)
- Gist: `artifacts/subagents/` is assigned here with 16 KiB inline and 512 KiB artifact limits. The v3 REQ-001..004 and AC-001..002 cover managed and native descendant record classes, `instruction-asserted`, and non-authoritative daemon state.
- Code:
  - 16/512 KiB: [A-ARTIFACT] :38-39 and :177-209, REACH=LEGACY_ONLY. The grep found no LIVE runtime module with child-output limits; `projects/chirality-runtime/packages/client/src/client.ts` and `contracts/src/harness/tool-descriptor.ts` matched `16 * 1024|512 * 1024` for other purposes and were not inspected further.
  - v3 REQ-001..004: [R-AGENTRUN] :62-104 (managed, sealed brief, hashes), [R-ROLEPOL] :20-43 (`instruction-asserted`, digest, actual attribution, `nativeDescendant`), [R-NATIVE]. All REACH=LIVE.
  - `projects/chirality-app-dev/frontend/src/lib/consent/hosted-engine-consent-port.ts:191` `INSTRUCTION_ASSERTED_EVIDENCE_LABEL`, REACH=LIVE
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/tool-result-artifacts.test.ts` (child cases :106, :122, :167)
  - `projects/chirality-runtime/tests/role-policy.test.ts` (3 cases)
  - `projects/chirality-runtime/tests/agent1-run.test.ts` :: "runs exactly one read-only Agent 2, records parentage/model epoch, and requires review"
  - `projects/chirality-app-dev/frontend/src/__tests__/components/account-consent-settings-states.test.ts` (`instruction-asserted` hits)
- Decisions: D-APP-56 (SoW:255, :257), RULED.

## DEL-08-05#CLM-019 — Procedure heading
- Gist: Heading only.
- Code: NO_CANDIDATES. HINTS has an empty token row.
- Tests: NO_CANDIDATES.
- Decisions: none.

## DEL-08-05#CLM-020 — Purpose (procedure)
- Gist: Operational steps for producing and validating child-run records and artifact references for governed Type 2 execution.
- Code: NO_CANDIDATES. HINTS has an empty token row, and the unit is purpose prose.
- Tests: NO_CANDIDATES.
- Decisions: none.

## DEL-08-05#CLM-021 — Prerequisites
- Gist: Prerequisites: source corpus, DEL-08-04 as an ASSUMPTION edge, `HarnessEvent` targets, artifact policy source, and the D-APP-40 denied ruling.
- Code: NO_CANDIDATES. The unit is documentary. For the DEL-08-04 edge see `Dependencies.csv:5` (DEP-08-05-004) and :12 (DEP-08-05-011), both naming DEL-08-04 as UPSTREAM.
- Tests: NO_CANDIDATES.
- Decisions: D-APP-38 (SoW:288), D-APP-40 (:292). Both RULED.

## DEL-08-05#CLM-022 — Steps 1-15
- Gist: Procedure:
  - define the record and its status enum
  - link the parent and brief
  - capture metadata without timestamps
  - emit the four `subagent.*` events and apply the 16/512 KiB policy
  - set `outputArtifactPath`, redact, keep SDK metadata secondary
  - add replay and denied fixtures, check retired scope, verify lineage replay
- Code: as CLM-012. Step 4 sealed-brief linkage: [A-MANAGED] :366-384 and :688-741, REACH=LEGACY_ONLY; [R-AGENTRUN] :294-317, REACH=LIVE.
- Tests: as CLM-012 and CLM-014.
- Decisions: D-APP-40 (SoW:305, :311), RULED.

## DEL-08-05#CLM-023 — Verification (procedure)
- Gist: Check table covering required fields, status enum, envelope, append-only JSONL, 16/512 KiB references, artifact metadata fields, redaction, replay reconstruction, terminal status, scope boundary and managed lineage.
- Code: as CLM-012.
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/tool-result-artifacts.test.ts` :: "persists over-inline child output summaries with redacted linkage metadata" (metadata fields)
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/session-events.test.ts` :: "replays interleaved tool artifact events in append order with checksum metadata"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` :: "flags completed child runs that lack output artifact references"
- Decisions: none in DECISION_HITS for SoW lines 316-333.

## DEL-08-05#CLM-024 — Pass 3 disposition evidence (procedure)
- Gist: F-001, F-002, E-001 and E-002 are incorporated into the Prerequisites, Step 13, the Verification table and Step 7.
- Code: NO_CANDIDATES. The unit is documentary provenance.
- Tests: NO_CANDIDATES.
- Decisions: D-APP-40 (SoW:341, :342), RULED.

## DEL-08-05#CLM-025 — Records, VER-001 and VER-002
- Gist: Record set: `ChildRunRecord` type and tests, lifecycle fixtures, artifact-path fixtures, replay fixtures, and the D-APP-40 record. VER-001 is the legacy source check set; VER-002 is managed and native replay and reconstruction.
- Code: VER-001 is [A-CONTRACT], [A-MAPPER], [A-ARTIFACT] and [A-SESSEV], all REACH=LEGACY_ONLY. VER-002 is [R-AGENTRUN], [R-ROLEPOL] and [R-NATIVE], all REACH=LIVE.
- Tests: VER-001 uses the frontend tests listed in CLM-012. VER-002 uses `projects/chirality-runtime/tests/agent1-run.test.ts`, `role-policy.test.ts`, `stagec-native-child-history.test.ts` and `native-event-adapter.test.ts`. No test combining managed and native reconstruction was found (grep `native` together with `agent-run` in `chirality-runtime/tests`).
- Decisions: D-APP-40 (SoW:355), RULED. The D-APP-40 ruling record is at `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md:55`.

## DEL-08-05#CLM-026 — Guidance heading
- Gist: Heading only.
- Code: NO_CANDIDATES. HINTS has an empty token row.
- Tests: NO_CANDIDATES.
- Decisions: none.

## DEL-08-05#CLM-027 — Purpose (guidance)
- Gist: Governed subagent execution should be replayable and auditable without expanding authority, through a durable record of child, linkage, status and artifact.
- Code: NO_CANDIDATES. HINTS has an empty token row, and the unit is value prose.
- Tests: NO_CANDIDATES.
- Decisions: none.

## DEL-08-05#CLM-028 — Principles
- Gist: Chirality events stay canonical, the gate is kept separate from persistence, fail-closed outcomes stay visible, references are stored rather than payloads, retired scope is not reintroduced, and secrets and professional-approval claims are excluded.
- Code:
  - [R-STORE], REACH=LIVE
  - [A-CONTRACT] :138-180, REACH=LEGACY_ONLY
  - [A-ARTIFACT], REACH=LEGACY_ONLY
  - `run-logger.ts:81-95`, REACH=LIVE
- Tests: as CLM-004.
- Decisions: D-APP-40 (SoW:382), D-APP-56 (:383), D-APP-68 (:383). All RULED.

## DEL-08-05#CLM-029 — Considerations
- Gist: Keep the record small, keep `childRunId` distinct from `eventId`, keep `parentTurnId` optional, never synthesize SDK or model fields, make status child-scoped, use relative paths, keep 16/512 KiB ownership here, and include four-status fixtures.
- Code:
  - [A-CONTRACT] :103-129 `createStableChildRunId` (`child_<sha16>`), REACH=LEGACY_ONLY
  - [A-MAPPER] :195-243, REACH=LEGACY_ONLY
  - [A-ARTIFACT] :209 relative path segment, REACH=LEGACY_ONLY
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-event-views.test.ts` :: "collapses a completion that lacks childRunId onto the running row via taskId"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` (all 5 cases)
- Decisions: D-APP-40 (SoW:400), RULED.

## DEL-08-05#CLM-030 — Trade-offs
- Gist: Trade-off table covering denial recording, SDK metadata depth, and inline versus artifact output storage.
- Code: NO_CANDIDATES. The unit is option analysis. The `tool.permission` hits are in tests and proofs only.
- Tests: NO_CANDIDATES.
- Decisions: D-APP-40 (SoW:410), RULED.

## DEL-08-05#CLM-031 — Examples heading
- Gist: Heading only.
- Code: NO_CANDIDATES. HINTS has an empty token row.
- Tests: NO_CANDIDATES.
- Decisions: none.

## DEL-08-05#CLM-032 — Example `ChildRunRecord`
- Gist: JSON example with the full field set: `mode: workspaceWrite`, `status: completed`, empty policy and governance objects, `contractVersion "1"`, and an artifact path under `artifacts/subagents/child_123/`.
- Code:
  - [A-CONTRACT] :10 (`contractVersion` is numeric `1 as const`) and :71-85, REACH=LEGACY_ONLY
  - [A-ARTIFACT] :205-212 path composition (`subagents/<taskId|childRunId|toolUseId>`), REACH=LEGACY_ONLY
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/agent-runtime-contract.test.ts` :: "creates provider-neutral child-run preflight records from governance decisions"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts` :: "embeds adapter-observed child-run records in SDK task lifecycle events"
- Decisions: none in DECISION_HITS for SoW lines 422-441.

## DEL-08-05#CLM-033 — Example lifecycle event payload
- Gist: `subagent.started` `HarnessEvent` example with `data` containing `childRunId`, `agentName` and `status`. Payload keys are bounded by the envelope and the minimum linkage.
- Code:
  - [A-MAPPER] :243 `childRunEventData` and :1075, REACH=LEGACY_ONLY
  - [A-CONTRACT] :235 `childRunRecordToEventData`, REACH=LEGACY_ONLY
  - [F-VIEWS] `harness-event-views.ts:501`, REACH=LIVE (consumer)
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts` :: "embeds adapter-observed child-run records in SDK task lifecycle events"
  - `projects/chirality-app-dev/frontend/src/__tests__/components/harness-stream-views.test.ts` :: "renders a row with agent name, description, and status badge"
- Decisions: none in DECISION_HITS for SoW lines 444-465.

## DEL-08-05#CLM-034 — Conflict table (guidance)
- Gist: C-001 is resolved by D-APP-38. The denied allocation ruling (D-APP-40) is restated for guidance.
- Code: NO_CANDIDATES. The unit is documentary.
- Tests: NO_CANDIDATES.
- Decisions: D-APP-38 (SoW:473), D-APP-40 (:474). Both RULED.

## DEL-08-05#CLM-035 — D-APP-56 R5 P45 reconciliation (guidance copy)
- Gist: Same UPD-138 and UPD-139 statement as CLM-009.
- Code: as CLM-009. [A-CONTRACT] :71-85, REACH=LEGACY_ONLY; [R-AGENTRUN] :102, REACH=LIVE.
- Tests: as CLM-009.
- Decisions: D-APP-56 (SoW:477, :479), RULED.

## DEL-08-05#CLM-036 — D-APP-68 managed-orchestration ownership mapping
- Gist: DEL-08-05 solely owns managed-child lifecycle, parent and declared linkage, replayable records, coordination persistence, and `artifacts/subagents/` output. DEL-05-05 keeps `descriptor.resultBudget`. DEL-08-04 owns admission and `delegate_agent`.
- Code:
  - [A-MANAGED] :768-975, REACH=LEGACY_ONLY
  - [A-ARTIFACT] :141, REACH=LEGACY_ONLY
  - `delegate_agent`: `projects/chirality-app-dev/frontend/src/lib/harness/subagent-bridge.ts` and `.../mcp/coordination-tools.ts`, both REACH=LEGACY_ONLY
  - `projects/chirality-runtime/packages/contracts/src/harness/mcp/tool-names.ts` and `.../harness/tool-descriptor.ts:1258-1268` (Agent/subagent descriptor, `emits` `subagent.*`), both REACH=LIVE
- Tests:
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/managed-delegation.test.ts` :: "persists child→parent notices and parent→child updates with acknowledgments"
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-tool-bridge.test.ts` (`resultBudget` hit)
- Decisions: D-APP-56 (SoW:487), D-APP-68 (SoW:483, :485, :487; register `_REGISTER.md:83`). Both RULED.

## DEL-08-05#REM-1 — DEL-08-05-V3-01 (`_STATUS.md:11`)
- Gist: Reconstructible evidence records for managed and native descendants, with replay and reconstruction fixtures and durable recomputable evidence. Currently not selectable.
- Gate suffix, verbatim: `NOT_SELECTABLE_UNTIL: Root WP-03/WP-05 fixtures (accepted DEL-02-07 and DEL-02-10 returns routed to App) and DEL-08-04-V3-01 landed; G4 for claims`
- Where each gate may be checked (App surfaces only):
  - **Root WP-03/WP-05 fixtures routed to App.** DEL-02-07 and DEL-02-10 are not App deliverable folders; there is no match under `projects/chirality-app-dev/execution/PKG-02*/1_Working/`. Check App inbound routing and notices under `projects/chirality-app-dev/execution/_Coordination/`. The same gate text appears in DEL-08-04 `_STATUS.md:17`.
  - **DEL-08-04-V3-01 landed.** Check `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_*/_STATUS.md:17` (Remaining item still present at the frozen basis), plus DEL-08-05 `Dependencies.csv:5` and :12 (DEP-08-05-004 and DEP-08-05-011).
  - **G4 for claims.** Check the App gate and evidence records named in the v3 release plan referenced at `_STATUS.md:13`. No G4 record for DEL-08-05 was located in the deliverable folder.
- Code:
  - Write locus `frontend/src/lib/harness/**`: [A-MANAGED], [A-CONTRACT] and [A-ARTIFACT], all REACH=LEGACY_ONLY
  - Current checkout AgentRun writer: [R-AGENTRUN] :905-926, REACH=LIVE
  - Native lineage: [R-NATIVE], REACH=LIVE
- Tests: `projects/chirality-runtime/tests/agent1-run.test.ts` (9 cases), `stagec-native-child-history.test.ts`, `role-policy.test.ts`.
- Decisions: D-GOV-35 (ROOT, `_STATUS.md:14`), D-APP-36 (`_STATUS.md:16`, RULED), and D-APP-117 (`_REGISTER.md:133`, AWAITING_RULING, which scopes out DEL-08-05 persistence). Ruling files also naming DEL-08-05: D-APP-70 (`D-APP-70_RULING_2026-07-20.md:51`) and D-APP-74 (`D-APP-74_RULING_2026-07-23.md:88`), both RULED.

## Cross-cutting

- **Recurrent modules** (number of units citing each):

  | Module | Units | REACH |
  |---|---|---|
  | `projects/chirality-app-dev/frontend/src/lib/harness/agent-runtime-contract.ts` | 17 | LEGACY_ONLY |
  | `projects/chirality-app-dev/frontend/src/lib/harness/tool-result-artifacts.ts` | 11 | LEGACY_ONLY |
  | `projects/chirality-app-dev/frontend/src/lib/harness/sdk-message-mapper.ts` | 9 | LEGACY_ONLY |
  | `projects/chirality-runtime/packages/core/src/agent1-run-coordinator.ts` | 8 | LIVE |
  | `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts` | 7 | LEGACY_ONLY |
  | `projects/chirality-runtime/packages/core/src/session-store.ts` | 6 | LIVE |
  | `projects/chirality-runtime/packages/core/src/role-policy.ts` | 5 | LIVE |
  | `projects/chirality-runtime/packages/contracts/src/harness/event-schema.ts` | 5 | LIVE |

- **Reach split, stated as reach facts only:**
  - Every module that defines or writes `ChildRunRecord`, `childRunId`, `artifacts/subagents` or the 16/512 KiB child-output limits is REACH=LEGACY_ONLY: the contract, mapper, artifacts, managed-delegation and session-events modules.
  - The LIVE modules for these concerns fall into three groups:
    - runtime event envelope and store: `event-schema.ts`, `session-store.ts`
    - managed Agent-1/Agent-2 `AgentRunRecord` writer (`agent1-run-coordinator.ts`) and role-policy evidence (`role-policy.ts`, `delegated-runtime.ts`)
    - native-child association and observation: `engine.ts`, `delegated.ts`, `runtime-method-service.ts`, `codex-supervisor.ts`
  - The LIVE App UI consumes `subagent.*` and `outputArtifactPath` for display: `harness-event-views.ts`, `turn-activity.ts`, `subagent-stream-view.tsx`, `activity-shelf.tsx`.
  - In LIVE runtime src, `subagent.*` appears only in the type enum and the Agent tool descriptor `emits`. `delegated-engine-adapter.ts:277-287` maps native `collabAgentToolCall` to `tool.*` and `codex.notification`.
- **Touched paths:**
  - `codex-supervisor.ts` has TOUCHED ranges (`da95ec194`, `cb08dbe2f`): 4-7, 28, 58, 65-76, 120-179 (partial), 219-273 (partial), 391-435 (partial), 526-544, 570-573, 613-695. The cited lines 280-309, 518-519 and 590-591 are outside every range.
  - `session-store.ts` has TOUCHED ranges 6-8 and 128-158 (`da95ec194`). The cited lines 654-1126 are outside them.
  - No other cited module appears in TOUCHED_PATHS.csv.
- **HINTS noise.** A large share of hint rows for this deliverable are token collisions: `denied`, `completed` and `cancelled` in IPC and attachment contracts, and doc names in `harness-section9-manifest.json`. Forward workers should rely on the anchors above rather than raw HINTS.

#END
