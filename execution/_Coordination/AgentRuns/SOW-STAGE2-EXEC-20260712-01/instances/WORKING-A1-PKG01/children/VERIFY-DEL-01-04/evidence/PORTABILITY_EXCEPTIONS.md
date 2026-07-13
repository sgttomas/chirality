# VERIFY-DEL-01-04 Portability Inventory

Verdict: `PASS WITH PRESERVED_SOURCE_LITERAL`

The accepted checkout-prefixed `AGENT_SOFTWARE_DECOMP.md` reference is preserved, not verifier-authored meaning. Its exact source, hash, line, marker, and derivative bindings follow without re-emitting the machine prefix in generated metadata.

| Surface | Exact source/hash/line binding | Marker or derivative binding | Occurrences | Disposition |
|---|---|---|---:|---|
| `workspace/Datasheet.md` | `Datasheet.md` SHA-256 `c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd`, line 80 | Source range 70–80 for `CLM-007` | 1 | `PRESERVED_SOURCE_LITERAL` |
| `workspace/_REFERENCES.md` | `_REFERENCES.md` SHA-256 `8690002970f937ec20cde7cb5437f9d051ccdd81e8e49203260292465357c216`, line 13 | Exact accepted control input; not transformed into candidate content | 1 | `PRESERVED_SOURCE_LITERAL` |
| accepted candidate and seeded `workspace/ScopeOfWork.md` | Candidate SHA-256 `13a2a49d1cb74fc83b9c64dc39c25f8ae98107b5b666b5b7352a95b4e626a068`, line 132 | Marker at line 121 binds `Datasheet.md` lines 70–80, source hash above, to `CLM-007`; exact accepted candidate and seeded copy are byte-identical | 1 logical occurrence in each exact copy | `PRESERVED_SOURCE_LITERAL` |
| `evidence/ScopeOfWork.1.html` | Deterministic render of candidate SHA-256 above, line 97 | Rendered `CLM-007` source text; canonical candidate hash bound at lines 7 and 13 | 1 | `PRESERVED_SOURCE_LITERAL` |
| `evidence/ScopeOfWork.2.html` | Deterministic render of candidate SHA-256 above, line 97 | Rendered `CLM-007` source text; canonical candidate hash bound at lines 7 and 13 | 1 | `PRESERVED_SOURCE_LITERAL` |

All generated verifier metadata, run evidence, reports, manifests, returns, and status use repository-relative or `~/` notation and contain zero checkout-prefix, temporary-directory-prefix, or `file://` occurrence. The two render echoes above are the only generated derivative exceptions and are required deterministic preservation outputs.
