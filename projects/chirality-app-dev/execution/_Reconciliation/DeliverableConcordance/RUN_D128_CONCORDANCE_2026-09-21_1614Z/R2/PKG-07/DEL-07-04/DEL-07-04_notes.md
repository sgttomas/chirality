# DEL-07-04 Status Transition API and MCP Tool — R2 forward notes (pass 1)

Basis: frozen tree at `00115c719`. Ledger: `DEL-07-04_claims.csv` (67 rows). Validator: `RESULT PASS errors=0 warnings=0`.

## 1. Census

**By Disposition (sealed):** STALE_SPECIFICATION 21 · PARTIALLY_IMPLEMENTED 18 · ALIGNED 12 ·
NOT_AUDITABLE 6 · DOCUMENTED_UNIMPLEMENTED 5 · REMAINING_STATE_MISMATCH 3 · AUTHORITY_CONFLICT 1 ·
ACCEPTED_DIVERGENCE 1.

**By ClaimType:** REQUIREMENT 24 · ACCEPTANCE 16 · CONTEXT_CLAIM 13 · STATE_ASSERTION 10 · REGISTER_DEFECT 4.

**ClaimType × Disposition:**

| ClaimType | Dispositions |
|---|---|
| REQUIREMENT (24) | PARTIALLY_IMPLEMENTED 11, ALIGNED 6, DOCUMENTED_UNIMPLEMENTED 3, STALE_SPECIFICATION 2, AUTHORITY_CONFLICT 1, ACCEPTED_DIVERGENCE 1 |
| ACCEPTANCE (16) | PARTIALLY_IMPLEMENTED 7, ALIGNED 6, DOCUMENTED_UNIMPLEMENTED 2, STALE_SPECIFICATION 1 |
| CONTEXT_CLAIM (13) | STALE_SPECIFICATION 7, NOT_AUDITABLE 6 |
| STATE_ASSERTION (10) | STALE_SPECIFICATION 9, REMAINING_STATE_MISMATCH 1 |
| REGISTER_DEFECT (4) | STALE_SPECIFICATION 2, REMAINING_STATE_MISMATCH 2 |

**SEE rows (counted separately, MR-4):** 15 in total (all 15 are also counted in the Disposition figures
above):

- 10 point to `REGISTER-1`, the REF-006 / PRD MATCH restatements: CLM-001, 006, 009, 011.18, 013.11,
  017, 024, 026, 033 and 034.
- 1 points to `REGISTER-2`: CLM-008.
- 4 point to earlier units: CLM-013.9→CLM-011.16, CLM-020→CLM-010, CLM-022→CLM-014 and
  CLM-023→CLM-019.

Without SEE rows there are 52 dispositioned rows: STALE_SPECIFICATION 9, PARTIALLY_IMPLEMENTED 15,
ALIGNED 12, NOT_AUDITABLE 6, DOCUMENTED_UNIMPLEMENTED 5, REMAINING_STATE_MISMATCH 3,
AUTHORITY_CONFLICT 1, ACCEPTED_DIVERGENCE 1.

**Split rate:** 2 of 34 indexed units split (5.9%). CLM-011 (the requirement table) → `.1`–`.18`, one per
DEL-07-04-REQ-001..018 (independently dispositionable table rows; index lists no SubItems for it).
CLM-013 → `.1`–`.12`, one per listed SubItem in index order (REQ-001, 003, 005, 007, 009, 011, 013, 015,
016, 017, 018, 004); each row names its item in Notes. CLM-016 (AC-001) and CLM-025 (VER-001) list one
item each and take one row. Run-local rows: REGISTER-1..4, STATE-1.

**HumanDecisionNeeded:** NO 43; R4-Q1 on 19 rows; R4-Q3 on 7 rows (two rows carry both).

No errata file exists (pass 1).

## 2. Least-confident rows

- **CLM-032** (Conflict table, LOW). Sealed STALE_SPECIFICATION: the table stands as the current "for
  human ruling" table with no rows, while three source conflicts now exist (SPEC §4.3 reversal amendment
  vs REQ-004; D-GOV-43 Codex-only basis vs unamended SPEC §14.2 / K-MCP-1; D-APP-13 vs K-AUTH-1/K-GATE-1).
  Alternative: NOT_AUDITABLE, because the row says "during P1/P2 drafting" and was true then (MR-8(iv)
  snapshot reading).
- **CLM-013.7** (REQ-013 verification, LOW). Sealed PARTIALLY_IMPLEMENTED. Alternative: ALIGNED, if the
  INSP-03 REQ-013 review conclusion counts as the "review check" the row allows.
- **CLM-011.13** (REQ-013, MEDIUM). Sealed AUTHORITY_CONFLICT (R4-Q3). Alternative: PARTIALLY_IMPLEMENTED
  on the live route with D-APP-13 read as governing only the MCP tool. I chose the conflict because
  D-APP-13 declares a format-valid `approvalSha` with actor `HUMAN` "required and sufficient", which
  undercuts unamended K-AUTH-1/K-GATE-1 without naming them.
