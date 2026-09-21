# DEL-03-02 notes: Thin TurnEngine and Session Locking (R2 forward pass)

Basis: frozen tree `00115c719`. Rulebook: `CONVENTIONS.md`, with the PKG-03 manager's rule additions
(RUN_BASIS Addenda 4 and 5: R4-Q4 token; STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break)
applied before sealing. No rows turn on R4-Q4.

## 1. Census

- **Rows:** 52 (29 indexed units plus 5 run-local rows: REGISTER-1..4 and STATE-1). All 29 units are covered.
- **By ClaimType:** REQUIREMENT 22 · CONTEXT_CLAIM 16 · ACCEPTANCE 7 · REGISTER_DEFECT 4 · STATE_ASSERTION 2 · REMAINING_WORK 1.
- **By Disposition (all rows):** STALE_SPECIFICATION 17 · IMPLEMENTED_DIFFERENTLY 12 · NOT_AUDITABLE 8 · ALIGNED 8 ·
  PARTIALLY_IMPLEMENTED 3 · AUTHORITY_CONFLICT 2 · DOCUMENTED_UNIMPLEMENTED 1 · REMAINING_STATE_MISMATCH 1.
- **SEE rows (counted separately, MR-4):** 9 in total.
  - SEE rows under MR-4: CLM-017 → CLM-011; CLM-020 → CLM-008; CLM-021.1/.2/.3/.5/.6 → CLM-009.3/.10/.5/.7/.12.
  - Rule-3 pointers to a register row: CLM-006 and CLM-025 → REGISTER-1.
  - **Without SEE rows (43):** STALE_SPECIFICATION 14 · IMPLEMENTED_DIFFERENTLY 8 · NOT_AUDITABLE 8 · ALIGNED 7 ·
    PARTIALLY_IMPLEMENTED 3 · AUTHORITY_CONFLICT 1 · DOCUMENTED_UNIMPLEMENTED 1 · REMAINING_STATE_MISMATCH 1.
- **Split rate:** 3 of 29 units split, into 21 rows. None of them lists SubItems.
  - SEC-2 has three numbered obligations, which take different Dispositions.
  - CLM-009 has twelve REQ rows.
  - CLM-021 has six principles.
  - CLM-012 (AC-001) and CLM-018 (VER-001) each list one sub-item and are single rows that name it.
- **Errata:** none (forward pass only).

## 2. Least-confident rows (no LOW rows; the closest MEDIUM calls, with the alternative reading)

- **SEC-2.1**, STALE_SPECIFICATION.
  - Alternative: ALIGNED, if "daemon" is read as the retained `RuntimeDaemon` class behind the socket API.
  - Chosen reading: D-APP-127 names the PKG-03 architecture clauses for revision, and the text names the retired
    shared daemon.
- **CLM-009.1**, IMPLEMENTED_DIFFERENTLY.
  - Alternative: ALIGNED. REQ-001 allows "or equivalent runtime service", and the Runtime `TurnCoordinator` is one.
  - Chosen by the REACH rule: the App TurnEngine is UNREACHED, and the live path uses another mechanism.
- **CLM-009.7 / CLM-021.5**, STALE_SPECIFICATION.
  - Alternative: ALIGNED, because the eight names are still emitted.
  - Chosen reading: the requirement restates the SPEC §11 closed set that D-GOV-43 superseded.
- **CLM-009.10 / CLM-021.2**, AUTHORITY_CONFLICT (R4).
  - Alternative: ALIGNED, if Codex `method`/`params` carried inside `codex.notification` is taken to be the
    "adapter metadata" K-ENGINE-4 allows.
  - Chosen reading: K-EVENT-1/6 and SPEC §11 (amended) require upstream payloads to be preserved. K-ENGINE-4 and
    SPEC §10.3 (unamended) forbid provider-shaped public events. DIRECTIVE §0 cannot rank two CONTRACT rows.
