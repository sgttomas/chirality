# DEL-09-03 Unit and Integration Test Expansion: R2 forward-pass notes

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-09 wave 5, pass 1. Basis: frozen tree `00115c719`.
Ledger: `DEL-09-03_claims.csv` (54 rows). The Addendum 9 rule notice (R4-Q6) arrived **before sealing**
and is applied: R4-Q6 is cited alongside R4-Q1 on the three denied-action rows (they restate K-PERM-1).

## 1. Census

Indexed units: 29 (27 CLM, 2 REM). Run-local rows: REGISTER-1..5, STATE-1..2.

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 25 |
| STATE_ASSERTION | 14 |
| CONTEXT_CLAIM | 7 |
| REGISTER_DEFECT | 5 |
| REMAINING_WORK | 2 |
| ACCEPTANCE | 1 |

| Disposition | All rows | Non-SEE rows | SEE rows |
|---|---:|---:|---:|
| STALE_SPECIFICATION | 21 | 12 | 9 |
| ALIGNED | 13 | 11 | 2 |
| NOT_AUDITABLE | 6 | 6 | 0 |
| PARTIALLY_IMPLEMENTED | 5 | 4 | 1 |
| IMPLEMENTED_DIFFERENTLY | 4 | 2 | 2 |
| AUTHORITY_CONFLICT | 2 | 1 | 1 |
| REMAINING_STATE_MISMATCH | 2 | 2 | 0 |
| STALE_VERIFICATION | 1 | 1 | 0 |
| **Total** | **54** | **39** | **15** |

- Split rate: 2 of 29 indexed units split (6.9%): CLM-005 (Construction table, 8 independently
  dispositionable rows) and CLM-009 (12 numbered REQ items), giving 20 rows. The two single-item
  SubItems units (CLM-012 AC-001, CLM-020 VER-001) take one row each and name the item in Notes.
- SEE rows (MR-4): 15. CLM-007/010/013/016/021/024 SEE CLM-001 (REF-006 "is MATCH" restatement);
  CLM-001 SEE REGISTER-1; CLM-009.1/.2/.5/.6/.7/.8/.9 SEE the matching CLM-005 row; CLM-023 SEE CLM-009.10.
- HumanDecisionNeeded: NO 47; `R4-Q1; R4-Q6` 3 (CLM-005.8, CLM-009.9, CLM-011); `R4-Q1` 2 (CLM-005.3,
  CLM-009.5); `R4-Q5` 2 (CLM-009.10, CLM-023).
- Confidence: HIGH 26, MEDIUM 28, LOW 0.
- No errata file (pass 1).

## 2. Least-confident rows

- **STATE-2** (daemon-era proofs in `_STATUS` History / `MEMORY.md`), `STALE_VERIFICATION`. Alternative:
  `NOT_AUDITABLE`, because the entries are dated history and truthful as of their date. I chose
  STALE_VERIFICATION because the recorded proof file
  (`frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`) is gone at
  the frozen basis (last touched by `39c0bb6ab`, D-GOV-43 A2) and the topology it proved is retired.
- **CLM-005.2 / CLM-009.2** (SSE event names), `STALE_SPECIFICATION`. Alternative: `ALIGNED` on a
  test-exists reading, since `routes.test.ts:631` asserts the names and the Runtime TurnCoordinator still
  emits them. I chose STALE because amended SPEC §11 (D-GOV-43) and D-APP-127 retire the closed vocabulary
  that the requirement protects, and the route test gets its events from the legacy in-process harness
  behind the test-only fake daemon port.
- **CLM-005.4 / CLM-009.6** (attachments), `STALE_SPECIFICATION`. Alternative: `IMPLEMENTED_DIFFERENTLY`
  (recorded as `ALSO:`). Amended SPEC §16.1 itself assigns partial failure to the legacy path, so the
  repair is to the deliverable text.