- **CLM-011.4** (REQ-004, MEDIUM). Sealed STALE_SPECIFICATION (SoW restates the pre-2026-07-11 SPEC
  §4.3 text; DIRECTIVE §0 puts the amended SPEC above the SoW). ALSO:PARTIALLY_IMPLEMENTED — the code
  equally lacks the two human reversal transitions.
- **CLM-011.9 / .10 / .11** (MCP exposure). Sealed DOCUMENTED_UNIMPLEMENTED on the live path with
  ALSO_MODULE verdicts. An AUTHORITY_CONFLICT reading (D-GOV-43 vs unamended SPEC §14.2 / K-MCP-1 /
  FR-119) is also defensible; R4-Q1 is cited either way.
- **Reach of the status routes** (CLM-011.7, .8 and every REACH_NOTE row). Tagged REACH=LIVE as Next
  API route handlers, which run on request. No rendered UI calls them (see §5), so "LIVE" means
  "an executable product endpoint", not "a path the product exercises".

## 3. Register-defect summary

- **REGISTER-1** — `_REFERENCES.md` REF-002 (CONTRACT), REF-003 (SPEC), REF-006 (PRD) recorded MATCH;
  none reproduces (`HASH-RECOMPUTE@00115c719`, pack `REFERENCE_HASHES.csv`). I recomputed REF-001
  DIRECTIVE, REF-004 TYPES and REF-005 PLAN with `shasum` at the frozen tree: they reproduce. REF-007/009/010
  (Root workflows) are outside the evidence roots. The INSP-03 P40 annotation records a third PRD
  "MATCH" hash (`ac35fba4…`) that disagrees with `_REFERENCES.md` (`8649ccba…`). Ten SEE rows point
  here. CLM-004, CLM-012, CLM-016 and CLM-029 also restate the MATCH claim, as part of mixed rows.
- **REGISTER-2** — `Dependencies.csv` DEP-07-04-008 is SATISFIED with TargetLocation
  `frontend/src/lib/harness/status-transition.ts; frontend/src/lib/harness/mcp/status-tools.ts`. Neither
  file exists, and `git log` shows no history for either path, so the D-APP-56 R5 P45 UPD-132 correction
  was wrong when written. The real modules are `frontend/src/lib/lifecycle/{status-parser,transition,status-writer}.ts`,
  `frontend/src/lib/workspace/deliverable-contracts.ts`, the two routes, and (legacy)
  `frontend/src/lib/harness/mcp/read-tools.ts`. MEMORY.md:10 repeats the claim.
- **REGISTER-3** — `_DEPENDENCIES.md` lags its own P45 block and the CSV (TBD edges, the
  IMPLEMENTATION_LOCATION_TBD warning, a TBD summary count). The run notes also name
  Datasheet/Specification/Guidance/Procedure.md, which no longer exist.
- **REGISTER-4** — `_STATUS.md` header: Last Updated 2026-07-12 is behind the 2026-07-19 history entry.
  Authorization Basis still names D-APP-19 after the D-APP-54 rebaseline superseded it, and the Checking
  Approval SHA is carried while the state is IN_PROGRESS.
- **STATE-1** — `_STATUS.md ## Remaining` is empty even though the evidence shows open deliverable
  scope (rule 2(a)).
- **Carrier propagation.** No DEL-07-04 carrier cites D-APP-127 / D-GOV-43 (pack map: all five NO).
  The SoW, `_CONTEXT.md` and `Dependencies.csv` still describe the in-process SDK MCP surface as the
  product surface (CLM-003, CLM-005, CLM-010).

## 4. Direction and cause

- **CauseTags:** DOC_HYGIENE 17, PRE_V3_DRIFT 14, CODEX_SOLE_ENGINE 12, CARRIER_PROPAGATION 6, NONE 18.
  CAUSE2 secondaries: CARRIER_PROPAGATION on the hash-restatement rows; PRE_V3_DRIFT on the mixed
  live/legacy rows (CLM-003, 006, 011.12, 012, 021, 025, 028, 032, STATE-1); DOC_HYGIENE on CLM-004.
- **GOV direction used:**
  - D-GOV-43: Codex sole engine, and the CONTRACT/SPEC/PRD amendments of 2026-09-12 that explain the
    hash drift.
  - D-APP-13: ruled the workspaceWrite-gated `status_transition` MCP tool, with `approvalSha` + `HUMAN`
    "required and sufficient".
  - D-APP-54: the lifecycle rebaseline.
  - D-APP-66: content-SHA revalidation kept as a governance checklist, which makes REQ-014 an
    ACCEPTED_DIVERGENCE.
