# Decision Log — COV_SCA003_POSTCHANGE_INTERIM

| Ref | Decision | Rationale |
|---|---|---|
| D-1 | Audit `ALL`; bind `Packages`, `Deliverables`, and `Scope Ledger` by heading text. | Sealed brief and AUDIT_DECOMP protocol. |
| D-2 | Treat revision 1.3 working state as the expected source, without treating this derivative audit as acceptance authority. | The brief identifies the accepted working state being assembled into SCA-003; SCOPE_CHANGE owns the immutable amendment snapshot and pointer. |
| D-3 | Check 9 is `SKIPPED`. | Derivative-package parity is not variant-owned for SOFTWARE. |
| D-4 | Apply full companion-register severity in Check 9b. | `ScopeLedger.csv`, `Deliverables.csv`, `ContextBudgetQA.csv`, and `Companion_Inventory.csv` exist; the main document explicitly declares their roles. |
| D-5 | Keep absent anticipated production artifacts at `INFO`. | All lifecycle states are `OPEN` or `INITIALIZED`, earlier than `IN_PROGRESS`. |
| D-6 | Resolve 32 contracts as `SOW_V1` and 32 as absent at `OPEN`; do not assess semantic freshness of excluded ScopeOfWork content. | Exact schema markers establish contract shape. The SCA-003 brief excludes contract amendment, and AUDIT_DECOMP Check 6 validates presence/shape rather than performing contract concordance. |
| D-7 | Check 10 evaluates the currently active SCA-002 snapshot and passes it. | `_ScopeChange/_LATEST.md` still points to exactly one complete, honest SCA-002 snapshot at the specified pre-SCA-003-snapshot boundary. |
| D-8 | Reuse the pre-change matrix and issue rows only after independently revalidating all 64 current contexts, lifecycle files, contract shapes, objective mappings, and ledger references. | SCA-003 changes statement text and three exact context descriptions, but not any matrix metric or informational finding. Mechanical copying preserves deterministic row order. |
