# Fail-Closed Negative Checks

| Case | Validator | Checklist compiler | Output artifact | Verdict |
|---|---:|---:|---|---|
| Partial legacy kit (Procedure.md absent) with isolated authority | exit 1, `INVALID` | exit 1 | absent | PASS |
| Complete dual kit without isolated authority | exit 1, `AMBIGUOUS` | exit 1 | absent | PASS |

The partial case reported `partial legacy production kit; missing: Procedure.md`.
The unauthorized-dual case reported `dual production formats require an isolated conversion workspace and exact migration authority`.
