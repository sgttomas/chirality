# DEL-04-01 — forward-pass notes (RUN_D128, R2, PKG-04)

Frozen basis `00115c719`. Ledger `DEL-04-01_claims.csv`: 64 rows, validator 0 errors, 0 warnings.

## 1. Census

Sealed figures only (no errata file exists).

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 25 |
| STATE_ASSERTION | 15 |
| ACCEPTANCE | 14 |
| CONTEXT_CLAIM | 7 |
| REGISTER_DEFECT | 3 |

| Disposition | Rows | of which SEE rows |
|---|---:|---:|
| ALIGNED | 35 | 2 (CLM-030, CLM-021.1 → CLM-007) |
| REMAINING_STATE_MISMATCH | 12 | 5 (CLM-008, CLM-015, CLM-022, CLM-004.2, CLM-013.10 → CLM-001) |
| STALE_SPECIFICATION | 6 | 0 |
| PARTIALLY_IMPLEMENTED | 6 | 2 (CLM-013.6 → CLM-010.8; CLM-021.2 → CLM-014.2) |
| NOT_AUDITABLE | 4 | 0 |
| AUTHORITY_CONFLICT | 1 | 0 |

- **SEE rows:** 9 in total, counted separately from 55 primary rows.
- **Coverage:** all 31 indexed units are covered, plus 3 REGISTER rows and 3 STATE rows.
- **Split rate:** 5 of 31 units were split (16%), giving 32 sub-rows:
  - CLM-004: condition table rows, 2 sub-rows;
  - CLM-010: REQ-001..015, 15 sub-rows;
  - CLM-013: VER-001..011, 11 sub-rows;
  - CLM-014: records and AC-001, 2 sub-rows;
  - CLM-021: note and VER-001, 2 sub-rows.
- **Confidence:** 34 HIGH, 30 MEDIUM, 0 LOW.
- **HumanDecisionNeeded other than NO:** 10 rows (8 × R4-Q1, 2 × R4).

## 2. Least-confident rows

No row is LOW. These are the weakest MEDIUM rows, each with its alternative reading:

- **CLM-003 (AUTHORITY_CONFLICT, R4-Q1).**
  - *Reading taken:* App `docs/DIRECTIVE.md` §2.8 is unamended and still names the Claude
    Agent SDK path as the first concrete adapter and key-aware default. DIRECTIVE §0 ranks
    DIRECTIVE above CONTRACT, SPEC and PRD. The Codex-only rule arrives through the
    PRD/CONTRACT/SPEC preambles and Root DIRECTIVE §7 (the D-GOV-43 tranche), and neither
    names §2.8 or DEL-04-01. The authority order therefore does not settle the question.
  - *Alternative:* the preambles are themselves the governing interpretation rule, and Root
    DIRECTIVE outranks the App DIRECTIVE. On that reading the row is `STALE_SPECIFICATION`,
    `CODEX_SOLE_ENGINE`, NO.
- **CLM-009 (STALE_SPECIFICATION, R4).**
  - *Reading taken:* the SoW scope lags the governing decomposition row: packaged-daemon/client
    compatibility, plus the App Server observation that SCA-APP-009 added.
  - *Alternative:* the governing row itself carries retired premises (the daemon, and
    Root-owned supply), so the row is `AUTHORITY_CONFLICT`.
- **STATE-1 (REMAINING_STATE_MISMATCH, R4).**
  - *Alternative:* `DOCUMENTED_UNIMPLEMENTED` against SOW-079, because no App-side App Server
    adoption evidence exists for this deliverable.
- **CLM-010.8 / CLM-013.6 / CLM-018 / CLM-019 (PARTIALLY_IMPLEMENTED).**
  - *Reading taken:* the probe record omits SDK resume and `SessionStore` behavior.
  - *Alternative:* D-APP-68's twelve-area verdict accepted the session and transcript evidence
    as sufficient (residual area 8), which would make these rows ALIGNED.
- **CLM-014.2 / CLM-021.2 (PARTIALLY_IMPLEMENTED).**
  - *Reading taken:* the evidence package has no "future-provider criteria".
  - *Alternative:* residual area 12 and the fallback triggers count as those criteria, which
    would make these rows ALIGNED.
- **Module-level ALIGNED rows** (CLM-004.1, CLM-010.5–.7, CLM-013.3–.5, CLM-026).
  - *Alternative:* if R4-Q1 rules the retained SDK adapter to be history, these rows become
    `RETIRED_BY_RULING` or moot rather than ALIGNED.

## 3. Register-defect summary

- **REGISTER-1.** `_REFERENCES.md` REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) record
  MATCH, but their hashes do not reproduce at `00115c719`. `REFERENCE_HASHES.csv` gives
  `Match=NO`, and the change traces to the D-GOV-43 A2 amendments of 2026-09-12. DIRECTIVE,
  TYPES, PLAN and the three workflow references reproduce; I recomputed them myself. The rows
  that restate MATCH cite this key: the CLM-001 family, CLM-004.2, CLM-006, CLM-013.10, CLM-017,
  CLM-025 and CLM-029.
