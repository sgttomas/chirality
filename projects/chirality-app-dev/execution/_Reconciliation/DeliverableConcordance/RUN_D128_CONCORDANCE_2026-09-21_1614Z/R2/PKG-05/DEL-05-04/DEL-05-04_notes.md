# DEL-05-04 — forward-pass notes (R2, PKG-05)

Ledger: `DEL-05-04_claims.csv` (57 rows, validator `RESULT PASS errors=0 warnings=0`). Basis: frozen tree `00115c719`.
Rule notice RUN_BASIS Addendum 6 (the legacy-versus-live subject test for R4-Q1) arrived **before** sealing and is applied:
R4-Q1 is cited on every row where the only code meeting the claim is `REACH=LEGACY_ONLY`. Product-behaviour rows of that kind
also carry `ALSO_MODULE:ALIGNED`.

## 1. Census

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 37 | STALE_SPECIFICATION 13, ALIGNED 12, IMPLEMENTED_DIFFERENTLY 4, STALE_VERIFICATION 3, PARTIALLY_IMPLEMENTED 3, DOCUMENTED_UNIMPLEMENTED 2 |
| CONTEXT_CLAIM | 10 | NOT_AUDITABLE 8, STALE_SPECIFICATION 2 |
| REMAINING_WORK | 3 | ALIGNED 1, PARTIALLY_IMPLEMENTED 1, REMAINING_STATE_MISMATCH 1 |
| REGISTER_DEFECT | 3 | STALE_SPECIFICATION 3 |
| ACCEPTANCE | 2 | PARTIALLY_IMPLEMENTED 1, UNKNOWN 1 |
| STATE_ASSERTION | 2 | STALE_SPECIFICATION 2 |

Dispositions overall: STALE_SPECIFICATION 20, ALIGNED 13, NOT_AUDITABLE 8, PARTIALLY_IMPLEMENTED 5, IMPLEMENTED_DIFFERENTLY 4,
STALE_VERIFICATION 3, DOCUMENTED_UNIMPLEMENTED 2, REMAINING_STATE_MISMATCH 1, UNKNOWN 1.

- **SEE rows (counted separately):** 5 of 57. CLM-007 and CLM-026 → REGISTER-1; CLM-010.1 and CLM-010.9 → CLM-003.1;
  CLM-010.14 → CLM-004.2. Without them there are 52 primary dispositions.
- **Split rate:** 5 of 30 indexed units split (17%), giving 29 rows:
  - CLM-003: 3 rows (Attributes table);
  - CLM-004: 3 rows (Conditions table);
  - CLM-010: 19 rows, one per REQ-001..REQ-019;
  - CLM-013: 2 rows (documentation, AC-001);
  - CLM-019: 2 rows (records, VER-001).
  Run-local rows: REGISTER-1..3. No STATE-n rows.
- **HumanDecisionNeeded:** NO 35, R4-Q1 14, R4 7, `R4-Q1; R4` 1.
- **Confidence:** HIGH 31, MEDIUM 24, LOW 2.
- **No errata file** (pass 1).

## 2. Least-confident rows

- **CLM-010.7 (REQ-007), LOW: IMPLEMENTED_DIFFERENTLY.**
  - What the code does: Claude SDK fields stay under `sdkLinkage`. But the public `HarnessEventType` union carries the
    provider-named `codex.notification`, `codex.steer`, `codex.request` and `codex.request.resolved`, and `TranscriptItem`
    carries `nativeItemId` and `providerThreadId`.
  - Alternative 1, AUTHORITY_CONFLICT: CONTRACT K-ENGINE-4 is unamended, but the amended K-EVENT-6 says upstream
    notifications cross with their method names and identifiers preserved.
  - Alternative 2, ALIGNED: the `codex.*` envelope counts as Chirality-owned and the provider payload counts as adapter
    metadata.
- **CLM-019.2 (VER-001), LOW: UNKNOWN.**
  - What was found: VER-001 is the SoW-conversion check. The Root `tools/scope_of_work` render and test tooling exists, but
    I found no DEL-05-04 run record of it.
  - Alternative: ALIGNED if it ran centrally, or DOCUMENTED_UNIMPLEMENTED if it never ran for this SoW.
