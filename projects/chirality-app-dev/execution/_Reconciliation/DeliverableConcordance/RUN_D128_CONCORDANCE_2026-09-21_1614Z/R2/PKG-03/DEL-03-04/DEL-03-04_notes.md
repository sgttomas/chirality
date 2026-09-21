# DEL-03-04 — forward-pass notes (R2, PKG-03)

Deliverable folder (frozen basis `00115c719`):
`projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-04_Interrupt_Cancel_and_Terminal_Outcome_Handling/`.
In the ledger, `ScopeOfWork.md:NN`, `_STATUS.md:NN` and the like are relative to that folder.
The owner additions relayed by the PKG-03 manager (RUN_BASIS Addenda 4 and 5: the R4-Q4 token
and the STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break) were applied before sealing.

## 1. Census

- **Rows:** 69 in total: 60 on indexed units (31 units) and 9 run-local (STATE-1..5, REGISTER-1..4).
- **Split rate:** 5 of 31 units were split (16%), giving 34 sub-rows:
  - CLM-004: 6 Conditions-table rows;
  - CLM-009: 15 REQ items (REQ-001..014 plus REQ-006A);
  - CLM-010: 5 Standards rows;
  - CLM-013: .1 is the UPD-117 note, .2 is AC-001;
  - CLM-022: 6 numbered principles.

  CLM-013 and CLM-019 each list one sub-item, so they satisfy V-SUBITEMS.

**Rows by ClaimType**

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 39 |
| CONTEXT_CLAIM | 15 |
| STATE_ASSERTION | 7 |
| ACCEPTANCE | 4 |
| REGISTER_DEFECT | 4 |

**Rows by Disposition** (sealed; no errata)

| Disposition | All rows | SEE rows | Non-SEE rows |
|---|---:|---:|---:|
| STALE_SPECIFICATION | 25 | 6 | 19 |
| ALIGNED | 20 | 3 | 17 |
| NOT_AUDITABLE | 10 | 0 | 10 |
| PARTIALLY_IMPLEMENTED | 8 | 2 | 6 |
| AUTHORITY_CONFLICT | 2 | 0 | 2 |
| REMAINING_STATE_MISMATCH | 2 | 0 | 2 |
| IMPLEMENTED_DIFFERENTLY | 1 | 0 | 1 |
| STALE_ASSESSMENT | 1 | 0 | 1 |
| **Total** | **69** | **11** | **58** |

**Other counts**

- SEE rows (MR-4), 11 in total:
  - CLM-009.4, CLM-027 → CLM-004.2;
  - CLM-009.5, CLM-028 → CLM-004.3;
  - CLM-009.13 → CLM-004.6;
  - CLM-010.3, CLM-022.5 → CLM-009.11;
  - CLM-022.2 → CLM-009.6;
  - CLM-022.3 → CLM-009.12;
  - CLM-018 → CLM-011;
  - CLM-031 → CLM-013.1.
- Confidence: 37 HIGH, 27 MEDIUM, 5 LOW.
- HumanDecisionNeeded: 66 `NO`; 2 `R4` (CLM-009.7, CLM-022.4); 1 `R4-Q1` (CLM-010.4). No row turns on R4-Q4.

## 2. Least-confident rows (with alternative readings)

- **CLM-009.12 (REQ-011)** and **CLM-022.3 (SEE):** STALE_SPECIFICATION, because a disconnect no
  longer releases the turn: under D-GOV-43 the turn keeps running. *Alternative:* ALIGNED, if the
  requirement means only that no session is left locked. The live path meets that, since the lock is
  released at the turn's own terminal (`turn-coordinator.ts:487-490`).
- **CLM-013.1 (UPD-117 note)** and **CLM-031 (SEE):** STALE_SPECIFICATION, because the named basis
  `RunningHarnessTurn.cancel` is LEGACY_ONLY and inverted on the live path. *Alternative:* a dated
  snapshot note under MR-8(iv), which would make it a REGISTER row, or ALIGNED as dated history.
- **STATE-3 (MEMORY.md entries of 2026-08-15 and 2026-07-10):** STALE_SPECIFICATION. The drain-proof
  test file was deleted at `39c0bb6ab`, and disconnect `turn.cancelled` is legacy only.
  *Alternative:* ALIGNED as dated history, since `_STATUS.md:13` preserves the proof as history.
- **MEDIUM, worth checking:**
  - CLM-004.6, CLM-009.10 and CLM-009.13 (redaction): no structural redaction was found on the live
    writer or SSE path. If a redaction step exists outside `packages/core/src` and
    `packages/daemon/src`, these become ALIGNED.
  - CLM-022.4 (AUTHORITY_CONFLICT on the `codex.*` HarnessEvent types): the alternative reading treats
    the `codex.*` envelopes as "adapter metadata" under K-ENGINE-4, which would make the row ALIGNED.

