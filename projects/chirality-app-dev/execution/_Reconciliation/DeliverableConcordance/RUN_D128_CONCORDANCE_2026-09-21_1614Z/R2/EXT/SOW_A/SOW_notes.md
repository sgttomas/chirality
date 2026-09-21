# SOW half A (SOW-001..SOW-042): notes

Ledger: `SOW_claims.csv`, 51 rows. Sealed SHA-256
`7bbef23795458e20cba6ebe8c1cfe8aaccc49ed91925629c03c9e9d5eb370988`. There is no errata file.

## 1. Census

- **Units:** 42, all `IN`. **Rows:** 51. Nine units are split into `.1` (live-deliverable
  mapping) and `.2` (code or explicit deferral): SOW-005, 006, 018, 019, 024, 025, 027, 031
  and 033. **Split rate:** 9 of 42 (21%). **SEE rows:** 0. **Run-local rows
  (REGISTER/STATE):** 0.
- **ClaimType:** REQUIREMENT 51.
- **AuthorityTier:** PRD 43 (rows whose SourceRef is REF-006 = `docs/PRD.md` alone);
  LOCAL_DESIGN 8 (rows that also cite SCA-APP-010).
- **Disposition:** ALIGNED 42 (33 unsplit rows and 9 `.1` rows); PARTIALLY_IMPLEMENTED 4
  (005.2, 006.2, 025.2, 031.2); AUTHORITY_CONFLICT 1 (018.2); STALE_SPECIFICATION 1 (019.2);
  DOCUMENTED_UNIMPLEMENTED 1 (024.2); IMPLEMENTED_DIFFERENTLY 1 (027.2);
  DEFERRED_AGENT_WORKFLOW 1 (033.2).
- **Confidence:** HIGH 30, MEDIUM 19, LOW 2.
- **HumanDecisionNeeded:** NO 45; R4-Q4 2 (005.2, 031.2); R4-Q1 1 (027.2); R4-Q1 with R4-Q2
  1 (018.2); R4-Q2 1 (SOW-037); R4-Q5 1 (SOW-039).
- **Summary flags for the manager:**
  - `NO_LIVE_DELIVERABLE`: none. Every mapped deliverable is IN_PROGRESS in
    `DELIVERABLE_INVENTORY.csv`, and none of the rows maps to DEL-09-07.
  - `NO_CODE_NO_DEFERRAL`: SOW-033.2 only.
- **Mapping basis for part 1** (HIGH on every unit):
  - A script check found that §8 `CoversScopeItems` agrees with the §9 row for all 42 units.
  - Every mapped deliverable's `ScopeOfWork.md` front matter `project_scope_refs` lists the
    unit.
- **Manager rule applied** (message received mid-task):
  - A gated Remaining item that names the row's scope counts as an explicit deferral. On that
    basis SOW-003, SOW-008, SOW-010 and SOW-037 are single ALIGNED rows. Each cites the
    `_STATUS.md` item by path and line.
  - Build scripts that are missing from REACHABILITY.csv but are run by a live packaging entry
    are tagged `REACH=LIVE` (SOW-030, SOW-032). Check scripts are tagged `TEST_ONLY` (SOW-035,
    SOW-036).

## 2. Least-confident rows (with alternative readings)

- **SOW-031.2 (LOW), PARTIALLY_IMPLEMENTED.**
  - Evidence: the agent-metadata conformance validator is only in the legacy module and is
    tested on synthetic inputs. The live Runtime parses AGENT_TYPE without validating it.
  - Alternative readings: ALIGNED at module level (the validator exists), or
    DOCUMENTED_UNIMPLEMENTED on the live path.
- **SOW-033.2 (LOW), DEFERRED_AGENT_WORKFLOW.**
  - Evidence: immutable snapshots are a workflow convention, and no App or Runtime code
    produces snapshots.
  - Alternative readings: ALIGNED as a documentation-only convention (DEL-07-06 is a
    DOC_UPDATE deliverable), or DOCUMENTED_UNIMPLEMENTED if the row is read as product scope.
