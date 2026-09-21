# DEL-06-04 notes (R2 forward pass, PKG-06)

Deliverable: DEL-06-04 Write/Edit Surface and Path Hooks. Frozen basis `00115c719`. Ledger
`DEL-06-04_claims.csv`, 63 rows. Sealed SHA-256
`b9add1f7f08d6e6738d0a6ea86e82e78692358587b70acb700a42964529f9cd2`. Validator: `RESULT PASS errors=0 warnings=0`.

## 1. Census

- **Units:** 32 indexed units (CLM-001..CLM-032). There are no REM or REMTXT units, because the `_STATUS.md` Remaining list is empty. All 32 units are covered.
- **Rows:** 56 indexed rows plus 7 run-local rows (STATE-1..3, REGISTER-1..4).
- **Split rate:** 5 of 32 units were split (15.6%):
  - CLM-004: Conditions table, 7 rows;
  - CLM-009: DEL-06-04-REQ-001..016, 16 rows;
  - CLM-013: traceability table plus AC-001;
  - CLM-019: records list plus VER-001;
  - CLM-032: AC-002 and VER-002.
  - V-SUBITEMS is satisfied.
- **SEE rows:** 15, counted separately below.

| ClaimType | All rows | Non-SEE rows |
|---|---:|---:|
| REQUIREMENT | 34 | 25 |
| STATE_ASSERTION | 10 | 6 |
| CONTEXT_CLAIM | 9 | 9 |
| ACCEPTANCE | 6 | 4 |
| REGISTER_DEFECT | 4 | 4 |

| Disposition | All rows | Non-SEE rows |
|---|---:|---:|
| STALE_SPECIFICATION | 21 | 15 |
| AUTHORITY_CONFLICT | 18 | 13 |
| PARTIALLY_IMPLEMENTED | 7 | 5 |
| NOT_AUDITABLE | 6 | 6 |
| ALIGNED | 6 | 4 |
| IMPLEMENTED_DIFFERENTLY | 3 | 3 |
| DOCUMENTED_UNIMPLEMENTED | 1 | 1 |
| REMAINING_STATE_MISMATCH | 1 | 1 |

- **HumanDecisionNeeded:** R4-Q1 on 31 rows; NO on 32.
- **Confidence:** HIGH 26; MEDIUM 36; LOW 1.
- **Errata:** none. This is pass 1, so there are no errata-applied figures yet.

## 2. Least-confident rows

- **`CLM-009.5` (REQ-005 exact edit; LOW; DOCUMENTED_UNIMPLEMENTED).**
  - What I found: the live Codex path has no Chirality precondition check on fileChange.
  - Alternative reading: `IMPLEMENTED_DIFFERENTLY`, if Codex apply_patch context matching is accepted as the PRD 7.9 exact precondition. That behaviour is external to the repo and not evidenced here.
- **`CLM-009.4` (symlink; MEDIUM).** Codex/Seatbelt sandbox behaviour for in-root symlinks is not evidenced in the repo. The alternative reading is `PARTIALLY_IMPLEMENTED`.
- **`CLM-032.1` (AC-002; MEDIUM; AUTHORITY_CONFLICT).**
  - Alternative reading: module-level `ALIGNED` for the retained managed-delegation path.
  - This row applies if the owner rules that D-APP-68 managed children are legacy-only history. That question is R4-Q1.
- **`CLM-009.8`, `.11`, `.12` (IMPLEMENTED_DIFFERENTLY; MEDIUM).**
  - These treat the Codex sandbox and the Codex fileChange/approval event stream as the live mechanism.
  - Persistence of sandbox-denied writes as records is not proved by a test.
- **`STATE-2` (daemon conformance; MEDIUM).** The wording is inherited from the decomposition package row, so the repair may belong to the decomposition rather than this carrier.

## 3. Register-defect summary

- **REGISTER-1 (hash drift).** The `_REFERENCES.md` MATCH hashes for REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) do not reproduce (`HASH-RECOMPUTE@00115c719`).
  - My own recompute shows REF-001, 004 and 005 (DIRECTIVE, TYPES, PLAN) and REF-007, 009 and 010 (the software-decomp workflow files) do reproduce.
  - SoW rows that restate it: CLM-001/007/020/028, CLM-004.1, CLM-006, CLM-010, CLM-016, CLM-031, CLM-009.16.
- **REGISTER-2.** `_STATUS.md` "Last Updated" says 2026-07-12, but the History has a 2026-07-19 entry.
- **REGISTER-3.** `_DEPENDENCIES.md` Declared Upstream/Downstream still says "TBD - no accepted dependency edges", which contradicts its own register and `Dependencies.csv`. SoW CLM-004.7 repeats the same stale claim.
- **REGISTER-4.** DEP-06-04-010 is marked SATISFIED on the premise that REF-006 is MATCH, which fails (see REGISTER-1). Its EvidenceQuote still says HASH_MISMATCH.
- **Stale conflict table (CLM-031).** CONFLICT-002 was garbled by the D-APP-56 mechanical rewrite ("content-accessible but current and MATCH"). CONFLICT-001 (root naming) has been open since 2026-05.
- **Carrier propagation.** No DEL-06-04 carrier cites D-APP-127 or D-GOV-43 (application map: all NO). `_CONTEXT.md` still names the Claude Agent SDK as the current path (STATE-1) and includes "daemon conformance" (STATE-2).
- **Not rowed (history only).** `_SEMANTIC.md` / `_SEMANTIC_LENSING.md` (generated 2026-05-20) list retired four-document inputs and machine-specific paths.

