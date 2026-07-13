# Preserved Source Literal Inventory

Verdict: `PASS`

Selected high-risk literal counts are byte-preserved between the four source documents and candidate source blocks:

| Literal | Source | Candidate |
|---|---:|---:|
| `settingSources: []` | 8 | 8 |
| `['project']` | 6 | 6 |
| `` `allowedTools` `` | 10 | 10 |
| `` `opts.tools` `` | 3 | 3 |
| `` `maxTurns` `` | 3 | 3 |
| `` `CHIRALITY_GLOBAL_MODEL` `` | 1 | 1 |
| `` `mcp__chirality__*` `` | 1 | 1 |
| `` `SdkOptionsBuilder` `` | 3 | 3 |
| `HASH_MISMATCH` | 4 | 4 |
| `CONFLICT-DEL-04-02-001` | 1 | 1 |

The sole `/Users/ryan/` production-content literal is the pre-existing `REF-007` row in `_REFERENCES.md`, preserved into neither generated metadata nor verifier conclusions. TASK-required absolute paths occur only in the run record. All terminal manifests and evidence references are repository-relative.
