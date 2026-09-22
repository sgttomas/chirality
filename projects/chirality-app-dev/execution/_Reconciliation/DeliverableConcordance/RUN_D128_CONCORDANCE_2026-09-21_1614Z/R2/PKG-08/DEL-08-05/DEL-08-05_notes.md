# DEL-08-05 — forward notes (RUN_D128, R2 PKG-08, rerun worker)

- Ledger: `DEL-08-05_claims.csv`, 64 rows plus `#END`. It is sealed at SHA-256 `543a194e954f8992ae7916e725f42a9816144a071adaa47f49496b55eb473e0f`.
- Validator: `RULES errors none | warnings none`; `RESULT PASS errors=0 warnings=0`.
- Basis: frozen tree `00115c719`. All paths are repo-relative.

## 1. Census

**Coverage.** 38 indexed units: 37 CLM and 1 REM. Every one appears at least once. There are also 5 `REGISTER-n` rows and 1 `STATE-n` row.

**Rows by ClaimType × Disposition:**

| ClaimType | Disposition | Rows |
|---|---|---:|
| REQUIREMENT (28) | PARTIALLY_IMPLEMENTED | 9 |
| | ALIGNED | 5 |
| | DOCUMENTED_UNIMPLEMENTED | 5 |
| | STALE_SPECIFICATION | 3 |
| | AUTHORITY_CONFLICT | 3 |
| | IMPLEMENTED_DIFFERENTLY | 3 |
| ACCEPTANCE (6) | PARTIALLY_IMPLEMENTED | 4 |
| | DOCUMENTED_UNIMPLEMENTED | 2 |
| EXCLUSION (1) | ALIGNED | 1 |
| CONTEXT_CLAIM (18) | NOT_AUDITABLE | 15 |
| | STALE_SPECIFICATION | 3 |
| STATE_ASSERTION (5) | ALIGNED | 3 |
| | STALE_SPECIFICATION | 2 |
| REMAINING_WORK (1) | REMAINING_STATE_MISMATCH | 1 |
| REGISTER_DEFECT (5) | STALE_SPECIFICATION | 3 |
| | REMAINING_STATE_MISMATCH | 2 |

**Totals by Disposition:**
- PARTIALLY_IMPLEMENTED: 13
- NOT_AUDITABLE: 15
- STALE_SPECIFICATION: 11
- ALIGNED: 9
- DOCUMENTED_UNIMPLEMENTED: 7
- IMPLEMENTED_DIFFERENTLY: 3
- AUTHORITY_CONFLICT: 3
- REMAINING_STATE_MISMATCH: 3

**Split rate.** 3 of 38 indexed units were split, which is 7.9% of units. They produced 23 of 64 rows (36%).
- CLM-012 → 13 rows. The unit is a table of 13 independently dispositionable requirements, DEL-08-05-REQ-001..013.
- CLM-018 → 7 rows. The index lists 6 SubItems (REQ-001..004, AC-001, AC-002). Row .7 is the D-APP-56 amendment paragraph.
- CLM-025 → 3 rows. The index lists 2 SubItems (VER-001, VER-002). Row .3 is the Records list.

**SEE rows** (counted separately): 9. Each target carries the same Disposition.

| SEE row | Target |
|---|---|
| CLM-012.1, CLM-012.2 | CLM-006 |
| CLM-013, CLM-028 | CLM-003 |
| CLM-018.1, CLM-018.2 | CLM-037 |
| CLM-018.7 | CLM-012.7 |
| CLM-034 | CLM-017 |
| CLM-035 | CLM-009 |

**HumanDecisionNeeded:**
- NO: 41
- R4-Q1: 20
- `R4; R4-Q1`: 3. These are CLM-006, CLM-012.1 and CLM-012.2.

**Other counts:**
- Confidence: HIGH 36, MEDIUM 25, LOW 3.
- AuthorityTier: GOVERNANCE_INVARIANT 18, LOCAL_DESIGN 23, PRD 2, NOT_APPLICABLE 21.

**Errata.** The reverse pass raised 11 errata rows in `DEL-08-05_errata.csv`: 9 on ImplementationEvidence and 2 on Notes. None touches Disposition, CauseTag, HumanDecisionNeeded, Confidence, AuthorityTier or ClaimType.

**Sealed vs errata-applied figures:**

| Figure | Sealed | Errata-applied |
|---|---|---|
| Rows | 64 | 64 |
| Disposition totals | as above | identical |
| CauseTag totals | as above | identical |
| HumanDecisionNeeded | NO 41, R4-Q1 20, `R4; R4-Q1` 3 | identical |
| SEE rows | 9 | 9 |
| Split rate | 3 of 38 units | identical |

**What the errata qualify.** Two runtime symbols I cited as live native-lineage evidence are not executed on the product path:
- `delegated.ts:247`, the callback `nativeChild` association (dead contract, CAP-RTCONTRACT-028);
- `runtime-method-service.ts:454-469`, which has no producer of `executionContext.nativeChild`.

