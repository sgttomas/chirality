# ROUTED REQUEST — HELPS_HUMANS tooling/skill-contract consolidation (from PEC PROJECT_SETUP)

**Date:** 2026-07-25 · **Requesting loop:** PEC PROJECT_SETUP (D-PEC-63
ruling, Q2 — owner-selected: "Consolidation packet via HELPS_HUMANS")
**Status:** ROUTED; **INTAKE COMPLETE 2026-07-25** — all 8 items
dispositioned by HELPS_HUMANS (item 2/OI-013 closed on the tooling
side; items 1, 3–8 awaiting owner approval as proposals). Response:
`NOTICE_2026-07-25_helps_humans_oi013_response.md`. Original posture
stands: coordination notice, not authority. HELPS_HUMANS
adopts, amends, or declines under its own instruments; every `skills/**`
and `tools/**` edit follows its own proposal/approval flow. PEC surfaces
are NOT in scope here.
**Priority note:** item 1 is the D-PEC-63 wave's canary-halt dependency
(packet §3.1) — if the canary trips on it, the wave is halted until a
fix lands.

## Defect classes (evidence pointers, all owner-disclosed)

1. **scope-of-work INIT-mode companion-file branches (R1a-F7; wave
   plan §1, packet §3.1).** `skills/scope-of-work/TOOL_POLICY.md` steps
   4–7 are unconditional and conversion-shaped (finalizer/production
   candidate INIT never produces); `SKILL.md` mandates the finalizer
   unconditionally; `BRIEF_SCHEMA.md`'s write-boundary enumerates
   conversion targets only, and declares none of
   `STATUS_POLICY`/`DECOMP_VARIANT`/`PHASE` used as brief metadata by
   the PEC wave. Needed: explicit INIT branches (write boundary =
   `{ScopePath}/ScopeOfWork.md` + run records; tool sequence author →
   validate → checklist; vocabulary for the three metadata keys).
2. **OI-013 — no durable register validator** for decomposition
   companion registers (defect class demonstrated by W-1: a §5 prose
   count drifted from register truth inside an accepted revision).
   *(Evidence extended 2026-07-25, D-PEC-63 wave B4–B8; scale measured
   at closure refutation R4:)* the defect class is **SYSTEMIC to the
   D-PEC-62 seeding generator, not instance-level**. R4's independent
   scan of all 64 deliverable-local `Dependencies.csv` files: **0 of the
   120 EXECUTION rows are well-formed** — 87 carry the exhibit's
   `BasisCitation` text in BOTH `SourceRef` and `EvidenceQuote` (with
   the exhibit's `Rationale` in `Statement`), and 33 have empty
   `EvidenceQuote` with `SourceRef` "location TBD" (mirroring an empty
   exhibit `BasisCitation`); **all 135 ANCHOR rows are clean**.
   Exemplar instances surfaced in-contract during the wave
   (non-exhaustive): empty-EvidenceQuote — DEP-03-01-006,
   DEP-03-02-003, DEP-03-03-003, DEP-03-04-003, DEP-03-06-003/-004,
   DEP-04-01-005, DEP-04-02-003, DEP-04-03-004, DEP-04-05-005,
   DEP-08-03-004, DEP-08-04-004/-005/-006; both-cells mapping defect —
   DEP-08-03-003, DEP-04-05-003/-004, DEP-08-04-003. All carried as
   in-contract observations, none repaired in place. Note also that
   `analyze_dep_closure.py`'s "Evidence coverage 255/255" tests
   `EvidenceFile` presence only, not quote quality — a register
   validator should test both sub-classes and distinguish the two
   metrics.
3. **`tools/query/count_workspace_state.sh` history-substring defect** —
   whole-file `grep -l` matches `_STATUS.md` History lines; unusable
   after any lifecycle transition. Census replacement in use:
   `grep -h '^\*\*Current State:\*\*' … | sort | uniq -c`.
4. **`tools/validation/validate_semantic_pipeline_scope.py`** — no
   `--step init` guard (`STEP_CHOICES` lacks `init`). Note: PEC ruled
   Q1=(b) (semantic pipeline unused for PEC), so this is repo-general
   hygiene, not a PEC dependency.
5. **AUDIT_DECOMP contract inconsistencies** (found during SCA-002):
   IssueLog schema declares `CheckNumber` 1–11 while SPEC runs 12
   checks (the SCA-002 pre-change WARNING row shipped invalid
   `CheckNumber=96`); `coverage_summary.json` gained two additive
   fields beyond the schema template
   (`deliverables_without_objective_mapping`,
   `in_ledger_rows_without_objective_mapping`).
6. **(Carried observation, lower priority) OI-A** — `AGENT_SCOPE_CHANGE.md`
   / `AGENT_AUDIT_DECOMP.md` hard-code `SOFTWARE_DECOMP` section numbers
   that drift from live documents; heading-text binding was the
   workaround used in SCA-002.
7. **(Added 2026-07-25, B2 wave evidence) No upstream-ID citation
   convention for INIT contracts.** Neither `SKILL.md` nor any companion
   says how an INIT-authored contract cites an upstream deliverable's
   local IDs. A bare `DEL-01-06-REQ-004` is scanned by the validator as
   an unresolved *local* `REQ-004`, or silently collides with the
   authoring contract's own `REQ-004` (`tools/scope_of_work/common.py`
   ID extraction). The B2 batch's de facto convention: quote upstream
   text inside §4-provision blockquotes (blank blockquote lines exempt
   from ID extraction, `common.py` ~183–187) plus an explicit
   upstream-context carve-out sentence ("ID-shaped text inside this
   quotation is upstream source context, not a local definition or
   reference") and/or `DEL-NN-NN/REQ-NNN` qualified form. If adopted
   wave-wide it belongs in `SKILL.md`. Evidence: DEL-02-07 CLM-007
   (origin), DEL-01-01 CLM-009 (collision caught at refutation R3-wave
   F6), `WAVE_D-PEC-63/BATCH_B2_FANIN.md`.
8. **(Added 2026-07-25, B3 wave evidence)
   `tools/scope_of_work/derive_review_checklist.py` row-scoped AC→VER
   union linkage.** The deriver sources AC→VER linkage from Output and
   Evaluation Matrix *rows* (`matrix_links`, lines ~60–81): every AC in
   a row receives the **union** of all VER refs in that row. Grouping
   multiple ACs with distinct VERs in one row therefore inflates each
   AC's checklist entry with sibling methods (superset — no AC ever
   loses its own method, so coverage is conservative, but REVIEW
   checklists carry deterministic over-linkage noise). No validator
   check and no SKILL.md/QA_CHECKS.md statement of the row semantics;
   byte-identical re-derivation cannot reveal it. Dispatcher back-scan
   (2026-07-25): 21 multi-AC/multi-VER rows across 10 of the 12
   then-accepted wave contracts carry this over-linkage; dispositioned
   accepted-as-conservative, no revision ordered
   (`WAVE_D-PEC-63/BATCH_B3_FANIN.md`). DEL-02-03's authoring run
   self-caught it and split rows to exact 1:1. Needed: either intra-row
   pairing/a warning in the deriver, or an explicit row-semantics rule
   in the skill contract (one AC per row, or row VER set = exactly the
   union of the row's ACs' own methods). Evidence: DEL-02-03
   `_run_records/TASK_RUN_2026-07-25_2240.md`.

