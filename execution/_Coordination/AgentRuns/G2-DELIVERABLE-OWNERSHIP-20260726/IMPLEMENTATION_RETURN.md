# HELPS_HUMANS Implementation Return

## Outcome

The owner-approved bounded G2 correction is implemented and validated in the
isolated candidate checkout. No Git action was performed.

## Exact behavior change

For `kind: deliverable` entries only, G2 now:

1. identifies exactly one declared deliverable tree from the literal root of a
   write target whose final component is the exact `DeliverableID`;
2. requires that tree to exist as a directory;
3. loads exactly one accepted adjacent `*deliverable_register*.csv`;
4. requires an exact `DeliverableID` row and exact
   `decomposition_ref == DeliverableID`;
5. obtains the owning package from `ParentPackageID`; and
6. resolves the tree and requires strict containment beneath
   `execution/<ParentPackageID>/`.

Other write targets, including `runtime/**`, remain available to the entry and
are not treated as its declared deliverable tree.

## Preserved behavior

- `kind: package` retains the original `execution/<PackageID>/**` rule.
- Package entries do not gain a directory-existence requirement.
- Static overlap remains informational; concurrency remains G3's concern.
- No recursive nested-deliverable discovery was added.
- No schema, authority, ownership policy, other validator, Project Setup,
  decomposition, product, runtime, or downstream-loop surface changed.

## Tests added

- registered existing nested tree passes;
- missing declared tree blocks;
- foreign-package tree blocks;
- absent exact deliverable-register row blocks;
- mismatched exact decomposition reference blocks; and
- package behavior is explicitly regression-locked.

## Scope and hashes

The instruction-surface candidates and their SHA-256 values are recorded in
`VALIDATION.md`. The other authorized writes are the M2 manifest and this
bounded run-record directory.

## Limitations

Register filename and the two authoritative columns are Root decomposition
conventions. Ambiguous or absent companion registers fail closed. Broader
decomposition-register integrity remains owned by the decomposition audits.
