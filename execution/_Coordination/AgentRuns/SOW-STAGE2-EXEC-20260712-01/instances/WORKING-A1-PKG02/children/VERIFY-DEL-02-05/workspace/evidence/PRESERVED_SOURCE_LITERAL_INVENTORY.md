# Preserved Source Literal Inventory

The accepted copied source/control bytes contain exactly two machine-specific checkout-root strings. They are classified `PRESERVED_SOURCE_LITERAL` and were not normalized:

1. `_REFERENCES.md:13` — accepted REF-007 source path.
2. `_DEPENDENCIES.md:42` — dated dependency-run decomposition path.

These occurrences are bound by the accepted `_REFERENCES.md` and `_DEPENDENCIES.md` hashes in `IDENTITIES.tsv`. The candidate, four marker-bound legacy sources, rendered HTML, deterministic reports, generated verifier metadata, run record, and terminal surfaces contain zero machine-specific checkout-root or temporary-prefix strings.
