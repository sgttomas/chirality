# DEL-09-02 — forward-pass notes (worker B, double-blind)

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, R2 wave 5 (PKG-09). Basis `00115c719`. Ledger
`DEL-09-02_claims.csv` (50 rows). Validator: `RESULT PASS errors=0 warnings=0`.

## 1. Census

- **Indexed units:** 29 (28 CLM + 1 REM), all covered. Run-local rows: REGISTER-1..3, STATE-1.
- **Split rate:** 3 of 29 units split (10%):
  - CLM-010 into 16 rows, one per RQ-001..RQ-016 (a table of independently dispositionable rows);
  - CLM-014 into .1 (P45 note) and .2 (AC-001);
  - CLM-020 into .1 (Records) and .2 (VER-001).
- **By ClaimType:** REQUIREMENT 23, CONTEXT_CLAIM 14, STATE_ASSERTION 4, ACCEPTANCE 4,
  REGISTER_DEFECT 3, EXCLUSION 1, REMAINING_WORK 1.
- **By Disposition (all rows):**

| Disposition | Rows | of which SEE rows |
|---|---:|---:|
| STALE_SPECIFICATION | 25 | 10 (REF-006 restatements → REGISTER-1: CLM-001, 006, 008, 011, 013, 015, 017, 021; CLM-020.1 → CLM-018; CLM-025 → CLM-024) |
| ALIGNED | 6 | 2 (CLM-014.1, CLM-028 → CLM-007) |
| IMPLEMENTED_DIFFERENTLY | 6 | 0 |
| DOCUMENTED_UNIMPLEMENTED | 4 | 0 |
| NOT_AUDITABLE | 4 | 0 |
| PARTIALLY_IMPLEMENTED | 3 | 1 (CLM-014.2 → CLM-010.14) |
| STALE_VERIFICATION | 1 | 0 |
| REMAINING_STATE_MISMATCH | 1 | 0 |
| **Total** | **50** | **13** |

- **Without SEE rows:** 37 rows, of which 15 are STALE_SPECIFICATION, 4 ALIGNED and 2 PARTIALLY_IMPLEMENTED.
- **HumanDecisionNeeded:** R4-Q1 on 12 rows (CLM-010.2–011, CLM-010.14, CLM-014.2). R4-Q2 is added on
  CLM-010.2 and R4-Q5 on CLM-010.3. All other rows are `NO`.
- **No errata file** exists yet (pass 1).

## 2. Least-confident rows

- **CLM-010.9 (RQ-009, tool-result budget), LOW.**
  - Judged DOCUMENTED_UNIMPLEMENTED on the live path: the only Section 9 check is over
    `tool-result-artifacts.ts` / `tool-evidence.ts`, which are LEGACY_ONLY.
  - Alternative: the Runtime may budget or artifact Codex tool output somewhere my grep did not tie to
    tool results. That would make the row IMPLEMENTED_DIFFERENTLY.
- **CLM-010.10 (RQ-010, compaction), LOW.**
  - Judged DOCUMENTED_UNIMPLEMENTED on the live path.
  - Alternative: `projects/chirality-runtime/packages/contracts/src/events.ts:11` has a `compaction`
    event kind, so the live store may persist compaction boundaries. That reading gives
    PARTIALLY_IMPLEMENTED.
- **CLM-010.14 / CLM-014.2 (RQ-014, AC-001), MEDIUM.**
  - I cite R4-Q1 because the verdict depends on whether passes over retained-harness modules count as
    "landed runtime phases". This is not the rule-3 trigger: the validator itself is LIVE.
  - Alternative: a module-level reading of the validator's contract gives ALIGNED with HDN `NO`.
- **CLM-010.6 / CLM-010.8 (permission overlay; path/hooks), MEDIUM.**
  - Alternative: AUTHORITY_CONFLICT. The unamended K-PERM-1..4, K-HOOK-1 and K-PATH-2/3 sit against the
    D-GOV-43 item 4 user-chosen policy (App CONTRACT K-UNTYPED-1).
  - I kept IMPLEMENTED_DIFFERENTLY because R4-Q1 names exactly these clauses (K-PATH, K-HOOK, SPEC §15.2).
- **CLM-020.2 (VER-001), MEDIUM.** STALE_VERIFICATION against ADQ-14. The alternative is
  DOCUMENTED_UNIMPLEMENTED: no recorded premerge run over the 16-ID manifest exists anywhere in-root.

## 3. Register-defect summary

- **REGISTER-1 (STALE_SPECIFICATION).**
  - `_REFERENCES.md` REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD record ActualSHA256 = Expected,
    MATCH. None of the three reproduces (`HASH-RECOMPUTE@00115c719`).
  - DIRECTIVE, TYPES and PLAN recompute equal to their recorded values.
  - REF-007/009/010 are Root `workflows/` files and were not recomputed.
- **REGISTER-2 (STALE_SPECIFICATION).**
  - `_DEPENDENCIES.md` still carries `[WARNING] TBD_SURFACES` for paths that have now landed.
  - Its 25 SatisfactionStatus `TBD` values are genuinely open.
  - Two INTERFACE targets are the retired-engine SDK deliverables (DEL-04-02, DEL-04-03).
- **REGISTER-3 (REMAINING_STATE_MISMATCH).**
  - `_STATUS.md` Last Updated is 2026-09-03, but its History has a 2026-09-05 entry.
  - There is no D-GOV-43/D-APP-127 entry. The DEL-09-03..07 siblings have one.
- **Stale conflict table:** CLM-027. CONFLICT-002 still shows the human ruling as TBD, although
  D-APP-50/51 and UPD-144 settled it.
