# DEL-03-03 forward-pass notes (R2, PKG-03)

Deliverable: DEL-03-03 Harness API and SSE Compatibility Adapter. Basis: frozen tree at `00115c719`.
Ledger: `DEL-03-03_claims.csv`, 59 rows. The manager's tie-break rule for STALE_SPECIFICATION versus
REMAINING_STATE_MISMATCH (RUN_BASIS Addendum 5) and the R4-Q4 token (Addendum 4) were applied before
sealing. No row turns on R4-Q4.

## 1. Census

**Rows:** 59 in total.

- 54 rows come from the 28 indexed units (27 CLM plus REM-1).
- 3 are `REGISTER-n` rows and 2 are `STATE-n` rows.

**Split rate:** 5 of 28 units were split (17.9%).

| Unit | Rows | Split basis |
|---|---:|---|
| CLM-003 | 7 | Attribute table |
| CLM-004 | 5 | Condition table |
| CLM-005 | 4 | Construction table |
| CLM-009 | 10 | Numbered items DEL-03-03-REQ-001..010 |
| CLM-023 | 5 | Principles table |

The claim index lists only two sub-items for this deliverable, AC-001 (in CLM-013) and VER-001 (in
CLM-020). Each unit holds one item, so neither unit was split.

**By ClaimType:**

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 35 |
| CONTEXT_CLAIM | 10 |
| STATE_ASSERTION | 6 |
| ACCEPTANCE | 4 |
| REGISTER_DEFECT | 3 |
| REMAINING_WORK | 1 |

**By Disposition** (20 SEE rows are counted separately, per MR-4):

| Disposition | All rows | Non-SEE | SEE |
|---|---:|---:|---:|
| STALE_SPECIFICATION | 28 | 17 | 11 |
| PARTIALLY_IMPLEMENTED | 8 | 5 | 3 |
| NOT_AUDITABLE | 7 | 7 | 0 |
| ALIGNED | 7 | 7 | 0 |
| IMPLEMENTED_DIFFERENTLY | 4 | 1 | 3 |
| AUTHORITY_CONFLICT | 4 | 1 | 3 |
| REMAINING_STATE_MISMATCH | 1 | 1 | 0 |

**By Confidence:** HIGH 26, MEDIUM 32, LOW 1.

No errata file exists yet, so there are no errata-applied figures.

## 2. Least-confident rows (with the alternative reading)

- **STATE-2 (LOW).** Sealed: STALE_SPECIFICATION. `RouteAdapterTestIndex.md` and
  `SSE_Compatibility_Fixture_README.md` carry no history marker, although `_STATUS.md:21` calls them
  history.
  - Alternative: no defect. They are dated 2026-07-18 agent findings, and `_STATUS` already
    classifies them.
- **CLM-003.3 and its SEE rows (MEDIUM).** Sealed: IMPLEMENTED_DIFFERENTLY with R4-Q1. The route
  takes no lock and makes no TurnEngine call; the Runtime service owns both.
  - Alternative: AUTHORITY_CONFLICT. SPEC 10.4 is unamended, while SPEC 17.1 was amended to say the
    routes are "thin loopback adapters over the Runtime service's socket API".
- **CLM-003.5 (MEDIUM).** Sealed: STALE_SPECIFICATION on the words "stable and compact".
  - Alternative: ALIGNED on the separation clause, which amended K-EVENT-1 keeps.
- **CLM-003.6 and its SEE rows (MEDIUM).** Sealed: AUTHORITY_CONFLICT with R4.
  - Alternative: no conflict, if the upstream method and params inside a Chirality-typed
    `codex.notification` count as "adapter metadata" under K-ENGINE-4.
- **CLM-013 (MEDIUM).** Sealed: PARTIALLY_IMPLEMENTED on AC-001.
  - Alternative: STALE_SPECIFICATION, because AC-001 rests on "preserved legacy requirements" that
    D-GOV-43 partly superseded.
- **REM-1 (MEDIUM).** Sealed: REMAINING_STATE_MISMATCH (tie-break rule 2a). The gate's premise, the
  transport repair on the production path, is met in live code, yet the item stays NOT_SELECTABLE.
  - Alternative: PARTIALLY_IMPLEMENTED. The code has landed, but the Return evidence bundle and the
    SSE fixtures do not exist.
