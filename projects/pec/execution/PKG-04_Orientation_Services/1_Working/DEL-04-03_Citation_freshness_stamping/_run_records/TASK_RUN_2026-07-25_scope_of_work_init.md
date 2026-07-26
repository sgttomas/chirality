# TASK RUN — scope-of-work (MODE=INIT) — DEL-04-03

| Field | Value |
|---|---|
| RunKind | TASK + `scope-of-work`, MODE=INIT |
| Authorization | D-PEC-63 (PEC Phase 2.2 SOW initialization wave, batch B6) |
| RequestedBy | PROJECT_SETUP (Agent 1) |
| Executor | Agent 2 (sealed TASK instance); no delegation performed |
| Date | 2026-07-25 |
| ScopePath | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping` |
| ResolvedSkillVersion | `skills/scope-of-work/SKILL.md`, `chirality-skill-version: "1"`, `chirality-task-profile: NONE` |
| CompanionFiles read | `BRIEF_SCHEMA.md`, `TOOL_POLICY.md`, `QA_CHECKS.md` |
| DECOMPOSITION_BASIS | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b` (revision 1.2, `current_basis`) |
| SOURCE_STATE | `OPEN` (unchanged by this run) |

## Outputs

| Artifact | sha256 |
|---|---|
| `ScopeOfWork.md` (production) | `fa19a9ee94cdb1cc7f30bc828f85bfe43151a57ae1e7f8f750a84905777ad531` |
| `_STATUS.md` (read-only, before == after) | `5f691be521373ae9d5eeb3e29cf61929bce36d05ad97f32d9a4cfba383448006` |

## Tool invocations

1. `python3 tools/scope_of_work/validate_scope_of_work.py "<ScopePath>"` —
   final line verbatim:
   `PASS format=SOW_V1 target=projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping`
2. `python3 tools/scope_of_work/derive_review_checklist.py "<ScopePath>"` — run
   twice to stdout, outputs byte-identical (`cmp` clean). `item_count` 15;
   `source.sha256` binds the production contract hash above. JSON not persisted.

`render_scope_of_work.py` not invoked (`RENDER_HTML: false`). Conversion tools
(`convert_four_documents_to_scope_of_work.py`, `finalize_scope_of_work.py`,
`map_scope_of_work_claims.py`, `report_scope_of_work_parity.py`) not invoked:
structurally CONVERT-only and INERT under MODE=INIT per the D-PEC-63 §3.1
pre-ruling; no evidence candidate exists or was produced.

## Contract shape

OUT 2 · CLM 17 · TBD 4 · REQ 15 · AC 15 · CON 4 · VER 14 · AX 11. Matrix rows
15 (14 × OUT-001, 1 × OUT-002). AC↔VER is 1:1 for AC-001..AC-014; AC-015 is
`HUMAN_REVIEW`. AC-014 states the range VER-001..VER-013, excluding its own
summary method VER-014.

## Write authorization and boundary

Writes confined to the two `AllowedWriteTargets`: `ScopeOfWork.md` and
`_run_records/`. `git status --porcelain` over the ScopePath after authoring
showed exactly one entry (`?? .../ScopeOfWork.md`). `_STATUS.md`, `_CONTEXT.md`,
`_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and `_SEMANTIC.md`
were read only and are byte-identical. Lifecycle untouched
(`STATUS_POLICY: NO_STATUS_TOUCH`); `OPEN` → `INITIALIZED` advancement remains a
separate deterministic act under D-PEC-63 §3.2.

## Grounding sources read (read-only)

`ScopeLedger.csv` (SOW-006, SOW-007 and adjacent rows) · `Deliverables.csv`
(DEL-04-03 and named neighbours) · `docs/PRD.md` (§6 PEC-K-02/-04/-05/-06/-08/-10,
§7.1–7.3, §9.1 PEC-ORI-003/004, §9.2 PEC-RCN-002/003, §9.4 PEC-PRS-005/007) ·
`SOFTWARE_DECOMP.md` (frontmatter, §2.1, §3, §4, §5 PKG-04, §8, §9, §10, §11
DL-13/DL-14) · deliverable-local `_CONTEXT.md`, `_REFERENCES.md`,
`_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md` ·
`_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` (§4.1 edges, §4.2
constraints, §7) · `_Coordination/_DECISIONS/D-PEC-62_...md` §1 ·
`_ScopeChange/SCA-002_2026-07-25_1042/Brief.md` (A001, A002) and
`Amendment_Preview.md` (A003b lines 320/321; Q2 INDIRECT-8 table) ·
upstream `DEL-04-01_Loop_orientation_return/ScopeOfWork.md` (full).

## Notes

- One incidental read outside the declared grounding set: two grep-matched
  lines of `DEL-03-02_Incremental_reconcile_on_Git_delta/ScopeOfWork.md`, to
  check the brief's pointer to that contract's CON-001. It is **not** cited as
  a basis anywhere in the contract; CON-002 rests only on the upstream
  DEL-04-01 quotation and on register-level `SOW-018` / `PEC-RCN-003` text.