## 3. Register-defect summary

- **REGISTER-1:** `_REFERENCES.md` records MATCH for CONTRACT, SPEC and PRD, and none of the three
  reproduces (`HASH-RECOMPUTE@00115c719`). The worker also recomputed DIRECTIVE, TYPES, PLAN and
  `workflows/software-decomp/WORKFLOW.md`; all four still match. The following rows cite it:
  - CLM-006 and CLM-010.5, which say REF-006 is "reconciled";
  - CLM-030, which says the PRD is "current";
  - CLM-003's PRD attribute.
- **REGISTER-2:** `_DEPENDENCIES.md` says no edges have been extracted and gives stale
  SatisfactionStatus counts (NA 5 / TBD 4 against actual 6 / 3). It is STALE_SPECIFICATION under
  tie-break rule 1, with `ALSO:REMAINING_STATE_MISMATCH` in Notes.
- **REGISTER-3:** `Dependencies.csv` DEP-006, DEP-007 and DEP-009 still assume that the App owns the
  JSONL writer and the lock. That premise has been false since SCA-APP-005 and D-GOV-43.
- **REGISTER-4:** the SoW `decomposition_basis` pin (`7b0be4d8`) lags later decomposition revisions.
  The DEL-03-04 row has not changed since `16f7ed612`, so this is metadata lag only
  (REMAINING_STATE_MISMATCH, rule 2b).

## 4. Direction and cause

**Main CauseTags**

| CauseTag | Rows | What it covers |
|---|---:|---|
| A2_TOPOLOGY | 20 | Disconnect rule, SSE representation, service-shutdown interruption |
| RUNTIME_EXTRACTION | 12 | Lifecycle, mapper, writer and redaction moved into `projects/chirality-runtime` under SCA-APP-005 |
| DOC_HYGIENE | 6 | Hashes, dependency summary, pin |
| CARRIER_PROPAGATION | 1 | STATE-2 |

**CAUSE2 secondaries**

| CAUSE2 tag | Rows |
|---|---:|
| CARRIER_PROPAGATION | 8 |
| RUNTIME_EXTRACTION | 6 |
| A2_TOPOLOGY | 5 |
| CREDENTIAL_CUSTODY | 3 |
| PRE_V3_DRIFT | 1 |

**Governing records used**

- **D-APP-127.** Its governing facts say "a renderer disconnect no longer interrupts a turn", and its
  consequential applications list "PKG-03 DEL-03-01 to DEL-03-04 … clauses revised". Because the
  ruling names this deliverable explicitly, MR-11 applies: the stale SoW wording is
  STALE_SPECIFICATION with `LatestDecision = D-APP-127`. The ruling was applied only to `_STATUS.md`
  (per the application map), which gives STATE-2.
- **SCA-APP-005.** `Propagation_Plan.md` has status APPROVED_AND_APPLIED and says "ScopeOfWork
  contracts … explicitly unchanged". It re-expressed DEL-03-04 as App forwarding over Runtime-owned
  semantics.
- **SPEC §11, SPEC §17.1, PRD FR-017/FR-019 and amended CONTRACT K-EVENT-3/4/6** (all revised under
  D-GOV-43), with DIRECTIVE §0 applied over the deliverable text.
- **D-APP-40.**

**CONTEXT records used** (CTX)

- `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md` §3 (the disconnection rule).
- `SPIKE_DESIGN.md` §1 and §5, which record that service shutdown is written as `turn.interrupted`
  with reason `service-shutdown`.

**Authority handling**

