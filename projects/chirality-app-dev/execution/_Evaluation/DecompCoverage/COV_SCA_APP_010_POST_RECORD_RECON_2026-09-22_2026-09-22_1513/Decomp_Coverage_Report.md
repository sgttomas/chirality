# Full SOFTWARE Decomposition Coverage Report

Run: `SCA_APP_010_POST_RECORD_RECON_2026-09-22`  
Timestamp: `2026-09-22T15:27:41-06:00`  
Scope: `ALL`  
Result: **WARNINGS**; blockers: **0**.

## Basis and boundary

This is a full structural audit of the current App SOFTWARE decomposition and its companion invariant register. The exact input hashes are in `INPUT_MANIFEST.sha256`. The active source is SCA-APP-010, which remains `OPEN_PENDING_DERIVATIVE_CLOSURE`; this audit does not accept the amendment, close product work, or assert owner acceptance.

The decomposition declares 10 packages, 52 deliverables, 10 objectives and 84 ledger rows. The filesystem has 11 package-shaped folders and 54 deliverable-shaped folders: the extra package and two extra deliverables are disclosed DAG/project-control surfaces, not silently counted as product scope.

## Core checks

| Check | Result | Evidence |
|---|---|---|
| 1 — Forward coverage: packages | **PASS** | 10 declared; 10 matching folders; no missing package folder. |
| 2 — Forward coverage: deliverables | **PASS** | 52 declared; all have matching folders. |
| 3 — Reverse coverage: folders | **WARNING** | One undeclared control package and two control-only deliverable-shaped folders; tracked explicitly as control surfaces. |
| 4 — ID consistency | **PASS** | Declared package/deliverable IDs and parent-package relationships match folder IDs; legacy suffix on DEL-02-02 is accepted and ID remains exact. |
| 5 — Context fidelity | **WARNING** | 51 MATCH, 1 PARTIAL, 0 MISSING among 52 declared deliverables; DEL-09-07 retained historical context still describes retired installer work. |
| 6 — Artifact presence | **WARNING** | Filename-screen coverage 11/194 anticipated artifact descriptions over active declared units; 50 IN_PROGRESS deliverables have incomplete filename matches. Structural presence is not product acceptance. |
| 7 — Objective mapping | **PASS** | 10 objectives; all are supported by at least one existing declared deliverable; no unmapped ObjectiveID; 9 objective summary rows differ from authoritative ledger reverse view (INFO). |
| 8 — Ledger integrity | **PASS** | 84 ledger rows; states {'IN': 78, 'OUT': 5, 'TBD': 1}; no dangling or Scope Ledger ↔ Deliverables reverse-view mismatches. |
| 9 — Derivative package parity | **SKIPPED** | Not variant-owned for SOFTWARE, per method. |
| 9b — Package-shape conformance | **PASS** | Main decomposition labels itself authoritative; §2.2 labels the companion register authoritative and specifies its purpose; no duplicate heavy truth or derived-surface authority confusion found. |
| 10 — Active snapshot and handoff state | **WARNING** | Active SCA-APP-010 pointer resolves uniquely; active root artifacts 11/11; manifest 59/59 entries match. Historical SCA-APP-008 residue remains incomplete: six required root artifacts are absent and two conditional supersession files are also absent (carried from the prior accepted audit). |
| 11 — Lifecycle distribution | **PASS** | Physical deliverable folders lifecycle counts: {'IN_PROGRESS': 53, 'OPEN': 1}; recognized states; OPEN retained DEL-09-07 is not inferred as active product work. |

## Interpretation of warnings

The largest warning class is anticipated-artifact filename coverage: 11 of 194 active descriptions matched the deterministic filename screen, and 50 active `IN_PROGRESS` deliverables have incomplete matches. These are mechanism/evidence-presence gaps for follow-up, not findings that the product code is absent, that the deliverables are rejected, or that implementation failed. One context warning remains: DEL-09-07 is retired by prior authority, yet its retained scaffold `_CONTEXT.md` still describes the old installer. Its `OPEN` lifecycle is preserved as historical data and is not treated as evidence of active work.

The historical SCA-APP-008 snapshot lacks required root artifacts. It is non-current residue and does not invalidate the uniquely pointed active SCA-APP-010 snapshot. SCA-APP-010 remains open pending derivative closure, so closure readiness is **FAIL** despite zero structural blockers.

### What to fix for a cleaner rerun

1. If DEL-09-07 remains in the declared topology as a retired historical row, align its context note to the retirement ruling while preserving its lifecycle history.
2. For each live deliverable, provide or point to named evidence matching its anticipated-artifact claims, or revise the claims through the owning authority when the artifacts are not the right evidence.
3. Keep the control-only DAG closure surfaces explicitly labeled and excluded from product-scope denominators.
4. Complete the separate SCA-APP-010 derivative closure and update its navigation record after all fresh audits are integrated.

## Scope of Work validation

All physical deliverable-shaped folders were checked with the current ScopeOfWork validator: **54/54 passed**. Full per-folder output is preserved in `coverage_summary.json`. This validates document form only; it does not establish feature acceptance.

## Comparison to prior full audit

Compared with `COV_SCA_APP_010_POST_D_APP_109_2026-09-05_0807`, the current topology keeps 10 packages and 52 declared deliverables while the ledger moved from 79 IN / 4 OUT / 1 TBD to 78 IN / 5 OUT / 1 TBD as the retired installer scope was propagated. Context alignment is now 51 MATCH / 1 PARTIAL among declared deliverables; DEL-09-07's historical context is the remaining partial. Artifact denominator is reported as 194 active descriptions after excluding two retired DEL-09-07 descriptions; this is not directly comparable to the earlier 202-row denominator. No product-status improvement is inferred from these structural counts.