- **CLM-005.7** (interrupts), `ALIGNED`. Alternative: `PARTIALLY_IMPLEMENTED`, because
  `routes.test.ts:1270` still asserts that an SSE reader disconnect cancels the turn, contrary to
  amended SPEC §11. That test runs through the legacy-backed fixture; the live-path Runtime tests
  (`daemon.test.ts:410`, `codex-supervisor.test.ts:169`, `turn-hardening.test.ts:504`) meet the claim.
- **CLM-005.1 / CLM-009.1** (TurnEngine): no R4-Q1, because LIVE Runtime code (TurnCoordinator) meets
  the behaviour (rule 3). A reader who treats the claim as naming the TurnEngine module would give
  `ALIGNED` plus R4-Q1.
- **REM-1** `MechanicallyUnblocked = UNKNOWN`. The gate appears met on App code, but the Depends items
  DEL-03-03-V3-01 and DEL-05-02-V3-01 sit in other packages' folders, outside my reading bounds.

## 3. Register-defect summary

- **REGISTER-1**: `_REFERENCES.md` REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD are recorded MATCH,
  and none reproduces (`HASH-RECOMPUTE@00115c719`, pack `REFERENCE_HASHES.csv`). My own `shasum` at the
  frozen basis shows REF-001 DIRECTIVE, REF-004 TYPES and REF-005 PLAN still match. REF-007/009/010 (Root
  workflow files) were not recomputed. Six SoW current-state notes restate "is MATCH" (CLM-001 plus SEE rows).
- **REGISTER-2**: `Dependencies.csv`. All 13 TargetLocation line pointers are wrong at the frozen basis:
  the decomposition was revised on 2026-09-04 (`87f2d2a75`, `dbd812a52`), so PKG-09 is now at :287, the
  DEL-09-03 row at :380, SOW rows at :414–:432 and OBJ rows at :263–:269. SOW-011/012/014/015 and
  OBJ-002/003 were rewritten, so TargetName and EvidenceQuote no longer match. DEP-013 still cites a
  `Guidance.md` that no longer exists. Every row stays SATISFIED on the strength of the 2026-07-10 checks.
- **REGISTER-3**: `_DEPENDENCIES.md` Declared Upstream/Downstream still reads "TBD – no accepted
  dependency edges", although the same file lists 13 rows.
- **REGISTER-4**: the SoW `decomposition_basis` is pinned at `d6f6cadb2`, before the two revisions. The
  `_STATUS` V3-01 trace "row L366" refers to that basis. This is bookkeeping lag.
- **REGISTER-5**: the `_STATUS` header still names D-APP-19 as the Authorization Basis, although its own
  History records the D-APP-54 rebaseline.
- Related STATE rows: STATE-1 (`_CONTEXT.md` still names Claude/Anthropic as the current path and cites
  kit files that no longer exist; D-APP-127 map: `_CONTEXT` Revised=NO); STATE-2 (daemon-era proofs).

## 4. Direction and cause

- Main CauseTags:
  - CODEX_SOLE_ENGINE: 11 rows (SSE vocabulary, attachments, denied actions, event neutrality, `_CONTEXT`).
  - DOC_HYGIENE: 10 (reference and MATCH restatements, conflict table, pin).
  - PRE_V3_DRIFT: 7 (the D-APP-53/D-APP-56 July reconciliations never reached SoW Prerequisites, Records
    or `_DEPENDENCIES`).
  - RUNTIME_EXTRACTION: 4 (TurnEngine replaced by the Runtime TurnCoordinator; the replay test did not
    move with the code).
- `CAUSE2` secondaries: A2_TOPOLOGY, CARRIER_PROPAGATION, DOC_HYGIENE, CODEX_SOLE_ENGINE, RUNTIME_EXTRACTION.
- GOVERNING records used:
  - D-APP-127: its Governing facts retire the closed event vocabulary; the Runtime service owns turns.
  - D-GOV-43: App SPEC §11, §16.1 and CONTRACT K-EVENT-1/K-EVENT-6 amended; the CONTRACT
    "Current Codex-only MVP release basis".
  - D-APP-53 (dependency reconciliation), D-APP-56 (UPD-145), D-APP-54 (lifecycle rebaseline), D-APP-38
    (reference model).
