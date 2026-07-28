# Decision Log — COV_SCA003_POSTCHANGE_FINAL

| Ref | Decision | Rationale |
|---|---|---|
| D-1 | Audit `ALL`; bind `Packages`, `Deliverables`, and `Scope Ledger` by heading text. | Sealed brief and AUDIT_DECOMP protocol. |
| D-2 | Re-read the current decomposition after the manager's telemetry-correction notice and bind all evidence to SHA-256 `3f65ea0e...`. | Prevents the final audit from citing the superseded intermediate postimage. |
| D-3 | Check 9 is `SKIPPED`. | Derivative-package parity is not variant-owned for SOFTWARE. |
| D-4 | Apply full companion-register severity in Check 9b. | Companion registers exist; `Companion_Inventory.csv` and the main-document inventory make their roles discoverable. |
| D-5 | Keep absent anticipated production artifacts at `INFO`. | All lifecycle states are `OPEN` or `INITIALIZED`, earlier than `IN_PROGRESS`. |
| D-6 | Resolve 32 contracts as `SOW_V1` and 32 as absent at `OPEN`; do not assess semantic freshness of excluded ScopeOfWork content. | Exact schema markers establish contract shape. Contract concordance is outside AUDIT_DECOMP and expressly excluded from SCA-003. |
| D-7 | Check 10 passes SCA-003. | `_ScopeChange/_LATEST.md` names exactly one active snapshot; all 11 required SCOPE_CHANGE artifacts exist; the handoff limits closure to scope change and explicitly freezes reliance and downstream regeneration. |
| D-8 | Treat the clean interim summary in `Post_Change_Coverage.json` as sufficient assembly evidence for the final two-pass check. | The final run independently re-executes every audit check. On completion this snapshot and the audit pointer are the final evidence for the manager to copy into the SCA snapshot. |
| D-9 | Reuse the interim matrix and issue rows only after revalidating their current inputs. | Topology, contexts, lifecycle, contract shape, objective support, and ledger references are unchanged; deterministic row order is preserved. |