- **CLM-004.3 (MEDIUM, ALIGNED).** The terminal-signal semantics match amended SPEC 11.
  - Alternative: the process-level `process:exit` framing is itself part of the superseded
    eight-name set.

## 3. Register-defect summary

- **REGISTER-1: `_REFERENCES.md` hashes.** REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD)
  record MATCH, but none reproduces at `00115c719`.
  - Evidence: `HASH-RECOMPUTE@00115c719`.
  - DIRECTIVE, TYPES, PLAN and the three `workflows/software-decomp` references do reproduce.
  - These SEE rows restate REGISTER-1 as current: CLM-004.5, CLM-009.9 and CLM-027.
  - These rows cite it with extra findings of their own: CLM-006, CLM-016 and CLM-024.
- **REGISTER-2: `_DEPENDENCIES.md` mirror is stale.**
  - DEP-03-03-009 is shown ACTIVE; the CSV says RETIRED.
  - DEP-03-03-011 is missing from the Active Rows table.
  - The block labelled "current" says ACTIVE 9; the CSV has 10.
  - Declared Upstream/Downstream still says "TBD - no accepted dependency edges".
  - Line 53 carries a machine-specific absolute path (not reproduced here).
- **REGISTER-3: `Dependencies.csv` DEP-03-03-011** still gates on the "closed schema v2", which
  D-GOV-43 retired.
  - `_STATUS` V3-01 Depends omits 011, although the CSV says V3-01 consumes it.
- **Other SoW register-type findings:**
  - CLM-006: SoW REF-007 names `agents/AGENT_SOFTWARE_DECOMP.md`, which is absent at the frozen
    basis and differs from `_REFERENCES.md` REF-007.
  - CLM-016: "no accepted dependency edges extracted yet" is false.
  - CLM-027: the conflict table is stale, and it omits the D-GOV-43 adapter-boundary tension.

## 4. Direction and cause

**Main CauseTags:**

| CauseTag | Rows | Covers |
|---|---:|---|
| CODEX_SOLE_ENGINE | 21 | The event representation; the adapter boundary |
| A2_TOPOLOGY | 8 | Route, lock and disconnect semantics |
| PRE_V3_DRIFT | 8 | Missing fixtures and UI event docs |
| DOC_HYGIENE | 7 | Hashes and dependency mirrors |
| CARRIER_PROPAGATION | 1 | REM-1 |

**Secondary causes:**

- `CAUSE2:CARRIER_PROPAGATION` is on every stale SoW, `_CONTEXT` or `Dependencies.csv` row. D-APP-127
  reached only `_STATUS.md`; the application map shows ScopeOfWork, `_CONTEXT`, Dependencies.csv and
  `_REFERENCES` all Revised=NO.
- `CAUSE2:RUNTIME_EXTRACTION` is on CLM-003.3 and CLM-026.
- `CAUSE2:A2_TOPOLOGY` is on REM-1.
- `CAUSE2:CODEX_SOLE_ENGINE` is on CLM-020.
- `CAUSE2:PRE_V3_DRIFT` is on CLM-016 and REGISTER-2.

**Governing basis:**

- D-APP-127 names DEL-03-03, so MR-11 applies to this deliverable. It retains and repairs the routes
  and retires the closed event vocabulary.
- SPEC 11, TYPES 7.4, PRD 9.1/9.3 and CONTRACT K-EVENT-1/K-EVENT-6 were amended under D-GOV-43.
  DIRECTIVE 0 places them above the SoW, so the SoW restatements are STALE_SPECIFICATION rather than
  conflicts.