- **Absolute path:** the SoW CLM-006 REF-007 cites a machine-specific absolute path, which also
  disagrees with `_REFERENCES.md` REF-007. It is not reproduced in the ledger.

## 4. Direction and cause

- **Main CauseTags:**
  - CARRIER_PROPAGATION (13): the D-APP-56 R5 P45 notes (UPD-143/144) were appended as
    "current-state reconciliation" notes at CLM-007/014/028, and the body text was left unchanged.
    That body still says: registry path is the runner, warning/blocker fields are future work, paths
    and command are TBD, domain-profile validation is gated.
  - CODEX_SOLE_ENGINE (12): every Section 9 runtime check validates the retained in-process
    Claude-SDK harness, and none validates the live Codex path. The amended CONTRACT preamble names
    Claude/Anthropic descriptions as compatibility history. `_CONTEXT.md` (STATE-1) still calls the
    Claude SDK the current path.
  - DOC_HYGIENE (11): REF-006 MATCH restatements and register lag.
  - PRE_V3_DRIFT (2): the SoW keeps the pre-2026-06-13 IDs `sdk_turn_engine_event_log` and
    `sdk_message_mapper` (CLM-003), and ADQ-14 is the only recorded run (CLM-020.2).
- **CAUSE2 secondaries:** DOC_HYGIENE (CLM-004, 019), RUNTIME_EXTRACTION (CLM-010.7),
  CODEX_SOLE_ENGINE (CLM-010.11, 012, 020.2, REGISTER-2), NATIVE_DELEGATION (REM-1).
- **Rulings used:**
  - D-GOV-43 (App CONTRACT "Current Codex-only MVP release basis", K-UNTYPED-1, K-SUBAGENT-1, K-EVENT-1)
  - D-APP-56 (R4-P23 option A: report-only, pass/fail, enum deferred; R4-P45: UPD-143/144)
  - D-APP-38; D-APP-50/51; D-APP-03 (context); D-APP-114 (context)
- **CONTEXT used:** `Evidence_ADQ-14_Release_Quality_Validation_Wrapper.md` and the v3 release plan,
  cited as the completion reference in REM-1.
- **Done-declaration questions (Notes only):** Q-06 (sole-engine rule), Q-07 (containment), Q-11
  (managed multi-child).
- **Searches:**
  - `_REGISTER.md` grep for `Section 9|section9|DEL-09-02`: only D-APP-114 names the deliverable.
    D-APP-56 R4-P23 and R4-P45 were found through the D-APP-56 ruling and the D-APP-55 run's
    `PROPOSED_DELIVERABLE_UPDATES.csv`.
  - D-APP-127 ruling grep for DEL-08-04/05, Section 9 and WP-03/05: no hits, so there is no MOOT for
    REM-1.
  - No row uses `NONE_FOUND` DirectionEvidence.

## 5. Method friction

- **The R4-Q1 rule 3 trigger does not fit validation deliverables.** Here the validator is LIVE and
  the modules it tests are LEGACY_ONLY. Read literally, rule 3 cites R4-Q1 on the RQ-002..011 rows,
  because the only code meeting "validation must confirm product behaviour X" is legacy. It is silent
  on RQ-014, where a LIVE validator reports passes for legacy phases.
  - Proposal: for TEST_SUITE deliverables, state that the REACH of the *validated subject* decides
    R4-Q1, not the REACH of the runner.
- **Package-level REACH for build/validation scripts.** Validator scripts are reached from package.json
  validation scripts and the in-root workflow, not from `desktop:*` packaging scripts. I tagged them
  LIVE under the brief's "or the in-root workflow" clause.
  - Caveat: `projects/chirality-app-dev/.github/workflows/harness-premerge.yml` is not at the repository
    root, so GitHub would not run it as written.
- **Gate transcript granularity.** The APP transcript gives only aggregate counts (222 files passed,
  1 skipped). Per-file citations therefore mean "included in the aggregate pass", and I cannot tell
  which file was skipped.

## 6. Effort

- **Files read:** about 30 whole or partial. These include the deliverable's SoW, _STATUS, _CONTEXT,
  MEMORY, _REFERENCES, _DEPENDENCIES/Dependencies.csv and INSP-03, plus the ADQ-14 evidence.
- **Code and docs:**
  - the Section 9 runner and manifest, the premerge wrapper and the release-quality wrapper;
  - the in-root workflow and package.json;
  - PRD §12.3–12.4, SPEC §19.2–19.4 and CONTRACT key rows;
  - Runtime session-store, application-tools and descendant-tracker (excerpts);
  - D-APP-56 and the D-APP-55 run packet excerpts.
- **Context budget:** adequate, not tight. `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` (about 70 KB) were
  not read beyond their names: they are declared state from 2026-05, and their claims are not index units.

## Coverage gaps

- **Unowned Section 9 validation of the live Codex path.**
  - No Section 9 ID covers the live Runtime/Codex surfaces: the Runtime `session-store.ts` event store,
    the `application-tools.ts` dynamic tools and the `descendant-tracker.ts` native descendants.
  - REM-1 covers only descendant classes, role attribution, closed schema and cancellation. It does not
    cover engine-boundary, event-log, replay, permission or tool validation of the Codex path.
  - Whether that is DEL-09-02 scope depends on R4-Q1 and R4-Q2.
- **The Section 9 summary is not preserved in CI.** The in-root workflow uploads only the Section 8
  summary, and no deliverable row owns the missing Section 9 artifact upload (DEL-09-01/09-05 may).
- **`_SEMANTIC.md` / `_SEMANTIC_LENSING.md` were not audited.** They are not index units, and they
  likely repeat the same TBD and SDK-framing staleness.