See `DEL-08-05_reverse_notes.md`.

## 2. Least-confident rows

- **CLM-012.9** (REQ-009, redaction), PARTIALLY_IMPLEMENTED, LOW.
  - What I found: the live `session-store.ts` `appendEvent` persists its input without calling redaction.
  - Alternative reading: K-EVENT-6 structural redaction may run upstream on a live path I did not trace. If so, the row would be ALIGNED for events, leaving only the absent child artifacts.
- **CLM-012.12** (REQ-012, denied record after allocation), DOCUMENTED_UNIMPLEMENTED, LOW.
  - Alternative reading: the requirement only applies once an attempt reaches the child-run record layer, and the live path has no such layer. It may therefore be vacuously ALIGNED.
  - Even on the legacy path, `createDelegationChildRunRecord` has no product caller.
- **STATE-1** (`_CONTEXT.md` daemon linkage), STALE_SPECIFICATION, LOW.
  - Alternative reading: "daemon" still names the `packages/daemon` process that A2 runs as an App-owned child, so the wording may remain accurate.
- **CLM-006 / CLM-012.1 / CLM-012.2** (AUTHORITY_CONFLICT), MEDIUM.
  - Alternative reading: the two `ChildRunRecord` shapes are separate record families that share one name. On that reading there is no conflict: the SoW's citation of TYPES §10 would be STALE_SPECIFICATION, and D-APP-56 would govern.
  - Why I kept the conflict: TYPES §10 names a single `ChildRunRecord` and defines "Child run" as the governed managed-session record. DIRECTIVE §0 does not rank rulings against TYPES.

## 3. Register-defect summary

- **REGISTER-1/2/3.** `_REFERENCES.md` records CONTRACT, PRD and SPEC as MATCH, but none of the three hashes reproduces at `00115c719` (pack `REFERENCE_HASHES.csv`, all `NO`). There is one row per document, cited as `HASH-RECOMPUTE@00115c719`. CLM-008 cites REGISTER-2 for its PRD currency claim.
- **REGISTER-4.** `_DEPENDENCIES.md:14,18` says "no accepted dependency edges", but `Dependencies.csv` holds 11 ACTIVE rows, including DEL-08-04 upstream rows DEP-08-05-004 and -011. This is metadata lag.
- **REGISTER-5.** `_DEPENDENCIES.md:107-112` calls itself the "current structured-register mirror" (ACTIVE 10, TBD 5). The CSV and the same file's Lifecycle Summary both show 11 ACTIVE, 5 SATISFIED and 6 TBD.
- **Related SoW rows** with the same hygiene cause:
  - CLM-021: the stale ASSUMPTION note on the DEL-08-04 edge.
  - CLM-015: `Procedure.md` no longer exists as a file, and E-002 contradicts REQ-004's `subagent.failed`.
  - CLM-032: `contractVersion` is shown as the string `"1"`; the code uses the numeric `1`.
  - CLM-008: the reference list contains a machine-specific absolute path (not reproduced here).

## 4. Direction and cause

**The main finding.** Every module that writes `ChildRunRecord`, `subagent.*` lifecycle events, `artifacts/subagents` or the 16/512 KiB child-output policy is REACH=LEGACY_ONLY:
- `agent-runtime-contract.ts`
- `sdk-message-mapper.ts`
- `tool-result-artifacts.ts`
- `managed-delegation.ts`
- `session-events.ts`

**What the live Codex path does instead.**
- It emits native children as `tool.*` and `codex.notification` events carrying `agentThreadIds` (`delegated-engine-adapter.ts:277-287`).
- It tracks parent threads in memory and ends observation with `chirality/nativeChildren/observationEnded` (`codex-supervisor.ts`).
- It records configured-role child method history (`runtime-method-service.ts:454-469`).
- It emits `instruction-asserted` role evidence per turn (`role-policy.ts`, `delegated-runtime.ts:321`). `nativeDescendant` is never set true.

**Why the managed AgentRun writer counts as not executed (verification lesson 4).** `agent1-run-coordinator.ts` is LIVE in REACHABILITY.csv. However, `GovernedAgent1RunCoordinator` is never constructed outside `tests/agent1-run.test.ts`: I grepped `projects/chirality-runtime/packages`, `frontend/src` and `frontend/electron`. I therefore treated it as not executed on the product path, and say so in Notes on each row that relies on it.

**CauseTags:**

| CauseTag | Rows | Where |
|---|---:|---|
| CODEX_SOLE_ENGINE | 15 | legacy-only rows judged on the live path; usually with CAUSE2:NATIVE_DELEGATION |
| DOC_HYGIENE | 8 | register and SoW hygiene rows |
| LIFECYCLE_GATE_PENDING | 8 | v3 rows tracked by REM-1 |
| A2_TOPOLOGY | 4 | canonical-store statements; STATE-1 |
| PRE_V3_DRIFT | 4 | the TYPES §10 conflict rows and the CLM-032 example |
| RUNTIME_EXTRACTION | 1 | REM-1: its write locus names the LEGACY_ONLY frontend harness tree, but the live writers are in `projects/chirality-runtime/packages` |

