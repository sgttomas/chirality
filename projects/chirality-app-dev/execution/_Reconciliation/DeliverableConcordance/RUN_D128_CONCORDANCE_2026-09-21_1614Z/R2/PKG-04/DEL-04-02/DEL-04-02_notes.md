# DEL-04-02 — forward-pass notes (RUN_D128, R2 wave 1, PKG-04)

Deliverable: SdkOptionsBuilder and Settings Isolation. Frozen basis `00115c719`. Forward ledger
`DEL-04-02_claims.csv`: 48 rows. The validator returned 0 errors and 0 warnings.

## 1. Census

- **Coverage:** all 31 indexed units are covered (CLM-001..031). CLM-014 (AC-001) and CLM-021
  (VER-001) each list one sub-item, so each has one row.
- **Split:** CLM-010 (the REQ table) is split into 14 rows, `.1` to `.14`, one per
  DEL-04-02-REQ-001..014. This is permitted because the items are separately numbered. Split rate:
  1 of 31 units (3%) is split, and it yields 14 of 48 rows.
- **Run-local rows (4):** REGISTER-1 and REGISTER-2 (register defects); STATE-1 (`_CONTEXT.md`);
  STATE-2 (`_STATUS.md`).

| ClaimType | ALIGNED | PARTIALLY_IMPL | STALE_SPEC | REM_STATE_MISMATCH | NOT_AUDITABLE | IMPL_DIFFERENTLY | LIFECYCLE_REASSESS | Total |
|---|---|---|---|---|---|---|---|---|
| REQUIREMENT | 13 | 9 | 4 | 0 | 0 | 2 | 0 | 28 |
| ACCEPTANCE | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| STATE_ASSERTION | 1 | 0 | 4 | 3 | 0 | 0 | 1 | 9 |
| CONTEXT_CLAIM | 0 | 0 | 2 | 0 | 5 | 0 | 0 | 7 |
| REGISTER_DEFECT | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 |
| **Total** | 14 | 11 | 10 | 5 | 5 | 2 | 1 | 48 |

- **SEE rows (4), counted separately:**
  - CLM-008 → CLM-001;
  - CLM-022 → CLM-001;
  - CLM-019 → CLM-012;
  - CLM-020 → CLM-013.

  Excluding them leaves 44 primary rows.
- **HumanDecisionNeeded:** 31 rows are `R4-Q1`, and 17 are `NO`.
- **Confidence:** HIGH 21, MEDIUM 26, LOW 1.
- **Errata:** none yet (forward pass only).

## 2. Least-confident rows

- **CLM-028 (LOW), example fallback trace.** Recorded as `IMPLEMENTED_DIFFERENTLY`: the
  `CHIRALITY_GLOBAL_MODEL` tier now sits in the Runtime compatibility engine selection
  (`compatibility-session-policy.ts:54`, LIVE) and not in the App option path (`options.ts:30`).
  - Alternative reading: `PARTIALLY_IMPLEMENTED`. That Runtime policy only covers selecting the
    Claude or stub compatibility engine, so the env tier may have been dropped rather than moved.
- **Module-level ALIGNED rows** (CLM-010.2–.9, .11, .13; CLM-011, 026, 030). These are judged at
  module level on the retained Claude builder (REACH=LEGACY_ONLY), because the claims describe the
  builder itself.
  - Alternative reading: judge them on the live Codex path. Several REQs would then become
    `DOCUMENTED_UNIMPLEMENTED`, and REQ-003/004 in particular would be inverted, because the
    effective Codex home deliberately shares the user's `~/.codex` configuration.
  - I tagged all of them `R4-Q1`, so the owner's answer on whether the retained harness is
    history, compatibility or obligation decides which reading governs.
- **CLM-004 and CLM-023 (MEDIUM).** Recorded as `STALE_SPECIFICATION`, not `AUTHORITY_CONFLICT`.
  - DIRECTIVE §2.8 is unamended and says "Claude remains the default and supervisor".
  - However, §2.8 itself says other provider paths need a fresh governed tranche. D-GOV-43 and
    D-APP-127 are that tranche, and the CONTRACT, SPEC and PRD Codex-only preambles record it.
    I therefore treated the authority order as resolving the difference.
  - Alternative reading: `AUTHORITY_CONFLICT` with R4-Q1, because DIRECTIVE §2.8 was never
    re-amended.
- **CLM-009 (MEDIUM), `IMPLEMENTED_DIFFERENTLY`.**
  - Alternative reading: `RETIRED_BY_RULING`. I did not use it because no ruling names DEL-04-02
    or preserves it as history: DECISION_HITS has no REGISTER or RULING rows for DEL-04-02, and
    D-APP-127 does not address the Claude builder.

## 3. Register defects

- **REGISTER-1.** In `_REFERENCES.md`, the CONTRACT, SPEC and PRD MATCH hashes do not reproduce at
  `00115c719`: the pack shows `Match = NO` for all three. This is metadata lag, so the row is
  `REMAINING_STATE_MISMATCH`.
  - Restated by CLM-001, 004, 006, 008, 022, 024, 025 and 031.
  - CLM-025 and CLM-031 became incoherent after the D-APP-56 mechanical MATCH substitution. For
    example, CLM-031 names as a "conflict" that the register "reports MATCH".
