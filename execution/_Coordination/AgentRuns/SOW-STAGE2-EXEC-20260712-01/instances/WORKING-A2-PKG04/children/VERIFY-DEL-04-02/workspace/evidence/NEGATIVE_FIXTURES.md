# Negative Fixtures

Verdict: `PASS`

| Fixture | Validation | Checklist | Output containment |
|---|---|---|---|
| Partial legacy kit plus candidate | exit 1; `INVALID`; three legacy files missing | exit 1 | `SHOULD_NOT_EXIST.json` absent |
| Complete dual kit without exact authority | exit 1; `AMBIGUOUS`; authority required | exit 1 | `SHOULD_NOT_EXIST.json` absent |

All fixture copies and outputs are confined to the verifier workspace.
