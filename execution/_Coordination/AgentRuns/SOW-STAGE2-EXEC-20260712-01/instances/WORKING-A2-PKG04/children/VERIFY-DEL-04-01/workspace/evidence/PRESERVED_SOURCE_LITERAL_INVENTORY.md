# Preserved Source-Literal Inventory

Classification: `PRESERVED_SOURCE_LITERAL`

Two machine-specific literals occur in accepted control inputs and were copied byte-for-byte without normalization:

| Input | Line | Classification | Propagation |
|---|---:|---|---|
| `_DEPENDENCIES.md` | 54 | `PRESERVED_SOURCE_LITERAL` | accepted control copy only; absent from candidate and render |
| `_REFERENCES.md` | 13 | `PRESERVED_SOURCE_LITERAL` | accepted control copy only; absent from candidate and render |

No machine-specific literal occurs in the four production sources, marker-bound candidate text, or either HTML render. A scan of genuinely generated metadata/evidence, excluding this explicit inventory and the two renders, found zero machine-specific literal hits. Repository-relative run paths in deterministic reports are portable and are not machine-specific literals.