- **CLM-009.12**, ALIGNED. Alternative: UNKNOWN, because "this slice" no longer maps to a distinct code change.
- **REM-1**, ALIGNED (the item is open and the code lacks it).
  - Alternative: LIFECYCLE_REASSESSMENT_REQUIRED.
  - Reason: the item's own text mixes Codex-native `[agents]` delegation with a dependency on the legacy
    DEL-08-04 managed-delegation bridge and a legacy `session-manager.ts` write locus (touches R4-Q1).
- **CLM-009.3**, IMPLEMENTED_DIFFERENTLY.
  - Alternative: AUTHORITY_CONFLICT. SPEC §10.4, unamended, still has the route obtain the lock.
  - Chosen reading: SPEC §11 and §17.1, as revised, are read as consistent on route thinness.

## 3. Register-defect summary

- **REGISTER-1** (STALE_SPECIFICATION). The `_REFERENCES.md` CONTRACT, SPEC and PRD values are recorded as `MATCH`,
  but none reproduces at `00115c719` (`HASH-RECOMPUTE@00115c719`). The DIRECTIVE, TYPES and PLAN hashes were
  recomputed and still match. SoW CLM-004, 006, 012, 018 and 025 restate the failing values; CLM-006 and CLM-025
  point to REGISTER-1 with `SEE:`.
- **REGISTER-2** (STALE_SPECIFICATION). `Dependencies.csv` DEP-03-02-014 is an ACTIVE/PENDING edge on Root
  DEL-02-11. `_STATUS.md` L14 records Root DEL-02-11 as retired under D-GOV-43.
- **REGISTER-3** (STALE_SPECIFICATION, ALSO:REMAINING_STATE_MISMATCH). DEP-03-02-015 still describes the pre-A2
  daemon target with "Root location TBD".
- **REGISTER-4** (REMAINING_STATE_MISMATCH, tie-break 2b). `_REFERENCES.md` reuses REF-009 and REF-010 for two
  different sources each.
- **Related carrier rows:**
  - SEC-3: the seating note says DEP-009/010 still "await" an extract pass, which ran on 2026-09-05.
  - STATE-1: `_CONTEXT.md` still uses daemon-topology wording.
  - CLM-015: the text says "all remain PENDING", but DEP-006..010 have been SATISFIED since 2026-07-12.
- **Not raised as a row:** MEMORY.md and the `_STATUS.md` History entry dated 2026-08-02 cite
  `frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`. That file no longer
  exists at the frozen basis. Both entries are dated history, and D-APP-127 preserves daemon-era records unchanged.

## 4. Direction and cause

- **Main CauseTags:**
  - RUNTIME_EXTRACTION: the lifecycle, lock and persistence now live in `projects/chirality-runtime`
    (`TurnCoordinator`, `TurnRegistry`, `RuntimeService`), composed into the App-owned Runtime service.
  - CARRIER_PROPAGATION: D-APP-127 reached `_STATUS.md` only, so the SoW, `_CONTEXT.md` and `Dependencies.csv`
    were not revised.
  - A2_TOPOLOGY: a route disconnect no longer ends the turn; the Runtime owns the turn and lock.
  - LIFECYCLE_GATE_PENDING: the delegation-policy binding in REM-1 is not selectable.
  - CODEX_SOLE_ENGINE: the event contract and SSE names.
  - DOC_HYGIENE: the reference hashes.
  - PRE_V3_DRIFT: the dependency-record lag from 2026-07-12.
- **CAUSE2 secondaries used:** A2_TOPOLOGY, CARRIER_PROPAGATION, CODEX_SOLE_ENGINE, FACADE_DEPRECATION,
  RUNTIME_EXTRACTION, PRE_V3_DRIFT, DOC_HYGIENE, LIFECYCLE_GATE_PENDING.
- **GOV records cited:**
  - D-APP-127, D-GOV-43, D-APP-108, D-APP-109, D-APP-56 and D-APP-38.
  - The amended CONTRACT K-EVENT-1/3/4/6 and SPEC §11/§17.1 (D-GOV-43).