**CAUSE2 secondaries:**
- NATIVE_DELEGATION
- CODEX_SOLE_ENGINE (CLM-003, CLM-006, CLM-025.1)
- A2_TOPOLOGY (CLM-012.7, CLM-018.4)
- PRE_V3_DRIFT (CLM-015)
- CARRIER_PROPAGATION (REM-1 and STATE-1). The pack's D-APP-127 map shows all five carriers `Revised=NO`.

**CONTEXT records used:**
- `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, lines 301, 309, 374, 841 (AT-028) and 1221: native descendants are observations, not fabricated managed AgentRun records.
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`.

**GOV citations:**
- D-GOV-43: K-EVENT-4 was re-expressed in tranche `23b3879b3`.
- D-APP-40 and D-APP-56: they explain the SoW's legacy `ChildRunRecord` shape.

**Authority-order applications (verification lesson 1):**
- CLM-003/013/028. CONTRACT K-EVENT-4 now names `{userData}/runtime/...` as the canonical store and `.chirality/sessions` as legacy compatibility. SPEC §8.2 still shows the `.chirality` layout. DIRECTIVE §0 ranks CONTRACT above SPEC, so these rows are STALE_SPECIFICATION, not AUTHORITY_CONFLICT.
- CLM-006. TYPES §10 (amended 2026-07-11, `c9734a6ee` and `ee35409f5`) defines a different shape from D-APP-40 (2026-06-21) and D-APP-56 UPD-138 (2026-07-12). Both rulings address this deliverable but do not name TYPES §10, and §0 does not resolve the disagreement. It is carried as AUTHORITY_CONFLICT with `R4; R4-Q1`.

**Rows with DirectionEvidence NONE_FOUND.** These are CLM-008, CLM-021, CLM-032, REGISTER-1..5 and REM-1's non-CTX parts.
- Search: the `_DECISIONS/_REGISTER.md` rows naming DEL-08-05 (D-APP-40, 68, 117; the pack's DECISION_HITS), plus grep of the CONTEXT steers and plan for `DEL-08-05`, `contractVersion`, `reference refresh` and `_DEPENDENCIES`.
- Result: no direction record beyond D-APP-38's reference model. The RUN_BASIS known defect says corpus drift is deferred.

**No other decision applies.** D-APP-117 (AWAITING_RULING) names DEL-08-05 persistence as separately activated. It is not GOVERNING and was not used.

**Checks on the REM-1 Checks line (verification lesson 3):**
- D-APP-127 retired the `APP-HOLD-1-INIT-DEL-09-07` hold row.
- The APP-HOLD-1 reliance preflight (`execution/_Scripts/app_hold.py`; App `AGENTS.md` §APP-HOLD-1 Reliance Preflight) still exists.
- So that check is not stale, and no defect was raised on it.

**PostReleaseBasis.** Two cited files are touched paths:
- `session-store.ts`: I blamed lines 654-668, 815-845 and 1116-1127.
- `codex-supervisor.ts`: I blamed lines 280-309, 515-520 and 588-592.

None of these lines blames to `da95ec194`, `cb08dbe2f`, `9ecbdecdf` or `ccb95e06a`, so every row is `NO`.

## 5. Method friction

- **REM rows with a mis-sited write locus.** A REM item whose gate text is accurate but whose declared write locus points at a LEGACY_ONLY tree has no crisp disposition. I used REMAINING_STATE_MISMATCH with RUNTIME_EXTRACTION.
  - Proposal: add a note that locus-versus-reach mismatch on REM rows takes REMAINING_STATE_MISMATCH.
- **Rulings versus later GOVERNING doc edits.** A ruling can be newer than a GOVERNING doc edit, or older; here D-APP-40 is older than TYPES §10 and D-APP-56 is newer. MR-11's "older untranscribed wording" test does not say which way to decide.
  - Proposal: state explicitly that a ruling never outranks a later-amended GOVERNING doc without naming it, which makes such cases AUTHORITY_CONFLICT.
- **PREGATHER header.** Its NO_CANDIDATES count (8) is wrong, as the brief warned. I relied on the unit sections and confirmed every cited path.

## 6. Effort

- About 30 files or excerpts read, including:
  - all deliverable carriers;
  - the pack files;
  - the governing-doc excerpts (CONTRACT, TYPES §10, SPEC §8–9, DIRECTIVE §0);
  - the D-APP-40, 56, 68 and 127 records;
  - the key runtime and frontend modules;
  - the test case listings.
- The context budget was adequate but not loose. `_SEMANTIC*.md` and `_run_records/**` were not needed and were not read.
