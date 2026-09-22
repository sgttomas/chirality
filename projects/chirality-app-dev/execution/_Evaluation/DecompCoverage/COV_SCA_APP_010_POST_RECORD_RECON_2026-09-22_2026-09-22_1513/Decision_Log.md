# Decision Log

- Used the `bundled:chirality-root/audit-decomp` workflow for a SOFTWARE / ALL audit.
- Treated Scope Ledger `ObjectiveID(s)` as authoritative for Check 7; the Objective table's `MappedScopeItems` is a secondary reverse summary. Differences are INFO, not a redefinition of scope.
- Treated the one undeclared package and two undeclared deliverable-shaped folders as known control surfaces, not product scope, while preserving them in the reverse-coverage matrix.
- Preserved DEL-09-07 as a stable retired historical row with its existing OPEN lifecycle. The old scaffold context is reported as a current carrier-context warning; no lifecycle transition is inferred.
- Excluded DEL-09-07's two retired artifact descriptions from active artifact coverage, consistent with the retirement text saying no new artifacts are required.
- Artifact filename matches are structural indicators only; they do not determine code existence, implementation acceptance, or release status.
- SOFTWARE Check 9 is SKIPPED under the method. Package-shape Check 9b passes because authority and companion roles are explicit.
- Closure readiness is FAIL while SCA-APP-010 remains open pending derivative closure and concrete product/evidence work remains. This audit does not make acceptance decisions.
