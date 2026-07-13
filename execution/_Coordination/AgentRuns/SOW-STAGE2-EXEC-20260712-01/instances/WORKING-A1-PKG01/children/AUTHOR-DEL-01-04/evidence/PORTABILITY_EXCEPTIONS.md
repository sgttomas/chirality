# Portability Inventory

Verdict: `PASS WITH PRESERVED_SOURCE_LITERAL`

Generated run/evidence surfaces contain zero checkout-prefix or temp-prefix literals except the following exact deterministic preservation outputs, which must not be rewritten:

| Surface | Source binding | Marker binding | Occurrences | Disposition |
|---|---|---|---:|---|
| `workspace/ScopeOfWork.md` | `Datasheet.md` line 80, SHA-256 `c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd` | `CLM-007`, source lines 70–80 | 1 | `PRESERVED_SOURCE_LITERAL` |
| `evidence/ScopeOfWork.1.html` | deterministic render of candidate SHA-256 `13a2a49d1cb74fc83b9c64dc39c25f8ae98107b5b666b5b7352a95b4e626a068` | rendered `CLM-007` source text | 1 | `PRESERVED_SOURCE_LITERAL` |
| `evidence/ScopeOfWork.2.html` | deterministic render of candidate SHA-256 `13a2a49d1cb74fc83b9c64dc39c25f8ae98107b5b666b5b7352a95b4e626a068` | rendered `CLM-007` source text | 1 | `PRESERVED_SOURCE_LITERAL` |

The copied `workspace/Datasheet.md` and `workspace/_REFERENCES.md` are exact accepted source/control inputs and retain their original literal by rule. All authored references use repository-relative or `~/` notation. No local temporary-directory prefix is present.