- The only unresolved governing tension is CLM-003.6 (R4). Amended K-EVENT-1/K-EVENT-6 and SPEC 11
  ("preserve upstream method names") pull against unamended K-ENGINE-4 and SPEC 10.3 ("translate
  external message names; provider values only as adapter metadata").

**CONTEXT records used:**

- `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md`, "Transport
  repair and the disconnection rule (settled)".
- `RUN_LOG.md` in the same folder, entry 2026-09-12T15:40Z (the proxy keepalive fix). Used for REM-1.

**Searches behind each NONE_FOUND:**

- `_DECISIONS/_REGISTER.md` was grepped for `DEL-03-03`, "fixture capture", "route adapter" and "SSE
  compat". Only the D-APP-65 row matched; it authorised the index and README.
- Also checked: the DECISION_HITS rows for DEL-03-03, and the APP_V3_CODEX_HOST_REPLATFORM_20260912
  HANDOFF and RUN_LOG for DEL-03-03, "keepalive", "transport repair" and "S-2".
- None of these explains the missing fixtures or UI event docs, the stale hashes, or the stale
  dependency mirror.

**How reach was confirmed:**

- **Route handlers.** Each route under `frontend/src/app/api/harness/**` is an executed Next route
  (map: LIVE).
- **Runtime chain.** `electron/main.ts:455-471` launches the packaged `runtime-service/standalone-bin`.
  That leads to `standalone.ts`, then `app-owned-composition.ts`. At line 214 it registers
  `createDelegatedEngineAdapter`; at line 226 it builds the `TurnCoordinator`; at line 228 it builds
  `RuntimeDaemon`. So `delegated-engine-adapter.ts`, `turn-coordinator.ts`, `runtime-daemon.ts` and
  `turn-registry.ts` are LIVE through execution, not only through the barrel chain the map shows
  (`electron/attachment-picker.ts > core/index.ts`).
- **Renderer.** `chat-panel.tsx` is mounted by `loop-shell.tsx`, `app-shell.tsx` and
  `loop-tertiary-shell.tsx`. It renders `TurnActivityDisclosure`, which uses
  `lib/shell/turn-activity.ts` and, through it, `deriveCodexNotifications`.
- **Legacy modules.** `turn-engine.ts`, `sdk-message-mapper.ts` and `harness-ui-bridge.ts` are
  LEGACY_ONLY, which agrees with the map.
- **Tests.** `routes.test.ts` drives LIVE routes through a fake daemon port over the retained
  in-process runtime, so it is tagged TEST_ONLY.
- **Result.** No disagreement with REACHABILITY.csv for the cited modules.

**PostReleaseBasis:**

- Blamed ranges: `client.ts` 190-212 and 755-770; `runtime-daemon.ts` 60-64 and 956-1030;
  `app-owned-composition.ts` 214-226.
- None of these lines blames to da95ec194, cb08dbe2f, 9ecbdecdf or ccb95e06a. The touched ranges are
  `client.ts` 50-54 and 363-383, and `runtime-daemon.ts` 15-16, 57, 169-171 and 660-686.
- No other cited file appears in TOUCHED_PATHS.csv, so every row is `NO`.

**Cross-deliverable observations:**

- Many live v3 routes are not in the SPEC 17.1 catalog: `session/[id]/turn/stream`, `turn/state`,
  `requests`, `steer`, `native-plan/*`, `methods`, `roles` and `hosted-bootstrap/*`.
- The retained `routes.test.ts` case "persists ... cancellation when the SSE reader disconnects"
  asserts the pre-D-GOV-43 disconnect semantics.

## 5. Method friction

- **SEE pointers to REGISTER rows.** Under tie-break rule 3 a SoW row that restates a register MATCH
  as current points to the REGISTER row with `SEE:`. That makes REGISTER rows SEE targets. The
  validator accepts this.
  - Proposed revision: state explicitly that SEE may target run-local REGISTER keys, and that such a
    row still counts once in the SEE census.
- **CauseTag for event-representation changes.** Neither CODEX_SOLE_ENGINE nor A2_TOPOLOGY describes
  the D-GOV-43 retirement of the closed event vocabulary exactly. I used CODEX_SOLE_ENGINE (upstream
  App Server events).
  - Proposed revision: a vocabulary note, or `OTHER:EVENT_REPRESENTATION`.
- **SubItems do not list REQ items.** CLM-009's numbered items (DEL-03-03-REQ-001..010) are absent
  from the index's SubItems column. The unit was split anyway, under the "separately numbered REQ
  items" rule.

## 6. Effort

- About 45 files or excerpts were read, including the deliverable files (SoW, `_STATUS`, `_CONTEXT`,
  MEMORY, `_REFERENCES`, `_DEPENDENCIES`, `Dependencies.csv`, Assessment, and the heads of the index
  and README).
- Also read: the evidence pack; the D-APP-127 record; the SPEC, CONTRACT, TYPES, PRD and DIRECTIVE
  sections; about 15 App route and lib files; about 8 Runtime package files; test case names; and
  the CONTEXT handoff and run log.
- `_SEMANTIC*.md` and `_run_records/**` were not read; no unit depends on them.
- The context budget was adequate, not tight.
