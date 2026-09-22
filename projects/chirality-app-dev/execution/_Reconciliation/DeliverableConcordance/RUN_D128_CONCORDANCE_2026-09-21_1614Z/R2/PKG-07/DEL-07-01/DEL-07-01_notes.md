# DEL-07-01 — forward-pass notes (R2, PKG-07, wave 3)

Deliverable: `DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection`, read from the
frozen tree at `00115c719`. Ledger: `DEL-07-01_claims.csv` (51 rows, sealed after validation).

## 1. Census

- **Rows:** 51. There are 35 indexed units (SEC-1..3, CLM-001..031, REM-1). CLM-011 is split into
  `.1`–`.11` (REQ-07-01-001..011), and there are 6 run-local `REGISTER-n` rows.
- **Split rate:** 1 of 35 units was split (CLM-011, 11 rows). CLM-015 (AC-001) and CLM-022 (VER-001)
  each list one sub-item and have one row each, with the item named in Notes. The numbered SEC-2
  obligations are not REQ, AC or VER items, so SEC-2 is not split.
- **SEE rows (counted separately):** 12.
  - SEE:REGISTER-1: CLM-001, 008, 012, 016, 023, 027, 029, 031.
  - SEE:CLM-013: CLM-020.
  - SEE:CLM-014: CLM-021.
  - SEE:CLM-011.4: CLM-024.
  - SEE:CLM-018: CLM-026.

| Disposition | All rows | Non-SEE rows |
|---|---:|---:|
| STALE_SPECIFICATION | 22 | 12 |
| PARTIALLY_IMPLEMENTED | 14 | 13 |
| AUTHORITY_CONFLICT | 6 | 5 |
| ALIGNED | 3 | 3 |
| NOT_AUDITABLE | 3 | 3 |
| REMAINING_STATE_MISMATCH | 2 | 2 |
| IMPLEMENTED_DIFFERENTLY | 1 | 1 |

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 19 | 9 PARTIALLY_IMPLEMENTED, 6 AUTHORITY_CONFLICT, 3 ALIGNED, 1 IMPLEMENTED_DIFFERENTLY |
| STATE_ASSERTION | 11 | 11 STALE_SPECIFICATION |
| CONTEXT_CLAIM | 9 | 6 STALE_SPECIFICATION, 3 NOT_AUDITABLE |
| REGISTER_DEFECT | 6 | 4 STALE_SPECIFICATION, 2 REMAINING_STATE_MISMATCH |
| ACCEPTANCE | 5 | 5 PARTIALLY_IMPLEMENTED |
| REMAINING_WORK | 1 | 1 STALE_SPECIFICATION |

- **HumanDecisionNeeded:**
  - `NO`: 28 rows.
  - `R4-Q1`: 20 rows.
  - `D-APP-119; R4-Q1`: 2 rows (SEC-1, SEC-2).
  - `D-APP-119`: 1 row (REM-1).
- **Reach, confirmed per symbol:**
  - **LIVE, working-root validation.** `assertProjectRootAccessible` (session-manager.ts:161-206)
    is reached from the root layout: `app/layout.tsx` → `WorkspaceProvider` →
    `fetch('/api/working-root/validate')` → `validate/route.ts` → `assertProjectRootAccessible`.
    The file, workflow and workflow-drafts routes also call it.
  - **LIVE, Runtime root disjointness.** Electron `main.ts` forks the Runtime service entry
    (`runtime-service-launcher.ts` `utilityProcess.fork`). The service's `project-registry.ts`
    `roots()` rejects a runtime instruction root that overlaps the working root. `roots()` is
    called from `runtime-service.ts` and `runtime-method-service.ts`.
  - **LIVE, Codex sandbox.** `codex-supervisor.ts` `sandboxPolicy` passes the user's
    `PolicySelection` to `thread/start` and `turn/start`. `delegated.ts:318-326` maps `bypass` to
    `danger-full-access`. `approvalDecision` (719-728) relays the user's verdict, with no path
    policy.
  - **LEGACY_ONLY.** `tool-path-policy.ts`, `chirality-hooks.ts`, `permission-overlay.ts`,
    `chirality-tool-bridge.ts` and `mcp/read-tools.ts` are reached only through
    `sdk-options-builder.ts`, which is itself LEGACY_ONLY.
  - **No disagreement with the pack's map for the cited symbols.**
    `frontend/electron/daemon-instruction-root.ts` does not exist at the frozen basis: `39c0bb6ab`
    (D-GOV-43, A2) deleted it.
- **PostReleaseBasis:** `NO` on every row.
  - The only touched cited file is `codex-supervisor.ts`.
  - The cited ranges 104-110 and 719-728 were blamed with `git blame -L`. None of their lines
    blames to the four commits. Line 219, which is touched by `da95ec194`, was deliberately not
    cited.

## 2. Least-confident rows

