# PREGATHER — DEL-05-04 Runtime Replay and Transcript View

Read-only evidence map (TASK, Type 2) for run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-05 R2.
Basis: frozen tree `00115c719`. Candidate pointers only; no dispositions or alignment judgments.
REACH = module-level value from `R2/PKG-05/EVIDENCE_PACK/REACHABILITY.csv` (hint only).
TOUCHED = path appears in `TOUCHED_PATHS.csv` (commit `da95ec194`; line ranges noted).

## Orientation

### Deliverable key files (frozen tree, `.../1_Working/DEL-05-04_Runtime_Replay_and_Transcript_View/`)

| File | Bytes |
|---|---:|
| `ScopeOfWork.md` | 37985 |
| `_SEMANTIC.md` | 44528 |
| `_SEMANTIC_LENSING.md` | 38325 |
| `_STATUS.md` | 10323 |
| `Assessment_INSP-03_DEL-05-04.md` | 7217 |
| `Dependencies.csv` | 6881 |
| `_DEPENDENCIES.md` | 4821 |
| `MEMORY.md` | 3856 |
| `_REFERENCES.md` | 3785 |
| `_CONTEXT.md` | 2884 |
| `_run_records/` | 12 records (incl. `CANONICAL_REPLAY_RESTART_2026-08-17.md`, `R3_DAPP86_REAL_DAEMON_REPLAY_2026-08-03.md`) |

`_STATUS.md` state: IN_PROGRESS (last updated 2026-09-04).

### Decision IDs cited most (ScopeOfWork.md + _STATUS.md + _CONTEXT.md, raw counts)

ADQ-09 (23), D-APP-41 (15), SCA-APP-004 (13), D-APP-38 (7), ADQ-08 (4), D-APP-55 (3), ADQ-10 (3), SCA-APP-010 (2), D-APP-54 (2), D-APP-42 (2).
SoW CLM-004 also cites D-APP-48 (transcript-replay relocation).

### Main code areas

