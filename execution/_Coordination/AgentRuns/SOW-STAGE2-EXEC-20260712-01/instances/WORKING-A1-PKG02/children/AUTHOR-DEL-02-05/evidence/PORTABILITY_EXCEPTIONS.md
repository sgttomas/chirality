# Preserved Source-Literal Inventory

Verdict: `PASS WITH PRESERVED_SOURCE_LITERAL`

Generated run/evidence metadata and candidate/render outputs contain zero checkout-prefix, temporary-prefix, home-prefix, or worktree-prefix literals. The following two machine-specific occurrences remain only in exact accepted control-source copies and must not be rewritten:

| Surface | Accepted source binding | Occurrences | Disposition |
|---|---|---:|---|
| `workspace/_REFERENCES.md` line 13 | SHA-256 `f196b70ae5f2092f91052f9776be8eb8f4aa3c58a9895e12708f9e66418c74a3` | 1 | `PRESERVED_SOURCE_LITERAL` |
| `workspace/_DEPENDENCIES.md` line 42 | SHA-256 `85b9322cf8f690c6cfd37c37571b02a2a6e43d4722e01d6047d81c180f122922` | 1 | `PRESERVED_SOURCE_LITERAL` |

The candidate and both deterministic render derivatives contain zero machine-specific path literals. All authored references use repository-relative or `~/` notation.
