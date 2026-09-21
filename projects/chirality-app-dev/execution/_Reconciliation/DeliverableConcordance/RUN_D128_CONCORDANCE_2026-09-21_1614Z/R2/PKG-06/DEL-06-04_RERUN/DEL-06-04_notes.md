# DEL-06-04 concordance notes — rerun (pass 1, forward)

Independent rerun ledger `DEL-06-04_claims.csv` (62 rows). It was built without reading the
original DEL-06-04 ledger folder, `_verify`, or `R0_CALIBRATION`. Basis: frozen tree `00115c719`.

## 1. Census

- **Rows:** 62, covering 32 indexed units (CLM-001..CLM-032). There are 56 unit rows plus 6 run-local
  rows (REGISTER-1..4, STATE-1..2).
- **Split rate:** 5 of 32 units are split (15.6%), giving 29 sub-rows:
  - CLM-004: 7 Conditions-table rows.
  - CLM-009: 16 rows, REQ-001..REQ-016.
  - CLM-019: 2 rows, VER-001 and the Records list.
  - CLM-031: 2 rows, CONFLICT-001 and CONFLICT-002.
  - CLM-032: 2 rows, AC-002 and VER-002.
  - SubItems check: CLM-013 has AC-001 in 1 row; CLM-019 and CLM-032 are satisfied.
- **SEE rows (counted separately):** there are 5.
  - CLM-004.1, CLM-007, CLM-020 and CLM-028 point to SEE:CLM-001.
  - CLM-010 points to SEE:CLM-006.
  - All 5 are STALE_SPECIFICATION.

| ClaimType | Disposition | Rows |
|---|---|---:|
| REQUIREMENT | AUTHORITY_CONFLICT | 14 |
| REQUIREMENT | IMPLEMENTED_DIFFERENTLY | 5 |
| REQUIREMENT | PARTIALLY_IMPLEMENTED | 4 |
| REQUIREMENT | STALE_SPECIFICATION | 5 |
| REQUIREMENT | ALIGNED | 1 |
| ACCEPTANCE | AUTHORITY_CONFLICT | 3 |
| ACCEPTANCE | IMPLEMENTED_DIFFERENTLY | 1 |
| ACCEPTANCE | PARTIALLY_IMPLEMENTED | 1 |
| ACCEPTANCE | STALE_VERIFICATION | 2 |
| STATE_ASSERTION | STALE_SPECIFICATION | 11 |
| STATE_ASSERTION | AUTHORITY_CONFLICT | 1 |
| CONTEXT_CLAIM | NOT_AUDITABLE | 7 |
| CONTEXT_CLAIM | STALE_SPECIFICATION | 3 |
| REGISTER_DEFECT | STALE_SPECIFICATION | 3 |
| REGISTER_DEFECT | REMAINING_STATE_MISMATCH | 1 |

- **Disposition totals** (all rows / excluding SEE rows):

  | Disposition | All rows | Excluding SEE |
  |---|---:|---:|
  | STALE_SPECIFICATION | 22 | 17 |
  | AUTHORITY_CONFLICT | 18 | 18 |
  | NOT_AUDITABLE | 7 | 7 |
  | IMPLEMENTED_DIFFERENTLY | 6 | 6 |
  | PARTIALLY_IMPLEMENTED | 5 | 5 |
  | STALE_VERIFICATION | 2 | 2 |
  | ALIGNED | 1 | 1 |
  | REMAINING_STATE_MISMATCH | 1 | 1 |

- **Errata:** none at pass 1, so there are no errata-applied figures.
- **Reachability of the cited code:**
  - Every gate the SoW describes is in `frontend/src/lib/harness/**` and is `LEGACY_ONLY`:
    - the PreToolUse, PostToolUse and PostToolUseFailure hooks;
    - the path policy;
    - the permission overlay;
    - the mutating MCP wrapper;
    - the managed-child scopes.
  - The live Codex path limits writes only through the user-chosen Codex approval/sandbox pair:
    - `contracts/src/delegated.ts:321-331`;
    - `daemon/src/codex-supervisor.ts:104-110`;
    - `chat-panel.tsx:129-136`.
  - LIVE Chirality-owned writers:
    - the atomic status and dependency writers (`atomic-write.ts`, `transition.ts:210`,
      `deliverable-contracts.ts:538`);
    - the plan-export target check (`electron/plan-export-dialog.ts:19-31`).

