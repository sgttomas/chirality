# WORKING-A1-PKG02 Preserved Source Literal Inventory

Disposition: `PRESERVED_SOURCE_LITERAL — NON-PORTABILITY-DEFECT`.

The exact accepted `_REFERENCES.md` and `_DEPENDENCIES.md` control inputs for
PKG-02 contain machine-specific checkout strings. The authors and verifiers
copied those bytes without modification as required by the frozen manifest.
Across the package instance there are 34 occurrences in 24 exact copied
control files: each author/verifier workspace has its two bound control files,
and the DEL-02-01 and DEL-02-04 negative-fixture substrates include an
additional exact `legacy_state` copy of the same two files.

Every occurrence is source/control provenance, never generated path
authority. The candidates and rendered derivatives contain zero such strings.
Generated run records, returns, statuses, manifests, checks, verdicts,
mapping/parity/checklist evidence, and normalized project-check records contain
zero checkout-root, private-temp, or machine-temp prefix. Exact child-level
inventories bind member/file/count detail. Normalizing any copied control byte
would violate the accepted source hashes and is not authorized.