- **SOW-003 (MEDIUM), ALIGNED.** It relies on the DEL-02-03-V3-01 trace ("scan-state
  feedback") naming scope scans. Without that reading it is PARTIALLY_IMPLEMENTED, because the
  scope-scan endpoint's only UI consumer is the unmounted Workbench.
- **SOW-008 (MEDIUM), ALIGNED.** Context references, artifact anchors and chat rung/declined
  are persisted but never read. The ALIGNED verdict depends on the manager rule; without it
  the row is PARTIALLY_IMPLEMENTED.
- **SOW-018.2 (MEDIUM), AUTHORITY_CONFLICT.**
  - D-APP-127 supersedes the packaged-daemon subject, and the Codex sole-engine rule stands.
    Neither names DEL-04-01 or this row, so §1 requires AUTHORITY_CONFLICT.
  - Alternative readings: STALE_SPECIFICATION under MR-11 if D-APP-127 is read as addressing
    the row, or IMPLEMENTED_DIFFERENTLY on the live path.
- **SOW-024.2 (MEDIUM), DOCUMENTED_UNIMPLEMENTED.**
  - Why the live path fails: the App-owned Runtime composition passes no ProjectScaffoldPort,
    so scaffolding returns 501. `scaffoldExecutionRoot` has no caller outside tests.
  - Why REACH reads LIVE: the static pack tags `scaffold.ts` LIVE only through a type import.
  - Alternative reading: PARTIALLY_IMPLEMENTED at module level.
- **SOW-027.2 (MEDIUM), IMPLEMENTED_DIFFERENTLY.**
  - Mechanism: agent-tool containment comes from the Codex sandbox. The user-selectable Full
    access mode (`chat-panel.tsx:133`, `delegated.ts:326`) removes containment and
    instruction-root protection.
  - Alternative reading: PARTIALLY_IMPLEMENTED.
  - HDN: R4-Q1 is cited because the row turns on K-PATH, although live code meets part of the
    claim.
- **SOW-006.2 (MEDIUM), PARTIALLY_IMPLEMENTED.** The exact posture labels exist only in the
  consent panel, which is never rendered. The view is named Agents, not "Who is working".
  Alternative reading: ALIGNED, if the labels are taken to have retired along with per-root
  consent (D-APP-127 does not say so).

## 3. Register-defect summary

- The §8/§9 reverse view and the ScopeOfWork `project_scope_refs` agree for all 42 units, so
  there are no REGISTER rows.
- Adjacent observations, recorded in Notes only:
  - `electron/main.ts:133` still allowlists `api.anthropic.com` (SOW-020).
  - The Section 9 manifest `evidenceFiles` point at legacy engine modules (SOW-036).
  - The Runtime scaffold port is absent (SOW-024).

## 4. Direction and cause

- **CauseTags:**
  - CODEX_SOLE_ENGINE 3 (018.2, 027.2, 031.2)
  - CREDENTIAL_CUSTODY 2 (006.2, 019.2)
  - A2_TOPOLOGY 2 (024.2, 025.2)
  - OTHER:V3_ROLE_ADOPTION 1 (005.2)
  - **OTHER:WORKFLOW_CONVENTION** 1 (033.2). This is a new OTHER token: a workflow or agent
    convention with no product mechanism.
- **CAUSE2:** SHELL_REDESIGN (006.2, 024.2 in Notes), A2_TOPOLOGY (018.2),
  OTHER:V3_ROLE_ADOPTION (031.2), NATIVE_DELEGATION (mentioned for SOW-010, which is ALIGNED
  and carries no CAUSE2 token).
- **GOVERNING records used:**
  - D-APP-127: its governing facts and supersessions of D-APP-100, D-APP-122 and D-APP-126.
  - D-APP-108: Q3, and the seating of the V3 Remaining items.
  - D-GOV-43, as applied by D-APP-127 (approval and sandbox policy are the user's choice).
- **CONTEXT used:**
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/UI_SOURCE_FREEZE_v7.md`
  (SOW-005.2).
- **NONE_FOUND searches** (`_DECISIONS/_REGISTER.md` grep, plus the named records):
  - `scaffold`: only D-APP-104 and D-APP-107, both about DEL-09-07 bootstrap. Also checked:
    the D-APP-127 text and DEL-07-02 `_STATUS` (Remaining empty). Applies to 024.2 and 025.2.
  - `conformance`: D-APP-45, D-APP-116. `agent instruction`: none. Also checked:
    CHIRALITY_V3_APP_ADOPTION_20260909 records (only "candidate conformance" of the corpus
    review). Applies to 031.2.
  - `snapshot`: D-APP-38, 53, 55, 109, 110, 111, 114, all closure or coverage snapshots.
    `K-SNAP`: none. Applies to 033.2.
  - `conformance`/`K-ENGINE`: D-APP-44, 45, 116. Applies to SOW-037, which is recorded in
    Notes because the row is ALIGNED.
- **Done-declaration questions** Q-01..Q-13 were not consulted and are not cited.

## 5. Method friction

- **AuthorityTier:** every row cites REF-006 (the PRD) as its SourceRef, so a literal reading
  makes all 42 PRD rows. Rows that also cite SCA-APP-010 were given LOCAL_DESIGN, because their
  added content comes from the SCA. Proposal: state the rule for mixed SourceRefs.
- **Many ALIGNED rows name a "daemon".** Under A2 this is read as the App-owned Runtime service
  child, which keeps the socket API. "Packaged daemon" wording was treated as stale only where
  the mechanism itself changed (019 custody, 018 first adapter). Proposal: the manager
  confirms this reading so both halves agree.
- **Deferral versus seated work:** the manager rule settled this question (§1). Before the
  rule, seated Remaining items were being treated as LIFECYCLE_GATE_PENDING divergences.
- **Static REACH versus functional use:** the pack tags `scaffold.ts` and
  `engine-conformance.ts` as LIVE only through type or barrel imports. The tags follow the
  pack, and Notes give the functional reading.
- **No test runs**, so the test case names cited are the files' first `describe` blocks.

## 6. Effort

- About 60 files read in whole or in part: the decomposition §7 to §9, CONVENTIONS,
  RUN_BASIS, D-APP-127, parts of D-APP-108 and of the register, and about 20 `_STATUS.md`
  Remaining sections. The rest were targeted code greps, all 11 capability CSVs, and the
  REACHABILITY and TOUCHED_PATHS packs.
- The context budget was adequate but not loose.
- PostReleaseBasis is NO on every row: no relied-on line falls inside a TOUCHED_PATHS range.
  The session-store.ts, app-owned-composition.ts and codex-supervisor.ts citations were each
  checked against their listed ranges.