- **REGISTER-2.** `Dependencies.csv` rows cite `Datasheet.md`, `Specification.md` and
  `Procedure.md`, which no longer exist.
  - Only DEP-04-02-006 carries the ScopeOfWork migration note.
  - DEP-007..011 are still `TBD` with LastSeen 2026-05-20.
- **D-APP-127 carriers.** All five are `Revised = NO` (pack item 5). This feeds STATE-1 and STATE-2.

## 4. Direction and cause

- **Main CauseTags:**
  - `PRE_V3_DRIFT` (8): settings-source metadata, the terminal max-turn fixture and the policy
    adequacy check were already PARTIAL at INSP-03 on 2026-06-20.
  - `DOC_HYGIENE` (7).
  - `CODEX_SOLE_ENGINE` (5).
  - `CARRIER_PROPAGATION` (5): the D-APP-56 P45 note says the paths are landed, but the TBDs were
    left in place.
  - `RUNTIME_EXTRACTION` (4).
- **`RUNTIME_EXTRACTION` rows:** the fallback-chain truncation. Commit `9b005c23a` (2026-09-09, v3
  adoption) removed the frontmatter tiers; `options.ts:23-26` now says "Role and method
  configuration is resolved by Runtime". SPEC §13.1 and PRD FR-023 are unamended.
- **CAUSE2 secondaries:** PRE_V3_DRIFT, CODEX_SOLE_ENGINE, DOC_HYGIENE, A2_TOPOLOGY,
  CARRIER_PROPAGATION and RUNTIME_EXTRACTION, each on the rows named in Notes.
- **GOVERNING records used:**
  - `GOV:D-GOV-43; GOV:D-APP-127` on CLM-004, 009 and 023, and on STATE-1 and STATE-2;
  - `GOV:D-APP-60` on CLM-010.12, 013, 017 and 020, because the DEP-04-02-006 probe prerequisite
    was closed on 2026-07-18.
- **CONTEXT record used:**
  `CTX:execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/CORPUS_V21_CANDIDATE.md:10`,
  which says the Runtime context contract supplies role instructions. It is a weak explanation of
  the fallback truncation.
- **Searches behind each `NONE_FOUND`:**
  - I grepped `_DECISIONS/_REGISTER.md` for DEL-04-02, SdkOptionsBuilder, settings isolation,
    K-SDK-1 and settingSources. No row names this deliverable.
  - I grepped the D-APP-127 ruling record for Claude, legacy, harness and settings. It does not
    address the Claude builder.
  - I grepped the CONTEXT sources (`plans/steers/chirality_app_v3_*`, `AgentRuns/APP_V3_*`,
    `CHIRALITY_V3_APP_ADOPTION_20260909`) for sdk-options-builder and DEL-04-02. There was no
    explaining record; only incidental hits in integration-source copies and a phase-0 steer line
    citation.
- **Live-path facts:**
  - `codex-supervisor.ts:219` (`thread/start`) blames to `da95ec194`, so the rows that cite it
    have PostReleaseBasis `YES`.
  - I blamed `codex-supervisor.ts:191`; it goes to `3ad6fac0d`, which is not in the list, and I
    did not cite it.
  - No other cited file is in `TOUCHED_PATHS.csv`.

## 5. Method friction

- **MR-4 versus the SoW's summary tables.** CLM-003 (Attributes) comes before CLM-010 (REQs) and
  restates most REQs in compressed form. Strict MR-4 would put every disposition on CLM-003 and
  make the REQ rows SEE rows, which would lose the per-REQ findings.
  - What I did: gave CLM-003 its own composite disposition and treated the REQ rows as the
    primary per-item dispositions.
  - Proposed revision: MR-4 should prefer the numbered REQ unit as the anchor when an earlier
    unit is a summary table.
- **LEGACY_ONLY module versus the live path when the deliverable is Claude-specific.** The
  §2.3 rule does not say which way to judge a claim like "Shipped SDK options MUST use
  settingSources []". It is about the retained module, but on the live path the premise is
  vacuous, or even inverted.
  - What I did: judged at module level and tagged `R4-Q1`, which puts `R4-Q1` on 31 rows.
  - Proposed revision: allow one deliverable-level R4-Q1 row, with the module-level rows citing
    it, to reduce noise.
- **The gate transcript has no per-file test listing.** VerificationEvidence therefore cites the
  suite-level transcript plus a test file and case that I read but did not see individually
  reported.

## 6. Effort

- **Files read (about 25):**
  - deliverable files: ScopeOfWork, `_STATUS`, MEMORY, `_CONTEXT`, `_REFERENCES`,
    `Dependencies.csv` and the INSP-03 assessment;
  - code: `sdk-options-builder.ts`, `options.ts`, `tool-pool.ts` (part) and `turn-engine.ts`
    (part);
  - Runtime: `codex-supervisor.ts` (grep and line ranges), `codex-effective-home.ts` (header) and
    `compatibility-session-policy.ts` (part);
  - test case listings for four test files;
  - governing text: CONTRACT, SPEC and DIRECTIVE excerpts;
  - the pack CSVs and the manifests.
- **Not read:** the `_SEMANTIC*` files and `_DEPENDENCIES.md`.
- The context budget was comfortable.