- **Live replay path (App → Runtime daemon):** `frontend/src/app/api/harness/session/[id]/events/route.ts:28` → `frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts:294-310` → `chirality-runtime/packages/client/src/client.ts:469` → `chirality-runtime/packages/daemon/src/runtime-daemon.ts:797-810` (`deriveTranscriptView` at :807) → `chirality-runtime/packages/core/src/session-store.ts:829-905` (`replayDetailed` / `replayDetailedUnlocked`).
- **Transcript model:** `chirality-runtime/packages/contracts/src/harness/transcript-replay.ts` (449 lines; `deriveTranscriptView` :252). `frontend/packages/harness-contract/src/transcript-replay.ts` is a 2-line `@deprecated` re-export of `@chirality/runtime-contracts/transcript-replay`.
- **App-local parser (pre-daemon):** `frontend/src/lib/harness/session-events.ts` (85 lines; `appendHarnessEvent` :16, `replayHarnessEvents` :50, read-time `redactJsonLike` :78).
- **Woven Dialogue replay lens:** `frontend/src/lib/woven-dialogue/selected-session-replay.ts`, `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, mounted in `woven-dialogue-shell.tsx:1024` inside `CoordinationPanel` `replaySlot`; parent link in `right-panel.tsx:29-65,162`.
- **Compatibility transcript UI:** `frontend/src/components/shell/transcript-stream-view.tsx:103-107`.

### Path-level facts relevant across units

- SoW paths **missing** at the frozen tree: `frontend/src/lib/harness/transcript-replay.ts` (cited CLM-006, CLM-013, CLM-016) and `frontend/src/lib/harness/event-schema.ts` (cited CLM-016). Event schema is at `chirality-runtime/packages/contracts/src/harness/event-schema.ts` (REACH=LIVE); `session-events.ts:3` imports it from `@chirality/runtime-contracts/event-schema`.
- `replayHarnessEvents` (session-events.ts:50) has no non-test caller: production modules import only `appendHarnessEvent` (e.g. `turn-engine.ts:6`, `permission-overlay.ts:5`, `chirality-hooks.ts:14`) or the type `HarnessReplaySummary` (`lib/harness/client.ts:4`). Callers of `replayHarnessEvents` are `src/__tests__/**` and the test double `src/__tests__/api/harness/fake-daemon-harness-port.ts:153-159`. REACH for `session-events.ts` = LEGACY_ONLY.
- Route docstring `route.ts:15` says it "reuses `replayHarnessEvents`"; the handler body calls `getDaemonHarnessPort().replaySession(...)` (route.ts:28).
- `routes.test.ts` replay cases (describe `session events replay (D-APP-22)` :1511; :1512, :1605) run against `createFakeDaemonHarnessPort()` (routes.test.ts:95-97), which uses `replayHarnessEvents` + `deriveTranscriptView`, not the daemon `session-store` path.
- Runtime `replayDetailedUnlocked` (session-store.ts:869-890) increments `malformedLineCount` for any unparsable line (not only the tail) and also for lines whose `schemaVersion` ∉ {1,2} or whose `sessionId` differs (:880-883). No `redact` symbol occurs in `chirality-runtime/packages/core/src/*.ts`; `persistEvent` (session-store.ts:812-822) appends without a redaction call. Read-time redaction exists only in the App-local `session-events.ts:78`.
- TOUCHED files on the live path: `client.ts` (da95ec194 :50-54, :363-383), `session-store.ts` (:6-8, :128-158), `runtime-daemon.ts` (:15-16, :57, :169-171, :660-686), `contracts/src/protocol.ts` (:66-71). None of the touched ranges contains the replay lines cited above (client.ts:469, session-store.ts:829-905, runtime-daemon.ts:797-810, protocol.ts:287-296).
- `TranscriptStreamView` (transcript-stream-view.tsx:103) is rendered by `workspace-sidebar.tsx:202` (reached via `app-shell.tsx`, whose only app importer is `app/not-found.tsx`) and by `ActivityShelf` (`activity-shelf.tsx:72`), which no component imports (shell imports `ActivityStrip`, right-panel imports `ActivityView`). `ActivityView` (activity-shelf.tsx:221-234) calls `deriveTranscriptView` directly and is rendered by `right-panel.tsx:191`.

---

## Deliverable Definition — Ontology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-001 | Datasheet heading | — | — | DOC_ONLY (heading) |
| CLM-002 | Identification | — | — | DOC_ONLY (identification table; "Anticipated artifacts" list maps to the code areas above) |
| CLM-003 | Attributes (primary store, session metadata, legacy input, event shape, replay tolerance, transcript target, SDK status, UI/runtime separation, secret handling) | `chirality-runtime/packages/core/src/session-store.ts:848-905` (LIVE, TOUCHED other ranges); `frontend/src/lib/harness/session-events.ts:9-14,50-85` (LEGACY_ONLY); `chirality-runtime/packages/contracts/src/harness/event-schema.ts` (LIVE); `chirality-runtime/packages/contracts/src/harness/transcript-replay.ts:6-72,205-225` (LIVE); `chirality-runtime/packages/contracts/src/harness/types.ts` (UIEvent type; LIVE); legacy: `session-store.ts:112-116,170-174,932` (LIVE) | `src/__tests__/lib/session-events.test.ts:21,64,219`; `src/__tests__/lib/transcript-replay.test.ts:106`; `chirality-runtime/tests/contracts-and-project.test.ts:198` | Canonical path in runtime is `this.eventsFile(projectId, sessionId)` (session-store.ts:863), project-scoped; App-local path is `CHIRALITY_SESSION_ROOT ?? cwd/.chirality/sessions` (session-events.ts:9-14). See redaction note in Orientation. |
| CLM-004 | Conditions (exact parser API, route/UI placement, selected-session posture, projection authority, parentage consumption, tool summary level) | `session-events.ts:50` `replayHarnessEvents` (LEGACY_ONLY); `frontend/packages/harness-contract/src/transcript-replay.ts` (2-line re-export; not in REACHABILITY map) → `chirality-runtime/packages/contracts/src/harness/transcript-replay.ts:252` (LIVE); `route.ts:17-35` (LIVE); `transcript-stream-view.tsx` (LIVE); `selected-session-replay.ts:143-260` (LIVE); `selected-session-replay-lens.tsx:328-382` (LIVE); `right-panel.tsx:29-65` (LIVE); `recorded-agent-hierarchy.ts:126` (LIVE) | `transcript-replay.test.ts`; `routes.test.ts:1512`; `selected-session-replay.test.ts:62,86,131`; `selected-session-replay-lens.test.tsx:79,119`; `woven-right-panel.test.tsx:41` | Live route uses daemon `replaySession`, not `replayHarnessEvents` (see Orientation). Hint tokens also hit `deliverable-contracts.test.ts` (governance scanner, not replay). |
| CLM-005 | Pass 3 Semantic Lensing Notes | — | — | DOC_ONLY (B-001/C-001/D-001 dispositions). `REFERENCE_HASHES.csv`: all DEL-05-04 CONTRACT/SPEC/PRD rows `Match = NO` at frozen basis (pack manifest note). |
| CLM-006 | Construction (parser, transcript reconstruction, SDK linkage, artifact link, fixtures) | Parser: `session-store.ts:848-905` (LIVE), `session-events.ts:50-85` (LEGACY_ONLY). Transcript: `contracts/src/harness/transcript-replay.ts:252-449` (LIVE). SDK linkage: `transcript-replay.ts:205-225` `deriveSdkLinkage`. Artifact link: `transcript-replay.ts:143-160` `artifactLink`, :392-404 | `transcript-replay.test.ts:26,106`; `session-events.test.ts:97,253`; `harness-stream-views.test.ts:90`; `routes.test.ts:1512` | Cited path `frontend/src/lib/harness/transcript-replay.ts` does not exist at frozen tree. |
| CLM-007 | References | — | — | DOC_ONLY (REF-001..REF-007 table; see `REFERENCE_HASHES.csv`) |

## Completion and Reliance Basis — Epistemology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-008 | Specification heading | — | — | DOC_ONLY (heading) |
| CLM-009 | Scope (in/out of scope bullets) | Same set as CLM-004; selected-session read-only lens: `selected-session-replay-lens.tsx:41` ("Recorded chat · read-only"), :54-55 (Return to primary), :304; disclosure `selected-session-replay.ts:121-131,173-195`; continuation `selected-session-replay.ts:47-51`, `woven-dialogue-shell.tsx:422-443` (LIVE) | `selected-session-replay-lens.test.tsx:79,119,158,188,202`; `woven-dialogue-shell.test.tsx:169,233,316` | Lens exposes an `onContinue` action (`woven-dialogue-shell.tsx:1028`) gated by `canContinueRecordedConversation` (selected-session-replay.ts:47); test `woven-dialogue-shell.test.tsx:316` "continues a compatible v3 replay in the mounted primary dialogue". |
| CLM-010 | Requirements REQ-001..REQ-019 | REQ-001/002: `session-store.ts:863-890` (LIVE); REQ-003: `session-store.ts:870-890`, `session-events.ts:69-78`; REQ-004/007: `transcript-replay.ts:53-64,205-225` (`sdkLinkage` separate field); REQ-005/006: `transcript-replay.ts:126-140,188-203,392-422`; REQ-008: `session-events.ts:19,78` (`redactJsonLike`, `run-logger.ts` LIVE); REQ-009: `session-store.ts:112-116,170-174`, `runtime-daemon-harness-port.ts:307` (`asLegacySession`), `session-manager.ts:12-33` (LIVE); REQ-011: `transcript-replay.ts:143-160,182`; REQ-013: paths listed in Orientation; REQ-014/015/019: `selected-session-replay-lens.tsx`, `woven-dialogue-shell.tsx:1013-1040`; REQ-016: `selected-session-replay.ts:86-110,129-131,150-158`; REQ-017: `right-panel.tsx:29-65`, `coordination-panel.tsx:74`, `recorded-agent-hierarchy.ts:126`; REQ-018: `transcript-replay.ts:47-48,66-72` (`terminalStatus` / `terminalReason`) | REQ-001/002/003: `session-events.test.ts:64`, `routes.test.ts:1512,1605`, `chirality-runtime/tests/runtime-v3-api.test.ts:94,108`; REQ-004/007: `transcript-replay.test.ts:106`; REQ-005/006: `transcript-replay.test.ts:26,91,146,160,170`; REQ-008: `redaction-path-matrix.test.ts:23,65`, `session-events.test.ts:97,219`; REQ-009: `chirality-runtime/tests/contracts-and-project.test.ts:198`; REQ-014/015/019: `selected-session-replay-lens.test.tsx:79,119,158,188`, `woven-dialogue-shell.test.tsx:169,233,292`; REQ-016: `selected-session-replay.test.ts:62,86,131,158,204`; REQ-017: `woven-right-panel.test.tsx:41`, `woven-dialogue-shell.test.tsx:292` | REQ-003 (tail-only) vs runtime counting any unparsable line and schema/session mismatches (session-store.ts:880-889). REQ-008: no redaction symbol in runtime core replay/persist path. No runtime test asserting `malformedLineCount` found (grep `malformedLineCount|malformed` over `chirality-runtime/tests`). REQ-013 lists `frontend/packages/harness-contract/src/transcript-replay.ts` (re-export only). |
| CLM-011 | Standards (session layout, HarnessEvent, adapter rule, K-EVENT, K-SDK-3) | `contracts/src/harness/event-schema.ts` (LIVE); `session-store.ts` (LIVE); `transcript-replay.ts` (LIVE) | `session-events.test.ts:21` (provider-neutral types); `transcript-replay.test.ts:106` | Standards table; code pointers as CLM-003. |
| CLM-012 | Verification (per-REQ approaches; fixture paths; section9 IDs) | `frontend/scripts/harness-section9-manifest.json:31-35` (`section9.session_event_replay`: testFiles `session-events.test.ts`, `transcript-replay.test.ts`; evidenceFiles `src/lib/harness/session-events.ts`), :52 (`section9.sdk_session_link_resume`); `scripts/validate-harness-section9.mjs` | Named fixtures all exist: `src/__tests__/lib/session-events.test.ts` (345 lines), `src/__tests__/lib/transcript-replay.test.ts` (172), `src/__tests__/api/harness/routes.test.ts` (1640), `src/__tests__/components/harness-stream-views.test.ts` (185); also `src/__tests__/scripts/validate-harness-section9.test.ts` | section9 evidence file is the LEGACY_ONLY `session-events.ts`. Integration: `src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts:334-429` (desktop replay before/after restart). |
| CLM-013 | Documentation (+ AC-001) | Paths as REQ-013; transcript model cited as `frontend/src/lib/harness/transcript-replay.ts` (missing; actual `contracts/src/harness/transcript-replay.ts`, LIVE); "Woven Dialogue replay lens ... TBD" — now `selected-session-replay-lens.tsx`, `selected-session-replay.ts` (LIVE) | As CLM-012 plus `selected-session-replay.test.ts`, `selected-session-replay-lens.test.tsx` | **AC-001** (sub-item): canonical precedence → daemon replay path; ordering/malformed-tail → `session-store.ts:869-890`; redaction → `session-events.ts:78` only; adapter-only SDK linkage → `transcript-replay.ts:205-225`; compact artifact refs → `transcript-replay.ts:143-182`; parentage → `right-panel.tsx:29-65`; stale/unknown/bounded → `selected-session-replay.ts:121-195`; read-only separation → lens + shell tests above. Workspace sidebar Transcript tab: `workspace-sidebar.tsx:202` (reach note in Orientation). |

## Production and Verification Method — Praxeology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-014 | Procedure heading | — | — | DOC_ONLY (heading) |
| CLM-015 | Purpose | — | — | DOC_ONLY |
| CLM-016 | Prerequisites | `session-store.ts:112-116,170-174` (legacy conversion; LIVE); `contracts/src/harness/event-schema.ts` (LIVE); `session-events.ts` (LEGACY_ONLY); `transcript-replay.ts:205-225` (LIVE) | `transcript-replay.test.ts:106`; `redaction-path-matrix.test.ts:23` | Cites `frontend/src/lib/harness/event-schema.ts` and `frontend/src/lib/harness/transcript-replay.ts` — both missing at frozen tree. "Read-time redaction" claim points to `session-events.ts:78` (App-local, LEGACY_ONLY). |
| CLM-017 | Steps 1-10 | Step 2 `CHIRALITY_SESSION_ROOT`: `session-events.ts:9-10`; runtime uses project registry paths (`session-store.ts:863`). Step 3: `session-store.ts:869-890`. Step 4: `transcript-replay.ts:252-449`. Step 5 SDK fields: `transcript-replay.ts:210-221` (engineSessionId, claudeSessionId, sdkSessionId, sdkTranscriptPath, sdkSessionStoreKey, sdkConfigDir, sdkSettingSources, sdk versions, model). Step 6: `session-events.ts:19,78`. Step 10: `woven-dialogue-shell.tsx:1013-1040`, `selected-session-replay-lens.tsx:54`, `right-panel.tsx:29-65` | Step 7/8 fixtures as CLM-012; Step 10: `woven-dialogue-shell.test.tsx:169,233,292,316`, `selected-session-replay-lens.test.tsx:119` | Hint tokens also hit `scripts/validate-harness-section8.mjs` (9 hits: session layout tokens). `sdkResumeMode` has no occurrence in `chirality-runtime/packages/contracts/src` or `frontend/src/lib` (grep). |
| CLM-018 | Verification checks table | As CLM-010/012 | Canonical replay: `transcript-replay.test.ts:26`; malformed tail: `routes.test.ts:1512`, `session-events.test.ts`; SDK linkage: `transcript-replay.test.ts:106`; legacy read: `chirality-runtime/tests/contracts-and-project.test.ts:198`, `chirality-runtime/tests/helpers.ts:34`; redaction: `redaction-path-matrix.test.ts:23`, `session-events.test.ts:219`; contract separation: `session-events.test.ts:21`, `turn-route-attachments.test.ts` (UIEvent/HarnessEvent hint hits) | "Contract separation": `UIEvent` defined in `chirality-runtime/packages/contracts/src/harness/types.ts` (LIVE) and referenced in `frontend/src/lib/harness/agent-sdk-manager.ts` (LEGACY_ONLY). |
| CLM-019 | Records (+ VER-001) | Records list: `session-events.ts`, `frontend/packages/harness-contract/src/transcript-replay.ts` (re-export), `route.ts`, `transcript-stream-view.tsx` | As CLM-012 | **VER-001** (sub-item): schema/traceability/parity/REVIEW checklist/HTML rendering of the SoW itself — DOC_ONLY (no product code). Hint tokens (`MATCH`) hit only `scripts/verify-version-identity.mjs` (unrelated). |

## Governing Values and Decisions — Axiology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| CLM-020 | Guidance heading | — | — | DOC_ONLY (heading) |
| CLM-021 | Purpose | — | — | DOC_ONLY (purpose prose; realised by CLM-006 pointers) |
| CLM-022 | Principles 1-5 | 1: daemon path `session-store.ts:829-905`; 2: `contracts/src/harness/types.ts` (UIEvent), `event-schema.ts`; 3: `transcript-replay.ts:53-64` (`TranscriptSdkLinkage` separate from items); 4: `session-store.ts:869-890`; 5: `session-events.ts:78`, `transcript-replay.ts:143-160` | `session-events.test.ts:21,219`; `transcript-replay.test.ts:106`; `routes.test.ts:1512` | Guidance prose; pointers as CLM-010. |
| CLM-023 | Considerations | `TranscriptView`/`TranscriptItem`: `contracts/src/harness/transcript-replay.ts:30-72` (LIVE); `session-manager.ts` (LIVE; hint hits for sdk fields) ; `chat-panel.tsx:4,967,1147,1227-1229,1561-1563` (LIVE) | `transcript-replay.test.ts`; `woven-dialogue-shell.test.tsx` (hint hits) | Cites model location `frontend/packages/harness-contract/src/transcript-replay.ts` (re-export only). `sdkResumeMode` named here; not among fields read in `deriveSdkLinkage` (transcript-replay.ts:210-221). |
| CLM-024 | Trade-offs | `session-store.ts:869-890`; `transcript-replay.ts:143-182` | `session-events.test.ts:97,253` | Guidance prose. |
| CLM-025 | Examples | `transcript-replay.ts:252-449`; `session-store.ts:869-890`; `transcript-replay.ts:215` (`sdkTranscriptPath`) | `transcript-replay.test.ts:26,106`; `routes.test.ts:1512`; fixture `src/__tests__/fixtures/sessions/v2/manifest.json` (hint hit) | Guidance examples. |
| CLM-026 | Source-State Notes | — | — | DOC_ONLY. `REFERENCE_HASHES.csv` shows `Match = NO` for DEL-05-04 CONTRACT/SPEC/PRD at frozen basis. |
| CLM-027 | Conflict Table | — | — | DOC_ONLY ("None"). |

## _STATUS.md — Remaining

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| REM-1 | Prior scope note (daemon/client vertical slice closed 2026-08-17) | Live daemon replay path (Orientation) | `src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts:334-429`; `chirality-runtime/tests/runtime-v3-api.test.ts:94,108`; `chirality-runtime/tests/app-owned-composition.test.ts:339,359` | Closure record: `_run_records/CANONICAL_REPLAY_RESTART_2026-08-17.md`. Hint tokens produced no hits. |
| REM-2 | DEL-05-04-V3-01 — restart/resume continuity in read-only replay lens (NOT_SELECTABLE_UNTIL Root DEL-02-11 + DEL-05-01-V3-02) | `selected-session-replay.ts:47-51` (`canContinueRecordedConversation`: projectRoot match + disclosure gate); `woven-dialogue-shell.tsx:422-443`; `chat-panel.tsx:1227-1229,1561-1563` (v3 `schemaVersion` check) (all LIVE) | `selected-session-replay.test.ts:226`; `selected-session-replay-lens.test.tsx:202`; `woven-dialogue-shell.test.tsx:316`; `chirality-runtime/tests/runtime-v3-api.test.ts:108` | Item requires "exact root/account/policy match"; `canContinueRecordedConversation` compares `continuation.projectRoot` only (selected-session-replay.ts:48-50). Hint tokens (`frontend/`, `main`, `npm run validate:release-quality`) hit unrelated scripts / `electron/api-key-*.ts`. |
| REM-3 | DEL-05-04-V3-02 — Session view: replay lens in right panel with read-only banner and parent link (NOT_SELECTABLE_UNTIL DEL-02-03-V3-01) | `woven-dialogue-shell.tsx:101,116,443,1013-1040` (`coordinationView 'session'`, `replaySlot`); `coordination-panel.tsx:12-19,47-63,74` (Session/Agents switch; LIVE); `right-panel.tsx:29-65,162` (parent button; LIVE); `selected-session-replay-lens.tsx:41,54` (LIVE) | `woven-dialogue-shell.test.tsx:169,233,292`; `woven-right-panel.test.tsx:41`; `selected-session-replay-lens.test.tsx:79` | Hint tokens as REM-2 (unrelated hits). `frontend/src/lib/woven-dialogue/contracts.ts` (parentage types grep hit) is REACH=LEGACY_ONLY + UNREACHED. |

## Units with NO_CANDIDATE

None. DOC_ONLY units: CLM-001, CLM-002, CLM-005, CLM-007, CLM-008, CLM-014, CLM-015, CLM-020, CLM-021, CLM-026, CLM-027, and sub-item VER-001.

## Search record

Grep terms used (frozen tree; runtime limited to `packages/` and `tests/`): `replayHarnessEvents`, `deriveTranscriptView`, `replaySession`, `replayDetailed`, `malformedLineCount`, `malformed`, `redact`, `legacy`, `legacySessionRoots`, `SelectedSessionReplayLens`, `createSelectedSessionReplayLoader`, `canContinueRecordedConversation`, `TranscriptStreamView`, `WorkspaceSidebar`, `AppShell`, `ActivityShelf`, `parentSessionId|parentRunId`, `session_event_replay|sdk_session_link_resume`, `UIEvent`, `harness/session-events`.
