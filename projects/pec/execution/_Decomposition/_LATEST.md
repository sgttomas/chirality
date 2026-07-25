# Latest — revision pointer and handoff state

Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.1**
(**`current_basis`** — accepted 2026-07-24 as the SCA-001 successor under
`D-PEC-61`).

## Handoff state

- **Basis:** D-PEC-60 SOFTWARE_DECOMP revision 1.0 over PRD v2.0, amended by
  SCA-001 to reconcile PRD v2.1's directed-bootstrap clarification adopted
  by D-PEC-61. SCOPE_CHANGE Gates 1–5 were separately owner-confirmed.
- **Package:** working surface + `ScopeLedger.csv` (94 rows) +
  `Deliverables.csv` (64) + `ContextBudgetQA.csv` +
  `Companion_Inventory.csv` (unchanged).
- **Closure verdict: `CLOSED_FOR_SCOPE_CHANGE_ONLY`.** Revision 1.1 is the
  accepted decomposition basis. No package, deliverable, objective, scope
  item, product function, stable ID, or dependency edge was added or removed.
- **Verification:** deterministic pre/post register-integrity comparison
  confirms 94 scope items (71 IN / 14 OUT / 9 TBD), 11 packages,
  64 deliverables, 6 objectives, zero dangling mappings,
  `SOW-064 → PKG-10 → DEL-10-10 → OBJ-006`, and Context Envelope counts
  S 28 / M 34 / L 2 / XL 0.
- **AuditState: `WARNINGS`.** Pre/post `AUDIT_DECOMP` cannot measure
  filesystem coverage before Project Setup because no package/deliverable
  folders exist; its contract-required `FAILED_INPUTS` result is preserved.
  OI-013 remains the durable register-validator follow-on.
- **Blockers / open issues:** none blocks Project Setup. OI-001..009 remain
  the §16 owner decisions; OI-012 remains the core-isolation ADR; OI-013
  remains the validator follow-on.
- **ReadyForNextPhase: `REGEN_ONLY`.** `PROJECT_SETUP` is the next owner.
  `FULL_GRAPH` is already owner-selected; Project Setup must materialize the
  complete accepted dependency graph and blocker computation from revision
  1.1. Its Phase 1.3 dependency-maturity threshold and register-storage
  choices remain at their normal owner gate.
- **Fallback and authority:** the full DAG is PEC's initial file-native
  self-ingestion corpus; later nodes may consume only predecessor
  capabilities already produced and accepted. Observed friction may generate
  evidence-linked candidates or amendment requests but changes no accepted
  scope and grants no authority. File-native fallback remains operable.
