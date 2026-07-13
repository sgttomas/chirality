# Preserved Source Literal Inventory

Verdict: `PASS`

The frozen live source/control kit contains two checkout-specific literals. They are accepted, hash-bound source bytes and are classified `PRESERVED_SOURCE_LITERAL`; they were not normalized or repaired.

| Artifact | Line | Occurrences | Classification |
|---|---:|---:|---|
| `workspace/_REFERENCES.md` | 13 | 1 | `PRESERVED_SOURCE_LITERAL` in exact control input |
| `workspace/_DEPENDENCIES.md` | 25 | 1 | `PRESERVED_SOURCE_LITERAL` in exact control input |

The marker-bound candidate and its deterministic HTML renders contain zero checkout-specific literals for this deliverable. Genuinely generated JSON, TSV, Markdown, run-record, fixture-result, return, and status metadata contain zero checkout prefixes and zero temporary-directory prefixes. Relative repo paths and the portable `~` repo shorthand are used in generated records.