- CONTEXT records used:
  - `RUN_BASIS.md` §5 known basis defect (REGISTER-4).
  - `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md` for REM-2: a signed but
    un-notarized 3.0.0-rc.1 DMG; agent-recorded, not a ruling.
- NONE_FOUND searches, for CLM-005.3, CLM-009.5, CLM-009.11, CLM-012 and REGISTER-4:
  - `_DECISIONS/_REGISTER.md`: grep for DEL-09-03 found no row.
  - D-APP-127 names DEL-09-03 only for the V3-02 re-point.
  - CONTEXT checked: the release plan and the APP_V3_CODEX_HOST_REPLATFORM AgentRuns folder.
  - None of these records explains the missing live-path replay test or the absent coverage table.
- Done-declaration context: Q-02 (release act / F-APP-2) touches REM-2 only; noted, not cited.

## 5. Method friction

- **Test-existence claims against superseded contracts.** Several claims say "tests shall preserve X",
  where X was later amended (SSE names, attachment partial failure). The tests exist but protect
  superseded behaviour. The rulebook has no verdict that fits exactly; I used `STALE_SPECIFICATION` via
  MR-11, since the amended SPEC clause names the change. Proposal: state that a test-coverage requirement
  whose protected behaviour a ruling superseded takes `STALE_SPECIFICATION`, with `ALSO:` giving the
  test-level reading.
- **Legacy-backed fixtures behind live routes.** `frontend/src/__tests__/api/harness/fake-daemon-harness-port.ts`
  drives the LIVE route modules (turn, interrupt, events) with events produced by the LEGACY_ONLY
  in-process harness. The REACH map cannot express "live route, legacy event source". I tagged the
  fixture TEST_ONLY and the route LIVE and explained this in Notes. Proposal: add a note convention such
  as `FIXTURE=LEGACY_BACKED`.
- **REM Depends in other packages.** `MechanicallyUnblocked` has no out-of-bounds case, so I used
  UNKNOWN with an explanation.

## 6. Effort

About 45 files or ranges read: all deliverable files except the `_SEMANTIC*` and `_run_records` bodies,
which I only listed. Also: the evidence-pack rows, gate transcripts, key SPEC/CONTRACT sections, about
15 App and Runtime source files and about 20 test files by grep and range. The context budget was
moderate, not tight.

## Coverage gaps

- **Live-path replay malformed-tail test missing.** Runtime `SessionStore.replay`
  (`projects/chirality-runtime/packages/core/src/session-store.ts:870-890`) counts malformed lines, but
  neither Runtime nor App tests exercise a malformed line on it. Owned by CLM-005.3/REQ-005 for
  DEL-09-03; the implementation owner is outside this package.
- **Test asserting superseded disconnect behaviour.**
  `frontend/src/__tests__/api/harness/routes.test.ts:1270` expects an SSE reader disconnect to cancel the
  turn (legacy-backed fixture). Amended SPEC §11 and D-APP-127 say a closed connection must not
  interrupt. No DEL-09-03 row owns removing or retargeting this test; flagged for the manager.
- **Provider-neutrality test is weaker than its name.** `frontend/src/__tests__/lib/session-events.test.ts:21`
  rejects only `sdk|claude|anthropic`, so the canonical `codex.*` types pass. Tied to R4-Q5 (CLM-009.10).
- **Test families outside the eight groups.** Codex supervisor, application tools, native plan,
  attachment copy and event views are delivered with tests. `_STATUS` V3-01 assigns them to their owning
  carriers ("not here"), so DEL-09-03 has no row for them.
