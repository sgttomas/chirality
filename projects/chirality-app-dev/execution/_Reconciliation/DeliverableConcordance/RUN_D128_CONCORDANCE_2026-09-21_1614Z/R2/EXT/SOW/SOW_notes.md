# SOW notes (merged from the two half workers)

Merged by `_scripts/merge_sow.py`. Half A covers SOW-001..042 and half B SOW-043..084;
each half's notes follow unchanged.


---

# Half A (`SOW_A/SOW_notes.md`)

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


---

# Half B (`SOW_B/SOW_notes.md`)

# SOW half B notes (SOW-043..SOW-084): RUN_D128 R2 extension item 5

Ledger: `SOW_claims.csv`. It has 62 rows covering 42 units, validates against `EXTENSION_INDEX_SOW_B.csv` with 0 errors and 0 warnings, and is sealed (SHA-256 in `RETURN.md`). No run-local keys were needed: no `SOW:REGISTER-n` or `SOW:STATE-n` rows (the reserved range 51–99 is unused).

## 1. Census

| ClaimType | Disposition | Rows |
|---|---|---|
| REQUIREMENT | ALIGNED | 36 |
| REQUIREMENT | PARTIALLY_IMPLEMENTED | 8 |
| REQUIREMENT | IMPLEMENTED_DIFFERENTLY | 8 |
| REQUIREMENT | DOCUMENTED_UNIMPLEMENTED | 3 |
| REQUIREMENT | AUTHORITY_CONFLICT | 2 |
| REQUIREMENT | STALE_SPECIFICATION | 1 |
| EXCLUSION | ALIGNED | 3 |
| EXCLUSION | AUTHORITY_CONFLICT | 1 |

- **Split rate.** 20 of 42 units (48%) are split into `.1`, a live-deliverable mapping row, and `.2`, a code or deferral row. A unit was split whenever its two parts took different dispositions. In 19 of the 20, `.1` is ALIGNED and the finding sits on `.2`. SOW-079 is the exception: both parts are non-ALIGNED.
- **SEE rows:** 0. No normative statement recurs within this half.
- **Other counts.**
  - Confidence: 24 HIGH, 35 MEDIUM, 3 LOW.
  - PostReleaseBasis YES: 3 rows (SOW-047.2, 048.2, 064.2). Each cites the Runtime application-tool hosting that `da95ec194` added.
  - HumanDecisionNeeded:
    - `R4-Q1`: 6 rows (045.2, 050.2, 052.2, 057.2, and ALIGNED rows 068 and 070 by rule 3);
    - `R4`: 2 rows (075.2, 076);
    - `R4-Q2; R4-Q5`: 1 row (044.2);
    - `R4-Q5`: 1 row (061.2);
    - `D-APP-116`: 1 row (059.2);
    - `D-APP-119`: 1 row (084.2);
    - `NO`: the remaining 50 rows.
- **Manager summary tokens.**
  - `NO_LIVE_DELIVERABLE` (2 rows):
    - SOW-079.1: the decomposition names DEL-04-01, but DEL-04-01 `_STATUS.md` records the item as `SCOPE_AMENDMENT_REQUIRED` and its SoW does not cite SOW-079.
    - SOW-080: its only owner, DEL-09-07, was retired by D-APP-127.
  - `NO_CODE_NO_DEFERRAL` (1 row): SOW-084.2, for its organisation-layer part only. The bundled base layer is live.

## 2. Least-confident rows (with alternative readings)

- **SOW-061.2 (LOW), PARTIALLY_IMPLEMENTED.** Codex `contextCompaction` reaches the App only as a generic `codex.notification`. There is no compaction-specific view and no replay check.
  - Alternative: DOCUMENTED_UNIMPLEMENTED with R4-Q1, since only the legacy Pi mapper emits named compaction events.
