# Preserved Source-Literal Inventory

Verdict: `PASS_WITH_PRESERVED_SOURCE_LITERAL`

The accepted control inputs contain two distinct machine-rooted strings in three source locations. They are copied byte-for-byte and classified `PRESERVED_SOURCE_LITERAL`; they are not generated verifier metadata and were not normalized.

| Artifact | Source locations | Occurrences | Classification |
|---|---:|---:|---|
| `_DEPENDENCIES.md` | lines 48 and 65 | 2 in the workspace source copy; 2 in `legacy_state/` | `PRESERVED_SOURCE_LITERAL` |
| `_REFERENCES.md` | line 13 | 1 in the workspace source copy; 1 in `legacy_state/` | `PRESERVED_SOURCE_LITERAL` |

Candidate `ScopeOfWork.md`: zero machine-specific literals.

Both rendered HTML files: zero machine-specific literals.

Generated verifier metadata and evidence outside this inventory: zero machine-specific literals after portable `{REPO_ROOT}` normalization in the TASK run record.
