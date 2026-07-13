# W-A2 Portability Inventory

Verdict: `PASS`.

Generated candidate, package, child, check, return, run-record, and manifest
evidence contains zero unclassified checkout-root or machine-temp literals.
Package normalization proofs and their direct rebound manifests reproduce at
the accepted package hashes.

Exactly 81 checkout-root occurrences remain in 48 immutable copied source or
control files: APP-PKG-04 has 16 occurrences in 16 files, APP-PKG-05 has 14
in 14 files, and APP-PKG-06 has 51 in 18 files. They are confined to copied
`_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`, and
`_SEMANTIC_LENSING.md` surfaces and are inventoried in
`detailed/PORTABILITY_HITS.tsv`. Machine temp-root occurrences are zero.

No portability action was performed by reconciliation. Candidate, source,
status, control, map, parity, checklist, render, check verdict, project,
lifecycle, and authority semantics remain unchanged.

