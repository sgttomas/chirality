# Preserved Source Literal Inventory

Verdict: `PASS_WITH_PRESERVED_SOURCE_LITERAL_INVENTORY`.

Machine-specific strings occur only in exact accepted control-input bytes and are classified `PRESERVED_SOURCE_LITERAL`; they are not generated verifier metadata and were not normalized.

| Artifact | Line | Occurrences | Classification | Reason |
|---|---:|---:|---|---|
| `workspace/_REFERENCES.md` | 13 | 1 | `PRESERVED_SOURCE_LITERAL` | Exact accepted source/control byte. |
| `workspace/_DEPENDENCIES.md` | 51 | 2 | `PRESERVED_SOURCE_LITERAL` | Exact accepted source/control byte; `RUN_ROOT` and `DECOMPOSITION_PATH`. |
| `workspace/_DEPENDENCIES.md` | 58 | 1 | `PRESERVED_SOURCE_LITERAL` | Exact accepted source/control byte; historical validator command. |

Total preserved occurrences: `4`.

Generated verifier metadata/evidence occurrences after portable-path normalization: `0`.
