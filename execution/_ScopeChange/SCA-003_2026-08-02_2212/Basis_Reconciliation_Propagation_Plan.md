---
amendment_id: SCA-003
doc_kind: scope_change.basis_reconciliation_propagation_plan
created: 2026-08-02
status: AWAITING_OWNER_APPROVAL
---

# SCA-003 antecedent basis reconciliation — propagation plan

## Approved-write boundary proposed for a later application act

The current preparation run writes no live surface. If the exact candidate,
impact assessment, and this plan are accepted, the applying workflows proceed
in this order and stop wherever a required gate is not expressly authorized:

1. Reverify the two live source hashes from
   `Basis_Reconciliation_Validation.json` and require 17/17 checks PASS.
2. Under the separately authorized Root product-basis M2 lane, apply exact
   candidate SHA-256
   `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`
   to `docs/PRD_ROOT.md`.
3. Satisfy the M2 application obligations required by PRD §9.4: exact tranche
   manifest, same-tranche routed coordination notices to the registered loops,
   and explicit public-export/export-manifest regeneration or deferral
   evidence. These surfaces require owner application authority beyond the
   current preparation ruling.
4. Verify the applied PRD SHA-256 equals the REF-001 pin in the decomposition
   candidate.
5. Under SCOPE_CHANGE's approved metadata-write lane, apply exact candidate
   SHA-256
   `69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c`
   to
   `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`.
6. Prove the scope-ledger and deliverable-register hashes remain unchanged,
   rerun the 17 deterministic checks, and dispatch a read-only AUDIT_DECOMP
   against the applied state.
7. Record applied before/after hashes and validation evidence in SCA-003;
   leave `_ScopeChange/_LATEST.md` pointing to accepted SCA-002 because this
   antecedent metadata repair does not close or accept the still-open SCA-003
   TM-ROOT-107 intake.
8. Return the applied state for human post-change confirmation. Only after
   that confirmation may SCA-003 Gate 1 be refreshed and the owner asked to
   confirm the zero-action/no-decomposition-change intake disposition.
9. CHANGE owns commit/push/PR closeout. Merge remains the owner's gate.

## Explicit exclusions

- No scope, topology, mapping, count, objective, status-row, runtime,
  lifecycle, release, reliance, Task Management, or project product-basis
  change.
- No companion-register, `_LATEST.md`, live project-loop, runtime, or Git
  write by this preparation run.
- No reconstruction or edit of immutable SCA-002 evidence, D-GOV-31, Receipt
  63, Receipt 64, or prior candidate history.
- Acceptance of the exact two-file candidate does not itself authorize M2
  foreign-loop notice writes or application; the owner application ruling
  must do so explicitly.

## Owner Gate-4 question

Do you approve this propagation plan, including its PRD-first order, required
M2 application obligations, post-application audit, and stop before SCA-003
Gate-1 confirmation?
