# PREGATHER — DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision

Read-only pre-gather leads for R2 concordance workers (run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`,
frozen basis `00115c719`). Leads only: no dispositions, no alignment judgments, no ledger rows.

Conventions used below:

- Path prefixes: `FE/` = `projects/chirality-app-dev/frontend/`; `RT/` = `projects/chirality-runtime/`;
  `DEL/` = `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/`.
- REACH tags are copied from `EVIDENCE_PACK/REACHABILITY.csv`; scripts, manifests and docs are not in the map and carry no tag.
- Gate membership `APP*` / `RUNTIME*`: the gate transcripts record only aggregate Vitest results
  (APP: 222 files passed + 1 skipped; RUNTIME: 42 files passed) and do not name most individual files, so a
  frontend test is `APP*` (covered by the aggregate run, file not named) and a runtime test is `RUNTIME*`.
  Which APP file was the 1 skipped file is not recorded; none of the test files listed below contains
  `.skip`/`skipIf`/`runIf`.
- Decisions: from `DECISION_HITS.csv` rows whose `ScopeOfWork.md` line falls inside the unit, plus IDs named in the unit text.
- Context lead that applies to every code lead: the Claude Agent SDK adapter modules are `LEGACY_ONLY`
  (reached only from themselves/`FE/src/lib/harness/runtime.ts`), `RT/packages/engine-claude/src/index.ts` is
  `UNREACHED`, and `FE/scripts/verify-packaged-dependency-boundary.mjs:51` lists `@anthropic-ai/claude-agent-sdk`
  in `forbiddenLegacyRuntimePackages` (Claude platform packages pattern at :59; legacy-engine source list at
  :146-151). The live engine path is `RT/packages/daemon/src/codex-supervisor.ts` REACH=LIVE (touched).
  `D-APP-127_APPLICATION_MAP.csv` records no D-APP-127/D-GOV-43 citation in any DEL-04-01 carrier.

## DEL-04-01#CLM-001 — Datasheet: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision   (SubItems: none)
- code: no candidate found (heading/current-state note only; searched: HINTS `MATCH`, `docs/PRD.md` — hits in `FE/scripts/verify-version-identity.mjs`, `FE/scripts/harness-section9-manifest.json` are token noise)
- doc: `DEL/_REFERENCES.md` REF-006; `EVIDENCE_PACK/REFERENCE_HASHES.csv` (DEL-04-01 PRD row: recorded `MATCH`, recomputed `Match=NO` at frozen basis)
- decisions: D-APP-38, D-APP-56

## DEL-04-01#CLM-002 — Identification   (SubItems: none)
- code: no candidate found (identification table; searched: HINTS — no tokens emitted)
- doc: `DEL/_CONTEXT.md`, `DEL/_STATUS.md`
- decisions: none in pack

## DEL-04-01#CLM-003 — Attributes   (SubItems: none)
- code: `FE/package.json:63` (`@anthropic-ai/claude-agent-sdk` `0.3.150`); `FE/package-lock.json:124-126`
- code: `RT/packages/contracts/src/harness/agent-engine-port.ts:77` `AgentEnginePort`, `:90` `RuntimeEngineContract` REACH=LIVE
- code: `FE/src/lib/harness/claude-agent-sdk-manager.ts:80` `ClaudeAgentSdkManager implements … AgentEnginePort` REACH=LEGACY_ONLY
- code: `FE/src/lib/harness/sdk-options-builder.ts:248` `settingSources`, `:183` `createSdkMcpServer` REACH=LEGACY_ONLY
- code: `FE/src/lib/harness/permission-overlay.ts:364` `createHarnessCanUseTool` REACH=LEGACY_ONLY
- code: `FE/scripts/verify-packaged-agent-sdk-runtime.mjs:177` (`claude_code_version: '2.1.150'` fixture)
- test: `FE/src/__tests__/lib/claude-agent-sdk-manager.test.ts`:"passes only Runtime-supplied instructions and tools to the real SDK adapter boundary" (APP*)
- test: `FE/src/__tests__/integration/runtime-successor-adapters.integration.test.ts` (AgentEnginePort/SessionStore hits) (APP*)
- decisions: D-APP-52, D-APP-68

## DEL-04-01#CLM-004 — Conditions   (SubItems: none)
- code: `FE/src/lib/harness/sdk-options-builder.ts:30-42` `parseSettingSources` (empty default; `['project']` only via `CHIRALITY_SDK_SETTING_SOURCES`) REACH=LEGACY_ONLY
- code: `FE/src/lib/harness/permission-overlay.ts:112` `resolveHarnessPermissionDecision` REACH=LEGACY_ONLY
- code: `FE/src/lib/harness/sdk-message-mapper.ts:633` `mapSdkMessageToHarness` REACH=LEGACY_ONLY
- test: `FE/src/__tests__/lib/sdk-options-builder.test.ts`:"defaults to SDK settings isolation and exposes only requested read-class tools"; :"allows only explicit project settings and never user or local sources" (APP*)
- test: `FE/src/__tests__/lib/permission-overlay.test.ts`:"lets explicit hard denies override abstract allow and ask decisions" (APP*)
- code: `FE/scripts/harness-section9-manifest.json:25,46,53` (K-SDK-1 / K-SDK-3 source refs)
- decisions: D-APP-38

## DEL-04-01#CLM-005 — Construction   (SubItems: none)
- code: `FE/package.json:63`; `FE/package-lock.json:124`
- doc: `DEL/Decision_Version_Pinned_SDK_Adoption_2026-07-19.md` (Fallback Triggers section at :98); `DEL/Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`
- code: `docs/harness/` hits (`FE/src/__tests__/contract-pins.manifest.ts`, `RT/packages/contracts/src/harness/tool-catalog.ts`) are token noise for the superseded location note
- decisions: D-APP-68

## DEL-04-01#CLM-006 — References   (SubItems: none)
- code: no candidate found (reference table; searched: HINTS `docs/*.md` — only manifest/test path strings)
- doc: `DEL/_REFERENCES.md`; `EVIDENCE_PACK/REFERENCE_HASHES.csv` (all DEL-04-01 rows `Match=NO` at frozen basis)
- decisions: D-APP-38

## DEL-04-01#CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)   (SubItems: none)
- code: no candidate found (status reconciliation note; searched: HINTS — no tokens)
- doc: `DEL/Dependencies.csv`, `DEL/Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`, `DEL/Evidence_CODEV-001_SDK_Probe_Record.md`
- decisions: D-APP-56

## DEL-04-01#CLM-008 — Specification: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision   (SubItems: none)
- code: no candidate found (heading/current-state note; searched: HINTS `MATCH`, `docs/PRD.md`)
- decisions: D-APP-38, D-APP-56

## DEL-04-01#CLM-009 — Scope   (SubItems: none)
- code: `FE/src/lib/harness/sdk-options-builder.ts:125` `buildSdkOptions` REACH=LEGACY_ONLY (named as excluded implementation)
- code: `FE/src/lib/harness/sdk-message-mapper.ts:633` REACH=LEGACY_ONLY; `FE/src/lib/harness/turn-engine.ts:155` `TurnEngine` REACH=LEGACY_ONLY
- code: `FE/scripts/run-dapp52-live-sdk-probe.mjs:2` (header names DEL-04-01 residuals)
- code: `RT/packages/contracts/src/harness/agent-engine-port.ts:77,90` REACH=LIVE
- test: `FE/src/__tests__/api/harness/agent-sdk-dev-turn.test.ts`:"runs the route-level agentSdk turn through real SDK query with an offline subprocess" (APP*)
- decisions: none in pack

## DEL-04-01#CLM-010 — Requirements   (SubItems: none)
- REQ-001/002 version: `FE/package.json:63`; `FE/package-lock.json:124-126`; `FE/scripts/verify-packaged-agent-sdk-runtime.mjs:177`
- REQ-003/004 mapping: `FE/src/lib/harness/sdk-message-mapper.ts:633,1190` REACH=LEGACY_ONLY; test `FE/src/__tests__/lib/sdk-message-mapper.test.ts`:"maps SDK-only system messages into provider-neutral HarnessEvent types" (APP*); `FE/src/__tests__/lib/engine-conformance.test.ts`:"flags non-public event names from scripted adapters" (APP*)
- REQ-005 settings: `FE/src/lib/harness/sdk-options-builder.ts:30,248` REACH=LEGACY_ONLY; tests in `FE/src/__tests__/lib/sdk-options-builder.test.ts` lines 162, 449 (APP*)
- REQ-006 permissions: `FE/src/lib/harness/permission-overlay.ts:112,306,364` REACH=LEGACY_ONLY; `FE/src/lib/harness/chirality-hooks.ts:426` REACH=LEGACY_ONLY; tests `FE/src/__tests__/lib/permission-overlay.test.ts` (APP*), `FE/src/__tests__/lib/chirality-hooks.test.ts`:"blocks outside-root, instruction-root, and symlink write attempts" (APP*)
- REQ-007 MCP: `FE/src/lib/harness/mcp/read-tools.ts:1005,1259` REACH=LEGACY_ONLY; `FE/src/lib/harness/sdk-options-builder.ts:183`; test `FE/src/__tests__/lib/agent-sdk-mcp-behavior-probe.test.ts`:"shows SDK MCP messages do not automatically invoke permission or hook callbacks" (APP*)
- REQ-008 session/resume: `FE/src/lib/harness/sdk-options-builder.ts:247` (`resume: sdkSessionId`); `FE/src/lib/harness/claude-agent-sdk-manager.ts:254,296` REACH=LEGACY_ONLY; `RT/packages/core/src/session-store.ts:997-1033` adapter inference REACH=LIVE; `CLAUDE_CONFIG_DIR` only in scripts (`FE/scripts/run-dapp52-live-sdk-probe.mjs:234`) — no candidate in `FE/src/lib` or `RT/packages` (searched: `CLAUDE_CONFIG_DIR`)
- REQ-009 canonical JSONL: `RT/packages/core/src/session-store.ts` REACH=LIVE
- REQ-010 interrupt: `FE/src/lib/harness/claude-agent-sdk-manager.ts:147-178` `interrupt` REACH=LEGACY_ONLY; `FE/src/lib/harness/sdk-options-builder.ts:105`; test `FE/src/__tests__/lib/engine-conformance.test.ts`:"requires interrupted adapter turns to emit interruption terminal evidence" (APP*)
- REQ-011 packaging: `FE/scripts/verify-packaged-agent-sdk-runtime.mjs:274-280`; `FE/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs:417-457`; contrast `FE/scripts/verify-packaged-dependency-boundary.mjs:51`; `asarUnpack` found only in `FE/scripts/verify-pi-supply-chain.mjs`
- REQ-012 key handoff/redaction: `FE/src/lib/harness/claude-agent-sdk-manager.ts:39-76` env inject/restore, `:501` redaction REACH=LEGACY_ONLY; `FE/src/lib/harness/run-logger.ts:81,95` REACH=LIVE; tests `FE/src/__tests__/lib/claude-agent-sdk-manager.test.ts`:"injects active API key into SDK env, restores prior env, and redacts persisted failures" (APP*), `FE/src/__tests__/lib/run-logger.test.ts`:"redacts raw and encoded configured API-key variants" (APP*)
- REQ-013 fallback: `DEL/Decision_Version_Pinned_SDK_Adoption_2026-07-19.md:98`; code token `FALLBACK` hits (`FE/src/lib/harness/anthropic-agent-sdk-manager.ts:46` `FALLBACK_MODEL`) are noise
- REQ-014 no local tools: `FE/scripts/run-dapp52-live-sdk-probe.mjs:239-242` (`dontAsk`, `allowedTools:['Read']`, disallowed list)
- REQ-015 residual risks: doc only (`DEL/Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`)
- test: `RT/tests/contracts-and-project.test.ts` (claude-agent-sdk hits) (RUNTIME*)
- touched: YES (`RT/packages/core/src/session-store.ts`)
- decisions: none in pack for this range; text cites K-SDK-1/2, K-PERM-1..3, K-MCP-1, K-KEY-1, K-ENGINE-4/5

## DEL-04-01#CLM-011 — Probe Evidence Thresholds   (SubItems: none)
- code: version pin `FE/package.json:63`, `FE/package-lock.json:124`
- code: settings `FE/scripts/run-dapp52-live-sdk-probe.mjs:242`; `FE/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs:494`
- code: permissions `FE/src/lib/harness/permission-overlay.ts:112` REACH=LEGACY_ONLY
- code: terminal outcomes `FE/src/lib/harness/turn-engine.ts:155` REACH=LEGACY_ONLY; test `FE/src/__tests__/lib/turn-engine.test.ts`:"persists accepted input and typed terminal evidence for every provider preflight failure, then releases the lock" (APP*)
- code: key/redaction `FE/src/lib/harness/run-logger.ts:81` REACH=LIVE; test `FE/src/__tests__/scripts/run-live-packaged-agent-sdk-read-tool-proof.test.ts`:"passes with an explicit api key file and writes no key material to the summary" (APP*)
- code: packaging test `FE/src/__tests__/scripts/verify-packaged-agent-sdk-runtime.test.ts`:"passes when the packaged SDK resolves the native command under app.asar.unpacked" (APP*)
- code: `K-KEY-1` hits `FE/src/lib/consent/hosted-engine-consent-port.ts` (token overlap; hosted consent, not SDK)
- decisions: D-APP-65, D-APP-68

## DEL-04-01#CLM-012 — Standards   (SubItems: none)
- code: `RT/packages/contracts/src/harness/agent-engine-port.ts:90` REACH=LIVE; `RT/packages/contracts/src/harness/engine-conformance.ts` REACH=LIVE; `RT/packages/contracts/src/harness/tool-descriptor.ts:49` (`'claude-agent-sdk-builtin'` surface) REACH=LIVE
- code: `FE/scripts/harness-section9-manifest.json` (SPEC/CONTRACT refs)
- decisions: none in pack

## DEL-04-01#CLM-013 — Verification   (SubItems: none)
- VER-001: `FE/package.json:63`, `FE/package-lock.json:124`
- VER-002: `FE/src/__tests__/lib/sdk-message-mapper.test.ts` (APP*); `FE/src/__tests__/lib/engine-conformance.test.ts`:"passes a Claude Agent SDK success stream against the provider-neutral engine contract" (APP*)
- VER-003: `FE/src/__tests__/lib/sdk-options-builder.test.ts` lines 162, 449 (APP*)
- VER-004: `FE/src/__tests__/lib/permission-overlay.test.ts` (APP*); `FE/src/__tests__/lib/sdk-options-builder.test.ts`:"fails closed when a provider callback or hook names a tool omitted from the admitted turn set" (APP*)
- VER-005: `FE/src/__tests__/lib/agent-sdk-mcp-behavior-probe.test.ts` (APP*)
- VER-006: `FE/src/__tests__/lib/claude-agent-sdk-manager.test.ts`:"prepares a reversible successor and starts it with a fresh provider identity" (resume at :109) (APP*)
- VER-007: `FE/src/__tests__/lib/engine-conformance.test.ts` case at :457 (APP*)
- VER-008: `FE/src/__tests__/scripts/verify-packaged-agent-sdk-runtime.test.ts` (APP*); `FE/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs`
- VER-009/010/011: doc only (`DEL/Decision_…2026-07-19.md`, `DEL/_REFERENCES.md`)
- decisions: D-APP-38

## DEL-04-01#CLM-014 — Documentation   (SubItems: AC-001)
- code: `FE/package.json:63`, `FE/package-lock.json:124`; test `FE/src/__tests__/scripts/verify-version-identity.test.ts` (package.json/package-lock path hits) (APP*)
- code: `FE/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs:417-457` (`app.asar.unpacked`); `FE/scripts/finalize-electron-resources.mjs:65`
- AC-001 message mapping: `FE/src/lib/harness/sdk-message-mapper.ts:633` REACH=LEGACY_ONLY; session link `FE/src/lib/harness/claude-agent-sdk-manager.ts:296` REACH=LEGACY_ONLY
- AC-001 future-provider criteria: no candidate found in code (searched: `future-provider`, `provider/SDK` — single hit `RT/packages/engine-pi-omlx/src/pi-event-mapper.ts` is a comment token)
- doc: `DEL/Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`, `DEL/Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`, `DEL/Evidence_DAPP52_PACKAGED_LIVE_PROOF_2026-07-18_summary.json`
- decisions: D-APP-38, D-APP-65, D-APP-68

## DEL-04-01#CLM-015 — Procedure: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision   (SubItems: none)
- code: no candidate found (heading/current-state note; searched: HINTS `MATCH`, `docs/PRD.md`)
- decisions: D-APP-38, D-APP-56

## DEL-04-01#CLM-016 — Purpose   (SubItems: none)
- code: no candidate found (procedure purpose; searched: HINTS — no tokens)
- decisions: none in pack

## DEL-04-01#CLM-017 — Prerequisites   (SubItems: none)
- code: `FE/package.json:63`; `FE/scripts/verify-packaged-agent-sdk-runtime.mjs:15` (`darwin:arm64` platform map)
- test: `FE/src/__tests__/api/harness/routes.test.ts` (`0.3.150` hit) (APP*); fixtures `FE/src/__tests__/fixtures/sessions/v2/sess_v2_readable.json`
- doc: `DEL/Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`; `DEL/_DEPENDENCIES.md`
- decisions: D-APP-38, D-APP-68

## DEL-04-01#CLM-018 — Steps   (SubItems: none)
- step 3: `FE/package.json:63`, `FE/package-lock.json:124`
- step 4: `FE/scripts/run-dapp52-live-sdk-probe.mjs`; `FE/src/lib/harness/sdk-message-mapper.ts:633` REACH=LEGACY_ONLY
- step 5: `FE/src/lib/harness/sdk-options-builder.ts:30,248` REACH=LEGACY_ONLY
- step 6: `FE/src/lib/harness/permission-overlay.ts:364` REACH=LEGACY_ONLY; `FE/scripts/run-dapp52-live-sdk-probe.mjs:239-242`
- step 7: `FE/src/lib/harness/mcp/read-tools.ts:1259` REACH=LEGACY_ONLY; `FE/src/lib/harness/chirality-hooks.ts:426` REACH=LEGACY_ONLY
- step 8: `FE/scripts/run-dapp52-live-sdk-probe.mjs:234` (`CLAUDE_CONFIG_DIR`); `RT/packages/core/src/session-store.ts:997-1033` REACH=LIVE; `SessionStore` hits `FE/scripts/controlled-ci-runtime.ts`, `FE/src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts` (APP*)
- step 9: `FE/src/lib/harness/claude-agent-sdk-manager.ts:39-76` REACH=LEGACY_ONLY
- step 10: `FE/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs`; `FE/scripts/verify-packaged-agent-sdk-runtime.mjs`
- step 11-13: doc only (`DEL/Decision_…2026-07-19.md`)
- touched: YES (`RT/packages/core/src/session-store.ts`)
- decisions: D-APP-38, D-APP-68

## DEL-04-01#CLM-019 — Verification   (SubItems: none)
- code: permissions `FE/scripts/run-dapp52-live-sdk-probe.mjs:239-242`; `FE/scripts/verify-packaged-agent-sdk-runtime.mjs:306-307`
- test: `FE/src/__tests__/lib/claude-agent-sdk-manager.test.ts`, `FE/src/__tests__/lib/permission-overlay.test.ts` (canUseTool hits) (APP*)
- test: interrupts `FE/src/__tests__/lib/engine-conformance.test.ts` case at :457 (APP*)
- decisions: D-APP-38, D-APP-68

## DEL-04-01#CLM-020 — Records   (SubItems: none)
- code: `FE/package.json:63`, `FE/package-lock.json:124`; `FE/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs:417-457`
- test: `FE/src/__tests__/scripts/run-live-packaged-agent-sdk-read-tool-proof.test.ts` (APP*); `FE/src/__tests__/scripts/verify-version-identity.test.ts` (APP*)
- doc: `DEL/Decision_…2026-07-19.md`; `DEL/Evidence_DAPP52_PACKAGED_LIVE_PROOF_2026-07-18_summary.json`
- decisions: D-APP-68

## DEL-04-01#CLM-021 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)   (SubItems: VER-001)
- code: no candidate found for the note (searched: HINTS — no tokens)
- VER-001: doc inspection of `DEL/` evidence package (`Decision_…`, `Evidence_CODEV-001_SDK_Probe_Record.md`, `Evidence_DAPP52_*`, `Evidence_HANDOVER_CONSUMPTION_2026-07-18.md`, `Assessment_INSP-03_DEL-04-01.md`)
- decisions: D-APP-56

## DEL-04-01#CLM-022 — Guidance: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision   (SubItems: none)
- code: no candidate found (heading/current-state note; searched: HINTS `MATCH`, `docs/PRD.md`)
- decisions: D-APP-38, D-APP-56

## DEL-04-01#CLM-023 — Purpose   (SubItems: none)
- code: no candidate found beyond `FE/scripts/run-dapp52-live-sdk-probe.mjs:2` (DEL-04-01 header) (searched: HINTS `DEL-04-01`, `docs/DIRECTIVE.md`, `docs/PLAN.md`)
- decisions: none in pack

## DEL-04-01#CLM-024 — Principles   (SubItems: none)
- P1 contracts: `RT/packages/contracts/src/harness/agent-engine-port.ts:77,90` REACH=LIVE; `FE/src/lib/harness/harness-ui-bridge.ts` REACH=LEGACY_ONLY (`providerMetadataAllowed` comment at :17)
- P4 settings: `FE/src/lib/harness/sdk-options-builder.ts:30` REACH=LEGACY_ONLY
- P5 permissions: `FE/src/lib/harness/permission-overlay.ts:364` REACH=LEGACY_ONLY
- P6 transcripts: `RT/packages/core/src/session-store.ts` REACH=LIVE
- test: `FE/src/__tests__/lib/engine-conformance.test.ts` (APP*); `FE/src/__tests__/integration/pi-omlx-wire.integration.test.ts` (AgentEnginePort hit) (APP*)
- touched: YES (`RT/packages/core/src/session-store.ts`)
- decisions: none in pack; text cites K-ENGINE-1..5, K-RELIANCE-1/2, K-SDK-3, K-PERM-3

## DEL-04-01#CLM-025 — Considerations   (SubItems: none)
- code: packaging `FE/scripts/verify-packaged-agent-sdk-runtime.mjs:274-280`; current packaged exclusion `FE/scripts/verify-packaged-dependency-boundary.mjs:51,146-151`; test `FE/src/__tests__/scripts/verify-packaged-dependency-boundary.test.ts`:"flags legacy runtime packages and Claude platform packages" (APP*)
- code: transcript placement `FE/scripts/run-dapp52-live-sdk-probe.mjs:234`
- decisions: D-APP-38, D-APP-52, D-APP-68

## DEL-04-01#CLM-026 — Trade-offs   (SubItems: none)
- code: event model `FE/src/lib/harness/sdk-message-mapper.ts:633` REACH=LEGACY_ONLY; permissions `FE/src/lib/harness/permission-overlay.ts:112` REACH=LEGACY_ONLY; settings `FE/src/lib/harness/sdk-options-builder.ts:30` REACH=LEGACY_ONLY; session storage `RT/packages/core/src/session-store.ts` REACH=LIVE
- code: `.claude` hits `FE/scripts/validate-harness-section8.mjs`, `FE/scripts/run-dapp52-live-sdk-probe.mjs`
- touched: YES (`RT/packages/core/src/session-store.ts`)
- decisions: none in pack; text cites K-SDK-1, K-SDK-2

## DEL-04-01#CLM-027 — Residual-Risk Appraisal Method   (SubItems: none)
- code: no candidate found (appraisal method; searched: HINTS `FALLBACK` — `FE/src/components/shell/app-update-provider.tsx`, `FE/src/lib/harness/anthropic-agent-sdk-manager.ts:46` are token noise)
- doc: `DEL/Decision_…2026-07-19.md` (twelve residual-risk assessments)
- decisions: none in pack; text cites K-ENGINE-5, K-RELIANCE-1/2, K-SDK-2

## DEL-04-01#CLM-028 — Examples   (SubItems: none)
- code: `FE/scripts/run-dapp52-live-sdk-probe.mjs:234-242`; `FE/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs:480-494`
- test: `FE/src/__tests__/lib/claude-agent-sdk-manager.test.ts`:"maps SDK stream messages to existing UI events and appends HarnessEvent evidence" (APP*)
- doc: `DEL/Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`
- decisions: none in pack

## DEL-04-01#CLM-029 — Conflict Table (for human ruling)   (SubItems: none)
- code: no candidate found (source-state conflict SRC-001; searched: HINTS `MATCH`, `_REFERENCES.md`, `docs/PRD.md`)
- doc: `DEL/_REFERENCES.md`; `EVIDENCE_PACK/REFERENCE_HASHES.csv` (PRD recomputed hash differs from recorded)
- decisions: D-APP-38

## DEL-04-01#CLM-030 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)   (SubItems: none)
- code: no candidate found (status note; searched: HINTS — no tokens)
- decisions: D-APP-56

## DEL-04-01#CLM-031 — D-APP-68 version-pinned adoption verdict (2026-07-19)   (SubItems: none)
- code: `FE/package.json:63`; `FE/package-lock.json:124`; `FE/scripts/verify-packaged-agent-sdk-runtime.mjs:177`
- code: current-state context — `FE/scripts/verify-packaged-dependency-boundary.mjs:51` (SDK forbidden in packaged bundle); git log on that script and `FE/src/lib/harness/claude-agent-sdk-manager.ts` shows `39c0bb6ab` (2026-09-12, D-GOV-43 A2), `2f825f180` (2026-09-10, Codex MVP chat)
- test: `FE/src/__tests__/api/harness/agent-sdk-dev-turn.test.ts` (2.1.150 hit) (APP*)
- decisions: D-APP-65, D-APP-68

## Shared evidence

- `FE/package.json:63` / `FE/package-lock.json:124-126` — SDK pin (cited by CLM-003, 005, 010, 011, 013, 014, 017, 018, 020, 031).
- `FE/src/lib/harness/sdk-options-builder.ts`, `sdk-message-mapper.ts`, `permission-overlay.ts`, `claude-agent-sdk-manager.ts`, `chirality-hooks.ts`, `mcp/read-tools.ts`, `turn-engine.ts` — all REACH=LEGACY_ONLY.
- `FE/scripts/run-dapp52-live-sdk-probe.mjs`, `run-live-packaged-agent-sdk-read-tool-proof.mjs`, `verify-packaged-agent-sdk-runtime.mjs` (npm scripts `harness:validate:agentsdk-*` at `FE/package.json:24-25`).
- `FE/scripts/verify-packaged-dependency-boundary.mjs:51,59,146-151` (npm `desktop:verify-dependencies`, `FE/package.json:39`) — current packaged-bundle exclusion of the SDK.
- `RT/packages/contracts/src/harness/agent-engine-port.ts` REACH=LIVE; `RT/packages/core/src/session-store.ts` REACH=LIVE, touched; `RT/packages/core/src/compatibility-session-policy.ts:29-39` REACH=LIVE; `RT/packages/engine-claude/src/index.ts` REACH=UNREACHED (reached from no product entry).
- Deliverable records: `DEL/Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`, `DEL/Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`, `DEL/Evidence_CODEV-001_SDK_Probe_Record.md`.
- Gate transcripts: aggregate-only; no per-file membership recoverable.

Effort: 31/31 units covered; ~25 read-only greps/reads over frozen tree, pack, hints and transcripts; 2 read-only `git log` calls.