## Canary evidence for item 1 (added 2026-07-25 after the D-PEC-63 canary-3)

Three independent `MODE=INIT` runs (DEL-01-06, DEL-08-02, DEL-00-01) all
COMPLETED with `PASS format=SOW_V1` — the INIT path works — and returned
converging contract-text findings (full detail in each deliverable's
`_run_records/TASK_RUN_2026-07-25_1400.md`):
- `TOOL_POLICY.md` steps 3–5 order INIT runs to refine/map/finalize an
  evidence candidate that cannot exist; all three runs called this the
  clause that would have blocked them absent the brief's pre-ruling. The
  conversion tools are structurally CONVERT-only (require `--source-dir`
  / marker-bearing candidates), which makes the gap safe but unstated.
- `QA_CHECKS.md` item 3 is **actively wrong for INIT**: it requires
  `_STATUS.md` to remain `IN_PROGRESS`, failing a correct INIT run at
  `OPEN`. Suggested restatement: "`_STATUS.md` is byte-identical and its
  state unchanged." Items 1–2, 5–7, 10–12, 14–15, 17 are conversion-only;
  the INIT-applicable subset (4, 8, 9, 13, 16, 18) passed on all three.
- `BRIEF_SCHEMA.md`'s write boundary never authorizes a first-authored
  production `ScopeOfWork.md`; only the dispatching brief's fence did.
  `ExpectedOutputs` is the one field with correct conditional phrasing
  ("for conversion, …") — the pattern the other files need.
- `SKILL.md` Method steps 5–7 and the return contract demand
  finalization/claim-map/parity hashes unproducible under INIT; step 7's
  "before/after hash" of `_STATUS.md` is a read-only invariant under
  `NO_STATUS_TOUCH`, not a pair.

Evidence trail: `projects/pec/execution/_Coordination/PLAN_2026-07-25_pec_phase_2_2_sow_wave.md`
§6 (refutation logs R1, R-2a, R-2b-g1..g5, R-3);
`projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Handoff_State.md` §6.

9. **(Added 2026-07-26, D-PEC-66 act-3 evidence) `skills/scope-of-work`
   row-semantics clause harmonization.** `SKILL.md`'s authoring rule
   ("Group … only when the row's verification set is exactly the union of
   those criteria's own methods") states QA item 20's clause 1 only, which
   post-repair measurement shows is near-vacuous (it passed on all 21
   genuinely over-linked rows; it can only fire when a row carries a VER
   verifying none of its ACs). Item 20's clause 2 (per-AC: no inherited
   non-verifying method) is the operative test and matches the deriver's
   row-scoped semantics. Needed: one-sentence SKILL.md amendment ("…and
   only when those criteria's method sets are identical") and optionally
   the same tightening in item 20 clause 1. Evidence: D-PEC-66 closure
   refutation F1/F2 (`FOLLOWON_D-PEC-66/CLOSURE_2026-07-26.md`); 21/21
   clause-measurement reproduced independently by the closure refuter.