- **CLM-011.9 (REQ-07-01-009), LOW.** Recorded as `IMPLEMENTED_DIFFERENTLY`: on the live path,
  enforcement is Codex's own sandbox, which is runtime code and not prompt text.
  - **Alternative reading:** `AUTHORITY_CONFLICT`, like CLM-011.4–.8. DIRECTIVE §2.9 is unamended,
    and under `bypass` there is no enforcement at all.
- **CLM-011.4–.8, MEDIUM, `AUTHORITY_CONFLICT`.** These rows turn on D-GOV-43 items 4 and 10 (the
  user chooses the sandbox, including `danger-full-access`, and the App does not veto it).
  - Those items undercut the unamended CONTRACT K-ROOT-2, K-PATH-2, K-PATH-3 and K-HOOK-1 and PRD
    FR-050/051/095/097 without naming them.
  - **Alternative reading:** judge them on the live path per §2.3. That gives
    `IMPLEMENTED_DIFFERENTLY` for .4 and .5 (workspace-write confines writes to cwd, which is
    disjoint from the instruction root) and `DOCUMENTED_UNIMPLEMENTED` for .6, .7 and .8.
- **Mixed product-behaviour units, MEDIUM, `PARTIALLY_IMPLEMENTED` + R4-Q1.** These are SEC-1,
  CLM-004, 009, 015, 019, 025 and 028. Their validation clauses are met by LIVE code, and their
  containment, protection, symlink and fail-closed clauses sit in the same conflict.
  - **Alternative reading:** `AUTHORITY_CONFLICT` for the whole unit.
  - I chose `PARTIALLY_IMPLEMENTED` because the live path does meet part of each unit.
- **CLM-011.3, MEDIUM, `ALIGNED`.**
  - The App validator uses `path.resolve`, a lexical check. A symlinked root that resolves into
    the instruction root therefore passes `/api/working-root/validate`.
  - The Runtime registry and `file-policy.ts` canonicalize with `realpath` and do reject it.
  - **Alternative reading:** `PARTIALLY_IMPLEMENTED`.
- **REM-1, MEDIUM, `STALE_SPECIFICATION`.** The open status is correct (nothing is implemented).
  The defect is the write locus, which names a deleted daemon resolver, and the blocker analysis,
  which D-APP-127 retired. `REMAINING_STATE_MISMATCH` does not fit, because the open/done status
  is not contradicted.
- **REGISTER-2, MEDIUM.** Duplicate RefIDs could be read as a harmless second table. I recorded it
  as a bookkeeping defect.

## 3. Register-defect summary

- **REGISTER-1.** In `_REFERENCES.md`, REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) record
  MATCH, but none reproduces (`HASH-RECOMPUTE@00115c719`).
  - I recomputed DIRECTIVE, TYPES and PLAN myself; their hashes reproduce.
  - The REF-007/009/010 workflow paths are Root-owned, so I did not check them.
  - Eight SoW units restate REF-006 MATCH as current and point here with SEE.
- **REGISTER-2.** In `_REFERENCES.md`, REF-009 and REF-010 are each used for two different
  documents (the workflow resources and the SCA-APP-010 Gate-3/Propagation files).
- **REGISTER-3.** `_DEPENDENCIES.md` says no accepted edges have been extracted and calls the
  2026-09-05 register a "report-only preview". The 12-row post-image is on the carrier, applied
  under D-APP-109.
- **REGISTER-4.** `Dependencies.csv` DEP-07-01-005 says `SATISFIED` and "Resolved to live
  modules", but `tool-path-policy.ts` is LEGACY_ONLY at the frozen basis.
- **REGISTER-5.** DEP-07-01-012 Notes say REF-002 "resolves by its pinned hash" to K-ROOT-1 "at
  L42". The hash does not reproduce, and K-ROOT-1 is at CONTRACT.md:51.
- **REGISTER-6.** No DEL-07-01 carrier records D-APP-127 or D-GOV-43 (application map: all
  `NO`). `_STATUS.md` was last updated 2026-09-05, before the 2026-09-12 application that
  changed REM-1's premise.

## 4. Direction and cause

- **Main CauseTags:**
  - `CODEX_SOLE_ENGINE` (20): containment, protection and hooks are met by Chirality code only on
    the legacy harness, while the product uses the user-chosen Codex sandbox.
  - `DOC_HYGIENE` (15): the hash drift and stale kit text.
  - `CARRIER_PROPAGATION` (6).
  - `PRE_V3_DRIFT` (2): CLM-011.10 and .11. INSP-03 already recorded both gaps on 2026-06-21.
  - `A2_TOPOLOGY` (1): REM-1.
  - `LIFECYCLE_GATE_PENDING` (1): SEC-2.
- **`CAUSE2:` secondaries:**
  - `LIFECYCLE_GATE_PENDING`: SEC-1.
  - `CODEX_SOLE_ENGINE`: SEC-2, CLM-011.10.
  - `CARRIER_PROPAGATION`: CLM-003, 005, 009, REM-1, REGISTER-4.
  - `PRE_V3_DRIFT`: CLM-013, 025.
  - `RUNTIME_EXTRACTION`: CLM-011.11.