- **SOW-075.2 (LOW), AUTHORITY_CONFLICT.** The effective Codex home shares the user's `memories` and `sessions/` by reference (CTX SPIKE_DESIGN §3), outside the project checkout. DIRECTIVE §2 ("no hidden project memory") is unamended.
  - Alternative: ALIGNED, if Codex memories count as user-level context rather than project memory.
- **SOW-076 (LOW, OUT), AUTHORITY_CONFLICT.** The live chat panel ships a "Full access" mode (`danger-full-access`, approval `never`) and loads the user's Codex `config.toml`. This crosses the literal boundary. The governing texts point both ways:
  - D-GOV-43 and the amended CONTRACT K-UNTYPED-1 make approval and sandbox the user's choice.
  - PRD non-goals and CONTRACT K-PERM-6/K-SDK-1 are unamended and SDK-worded.
  - Alternative: ALIGNED, reading the boundary as naming only SDK `bypassPermissions` and Claude Code settings.
- **MEDIUM rows that could reasonably go another way:**
  - SOW-050.2: AUTHORITY_CONFLICT versus IMPLEMENTED_DIFFERENTLY. The live path exposes writes and shell from the first turn, against the decomposition's read-first sequencing invariant.
  - SOW-048.2: PARTIALLY_IMPLEMENTED versus ALIGNED at module level. The descriptor contracts are live modules, but the App registers no tools.
  - SOW-052.2: DOCUMENTED_UNIMPLEMENTED versus PARTIALLY_IMPLEMENTED. The live toolkit still collects `maxTurns`, but the Runtime ignores `opts`.
  - SOW-043: ALIGNED. The daemon-shape migration is read as deferred by DEL-05-01-V3-02, whose Root DEL-02-11 gate premise A2 may have changed.

## 3. Register-defect summary

No REGISTER rows. Observations for the manager:

- **The decomposition was never updated after D-GOV-43 / D-APP-127.** Its last change is the SCA-APP-010 Gate-5 application `dbd812a52`. As a result:
  - SOW-080 still reads IN, and its Notes say "F-APP-2/D-APP-97 remain active";
  - OI-003 and OI-007 still carry the DEL-09-07 installer and Root-owned supply;
  - OBJ-008 still lists SOW-080.
- **SOW-080** is recorded as STALE_SPECIFICATION under MR-11. D-APP-127 names DEL-09-07, and the ledger row lies outside the preserved set.
- **SOW-079 mapping.** The decomposition's §8 row for DEL-04-01 and its §9 row name DEL-04-01, but DEL-04-01 does not carry the item. SOW-079.1 is recorded as DOCUMENTED_UNIMPLEMENTED with CARRIER_PROPAGATION.
- **Cross-deliverable, not in this ledger.** DEL-07-03 `_STATUS.md` has no `## Remaining` section. Yet its History (2026-09-05) says DEL-07-03-V3-01 was "retained". This belongs to the PKG-07 ledger.

## 4. Direction and cause

- **Main CauseTags:**
  - CODEX_SOLE_ENGINE, 15 rows: SDK-era mechanisms (canUseTool, hooks, Chirality overlay, Bash and path policy, the tool pool, `maxTurns`) replaced by Codex approval requests and the PolicySelection sandbox pairs.
  - A2_TOPOLOGY, 5 rows: SOW-056.2, 064.2, 075.2, 079.2, 080.
  - SHELL_REDESIGN, 2 rows: SOW-081.2, 084.2.
  - CARRIER_PROPAGATION, 1 row: SOW-079.1.
- **CAUSE2 secondaries:**
  - A2_TOPOLOGY: 044.2, 045.2, 076;
  - CODEX_SOLE_ENGINE: 056.2, 064.2, 075.2, 079.2;
  - DOC_HYGIENE: 079.1.