- **MEDIUM rows worth a second look:**
  - **CLM-003.3 and CLM-010.8 (redaction absent on the live path).** I grepped `redact`, `sanitiz`, `secret`, `scrub` and
    `mask` over `projects/chirality-runtime/packages/*/src`. The only hits are type fields and Codex stderr account-text
    masking. `delegated-engine-adapter.ts:282,289` persists `params` raw. I did not trace every event producer, so a
    producer-side redaction elsewhere would change these rows to ALIGNED.
  - **CLM-004.2, CLM-010.14, CLM-010.15, CLM-010.19 and REM-2 (continuation from replay).** Alternative: read the
    continuation feature as the V3-01 work arriving early, and REQ-014 as out of date rather than diverged
    (STALE_SPECIFICATION).
  - **REM-3.** Alternative: PARTIALLY_IMPLEMENTED. The Return's "never transfers draft/context" clause is strained by
    continuation, and "review PASS" is unevidenced.

## 3. Register-defect summary

- **REGISTER-1: `_REFERENCES.md` hash drift.** REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) record MATCH, but none
  reproduces at `00115c719` (HASH-RECOMPUTE, `REFERENCE_HASHES.csv`).
  - DIRECTIVE, TYPES, PLAN and the three software-decomp workflow hashes do reproduce (recomputed here).
  - The SoW CLM-007 table also names a REF-007 `AGENT_SOFTWARE_DECOMP.md` that does not exist at the root.
- **REGISTER-2: `Dependencies.csv` DEP-05-04-008 is SATISFIED** on the strength of "read-time replay redaction". Only the
  LEGACY_ONLY `session-events.ts` meets it (R4-Q1).
- **REGISTER-3: DEP-05-04-005 notes describe the pre-extraction path** (ADQ-08/D-APP-41 folder conversion; the replay route
  through the session manager).
  - REM-2 still lists DEP-05-04-005/006 as dependencies, while the CSV marks both SATISFIED.
- **Carriers without D-APP-127/D-GOV-43:** the evidence pack shows none of the five DEL-05-04 carriers cites them. The SoW
  still states the pre-A2 project-local canonical store. That staleness is carried on CLM-003.1 and the rows that SEE it.

## 4. Direction and cause

- **Main cause, RUNTIME_EXTRACTION (23 rows).** Replay moved from the App-local `session-events.ts` parser to the Runtime:
  - `SessionStore.replayDetailed`;
  - `runtime-daemon.ts` `/replay`;
  - `deriveTranscriptView` in `@chirality/runtime-contracts`.

  The SoW, Assessment and Dependencies still point at the App files. `frontend/src/lib/harness/transcript-replay.ts` and
  `event-schema.ts` no longer exist, and the harness-contract file is a deprecated re-export with no product importer.

  Secondary causes on these rows: CAUSE2:A2_TOPOLOGY, FACADE_DEPRECATION and DOC_HYGIENE.
- **Governing direction used.**
  - D-APP-73 (central sessions; lazy non-destructive migration; it prospectively extends D-APP-41).
  - D-APP-127, whose D-GOV-43 tranche `23b3879b3` amended CONTRACT K-EVENT-4 to name
    `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl` as canonical, and amended K-EVENT-6.
  - SPEC §8.2 still shows the project-local layout. The DIRECTIVE §0 order (CONTRACT above SPEC) resolves that, so
    AUTHORITY_CONFLICT is not used.
- **V3_RELEASE_SCOPE (5 rows): the "Continue this chat" continuation from the replay lens.**
  - Introduced in `0ed1a1a7f`, 2026-09-11.
  - It contradicts the SCA-APP-004 read-only posture (REQ-014, REQ-015, REQ-019) and anticipates V3-01.
  - CONTEXT: `execution/_Coordination/AgentRuns/APP_V3_TRIAL_COMPLETION_20260910/R14_FUNCTIONAL_FINDINGS.md` L38-40, and
    the v3 plan AT-036 via `_STATUS.md`.
  - No register ruling: `_REGISTER.md` grep for `continu`/`resum` found only D-APP-10, which is unrelated. These rows cite
    `R4`.
