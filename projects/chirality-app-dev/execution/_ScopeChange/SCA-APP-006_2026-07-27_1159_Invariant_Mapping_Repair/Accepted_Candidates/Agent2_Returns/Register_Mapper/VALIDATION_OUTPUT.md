# Validation output

**Result:** `PASS_WITH_EXPLICIT_UNKNOWNS`

| Check | Result |
|---|---|
| Accepted basis exists | PASS — `c487b7dd57a378e2f74417118e78e7f61a161629` |
| CONTRACT identity | PASS — `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` |
| Decomposition identity | PASS — `69b3110c26cb0b435ced4144845282bf6905cde4c0474b21282b9a1806984946` |
| Exact invariant population | PASS — 81/81 |
| Unique exact IDs | PASS — 81/81 |
| Family population | PASS — 48/48 |
| Missing/extra CONTRACT IDs | PASS — none |
| App PKG references | PASS — all resolve |
| App DEL references | PASS — all resolve |
| Closed enum values | PASS |
| Open-issue references | PASS — all resolve |
| Explicit UNKNOWN semantic owners | WARN — 14; preserved by design |

No validation error was returned. The warning is the required explicit
non-invention posture for unresolved composite seams and future domain
ownership.
