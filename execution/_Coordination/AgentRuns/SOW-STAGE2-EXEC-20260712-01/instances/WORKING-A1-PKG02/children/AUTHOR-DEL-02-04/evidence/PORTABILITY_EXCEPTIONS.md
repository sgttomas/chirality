# Preserved Source-Literal Inventory

Verdict: `PASS WITH PRESERVED_SOURCE_LITERAL`

Generated run/evidence metadata contains zero checkout-prefix, temporary-prefix, or worktree-prefix literals. The following three machine-specific occurrences remain only in exact accepted control-source copies and must not be rewritten:

| Surface | Accepted source binding | Occurrences | Disposition |
|---|---|---:|---|
| `workspace/_REFERENCES.md` line 13 | SHA-256 `4e73b30b8ce1029e10cd2f48ef40c97ed552c071e7c6f6e7b0f119719cd7846d` | 1 | `PRESERVED_SOURCE_LITERAL` |
| `workspace/_DEPENDENCIES.md` line 53 | SHA-256 `a81ae0ee95103979cfd923f6666e74680d3d69c66a43a86418d9a55424251b1d` | 2 | `PRESERVED_SOURCE_LITERAL` |

The candidate and both deterministic render derivatives contain zero machine-specific path literals. All authored references use repository-relative or `~/` notation.
