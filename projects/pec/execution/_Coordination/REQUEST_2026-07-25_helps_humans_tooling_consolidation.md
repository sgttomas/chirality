# ROUTED REQUEST — HELPS_HUMANS tooling/skill-contract consolidation (from PEC PROJECT_SETUP)

**Date:** 2026-07-25 · **Requesting loop:** PEC PROJECT_SETUP (D-PEC-63
ruling, Q2 — owner-selected: "Consolidation packet via HELPS_HUMANS")
**Status:** ROUTED — coordination notice, not authority. HELPS_HUMANS
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