## 2. Least-confident rows (with alternative reading)

No row is LOW. These MEDIUM rows are the most arguable:

- **CLM-009.9 (REQ-009) and CLM-004.2: IMPLEMENTED_DIFFERENTLY.**
  - Basis: SPEC 15.1 is titled a first-adapter (Claude SDK) mapping. SPEC.md:15 makes Claude
    descriptions compatibility history.
  - Alternative: AUTHORITY_CONFLICT, because the table's "Chirality overlay" column is
    engine-neutral and unamended.
- **CLM-009.8 (REQ-008): IMPLEMENTED_DIFFERENTLY.**
  - Alternative: ALIGNED, because nothing on the live path relies on `allowedTools`.
- **CLM-009.10 (REQ-010) and CLM-004.4: IMPLEMENTED_DIFFERENTLY.**
  - Basis: no Chirality MCP write tool exists on the Codex path. Status and dependency writes go
    through App routes.
  - Alternative: ALIGNED, because the conditional "before mutation behavior is enabled" is
    vacuously met.
- **CLM-009.5 (REQ-005): AUTHORITY_CONFLICT.**
  - Basis: D-APP-43 3B (GOVERNING) requires exact-edit denial. D-GOV-43 moves writes to the Codex
    supplier without naming D-APP-43.
  - Alternative: DOCUMENTED_UNIMPLEMENTED, judging on the live path alone.
- **CLM-001: STALE_SPECIFICATION.**
  - Basis: MR-8(i). The note says "is MATCH" in the present tense.
  - Alternative: under MR-8(iv) it is a snapshot claim that lives only in REGISTER-1.
- **STATE-2: AUTHORITY_CONFLICT.**
  - Basis: the decomposition PKG-06 scope and SOW-057 still say "daemon conformance", unamended
    under A2.
  - Alternative: STALE_SPECIFICATION of the `_CONTEXT.md` carrier alone.

## 3. Register-defect summary

- **REGISTER-1: `_REFERENCES.md` hashes do not reproduce.**
  - REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD all have Match=NO in the pack's
    REFERENCE_HASHES.csv.
  - REF-001, REF-004 and REF-005, and the workflow files REF-007/009/010, reproduce. This worker
    recomputed them with `shasum -a 256` on the frozen tree.
  - Rows restating it: CLM-001, CLM-004.1, CLM-006, CLM-007, CLM-009.16, CLM-010, CLM-016,
    CLM-020, CLM-028 and CLM-031.2.
- **REGISTER-2: `_DEPENDENCIES.md` contradicts the register.**
  - The Declared Upstream/Downstream sections say "TBD - no accepted dependency edges".
  - The same file's register, and `Dependencies.csv`, carry ACTIVE edges DEP-06-04-007 and -008.
  - The assessment also treats DEL-06-06 as pending, although DEP-06-04-009 is RETIRED.
- **REGISTER-3: DEP-06-04-010 is marked SATISFIED on a MATCH that no longer reproduces.**
- **REGISTER-4: `_STATUS.md` metadata lag.** Last Updated is 2026-07-12, but the last history entry
  is 2026-07-19.
- **Carrier propagation:**
  - The D-APP-127 application map shows every carrier as `NO`.
  - STATE-1: `_CONTEXT.md` still names the Claude Agent SDK as the current path.
  - STATE-2: `_CONTEXT.md` still carries "daemon conformance".

## 4. Direction and cause

- **Main CauseTags:**
  - CODEX_SOLE_ENGINE: 30 rows. The whole write/edit gate is retained in-process harness code.
  - DOC_HYGIENE: 11 rows. These are the hash-drift restatements.
  - PRE_V3_DRIFT: 10 rows. These are TBD paths and choices never written back after ADQ-11
    (2026-06-21), and the scaffold classification of 2026-06-14.
  - NATIVE_DELEGATION: 2 rows, for AC-002 and VER-002.
  - A2_TOPOLOGY: 1 row, STATE-2.
- **Secondary tags:** CAUSE2 is used for CARRIER_PROPAGATION, PRE_V3_DRIFT, CODEX_SOLE_ENGINE and
  DOC_HYGIENE.