- **CONTEXT record used:** `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md` §3.
  It says the Runtime owns the active turn and that a renderer disconnect does not interrupt it.
- **Searches behind each NONE_FOUND DirectionEvidence** (CLM-006, CLM-025, REGISTER-1, REGISTER-4):
  - `_DECISIONS/_REGISTER.md`: the D-APP-38, D-APP-127 and D-APP-108/109 rows.
  - The DIRECTION_RECORD_INDEX entries for turn, lock, delegation and re-platform (the HANDOFF,
    `plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md` and the SCA-APP-008 D-GOV-43
    revision).
  - No record defers the reference refresh or the RefID numbering.
- **R4 questions:**
  - R4-Q2 on CLM-009.2: the Codex adapter has not been through K-ENGINE-2; the only conformance fixtures are
    scripted Claude SDK and Pi.
  - R4-Q1 on CLM-004: the Claude SDK `settingSources` condition from SPEC §12.2, unamended.
  - Plain R4 on CLM-009.10 and CLM-021.2: the event-contract tension.
- **How reach was confirmed:**
  - Runtime side:
    - `electron/main.ts` `resolveRuntimeServiceEntry` forks `packages/daemon` `standalone-bin`.
    - That runs `standalone.ts` and then `app-owned-composition.ts:226-227`, which builds `RuntimeService` with
      `TurnCoordinator` and `TurnRegistry`.
    - `runtime-daemon.ts:812-820` sends the socket turn action to `turns.start`.
  - App side: the Next route handler `turn/route.ts` goes through `getDaemonHarnessPort` to
    `RuntimeDaemonHarnessPort`.
  - Disagreement with REACHABILITY.csv: the map reaches `core/*` through `electron/main.ts>attachment-picker.ts>core/index.ts`,
    a barrel chain. That chain is not the path that executes the code. The LIVE tag is kept, on the service-entry chain.
  - `frontend/src/lib/harness/turn-engine.ts` and the SDK managers are imported only by `lib/harness/runtime.ts`
    (which nothing in the product imports) and by tests. They are tagged `REACH=LEGACY_ONLY`, noted UNREACHED,
    consistent with the map.
- **PostReleaseBasis:** NO on every row.
  - None of the relied-on lines blames to the four post-release commits.
  - The files checked with `blame -L` were `app-owned-composition.ts:226-228`, `runtime-daemon.ts:205-210,810-820`
    and `session-store.ts:105-120,240-290,940-975`.
  - I narrowed the `app-owned-composition` citation to 226-227 because line 228 blames to `da95ec194` and is not
    relied on.

## 5. Method friction

- **Superseded SoW sections.** The SoW's controlling SCA-APP-010 section declares every older section "dated
  compatibility history", but the index still makes those sections audit units.
  - I judged them on the live path, as REQ rows. RETIRED_BY_RULING does not fit, because no ruling names them.
  - Proposal: allow one row per superseded section when the deliverable's own controlling section demotes it.
- **Rule 3 of the tie-break versus MR-4.** Rule 3 asks for `SEE:` to a REGISTER row. The validator then counts
  such rows as MR-4 SEE rows even when they carry other content.
  - I used `SEE:` only where the row's substance was the restated register value (CLM-006, CLM-025). CLM-004,
    CLM-012 and CLM-018 name REGISTER-1 in prose instead.
  - Proposal: a separate token (e.g. `REG:`) for register pointers.
- **The `(context)` LatestDecision rule** conflicts with the rule that one value is allowed per row, where a row
  turns on both a governing and a context ruling. I kept the governing ruling in the field.

## 6. Effort

- **Read:** about 30 files or file ranges.
- **Deliverable folder:** all carriers. Of the run records, only the three 2026-09-05 headers.
- **Governing docs:** targeted sections of CONTRACT, SPEC, PRD and DIRECTIVE §0, plus D-APP-127.
- **Code:** about 12 App and Runtime source files and about 8 test files, at the line ranges cited.
- **Context budget:** adequate, not tight.
