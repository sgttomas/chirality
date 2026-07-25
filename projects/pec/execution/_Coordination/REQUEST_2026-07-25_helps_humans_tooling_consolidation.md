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

Evidence trail: `projects/pec/execution/_Coordination/PLAN_2026-07-25_pec_phase_2_2_sow_wave.md`
§6 (refutation logs R1, R-2a, R-2b-g1..g5, R-3);
`projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Handoff_State.md` §6.