- **CLM-010.4** (AUTHORITY_CONFLICT, R4-Q1): SPEC 10.4, which is unamended ("route obtains session
  lock, forwards to TurnEngine"), and PRD FR-070/071 conflict with SPEC 17.1 and 25.1 as amended.
  The amended text makes the routes thin clients that MUST NOT construct an engine runtime.
  DIRECTIVE §0 does not order clauses within one document, and D-GOV-43 does not name 10.4.
- **CLM-022.4** (AUTHORITY_CONFLICT, R4): unamended K-ENGINE-4 and SPEC 10.3 ("not provider-shaped
  except adapter metadata") conflict with amended K-EVENT-6 and SPEC §11 ("preserve upstream method
  names/payloads"). On the live path the HarnessEvent types are
  `codex.notification`/`codex.request`/`codex.request.resolved`, while terminal events are
  Chirality-owned. Terminal-only rows (CLM-009.8, CLM-009.14) are ALIGNED because they do not turn on
  this conflict.
- **CLM-009.7** (IMPLEMENTED_DIFFERENTLY, R4): D-APP-40 reserves `turn.cancelled` for disconnect and
  system cancellation. The live Runtime never writes `turn.cancelled`: service shutdown and restart
  are recorded as `turn.interrupted{reason}`, and D-GOV-43 separately makes disconnect a non-event.
  The only explanation is CONTEXT (SPIKE_DESIGN), which cannot change the Disposition.

**Searches behind NONE_FOUND**

- **Redaction** (CLM-004.6, CLM-009.10, CLM-009.13): grep for `redact|sanitiz|scrub|secret` over
  runtime `core/src` and `daemon/src`, and grep for `redact` in `frontend/src/lib/runtime-client` and
  `http.ts`. `_REGISTER.md` was searched too; its only redaction row is D-APP-67, which covers
  DEL-05-03. HANDOFF and SPIKE_DESIGN mention only e-mail redaction of stderr.
- **Documentation** (CLM-012): grep for D-APP-40 across the frontend, runtime packages and docs. It
  appears only in the legacy `turn-engine.ts`.
- **Reference refresh** (REGISTER-1, CLM-006, CLM-030) and **pin** (REGISTER-4): `_REGISTER.md` has
  no ruling that covers DEL-03-04.
- **Dependency summary** (REGISTER-2): no ruling found.

**Reach: how it was confirmed** (not the map alone)

- *App side:* the `frontend/src/app/api/harness/{interrupt,turn}/route.ts` handlers call
  `getDaemonHarnessPort()`. That goes to `runtime-daemon-harness-port.ts`, then to `RuntimeClient`
  over the socket.
- *Runtime side:* Electron main forks the packaged `runtime-service/standalone-bin.mjs`
  (`scripts/build-electron.mjs:29,38`; `runtime-service-host.ts:412`). The chain then runs:
  1. `standalone.ts:22-26`;
  2. `startAppOwnedRuntime`, which composes `RuntimeService`, `TurnCoordinator`, `TurnRegistry`,
     `RuntimeDaemon` and `CodexSupervisor`, and registers the delegated Codex adapter
     (`app-owned-composition.ts:214,226-228`).
- *Map agreement:* the map agrees for every module cited. The App `turn-engine.ts`,
  `session-events.ts`, `sdk-message-mapper.ts` and the Claude/Anthropic managers are LEGACY_ONLY,
  consistent with the map.

**PostReleaseBasis**

- `git blame -L` was run on the cited ranges in touched files:
  - `codex-supervisor.ts:387-399`: lines 391-392 blame to `da95ec194`, so the citation was narrowed
    to 395-399, which is not touched;
  - `app-owned-composition.ts:170-178` and `226-236`: line 170-171 and line 228 are `da95ec194` and
    are not cited;
  - `runtime-daemon.ts:812-828` and `955-980`, and `client.ts:575-590`: no touched lines.
- The cited `session-store.ts` ranges fall outside the touched runs (6-8 and 128-158).
- Result: every row is `NO`.

**Cross-deliverable observations**

- The decomposition row for DEL-03-04 (`:320`) and SOW-012 (`:182`) still say "forward … disconnects"
  to the daemon. This is relevant to the EXT SOW ledger.
- The frozen 2026-08-15 drain-proof test was deleted in the D-GOV-43 App commit `39c0bb6ab`.
  DEL-09-03 relied on it as input.

## 5. Method friction

- **LatestDecision** accepts only D-APP or D-GOV IDs, so an accepted SCA (SCA-APP-005) that
  explains a divergence can only appear in DirectionEvidence as `GOV:`. *Proposal:* allow `SCA-APP-nnn`
  in LatestDecision.
- **MR-4 "earliest unit"** made the REQ items SEE the earlier Conditions-table rows (for example,
  REQ-004 points to CLM-004.2). The REQ items are the more natural anchor. *Proposal:* let the
  numbered REQ item be the anchor when an earlier table row paraphrases it.
- **VerificationEvidence:** the gate transcripts give only the pass totals and a log tail. The cited
  test cases are inferred from files in the frozen tree under a suite-wide PASS, not from per-case
  lines.

## 6. Effort

- About 45 file reads or targeted range reads: the deliverable folder (all files), the governing
  SPEC, CONTRACT, PRD and DIRECTIVE slices, D-APP-127 and D-APP-40, the SCA-APP-005 plan, HANDOFF and
  SPIKE_DESIGN slices, about 12 runtime and App source files by range, and test-name greps.
- The context budget was adequate, not tight.
