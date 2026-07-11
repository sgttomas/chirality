# Evidence - D-APP-53 Dependency Reconciliation (DRQ-04, DEL-04-01)

Date: 2026-07-10
Queue row: DRQ-04 of `plans/PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md`
Authority: D-APP-53 ruling, Option A (`execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`)

## Epistemic Status

This is derivative evidence produced by a governed dependency-register reconciliation pass.
It does not replace decomposition truth, source/test evidence, decision records, or human
lifecycle approvals. It authorizes no issuance: no `CHECKING -> ISSUED` transition (F-APP-4),
no release/distribution act (F-APP-2), no provider expansion (F-APP-1 as amended by
D-APP-44), no domain-engine implementation (F-APP-3). `_STATUS.md` is untouched and remains
`CHECKING`. Satisfaction-state changes below are register bookkeeping against cited live
evidence, per the plan's section 3 rules.

## Per-Row Reconciliation

| DependencyID | Prior status | New status | Basis / left-open reason |
|---|---|---|---|
| DEP-04-01-001 | ACTIVE / SATISFIED | unchanged | Not in scope; already satisfied (PKG-04 package anchor). |
| DEP-04-01-002 | ACTIVE / SATISFIED | unchanged | Not in scope; already satisfied (SOW-018 anchor). |
| DEP-04-01-003 | ACTIVE / SATISFIED | unchanged | Not in scope; already satisfied (SOW-044 anchor). |
| DEP-04-01-004 | ACTIVE / SATISFIED | unchanged | Not in scope; already satisfied (SOW-046 anchor). |
| DEP-04-01-005 | ACTIVE / SATISFIED | unchanged | Not in scope; already satisfied (OBJ-004 anchor). |
| DEP-04-01-006 | ACTIVE / TBD | ACTIVE / SATISFIED | REF-006 `docs/PRD.md` source-state constraint resolved: `_REFERENCES.md` records REF-006 `MATCH` (Expected = Actual = `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`); live `shasum -a 256 docs/PRD.md` re-verified 2026-07-10 and matches; `Evidence_CODEV-001_SDK_Probe_Record.md` (2026-07-10 refresh) records the D-APP-38 authority corpus resolving the earlier caveat. Stale CSV note claiming `HASH_MISMATCH` corrected in the same edit. ProposedMaturity set to `SEMANTIC_READY`. |
| DEP-04-01-007 | ACTIVE / TBD | ACTIVE / TBD (annotated) | Owner-gated residual per plan section 3.5 — annotate-only. Landed: `frontend/package.json` pins `@anthropic-ai/claude-agent-sdk@0.3.150` and `@anthropic-ai/sdk@0.93.0`; deterministic test harness present (`sdk-options-builder` / `sdk-message-mapper` tests); packaging posture in PKG-09 `Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`. Still open: live Claude Code subprocess version is `BLOCKED_TBD` (`Evidence_CODEV-001_SDK_Probe_Record.md` Version Evidence); the live-LLM demonstration is owner-gated per D-APP-52. Notes and LastSeen updated; SatisfactionStatus unchanged. |
| DEP-04-01-008 | RETIRED / NOT_APPLICABLE | unchanged | Retired 2026-05-24 by RUL-SCC-001-TRANCHE-001 (CSV already correct); this file's `_DEPENDENCIES.md` summary tables were stale and are synced under Hygiene below. |
| DEP-04-01-009 | ACTIVE / TBD | ACTIVE / SATISFIED | Mapped P0 reliance-boundary expectations verified present: DEL-01-02 `Datasheet.md` Boundary Taxonomy records 13 RB-* rows (RB-ENGINE through RB-FALLBACK) with product-critical semantics, primary enforcement surfaces, and source support (`execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/Datasheet.md`). ProposedMaturity set to `SEMANTIC_READY`. (DEL-01-02 was read-only for this slice; its own register reconciliation runs under DRQ-01.) |
| DEP-04-01-010 | ACTIVE / TBD | ACTIVE / TBD (annotated) | Left open (conservative, plan section 3.1): no handover artifact records implementation requirements sent to DEL-04-02 per `Procedure.md#Steps` step 13; consumer mirror row DEP-04-02-006 in DEL-04-02 `Dependencies.csv` remains TBD, so consumption is not verifiable. |
| DEP-04-01-011 | ACTIVE / TBD | ACTIVE / TBD (annotated) | Left open: no handover artifact; consumer mirror row DEP-04-03-007 remains TBD and DEL-04-03 `_DEPENDENCIES.md` still carries the warning that DEL-04-01 probe evidence is TBD. |
| DEP-04-01-012 | ACTIVE / TBD | ACTIVE / TBD (annotated) | Left open: no handover artifact, and DEL-04-04 contains no reference to DEL-04-01 in any register or document — no consumption trace exists at all. |
| DEP-04-01-013 | ACTIVE / TBD | ACTIVE / TBD (annotated) | Left open: no handover artifact; consumer mirror row DEP-04-05-007 in DEL-04-05 `Dependencies.csv` remains TBD, so consumption is not verifiable. |

Result: 13 rows — 7 SATISFIED (001-006, 009), 5 TBD left open (007, 010-013), 1 RETIRED /
NOT_APPLICABLE (008). Rows 007 and 010-013 received dated annotations and `LastSeen`
bumps only; their `SatisfactionStatus` and maturity columns are unchanged.

## Hygiene

1. **DEP-04-01-006 stale note** — the CSV `Notes` field claimed "_REFERENCES.md records
   REF-006 HASH_MISMATCH", contradicting the live `_REFERENCES.md` (REF-006 `MATCH`).
   Corrected with a dated `FACT (corrected 2026-07-10)` note as part of closing the row.
2. **`_DEPENDENCIES.md` summary sync** — the summary table listed DEP-04-01-008 as
   `ACTIVE | SATISFIED` and the metric/lifecycle tables read ACTIVE 13 / RETIRED 0,
   SATISFIED 6 / TBD 7, none of which matched the CSV (DEP-04-01-008 has been
   `RETIRED / NOT_APPLICABLE` since 2026-05-24). Synced to ACTIVE 12 / RETIRED 1;
   SATISFIED 7 / TBD 5 / NOT_APPLICABLE 1; per-row table updated for rows 006, 008, 009.
3. **Stale run-note warnings** — `[WARNING] SOURCE_STATE` (REF-006 HASH_MISMATCH) and the
   partially stale `[WARNING] TBD_PROBE_ENVIRONMENT` were corrected with dated 2026-07-10
   D-APP-53 reconciliation notes appended to Run Notes; the original warning text is
   retained as history (plan section 3.7: corrected with a dated note, not silently
   rewritten).

## Validation

`python3 execution/_Scripts/validate_dependencies.py <this deliverable>/Dependencies.csv`
run after reconciliation on 2026-07-10 (UTC 2026-07-11T02:15:29Z): **PASS** — Rows: 13,
Errors: 0, Warnings: 0 (plan section 5 gate satisfied for this register).
