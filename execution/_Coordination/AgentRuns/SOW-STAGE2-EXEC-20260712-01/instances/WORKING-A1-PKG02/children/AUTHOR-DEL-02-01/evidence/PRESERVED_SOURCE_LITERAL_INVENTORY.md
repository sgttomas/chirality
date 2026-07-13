# Preserved Source-Literal Inventory — DEL-02-01

Classification rule: a machine-specific checkout string is acceptable only when it is already embedded in accepted source/control bytes copied verbatim into the isolated workspace or marker-bound candidate/render content. Generated evidence metadata must use repository-relative paths or `{REPO_ROOT}` tokens.

## Inventory

| Artifact | Occurrence | Classification | Preservation basis |
|---|---:|---|---|
| `workspace/_REFERENCES.md` | 1 | `PRESERVED_SOURCE_LITERAL` | Exact copied control input; workspace and live hashes both equal manifest SHA-256 `0e63d846a82d02fa2240f4192c8aa040f069310b0bf494da9875ac9ebc2ef554`. |
| `workspace/_DEPENDENCIES.md` | 2 | `PRESERVED_SOURCE_LITERAL` | Exact copied control input; workspace and live hashes both equal manifest SHA-256 `f60ddd1687e169bf3c0904f361d09601f4c9e7fa6a0966f939a92e90f8c83109`. |

## Boundary verdict

- Candidate `ScopeOfWork.md`: zero machine-specific absolute checkout strings.
- Rendered derivatives: zero machine-specific absolute checkout strings.
- Generated evidence and terminal metadata: zero machine-specific absolute checkout strings.
- No source, control, candidate, or render bytes were normalized or repaired.

Verdict: `PASS_WITH_PRESERVED_SOURCE_LITERAL_INVENTORY`.