- **GOVERNING records used, as `GOV:`:**
  - D-GOV-43, cited through:
    - Root `AGENTS.md`: "Approval and sandbox policy are the user's choice";
    - `docs/SPEC.md:15` and `docs/CONTRACT.md:15`, the Codex-only basis;
    - the amendment markers `CONTRACT.md:7`, `SPEC.md:7` and `PRD.md:11`;
    - `CONTRACT.md:128`, K-UNTYPED-1.
  - D-APP-127, its Retired list.
  - D-APP-43, ruling 3B.
  - D-APP-70, ruling lines 70-73: the attachment boundary is not DEL-06-04's.
- **LatestDecision:**
  - It names D-GOV-43 on every row where D-GOV-43 explains or governs the live-path divergence.
  - It uses `D-GOV-43 (context)` where D-GOV-43 only explains hash drift or engine context.
  - It uses D-APP-43 on exact-edit rows, and D-APP-70 on REQ-014.
- **AUTHORITY_CONFLICT rows (18) and R4-Q1:**
  - D-GOV-43 does not name K-PATH-2, K-PATH-3, K-ROOT-2, K-HOOK-1 or K-PERM-1, SPEC 15.2, or
    D-APP-43 3B. These remain unamended at the frozen basis (CONTRACT.md:52, 90, 99-101). MR-11 is
    therefore not applied.
  - Every AUTHORITY_CONFLICT row except STATE-2 carries R4-Q1. STATE-2 carries plain R4.
  - REQ-010 adds R4-Q3.
  - REQ-015, CLM-011 and VER-001 add R4-Q2.
- **CONTEXT sources:** none was needed to explain a divergence.
  - The v3 plan: its only hook mention is Codex project-trust, which is unrelated.
  - The steers: `root_ruling_record_r3` mentions DEL-06-04 only for an SCA-004 objective trace.
- **Searches behind each `NONE_FOUND`:**
  - `grep DEL-06-04` in `_DECISIONS/_REGISTER.md` gives 0 hits.
  - `grep scaffold_preview` in the register gives 0 hits.
  - `grep DEL-06-04|PKG-06` over `plans/steers` and the v3 plan gives one unrelated hit.
- **PostReleaseBasis:**
  - The only cited file in `TOUCHED_PATHS.csv` is `codex-supervisor.ts`.
  - `git blame -L` at `00115c719` on lines 104-110, 191, 255-262, 700-704 and 719-728 attributes
    them to 95364569a, 1cb09c09d, 0ed1a1a7f, 2f825f180 and 3ad6fac0d (line 191). None is one of
    the four release commits, so every row is `NO`.
  - Line 219 (thread/start `dynamicTools`, da95ec194) is deliberately not relied on.

## 5. Method friction

- **Assessment line drift.**
  - The 2026-06-21 INSP-03 anchors no longer point at the cited behaviour. For example:
    - `tool-path-policy.ts` 162-225 is now 249-259;
    - the hooks test at 370-449 is now the Bash test;
    - the frontend `tool-descriptor.ts` no longer exists.
  - Proposal: AssessmentEvidence could carry a standard "anchors drifted" flag.
- **Module-level REACH.**
  - `packages/contracts/src/harness/tool-descriptor.ts` is LIVE as a module because the daemon
    imports it. Its Write/Edit/MCP descriptors, however, are consumed only by LEGACY_ONLY code.
  - Proposal: allow a symbol-level note, `REACH=LIVE (descriptor consumed LEGACY_ONLY)`.
- **Conditions tables.**
  - Datasheet tables (CLM-003/004) restate REQ rows that come later in the SoW. MR-4 would make the
    datasheet the disposition anchor.
  - I dispositioned them independently, without SEE, because the wording differs.
- **Validator `CODE_PATH` false positive.**
  - The pattern `frontend/...` matches prose search descriptions such as "grep … frontend/src".
  - I rephrased the prose to avoid it.

## 6. Effort

- **Files read:** about 35.
  - Deliverable files: 8.
  - Run and evidence-pack files: 8.
  - App harness and code modules, in ranges: 12.
  - Runtime modules, in ranges: 6.
  - Rulings: D-GOV-43, D-APP-127, D-APP-43 and D-APP-70.
  - Tests, case lists only: 8.
- **Git:** read-only `log -S` and `blame -L` against the frozen tree.
- **Context budget:** adequate, not tight.
