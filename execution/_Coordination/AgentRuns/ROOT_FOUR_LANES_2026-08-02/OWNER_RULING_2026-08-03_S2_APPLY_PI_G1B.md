# Owner ruling — S2 application and Pi G1-B selection

Date: `2026-08-03`
Run ID: `ROOT_FOUR_LANES_2026-08-02`
Authority: `HUMAN OWNER`

## Pi G1 ruling

`SELECT_G1_B_FOR_VALIDATION_ONLY`

Effect: App's presently executable `PiAgentEngineAdapter` family is the exact
implementation family to materialize as the Pi `0.82.0` validation target.
This is not Pi approval, D-APP-72/SCA-APP-002 supersession, App work
authorization, implementation activation, release, reliance, or Task
Management closure.

## SCA-003 candidate acceptance

```text
ACCEPT SCA-003 BASIS RECONCILIATION c3ce8db0: accept
Basis_Reconciliation_Impact_Assessment.md and
Basis_Reconciliation_Propagation_Plan.md; approve exact PRD candidate SHA-256
d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4 and
exact decomposition candidate SHA-256
69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c;
preserve immutable SCA-002 evidence and prior candidate history; no scope,
topology, mapping, count, or substantive requirement change.
```

## SCA-003 application authorization

```text
APPLY SCA-003 BASIS RECONCILIATION c3ce8db0: authorize the Root product-basis
M2 applying workflow to apply exact PRD SHA-256 d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4
first and satisfy its tranche-manifest, routed-notice, and export-disposition
obligations; then authorize SCOPE_CHANGE to apply exact decomposition SHA-256
69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c,
validate the paired REF-001 pin, rerun AUDIT_DECOMP, and return the applied
state for confirmation. Do not change _ScopeChange/_LATEST.md, scope,
topology, mappings, counts, substantive requirements, runtime, lifecycle,
release, reliance, or Task Management state; do not merge.
```

## Ordered effect

1. M2 applies the exact PRD candidate and completes its manifest, notices,
   export disposition, and validation.
2. Only after M2 fan-in is accepted does SCOPE_CHANGE apply the exact
   decomposition candidate and rerun the paired validation/AUDIT_DECOMP.
3. The original SCA-003 zero-action Gate-1 disposition remains a later owner
   confirmation.
4. W2 may instantiate its packet only after the applied S2 evidence exists;
   packet acceptance remains a separate exact owner gate before N0-R2.