- **REGISTER-2.** `_DEPENDENCIES.md` declares upstream and downstream as "TBD – no accepted
  dependency edges", while the same file and `Dependencies.csv` hold 13 extracted rows.
- **REGISTER-3.** `Dependencies.csv` has no anchor rows for SOW-079 or OBJ-002, both of which the
  governing decomposition now maps to DEL-04-01 (SCA-APP-009).
- **Also recorded in rows:**
  - SoW REF-007 (`AGENT_SOFTWARE_DECOMP.md`) disagrees with `_REFERENCES.md` REF-007
    (`workflows/software-decomp/WORKFLOW.md`), and the SoW omits REF-009 and REF-010 (CLM-006).
  - The `MEMORY.md` Open Items list is stale (STATE-3).

## 4. Direction and cause

**Main CauseTags:**

- `DOC_HYGIENE` (12): reference hashes and registers.
- `PRE_V3_DRIFT` (7): the resume/`SessionStore` and future-provider gaps date from the
  2026-07-19 decision; the dependency TBD wording dates from May.
- `CARRIER_PROPAGATION` (4): SCA-APP-009's S-1 modification of DEL-04-01 (SOW-079, OBJ-002) did
  not reach the SoW, `_STATUS`, `_CONTEXT` or `Dependencies.csv`.
- `CODEX_SOLE_ENGINE` (2): CLM-003 and STATE-2.

**CAUSE2 secondaries:** `A2_TOPOLOGY` on CLM-001, CLM-009, REGISTER-1, STATE-1 and STATE-2;
`DOC_HYGIENE` on CLM-017; `PRE_V3_DRIFT` on REGISTER-2.

**Records used:**

- GOVERNING:
  - D-GOV-43, with Root `docs/DIRECTIVE.md` §7 ("Codex is the sole engine");
  - the App PRD/CONTRACT/SPEC line-13 "Current Codex-only MVP release basis";
  - SCA-APP-009 (`Impact_Assessment.md` S-1 and line 57);
  - D-APP-68 (register line 83, packet recommendation 8);
  - D-APP-38.
- CONTEXT: `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/MAPPING.md` WP-02
  and S-1.

**Searches behind each `NONE_FOUND`:**

- `_DECISIONS/_REGISTER.md` was grepped for `DEL-04-01`, `Claude`, `Codex`, `sole engine`,
  `SessionStore`, `resume` and `future-provider`. The only DEL-04-01 rows are D-APP-63 and
  D-APP-68, and neither addresses the gaps.
- CONTEXT: the `APP_V3_PATHWAY_SEATING` MAPPING and the SCA-APP-009 folder.
- The deliverable folder was grepped for `future-provider`, `SessionStore` and `resume`.

**Other notes:**

- `D-APP-127_APPLICATION_MAP.csv` shows that no DEL-04-01 carrier cites D-APP-127 or D-GOV-43.
- The done-declaration questions (Q-01..Q-13) were not used.

## 5. Method friction

- **REACH tags on non-module paths.** Manifests (`frontend/package.json`) and scripts
  (`frontend/scripts/*.mjs`) match the validator's code-path pattern, but `REACHABILITY.csv`
  does not map them.
  - *What I did:* I cited them as "outside the REACH map" beside a tagged consuming module.
  - *Proposed revision:* either add a tag such as `REACH=TOOLING`, or exempt `package*.json`
    and `scripts/` from V-REACH.
- **Mixed tables that are not REQ/AC/VER items** (CLM-025 bullets, CLM-019 criteria).
  - *Problem:* one lagging bullet forces a non-ALIGNED disposition on an otherwise aligned unit.
  - *Proposed revision:* allow splitting of bulleted lists whose items can be dispositioned
    independently.
- **A deliverable whose whole subject is a legacy engine.**
  - *Problem:* documentary requirements are met as records, but their standing depends on
    R4-Q1. I kept ALIGNED at record and module level and put the direction question on CLM-003
    alone, to avoid flagging R4-Q1 on 40 rows.
  - *Proposed revision:* the verifier should confirm or reject this concentration.

## 6. Effort

- About 30 targeted reads and greps over the frozen tree:
  - the SoW, `_STATUS`, `_CONTEXT`, `_REFERENCES`, `MEMORY`, `_DEPENDENCIES`,
    `Dependencies.csv`, the Decision and Evidence files, and INSP-03;
  - the App DIRECTIVE, PRD, CONTRACT and SPEC preambles, and Root DIRECTIVE §7;
  - the decomposition rows;
  - D-APP-68, D-APP-127, D-GOV-43 and SCA-APP-009;
  - about ten code and test spot-checks.
- I also used the evidence pack and PREGATHER, and ran read-only git: `log -S SOW-079`,
  `log` on PRD, `show d6f6cadb2`, and one `blame -L` on `codex-app-server-client.ts:6-8`
  (not touched).
- No cited file appears in `TOUCHED_PATHS.csv`, so PostReleaseBasis is NO on every row.
- The context budget was adequate, not tight.
