---
run-id: TASK_RUN_DEL-08-04_2026-07-25_B8_INIT
timestamp: 2026-07-25
run-status: SUCCESS
control-surface: INLINE
scope-path: /Users/ryan/dev/chirality/.claude/worktrees/project-setup-agent-config-5c0d34/projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms
task-profile: NONE
task-skill: scope-of-work
resolved-skill-path: /Users/ryan/dev/chirality/.claude/worktrees/project-setup-agent-config-5c0d34/skills/scope-of-work
resolved-skill-version: "1"
resolved-task-profile-requirement: NONE
companion-files:
  - BRIEF_SCHEMA.md (found)
  - TOOL_POLICY.md (found)
  - QA_CHECKS.md (found)
tools-invoked:
  - python3 tools/scope_of_work/validate_scope_of_work.py
  - python3 tools/scope_of_work/derive_review_checklist.py
write-authorization: ALLOWED_WRITE_TARGETS
runtime-overrides:
  MODE: INIT
  AUTHORIZATION: D-PEC-63 (PEC Phase 2.2 SOW initialization wave, batch B8)
  DELIVERABLE_PATH: projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms
  DECOMPOSITION_BASIS: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
  PROJECT_SCOPE_REFS: [SOW-041]
  PACKAGE_OBJECTIVE_REFS: [OBJ-001]
  SOURCE_STATE: OPEN
  RENDER_HTML: false
  DECOMP_VARIANT: SOFTWARE
  PHASE: PROJECT_SETUP_PHASE_2_2
  STATUS_POLICY: NO_STATUS_TOUCH
---

# TASK Run Record — DEL-08-04 ScopeOfWork INIT