## 4. Direction and cause

- **Main CauseTag: CODEX_SOLE_ENGINE (29 rows).**
  - The whole enforcement design exists only in the retained, LEGACY_ONLY Claude SDK harness:
    - `chirality-hooks.ts` PreToolUse/PostToolUse;
    - `tool-path-policy.ts` containment, instruction-root and symlink checks;
    - `permission-overlay.ts`;
    - mutating MCP in `mcp/read-tools.ts`.
  - On the live Codex path, writes are bounded only by the user-chosen Codex sandbox and approval policy:
    - `codex-supervisor.ts:104-110` maps the choice to a sandbox, with workspace-write using writableRoots [cwd];
    - `delegated.ts:322-331` maps App permission modes to Codex policy;
    - `chat-panel.tsx:129-134` offers the choices, including Full access, which is danger-full-access with approval never.
  - CONTRACT K-PATH-2/3, K-ROOT-2, K-HOOK-1, K-PERM-1/3, K-MCP-1 and SPEC 14.3/15.1/15.2 are unamended for D-GOV-43. Every row restating them is therefore `AUTHORITY_CONFLICT` with R4-Q1 (MR-11: D-GOV-43 does not name these clauses).
- **Other tags:**
  - DOC_HYGIENE (14): hash and register rows.
  - PRE_V3_DRIFT (6): TBD markers left stale after ADQ-11/D-APP-43 (2026-06-21), plus the VER-002 test gap.
  - NATIVE_DELEGATION (1): CLM-032.1.
  - A2_TOPOLOGY (1): STATE-2.
- **CAUSE2 secondaries:** CARRIER_PROPAGATION, A2_TOPOLOGY, CODEX_SOLE_ENGINE, PRE_V3_DRIFT, DOC_HYGIENE.
- **Records used for DirectionEvidence:**
  - GOV: D-GOV-43, via App CONTRACT K-UNTYPED-1 and K-ENGINE-3; D-APP-38; D-APP-43; D-APP-127.
  - CTX: `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, on the outer authority boundary enforced by the App Server sandbox (G-SBX/G-PROT).
- **Searches behind each NONE_FOUND:**
  - `_REGISTER.md` rows D-APP-38/43/68/70/127 and a grep for DEL-06-04.
  - D-GOV-43 and its A2 supplement grepped for sandbox/approval/hook: no clause naming K-PATH, K-ROOT or K-HOOK.
  - D-APP-127 grepped for sandbox/hook/PKG-06: nothing.
  - CONTEXT plan/steers grepped for sandbox and protected-path.
  - NONE_FOUND rows: REGISTER-2, REGISTER-3, CLM-004.7, CLM-032.2.
- **Other cross-deliverable observations:**
  - The legacy exact-edit check accepts an `old_string` that occurs more than once (count ≥ 1) and does not require uniqueness.
  - No test injects a PreToolUse hook exception (REQ-006).
  - INSP-03's REQ006 evidence was Bash-policy tests.

## 5. Method friction

- **R4-Q1 scope.** R4-Q1 names K-PATH, K-ROOT, K-HOOK and SPEC 15.2, but K-PERM-1 and K-MCP-1 rows turn on the same question. I cited R4-Q1 for them. Proposal: widen the R4-Q1 text to "PKG-06 hook/overlay invariants".
- **Tier for REQ-011/012.** PLAN.md is not in the GOVERNING map but appears as a source. I tiered by PRD where PRD is also cited, and used LOCAL_DESIGN for REQ-015.
- **Dated history rows.** MEMORY.md-style dated entries fit STATE_ASSERTION = ALIGNED "as history". A rule saying explicitly that dated carrier entries are judged as of their date would help.

## 6. Effort

- **Files read:** about 30, including:
  - the deliverable carriers;
  - `chirality-hooks.ts` and `tool-path-policy.ts` in full;
  - targeted ranges of `read-tools.ts`, `codex-supervisor.ts`, `delegated.ts`, `chat-panel.tsx`, `delegated-engine-adapter.ts` and `agent1-run-coordinator.ts`;
  - test case lists;
  - CONTRACT/SPEC excerpts, the register, and the D-APP-127, D-APP-70 and D-GOV-43 records.
- **Blame:** read-only `git blame -L` was run on `codex-supervisor.ts` lines 40, 104-112, 255-262 and 719-731. None blame to the four post-release commits, so `PostReleaseBasis` is NO. No other cited file is in `TOUCHED_PATHS.csv`.
- **Context budget:** moderate; not tight.