- **CONTEXT records:** none explained a DEL-07-04 divergence.
- **Searches behind every `NONE_FOUND`:**
  - `_DECISIONS/_REGISTER.md`, grepped for status transition, `status_transition`, DEL-07-04, R4-P19 and
    actor. Hits: D-APP-13, D-APP-55, D-APP-56 R4-P19, D-APP-66. None covers reversal transitions, the
    missing human cells in the actor table, dropping `## Remaining` on write, schema fixtures, or the
    UPD-132 module paths.
  - CONTEXT sources: `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`,
    `plans/steers/`, `AgentRuns/APP_V3_*`, `APPDEV_V3_NODE_*` and `CHIRALITY_V3_APP_ADOPTION_20260909`,
    grepped for `status_transition`, `mcp__chirality`, "Chirality MCP" and DEL-07-04. Only APP_V3
    decision-source copies of this deliverable's own files were found; no direction.
- **Named R4 questions:**
  - **R4-Q1:** every row where the MCP tool, or the permission/hook policy half of a guarantee, is met
    only by LEGACY_ONLY `read-tools.ts`. I also cited it on mixed rows whose verdict would change with
    the R4-Q1 answer (brief: cite the named question whenever the row turns on it).
  - **R4-Q3:** actor authorization on both surfaces. The actor is a free string in the POST body
    (`route.ts:11-19,59`) and in the MCP args (`read-tools.ts:110-117`).
  - **R4-Q4:** not cited. SPEC §4.3's actor vocabulary (PREPARATION / 4_DOCUMENTS / CHIRALITY_FRAMEWORK)
    uses pre-v3 agent names, but SPEC §4.3 is not among the clauses R4-Q4 names. Flagged in CLM-011.5
    Notes for R3.

## 5. Method friction

- **Reach confirmation.**
  - `REACHABILITY.csv` marks `pipeline-surface.tsx` and `workbench-surface.tsx` LIVE via
    `loop-shell.tsx` → `tertiary-sidebar-tabs.tsx`.
  - `LoopShell` is passed only as the `legacy` prop of `WovenDialogueRoute`, which discards it
    (`woven-dialogue-route.tsx:16-18`, `void legacy`). The `/pipeline` and `/workbench` pages do the same.
  - So the only UI callers of `fetchDeliverableStatus` / `transitionDeliverableStatus`
    (`pipeline-surface.tsx:406,572`, `workbench-surface.tsx:263,395`) are never rendered.
  - The route handlers remain executable Next endpoints, so I tagged them LIVE and recorded the
    no-caller fact in Notes.
  - `read-tools.ts` is LEGACY_ONLY in the map. I confirmed the Codex path registers no Chirality MCP
    server: the runtime packages grep finds only a fingerprint `mcpServers: []` at `runtime-service.ts:580`.
  - The post-release Runtime dynamic-tool facility (`packages/daemon/src/application-tools.ts`, touched
    paths) exists, but the App registers no status tool with it. I mention it only in Notes, so no
    PostReleaseBasis applies.
- **PostReleaseBasis.** No file cited as evidence is in `TOUCHED_PATHS.csv`, so every row is `NO`. No
  blame was needed. Read-only blames of `transition.ts` and `docs/SPEC.md` dated the drift instead.
- **Proposal: no-caller reach tag.** The REACH vocabulary has no value for "executable endpoint with no
  product caller". A `REACH=LIVE` qualifier (for example a `NO_CALLER` Notes token) would keep
  route-only surfaces from reading as exercised.
- **Proposal: R4-Q1 on mixed rows.** Rule 3 of the subject test says cite R4-Q1 when the *only* code is
  legacy. On mixed rows the verdict still turns on R4-Q1. I cited it there and said so. A one-line
  clarification would settle this.

## Coverage gaps

- **Writer behaviour.** A transition rewrites `_STATUS.md` from parsed fields only
  (`status-writer.ts:89-123,125-160`). That drops `## Remaining` and every free-form history line. No
  SoW unit states a Remaining-preservation requirement; the only anchor is SPEC §4.1 as amended
  2026-07-11. I recorded it on CLM-011.2 (REQ-002 history extraction), which fits only partly.
- **`_SEMANTIC.md` / `_SEMANTIC_LENSING.md`.**
  - Neither file is an indexed unit.
  - They carry absolute machine paths and a 2026-05-20 "PRD HASH_MISMATCH" warning as dated
    generation records.
  - They have no rows. CLM-004 covers the SoW's false "NOT_GENERATED" claim about them.
- **`_CONTEXT.md`.** Accurate against the decomposition. It has no D-APP-127 revision (pack map), but
  states nothing now false, so it has no row.

## 6. Effort

- About 45 file reads or greps, including:
  - all DEL-07-04 carriers, the SoW and INSP-03;
  - the route, lifecycle, workspace-contracts and MCP modules, plus shell reach files;
  - three test files;
  - SPEC §4, §14 and §17.2, the CONTRACT invariants, and the PRD FR rows;
  - the D-APP-13 and D-APP-56 rulings and the register.
- Context budget was adequate, not tight.
