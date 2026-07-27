# Sealed Brief — Read-only G2 Adversarial Test-Design Review

## Parent and construction

- Parent: `HELPS_HUMANS` (Agent 1)
- Child form: one ephemeral generalist Agent 2
- Delegation: prohibited
- Writes: prohibited

## Objective

Inspect the current G2 validator and tests, D-GOV-21 M1/G2/G4, the accepted
Root deliverable register, and the pending Project Setup G2 state. Recommend
the smallest deterministic semantics and adversarial test matrix that:

1. validates a deliverable entry's actual nested declared tree;
2. requires that tree to exist;
3. requires it to be contained within the owning package tree from the
   deliverable register;
4. requires the entry to match the deliverable register;
5. BLOCKs a foreign-tree deliverable; and
6. proves package-entry behavior remains unchanged.

## Read scope

- `tools/validation/validate_root_surface_ownership.py`
- `tools/validation/test_validate_root_surface_ownership.py`
- `docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md`
- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- `/Users/ryan/dev/chirality-root-project-setup-del0206/execution/_harness/surface_ownership.yaml`

## Constraints

- No schema or ownership-policy change.
- No recursive discovery requirement for unregistered nested deliverables.
- No edits, Git actions, delegation, or authority claims.
- Return edge cases, exact assertions, interpretation risks, and a final
  verdict after the manager dispositions the first review.

## Acceptance

The return must address the positive nested-tree case, missing-tree case,
foreign-tree case, register mismatch, package regression, external write
loci such as `runtime/**`, and any symlink/containment issue.
