# C2R Compatibility Matrix

| Case | Resolver/result | Operational contract | Evidence |
|---|---|---|---|
| Legacy-only, complete | `LEGACY_FOUR_DOC` / valid | Existing readers and `four-documents` compatibility remain; new initialization is refused | focused + full suites |
| SOW-only, valid | `SOW_V1` / valid | Canonical selected production contract; checklist consumes exact registered ACs | focused tests |
| Missing production contract | `INVALID` | fail closed; no output | resolver tests |
| Partial legacy kit | `INVALID` | fail closed with missing-file detail | resolver/semantic/reporting tests |
| Unauthorized dual | `AMBIGUOUS` | fail closed; never accepted baseline | resolver tests |
| Authorized isolated dual | `MIGRATION_DUAL` | authority must equal `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` and the candidate must bind that exact marker; candidate remains derivative | resolver/converter tests |
| Syntactic or self-bound unruled authority | `AMBIGUOUS` / refused | `D-GOV-16@0123456`, other valid-looking SHAs, malformed values, missing values, and mismatched markers fail closed | C2R-R1 regressions |
| Padded ruled authority | `AMBIGUOUS` / refused | leading or trailing whitespace around the exact ruled token fails closed without normalization, conversion output, or checklist output, even when the candidate marker is exact | C2R-R2 resolver/converter and C2R-R3 checklist regressions |
| Invalid SOW | `INVALID` | fail closed with validation findings | resolver tests |
| ISSUED without bindings | refused | no preparation output | converter test |
| ISSUED with bound accepted basis, source commit, four source hashes, and status hash | isolated preparation allowed | accepted basis is bounded and single-line; every binding is embedded exactly; `_STATUS.md` remains byte-identical; no reissue or integration; H1 remains required later | C2R-R1 converter tests |

DOMAIN/KTY, scope-change packets, SCC cases, drawing schemas, fixtures, archives, and other independent grammars remain outside this resolver and unchanged.