- **Other causes.**
  - CODEX_SOLE_ENGINE: CLM-010.7.
  - SHELL_REDESIGN: REM-3.
  - DOC_HYGIENE: hash, reference and conflict-table rows.
- **NONE_FOUND searches.**
  - Redaction and verification-gap rows (CLM-003.3, CLM-010.8, CLM-010.10, CLM-012, CLM-013.2, CLM-018, REGISTER-2): grep of
    `_DECISIONS/_REGISTER.md` for redact, replay and session store, plus a check of the CONTEXT `AgentRuns/APP_V3_*` trial
    findings. Neither records the loss of replay redaction on the Runtime path.
  - CLM-007, CLM-026 and REGISTER-1: the register's D-APP-38 row only.
  - CLM-027: no DEL-05-04 conflict row in the register.
- **Named R4 questions.**
  - R4-Q1 on 15 rows: the redaction rows; the rows naming the `replayHarnessEvents` parser or `session-events.ts` as the
    parser of record; the verification rows whose malformed-tail and redaction fixtures run only the LEGACY_ONLY parser via
    `fake-daemon-harness-port.ts`.
  - R4-Q2, R4-Q3 and R4-Q4 do not apply.

## 5. Method friction

- **REACHABILITY misses re-export facades under `frontend/packages/**`.** `frontend/packages/harness-contract/src/transcript-replay.ts`
  is not in the map, and I tagged it `REACH=TEST_ONLY` by grep: only `harness-contract-rollback.test.ts` imports the
  package.
  - Proposal: extend the map to `frontend/packages/**`.
- **"Entry points" can be a 404 page.** `transcript-stream-view.tsx` is LIVE only through `AppShell`, which only
  `app/not-found.tsx` renders.
  - Proposal: let workers flag entry-by-404-page reach explicitly.
- **Stale test docstrings.** The route docstring (`route.ts:15`, "reuses `replayHarnessEvents`") and the routes-test replay
  cases (which run a test fake over the legacy parser) make gate-transcript PASS look like live-path verification. Grep hits
  on such docstrings can mislead.
- **VER-001 has no rule.** SoW-conversion VER items (the SoW-render pipeline) are not product claims.
  - Proposal: add a CONTEXT-like disposition, or route VER-001 to a corpus-wide row.
- **Splitting Conditions/Attributes tables.** They were split so that ALIGNED and non-aligned table rows are not averaged.
  The rule allows it ("table of independently dispositionable rows"), but it raises the row count for this deliverable.
- **Coverage gaps (no forward row owned here).**
  - The replay-continuation feature (`chat-panel.tsx:678-742` resume and `recoverActiveTurn`) is product behaviour whose
    owning carrier is unclear. It may belong to DEL-02-02 or DEL-08-02, not DEL-05-04.
  - Recorded instruction-basis history in the replay payload (`runtime-daemon.ts:801-808`) has no DEL-05-04 SoW clause.

## 6. Effort

- **Files read:** about 40.
  - DEL-05-04 deliverable files: SoW, `_STATUS`, `_CONTEXT`, `_REFERENCES`, `MEMORY`, `Dependencies.csv`, Assessment
    headers.
  - Runtime: `session-store`, `runtime-daemon` replay handler, `transcript-replay`, `event-schema`.
  - App: route, port, `session-events`, `selected-session-replay`, lens, shell, right-panel, chat-panel resume, test
    headers, section9 manifest.
  - Governance: CONTRACT K-EVENT/K-ENGINE rows, SPEC §8–9, DIRECTIVE §0, D-APP-73 ruling, register rows.
  - Two gate transcripts.
- **Git:** blame -L on the touched files `session-store.ts`, `runtime-daemon.ts` and `client.ts`. No relied-on line blames
  to `da95ec194`, `cb08dbe2f`, `9ecbdecdf` or `ccb95e06a`, so every row has PostReleaseBasis NO.
- **Context budget:** adequate, not tight. PREGATHER was used as a map, and every cited line was re-read.