- **GOVERNING records used:**
  - D-GOV-43 items 4 and 10, quoted through the CONTEXT candidate.
  - D-APP-127, whose D-APP-100 section says there is no packaged daemon and that the Runtime
    service child resolves the instruction root.
  - D-APP-108 (seating).
  - D-APP-109 (dependency re-extraction).
  - D-APP-38 (the reference model).
  - The CONTRACT.md:7 and SPEC.md:7 amendment headers, which explain the hash drift.
- **CONTEXT used:** `R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md` DONE-05 and Q-07. Q-07
  ("containment conflict") is the same question as R4-Q1 for this deliverable. It is cited as
  CONTEXT only (Ruling B).
- **Searches behind each `NONE_FOUND` DirectionEvidence** (CLM-006, 011.10, 011.11, 014, 018, 021,
  026, 030, REGISTER-2):
  - `_DECISIONS/_REGISTER.md` rows for D-APP-38, 56, 80, 98, 108, 109, 119 and 127.
  - The RUN_BASIS §5 CONTEXT sources: the done-declaration candidate (grep sandbox, containment,
    instruction root, K-PATH, K-HOOK, DEL-07-01) and the `APP_V3_CODEX_HOST_REPLATFORM_20260912`
    file list (sandbox grep only).
  - None of these explains the stale kit text or the tree/scope validator gap.
- **Observations (not dispositions):**
  - `_STATUS.md` REM-1 cites "(additive; D-APP-98)" for the daemon locus. D-APP-98 is the
    Electron-version authority; D-APP-100 was the packaged-daemon instruction root. This looks
    like a mis-citation.
  - Next routes resolve the instruction root from `CHIRALITY_INSTRUCTION_ROOT`, which `main.ts:808`
    sets before start. The Runtime receives it through `buildRuntimeServiceConfig`.
  - The App routes use three different root normalizers:
    - `session-manager.ts` (full check);
    - `workspace/filesystem.ts` (stat and isDirectory only; used by tree and scope);
    - `file-policy.ts` (realpath).
  - CLM-025's "one containment model" principle is therefore not met even at App level.

## 5. Method friction

- **§2.3 live-path rule versus §1 AUTHORITY_CONFLICT.** For security-control requirements whose
  only Chirality implementation is legacy, §2.3 prescribes a live-path verdict, while §1 and the
  brief route "ruling undercuts an unamended clause" to AUTHORITY_CONFLICT.
  - I used AUTHORITY_CONFLICT where the whole claim is the conflicted K-clause (CLM-011.4–.8,
    CLM-024).
  - I used a live-path verdict with R4-Q1 where the unit mixes live-met and conflicted clauses.
  - **Proposed revision:** state that when a D-GOV ruling's user-choice policy directly permits
    what an unamended K-clause forbids, the row is AUTHORITY_CONFLICT, even though the live path
    could otherwise be dispositioned.
- **MR-4 "earliest indexed unit"** does not fit mixed tables well. CLM-004 (Conditions) restates
  REQ-004..007 earlier than CLM-011 but mixes live-met rows with conflicted ones, so I used SEE
  only for single repeated statements.
- **The REF-006 "MATCH under D-APP-38" note appears in 15+ units.** Tie-break rule 3 plus SEE
  handles it, but ClaimType varies by unit shape (STATE_ASSERTION versus CONTEXT_CLAIM). I kept
  whole-unit rows and mentioned the MATCH restatement as "cf. REGISTER-1" in mixed units, so as
  not to create false SEE equivalence.

## 6. Effort

- **Files read** (about 30):
  - the deliverable folder: SoW, _STATUS, _CONTEXT, MEMORY, _REFERENCES, the Dependencies.csv rows
    (by script), part of _DEPENDENCIES, the INSP-03 assessment, and the _SEMANTIC header;
  - about 14 code ranges in App frontend and Runtime packages, and test-name greps;
  - the gate transcripts, register rows, and the D-APP-127 excerpt;
  - the CONTEXT candidate excerpt and the evidence-pack rows.
- **Context budget:** comfortable.
- **Not read:** `_run_records/**` beyond the file list (assessment evidence, not needed for any
  conclusion) and `_SEMANTIC_LENSING.md`.

## Coverage gaps

- **SoW `## Purpose and Objective Traceability`** (OUT-001 and the D-APP-80 SOW-075 note) is not
  an indexed unit. OUT-001 still says "initial symlink-write rejection" and "fail-closed hooks",
  which are now legacy-only. No forward row can own it.
- **SoW `## Output and Evaluation Matrix`** (OUT-001 → CLM-008 / AC-001 / VER-001) is not an
  indexed unit. It maps OUT-001 requirements to CLM-008, which is only the D-APP-56 note, not a
  requirement unit.
- **`_SEMANTIC.md`** is not indexed. Its header embeds machine-specific absolute paths and names
  the retired four-document kit (Datasheet/Specification/Guidance/Procedure). It is a dated
  generated lens and carries no current-state claim that I relied on.