Decision packet: `D-PEC-63` (PEC Phase 2.2 SOW initialization wave, batch B8 —
the wave's final authoring dispatch). Requested by `PROJECT_SETUP`. No
delegation. Sole authoring instance; no sibling ran concurrently.

## Requested Tasks

- Load `skills/scope-of-work/SKILL.md` plus `BRIEF_SCHEMA.md`, `TOOL_POLICY.md`,
  `QA_CHECKS.md`.
- Read the deliverable-local truth set and the grounding sources named in
  `CustomInstructions`.
- Read the four `INITIALIZED` upstream contracts: `DEL-10-01` `[E-A28]`
  (DECLARED), `DEL-08-03` `[E-N12]`, `DEL-04-01` `[E-P51]`, `DEL-08-01`
  `[E-P52]` (all PROPOSAL).
- Author `ScopeOfWork.md` as a source-grounded `SOW_V1` contract (`MODE=INIT`).
- Validate until PASS; derive the REVIEW checklist twice to stdout without
  persisting it.

## Skill-Contract Application (MODE=INIT)

Per the `D-PEC-63` §3.1 pre-ruling: `TOOL_POLICY.md` steps 2–5 (converter,
candidate refinement, claim map, parity, finalizer) are INERT under `INIT` —
no conversion candidate exists and none was produced; those tools are
structurally CONVERT-only and none was invoked. `render_scope_of_work.py` was
not invoked (`RENDER_HTML=false`). `QA_CHECKS` item 3 was applied in its INIT
restatement: `_STATUS.md` byte-identical, state unchanged at `OPEN`. The
INIT-applicable QA subset 4, 8, 9, 13, 16, 18 was applied and passes.

## Grounding Sources (read; hashed at run time)

| Source | SHA-256 |
|---|---|
| `DEL-08-04/_STATUS.md` | `b44e6d40935d3f5c33d074687247be811805db39132e9f8c88c41c7d42b9d42c` |
| `DEL-08-04/_CONTEXT.md` | `2106134e957c6ee0e6dcddaf8d4d0b8456114e6734db21fa45463b5fffc4ccec` |
| `DEL-08-04/Dependencies.csv` | `d74dd669ef099c959b0b660afd535b1c6bd2988af1311a996932c03e306a223b` |
| `_Decomposition/SOFTWARE_DECOMP.md` | `3e5be4e453ed48d7fbfa48ecc486156124bb197798b47f57aa5284698346dd58` |
| `_Decomposition/ScopeLedger.csv` | `1b2dbf5f8d542f304173c48731c288caf1d3d0338ef772f1eee92fa83d0eb07f` |
| `_Decomposition/Deliverables.csv` | `90baadeb47b69601b68f5ae54060cb13151ffca5845edbe4251715325dcfb217` |
| `projects/pec/docs/PRD.md` | `de0a969cad1519dda61e871ab4bf14be34dce995049c042746f08e1c82d14684` |
| `DEL-10-01/ScopeOfWork.md` (upstream `[E-A28]`) | `f133318531206b6be7c1bbde391914ce967ca602348cb1df819cd0a684c327ff` |
| `DEL-04-01/ScopeOfWork.md` (upstream `[E-P51]`) | `dc667f992c25ed037b195400167319d120a1e5e0118ce777a29f5a64186d0feb` |
| `DEL-08-03/ScopeOfWork.md` (upstream `[E-N12]`) | `a9ed7f560a7655aa4b873ab9f35e8e662d1427044e64febbecf450017f5b884a` |
| `DEL-08-01/ScopeOfWork.md` (upstream `[E-P52]`) | `3c34072d57f5280e37b8ada2c2f505bb9f9e13b2b512be1ec69ff39318b858c3` |

Also read read-only: `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`,
`_Decomposition/ContextBudgetQA.csv`,
`_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`,
`_Coordination/_DECISIONS/D-PEC-62_...md`,
`_ScopeChange/SCA-002_2026-07-25_1042/{Brief.md,Amendment_Preview.md,Decision_Log.md,Amendment_Actions.csv}`,
`PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md`
(accepted perf-bound precedent, read for pattern only — not an upstream edge),
and the scope-of-work tool sources.

## Verification

- Validation result (verbatim):
  `PASS format=SOW_V1 target=projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms`
- Production sha256:
  `48c38fc8dc3685297ffbd992b095d6005b9ba520129b96fdbf2ffba25722ea2d`
  (bound by the checklist's `source.sha256`).
- `derive_review_checklist.py` to stdout, not persisted: `item_count` **16**
  (`AC-001`..`AC-016`). Derived twice; both stdout captures byte-identical,
  stdout sha256
  `2feda7bd88c2cb39014254b047c4086e0f4ca0ecd52e140d11371561fc28c79a`.
- Quotation census: 34 register/exhibit/PRD/decomposition spans and 19
  blockquoted upstream contract records re-checked against their own source
  files by script; all 53 present verbatim in both source and contract. The 19
  upstream records distribute 4 (`DEL-10-01`, CLM-006), 7 (`DEL-04-01`,
  CLM-007), 2 (`DEL-08-03`, CLM-008), 6 (`DEL-08-01`, CLM-009) — matching the
  count the contract's quotation record states.
- Ellipsis census: **zero** `…` characters and zero `...` sequences in the
  document; no quotation is elided. The 24 `..` sequences are the sources' own
  range notation inside quotations plus two of this contract's own prose
  restatements of the `A001`/`A002` target cells, both enumerated in the
  quotation record.

## Contract Shape

`OUT-001`–`OUT-002`, `CLM-001`–`CLM-015`, `TBD-001`–`TBD-004`,
`REQ-001`–`REQ-013`, `AC-001`–`AC-016`, `CON-001`–`CON-006`,
`VER-001`–`VER-014`, `AX-001`–`AX-012` (82 definitions). No `REM-*`. No
duplicate definitions, no unresolved references, 16 matrix rows (one per `AC`,
1:1 with `VER` except `AC-015` and `AC-016`, which use `HUMAN_REVIEW`).
`AC-014` states the implemented range as `VER-001` through `VER-013`,
excluding the mapping method `VER-014` from its own range.

## Applied Changes

- Created `ScopeOfWork.md` and this run record under `_run_records/`.
- No other path written. `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`,
  `_DEPENDENCIES.md`, `Dependencies.csv`, and `_SEMANTIC.md` are untouched and
  byte-identical; lifecycle remains `OPEN`. No register, decomposition, PRD, or
  upstream-deliverable edit. `git status` shows exactly two untracked
  additions and no modification.

## Needs Human Ruling / Carried Forward

- `CON-006` — the bound is stated numerically but the act, gate, and
  consequence attaching to a failing measurement are unowned; `AC-015` routes
  this, together with the unresolved `C-08` standing-node exclusion, to an
  accountable owner.
- `CON-001`, `CON-003`, `CON-005` — corpus denotation, measured-act boundary
  and vantage, and measurement environment / percentile sample design are
  stated by no accepted source; all three are required to be declared and
  recorded in production rather than ruled here.
- `CON-002`, `CON-004` — carried from the three measured surfaces' own open
  records (surfaces that do not exist; return content conditioned by
  `DEL-04-01`'s open records) and are not this deliverable's to resolve.
- `TBD-001`–`TBD-004`: responsible party, budget-record path and form,
  measurement harness, and concrete corpus identity.
- Two `Dependencies.csv` register observations recorded at CLM-004
  (`OI-013` class), not repaired: the three `PROPOSAL` rows' "location TBD"
  `SourceRef` with empty `EvidenceQuote`, and the generator column mapping
  (exhibit `Rationale` → `Statement` on all four `EXECUTION` rows; exhibit
  `BasisCitation` → both `SourceRef` and `EvidenceQuote` on `DEP-08-04-003`,
  the one row whose exhibit `BasisCitation` is populated).

---

## Erratum (appended 2026-07-25 by `TASK_RUN_DEL-08-04_2026-07-25_B8_REV01`; body above unchanged)

- Ellipsis census above states "The 24 `..` sequences"; the count at the hashed production state was **25** (19 range-forms plus 6 backticked notation-mentions). The zero-ellipsis finding itself is unaffected.
