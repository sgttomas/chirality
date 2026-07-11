# Evidence: D-APP-53 Dependency Reconciliation - DEL-10-04 (DRQ-09)

**Date:** 2026-07-10
**Deliverable:** DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture (PKG-10)
**Queue row:** DRQ-09 of `plans/PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md`
**Authority:** `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md` (Option A, no riders)
**Register:** `Dependencies.csv` v3.1 (8 rows)

## Epistemic status (disclaimer)

This is a derivative reconciliation record. It does not replace decomposition truth, source/test
evidence, decision records, or human lifecycle approvals. It authorizes no issuance: no
`CHECKING -> ISSUED` transition occurred or is implied (F-APP-4), `_STATUS.md` was not touched, and
no domain-engine implementation occurred (F-APP-3). All judgments rest on live-filesystem
verification performed 2026-07-10 in the DRQ-09 worktree.

## Per-row reconciliation

4 of 8 rows closed; -004/-006 annotate-only per plan §3.5; -007/-008 left open with reasons.
`LastSeen` bumped to 2026-07-10 on all rows; `ProposedMaturity` set to `SEMANTIC_READY` on closed
rows (their `RequiredMaturity`); maturity untouched on rows left open.

| DependencyID | Prior status | New status | Basis / left-open or annotate reason |
|---|---|---|---|
| DEP-10-04-001 | PENDING | SATISFIED | PKG-10 package row live at decomposition §7 line 270; §8 PKG-10 deliverable table (line 367) still lists DEL-10-04 at line 374. |
| DEP-10-04-002 | PENDING | SATISFIED | SOW-070 live at §5 SSOW line 228 and §9 Scope Ledger line 452, still listing DEL-10-04. |
| DEP-10-04-003 | PENDING | SATISFIED | OBJ-010 live at §6 Objectives line 253; DEL-10-04 deliverable row line 374 lists OBJ-010. |
| DEP-10-04-004 | PENDING | PENDING (annotate-only) | Plan §3.5 owner gate: D-APP-50/51/52 rulings and the D-T0-06 profile adoption exist, but whether they constitute the "accepted PKG-10 amendment or explicit human authorization" is an owner call; D-APP-53 reaffirms F-APP-3. Notes updated; status unchanged. |
| DEP-10-04-005 | PENDING | SATISFIED | Full source corpus accessible with hash MATCH under the D-APP-38 corpus: `_REFERENCES.md` REF-002 CONTRACT (line 8), REF-003 SPEC (line 9), REF-004 TYPES (line 10), REF-005 PLAN (line 11), REF-006 PRD (line 12) — all Status MATCH. Stale REF-006 `SOURCE_HASH_MISMATCH` note corrected (PRD SHA `ac35fba4...` expected == observed). |
| DEP-10-04-006 | PENDING | PENDING (annotate-only) | Plan §3.5: ResponsibleParty assignment is an owner act fenced by the INSP-05 addendum §5. Re-verified live: `_CONTEXT.md` line 14 and `Datasheet.md` line 13 both still record `ResponsibleParty | TBD`. Notes updated; status unchanged. |
| DEP-10-04-007 | PENDING | PENDING (left open) | Partial satisfaction only: concrete test paths now exist (`frontend/src/__tests__/lib/domain-profile.test.ts`, `domain-profile-registry.test.ts`, `domain-proposal-tools.test.ts`, `operation-proposal.test.ts`) but no source assigns a domain-engine adapter manifest location. The candidate `projects/chirality-piping/_harness/adapter.yaml` was inspected and is a practitioner-harness configuration authority (`schema: practitioner-harness-adapter/v1`), not a domain-engine adapter manifest. The row's Statement requires both; closing on half the target would stretch evidence. |
| DEP-10-04-008 | PENDING | PENDING (left open) | Extraction is satisfied (this register). Project graph validation exists as the immutable DepClosure snapshot series (`execution/_Reconciliation/DepClosure/`, latest `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z` per `_LATEST.md`), but that snapshot predates this reconciliation tranche's register mutations; a fresh FULL_GRAPH snapshot over the reconciled registers is queued as plan DRQ-11. Closing now would attest validation of a state that no longer exists. |

Rows left open: DEP-10-04-004, -006 (owner-gated, plan §3.5), -007, -008 (evidence-gated, above).

## Hygiene

1. **Stale `SOURCE_HASH_MISMATCH` warning corrected** in `_DEPENDENCIES.md` Run Notes with a dated
   2026-07-10 note (history retained): `_REFERENCES.md` line 12 now records REF-006 `docs/PRD.md`
   Status MATCH.
2. **`TEST_PATH_TBD` warning updated** with a dated note: now partial — tests exist, adapter
   manifest location does not.
3. **`_DEPENDENCIES.md` synced to CSV state:** Lifecycle Summary now records SATISFIED 4 /
   PENDING 4 (previously PENDING 8) with a dated closure-state update naming the four residuals;
   Run History appended with the 2026-07-10 reconciliation entry.

## Validation

`python3 projects/chirality-app-dev/execution/_Scripts/validate_dependencies.py .../DEL-10-04_Domain_Profile_Validation_and_OpenPipeStress_Fixture/Dependencies.csv`
-> Status: PASS, Rows: 8, Errors: 0, Warnings: 0 (run 2026-07-11T02:19:44Z UTC = 2026-07-10 local).