- **No `OTHER:` tokens used.**
- **Records cited:**
  - GOV: D-APP-127, with D-GOV-43 items 3 and 6 as it records them.
  - CTX:
    - `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/SPIKE_DESIGN.md`: §3 effective home, §4 PolicySelection and delegation, §6 event representation, §7 server requests ("we register none" for dynamic tools), §8, §10;
    - `APP_V3_PATHWAY_SEATING_2026-09-03/MAPPING.md`, for SOW-079.1;
    - the amended App `docs/CONTRACT.md` K-UNTYPED-1.
- **Searches behind each `NONE_FOUND` DirectionEvidence:**
  - SOW-052.2: searched `_DECISIONS/_REGISTER.md` for "maxTurns / max-turn / max turn" (0 hits) and SPIKE_DESIGN.md (0 hits).
  - SOW-057.2: searched `_REGISTER.md` for "hook" (2 hits, both D-APP-04-era capability lanes and irrelevant) and SPIKE_DESIGN.md (no hook direction).
  - SOW-084.2: searched `_REGISTER.md` for "organisation" (1 hit, D-APP-119, AWAITING_RULING, cited in HumanDecisionNeeded) and SPIKE_DESIGN.md (none).
- **Code searches behind `NONE_FOUND` ImplementationEvidence:** SOW-057.2 (hook callbacks), SOW-080 (launchd installer), SOW-082 (`proposal.offered`, ProposalCard, propose tool), SOW-083 (per-chat delegation policy) and SOW-084.2 (organisation layer). Each search covered `frontend/src`, `frontend/electron` and `chirality-runtime/packages` (execution excluded).
- **Done-declaration context (Q-01..Q-13):** not relied on for any row.
- **D-APP-87** (dual target, domain-first; PENDING_EFFECT) is cited only as `(context)` on the domain rows.

## 5. Method friction

- **What counts as "explicit deferral".** A gated Remaining item (`NOT_SELECTABLE_UNTIL: …`) was read as deliverable text that explicitly defers the work. On that reading:
  - SOW-043, 063, 082 and 083 are ALIGNED;
  - SOW-084's SELECTABLE item DEL-07-01-V3-01 is not a deferral;
  - SOW-081's DEL-02-02-V3-04, whose gates appear landed, is not a deferral either.
  - Proposal: state in §8 whether a gated Remaining item satisfies "explicit deferral", or whether only a ruling or OUT/future-boundary text does.
- **R4-Q1 on ALIGNED rows.** Rule 3 is mechanical, so SOW-068 and SOW-070 cite R4-Q1 even though they are ALIGNED through the DEC-006/OI-005 deferral. Proposal: limit rule 3 to rows whose disposition rests on code.
- **Build-pipeline evidence has no REACH vocabulary.** `package.json` and `frontend/scripts/*.mjs` are not in `REACHABILITY.csv`. They were tagged `REACH=LIVE` as the product build pipeline, with a Note saying so, because `LEGACY_ONLY` plus UNREACHED would wrongly trigger R4-Q1. Proposal: add a `BUILD` reach class, or exempt build configuration from tagging.
- **The authority tier of decomposition rows.** RUN_BASIS §5 lists the decomposition as GOVERNING, yet Ruling D makes its ledger rows audit targets. AUTHORITY_CONFLICT was used only where a ruling contradicts the row's substance (SOW-050, 075, 076), not for mechanism changes (IMPLEMENTED_DIFFERENTLY).
- **The two-part split.** Nearly every non-ALIGNED IN row splits, because the mapping part is almost always ALIGNED. This doubles those rows without adding information. Proposal: make `.1` implicit when it is ALIGNED.

## 6. Effort

- **Files read:** about 25 files or ranges.
  - Rulebook and briefs; the decomposition's §9, §2.2, §11 and §12 ranges; D-APP-127.
  - About 20 deliverable `_STATUS.md` Remaining extracts and grep hits across the SoWs.
  - About 15 code files by grep and short ranges; SPIKE_DESIGN §3–4; the evidence-pack CSVs, read by script.
- **Budget:** the context budget was adequate but not loose.
- **Not done:** no test runs and no installs. Git was not needed beyond one `git log` on the decomposition file.
