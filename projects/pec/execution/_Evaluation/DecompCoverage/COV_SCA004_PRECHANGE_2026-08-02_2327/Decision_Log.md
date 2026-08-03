# Decision Log — COV_SCA004_PRECHANGE_2026-08-02

| Ref | Decision | Rationale |
|---|---|---|
| D-1 | Audit `ALL`; bind `Packages`, `Deliverables`, and `Scope Ledger` by heading text. | Sealed brief and AUDIT_DECOMP protocol. |
| D-2 | Bind the authoritative pre-change basis to revision 1.3 `current_basis`, D-PEC-78 O-A, and the confirmed SCA-004 Gate 1 intake. | These are the exact accepted inputs Gate 2 is assessing. |
| D-3 | Check 9 is `SKIPPED`. | Derivative-package parity is not variant-owned for SOFTWARE. |
| D-4 | Apply full companion-register severity in Check 9b. | Companion registers exist; `Companion_Inventory.csv` and the main-document inventory make roles discoverable. |
| D-5 | Resolve 32 contracts as `SOW_V1` and 32 as absent at `OPEN`. | Exact `schema: chirality-deliverable-sow/v1` markers establish contract shape; no legacy/dual form exists. |
| D-6 | Treat anticipated-artifact matching as deliverable-folder-local. | Check 6 directs the audit to scan the deliverable folder; accepted bytes elsewhere are not silently relocated or reclassified. |
| D-7 | Escalate the absent DEL-08-02 anticipated schema/test set to `WARNING`. | Its current lifecycle is `CHECKING`, which is later than `IN_PROGRESS`; the protocol requires escalation. |
| D-8 | Check 10 passes the accepted SCA-003 pointer state and cites SCA-004 Gate 1 separately. | SCA-004 is confirmed intake for this pre-change audit, not yet the active accepted `_ScopeChange/_LATEST.md` snapshot. |
| D-9 | Do not update `_Evaluation/DecompCoverage/_LATEST.md`. | The sealed brief expressly narrows the normal protocol to one immutable snapshot with no pointer write. |
